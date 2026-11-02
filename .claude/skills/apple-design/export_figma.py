#!/usr/bin/env python3
"""Turn a design into pages Figma can import, one frame per screen and state.

    python3 export_figma.py ./design            # light
    python3 export_figma.py ./design --dark     # light and dark

Writes design/figma/figma-light-1.html (and -dark-, and -2, -3 when there
are more than 20 frames, Figma's limit per import). Each file stands on
its own: the stylesheets, fonts and images are inlined and the scripts are
gone, because Figma's importer fetches nothing.

What it captures: the four states (populated, loading, empty, error), then
every screen and sheet the page's controls open (data-go, data-push,
data-sheet from prototype.js), each one tapped in a real browser so the
frame shows what a person would see. Duplicates are dropped.

To send a file to Figma, with Figma's MCP server connected:
  1. call html_to_figma with the Figma file's key and cssSelector
     ".figma-frame"; it returns a one-time upload URL
  2. curl -sS -X POST -H "Content-Type: text/html" \\
       --data-binary @design/figma/figma-light-1.html "<that URL>"
The reply holds the Figma link. The frames arrive as plain layers, not as
components, and the text keeps the page's font names.
"""

import argparse
import base64
import mimetypes
import os
import re
import sys

ROOTS = ".device, .ipad, .mac-window, .m3-device"
OPENERS = "[data-go], [data-push], [data-sheet], [data-screen-set]"
LIMIT = 20

CAPTURE_JS = r"""(roots) => {
  const dev = document.querySelector(roots);
  if (!dev) return null;
  const held = dev.parentElement && dev.parentElement.closest('[data-state]');
  const root = held && held !== document.body && held !== document.documentElement ? held : dev;
  const copy = root.cloneNode(true);
  copy.querySelectorAll('.demo__bar, script').forEach(e => e.remove());
  // Form fields keep what was typed; cloneNode drops it.
  const src = root.querySelectorAll('input, textarea'), dst = copy.querySelectorAll('input, textarea');
  src.forEach((e, i) => { if (dst[i]) { dst[i].setAttribute('value', e.value);
    if (e.checked) dst[i].setAttribute('checked', ''); } });
  const sig = [...dev.querySelectorAll('*')].filter(e => e.offsetParent !== null && e.children.length === 0)
    .map(e => e.textContent.trim()).filter(Boolean).join('|').slice(0, 4000);
  return { html: copy.outerHTML, sig };
}"""

OPENERS_JS = r"""(sel) => [...document.querySelectorAll(sel)]
  .filter(e => !e.closest('[data-set]'))
  .map((e, i) => ({ i, label: (e.getAttribute('aria-label') || e.innerText || e.getAttribute('data-go') ||
     e.getAttribute('data-push') || e.getAttribute('data-sheet') || '').trim().split('\n')[0].slice(0, 40),
     key: e.getAttribute('data-go') || e.getAttribute('data-push') || e.getAttribute('data-sheet') ||
     e.getAttribute('data-screen-set') }))"""


def data_uri(path):
    mime = mimetypes.guess_type(path)[0] or ("font/woff2" if path.endswith(".woff2") else "application/octet-stream")
    with open(path, "rb") as f:
        return f"data:{mime};base64,{base64.b64encode(f.read()).decode()}"


def inline_urls(css, base):
    def sub(m):
        ref = m.group(2).strip()
        if ref.startswith(("data:", "http:", "https:", "#")):
            return m.group(0)
        path = os.path.normpath(os.path.join(base, ref.split("?")[0].split("#")[0]))
        return f'url("{data_uri(path)}")' if os.path.isfile(path) else m.group(0)
    return re.sub(r"""url\(\s*(['"]?)([^'")]+)\1\s*\)""", sub, css)


def stylesheets(index):
    """Every stylesheet the page uses, in its order, with fonts and images inlined."""
    base = os.path.dirname(index)
    html = open(index, encoding="utf-8").read()
    out = []
    for m in re.finditer(r"<link\b[^>]*>|<style\b[^>]*>(.*?)</style>", html, re.S | re.I):
        tag = m.group(0)
        if tag.lower().startswith("<style"):
            out.append(inline_urls(m.group(1), base))
        elif re.search(r"""rel=["']?stylesheet""", tag, re.I):
            href = re.search(r"""href=["']([^"']+)""", tag)
            if href and not href.group(1).startswith(("http:", "https:")):
                path = os.path.normpath(os.path.join(base, href.group(1)))
                if os.path.isfile(path):
                    out.append(inline_urls(open(path, encoding="utf-8").read(), os.path.dirname(path)))
    return "\n".join(out)


def inline_images(fragment, base):
    def sub(m):
        ref = m.group(2)
        if ref.startswith(("data:", "http:", "https:")):
            return m.group(0)
        path = os.path.normpath(os.path.join(base, ref))
        return f'{m.group(1)}"{data_uri(path)}"' if os.path.isfile(path) else m.group(0)
    return re.sub(r"""(\bsrc=)["']([^"']+)["']""", sub, fragment)


def capture(index, scheme):
    from playwright.sync_api import sync_playwright
    url = "file://" + os.path.abspath(index)
    frames, seen = [], set()
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--no-sandbox"])
        pg = b.new_page(viewport={"width": 1400, "height": 1000}, color_scheme=scheme)

        def keep(label):
            got = pg.evaluate(CAPTURE_JS, ROOTS)
            if got and got["sig"] not in seen:
                seen.add(got["sig"])
                frames.append((label, got["html"]))

        for st in ("populated", "loading", "empty", "error"):
            pg.goto(f"{url}?state={st}", wait_until="load")
            pg.wait_for_timeout(250)
            keep(st.capitalize())
        pg.goto(f"{url}?state=populated", wait_until="load")
        openers, done = pg.evaluate(OPENERS_JS, OPENERS), set()
        for o in openers:
            if not o["key"] or o["key"] in done:
                continue
            done.add(o["key"])
            pg.goto(f"{url}?state=populated", wait_until="load")
            pg.wait_for_timeout(150)
            pg.evaluate("([sel, i]) => [...document.querySelectorAll(sel)]"
                        ".filter(e => !e.closest('[data-set]'))[i].click()", [OPENERS, o["i"]])
            pg.wait_for_timeout(350)
            keep(o["label"] or o["key"])
        b.close()
    return frames


def page(frames, css, scheme, apple):
    if scheme == "dark":
        css = (css.replace("prefers-color-scheme: dark", "min-width: 0px")
                  .replace("prefers-color-scheme:dark", "min-width: 0px")
                  .replace("prefers-color-scheme: light", "max-width: 0px")
                  .replace("prefers-color-scheme:light", "max-width: 0px"))
    font = ('\n.figma-frame, .figma-frame * { font-family: "SF Pro", "SF Pro Text", '
            '-apple-system, BlinkMacSystemFont, Inter, sans-serif !important; }') if apple else ""
    board = f"""
html, body {{ margin: 0; background: {'#1E1E1E' if scheme == 'dark' else '#F5F5F5'}; }}
body {{ display: flex; flex-wrap: wrap; align-items: flex-start; gap: 120px; padding: 120px; }}
.figma-frame {{ flex: none; position: relative; }}
.figma-frame > .device, .figma-frame > .m3-device {{ box-shadow: none !important; border-radius: 0 !important; }}{font}
"""
    body = "\n".join(f'<div class="figma-frame" data-name="{label} ({scheme})" '
                     f'aria-label="{label} ({scheme})">\n{html}\n</div>' for label, html in frames)
    return (f'<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
            f'<title>Figma export ({scheme})</title>\n<style>\n{css}\n{board}</style></head>\n'
            f'<body>\n{body}\n</body></html>\n')


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("design", help="the design folder, holding index.html")
    ap.add_argument("--dark", action="store_true", help="also export dark mode")
    ap.add_argument("-o", "--out", help="output folder (default: <design>/figma)")
    a = ap.parse_args()
    index = os.path.join(a.design, "index.html")
    if not os.path.isfile(index):
        sys.exit(f"no index.html in {a.design}")
    try:
        import playwright  # noqa: F401
    except ImportError:
        sys.exit("needs Playwright: pip3 install playwright && python3 -m playwright install chromium")
    out = a.out or os.path.join(a.design, "figma")
    os.makedirs(out, exist_ok=True)
    css = stylesheets(index)
    apple = "material-components.css" not in open(index, encoding="utf-8").read()
    written = []
    for scheme in ("light", "dark") if a.dark else ("light",):
        frames = [(label, inline_images(h, a.design)) for label, h in capture(index, scheme)]
        if not frames:
            sys.exit(f"found no {ROOTS} in index.html to capture")
        for n in range(0, len(frames), LIMIT):
            path = os.path.join(out, f"figma-{scheme}-{n // LIMIT + 1}.html")
            with open(path, "w", encoding="utf-8") as f:
                f.write(page(frames[n:n + LIMIT], css, scheme, apple))
            written.append((path, frames[n:n + LIMIT]))
    for path, frames in written:
        print(f"{path}: {len(frames)} frame(s) -- {', '.join(l for l, _ in frames)}")
    print('\nSend each with Figma\'s html_to_figma (cssSelector ".figma-frame"), then POST the '
          'file to the URL it returns:\n  curl -sS -X POST -H "Content-Type: text/html" '
          '--data-binary @<file> "<url>"')
    return 0


if __name__ == "__main__":
    sys.exit(main())
