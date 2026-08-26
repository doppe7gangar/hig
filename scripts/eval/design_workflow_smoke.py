#!/usr/bin/env python3
"""Smoke-test the deterministic parts of the apple-design workflow.

This is deliberately cheaper than projtest.py: no model call. It proves that
reference selection, each emitted scaffold model, the mechanical checker, and
(optionally) the rendered-review setup still execute together.

    python3 scripts/eval/design_workflow_smoke.py
    python3 scripts/eval/design_workflow_smoke.py --browser
"""

import argparse
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DESIGN = os.path.join(ROOT, ".claude", "skills", "apple-design")
SELECT = os.path.join(DESIGN, "select_references.py")
SCAFFOLD = os.path.join(DESIGN, "new_project.py")
CHECK = os.path.join(DESIGN, "check_design.py")
RENDER = os.path.join(DESIGN, "render_review.py")


def run(args, cwd=None, expect=0):
    p = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    if p.returncode != expect:
        cmd = " ".join(args)
        raise RuntimeError(
            f"command returned {p.returncode}, expected {expect}: {cmd}\n"
            f"stdout:\n{p.stdout}\nstderr:\n{p.stderr}"
        )
    return p


def exists(path):
    if not os.path.exists(path):
        raise RuntimeError(f"missing expected path: {path}")


def test_reference_selector(tmp):
    out = os.path.join(tmp, "REFERENCES.md")
    run([sys.executable, SELECT,
         "--query", "analytics dashboard filters search status settings",
         "--model", "dashboard", "--limit", "5", "-o", out])
    exists(out)
    text = open(out, encoding="utf-8").read()
    if "## Selected references" not in text or "## Synthesis before composition" not in text:
        raise RuntimeError("reference selector did not emit the expected review structure")
    if "apple-hig/references/pages/" not in text:
        raise RuntimeError("reference selector emitted no HIG provenance")
    if "apple-hig/assets/ui-kit/" not in text:
        raise RuntimeError("reference selector emitted no visual references")
    print("ok reference selector")


def scaffold(tmp, kind, model, name):
    out = os.path.join(tmp, name)
    args = [sys.executable, SCAFFOLD,
            "--name", name,
            "--brand", "#4C7DFF",
            "--kind", kind,
            "--screens", "Home,Browse,Settings",
            "--thing", "items",
            "-o", out]
    if model:
        args[args.index("--screens"):args.index("--screens")] = ["--model", model]
    run(args)
    for rel in ("index.html", "DESIGN.md", "README.md", "theme.css",
                os.path.join("vendor", "ios-tokens.css"),
                os.path.join("vendor", "ios-components.css")):
        exists(os.path.join(out, rel))
    run([sys.executable, CHECK, out, "--no-browser"])
    return out


def test_models(tmp):
    outputs = {}
    for model in ("workspace", "list-detail", "dashboard", "document"):
        outputs[model] = scaffold(tmp, "web", model, "web-" + model)
        print(f"ok web model {model}")
    outputs["ios-stack"] = scaffold(tmp, "ios", "stack", "ios-stack")
    print("ok ios stack")
    outputs["ios-tabs"] = scaffold(tmp, "ios", "tabs", "ios-tabs")
    print("ok ios tabs")
    outputs["marketing"] = scaffold(tmp, "marketing", None, "marketing")
    print("ok marketing editorial")
    return outputs


def test_render_review(project):
    p = subprocess.run([sys.executable, RENDER, project], capture_output=True, text=True)
    if p.returncode != 0:
        combined = (p.stdout + "\n" + p.stderr).lower()
        if "playwright" in combined or "browser" in combined or "chromium" in combined:
            print("skip rendered review (browser unavailable)")
            return
        raise RuntimeError(f"render review failed:\n{p.stdout}\n{p.stderr}")

    review = os.path.join(project, "VISUAL_REVIEW.md")
    audit = os.path.join(project, ".visual-review", "audit.json")
    exists(review)
    exists(audit)

    # A freshly generated sheet must fail completion: the pending judgments
    # are intentional. If this unexpectedly passes, the guard has stopped
    # guarding the human/model inspection step.
    run([sys.executable, RENDER, project, "--check"], expect=1)
    print("ok rendered review produces intentionally incomplete critique")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--browser", action="store_true",
                    help="also exercise Playwright screenshot rendering")
    a = ap.parse_args()

    for path in (SELECT, SCAFFOLD, CHECK, RENDER):
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