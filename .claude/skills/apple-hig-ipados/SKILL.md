---
name: apple-hig-ipados
description: iPadOS design guidance from Apple's Human Interface Guidelines — the conventions, component behavior, and layout rules that are specific to iPadOS rather than shared across Apple platforms. Covers how standard UI differs on iPadOS and the interactions unique to it. Use this whenever building, designing, reviewing, or debugging the UI of a iPadOS app — including SwiftUI and UIKit code review — and especially when deciding how something should look or behave on iPadOS specifically, or how a shared design needs to change to feel native there. Trigger on mentions of iPadOS, iPad apps, or the iPad, even when Apple's guidelines are never named.
---

# Designing for iPadOS

iPadOS is a large touch display that also handles pointer, keyboard, and Apple Pencil input, runs apps side by side, and spans a wide range of window sizes. Guidance that holds across every Apple platform lives in the general `apple-hig` skill; this skill carries what's specific to iPadOS, so you can answer platform questions without reading around the other five.

## What's here

- **`references/platform-notes.md`** — every iPadOS-specific rule in the HIG, collected from the 49 pages that state one. Upstream these are scattered one section at a time across the whole corpus; this is the only place they sit together. **Start here** for "how should this component behave on iPadOS".
- **`references/designing-for-ipados.md`** — Apple's iPadOS overview: the platform's character, its conventions, and what to prioritize.
- **1 iPadOS-only pages**, in full — `apple-pencil-and-scribble` (Apple Pencil and Scribble). Apple marks these as applying to iPadOS alone, so the whole page is iPadOS guidance.

## How to use it

1. **Grep `references/platform-notes.md` first.** It's organized by page under `## <Page Title>` headings, so `grep -n -A20 '^## Sheets' references/platform-notes.md` gets you straight to the iPadOS rules for sheets. If a component isn't in there, the HIG states no iPadOS-specific rule for it — which is a real answer worth giving.

2. **Remember what this skill omits.** platform-notes.md holds only the iPadOS deltas. The general rules still apply and often matter more — a button's minimum hit region, an alert's button wording. When a question needs both, pull the general rule from the `apple-hig` skill's full page (each entry links to it) and layer the iPadOS specifics on top. Answering purely from the deltas gives a confidently incomplete answer.

3. **Say when iPadOS genuinely doesn't differ.** Many components behave identically everywhere, and Apple often says so outright. "The HIG gives no iPadOS-specific rule here, so the general guidance applies" is more useful than inventing a platform quirk to justify the lookup.

4. **Match the API layer to the platform.** The full pages list SwiftUI, UIKit, and AppKit symbols; reach for the framework that actually ships on iPadOS.

---

Scraped from developer.apple.com on 2026-08-11. Regenerate with `python3 scripts/build_platform_skills.py`. Point-in-time snapshot — if a question turns on something that may have shifted with a new OS release, say so rather than presenting the snapshot as certainly current.
