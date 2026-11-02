#!/usr/bin/env python3
"""Assert the macOS recipes render the values they were measured at.

Drives a real browser over mac-example.html and reads what the layout
engine actually produced: the window's corners, the traffic lights'
size, pitch and position, the toolbar band and its glass controls, the
control heights and corners, the sidebar's width, rows and insets, the
menu's rows and highlight, the table's rows and selection, the alert's
width and buttons, the sheet's corners, the type, and the colours in
light, dark and Increased Contrast. Each expected number is the one
macos-components.css says Apple's macOS 27 kit carries, so a recipe that
drifts from its comment fails here.

    python3 verify_mac_ui.py        # from inside the skill
    python3 verify_mac_ui.py -v     # print every check
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
PAGE = "file://" + os.path.join(HERE, "mac-example.html")

BOX = """(sel) => { const e = document.querySelector(sel); if (!e) return null;
  const r = e.getBoundingClientRect(), s = getComputedStyle(e);
  return {x: r.left, y: r.top, w: r.width, h: r.height, radius: s.borderTopLeftRadius,
          font: s.fontSize, weight: s.fontWeight, lh: s.lineHeight, bg: s.backgroundColor,
          color: s.color, family: s.fontFamily}; }"""
# A custom property reads back as written ("#FFFFFF", "var(...)"), so a
# colour is resolved the way an element would: set it, read it computed.
COLOR = """(name) => { const e = document.createElement('span');
  e.style.color = 'var(' + name + ')'; document.body.appendChild(e);
  const c = getComputedStyle(e).color; e.remove(); return c; }"""
AFTER = """(sel) => { const s = getComputedStyle(document.querySelector(sel), '::after');
  return {w: parseFloat(s.width), h: parseFloat(s.height)}; }"""


def rgba(css):
    m = [float(v) for v in re.findall(r"[\d.]+", css or "")]
    if css and css.startswith("color(srgb"):
        return tuple(round(v * 255) for v in m[:3]) + ((m[3],) if len(m) > 3 else (1.0,))
    return tuple(round(v) for v in m[:3]) + ((m[3],) if len(m) > 3 else (1.0,))


def rgb(css):
    return rgba(css)[:3]


def over(fg, bg):
    """A translucent colour as it renders on an opaque one."""
    a = fg[3]
    return tuple(round(fg[i] * a + bg[i] * (1 - a)) for i in range(3))


def lum(c):
    def f(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2])


def ratio(a, b):
    x, y = lum(a), lum(b)
    return (max(x, y) + 0.05) / (min(x, y) + 0.05)


def hexs(c):
    return "#" + "".join(f"{v:02X}" for v in c)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--verbose", action="store_true")
    a = ap.parse_args()
    results = []

    def check(label, ok, got=""):
        results.append((bool(ok), label, got))

    def near(label, got, want, tol=0.6):
        check(f"{label} = {want}", got is not None and abs(got - want) <= tol, f"got {got}")

    def close(label, got, want, tol=2):
        check(f"{label} is {hexs(want)}", all(abs(x - y) <= tol for x, y in zip(got, want)), hexs(got))

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        for scheme, more in (("light", False), ("dark", False), ("light", True), ("dark", True)):
            kw = {"viewport": {"width": 1200, "height": 900}, "color_scheme": scheme}
            if more:
                kw["contrast"] = "more"
            pg = browser.new_page(**kw)
            pg.goto(PAGE)
            pg.wait_for_timeout(150)
            box = lambda sel: pg.evaluate(BOX, sel)
            var = lambda n: pg.evaluate(COLOR, n)
            tag = scheme + (" + Increased Contrast" if more else "")

            if not more:
                win = box("#win")
                dots = pg.evaluate("() => [...document.querySelectorAll('#lights > span')]"
                                   ".map(e => { const r = e.getBoundingClientRect();"
                                   " return [r.left + r.width / 2, r.top + r.height / 2, r.width]; })")
                if scheme == "light":
                    near("window corner radius", float(win["radius"][:-2]), 16)
                    near("traffic light diameter", dots[0][2], 14)
                    near("traffic light pitch", dots[1][0] - dots[0][0], 23)
                    near("close button centre from the window's left", dots[0][0] - win["x"], 26)
                    near("close button centre from the window's top", dots[0][1] - win["y"], 26)
                    near("toolbar band height", box("#toolbar")["h"], 52)
                    tool = box("#tool")
                    near("toolbar glass control height", tool["h"], 36)
                    near("toolbar glass control is a circle", tool["w"], 36)
                    near("toolbar segmented control height", box("#tabs")["h"], 36)
                    near("tool group height", box("#toolgroup")["h"], 36)
                    near("toolbar control centred on the traffic lights",
                         tool["y"] + tool["h"] / 2 - win["y"], 26)

                    btn = box("#btn")
                    near("push button height", btn["h"], 24)
                    near("push button corner radius", float(btn["radius"][:-2]), 6)
                    near("default button height", box("#btn-default")["h"], 24)
                    near("text field height", box("#field")["h"], 24)
                    near("search field height", box("#search")["h"], 24)
                    near("pop-up height", box("#popup")["h"], 24)
                    seg = box("#seg")
                    near("segmented control height", seg["h"], 24)
                    near("segmented control corner radius", float(seg["radius"][:-2]), 6)
                    sw = box("#switch")
                    check("switch is 54 x 24", abs(sw["w"] - 54) <= .6 and abs(sw["h"] - 24) <= .6,
                          f"{sw['w']} x {sw['h']}")
                    knob = pg.evaluate(AFTER, "#switch span")
                    check("switch knob is 32 x 20", abs(knob["w"] - 32) <= .6 and abs(knob["h"] - 20) <= .6,
                          f"{knob['w']} x {knob['h']}")
                    cb = box("#check")
                    check("checkbox is 16pt with 5.5pt corners",
                          abs(cb["w"] - 16) <= .6 and abs(float(cb["radius"][:-2]) - 5.5) <= .3,
                          f"{cb['w']} {cb['radius']}")

                    side = box("#sidebar")
                    side_a, side_b = box("#side-a"), box("#side-b")
                    near("sidebar width", side["w"], 240)
                    near("sidebar row height", side_a["h"], 32)
                    near("sidebar row pitch", side_b["y"] - side_a["y"], 32)
                    near("sidebar selection 10pt from the window's edge", side_a["x"] - win["x"], 10)
                    near("sidebar icon column starts 14pt in", box("#side-a-icon")["x"] - win["x"], 14)
                    near("sidebar text starts 42pt in", box("#side-a-text")["x"] - win["x"], 42, 1.0)
                    near("sidebar selection corner radius", float(side_a["radius"][:-2]), 8)
                    head = box("#sidehead")
                    check("sidebar header is 13pt bold", head["font"] == "13px" and int(head["weight"]) >= 700,
                          f"{head['font']} {head['weight']}")

                    menu, hi, item2 = box("#menu"), box("#menu-hi"), box("#menu-2")
                    near("menu corner radius", float(menu["radius"][:-2]), 12)
                    near("menu row height", hi["h"], 24)
                    near("menu rows start 5pt down", hi["y"] - menu["y"], 5)
                    near("menu highlight 5pt from the menu's side", hi["x"] - menu["x"], 5)
                    near("menu highlight corner radius", float(hi["radius"][:-2]), 8)
                    near("menu separator slot", box("#menu-head")["y"] - (item2["y"] + item2["h"]), 11)

                    table, sel, th = box("#table"), box("#selrow td"), box("#th")
                    near("table row height", sel["h"], 20)
                    near("table selection inset 10pt", sel["x"] - table["x"], 10)
                    near("table selection corner radius", float(sel["radius"][:-2]), 8)
                    near("table header height", th["h"], 28)
                    check("table header is 11pt", th["font"] == "11px", th["font"])

                    alert = box("#alert")
                    near("alert width", alert["w"], 260)
                    near("alert corner radius", float(alert["radius"][:-2]), 34)
                    b1, b2 = box("#alert-1"), box("#alert-2")
                    near("alert button height", b1["h"], 28)
                    near("alert buttons 6pt apart", b2["y"] - (b1["y"] + b1["h"]), 6)
                    near("alert buttons full width", b1["w"], 260 - 32)
                    check("alert message is 11pt", box("#am")["font"] == "11px", box("#am")["font"])
                    near("sheet corner radius", float(box("#sheet")["radius"][:-2]), 16)
                    near("panel corner radius", float(box("#panel")["radius"][:-2]), 16)

                    check("controls use 13pt Medium (510)", btn["font"] == "13px" and btn["weight"] == "510",
                          f"{btn['font']} {btn['weight']}")
                    t1, t2, sub = box("#title-sub"), box("#title-alone"), box("#subtitle")
                    check("a title over a subtitle is 13pt bold", t1["font"] == "13px" and int(t1["weight"]) >= 700,
                          f"{t1['font']} {t1['weight']}")
                    check("a title alone is 13pt bold", t2["font"] == "13px" and int(t2["weight"]) >= 700,
                          f"{t2['font']} {t2['weight']}")
                    check("subtitle is 11pt", sub["font"] == "11px", sub["font"])
                    fam = btn["family"].lower()
                    check("text resolves to the system font, SF Pro or Inter",
                          "-apple-system" in fam or "sf pro" in fam or "inter" in fam, btn["family"][:50])

                # Colours, per appearance.
                want = {"light": {"--mac-content-bg": (255, 255, 255), "--mac-sidebar-bg": (230, 230, 230),
                                  "--mac-accent": (0, 136, 255)},
                        "dark": {"--mac-content-bg": (30, 30, 30), "--mac-sidebar-bg": (22, 22, 22),
                                 "--mac-accent": (0, 145, 255)}}[scheme]
                for name, value in want.items():
                    close(f"{tag}: {name}", rgb(var(name)), value, 0)
                selection = {"light": (1, 101, 226), "dark": (0, 88, 208)}[scheme]
                row = rgb(box("#selrow td")["bg"])
                close(f"{tag}: a selected table row", row, selection, 0)
                check(f"{tag}: white on a selected row clears 4.5:1",
                      ratio((255, 255, 255), row) >= 4.5, f"{ratio((255, 255, 255), row):.2f}:1")
                hi_bg = rgb(box("#menu-hi")["bg"])
                close(f"{tag}: a highlighted menu item", hi_bg, (0, 105, 249), 0)
                check(f"{tag}: white on a highlighted menu item clears 4.5:1",
                      ratio((255, 255, 255), hi_bg) >= 4.5, f"{ratio((255, 255, 255), hi_bg):.2f}:1")
                sidebar_bg = rgb(var("--mac-sidebar-bg"))
                close(f"{tag}: the sidebar selection renders",
                      over(rgba(box("#side-a")["bg"]), sidebar_bg),
                      {"light": (217, 217, 217), "dark": (35, 35, 35)}[scheme])
                close(f"{tag}: a selected sidebar row keeps its text colour", rgb(box("#side-a-text")["color"]),
                      {"light": (26, 26, 26), "dark": (245, 245, 245)}[scheme], 0)
                close(f"{tag}: sidebar icons are the vibrant accent", rgb(box("#side-a-icon")["color"]),
                      {"light": (0, 120, 240), "dark": (10, 153, 255)}[scheme], 0)
                close(f"{tag}: sidebar headers are the vibrant secondary grey", rgb(box("#sidehead")["color"]),
                      {"light": (114, 114, 114), "dark": (138, 138, 138)}[scheme], 0)

                # A brand set on --mac-accent must survive the appearance.
                pg.evaluate("() => document.documentElement.style.setProperty('--mac-accent', '#2F7D5B')")
                got = rgb(box("#btn-default")["bg"])
                check(f"{tag}: a brand on --mac-accent survives {scheme}", got == (47, 125, 91), got)
                pg.evaluate("() => document.documentElement.style.removeProperty('--mac-accent')")
                # One bridged from theme.css reaches every accent surface.
                pg.evaluate("() => document.documentElement.style.setProperty('--ios-accent', '#2F7D5B')")
                got = {k: rgb(box(s)[p]) for k, s, p in (("default button", "#btn-default", "bg"),
                                                         ("selected row", "#selrow td", "bg"),
                                                         ("menu highlight", "#menu-hi", "bg"),
                                                         ("sidebar icon", "#side-a-icon", "color"))}
                bad = {k: v for k, v in got.items() if v != (47, 125, 91)}
                check(f"{tag}: a brand from theme.css fills the button, selections and sidebar icons",
                      not bad, bad)
                pg.evaluate("() => document.documentElement.style.removeProperty('--ios-accent')")
                # theme.css also sends a darker selection for white text.
                pg.evaluate("() => document.documentElement.style.setProperty('--mac-brand-selection', '#1F5A40')")
                got = (rgb(box("#selrow td")["bg"]), rgb(box("#menu-hi")["bg"]))
                check(f"{tag}: theme.css's selection colour fills rows and the menu highlight",
                      got == ((31, 90, 64), (31, 90, 64)), got)
                pg.evaluate("() => document.documentElement.style.removeProperty('--mac-brand-selection')")
            else:
                # Under Increased Contrast, text that was under 4.5:1 clears it.
                content = rgb(var("--mac-content-bg"))
                fg = over(rgba(var("--mac-label-secondary")), content)
                check(f"{tag}: secondary text clears 4.5:1 on the content",
                      ratio(fg, content) >= 4.5, f"{ratio(fg, content):.2f}:1")
                sidebar_bg = rgb(var("--mac-sidebar-bg"))
                head = rgb(box("#sidehead")["color"])
                check(f"{tag}: a sidebar header clears 4.5:1 on the sidebar",
                      ratio(head, sidebar_bg) >= 4.5, f"{ratio(head, sidebar_bg):.2f}:1")
                if scheme == "light":
                    fill = rgb(box("#btn-default")["bg"])
                    check(f"{tag}: white on the default button clears 4.5:1",
                          ratio((255, 255, 255), fill) >= 4.5, f"{ratio((255, 255, 255), fill):.2f}:1")
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
