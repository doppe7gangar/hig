#!/usr/bin/env python3
"""Does concepts.md fix the 'HIG is silent on X' failure?

Built after concluding the HIG had no empty-state guidance -- it does, in
writing.md, and a component-shaped search missed it. These cases all ask
about concerns with no page of their own, where the wrong answer ("Apple
doesn't cover that") is the easy one to give.
"""

import concurrent.futures as cf
import os
import re
import shutil
import subprocess
import tempfile

SKILLS_SRC = "/tmp/claude-0/-home-user-apple-hig/19e48567-ea3b-518d-bd47-52b9e41c0d63/scratchpad/hig-build/.claude/skills"
MODEL = "claude-opus-5"
TIMEOUT = 600

CASES = [
    ("does apple's HIG say anything about empty states? i've got a list screen "
     "with no items yet and i'm not sure what to put there",
     [r"blank screen|empty state", r"writing|next step"],
     r"no guidance|doesn't cover|not covered|silent",
     "THE ORIGINAL FAILURE: empty-state rule lives in writing.md"),

    ("what does apple say about error handling in my iOS app? like when a "
     "network request fails",
     [r"error"],
     # Only a blanket denial of the whole topic counts as failure. An earlier
     # version flagged any "HIG is silent", which punished the correct
     # behavior: giving the guidance that exists, then scoping the specific
     # sub-aspects Apple genuinely doesn't cover (retry policy, backoff).
     # That scoping is the discipline SKILL.md asks for, not a miss.
     r"(no|isn't any|is no) (specific )?(guidance|rule)s? (on|about|for) error"
     r"|apple (doesn't|does not) cover error",
     "error handling: 16 rules across 14 pages, no errors.md"),

    ("i want to make sure my app works for colorblind users. any apple "
     "guidance on that?",
     [r"color"],
     r"no guidance|doesn't cover|not covered",
     "color blindness: no page, filed under accessibility/color/inclusion"),
]


def make_project():
    root = tempfile.mkdtemp(prefix="hig-v4-")
    dst = os.path.join(root, ".claude", "skills")
    os.makedirs(dst)
    shutil.copytree(os.path.join(SKILLS_SRC, "apple-hig"), os.path.join(dst, "apple-hig"))
    return root


def ask(query, root):
    env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
    try:
        p = subprocess.run(["claude", "-p", query, "--model", MODEL],
                           cwd=root, env=env, capture_output=True,
                           text=True, timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        return "<TIMEOUT>"
    return p.stdout.strip()


if __name__ == "__main__":
    root = make_project()
    res = {}
    with cf.ThreadPoolExecutor(max_workers=3) as ex:
        futs = {ex.submit(ask, q, root): q for q, _, _, _ in CASES}
        for f in cf.as_completed(futs):
            res[futs[f]] = f.result()
    shutil.rmtree(root, ignore_errors=True)

    passed = 0
    for q, want, must_not, note in CASES:
        ans = res[q]
        missing = [p for p in want if not re.search(p, ans, re.I)]
        wrongly_denied = re.search(must_not, ans, re.I)
        ok = not missing and not wrongly_denied
        passed += ok
        print(f"\n[{'PASS' if ok else 'FAIL'}] {note}")
        if missing:
            print(f"   MISSING: {missing}")
        if wrongly_denied:
            print(f"   WRONGLY CLAIMED NO GUIDANCE: '{wrongly_denied.group(0)}'")
        print(f"   ANSWER: {' '.join(ans.split())[:340]}")
    print(f"\n{passed}/{len(CASES)} concept lookups answered without falsely denying coverage")
