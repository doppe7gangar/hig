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

The tests run on your account's usage. If it hits a limit, every model
call fails at once and a test looks broken when it never ran. So a run
that fails is checked against the limit -- its own output, then a
one-word probe -- and if the limit is the reason, the run is marked
blocked, not failed, and no further runs start. --resume picks up from
there once the limit resets.

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
# Seen so far: "hit your weekly limit", "hit your 5-hour limit", each
# followed by "· resets <time>". Match the shape, not a list of words.
LIMIT = re.compile(r"hit your [^\n]{0,30}?limit[^\n]*|limit · resets[^\n]*|"
                   r"\b(usage|session|rate) limit[^\n]*", re.I)
HALT = threading.Event()
REASON = []


def limit_reached(text):
    """The limit message, from the output or from a one-word probe."""
    m = LIMIT.search(text)
    if m:
        return m.group(0).strip()
    try:
        p = subprocess.run(["claude", "-p", "reply with the single word ok"],
                           capture_output=True, text=True, timeout=120,
                           env={k: v for k, v in os.environ.items() if k != "CLAUDECODE"})
        m = LIMIT.search(p.stdout + p.stderr)
        return m.group(0).strip() if m else None
    except Exception:
        return None


def run(name, n, out, resume=False):
    """One run of one test. Returns its record; never raises.

    A finished run's log ends with a footer line. With resume, a log that
    has one is read back instead of run again; a blocked run's log has a
    different footer, so it runs again."""
    cmd, pattern, limit = TESTS[name]
    log = os.path.join(out, f"{name}-{n}.txt")
    record = dict(name=name, n=n, ok=False, passed=0, total=None, code=None,
                  minutes=0.0, fails=[], log=log, status="done")
    previous = open(log, encoding="utf-8").read() if resume and os.path.exists(log) else ""
    footer = FOOTER.search(previous)
    if footer:
        text, record["minutes"] = previous, float(footer.group(1))
        record["code"] = None if footer.group(2) == "None" else int(footer.group(2))
    elif HALT.is_set():
        return dict(record, status="not run")
    else:
        env = dict(os.environ, EVAL_WORK=os.path.join(out, f"{name}-{n}.work"))
        started = time.time()
        try:
            p = subprocess.run([sys.executable, os.path.join(HERE, cmd[0])] + cmd[1:],
                               cwd=os.path.dirname(os.path.dirname(HERE)), env=env,
                               capture_output=True, text=True, timeout=limit * 60)
            text, record["code"] = p.stdout + p.stderr, p.returncode
        except subprocess.TimeoutExpired as e:
            text = (e.stdout or "") if isinstance(e.stdout, str) else (e.stdout or b"").decode("utf-8", "replace")
            text += f"\nTIMEOUT after {limit} min\n"
        record["minutes"] = (time.time() - started) / 60

    m = list(re.finditer(pattern, text))
    if m and m[-1].group(1) in ("PASS", "FAIL"):
        record.update(passed=int(m[-1].group(1) == "PASS"), total=1)
    elif m:
        record.update(passed=int(m[-1].group(1)), total=int(m[-1].group(2)))
    record["ok"] = record["total"] is not None and record["passed"] == record["total"]
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if re.search(r"\bFAIL\b|TIMEOUT|ERROR|Traceback", line):
            record["fails"].append(line.rstrip())
            if i + 1 < len(lines) and lines[i + 1].startswith(" "):
                record["fails"].append(lines[i + 1].rstrip())

    if not footer:
        reason = None if record["ok"] else limit_reached(text)
        with open(log, "w", encoding="utf-8") as f:
            if reason:
                f.write(text + f"\nrun_live: blocked by a usage limit: {reason}\n")
            else:
                f.write(text + f"\nrun_live: {record['minutes']:.1f} min, exit {record['code']}\n")
        if reason:
            REASON.append(reason)
            HALT.set()
            record["status"] = "blocked"
    return record


def summary(records, names, runs, out, started, done):
    rows, detail = [], []
    for name in names:
        rs = sorted((r for r in records if r["name"] == name), key=lambda r: r["n"])
        ran = [r for r in rs if r["status"] == "done"]
        missing = len(rs) - len(ran)
        if not rs:
            rows.append(f"| {name} | waiting | | |")
            continue
        if not ran:
            rows.append(f"| {name} | none finished ({missing} stopped by the limit) | | |")
            continue
        cases = sum(r["passed"] for r in ran)
        total = sum(r["total"] or 0 for r in ran)
        note = f" ({missing} stopped by the limit)" if missing else ""
        rows.append(f"| {name} | {sum(r['ok'] for r in ran)}/{len(ran)}{note} | {cases}/{total} | "
                    + ", ".join(f"{r['minutes']:.0f}" for r in ran) + " |")
        for r in ran:
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
    body = [f"# Live tests, {runs} run{'s' if runs > 1 else ''} each, started {t0}", ""]
    if REASON:
        body += [f"**Stopped early: the account hit a usage limit** ({REASON[0]}). "
                 "Runs it stopped are not counted as failures. Re-run with "
                 "`--resume` once it resets; finished runs are kept.", ""]
    body += ["| Test | Runs passed | Cases passed | Minutes per run |", "|---|---|---|---|",
             *rows, ""]
    body += ["## Failures", "", *detail] if detail else ["No failures among finished runs.", ""]
    finished = sum(r["status"] == "done" for r in records)
    if done:
        body.append(f"DONE {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}: "
                    f"{finished} runs finished, {len(records) - finished} stopped by "
                    f"the limit, outputs in {out}")
    else:
        body.append(f"IN PROGRESS: {finished} of {len(names) * runs} runs finished")
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
    if HALT.is_set():
        return 2
    return 0 if all(r["ok"] for r in records) else 1


if __name__ == "__main__":
    sys.exit(main())
