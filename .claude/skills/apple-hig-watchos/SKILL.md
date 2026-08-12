---
name: apple-hig-watchos
description: watchOS design guidance from Apple's Human Interface Guidelines — the conventions, component behavior, and layout rules that are specific to watchOS rather than shared across Apple platforms. Covers how standard UI differs on watchOS and the interactions unique to it. Use this whenever building, designing, reviewing, or debugging the UI of a watchOS app — including SwiftUI and WatchKit code review — and especially when deciding how something should look or behave on watchOS specifically, or how a shared design needs to change to feel native there. Trigger on mentions of watchOS, Apple Watch apps, watch faces, or complications, even when Apple's guidelines are never named.
---

# Designing for watchOS

watchOS is a very small, glanceable screen worn on the wrist, built for interactions measured in seconds, with the Digital Crown as a key input. Guidance that holds across every Apple platform lives in the general `apple-hig` skill; this skill carries what's specific to watchOS, so you can answer platform questions without reading around the other five.

## What's here

- **`references/platform-notes.md`** — every watchOS-specific rule in the HIG, collected from the 44 pages that state one. Upstream these are scattered one section at a time across the whole corpus; this is the only place they sit together. **Start here** for "how should this component behave on watchOS".
- **`references/designing-for-watchos.md`** — Apple's watchOS overview: the platform's character, its conventions, and what to prioritize.
- **2 watchOS-only pages**, in full — `complications` (Complications), `watch-faces` (Watch faces). Apple marks these as applying to watchOS alone, so the whole page is watchOS guidance.

## How to use it

1. **Grep `references/platform-notes.md` first.** It's organized by page under `## <Page Title>` headings, so `grep -n -A20 '^## Sheets' references/platform-notes.md` gets you straight to the watchOS rules for sheets. If a component isn't in there, the HIG states no watchOS-specific rule for it — which is a real answer worth giving.

2. **Remember what this skill omits.** platform-notes.md holds only the watchOS deltas. The general rules still apply and often matter more — a button's minimum hit region, an alert's button wording. When a question needs both, pull the general rule from the `apple-hig` skill's full page (each entry links to it) and layer the watchOS specifics on top. Answering purely from the deltas gives a confidently incomplete answer.

3. **Say when watchOS genuinely doesn't differ.** Many components behave identically everywhere, and Apple often says so outright. "The HIG gives no watchOS-specific rule here, so the general guidance applies" is more useful than inventing a platform quirk to justify the lookup.

4. **Match the API layer to the platform.** The full pages list SwiftUI, UIKit, and AppKit symbols; reach for the framework that actually ships on watchOS.

---

Scraped from developer.apple.com on 2026-08-11. Regenerate with `python3 scripts/build_platform_skills.py`. Point-in-time snapshot — if a question turns on something that may have shifted with a new OS release, say so rather than presenting the snapshot as certainly current.
