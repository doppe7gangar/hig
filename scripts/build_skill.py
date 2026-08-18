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


DEVDOC_RE = re.compile(r"^\[([^\]]+)\]\(([^)]+)\)\s*—\s*(.+)$")


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
            m = DEVDOC_RE.match(line.strip())
            if not m:
                continue
            symbol, url, framework = m.group(1), m.group(2), m.group(3).strip()
            rows.append((symbol, url, framework))
            by_framework.setdefault(framework, []).append((symbol, url, page, slug))
            total += 1
        if rows:
            by_page[(page, slug)] = rows

    out = [
        "# API map: guidance to implementation",
        "",
        f"{total} symbol references pulled from every page's 'Developer "
        "documentation' section — the exact SwiftUI, UIKit, AppKit, and "
        "framework-specific API that implements each piece of guidance.",
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
            out.append(f"- [{symbol}]({url}) — {framework}")
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


if __name__ == "__main__":
    if os.path.isdir(REFS):
        shutil.rmtree(REFS)
    os.makedirs(os.path.join(REFS, "pages"), exist_ok=True)

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
    print(f"pages/            {len(os.listdir(os.path.join(REFS, 'pages')))} files")
