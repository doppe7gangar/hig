#!/usr/bin/env python3
"""Turn measured UI-kit values into CSS custom properties.

Two sources, kept distinct. Apple publishes the system palette on the
HIG's Color page, in the alt text of each swatch ("R-0,G-136,B-255"),
and those values are read straight out. Everything the table does not
cover -- semantic colours, control geometry, interaction states,
materials -- is measured off the kit renderings.

The overlap is the point: every measured value that also appears in the
published table matches it exactly, which is what makes the measured
values that have no published counterpart worth trusting.

Every token here is traced back to the file it was measured from, and the
provenance is written into the CSS as a comment. Nothing is filled in
from memory -- which matters more than usual, because the iOS 27 kit does
not agree with the palette that circulates on the web:

    accent    #0088FF   not the #007AFF everyone hand-codes
    red       #FF383C   not #FF3B30
    label     black on a plain background, but #1A1A1A on glass

Values that *do* match Apple's published semantics are what make the rest
credible: the switch measures #34C759 light and #30D158 dark, exactly
Apple's systemGreen for each appearance, and the secondary-label and
placeholder greys land on rgba(60,60,67,0.6) and rgba(60,60,67,0.3) to
the digit.

    python3 scripts/build_design_tokens.py
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
REFS = os.path.join(REPO, ".claude", "skills", "apple-ui-kit")
TOKENS_JSON = os.path.join(REFS, "ui-kit-tokens.json")

# role -> (file substring, appearance, how to choose the colour)
#
# "top" takes the most-covering colour; ("hue", lo, hi) takes the most
# common one whose hue sits in that range, which is how the accent blue is
# picked out of artwork that is mostly white; ("alpha", v) matches a
# translucent value, for the label and fill ladders.
ROLES = {
    # A glass button's label is the *vibrant* label. It was once taken for
    # the primary label, which put #1A1A1A on every line of body text; the
    # kit's variables (below) say plain text is black.
    "label-vibrant": [
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

# Apple's iOS 27 design kit for Figma names its system colours as
# variables, in a light and a dark mode. A variable is what the system
# colour *is*; a rendering is what one component drew with it. Where a
# role has a variable, the variable wins, and every rendering-measured
# value that also has one is checked against it. That cross-check is how
# the old "label" turned out to be the vibrant label off a glass button:
# the kit's Labels/Primary is black, and #1A1A1A is Labels - Vibrant,
# for text on glass.
#
# role: (variable, light, dark)
KIT_VARIABLES = {
    "label": ("Labels/Primary", "#000000", "#FFFFFF"),
    "label-secondary": ("Labels/Secondary", "rgba(60, 60, 67, 0.6)", "rgba(235, 235, 245, 0.7)"),
    "label-tertiary": ("Labels/Tertiary", "rgba(60, 60, 67, 0.3)", "rgba(235, 235, 245, 0.3)"),
    "label-quaternary": ("Labels/Quaternary", "rgba(60, 60, 67, 0.18)", "rgba(235, 235, 245, 0.16)"),
    "label-vibrant": ("Labels - Vibrant/Primary", "#1A1A1A", "#F5F5F5"),
    "label-vibrant-secondary": ("Labels - Vibrant/Secondary", "#727272", "#8A8A8A"),
    "fill-vibrant-tertiary": ("Fills - Vibrant/Tertiary", "#EDEDED", "#121212"),
    "fill-secondary": ("Fills/Secondary", "rgba(120, 120, 128, 0.16)", None),
    "separator": ("Separators/Non-opaque", "rgba(0, 0, 0, 0.12)", "rgba(255, 255, 255, 0.17)"),
    "separator-opaque": ("Separators/Opaque", "#C6C6C8", "#38383A"),
    "bg-primary": ("Backgrounds/Primary", "#FFFFFF", "#000000"),
    "bg-secondary": ("Backgrounds/Secondary", "#F2F2F7", "#1C1C1E"),
    "bg-tertiary": ("Backgrounds/Tertiary", "#FFFFFF", "#2C2C2E"),
    "bg-elevated": ("Backgrounds/Primary - Elevated", "#FFFFFF", "#1C1C1E"),
    "bg-grouped": ("Backgrounds - Grouped/Primary", "#F2F2F7", "#000000"),
    "bg-grouped-secondary": ("Backgrounds - Grouped/Secondary", "#FFFFFF", "#1C1C1E"),
    "bg-grouped-tertiary": ("Backgrounds - Grouped/Tertiary", "#F2F2F7", "#2C2C2E"),
    "overlay": ("Overlays/Default", "rgba(0, 0, 0, 0.2)", None),
    "accent": ("Accents/Blue", "#0088FF", "#0091FF"),
    "red": ("Accents/Red", "#FF383C", "#FF4245"),
    "orange": ("Accents/Orange", "#FF8D28", "#FF9230"),
    "yellow": ("Accents/Yellow", "#FFCC00", "#FFD600"),
    "green": ("Accents/Green", "#34C759", "#30D158"),
    "mint": ("Accents/Mint", "#00C8B3", "#00DAC3"),
    "teal": ("Accents/Teal", "#00C3D0", "#00D2E0"),
    "cyan": ("Accents/Cyan", "#00C0E8", "#3CD3FE"),
    "blue": ("Accents/Blue", "#0088FF", "#0091FF"),
    "indigo": ("Accents/Indigo", "#6155F5", "#6D7CFF"),
    "purple": ("Accents/Purple", "#CB30E0", "#DB34F2"),
    "pink": ("Accents/Pink", "#FF2D55", "#FF375F"),
    "brown": ("Accents/Brown", "#AC7F5E", "#B78A66"),
    "gray": ("Grays/Gray", "#8E8E93", "#8E8E93"),
    "gray-2": ("Grays/Gray 2", "#AEAEB2", "#636366"),
    "gray-3": ("Grays/Gray 3", "#C7C7CC", "#48484A"),
    "gray-4": ("Grays/Gray 4", "#D1D1D6", "#3A3A3C"),
    "gray-5": ("Grays/Gray 5", "#E5E5EA", "#2C2C2E"),
    "gray-6": ("Grays/Gray 6", "#F2F2F7", "#1C1C1E"),
}


def kit_colour(css):
    """A KIT_VARIABLES value as the dict the rendering measurements use."""
    m = re.match(r"rgba\((\d+), (\d+), (\d+), ([\d.]+)\)", css)
    if m:
        r, g, b, a = int(m[1]), int(m[2]), int(m[3]), float(m[4])
        return {"hex": f"#{r:02X}{g:02X}{b:02X}", "alpha": a, "css": css}
    return {"hex": css.upper(), "alpha": 1.0, "css": css.upper()}


def rgba_of(col):
    h = col["hex"].lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)) + (col["alpha"],)


# Geometry read off the rendered shapes, in points. Kept separate from
# colour because it doesn't vary by appearance.
GEOMETRY = {
    "switch": ("Toggles/Light_Idle_Is On_Is Enabled_Toggle", "size_pt", "radius_pt"),
    "stepper": ("Steppers/Light_Default Increment", "size_pt", "radius_pt"),
    "tab-pill": ("Tab Bars/_Tab Bar Button/iPad/Dark_Selected Dark Tab Bar"
                 " Button - iPad - Text", "size_pt", "radius_pt"),
}



# Type styles and the point size each one is at the Large (default)
# Dynamic Type setting, from specs.md. Tracking is looked up per size.
TYPE_SIZES = {
    "large-title": 34, "title1": 28, "title2": 22, "title3": 20,
    "headline": 17, "body": 17, "callout": 16, "subhead": 15,
    "footnote": 13, "caption1": 12, "caption2": 11,
}

# SF Pro's weight axis does not use the CSS ladder. Read off the named
# instances in the variable font: Medium is 510 and Semibold is 590, not
# 500 and 600. Asking for font-weight: 600 gets you a weight between two
# real ones that Apple does not ship.
SF_WEIGHTS = {
    "ultralight": 31, "thin": 111, "light": 274, "regular": 400,
    "medium": 510, "semibold": 590, "bold": 700, "heavy": 860,
    "black": 1000,
}


def read_tracking():
    """Apple's per-size tracking table, parsed out of specs.md.

    Typography is where an otherwise accurate page stops looking like
    Apple, and tracking is why: the values are not monotonic. Body at
    17pt is tracked -26/1000 em, but Large Title at 34pt is +12 -- looser,
    not tighter. Guessing "big text is tight" gets the most prominent
    text on the screen wrong by about 34/1000 em.

    On Apple platforms the font's own trak table does this. Browsers
    ignore trak, so it has to be applied as letter-spacing.
    """
    specs = os.path.join(REPO, ".claude", "skills", "apple-hig",
                         "references", "specs.md")
    if not os.path.exists(specs):
        return {}
    text = open(specs, encoding="utf-8").read()
    i = text.find("Tracking values \u2192 SF Pro")
    if i == -1:
        i = text.find("Tracking values → SF Pro")
    if i == -1:
        return {}
    # Stop at the next table. specs.md carries three tracking tables --
    # SF Pro, SF Pro Rounded, New York -- one after another, and a window
    # wide enough to hold SF Pro's 96 rows runs into Rounded's. Keyed by
    # size, the later rows silently overwrite the earlier ones and every
    # value comes out subtly wrong rather than obviously broken.
    rest = text[i + 10:]
    j = rest.find("*Specifications")
    chunk = rest[:j] if j != -1 else rest[:4000]
    table = {}
    for m in re.finditer(r"^\|\s*(\d+)\s*\|\s*([+-]?\d+)\s*\|", chunk, re.M):
        table[int(m.group(1))] = int(m.group(2))
    return table



# Apple does publish the palette after all -- on the Color page, in the
# alt text of each swatch image: "R-0,G-136,B-255". A grep for hex or
# rgb() finds nothing, which is how this repo spent its whole life
# believing the corpus had no colour values in it and measuring them off
# the PNGs instead. The measurements were right -- every one matches the
# published table exactly -- but they were never the only source.
#
# What the table adds beyond confirmation: the nine colours nobody had
# measured, the six-step grey ramp, and the Increased Contrast variants,
# which were previously approximated by darkening until the ratio cleared
# 4.5:1.
COLOR_PAGE = os.path.join(REPO, "content", "color.md")
RGB_ALT_RE = re.compile(r"R-(\d+),G-(\d+),B-(\d+)")


def read_published_palette():
    """name -> [light, dark, ic_light, ic_dark] from the Color page."""
    if not os.path.exists(COLOR_PAGE):
        return {}, {}
    text = open(COLOR_PAGE, encoding="utf-8").read()

    def section(header):
        i = text.find(header)
        if i == -1:
            return ""
        j = text.find("\n### ", i + len(header))
        return text[i:j if j != -1 else len(text)]

    def parse(chunk):
        out = {}
        for line in chunk.split("\n"):
            if not line.startswith("| ") or "---" in line or "API |" in line:
                continue
            name = line.split("|")[1].strip()
            trips = RGB_ALT_RE.findall(line)
            if name and trips:
                out[name] = [f"#{int(r):02X}{int(g):02X}{int(b):02X}"
                             for r, g, b in trips]
        return out

    return (parse(section("### System colors")),
            parse(section("### iOS, iPadOS system gray colors")))


def slug(name):
    return (name.lower().replace(" (", "-").replace(")", "")
            .replace(" ", "-"))


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

    # The kit's variables win; a measurement that disagrees is reported.
    disagree = []
    for role, (var, light, dark) in KIT_VARIABLES.items():
        for mode, css in (("light", light), ("dark", dark)):
            if css is None:
                continue
            col = kit_colour(css)
            prev = resolved.get((role, mode))
            if prev:
                a, b = rgba_of(prev[0]), rgba_of(col)
                if max(abs(x - y) for x, y in zip(a[:3], b[:3])) > 2 or abs(a[3] - b[3]) > .02:
                    disagree.append(f"--ios-{role} {mode}: measured {prev[0]['css']} "
                                    f"({prev[1]}), kit variable {var} is {col['css']}")
            resolved[(role, mode)] = (col, f"kit variable {var}")

    geo = {}
    for name, (sub, *fields) in GEOMETRY.items():
        row = find(sub, None)
        if row:
            geo[name] = ({f: row[f] for f in fields}, row["file"])
        else:
            misses.append(f"geometry {name}: no file matching {sub}")

    outdir = os.path.join(REFS, "tokens")
    os.makedirs(outdir, exist_ok=True)
    written = emit_all(resolved, geo, outdir)

    print(f"resolved {len(resolved)} colour tokens, {len(geo)} geometry groups")
    for (role, mode), (col, src) in sorted(resolved.items()):
        print(f"  --ios-{role:18} {mode:5} {col['css']:28} <- {src}")
    for name, (vals, src) in geo.items():
        print(f"  {name:24}       {vals}")
    if disagree:
        print("\nRENDERINGS THAT DISAGREE WITH THE KIT'S VARIABLES (the variable is used):")
        for d in disagree:
            print("  " + d)
    if misses:
        print("\nUNRESOLVED (fix ROLES or re-extract):")
        for m in misses:
            print("  " + m)
    print()
    for f in written:
        print(f"  wrote tokens/{f}")
    if misses:
        return 1
    run_doctor()
    return 0


def build_css(resolved, geo):
    roles = sorted({r for r, _ in resolved})
    L = ["/* Apple iOS 27 design tokens: the system colours from the variables in",
         " * Apple's iOS 27 design kit, cross-checked against measurements of the",
         " * kit's renderings, plus geometry measured off those renderings.",
         " *",
         " * Generated by scripts/build_design_tokens.py -- do not hand-edit.",
         " * Each value carries its source. These are the iOS 27 values and they",
         " * differ from the palette that circulates online: the accent is",
         " * #0088FF, not #007AFF. Text is black on a plain background",
         " * (--ios-label) and #1A1A1A on glass (--ios-label-vibrant).",
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
    ]
    track = read_tracking()
    if track:
        for style, size in TYPE_SIZES.items():
            if size in track:
                L.append(f"  --ios-track-{style}: {track[size]/1000:+.3f}em;")
        L.append("")
    L += [
        "  /* SF Pro's weight axis, read off the variable font's named",
        "     instances. It is not the CSS ladder: Medium is 510 and",
        "     Semibold is 590, so font-weight: 600 asks for a weight",
        "     between two real ones that Apple never ships. */",
    ]
    for name, w in SF_WEIGHTS.items():
        L.append(f"  --ios-weight-{name}: {w};")
    L.append("")

    L += [
        "  /* Order matters more than it looks. system-ui resolves to",
        "     *something* on every platform, so anything listed after it is",
        "     dead: putting Inter there would mean it never loads anywhere.",
        "",
        "     -apple-system and BlinkMacSystemFont resolve only on Apple",
        "     platforms, where they give the real SF Pro. Inter sits next,",
        "     so it takes over on Windows, Android and Linux, where the",
        "     stack used to fall to Segoe UI or Roboto and stop looking",
        "     Apple-ish at all. system-ui remains as the backstop for when",
        "     fonts/inter.css was not loaded.",
        "",
        "     SF Pro itself is deliberately absent: its licence does not",
        "     cover self-hosting as a webfont, and on the platforms that",
        "     have it -apple-system already found it. */",
        "  --ios-font: -apple-system, BlinkMacSystemFont, 'Inter', system-ui,",
        "      'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;",
        "",
    ]

    sysc, grays = read_published_palette()
    if sysc or grays:
        L += [
            "  /* Apple's published palette, from the Color page's swatch alt",
            "     text (R-0,G-136,B-255). Not measured -- stated. Every value",
            "     the kit was measured for matches this table exactly, which",
            "     is why the measurements can be trusted; these add the nine",
            "     colours nobody measured and the grey ramp. */",
        ]
        # A colour the kit's variables already gave is written once, above,
        # with its dark value; the published table confirms it here.
        for name, v in sorted(sysc.items()) + sorted(grays.items()):
            if slug(name) in roles:
                if resolved[(slug(name), "light")][0]["hex"] != v[0]:
                    L.append(f"  /* {name}: the Color page says {v[0]} */")
                continue
            L.append(f"  --ios-{slug(name)}: {v[0]};")
        L.append("")

    L += [
        "  /* Tracking, from specs.md's SF Pro table, one value per style at",
        "     its Large-setting size. Not monotonic, which is the trap: body",
        "     at 17pt is -26/1000 em but Large Title at 34pt is +12, tracked",
        "     looser rather than tighter. On Apple platforms the font's trak",
        "     table applies these; browsers ignore trak, so they have to be",
        "     set as letter-spacing or the most prominent text on the page is",
        "     the most wrong. */",
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



# --------------------------------------------------------------- emitters
#
# The same measured values, in the formats each target actually consumes.
# CSS was the only output at first, which made the work look web-only when
# the measurements are platform-neutral -- a colour is a colour.
#
# A caution belongs in every native file, so it travels with the code:
# on Apple platforms you should almost never paste these literals. Use
# Color.accentColor / UIColor.systemBlue and let the OS resolve them, so
# they follow Dark Mode, Increase Contrast, and whatever Apple changes
# next. Literals are for the cases the semantic API can't reach -- Core
# Graphics drawing, a canvas, matching Apple's palette on a platform that
# has no notion of it.

NATIVE_CAUTION = [
    "From Apple's iOS 27 design kit: its colour variables, and",
    "measurements of its renderings. Generated by",
    "scripts/build_design_tokens.py -- do not hand-edit.",
    "",
    "On Apple platforms, prefer the semantic APIs (Color.accentColor,",
    "UIColor.systemBlue, .primary) over these literals: they adapt to",
    "Dark Mode and Increase Contrast on their own, and they track",
    "whatever Apple changes next. Reach for these values only where the",
    "semantic API can't -- custom drawing, a canvas, or matching Apple's",
    "palette on a platform that has none.",
]

CROSS_CAUTION = [
    "From Apple's iOS 27 design kit: its colour variables, and",
    "measurements of its renderings. Generated by",
    "scripts/build_design_tokens.py -- do not hand-edit.",
    "",
    "On Android, this is Apple's palette on a platform with its own.",
    "Material has its own colour roles and its own switch, and users",
    "expect them. Use these when brand consistency across platforms is",
    "the deliberate goal -- not by default.",
]


def rgba_parts(col):
    h = col["hex"].lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return r, g, b, col["alpha"]


def camel(role):
    head, *rest = role.split("-")
    return head + "".join(w.capitalize() for w in rest)


def block(lines, prefix):
    return "\n".join(f"{prefix} {l}".rstrip() for l in lines)


def emit_json(resolved, geo, _):
    """Design Tokens style -- what Style Dictionary and Figma plugins read."""
    out = {"color": {}, "size": {}}
    for (role, mode), (col, src) in sorted(resolved.items()):
        out["color"].setdefault(role, {})[mode] = {
            "$value": col["css"], "$type": "color",
            "$extensions": {"measuredFrom": src},
        }
    for name, (vals, src) in sorted(geo.items()):
        size, rad = vals.get("size_pt"), vals.get("radius_pt")
        entry = {}
        if size:
            entry["width"] = {"$value": f"{size[0]}px", "$type": "dimension"}
            entry["height"] = {"$value": f"{size[1]}px", "$type": "dimension"}
        if rad is not None:
            entry["radius"] = {"$value": f"{rad}px", "$type": "dimension"}
        entry["$extensions"] = {"measuredFrom": src}
        out["size"][name] = entry
    return "tokens.json", json.dumps(out, indent=2) + "\n"


def emit_swift(resolved, geo, _):
    L = [block(NATIVE_CAUTION, "//"), "", "import SwiftUI", "",
         "public enum AppleKitColor {"]
    for role in sorted({r for r, _ in resolved}):
        light = resolved.get((role, "light"))
        dark = resolved.get((role, "dark"))
        if not light:
            continue
        name = camel(role)
        lr, lg, lb, la = rgba_parts(light[0])
        dr, dg, db, da = rgba_parts(dark[0]) if dark else (lr, lg, lb, la)
        L += [
            f"    /// light {light[0]['css']}"
            + (f" · dark {dark[0]['css']}" if dark else ""),
            f"    public static let {name} = Color(uiColor: UIColor {{ t in",
            "        t.userInterfaceStyle == .dark",
            f"            ? UIColor(red: {dr/255:.3f}, green: {dg/255:.3f},"
            f" blue: {db/255:.3f}, alpha: {da:.3f})",
            f"            : UIColor(red: {lr/255:.3f}, green: {lg/255:.3f},"
            f" blue: {lb/255:.3f}, alpha: {la:.3f})",
            "    })",
        ]
    L += ["}", "", "public enum AppleKitMetric {"]
    for name, (vals, _src) in sorted(geo.items()):
        size, rad = vals.get("size_pt"), vals.get("radius_pt")
        n = camel(name)
        if size:
            L.append(f"    public static let {n}Size = CGSize(width: {size[0]},"
                     f" height: {size[1]})")
        if rad is not None:
            L.append(f"    public static let {n}Radius: CGFloat = {rad}")
    L += ["    /// buttons.md states 44x44 pt as the general hit-region rule.",
          "    public static let hitTarget: CGFloat = 44", "}", ""]
    return "AppleKitTokens.swift", "\n".join(L)


def emit_compose(resolved, geo, _):
    L = [block(CROSS_CAUTION, "//"), "", "package design.applekit", "",
         "import androidx.compose.ui.graphics.Color",
         "import androidx.compose.ui.unit.dp", "",
         "object AppleKitLight {"]

    def argb(col):
        r, g, b, a = rgba_parts(col)
        return f"0x{int(round(a * 255)):02X}{r:02X}{g:02X}{b:02X}"

    for mode, obj in (("light", "AppleKitLight"), ("dark", "AppleKitDark")):
        if mode == "dark":
            L += ["}", "", "object AppleKitDark {"]
        for role in sorted({r for r, _ in resolved}):
            e = resolved.get((role, mode)) or resolved.get((role, "light"))
            if e:
                L.append(f"    val {camel(role)} = Color({argb(e[0])})")
    L += ["}", "", "object AppleKitMetric {"]
    for name, (vals, _s) in sorted(geo.items()):
        size, rad = vals.get("size_pt"), vals.get("radius_pt")
        n = camel(name)
        if size:
            L.append(f"    val {n}Width = {size[0]}.dp")
            L.append(f"    val {n}Height = {size[1]}.dp")
        if rad is not None:
            L.append(f"    val {n}Radius = {rad}.dp")
    L += ["    val hitTarget = 44.dp", "}", ""]
    return "AppleKitTokens.kt", "\n".join(L)


def emit_android_xml(resolved, _geo, _):
    L = ['<?xml version="1.0" encoding="utf-8"?>',
         "<!--", block(CROSS_CAUTION, "   "), "-->", "<resources>"]
    for role in sorted({r for r, _ in resolved}):
        e = resolved.get((role, "light"))
        if not e:
            continue
        r, g, b, a = rgba_parts(e[0])
        name = role.replace("-", "_")
        L.append(f'    <color name="ios_{name}">'
                 f"#{int(round(a*255)):02X}{r:02X}{g:02X}{b:02X}</color>")
    L += ["</resources>", ""]
    return "colors.xml", "\n".join(L)


def emit_dart(resolved, geo, _):
    L = [block(CROSS_CAUTION, "//"), "", "import 'dart:ui';", ""]

    def c(col):
        r, g, b, a = rgba_parts(col)
        return f"Color(0x{int(round(a*255)):02X}{r:02X}{g:02X}{b:02X})"

    for mode, cls in (("light", "AppleKitLight"), ("dark", "AppleKitDark")):
        L.append(f"class {cls} {{")
        for role in sorted({r for r, _ in resolved}):
            e = resolved.get((role, mode)) or resolved.get((role, "light"))
            if e:
                L.append(f"  static const {camel(role)} = {c(e[0])};")
        L += ["}", ""]
    L.append("class AppleKitMetric {")
    for name, (vals, _s) in sorted(geo.items()):
        size, rad = vals.get("size_pt"), vals.get("radius_pt")
        n = camel(name)
        if size:
            L.append(f"  static const {n}Width = {size[0]};")
            L.append(f"  static const {n}Height = {size[1]};")
        if rad is not None:
            L.append(f"  static const {n}Radius = {rad};")
    L += ["  static const hitTarget = 44.0;", "}", ""]
    return "apple_kit_tokens.dart", "\n".join(L)


def emit_ts(resolved, geo, _):
    """React Native / any JS target."""
    L = [block(NATIVE_CAUTION[:2] + [""] + CROSS_CAUTION[3:], "//"), ""]
    for mode, name in (("light", "light"), ("dark", "dark")):
        L.append(f"export const {name} = {{")
        for role in sorted({r for r, _ in resolved}):
            e = resolved.get((role, mode)) or resolved.get((role, "light"))
            if e:
                L.append(f"  {camel(role)}: '{e[0]['css']}',")
        L += ["} as const;", ""]
    L.append("export const metric = {")
    for name, (vals, _s) in sorted(geo.items()):
        size, rad = vals.get("size_pt"), vals.get("radius_pt")
        n = camel(name)
        if size:
            L.append(f"  {n}Width: {size[0]},")
            L.append(f"  {n}Height: {size[1]},")
        if rad is not None:
            L.append(f"  {n}Radius: {rad},")
    L += ["  hitTarget: 44,", "} as const;", ""]
    return "tokens.ts", "\n".join(L)


EMITTERS = [emit_json, emit_swift, emit_compose, emit_android_xml,
            emit_dart, emit_ts]


def emit_all(resolved, geo, outdir):
    written = ["ios-tokens.css"]
    open(os.path.join(outdir, "ios-tokens.css"), "w").write(
        build_css(resolved, geo))
    for fn in EMITTERS:
        name, body = fn(resolved, geo, outdir)
        open(os.path.join(outdir, name), "w").write(body)
        written.append(name)
    return written

def run_doctor():
    """Fail the build if a generated file no longer matches its claims.

    Every stale count in this repo's history was written by a build and
    found by hand weeks later. Checking here closes that gap.
    """
    import subprocess
    doc = os.path.join(HERE, "doctor.py")
    if not os.path.exists(doc):
        return
    r = subprocess.run([sys.executable, doc, "--fast"],
                       capture_output=True, text=True)
    if r.returncode:
        print("\n--- doctor found a problem ---")
        print(r.stdout.strip()[-800:])
        sys.exit(1)
    print("doctor         consistency checks pass")


if __name__ == "__main__":
    sys.exit(main())
