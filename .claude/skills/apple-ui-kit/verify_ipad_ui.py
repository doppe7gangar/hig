#!/usr/bin/env python3
"""Assert the iPadOS recipes render the values they were measured at.

Drives a real browser over ipad-example.html and reads what the layout
engine produced: the iPad's screen and corners, the 32pt status bar with
the app's menu, the 320pt glass sidebar -- its toolbar, search field,
44pt rows, symbol column, selection capsule and section headers -- the
top toolbar's floating glass controls, the tab bar at the top centre,
the title block, the sheet with its grabber, the popover and the dim,
in light and dark. The expected numbers are written out here, from
Apple's iOS and iPadOS 27 design kit, not read back from the
stylesheet, so a recipe that drifts from the kit fails.

    python3 verify_ipad_ui.py        # from inside the skill
    python3 verify_ipad_ui.py -v     # print every check
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
PAGE = "file://" + os.path.join(HERE, "ipad-example.html")

BOX = """(sel) => { const e = document.querySelector(sel); if (!e) return null;
  const r = e.getBoundingClientRect(), s = getComputedStyle(e);
  return {x: r.left, y: r.top, w: r.width, h: r.height, right: r.right, bottom: r.bottom,
          radius: s.borderTopLeftRadius, font: s.fontSize, lh: s.lineHeight, weight: s.fontWeight,
          bg: s.backgroundColor, color: s.color, shadow: s.boxShadow,
          pt: s.paddingTop, pr: s.paddingRight, pb: s.paddingBottom, pl: s.paddingLeft,
          mb: s.marginBottom, mt: s.marginTop, gap: s.columnGap}; }"""
PSEUDO = """([sel, which]) => { const s = getComputedStyle(document.querySelector(sel), which);
  return {w: parseFloat(s.width), h: parseFloat(s.height), left: s.left, bg: s.backgroundColor}; }"""

# The kit's values per appearance. Sidebar dark, popover dark and the
# grabber dark are chosen (the kit draws them light only) and are held
# here so they don't drift either.
KIT = {
    "light": {"label": (0, 0, 0), "vibrant": (26, 26, 26), "vibrant2": (114, 114, 114),
              "accent": (0, 136, 255), "content": (255, 255, 255), "grouped": (242, 242, 247),
              "sidebar": (218, 218, 218), "selection": (200, 200, 200), "tabsel": (237, 237, 237)},
    "dark": {"label": (255, 255, 255), "vibrant": (245, 245, 245), "vibrant2": (138, 138, 138),
             "accent": (0, 145, 255), "content": (0, 0, 0), "grouped": (0, 0, 0),
             "sidebar": (30, 30, 32), "selection": (52, 52, 54), "tabsel": (18, 18, 18)},
}


def rgba(css):
    m = [float(v) for v in re.findall(r"[\d.]+", css or "")]
    return tuple(round(v) for v in m[:3]) + ((m[3],) if len(m) > 3 else (1.0,))


def rgb(css):
    return rgba(css)[:3]


def over(fg, bg):
    a = fg[3]
    return tuple(round(fg[i] * a + bg[i] * (1 - a)) for i in range(3))


def px(v):
    m = re.match(r"-?[\d.]+", v or "")
    return float(m.group()) if m else None


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
        for scheme in ("light", "dark"):
            pg = browser.new_page(viewport={"width": 1400, "height": 1000}, color_scheme=scheme)
            pg.goto(PAGE)
            pg.wait_for_function("() => document.fonts.status === 'loaded'", timeout=10000)
            pg.wait_for_timeout(200)
            box = lambda sel: pg.evaluate(BOX, sel)
            pseudo = lambda sel, which: pg.evaluate(PSEUDO, [sel, which])
            k = KIT[scheme]

            # ---- Colours in this appearance.
            side, row, sel = box("#sidebar"), box("#row"), box("#row-selected")
            check(f"{scheme}: the sidebar is {k['sidebar']}", rgb(side["bg"]) == k["sidebar"], side["bg"])
            check(f"{scheme}: the selected row's capsule", over(rgba(sel["bg"]), k["sidebar"]) == k["selection"],
                  sel["bg"])
            check(f"{scheme}: row titles are the plain label", rgb(box("#row-title")["color"]) == k["label"],
                  box("#row-title")["color"])
            check(f"{scheme}: row detail is the vibrant secondary label",
                  rgb(box("#row-detail")["color"]) == k["vibrant2"], box("#row-detail")["color"])
            check(f"{scheme}: sidebar symbols take the accent",
                  rgb(box("#row .ipad-sidebar__icon")["color"]) == k["accent"],
                  box("#row .ipad-sidebar__icon")["color"])
            check(f"{scheme}: the grouped content behind the list", rgb(box("#content")["bg"]) == k["grouped"],
                  box("#content")["bg"])
            check(f"{scheme}: the tab layout's content is the primary background",
                  rgb(box("#content-tabs")["bg"]) == k["content"], box("#content-tabs")["bg"])
            check(f"{scheme}: the title is the vibrant label", rgb(box("#title-text")["color"]) == k["vibrant"],
                  box("#title-text")["color"])
            check(f"{scheme}: the subtitle is the vibrant secondary label",
                  rgb(box("#subtitle")["color"]) == k["vibrant2"], box("#subtitle")["color"])
            check(f"{scheme}: unselected tabs are the vibrant label", rgb(box("#tab")["color"]) == k["vibrant"],
                  box("#tab")["color"])
            check(f"{scheme}: the selected tab sits on the neutral capsule",
                  rgb(box("#tab-selected")["bg"]) == k["tabsel"], box("#tab-selected")["bg"])
            check(f"{scheme}: the selected tab takes the accent", rgb(box("#tab-selected")["color"]) == k["accent"],
                  box("#tab-selected")["color"])
            check(f"{scheme}: glass controls are monochrome", rgb(box("#group button")["color"]) == k["vibrant"],
                  box("#group button")["color"])
            check(f"{scheme}: the status bar is the plain label", rgb(box("#statusbar")["color"]) == k["label"],
                  box("#statusbar")["color"])
            sc = rgba(box("#scrim")["bg"])
            check(f"{scheme}: a sheet dims the window 20% black", sc[:3] == (0, 0, 0) and abs(sc[3] - .2) < .01, sc)

            if scheme == "dark":
                pg.close()
                continue

            # ---- Geometry (light; dark changes no sizes).
            dev = pg.evaluate("""() => { const e = document.querySelector('#ipad-split'), s = getComputedStyle(e);
                return {w: e.clientWidth, h: e.clientHeight, b: s.borderTopWidth, r: s.borderTopLeftRadius}; }""")
            check("the iPad Pro 11-inch screen, 1210 x 834, with 30pt corners inside the bezel",
                  (dev["w"], dev["h"], px(dev["r"]) - px(dev["b"])) == (1210, 834, 30), dev)
            sb = box("#statusbar")
            check("status bar: 32pt, 16pt in, 14pt medium", (sb["h"], px(sb["pl"]), px(sb["font"]), sb["weight"])
                  == (32, 16, 14, "510"), sb)
            check("the app's menu is its name in bold", box("#statusbar-app")["weight"] == "700",
                  box("#statusbar-app")["weight"])

            check("sidebar: 320pt wide", side["w"] == 320, side["w"])
            check("sidebar: 32pt under the status bar, 10pt in",
                  (px(side["pt"]), px(side["pl"]), px(side["pr"])) == (32, 10, 10), (side["pt"], side["pl"]))
            ed, ci = box("#edit"), box("#circle")
            check("Edit is a 44pt glass capsule", ed["h"] == 44 and px(ed["radius"]) >= 22, (ed["h"], ed["radius"]))
            check("a lone symbol is a 44pt glass circle", (ci["w"], ci["h"]) == (44, 44), (ci["w"], ci["h"]))
            check("glass controls carry the kit's 0.5pt rim", "0.5px" in ci["shadow"], ci["shadow"][:70])
            near("the sidebar toolbar's 10pt under it", box("#search")["y"] - ed["bottom"], 10)
            se = box("#search")
            check("search: a 44pt capsule in Fills/Secondary", se["h"] == 44 and px(se["radius"]) >= 22
                  and rgba(se["bg"]) == (120, 120, 128, 0.16), (se["h"], se["bg"]))
            near("search: 11pt padding", px(se["pl"]), 11)
            near("search: 20pt before the rows", row["y"] - se["bottom"], 20)
            near("sidebar rows are 44pt", row["h"], 44)
            near("a row's title sits 48pt in: 10, a 34pt symbol column, 4", box("#row-title")["x"] - row["x"], 48)
            near("the symbol column is 34pt", box("#row .ipad-sidebar__icon")["w"], 34)
            check("row titles in body, 17/22", (px(box("#row-title")["font"]), px(box("#row-title")["lh"]))
                  == (17, 22), box("#row-title")["font"])
            check("the selected row is a full-width capsule", px(sel["radius"]) >= 22 and sel["w"] == 300,
                  (sel["radius"], sel["w"]))
            hd = box("#header")
            check("section header: 21 / 12 / 11 padding", (px(hd["pt"]), px(hd["pl"]), px(hd["pb"])) == (21, 12, 11),
                  (hd["pt"], hd["pl"], hd["pb"]))

            tb = box("#toolbar")
            check("toolbar: under the status bar, 10pt in", (px(tb["pt"]), px(tb["pl"])) == (32, 10), (tb["pt"], tb["pl"]))
            near("back is a 44pt circle", box("#back")["w"], 44)
            g = box("#group")
            check("a three-symbol group is 160 x 44: symbols on a 56pt pitch", (g["w"], g["h"]) == (160, 44),
                  (g["w"], g["h"]))
            t, st = box("#title-text"), box("#subtitle")
            check("large title: 34/41 bold", (px(t["font"]), px(t["lh"]), t["weight"]) == (34, 41, "700"), t["font"])
            check("subtitle: 15/20 medium", (px(st["font"]), px(st["lh"]), st["weight"]) == (15, 20, "510"), st["font"])
            near("the title starts 20pt in", t["x"] - box("#content")["x"], 20)

            bar, tab, ic = box("#tabbar"), box("#tab"), box("#tab-sidebar")
            check("the tab bar: 44pt, 4pt around 36pt tabs", (bar["h"], tab["h"]) == (44, 36), (bar["h"], tab["h"]))
            check("tabs: 15/20 medium, 18pt each side", (px(tab["font"]), px(tab["lh"]), tab["weight"], px(tab["pl"]))
                  == (15, 20, "510", 18), (tab["font"], tab["weight"], tab["pl"]))
            near("symbol tabs are 54pt wide", ic["w"], 54)
            ct = box("#content-tabs")
            near("the tab bar is centred over the content", (bar["x"] + bar["w"] / 2) - (ct["x"] + ct["w"] / 2), 0, 1)
            near("the tab bar sits in the toolbar row, 32pt down", bar["y"] - ct["y"], 32)

            sh, gr = box("#sheet"), box("#grabber")
            check("sheet: 936pt wide, 38pt corners", (sh["w"], px(sh["radius"])) == (936, 38), (sh["w"], sh["radius"]))
            near("the sheet hangs 32pt from the top", sh["y"] - box("#ipad-sheet")["y"] - 40, 32)
            check("the sheet's shadow", sh["shadow"] == "rgba(0, 0, 0, 0.18) 0px 15px 37.5px 0px", sh["shadow"])
            check("grabber: 60 x 4, 6pt from the top", (gr["w"], gr["h"], gr["y"] - sh["y"]) == (60, 4, 6),
                  (gr["w"], gr["h"], gr["y"] - sh["y"]))
            po = box("#popover")
            check("popover: 38pt corners, the 10/50 shadow", px(po["radius"]) == 38
                  and po["shadow"] == "rgba(0, 0, 0, 0.3) 0px 10px 50px 0px", (po["radius"], po["shadow"]))
            arrow = pseudo("#popover", "::after")
            check("the popover's arrow is 56 x 13", (arrow["w"], arrow["h"]) == (56, 13), arrow)
            sort = box("#sort")
            near("the arrow points at its source", po["x"] + px(arrow["left"]) - (sort["x"] + sort["w"] / 2), 0, 1)
            check("no iPhone tab bar on an iPad", pg.evaluate("() => !document.querySelector('.ios-tabbar')"))
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
