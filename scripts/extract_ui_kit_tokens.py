#!/usr/bin/env python3
"""Measure real design values out of the iOS UI kit PNGs.

The HIG corpus contains no colour values at all -- not one hex, not one
RGB triple. Apple documents colour by name ("system blue") because on
Apple platforms you're meant to use the semantic API and let the system
resolve it. That's fine in SwiftUI and useless anywhere else: you cannot
build an iOS-looking web page from the written guidance, because the
guidance never says what the colours are.

The UI kit is the only place in this repo where the actual values exist.
A toggle screenshot is a rendering of Apple's real components, so the
pixels *are* the palette. Measuring the "on" switch gives #34C759 in
light and #30D158 in dark -- exactly Apple's published systemGreen for
each appearance, which is what makes the rest of the measurements
trustworthy.

What this pulls out, per component and state:

  colours    every colour covering a meaningful share of the artwork,
             kept as RGB *plus alpha* -- Apple's fill and separator
             colours are defined as one base grey at several opacities,
             and flattening them would throw that structure away
  geometry   canvas size, the artwork's bounding box, aspect ratio, and
             the corner radius measured off the rendered shape
  states     the same component across idle/pressed, on/off, and
             enabled/disabled, so the deltas between them are visible.
             There is no single disabled treatment: the switch halves
             its track alpha (0.298 -> 0.149) while the stepper drops
             0.239 -> 0.18, so it has to be read per component rather
             than assumed.

Output is JSON, consumed by build_web_tokens.py:

    python3 scripts/extract_ui_kit_tokens.py
    python3 scripts/extract_ui_kit_tokens.py --only Toggles Buttons
"""

import argparse
import collections
import json
import os
import re
import sys

try:
    from PIL import Image
except ImportError:
    sys.exit("needs Pillow:  pip install Pillow")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
KIT = os.path.join(REPO, "ios-27-ui-kit_assets")
SKILL = os.path.join(REPO, ".claude", "skills", "apple-web-ui")
REFS = SKILL

# Figma exported these at 4x: the switch lands on 256x112 px, and 64x28 pt
# is the only sane reading of that. Every geometry figure is reported in
# points using this divisor, with the raw pixels kept alongside so a wrong
# guess here can't silently corrupt the numbers.
SCALE = 4

# A colour has to cover this share of the visible artwork to count as part
# of the design rather than an antialiasing artifact.
MIN_SHARE = 0.02
ALPHA_FLOOR = 8


def parse_name(path):
    """Pull appearance and state out of the kit's filename convention."""
    rel = os.path.relpath(path, KIT)
    parts = rel.split(os.sep)
    component = parts[0]
    stem = os.path.splitext(parts[-1])[0]
    fields = [f.strip() for f in stem.split("_") if f.strip()]

    appearance = None
    state = {}
    labels = []
    for f in fields:
        low = f.lower()
        if low in ("light", "dark"):
            appearance = low
        elif low in ("idle", "pressed", "active", "inactive"):
            state["interaction"] = low
        elif low in ("disabled", "is disabled"):
            state["enabled"] = False
        elif low in ("enabled", "is enabled"):
            state["enabled"] = True
        elif low in ("is on", "on"):
            state["value"] = "on"
        elif low in ("is off", "off"):
            state["value"] = "off"
        else:
            labels.append(f)
    return {
        "component": component,
        "group": "/".join(parts[1:-1]) or None,
        "appearance": appearance,
        "state": state,
        "labels": labels,
        "file": rel,
    }


def measure(path):
    im = Image.open(path).convert("RGBA")
    w, h = im.size

    # getcolors and getbbox run in C. The obvious per-pixel Python loop is
    # fine on a 256x112 switch and hopeless on a 2640x1480 screenshot,
    # which is most of what's left once the controls are done.
    raw = im.getcolors(maxcolors=w * h)
    if not raw:
        return None
    counts = collections.Counter()
    for n, (r, g, b, a) in raw:
        if a >= ALPHA_FLOOR:
            counts[(r, g, b, a)] += n
    if not counts:
        return None

    box = im.getbbox()
    if not box:
        return None
    x0, y0, x1e, y1e = box
    x1, y1 = x1e - 1, y1e - 1
    px = im.load()

    visible = sum(counts.values())
    colours = []
    for (r, g, b, a), n in counts.most_common(12):
        share = n / visible
        if share < MIN_SHARE:
            continue
        colours.append({
            "hex": f"#{r:02X}{g:02X}{b:02X}",
            "alpha": round(a / 255, 3),
            "share": round(share, 3),
            "css": (f"#{r:02X}{g:02X}{b:02X}" if a == 255
                    else f"rgba({r}, {g}, {b}, {round(a/255, 3)})"),
        })

    bw, bh = x1 - x0 + 1, y1 - y0 + 1
    return {
        "canvas_px": [w, h],
        "bbox_px": [bw, bh],
        "size_pt": [round(bw / SCALE, 2), round(bh / SCALE, 2)],
        "aspect": round(bw / bh, 3) if bh else None,
        "radius_pt": corner_radius(px, x0, y0, x1, y1),
        "colours": colours,
    }


def corner_radius(px, x0, y0, x1, y1):
    """Corner radius, read off the shape rather than assumed.

    Walk in from the top-left corner along the diagonal until the pixel
    turns opaque. For a rounded rectangle that crossing point sits at
    r - r/sqrt(2) in from the corner, which inverts to the radius. A
    square corner gives 0; a pill gives half the height.
    """
    h = y1 - y0 + 1
    limit = min((x1 - x0) // 2, h // 2)
    d = 0
    while d < limit:
        _, _, _, a = px[x0 + d, y0 + d]
        if a >= 128:
            break
        d += 1
    if d == 0:
        return 0.0
    r = d / (1 - 1 / 2 ** 0.5)
    r = min(r, h / 2)
    return round(r / SCALE, 1)


def walk(only=None):
    out = []
    for dirpath, _, files in os.walk(KIT):
        for f in sorted(files):
            if not f.lower().endswith(".png"):
                continue
            path = os.path.join(dirpath, f)
            meta = parse_name(path)
            if only and meta["component"] not in only:
                continue
            m = measure(path)
            if m:
                meta.update(m)
                out.append(meta)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", help="limit to these components")
    args = ap.parse_args()

    if not os.path.isdir(KIT):
        sys.exit(f"UI kit not found at {KIT}")

    rows = walk(set(args.only) if args.only else None)
    os.makedirs(REFS, exist_ok=True)
    path = os.path.join(REFS, "ui-kit-tokens.json")
    json.dump(rows, open(path, "w"), indent=1)

    comps = collections.Counter(r["component"] for r in rows)
    print(f"measured {len(rows)} images across {len(comps)} components")
    for c, n in comps.most_common(10):
        print(f"  {c:34} {n:4}")
    print(f"\nwrote {path}")


if __name__ == "__main__":
    main()
