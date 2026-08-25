#!/usr/bin/env python3
"""Generate a full token set for a brand colour, in Apple's structure.

The tokens in apple-ui-kit are Apple's palette. That is right for an
iOS-looking app and wrong for almost every real project, which has its
own brand and needs Apple's *craft* rather than Apple's blue. Told to use
a client's colour, the honest options were previously to hand-edit one
token and leave the rest of the system Apple's, or to abandon the system.

What actually transfers is the structure, and the structure is the
valuable part:

  - a label ladder built as one base grey at several opacities, so text
    composites correctly on any surface instead of being flattened per
    background
  - a grouped-background pair: page behind, cards floating on it
  - fills as translucent greys, not solid ones
  - an Increased Contrast variant for every colour that needs one
  - tinted and pressed states derived from the accent rather than picked

So this takes one brand colour and derives the rest, keeping Apple's
relationships and replacing only the hue. Contrast is checked as it goes:
where the brand colour cannot meet 4.5:1 as text on the light surface --
which is most saturated brands, Apple's own blue included at 3.52:1 --
it says so and emits a darkened variant for text use rather than
pretending.

    python3 scripts/build_theme.py "#7A5AF8" --name violet
    python3 scripts/build_theme.py "#0F9D58" --name forest -o theme.css
"""

import argparse
import colorsys
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)

# Apple's own structure, from the measured tokens and the Color page.
# Only the hue is replaced; these relationships stay.
LABEL_BASE_LIGHT = (60, 60, 67)      # rgba(60,60,67,a) - the label ladder
LABEL_BASE_DARK = (235, 235, 245)
FILL_BASE_LIGHT = (116, 116, 128)
FILL_BASE_DARK = (118, 118, 128)
LABEL_ALPHAS = [("secondary", 0.60), ("tertiary", 0.30), ("quaternary", 0.18)]

# systemGray6 / secondarySystemGroupedBackground, from the Color page.
BG_LIGHT, CARD_LIGHT = "#F2F2F7", "#FFFFFF"
BG_DARK, CARD_DARK = "#000000", "#1C1C1E"


def hex_to_rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if not re.fullmatch(r"[0-9A-Fa-f]{6}", h):
        raise ValueError(f"not a hex colour: #{h}")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return "#{:02X}{:02X}{:02X}".format(*(max(0, min(255, round(c)))
                                          for c in rgb))


def luminance(rgb):
    def f(c):
        c /= 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (f(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def adjust_lightness(rgb, factor):
    """Scale lightness in HLS, keeping hue and saturation."""
    r, g, b = (c / 255 for c in rgb)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    l = max(0.0, min(1.0, l * factor))
    return tuple(c * 255 for c in colorsys.hls_to_rgb(h, l, s))


def meet_contrast(rgb, bg, target=4.5, darken=True):
    """Nudge lightness until the pair clears `target`, or give up.

    Apple's own accent does not clear 4.5:1 as text on white -- it is
    3.52:1 -- so this is the common case rather than the exception, and
    the honest output is a separate text-safe variant rather than
    silently altering the brand colour everywhere.
    """
    if contrast(rgb, bg) >= target:
        return rgb, True
    step = 0.97 if darken else 1.03
    cur = rgb
    for _ in range(60):
        cur = adjust_lightness(cur, step)
        if contrast(cur, bg) >= target:
            return cur, True
    return cur, False


def dark_variant(rgb):
    """Apple lightens accents for dark mode: #0088FF -> #0091FF."""
    return adjust_lightness(rgb, 1.06)


def build(brand_hex, name):
    brand = hex_to_rgb(brand_hex)
    accent_l = brand
    accent_d = dark_variant(brand)

    card_l, bg_l = hex_to_rgb(CARD_LIGHT), hex_to_rgb(BG_LIGHT)
    text_l, ok_l = meet_contrast(accent_l, card_l, 4.5)
    ic_l, _ = meet_contrast(accent_l, card_l, 7.0)

    notes = []
    ratio = contrast(accent_l, card_l)
    if ok_l and rgb_to_hex(text_l) != rgb_to_hex(accent_l):
        notes.append(
            f"the brand colour is {ratio:.2f}:1 on white, under the 4.5:1 "
            f"accessibility.md wants for text up to 17 pt, so "
            f"--{name}-accent-text is a darkened variant at "
            f"{contrast(text_l, card_l):.2f}:1. Apple's own accent has the "
            f"same problem at 3.52:1. Use the brand colour for fills and "
            f"the text variant for coloured text.")
    elif not ok_l:
        notes.append(
            f"the brand colour cannot reach 4.5:1 on white by lightness "
            f"alone (best {contrast(text_l, card_l):.2f}:1). Use it as a "
            f"fill behind white text, not as coloured text.")

    # White unless white cannot clear 3:1 -- not "whichever scores
    # higher". On Apple's own #0088FF black scores 5.97:1 against white's
    # 3.52:1, so picking the maximum would put black text on Apple's own
    # button, which Apple never does. Their practice is white on a
    # saturated fill, using the 3:1 that accessibility.md allows at bold,
    # and black only where white genuinely fails -- systemYellow, where
    # white is 1.51:1 and Apple does use dark text.
    white_ratio = contrast((255, 255, 255), accent_l)
    if white_ratio >= 3.0:
        on_accent = (255, 255, 255)
    else:
        on_accent = (0, 0, 0)
    notes.append(
        f"text on the accent fill is "
        f"{'white' if on_accent == (255,255,255) else 'black'} at "
        f"{contrast(on_accent, accent_l):.2f}:1 — a button label is "
        f"semibold, and accessibility.md allows 3:1 at bold."
        + ("" if on_accent == (255, 255, 255) else
           f" White would only reach {white_ratio:.2f}:1 here, so dark "
           f"text it is — the same call Apple makes on systemYellow."))

    L = [
        f"/* {name} — a design system in Apple's structure, your colour.",
        " *",
        " * Generated by scripts/build_theme.py. Apple's relationships are",
        " * kept and only the hue is replaced: the label ladder is one base",
        " * grey at several opacities so text composites correctly on any",
        " * surface, fills are translucent rather than solid, and the page",
        " * sits behind cards rather than the other way round.",
        " *",
        " * Load after tokens/ios-tokens.css to override the Apple palette,",
        " * or on its own if you want none of it.",
        " */",
        "",
        ":root {",
        f"  --{name}-accent: {rgb_to_hex(accent_l)};",
        f"  --{name}-accent-text: {rgb_to_hex(text_l)};",
        f"  --{name}-on-accent: {rgb_to_hex(on_accent)};",
        f"  --{name}-accent-tint: color-mix(in srgb, "
        f"var(--{name}-accent) 15%, transparent);",
        f"  --{name}-accent-pressed: color-mix(in srgb, "
        f"var(--{name}-accent) 85%, #000);",
        "",
        "  /* Label ladder: one grey, several opacities. */",
        f"  --{name}-label: #1A1A1A;",
    ]
    for label, a in LABEL_ALPHAS:
        L.append(f"  --{name}-label-{label}: "
                 f"rgba({LABEL_BASE_LIGHT[0]}, {LABEL_BASE_LIGHT[1]}, "
                 f"{LABEL_BASE_LIGHT[2]}, {a});")
    L += [
        "",
        f"  --{name}-fill: rgba({FILL_BASE_LIGHT[0]}, {FILL_BASE_LIGHT[1]}, "
        f"{FILL_BASE_LIGHT[2]}, 0.12);",
        f"  --{name}-separator: rgba(60, 60, 67, 0.29);",
        "",
        "  /* Page behind, cards on top. Getting this pair backwards is the",
        "     fastest way to look not-quite-right. */",
        f"  --{name}-bg: {BG_LIGHT};",
        f"  --{name}-bg-card: {CARD_LIGHT};",
        "}",
        "",
        "@media (prefers-color-scheme: dark) {",
        "  :root {",
        f"    --{name}-accent: {rgb_to_hex(accent_d)};",
        f"    --{name}-accent-text: {rgb_to_hex(accent_d)};",
        f"    --{name}-label: #F5F5F5;",
    ]
    for label, a in LABEL_ALPHAS:
        L.append(f"    --{name}-label-{label}: "
                 f"rgba({LABEL_BASE_DARK[0]}, {LABEL_BASE_DARK[1]}, "
                 f"{LABEL_BASE_DARK[2]}, {a});")
    L += [
        f"    --{name}-fill: rgba({FILL_BASE_DARK[0]}, {FILL_BASE_DARK[1]}, "
        f"{FILL_BASE_DARK[2]}, 0.24);",
        f"    --{name}-separator: rgba(84, 84, 88, 0.6);",
        f"    --{name}-bg: {BG_DARK};",
        f"    --{name}-bg-card: {CARD_DARK};",
        "  }",
        "}",
        "",
        "@media (prefers-contrast: more) {",
        "  :root {",
        f"    --{name}-accent-text: {rgb_to_hex(ic_l)};",
        f"    --{name}-label-secondary: rgba(60, 60, 67, 0.72);",
        "  }",
        "}",
        "",
        "/* Bridge to the apple-ui-kit component recipes, so .ios-btn and",
        "   the rest use this palette without being rewritten. */",
        ":root {",
        f"  --ios-accent: var(--{name}-accent);",
        f"  --ios-label: var(--{name}-label);",
        f"  --ios-label-secondary: var(--{name}-label-secondary);",
        f"  --ios-label-tertiary: var(--{name}-label-tertiary);",
        f"  --ios-bg: var(--{name}-bg);",
        f"  --ios-bg-card: var(--{name}-bg-card);",
        f"  --ios-separator: var(--{name}-separator);",
        "}",
        "",
    ]
    return "\n".join(L), notes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("colour", help='brand colour, e.g. "#7A5AF8"')
    ap.add_argument("--name", default="brand", help="token prefix")
    ap.add_argument("-o", "--out", help="write here instead of stdout")
    args = ap.parse_args()

    try:
        css, notes = build(args.colour, args.name)
    except ValueError as e:
        sys.exit(str(e))

    if args.out:
        open(args.out, "w", encoding="utf-8").write(css)
        print(f"wrote {args.out}")
    else:
        print(css)

    print("\n--- contrast ---", file=sys.stderr)
    for n in notes:
        print("  " + n, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
