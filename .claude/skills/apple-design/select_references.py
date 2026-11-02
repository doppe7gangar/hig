#!/usr/bin/env python3
"""Select relevant Apple references before composing a design.

HIG guidance and measured visual evidence are separate authorities. The
guidance is Apple's page, read on Apple's site: topics.md lists every page
with its official address and platforms. The visual evidence is the kit's
own recipes, measured from Apple's design kits for iOS/iPadOS 27 and macOS
27; other Apple platforms get the guidance only and must not be presented
as having measured visual evidence until a kit is registered here.
"""

import argparse
import os
import re
import sys
from dataclasses import dataclass, field

HERE = os.path.dirname(os.path.abspath(__file__))
SKILLS = os.path.dirname(HERE)
HIG = os.path.join(SKILLS, "apple-hig")
INDEX = os.path.join(HIG, "references", "topics.md")
KIT = "apple-ui-kit"

# Visual corpora are deliberately explicit. Adding a future macOS kit should
# be a data/config change, not a redesign of the workflow.
CORPORA = {
    "ios": {"label": "iOS 27 measured kit (apple-ui-kit)", "available": True,
            "evidence": ["ios-screens.html", "example.html"]},
    "ipados": {"label": "iPadOS 27 measured kit (apple-ui-kit)", "available": True,
               "evidence": ["ipad-example.html", "ios-screens.html"]},
    "macos": {"label": "macOS 27 measured kit (apple-ui-kit)", "available": True,
              "evidence": ["mac-example.html"]},
    "visionos": {"label": "visionOS measured kit", "available": False, "evidence": []},
    "watchos": {"label": "watchOS measured kit", "available": False, "evidence": []},
    "tvos": {"label": "tvOS measured kit", "available": False, "evidence": []},
    "web": {"label": "iOS 27 measured kit, comparative (not a web specification)", "available": True,
            "evidence": ["ios-screens.html", "example.html"]},
    "marketing": {"label": "iOS 27 measured kit, comparative (not a marketing specification)",
                  "available": True, "evidence": ["ios-screens.html"]},
}

# Which kit recipe draws each HIG topic, per platform family. A topic with
# no entry has guidance but no measured recipe yet.
RECIPES = {
    "Tab bars": {"ios": ".ios-tabbar", "ipados": ".ipad-tabbar", "macos": ".mac-tabs"},
    "Toggles": {"ios": ".ios-switch", "ipados": ".ios-switch", "macos": ".mac-switch"},
    "Lists and tables": {"ios": ".ios-list", "ipados": ".ios-list", "macos": ".mac-table"},
    "Sheets": {"ios": ".ios-sheet", "ipados": ".ipad-sheet", "macos": ".mac-sheet"},
    "Alerts": {"ios": ".ios-alert", "ipados": ".ios-alert", "macos": ".mac-alert"},
    "Action sheets": {"ios": ".ios-actionsheet", "ipados": ".ios-actionsheet"},
    "Sidebars": {"ipados": ".ipad-sidebar", "macos": ".mac-sidebar"},
    "Split views": {"ipados": ".ipad-split", "macos": ".mac-window"},
    "Toolbars": {"ios": ".ios-navbar", "ipados": ".ipad-toolbar", "macos": ".mac-toolbar"},
    "Search fields": {"ios": ".ios-field", "ipados": ".ipad-search", "macos": ".mac-search"},
    "Text fields": {"ios": ".ios-field", "ipados": ".ios-field", "macos": ".mac-field"},
    "Segmented controls": {"ios": ".ios-segmented", "ipados": ".ios-segmented", "macos": ".mac-segmented"},
    "Sliders": {"ios": ".ios-slider", "ipados": ".ios-slider"},
    "Steppers": {"ios": ".ios-stepper", "ipados": ".ios-stepper"},
    "Buttons": {"ios": ".ios-btn", "ipados": ".ios-btn", "macos": ".mac-btn"},
    "Popovers": {"ipados": ".ipad-popover", "macos": ".mac-popover"},
    "Pop-up buttons": {"ios": ".ios-popup", "ipados": ".ios-popup", "macos": ".mac-popup"},
    "Menus": {"macos": ".mac-menu"},
    "Page controls": {"ios": ".ios-pagecontrol", "ipados": ".ios-pagecontrol"},
    "Progress indicators": {"macos": ".mac-progress"},
    "Windows": {"macos": ".mac-window"},
    "Pickers": {"ios": ".ios-pill", "ipados": ".ios-pill"},
    "Writing": {"ios": ".ios-empty", "ipados": ".ios-empty", "macos": ".mac-empty"},
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
    "detail": ["toolbars", "buttons"],
    "edit": ["buttons", "menus", "text fields"], "error": ["alerts", "writing"],
    "filter": ["segmented controls", "menus", "search fields"],
    "form": ["text fields", "pickers", "buttons"],
    "list": ["lists and tables", "toolbars"],
    "login": ["text fields", "buttons"], "menu": ["menus"],
    "modal": ["sheets", "alerts"],
    "navigation": ["toolbars", "tab bars", "sidebars"],
    "notification": ["notifications", "notifications"],
    "onboarding": ["page controls", "buttons"], "picker": ["pickers"],
    "progress": ["progress indicators"], "search": ["search fields"],
    "settings": ["toggles", "sliders", "pickers", "lists and tables"],
    "share": ["activity views"], "sidebar": ["sidebars"],
    "status": ["notifications", "progress indicators"], "tab": ["tab bars"],
    "table": ["lists and tables"], "toolbar": ["toolbars"],
    "upload": ["progress indicators"],
}

MODEL_HINTS = {
    "workspace": ["sidebars", "toolbars", "menus", "search fields", "buttons"],
    "list-detail": ["lists and tables", "toolbars", "search fields", "menus"],
    "dashboard": ["charts", "segmented controls", "progress indicators", "buttons"],
    "document": ["toolbars", "menus", "text fields", "buttons"],
    "editorial": ["buttons", "text fields"],
    "stack": ["toolbars", "buttons", "sheets", "menus"],
    "tabs": ["tab bars", "toolbars", "buttons"],
    "inspector": ["sidebars", "sliders", "pickers", "toggles", "toolbars"],
    "command": ["search fields", "menus", "buttons"],
    "feed": ["toolbars", "search fields", "menus"],
}


@dataclass
class Group:
    title: str
    url: str = ""
    platforms: str = ""
    score: float = 0.0
    reasons: list[str] = field(default_factory=list)

    @property
    def text(self):
        return self.platforms


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def tokens(s):
    return {w for w in norm(s).split() if len(w) > 1 and w not in STOP}


def parse_index(text):
    """topics.md rows: | Title | [slug](official address) | platforms |"""
    groups = []
    for m in re.finditer(r"^\| ([^|]+?) \| \[[^\]]+\]\((https://[^)]+)\) \| ([^|]*)\|$", text, re.M):
        groups.append(Group(title=m.group(1).strip(), url=m.group(2), platforms=m.group(3).strip()))
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
    group.score = score
    group.reasons = list(dict.fromkeys(reasons))[:3]
    return score


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
    family = "macos" if platform == "macos" else "ipados" if platform == "ipados" else "ios"
    if not corpus["available"]:
        lines += [
            f"**No measured {platform} kit is registered.** The shortlist below is HIG vocabulary only. Do not use iOS recipes as measured evidence for this platform.",
            "",
            "Read each page's platform section on Apple's site, and use `apple-hig/references/numbers.md`, `framework-index.md` and `api-map.md` for platform-specific decisions.", "",
        ]

    selected = [g for g in groups if g.score > 0][:limit]
    if not selected:
        lines += ["No strong match was found. Use `apple-hig/references/topics.md` and `concepts.md` to identify HIG vocabulary, then rerun.", ""]
        return "\n".join(lines)

    for i, g in enumerate(selected, 1):
        lines += [f"### {i}. {g.title}", ""]
        if g.reasons:
            lines.append("**Why shortlisted:** " + "; ".join(g.reasons) + ".")
        lines.append(f"**HIG guidance:** [{g.title}]({g.url}) — read it on Apple's site"
                     + (f" ({g.platforms})" if g.platforms else ""))
        recipe = RECIPES.get(g.title, {}).get(family)
        if corpus["available"] and recipe:
            files = ", ".join(f"`{KIT}/{f}`" for f in corpus["evidence"])
            lines.append(f"**Measured recipe:** `{recipe}`, drawn in {files}")
        elif recipe:
            lines.append("**Visual evidence:** unavailable for the target platform; do not substitute the iOS recipe as measured appearance.")
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
        sys.exit(f"apple-hig topic index not found: {INDEX}")
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