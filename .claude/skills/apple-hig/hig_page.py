#!/usr/bin/env python3
"""Read one page of Apple's Human Interface Guidelines, from Apple's site.

    python3 hig_page.py buttons                      # the whole page
    python3 hig_page.py sheets --section "Platform considerations"
    python3 hig_page.py "tab bars" --grep sidebar    # paragraphs that mention it
    python3 hig_page.py https://developer.apple.com/design/human-interface-guidelines/alerts

This is how the skill reads what Apple says: the page is fetched from
developer.apple.com when it's asked for, the way a browser would, and
printed as text for you to read. Nothing of Apple's is stored in this
repository. A fetched page is cached in ~/.cache/apple-hig/pages/ on your
own machine for a week, so asking twice doesn't fetch twice; --refresh
fetches it again.

Quote what you read here sparingly and exactly, with the page's link, which
the first line of the output gives. Images are left out: their
descriptions are printed in their place.
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

ROOT_PATH = "/design/human-interface-guidelines"
DATA_BASE = "https://developer.apple.com/tutorials/data"
SITE_BASE = "https://developer.apple.com"
IMAGE_BASE = SITE_BASE + "/tutorials"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
HERE = os.path.dirname(os.path.abspath(__file__))
TOPICS = os.path.join(HERE, "references", "topics.md")
WEEK = 7 * 24 * 3600


def cache_dir():
    base = os.environ.get("XDG_CACHE_HOME") or os.path.expanduser("~/.cache")
    return os.path.join(base, "apple-hig", "pages")


def fetch_json(path):
    url = f"{DATA_BASE}{path}.json"
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    last_err = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            last_err = e
            if e.code in (404, 410):
                return None
            time.sleep(2 * (attempt + 1))
        except Exception as e:  # network trouble: retry, then report
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
        return absolute_image(ref.get("url"))

    def score(variant):
        traits = variant.get("traits", [])
        res = 0
        for t in traits:
            if t.endswith("x") and t[:-1].isdigit():
                res = max(res, int(t[:-1]))
        dark = 1 if "dark" in traits else 0
        return (res, -dark)

    best = max(variants, key=score)
    return absolute_image(best.get("url"))


def absolute_image(url):
    return IMAGE_BASE + url if url and url.startswith("/") else url


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
    elif t == "tabNavigator":
        # Tabbed panes. Apple uses these for content that varies along an
        # axis -- most importantly the Dynamic Type scales, where each tab
        # is one text-size setting (xSmall...xxxLarge) holding a full table.
        # This block type was unhandled, so every pane fell through to the
        # fallback and vanished: 151 panes across 28 pages, including 26
        # tables on typography and 8 on layout. That is why the corpus had
        # macOS and tvOS type scales but no iOS one.
        #
        # The tab title is real data (it names the size setting or platform),
        # so it becomes a heading rather than being flattened away.
        for tab in b.get("tabs", []):
            title = " ".join(str(tab.get("title", "")).split())
            content = tab.get("content", [])
            # Panes often open with a heading repeating the tab title; emit
            # the title only when it isn't already the first heading, so the
            # label isn't printed twice.
            first = content[0] if content else {}
            dup = (isinstance(first, dict) and first.get("type") == "heading"
                   and " ".join(str(first.get("text", "")).split()) == title)
            if title and not dup:
                lines.append(f"**{title}**")
                lines.append("")
            lines.extend(render_blocks(content, refs, depth))
        lines.append("")
    elif t == "video":
        # Poster image + media reference; keep the caption if there is one so
        # the surrounding prose still reads, but there is no text to mirror.
        ident = b.get("identifier") or b.get("poster")
        ref = refs.get(ident, {}) if ident else {}
        alt = ref.get("alt")
        if alt:
            lines.append(f"*(video: {alt})*")
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


def topics():
    """slug -> title, from topics.md."""
    out = {}
    if os.path.exists(TOPICS):
        text = open(TOPICS, encoding="utf-8").read()
        for m in re.finditer(r"^\| ([^|]+?) \| \[([a-z0-9-]+)\]", text, re.M):
            out[m.group(2)] = m.group(1)
    return out


def slug_for(name):
    """A slug, a title or an official address -> the page's slug."""
    m = re.search(r"human-interface-guidelines/([a-z0-9-]+)", name)
    if m:
        return m.group(1)
    known = topics()
    want = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    if want in known:
        return want
    for slug, title in known.items():
        if title.lower() == name.lower():
            return slug
    close = [s for s in known if want in s]
    if len(close) == 1:
        return close[0]
    if close:
        sys.exit(f"{name!r} matches several pages: {', '.join(sorted(close)[:8])}")
    return want


def page(slug, refresh=False):
    """(title, url, markdown) for one page, from the cache or Apple's site."""
    os.makedirs(cache_dir(), exist_ok=True)
    cached = os.path.join(cache_dir(), slug + ".md")
    url = f"{SITE_BASE}{ROOT_PATH}/{slug}"
    if not refresh and os.path.exists(cached) and time.time() - os.path.getmtime(cached) < WEEK:
        text = open(cached, encoding="utf-8").read()
        return text.split("\n", 1)[0].lstrip("# ").strip(), url, text
    data = fetch_json(f"{ROOT_PATH}/{slug}")
    if data is None:
        sys.exit(f"Apple has no HIG page called {slug!r}. grep topics.md for the right name.")
    md, title, _ = render_page(data, f"{ROOT_PATH}/{slug}")
    # Text only: an image becomes its description.
    md = re.sub(r"!\[([^\]]*)\]\([^)]*\)",
                lambda m: f"[image: {m.group(1)}]" if m.group(1) else "", md)
    with open(cached, "w", encoding="utf-8") as f:
        f.write(md)
    return title, url, md


def section(md, name):
    """The part of the page under a heading that contains name."""
    out, level = [], None
    for line in md.splitlines():
        m = re.match(r"^(#+) (.*)", line)
        if m and level is not None and len(m.group(1)) <= level:
            break
        if m and level is None and name.lower() in m.group(2).lower():
            level = len(m.group(1))
        if level is not None:
            out.append(line)
    return "\n".join(out)


def grep(md, word):
    """Paragraphs that mention word, each under the heading it sits in."""
    heading, out = "", []
    for block in re.split(r"\n\s*\n", md):
        stripped = block.strip()
        if stripped.startswith("#"):
            heading = stripped.splitlines()[0]
        if re.search(re.escape(word), block, re.I):
            prefix = heading + "\n" if heading and not stripped.startswith("#") else ""
            out.append(prefix + stripped)
    return "\n\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="Read one HIG page from Apple's site.")
    ap.add_argument("page", help="slug (tab-bars), title (Tab bars) or official address")
    ap.add_argument("--section", help="only the part under a heading containing this")
    ap.add_argument("--grep", help="only the paragraphs mentioning this")
    ap.add_argument("--refresh", action="store_true", help="fetch again, ignoring the cache")
    a = ap.parse_args()
    slug = slug_for(a.page)
    try:
        title, url, md = page(slug, a.refresh)
    except Exception as e:  # offline, blocked, Apple down
        sys.exit(f"Couldn't fetch {SITE_BASE}{ROOT_PATH}/{slug} ({e}). Say so, and answer "
                 f"from numbers.md, concepts.md and patterns.md with the link.")
    body = md
    if a.section:
        body = section(md, a.section) or f"(no heading containing {a.section!r})"
    if a.grep:
        body = grep(body, a.grep) or f"(nothing mentions {a.grep!r})"
    print(f"Source: {url} -- Apple's text, fetched from developer.apple.com. "
          f"Quote sparingly, exactly, with this link.\n")
    print(body)
    return 0


if __name__ == "__main__":
    sys.exit(main())
