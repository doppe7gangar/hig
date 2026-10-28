#!/usr/bin/env python3
"""Check SwiftUI code against the HIG before it ships.

Reads Swift source and reports what can be decided from the code alone:
fixed font sizes, colours that won't adapt, icon-only buttons with no
label, destructive actions without the destructive role, and the rest
below. Each finding is one of three kinds, kept apart because they are
not equally serious:

  violation  the HIG states the rule and the code breaks it
  guidance   the HIG says prefer or avoid, or its answer depends on
             something the code can't show; deviating can be right, with
             a reason
  api        not a HIG matter: deprecated or broken API. Fix it, but
             don't file it under design.

Every HIG finding names the page in references/pages/ that says so, and
anything in quotation marks is Apple's sentence, verbatim.

SF Symbol names are checked too, once sf_symbols.py --install has copied
your Mac's list: a name that doesn't exist, or that needs a newer OS than
the deployment target, draws nothing. The target comes from --ios, or
from the project's settings when the folder holds them.

Some things need eyes, not a regex -- whether an alert interrupts a
common, undoable action, or whether a chart separates series by colour
alone. Those aren't reported here; review them.

    python3 check_swiftui.py Sources/
    python3 check_swiftui.py ContentView.swift --json

Exit status is 1 if anything is a violation, 0 otherwise.
"""

import argparse
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sf_symbols  # noqa: E402

DESTRUCTIVE = re.compile(r"\b(delete|remove|erase|reset|discard|clear|wipe|destroy)\b", re.I)


# ---------------------------------------------------------------- lexing

def mask(src):
    """Blank comments and string contents, keeping every offset in place.

    Rules match against the masked text, so a comment that says
    `.font(.system(size: 12))` or a string that reads "Delete" can't set
    one off. String contents are kept separately for the rules that need
    a button's title.
    """
    out, strings, i, n = list(src), [], 0, len(src)

    def blank(a, b):
        for k in range(a, min(b, n)):
            if out[k] != "\n":
                out[k] = " "

    while i < n:
        if src.startswith("//", i):
            j = src.find("\n", i)
            j = n if j < 0 else j
            blank(i, j)
            i = j
        elif src.startswith("/*", i):
            depth, j = 1, i + 2
            while j < n and depth:
                if src.startswith("/*", j):
                    depth, j = depth + 1, j + 2
                elif src.startswith("*/", j):
                    depth, j = depth - 1, j + 2
                else:
                    j += 1
            blank(i, j)
            i = j
        elif src[i] == '"' or (src[i] == "#" and re.match(r'#+"', src[i:i + 8])):
            hashes = len(src[i:]) - len(src[i:].lstrip("#"))
            start = i + hashes
            if src.startswith('"""', start):
                close = '"""' + "#" * hashes
                end = src.find(close, start + 3)
                end = n if end < 0 else end
                strings.append((start + 3, end, src[start + 3:end]))
                blank(start + 3, end)
                i = end + len(close)
                continue
            close, j = '"' + "#" * hashes, start + 1
            while j < n and src[j] != "\n" and not src.startswith(close, j):
                if src[j] == "\\" and not hashes:
                    if src.startswith("\\(", j):             # interpolation
                        depth, j = 1, j + 2
                        while j < n and depth:
                            depth += {"(": 1, ")": -1}.get(src[j], 0)
                            j += 1
                        continue
                    j += 2
                    continue
                j += 1
            strings.append((start + 1, j, src[start + 1:j]))
            blank(start + 1, j)
            i = j + len(close)
        else:
            i += 1
    return "".join(out), strings


def closing(code, i):
    """Index just past the bracket that closes the one at i."""
    pairs = {"(": ")", "{": "}", "[": "]"}
    stack = [pairs[code[i]]]
    j = i + 1
    while j < len(code) and stack:
        c = code[j]
        if c in pairs:
            stack.append(pairs[c])
        elif stack and c == stack[-1]:
            stack.pop()
        j += 1
    return j


def skip_space(code, j):
    while j < len(code) and code[j] in " \t\r\n":
        j += 1
    return j


def call_end(code, j):
    """End of a call starting at j: its arguments and trailing closures."""
    j = skip_space(code, j)
    if j < len(code) and code[j] == "(":
        j = closing(code, j)
    after_closure = False
    while True:
        k = skip_space(code, j)
        if k < len(code) and code[k] == "{":
            j, after_closure = closing(code, k), True
            continue
        m = re.match(r"[A-Za-z_]\w*\s*:\s*\{", code[k:]) if after_closure else None
        if m:                                       # } label: { ... }
            j = closing(code, k + m.end() - 1)
            continue
        return j


def chain_end(code, j):
    """End of the modifier chain that follows an expression ending at j."""
    while True:
        k = skip_space(code, j)
        m = re.match(r"\.[A-Za-z_]\w*", code[k:])
        if not m:
            return j
        j = call_end(code, k + m.end())


# ----------------------------------------------------------------- rules

class File:
    def __init__(self, path, src):
        self.path, self.src = path, src
        self.code, self.strings = mask(src)
        self.lines = [0] + [i + 1 for i, c in enumerate(src) if c == "\n"]

    def line(self, pos):
        lo, hi = 0, len(self.lines)
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if self.lines[mid] <= pos:
                lo = mid
            else:
                hi = mid
        return lo + 1

    def strings_in(self, a, b):
        return [s for start, end, s in self.strings if a <= start < b]

    def containers(self, pattern):
        """Extents of calls matching pattern, e.g. every .alert(...)."""
        out = []
        for m in re.finditer(pattern, self.code):
            out.append((m.start(), call_end(self.code, m.end())))
        return out


def finding(f, pos, kind, rule, message, page=None):
    return dict(path=f.path, line=f.line(pos), kind=kind, rule=rule,
                message=message, page=page)


def symbol_names(f):
    """(position, name) for every symbol a systemName:/systemImage: argument can be."""
    for m in re.finditer(r"\b(?:systemName|systemImage)\s*:", f.code):
        depth, j = 0, m.end()
        while j < len(f.code):
            c = f.code[j]
            if c in "([{":
                depth += 1
            elif c in ")]}":
                if depth == 0:
                    break
                depth -= 1
            elif c == "," and depth == 0:
                break
            j += 1
        for start, end, text in f.strings:
            if m.end() <= start < j and re.fullmatch(r"[A-Za-z0-9.]+", text):
                yield start, text


def check_symbols(f, db, ios):
    out = []
    for pos, name in symbol_names(f):
        status, detail = sf_symbols.lookup(db, name, ios)
        if status == "unknown":
            hint = f" Did you mean `{detail}`?" if detail else ""
            out.append(finding(f, pos, "api", "sf-symbol",
                f"There's no SF Symbol named `{name}`, so this draws nothing.{hint}"))
        elif status == "too-new":
            out.append(finding(f, pos, "api", "sf-symbol",
                f"`{name}` arrived in iOS {detail}; below that it draws nothing "
                f"(deployment target iOS {ios})."))
        elif status == "renamed":
            out.append(finding(f, pos, "api", "sf-symbol",
                f"`{name}` was renamed `{detail}`."))
    return out


def deployment_target(paths):
    """The lowest iOS deployment target in the Xcode project or Package.swift
    the paths belong to: looked for below each path, then in the folders
    above it, up to the repository root."""
    found = []
    for p in paths:
        root = os.path.abspath(p if os.path.isdir(p) else os.path.dirname(p) or ".")
        files = (glob.glob(os.path.join(root, "**", "project.pbxproj"), recursive=True)
                 + glob.glob(os.path.join(root, "**", "Package.swift"), recursive=True))
        d = root
        while not files and not os.path.isdir(os.path.join(d, ".git")) \
                and os.path.dirname(d) != d:
            d = os.path.dirname(d)
            files = (glob.glob(os.path.join(d, "*.xcodeproj", "project.pbxproj"))
                     + glob.glob(os.path.join(d, "Package.swift")))
        for f in files:
            if re.search(r"[/\\](\.build|checkouts|DerivedData|Pods|Carthage)[/\\]", f):
                continue                 # dependencies, with targets of their own
            text = open(f, encoding="utf-8", errors="replace").read()
            found += re.findall(r'IPHONEOS_DEPLOYMENT_TARGET = "?([0-9.]+)"?;', text)
            found += [g[2] or ".".join(x for x in g[:2] if x) for g in
                      re.findall(r'\.iOS\(\s*(?:\.v(\d+)(?:_(\d+))?|"([0-9.]+)")', text)]
    return min(found, key=sf_symbols.version) if found else None


def check(f):
    code, out = f.code, []
    alerts = f.containers(r"\.alert\s*(?=\()")
    menus = f.containers(r"\.confirmationDialog\s*(?=\()|\.contextMenu\b|\bMenu\s*(?=[({])|"
                         r"\.swipeActions\b")
    inside = lambda pos, spans: any(a <= pos < b for a, b in spans)

    # Fixed font sizes.
    for m in re.finditer(r"\.system\(\s*size:\s*[0-9.]+", code):
        out.append(finding(f, m.start(), "violation", "fixed-font-size",
            "A fixed point size doesn't grow with Dynamic Type. Use a text "
            "style (.body, .headline, .caption) or @ScaledMetric; accessibility.md: "
            "\"Support larger text sizes.\"", "pages/accessibility.md"))
    for m in re.finditer(r"\.custom\(", code):
        args = code[m.end() - 1:closing(code, m.end() - 1)]
        if "size:" in args and "relativeTo" not in args:
            out.append(finding(f, m.start(), "violation", "fixed-font-size",
                "A custom font at a fixed size doesn't grow with Dynamic Type. "
                "Pass relativeTo: a text style; accessibility.md: "
                "\"Support larger text sizes.\"", "pages/accessibility.md"))

    # Colours that won't adapt to Dark Mode or Increase Contrast.
    colour = re.compile(
        r"\bColor\.(white|black)\b(?!\s*\.opacity)"
        r"|\.(?:background|foregroundColor|foregroundStyle|fill|stroke|tint)\(\s*\.(white|black)\b(?!\s*\.opacity)"
        r"|\bColor\(\s*(?:white|red|hue|\.sRGB|\.displayP3)\s*:"
        r"|\bColor\(\s*hex|#colorLiteral\(|\bUIColor\(\s*(?:red|white|hue)\s*:")
    for m in colour.finditer(code):
        out.append(finding(f, m.start(), "violation", "fixed-colour",
            "A fixed colour stays the same in Dark Mode and Increase Contrast. "
            "Use a semantic one (.primary, .secondary, Color(.systemBackground), "
            "an asset-catalog colour); dark-mode.md: \"Embrace colors that adapt "
            "to the current appearance.\"", "pages/dark-mode.md"))

    # Status shown by colour alone.
    for m in re.finditer(r"\?\s*(?:Color)?\.(green|red)\s*:\s*(?:Color)?\.(red|green)\b", code):
        out.append(finding(f, m.start(), "violation", "colour-only",
            "A red/green state with nothing else to tell them apart. Add a "
            "symbol or text; accessibility.md: \"Convey information with more "
            "than color alone.\"", "pages/accessibility.md"))

    # A hand-built modal: a dimmed backdrop you tap to dismiss.
    for m in re.finditer(r"\bColor\.black\.opacity\(", code):
        near = code[m.start():m.start() + 300]
        if ".onTapGesture" in near:
            out.append(finding(f, m.start(), "violation", "custom-modal",
                "A hand-built modal: VoiceOver can still reach what's behind the "
                "dimming, and it has none of the system's dismissal. Present it with "
                ".sheet (presentationDetents for a small panel) or .alert.",
                "pages/sheets.md"))

    # Too many tabs.
    for m in re.finditer(r"\bTabView\b", code):
        end = call_end(code, m.end())
        body = code[m.end():end]
        n = len(re.findall(r"\.tabItem\b", body)) + len(re.findall(r"\bTab\s*\(", body))
        if n > 5:
            out.append(finding(f, m.start(), "guidance", "overflow-tabs",
                f"{n} tabs. When they don't fit, \"the trailing tab becomes a More "
                "tab in iOS and iPadOS\" (tab-bars.md, under \"Avoid overflow "
                "tabs.\"). Fold the least-used into another tab or a sidebar.",
                "pages/tab-bars.md"))

    # Buttons: label, target size, destructive role.
    for m in re.finditer(r"\bButton\s*(?=[({])", code):
        start = m.start()
        expr = call_end(code, m.end())
        chain = chain_end(code, expr)
        own = code[start:expr]
        whole = code[start:chain]
        args_end = closing(code, m.end()) if code[m.end()] == "(" else m.end()
        title = (f.strings_in(m.end(), args_end) or [None])[0]
        texts = [s for s in f.strings_in(start, expr)]

        icon_only = (title is None and re.search(r"\bImage\(", own)
                     and not re.search(r"\b(Text|Label)\(", own))
        if icon_only and ".accessibilityLabel(" not in whole:
            symbol = next((s for s in texts), None)
            named = f" VoiceOver will read the symbol's name, `{symbol}`." if symbol else ""
            out.append(finding(f, start, "violation", "unlabelled-icon-button",
                "An icon-only button with no accessibility label." + named +
                " Add .accessibilityLabel(_:) or use Label(_:systemImage:) "
                "with .labelStyle(.iconOnly); voiceover.md: \"Provide alternative "
                "labels for all key interface elements.\"", "pages/voiceover.md"))

        sizes = []
        for fm in re.finditer(r"\.frame\(([^()]*)\)", whole):
            for dim in re.finditer(r"\b(width|height):\s*([0-9.]+)", fm.group(1)):
                sizes.append(float(dim.group(2)))
        if sizes and min(sizes) < 44:
            d = min(sizes)
            kind = "violation" if d < 28 else "guidance"
            why = ("below the 28x28pt minimum" if d < 28 else
                   "within the 28x28pt minimum but under the 44x44pt default; "
                   "for a control people use often, give it 44")
            out.append(finding(f, start, kind, "small-target",
                f"A {d:g}pt button, {why} (accessibility.md, control size table).",
                "pages/accessibility.md"))

        label = title or " ".join(texts)
        if label and DESTRUCTIVE.search(label) and ".destructive" not in own:
            if inside(start, alerts):
                out.append(finding(f, start, "guidance", "destructive-role",
                    f"`{label}` in an alert without role: .destructive. Mark it if "
                    "the person didn't choose this action; leave it if the alert "
                    "confirms one they just chose. alerts.md: \"Use the destructive "
                    "style to identify a button that performs a destructive action "
                    "people didn't deliberately choose.\"", "pages/alerts.md"))
            else:
                styled = re.search(r"\.(foregroundColor|foregroundStyle|tint)\(\s*(?:Color)?\.(blue|accentColor)", whole)
                extra = " It's styled as an ordinary action too." if styled else ""
                where = "pages/action-sheets.md" if inside(start, menus) else "pages/buttons.md"
                out.append(finding(f, start, "violation", "destructive-role",
                    f"`{label}` destroys data but has no role: .destructive, so it "
                    "isn't shown in red." + extra + " buttons.md: \"a destructive "
                    "button uses the system red color.\"", where))

    # Not HIG: deprecated or broken API.
    api = [
        (r"\.foregroundColor\(", "foregroundColor(_:) is deprecated; use foregroundStyle(_:)."),
        (r"\.accentColor\(", "accentColor(_:) is deprecated; use tint(_:)."),
        (r"\.cornerRadius\(", "cornerRadius(_:) is deprecated; use clipShape(.rect(cornerRadius:))."),
        (r"\bNavigationView\b", "NavigationView is deprecated; use NavigationStack or NavigationSplitView."),
        (r"\.navigationBarTitle\(", "navigationBarTitle(_:) is deprecated; use navigationTitle(_:)."),
        (r"\.navigationBarItems\(", "navigationBarItems is deprecated; use toolbar { }."),
        (r"\.actionSheet\(|\bActionSheet\(", "ActionSheet is deprecated; use confirmationDialog."),
        (r"\bAlert\(\s*title:", "The Alert type is deprecated; use alert(_:isPresented:actions:message:)."),
        (r"\bMagnificationGesture\b", "MagnificationGesture is deprecated; use MagnifyGesture."),
        (r"\bRotationGesture\b", "RotationGesture is deprecated; use RotateGesture."),
        (r"\.onChange\(of:[^)]*\)\s*\{\s*[A-Za-z_]\w*\s+in\b|\.onChange\([^)]*perform:",
         "onChange(of:perform:) is deprecated; use the two- or zero-parameter closure."),
        (r"isPresented:\s*\.constant\(", "isPresented: .constant(...) can't be set back, so the "
         "presentation can't dismiss itself; bind it to @State."),
    ]
    for pattern, message in api:
        for m in re.finditer(pattern, code):
            out.append(finding(f, m.start(), "api", "api", message))
    tabs = list(re.finditer(r"\.tabItem\b", code))
    if tabs:
        out.append(finding(f, tabs[0].start(), "api", "api",
            f"tabItem(_:) is deprecated ({len(tabs)} uses); use Tab(_:systemImage:) inside TabView."))
    for m in re.finditer(r"\.animation\(", code):
        if "value:" not in code[m.end() - 1:closing(code, m.end() - 1)]:
            out.append(finding(f, m.start(), "api", "api",
                "animation(_:) without value: is deprecated; pass the value it animates."))
    return out


def swift_files(paths):
    for p in paths:
        if os.path.isdir(p):
            for root, dirs, files in os.walk(p):
                dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ("Pods", ".build")]
                for name in sorted(files):
                    if name.endswith(".swift"):
                        yield os.path.join(root, name)
        else:
            yield p


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("paths", nargs="+", help="Swift files or folders")
    ap.add_argument("--json", action="store_true", help="print findings as JSON")
    ap.add_argument("--ios", help="deployment target for symbol availability, e.g. 17")
    a = ap.parse_args()

    db = sf_symbols.load()
    ios = a.ios or deployment_target(a.paths)
    found = []
    for path in swift_files(a.paths):
        with open(path, encoding="utf-8", errors="replace") as fh:
            f = File(path, fh.read())
        found += check(f) + (check_symbols(f, db, ios) if db else [])
    found.sort(key=lambda x: (x["path"], x["line"]))

    if a.json:
        print(json.dumps(found, indent=1))
    else:
        order = {"violation": 0, "guidance": 1, "api": 2}
        for kind in sorted({x["kind"] for x in found}, key=order.get):
            print(f"\n{kind.upper()}")
            for x in (y for y in found if y["kind"] == kind):
                where = f"  ({x['page']})" if x["page"] else ""
                print(f"  {x['path']}:{x['line']}  {x['message']}{where}")
        counts = {k: sum(x["kind"] == k for x in found) for k in order}
        print(f"\n{counts['violation']} violations, {counts['guidance']} guidance, "
              f"{counts['api']} API issues")
        if not db:
            print("SF Symbol names not checked: run  python3 sf_symbols.py --install  on a Mac.")
        elif not ios:
            print("SF Symbol names checked; availability not, as no deployment target was "
                  "found. Pass --ios 17 to check it.")
        else:
            print(f"SF Symbol names checked, and that each exists on iOS {ios}.")
    return 1 if any(x["kind"] == "violation" for x in found) else 0


if __name__ == "__main__":
    sys.exit(main())
