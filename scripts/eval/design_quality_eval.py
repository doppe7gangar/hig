#!/usr/bin/env python3
"""Run diverse product briefs and flag structural sameness/regressions.

Requires the local `claude` CLI. Mechanical and direction gates are run on each
produced design. The cross-run summary looks for repeated architecture; it does
not pretend to score beauty.
"""

import argparse
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
        shutil.copytree(os.path.join(SKILLS, name), os.path.join(dst, name),
                        ignore=shutil.ignore_patterns("__pycache__"))


def find_design(root):
    candidates = []
    for dp, dns, files in os.walk(root):
        dns[:] = [d for d in dns if d not in (".claude", "vendor", "node_modules")]
        if "DESIGN.md" in files and any(f.endswith(".html") for f in files):
            candidates.append(dp)
    return min(candidates, key=len) if candidates else None


def extract_direction(path):
    text = open(os.path.join(path, "DESIGN.md"), encoding="utf-8").read()
    def section(name):
        m = re.search(rf"^#+\s+{re.escape(name)}\s*$([\s\S]*?)(?=^#+\s|\Z)",
                      text, re.I | re.M)
        return m.group(1).strip() if m else ""
    chosen = section("Chosen direction") or section("Spatial model")
    inv = section("Design invariants")
    return {
        "chosen": re.sub(r"\s+", " ", chosen)[:240],
        "invariants": len(re.findall(r"^\s*[-*]\s+", inv, re.M)),
    }


def structural_metrics(path):
    htmls = []
    for dp, dns, files in os.walk(path):
        dns[:] = [d for d in dns if d not in ("vendor", "node_modules")]
        for f in files:
            if f.endswith(".html"):
                htmls.append(open(os.path.join(dp, f), encoding="utf-8").read())
    text = "\n".join(htmls)
    return {
        "cards": len(re.findall(r'class="[^"]*\bcard\b', text, re.I)),
        "asides": len(re.findall(r"<aside\b", text, re.I)),
        "navs": len(re.findall(r"<nav\b", text, re.I)),
        "tables": len(re.findall(r"<table\b", text, re.I)),
        "tabbars": len(re.findall(r"tabbar|tab-bar", text, re.I)),
    }


def run_one(name, brief, workroot, model):
    root = os.path.join(workroot, name)
    shutil.rmtree(root, ignore_errors=True)
    os.makedirs(root, exist_ok=True)
    install_skills(root)
    env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
    p = subprocess.run([
        "claude", "-p", brief, "--model", model,
        "--permission-mode", "acceptEdits",
        "--allowedTools", "Bash,Read,Write,Edit,Glob,Grep,Skill,WebFetch",
    ], cwd=root, env=env, capture_output=True, text=True, timeout=2400)
    design = find_design(root)
    result = {"id": name, "returncode": p.returncode, "design": design}
    if not design:
        result["failure"] = "no design directory with DESIGN.md + HTML"
        return result
    mec = subprocess.run([sys.executable, CHECK, design, "--no-browser"],
                         capture_output=True, text=True, timeout=300)
    direction = subprocess.run([sys.executable, DIRECTION, design],
                               capture_output=True, text=True, timeout=60)
    result.update({
        "mechanical": mec.returncode,
        "direction_gate": direction.returncode,
        "direction": extract_direction(design),
        "metrics": structural_metrics(design),
    })
    return result


def summarize(results):
    warnings = []
    chosen = [r.get("direction", {}).get("chosen", "") for r in results]
    prefixes = {}
    for c in chosen:
        key = c.lower()[:80]
        if key:
            prefixes[key] = prefixes.get(key, 0) + 1
    for key, n in prefixes.items():
        if n >= max(3, int(len(results) * .6)):
            warnings.append(f"chosen-direction wording/structure repeats in {n}/{len(results)} runs: {key}")

    card_heavy = [r["id"] for r in results if r.get("metrics", {}).get("cards", 0) >= 6]
    if len(card_heavy) >= max(4, int(len(results) * .5)):
        warnings.append("many unrelated products are card-heavy: " + ", ".join(card_heavy))

    missing_direction = [r["id"] for r in results if r.get("direction_gate") not in (0,)]
    if missing_direction:
        warnings.append("direction evidence gate failed: " + ", ".join(missing_direction))

    return warnings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*", help="benchmark IDs; default all")
    ap.add_argument("--model", default="claude-opus-5")
    ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "quality-work"))
    args = ap.parse_args()
    ids = args.ids or list(BRIEFS)
    os.makedirs(args.out, exist_ok=True)
    results = []
    for name in ids:
        if name not in BRIEFS:
            print(f"unknown benchmark: {name}", file=sys.stderr)
            return 2
        print(f"running {name}...", flush=True)
        results.append(run_one(name, BRIEFS[name], args.out, args.model))

    print(json.dumps(results, indent=2))
    warnings = summarize(results)
    print("\nCross-run regression review:")
    if warnings:
        for w in warnings:
            print("WARN " + w)
    else:
        print("ok no obvious structural-sameness regression detected")

    hard = [r for r in results if r.get("mechanical") not in (0,) or r.get("direction_gate") not in (0,)]
    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main())