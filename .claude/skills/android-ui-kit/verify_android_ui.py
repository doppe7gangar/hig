#!/usr/bin/env python3
"""Assert the Material 3 recipes render the values they were measured at.

Drives a real browser over android-example.html and reads what the layout
engine actually produced: the phone, the status and gesture bars, the
three top app bars, the nav bar and its indicator, buttons, FABs, icon
buttons, chips, cards, lists, the search bar, switches, checkboxes,
radios, text fields, the dialog, menu, tabs, bottom sheet, snackbar and
progress bar, the type, and every colour role in light and dark. The
expected numbers are written out here, from Google's Material 3 Design
Kit, not read back from the stylesheet -- so a recipe that drifts from
the kit fails rather than agreeing with itself.

It also holds build_m3_theme.py to the kit: seeded with the kit's own
#6750A4, the derived scheme has to land on the kit's colours, and a
brand theme has to reach every component through the role names.

    python3 verify_android_ui.py        # from inside the skill
    python3 verify_android_ui.py -v     # print every check
"""

import argparse
import os
import re
import sys

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("needs playwright:\n  pip install playwright && playwright install chromium")

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = "file://" + os.path.join(HERE, "android-example.html")
sys.path.insert(0, HERE)
import build_m3_theme  # noqa: E402
from icon import ICONS  # noqa: E402

BOX = """(sel) => { const e = document.querySelector(sel); if (!e) return null;
  const r = e.getBoundingClientRect(), s = getComputedStyle(e);
  return {x: r.left, y: r.top, w: r.width, h: r.height, right: r.right, bottom: r.bottom,
          radius: s.borderTopLeftRadius, radiusBR: s.borderBottomRightRadius,
          font: s.fontSize, weight: s.fontWeight, lh: s.lineHeight, track: s.letterSpacing,
          bg: s.backgroundColor, color: s.color, family: s.fontFamily, shadow: s.boxShadow,
          border: s.borderTopWidth, borderColor: s.borderTopColor, pl: s.paddingLeft, pr: s.paddingRight,
          pt: s.paddingTop, gap: s.columnGap}; }"""
PSEUDO = """([sel, which]) => { const e = document.querySelector(sel); if (!e) return null;
  const s = getComputedStyle(e, which);
  return {w: parseFloat(s.width), h: parseFloat(s.height), top: s.top, left: s.left, bg: s.backgroundColor,
          radius: s.borderTopLeftRadius, inset: s.top}; }"""

# The kit's scheme, both appearances.
KIT = {
    "light": {
        "primary": "#6750A4", "on-primary": "#FFFFFF", "primary-container": "#EADDFF",
        "on-primary-container": "#4F378A", "secondary": "#625B71", "on-secondary": "#FFFFFF",
        "secondary-container": "#E8DEF8", "on-secondary-container": "#4A4459", "tertiary": "#7D5260",
        "on-tertiary": "#FFFFFF", "tertiary-container": "#FFD8E4", "on-tertiary-container": "#633B48",
        "error": "#B3261E", "on-error": "#FFFFFF", "error-container": "#F9DEDC", "on-error-container": "#852221",
        "surface": "#FEF7FF", "surface-dim": "#DED8E1", "surface-bright": "#FEF7FF",
        "surface-container-lowest": "#FFFFFF", "surface-container-low": "#F7F2FA", "surface-container": "#F3EDF7",
        "surface-container-high": "#ECE6F0", "surface-container-highest": "#E6E0E9", "on-surface": "#1D1B20",
        "on-surface-variant": "#49454F", "outline": "#79747E", "outline-variant": "#CAC4D0",
        "inverse-surface": "#322F35", "inverse-on-surface": "#F5EFF7", "inverse-primary": "#D0BCFF",
    },
    "dark": {
        "primary": "#D0BCFE", "on-primary": "#381E72", "primary-container": "#4F378B",
        "on-primary-container": "#EADDFF", "secondary": "#CCC2DC", "on-secondary": "#332D41",
        "secondary-container": "#4A4458", "on-secondary-container": "#E8DEF8", "tertiary": "#EFB8C8",
        "on-tertiary": "#492532", "tertiary-container": "#633B48", "on-tertiary-container": "#FFD8E4",
        "error": "#F2B8B5", "on-error": "#601410", "error-container": "#8C1D18", "on-error-container": "#F9DEDC",
        "surface": "#141218", "surface-dim": "#141218", "surface-bright": "#3B383E",
        "surface-container-lowest": "#0F0D13", "surface-container-low": "#1D1B20", "surface-container": "#211F26",
        "surface-container-high": "#2B2930", "surface-container-highest": "#36343B", "on-surface": "#E6E0E9",
        "on-surface-variant": "#CAC4D0", "outline": "#938F99", "outline-variant": "#49454F",
        "inverse-surface": "#E6E0E9", "inverse-on-surface": "#322F35", "inverse-primary": "#6750A4",
    },
}
L1 = "rgba(0, 0, 0, 0.3) 0px 1px 2px 0px, rgba(0, 0, 0, 0.15) 0px 1px 3px 1px"
L3 = "rgba(0, 0, 0, 0.3) 0px 1px 3px 0px, rgba(0, 0, 0, 0.15) 0px 4px 8px 3px"

# Which element shows which role, as (selector, property, role).
SURFACES = [
    ("#phone-home", "bg", "surface"), ("#tab", "bg", "surface"), ("#nav", "bg", "surface-container"),
    ("#gesture", "bg", "surface-container"), ("#nav-active-icon", "bg", "secondary-container"),
    ("#nav-active-icon", "color", "on-secondary-container"), ("#nav-active-label", "color", "secondary"),
    ("#nav-item", "color", "on-surface-variant"), ("#tab-title", "color", "on-surface"),
    ("#tab-lead", "color", "on-surface"), ("#tab-more", "color", "on-surface-variant"),
    ("#search", "bg", "surface-container-high"), ("#chip-sel", "bg", "secondary-container"),
    ("#chip-sel", "color", "on-secondary-container"), ("#chip", "borderColor", "outline-variant"),
    ("#chip", "color", "on-surface-variant"), ("#fab", "bg", "primary-container"),
    ("#fab", "color", "on-primary-container"), ("#btn", "bg", "primary"), ("#btn", "color", "on-primary"),
    ("#btn-tonal", "bg", "secondary-container"), ("#btn-tonal", "color", "on-secondary-container"),
    ("#btn-outlined", "color", "on-surface-variant"), ("#btn-elevated", "bg", "surface-container-low"),
    ("#btn-elevated", "color", "primary"), ("#btn-text", "color", "primary"),
    ("#li-headline", "color", "on-surface"), ("#li-support", "color", "on-surface-variant"),
    ("#li-avatar", "bg", "primary-container"), ("#media-image", "bg", "surface-container-high"),
    ("#card-elevated", "bg", "surface-container-low"), ("#card-filled", "bg", "surface-container-highest"),
    ("#card-outlined", "bg", "surface"), ("#card-outlined", "borderColor", "outline-variant"),
    ("#card-subhead", "color", "on-surface-variant"), ("#dialog", "bg", "surface-container-high"),
    ("#dt", "color", "on-surface"), ("#dd", "color", "on-surface-variant"), ("#dialog-confirm", "color", "primary"),
    ("#menu", "bg", "surface-container-low"), ("#menu-item", "color", "on-surface"),
    ("#menu-divider", "bg", "outline-variant"), ("#tab-sel", "color", "primary"),
    ("#tab-off", "color", "on-surface-variant"), ("#tabs", "bg", "surface"),
    ("#sheet", "bg", "surface-container-low"), ("#sheet-handle", "bg", "outline"),
    ("#snackbar", "bg", "inverse-surface"), ("#snackbar-text", "color", "inverse-on-surface"),
    ("#snackbar-action", "color", "inverse-primary"), ("#field", "bg", "surface-container-highest"),
    ("#field-label", "color", "on-surface-variant"), ("#field-support", "color", "on-surface-variant"),
    ("#bg-sel", "bg", "secondary"), ("#bg-sel", "color", "on-secondary"),
    ("#bg-mid", "bg", "secondary-container"), ("#ib-filled", "color", "on-primary"),
    ("#ib-tonal", "color", "on-secondary-container"), ("#ib-standard", "color", "on-surface-variant"),
    ("#badge", "bg", "error"), ("#badge", "color", "on-error"),
]


def rgba(css):
    m = [float(v) for v in re.findall(r"[\d.]+", css or "")]
    return tuple(round(v) for v in m[:3]) + ((m[3],) if len(m) > 3 else (1.0,))


def rgb(css):
    return rgba(css)[:3]


def hexrgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))


def hexs(c):
    return "#" + "".join(f"{v:02X}" for v in c)


def ratio(a, b):
    def lum(c):
        def f(v):
            v /= 255
            return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
        return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2])
    x, y = lum(a), lum(b)
    return (max(x, y) + 0.05) / (min(x, y) + 0.05)


def px(v):
    return float(re.match(r"-?[\d.]+", v).group()) if v and re.match(r"-?[\d.]+", v) else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--verbose", action="store_true")
    a = ap.parse_args()
    results = []

    def check(label, ok, got=""):
        results.append((bool(ok), label, got))

    def near(label, got, want, tol=0.6):
        check(f"{label} = {want}", got is not None and abs(got - want) <= tol, f"got {got}")

    def font(label, b, size, lh, weight):
        check(f"{label} is {size}/{lh} at {weight}",
              (px(b["font"]), px(b["lh"]), int(b["weight"])) == (size, lh, weight),
              f"{b['font']}/{b['lh']} {b['weight']}")

    # ---- The theme generator against the kit, before any browser.
    sch = build_m3_theme.scheme("#6750A4")
    worst, within1, n = 0, 0, 0
    for mode in ("light", "dark"):
        for role, want in KIT[mode].items():
            d = max(abs(x - y) for x, y in zip(hexrgb(sch[mode][role]), hexrgb(want)))
            worst, n = max(worst, d), n + 1
            within1 += d <= 1
    check("build_m3_theme.py seeded #6750A4 reproduces the kit's 62 role colours within 3/255",
          worst <= 3 and n == 62, f"worst {worst}/255 over {n}")
    check("...and at least 59 of them within 1/255", within1 >= 59, f"{within1} of {n}")
    blue = build_m3_theme.hct((0, 0, 255))
    check("HCT of pure blue matches material-color-utilities (282.79, 87.23, 32.30)",
          abs(blue[0] - 282.788) < .01 and abs(blue[1] - 87.230) < .01 and abs(blue[2] - 32.302) < .01,
          tuple(round(v, 3) for v in blue))
    brand = build_m3_theme.scheme("#C1552E")
    bad = build_m3_theme.notes(brand)
    check("a brand scheme (#C1552E) keeps every text role at 4.5:1 or better", not bad, bad[:2])

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        for scheme in ("light", "dark"):
            pg = browser.new_page(viewport={"width": 1900, "height": 1100}, color_scheme=scheme)
            pg.goto(PAGE)
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(150)
            box = lambda sel: pg.evaluate(BOX, sel)
            pseudo = lambda sel, which: pg.evaluate(PSEUDO, [sel, which])
            kit = KIT[scheme]

            # ---- Colours: every component shows the role the kit gives it.
            for sel, prop, role in SURFACES:
                b = box(sel)
                got = rgb(b[prop]) if b else None
                check(f"{scheme}: {sel} {prop} is {role} {kit[role]}", got == hexrgb(kit[role]),
                      hexs(got) if got else "missing")
            # Unselected switch and on switch tracks, the scrim, the camera.
            check(f"{scheme}: an off switch track is surface-container-highest",
                  rgb(box("#switch-off span")["bg"]) == hexrgb(kit["surface-container-highest"]),
                  box("#switch-off span")["bg"])
            check(f"{scheme}: an on switch track is primary",
                  rgb(box("#switch-on span")["bg"]) == hexrgb(kit["primary"]), box("#switch-on span")["bg"])
            check(f"{scheme}: the on handle is on-primary",
                  rgb(pseudo("#switch-on span", "::before")["bg"]) == hexrgb(kit["on-primary"]),
                  pseudo("#switch-on span", "::before")["bg"])
            check(f"{scheme}: the off handle is outline",
                  rgb(pseudo("#switch-off span", "::before")["bg"]) == hexrgb(kit["outline"]),
                  pseudo("#switch-off span", "::before")["bg"])
            sc = rgba(box("#scrim")["bg"])
            check(f"{scheme}: the scrim is black at 32%", sc[:3] == (0, 0, 0) and abs(sc[3] - .32) < .01, sc)
            check(f"{scheme}: a checked checkbox fills with primary",
                  rgb(box("#check input")["bg"]) == hexrgb(kit["primary"]), box("#check input")["bg"])
            check(f"{scheme}: an unchecked checkbox is a 2 dp on-surface-variant outline",
                  (px(box("#check-off input")["border"]), rgb(box("#check-off input")["borderColor"]))
                  == (2, hexrgb(kit["on-surface-variant"])), box("#check-off input")["borderColor"])
            check(f"{scheme}: the selected tab's indicator is primary",
                  rgb(pseudo("#tab-sel-label", "::after")["bg"]) == hexrgb(kit["primary"]),
                  pseudo("#tab-sel-label", "::after")["bg"])
            # Text on its container clears 4.5:1 in this appearance.
            for fg_sel, fg_prop, bg_sel in (("#btn", "color", "#btn"), ("#nav-active-label", "color", "#nav"),
                                            ("#nav-item", "color", "#nav"), ("#li-support", "color", "#phone-home"),
                                            ("#dd", "color", "#dialog"), ("#snackbar-text", "color", "#snackbar"),
                                            ("#chip-sel", "color", "#chip-sel"), ("#field-label", "color", "#field")):
                r = ratio(rgb(box(fg_sel)[fg_prop]), rgb(box(bg_sel)["bg"]))
                check(f"{scheme}: {fg_sel} text clears 4.5:1 on its background", r >= 4.5, f"{r:.2f}:1")

            if scheme == "dark":
                # data-theme="light" pins light on a dark system.
                pg.evaluate("() => document.documentElement.dataset.theme = 'light'")
                check("dark system + data-theme=light: the surface is the light one",
                      rgb(box("#phone-home")["bg"]) == hexrgb(KIT["light"]["surface"]), box("#phone-home")["bg"])
                pg.close()
                continue

            # ---- Geometry (light; dark changes no sizes).
            dev = pg.evaluate("""() => { const e = document.querySelector('#phone-home'), s = getComputedStyle(e);
                return {w: e.clientWidth, h: e.clientHeight, border: s.borderTopWidth, radius: s.borderTopLeftRadius}; }""")
            check("the phone is 412 x 917 dp inside an 8 dp bezel with 36 dp corners",
                  (dev["w"], dev["h"], px(dev["border"]), px(dev["radius"])) == (412, 917, 8, 36), dev)
            check("the bezel is outline-variant", rgb(pg.evaluate(
                "() => getComputedStyle(document.querySelector('#phone-home')).borderTopColor"))
                == hexrgb(KIT["light"]["outline-variant"]))
            near("status bar height", box("#sb")["h"], 52)
            font("status bar time", box("#sb"), 14, 20, 500)
            near("status bar padding", px(box("#sb")["pl"]), 24)
            cam = pseudo("#sb", "::after")
            check("camera cutout is a 24 dp circle 18 dp from the top",
                  (cam["w"], cam["h"], px(cam["top"])) == (24, 24, 18), cam)
            near("gesture bar height", box("#gesture")["h"], 24)
            hd = pseudo("#gesture", "::after")
            check("gesture handle is 108 x 4", (hd["w"], hd["h"]) == (108, 4), hd)

            bar, title = box("#tab"), box("#tab-title")
            near("small top app bar height", bar["h"], 64)
            near("title starts 56 dp in, after the leading button", title["x"] - bar["x"], 56)
            font("small app bar title (title-large)", title, 22, 28, 400)
            near("icon button target", box("#tab-lead")["w"], 48)
            near("icon button container", pseudo("#ib-tonal", "::before")["w"], 40)
            med, mt = box("#tab-medium"), box("#tab-medium-title")
            near("medium flexible app bar height", med["h"], 112)
            near("medium title text 16 dp in", mt["x"] + px(mt["pl"]) - med["x"], 16)
            font("medium title (headline-medium, emphasized)", mt, 28, 36, 500)
            near("medium title 12 dp above the bar's bottom", med["bottom"] - mt["bottom"], 12)
            lg, lt = box("#tab-large"), box("#tab-large-title")
            near("large flexible app bar height", lg["h"], 120)
            font("large title (display-small, emphasized)", lt, 36, 44, 500)
            c, ct = box("#tab-center"), box("#tab-center-title")
            near("centre-aligned title is centred", (ct["x"] + ct["w"] / 2) - (c["x"] + c["w"] / 2), 0, 1)

            nav, ind, lab = box("#nav"), box("#nav-active-icon"), box("#nav-active-label")
            near("nav bar height", nav["h"], 64)
            check("active indicator is 56 x 32 with 16 dp corners",
                  (ind["w"], ind["h"], px(ind["radius"])) == (56, 32, 16), (ind["w"], ind["h"], ind["radius"]))
            near("indicator 6 dp below the bar's top", ind["y"] - nav["y"], 6)
            near("label 4 dp under the indicator", lab["y"] - ind["bottom"], 4)
            font("nav label (label-medium)", lab, 12, 16, 500)
            check("the active destination draws its filled glyph",
                  pg.evaluate("() => document.querySelector('#nav-active-icon path').getAttribute('d')")
                  == ICONS["home"]["fill"])
            near("navigation rail width", box("#rail")["w"], 96)

            b = box("#btn")
            near("button height", b["h"], 40)
            check("button is fully round", px(b["radius"]) >= 20, b["radius"])
            near("button side padding", px(b["pr"]), 16)
            font("button label (label-large)", b, 14, 20, 500)
            near("button icon", pg.evaluate("() => document.querySelector('#btn svg').getBoundingClientRect().width"), 20)
            near("button icon-to-label gap", px(b["gap"]), 8)
            check("an outlined button's border is 1 dp outline-variant",
                  "inset" in box("#btn-outlined")["shadow"] and "1px" in box("#btn-outlined")["shadow"],
                  box("#btn-outlined")["shadow"])
            check("an elevated button sits at level 1", box("#btn-elevated")["shadow"] == L1, box("#btn-elevated")["shadow"])
            near("text button padding", px(box("#btn-text")["pl"]), 12)
            bm = box("#btn-medium")
            check("medium button: 56 tall, 24 dp padding, title-medium",
                  (bm["h"], px(bm["pl"]), px(bm["font"]), px(bm["lh"])) == (56, 24, 16, 24), bm)
            target = pseudo("#btn", "::after")
            near("button touch target", target["h"], 48)

            f = box("#fab")
            check("FAB is 56 dp with 16 dp corners at level 3",
                  (f["w"], f["h"], px(f["radius"]), f["shadow"]) == (56, 56, 16, L3), (f["w"], f["radius"], f["shadow"]))
            phone = box("#phone-home")
            near("FAB 16 dp from the screen's right edge", phone["right"] - 8 - f["right"], 16)
            near("FAB 16 dp above the nav bar", nav["y"] - f["bottom"], 16)
            fm, fl = box("#fab-medium"), box("#fab-large")
            check("medium FAB 80 dp, 20 dp corners", (fm["w"], px(fm["radius"])) == (80, 20), (fm["w"], fm["radius"]))
            check("large FAB 96 dp, 28 dp corners", (fl["w"], px(fl["radius"])) == (96, 28), (fl["w"], fl["radius"]))

            ch, cs, row = box("#chip"), box("#chip-sel"), box("#chips")
            check("chip: 32 tall, 8 dp corners, 1 dp border, 16 dp padding",
                  (ch["h"], px(ch["radius"]), px(ch["border"]), px(ch["pl"])) == (32, 8, 1, 16), ch)
            near("selected chip leads with its check 8 dp in", px(cs["pl"]), 8)
            near("selected chip's check", pg.evaluate("() => document.querySelector('#chip-sel svg').getBoundingClientRect().width"), 18)
            check("chip row: 8 dp padding, 4 dp apart", (px(row["pt"]), px(row["gap"])) == (8, 4), (row["pt"], row["gap"]))
            check("elevated assist chip sits at level 1", box("#chip-elevated")["shadow"] == L1)

            check("cards have 12 dp corners", all(px(box(s)["radius"]) == 12 for s in
                                                  ("#card-elevated", "#card-filled", "#card-outlined")))
            check("an elevated card sits at level 1", box("#card-elevated")["shadow"] == L1, box("#card-elevated")["shadow"])
            font("card title (title-medium)", box("#card-title"), 16, 24, 500)
            check("media tile image has 16 dp corners", px(box("#media-image")["radius"]) == 16)
            font("media title (title-small)", box("#media-title"), 14, 20, 500)
            font("media meta (body-small)", box("#media-meta"), 12, 16, 400)

            near("two-line list item", box("#li-2l")["h"], 72)
            near("three-line list item", box("#li-3l")["h"], 88)
            near("one-line list item", box("#li-1l")["h"], 56)
            near("list side padding", px(box("#li-2l")["pl"]), 16)
            near("list avatar", box("#li-avatar")["w"], 40)
            th = box("#li-thumb")
            check("list thumbnail 56 dp with 16 dp corners", (th["w"], px(th["radius"])) == (56, 16), th)
            font("list headline (body-large)", box("#li-headline"), 16, 24, 400)
            font("list supporting text (body-medium)", box("#li-support"), 14, 20, 400)
            font("list trailing text (label-small)", box("#li-trailing"), 11, 16, 500)
            check("section header: 48 tall, title-large",
                  (box("#section")["h"], px(box("#section")["font"])) == (48, 22), box("#section"))

            s = box("#search")
            check("search bar: 56 tall, fully round", (s["h"], px(s["radius"])) == (56, 28), (s["h"], s["radius"]))

            tr = box("#switch-off span")
            check("switch track 52 x 32", (tr["w"], tr["h"]) == (52, 32), (tr["w"], tr["h"]))
            ho = pg.evaluate("() => { const t = document.querySelector('#switch-off span').getBoundingClientRect();"
                             " const s = getComputedStyle(document.querySelector('#switch-off span'), '::before');"
                             " return [parseFloat(s.width), parseFloat(s.left) + 2 + parseFloat(s.width) / 2]; }")
            check("off handle: 16 dp, centred 16 dp from the track's start", ho == [16, 16], ho)
            hn = pg.evaluate("() => { const s = getComputedStyle(document.querySelector('#switch-on span'), '::before');"
                             " return [parseFloat(s.width), parseFloat(s.left) + 2 + parseFloat(s.width) / 2]; }")
            check("on handle: 24 dp, centred 16 dp from the track's end", hn == [24, 36], hn)
            cb = box("#check input")
            check("checkbox 18 dp with 2 dp corners", (cb["w"], px(cb["radius"])) == (18, 2), cb)
            near("checkbox target", box("#check")["h"], 48)
            near("radio ring", box("#radio input")["w"], 20)
            near("radio target", box("#radio")["h"], 48)
            near("radio dot", pseudo("#radio input", "::after")["w"], 10)

            fd, fe = box("#field"), box("#field-empty")
            check("filled field: 56 tall, 4 dp top corners, square bottom",
                  (fd["h"], px(fd["radius"]), px(fd["radiusBR"])) == (56, 4, 0), (fd["h"], fd["radius"], fd["radiusBR"]))
            check("its indicator is 1 dp of on-surface-variant",
                  "inset" in fd["shadow"] and "-1px" in fd["shadow"], fd["shadow"])
            font("an empty field's label (body-large)", box("#field-empty-label"), 16, 24, 400)
            font("a filled field's label (body-small)", box("#field-label"), 12, 16, 400)
            pg.focus("#field-empty input")
            pg.wait_for_timeout(300)  # past the 150 ms transition
            fe2 = box("#field-empty")
            check("focused, the indicator is 3 dp of primary",
                  "-3px" in fe2["shadow"] and rgb(fe2["shadow"]) == hexrgb(KIT["light"]["primary"]), fe2["shadow"])
            check("focused, the label rises and turns primary",
                  (px(box("#field-empty-label")["font"]), rgb(box("#field-empty-label")["color"]))
                  == (12, hexrgb(KIT["light"]["primary"])))
            pg.evaluate("() => document.activeElement.blur()")
            fo = box("#field-out")
            check("outlined field: 4 dp corners, 1 dp outline",
                  px(fo["radius"]) == 4 and "1px" in fo["shadow"] and rgb(fo["shadow"]) == hexrgb(KIT["light"]["outline"]),
                  fo["shadow"])
            font("supporting text (body-small)", box("#field-support"), 12, 16, 400)
            near("supporting text 16 dp in", px(box("#field-support")["pl"]), 16)

            d, conf = box("#dialog"), box("#dialog-confirm")
            check("dialog: 312 wide, 28 dp corners, 24 dp padding",
                  (d["w"], px(d["radius"]), px(d["pl"])) == (312, 28, 24), (d["w"], d["radius"], d["pl"]))
            font("dialog title (headline-small)", box("#dt"), 24, 32, 400)
            font("dialog text (body-medium)", box("#dd"), 14, 20, 400)
            near("dialog actions end 24 dp from the right", d["right"] - conf["right"], 24)
            near("dialog actions 24 dp above the bottom", d["bottom"] - conf["bottom"], 24)
            near("dialog actions 24 dp under the text", conf["y"] - box("#dd")["bottom"], 24)

            m, mi = box("#menu"), box("#menu-item")
            check("menu: 16 dp corners, level 3", (px(m["radius"]), m["shadow"]) == (16, L3), (m["radius"], m["shadow"]))
            near("menu item row", mi["h"], 44)
            near("menu item pitch (row plus its 2 dp insets)", mi["y"] - m["y"], 4)
            near("menu item inset from the sides", mi["x"] - m["x"], 4)
            font("menu item (label-large)", mi, 14, 20, 500)
            near("menu icon", pg.evaluate("() => document.querySelector('#menu-item svg').getBoundingClientRect().width"), 20)

            t, ts = box("#tabs"), box("#tab-sel")
            near("tabs height", t["h"], 48)
            font("tab label (title-small)", ts, 14, 20, 500)
            near("tab indicator height", pseudo("#tab-sel-label", "::after")["h"], 3)

            sh, hd2 = box("#sheet"), box("#sheet-handle")
            check("bottom sheet: 28 dp top corners, square bottom",
                  (px(sh["radius"]), px(sh["radiusBR"])) == (28, 0), (sh["radius"], sh["radiusBR"]))
            check("drag handle 32 x 4, 16 dp from the top", (hd2["w"], hd2["h"], hd2["y"] - sh["y"]) == (32, 4, 16), hd2)

            sn = box("#snackbar")
            check("snackbar: 48 tall, 4 dp corners, 16 dp before the text, level 3",
                  (sn["h"], px(sn["radius"]), px(sn["pl"]), sn["shadow"]) == (48, 4, 16, L3), sn)
            font("snackbar text (body-medium)", box("#snackbar-text"), 14, 20, 400)

            near("linear progress track", box("#progress")["h"], 4)
            check("progress: the done part is primary",
                  rgb(pseudo("#progress", "::before")["bg"]) == hexrgb(KIT["light"]["primary"]))

            g, gs = box("#btngroup"), box("#bg-sel")
            check("connected group: 2 dp apart, the selected one fully round",
                  (px(g["gap"]), px(gs["radius"])) == (2, 20), (g["gap"], gs["radius"]))

            # ---- Type and icons.
            check("Roboto loaded, variable weight", pg.evaluate(
                "() => document.fonts.check('500 14px Roboto') && [...document.fonts].some(f => f.family === 'Roboto' && f.status === 'loaded')"))
            check("text renders in Roboto", box("#tab-title")["family"].startswith('Roboto'), box("#tab-title")["family"])
            icons = pg.evaluate("() => [...document.querySelectorAll('svg[data-icon]')].map(s => [s.dataset.icon, s.getAttribute('viewBox'), s.querySelector('path').getAttribute('d')])")
            bad = [i[0] for i in icons if i[1] != "0 0 24 24" or i[0] not in ICONS
                   or i[2] not in (ICONS[i[0]]["outline"], ICONS[i[0]]["fill"])]
            check(f"all {len(icons)} icons are Material Symbols drawn for 24 dp", icons and not bad, bad[:3])

            # ---- A brand theme reaches every component through the roles.
            css = build_m3_theme.to_css(brand, "#C1552E")
            pg.add_style_tag(content=css)
            pg.wait_for_timeout(300)  # the nav indicator eases to its new colour
            want = {"#btn": ("bg", "primary"), "#nav-active-icon": ("bg", "secondary-container"),
                    "#fab": ("bg", "primary-container"), "#phone-home": ("bg", "surface"),
                    "#dialog": ("bg", "surface-container-high"), "#tab-sel": ("color", "primary")}
            got = {k: hexs(rgb(box(k)[p])) for k, (p, r) in want.items()}
            miss = {k: v for k, v in got.items() if v != brand["light"][want[k][1]]}
            check("theme.css from a brand seed recolours the button, nav, FAB, surfaces, dialog and tabs",
                  not miss, miss)
            pg.evaluate("() => document.documentElement.dataset.theme = 'dark'")
            pg.wait_for_timeout(300)
            got = hexs(rgb(box("#btn")["bg"]))
            check("...and its dark scheme follows data-theme=dark", got == brand["dark"]["primary"], got)
            pg.close()
        browser.close()

    failed = [r for r in results if not r[0]]
    for ok, label, got in results:
        if a.verbose or not ok:
            print(f"  {'ok  ' if ok else 'FAIL'} {label}" + ("" if ok else f"  ({got})"))
    print(f"\n{len(results) - len(failed)}/{len(results)} checks passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
