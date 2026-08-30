#!/usr/bin/env python3
"""Compare the built kit against the renderings it was measured from.

The skill ships 947 renderings of Apple's own UI kit across 27 component
families, and nothing ever checked the CSS against them. Six rounds of
"that doesn't look like iOS" were fixed by looking at photographs of a
phone, and every one of those answers was already on disk: the floating
tab bar under Tab Bars, the accent action beside a section header under
List/_Header Trailing Accessories, the status bar under Status Bars.

This reports three things:

  missing    a rendered family with no component at all
  thin       a component whose family renders many more states than the
             CSS distinguishes -- usually a variant nobody built
  unmapped   a family this script has no opinion about, so the mapping
             stays honest as the corpus grows

Coverage is not a score to maximise. A keyboard has no business in a web
kit and Face ID cannot be reproduced at all. The point is to know which
gaps are decisions and which are oversights.

    python3 scripts/audit_kit_coverage.py
    python3 scripts/audit_kit_coverage.py --family "Empty States"
"""

import argparse
import os
import re
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
ASSETS = os.path.join(REPO, ".claude", "skills", "apple-hig", "assets", "ui-kit")
KIT = os.path.join(REPO, ".claude", "skills", "apple-ui-kit", "ios-components.css")

# family -> the class that implements it. Deliberately explicit: a
# generated guess would quietly go stale in exactly the way this exists
# to catch.
IMPLEMENTS = {
    "Tab Bars": "ios-tabbar",
    "List": "ios-list",
    "Buttons": "ios-btn",
    "Toggles": "ios-switch",
    "Text Fields": "ios-field",
    "Materials": "ios-material",
    "Steppers": "ios-stepper",
    "Empty States": "ios-empty",
    "Alerts": "ios-alert",
    "Action Sheets": "ios-actionsheet",
    "Sliders": "ios-slider",
    "Page Controls": "ios-pagecontrol",
    "Notifications": "ios-notification",
    "Contextual Menus": "ios-menu",
    "Pop-up Buttons": "ios-popup",
    "Status Bars and Menu Bars": "ios-statusbar",
    "Date & Time Pickers": "ios-datepicker",
    "Color Pickers": "ios-colorpicker",
    "Activity View": "ios-activity",
    "Edit Menu": "ios-editmenu",
}

# Families a web kit should not implement, with the reason. Being
# explicit about these keeps them out of the missing list without
# pretending they were done.
OUT_OF_SCOPE = {
    "Keyboards": "the platform draws it; a web kit cannot and should not",
    "Face ID": "hardware affordance, not a component",
    "App Icons": "artwork, not markup",
    "Colors": "already in tokens/ios-tokens.css",
    "System": "assorted system art rather than a component",
    "Windows": "macOS chrome, and there is no measured Mac kit",
    "Activity View": "a system share sheet the app does not draw",
}


def families():
    out = {}
    for name in sorted(os.listdir(ASSETS)):
        d = os.path.join(ASSETS, name)
        if not os.path.isdir(d):
            continue
        n = sum(len(f) for _, _, f in os.walk(d))
        out[name] = n
    return out


def kit_classes():
    css = open(KIT, encoding="utf-8").read()
    base = {c.split("--")[0] for c in re.findall(r"^\.(ios-[\w-]+)", css, re.M)}
    variants = defaultdict(set)
    for c in re.findall(r"^\.(ios-[\w-]+)", css, re.M):
        variants[c.split("--")[0]].add(c)
    return base, variants


def main():
    ap = argparse.ArgumentParser(description="Audit kit coverage of the renderings.")
    ap.add_argument("--family", help="list the renderings in one family")
    a = ap.parse_args()

    if not os.path.isdir(ASSETS):
        sys.exit(f"no renderings at {ASSETS}")

    fams = families()
    if a.family:
        d = os.path.join(ASSETS, a.family)
        if not os.path.isdir(d):
            sys.exit(f"no such family: {a.family}")
        for root, _, fs in os.walk(d):
            for f in sorted(fs):
                print("  " + os.path.relpath(os.path.join(root, f), d))
        return 0

    base, variants = kit_classes()
    missing, thin, scoped, unmapped = [], [], [], []

    for fam, n in sorted(fams.items()):
        if fam in OUT_OF_SCOPE:
            scoped.append((fam, n, OUT_OF_SCOPE[fam]))
            continue
        cls = IMPLEMENTS.get(fam)
        if cls is None:
            unmapped.append((fam, n))
        elif cls not in base:
            missing.append((fam, n, cls))
        else:
            # A family rendering many states against a component with one
            # or two classes is usually a variant nobody built.
            v = len(variants[cls])
            if n >= 12 and v <= 2:
                thin.append((fam, n, cls, v))

    print(f"{sum(fams.values())} renderings, {len(fams)} families, "
          f"{len(base)} component families in the kit\n")

    if missing:
        print(f"MISSING -- rendered, and no component ({len(missing)}):")
        for fam, n, cls in missing:
            print(f"  {fam:32} {n:4} renderings   would be .{cls}")
        print()
    if thin:
        print(f"THIN -- component exists, variants may not ({len(thin)}):")
        for fam, n, cls, v in thin:
            print(f"  {fam:32} {n:4} renderings   .{cls} has {v} class(es)")
        print()
    if unmapped:
        print(f"UNMAPPED -- no opinion recorded ({len(unmapped)}):")
        for fam, n in unmapped:
            print(f"  {fam:32} {n:4} renderings")
        print()
    if scoped:
        print(f"OUT OF SCOPE, deliberately ({len(scoped)}):")
        for fam, n, why in scoped:
            print(f"  {fam:32} {why}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
