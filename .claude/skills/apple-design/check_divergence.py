#!/usr/bin/env python3
"""Validate that DESIGN.md contains real structural divergence before commitment.

This checker does not decide which direction is best. It verifies evidence that
multiple credible structural directions were actually compared rather than
retroactively naming cosmetic variants after one layout had already won.
"""

import argparse
import os
import re
import sys

FIELDS = [
    "Model",
    "Design idea",
    "Primary region",
    "Secondary/contextual regions",
    "Persistent chrome",
    "Compact transformation",
    "Strength",
    "Risk",
    "Structural differences",
]

CRITERIA = [
    "Primary-task fit",
    "Hierarchy clarity",
    "Information relationship",
    "Platform fit",
    "Adaptivity",
    "Restraint",
    "Distinctiveness through product logic",
]

# Aesthetic labels the divergence protocol rejects as reasons, plus the
# usual unfilled-template markers.
#
# "direction a" and "direction b" used to be here and could not be: the
# comparison table this gate requires is headed
# `| Criterion | Direction A | Direction B |` in
# references/design-direction-template.md, candidate_blocks below
# explicitly accepts "### Direction A" as a heading, and any honest
# trade-off paragraph names the directions it is weighing. The gate
# banned the vocabulary its own template mandates, so no document that
# followed the instructions could pass. Thin or cosmetic divergence is
# caught by the structural-difference checks further down, which is
# where it belongs.
PLACEHOLDERS = (
    "[pending]", "todo", "tbd", "replace this",
    "clean and modern", "more apple-like", "less apple-like",
)


def section(text, heading):
    m = re.search(
        rf"^##\s+{re.escape(heading)}\s*$([\s\S]*?)(?=^##\s|\Z)",
        text, flags=re.I | re.M)
    return m.group(1) if m else None


def candidate_blocks(body):
    # Candidate headings may be "### Direction A" or named directions such as
    # "### Direction: Focused detail". Stop at the next level-3 heading.
    matches = list(re.finditer(r"^###\s+(.+?)\s*$", body, flags=re.M))
    out = []
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        title = m.group(1).strip()
        block = body[start:end]
        if title.lower().startswith("direction"):
            out.append((title, block))
    return out


def field_value(block, name):
    # Supports "- **Model:** value" and "- Model: value".
    m = re.search(
        rf"^\s*[-*]\s+(?:\*\*)?{re.escape(name)}(?:\*\*)?\s*:\s*(.+?)\s*$",
        block, flags=re.I | re.M)
    return m.group(1).strip() if m else None


def parse_score_table(body):
    lines = [ln.strip() for ln in body.splitlines() if ln.strip().startswith("|")]
    if len(lines) < 3:
        return None, []
    rows = []
    for ln in lines:
        cells = [c.strip() for c in ln.strip("|").split("|")]
        if cells and not all(set(c) <= set("-: ") for c in cells):
            rows.append(cells)
    if len(rows) < 2:
        return None, []
    return rows[0], rows[1:]


def main():
    ap = argparse.ArgumentParser(description="Validate structural design divergence evidence.")
    ap.add_argument("directory")
    args = ap.parse_args()

    path = os.path.join(os.path.abspath(args.directory), "DESIGN.md")
    if not os.path.isfile(path):
        print("FAIL DESIGN.md is missing")
        return 1
    text = open(path, encoding="utf-8").read()
    failures = []

    low = text.lower()
    for p in PLACEHOLDERS:
        if p in low:
            failures.append(f"unfinished/cosmetic divergence language: {p}")

    candidates_body = section(text, "Candidate directions")
    if candidates_body is None:
        failures.append("missing section: Candidate directions")
        candidates = []
    else:
        candidates = candidate_blocks(candidates_body)
        if len(candidates) < 2:
            failures.append("need at least 2 credible candidate directions")
        if len(candidates) > 3:
            failures.append("use at most 3 candidate directions; divergence should stay selective")

    models = []
    for title, block in candidates:
        for field in FIELDS:
            value = field_value(block, field)
            if not value:
                failures.append(f"{title}: missing field {field}")
            elif len(value.split()) < 2 and field not in ("Model",):
                failures.append(f"{title}: {field} is too thin to be evidence")
        model = field_value(block, "Model")
        if model:
            models.append(model.lower())
        differences = field_value(block, "Structural differences") or ""
        # Require at least two declared differences, using semicolon/comma/and
        # as a lightweight auditable signal. The prose still carries judgment.
        pieces = [p.strip() for p in re.split(r";|,|\band\b", differences, flags=re.I) if p.strip()]
        if differences and len(pieces) < 2:
            failures.append(f"{title}: declare at least 2 structural differences")

    if len(candidates) >= 2 and len(set(models)) == 1:
        failures.append("all candidate directions use the same model; explain real structural divergence or choose different models")

    scoring_body = section(text, "Direction comparison")
    if scoring_body is None:
        failures.append("missing section: Direction comparison")
    else:
        header, rows = parse_score_table(scoring_body)
        if not header:
            failures.append("Direction comparison needs a markdown score table")
        else:
            if len(header) < 3:
                failures.append("Direction comparison needs criterion plus at least 2 candidate columns")
            names = {row[0].lower(): row for row in rows if row}
            for criterion in CRITERIA:
                row = next((r for k, r in names.items() if criterion.lower() in k), None)
                if row is None:
                    failures.append(f"Direction comparison missing criterion: {criterion}")
                    continue
                for cell in row[1:]:
                    m = re.search(r"\b([1-5])\b", cell)
                    if not m:
                        failures.append(f"{criterion}: every candidate needs a 1–5 score")
                        break
        if "trade-off" not in scoring_body.lower() and "tradeoff" not in scoring_body.lower():
            failures.append("Direction comparison needs written trade-off interpretation; do not choose by total alone")

    rejected = section(text, "Rejected directions")
    if rejected is None:
        failures.append("missing section: Rejected directions")
    elif len(candidates) >= 2:
        rejected_lines = [ln for ln in rejected.splitlines() if re.match(r"^\s*[-*]", ln)]
        if len(rejected_lines) < len(candidates) - 1:
            failures.append("Rejected directions needs one product-specific rejection per losing candidate")
        for ln in rejected_lines:
            if not re.search(r"because|would|fails|conflicts|costs|hides|weakens", ln, re.I):
                failures.append("every rejected direction needs a concrete consequence/reason")

    chosen = section(text, "Chosen direction")
    if chosen is None:
        failures.append("missing section: Chosen direction")
    else:
        required_words = ("because", "primary", "transform")
        for word in required_words:
            if word not in chosen.lower():
                failures.append(f"Chosen direction must explain {word}")

    if failures:
        for failure in dict.fromkeys(failures):
            print("FAIL " + failure)
        return 1

    print(f"ok {len(candidates)} structural directions compared across {len(CRITERIA)} criteria with explicit rejection and commitment evidence")
    return 0


if __name__ == "__main__":
    sys.exit(main())