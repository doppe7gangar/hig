#!/usr/bin/env python3
"""Validate project-local design grammar evidence."""

import argparse
import os
import re
import sys

DOMAINS = {
    "typography", "spacing", "geometry", "surfaces", "navigation", "selection",
    "actions", "controls", "content", "interaction", "motion", "language",
    "icons", "adaptivity", "material", "materials"
}


def meaningful(s):
    s = re.sub(r"[`*_>#|:-]", " ", s or "")
    s = re.sub(r"\s+", " ", s).strip()
    return len(s) >= 10 and s.lower() not in {"", "n/a", "none", "todo", "pending", "tbd", "-", "—"} and "______" not in s


def section(text, name):
    m = re.search(rf"^#+\s+{re.escape(name)}\s*$([\s\S]*?)(?=^#+\s|\Z)", text, re.I | re.M)
    return m.group(1).strip() if m else ""


def rows(sec):
    out=[]
    for line in sec.splitlines():
        if "|" not in line: continue
        cells=[c.strip() for c in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r"[-: ]+", c or "-") for c in cells): continue
        out.append(cells)
    return out


def main():
    # argparse, like the other gates. Reading sys.argv[1] raw meant
    # --help was taken as a directory name, so the tool answered a
    # request for its own documentation with "FAIL missing
    # PROJECT_GRAMMAR.md" and exit 1.
    ap = argparse.ArgumentParser(
        description="Validate the project's design grammar memory.")
    ap.add_argument("directory", nargs="?", default=".")
    root = ap.parse_args().directory
    path=os.path.join(root,"PROJECT_GRAMMAR.md")
    if not os.path.exists(path):
        print("FAIL missing PROJECT_GRAMMAR.md")
        return 1
    text=open(path,encoding="utf-8").read(); errors=[]

    scope=section(text,"Scope")
    if len(re.findall(r"^\s*[-*]\s+.+",scope,re.M))<3:
        errors.append("Scope needs product/platform/evidence context")

    established=rows(section(text,"Established rules"))
    data=[r for r in established if r and r[0].lower()!="domain"]
    if len(data)<5:
        errors.append("need at least five established semantic rules")
    seen=set()
    for i,r in enumerate(data,1):
        # meaningful() asks for ten characters of substance, which is the
        # right test for a rule, its evidence and its scope, and the
        # wrong one for the domain -- that cell is a one-word enum,
        # already validated against DOMAINS below. Applying the length
        # floor to it rejected twelve of the sixteen domains this gate
        # accepts, including spacing, actions, icons and selection, so a
        # grammar could only satisfy "rules across at least four
        # domains" by using the exact four long enough to qualify.
        if len(r) < 4 or not r[0].strip() or sum(meaningful(c) for c in r[1:4]) < 3:
            errors.append(f"established rule {i} lacks domain/rule/evidence/scope")
            continue
        d=r[0].lower().strip(); seen.add(d)
        if d not in DOMAINS:
            errors.append(f"established rule {i} has unclear domain: {r[0]}")
        if not re.search(r"[;,]|\band\b|\bstate\b|\bscreen\b|\bview\b",r[2],re.I):
            errors.append(f"established rule {i} evidence appears too thin; cite repeated/architectural evidence")
    if len(seen)<4:
        errors.append("established grammar needs rules across at least four domains")

    language=rows(section(text,"Canonical language"))
    ldata=[r for r in language if r and r[0].lower()!="concept"]
    if not ldata:
        errors.append("Canonical language needs at least one stable term/icon mapping")

    adaptive=rows(section(text,"Adaptive transformations"))
    adata=[r for r in adaptive if r and r[0].lower()!="structure"]
    if not adata:
        errors.append("Adaptive transformations needs at least one recurring transformation")
    elif any(len(r)<4 or sum(meaningful(c) for c in r[:4])<4 for r in adata):
        errors.append("adaptive transformation rows need structure/wide/compact/invariant")

    if errors:
        for e in errors: print("FAIL "+e)
        return 1
    print("ok project design grammar evidence")
    return 0


if __name__=="__main__": sys.exit(main())
