#!/usr/bin/env python3
"""Build a task-oriented HIG skill from the scraped corpus.

Shipping the corpus with an index on top answers "what does Apple say about
X" if you already know to ask about X -- a search tool, not a skill. Apple's
pages have exploitable structure that turns into actual working references
instead: every guideline is a bolded imperative with rationale, every hard
number sits in a table, every page opens with a one-line purpose statement,
and 147 pages list the exact API that implements the guidance. All four
extract mechanically:

  rules.md          every guideline as a one-line imperative, grouped by
                    topic and tagged with the platform it applies to.
                    Greppable as a review checklist.
  specs.md          every table and measurement in the corpus, with source,
                    so "what size / what ratio" is one lookup.
  platform-diffs.md what actually changes per platform, by topic.
  api-map.md        HIG concept -> exact SwiftUI/UIKit/AppKit/etc symbol,
                    so guidance connects to the code that implements it.
  components.md      one-line purpose for every page -- the fastest way to
                    find the right component before reading anything else.
  pages/            the full prose, for when the rule needs its rationale.
"""

import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
CONTENT = os.path.join(REPO, "content")
OUT = os.path.join(REPO, ".claude", "skills", "apple-hig")
REFS = os.path.join(OUT, "references")

PLATFORMS = ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]


def title_of(text):
    return text.lstrip().split("\n", 1)[0].lstrip("# ").strip()


def sections(text):
    """Yield (heading_path, body) so a rule can be tagged with its platform."""
    cur_h2, cur_h3 = None, None
    buf = []
    for line in text.split("\n"):
        if line.startswith("## "):
            if buf:
                yield (cur_h2, cur_h3), "\n".join(buf)
            cur_h2, cur_h3, buf = line[3:].strip(), None, []
        elif line.startswith("### "):
            if buf:
                yield (cur_h2, cur_h3), "\n".join(buf)
            cur_h3, buf = line[4:].strip(), []
        else:
            buf.append(line)
    if buf:
        yield (cur_h2, cur_h3), "\n".join(buf)


def platform_tag(h2, h3):
    if h2 and "Platform considerations" in h2 and h3:
        found = [p for p in PLATFORMS if re.search(rf"\b{re.escape(p)}\b", h3)]
        if found:
            return found
    return []


RULE_RE = re.compile(r"^\*\*(.+?)\*\*\s*(.*)$")


def extract_rules():
    by_page = {}
    total = 0
    for fn in sorted(os.listdir(CONTENT)):
        if not fn.endswith(".md"):
            continue
        text = open(os.path.join(CONTENT, fn), encoding="utf-8").read()
        page = title_of(text)
        rows = []
        for (h2, h3), body in sections(text):
            plats = platform_tag(h2, h3)
            for line in body.split("\n"):
                m = RULE_RE.match(line.strip())
                if not m:
                    continue
                rule = " ".join(m.group(1).split())
                if len(rule) < 12 or not re.search(r"[a-z]", rule):
                    continue
                why = " ".join(m.group(2).split())
                if len(why) > 240:
                    why = why[:237].rsplit(" ", 1)[0] + "..."
                rows.append((rule, why, plats))
                total += 1
        if rows:
            by_page[(page, fn[:-3])] = rows
    return by_page, total


def write_rules(by_page, total):
    out = [
        "# Every HIG rule, as a checklist",
        "",
        f"{total} guidelines, one line each, grouped by topic. Apple states each "
        "as a bolded imperative followed by its reasoning; the imperative is the "
        "rule, the rest is why.",
        "",
        "`[iOS]`-style tags mark rules that apply only to those platforms. An "
        "untagged rule applies everywhere.",
        "",
        "Grep this file to review something against the guidelines without "
        "reading 178 pages — `grep -A1 -i 'button' rules.md` gets you every "
        "button rule. Open `pages/<slug>.md` when a rule's rationale matters.",
        "",
        "---",
        "",
    ]
    for (page, slug), rows in sorted(by_page.items()):
        out.append(f"## {page}")
        out.append(f"<sub>`pages/{slug}.md`</sub>")
        out.append("")
        for rule, why, plats in rows:
            tag = f" `[{', '.join(plats)}]`" if plats else ""
            out.append(f"- **{rule}**{tag}")
            if why:
                out.append(f"  {why}")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


TABLE_RE = re.compile(r"(?:^\|.*\|\s*$\n?)+", re.M)
NUM_RE = re.compile(r"\b\d+(?:\.\d+)?\s?(?:x\s?\d+(?:\.\d+)?)?\s?(?:pt|px|points|pixels)\b|\b\d+(?:\.\d+)?:1\b|\b\d+\s?(?:percent|%)")


def extract_specs():
    out = [
        "# Specs: every concrete number in the HIG",
        "",
        "Sizes, ratios, and limits pulled from the corpus, with the page each "
        "came from. Apple keeps these in tables scattered across 178 pages; this "
        "is all of them in one place.",
        "",
        "Numbers are in points unless marked px. When a value differs by "
        "platform the source table says so — don't quote one row as if it were "
        "universal.",
        "",
        "---",
        "",
    ]
    for fn in sorted(os.listdir(CONTENT)):
        if not fn.endswith(".md"):
            continue
        text = open(os.path.join(CONTENT, fn), encoding="utf-8").read()
        page, slug = title_of(text), fn[:-3]
        chunks = []

        for (h2, h3), body in sections(text):
            where = " → ".join(x for x in (h2, h3) if x)
            for tbl in TABLE_RE.findall(body):
                if NUM_RE.search(tbl):
                    chunks.append((where, tbl.strip()))
            for line in body.split("\n"):
                s = line.strip()
                if not s or s.startswith("|") or s.startswith("!["):
                    continue
                if NUM_RE.search(s) and len(s) < 400:
                    s = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", s).strip()
                    if s:
                        chunks.append((where, " ".join(s.split())))
        if chunks:
            out.append(f"## {page}")
            out.append(f"<sub>`pages/{slug}.md`</sub>")
            out.append("")
            seen = set()
            for where, chunk in chunks:
                if chunk in seen:
                    continue
                seen.add(chunk)
                if where:
                    out.append(f"*{where}*")
                out.append(chunk if chunk.startswith("|") else f"- {chunk}")
                out.append("")
    return "\n".join(out).rstrip() + "\n"


def extract_platform_diffs():
    per = {p: [] for p in PLATFORMS}
    for fn in sorted(os.listdir(CONTENT)):
        if not fn.endswith(".md"):
            continue
        text = open(os.path.join(CONTENT, fn), encoding="utf-8").read()
        page, slug = title_of(text), fn[:-3]
        for (h2, h3), body in sections(text):
            plats = platform_tag(h2, h3)
            body = body.strip()
            if not plats or not body:
                continue
            for p in plats:
                per[p].append((page, slug, h3, body))

    out = [
        "# What changes per platform",
        "",
        "The HIG documents a component once and lists its platform exceptions "
        "in a 'Platform considerations' section. Those exceptions are collected "
        "here, by platform, so adapting a design to another Apple platform is "
        "one lookup rather than 178.",
        "",
        "A topic absent from a platform's section means the HIG states no "
        "exception for it — the general rule applies. That's a real answer, not "
        "a gap.",
        "",
        "---",
        "",
    ]
    for p in PLATFORMS:
        entries = per[p]
        out.append(f"## {p}")
        out.append("")
        if not entries:
            out.append("*No platform-specific guidance in the corpus.*")
            out.append("")
            continue
        for page, slug, h3, body in sorted(entries):
            out.append(f"### {page}")
            out.append(f"<sub>`pages/{slug}.md`" + (f" — upstream heading: {h3}" if h3 != p else "") + "</sub>")
            out.append("")
            out.append(body)
            out.append("")
    return "\n".join(out).rstrip() + "\n"


# The URL group must be greedy: Swift symbol URLs embed parentheses
# (.../View/sheet(item:onDismiss:content:)), so a lazy [^)]+ stops at the
# first inner ')' and drops the line entirely. That silently lost 14
# symbols -- disproportionately the SwiftUI modifiers most worth having
# (confirmationDialog, alert(_:isPresented:actions:), fullScreenCover).
# Greedy .+ backtracks to the final ') — ', which is the real delimiter.
DEVDOC_RE = re.compile(r"^\[([^\]]+)\]\((.+)\)\s*—\s*(.+)$")
# A plain link with no framework suffix -- the target is itself a
# framework or a guide.
BARE_LINK_RE = re.compile(r"^\[([^\]]+)\]\((.+)\)\s*$")


def extract_api_map():
    """HIG concept -> exact API symbol, from each page's Developer documentation section."""
    by_page = {}
    by_framework = {}
    total = 0
    for fn in sorted(os.listdir(CONTENT)):
        if not fn.endswith(".md"):
            continue
        text = open(os.path.join(CONTENT, fn), encoding="utf-8").read()
        page, slug = title_of(text), fn[:-3]
        if "#### Developer documentation" not in text:
            continue
        section_text = text.split("#### Developer documentation", 1)[1]
        section_text = re.split(r"\n#### |\n## ", section_text, 1)[0]
        rows = []
        for line in section_text.split("\n"):
            s = line.strip()
            m = DEVDOC_RE.match(s)
            if m:
                symbol, url, framework = m.group(1), m.group(2), m.group(3).strip()
                rows.append((symbol, url, framework))
                by_framework.setdefault(framework, []).append((symbol, url, page, slug))
                total += 1
                continue
            # Entries without a "— Framework" suffix: the link IS the
            # framework or a guide (AVFoundation, App Intents, "Building
            # accessible apps"). 99 of these -- 29% of the section's links --
            # were being dropped, so "what framework handles AirPlay?" was
            # unanswerable from api-map despite sitting in the corpus.
            m2 = BARE_LINK_RE.match(s)
            if m2:
                name, url = m2.group(1), m2.group(2)
                rows.append((name, url, None))
                total += 1
        if rows:
            by_page[(page, slug)] = rows

    out = [
        "# API map: guidance to implementation",
        "",
        f"{total} references pulled from every page's 'Developer "
        "documentation' section: the exact SwiftUI, UIKit, AppKit, and "
        "framework-specific API that implements each piece of guidance, "
        "plus the frameworks and guides a page points to. Entries marked "
        "framework/guide are the framework itself (AVFoundation, App "
        "Intents) or an Apple how-to, not a single symbol.",
        "",
        "Use this to go from a design decision straight to the right API "
        "instead of guessing at a class or modifier name. When reviewing code, "
        "check the symbol used against what the HIG actually names here — a "
        "hand-rolled view where a system API exists is itself worth flagging.",
        "",
        "---",
        "",
        "## By component",
        "",
    ]
    for (page, slug), rows in sorted(by_page.items()):
        out.append(f"**{page}** <sub>`pages/{slug}.md`</sub>")
        for symbol, url, framework in rows:
            if framework:
                out.append(f"- [{symbol}]({url}) — {framework}")
            else:
                out.append(f"- [{symbol}]({url}) <sub>framework/guide</sub>")
        out.append("")

    out.append("---")
    out.append("")
    out.append("## By framework")
    out.append("")
    out.append("Same data, grouped the other direction — everything the HIG "
                "cites for a given framework.")
    out.append("")
    for framework in sorted(by_framework):
        out.append(f"### {framework}")
        for symbol, url, page, slug in by_framework[framework]:
            out.append(f"- [{symbol}]({url}) — {page} (`pages/{slug}.md`)")
        out.append("")

    return "\n".join(out).rstrip() + "\n", total


LINK_LIST_LINE = re.compile(r"^\s*-\s*\[")


def extract_component_index():
    """One-line purpose for every page that has one -- the fastest lookup for
    'which component do I use', at full coverage rather than a hand-picked few."""
    rows = []
    skipped = []
    for fn in sorted(os.listdir(CONTENT)):
        if not fn.endswith(".md"):
            continue
        text = open(os.path.join(CONTENT, fn), encoding="utf-8").read()
        lines = text.split("\n")
        page, slug = title_of(text), fn[:-3]
        purpose = lines[2].strip() if len(lines) > 2 else ""
        if not purpose or LINK_LIST_LINE.match(purpose) or purpose.startswith("!["):
            skipped.append((page, slug))
            continue
        if len(purpose) > 200:
            purpose = purpose[:197].rsplit(" ", 1)[0] + "..."
        rows.append((page, slug, purpose))

    out = [
        "# Component index: one line each",
        "",
        f"Every page's opening purpose statement, {len(rows)} of them, so "
        "finding the right component doesn't require opening pages one at a "
        "time. Sorted alphabetically — grep or scan for a keyword.",
        "",
        "This is coverage, not a decision procedure: it tells you what each "
        "thing *is*, not which one to pick when two are plausible. For the "
        "recurring hard choices (sheet vs popover vs alert vs action sheet, "
        "tab bar vs sidebar), see the decision tables in SKILL.md — those "
        "encode Apple's actual stated preference, which a purpose line alone "
        "won't.",
        "",
        "| Component | Purpose | Page |",
        "|---|---|---|",
    ]
    for page, slug, purpose in rows:
        purpose_escaped = purpose.replace("|", "\\|")
        out.append(f"| **{page}** | {purpose_escaped} | `pages/{slug}.md` |")

    if skipped:
        out.append("")
        out.append(f"<sub>{len(skipped)} pages omitted — hub/category pages "
                    "that open with a link list rather than a purpose "
                    "statement: " + ", ".join(p for p, _ in skipped) + "</sub>")

    return "\n".join(out).rstrip() + "\n", len(rows)


# Design concerns that recur across the corpus. Guidance for these is filed
# by topic, not by component, so searching component pages for them fails --
# the empty-state rule lives in writing.md, contrast rules are spread over
# 12 pages.
#
# Each entry is (label, regex, home_page_slug). home_page_slug is stated
# explicitly rather than derived from the label: substring-matching a label
# against slugs gets it wrong in both directions (first-word-only misses
# motion.md for "animation & motion"; loose matching hits menus-and-actions
# for "destructive actions" and wrongly implies a home page exists). None
# means the concept has no page of its own, which is the case worth
# flagging. Every slug here is verified to exist at build time.
CONCEPTS = [
    ("empty state", r"empty state|blank screen", None),
    ("loading", r"\bloading\b|progress indicator", "loading"),
    ("error handling", r"\berror\b", None),
    ("onboarding", r"\bonboarding\b|first launch", "onboarding"),
    ("dark mode", r"dark mode", "dark-mode"),
    ("Dynamic Type", r"dynamic type", None),          # lives in typography
    ("VoiceOver", r"voiceover", "voiceover"),
    ("contrast", r"contrast", None),                  # accessibility + color
    ("color blindness", r"color blind|colorblind", None),
    ("haptics", r"haptic", "playing-haptics"),
    ("animation & motion", r"\banimat|\bmotion\b", "motion"),
    ("gestures", r"\bgesture", "gestures"),
    ("keyboard shortcuts", r"keyboard shortcut", "keyboards"),
    ("focus & selection", r"\bfocus\b", "focus-and-selection"),
    ("safe area", r"safe area", None),                # lives in layout
    ("landscape & orientation", r"landscape|orientation", None),
    ("multitasking", r"multitask|split view|stage manager", "multitasking"),
    ("offline & connectivity", r"offline|no connection|network", None),
    ("permissions", r"\bpermission|authoriz", None),  # lives in privacy
    ("privacy", r"\bprivacy\b", "privacy"),
    ("notifications", r"notification", "notifications"),
    ("search", r"\bsearch\b", "searching"),
    ("undo & redo", r"\bundo\b|\bredo\b", "undo-and-redo"),
    ("drag and drop", r"drag and drop|drag-and-drop", "drag-and-drop"),
    ("destructive actions", r"destructive", None),
    ("confirmation", r"confirm", None),
    ("Liquid Glass", r"liquid glass", None),          # discussed in materials
    ("SF Symbols", r"sf symbol", "sf-symbols"),
    ("localization & RTL", r"right-to-left|right to left|localiz", "right-to-left"),
    ("data entry & validation", r"\bvalidat|data entry", "entering-data"),
]


def extract_concept_index(by_page):
    """Concept -> the rules about it, wherever they're filed.

    rules.md is organized by page, which mirrors how Apple files things and
    inherits the same blind spot: a concern that isn't a component has no
    obvious page to look under. This inverts that -- ask "what does the HIG
    say about empty states" and get the answer even though it lives under
    Writing.

    Counts rules, not word occurrences: a page that merely mentions
    "contrast" in passing isn't where the contrast guidance lives.
    """
    slugs = {slug for (_page, slug) in by_page}
    out = [
        "# Concept index: where guidance actually lives",
        "",
        "Design concerns mapped to the rules about them, wherever those "
        "rules are filed. Apple organizes the HIG by component, so a concern "
        "that isn't a component — empty states, error handling, offline "
        "behavior — has no page to look under, and searching component pages "
        "for it comes up empty even when the guidance exists.",
        "",
        "The empty-state rule, for instance, lives in **Writing**. Nothing "
        "about the page list suggests that.",
        "",
        "Counts are **rules**, not mentions — a page that says \"contrast\" "
        "in passing isn't where the contrast guidance is. Grep `rules.md` "
        "for the concept to read the rules themselves.",
        "",
        "---",
        "",
    ]

    bad_home = []
    for label, pattern, home in CONCEPTS:
        rx = re.compile(pattern, re.I)
        hits = []
        for (page, slug), rows in by_page.items():
            n = sum(1 for rule, why, _p in rows if rx.search(rule) or rx.search(why))
            if n:
                hits.append((n, page, slug))
        if not hits:
            continue
        hits.sort(key=lambda h: (-h[0], h[1]))
        total = sum(n for n, _, _ in hits)

        # Fail loudly if a declared home page doesn't exist, rather than
        # silently emitting a link to nothing.
        if home and home not in slugs:
            bad_home.append((label, home))

        out.append(f"## {label}")
        out.append("")
        if home:
            out.append(f"{total} rule(s) across {len(hits)} page(s). "
                       f"Home page: `pages/{home}.md`.")
        else:
            out.append(f"{total} rule(s) across {len(hits)} page(s). "
                       "⚠︎ **No page of its own — the guidance is filed "
                       "under the topics below.**")
        out.append("")
        for n, page, slug in hits[:8]:
            out.append(f"- **{page}** — {n} rule(s) · `pages/{slug}.md`")
        if len(hits) > 8:
            rest = ", ".join(p for _n, p, _s in hits[8:])
            out.append(f"- <sub>also: {rest}</sub>")
        out.append("")

    if bad_home:
        raise SystemExit(
            "concept index declares home pages that don't exist: "
            + ", ".join(f"{lbl} -> {h}" for lbl, h in bad_home)
        )

    return "\n".join(out).rstrip() + "\n", len(CONCEPTS)


# Files this script owns. Anything else in references/ belongs to another
# builder (assets-index.md comes from build_ui_kit_index.py) and must
# survive a rebuild -- an earlier version rmtree'd the whole directory,
# which silently deleted the UI-kit index whenever this ran on its own.
OWNED = ["rules.md", "specs.md", "platform-diffs.md", "api-map.md",
         "components.md", "concepts.md"]

if __name__ == "__main__":
    # Clear only what we regenerate, so a co-resident file from another
    # builder isn't destroyed as a side effect.
    for name in OWNED:
        p = os.path.join(REFS, name)
        if os.path.exists(p):
            os.remove(p)
    pages_dir = os.path.join(REFS, "pages")
    if os.path.isdir(pages_dir):
        shutil.rmtree(pages_dir)
    os.makedirs(pages_dir, exist_ok=True)

    by_page, total = extract_rules()
    open(os.path.join(REFS, "rules.md"), "w", encoding="utf-8").write(
        write_rules(by_page, total))
    open(os.path.join(REFS, "specs.md"), "w", encoding="utf-8").write(
        extract_specs())
    open(os.path.join(REFS, "platform-diffs.md"), "w", encoding="utf-8").write(
        extract_platform_diffs())
    api_map, api_total = extract_api_map()
    open(os.path.join(REFS, "api-map.md"), "w", encoding="utf-8").write(api_map)
    comp_index, comp_total = extract_component_index()
    open(os.path.join(REFS, "components.md"), "w", encoding="utf-8").write(comp_index)
    concept_index, concept_total = extract_concept_index(by_page)
    open(os.path.join(REFS, "concepts.md"), "w", encoding="utf-8").write(concept_index)

    for fn in sorted(os.listdir(CONTENT)):
        if fn.endswith(".md"):
            shutil.copy2(os.path.join(CONTENT, fn),
                         os.path.join(REFS, "pages", fn))

    def kb(p):
        return os.path.getsize(os.path.join(REFS, p)) // 1024
    print(f"rules.md          {total} rules across {len(by_page)} topics, {kb('rules.md')} KB")
    print(f"specs.md          {kb('specs.md')} KB")
    print(f"platform-diffs.md {kb('platform-diffs.md')} KB")
    print(f"api-map.md        {api_total} symbols, {kb('api-map.md')} KB")
    print(f"components.md     {comp_total} components, {kb('components.md')} KB")
    print(f"concepts.md       {concept_total} concepts, {kb('concepts.md')} KB")
    print(f"pages/            {len(os.listdir(os.path.join(REFS, 'pages')))} files")
