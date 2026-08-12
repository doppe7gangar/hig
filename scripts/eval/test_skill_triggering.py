#!/usr/bin/env python3
"""Measure whether the HIG skills actually get consulted, and which one.

Skills are pull-based: Claude decides whether to reach for one. For a
reference corpus that competes with what the model already believes it
knows, that decision is the whole ballgame -- perfect content nobody
consults is worth nothing. This measures the decision.

It installs the real skills into a throwaway project and runs `claude -p`
against realistic queries, recording which skill (if any) was invoked.

    python3 scripts/eval/test_skill_triggering.py                # default cases
    python3 scripts/eval/test_skill_triggering.py --cases my.json

Cases file is a list of {"query": ..., "expect": "<skill name>" | null},
where null means no skill should fire.

See README.md in this directory for the two measurement traps this avoids.
"""

import argparse
import concurrent.futures as cf
import json
import os
import shutil
import subprocess
import sys
import tempfile

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SKILLS_SRC = os.path.join(REPO, ".claude", "skills")
DEFAULT_MODEL = "claude-opus-5"
DEFAULT_TIMEOUT = 600

DEFAULT_CASES = [
    {"query": "my mac app's toolbar just feels off compared to native apps, 9 icon "
              "buttons crammed up top and a search box on the left. what am i doing wrong",
     "expect": "apple-hig-macos"},
    {"query": "adding a watchOS companion to our fitness app. what can i actually put "
              "on the watch face and how much info fits in a complication",
     "expect": "apple-hig-watchos"},
    {"query": "porting our iPad app to Vision Pro. where should windows go in space and "
              "does the navigation need to change",
     "expect": "apple-hig-visionos"},
    {"query": "building a reading app for iphone + ipad, 7 top level sections. tab bar "
              "or sidebar on the iPad specifically",
     "expect": "apple-hig-ipados"},
    {"query": "our designer used a fixed 13pt font everywhere in the iOS app and QA "
              "flagged it as an accessibility problem. whats the minimum we should support",
     "expect": "apple-hig"},
    # Near-misses: Apple-adjacent but not UI design. A skill that fires here is
    # interrupting work it can't help with, which is its own kind of failure.
    {"query": "xcode 26 keeps failing my archive with 'no profiles for com.acme.app "
              "were found'. how do i fix code signing for a team distribution build",
     "expect": None},
    {"query": "our core data migration from v3 to v4 is losing the relationship between "
              "Order and LineItem. do i need a mapping model",
     "expect": None},
]


def make_project():
    root = tempfile.mkdtemp(prefix="hig-eval-")
    dst = os.path.join(root, ".claude", "skills")
    os.makedirs(dst)
    installed = []
    for d in sorted(os.listdir(SKILLS_SRC)):
        if d.startswith("apple-hig"):
            shutil.copytree(os.path.join(SKILLS_SRC, d), os.path.join(dst, d))
            installed.append(d)
    return root, installed


def probe(query, root, model, timeout):
    """Skills invoked for one query. Distinguishes timeout from non-trigger --
    conflating them makes a slow run look like a dead skill."""
    env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
    try:
        p = subprocess.run(
            ["claude", "-p", query, "--output-format", "stream-json",
             "--verbose", "--model", model],
            cwd=root, env=env, capture_output=True, text=True, timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return ["TIMEOUT"]
    if p.returncode != 0:
        return [f"ERROR(rc={p.returncode})"]
    picked = []
    for line in p.stdout.splitlines():
        try:
            ev = json.loads(line)
        except Exception:
            continue
        msg = ev.get("message")
        if not isinstance(msg, dict):
            continue
        for b in msg.get("content") or []:
            if isinstance(b, dict) and b.get("type") == "tool_use" and b.get("name") == "Skill":
                s = str(b.get("input", {}).get("skill", ""))
                if s and s not in picked:
                    picked.append(s)
    return picked


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cases")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    ap.add_argument("--workers", type=int, default=3)
    args = ap.parse_args()

    cases = json.load(open(args.cases)) if args.cases else DEFAULT_CASES
    root, installed = make_project()
    print(f"installed {len(installed)} skills: {', '.join(installed)}\n")

    results = {}
    with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(probe, c["query"], root, args.model, args.timeout): c
                for c in cases}
        for f in cf.as_completed(futs):
            results[futs[f]["query"]] = f.result()
    shutil.rmtree(root, ignore_errors=True)

    good = 0
    for c in cases:
        got = results[c["query"]]
        expect = c["expect"]
        fired = [g for g in got if g.startswith("apple-hig")]
        if expect is None:
            ok = not fired
        else:
            ok = expect in fired
        good += ok
        label = "ok  " if ok else "FAIL"
        shown = ",".join(got) if got else "none"
        print(f"[{label}] expect={expect or 'no skill':22} got={shown}")
        print(f"        {c['query'][:86]}")

    print(f"\n{good}/{len(cases)} cases correct")
    return 0 if good == len(cases) else 1


if __name__ == "__main__":
    sys.exit(main())
