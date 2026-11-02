# Patterns: HIG-correct SwiftUI starting points

Everything else in this skill answers *"what does Apple say?"*. This answers *"so what do I write?"* — correct-by-default scaffolding for the things people build most, with the real API and the real numbers already in place.

**This file is synthesis, not extraction.** The other references are pulled mechanically from Apple's pages; these snippets are assembled from them. Every rule and number cites its source so you can check the reasoning, and anything *not* backed by the corpus is marked **[not in corpus]** rather than passed off as Apple's word.

Adapt rather than paste — these encode the constraints, not your layout.

---

## Text that scales

The single most common violation, and it fails silently: fixed point sizes ignore the user's text-size setting, so the app is unusable for anyone who's changed it.

```swift
// Correct — scales with the user's setting
Text("Notifications").font(.body)
Text("Settings").font(.largeTitle)

// Wrong — frozen, ignores Dynamic Type
Text("Notifications").font(.system(size: 15))
```

- Reach for the system font, its built-in text styles and SF Symbols before anything custom: they scale with Dynamic Type for free — [Typography](https://developer.apple.com/design/human-interface-guidelines/typography)
- If you must use a fixed size, the floor is **11 pt on iOS/iPadOS** (macOS 10, tvOS 23, visionOS 12, watchOS 12) — `numbers.md` → Accessibility. Default body is 17 pt.

Need a custom face but still want scaling: `.font(.custom("Name", size: 17, relativeTo: .body))`. **[not in corpus]** — the HIG states the requirement, not this API.

---

## Tappable things

```swift
Button(action: dismiss) {
    Image(systemName: "xmark")
}
.frame(minWidth: 44, minHeight: 44)   // hit region, not icon size
```

The hit region is what counts, not the drawn size: at least **44×44 pt**, and **60×60 pt** in visionOS, however people point at it — [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons)

The icon can be smaller; the *touch target* can't. A 24 pt glyph in a 44 pt frame is correct.

---

## Choosing a presentation

Match Apple's stated purpose for each, then use its API. Full decision table in `SKILL.md`; APIs from `api-map.md`.

```swift
// Choices after an action the person just took
.confirmationDialog("Export as", isPresented: $showExport) {
    Button("PDF") { export(.pdf) }
    Button("PNG") { export(.png) }
    Button("Cancel", role: .cancel) { }
}

// Critical info, or an uncommon + unrecoverable action
.alert("Delete account?", isPresented: $showDelete) {
    Button("Delete", role: .destructive) { delete() }
    Button("Cancel", role: .cancel) { }
} message: {
    Text("This can't be undone.")
}

// A scoped task tied to the current context
.sheet(item: $editing) { item in EditView(item: item) }

// In-depth content or a complex task
.fullScreenCover(isPresented: $onboarding) { OnboardingFlow() }
```

- `confirmationDialog(_:isPresented:titleVisibility:actions:)`, `alert(_:isPresented:actions:)`, `sheet(item:onDismiss:content:)`, `fullScreenCover(item:onDismiss:content:)` — all in `api-map.md`
- Choices that follow from something the person just chose to do belong in an action sheet, not an alert — [Action sheets](https://developer.apple.com/design/human-interface-guidelines/action-sheets)
- Something common that can be undone doesn't need an alert, even when it deletes: deleting one email needs no confirmation — [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts)
- One sheet at a time from the main interface; don't stack them — [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets)

### Destructive styling has a catch

```swift
// Person chose "Empty Trash" themselves → confirm WITHOUT destructive styling
Button("Empty Trash") { empty() }          // not .destructive

// Consequence they didn't ask for → destructive styling
Button("Delete", role: .destructive) { delete() }
```

The destructive style marks a destructive action the person **didn't set out to take**; when they chose it on purpose, the plain style is enough — [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts)

Reflexively marking every destructive button red is the common mistake, and it inverts Apple's rule.

---

## Navigation that adapts

```swift
// iPhone + iPad: tab bar that becomes a sidebar where there's room
TabView {
    Tab("Library", systemImage: "books.vertical") { LibraryView() }
    Tab("Search",  systemImage: "magnifyingglass") { SearchView() }
}
.tabViewStyle(.sidebarAdaptable)

// Sidebar only, no tab bar — a different construct
NavigationSplitView {
    SidebarView()
} detail: {
    DetailView()
}
```

- On iPadOS, a tab bar is the first choice for moving between top-level sections — [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars)
- Tabs navigate; they don't do things. Actions belong in a toolbar.
- Aim for **five or fewer** tabs when they're customizable, for consistency across size classes.
- `TabView`, `NavigationSplitView` — `api-map.md`. Sidebar-only means `NavigationSplitView`, *not* a `TabView`.

---

## Empty states

```swift
ContentUnavailableView(
    "No Bookmarks",
    systemImage: "bookmark",
    description: Text("Bookmarks you save will appear here.")
)
```

A blank screen should say what to do next, and offer the button or link that does it. It's usually temporary, so nothing the person needs later should live only there — [Writing](https://developer.apple.com/design/human-interface-guidelines/writing)

Filed under **Writing**, not any component page — see `concepts.md`. `ContentUnavailableView` is **[not in corpus]**; the HIG describes the pattern without naming the API.

---

## Before you call a screen done

Fast pass — each maps to a rule you can cite:

- [ ] No `.font(.system(size:))` on user-facing text → Dynamic Type
- [ ] Every tappable control ≥ 44×44 pt hit region (60×60 visionOS)
- [ ] Destructive styling only where the person *didn't* choose the action
- [ ] Alerts reserved for critical or unrecoverable — not routine confirmations
- [ ] Empty/loading/error states exist, not just the happy path
- [ ] Text contrast ≥ 4.5:1 under 17 pt, 3:1 at 18 pt or bold — `numbers.md`
- [ ] Light **and** dark checked — compare against the measured recipes in `../apple-ui-kit`
- [ ] Interactive states: pressed and disabled, not just default
- [ ] System components preferred over hand-rolled ones — `api-map.md`
- [ ] On iPad/Mac: layout adapts, doesn't just stretch — the official page
