#!/usr/bin/env python3
"""Turn measured UI-kit values into CSS custom properties.

The HIG corpus has no colour values in it -- Apple documents colour by
name because on its own platforms you use the semantic API and let the
system resolve it. On the web there is no system to ask, so the guidance
alone cannot get you an iOS-looking page. These values only exist in the
UI kit renderings, which is what makes measuring them worth doing.

Every token here is traced back to the file it was measured from, and the
provenance is written into the CSS as a comment. Nothing is filled in
from memory -- which matters more than usual, because the iOS 27 kit does
not agree with the palette that circulates on the web:

    accent    #0088FF   not the #007AFF everyone hand-codes
    red       #FF383C   not #FF3B30
    label     #1A1A1A   not pure black

Values that *do* match Apple's published semantics are what make the rest
credible: the switch measures #34C759 light and #30D158 dark, exactly
Apple's systemGreen for each appearance, and the secondary-label and
placeholder greys land on rgba(60,60,67,0.6) and rgba(60,60,67,0.3) to
the digit.

    python3 scripts/build_web_tokens.py
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
REFS = os.path.join(REPO, ".claude", "skills", "apple-web-ui")
TOKENS_JSON = os.path.join(REFS, "ui-kit-tokens.json")

# role -> (file substring, appearance, how to choose the colour)
#
# "top" takes the most-covering colour; ("hue", lo, hi) takes the most
# common one whose hue sits in that range, which is how the accent blue is
# picked out of artwork that is mostly white; ("alpha", v) matches a
# translucent value, for the label and fill ladders.
ROLES = {
    "label": [
        ("Buttons/Light_Label - Symbol - Default", "light", "top"),
        ("Buttons/Dark_Label - Symbol - Default", "dark", "top"),
    ],
    "label-secondary": [
        ("List/Light_Section Title", "light", ("alpha", 0.6)),
        ("List/_Header/Dark_Nested Header without Subtitle", "dark",
         ("alpha", 0.698)),
    ],
    "label-tertiary": [
        ("Text Fields/Light_Placeholder", "light", ("alpha", 0.298)),
        ("Text Fields/Dark_Placeholder", "dark", ("alpha", 0.298)),
    ],
    "accent": [
        ("Text Fields/Light_Focused", "light", ("hue", 195, 225)),
        ("Text Fields/Dark_Focused", "dark", ("hue", 195, 225)),
    ],
    "red": [
        ("Buttons/_Label - Symbol - Destructive", None, ("hue", 350, 10)),
        ("Buttons/Dark_Label - Symbol - Destructive", "dark", ("hue", 350, 10)),
    ],
    "green": [
        ("Toggles/Light_Idle_Is On_Is Enabled_Toggle", "light", ("hue", 100, 160)),
        ("Toggles/Dark_Idle_Is On_Is Enabled_Toggle", "dark", ("hue", 100, 160)),
    ],
    "fill-control": [
        ("Steppers/Light_Default Increment", "light", "top"),
        ("Steppers/Dark_Default Increment", "dark", "top"),
    ],
    "fill-track": [
        ("Toggles/Light_Idle_Is Off_Is Enabled_Toggle", "light", ("alpha", 0.298)),
        ("Toggles/Dark_Idle_Is Off_Is Enabled_Toggle", "dark", ("alpha", 0.298)),
    ],
    "surface": [
        ("Text Fields/Light_Placeholder", "light", "top"),
        ("Text Fields/Dark_Placeholder", "dark", "top"),
    ],
}

# Geometry read off the rendered shapes, in points. Kept separate from
# colour because it doesn't vary by appearance.
GEOMETRY = {
    "switch": ("Toggles/Light_Idle_Is On_Is Enabled_Toggle", "size_pt", "radius_pt"),
    "stepper": ("Steppers/Light_Default Increment", "size_pt", "radius_pt"),
    "tab-pill": ("Tab Bars/_Tab Bar Button/iPad/Dark_Selected Dark Tab Bar"
                 " Button - iPad - Text", "size_pt", "radius_pt"),
}


def hue_of(hexv):
    r, g, b = (int(hexv[i:i + 2], 16) / 255 for i in (1, 3, 5))
    mx, mn = max(r, g, b), min(r, g, b)
    d = mx - mn
    if d == 0:
        return None
    if mx == r:
        h = 60 * (((g - b) / d) % 6)
    elif mx == g:
        h = 60 * ((b - r) / d + 2)
    else:
        h = 60 * ((r - g) / d + 4)
    return h


def in_hue(hexv, lo, hi):
    h = hue_of(hexv)
    if h is None:
        return False
    return (lo <= h <= hi) if lo <= hi else (h >= lo or h <= hi)


def pick(row, how):
    cols = row["colours"]
    if not cols:
        return None
    if how == "top":
        return cols[0]
    kind = how[0]
    if kind == "hue":
        _, lo, hi = how
        for c in cols:
            if in_hue(c["hex"], lo, hi):
                return c
    elif kind == "alpha":
        _, target = how
        best = min(cols, key=lambda c: abs(c["alpha"] - target))
        if abs(best["alpha"] - target) <= 0.06:
            return best
    return None


def main():
    if not os.path.exists(TOKENS_JSON):
        sys.exit("run extract_ui_kit_tokens.py first")
    rows = json.load(open(TOKENS_JSON))

    def find(sub, appearance):
        for r in rows:
            if sub in r["file"] and (appearance is None
                                     or r["appearance"] == appearance):
                return r
        return None

    resolved = {}
    misses = []
    for role, entries in ROLES.items():
        for sub, appearance, how in entries:
            row = find(sub, appearance)
            if not row:
                misses.append(f"{role}: no file matching {sub}")
                continue
            col = pick(row, how)
            if not col:
                misses.append(f"{role}: no colour matched in {row['file']}")
                continue
            mode = appearance or "light"
            resolved[(role, mode)] = (col, row["file"])

    geo = {}
    for name, (sub, *fields) in GEOMETRY.items():
        row = find(sub, None)
        if row:
            geo[name] = ({f: row[f] for f in fields}, row["file"])
        else:
            misses.append(f"geometry {name}: no file matching {sub}")

    css = build_css(resolved, geo)
    out = os.path.join(REFS, "ios-web-tokens.css")
    open(out, "w").write(css)

    print(f"resolved {len(resolved)} colour tokens, {len(geo)} geometry groups")
    for (role, mode), (col, src) in sorted(resolved.items()):
        print(f"  --ios-{role:18} {mode:5} {col['css']:28} <- {src}")
    for name, (vals, src) in geo.items():
        print(f"  {name:24}       {vals}")
    if misses:
        print("\nUNRESOLVED (fix ROLES or re-extract):")
        for m in misses:
            print("  " + m)
    print(f"\nwrote {out}")
    return 1 if misses else 0


def build_css(resolved, geo):
    roles = sorted({r for r, _ in resolved})
    L = ["/* Apple iOS 27 design tokens, measured from the UI kit renderings.",
         " *",
         " * Generated by scripts/build_web_tokens.py -- do not hand-edit.",
         " * Each value carries the file it was measured from. These are the",
         " * iOS 27 values and they differ from the palette that circulates",
         " * online: the accent is #0088FF, not #007AFF, and the primary label",
         " * is #1A1A1A, not black.",
         " */", "", ":root {"]

    for role in roles:
        entry = resolved.get((role, "light"))
        if entry:
            col, src = entry
            L.append(f"  --ios-{role}: {col['css']};".ljust(46)
                     + f"/* {src} */")
    L.append("")
    for name, (vals, src) in geo.items():
        size = vals.get("size_pt")
        rad = vals.get("radius_pt")
        if size:
            L.append(f"  --ios-{name}-w: {size[0]}px;")
            L.append(f"  --ios-{name}-h: {size[1]}px;")
        if rad is not None:
            L.append(f"  --ios-{name}-radius: {rad}px;")
    L += [
        "",
        "  /* Type scale: iOS/iPadOS Dynamic Type at the Large (default)",
        "     setting, from specs.md. rem so browser text scaling works --",
        "     the web's nearest equivalent to Dynamic Type.",
        "",
        "     These are complete `font` shorthands, family included, so",
        "     `font: var(--ios-text-body)` is valid on its own. A shorthand",
        "     without a family is invalid CSS and the browser drops the whole",
        "     declaration -- which silently left every size at the default",
        "     16px while the page still looked broadly right. */",
        "  --ios-text-large-title: 400 2.125rem/2.5625rem var(--ios-font);",
        "  --ios-text-title1:      400 1.75rem/2.125rem var(--ios-font);",
        "  --ios-text-title2:      400 1.375rem/1.75rem var(--ios-font);",
        "  --ios-text-title3:      400 1.25rem/1.5625rem var(--ios-font);",
        "  --ios-text-headline:    590 1.0625rem/1.375rem var(--ios-font);",
        "  --ios-text-body:        400 1.0625rem/1.375rem var(--ios-font);",
        "  --ios-text-callout:     400 1rem/1.3125rem var(--ios-font);",
        "  --ios-text-subhead:     400 0.9375rem/1.25rem var(--ios-font);",
        "  --ios-text-footnote:    400 0.8125rem/1.125rem var(--ios-font);",
        "  --ios-text-caption1:    400 0.75rem/1rem var(--ios-font);",
        "  --ios-text-caption2:    400 0.6875rem/0.8125rem var(--ios-font);",
        "",
        "  /* SF Pro ships on Apple devices only; system-ui gets it there and",
        "     a sane native face everywhere else. Do not self-host SF Pro --",
        "     its licence does not cover general web use. */",
        "  --ios-font: system-ui, -apple-system, 'SF Pro Text', 'Segoe UI',",
        "      Roboto, 'Helvetica Neue', Arial, sans-serif;",
        "",
        "  /* Hit target. buttons.md states 44x44 pt as the general rule;",
        "     the accessibility Mobility table gives 28x28 as the floor for",
        "     less important controls. 44 is the one to build to. */",
        "  --ios-hit-target: 44px;",
        "",
        "  /* Measured state deltas. The switch halves its track alpha when",
        "     disabled (0.298 -> 0.149); the stepper drops 0.239 -> 0.18",
        "     instead. There is no single disabled opacity in this kit, so",
        "     0.5 is the switch's value, not a universal rule. */",
        "  --ios-disabled-opacity: 0.5;",
        "}", "",
        "@media (prefers-color-scheme: dark) {",
        "  :root {",
    ]
    for role in roles:
        entry = resolved.get((role, "dark"))
        if entry:
            col, src = entry
            L.append(f"    --ios-{role}: {col['css']};".ljust(48)
                     + f"/* {src} */")
    L += ["  }", "}", ""]
    return "\n".join(L)


if __name__ == "__main__":
    sys.exit(main())
