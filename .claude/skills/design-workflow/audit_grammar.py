#!/usr/bin/env python3
"""Extract implementation patterns and compare them with PROJECT_GRAMMAR.md.

This is an evidence tool, not an aesthetic judge. It reports repeated and
one-off implementation patterns, potential drift, and documented-vs-observed
coverage. It never promotes an observation into a design rule automatically.

Usage:
    python3 audit_grammar.py ./design
    python3 audit_grammar.py ./design --check
"""

import argparse
import collections
import glob
import json
import os
import re
import sys

IGNORE_DIRS = {"vendor", "node_modules", ".git", ".visual-review"}
CSS_PROPS = {
    "font-size": "typography",
    "font-weight": "typography",
    "line-height": "typography",
    "letter-spacing": "typography",
    "gap": "spacing",
    "row-gap": "spacing",
    "column-gap": "spacing",
    "padding": "spacing",
    "margin": "spacing",
    "border-radius": "geometry",
    "box-shadow": "surfaces",
    "backdrop-filter": "materials",
    "background": "surfaces",
}


def files(root, suffix):
    out=[]
    for dp, dns, names in os.walk(root):
        dns[:] = [d for d in dns if d not in IGNORE_DIRS]
        for n in names:
            if n.endswith(suffix): out.append(os.path.join(dp,n))
    return out


def read(path):
    return open(path,encoding="utf-8",errors="replace").read()


def normalize_value(v):
    v=re.sub(r"\s+"," ",v.strip())
    return v[:160]


def extract_css(root):
    chunks=[]
    for p in files(root,".css"):
        if os.path.basename(p)=="theme.css": continue
        chunks.append((p,read(p)))
    for p in files(root,".html"):
        t=read(p)
        for css in re.findall(r"<style[^>]*>(.*?)</style>",t,re.S|re.I): chunks.append((p+"::<style>",css))
        inline="\n".join(re.findall(r'style=["\']([^"\']+)["\']',t,re.I))
        if inline: chunks.append((p+"::inline",inline))
    return chunks


def css_observations(root):
    values=collections.defaultdict(collections.Counter)
    locations=collections.defaultdict(lambda:collections.defaultdict(set))
    for path,css in extract_css(root):
        css=re.sub(r"/\*.*?\*/"," ",css,flags=re.S)
        for prop,domain in CSS_PROPS.items():
            for m in re.finditer(rf"(?<![-\w]){re.escape(prop)}\s*:\s*([^;}}]+)",css,re.I):
                v=normalize_value(m.group(1)); values[(domain,prop)][v]+=1; locations[(domain,prop)][v].add(os.path.relpath(path,root))
    return values,locations


def html_semantics(root):
    c=collections.Counter(); labels=collections.Counter(); classes=collections.Counter()
    for p in files(root,".html"):
        t=read(p)
        for tag in ("nav","aside","main","header","footer","dialog","table","form","button","input","select","textarea"):
            c[tag]+=len(re.findall(rf"<{tag}\b",t,re.I))
        for lab in re.findall(r"<(?:button|a)[^>]*>(.*?)</(?:button|a)>",t,re.S|re.I):
            s=re.sub(r"<[^>]+>"," ",lab); s=re.sub(r"\s+"," ",s).strip()
            if 1<=len(s)<=60: labels[s]+=1
        for attr in re.findall(r'class=["\']([^"\']+)["\']',t,re.I):
            for cls in attr.split(): classes[cls]+=1
    return c,labels,classes


def grammar_text(root):
    p=os.path.join(root,"PROJECT_GRAMMAR.md")
    return read(p) if os.path.exists(p) else ""


def documented_terms(grammar):
    terms=set()
    for line in grammar.splitlines():
        if "|" in line:
            for c in line.strip().strip("|").split("|"):
                c=re.sub(r"[`*_]","",c).strip().lower()
                if len(c)>=4: terms.add(c)
    return terms


def smell(values):
    warnings=[]
    by_domain=collections.defaultdict(set)
    for (domain,prop),counter in values.items():
        by_domain[domain].update(counter)
        singletons=[v for v,n in counter.items() if n==1]
        if prop in ("font-size","border-radius","gap") and len(counter)>=7:
            warnings.append(f"{prop} has {len(counter)} distinct values; review whether semantic roles/rhythm have drifted")
        if prop in ("font-size","border-radius","gap") and len(singletons)>=4:
            warnings.append(f"{prop} has {len(singletons)} one-off values; review undocumented exceptions")
    if len(by_domain.get("surfaces",set()))>=12:
        warnings.append("surface/background treatment is highly varied; confirm material roles remain semantic")
    return warnings


def report(root):
    vals,locs=css_observations(root); sem,labels,classes=html_semantics(root); grammar=grammar_text(root); warnings=smell(vals)
    out=["# Implementation grammar audit","","> Observations are evidence prompts, not automatic design rules.",""]
    if not grammar:
        out += ["## Grammar status","","No `PROJECT_GRAMMAR.md` found. Implementation observations can inform a future grammar but must not be promoted automatically.",""]
    else:
        out += ["## Grammar status","","`PROJECT_GRAMMAR.md` found. Compare observations below with established/provisional/exception/retired rules.",""]
    out += ["## Repeated implementation patterns",""]
    for (domain,prop),counter in sorted(vals.items()):
        repeated=[(v,n) for v,n in counter.most_common() if n>=2]
        if not repeated: continue
        out.append(f"### {domain} · `{prop}`")
        for v,n in repeated[:12]:
            where=", ".join(sorted(locs[(domain,prop)][v])[:4])
            out.append(f"- `{v}` — {n} occurrences — {where}")
        out.append("")
    out += ["## One-off / possible drift observations",""]
    any_one=False
    for (domain,prop),counter in sorted(vals.items()):
        singles=[v for v,n in counter.items() if n==1]
        if prop not in ("font-size","gap","border-radius","box-shadow","backdrop-filter") or not singles: continue
        any_one=True; out.append(f"### {domain} · `{prop}`")
        for v in singles[:12]:
            where=", ".join(sorted(locs[(domain,prop)][v])[:3]); out.append(f"- `{v}` — {where}")
        out.append("")
    if not any_one: out += ["No obvious one-off values in the watched properties.",""]
    out += ["## Structural/interaction observations","",f"- Semantic element counts: `{json.dumps(dict(sem),sort_keys=True)}`"]
    repeated_labels=[(s,n) for s,n in labels.most_common() if n>=2]
    if repeated_labels: out.append("- Repeated action/link labels: "+"; ".join(f"{s} ×{n}" for s,n in repeated_labels[:12]))
    repeated_classes=[(s,n) for s,n in classes.most_common() if n>=3]
    if repeated_classes: out.append("- Repeated implementation classes: "+"; ".join(f"{s} ×{n}" for s,n in repeated_classes[:15]))
    out += ["","## Automated drift prompts",""]
    if warnings:
        out += [f"- {w}" for w in warnings]
    else: out.append("- No high-volume drift prompt triggered by the watched properties.")
    out += ["","## Review decisions","","Replace every `[PENDING]` line with a decision. Observed repetition alone is not enough to establish a grammar rule.","",
            "- [PENDING] Which repeated observations confirm established grammar rules?",
            "- [PENDING] Which observations are accidental implementation repetition and should be refactored?",
            "- [PENDING] Which one-off values are justified exceptions, and where are those exceptions documented?",
            "- [PENDING] Which new repeated behavior should remain provisional versus become established?",
            "- [PENDING] Did any implementation evidence contradict or retire an existing grammar rule?","",
            "## Audit status","","PENDING"]
    return "\n".join(out)+"\n"


def check(root):
    p=os.path.join(root,"IMPLEMENTATION_GRAMMAR_AUDIT.md")
    if not os.path.exists(p): print("FAIL missing IMPLEMENTATION_GRAMMAR_AUDIT.md"); return 1
    t=read(p)
    if "[PENDING]" in t: print("FAIL implementation grammar audit still contains [PENDING] decisions"); return 1
    m=re.search(r"^## Audit status\s*$\s*([^\n]+)",t,re.M|re.I)
    if not m or m.group(1).strip().upper()!="COMPLETE": print("FAIL Audit status must be COMPLETE"); return 1
    print("ok implementation grammar audit completed"); return 0


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("root",nargs="?",default="."); ap.add_argument("--check",action="store_true"); a=ap.parse_args(); root=os.path.abspath(a.root)
    if a.check: return check(root)
    path=os.path.join(root,"IMPLEMENTATION_GRAMMAR_AUDIT.md"); open(path,"w",encoding="utf-8").write(report(root)); print(path); return 0


if __name__=="__main__": sys.exit(main())
