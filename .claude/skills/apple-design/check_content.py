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

    reps = section(text, "Representation decisions")
    if reps:
        rlow = reps.lower()
        if not any(term in rlow for term in REPRESENTATION_TERMS):
            failures.append("Representation decisions names no actual representation")
        for key in ("why", "failure"):
            if key not in rlow:
                failures.append(f"Representation decisions should include {key} rationale")

        # Charts must document the analytical question and basic data context.
        if "chart" in rlow:
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