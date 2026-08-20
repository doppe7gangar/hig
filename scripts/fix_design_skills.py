#!/usr/bin/env python3
"""Bring the third-party skills' Apple values in line with the measured ones.

Companion to audit_design_skills.py. The audit reports disagreements;
this applies the ones that are a straight substitution, and refuses to
touch anything that isn't.

What it changes:
  - superseded palette values, but only where the value is being *used*.
    A line like "hardcoding #007AFF is a maintenance trap, use
    Color.blue" is correct advice that happens to name the old value;
    rewriting it would turn good guidance into nonsense, so the same
    cautionary test the audit uses guards the edit.
  - weight numbers attached to the words Medium and Semibold, which are
    510 and 590 in SF Pro's own fvar table rather than the CSS 500/600.

What it deliberately leaves alone:
  - prose claims. The tracking assertion in apple-design-foundations is
    a paragraph making an argument, not a number to swap, and rewriting
    an argument mechanically produces something that reads like it means
    something and doesn't. That one is edited by hand.

Every touched file gets a provenance line so it is obvious later that
this is no longer purely upstream content.

    python3 scripts/fix_design_skills.py --dry-run
    python3 scripts/fix_design_skills.py
"""

import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from audit_design_skills import (SUPERSEDED, SF_WEIGHTS, CSS_LADDER,  # noqa
                                 is_cautionary, DEFAULT_DIR)

NOTE = ("<!-- Apple values in this file were reconciled against the "
        "measurements in\n     .claude/skills/apple-ui-kit/tokens/ by "
        "scripts/fix_design_skills.py.\n     The originals were the "
        "pre-iOS-26 palette and the CSS weight ladder. -->\n")

EXT = (".md", ".css", ".ts", ".tsx", ".js", ".jsx", ".html")


def fix_text(text):
    changes = []
    out = []
    for line in text.split("\n"):
        original = line
        if not is_cautionary(line):
            for old, (new, what) in SUPERSEDED.items():
                for variant in (old, old.lower()):
                    if variant in line:
                        cased = new if variant == old else new.lower()
                        line = line.replace(variant, cased)
                        changes.append(f"{old} -> {new} ({what})")
        for name, real in SF_WEIGHTS.items():
            css = CSS_LADDER[name]
            pat = re.compile(rf"({name}[^\n]{{0,24}}?\b){css}\b", re.I)
            if pat.search(line):
                line = pat.sub(rf"\g<1>{real}", line)
                changes.append(f"{name} {css} -> {real}")
        out.append(line)
        del original
    return "\n".join(out), changes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=DEFAULT_DIR)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    total = 0
    touched = 0
    for dirpath, dirnames, files in os.walk(args.dir):
        dirnames[:] = [d for d in dirnames if d not in {".git", "node_modules"}]
        for fn in sorted(files):
            if not fn.endswith(EXT):
                continue
            path = os.path.join(dirpath, fn)
            try:
                text = open(path, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            new, changes = fix_text(text)
            if not changes:
                continue
            touched += 1
            total += len(changes)
            rel = os.path.relpath(path, args.dir)
            print(f"{rel}  ({len(changes)})")
            for c in sorted(set(changes)):
                print(f"    {c}")
            if not args.dry_run:
                if fn.endswith(".md") and NOTE not in new:
                    new = NOTE + new
                open(path, "w", encoding="utf-8").write(new)

    verb = "would change" if args.dry_run else "changed"
    print(f"\n{verb} {total} values across {touched} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
