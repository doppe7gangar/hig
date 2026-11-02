#!/usr/bin/env python3
"""Run diverse product briefs and flag design-system regressions.

Requires the local `claude` CLI. Mechanical, direction, divergence, content,
interaction, and cross-screen coherence gates run on each produced design.
Cross-run analysis looks for architectural collapse without scoring beauty.
"""

import argparse
import collections
import json
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SKILLS = os.path.join(ROOT, ".claude", "skills")
CHECK = os.path.join(SKILLS, "apple-design", "check_design.py")
DIRECTION = os.path.join(SKILLS, "apple-design", "check_direction.py")
DIVERGENCE = os.path.join(SKILLS, "apple-design", "check_divergence.py")
CONTENT = os.path.join(SKILLS, "apple-design", "check_content.py")
INTERACTION = os.path.join(SKILLS, "apple-design", "check_interaction.py")
COHERENCE = os.path.join(SKILLS, "apple-design", "check_coherence.py")

BRIEFS = {
    "analytics": "Design a desktop-first web support analytics product: ticket volume, SLA health, response time, staffing. Brand #1F6FEB. Apple sensibility without iOS chrome.",
    "mail": "Design a macOS mail client for heavy daily use. Inbox, folders, search, message reading/composing. Follow macOS HIG and prefer native patterns.",
    "photo": "Design a macOS photo editor with library browsing, large editing canvas, adjustment controls, export, and keyboard-heavy professional use. Follow macOS HIG.",
    "finance": "Design an iOS personal finance overview for spending, upcoming bills and monthly health. Avoid generic metric-card dashboards. Brand #4E6AF3.",
    "plants": "Design an iOS plant-watering tracker with upcoming care, plant detail and history. Brand #4C8C3F.",
    "notes": "Design an iPadOS research-notes product with notebooks, notes, backlinks and writing. Use the width intelligently and follow HIG.",
    "devtool": "Design a desktop web API debugging tool: request editor, environments, response inspector, history and keyboard commands. Brand #6E56CF.",
    "settings": "Design a macOS configuration utility with several categories and advanced options. Follow macOS HIG; do not make it look like an iPhone Settings screen.",
    "media": "Design an iOS/iPadOS music listening experience where album artwork and playback own the screen and controls recede appropriately.",
    "commerce": "Design a responsive web shop for browsing a catalog and studying one product in detail. Apple-like restraint, normal web behavior.",
    "landing": "Design a marketing landing page for a B2B time-tracking product. Brand #0F7B4F. Editorial narrative, not feature-card wallpaper.",
    "operations": "Design a desktop web incident-monitoring product for a security operations team: current incidents, severity, site status, response evidence. Dense but calm.",
    "messaging": "Design a desktop team messaging web app with workspaces/channels, conversation, threads, search and compose. Avoid generic SaaS cards.",
    "calendar": "Design an iPadOS scheduling product with day/week context, event detail and creation. Follow HIG and adapt across iPad widths.",
    "files": "Design a macOS file manager for power users: locations, files, preview, multi-selection, context menus and keyboard shortcuts. Follow macOS HIG.",
}


def install_skills(root):
    dst = os.path.join(root, ".claude", "skills")
    os.makedirs(dst, exist_ok=True)
    for name in ("apple-hig", "apple-ui-kit", "apple-motion", "apple-design"):
        shutil.copytree(os.path.join(SKILLS, name), os.path.join(dst, name), ignore=shutil.ignore_patterns("__pycache__"))


def find_design(root):
    candidates = []
    for dp, dns, files in os.walk(root):
        dns[:] = [d for d in dns if d not in (".claude", "vendor", "node_modules")]
        if "DESIGN.md" in files and any(f.endswith(".html") for f in files):
            candidates.append(dp)
    return min(candidates, key=len) if candidates else None


def section(text, name):
    m = re.search(rf"^#+\s+{re.escape(name)}\s*$([\s\S]*?)(?=^#+\s|\Z)", text, re.I | re.M)
    return m.group(1).strip() if m else ""


def extract_direction(path):
    text = open(os.path.join(path, "DESIGN.md"), encoding="utf-8").read()
    chosen = section(text, "Chosen direction") or section(text, "Spatial model")
    inv = section(text, "Design invariants")
    candidates = section(text, "Candidate directions")
    candidate_count = len(re.findall(r"^###\s+Direction", candidates, re.I | re.M))
    return {
        "chosen": re.sub(r"\s+", " ", chosen)[:320],
        "invariants": len(re.findall(r"^\s*[-*]\s+", inv, re.M)),
        "candidate_count": candidate_count,
        "content_model_chars": len(section(text, "Content model")),
        "representation_chars": len(section(text, "Representation decisions")),
        "interaction_chars": len(section(text, "Primary interaction flow")),
        "coherence_chars": len(section(text, "Product coherence contract")),
        "transition_chars": len(section(text, "Cross-screen transition audit")),
    }


def read_html(path):
    htmls = []
    for dp, dns, files in os.walk(path):
        dns[:] = [d for d in dns if d not in ("vendor", "node_modules")]
        for filename in files:
            if filename.endswith(".html"):
                htmls.append(open(os.path.join(dp, filename), encoding="utf-8").read())
    return "\n".join(htmls)


def infer_model(text):
    probes = [("workspace", r"\bworkspace(?:__|\b)"), ("list-detail", r"\blistdetail\b|\bcollection__item\b"),
              ("dashboard", r"\bhero-metric\b|\bsummary__head\b"), ("document", r"\bdocument-shell\b|\bdocument-top\b"),
              ("editorial", r"\bmarketing\b|\bmkt-page\b"), ("ios-tabs", r"ios-tabbar"), ("ios-stack", r'class="phone"')]
    for name, pattern in probes:
        if re.search(pattern, text, re.I): return name
    return "custom/unknown"


def structural_metrics(path):
    text = read_html(path)
    metrics = {"model": infer_model(text), "cards": len(re.findall(r'class="[^"]*\bcard\b', text, re.I)),
               "asides": len(re.findall(r"<aside\b", text, re.I)), "navs": len(re.findall(r"<nav\b", text, re.I)),
               "tables": len(re.findall(r"<table\b", text, re.I)), "forms": len(re.findall(r"<form\b", text, re.I)),
               "tabbars": len(re.findall(r"tabbar|tab-bar", text, re.I)),
               "split_regions": len(re.findall(r"grid-template-columns|split|pane|inspector", text, re.I))}
    def bucket(n): return "0" if n == 0 else "1-2" if n <= 2 else "3-5" if n <= 5 else "6+"
    metrics["signature"] = "/".join([metrics["model"], "a"+bucket(metrics["asides"]), "n"+bucket(metrics["navs"]),
                                      "t"+bucket(metrics["tables"]), "f"+bucket(metrics["forms"]),
                                      "s"+bucket(metrics["split_regions"]), "c"+bucket(metrics["cards"])])
    return metrics


def run_gate(script, design, timeout=60, extra=None):
    args = [sys.executable, script, design] + (extra or [])
    return subprocess.run(args, capture_output=True, text=True, timeout=timeout)


def run_one(name, brief, workroot, model):
    root = os.path.join(workroot, name); shutil.rmtree(root, ignore_errors=True); os.makedirs(root, exist_ok=True); install_skills(root)
    env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
    p = subprocess.run(["claude", "-p", brief, "--model", model, "--permission-mode", "acceptEdits",
                        "--allowedTools", "Bash,Read,Write,Edit,Glob,Grep,Skill,WebFetch"], cwd=root, env=env,
                       capture_output=True, text=True, timeout=2400)
    design = find_design(root); result = {"id": name, "returncode": p.returncode, "design": design}
    if not design: result["failure"] = "no design directory with DESIGN.md + HTML"; return result
    gates = {"mechanical": run_gate(CHECK, design, 300, ["--no-browser"]), "direction_gate": run_gate(DIRECTION, design),
             "divergence_gate": run_gate(DIVERGENCE, design), "content_gate": run_gate(CONTENT, design),
             "interaction_gate": run_gate(INTERACTION, design), "coherence_gate": run_gate(COHERENCE, design)}
    result.update({k: v.returncode for k, v in gates.items()})
    result.update({"direction": extract_direction(design), "metrics": structural_metrics(design),
                   "gate_output": {k: v.stdout.strip() for k, v in gates.items() if k != "mechanical"}})
    return result


def repeated(counter, total, minimum=3, fraction=.6):
    threshold = max(minimum, int(total * fraction + .999)); return [(k,n) for k,n in counter.items() if k and n >= threshold]


def summarize(results):
    warnings=[]; usable=[r for r in results if r.get("metrics")]; total=len(usable)
    if not total: return ["no usable generated designs to compare"]
    prefixes=collections.Counter(r.get("direction",{}).get("chosen","").lower()[:90] for r in usable)
    for k,n in repeated(prefixes,total): warnings.append(f"chosen-direction wording/structure repeats in {n}/{total} runs: {k}")
    models=collections.Counter(r["metrics"]["model"] for r in usable)
    for m,n in repeated(models,total,4,.6): warnings.append(f"spatial-model collapse: {m} appears in {n}/{total} unrelated products")
    sigs=collections.Counter(r["metrics"]["signature"] for r in usable)
    for s,n in repeated(sigs,total,3,.4): warnings.append(f"near-identical structural signature repeats in {n}/{total}: {s}")
    for key,label in (("direction_gate","direction"),("divergence_gate","divergence"),("content_gate","content"),
                      ("interaction_gate","interaction"),("coherence_gate","coherence")):
        failed=[r["id"] for r in usable if r.get(key)!=0]
        if failed: warnings.append(f"{label} evidence gate failed: "+", ".join(failed))
    thin=[r["id"] for r in usable if r.get("direction",{}).get("coherence_chars",0)<180 or r.get("direction",{}).get("transition_chars",0)<100]
    if thin: warnings.append("cross-screen coherence/transition evidence suspiciously thin: "+", ".join(thin))
    card_heavy=[r["id"] for r in usable if r["metrics"].get("cards",0)>=6]
    if len(card_heavy)>=max(4,int(total*.5+.999)): warnings.append("many unrelated products are card-heavy: "+", ".join(card_heavy))
    mac_ids={"mail","photo","settings","files"}; mobile=[r["id"] for r in usable if r["id"] in mac_ids and (r["metrics"]["model"] in ("ios-tabs","ios-stack") or r["metrics"]["tabbars"])]
    if mobile: warnings.append("macOS benchmark emitted mobile-style navigation: "+", ".join(mobile))
    return warnings


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("ids",nargs="*"); ap.add_argument("--model",default="claude-opus-5"); ap.add_argument("--out",default=os.path.join(os.path.dirname(__file__),"quality-work")); args=ap.parse_args()
    ids=args.ids or list(BRIEFS); os.makedirs(args.out,exist_ok=True); results=[]
    for name in ids:
        if name not in BRIEFS: print(f"unknown benchmark: {name}",file=sys.stderr); return 2
        print(f"running {name}...",flush=True); results.append(run_one(name,BRIEFS[name],args.out,args.model))
    print(json.dumps(results,indent=2)); warnings=summarize(results); print("\nCross-run regression review:")
    for w in warnings: print("WARN "+w)
    if not warnings: print("ok no obvious structural/content/interaction/coherence regression detected")
    hard=[r for r in results if any(r.get(k)!=0 for k in ("mechanical","direction_gate","divergence_gate","content_gate","interaction_gate","coherence_gate"))]
    return 1 if hard else 0


if __name__ == "__main__": sys.exit(main())
