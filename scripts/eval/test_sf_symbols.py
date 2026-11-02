#!/usr/bin/env python3
"""Do the SF Symbol name checks work? No Mac needed.

The real list lives on a Mac and can't ship here, so this builds a small
stand-in in the same format -- name_availability.plist and
name_aliases.strings, as CoreGlyphs.bundle holds them -- and runs
everything against that:

1. sf_symbols.py --install --from reads it, binary or text, and of
   several lists picks the newest.
2. lookup() tells ok, renamed, too new and unknown apart, suggests the
   name a typo meant, and only suggests a rename the target OS can use.
3. check_swiftui.py flags bad names in Swift, and reads the deployment
   target from an Xcode project or Package.swift, ignoring dependencies.
4. check_design.py flags bad data-sf-symbol names and leaves alone names
   a script builds at run time.
5. With no list installed, both checkers say so and carry on.

    python3 scripts/eval/test_sf_symbols.py
"""

import os
import plistlib
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SKILLS = os.path.normpath(os.path.join(HERE, "..", "..", ".claude", "skills"))
HIG = os.path.join(SKILLS, "apple-hig")
sys.path.insert(0, HIG)
import sf_symbols  # noqa: E402

SYMBOLS = {
    "trash": "2019", "trash.fill": "2019", "plus": "2019", "list.bullet": "2019",
    "cart.fill": "2019", "creditcard": "2019", "tray": "2019", "gearshape": "2020",
    "fork.knife": "2021", "123.rectangle": "2021", "numbers.rectangle": "2024",
    "1.calendar": "2025",
}
RELEASES = {"2019": {"iOS": "13.0"}, "2020": {"iOS": "14.0"}, "2021": {"iOS": "15.0"},
            "2024": {"iOS": "18.0"}, "2025": {"iOS": "26.0"}}
ALIASES = {"123.rectangle": "numbers.rectangle", "_codename": "1.calendar"}

SWIFT = '''import SwiftUI

struct Row: View {
    var done: Bool
    var body: some View {
        HStack {
            Image(systemName: "trash.fil")
            Label("Due", systemImage: "1.calendar")
            Image(systemName: done ? "fork.knife" : "receipt.expense")
            Image(systemName: "123.rectangle")
            Image(systemName: "Cart.fill")
            Image(systemName: "\\(kind).fill")
            Text("plus")
        }
    }
    let kind = "tray"
}
'''

HTML = '''<!doctype html><html><body>
<span class="icon" data-sf-symbol="cart.fill"></span>
<span class="icon" data-sf-symbol="fork.knif"></span>
<span class="icon" data-sf-symbol="expense.tray"></span>
<template><span class="icon" data-sf-symbol="${cat.sf}"></span></template>
<span class="icon" :data-sf-symbol="item.icon"></span>
<script>row.innerHTML = '<span data-sf-symbol="' + cat.sf + '"></span>';</script>
</body></html>
'''


def write_source(folder, symbols, binary):
    os.makedirs(folder)
    fmt = plistlib.FMT_BINARY if binary else plistlib.FMT_XML
    with open(os.path.join(folder, "name_availability.plist"), "wb") as fh:
        plistlib.dump({"symbols": symbols, "year_to_release": RELEASES}, fh, fmt=fmt)
    with open(os.path.join(folder, "name_aliases.strings"), "wb") as fh:
        if binary:
            plistlib.dump(ALIASES, fh, fmt=fmt)
        else:
            fh.write("".join(f'"{k}" = "{v}";\n' for k, v in ALIASES.items()).encode())


def run(*args, env):
    p = subprocess.run([sys.executable, *args], capture_output=True, text=True, env=env)
    return p.returncode, p.stdout + p.stderr


def main():
    failures = []

    def expect(cond, what):
        print(("ok   " if cond else "FAIL ") + what)
        if not cond:
            failures.append(what)

    with tempfile.TemporaryDirectory() as d:
        env = dict(os.environ, APPLE_HIG_SF_SYMBOLS=os.path.join(d, "cache", "sf.json"))
        os.environ["APPLE_HIG_SF_SYMBOLS"] = env["APPLE_HIG_SF_SYMBOLS"]
        old, new = os.path.join(d, "old"), os.path.join(d, "new")
        write_source(old, {k: v for k, v in SYMBOLS.items() if v < "2024"}, binary=False)
        write_source(new, SYMBOLS, binary=True)

        # 1. Reading the list
        for folder, label in ((old, "text"), (new, "binary")):
            code, out = run(os.path.join(HIG, "sf_symbols.py"), "--install", "--from", folder, env=env)
            db = sf_symbols.load()
            expect(code == 0 and db and db["aliases"] == ALIASES and len(db["symbols"]) > 5,
                   f"--install --from reads the {label} plist and .strings")
        sf_symbols.SOURCES = [os.path.join(d, "*")]
        sf_symbols.install()
        expect(len(sf_symbols.load()["symbols"]) == len(SYMBOLS),
               "of several lists, --install keeps the newest")
        db = sf_symbols.load()

        # 2. Looking names up
        cases = [
            ("fork.knife", None, ("ok", "15.0")),
            ("trash.fil", None, ("unknown", "trash.fill")),
            ("receipt.expense", None, ("unknown", None)),
            ("1.calendar", "17", ("too-new", "26.0")),
            ("1.calendar", "26", ("ok", "26.0")),               # 26 is 26.0
            ("123.rectangle", "17", ("ok", "15.0")),            # new name needs 18
            ("123.rectangle", "18.0", ("renamed", "numbers.rectangle")),
            ("_codename", None, ("renamed", "1.calendar")),
        ]
        for name, ios, want in cases:
            got = sf_symbols.lookup(db, name, ios)
            expect(got == want, f"lookup {name} on iOS {ios or 'any'}: {got[0]}"
                   + ("" if got == want else f", wanted {want}"))

        # 3. Swift, with the target from the project
        proj = os.path.join(d, "App")
        os.makedirs(os.path.join(proj, "App"))
        os.makedirs(os.path.join(proj, "App.xcodeproj"))
        os.makedirs(os.path.join(proj, "Pods", "Pods.xcodeproj"))
        with open(os.path.join(proj, "App", "Row.swift"), "w") as fh:
            fh.write(SWIFT)
        with open(os.path.join(proj, "App.xcodeproj", "project.pbxproj"), "w") as fh:
            fh.write("IPHONEOS_DEPLOYMENT_TARGET = 18.0;\nIPHONEOS_DEPLOYMENT_TARGET = 17.0;\n")
        with open(os.path.join(proj, "Pods", "Pods.xcodeproj", "project.pbxproj"), "w") as fh:
            fh.write("IPHONEOS_DEPLOYMENT_TARGET = 9.0;\n")
        swift = os.path.join(proj, "App", "Row.swift")
        sys.path.insert(0, HIG)
        import check_swiftui
        expect(check_swiftui.deployment_target([swift]) == "17.0",
               "deployment target: the lowest in the project above the file")
        expect(check_swiftui.deployment_target([proj]) == "17.0",
               "deployment target: the project's, not the Pods project's below it")
        pkg = os.path.join(d, "Pkg")
        os.makedirs(os.path.join(pkg, "Sources"))
        with open(os.path.join(pkg, "Package.swift"), "w") as fh:
            fh.write('platforms: [.iOS(.v16_4), .macOS(.v14)]')
        expect(check_swiftui.deployment_target([os.path.join(pkg, "Sources")]) == "16.4",
               "deployment target from Package.swift")

        code, out = run(os.path.join(HIG, "check_swiftui.py"), swift, env=env)
        expect("`trash.fil`" in out and "Did you mean `trash.fill`?" in out, "Swift: typo found, fix suggested")
        expect("`receipt.expense`" in out, "Swift: invented name found, inside a ternary")
        expect("`Cart.fill`" in out and "`cart.fill`?" in out, "Swift: capitalised name found")
        expect("`1.calendar` arrived in iOS 26.0" in out and "iOS 17.0" in out,
               "Swift: symbol newer than the deployment target found")
        expect("123.rectangle" not in out, "Swift: no rename suggested the target can't use")
        expect("fork.knife" not in out and "kind" not in out and "plus" not in out,
               "Swift: real names, interpolated names and plain text left alone")
        expect("exists on iOS 17.0" in out, "Swift: says which target it checked against")
        code18, out18 = run(os.path.join(HIG, "check_swiftui.py"), swift, "--ios", "18", env=env)
        expect("renamed `numbers.rectangle`" in out18, "Swift: --ios 18 suggests the rename")

        # 4. HTML
        page = os.path.join(d, "design")
        os.makedirs(page)
        with open(os.path.join(page, "index.html"), "w") as fh:
            fh.write(HTML)
        check_design = os.path.join(SKILLS, "apple-design", "check_design.py")
        code, out = run(check_design, page, "--no-browser", env=env)
        line = next((l for l in out.splitlines() if "aren't SF Symbols" in l), "")
        expect("fork.knif (did you mean fork.knife?)" in line and "expense.tray" in line,
               "HTML: bad data-sf-symbol names found")
        expect(line and "cart.fill" not in line and "cat.sf" not in line
               and "item.icon" not in line and "+" not in line.split(":", 2)[-1],
               "HTML: real names, script-built names and bound attributes left alone")

        # 5. No list
        os.remove(env["APPLE_HIG_SF_SYMBOLS"])
        code, out = run(os.path.join(HIG, "check_swiftui.py"), swift, env=env)
        expect("SF Symbol names not checked" in out and "trash.fil" not in out,
               "no list: check_swiftui says it skipped the names")
        code, out = run(check_design, page, "--no-browser", env=env)
        expect("aren't SF Symbols" not in out and "Traceback" not in out,
               "no list: check_design carries on without it")

    print("\nsf_symbols test " + ("passed" if not failures else f"failed: {len(failures)} problems"))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
