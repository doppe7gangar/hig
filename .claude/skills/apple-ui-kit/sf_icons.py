#!/usr/bin/env python3
"""Swap a design's drawn icons for real SF Symbols, on a Mac.

    python3 sf_icons.py ./design

Every icon in the kit's markup names its symbol, data-sf-symbol="leaf",
and carries a hand-drawn SVG so it shows something anywhere. Those
drawings are the clearest thing that gives a page away as not iOS. On a
Mac this draws each named symbol with the Mac's own SF Symbols
(sf_render.swift, through the swift command that comes with Xcode or its
command-line tools), writes them into the design as vendor/sf-symbols.css,
and links that stylesheet before theme.css. The drawings stay in the
markup underneath, so the page still works where the stylesheet doesn't
reach. Run it again after adding icons.

Elsewhere it changes nothing and says so: the symbols only exist on
Apple's systems.

The symbols stay in your design, not in this repo: Apple's licence allows
them in mock-ups of apps for its platforms, not handed around on their
own. The design's .gitignore lists the stylesheet for that reason.
"""

import argparse
import base64
import glob
import os
import platform
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SWIFT = os.path.join(HERE, "sf_render.swift")
NAME = re.compile(r"""data-sf-symbol=["']([a-z0-9][a-z0-9.]*)["']""")


def cache_dir():
    base = os.environ.get("XDG_CACHE_HOME") or os.path.expanduser("~/.cache")
    return os.path.join(base, "apple-hig", "sf-symbol-png")


def names_in(design):
    found = set()
    for page in glob.glob(os.path.join(design, "*.html")):
        found |= set(NAME.findall(open(page, encoding="utf-8").read()))
    return sorted(found)


def render(names):
    """Draw whatever the cache lacks; return {name: png path} for what exists."""
    cache = cache_dir()
    os.makedirs(cache, exist_ok=True)
    todo = [n for n in names if not os.path.isfile(os.path.join(cache, n + ".png"))]
    missing = []
    if todo:
        run = subprocess.run(["swift", SWIFT, cache] + todo, capture_output=True, text=True)
        if run.returncode != 0:
            sys.exit("swift could not draw the symbols:\n" + (run.stderr or run.stdout)[-800:])
        missing = [l.split(" ", 1)[1] for l in run.stdout.splitlines() if l.startswith("missing ")]
    have = {n: os.path.join(cache, n + ".png") for n in names
            if os.path.isfile(os.path.join(cache, n + ".png"))}
    return have, missing


def stylesheet(have):
    out = ["/* SF Symbols drawn on this Mac by sf_icons.py. Not for redistribution:",
           "   regenerate with python3 sf_icons.py ./design rather than copying. */",
           "svg[data-sf-symbol], [data-sf-symbol] > svg { flex: none; }"]
    for name, path in sorted(have.items()):
        data = base64.b64encode(open(path, "rb").read()).decode()
        sel = f'svg[data-sf-symbol="{name}"], [data-sf-symbol="{name}"] > svg'
        out.append(f'{sel} {{ background: currentColor; '
                   f'-webkit-mask: url("data:image/png;base64,{data}") center / contain no-repeat; '
                   f'mask: url("data:image/png;base64,{data}") center / contain no-repeat; }}')
        out.append(f'svg[data-sf-symbol="{name}"] > *, [data-sf-symbol="{name}"] > svg > * '
                   f'{{ visibility: hidden; }}')
    return "\n".join(out) + "\n"


def link(design):
    """Link the stylesheet into every page, just before theme.css."""
    tag = '<link rel="stylesheet" href="vendor/sf-symbols.css">\n'
    for page in glob.glob(os.path.join(design, "*.html")):
        html = open(page, encoding="utf-8").read()
        if "vendor/sf-symbols.css" in html:
            continue
        m = re.search(r'<link[^>]+href="theme\.css"[^>]*>', html)
        html = html[:m.start()] + tag + html[m.start():] if m else html.replace("</head>", tag + "</head>", 1)
        open(page, "w", encoding="utf-8").write(html)
    ignore = os.path.join(design, ".gitignore")
    lines = open(ignore, encoding="utf-8").read().splitlines() if os.path.isfile(ignore) else []
    if "vendor/sf-symbols.css" not in lines:
        with open(ignore, "a", encoding="utf-8") as f:
            f.write("# SF Symbols drawn on this Mac; Apple's licence: not for redistribution\n"
                    "vendor/sf-symbols.css\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("design", help="the design folder")
    a = ap.parse_args()
    names = names_in(a.design)
    if not names:
        print("no data-sf-symbol names in this design; nothing to draw")
        return 0
    if platform.system() != "Darwin":
        print(f"{len(names)} symbols named, but SF Symbols only exist on a Mac. The design "
              f"keeps its drawn icons; run this on a Mac to swap them for the real ones.")
        return 0
    if not shutil.which("swift"):
        sys.exit("needs the swift command: xcode-select --install")
    have, missing = render(names)
    os.makedirs(os.path.join(a.design, "vendor"), exist_ok=True)
    with open(os.path.join(a.design, "vendor", "sf-symbols.css"), "w", encoding="utf-8") as f:
        f.write(stylesheet(have))
    link(a.design)
    print(f"drew {len(have)} of {len(names)} symbols into vendor/sf-symbols.css")
    if missing:
        print("not SF Symbols names on this Mac (fix the name, or the drawing stays): "
              + ", ".join(missing))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
