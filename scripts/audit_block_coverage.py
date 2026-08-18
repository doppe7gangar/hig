#!/usr/bin/env python3
"""Audit which of Apple's DocC block types the scraper actually renders.

Every other check in this repo compares extracted output against what the
parser saw, so a block type the parser never recognized is invisible to all
of them. tabNavigator was unhandled from the first scrape -- 151 panes
across 28 pages, including the entire iOS Dynamic Type scale -- and no
parity audit could detect it, because the parser wasn't producing those
tables to be counted in the first place.

This walks the live JSON, enumerates every `type` value Apple actually
emits, and reports which ones scrape_hig.py handles. For unhandled types it
measures the content at stake (text characters, nested tables) so a
genuinely inert type is distinguishable from one hiding a type scale.

    python3 scripts/audit_block_coverage.py            # full corpus
    python3 scripts/audit_block_coverage.py --quick    # 25-page sample

Exits non-zero if an unhandled type carries real content, so this can gate
a re-scrape.
"""

import argparse
import collections
import json
import os
import re
import sys
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
CONTENT = os.path.join(REPO, "content")
BASE = "https://developer.apple.com/tutorials/data/design/human-interface-guidelines"
ROOT_JSON = "https://developer.apple.com/tutorials/data/design/human-interface-guidelines.json"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# Pages scraped from plain HTML, not DocC -- no JSON to audit.
NON_DOCC = {"design", "resources", "icon-composer", "sf-symbols-app",
            "pass-designer", "reality-composer-pro"}

# Block/inline types scrape_hig.py renders. Kept in sync with render_block
# and render_inline_node; anything Apple emits outside this set is a gap.
HANDLED = {
    # block
    "heading", "paragraph", "unorderedList", "orderedList", "aside",
    "codeListing", "table", "termList", "row", "small", "links",
    "tabNavigator", "video",
    # inline
    "text", "codeVoice", "strong", "emphasis", "reference", "image",
    "inlineHead", "superscript", "newTerm",
}

# Structural containers that carry no renderable content of their own.
STRUCTURAL = {"tab", "column", "listItem"}


def fetch(slug):
    url = ROOT_JSON if slug == "human-interface-guidelines" else f"{BASE}/{slug}.json"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode("utf-8"))
    except Exception:
        return None


def text_len(node):
    """Renderable text under a node -- how much is actually at stake."""
    if isinstance(node, dict):
        if node.get("type") == "text":
            return len(node.get("text", ""))
        return sum(text_len(v) for v in node.values())
    if isinstance(node, list):
        return sum(text_len(x) for x in node)
    return 0


def count_type(node, wanted):
    if isinstance(node, dict):
        n = 1 if node.get("type") == wanted else 0
        return n + sum(count_type(v, wanted) for v in node.values())
    if isinstance(node, list):
        return sum(count_type(x, wanted) for x in node)
    return 0


def walk(node, counts, pages, slug, samples):
    if isinstance(node, dict):
        t = node.get("type")
        if isinstance(t, str):
            counts[t] += 1
            pages[t].add(slug)
            if t not in HANDLED and t not in STRUCTURAL and t not in samples:
                samples[t] = {
                    "page": slug,
                    "chars": text_len(node),
                    "tables": count_type(node, "table"),
                    "keys": sorted(k for k in node.keys() if k != "type"),
                }
        for v in node.values():
            walk(v, counts, pages, slug, samples)
    elif isinstance(node, list):
        for x in node:
            walk(x, counts, pages, slug, samples)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true",
                    help="sample 25 pages instead of the full corpus")
    args = ap.parse_args()

    slugs = sorted(f[:-3] for f in os.listdir(CONTENT) if f.endswith(".md"))
    slugs = [s for s in slugs if s not in NON_DOCC]
    if args.quick:
        slugs = slugs[::max(1, len(slugs) // 25)][:25]

    counts = collections.Counter()
    pages = collections.defaultdict(set)
    samples = {}
    fetched = 0

    for i, slug in enumerate(slugs, 1):
        d = fetch(slug)
        if not d:
            continue
        fetched += 1
        walk(d.get("primaryContentSections"), counts, pages, slug, samples)
        if i % 40 == 0:
            print(f"  ...{i}/{len(slugs)}", file=sys.stderr)

    print(f"\naudited {fetched} pages, {len(counts)} distinct block types\n")

    handled = {t: c for t, c in counts.items() if t in HANDLED}
    structural = {t: c for t, c in counts.items() if t in STRUCTURAL}
    gaps = {t: c for t, c in counts.items()
            if t not in HANDLED and t not in STRUCTURAL}

    print(f"HANDLED ({len(handled)} types, {sum(handled.values())} blocks)")
    for t, c in sorted(handled.items(), key=lambda kv: -kv[1])[:8]:
        print(f"  {t:22} {c:6}")
    if structural:
        print(f"\nSTRUCTURAL, no own content ({len(structural)} types)")
        for t, c in sorted(structural.items(), key=lambda kv: -kv[1]):
            print(f"  {t:22} {c:6}")

    if not gaps:
        print("\nNO GAPS — every type Apple emits is handled.")
        return 0

    print(f"\nUNHANDLED ({len(gaps)} types)")
    print(f"  {'type':22} {'count':>6} {'pages':>6} {'chars':>8} {'tables':>7}")
    material = []
    for t, c in sorted(gaps.items(), key=lambda kv: -kv[1]):
        s = samples.get(t, {})
        chars, tables = s.get("chars", 0), s.get("tables", 0)
        print(f"  {t:22} {c:6} {len(pages[t]):6} {chars:8} {tables:7}"
              f"   e.g. {s.get('page','?')}")
        # A type carrying prose or tables is real loss; one with neither is
        # probably a layout wrapper or a media pointer.
        if chars > 200 or tables > 0:
            material.append((t, c, chars, tables))

    if material:
        print("\n  ^ CARRYING REAL CONTENT — these are losing data:")
        for t, c, chars, tables in material:
            print(f"      {t}: {c} blocks, ~{chars} chars, {tables} tables in the sampled one")
        print("\n  Add cases to render_block/render_inline_node in scrape_hig.py,")
        print("  add them to HANDLED here, then re-scrape.")
        return 1

    print("\n  None carry prose or tables — safe to ignore, but keep watching.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
