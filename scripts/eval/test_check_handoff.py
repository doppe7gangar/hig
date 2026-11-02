#!/usr/bin/env python3
"""Does check_handoff.py notice what a SwiftUI handoff lost?

handoff/ holds a small design in the kit's markup and a faithful SwiftUI
translation of it. The faithful one must pass both check_handoff.py and
check_swiftui.py with nothing to report. Then each case below breaks the
Swift in one way a real handoff drifts, and the matching complaint has to
appear, and nothing else may fail.

    python3 scripts/eval/test_check_handoff.py
"""

import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SKILLS = os.path.normpath(os.path.join(HERE, "..", "..", ".claude", "skills"))
CHECK = os.path.join(SKILLS, "apple-design", "check_handoff.py")
SWIFTUI = os.path.join(SKILLS, "apple-hig", "check_swiftui.py")
DESIGN = os.path.join(HERE, "handoff", "design")
SWIFT = os.path.join(HERE, "handoff", "swift")
VIEW = os.path.join("Ledger", "ExpensesView.swift")
ASSET = os.path.join("Ledger", "Assets.xcassets", "AccentColor.colorset")

# (what drifted, [(old, new) in ExpensesView.swift], remove the asset?,
#  level, text the complaint must contain)
CASES = [
    ("error state's title rewritten",
     [("Couldn’t load expenses", "Something went wrong")], False,
     "FAIL", "Couldn’t load expenses"),
    ("a different symbol",
     [('"tram.fill"', '"bus.fill"')], False, "FAIL", "tram.fill"),
    ("segmented control became a menu",
     [(".pickerStyle(.segmented)", ".pickerStyle(.menu)")], False, "FAIL", "segmented"),
    ("action sheet became an alert",
     [(".confirmationDialog(", ".alert(")], False, "FAIL", ".confirmationDialog"),
    ("loading state dropped",
     [("ProgressView()", 'Text("Loading")')], False, "FAIL", "loading state"),
    ("a tab renamed",
     [('Tab("Budgets", systemImage: "chart.pie") { Text("Budgets") }',
       'Tab("Plans", systemImage: "chart.pie") { Text("Plans") }')], False, "FAIL", '"Budgets"'),
    ("titles set without navigationTitle",
     [(".navigationTitle(", ".navigationSubtitle(")], False, "FAIL", ".navigationTitle"),
    ("accent hard-coded instead of the asset",
     [("WindowGroup { RootView(state: .loaded(Expense.samples)) }",
       "WindowGroup { RootView(state: .loaded(Expense.samples)).tint(Color(hex: 0x2F7D5B)) }")],
     True, "FAIL", "written into the Swift as a literal"),
    ("accent asset missing",
     [], True, "warn", "no AccentColor asset"),
    ("previews dropped",
     [('#Preview("Loading") { RootView(state: .loading) }\n', ""),
      ('#Preview("Error") { RootView(state: .failed) }\n', "")], False,
     "warn", "#Preview"),
    ("a button relabelled",
     [('Button("Try Again")', 'Button("Retry")')], False, "warn", '"Try Again"'),
]

# Drift that isn't drift: these must still pass.
SAME = [
    ("straight apostrophe for a curly one",
     [("Couldn’t load expenses", "Couldn't load expenses")]),
]


def run(*args):
    p = subprocess.run([sys.executable, *args], capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def variant(tmp, edits, drop_asset):
    root = os.path.join(tmp, "swift")
    shutil.rmtree(root, ignore_errors=True)
    shutil.copytree(SWIFT, root)
    path = os.path.join(root, VIEW)
    src = open(path, encoding="utf-8").read()
    for old, new in edits:
        if old not in src:
            raise SystemExit(f"fixture changed: {old!r} isn't in {VIEW} any more")
        src = src.replace(old, new)
    open(path, "w", encoding="utf-8").write(src)
    if drop_asset:
        shutil.rmtree(os.path.join(root, ASSET))
    return root


def lines(out, level):
    mark = {"FAIL": "  FAIL ", "warn": "  warn "}[level]
    return [l for l in out.splitlines() if l.startswith(mark)]


def main():
    failures = []

    code, out = run(CHECK, DESIGN, SWIFT)
    if code != 0 or lines(out, "FAIL") or lines(out, "warn"):
        failures.append("the faithful handoff isn't clean:\n" + out)
    print(f"faithful handoff: exit {code}, {out.strip().splitlines()[-2]}")
    code, out = run(SWIFTUI, SWIFT)
    if code != 0 or "0 violations, 0 guidance, 0 API issues" not in out:
        failures.append("the faithful Swift has check_swiftui findings:\n" + out)

    with tempfile.TemporaryDirectory() as tmp:
        for label, edits, drop, level, needle in CASES:
            code, out = run(CHECK, DESIGN, variant(tmp, edits, drop))
            hits = [l for l in lines(out, level) if needle in l]
            fails = lines(out, "FAIL")
            want_code = 1 if level == "FAIL" else 0
            ok = hits and code == want_code and (level == "FAIL" or not fails)
            if level == "FAIL" and len(fails) > 1 and label != "a different symbol":
                ok = False                       # one change, one complaint
            print(f"{'ok  ' if ok else 'FAIL'} {label}: "
                  + (hits[0].strip()[:110] if hits else f"no {level} about {needle!r}"))
            if not ok:
                failures.append(f"{label}: exit {code}\n{out}")
        for label, edits in SAME:
            code, out = run(CHECK, DESIGN, variant(tmp, edits, False))
            ok = code == 0 and not lines(out, "FAIL")
            print(f"{'ok  ' if ok else 'FAIL'} {label} still passes")
            if not ok:
                failures.append(f"{label}:\n{out}")

    for f in failures:
        print("\nFAIL", f)
    print("\ncheck_handoff test " + ("passed" if not failures else f"failed: {len(failures)} problems"))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
