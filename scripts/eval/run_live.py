#!/usr/bin/env python3
"""Run the live tests several times and write one summary you can trust.

Every live test asks a real model, and a model answers differently from
one run to the next, so a single pass proves less than it looks. This runs
each test N times, keeps every run's output, and writes SUMMARY.md with
the pass rate, every failing line, and how long each run took.

SUMMARY.md is rewritten as runs finish and ends with a DONE line only when
all of them have. Read that file rather than trusting a "finished" notice
from whatever launched this: in testing, such notices arrived early and
reported results the files didn't contain.

    python3 scripts/eval/run_live.py                    # every test, 3 runs
    python3 scripts/eval/run_live.py --runs 5 --only triggering,with_without
    python3 scripts/eval/run_live.py --out /tmp/live    # default scripts/eval/out/live
    python3 scripts/eval/run_live.py --resume           # keep runs that finished
"""

import argparse
import concurrent.futures as cf
import os
import re
import subprocess
import sys
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))

# name: (command, pattern giving passed/total, limit in minutes)
TESTS = {
    "triggering":     (["test_skill_triggering.py"], r"(\d+)/(\d+) cases correct", 60),
    "full_skill":     (["test_full_skill.py"], r"(\d+)/(\d+) references reachable", 60),
    "with_without":   (["test_with_without.py", "--runs", "2"], r"(\d+)/(\d+) right with the skills", 60),
    "build_task":     (["test_build_task.py"], r"(\d+)/(\d+) build tasks", 60),
    "concept_lookup": (["test_concept_lookup.py"], r"(\d+)/(\d+) concept lookups", 60),
    "ui_kit_build":   (["test_ui_kit_build.py"], r"(\d+)/(\d+) checks passed", 75),
    "design_brief":   (["projtest.py", "p-split"], r"verdict: (PASS|FAIL)", 150),
}


FOOTER = re.compile(r"^run_live: (\S+) min, exit (\S+)$", re.M)


def run(name, n, out, resume=False):
    """One run of one test. Returns its record; never raises.

    Every log ends with a footer line, written only once the run is over.
    With resume, a log that has one is read back instead of run again, so
    a container restart costs the runs that were in flight, not all of
    them."""
    cmd, pattern, limit = TESTS[name]
    log = os.path.join(out, f"{name}-{n}.txt")
    previous = open(log, encoding="utf-8").read() if resume and os.path.exists(log) else ""
    footer = FOOTER.search(previous)
    if footer:
        text, minutes = previous, float(footer.group(1))
        code = None if footer.group(2) == "None" else int(footer.group(2))
    else:
        env = dict(os.environ, PROJTEST_WORK=os.path.join(out, f"{name}-{n}.work"))
        started = time.time()
        try:
            p = subprocess.run([sys.executable, os.path.join(HERE, cmd[0])] + cmd[1:],
                               cwd=os.path.dirname(os.path.dirname(HERE)), env=env,
                               capture_output=True, text=True, timeout=limit * 60)
            text, code = p.stdout + p.stderr, p.returncode
        except subprocess.TimeoutExpired as e:
            text = (e.stdout or "") if isinstance(e.stdout, str) else (e.stdout or b"").decode("utf-8", "replace")
            text, code = text + f"\nTIMEOUT after {limit} min\n", None
        minutes = (time.time() - started) / 60
        with open(log, "w", encoding="utf-8") as f:
            f.write(text + f"\nrun_live: {minutes:.1f} min, exit {code}\n")

    m = list(re.finditer(pattern, text))
    if not m:
        passed, total = 0, None
    elif m[-1].group(1) in ("PASS", "FAIL"):
        passed, total = int(m[-1].group(1) == "PASS"), 1
    else:
        passed, total = int(m[-1].group(1)), int(m[-1].group(2))
    fails, lines = [], text.splitlines()
    for i, line in enumerate(lines):
        if re.search(r"\bFAIL\b|TIMEOUT|ERROR|Traceback", line):
            fails.append(line.rstrip())
            if i + 1 < len(lines) and lines[i + 1].startswith(" "):
                fails.append(lines[i + 1].rstrip())
    ok = total is not None and passed == total
    return dict(name=name, n=n, ok=ok, passed=passed, total=total, code=code,
                minutes=minutes, fails=fails, log=log)


def summary(records, names, runs, out, started, done):
    rows, detail = [], []
    for name in names:
        rs = sorted((r for r in records if r["name"] == name), key=lambda r: r["n"])
        if not rs:
            rows.append(f"| {name} | waiting | | |")
            continue
        cases = sum(r["passed"] for r in rs)
        total = sum(r["total"] or 0 for r in rs)
        rows.append(f"| {name} | {sum(r['ok'] for r in rs)}/{len(rs)}"
                    f"{'' if len(rs) == runs else f' of {runs}'} | {cases}/{total} | "
                    + ", ".join(f"{r['minutes']:.0f}" for r in rs) + " |")
        for r in rs:
            if not r["ok"]:
                if r["code"] is None:
                    why = "timed out"
                elif r["total"] is None:
                    why = f"no summary line, exit {r['code']}"
                else:
                    why = f"{r['passed']}/{r['total']}, exit {r['code']}"
                detail.append(f"### {name}, run {r['n']} ({why})\n\n"
                              + "\n".join("    " + l for l in r["fails"][:20])
                              + f"\n\nFull output: `{r['log']}`\n")
    t0 = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(started))
    body = [f"# Live tests, {runs} run{'s' if runs > 1 else ''} each, started {t0}", "",
            "| Test | Runs passed | Cases passed | Minutes per run |", "|---|---|---|---|",
            *rows, ""]
    body += ["## Failures", "", *detail] if detail else ["No failures.", ""]
    if done:
        body.append(f"DONE {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}: "
                    f"{len(records)} runs finished, outputs in {out}")
    else:
        body.append(f"IN PROGRESS: {len(records)} of {len(names) * runs} runs finished")
    with open(os.path.join(out, "SUMMARY.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(body) + "\n")
    return "\n".join(body)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--only", help="comma-separated: " + ", ".join(TESTS))
    ap.add_argument("--workers", type=int, default=2,
                    help="runs at once; each test also runs its own cases in parallel")
    ap.add_argument("--out", default=os.path.join(HERE, "out", "live"))
    ap.add_argument("--resume", action="store_true",
                    help="reuse runs whose logs say they finished")
    a = ap.parse_args()

    names = a.only.split(",") if a.only else list(TESTS)
    unknown = [n for n in names if n not in TESTS]
    if unknown:
        sys.exit(f"unknown test(s): {', '.join(unknown)}; choose from {', '.join(TESTS)}")
    out = os.path.abspath(a.out)
    os.makedirs(out, exist_ok=True)
    started, records, lock = time.time(), [], threading.Lock()
    summary(records, names, a.runs, out, started, done=False)

    jobs = [(name, n) for n in range(1, a.runs + 1) for name in names]
    with cf.ThreadPoolExecutor(max_workers=a.workers) as ex:
        for fut in cf.as_completed([ex.submit(run, name, n, out, a.resume)
                                    for name, n in jobs]):
            with lock:
                records.append(fut.result())
                summary(records, names, a.runs, out, started, done=False)
    print(summary(records, names, a.runs, out, started, done=True))
    return 0 if all(r["ok"] for r in records) else 1


if __name__ == "__main__":
    sys.exit(main())
