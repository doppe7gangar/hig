#!/usr/bin/env python3
"""Validate that DESIGN.md records content-design and representation evidence."""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gate_placeholders import find as find_placeholders  # noqa: E402
import re
import sys

REQUIRED_HEADINGS = [
    "What the product knows",
    "Content model",
    "Representation decisions",
    "Content stress cases",
    "State continuity",
]

# Never legitimate anywhere in a design document.
LOOSE_PLACEHOLDERS = ("[pending]", "lorem ipsum")

# Placeholders only when they stand alone -- a whole cell, bullet, line,
# or a marked [todo]. This gate demands realistic content, and realistic
# content for a notes or commerce product says "todo" and "item 1" in
# passing; banning the substring made the two rules fight each other.
STRICT_PLACEHOLDERS = ("todo", "tbd", "replace this", "item 1")

REPRESENTATION_TERMS = {
    "number", "metric", "list", "table", "chart", "timeline", "prose",
    "image", "media", "form", "control", "canvas", "map", "custom"
}


def _chose(section_text, kind):
    """True when `kind` is named in a row's Representation column.

    Falls back to a whole-section scan where there is no table, so a
    design written as prose is still held to the same requirement.
    """
    rows, header = [], None
    for line in section_text.splitlines():
        t = line.strip()
        if not t.startswith("|"):
            continue
        cells = [c.strip().lower() for c in t.strip("|").split("|")]
        if all(set(c) <= set("-: ") for c in cells):
            continue
        if header is None:
            header = cells
            continue
        rows.append(cells)
    if not rows:
        return kind in section_text.lower()
    col = 1
    if header and "representation" in header:
        col = header.index("representation")
    return any(kind in (r[col] if col < len(r) else "") for r in rows)


# Places a product can get an answer from instead of asking for it. The
# distinctly Apple move on this axis is subtraction of input: a split
# bill at a restaurant already knows where you are, what time it is, who
# you are with and what you last did -- and every one of those it infers
# is a field somebody does not fill in. Substrings, never length-tested.
INFERENCE_SOURCES = (
    "location", "place", "nearby", "time", "date", "calendar", "contacts",
    "recent", "history", "last time", "previously", "already", "photo",
    "receipt", "scan", "camera", "default", "pattern", "habit", "usual",
    "device", "account", "sign-in", "signed in", "clipboard", "share sheet",
    "current", "context", "in the thread", "conversation",
)


def section(text, heading):
    m = re.search(rf"^#+\s+{re.escape(heading)}\s*$([\s\S]*?)(?=^#+\s|\Z)",
                  text, flags=re.I | re.M)
    return m.group(1).strip() if m else ""


def main():
    ap = argparse.ArgumentParser(description="Validate content-design evidence.")
    ap.add_argument("directory")
    args = ap.parse_args()

    path = os.path.join(os.path.abspath(args.directory), "DESIGN.md")
    if not os.path.isfile(path):
        print("FAIL DESIGN.md is missing")
        return 1

    text = open(path, encoding="utf-8").read()
    failures = []

    for heading in REQUIRED_HEADINGS:
        if not section(text, heading):
            failures.append(f"missing or empty section: {heading}")

    low = text.lower()
    for p in find_placeholders(text, loose=LOOSE_PLACEHOLDERS,
                               strict=STRICT_PLACEHOLDERS):
        failures.append(f"unfinished/generic content marker: {p}")

    content = section(text, "Content model")
    if content:
        needed = ("question", "decision", "content shape", "required context")
        for key in needed:
            if key not in content.lower():
                failures.append(f"Content model should record {key}")

    # Every question the interface asks is one the product declined to
    # answer for itself. Requiring this named, with where the answer
    # comes from, makes input economy a design decision rather than an
    # afterthought -- and it is where Apple's difference usually shows
    # before any pixel does.
    knows = section(text, "What the product knows")
    if knows:
        low = knows.lower()
        inferred = [b for b in re.findall(r"^\s*[-*]\s+(.+)$", knows, re.M)
                    if any(src in b.lower() for src in INFERENCE_SOURCES)]
        if len(inferred) < 2:
            failures.append(
                "What the product knows needs at least two things it infers "
                "rather than asks, each naming where the answer comes from "
                "(location, time, contacts, a receipt, what happened last "
                "time). Every question the interface asks is one the product "
                "declined to answer for itself.")
        if not re.search(r"\bask|\bprompt|\brequest|\benter\b|\btype\b", low):
            failures.append(
                "What the product knows must also say what it deliberately "
                "asks for, and why that one is worth a question.")

    reps = section(text, "Representation decisions")
    if reps:
        rlow = reps.lower()
        if not any(term in rlow for term in REPRESENTATION_TERMS):
            failures.append("Representation decisions names no actual representation")
        for key in ("why", "failure"):
            if key not in rlow:
                failures.append(f"Representation decisions should include {key} rationale")

        # Charts must document the analytical question and basic data
        # context -- but only where a chart is actually chosen. Testing
        # the whole section for the word meant "a table, not a chart"
        # demanded the question, unit and comparison of the chart it had
        # just ruled out. Declining a chart is the reduction this skill's
        # own critique asks for; a gate should not fine you for saying so.
        chose_chart = _chose(reps, "chart")
        if chose_chart:
            for key in ("question", "unit", "comparison"):
                if key not in rlow:
                    failures.append(f"chart representation should record {key}")

    stress = section(text, "Content stress cases")
    if stress:
        bullets = re.findall(r"^\s*[-*]\s+\S", stress, flags=re.M)
        if len(bullets) < 3:
            failures.append("Content stress cases needs at least 3 concrete cases")

    states = section(text, "State continuity")
    if states:
        slow = states.lower()
        for key in ("invariant", "loading", "empty", "error"):
            if key not in slow:
                failures.append(f"State continuity should address {key}")

    if failures:
        for f in failures:
            print("FAIL " + f)
        return 1

    print("ok DESIGN.md records content model, representation rationale, stress cases, and state continuity")
    return 0


if __name__ == "__main__":
    sys.exit(main())