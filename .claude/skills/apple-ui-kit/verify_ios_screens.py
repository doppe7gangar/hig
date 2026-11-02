#!/usr/bin/env python3
"""Hold ios-screens.html to the geometry of Apple's own example screens.

Every expected number here was read off the Examples page of Apple's iOS
and iPadOS 27 kit -- the screens Apple composes from its own parts -- and
is written in, not read back from the stylesheet, so a recipe that drifts
from Apple's layout fails. Light and dark.

    python3 verify_ios_screens.py        # -v prints every check
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = "file://" + os.path.join(HERE, "ios-screens.html")

BOX = """(sel) => { const e = document.querySelector(sel); if (!e) return null;
  const r = e.getBoundingClientRect(), s = e.closest('.screen').getBoundingClientRect();
  return [Math.round(r.left - s.left), Math.round(r.top - s.top), Math.round(r.width), Math.round(r.height)]; }"""
ALL = """(sel) => [...document.querySelectorAll(sel)].map(e => Math.round(e.getBoundingClientRect().height))"""


def main():
    verbose = "-v" in sys.argv
    from playwright.sync_api import sync_playwright
    results = []

    def c(ok, label, got=""):
        results.append(ok)
        if verbose or not ok:
            print(f"  {'ok  ' if ok else 'FAIL'} {label}" + ("" if ok else f"  ({got})"))

    with sync_playwright() as p:
        b = p.chromium.launch(args=["--no-sandbox"])
        for scheme in ("light", "dark"):
            pg = b.new_page(viewport={"width": 1900, "height": 960}, color_scheme=scheme)
            pg.goto(PAGE, wait_until="load")
            pg.wait_for_timeout(300)
            box = lambda sel: pg.evaluate(BOX, sel)
            t = scheme
            # The top of every screen: status bar, then the controls, then the title.
            c(box("#inset .ios-statusbar")[3] == 62, f"{t}: status bar 62pt", box("#inset .ios-statusbar"))
            ctl = box("#inset .ios-controls")
            c(ctl[1] == 62 and ctl[3] == 44, f"{t}: controls at y 62, 44pt tall", ctl)
            c(ctl[0] == 16 and ctl[2] == 44, f"{t}: back button a 44pt circle 16pt in", ctl)
            grp = box("#inset .ios-navbar > .ios-controls:last-child")
            c(grp[0] + grp[2] == 386, f"{t}: trailing group ends 16pt from the edge", grp)
            h1 = box("#inset .ios-largetitle h1")
            c(h1[0] == 16 and h1[1] == 116 and h1[3] == 41, f"{t}: large title 16pt in at y 116, 41pt", h1)
            sub = box("#tabs .ios-largetitle__subtitle")
            c(sub[1] == 157 and sub[3] == 20, f"{t}: a subtitle sits under it at y 157, 20pt", sub)
            # Inset list: Apple's 362pt table, 20pt in, at y 183.
            lst = box("#inset .ios-list")
            c(lst[0] == 20 and lst[2] == 362, f"{t}: inset list 20pt in, 362pt wide", lst)
            c(lst[1] == 183, f"{t}: inset list starts at y 183", lst)
            radius = pg.evaluate("getComputedStyle(document.querySelector('#inset .ios-list')).borderRadius")
            c(radius == "26px", f"{t}: inset list corners 26pt", radius)
            rows = pg.evaluate(ALL, "#inset .ios-list__row")
            c(rows[0] == 68, f"{t}: thumbnail row 68pt", rows[:1])
            c(all(h == 52 for h in rows[1:]), f"{t}: one-line rows 52pt", rows)
            thumb = box("#inset .ios-list__thumb")
            c(thumb[2] == 68 and thumb[3] == 68 and thumb[0] == 36, f"{t}: thumbnail 68pt square at the row inset", thumb)
            pill = box("#inset .ios-pill")
            c(pill[3] == 34, f"{t}: date capsule 34pt (6 + 22 + 6)", pill)
            step = box("#inset .ios-stepper")
            c(step[2] == 92 and step[3] == 32, f"{t}: stepper 92 x 32", step)
            # Plain list: full width, letter sections 39pt, rows 52pt.
            pl = box("#plain .ios-list--plain")
            c(pl[0] == 0 and pl[2] == 402, f"{t}: plain list full width", pl)
            secs = pg.evaluate(ALL, "#plain .ios-list__section")
            c(secs and all(h == 39 for h in secs), f"{t}: section titles 39pt", secs)
            prow = pg.evaluate(ALL, "#plain .ios-list__row")
            c(all(h == 52 for h in prow), f"{t}: plain rows 52pt", prow)
            bg = pg.evaluate("getComputedStyle(document.querySelector('#plain')).backgroundColor")
            want = "rgb(255, 255, 255)" if scheme == "light" else "rgb(0, 0, 0)"
            c(bg == want, f"{t}: plain screen on the primary background", bg)
            # Empty state: 50pt circle, centred; a 52pt capsule 36pt in and up.
            g = box("#empty .ios-empty__glyph")
            c(g[2] == 50 and g[3] == 50 and g[0] + 25 == 201, f"{t}: symbol circle 50pt, centred", g)
            act = box("#empty .ios-empty__action")
            c(act[3] == 52 and act[0] == 36 and act[2] == 330, f"{t}: action capsule 52pt, 36pt in", act)
            c(act[1] + act[3] == 874 - 36, f"{t}: action 36pt above the bottom", act)
            # Apple's circle sits at y 334: the message centred on the screen
            # above the button, not on what the title leaves.
            c(abs(g[1] - 334) <= 2, f"{t}: symbol circle at y 334, as Apple's", g)
            # Tab bar: 62pt glass, 21pt off the bottom and the sides.
            tb = box("#tabs .ios-tabbar")
            c(tb[3] == 62 and tb[0] == 21 and tb[1] + tb[3] == 874 - 21, f"{t}: tab bar 62pt, 21pt in", tb)
            pg.close()
        b.close()
    print(f"\n{sum(results)}/{len(results)} checks passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
