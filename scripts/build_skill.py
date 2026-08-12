#!/usr/bin/env python3
"""Build a task-oriented HIG skill from the scraped corpus.

The first version shipped the corpus with an index on top. That answers
"what does Apple say about X" if you already know to ask about X, which
makes it a search tool rather than a skill -- it carries no procedure, no
decision criteria, and nothing you'd check without being told to.

Apple states every guideline as a bolded imperative followed by rationale,
and puts every hard number in a table. Both are mechanically extractable,
and both are far more usable as a checklist and a spec sheet than as prose
spread over 178 pages. This produces:

  rules.md          every guideline as a one-line imperative, grouped by
                    topic and tagged with the platform it applies to.
                    Greppable as a review checklist.
  specs.md          every table and measurement in the corpus, with source,
                    so "what size / what ratio" is one lookup.
  platform-diffs.md what actually changes per platform, by topic.
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
    """Which platforms a section is scoped to, if any."""
    if h2 and "Platform considerations" in h2 and h3:
        found = [p for p in PLATFORMS if re.search(rf"\b{re.escape(p)}\b", h3)]
        if found:
            return found
    return []


RULE_RE = re.compile(r"^\*\*(.+?)\*\*\s*(.*)$")


def extract_rules():
    """Every bolded imperative, with a trimmed rationale and platform tag."""
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
                # a rule reads as an instruction; skip table cells and labels
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
    """Tables and number-bearing rules -- the 'what size / what ratio' lookups."""
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
    """What actually changes per platform, grouped by platform then topic."""
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

    for fn in sorted(os.listdir(CONTENT)):
        if fn.endswith(".md"):
            shutil.copy2(os.path.join(CONTENT, fn),
                         os.path.join(REFS, "pages", fn))

    def kb(p):
        return os.path.getsize(os.path.join(REFS, p)) // 1024
    print(f"rules.md          {total} rules across {len(by_page)} topics, {kb('rules.md')} KB")
    print(f"specs.md          {kb('specs.md')} KB")
    print(f"platform-diffs.md {kb('platform-diffs.md')} KB")
    print(f"pages/            {len(os.listdir(os.path.join(REFS, 'pages')))} files")
