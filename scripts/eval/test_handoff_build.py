#!/usr/bin/env python3
"""Given an approved design, does the model write SwiftUI that keeps it?

The design is the one in handoff/design, without the Swift beside it.
The model gets the skills and one line asking for the app, and what it
writes is graded on disk:

- a skill was consulted (apple-design or apple-hig);
- check_handoff.py finds every screen, tab, state, symbol and component
  the design decided;
- check_swiftui.py finds no HIG violations;
- it finished within the hour.

Nothing compiles the Swift; on a Mac, --save keeps it to open in Xcode.

    python3 scripts/eval/test_handoff_build.py
    python3 scripts/eval/test_handoff_build.py --save /tmp/handoff
    python3 scripts/eval/test_handoff_build.py --grade ./project   # grade a finished one
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
SKILLS = os.path.normpath(os.path.join(HERE, "..", "..", ".claude", "skills"))
DESIGN = os.path.join(HERE, "handoff", "design")
KIT = os.path.join(SKILLS, "apple-ui-kit")
MODEL, TIMEOUT = "claude-opus-5", 3600

PROMPT = ("the design in ./design is approved. write the SwiftUI app for it "
          "in ./Ledger, iOS 18 and later.")


def project():
    root = tempfile.mkdtemp(prefix="hig-handoff-")
    dst = os.path.join(root, ".claude", "skills")
    os.makedirs(dst)
    for d in sorted(os.listdir(SKILLS)):
        if d.startswith("apple-"):
            shutil.copytree(os.path.join(SKILLS, d), os.path.join(dst, d),
                            ignore=shutil.ignore_patterns("__pycache__"))
    shutil.copytree(DESIGN, os.path.join(root, "design"))
    vendor = os.path.join(root, "design", "vendor")
    os.makedirs(vendor)
    for f in ("ios-components.css", os.path.join("tokens", "ios-tokens.css")):
        shutil.copy(os.path.join(KIT, f), vendor)
    return root


def build(root):
    env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
    try:
        p = subprocess.run(
            ["claude", "-p", PROMPT, "--output-format", "stream-json",
             "--verbose", "--model", MODEL, "--permission-mode", "acceptEdits",
             "--allowedTools", "Bash,Read,Write,Edit,Glob,Grep,Skill"],
            cwd=root, env=env, capture_output=True, text=True, timeout=TIMEOUT)
        out, finished = p.stdout, True
    except subprocess.TimeoutExpired as e:
        out, finished = e.stdout or "", False
        if isinstance(out, bytes):
            out = out.decode("utf-8", "replace")
    skills = []
    for line in out.splitlines():
        try:
            m = json.loads(line).get("message")
        except Exception:
            continue
        for b in (m.get("content") or []) if isinstance(m, dict) else []:
            if isinstance(b, dict) and b.get("type") == "tool_use" and b.get("name") == "Skill":
                s = str(b.get("input", {}).get("skill", ""))
                if s and s not in skills:
                    skills.append(s)
    return skills, finished


def swift_root(root):
    """Where the Swift went: ./Ledger if it's there, else wherever it is."""
    preferred = os.path.join(root, "Ledger")
    for dirpath, dirnames, files in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in (".claude", "design")]
        if any(f.endswith(".swift") for f in files):
            return preferred if os.path.isdir(preferred) else root
    return None


def run(*args):
    p = subprocess.run([sys.executable, *args], capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def grade(root, skills=None, finished=True, minutes=None):
    checks = []
    if skills is not None:
        used = [s for s in skills if "apple-design" in s or "apple-hig" in s]
        checks.append((bool(used), "a skill was consulted",
                       ", ".join(skills) or "no skill was invoked"))
    if minutes is not None:
        checks.append((finished, "finished within the hour", f"{minutes:.0f} min"))
    swift = swift_root(root)
    checks.append((swift is not None, "SwiftUI was written", swift or "no .swift files"))
    if swift:
        code, out = run(os.path.join(SKILLS, "apple-design", "check_handoff.py"),
                        os.path.join(root, "design"), swift)
        missing = [l.strip() for l in out.splitlines() if l.startswith("  FAIL")]
        warns = [l.strip() for l in out.splitlines() if l.startswith("  warn")]
        tail = [l for l in out.splitlines() if l.startswith("handoff:")]
        checks.append((code == 0, "check_handoff: nothing the design decided is missing",
                       "; ".join(missing)[:600] or (tail[0] if tail else out[-300:])))
        for w in warns:
            print("   handoff " + w[:200])
        code, out = run(os.path.join(SKILLS, "apple-hig", "check_swiftui.py"), swift)
        summary = [l for l in out.splitlines() if "violations," in l]
        vio = [l.strip() for l in out.splitlines() if l.strip().startswith(swift)][:6]
        checks.append((code == 0, "check_swiftui: no HIG violations",
                       (summary[0] if summary else out[-300:]) + ("; " + " | ".join(vio) if code else "")))
    passed = 0
    for ok, label, detail in checks:
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {label}\n   {detail}")
    print(f"\n{passed}/{len(checks)} checks passed")
    return passed == len(checks)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--save", metavar="DIR", default=os.environ.get("EVAL_WORK"),
                    help="keep the project here (run_live.py sets this per run)")
    ap.add_argument("--grade", metavar="DIR", help="grade a finished project instead")
    a = ap.parse_args()
    if a.grade:
        return 0 if grade(os.path.abspath(a.grade)) else 1

    root = project()
    started = time.time()
    skills, finished = build(root)
    minutes = (time.time() - started) / 60
    ok = grade(root, skills, finished, minutes)
    if a.save:
        shutil.rmtree(a.save, ignore_errors=True)
        shutil.copytree(root, a.save, ignore=shutil.ignore_patterns(".claude"))
        print(f"saved to {a.save}")
    shutil.rmtree(root, ignore_errors=True)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
