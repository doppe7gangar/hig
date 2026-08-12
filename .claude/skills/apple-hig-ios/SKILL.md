---
name: apple-hig-ios
description: iOS design guidance from Apple's Human Interface Guidelines — the conventions, component behavior, and layout rules that are specific to iOS rather than shared across Apple platforms. Covers how standard UI differs on iOS and the interactions unique to it. Use this whenever building, designing, reviewing, or debugging the UI of a iOS app — including SwiftUI and UIKit code review — and especially when deciding how something should look or behave on iOS specifically, or how a shared design needs to change to feel native there. Trigger on mentions of iOS, iPhone apps, or the iPhone, even when Apple's guidelines are never named.
---

# Designing for iOS

iOS is a handheld, touch-first, mostly one-app-at-a-time device where screen space is scarce and thumbs are the primary input. Guidance that holds across every Apple platform lives in the general `apple-hig` skill; this skill carries what's specific to iOS, so you can answer platform questions without reading around the other five.

## What's here

- **`references/platform-notes.md`** — every iOS-specific rule in the HIG, collected from the 48 pages that state one. Upstream these are scattered one section at a time across the whole corpus; this is the only place they sit together. **Start here** for "how should this component behave on iOS".
- **`references/designing-for-ios.md`** — Apple's iOS overview: the platform's character, its conventions, and what to prioritize.
- **4 iOS-only pages**, in full — `camera-control` (Camera Control), `carplay` (CarPlay), `id-verifier` (ID Verifier), `tap-to-pay-on-iphone` (Tap to Pay on iPhone). Apple marks these as applying to iOS alone, so the whole page is iOS guidance.

## How to use it

1. **Grep `references/platform-notes.md` first.** It's organized by page under `## <Page Title>` headings, so `grep -n -A20 '^## Sheets' references/platform-notes.md` gets you straight to the iOS rules for sheets. If a component isn't in there, the HIG states no iOS-specific rule for it — which is a real answer worth giving.

2. **Remember what this skill omits.** platform-notes.md holds only the iOS deltas. The general rules still apply and often matter more — a button's minimum hit region, an alert's button wording. When a question needs both, pull the general rule from the `apple-hig` skill's full page (each entry links to it) and layer the iOS specifics on top. Answering purely from the deltas gives a confidently incomplete answer.

3. **Say when iOS genuinely doesn't differ.** Many components behave identically everywhere, and Apple often says so outright. "The HIG gives no iOS-specific rule here, so the general guidance applies" is more useful than inventing a platform quirk to justify the lookup.

4. **Match the API layer to the platform.** The full pages list SwiftUI, UIKit, and AppKit symbols; reach for the framework that actually ships on iOS.

---

Scraped from developer.apple.com on 2026-08-11. Regenerate with `python3 scripts/build_platform_skills.py`. Point-in-time snapshot — if a question turns on something that may have shifted with a new OS release, say so rather than presenting the snapshot as certainly current.
