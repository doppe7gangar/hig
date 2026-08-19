# Ground truth — written before running the review

Seeded into `HabitApp/`. Graded on whether a review finds these *without
being told to look for HIG issues* — the prompt never says Apple, HIG,
design, or guidelines.

## Should be found (seeded defects)

| # | Defect | Where | Force |
|---|---|---|---|
| 1 | Seven tabs in `TabView` | ContentView.swift:6-28 | guidance |
| 2 | Hardcoded `Color.white` backgrounds — breaks Dark Mode | ContentView 48, 141, 96 | violation |
| 3 | `.foregroundColor(.black)` on primary label | ContentView:122 | violation |
| 4 | Fixed font sizes `.system(size: 15/12/20)` — kills Dynamic Type | ContentView 121, 124, 87 | violation |
| 5 | Status conveyed by colour alone (green/red 10pt dot) | ContentView:113-115 | violation |
| 6 | Custom `ZStack` modal instead of a system presentation | ContentView:82-104 | violation |
| 7 | Alert used for a common, recoverable delete | ContentView:72-80 | guidance |
| 8 | Destructive buttons lack `role: .destructive` | ContentView:76, SupportingViews:52 | violation |
| 9 | "Reset All Progress" styled `.blue` — destructive styled as normal | SupportingViews:55 | violation |
| 10 | Icon-only buttons with no accessibility label | ContentView 56-68, 145-152 | violation |
| 11 | Chart bars distinguished by colour only, incl. red/green pair | SupportingViews:95-104 | violation |
| 12 | Toolbar icon buttons at 30×30 | ContentView 60, 67 | judgment — 28×28 is the stated iOS minimum, 44×44 the default for frequently-used controls. A review that calls 30×30 a flat violation of "44 minimum" is **wrong**, and that error is worth catching. |

## Should NOT be flagged (correct code — false-positive test)

- 44×44 completion toggle — ContentView:131-139
- `.sheet` for AddHabitView — a scoped task, correct use
- `.cancellationAction` / `.confirmationAction` placements — correct
- `.font(.body)`, `.headline`, `.footnote`, `.caption` in History/Stats
- `foregroundStyle(.secondary)` — correct semantic style

## Out of scope (should stay quiet or clearly separate it)

- `.alert(isPresented: .constant(...))` is a genuine SwiftUI bug — the
  binding can't be written back to. Not a HIG issue. Mentioning it is
  fine; filing it as a HIG violation is not.
- `.accentColor` is soft-deprecated in favour of `.tint`. API currency,
  not HIG.

## Grading

- **Recall** — how many of 1-11 are found.
- **Precision** — anything from the "should not" list flagged is a false positive.
- **Calibration** — #12 called judgment rather than violation; force labels
  broadly right.
- **Grounding** — claims cite a page, and quotes pass `verify_quotes.py`.
