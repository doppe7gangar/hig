#!/usr/bin/env python3
"""Render an Apple developer.apple.com marketing/landing page (plain
server-rendered HTML, not DocC) to Markdown: headings, paragraphs, CTA
links, and card/tile link lists, in document order. Skips images, videos,
and site chrome (nav, footer).

Usage: scrape_marketing_page.py <url> <out-path> [title]
"""

import sys
import urllib.request
from bs4 import BeautifulSoup, NavigableString, Tag

SITE_BASE = "https://developer.apple.com"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

SKIP_TAGS = {"script", "style", "template", "svg", "picture", "video", "img", "source", "nav", "figure"}


def abs_url(href):
    if not href:
        return href
    if href.startswith("http") or href.startswith("sketch://") or href.startswith("mailto:"):
        return href
    if href.startswith("/"):
        return SITE_BASE + href
    return href


def clean(text):
    return " ".join(text.split()).replace("\xa0", " ")


def inline_md(el):
    parts = []
    for node in el.children:
        if isinstance(node, NavigableString):
            parts.append(str(node))
        elif isinstance(node, Tag):
            if node.name == "a" and node.get("href"):
                label = clean(node.get_text(" ", strip=True))
                if label:
                    parts.append(f"[{label}]({abs_url(node['href'])})")
            elif node.name not in SKIP_TAGS:
                parts.append(node.get_text(" ", strip=True))
    return clean("".join(parts))


def render_tile_card(a):
    """A card/tile <a> wrapping an h5 (+ optional p description)."""
    title_el = a.select_one("h5, h4, h3")
    title = clean(title_el.get_text(" ", strip=True)) if title_el else clean(a.get_text(" ", strip=True))
    desc_el = a.select_one("p")
    desc = clean(desc_el.get_text(" ", strip=True)) if desc_el else ""
    href = abs_url(a.get("href", ""))
    if not title or not href:
        return None
    if desc:
        return f"- [{title}]({href}) — {desc}"
    return f"- [{title}]({href})"


def walk(node, lines, seen_cards):
    for child in node.children:
        if isinstance(child, NavigableString):
            continue
        if not isinstance(child, Tag):
            continue
        name = child.name
        cls = child.get("class") or []

        if name in SKIP_TAGS:
            continue
        if "globalnav-submenu-header" in cls or "footer-directory-column-section-title" in cls:
            continue

        if name in ("h1", "h2", "h3", "h4"):
            text = inline_md(child)
            if text:
                level = min(int(name[1]) , 4)
                lines.append(f"{'#' * level} {text}")
                lines.append("")
            continue

        if name == "a" and (
            "tile-link" in cls or "card-link" in cls or child.select_one("h5")
        ):
            card = render_tile_card(child)
            if card and card not in seen_cards:
                seen_cards.add(card)
                lines.append(card)
            continue

        if name == "a" and ("button" in cls or "more" in cls):
            label = clean(child.get_text(" ", strip=True))
            href = abs_url(child.get("href", ""))
            if label and href:
                line = f"[{label}]({href})"
                if line not in seen_cards:
                    seen_cards.add(line)
                    lines.append(line)
                    lines.append("")
            continue

        if name == "p":
            more_a = child.select_one("a.more")
            if more_a and len(child.get_text(strip=True)) == len(more_a.get_text(strip=True)):
                label = clean(more_a.get_text(" ", strip=True))
                href = abs_url(more_a.get("href", ""))
                if label and href:
                    lines.append(f"[{label}]({href})")
                    lines.append("")
                continue
            text = inline_md(child)
            if text:
                is_pure_link = text.startswith("[") and text.endswith(")") and text.count("[") == 1
                if is_pure_link:
                    if text in seen_cards:
                        continue
                    seen_cards.add(text)
                lines.append(text)
                lines.append("")
            continue

        # container: recurse
        walk(child, lines, seen_cards)


def render(html):
    soup = BeautifulSoup(html, "html.parser")
    main = soup.select_one("main#main") or soup.select_one("main")
    lines = []
    seen_cards = set()
    walk(main, lines, seen_cards)

    # collapse extra blank lines
    out = []
    prev_blank = False
    for l in lines:
        blank = (l == "")
        if blank and prev_blank:
            continue
        out.append(l)
        prev_blank = blank
    return "\n".join(out).strip() + "\n"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8")


if __name__ == "__main__":
    url = sys.argv[1]
    out_path = sys.argv[2]
    html = fetch(url)
    md = render(html)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"Wrote {out_path}", file=sys.stderr)
