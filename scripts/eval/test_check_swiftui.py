#!/usr/bin/env python3
"""Does check_swiftui.py find what's there, and only what's there?

Three tests, no model and no Xcode:

1. The real-life fixture in reallife/, against its GROUND_TRUTH.md: every
   mechanically checkable seeded defect is found, the correct code the
   ground truth lists is left alone, and the 30x30 toolbar buttons come
   back as guidance, not a violation -- the calibration the
   ground truth grades on. Two seeded defects need eyes rather than a
   pattern (an alert for an undoable delete, chart bars told apart by
   colour) and the checker is expected to stay quiet on them.
2. A clean, current SwiftUI file must produce nothing at all.
3. Comments and strings that read like violations must not trigger them.

    python3 scripts/eval/test_check_swiftui.py
"""

import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK = os.path.normpath(os.path.join(HERE, "..", "..", ".claude", "skills", "apple-hig",
                                      "check_swiftui.py"))
FIXTURE = os.path.join(HERE, "reallife", "fixture")
sys.path.insert(0, os.path.dirname(CHECK))
import check_swiftui  # noqa: E402

# (file, line, kind, rule) the fixture must produce. Ground-truth numbers
# in the comments; its line numbers drifted, so these are the file's own.
EXPECTED = {
    ("ContentView.swift", 7, "guidance", "overflow-tabs"),         # 1 seven tabs
    ("ContentView.swift", 51, "violation", "fixed-colour"),        # 2 Color.white
    ("ContentView.swift", 96, "violation", "fixed-colour"),        # 2
    ("ContentView.swift", 144, "violation", "fixed-colour"),       # 2
    ("ContentView.swift", 120, "violation", "fixed-colour"),       # 3 .black label
    ("ContentView.swift", 91, "violation", "fixed-font-size"),     # 4
    ("ContentView.swift", 119, "violation", "fixed-font-size"),    # 4
    ("ContentView.swift", 122, "violation", "fixed-font-size"),    # 4
    ("ContentView.swift", 114, "violation", "colour-only"),        # 5
    ("ContentView.swift", 86, "violation", "custom-modal"),        # 6
    ("ContentView.swift", 76, "guidance", "destructive-role"),     # 8, in an alert
    ("SupportingViews.swift", 61, "guidance", "destructive-role"), # 8, in an alert
    ("SupportingViews.swift", 50, "violation", "destructive-role"),# 8 + 9 styled blue
    ("ContentView.swift", 55, "violation", "unlabelled-icon-button"),   # 10
    ("ContentView.swift", 63, "violation", "unlabelled-icon-button"),   # 10
    ("ContentView.swift", 136, "violation", "unlabelled-icon-button"),  # 10
    ("ContentView.swift", 55, "guidance", "small-target"),         # 12 guidance, not violation
    ("ContentView.swift", 63, "guidance", "small-target"),         # 12
}

# Correct code the ground truth says must not be flagged, by line.
LEAVE_ALONE = {
    ("ContentView.swift", 128, "small-target"),       # the 44x44 completion toggle
    ("ContentView.swift", 71, None),                  # .sheet for AddHabitView
    ("SupportingViews.swift", 22, None),              # .cancellationAction
    ("SupportingViews.swift", 25, None),              # .confirmationAction
    ("SupportingViews.swift", 75, None),              # .font(.body)
    ("SupportingViews.swift", 78, None),              # .font(.footnote)
    ("SupportingViews.swift", 79, None),              # foregroundStyle(.secondary)
    ("SupportingViews.swift", 94, None),              # .font(.headline)
}

CLEAN = '''import SwiftUI

struct ExpensesView: View {
    @State private var expenses: [Expense] = []
    @State private var adding = false
    @State private var pendingDelete: Expense?
    @ScaledMetric(relativeTo: .body) private var iconSize = 22

    var body: some View {
        TabView {
            Tab("Expenses", systemImage: "list.bullet") {
                NavigationStack {
                    List {
                        ForEach(expenses) { expense in
                            HStack {
                                Image(systemName: expense.symbol)
                                    .font(.system(size: iconSize))
                                    .foregroundStyle(.tint)
                                Text(expense.title).font(.body)
                                Spacer()
                                Text(expense.amount, format: .currency(code: "USD"))
                                    .foregroundStyle(.secondary)
                            }
                            .swipeActions {
                                Button("Delete", systemImage: "trash", role: .destructive) {
                                    pendingDelete = expense
                                }
                            }
                        }
                    }
                    .navigationTitle("Expenses")
                    .toolbar {
                        Button("Add", systemImage: "plus") { adding = true }
                    }
                    .sheet(isPresented: $adding) { AddExpenseView() }
                    .background(Color(.systemGroupedBackground))
                }
            }
            Tab("Settings", systemImage: "gear") { SettingsView() }
        }
        .tint(.indigo)
    }
}

struct SettingsView: View {
    @State private var confirming = false
    var body: some View {
        Form {
            Button("Erase All Data", role: .destructive) { confirming = true }
        }
        .confirmationDialog("Erase everything?", isPresented: $confirming) {
            Button("Erase All Data", role: .destructive) { }
        }
        .animation(.smooth, value: confirming)
        .onChange(of: confirming) { old, new in }
    }
}
'''

TRICKY = '''import SwiftUI

// Old code used .font(.system(size: 12)) and Color.white here; not any more.
/* A Button("Delete") lived here once, with .foregroundColor(.blue). */
struct Notes: View {
    var body: some View {
        VStack {
            Text("Tap Delete to remove a note")
            Text("Use .font(.system(size: 12)) for nothing \\(count) times")
            Text(#"Raw: Color.black and "quotes""#)
        }
    }
    let count = 3
}
'''


def run_check(src, name="Test.swift"):
    return check_swiftui.check(check_swiftui.File(name, src))


def main():
    failures = []

    found = []
    for fn in ("ContentView.swift", "SupportingViews.swift", "HabitStore.swift"):
        with open(os.path.join(FIXTURE, fn), encoding="utf-8") as fh:
            found += [dict(x, path=fn) for x in check_swiftui.check(check_swiftui.File(fn, fh.read()))]
    got = {(x["path"], x["line"], x["kind"], x["rule"]) for x in found}
    for e in sorted(EXPECTED - got):
        failures.append(f"fixture: missing {e}")
    for path, line, rule in sorted(LEAVE_ALONE, key=str):
        hits = [x for x in found if x["path"] == path and x["line"] == line
                and (rule is None or x["rule"] == rule) and x["kind"] != "api"]
        if hits:
            failures.append(f"fixture: flagged correct code at {path}:{line}: {hits[0]['rule']}")
    if any(x["rule"] == "small-target" and x["kind"] == "violation" and x["line"] in (55, 63)
           for x in found):
        failures.append("fixture: 30x30 buttons called a violation; the ground truth wants guidance")
    print(f"fixture: {len(EXPECTED & got)}/{len(EXPECTED)} expected findings, "
          f"{len(found)} findings in all")

    clean = run_check(CLEAN)
    for x in clean:
        failures.append(f"clean file: unexpected {x['kind']} {x['rule']} at line {x['line']}: {x['message'][:70]}")
    print(f"clean file: {len(clean)} findings")

    tricky = run_check(TRICKY)
    for x in tricky:
        failures.append(f"comments/strings: unexpected {x['rule']} at line {x['line']}")
    print(f"comments and strings: {len(tricky)} findings")

    with tempfile.TemporaryDirectory() as d:
        ok_path = os.path.join(d, "Clean.swift")
        open(ok_path, "w").write(CLEAN)
        bad = subprocess.run([sys.executable, CHECK, FIXTURE], capture_output=True, text=True)
        good = subprocess.run([sys.executable, CHECK, ok_path], capture_output=True, text=True)
    if bad.returncode != 1 or good.returncode != 0:
        failures.append(f"exit status: fixture {bad.returncode} (want 1), clean {good.returncode} (want 0)")

    for f in failures:
        print("FAIL", f)
    print("\ncheck_swiftui test " + ("passed" if not failures else f"failed: {len(failures)} problems"))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
