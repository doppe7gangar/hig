---
name: apple-hig-tvos
description: tvOS design guidance from Apple's Human Interface Guidelines — the conventions, component behavior, and layout rules that are specific to tvOS rather than shared across Apple platforms. Covers how standard UI differs on tvOS and the interactions unique to it. Use this whenever building, designing, reviewing, or debugging the UI of a tvOS app — including SwiftUI and UIKit code review — and especially when deciding how something should look or behave on tvOS specifically, or how a shared design needs to change to feel native there. Trigger on mentions of tvOS, Apple TV apps, or the TV app experience, even when Apple's guidelines are never named.
---

# Designing for tvOS

tvOS is a shared, ten-foot screen navigated by remote through a focus model rather than direct manipulation, with no cursor and no touch. Guidance that holds across every Apple platform lives in the general `apple-hig` skill; this skill carries what's specific to tvOS, so you can answer platform questions without reading around the other five.

## What's here

- **`references/platform-notes.md`** — every tvOS-specific rule in the HIG, collected from the 25 pages that state one. Upstream these are scattered one section at a time across the whole corpus; this is the only place they sit together. **Start here** for "how should this component behave on tvOS".
- **`references/designing-for-tvos.md`** — Apple's tvOS overview: the platform's character, its conventions, and what to prioritize.
- **4 tvOS-only pages**, in full — `digit-entry-views` (Digit entry views), `lockups` (Lockups), `remotes` (Remotes), `top-shelf` (Top Shelf). Apple marks these as applying to tvOS alone, so the whole page is tvOS guidance.

## How to use it

1. **Grep `references/platform-notes.md` first.** It's organized by page under `## <Page Title>` headings, so `grep -n -A20 '^## Sheets' references/platform-notes.md` gets you straight to the tvOS rules for sheets. If a component isn't in there, the HIG states no tvOS-specific rule for it — which is a real answer worth giving.

2. **Remember what this skill omits.** platform-notes.md holds only the tvOS deltas. The general rules still apply and often matter more — a button's minimum hit region, an alert's button wording. When a question needs both, pull the general rule from the `apple-hig` skill's full page (each entry links to it) and layer the tvOS specifics on top. Answering purely from the deltas gives a confidently incomplete answer.

3. **Say when tvOS genuinely doesn't differ.** Many components behave identically everywhere, and Apple often says so outright. "The HIG gives no tvOS-specific rule here, so the general guidance applies" is more useful than inventing a platform quirk to justify the lookup.

4. **Match the API layer to the platform.** The full pages list SwiftUI, UIKit, and AppKit symbols; reach for the framework that actually ships on tvOS.

---

Scraped from developer.apple.com on 2026-08-11. Regenerate with `python3 scripts/build_platform_skills.py`. Point-in-time snapshot — if a question turns on something that may have shifted with a new OS release, say so rather than presenting the snapshot as certainly current.
