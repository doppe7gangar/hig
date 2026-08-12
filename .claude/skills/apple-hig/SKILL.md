---
name: apple-hig
description: Apple's Human Interface Guidelines (HIG) as searchable local reference — design principles and platform conventions for iOS, iPadOS, macOS, tvOS, visionOS, and watchOS, covering foundations (accessibility, color, typography, layout, materials, motion, Dark Mode, Liquid Glass, SF Symbols, app icons), UI components (buttons, alerts, sheets, sidebars, tab bars, lists, pickers, toolbars, widgets), interaction patterns (onboarding, notifications, modality, drag and drop, undo, search, settings), inputs (gestures, keyboards, Digital Crown, Apple Pencil, eyes, game controls), and technologies (Apple Pay, HomeKit, SharePlay, Sign in with Apple, Live Activities, Siri). Each page also names the exact SwiftUI/UIKit/AppKit API for what it describes. Use this whenever designing, building, reviewing, or critiquing UI for an Apple platform — including SwiftUI or UIKit code review — even when the user never says "HIG" or "Apple guidelines". Covers questions about control styling and sizing, sheet/modal/alert behavior, navigation structure (tab bar vs sidebar vs split view), spacing and tap targets, Dynamic Type and VoiceOver support, contrast ratios, Dark Mode, app icon specs, and "how should this differ on iPad vs Mac vs Vision Pro".
---

# Apple Human Interface Guidelines

A complete local mirror of Apple's HIG (`developer.apple.com/design/human-interface-guidelines`), plus Apple's design-tool pages, scraped 2026-08-11 — 178 pages in `references/`.

Use it so design answers carry Apple's actual current numbers and wording (tap targets, contrast ratios, type sizes, platform rules) instead of half-remembered general UI knowledge. The specifics genuinely change between OS releases, and stale advice here is worse than no advice — it sounds authoritative while being wrong.

## Finding the right page

**Grep first when the topic is cross-cutting; use the index when it maps to one thing.**

Many important topics are spread across dozens of pages rather than living in one: "Liquid Glass" appears in 19 files, SF Symbols in 31, VoiceOver in 20, contrast in 64. For those, the index below will send you to one page and you'll miss the rest — so search instead:

```
grep -ril "liquid glass" references/
grep -rn "44x44\|hit region" references/
```

When the question maps cleanly onto a component, pattern, or platform ("how do sheets work", "designing for watchOS"), skip the search and read that page directly.

Filenames are the page title in kebab-case, so you can usually guess the path without consulting the index: Tab bars → `references/tab-bars.md`, Live Activities → `references/live-activities.md`. Five exceptions: `gyro-and-accelerometer.md` (Gyroscope and accelerometer), `resources.md` (Apple Design Resources), `sf-symbols-app.md` (the SF Symbols *app*, vs `sf-symbols.md` for symbol usage guidance), `pass-designer.md`, `design.md`.

## How the pages are structured

Nearly every page follows the same shape, so you can jump straight to the part that answers the question:

- **Intro + Best practices** — the bolded lead sentences are the actual rules; the text after each explains the reasoning. When citing guidance, the bolded sentence is usually the quotable line.
- **Platform considerations** (148 of 178 pages) — where iOS/iPadOS/macOS/tvOS/visionOS/watchOS differences live. **Always read this section before answering anything platform-specific.** A page's main body often describes the iOS behavior, and the Mac or visionOS rule differs in ways the intro never hints at.
- **Resources → Developer documentation** (147 pages) — the exact SwiftUI, UIKit, and AppKit APIs implementing that guidance. See below.
- **Change log** — dates when guidance changed. Useful for judging whether something is new (e.g. Liquid Glass guidance landed in 2025) or long-standing.

## Connecting guidance to code

This is the part that makes the HIG useful inside a coding session rather than just a design conversation. Each page's **Developer documentation** section names the real API for the thing being described — `sheets.md`, for instance, lists `sheet(item:onDismiss:content:)` (SwiftUI), `UISheetPresentationController` (UIKit), and `presentAsSheet(_:)` (AppKit).

So when you're implementing or reviewing, read the page for the rule *and* pull the API name from that section. It saves guessing at the right modifier or class, and it keeps the recommendation concrete: "use a sheet, and on iOS that's `UISheetPresentationController` with detents" beats "consider a sheet here."

## Reviewing existing UI code

When asked to check SwiftUI/UIKit code or a design against the HIG, resist reviewing against everything — a 178-page checklist produces noise. Instead:

1. Identify which components and patterns the code actually uses (a `TabView`, a `.sheet`, a destructive `Button`).
2. Read those specific pages, including their Platform considerations for the platforms this code targets.
3. Report only real conflicts with Apple's stated guidance, quoting the relevant line. Distinguish firm rules ("a button needs a hit region of at least 44x44 pt") from softer preferences ("prefer a tab bar") — presenting a preference as a violation erodes trust in the whole review.
4. Say when something is a judgment call the HIG doesn't settle. The guidelines deliberately leave a lot open, and inventing a rule to fill the gap is the main failure mode here.

## Reference index

All paths are `references/<name>.md`.

**Overview** — `human-interface-guidelines.md` (top-level), `design.md` (Apple's design landing page)

**Getting started** — `getting-started.md`, `design-principles.md`, and `designing-for-` + `ios`, `ipados`, `macos`, `tvos`, `visionos`, `watchos`, `games`

**Foundations** — `foundations.md`, `accessibility`, `app-icons`, `branding`, `color`, `dark-mode`, `icons`, `images`, `immersive-experiences`, `inclusion`, `layout`, `materials`, `motion`, `privacy`, `right-to-left`, `sf-symbols`, `spatial-layout`, `typography`, `writing`

**Patterns** — `patterns.md`, `charting-data`, `collaboration-and-sharing`, `drag-and-drop`, `entering-data`, `feedback`, `file-management`, `going-full-screen`, `launching`, `live-viewing-apps`, `loading`, `managing-accounts`, `managing-notifications`, `modality`, `multitasking`, `offering-help`, `onboarding`, `playing-audio`, `playing-haptics`, `playing-video`, `printing`, `ratings-and-reviews`, `searching`, `settings`, `undo-and-redo`, `workouts`

**Components** — `components.md`, grouped into eight sections (each section hub is its own page too):
- *Content* (`content`) — `charts`, `image-views`, `text-views`, `web-views`
- *Layout and organization* (`layout-and-organization`) — `boxes`, `collections`, `column-views`, `disclosure-controls`, `labels`, `lists-and-tables`, `lockups`, `outline-views`, `split-views`, `tab-views`
- *Menus and actions* (`menus-and-actions`) — `activity-views`, `buttons`, `context-menus`, `dock-menus`, `edit-menus`, `home-screen-quick-actions`, `menus`, `ornaments`, `pop-up-buttons`, `pull-down-buttons`, `the-menu-bar`, `toolbars`
- *Navigation and search* (`navigation-and-search`) — `path-controls`, `search-fields`, `sidebars`, `tab-bars`, `token-fields`
- *Presentation* (`presentation`) — `action-sheets`, `alerts`, `page-controls`, `panels`, `popovers`, `scroll-views`, `sheets`, `windows`
- *Selection and input* (`selection-and-input`) — `color-wells`, `combo-boxes`, `digit-entry-views`, `image-wells`, `pickers`, `segmented-controls`, `sliders`, `steppers`, `text-fields`, `toggles`, `virtual-keyboards`
- *Status* (`status`) — `activity-rings`, `gauges`, `progress-indicators`, `rating-indicators`
- *System experiences* (`system-experiences`) — `app-shortcuts`, `complications`, `controls`, `live-activities`, `notifications`, `snippets`, `status-bars`, `top-shelf`, `watch-faces`, `widgets`

**Inputs** — `inputs.md`, `action-button`, `apple-pencil-and-scribble`, `camera-control`, `digital-crown`, `eyes`, `focus-and-selection`, `game-controls`, `gestures`, `gyro-and-accelerometer`, `keyboards`, `nearby-interactions`, `pointing-devices`, `remotes`

**Technologies** — `technologies.md`, `airplay`, `always-on`, `app-clips`, `apple-pay`, `augmented-reality`, `carekit`, `carplay`, `game-center`, `generative-ai`, `healthkit`, `homekit`, `icloud`, `id-verifier`, `imessage-apps-and-stickers`, `in-app-purchase`, `live-photos`, `mac-catalyst`, `machine-learning`, `maps`, `nfc`, `photo-editing`, `researchkit`, `shareplay`, `shazamkit`, `sign-in-with-apple`, `siri`, `tap-to-pay-on-iphone`, `voiceover`, `wallet`

**Apple's design tools** — `icon-composer`, `sf-symbols-app`, `pass-designer`, `reality-composer-pro`, `resources` (downloadable Figma/Sketch/Photoshop kits, fonts, product bezels)

## Things worth getting right

- **`sf-symbols.md` vs `sf-symbols-app.md`** — the first is HIG guidance on using symbols in a UI; the second is the SF Symbols app's product page. Design questions want the first.
- **The tool pages link to downloads, they aren't the downloads.** `resources.md`, `icon-composer.md`, and friends point at `.dmg`/Figma/Sketch files on Apple's servers. Give the user the link; don't imply the assets are local.
- **Images are hotlinked, not mirrored.** Pages embed real Apple CDN image URLs inline. If a visual detail matters, the URL is right there to hand over or fetch — but the bytes aren't in this repo.
- **This is a snapshot, not a live feed.** If a question touches something likely to have shifted since the scrape date — a brand-new OS, a component that's been redesigned — answer from the reference but say it's a point-in-time copy and point at developer.apple.com to confirm.
