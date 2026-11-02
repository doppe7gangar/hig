#!/usr/bin/env python3
"""Check that DESIGN.md records the decisions the design workflow requires."""

import argparse
import os
import re
import sys

REQUIRED = [
    "Platform constraints",
    "Information hierarchy",
    "Design invariants",
    "Candidate directions",
    "Rejected directions",
    "Chosen direction",
    "Adaptive architecture",
    "Interaction states",
    "Accessibility",
    "System component decisions",
]

PLACEHOLDERS = [
    "replace this",
    "[pending]",
    "todo",
    "tbd",
    "what the user came here",
    "supporting detail that can recede",
    "controls shown only when relevant",
]


def heading_present(text, heading):
    return bool(re.search(rf"^#+\s+{re.escape(heading)}\s*$", text,
                          flags=re.I | re.M))


def main():
    ap = argparse.ArgumentParser(description="Validate design-direction evidence.")
    ap.add_argument("directory")
    args = ap.parse_args()

    path = os.path.join(os.path.abspath(args.directory), "DESIGN.md")
    if not os.path.isfile(path):
        print("FAIL DESIGN.md is missing")
        return 1

    text = open(path, encoding="utf-8").read()
    failures = []

    for heading in REQUIRED:
        if not heading_present(text, heading):
            failures.append(f"missing section: {heading}")

    low = text.lower()
    for placeholder in PLACEHOLDERS:
        if placeholder in low:
            failures.append(f"unfinished placeholder: {placeholder}")

    invariants = re.search(
        r"^#+\s+Design invariants\s*$([\s\S]*?)(?=^#+\s|\Z)",
        text, flags=re.I | re.M)
    if invariants:
        bullets = re.findall(r"^\s*[-*]\s+\S", invariants.group(1), flags=re.M)
        if len(bullets) < 3:
            failures.append("Design invariants needs at least 3 concrete bullets")

    rejected = re.search(
        r"^#+\s+Rejected directions\s*$([\s\S]*?)(?=^#+\s|\Z)",
        text, flags=re.I | re.M)
    if rejected and not re.search(r"because|rejected|fails|would", rejected.group(1), re.I):
        failures.append("Rejected directions needs product-specific rationale")

    adaptive = re.search(
        r"^#+\s+Adaptive architecture\s*$([\s\S]*?)(?=^#+\s|\Z)",
        text, flags=re.I | re.M)
    if adaptive:
        body = adaptive.group(1).lower()
        if not any(k in body for k in ("compact", "narrow", "phone", "small", "wide")):
            failures.append("Adaptive architecture needs compact/wide transformation evidence")

    if failures:
        for f in failures:
            print("FAIL " + f)
        return 1

    print("ok DESIGN.md records platform, hierarchy, invariants, divergence, adaptivity, states, accessibility, and component decisions")
    return 0


if __name__ == "__main__":
    sys.exit(main())