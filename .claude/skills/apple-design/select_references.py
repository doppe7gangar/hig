#!/usr/bin/env python3
"""Select relevant Apple visual references before composing a design.

This is retrieval, not design. It turns a product brief + spatial model into a
small shortlist from apple-hig's assets index and links each visual group back
to its HIG page. The images still need to be inspected directly; filenames are
not evidence of appearance.

Examples:

    python3 select_references.py \
        --query "support analytics dashboard filters search settings" \
        --model dashboard -o REFERENCES.md

    python3 select_references.py \
        --query "plant watering iOS list add edit detail" \
        --model stack --limit 6
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


STOP = {
    "a", "an", "and", "app", "application", "are", "as", "at", "be", "build",
    "by", "design", "for", "from", "i", "in", "interface", "is", "it", "make",
    "of", "on", "or", "our", "page", "product", "screen", "the", "this", "to",
    "ui", "use", "user", "we", "web", "with",
}

# These are retrieval synonyms only. They do not assert HIG rules.
SYNONYMS = {
    "account": ["profile", "settings"],
    "add": ["buttons", "menus"],
    "analytics": ["charts", "progress indicators", "segmented controls"],
    "command": ["menus", "search fields", "buttons"],
    "dashboard": ["charts", "progress indicators", "segmented controls"],
    "date": ["pickers"],
    "delete": ["alerts", "action sheets", "menus"],
    "detail": ["navigation bars", "buttons"],
    "edit": ["buttons", "menus", "text fields"],
    "error": ["alerts", "empty states"],
    "filter": ["segmented controls", "menus", "search fields"],
    "form": ["text fields", "pickers", "buttons"],
    "list": ["lists and tables", "navigation bars"],
    "login": ["text fields", "buttons"],
    "menu": ["menus"],
    "modal": ["sheets", "alerts"],
    "navigation": ["navigation bars", "tab bars", "sidebars"],
    "notification": ["notifications", "badges"],
    "onboarding": ["page controls", "buttons"],
    "picker": ["pickers"],
    "progress": ["progress indicators"],
    "search": ["search fields"],
    "settings": ["switches", "sliders", "pickers", "lists and tables"],
    "share": ["activity view"],
    "sidebar": ["sidebars"],
    "status": ["badges", "progress indicators"],
    "tab": ["tab bars"],
    "table": ["lists and tables"],
    "toolbar": ["toolbars"],
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
    groups = []
    current = None
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
    s = 0.0
    reasons = []

    for word in base:
        if word in title.split():
            s += 4.0
            reasons.append(f'query term "{word}" matches component')
        elif re.search(rf"\b{re.escape(word)}\b", hay):
            s += 1.0

    for hint in hints:
        if hint == title:
            s += 6.0
            reasons.append(f'model/intent suggests "{group.title}"')
        elif hint in title:
            s += 4.0
            reasons.append(f'model/intent relates to "{group.title}"')
        elif hint in hay:
            s += 1.5

    # A state-rich group is more useful than a single beauty shot when tied.
    if group.files:
        state_words = sum(
            1 for f in group.files
            if re.search(r"dark|light|pressed|disabled|enabled|selected|focused|on|off", f, re.I)
        )
        s += min(state_words, 8) * 0.08

    group.score = s
    group.reasons = list(dict.fromkeys(reasons))[:3]
    return s


def representative_files(group, per_group=3):
    """Prefer a small state contrast rather than three near-identical shots."""
    if not group.files:
        return []
    picked = []
    preferences = [
        r"Light.*(?:Idle|Enabled|Default|iPhone)",
        r"Dark.*(?:Idle|Enabled|Default|iPhone)",
        r"Pressed|Selected|Focused|Disabled|On|Off",
    ]
    for pat in preferences:
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


def render(groups, query, model, limit):
    lines = [
        "# Apple reference shortlist",
        "",
        f"**Brief terms:** {query}",
        f"**Spatial model:** {model or 'not specified'}",
        "",
        "This is a retrieval shortlist, not a style prescription. Inspect the images directly before making visual claims. Extract relationships — hierarchy, grouping, state contrast, control placement, material role — rather than copying a screenshot as a template.",
        "",
        "## Selected references",
        "",
    ]
    selected = [g for g in groups if g.score > 0][:limit]
    if not selected:
        lines += [
            "No strong visual-reference match was found. Use `apple-hig/references/components.md` and `concepts.md` to identify the relevant HIG vocabulary, then rerun this selector with those terms.",
            "",
        ]
        return "\n".join(lines)

    for i, g in enumerate(selected, 1):
        lines.append(f"### {i}. {g.title}")
        lines.append("")
        if g.reasons:
            lines.append("**Why shortlisted:** " + "; ".join(g.reasons) + ".")
        if g.page:
            lines.append(f"**HIG guidance:** `apple-hig/references/pages/{g.page}`")
        if g.folder:
            lines.append(f"**Visual folder:** `apple-hig/assets/ui-kit/{g.folder}/`")
        reps = representative_files(g)
        if reps:
            lines.append("**Inspect these states:**")
            for f in reps:
                lines.append(f"- `apple-hig/assets/ui-kit/{g.folder}/{f}`")
        lines.append("")
        lines.append("Record after inspection:")
        lines.append("- hierarchy / reading order:")
        lines.append("- grouping / spacing relationship:")
        lines.append("- persistent vs contextual chrome:")
        lines.append("- state differences worth preserving:")
        lines.append("- what **not** to copy because the product context differs:")
        lines.append("")

    lines += [
        "## Synthesis before composition",
        "",
        "Before coding, write 3–5 design relationships learned from the references. Do not write adjectives like ‘clean’, ‘premium’, or ‘Apple-like’. Write relationships such as ‘selection is expressed by a quiet tint while the content remains dominant’ or ‘the toolbar is visually lighter than the work surface’. If the references disagree, prefer the one matching the target platform, task, and state.",
        "",
    ]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="Shortlist HIG + iOS UI-kit references for a design brief.")
    ap.add_argument("--query", required=True, help="product/task/component terms")
    ap.add_argument("--model", choices=sorted(MODEL_HINTS), help="chosen spatial model")
    ap.add_argument("--limit", type=int, default=6, help="component groups to shortlist")
    ap.add_argument("-o", "--out", help="write Markdown here; stdout when omitted")
    a = ap.parse_args()

    if not os.path.exists(INDEX):
        sys.exit(f"apple-hig assets index not found: {INDEX}")

    text = open(INDEX, encoding="utf-8").read()
    groups = parse_index(text)
    base, hints = expanded_terms(a.query, a.model)
    for g in groups:
        score_group(g, base, hints)
    groups.sort(key=lambda g: (-g.score, g.title.lower()))
    out = render(groups, a.query, a.model, max(1, a.limit))

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