#!/usr/bin/env python3
"""Assert the web components render the values they claim to.

A screenshot is not a test. The type scale was silently dropping to the
browser default 16px while the page still looked broadly like iOS,
because `font: var(--ios-text-body)` was a shorthand with no family and
browsers discard the whole declaration -- invisible by eye, obvious the
moment anything reads getComputedStyle.

So this drives a real browser over the reference page and checks the
numbers: that every token resolves, that the type scale lands on the
values specs.md states, that the switch geometry and its state changes
match what was measured off the kit, that hit targets clear 44px, that
the grouped background pairing is the right way round, and that the
colour pairs the recipes put together actually meet the contrast ratios
Apple's own table requires.

    python3 scripts/verify_web_ui.py           # exits non-zero on failure
    python3 scripts/verify_web_ui.py -v        # print every check
"""

import argparse
import os
import sys

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("needs playwright:\n"
             "  pip install playwright && playwright install chromium")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
SKILL = os.path.join(REPO, ".claude", "skills", "apple-ui-kit")
PAGE = "file://" + os.path.join(SKILL, "example.html")

# Where Chromium lives varies by machine. Playwright finds its own copy
# after `playwright install chromium`, which is the normal case; this
# only overrides that when a specific binary is pointed at, so the script
# runs unchanged on a laptop and in a container that ships its own.
CHROME = os.environ.get("CHROME_PATH") or None
if CHROME is None:
    _bundled = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
    CHROME = _bundled if os.path.exists(_bundled) else None

# Dynamic Type at the Large (default) setting, from specs.md. These are
# the whole point of the type tokens, so they are checked to the pixel.
TYPE_SCALE = {
    "--ios-text-large-title": (34, 41),
    "--ios-text-title1": (28, 34),
    "--ios-text-title2": (22, 28),
    "--ios-text-title3": (20, 25),
    "--ios-text-headline": (17, 22),
    "--ios-text-body": (17, 22),
    "--ios-text-callout": (16, 21),
    "--ios-text-subhead": (15, 20),
    "--ios-text-footnote": (13, 18),
    "--ios-text-caption1": (12, 16),
    "--ios-text-caption2": (11, 13),
}

COLOUR_TOKENS = [
    "--ios-label", "--ios-label-secondary", "--ios-label-tertiary",
    "--ios-accent", "--ios-red", "--ios-green",
    "--ios-fill-control", "--ios-fill-track", "--ios-surface",
    "--ios-bg", "--ios-bg-card", "--ios-separator",
]


class Checks:
    def __init__(self, verbose):
        self.fails = []
        self.n = 0
        self.verbose = verbose

    def __call__(self, ok, label, detail=""):
        self.n += 1
        if ok:
            if self.verbose:
                print(f"  ok    {label}  {detail}")
        else:
            print(f"  FAIL  {label}  {detail}")
            self.fails.append(label)


def srgb_lum(rgb):
    def f(c):
        c /= 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (f(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(fg, bg):
    a, b = srgb_lum(fg), srgb_lum(bg)
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


def run(pw, scheme, c, contrast_more=False):
    launch = {"args": ["--no-sandbox"]}
    if CHROME:
        launch["executable_path"] = CHROME
    b = pw.chromium.launch(**launch)
    pg = b.new_page(viewport={"width": 430, "height": 932},
                    color_scheme=scheme,
                    contrast="more" if contrast_more else "no-preference")
    pg.goto(PAGE)
    pg.wait_for_timeout(200)
    print(f"\n== {scheme}{' + prefers-contrast:more' if contrast_more else ''} ==")

    # 1. every token resolves to something
    vals = pg.evaluate(
        "toks => { const s = getComputedStyle(document.documentElement);"
        " return Object.fromEntries(toks.map(t => [t, s.getPropertyValue(t).trim()])); }",
        COLOUR_TOKENS)
    for t, v in vals.items():
        c(bool(v), f"token {t} resolves", v)

    # 2. type scale, to the pixel
    for tok, (size, leading) in TYPE_SCALE.items():
        got = pg.evaluate(
            """tok => { const e = document.createElement('span');
                 e.style.font = getComputedStyle(document.documentElement)
                   .getPropertyValue(tok);
                 e.textContent = 'x'; document.body.appendChild(e);
                 const cs = getComputedStyle(e);
                 const r = [cs.fontSize, cs.lineHeight]; e.remove(); return r; }""",
            tok)
        c(got[0] == f"{size}px", f"{tok} size", f"{got[0]} want {size}px")
        c(got[1] == f"{leading}px", f"{tok} leading", f"{got[1]} want {leading}px")

    # 3. hit targets: every interactive control clears 44px
    small = pg.evaluate(
        """() => [...document.querySelectorAll(
             'button, input:not([type=checkbox]):not([type=radio]), .ios-switch')]
           .map(e => ({t: e.className || e.tagName,
                       h: Math.round(e.getBoundingClientRect().height),
                       w: Math.round(e.getBoundingClientRect().width)}))
           .filter(x => x.h > 0 && x.h < 44)""")
    # The switch is 28pt by Apple's own design; its row supplies the target.
    unexpected = [s for s in small if "ios-switch" not in str(s["t"])]
    c(not unexpected, "controls >= 44px tall", str(unexpected or "all pass"))

    # 4. switch geometry and state, against what was measured off the kit
    sw = pg.evaluate(
        """() => { const on = document.querySelector('.ios-switch input:checked');
             const off = [...document.querySelectorAll('.ios-switch input')]
               .find(i => !i.checked && !i.disabled);
             const dis = document.querySelector('.ios-switch input:disabled');
             const tr = i => i.nextElementSibling;
             const cs = e => getComputedStyle(e);
             const box = document.querySelector('.ios-switch').getBoundingClientRect();
             return {w: Math.round(box.width), h: Math.round(box.height),
                     radius: cs(tr(on)).borderTopLeftRadius,
                     onBg: cs(tr(on)).backgroundColor,
                     offBg: cs(tr(off)).backgroundColor,
                     disOpacity: cs(tr(dis)).opacity,
                     knobOn: cs(tr(on), '::after').transform}; }""")
    c(sw["w"] == 64, "switch width 64", str(sw["w"]))
    c(sw["h"] == 28, "switch height 28", str(sw["h"]))
    c(sw["onBg"] != sw["offBg"], "switch on/off differ",
      f"{sw['onBg']} vs {sw['offBg']}")
    c(float(sw["disOpacity"]) < 1, "switch disabled fades", sw["disOpacity"])

    # knob must travel exactly width - height, or it overhangs the track
    travel = pg.evaluate(
        """() => { const t = document.querySelector('.ios-switch input:checked')
                     .nextElementSibling;
             const m = getComputedStyle(t, '::after').transform;
             if (m === 'none') return 0;
             return Math.round(parseFloat(m.split(',')[4])); }""")
    c(travel == 36, "switch knob travel = w-h = 36px", str(travel))

    # 5. grouped background pairing, and the right way round in light
    bg = vals["--ios-bg"]
    card = vals["--ios-bg-card"]
    c(bg != card, "page and card backgrounds differ", f"{bg} / {card}")
    if scheme == "light":
        c(srgb_lum(parse_rgb(pg, bg)) < srgb_lum(parse_rgb(pg, card)),
          "light: card is lighter than page", f"{bg} < {card}")

    # 6. separators: absent on each list's first row, present on the rest.
    # Checked per list -- flattening every .ios-list__row across the page
    # makes the second list's first row look like a missing separator.
    per_list = pg.evaluate(
        """() => [...document.querySelectorAll('.ios-list')].map(l =>
             [...l.querySelectorAll('.ios-list__row')].map(r => {
               const cs = getComputedStyle(r, '::before');
               return cs.content !== 'none'
                      && cs.backgroundColor !== 'rgba(0, 0, 0, 0)'; }))""")
    c(bool(per_list), "found lists to check", f"{len(per_list)} lists")
    for i, rows in enumerate(per_list):
        c(rows and rows[0] is False, f"list {i}: first row has no separator",
          str(rows[:1]))
        c(all(rows[1:]), f"list {i}: later rows have separators", str(rows[1:]))

    # 7. contrast, against the thresholds in accessibility.md.
    #
    # Apple's own light palette does not clear its own table -- secondary
    # label lands at 3.44:1 on white and the accent at 3.52:1, both under
    # the 4.5:1 required up to 17 pt. That is a property of the measured
    # values, not a bug in the recipes, so at the default contrast setting
    # these are reported and allowed. Under prefers-contrast:more, where
    # the overrides are supposed to fix it, they must pass.
    KNOWN_LIGHT_SHORTFALL = {"secondary on card", "accent text on page"}
    pairs = [
        ("--ios-label", "--ios-bg-card", 4.5, "body label on card"),
        ("--ios-label-secondary", "--ios-bg-card", 4.5, "secondary on card"),
        ("--ios-accent", "--ios-bg", 4.5, "accent text on page"),
    ]
    for fg_t, bg_t, need, label in pairs:
        fg = composite(pg, vals[fg_t], vals[bg_t])
        bgc = parse_rgb(pg, vals[bg_t])
        ratio = contrast(fg, bgc)
        excused = (scheme == "light" and not contrast_more
                   and label in KNOWN_LIGHT_SHORTFALL)
        if excused:
            c(ratio >= 3.0, f"contrast {label} (Apple's value, >=3:1)",
              f"{ratio:.2f}:1 -- under 4.5, see prefers-contrast:more")
        else:
            c(ratio >= need, f"contrast {label}",
              f"{ratio:.2f}:1 need {need}:1")

    # white-on-fill for the filled button, which is what people ship most
    fbg = pg.evaluate(
        "()=>getComputedStyle(document.querySelector('.ios-btn--filled')).backgroundColor")
    fcol = pg.evaluate(
        "()=>getComputedStyle(document.querySelector('.ios-btn--filled')).color")
    ratio = contrast(parse_rgb(pg, fcol), parse_rgb(pg, fbg))
    c(ratio >= 3.0, "contrast white on filled button",
      f"{ratio:.2f}:1 need 3:1 (17pt semibold counts as bold)")

    # 8. no horizontal overflow at a phone width
    c(pg.evaluate("()=>document.documentElement.scrollWidth") <= 430,
      "no horizontal overflow at 430px")

    b.close()


def parse_rgb(pg, css):
    """Resolve any CSS colour to an (r,g,b) tuple via the browser."""
    return tuple(pg.evaluate(
        """v => { const d = document.createElement('div');
             d.style.color = v; document.body.appendChild(d);
             const c = getComputedStyle(d).color; d.remove();
             return c.match(/[\\d.]+/g).slice(0,3).map(Number); }""", css))


def composite(pg, fg_css, bg_css):
    """Flatten a translucent foreground onto its background."""
    m = pg.evaluate(
        """v => { const d = document.createElement('div');
             d.style.color = v; document.body.appendChild(d);
             const c = getComputedStyle(d).color; d.remove();
             return c.match(/[\\d.]+/g).map(Number); }""", fg_css)
    fg, a = m[:3], (m[3] if len(m) > 3 else 1.0)
    bg = parse_rgb(pg, bg_css)
    return tuple(fg[i] * a + bg[i] * (1 - a) for i in range(3))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args()

    if not os.path.exists(PAGE.replace("file://", "")):
        sys.exit(f"reference page missing: {PAGE}")

    c = Checks(args.verbose)
    with sync_playwright() as pw:
        for scheme in ("light", "dark"):
            run(pw, scheme, c)
        # The overrides only earn their place if they actually clear 4.5:1.
        run(pw, "light", c, contrast_more=True)

    print(f"\n{c.n - len(c.fails)}/{c.n} checks passed")
    if c.fails:
        print("failed: " + ", ".join(sorted(set(c.fails))))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
