#!/usr/bin/env python3
"""Validate flow-level interaction evidence in DESIGN.md."""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gate_placeholders import find as find_placeholders  # noqa: E402
import re
import sys

REQUIRED_HEADINGS = [
    "Primary interaction flow",
    "Commit model",
    "Recovery and interruption",
]

# Matched anywhere in the document: nobody writes these on purpose.
LOOSE_PLACEHOLDERS = ("[pending]",)

# Standalone only: "an inline todo list" is a filled-in design.
STRICT_PLACEHOLDERS = ("todo", "tbd", "replace this")

# Matched only as a whole unfilled table cell. These two are also the
# column headings the flow table is *required* to carry -- see
# references/design-direction-template.md -- so scanning for them as
# substrings rejected every document that followed the template this
# skill ships, including its own smoke fixture. A gate that cannot be
# passed by doing exactly what it asks is worse than no gate.
CELL_PLACEHOLDERS = ["user action", "system response", "stage",
                     "state/context preserved", "failure/recovery"]


def unfilled_cells(text):
    """Body cells left as the template's own column heading."""
    found, header = [], None
    for line in text.splitlines():
        t = line.strip()
        if not t.startswith("|"):
            header = None
            continue
        cells = [c.strip().lower() for c in t.strip("|").split("|")]
        if header is None:
            header = cells          # first row of a table is its heading
            continue
        if all(set(c) <= set("-: ") for c in cells):
            continue                # the |---| separator
        for c in cells:
            if c in CELL_PLACEHOLDERS and c not in found:
                found.append(c)
    return found


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

    for p in find_placeholders(text, loose=LOOSE_PLACEHOLDERS,
                               strict=STRICT_PLACEHOLDERS):
        failures.append(f"unfinished interaction placeholder: {p}")

    for c in unfilled_cells(text):
        failures.append(f"interaction flow row still holds the template's "
                        f"own heading in a cell: {c}")

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

        # The section's keyword checks all passed on a commit model that
        # read "changes happen somehow", because the words they look for
        # were sitting in the neighbouring bullets. The one bullet that
        # carries the actual answer -- the moment a change stops being a
        # draft -- was never inspected, so this asks it directly.
        m = re.search(r"when the change becomes real[^:]*:\s*(.+)", c)
        if not m:
            failures.append("Commit model must say when the change becomes "
                            "real")
        else:
            moment = m.group(1)
            WHEN = ("acknowledg", "server", "immediat", "optimistic", "blur",
                    "submit", "confirm", "success", "response", "save",
                    "commit", "local", "debounce", "second", "keystroke",
                    "close", "accept")
            if not any(k in moment for k in WHEN):
                failures.append(
                    "Commit model says when the change becomes real without "
                    f"naming a moment: {moment.strip()[:60]!r}. Name the "
                    "trigger -- server acknowledgement, blur, submit, "
                    "optimistically with rollback.")

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