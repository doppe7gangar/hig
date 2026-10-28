#!/usr/bin/env python3
"""Did the SwiftUI keep what the design decided?

    python3 check_handoff.py ./design ./MyApp

Reads the design's HTML for what it decided: the screens and their
titles, the tabs, the SF Symbols, the components, the loading, empty and
error states, the words on the buttons, the accent colour. Then it looks
for each one in the Swift. Anything missing is a screen, state or label
that got lost between the two, the drift a reviewer otherwise finds by
clicking through both side by side.

It reads Swift as text and compiles nothing, so it says what's absent,
not that what's present works. HIG problems in the Swift itself are
check_swiftui.py's job, in apple-hig; run both. The mapping it checks
against is references/swiftui-handoff.md.

Exit status is 1 if anything the design decided is missing.
"""

import argparse
import html
import json
import os
import re
import sys
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "apple-hig"))
import check_swiftui  # noqa: E402

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "source", "track", "wbr"}
# Drawn by the system, not by the app: the status bar, and the back
# button's chevron, which a NavigationStack adds on its own.
SYSTEM_SYMBOLS = re.compile(r"^(cellularbars|wifi|battery\b|chevron\.(left|backward)$)")

# Kit class (or attribute) -> what has to be in the Swift, and what it is.
COMPONENTS = [
    ("ios-tabbar", r"\bTabView\b", "a tab bar", "TabView"),
    ("ios-list", r"\b(List|Form)\b", "a grouped list", "List or Form"),
    ("ios-list__row--tappable", r"\bNavigationLink\b|\.navigationDestination\(",
     "rows that open a screen", "NavigationLink"),
    ("ios-switch", r"\bToggle\b", "a switch", "Toggle"),
    ("ios-segmented", r"\.pickerStyle\(\s*\.segmented|SegmentedPickerStyle",
     "a segmented control", "Picker with .pickerStyle(.segmented)"),
    ("ios-stepper", r"\bStepper\b", "a stepper", "Stepper"),
    ("ios-slider", r"\bSlider\b", "a slider", "Slider"),
    ("ios-field", r"\b(TextField|SecureField)\b", "a text field", "TextField"),
    ("ios-sheet", r"\.sheet\(|\.fullScreenCover\(", "a sheet", ".sheet"),
    ("data-open", r"\.sheet\(|\.fullScreenCover\(", "a sheet", ".sheet"),
    ("ios-actionsheet", r"\.confirmationDialog\(", "an action sheet", ".confirmationDialog"),
    ("ios-alert", r"\.alert\(", "an alert", ".alert"),
    ("ios-empty", r"\bContentUnavailableView\b", "an empty or error state",
     "ContentUnavailableView"),
    ("ios-pagecontrol", r"\.tabViewStyle\(\s*\.page|PageTabViewStyle", "a page control",
     "TabView with .tabViewStyle(.page)"),
    ("ios-btn--destructive", r"role:\s*\.destructive", "a destructive button",
     "Button(role: .destructive)"),
    # A page's own markup for the same things.
    ("modal-dialog", r"\.sheet\(|\.fullScreenCover\(|\.confirmationDialog\(|\.alert\(",
     "a modal dialog", ".sheet"),
    ("input-text", r"\b(TextField|SecureField)\b", "a text input", "TextField"),
    ("input-date", r"\bDatePicker\b", "a date input", "DatePicker"),
    ("input-select", r"\b(Picker|Menu)\b", "a select menu", "Picker"),
    ("input-checkbox", r"\bToggle\b", "a checkbox or switch input", "Toggle"),
]
TEXT_INPUTS = {"", "text", "number", "email", "search", "tel", "url", "password"}


class Design(HTMLParser):
    """Text by class, every class and attribute used, and the symbol names."""

    WANT = ("largetitle", "ios-navbar__title", "ios-sheet__title", "ios-tabbar__item",
            "ios-empty__title", "ios-btn", "ios-alert__title", "ios-actionsheet__title")

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.open = [], []
        self.text = {k: [] for k in self.WANT}
        self.classes, self.attrs, self.symbols, self.components = set(), set(), set(), set()
        self.states, self.hidden, self.inside = set(), 0, 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = (a.get("class") or "").split()
        if "ios-sheet__title" not in cls and any(re.search(r"(^|[-_])sheet__title$", c)
                                                  for c in cls):
            cls.append("ios-sheet__title")          # a hand-built sheet's title
        kind = (a.get("type") or "").lower()
        if tag == "input" and kind in TEXT_INPUTS or tag == "textarea":
            self.classes.add("input-text")
        elif tag == "input" and kind in ("date", "time", "datetime-local"):
            self.classes.add("input-date")
        elif tag == "input" and kind == "checkbox":
            self.classes.add("input-checkbox")
        elif tag == "select":
            self.classes.add("input-select")
        if (a.get("role") == "dialog" and a.get("aria-modal") == "true"
                and not {"ios-sheet", "ios-actionsheet", "ios-alert"} & set(cls)):
            self.classes.add("modal-dialog")    # a page's own sheet or dialog
        self.classes.update(cls)
        self.attrs.update(k for k in a if k.startswith("data-"))
        sym = a.get("data-sf-symbol")
        if (sym and re.fullmatch(r"[A-Za-z0-9.]+", sym) and not SYSTEM_SYMBOLS.match(sym)
                and not self.inside and not a.get("data-component")):
            self.symbols.add(sym)           # not part of a system component's own art
        if a.get("data-component"):
            self.components.add(a["data-component"])
        if a.get("data-set"):
            self.states.add(a["data-set"])
        for c in cls:
            if c.startswith("state--"):
                self.states.add(c[7:])
        if tag in VOID:
            return
        quiet = tag in ("svg", "script", "style") or a.get("aria-hidden") == "true"
        comp = bool(a.get("data-component"))
        caps = [k for k in self.WANT if k in cls]
        for k in caps:
            self.open.append([k, len(self.stack), ""])
        self.stack.append((tag, quiet, len(caps), comp))
        self.hidden += quiet
        self.inside += comp

    def handle_endtag(self, tag):
        if tag in VOID or not any(e[0] == tag for e in self.stack):
            return
        while self.stack:
            t, quiet, caps, comp = self.stack.pop()
            self.hidden -= quiet
            self.inside -= comp
            for _ in range(caps):
                k, _, text = self.open.pop()
                text = " ".join(text.split()).strip(" ›‹>·")
                if re.search(r"[A-Za-z]", text):
                    self.text[k].append(text)
            if t == tag:
                break

    def handle_data(self, data):
        if not self.hidden:
            for cap in self.open:
                cap[2] += data


def design_facts(folder):
    d = Design()
    pages = []
    for root, dirs, files in os.walk(folder):
        dirs[:] = [x for x in dirs if x not in ("vendor", "node_modules") and not x.startswith(".")]
        pages += [os.path.join(root, f) for f in files if f.endswith(".html")]
    for p in sorted(pages):
        d.feed(open(p, encoding="utf-8", errors="replace").read())
        d.close()
        d.stack, d.open, d.hidden, d.inside = [], [], 0, 0
    accent = None
    theme = os.path.join(folder, "theme.css")
    if os.path.exists(theme):
        css = open(theme, encoding="utf-8").read()
        found = re.findall(r"--[a-z0-9-]*accent:\s*(#[0-9A-Fa-f]{6})\b", css)
        if found:
            accent = found[0].upper()
    return d, pages, accent


def norm(s):
    s = html.unescape(s).replace("’", "'").replace("‘", "'").replace("…", "...")
    return " ".join(s.split()).lower()


def swift_facts(folder):
    files = list(check_swiftui.swift_files([folder]))
    code, strings, symbols = [], [], set()
    for p in files:
        f = check_swiftui.File(p, open(p, encoding="utf-8", errors="replace").read())
        code.append(f.code)
        strings += [norm(t) for _, _, t in f.strings]
        symbols.update(name for _, name in check_swiftui.symbol_names(f))
    return files, "\n".join(code), strings, symbols


def accent_asset(folder):
    """The AccentColor's light value as #RRGGBB, '' if set some other way, None if absent."""
    for root, dirs, files in os.walk(folder):
        if os.path.basename(root) == "AccentColor.colorset" and "Contents.json" in files:
            try:
                data = json.load(open(os.path.join(root, "Contents.json")))
                c = data["colors"][0]["color"]["components"]
                vals = []
                for k in ("red", "green", "blue"):
                    v = str(c[k])
                    vals.append(int(v, 16) if v.startswith("0x") else
                                round(float(v) * 255) if "." in v else int(v))
                return "#" + "".join(f"{x:02X}" for x in vals)
            except (OSError, ValueError, KeyError, IndexError, TypeError):
                return ""
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("design", help="the design folder, with index.html")
    ap.add_argument("swift", help="the SwiftUI project or folder of .swift files")
    a = ap.parse_args()

    d, pages, accent = design_facts(a.design)
    files, code, strings, swift_symbols = swift_facts(a.swift)
    if not pages:
        sys.exit(f"No HTML in {a.design}.")
    if not files:
        sys.exit(f"No .swift files in {a.swift}.")
    out = {"ok": [], "warn": [], "FAIL": []}

    literals = set(strings)

    def present(text):
        # Whole string literals only: "Try Again" inside "check your
        # connection and try again" is not the button.
        return norm(text) in literals

    def words(texts, level, what):
        texts = sorted(set(texts))
        missing = [t for t in texts if not present(t)]
        if missing:
            out[level].append(f"{len(missing)} of {len(texts)} {what} not in the Swift: "
                              + ", ".join(f'"{t}"' for t in missing))
        elif texts:
            out["ok"].append(f"{len(texts)} of {len(texts)} {what} in the Swift")

    # Screens, tabs, states, sheets: the structure.
    words(d.text["largetitle"] + d.text["ios-navbar__title"], "FAIL", "screen titles")
    words(d.text["ios-tabbar__item"], "FAIL", "tab labels")
    words(d.text["ios-sheet__title"], "FAIL", "sheet titles")
    words(d.text["ios-alert__title"] + d.text["ios-actionsheet__title"], "FAIL",
          "alert and action sheet titles")
    words(d.text["ios-empty__title"], "FAIL", "empty and error state titles")
    words(d.text["ios-btn"], "warn", "button labels")

    if d.text["largetitle"] or d.text["ios-navbar__title"]:
        if re.search(r"\.navigationTitle\(", code):
            out["ok"].append("screens are titled with .navigationTitle")
        else:
            out["FAIL"].append("the design titles its screens; the Swift never calls "
                               ".navigationTitle, so the large titles are gone")

    seen = set()
    for key, pattern, what, api in COMPONENTS:
        used = (key in d.classes or key in d.attrs
                or (key == "ios-list__row--tappable" and "data-go" in d.attrs))
        if not used or pattern in seen:
            continue                    # one line per construct, however it was signalled
        seen.add(pattern)
        if re.search(pattern, code):
            out["ok"].append(f"{what}: {api}")
        else:
            shown = f" ({key})" if key.startswith(("ios-", "data-")) else ""
            out["FAIL"].append(f"the design has {what}{shown}; no {api} in the Swift")
    for name in sorted(d.components):
        if re.search(r"\b" + re.escape(name) + r"\b", code):
            out["ok"].append(f"data-component {name} is used")
        else:
            out["FAIL"].append(f"the design names {name} (data-component); the Swift doesn't use it")

    states = d.states & {"loading", "empty", "error"}
    if "loading" in states:
        if re.search(r"\bProgressView\b|\.redacted\(", code):
            out["ok"].append("loading state: ProgressView or .redacted")
        else:
            out["FAIL"].append("the design has a loading state; no ProgressView or .redacted "
                               "in the Swift")
    if states & {"empty", "error"} and "ios-empty" not in d.classes:
        if not re.search(r"\bContentUnavailableView\b", code):
            out["FAIL"].append("the design has empty or error states; no "
                               "ContentUnavailableView in the Swift")
    previews = len(re.findall(r"#Preview\b", code))
    if states and previews < len(states | {"populated"}):
        out["warn"].append(f"the design shows {len(states | {'populated'})} states; the Swift has "
                           f"{previews} #Preview(s). A preview per state lets you compare them "
                           "with the design one by one")

    # Symbols, both ways.
    missing = sorted(d.symbols - swift_symbols - {s for s in d.symbols if present(s)})
    if missing:
        out["FAIL"].append(f"{len(missing)} of {len(d.symbols)} SF Symbols in the design aren't "
                           f"in the Swift: {', '.join(missing)}")
    elif d.symbols:
        out["ok"].append(f"{len(d.symbols)} of {len(d.symbols)} SF Symbols in the design "
                         "are in the Swift")
    extra = sorted(swift_symbols - d.symbols)
    if extra:
        out["warn"].append(f"symbols in the Swift the design doesn't use: {', '.join(extra)}. "
                           "Fine if deliberate; otherwise the design and the app disagree")

    # The accent.
    if accent:
        asset = accent_asset(a.swift)
        digits = accent[1:].lower()             # as "#2F7D5B", 0x2F7D5B or "2F7D5B"
        literal = digits in code.lower() or any(digits in t for t in strings)
        if asset and asset == accent:
            out["ok"].append(f"AccentColor is the design's accent, {accent}")
        elif asset:
            out["warn"].append(f"AccentColor is {asset}; the design's accent is {accent}")
        elif asset == "":
            out["ok"].append("AccentColor is set (its value couldn't be read to compare)")
        elif literal:
            out["FAIL"].append(f"the accent {accent} is written into the Swift as a literal; put "
                               "it in the AccentColor asset so it adapts to Dark Mode")
        else:
            out["warn"].append(f"no AccentColor asset found; the design's accent is {accent}, "
                               "light and dark values in its theme.css")

    for level, mark in (("ok", "ok  "), ("warn", "warn"), ("FAIL", "FAIL")):
        for line in out[level]:
            print(f"  {mark} {line}")
    print(f"\nhandoff: {len(out['ok'])} ok, {len(out['warn'])} warnings, {len(out['FAIL'])} missing")
    print("Then: python3 ../apple-hig/check_swiftui.py " + a.swift)
    return 1 if out["FAIL"] else 0


if __name__ == "__main__":
    sys.exit(main())
