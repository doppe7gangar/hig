#!/usr/bin/env python3
"""Crawl Apple's Human Interface Guidelines (DocC JSON data API) and
convert every reachable page under /design/human-interface-guidelines
into Markdown files."""

import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
from collections import deque

ROOT_PATH = "/design/human-interface-guidelines"
DATA_BASE = "https://developer.apple.com/tutorials/data"
SITE_BASE = "https://developer.apple.com"
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "content")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

visited = set()
failed = []
pages = {}  # path -> {"title":..., "md":..., "children":[paths]}


def fetch_json(path):
    url = f"{DATA_BASE}{path}.json"
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    last_err = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            last_err = e
            if e.code in (404, 410):
                return None
            time.sleep(2 * (attempt + 1))
        except Exception as e:
            last_err = e
            time.sleep(2 * (attempt + 1))
    raise last_err


# ---------- inline content rendering ----------

def render_inline(nodes, refs):
    out = []
    for n in nodes:
        out.append(render_inline_node(n, refs))
    return "".join(out)


def render_inline_node(n, refs):
    t = n.get("type")
    if t == "text":
        return n.get("text", "")
    if t == "codeVoice":
        return f"`{n.get('code', '')}`"
    if t == "strong":
        return f"**{render_inline(n.get('inlineContent', []), refs)}**"
    if t == "emphasis":
        return f"*{render_inline(n.get('inlineContent', []), refs)}*"
    if t == "reference":
        ident = n.get("identifier", "")
        ref = refs.get(ident, {})
        title = ref.get("title") or n.get("overridingTitle") or ident
        url = resolve_url(ref)
        if url:
            return f"[{title}]({url})"
        return title
    if t == "image":
        ident = n.get("identifier", "")
        ref = refs.get(ident, {})
        alt = ref.get("alt") or ident
        url = resolve_image_url(ref) or ident
        return f"![{alt}]({url})"
    if t == "inlineHead":
        return render_inline(n.get("inlineContent", []), refs)
    if t == "superscript":
        return render_inline(n.get("inlineContent", []), refs)
    if t == "newTerm":
        return f"*{render_inline(n.get('inlineContent', []), refs)}*"
    # fallback: try inlineContent
    if "inlineContent" in n:
        return render_inline(n["inlineContent"], refs)
    if "text" in n:
        return n["text"]
    return ""


def resolve_url(ref):
    url = ref.get("url")
    if not url:
        return None
    if url.startswith("http"):
        return url
    if url.startswith("/"):
        return SITE_BASE + url
    return url


def resolve_image_url(ref):
    """Pick the best variant URL for an image reference: prefer the
    light-appearance, highest-resolution asset from Apple's CDN."""
    variants = ref.get("variants") or []
    if not variants:
        return ref.get("url")

    def score(variant):
        traits = variant.get("traits", [])
        res = 0
        for t in traits:
            if t.endswith("x") and t[:-1].isdigit():
                res = max(res, int(t[:-1]))
        dark = 1 if "dark" in traits else 0
        return (res, -dark)

    best = max(variants, key=score)
    return best.get("url")


# ---------- block content rendering ----------

def render_blocks(blocks, refs, depth=0):
    lines = []
    for b in blocks:
        lines.extend(render_block(b, refs, depth))
    return lines


def render_block(b, refs, depth=0):
    t = b.get("type")
    lines = []
    if t == "heading":
        level = min(max(b.get("level", 2), 1), 6)
        lines.append(f"{'#' * level} {render_inline_text(b, refs)}")
        lines.append("")
    elif t == "paragraph":
        text = render_inline(b.get("inlineContent", []), refs)
        if text.strip():
            lines.append(text)
            lines.append("")
    elif t == "unorderedList":
        for item in b.get("items", []):
            sub = render_blocks(item.get("content", []), refs, depth + 1)
            lines.extend(list_item_lines(sub, "-", depth))
        lines.append("")
    elif t == "orderedList":
        for i, item in enumerate(b.get("items", []), 1):
            sub = render_blocks(item.get("content", []), refs, depth + 1)
            lines.extend(list_item_lines(sub, f"{i}.", depth))
        lines.append("")
    elif t == "aside":
        style = b.get("style", "note").capitalize()
        sub = render_blocks(b.get("content", []), refs, depth)
        body = "\n".join(sub).strip()
        lines.append(f"> **{style}:** " + body.replace("\n", "\n> "))
        lines.append("")
    elif t == "codeListing":
        code = "\n".join(b.get("code", []))
        syntax = b.get("syntax") or ""
        lines.append(f"```{syntax}")
        lines.append(code)
        lines.append("```")
        lines.append("")
    elif t == "table":
        lines.extend(render_table(b, refs))
        lines.append("")
    elif t == "termList":
        for item in b.get("items", []):
            term = render_inline(item.get("term", {}).get("inlineContent", []), refs)
            definition = render_blocks(item.get("definition", {}).get("content", []), refs, depth)
            lines.append(f"- **{term}**: " + " ".join(d for d in definition if d).strip())
        lines.append("")
    elif t == "row":
        for col in b.get("columns", []):
            lines.extend(render_blocks(col.get("content", []), refs, depth))
    elif t == "small":
        text = render_inline(b.get("inlineContent", []), refs)
        if text.strip():
            lines.append(text)
            lines.append("")
    elif t == "links":
        # "See Also"-style link list
        for ident in b.get("items", []):
            ref = refs.get(ident, {})
            title = ref.get("title", ident)
            url = resolve_url(ref)
            if url:
                lines.append(f"- [{title}]({url})")
        lines.append("")
    else:
        # Best-effort fallback for unknown block types with inlineContent/content
        if "inlineContent" in b:
            text = render_inline(b["inlineContent"], refs)
            if text.strip():
                lines.append(text)
                lines.append("")
        elif "content" in b:
            lines.extend(render_blocks(b["content"], refs, depth))
    return lines


def render_inline_text(b, refs):
    if "inlineContent" in b:
        return render_inline(b["inlineContent"], refs)
    return b.get("text", "")


def list_item_lines(sub_lines, marker, depth):
    text = "\n".join(l for l in sub_lines if l is not None)
    text = text.strip("\n")
    if not text:
        return []
    parts = text.split("\n")
    indent = "  " * depth
    out = [f"{indent}{marker} {parts[0]}"]
    for p in parts[1:]:
        if p.strip():
            out.append(f"{indent}  {p}")
    return out


def render_table(b, refs):
    rows = b.get("rows", [])
    if not rows:
        return []
    lines = []

    def cell_text(cell_blocks):
        return render_blocks_inline_join(cell_blocks, refs)

    has_header = b.get("header", "none") != "none"
    header_row = rows[0] if has_header else None
    body_rows = rows[1:] if has_header else rows

    if header_row is not None:
        header_cells = [cell_text(c) for c in header_row]
        lines.append("| " + " | ".join(header_cells) + " |")
        lines.append("| " + " | ".join(["---"] * len(header_cells)) + " |")
    for row in body_rows:
        cells = [cell_text(c) for c in row]
        if header_row is None and lines == []:
            # no header info at all: synthesize a blank header for valid markdown
            lines.append("| " + " | ".join([""] * len(cells)) + " |")
            lines.append("| " + " | ".join(["---"] * len(cells)) + " |")
        lines.append("| " + " | ".join(cells) + " |")
    return lines


def render_blocks_inline_join(cell_blocks, refs):
    lines = render_blocks(cell_blocks, refs)
    return " ".join(l for l in lines if l.strip()).replace("|", "\\|")


# ---------- page-level rendering ----------

def render_page(data, path):
    refs = data.get("references", {})
    metadata = data.get("metadata", {})
    title = metadata.get("title", path.rsplit("/", 1)[-1])
    abstract = render_inline(data.get("abstract", []), refs)

    md = [f"# {title}", ""]
    if abstract.strip():
        md.append(abstract)
        md.append("")

    for section in data.get("primaryContentSections", []):
        if section.get("kind") == "content":
            md.extend(render_blocks(section.get("content", []), refs))
        elif "content" in section:
            md.extend(render_blocks(section.get("content", []), refs))

    # Topic sections (child page listings) rendered as links, for collection pages
    for ts in data.get("topicSections", []) or []:
        heading = ts.get("title")
        idents = ts.get("identifiers", [])
        links = []
        for ident in idents:
            ref = refs.get(ident, {})
            t = ref.get("title")
            url = resolve_url(ref)
            if t and url:
                links.append(f"- [{t}]({url})")
        if links:
            if heading:
                md.append(f"## {heading}")
                md.append("")
            md.extend(links)
            md.append("")

    return "\n".join(md).rstrip() + "\n", title, refs


def child_paths(data):
    """Return HIG-internal doc paths referenced as topic children of this page."""
    refs = data.get("references", {})
    children = []
    seen_idents = set()

    def add_from_ident_list(idents):
        for ident in idents:
            if ident in seen_idents:
                continue
            seen_idents.add(ident)
            ref = refs.get(ident, {})
            if ref.get("type") not in ("topic",):
                continue
            url = ref.get("url", "").split("#", 1)[0]
            if url.startswith(ROOT_PATH):
                children.append(url)

    for ts in data.get("topicSections", []) or []:
        add_from_ident_list(ts.get("identifiers", []))

    # Some pages only list children inside references without topicSections
    for ident, ref in refs.items():
        if ident in seen_idents:
            continue
        if ref.get("type") == "topic":
            url = ref.get("url", "").split("#", 1)[0]
            if url.startswith(ROOT_PATH):
                children.append(url)
                seen_idents.add(ident)

    return children


def path_to_filename(path):
    rel = path[len(ROOT_PATH):].strip("/")
    if not rel:
        return "human-interface-guidelines.md"
    return rel + ".md"


def crawl():
    q = deque([ROOT_PATH])
    order = []
    while q:
        path = q.popleft()
        if path in visited:
            continue
        visited.add(path)
        print(f"Fetching {path} ...", file=sys.stderr)
        try:
            data = fetch_json(path)
        except Exception as e:
            print(f"  FAILED: {e}", file=sys.stderr)
            failed.append((path, str(e)))
            continue
        if data is None:
            print("  404, skipping", file=sys.stderr)
            failed.append((path, "404"))
            continue
        md, title, refs = render_page(data, path)
        pages[path] = {"title": title, "md": md}
        order.append(path)
        for child in child_paths(data):
            if child not in visited:
                q.append(child)
    return order


if __name__ == "__main__":
    order = crawl()
    os.makedirs(OUT_DIR, exist_ok=True)
    for path in order:
        fname = path_to_filename(path)
        fpath = os.path.join(OUT_DIR, fname)
        os.makedirs(os.path.dirname(fpath) or OUT_DIR, exist_ok=True)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(pages[path]["md"])
    print(f"\nDone. {len(order)} pages written to {OUT_DIR}", file=sys.stderr)
    if failed:
        print(f"{len(failed)} failed:", file=sys.stderr)
        for p, e in failed:
            print(f"  {p}: {e}", file=sys.stderr)
    # write manifest
    with open(os.path.join(OUT_DIR, "_manifest.json"), "w") as f:
        json.dump({"pages": {p: pages[p]["title"] for p in order}, "failed": failed}, f, indent=2)
