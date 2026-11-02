#!/usr/bin/env python3
"""Validate cross-screen product-coherence evidence in DESIGN.md."""

import argparse
import os
import re
import sys


def section(text, name):
    m = re.search(rf"^#+\s+{re.escape(name)}\s*$([\s\S]*?)(?=^#+\s|\Z)", text, re.I | re.M)
    return m.group(1).strip() if m else ""


def meaningful(value):
    value = re.sub(r"[`*_>#|:-]", " ", value or "")
    value = re.sub(r"\s+", " ", value).strip()
    bad = {"", "n/a", "na", "none", "tbd", "todo", "pending", "-", "—"}
    return len(value) >= 12 and value.lower() not in bad and "______" not in value


def bullets(sec):
    return [m.group(1).strip() for m in re.finditer(r"^\s*[-*]\s+(.+)$", sec, re.M)]


def table_rows(sec):
    rows = []
    for line in sec.splitlines():
        if "|" not in line:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or all(re.fullmatch(r"[-: ]+", c or "-") for c in cells):
            continue
        rows.append(cells)
    return rows


def main():
    ap = argparse.ArgumentParser(
        description="Validate cross-screen product coherence evidence.")
    ap.add_argument("directory", nargs="?", default=".")
    root = ap.parse_args().directory
    path = os.path.join(root, "DESIGN.md")
    if not os.path.exists(path):
        print("FAIL missing DESIGN.md")
        return 1
    text = open(path, encoding="utf-8").read()
    errors = []

    contract = section(text, "Product coherence contract")
    required = [
        "Typography roles", "Spacing rhythm", "Surface/material roles",
        "Action placement", "Navigation/selection semantics",
        "Terminology/icon semantics", "Shared interaction contracts",
    ]
    if not contract:
        errors.append("missing Product coherence contract")
    else:
        for label in required:
            m = re.search(rf"\*\*{re.escape(label)}:\*\*\s*(.+)", contract, re.I)
            if not m or not meaningful(m.group(1)):
                errors.append(f"coherence contract missing meaningful {label}")

    matrix = section(text, "Screen-family coherence matrix")
    rows = table_rows(matrix)
    data = [r for r in rows if r and r[0].lower() not in ("screen/family", "screen", "family")]
    if len(data) < 2:
        errors.append("screen-family coherence matrix needs at least two meaningful screen/state families")
    else:
        for i, row in enumerate(data[:8], 1):
            if len(row) < 7 or sum(1 for c in row if meaningful(c)) < 5:
                errors.append(f"screen-family row {i} is too incomplete")

    intentional = section(text, "Intentional differences")
    if not intentional or not any(meaningful(x) for x in bullets(intentional)):
        errors.append("missing product-specific intentional cross-screen difference with rationale")

    transitions = section(text, "Cross-screen transition audit")
    transition_rows = table_rows(transitions)
    tdata = [r for r in transition_rows if r and r[0].lower() not in ("transition", "from → to", "from -> to")]
    if len(tdata) < 2:
        errors.append("cross-screen transition audit needs at least two transitions")
    else:
        for i, row in enumerate(tdata[:8], 1):
            if len(row) < 5 or sum(1 for c in row if meaningful(c)) < 4:
                errors.append(f"transition row {i} is too incomplete")

    drift = section(text, "Coherence drift review")
    drift_bullets = [x for x in bullets(drift) if meaningful(x)]
    if len(drift_bullets) < 2:
        errors.append("coherence drift review needs at least two concrete findings/checks")

    if errors:
        for e in errors:
            print("FAIL " + e)
        return 1
    print("ok product coherence evidence")
    return 0


if __name__ == "__main__":
    sys.exit(main())
