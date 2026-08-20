#!/usr/bin/env python3
"""Check third-party design skills against this repo's measured values.

design-skills/ holds 106 skills from six different collections, several
of them covering the same ground as apple-ui-kit. When two installed
skills disagree about what colour systemBlue is, the model gets both and
picks one, so the disagreements are worth knowing before installing
anything.

This repo has ground truth the collections don't: colours measured off
Apple's own iOS 27 UI kit renderings, weights read from SF Pro's fvar
table, and tracking parsed from the HIG's own published table. Anything
stated that contradicts a measurement is reported with both values.

It flags disagreements, not bad writing. A skill can be well written,
useful, and still carry the pre-iOS-26 palette that circulates
everywhere, because that palette was right until it wasn't.

    python3 scripts/audit_design_skills.py
    python3 scripts/audit_design_skills.py --dir some/other/skills
"""

import argparse
import collections
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)

DEFAULT_DIR = os.path.join(REPO, "design-skills")
TOKENS = os.path.join(REPO, ".claude", "skills", "apple-ui-kit", "tokens",
                      "ios-tokens.css")

# Superseded value -> what the kit actually measures. The left-hand side
# is not wrong-in-general; it is what Apple shipped before iOS 26.
SUPERSEDED = {
    "#007AFF": ("#0088FF", "accent blue, light"),
    "#0A84FF": ("#0091FF", "accent blue, dark"),
    "#FF3B30": ("#FF383C", "destructive red, light"),
    "#FF453A": ("#FF4245", "destructive red, dark"),
}

# SF Pro's weight axis, from the variable font's named instances.
SF_WEIGHTS = {"medium": 510, "semibold": 590}
CSS_LADDER = {"medium": 500, "semibold": 600}


def measured_colours():
    """Confirm the claims here still match the generated tokens."""
    if not os.path.exists(TOKENS):
        return set()
    text = open(TOKENS, encoding="utf-8").read()
    return {m.group(0).upper()
            for m in re.finditer(r"#[0-9A-Fa-f]{6}", text)}


def scan(root):
    hits = collections.defaultdict(list)
    for dirpath, dirnames, files in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in {".git", "node_modules"}]
        for fn in files:
            if not fn.endswith((".md", ".css", ".ts", ".tsx", ".js", ".jsx")):
                continue
            path = os.path.join(dirpath, fn)
            try:
                text = open(path, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            rel = os.path.relpath(path, root)

            for old, (new, what) in SUPERSEDED.items():
                for m in re.finditer(re.escape(old), text, re.I):
                    line = text[:m.start()].count("\n") + 1
                    hits["palette"].append((rel, line, old, new, what))

            for name, real in SF_WEIGHTS.items():
                pat = rf"{name}[^\n]{{0,24}}?\b({CSS_LADDER[name]})\b"
                for m in re.finditer(pat, text, re.I):
                    line = text[:m.start()].count("\n") + 1
                    hits["weight"].append((rel, line, name, CSS_LADDER[name],
                                           real))

            # The tracking claim that Apple's own table contradicts.
            for m in re.finditer(
                    r"tracking[^\n]{0,60}(inversely proportional|"
                    r"tighter[^\n]{0,20}larger|larger[^\n]{0,20}tighter)",
                    text, re.I):
                line = text[:m.start()].count("\n") + 1
                hits["tracking"].append((rel, line,
                                         text[m.start():m.start() + 90]))
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=DEFAULT_DIR)
    args = ap.parse_args()

    if not os.path.isdir(args.dir):
        sys.exit(f"not a directory: {args.dir}")

    measured = measured_colours()
    for _, (new, _) in SUPERSEDED.items():
        if measured and new.upper() not in measured:
            print(f"  note: {new} is no longer in the generated tokens; "
                  "re-check SUPERSEDED against ios-tokens.css")

    hits = scan(args.dir)
    n = sum(len(v) for v in hits.values())
    print(f"scanned {args.dir}\n")

    if hits["palette"]:
        by = collections.Counter((o, nw, w)
                                 for _, _, o, nw, w in hits["palette"])
        print(f"SUPERSEDED PALETTE — {len(hits['palette'])} occurrences")
        for (old, new, what), c in by.most_common():
            print(f"  {old} -> {new}   {what}   ({c}x)")
        files = {f for f, *_ in hits["palette"]}
        print(f"  across {len(files)} files, e.g.")
        for f in sorted(files)[:4]:
            print(f"    {f}")
        print()

    if hits["weight"]:
        print(f"WEIGHT LADDER — {len(hits['weight'])} occurrences")
        print("  SF Pro's axis is not the CSS ladder; from its fvar table:")
        for name, real in SF_WEIGHTS.items():
            print(f"    {name}: {real}, not {CSS_LADDER[name]}")
        for f, line, name, claimed, real in hits["weight"][:5]:
            print(f"    {f}:{line}  says {name} {claimed}")
        print()

    if hits["tracking"]:
        print(f"TRACKING DIRECTION — {len(hits['tracking'])} occurrences")
        print("  Apple's published table is a U, not a slope: +6 at 11pt,")
        print("  tightest at 17pt (-26), back through zero near 23pt, and")
        print("  +12 by 34pt. 'Inversely proportional to size' holds only")
        print("  up to 17pt, then reverses -- and large display type is")
        print("  where the claim is most visible and most wrong.")
        for f, line, snippet in hits["tracking"][:4]:
            print(f"    {f}:{line}")
            print(f"      {' '.join(snippet.split())[:80]}")
        print()

    if not n:
        print("No disagreements found.")
    else:
        print(f"{n} disagreements. These are not bugs in those skills so "
              "much as\nvalues that were correct before iOS 26 -- but "
              "installed alongside\napple-ui-kit they contradict it, and "
              "the model sees both.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
