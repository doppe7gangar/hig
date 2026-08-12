---
name: apple-hig-macos
description: macOS design guidance from Apple's Human Interface Guidelines — the conventions, component behavior, and layout rules that are specific to macOS rather than shared across Apple platforms. Covers how standard UI differs on macOS and the interactions unique to it. Use this whenever building, designing, reviewing, or debugging the UI of a macOS app — including SwiftUI and AppKit, or UIKit under Mac Catalyst code review — and especially when deciding how something should look or behave on macOS specifically, or how a shared design needs to change to feel native there. Trigger on mentions of macOS, Mac apps, or the Mac, even when Apple's guidelines are never named.
---

# Designing for macOS

macOS is a pointer-driven, multi-window desktop with a menu bar, where apps are expected to support keyboard navigation, resizing, and many simultaneous documents. Guidance that holds across every Apple platform lives in the general `apple-hig` skill; this skill carries what's specific to macOS, so you can answer platform questions without reading around the other five.

## What's here

- **`references/platform-notes.md`** — every macOS-specific rule in the HIG, collected from the 48 pages that state one. Upstream these are scattered one section at a time across the whole corpus; this is the only place they sit together. **Start here** for "how should this component behave on macOS".
- **`references/designing-for-macos.md`** — Apple's macOS overview: the platform's character, its conventions, and what to prioritize.
- **9 macOS-only pages**, in full — `column-views` (Column views), `combo-boxes` (Combo boxes), `dock-menus` (Dock menus), `image-wells` (Image wells), `outline-views` (Outline views), `panels` (Panels), `path-controls` (Path controls), `rating-indicators` (Rating indicators), `token-fields` (Token fields). Apple marks these as applying to macOS alone, so the whole page is macOS guidance.

## How to use it

1. **Grep `references/platform-notes.md` first.** It's organized by page under `## <Page Title>` headings, so `grep -n -A20 '^## Sheets' references/platform-notes.md` gets you straight to the macOS rules for sheets. If a component isn't in there, the HIG states no macOS-specific rule for it — which is a real answer worth giving.

2. **Remember what this skill omits.** platform-notes.md holds only the macOS deltas. The general rules still apply and often matter more — a button's minimum hit region, an alert's button wording. When a question needs both, pull the general rule from the `apple-hig` skill's full page (each entry links to it) and layer the macOS specifics on top. Answering purely from the deltas gives a confidently incomplete answer.

3. **Say when macOS genuinely doesn't differ.** Many components behave identically everywhere, and Apple often says so outright. "The HIG gives no macOS-specific rule here, so the general guidance applies" is more useful than inventing a platform quirk to justify the lookup.

4. **Match the API layer to the platform.** The full pages list SwiftUI, UIKit, and AppKit symbols; macOS work usually means AppKit or SwiftUI, not UIKit — recommending a `UI...` class for a Mac app is a common and obvious miss.

---

Scraped from developer.apple.com on 2026-08-11. Regenerate with `python3 scripts/build_platform_skills.py`. Point-in-time snapshot — if a question turns on something that may have shifted with a new OS release, say so rather than presenting the snapshot as certainly current.
