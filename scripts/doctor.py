#!/usr/bin/env python3
"""Check every claim in this repo that has a computable ground truth.

Written after finding the same class of bug four rounds running, one
instance at a time: a hardcoded 949 where the kit holds 947, a SKILL.md
still claiming 2,280 rules after a re-scrape made it 2,326, instructions
naming build_web_tokens.py months after it was renamed, a checker whose
documented path did not exist once the skill was installed. Each was
fixed on its own. None of them should have needed finding by hand,
because every one is a number or a path that can be resolved and
compared.

So this resolves them. It is the difference between "I fixed the stale
count" and "a stale count cannot ship".

    python3 scripts/doctor.py         # exits non-zero on any problem
    python3 scripts/doctor.py -v      # show every check
    python3 scripts/doctor.py --fast  # skip the browser run

build_skill.py and build_design_tokens.py call --fast on every rebuild,
so a regenerated file that no longer matches what the docs claim fails
at the moment it is written rather than months later in a test round.

What it will not catch: whether the values are *correct*. A confidently
wrong measurement stated consistently everywhere passes this cleanly.
That is what verify_web_ui.py and the eval runs are for.
"""

import argparse
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
SKILLS = os.path.join(REPO, ".claude", "skills")


class Doctor:
    def __init__(self, verbose):
        self.bad = []
        self.n = 0
        self.verbose = verbose

    def check(self, ok, label, detail=""):
        self.n += 1
        if ok:
            if self.verbose:
                print(f"  ok    {label}  {detail}")
        else:
            print(f"  FAIL  {label}  {detail}")
            self.bad.append(label)


def read(p):
    return open(p, encoding="utf-8", errors="replace").read()


def skill_docs():
    """Every SKILL.md plus the repo-level docs that make claims."""
    out = []
    for sk in sorted(os.listdir(SKILLS)):
        p = os.path.join(SKILLS, sk, "SKILL.md")
        if os.path.exists(p):
            out.append((sk, p))
    for name in ("TESTING.md", "README.md", "AGENTS.md"):
        p = os.path.join(REPO, name)
        if os.path.exists(p):
            out.append((None, p))
    return out


def truth():
    """Ground truth, derived rather than declared."""
    t = {}
    hig = os.path.join(SKILLS, "apple-hig")
    refs = os.path.join(hig, "references")

    rules = os.path.join(refs, "rules.md")
    if os.path.exists(rules):
        t["rules"] = len(re.findall(r"^- \*\*", read(rules), re.M))
    pages = os.path.join(refs, "pages")
    if os.path.isdir(pages):
        t["pages"] = len([f for f in os.listdir(pages) if f.endswith(".md")])
    assets = os.path.join(hig, "assets")
    if os.path.isdir(assets):
        t["screenshots"] = sum(len([f for f in fs if f.endswith(".png")])
                               for _, _, fs in os.walk(assets))
    api = os.path.join(refs, "api-map.md")
    if os.path.exists(api):
        t["frameworks"] = read(api).count("\n### ")

    kit = os.path.join(SKILLS, "apple-ui-kit", "ui-kit-tokens.json")
    if os.path.exists(kit):
        t["measurements"] = len(json.load(open(kit)))
    return t


# Claim patterns -> the key in truth() they must equal. Written to match
# how the docs actually phrase things, not how I wish they did.
# Each pattern must pin the claim to the whole corpus. A bare "N rules"
# also matches "11 rules on destructive actions across 8", which is a
# true statement about a subset -- flagging it as a stale total was the
# checker being wrong, not the doc.
CLAIMS = [
    (r"all ([\d,]+) HIG rules", "rules"),
    (r"\*\*([\d,]+) rules as one-line imperatives\*\*", "rules"),
    (r"holds all ([\d,]+) HIG rules", "rules"),
    (r"Contains all ([\d,]+) HIG rules", "rules"),
    (r"([\d,]+)-page corpus", "pages"),
    (r"([\d,]+)\s+(?:real component\s+)?screenshots", "screenshots"),
    (r"(\d+)\+ Apple frameworks", "frameworks"),
    (r"(\d+)\+ other frameworks", "frameworks"),
    (r"(\d+)\+ frameworks including", "frameworks"),
    (r"([\d,]+) renderings", "measurements"),
]


def check_counts(d, facts):
    for sk, path in skill_docs():
        text = read(path)
        rel = os.path.relpath(path, REPO)
        for pat, key in CLAIMS:
            if key not in facts:
                continue
            for m in re.finditer(pat, text):
                claimed = int(m.group(1).replace(",", ""))
                actual = facts[key]
                # "32+ frameworks" is a floor, not an equality.
                ok = claimed <= actual if "+" in m.group(0) else claimed == actual
                d.check(ok, f"{rel}: {key} count",
                        f"says {claimed}, actual {actual}")


def check_verifier_count(d):
    """The docs quote how many checks verify_web_ui runs. Run it and see."""
    claims = []
    for sk, path in skill_docs():
        for m in re.finditer(r"(\d+) checks\b", read(path)):
            claims.append((os.path.relpath(path, REPO), int(m.group(1))))
    if not claims:
        return
    script = os.path.join(SKILLS, "apple-ui-kit", "verify_web_ui.py")
    if not os.path.exists(script):
        d.check(False, "verify_web_ui.py present")
        return
    try:
        out = subprocess.run([sys.executable, script], capture_output=True,
                             text=True, timeout=900).stdout
    except Exception as e:
        d.check(False, "verify_web_ui.py runs", str(e))
        return
    m = re.search(r"(\d+)/(\d+) checks passed", out)
    if not m:
        d.check(False, "verify_web_ui.py reports a total", out[-200:])
        return
    actual = int(m.group(2))
    d.check(m.group(1) == m.group(2), "verify_web_ui all pass",
            f"{m.group(1)}/{actual}")
    for rel, claimed in claims:
        d.check(claimed == actual, f"{rel}: check count",
                f"says {claimed}, actual {actual}")


def check_script_refs(d):
    names = set(os.listdir(HERE))
    for sk, path in skill_docs():
        rel = os.path.relpath(path, REPO)
        for m in re.finditer(r"scripts/([\w.]+\.py)", read(path)):
            d.check(m.group(1) in names, f"{rel}: scripts/{m.group(1)} exists")


def check_skill_paths(d):
    """A skill must not name a file it won't have once installed."""
    for sk, path in skill_docs():
        if sk is None:
            continue
        base = os.path.join(SKILLS, sk)
        text = read(path)
        for m in re.finditer(
                r"`((?:references|tokens|fonts|assets)/[\w./ -]+)`", text):
            p = m.group(1)
            if "<" in p or p.endswith("/"):
                continue
            d.check(os.path.exists(os.path.join(base, p)),
                    f"{sk}: {p} present when installed")


def check_placeholders(d):
    """Generated files must not ship an unsubstituted placeholder."""
    for sk in sorted(os.listdir(SKILLS)):
        for dirpath, _, files in os.walk(os.path.join(SKILLS, sk)):
            for f in files:
                if not f.endswith((".md", ".css", ".json")):
                    continue
                p = os.path.join(dirpath, f)
                if os.path.getsize(p) > 5_000_000:
                    continue
                text = read(p)
                # Strip fenced code first. "{{" was flagging JSX inline
                # style -- style={{ x }} -- which is ordinary code, not an
                # unsubstituted template. Only genuinely ours count.
                prose = re.sub(r"^```.*?^```", "", text, flags=re.M | re.S)
                for ph in ("{TOTAL}", "TODO:", "FIXME", "XXX:"):
                    if ph in prose:
                        d.check(False,
                                f"{os.path.relpath(p, REPO)}: placeholder",
                                ph)


def check_quotes(d):
    """Apple quotes in our own SKILL.mds must be verbatim."""
    vq = os.path.join(SKILLS, "apple-hig", "verify_quotes.py")
    if not os.path.exists(vq):
        return
    for sk, path in skill_docs():
        if sk is None:
            continue
        out = subprocess.run(
            [sys.executable, vq, path, "--project", os.devnull],
            capture_output=True, text=True).stdout
        m = re.search(r"truncated (\d+), altered (\d+)", out)
        if not m:
            continue
        # Altered spans in a SKILL.md are usually its own example queries
        # ("should this be a sheet or a popover"), which are not Apple
        # quotes. Truncation is the one that means a real rule got cut.
        d.check(int(m.group(1)) == 0, f"{sk}: no truncated Apple quotes",
                f"truncated {m.group(1)}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--verbose", action="store_true")
    ap.add_argument("--fast", action="store_true",
                    help="skip the browser run; everything else is instant, "
                         "so the build can call this on every rebuild")
    args = ap.parse_args()

    d = Doctor(args.verbose)
    facts = truth()
    print("ground truth:", ", ".join(f"{k}={v}" for k, v in sorted(facts.items())))
    print()

    check_counts(d, facts)
    check_script_refs(d)
    check_skill_paths(d)
    check_placeholders(d)
    check_quotes(d)
    if not args.fast:
        check_verifier_count(d)

    print(f"\n{d.n - len(d.bad)}/{d.n} checks passed")
    if d.bad:
        print("failed: " + ", ".join(sorted(set(d.bad))))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
