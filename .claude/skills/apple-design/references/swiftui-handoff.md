# From the design to SwiftUI

The design is HTML because a browser can show it to anyone. The app is
SwiftUI, and most of what the kit measured is something SwiftUI already
draws: row heights, separator insets, bar heights, the grouped
background, the corner radii, the tab bar's glass. Translate what the design
*decided*, such as which screens exist, what is in each list, which
states each screen has, which symbol, which words and which accent. Don't
translate how the browser had to be told to draw iOS.

Then check the result:

```bash
python3 check_handoff.py ./design ./MyApp      # what the design decided, present in the code?
python3 ../apple-hig/check_swiftui.py ./MyApp  # HIG problems the code alone decides
```

## What to carry across

| In the design | In SwiftUI |
|---|---|
| A `.largetitle` / `.ios-navbar__title` | `.navigationTitle("Balances")` inside a `NavigationStack`. Large is the default for a top-level screen; for a pushed screen with a centred title, `.navigationBarTitleDisplayMode(.inline)` |
| A screen reached with `data-go` | `NavigationLink(value:)` plus `.navigationDestination(for:)`, or a `NavigationLink` with a destination |
| `.ios-tabbar`, one `__item` per tab | `TabView` with one `Tab("Label", systemImage: "name")` per item |
| `.ios-controls__item` in the bar | A `Button` in `.toolbar { ToolbarItem(placement: .topBarTrailing) { … } }`. iOS 26 groups and glazes toolbar buttons itself; `ToolbarSpacer` separates groups |
| `.ios-list` | `List { Section { … } }.listStyle(.insetGrouped)`. A settings-style screen of inputs is `Form`, which groups on its own |
| `.ios-list__header` / `__footer` | `Section { … } header: { Text("…") } footer: { Text("…") }` |
| `.ios-list__title` + `__value` | `LabeledContent("Title", value: "Value")`, or an `HStack` of two `Text`s with the value `.foregroundStyle(.secondary)` |
| `.ios-list__row--tappable` + chevron | `NavigationLink`. It draws the chevron; don't add one |
| `.rowicon` with `data-sf-symbol` | `Label("Title", systemImage: "name")`, or `Image(systemName:)` coloured with `.foregroundStyle(.orange)` when colour carries meaning |
| `.ios-switch` | `Toggle("Label", isOn: $value)` |
| `.ios-segmented` | `Picker("Label", selection: $value) { … }.pickerStyle(.segmented)` |
| `.ios-stepper` | `Stepper("Label", value: $value, in: 0...10)` |
| `.ios-slider` | `Slider(value: $value)` |
| `.ios-field` | `TextField("Placeholder", text: $value)`; `SecureField` for passwords |
| `.ios-chip` | A `Button` with `.buttonStyle(.bordered)` and `.buttonBorderShape(.capsule)`, or a `Picker`/`Menu` when the chips are a choice |
| `.ios-btn--filled` | `Button("Title") { … }.buttonStyle(.borderedProminent)` |
| `.ios-btn--tinted` | `.buttonStyle(.bordered)` |
| `.ios-btn--destructive` | `Button("Delete", role: .destructive) { … }` |
| `.ios-glass-btn`, `.ios-sheet__btn` | `.buttonStyle(.glass)`, or `.buttonStyle(.glassProminent)` for the confirming one (iOS 26) |
| `.ios-glass` on a custom floating control | `.glassEffect(.regular, in: .capsule)`; several near each other go in one `GlassEffectContainer`. Bars, toolbars and sheets get glass without asking |
| `.ios-sheet`, or a `data-sheet` layer | `.sheet(isPresented:)` or `.sheet(item:)`, with `.presentationDetents([.medium, .large])` when it opens at half height. The grabber is `.presentationDragIndicator(.visible)`; the bar's Cancel and Done are toolbar items with `.cancellationAction` and `.confirmationAction` placements |
| `.ios-actionsheet` | `.confirmationDialog("Title", isPresented: $shown) { … } message: { … }` |
| `.ios-alert` | `.alert("Title", isPresented: $shown) { … } message: { … }` |
| `.ios-empty` (the empty state) | `ContentUnavailableView("No bills yet", systemImage: "tray", description: Text("…"))`; with a button, the form that takes `label:`, `description:` and `actions:` |
| `.ios-empty` (the error state) | The same view with the error's symbol and a Try Again button |
| The loading state | `ProgressView()`, or the populated layout with `.redacted(reason: .placeholder)` |
| `.ios-pagecontrol` | `TabView { … }.tabViewStyle(.page)` |
| `data-component="PayWithApplePayButton"` | That type, by name. When the design needs a system component the kit has no class for, it says so with `data-component` |

Every API in this table was checked against `apple-hig/references/framework-index.json`,
except the style shorthands (`.insetGrouped`, `.segmented`,
`.borderedProminent`, `.bordered`, `.page`, `.inline`), which that index
doesn't list.

## The four states

Every screen the design shows in populated, loading, empty and error
states is one view switching on one value, with a preview per state, so
the design's state switcher has a counterpart you can click through in
Xcode's canvas:

```swift
enum LoadState<Value> { case loading, loaded(Value), failed(Error) }

struct BalancesView: View {
    var state: LoadState<[Balance]>

    var body: some View {
        NavigationStack {
            Group {
                switch state {
                case .loading:
                    ProgressView()
                case .loaded(let balances) where balances.isEmpty:
                    ContentUnavailableView("No bills yet", systemImage: "tray",
                        description: Text("Add a bill and it's split here."))
                case .loaded(let balances):
                    List(balances) { BalanceRow(balance: $0) }
                case .failed:
                    ContentUnavailableView("Couldn't load balances",
                        systemImage: "exclamationmark.triangle",
                        description: Text("Check your connection and try again."))
                }
            }
            .navigationTitle("Balances")
        }
    }
}

#Preview("Populated") { BalancesView(state: .loaded(Balance.samples)) }
#Preview("Loading") { BalancesView(state: .loading) }
#Preview("Empty") { BalancesView(state: .loaded([])) }
#Preview("Error") { BalancesView(state: .failed(URLError(.notConnectedToInternet))) }
```

Use the design's sample content in the previews. It was chosen to stress
the layout, with long names, large amounts and the odd missing value.

## What to leave behind

- **Measurements.** No `.frame(height: 52)` on rows, no hand-drawn
  separators, no `.cornerRadius(26)` on a list. The kit measured these so
  the *browser* would match iOS; on iOS the system already does.
- **Colours as hex.** Labels are `.primary` and `.secondary`, backgrounds
  are the system's own. The brand colour goes in the asset catalogue's
  `AccentColor`, light and dark values from the design's `theme.css`, and
  then reaches every control through the accent and `.tint`. A literal
  colour stops adapting to Dark Mode and Increase Contrast.
- **Type sizes.** The design's text classes are text styles: large title,
  title, headline, body, callout, subheadline, footnote, caption. Write
  `.font(.headline)`, never `.font(.system(size: 17, weight: .semibold))`,
  which stops scaling with Dynamic Type.
- **The status bar, home indicator and scroll-collapse script.** They're
  how a page imitates the device.
- **AppleKitTokens.swift**, unless you're drawing something custom. Its
  own header says to prefer the semantic APIs.

## Building it

Nothing here compiles Swift; the checks read it as text. On a Mac:

1. In Xcode, File › New › Project › iOS App, interface SwiftUI.
2. Add the views, set the `AccentColor` asset, and open the canvas. Each
   `#Preview` is one of the design's states; put the design's
   `index.html` beside it in a browser and compare them state by state.
3. From a terminal, a build without a device:
   `xcodebuild -scheme MyApp -destination 'generic/platform=iOS Simulator' build`
4. Run `check_handoff.py` and `check_swiftui.py` again after changes.
