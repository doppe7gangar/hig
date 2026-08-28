#!/usr/bin/env python3
"""Run every gate over one design directory and print a single verdict.

There are nine checks a finished design has to pass and no way to run
them together, so in practice people run one or two and infer the rest.
This is the whole set, in the order the workflow produces the evidence,
with the plumbing check last because it is the only one that opens a
browser and the slowest to wait on.

Point it at whatever the design lives in:

    python3 grade.py ./design
    python3 grade.py ./design --quick      # skip the browser pass

Exit is nonzero if any gate fails, so it works in a hook or CI. Missing
evidence is reported as skipped rather than failed: a design that has
not reached the coherence stage yet is unfinished, not wrong.
"""

import argparse
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# (script, the file it reads, what it is for)
GATES = [
    ("check_direction.py",   "DESIGN.md",         "platform, hierarchy, invariants"),
    ("check_divergence.py",  "DESIGN.md",         "structural alternatives compared"),
    ("check_content.py",     "DESIGN.md",         "content model and representation"),
    ("check_interaction.py", "DESIGN.md",         "flow, commit, recovery"),
    ("check_coherence.py",   "DESIGN.md",         "cross-screen semantics"),
    ("check_grammar.py",     "PROJECT_GRAMMAR.md", "project design grammar"),
    ("audit_grammar.py",     "IMPLEMENTATION_GRAMMAR_AUDIT.md",
     "implementation patterns classified"),
    ("render_review.py",     "VISUAL_REVIEW.md",  "rendered visual critique"),
    ("check_design.py",      None,                "implementation: order, states, contrast"),
]


def main():
    ap = argparse.ArgumentParser(
        description="Run every apple-design gate over one directory.")
    ap.add_argument("directory")
    ap.add_argument("--quick", action="store_true",
                    help="skip the browser pass in check_design")
    a = ap.parse_args()

    root = os.path.abspath(a.directory)
    if not os.path.isdir(root):
        sys.exit(f"not a directory: {a.directory}")

    passed, failed, skipped = [], [], []
    width = max(len(g[0]) for g in GATES)

    for script, needs, purpose in GATES:
        name = script[:-3]
        if needs and not os.path.exists(os.path.join(root, needs)):
            skipped.append((name, needs))
            print(f"  --   {name:<{width}}  no {needs} yet")
            continue

        cmd = [sys.executable, os.path.join(HERE, script), root]
        if script in ("render_review.py", "audit_grammar.py"):
            cmd.append("--check")
        if script == "check_design.py" and a.quick:
            cmd.append("--no-browser")

        r = subprocess.run(cmd, capture_output=True, text=True)
        first = next((l for l in r.stdout.splitlines()
                      if l.strip().startswith(("FAIL", "ok"))), "")
        if r.returncode == 0:
            passed.append(name)
            print(f"  ok   {name:<{width}}  {purpose}")
        else:
            failed.append((name, r.stdout.strip()))
            print(f"  FAIL {name:<{width}}  {first[:60]}")

    print()
    total = len(passed) + len(failed)
    print(f"{len(passed)}/{total} gates passed"
          + (f", {len(skipped)} not reached yet" if skipped else ""))

    if failed:
        # Three lines per gate. An unfilled scaffold fails every section
        # of every gate at once, and thirty lines of that scrolls the
        # summary off the screen -- which is how a grader stops being
        # read. The individual gate prints the full list.
        print()
        for name, out in failed:
            lines = [l.strip() for l in out.splitlines()
                     if l.strip().startswith(("FAIL", "warn"))]
            for line in lines[:3]:
                print(f"  {name}: {line}")
            if len(lines) > 3:
                print(f"  {name}: ...and {len(lines) - 3} more "
                      f"-- python3 {name}.py <dir>")
        return 1
    if skipped:
        print("Nothing failed, but the design is not finished: "
              + ", ".join(f"{n} needs {f}" for n, f in skipped))
        return 0
    print("Every gate passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
