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

## macOS: HIG-first, even without a measured Mac kit

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

Use SwiftUI/AppKit system components where available. Do not import iPhone proportions, oversized touch spacing, bottom-tab assumptions, or mobile modality simply to make the interface look Apple-like.

The current iOS measured corpus may be used for broad comparative relationships only, and must never be described as measured macOS appearance.

## iOS

Constrain candidates around touch-first navigation, content priority, direct manipulation, safe-area behavior, sheets/push navigation, and peer-level tabs only when justified.

Do not generate desktop inspector/table/sidebar candidates for iPhone merely to satisfy divergence.

## iPadOS

Do not treat iPad as a scaled iPhone. Consider width, split relationships, sidebars, adaptable tabs, inspectors, pointer/keyboard use, and multitasking where the task benefits.

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