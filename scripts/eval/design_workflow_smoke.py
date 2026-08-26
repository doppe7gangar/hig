#!/usr/bin/env python3
"""Smoke-test deterministic parts of the apple-design workflow.

No model call. It verifies platform-aware reference routing, scaffold models,
mechanical checks, the direction-evidence guard, and optionally screenshot
review setup.
"""

import argparse
import os
import subprocess
import sys
import tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DESIGN = os.path.join(ROOT, ".claude", "skills", "apple-design")
SELECT = os.path.join(DESIGN, "select_references.py")
SCAFFOLD = os.path.join(DESIGN, "new_project.py")
CHECK = os.path.join(DESIGN, "check_design.py")
DIRECTION = os.path.join(DESIGN, "check_direction.py")
RENDER = os.path.join(DESIGN, "render_review.py")


def run(args, cwd=None, expect=0):
    p = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    if p.returncode != expect:
        raise RuntimeError(
            f"command returned {p.returncode}, expected {expect}: {' '.join(args)}\n"
            f"stdout:\n{p.stdout}\nstderr:\n{p.stderr}")
    return p


def exists(path):
    if not os.path.exists(path):
        raise RuntimeError(f"missing expected path: {path}")


def test_reference_selector(tmp):
    ios = os.path.join(tmp, "REFERENCES-ios.md")
    run([sys.executable, SELECT, "--query",
         "analytics dashboard filters search status settings",
         "--model", "dashboard", "--platform", "ios", "--limit", "5", "-o", ios])
    text = open(ios, encoding="utf-8").read()
    if "apple-hig/references/pages/" not in text or "apple-hig/assets/ui-kit/" not in text:
        raise RuntimeError("iOS selector lost HIG or measured visual provenance")

    mac = os.path.join(tmp, "REFERENCES-macos.md")
    run([sys.executable, SELECT, "--query",
         "mail sidebar toolbar search list detail menus",
         "--model", "list-detail", "--platform", "macos", "--limit", "5", "-o", mac])
    text = open(mac, encoding="utf-8").read().lower()
    if "no measured macos visual corpus" not in text:
        raise RuntimeError("macOS selector failed to state the measured-corpus boundary")
    if "inspect these visual states" in text or "**visual folder:**" in text:
        raise RuntimeError("macOS selector incorrectly exposed iOS visuals as platform evidence")
    print("ok platform-aware reference selector")


def scaffold(tmp, kind, model, name):
    out = os.path.join(tmp, name)
    args = [sys.executable, SCAFFOLD, "--name", name, "--brand", "#4C7DFF",
            "--kind", kind, "--screens", "Home,Browse,Settings",
            "--thing", "items", "-o", out]
    if model:
        args[args.index("--screens"):args.index("--screens")] = ["--model", model]
    run(args)
    for rel in ("index.html", "DESIGN.md", "README.md", "theme.css",
                os.path.join("vendor", "ios-tokens.css"),
                os.path.join("vendor", "ios-components.css")):
        exists(os.path.join(out, rel))
    run([sys.executable, CHECK, out, "--no-browser"])
    # The scaffold deliberately contains an incomplete design direction. The
    # direction gate must reject it until the designer records real evidence.
    run([sys.executable, DIRECTION, out], expect=1)
    return out


def test_models(tmp):
    outputs = {}
    for model in ("workspace", "list-detail", "dashboard", "document"):
        outputs[model] = scaffold(tmp, "web", model, "web-" + model)
        print(f"ok web model {model}")
    outputs["ios-stack"] = scaffold(tmp, "ios", "stack", "ios-stack")
    outputs["ios-tabs"] = scaffold(tmp, "ios", "tabs", "ios-tabs")
    outputs["marketing"] = scaffold(tmp, "marketing", None, "marketing")
    print("ok iOS and marketing models; incomplete direction correctly rejected")
    return outputs


def test_render_review(project):
    p = subprocess.run([sys.executable, RENDER, project], capture_output=True, text=True)
    if p.returncode != 0:
        combined = (p.stdout + "\n" + p.stderr).lower()
        if "playwright" in combined or "browser" in combined or "chromium" in combined:
            print("skip rendered review (browser unavailable)")
            return
        raise RuntimeError(f"render review failed:\n{p.stdout}\n{p.stderr}")
    exists(os.path.join(project, "VISUAL_REVIEW.md"))
    exists(os.path.join(project, ".visual-review", "audit.json"))
    run([sys.executable, RENDER, project, "--check"], expect=1)
    print("ok rendered review requires completed critique")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--browser", action="store_true")
    a = ap.parse_args()
    for path in (SELECT, SCAFFOLD, CHECK, DIRECTION, RENDER):
        exists(path)
    with tempfile.TemporaryDirectory(prefix="apple-design-smoke-") as tmp:
        test_reference_selector(tmp)
        outputs = test_models(tmp)
        if a.browser:
            test_render_review(outputs["dashboard"])
    print("design workflow smoke test passed")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print("FAIL " + str(exc), file=sys.stderr)
        sys.exit(1)