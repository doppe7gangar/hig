#!/usr/bin/env python3
"""Assert the macOS recipes render the values they were measured at.

Drives a real browser over mac-example.html and reads what the layout
engine actually produced: the window's corners, the traffic lights'
size, pitch and position, the toolbar band and its glass controls, the
sidebar's rows and inset, the menu's rows and its concentric highlight,
the alert's width and buttons, the sheet's corners, the type sizes, and
the colours in light, dark and Increased Contrast. Each expected number
is the one macos-components.css says it measured from Apple's own
screenshots, so a recipe that drifts from its comment fails here.

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


def rgb(css):
    m = re.findall(r"[\d.]+", css or "")
    if css and css.startswith("color(srgb"):
        return tuple(round(float(v) * 255) for v in m[:3])
    return tuple(round(float(v)) for v in m[:3])


def lum(c):
    def f(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2])


def ratio(a, b):
    x, y = lum(a), lum(b)
    return (max(x, y) + 0.05) / (min(x, y) + 0.05)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--verbose", action="store_true")
    a = ap.parse_args()
    results = []

    def check(label, ok, got=""):
        results.append((bool(ok), label, got))

    def near(label, got, want, tol=0.6):
        check(f"{label} = {want}", got is not None and abs(got - want) <= tol, f"got {got}")

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
                win, lights = box("#win"), box("#lights")
                dots = pg.evaluate("() => [...document.querySelectorAll('#lights > span')]"
                                   ".map(e => { const r = e.getBoundingClientRect();"
                                   " return [r.left + r.width / 2, r.top + r.height / 2, r.width]; })")
                if scheme == "light":
                    near("window corner radius", float(win["radius"][:-2]), 26)
                    near("traffic light diameter", dots[0][2], 14)
                    near("traffic light pitch", dots[1][0] - dots[0][0], 22)
                    near("close button centre from the window's left", dots[0][0] - win["x"], 25.5)
                    near("close button centre from the window's top", dots[0][1] - win["y"], 26, 0.6)
                    near("toolbar band height", box("#toolbar")["h"], 52)
                    tool = box("#tool")
                    near("toolbar glass control height", tool["h"], 36)
                    near("toolbar glass control is a circle", tool["w"], 36)
                    near("tab view height", box("#tabs")["h"], 36)
                    near("tool group height", box("#toolgroup")["h"], 36)
                    near("toolbar control centred on the traffic lights",
                         tool["y"] + tool["h"] / 2 - win["y"], 26)
                    near("push button height", box("#btn")["h"], 24)
                    near("default button height", box("#btn-default")["h"], 24)
                    near("text field height", box("#field")["h"], 26)
                    near("search field height", box("#search")["h"], 26)
                    near("pop-up height", box("#popup")["h"], 24)
                    near("segmented control height", box("#seg")["h"], 24)
                    side_a, side_b = box("#side-a"), box("#side-b")
                    near("sidebar row height", side_a["h"], 30)
                    near("sidebar row pitch", side_b["y"] - side_a["y"], 32)
                    near("sidebar row lines up with the close button", side_a["x"] - win["x"], 18.5)
                    near("sidebar text starts 54pt in", box("#side-a-text")["x"] - win["x"], 54, 1.0)
                    near("sidebar row corner radius", float(side_a["radius"][:-2]), 7)
                    head = box("#sidehead")
                    check("sidebar header is 11pt bold", head["font"] == "11px" and int(head["weight"]) >= 700,
                          f"{head['font']} {head['weight']}")
                    menu, hi = box("#menu"), box("#menu-hi")
                    near("menu corner radius", float(menu["radius"][:-2]), 11)
                    near("menu row height", hi["h"], 23.5)
                    near("menu highlight inset", hi["x"] - menu["x"], 5.5)
                    near("menu highlight radius, concentric", float(hi["radius"][:-2]), 5.5)
                    alert = box("#alert")
                    near("alert width", alert["w"], 260)
                    near("alert corner radius", float(alert["radius"][:-2]), 26)
                    b1, b2 = box("#alert-1"), box("#alert-2")
                    near("alert button height", b1["h"], 28)
                    near("alert buttons 6pt apart", b2["y"] - (b1["y"] + b1["h"]), 6)
                    near("alert buttons full width", b1["w"], 260 - 32)
                    near("sheet corner radius", float(box("#sheet")["radius"][:-2]), 19)
                    near("panel corner radius", float(box("#panel")["radius"][:-2]), 20)
                    body = box("#btn")
                    check("controls use 13pt text", body["font"] == "13px", body["font"])
                    t1, t2, sub = box("#title-sub"), box("#title-alone"), box("#subtitle")
                    check("a title over a subtitle is 13pt bold", t1["font"] == "13px" and int(t1["weight"]) >= 700,
                          f"{t1['font']} {t1['weight']}")
                    check("a title alone is 15pt bold", t2["font"] == "15px" and int(t2["weight"]) >= 700,
                          f"{t2['font']} {t2['weight']}")
                    check("subtitle is 11pt", sub["font"] == "11px", sub["font"])
                    fam = body["family"].lower()
                    check("text resolves to the system font, SF Pro or Inter",
                          "-apple-system" in fam or "sf pro" in fam or "inter" in fam, body["family"][:50])

                # Colours, per appearance.
                want = {"light": {"--mac-content-bg": (255, 255, 255), "--mac-sidebar-bg": (227, 227, 227),
                                  "--mac-accent": (0, 136, 255)},
                        "dark": {"--mac-content-bg": (30, 30, 30), "--mac-sidebar-bg": (39, 39, 39),
                                 "--mac-accent": (0, 145, 255)}}[scheme]
                for name, value in want.items():
                    check(f"{tag}: {name} is #{''.join(f'{v:02X}' for v in value)}", rgb(var(name)) == value, var(name))
                sel = rgb(box("#selrow td")["bg"])
                acc = want["--mac-accent"]
                k = 0.85 if scheme == "light" else 0.80
                expect = tuple(round(c * k) for c in acc)
                check(f"{tag}: a selected row is the accent darkened",
                      all(abs(x - y) <= 2 for x, y in zip(sel, expect)), f"{sel} vs {expect}")
                check(f"{tag}: white on a selected row clears 4.5:1",
                      ratio((255, 255, 255), sel) >= 4.5, f"{ratio((255, 255, 255), sel):.2f}:1")
                side = rgb(box("#side-a")["color"])
                check(f"{tag}: the selected sidebar row's text is the accent", side == acc, side)

                # A brand set on --mac-accent must survive the appearance.
                pg.evaluate("() => document.documentElement.style.setProperty('--mac-accent', '#2F7D5B')")
                got = rgb(box("#btn-default")["bg"])
                check(f"{tag}: a brand accent survives {scheme}", got == (47, 125, 91), got)
                pg.evaluate("() => document.documentElement.style.removeProperty('--mac-accent')")
            else:
                # Under Increased Contrast, text that was under 4.5:1 clears it.
                content = rgb(var("--mac-content-bg"))
                sec = var("--mac-label-secondary")
                m = re.findall(r"[\d.]+", sec)
                alpha = float(m[3]) if len(m) > 3 else 1.0
                fg = tuple(round(float(m[i]) * alpha + content[i] * (1 - alpha)) for i in range(3))
                check(f"{tag}: secondary text clears 4.5:1 on the content",
                      ratio(fg, content) >= 4.5, f"{ratio(fg, content):.2f}:1")
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
