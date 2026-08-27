#!/usr/bin/env python3
"""Validate flow-level interaction evidence in DESIGN.md."""

import argparse
import os
import re
import sys

REQUIRED_HEADINGS = [
    "Primary interaction flow",
    "Commit model",
    "Recovery and interruption",
]

PLACEHOLDERS = ["[pending]", "todo", "tbd", "replace this", "user action", "system response"]


def section(text, name):
    m = re.search(rf"^#+\s+{re.escape(name)}\s*$([\s\S]*?)(?=^#+\s|\Z)",
                  text, re.I | re.M)
    return m.group(1).strip() if m else ""


def heading(text, name):
    return bool(re.search(rf"^#+\s+{re.escape(name)}\s*$", text, re.I | re.M))


def main():
    ap = argparse.ArgumentParser(description="Validate interaction architecture evidence.")
    ap.add_argument("directory")
    args = ap.parse_args()

    path = os.path.join(os.path.abspath(args.directory), "DESIGN.md")
    if not os.path.isfile(path):
        print("FAIL DESIGN.md is missing")
        return 1

    text = open(path, encoding="utf-8").read()
    low = text.lower()
    failures = []

    for h in REQUIRED_HEADINGS:
        if not heading(text, h):
            failures.append(f"missing section: {h}")

    for p in PLACEHOLDERS:
        if p in low:
            failures.append(f"unfinished interaction placeholder: {p}")

    flow = section(text, "Primary interaction flow")
    if flow:
        # Expect a Markdown table with at least four meaningful rows/stages.
        rows = [line for line in flow.splitlines()
                if line.strip().startswith("|") and "---" not in line]
        if len(rows) < 5:  # header + 4 stages
            failures.append("Primary interaction flow needs a table with at least four stages")
        required_words = ("entry", "act", "commit", "exit")
        f = flow.lower()
        missing = [w for w in required_words if w not in f]
        if missing:
            failures.append("Primary interaction flow missing stages: " + ", ".join(missing))
        for concept in ("failure", "recovery", "preserved"):
            if concept not in f:
                failures.append(f"Primary interaction flow needs {concept} evidence")

    commit = section(text, "Commit model")
    if commit:
        c = commit.lower()
        if not any(k in c for k in ("immediate", "explicit", "autosave", "continuous")):
            failures.append("Commit model must name immediate, explicit, or autosave/continuous behavior")
        if not any(k in c for k in ("undo", "cancel", "revert", "restore")):
            failures.append("Commit model must state undo/cancel/reversal policy")
        if not any(k in c for k in ("focus", "selection", "context")):
            failures.append("Commit model must state post-completion focus/selection/context")

    recovery = section(text, "Recovery and interruption")
    if recovery:
        r = recovery.lower()
        if not any(k in r for k in ("network", "offline", "failure", "error", "conflict")):
            failures.append("Recovery and interruption needs at least one failure condition")
        if not any(k in r for k in ("navigate", "dismiss", "focus", "background", "leave", "selection")):
            failures.append("Recovery and interruption needs at least one interruption/resumption case")
        if not any(k in r for k in ("preserve", "resume", "retry", "restore", "rollback", "undo")):
            failures.append("Recovery and interruption needs a concrete recovery/resumption behavior")

    stress = section(text, "Interaction stress cases")
    if not stress:
        failures.append("missing section: Interaction stress cases")
    else:
        bullets = re.findall(r"^\s*[-*]\s+\S", stress, re.M)
        if len(bullets) < 3:
            failures.append("Interaction stress cases needs at least 3 concrete cases")

    keyboard = section(text, "Keyboard and alternate input")
    if not keyboard:
        failures.append("missing section: Keyboard and alternate input")
    elif len(keyboard) < 60:
        failures.append("Keyboard and alternate input evidence is too thin")

    if failures:
        for f in failures:
            print("FAIL " + f)
        return 1

    print("ok DESIGN.md records flow, commit semantics, recovery, stress cases, and alternate input")
    return 0


if __name__ == "__main__":
    sys.exit(main())