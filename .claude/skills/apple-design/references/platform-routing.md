# Platform-first design routing

Use this immediately after identifying the target platform and before generating divergent layout candidates.

## Authority order

The absence of a measured visual kit never means the platform is unconstrained.

Use this authority order:

1. **Apple HIG** — behavior, structure, platform conventions, accessibility, adaptation
2. **Platform differences** — exceptions and input/window/navigation model
3. **System APIs/components** — prefer the platform-provided primitive where one exists
4. **Product composition** — hierarchy and spatial model for the actual task
5. **Measured visual corpus** — visual evidence only where a measured corpus exists
6. **Design judgment** — decisions not settled by the sources above

A measured kit supplements HIG. It does not replace it.

## Required HIG routing

For native Apple-platform work, inspect these before composition:

- `apple-hig/references/platform-diffs.md`
- relevant entries in `apple-hig/references/rules.md`
- `apple-hig/references/components.md` when choosing controls/presentations
- `apple-hig/references/framework-index.md` before inventing a custom control
- `apple-hig/references/api-map.md` when implementation/API choice matters
- relevant full pages only when the reasoning behind a rule matters

Do not use remembered platform folklore when the corpus can answer the question.

## macOS: a window, not a phone

Scaffold with `new_project.py --kind macos` (`--model sidebar` for a
library or inbox, `document` for a canvas) and build on
`macos-components.css`. Its window, traffic lights, sidebar, toolbar glass
controls, buttons, fields, menus, tables, sheets and alerts are measured
from Apple's macOS 27 design kit; it has fewer recipes than iOS, so
compose what it lacks from `apple-hig` and say so.

For macOS-first work, explicitly reason about:

- windows and multiwindow behavior
- title/toolbar region
- sidebars and split views
- inspectors
- tables and dense lists
- menus and context menus
- keyboard commands and shortcuts
- pointer/hover behavior
- focus and selection
- popovers and sheets
- resizable windows
- inactive-window state where relevant
- drag and drop where relevant

Use SwiftUI/AppKit system components where available. Do not import iPhone proportions, oversized touch spacing, bottom-tab assumptions, or mobile modality simply to make the interface look Apple-like. Body text on a Mac is 13pt, controls are 24pt, and the sidebar and toolbar replace the tab bar and navigation bar.

Never describe an iOS measurement as macOS appearance, or the reverse.

## iOS

Constrain candidates around touch-first navigation, content priority, direct manipulation, safe-area behavior, sheets/push navigation, and peer-level tabs only when justified.

Do not generate desktop inspector/table/sidebar candidates for iPhone merely to satisfy divergence.

## iPadOS

Do not treat iPad as a scaled iPhone. Consider width, split relationships, sidebars, adaptable tabs, inspectors, pointer/keyboard use, and multitasking where the task benefits.

Scaffold with `new_project.py --kind ipados` (`--model sidebar` for a
split view, `tabs` for the tab bar at the top) and build on
`ipados-components.css`, measured from Apple's iOS and iPadOS 27 design
kit: the 320pt glass sidebar with its 44pt rows, the toolbar whose
buttons float as glass with the large title under them, the tab bar at
the top centre, sheets and popovers with 38pt corners. The iPhone's
bottom tab bar has no place on an iPad; `check_design.py` fails it.

## visionOS

Candidates must respect eyes-and-hands interaction, depth, windows/volumes/immersive spaces, and 60pt interaction guidance where applicable. Do not reuse touch-only assumptions.

## watchOS

Favor glanceability, brief interaction, crown/touch expectations, and severe space constraints. Reject desktop/mobile compositions before divergence.

## tvOS

Treat navigation as focus-driven rather than pointer/touch driven. Persistent small controls and hover-dependent discovery are invalid assumptions.

## Web product

The browser is its own platform. Transfer Apple principles—hierarchy, restraint, material discipline, motion purpose, accessibility—but preserve browser expectations, desktop density, keyboard/pointer interaction, responsive behavior, and standard web semantics.

Do not dress a web product in native iOS chrome unless the task truly imitates an iOS surface.

## Marketing/editorial web

HIG does not define the marketing layout. Use Apple-like editorial discipline, but rely on web accessibility and browser behavior rather than native-app chrome.

## Android: Material 3, not an iPhone port

Scaffold with `new_project.py --kind android` (`--model tabs` for three
to five top-level destinations in a nav bar, `stack` for one) and build
on `android-ui-kit`'s `material-components.css`. Its phone, status and
gesture bars, top app bars, nav bar, buttons, FAB, chips, cards, lists,
fields, controls, dialogs, sheets, menus and snackbars are measured from
Google's Material 3 Design Kit, and `theme.css` is a full Material
scheme derived from the brand colour the way Android derives one.

What changes from iOS, and has to:

- a 64 dp top app bar with a title-large title, not a large title
- a 64 dp nav bar with a pill indicator, not a tab bar; a FAB for the
  primary action
- Roboto and Material's 15 type styles, not SF Pro's
- Material Symbols, named in `data-icon`, not SF Symbols
- surfaces as tonal containers, not grouped inset lists and blur
- 48 dp touch targets; sentence-case button labels
- the system back gesture, so no back-chevron text buttons

Apple's HIG doesn't govern Android. Use `apple-hig` for what transfers
(hierarchy, content, accessibility reasoning), and android-ui-kit's
SKILL.md for the platform.

## Cross-platform (`--kind cross`)

Structure transfers; appearance does not. A shared information
hierarchy, a shared commit model and a shared vocabulary are worth
holding across iOS, Android and web. A tab bar, a grouped list and a
capsule button are not — Android has its own controls and its own
expectations, and importing Apple's produces an app that reads as a port.

What the scaffolder emits for this kind:

- the web build, as the shared prototype the three platforms argue over
- `tokens/` — the same brand palette as `.swift`, `.kt` and `colors.xml`,
  both appearances, derived by the contrast pass that produced
  `theme.css` rather than copied out of it

Carry the palette where brand consistency is a deliberate decision.
Carry the *structure* always. Do not carry the chrome. When the Android
side needs a design of its own, scaffold it with `--kind android`; its
`build_m3_theme.py --format compose` hands the scheme to Compose.

On Apple platforms prefer the semantic APIs over these literals —
`Color.accentColor`, `.primary` — since they follow Dark Mode and
Increase Contrast without being told. The exported values are for the
cases the semantic API cannot reach: custom drawing, a canvas, or a
brand colour the system has no name for.

## Platform constraint before divergence

Before proposing candidate layouts, state:

- target platform(s)
- input model(s)
- window/viewport model
- expected density
- navigation constraints
- system components likely to apply
- patterns ruled out by platform fit

Only then generate divergent directions.

This prevents a false choice between one credible native composition and two intentionally bad cross-platform imports.