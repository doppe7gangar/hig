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
    """Every .py a doc tells you to run has to be where it says.

    Two forms, because scripts live in two places. `scripts/foo.py` is
    repo-relative and only ever run from the root. A bare `foo.py` in a
    SKILL.md means the script ships inside that skill -- which is the
    only form that still works once someone copies the skill into
    ~/.claude/skills/, and so the form the skills should prefer.

    The bare case went unchecked until apple-design's instructions moved
    off `scripts/` and onto its own bundled tools: coverage of that skill
    silently dropped by three checks, and a rename would have broken the
    documented command with nothing to catch it.
    """
    names = set(os.listdir(HERE))
    for sk, path in skill_docs():
        rel = os.path.relpath(path, REPO)
        text = read(path)
        for m in re.finditer(r"scripts/([\w.]+\.py)", text):
            d.check(m.group(1) in names, f"{rel}: scripts/{m.group(1)} exists")
        # A repo-level doc's invocations resolve from the repo root.
        # TESTING.md pointed at ../skilltest/projtest.py -- a harness that
        # lived outside the tree entirely, so the documented command was
        # broken for everyone but me. Same class as the two before it,
        # and unchecked because this loop skipped the repo-level docs.
        base = os.path.join(SKILLS, sk) if sk else REPO
        # Only invocations -- `python3 foo.py`. A bare mention in prose
        # ("doctor.py fails the build if...") is describing a tool, not
        # telling anyone to run it from here, and flagging those made the
        # check cry wolf on apple-ui-kit's perfectly correct sentence.
        for m in re.finditer(
                r"python3\s+((?:\.\./)?[\w./-]*[\w-]+\.py)\b", text):
            ref = m.group(1)
            # `scripts/foo.py` in a SKILL.md is repo-relative and already
            # handled above -- but only when it is a bare filename. A
            # nested one like scripts/eval/projtest.py matched neither
            # pattern and sailed through both, which is how a doc came to
            # point at a harness outside the tree. Resolve nested paths
            # from the repo root wherever they appear.
            if ref.startswith("scripts/"):
                if "/" not in ref[len("scripts/"):]:
                    continue
                where, label = REPO, "repo"
            else:
                where, label = base, (sk or "repo")
            d.check(os.path.exists(os.path.join(where, ref)),
                    f"{label}: {ref} present when installed")


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


WORDNUM = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,
           "eight":8,"nine":9,"ten":10,"eleven":11,"twelve":12}


def check_reference_count(d):
    """"Nine references" has to match how many are actually there.

    Added after shipping a framework-index and leaving the sentence above
    it reading "Eight references" -- the one stale count in this file
    that nothing else was watching, because it is spelled as a word.
    """
    for sk, path in skill_docs():
        if sk is None:
            continue
        refs = os.path.join(SKILLS, sk, "references")
        if not os.path.isdir(refs):
            continue
        actual = len([f for f in os.listdir(refs) if f.endswith(".md")])
        for m in re.finditer(r"\b(\w+) references,", read(path)):
            claimed = WORDNUM.get(m.group(1).lower())
            if claimed:
                d.check(claimed == actual, f"{sk}: reference count",
                        f"says {m.group(1)} ({claimed}), actual {actual}")


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



def check_corroboration(d, min_components=2):
    """Every measured colour should appear in more than one component.

    doctor otherwise proves only that the repo agrees with itself. This
    is the one check that says something about whether a value is
    *right*: a measurement error in one PNG cannot make the same hex turn
    up in fifteen unrelated components. #0088FF appears in nine, #1A1A1A
    in fifteen -- which is stronger evidence than the fact that they
    disagree with the palette circulating online.

    A value found in a single component is not necessarily wrong. It does
    mean nothing else in the kit backs it up, so it should be checked by
    hand before being trusted.
    """
    tokens = os.path.join(SKILLS, "apple-ui-kit", "tokens", "ios-tokens.css")
    kit = os.path.join(SKILLS, "apple-ui-kit", "ui-kit-tokens.json")
    if not (os.path.exists(tokens) and os.path.exists(kit)):
        return
    # Strip CSS comments first. The header explains that the accent is
    # #0088FF "not #007AFF", so scraping the raw file picks up the
    # superseded value and then reports it as uncorroborated -- which is
    # true, and entirely beside the point.
    css = re.sub(r"/\*.*?\*/", "", read(tokens), flags=re.S)
    wanted = sorted({m.group(0).upper()
                     for m in re.finditer(r"#[0-9A-Fa-f]{6}", css)})
    rows = json.load(open(kit))

    # Values Apple publishes outright, in the Color page's swatch alt
    # text, do not need corroborating against the kit -- a stated value
    # beats an inferred one. Several of them (pink, orange, yellow, two
    # greys) simply never appear in the components that were rendered.
    color_page = os.path.join(REPO, "content", "color.md")
    published = set()
    if os.path.exists(color_page):
        for r, g, b in re.findall(r"R-(\d+),G-(\d+),B-(\d+)",
                                  read(color_page)):
            published.add(f"#{int(r):02X}{int(g):02X}{int(b):02X}")

    for hexv in wanted:
        if hexv in published:
            d.check(True, f"colour {hexv} published by Apple", "Color page")
            continue
        comps = {r["component"] for r in rows
                 for c in r["colours"]
                 if c["hex"].upper() == hexv and c["alpha"] >= 0.99}
        if not comps:
            continue  # translucent or geometry-only; not a flat fill
        d.check(len(comps) >= min_components,
                f"colour {hexv} corroborated",
                f"{len(comps)} component(s)")


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
    check_reference_count(d)
    check_quotes(d)
    check_corroboration(d)
    if not args.fast:
        check_verifier_count(d)

    print(f"\n{d.n - len(d.bad)}/{d.n} checks passed")
    if d.bad:
        print("failed: " + ", ".join(sorted(set(d.bad))))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
