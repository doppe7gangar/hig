#!/usr/bin/env python3
"""What the onplatform GitHub Action runs, in your repository's CI.

Checks SwiftUI against the HIG (hig-guide's check_swiftui.py) and design
folders for anything they mustn't publish (design-workflow's
check_distribution.py). Each finding becomes a GitHub annotation, so it
shows on the pull request's diff at its line, and a summary goes to the
run's page. action.yml passes the inputs as environment variables:

    ONPLATFORM_SWIFTUI   Swift files or folders, one per line or separated by spaces
    ONPLATFORM_DESIGNS   design folders, the same way
    ONPLATFORM_PURPOSE   publish (default) or mockup
    ONPLATFORM_FAIL_ON   violation (default), guidance, or none
    ONPLATFORM_IOS       deployment target for SF Symbol availability, e.g. 17

Run it locally the same way: ONPLATFORM_SWIFTUI=MyApp python3 scripts/action_checks.py
"""

import json
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SWIFTUI = os.path.join(ROOT, ".claude", "skills", "hig-guide", "check_swiftui.py")
DISTRIBUTION = os.path.join(ROOT, ".claude", "skills", "design-workflow", "check_distribution.py")


def paths(name):
    raw = os.environ.get(name, "").strip()
    return [p for p in (raw.splitlines() if "\n" in raw else raw.split()) if p.strip()]


def escape(text, prop=False):
    text = str(text).replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
    return text.replace(":", "%3A").replace(",", "%2C") if prop else text


def annotate(level, message, file=None, line=None, title=None):
    props = ",".join(f"{k}={escape(v, True)}" for k, v in
                     (("file", file), ("line", line), ("title", title)) if v)
    print(f"::{level} {props}::{escape(message)}" if props else f"::{level}::{escape(message)}")


def check_swiftui(targets, ios):
    cmd = [sys.executable, SWIFTUI, "--json", *targets] + (["--ios", ios] if ios else [])
    run = subprocess.run(cmd, capture_output=True, text=True)
    try:
        findings = json.loads(run.stdout or "[]")
    except ValueError:
        annotate("error", f"check_swiftui.py didn't run: {(run.stderr or run.stdout)[-500:]}")
        return None
    for f in findings:
        level = "error" if f["kind"] == "violation" else "warning"
        link = f" {f['page']}" if f.get("page") else ""
        title = f"HIG {f['kind']}" + (f": {f['rule']}" if f.get("rule") and f["rule"] != f["kind"] else "")
        annotate(level, f"{f['message']}{link}", f["path"], f.get("line"), title)
    return findings


def check_designs(designs, purpose):
    results = {}
    for design in designs:
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "files.json")
            run = subprocess.run([sys.executable, DISTRIBUTION, design, "--purpose", purpose,
                                  "--manifest", out, "-q"], capture_output=True, text=True)
            print(run.stdout.rstrip())
            try:
                report = json.load(open(out, encoding="utf-8"))
            except (OSError, ValueError):
                annotate("error", f"check_distribution.py didn't run on {design}: {run.stderr[-500:]}")
                results[design] = None
                continue
        for message in report["problems"]:
            rel, _, text = message.partition(": ")
            target = os.path.join(design, rel) if text and os.path.exists(os.path.join(design, rel)) else design
            annotate("error", text or message, target, title="What this design mustn't publish")
        for message in report["warnings"]:
            rel, _, text = message.partition(": ")
            target = os.path.join(design, rel) if text and os.path.exists(os.path.join(design, rel)) else design
            annotate("warning", text or message, target, title="Before this design is published")
        results[design] = report
    return results


def main():
    swift, designs = paths("ONPLATFORM_SWIFTUI"), paths("ONPLATFORM_DESIGNS")
    purpose = os.environ.get("ONPLATFORM_PURPOSE", "publish").strip() or "publish"
    fail_on = os.environ.get("ONPLATFORM_FAIL_ON", "violation").strip() or "violation"
    if purpose not in ("publish", "mockup") or fail_on not in ("violation", "guidance", "none"):
        annotate("error", f"purpose must be publish or mockup, fail-on violation, guidance or none; "
                          f"got {purpose!r} and {fail_on!r}")
        return 2
    if not swift and not designs:
        annotate("warning", "Nothing to check: set swiftui, designs, or both.")
        return 0

    summary, failed = ["## onplatform checks", ""], False
    if swift:
        findings = check_swiftui(swift, os.environ.get("ONPLATFORM_IOS", "").strip())
        if findings is None:
            failed = True
        else:
            count = {k: sum(f["kind"] == k for f in findings) for k in ("violation", "guidance", "api")}
            summary += [f"**SwiftUI** ({', '.join(swift)}): {count['violation']} violations, "
                        f"{count['guidance']} guidance, {count['api']} API notes.", ""]
            failed |= fail_on != "none" and (count["violation"] > 0 or
                                             (fail_on == "guidance" and count["guidance"] > 0))
    if designs:
        for design, report in check_designs(designs, purpose).items():
            if report is None:
                failed = True
                continue
            n = len(report["problems"])
            summary.append(f"**{design}** ({purpose}): {len(report['files'])} files, "
                           f"{n} problem(s), {len(report['warnings'])} warning(s).")
            failed |= fail_on != "none" and n > 0
        summary.append("")
    summary.append("Each finding links Apple's page; a clean design check means nothing it knows to "
                   "look for was found, not that every use is licensed.")
    target = os.environ.get("GITHUB_STEP_SUMMARY")
    if target:
        with open(target, "a", encoding="utf-8") as fh:
            fh.write("\n".join(summary) + "\n")
    print("\n".join(summary))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
