#!/usr/bin/env python3
"""Smoke-test deterministic parts of the apple-design workflow.

No model call. It verifies platform-aware reference routing, structural
divergence evidence, scaffold models, mechanical checks, direction evidence,
and optionally screenshot review setup.
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
DIVERGENCE = os.path.join(DESIGN, "check_divergence.py")
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


def test_divergence_gate(tmp):
    root = os.path.join(tmp, "divergence-fixture")
    os.makedirs(root)
    valid = r'''# Design direction

## Candidate directions

### Direction: A — Answer first
- **Model:** dashboard
- **Design idea:** Today's support health owns the screen while evidence explains it.
- **Primary region:** one service-health answer and current change
- **Secondary/contextual regions:** trend and queue evidence below the answer
- **Persistent chrome:** compact global navigation and time-range control
- **Compact transformation:** evidence becomes sequential below the primary answer
- **Strength:** fastest status comprehension during repeated monitoring
- **Risk:** can under-serve users who spend long sessions inside one ticket
- **Structural differences:** summary before records; contextual evidence instead of persistent list

### Direction: B — Queue workspace
- **Model:** workspace
- **Design idea:** The active queue owns the work surface while status remains contextual.
- **Primary region:** dense ticket queue and active selection
- **Secondary/contextual regions:** service health in a quiet summary strip and inspector
- **Persistent chrome:** destination sidebar and queue controls
- **Compact transformation:** sidebar collapses and selected ticket becomes sequential detail
- **Strength:** supports triage sessions where operators act more than monitor
- **Risk:** overall service health becomes slower to scan at a glance
- **Structural differences:** persistent queue instead of summary; simultaneous work region instead of evidence sequence

## Direction comparison

| Criterion | Direction A | Direction B |
|---|---:|---:|
| Primary-task fit | 5 | 4 |
| Hierarchy clarity | 5 | 4 |
| Information relationship | 4 | 5 |
| Platform fit | 5 | 5 |
| Adaptivity | 5 | 4 |
| Restraint | 5 | 3 |
| Distinctiveness through product logic | 4 | 5 |

**Trade-off interpretation:** Direction B is stronger for prolonged triage, but this product's most frequent opening task is checking current health before deciding whether action is needed. The extra persistent queue chrome therefore costs more than its stronger record relationship helps. Direction A does not win merely by total; its monitoring-first weakness is acceptable because deeper ticket work remains one step away.

## Rejected directions

- Rejected Queue workspace because monitoring is the dominant opening task; making the queue persistent would weaken first-read status clarity.

## Chosen direction

We chose Answer first because the user's recurring task is checking service health. It keeps current status primary, makes queue evidence available without competing for attention, and transforms to a sequential evidence flow on narrow screens.
'''
    path = os.path.join(root, "DESIGN.md")
    open(path, "w", encoding="utf-8").write(valid)
    run([sys.executable, DIVERGENCE, root])

    broken = valid.replace(
        "summary before records; contextual evidence instead of persistent list",
        "different layout")
    open(path, "w", encoding="utf-8").write(broken)
    run([sys.executable, DIVERGENCE, root], expect=1)
    print("ok divergence gate accepts structural comparison and rejects cosmetic/thin evidence")


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
    run([sys.executable, DIRECTION, out], expect=1)
    run([sys.executable, DIVERGENCE, out], expect=1)
    return out


def test_models(tmp):
    outputs = {}
    for model in ("workspace", "list-detail", "dashboard", "document"):
        outputs[model] = scaffold(tmp, "web", model, "web-" + model)
        print(f"ok web model {model}")
    outputs["ios-stack"] = scaffold(tmp, "ios", "stack", "ios-stack")
    outputs["ios-tabs"] = scaffold(tmp, "ios", "tabs", "ios-tabs")
    outputs["marketing"] = scaffold(tmp, "marketing", None, "marketing")
    print("ok iOS and marketing models; incomplete direction/divergence correctly rejected")
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
    for path in (SELECT, SCAFFOLD, CHECK, DIRECTION, DIVERGENCE, RENDER):
        exists(path)
    with tempfile.TemporaryDirectory(prefix="apple-design-smoke-") as tmp:
        test_reference_selector(tmp)
        test_divergence_gate(tmp)
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