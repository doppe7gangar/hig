#!/usr/bin/env python3
"""Select relevant Apple references before composing a design.

HIG guidance and measured visual corpora are separate authorities. The current
measured corpus is iOS 27; other Apple platforms still receive HIG guidance but
must not be presented as having measured visual evidence until their corpus is
registered here.
"""

import argparse
import os
import re
import sys
from dataclasses import dataclass, field

HERE = os.path.dirname(os.path.abspath(__file__))
SKILLS = os.path.dirname(HERE)
HIG = os.path.join(SKILLS, "apple-hig")
INDEX = os.path.join(HIG, "references", "assets-index.md")

# Visual corpora are deliberately explicit. Adding a future macOS kit should
# be a data/config change, not a redesign of the workflow.
CORPORA = {
    "ios": {
        "label": "iOS 27 measured UI-kit corpus",
        "available": True,
        "asset_prefix": "apple-hig/assets/ui-kit",
    },
    "ipados": {
        "label": "iOS/iPadOS 27 measured UI-kit corpus",
        "available": True,
        "asset_prefix": "apple-hig/assets/ui-kit",
    },
    "macos": {
        "label": "macOS measured visual corpus",
        "available": False,
        "asset_prefix": None,
    },
    "visionos": {"label": "visionOS measured visual corpus", "available": False, "asset_prefix": None},
    "watchos": {"label": "watchOS measured visual corpus", "available": False, "asset_prefix": None},
    "tvos": {"label": "tvOS measured visual corpus", "available": False, "asset_prefix": None},
    "web": {
        "label": "iOS 27 comparative visual corpus (not native web specification)",
        "available": True,
        "asset_prefix": "apple-hig/assets/ui-kit",
    },
    "marketing": {
        "label": "iOS 27 comparative visual corpus (not marketing specification)",
        "available": True,
        "asset_prefix": "apple-hig/assets/ui-kit",
    },
}

STOP = {
    "a", "an", "and", "app", "application", "are", "as", "at", "be", "build",
    "by", "design", "for", "from", "i", "in", "interface", "is", "it", "make",
    "of", "on", "or", "our", "page", "product", "screen", "the", "this", "to",
    "ui", "use", "user", "we", "web", "with",
}

SYNONYMS = {
    "account": ["profile", "settings"], "add": ["buttons", "menus"],
    "analytics": ["charts", "progress indicators", "segmented controls"],
    "command": ["menus", "search fields", "buttons"],
    "dashboard": ["charts", "progress indicators", "segmented controls"],
    "date": ["pickers"], "delete": ["alerts", "action sheets", "menus"],
    "detail": ["navigation bars", "buttons"],
    "edit": ["buttons", "menus", "text fields"], "error": ["alerts", "empty states"],
    "filter": ["segmented controls", "menus", "search fields"],
    "form": ["text fields", "pickers", "buttons"],
    "list": ["lists and tables", "navigation bars"],
    "login": ["text fields", "buttons"], "menu": ["menus"],
    "modal": ["sheets", "alerts"],
    "navigation": ["navigation bars", "tab bars", "sidebars"],
    "notification": ["notifications", "badges"],
    "onboarding": ["page controls", "buttons"], "picker": ["pickers"],
    "progress": ["progress indicators"], "search": ["search fields"],
    "settings": ["switches", "sliders", "pickers", "lists and tables"],
    "share": ["activity view"], "sidebar": ["sidebars"],
    "status": ["badges", "progress indicators"], "tab": ["tab bars"],
    "table": ["lists and tables"], "toolbar": ["toolbars"],
    "upload": ["progress indicators"],
}

MODEL_HINTS = {
    "workspace": ["sidebars", "toolbars", "menus", "search fields", "buttons"],
    "list-detail": ["lists and tables", "navigation bars", "search fields", "menus"],
    "dashboard": ["charts", "segmented controls", "progress indicators", "buttons"],
    "document": ["toolbars", "menus", "text fields", "buttons"],
    "editorial": ["buttons", "text fields"],
    "stack": ["navigation bars", "buttons", "sheets", "menus"],
    "tabs": ["tab bars", "navigation bars", "buttons"],
    "inspector": ["sidebars", "sliders", "pickers", "switches", "toolbars"],
    "command": ["search fields", "menus", "buttons"],
    "feed": ["navigation bars", "search fields", "menus"],
}


@dataclass
class Group:
    title: str
    folder: str = ""
    page: str = ""
    files: list[str] = field(default_factory=list)
    text: str = ""
    score: float = 0.0
    reasons: list[str] = field(default_factory=list)


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def tokens(s):
    return {w for w in norm(s).split() if len(w) > 1 and w not in STOP}


def parse_index(text):
    groups, current = [], None
    for line in text.splitlines():
        if line.startswith("## "):
            if current:
                groups.append(current)
            current = Group(title=line[3:].strip())
            continue
        if not current:
            continue
        current.text += " " + line
        m = re.search(r"`assets/ui-kit/([^`]+)/`", line)
        if m:
            current.folder = m.group(1)
        m = re.search(r"\(pages/([^)]+\.md)\)", line)
        if m:
            current.page = m.group(1)
        m = re.match(r"- `([^`]+\.png)`", line)
        if m:
            current.files.append(m.group(1))
    if current:
        groups.append(current)
    return groups


def expanded_terms(query, model):
    base = tokens(query)
    hints = set()
    for word in list(base):
        for phrase in SYNONYMS.get(word, []):
            hints.add(norm(phrase))
    for phrase in MODEL_HINTS.get(model or "", []):
        hints.add(norm(phrase))
    return base, hints


def score_group(group, base, hints):
    title = norm(group.title)
    hay = norm(group.title + " " + group.text)
    score, reasons = 0.0, []
    for word in base:
        if word in title.split():
            score += 4.0
            reasons.append(f'query term "{word}" matches component')
        elif re.search(rf"\b{re.escape(word)}\b", hay):
            score += 1.0
    for hint in hints:
        if hint == title:
            score += 6.0
            reasons.append(f'model/intent suggests "{group.title}"')
        elif hint in title:
            score += 4.0
            reasons.append(f'model/intent relates to "{group.title}"')
        elif hint in hay:
            score += 1.5
    if group.files:
        states = sum(1 for f in group.files if re.search(
            r"dark|light|pressed|disabled|enabled|selected|focused|on|off", f, re.I))
        score += min(states, 8) * 0.08
    group.score = score
    group.reasons = list(dict.fromkeys(reasons))[:3]
    return score


def representative_files(group, per_group=3):
    if not group.files:
        return []
    picked = []
    for pat in (r"Light.*(?:Idle|Enabled|Default|iPhone)",
                r"Dark.*(?:Idle|Enabled|Default|iPhone)",
                r"Pressed|Selected|Focused|Disabled|On|Off"):
        for f in group.files:
            if f not in picked and re.search(pat, f, re.I):
                picked.append(f)
                break
    for f in group.files:
        if len(picked) >= per_group:
            break
        if f not in picked:
            picked.append(f)
    return picked[:per_group]


def render(groups, query, model, platform, limit):
    corpus = CORPORA[platform]
    lines = [
        "# Apple reference shortlist", "",
        f"**Brief terms:** {query}",
        f"**Spatial model:** {model or 'not specified'}",
        f"**Target platform:** {platform}",
        f"**Visual corpus:** {corpus['label']}", "",
        "HIG guidance and measured visual evidence are separate. HIG remains authoritative for platform behavior and structure even when no measured visual corpus is available.", "",
        "## Selected references", "",
    ]
    if not corpus["available"]:
        lines += [
            f"**No measured {platform} visual corpus is registered.** The shortlist below is HIG/navigation vocabulary only. Do not use iOS image appearance as measured evidence for this platform.",
            "",
            "Use `apple-hig/references/platform-diffs.md`, `rules.md`, `components.md`, `framework-index.md`, and `api-map.md` for platform-specific decisions.", "",
        ]

    selected = [g for g in groups if g.score > 0][:limit]
    if not selected:
        lines += ["No strong match was found. Use `apple-hig/references/components.md` and `concepts.md` to identify HIG vocabulary, then rerun.", ""]
        return "\n".join(lines)

    for i, g in enumerate(selected, 1):
        lines += [f"### {i}. {g.title}", ""]
        if g.reasons:
            lines.append("**Why shortlisted:** " + "; ".join(g.reasons) + ".")
        if g.page:
            lines.append(f"**HIG guidance:** `apple-hig/references/pages/{g.page}`")
        if corpus["available"] and g.folder:
            prefix = corpus["asset_prefix"]
            lines.append(f"**Visual folder:** `{prefix}/{g.folder}/`")
            reps = representative_files(g)
            if reps:
                lines.append("**Inspect these visual states:**")
                for f in reps:
                    lines.append(f"- `{prefix}/{g.folder}/{f}`")
        elif g.folder:
            lines.append("**Visual evidence:** unavailable for the target platform; do not substitute the iOS rendering as measured appearance.")
        lines += ["", "Record after inspection/research:",
                  "- hierarchy / reading order:",
                  "- grouping / spacing relationship:",
                  "- persistent vs contextual chrome:",
                  "- applicable interaction-state relationship:",
                  "- what must **not** transfer because platform/product context differs:", ""]

    lines += ["## Synthesis before composition", "",
              "Write 3–5 concrete relationships. Avoid adjectives like ‘clean’, ‘premium’, or ‘Apple-like’. When evidence conflicts, prefer the target platform, task, and state. A future platform corpus should plug into `CORPORA` without changing this decision process.", ""]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="Shortlist HIG guidance + available measured visual references.")
    ap.add_argument("--query", required=True, help="product/task/component terms")
    ap.add_argument("--model", choices=sorted(MODEL_HINTS), help="leading spatial model")
    ap.add_argument("--platform", choices=sorted(CORPORA), default="ios",
                    help="target platform; controls whether measured visual evidence is valid")
    ap.add_argument("--limit", type=int, default=6)
    ap.add_argument("-o", "--out")
    a = ap.parse_args()

    if not os.path.exists(INDEX):
        sys.exit(f"apple-hig assets index not found: {INDEX}")
    groups = parse_index(open(INDEX, encoding="utf-8").read())
    base, hints = expanded_terms(a.query, a.model)
    for g in groups:
        score_group(g, base, hints)
    groups.sort(key=lambda g: (-g.score, g.title.lower()))
    out = render(groups, a.query, a.model, a.platform, max(1, a.limit))
    if a.out:
        os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(out + "\n")
        print(a.out)
    else:
        print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())