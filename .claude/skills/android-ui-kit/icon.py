#!/usr/bin/env python3
"""Material Symbols as inline SVG, for the kit's markup.

The outlined and filled glyph of 158 common icons, drawn for 24 dp.
Outlined is the default; a nav bar's active destination takes the filled
one, as Android draws it.

    python3 icon.py home            # the outlined glyph
    python3 icon.py home --fill     # the filled one
    python3 icon.py --list          # every name

The names are Material Symbols' own -- arrow_back, more_vert -- the same
names the Material Symbols font and Compose's Icons.Outlined use, so an
engineer finds the same icon. data-icon carries it into the markup.

Glyphs: Google's Material Symbols, Outlined, optical size 24, weight 400,
grade 0. Apache 2.0; icons/LICENSE-Material-Symbols.txt.
"""

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "icons", "material-symbols.json"), encoding="utf-8") as _f:
    ICONS = json.load(_f)


def svg(name, fill=False, size=None, cls=None):
    """An inline <svg> for one icon; size in px, otherwise the CSS decides."""
    if name not in ICONS:
        raise KeyError(f"no icon {name!r}; python3 icon.py --list")
    attrs = f' class="{cls}"' if cls else ""
    if size:
        attrs += f' width="{size}" height="{size}"'
    return (f'<svg viewBox="0 0 24 24"{attrs} fill="currentColor" data-icon="{name}" '
            f'aria-hidden="true"><path d="{ICONS[name]["fill" if fill else "outline"]}"/></svg>')


def main():
    ap = argparse.ArgumentParser(description="Print a Material Symbol as inline SVG.")
    ap.add_argument("name", nargs="?")
    ap.add_argument("--fill", action="store_true", help="the filled glyph")
    ap.add_argument("--size", type=int, help="width and height in px")
    ap.add_argument("--list", action="store_true", help="list every icon name")
    a = ap.parse_args()
    if a.list or not a.name:
        print(" ".join(sorted(ICONS)))
        return 0
    try:
        print(svg(a.name, a.fill, a.size))
    except KeyError as e:
        sys.exit(e.args[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())
