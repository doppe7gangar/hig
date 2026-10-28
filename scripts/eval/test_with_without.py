#!/usr/bin/env python3
"""Do the skills change the answer, or would the model have said it anyway?

Every other live test checks that an answer with the skills installed is
right. That can't tell a working skill from a model that already knew,
and most of those questions a model answers from memory. This asks the
same questions twice -- once in a project with all four skills, once in
an empty one -- and only counts a case as evidence when the two differ.

The cases are chosen so memory is the wrong answer: values that changed
in iOS 26/27, and quotations, where a paraphrase in Apple's voice reads
exactly like the real sentence. Quotes are graded by verify_quotes.py,
not by eye.

Web tools are blocked in both arms. Without that, the empty project
isn't answering from memory: it fetches Apple's live pages, quotes them
correctly, and the comparison measures browsing against the skill.

    python3 scripts/eval/test_with_without.py
    python3 scripts/eval/test_with_without.py --runs 2   # repeat each arm
"""

import argparse
import concurrent.futures as cf
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SKILLS = os.path.normpath(os.path.join(HERE, "..", "..", ".claude", "skills"))
VERIFY = os.path.join(SKILLS, "apple-hig", "verify_quotes.py")
MODEL, TIMEOUT = "claude-opus-5", 600

# (label, query, required patterns, forbidden patterns, grade quotes)
CASES = [
    ("iOS 27 accent colour",
     "what's the exact hex for the default iOS system blue accent in the "
     "current iOS release? i'm matching it on a web page. just the hex and "
     "where it comes from.",
     [r"#?0088FF"], [], False),

    ("primary label colour",
     "what hex should primary label text be in light mode if i'm matching "
     "the current iOS look on the web?",
     [r"#?1A1A1A"], [], False),

    ("quotes the action sheet rule verbatim",
     "quote Apple's HIG, word for word in quotation marks, on when to use "
     "an action sheet instead of an alert. at least two quotes.",
     [r"action sheet"], [], True),

    ("quotes the tab bar rule verbatim",
     "quote Apple's HIG word for word, in quotation marks, on how many tabs "
     "an iPhone tab bar should have and what to do with the rest.",
     [r"tab"], [], True),
]


def project(with_skills):
    root = tempfile.mkdtemp(prefix="hig-ab-")
    if with_skills:
        dst = os.path.join(root, ".claude", "skills")
        os.makedirs(dst)
        for d in sorted(os.listdir(SKILLS)):
            if d.startswith("apple-"):
                shutil.copytree(os.path.join(SKILLS, d), os.path.join(dst, d))
    return root


def ask(query, with_skills):
    root = project(with_skills)
    env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
    try:
        p = subprocess.run(["claude", "-p", query, "--model", MODEL,
                            "--disallowedTools", "WebFetch,WebSearch"],
                           cwd=root, env=env, capture_output=True,
                           text=True, timeout=TIMEOUT)
        out = p.stdout if p.returncode == 0 else f"<ERROR rc={p.returncode}>"
    except subprocess.TimeoutExpired:
        out = "<TIMEOUT>"
    shutil.rmtree(root, ignore_errors=True)
    return out


def quotes(text):
    """ALTERED count, total quotes and the altered ones, per verify_quotes.py."""
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
        f.write(text)
    p = subprocess.run([sys.executable, VERIFY, f.name, "--project",
                        tempfile.gettempdir()], capture_output=True, text=True)
    os.unlink(f.name)
    counts = {k: int(v) for k, v in re.findall(
        r"(verbatim|elided|source|truncated|altered) (\d+)", p.stdout.lower())}
    altered = re.findall(r"^\s*ALTERED: (.*)$", p.stdout, re.M)
    return counts.get("altered", 0), sum(counts.values()), altered


def grade(text, need, avoid, check_quotes):
    if text.startswith("<"):
        return False, text
    miss = [r for r in need if not re.search(r, text, re.I)]
    hit = [r for r in avoid if re.search(r, text, re.I)]
    note = []
    ok = not miss and not hit
    if miss:
        note.append(f"missing {miss}")
    if hit:
        note.append(f"has {hit}")
    if check_quotes:
        altered, graded, which = quotes(text)
        note.append(f"{graded} quotes, {altered} altered"
                    + "".join(f"\n                  altered: {q[:110]}" for q in which))
        ok = ok and graded > 0 and altered == 0
    return ok, "; ".join(note)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", type=int, default=1)
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--only", help="run cases whose label contains this")
    ap.add_argument("--save", metavar="DIR", default=os.environ.get("EVAL_WORK"),
                    help="write every answer here (run_live.py sets this per run)")
    a = ap.parse_args()
    global CASES
    if a.only:
        CASES = [c for c in CASES if a.only in c[0]]

    jobs = [(c, arm, n) for c in CASES for arm in (True, False)
            for n in range(a.runs)]
    with cf.ThreadPoolExecutor(max_workers=a.workers) as ex:
        futs = {ex.submit(ask, c[1], arm): (c[0], arm, n) for c, arm, n in jobs}
        answers = {futs[f]: f.result() for f in cf.as_completed(futs)}
    if a.save:
        os.makedirs(a.save, exist_ok=True)
        for (label, arm, n), text in answers.items():
            name = f"{re.sub(r'[^a-z0-9]+', '-', label.lower())}-" \
                   f"{'with' if arm else 'without'}-{n + 1}.md"
            with open(os.path.join(a.save, name), "w") as f:
                f.write(text)

    evidence = with_ok = 0
    for label, query, need, avoid, cq in CASES:
        print(f"== {label}")
        passed = {}
        for arm in (True, False):
            name = "with skills" if arm else "without    "
            res = [grade(answers[(label, arm, n)], need, avoid, cq)
                   for n in range(a.runs)]
            passed[arm] = sum(ok for ok, _ in res)
            for ok, note in res:
                print(f"   {name}  {'ok  ' if ok else 'FAIL'}  {note}")
        with_ok += passed[True] == a.runs
        if passed[True] == a.runs and passed[False] < a.runs:
            evidence += 1
            print("   -> the skills made the difference")
        elif passed[True] == a.runs:
            print("   -> right either way; no evidence the skills mattered")
        else:
            print("   -> wrong WITH the skills")
    print(f"\n{with_ok}/{len(CASES)} right with the skills; "
          f"{evidence} where they made the difference")
    sys.exit(0 if with_ok == len(CASES) else 1)


if __name__ == "__main__":
    main()
