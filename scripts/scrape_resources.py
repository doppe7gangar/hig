#!/usr/bin/env python3
"""Fetch Apple's Design Resources page (developer.apple.com/design/resources)
and render its structure (sections, subsections, download links) to Markdown.

Unlike the HIG pages, this page is plain server-rendered HTML rather than
DocC JSON, and most of its content is links to downloadable design kits
(Figma/Sketch/Photoshop files, fonts, icon assets, product bezels) rather
than prose. This script captures the page structure and every link; it does
not download the linked binary files themselves."""

import os
import sys
import urllib.request
from bs4 import BeautifulSoup, NavigableString, Tag

URL = "https://developer.apple.com/design/resources/"
SITE_BASE = "https://developer.apple.com"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
OUT_FILE = os.path.join(os.path.dirname(__file__), "..", "content", "resources.md")


def abs_url(href):
    if not href:
        return href
    if href.startswith("http") or href.startswith("sketch://"):
        return href
    if href.startswith("/"):
        return SITE_BASE + href
    return href


def inline_md(el):
    parts = []
    for node in el.children:
        if isinstance(node, NavigableString):
            parts.append(str(node))
        elif isinstance(node, Tag):
            if node.name == "a" and node.get("href"):
                label = node.get_text(" ", strip=True)
                parts.append(f"[{label}]({abs_url(node['href'])})")
            else:
                parts.append(node.get_text(" ", strip=True))
    text = "".join(parts)
    return " ".join(text.split()).replace("\xa0", " ")


def clean(text):
    return " ".join(text.split()).replace("\xa0", " ")


def collect_links(item, seen_links):
    links = []
    for a in item.select("a[href]"):
        href = a.get("href", "")
        label = a.get_text(" ", strip=True).replace("\xa0", " ")
        if not href or href.startswith("#") or not label:
            continue
        href = abs_url(href)
        key = (label, href)
        if key in seen_links:
            continue
        seen_links.add(key)
        links.append((label, href))
    return links


def flush_item(lines, title, links):
    if not links:
        return
    if title:
        lines.append(f"- **{title}**")
        for label, href in links:
            lines.append(f"  - [{label}]({href})")
    else:
        for label, href in links:
            lines.append(f"- [{label}]({href})")


def fetch_html():
    req = urllib.request.Request(URL, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8")


def render(html):
    soup = BeautifulSoup(html, "html.parser")
    main = soup.select_one("main") or soup

    lines = ["# Apple Design Resources", ""]

    intro = soup.select_one("p.typography-intro")
    if intro:
        lines.append(clean(intro.get_text(" ", strip=True)))
        lines.append("")

    for section in main.select("section.section-download"):
        h2 = section.select_one("h2.typography-section-headline")
        if not h2:
            continue
        lines.append(f"## {h2.get_text(strip=True)}")
        lines.append("")

        content = section.select_one("div.section-content")
        if content is None:
            continue

        seen_links = set()
        pending_desc = []

        for child in content.find_all(["p"], recursive=False):
            more_a = child.select_one("a.more")
            if more_a:
                href = more_a.get("href", "")
                label = more_a.get_text(" ", strip=True) or "Learn more"
                if href:
                    pending_desc.append(f"[{label}]({abs_url(href)})")
                continue
            text = inline_md(child)
            if text:
                pending_desc.append(text)

        if pending_desc:
            lines.extend(pending_desc)
            lines.append("")

        for h4 in content.select("h4"):
            lines.append(f"### {clean(h4.get_text(' ', strip=True))}")
            lines.append("")
            grid = h4.find_next_sibling("div", class_="grid")
            if grid is None:
                continue
            for item in grid.select(":scope > div"):
                title_el = item.select_one("h5")
                title = title_el.get_text(strip=True) if title_el else None
                flush_item(lines, title, collect_links(item, seen_links))
            lines.append("")

        for dg in content.select("div.download-grid"):
            for dc in dg.select("div.download-content"):
                a = dc.find("a", href=True)
                if not a:
                    continue
                href = abs_url(a.get("href"))
                label = a.get_text(" ", strip=True).replace("\xa0", " ")
                if not label or not href:
                    continue
                key = (label, href)
                if key in seen_links:
                    continue
                seen_links.add(key)
                caption = dc.select_one("p.typography-caption")
                note = f" — {clean(caption.get_text(' ', strip=True))}" if caption else ""
                lines.append(f"- [{label}]({href}){note}")
            lines.append("")

        if not content.select("h4"):
            for grid in content.select("div.grid"):
                if grid.find_parent("div", class_="download-grid"):
                    continue
                for item in grid.select(":scope > div"):
                    title_el = item.select_one("h5")
                    title = title_el.get_text(strip=True) if title_el else None
                    flush_item(lines, title, collect_links(item, seen_links))
                lines.append("")

    return "\n".join(lines).rstrip() + "\n"


if __name__ == "__main__":
    html = fetch_html()
    md = render(html)
    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"Wrote {OUT_FILE}", file=sys.stderr)
