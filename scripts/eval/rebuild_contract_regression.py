#!/usr/bin/env python3
"""Regression checks for failures that made the rebuilt workflow unusable.

Covers:
1. new_project.py must compile on Python 3.11+ and scaffold all model families.
2. Evidence gates must accept their own mandated template vocabulary.
3. Browser contrast must sweep populated/loading/empty/error rather than visible state only.
4. Shared button contrast rules must live in common CSS so every spatial model inherits them.
"""

import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DESIGN = os.path.join(ROOT, ".claude", "skills", "apple-design")
NEW = os.path.join(DESIGN, "new_project.py")
DIV = os.path.join(DESIGN, "check_divergence.py")
INT = os.path.join(DESIGN, "check_interaction.py")
CHECK = os.path.join(DESIGN, "check_design.py")


def run(args, expect=0):
    p = subprocess.run(args, capture_output=True, text=True)
    if p.returncode != expect:
        raise RuntimeError(
            f"expected {expect}, got {p.returncode}: {' '.join(args)}\n"
            f"stdout:\n{p.stdout}\nstderr:\n{p.stderr}")
    return p


def test_compile_and_scaffold(tmp):
    run([sys.executable, "-m", "py_compile", NEW, DIV, INT, CHECK])
    cases = [
        ("web", "workspace"), ("web", "list-detail"),
        ("web", "dashboard"), ("web", "document"),
        ("ios", "stack"), ("ios", "tabs"), ("marketing", None),
    ]
    for kind, model in cases:
        out = os.path.join(tmp, kind + "-" + (model or "editorial"))
        args = [sys.executable, NEW, "--name", "Regression", "--brand", "#F2C94C",
                "--kind", kind, "--screens", "Home,Detail,Settings", "--thing", "items", "-o", out]
        if model:
            args[args.index("--screens"):args.index("--screens")] = ["--model", model]
        run(args)
        if not os.path.exists(os.path.join(out, "index.html")):
            raise RuntimeError(f"scaffolder emitted no index.html for {kind}/{model}")
    print("ok scaffolder compiles and all model families execute")


def test_gate_vocabulary(tmp):
    root = os.path.join(tmp, "gate-vocabulary")
    os.makedirs(root)
    design = r'''# Design direction

## Candidate directions
### Direction A
- **Frame:** standalone app
- **Model:** dashboard
- **Design idea:** Current health owns the first read.
- **Primary region:** service health and change
- **Secondary/contextual regions:** evidence below the answer
- **Persistent chrome:** global navigation and range control
- **Compact transformation:** evidence becomes sequential
- **Strength:** fast monitoring comprehension
- **Risk:** deeper triage is one step away
- **Structural differences:** answer before records; contextual evidence instead of persistent queue

### Direction B
- **Frame:** the conversation — it lives in the thread
- **Model:** workspace
- **Design idea:** Active queue owns the work surface.
- **Primary region:** queue and active selection
- **Secondary/contextual regions:** service health in contextual summary
- **Persistent chrome:** sidebar and queue controls
- **Compact transformation:** selection becomes sequential detail
- **Strength:** efficient prolonged triage
- **Risk:** overall status scans more slowly
- **Structural differences:** persistent queue instead of summary; simultaneous detail instead of evidence sequence

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

**Trade-off interpretation:** Direction A better matches the recurring monitoring task; Direction B better serves long triage sessions. The monitoring consequence matters more here, so the decision is not a numeric total.

## Rejected directions
- Rejected Direction B because persistent queue chrome weakens first-read service health.

## Chosen direction
We chose Direction A because current health is the primary recurring task; evidence stays available without competing, and the layout transforms to sequential evidence on compact widths.

## Primary interaction flow
| Stage | User action | System response | State/context preserved | Failure/recovery |
|---|---|---|---|---|
| Entry | Open current incident | Detail opens | queue selection and filters preserved | missing incident returns to queue with explanation |
| Act | Change assignee | Control updates | incident selection preserved | validation remains inline |
| Commit | Submit change | Server acknowledges | focus stays in detail | failure restores previous assignee and retry |
| Exit/continue | Select next incident | Next detail opens | queue scroll preserved | pending operation stays attached to original incident |

## Commit model
- **Frame:** a glanceable surface — a widget on the Home Screen
- **Model:** explicit for note submission and immediate for assignee selection.
- **When the change becomes real:** after server acknowledgement; assignee may update optimistically with rollback.
- **Undo/cancel/reversal policy:** cancel before submit and undo a completed reassignment.
- **Post-completion focus/selection/context:** focus and selection remain on the current incident.

## Recovery and interruption
- **Failure condition:** network error rolls back optimistic changes and exposes retry.
- **Interruption/resumption case:** selection may change while a request is pending without mutating the new selection.
- **What is preserved:** filters, scroll position, selection, and draft content.
- **Retry/rollback/restore behavior:** retry in place and restore the previous value on failure.

## Interaction stress cases
- Double-submit only creates one mutation.
- Change selection while request is pending; response applies to original object.
- Go offline mid-edit; draft survives reconnect.

## Keyboard and alternate input
- **Keyboard/command path where expected:** arrows change selection and Command-Return submits.
- **Escape/cancel and Return/commit semantics:** Escape cancels transient editing; Command-Return commits.
- **Focus restoration:** dismissal returns focus to its trigger.
- **Touch/pointer alternative:** visible controls exist for all keyboard commands.
'''
    open(os.path.join(root, "DESIGN.md"), "w", encoding="utf-8").write(design)
    run([sys.executable, DIV, root])
    run([sys.executable, INT, root])
    print("ok gates accept the exact vocabulary required by their templates")


def test_shared_css_and_state_sweep():
    new = open(NEW, encoding="utf-8").read()
    check = open(CHECK, encoding="utf-8").read()
    shared_rule = ".ios-btn:not(.ios-btn--filled):not(.ios-btn--destructive)"
    if shared_rule not in new:
        raise RuntimeError("shared non-filled accent-text rule missing from new_project.py")
    state_pos = new.find("STATE_CSS =")
    ios_pos = new.find("IOS_CSS =")
    rule_pos = new.find(shared_rule)
    if not (state_pos < rule_pos < ios_pos):
        raise RuntimeError("accent-text rule is not in shared STATE_CSS")
    # Structural rather than literal. Matching the loop as an exact
    # string went wrong in both directions: swapping single quotes for
    # double failed the guard while the behaviour was untouched, and
    # keeping the line but moving sweep() outside the braces passed it
    # while the checker went back to measuring one state. So: find the
    # loop that names all four states, and require it to sweep inside.
    sweep = None
    for m in re.finditer(r"for\s*\(\s*const\s+\w+\s+of\s*\[([^\]]*)\]\s*\)\s*\{(.*?)\n  \}",
                         check, re.S):
        listed = {t.strip().strip("'\"") for t in m.group(1).split(",")}
        if {"populated", "loading", "empty", "error"} <= listed:
            sweep = m
            break
    if sweep is None:
        raise RuntimeError(
            "browser checker has no loop naming all four states")
    if "sweep()" not in sweep.group(2):
        raise RuntimeError(
            "the four-state loop does not sweep inside its body, so only "
            "the state it leaves behind gets measured")
    print("ok shared contrast CSS and four-state browser sweep are guarded")


def test_hidden_state_contrast_is_caught(tmp):
    """The sweep has to work, not merely be present in the source.

    Guarding it by grepping the source proved to be a check on
    formatting: the loop could stay exactly as written with sweep()
    moved outside the braces, and check_design.py then called a page
    ready that had white-on-yellow at 1.23:1 in its empty panel. This
    builds that page and insists the checker rejects it.
    """
    out = os.path.join(tmp, "hidden-state")
    run([sys.executable, NEW, "--name", "Sun", "--brand", "#FFE81A",
         "--kind", "ios", "--screens", "Home,Browse", "--thing", "items",
         "-o", out])
    page = os.path.join(out, "index.html")
    html = open(page, encoding="utf-8").read()
    # White on a light brand fails; break only the hidden empty panel, so
    # a checker that measures just the visible state cannot notice.
    i, j = html.index('class="state state--empty"'), html.index('class="state state--error"')
    seg = html[i:j].replace('class="ios-btn ios-btn--filled"',
                            'class="ios-btn ios-btn--filled" style="color:#FFFFFF"')
    open(page, "w", encoding="utf-8").write(html[:i] + seg + html[j:])

    p = subprocess.run([sys.executable, CHECK, out], capture_output=True, text=True)
    if "playwright" in p.stdout.lower() and "skipped" in p.stdout.lower():
        print("-- browser unavailable; hidden-state contrast not exercised")
        return
    if p.returncode == 0:
        raise RuntimeError(
            "check_design.py passed a page whose hidden empty state has "
            "white on a light brand at about 1.2:1 -- the state sweep is "
            "not actually running")
    print("ok a contrast failure in a hidden state is still caught")


def main():
    for p in (NEW, DIV, INT, CHECK):
        if not os.path.exists(p):
            raise RuntimeError("missing required file: " + p)
    with tempfile.TemporaryDirectory(prefix="rebuild-contract-") as tmp:
        test_compile_and_scaffold(tmp)
        test_gate_vocabulary(tmp)
        test_shared_css_and_state_sweep()
        test_hidden_state_contrast_is_caught(tmp)
    print("rebuild contract regression passed")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print("FAIL " + str(exc), file=sys.stderr)
        sys.exit(1)
