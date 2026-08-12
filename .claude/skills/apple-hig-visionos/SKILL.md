---
name: apple-hig-visionos
description: visionOS design guidance from Apple's Human Interface Guidelines — the conventions, component behavior, and layout rules that are specific to visionOS rather than shared across Apple platforms. Covers how standard UI differs on visionOS and the interactions unique to it. Use this whenever building, designing, reviewing, or debugging the UI of a visionOS app — including SwiftUI and RealityKit code review — and especially when deciding how something should look or behave on visionOS specifically, or how a shared design needs to change to feel native there. Trigger on mentions of visionOS, Apple Vision Pro, or spatial apps, even when Apple's guidelines are never named.
---

# Designing for visionOS

visionOS is a spatial display where windows exist in three dimensions around the wearer and the primary input is eyes plus hands. Guidance that holds across every Apple platform lives in the general `apple-hig` skill; this skill carries what's specific to visionOS, so you can answer platform questions without reading around the other five.

## What's here

- **`references/platform-notes.md`** — every visionOS-specific rule in the HIG, collected from the 44 pages that state one. Upstream these are scattered one section at a time across the whole corpus; this is the only place they sit together. **Start here** for "how should this component behave on visionOS".
- **`references/designing-for-visionos.md`** — Apple's visionOS overview: the platform's character, its conventions, and what to prioritize.
- **4 visionOS-only pages**, in full — `eyes` (Eyes), `immersive-experiences` (Immersive experiences), `ornaments` (Ornaments), `spatial-layout` (Spatial layout). Apple marks these as applying to visionOS alone, so the whole page is visionOS guidance.

## How to use it

1. **Grep `references/platform-notes.md` first.** It's organized by page under `## <Page Title>` headings, so `grep -n -A20 '^## Sheets' references/platform-notes.md` gets you straight to the visionOS rules for sheets. If a component isn't in there, the HIG states no visionOS-specific rule for it — which is a real answer worth giving.

2. **Remember what this skill omits.** platform-notes.md holds only the visionOS deltas. The general rules still apply and often matter more — a button's minimum hit region, an alert's button wording. When a question needs both, pull the general rule from the `apple-hig` skill's full page (each entry links to it) and layer the visionOS specifics on top. Answering purely from the deltas gives a confidently incomplete answer.

3. **Say when visionOS genuinely doesn't differ.** Many components behave identically everywhere, and Apple often says so outright. "The HIG gives no visionOS-specific rule here, so the general guidance applies" is more useful than inventing a platform quirk to justify the lookup.

4. **Match the API layer to the platform.** The full pages list SwiftUI, UIKit, and AppKit symbols; reach for the framework that actually ships on visionOS.

---

Scraped from developer.apple.com on 2026-08-11. Regenerate with `python3 scripts/build_platform_skills.py`. Point-in-time snapshot — if a question turns on something that may have shifted with a new OS release, say so rather than presenting the snapshot as certainly current.
