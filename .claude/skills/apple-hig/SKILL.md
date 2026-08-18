---
name: apple-hig
description: Apple Human Interface Guidelines as a working reference — review UI code or designs against Apple's actual rules, pick the right control or presentation (sheet vs popover vs alert vs full-screen, tab bar vs sidebar vs split view), look up exact specs (tap targets, type sizes, contrast ratios, icon dimensions, safe areas), find the exact SwiftUI/UIKit/AppKit/framework API for a piece of guidance, see the real system appearance of a component (light/dark, pressed/idle, on/off, enabled/disabled) from Apple's actual iOS 27 UI kit, and adapt a design across iOS, iPadOS, macOS, tvOS, visionOS, and watchOS. Contains all 2,280 HIG rules as a greppable checklist, every spec table, a component-purpose index, an API map covering 30+ Apple frameworks, 947 real component screenshots across every interaction state, and the full 178-page corpus. Use whenever building, reviewing, critiquing, or fixing UI for an Apple platform — including SwiftUI, UIKit, and AppKit code review — and whenever a question turns on what Apple actually specifies or actually looks like, rather than general UI instinct. Trigger on Apple platform UI work even when the HIG is never mentioned: "is this button too small", "should this be a sheet or a popover", "why does my Mac app feel wrong", "make this work on iPad", "is this accessible", "what SwiftUI view do I use for this", "what does a disabled toggle look like", app icons, Dark Mode, Dynamic Type, VoiceOver, SF Symbols, Liquid Glass.
---

# Apple Human Interface Guidelines

Apple's design guidance, restructured for doing work rather than browsing. Seven references, each for a different question:

| File | Use it for |
|---|---|
| `references/rules.md` | **2,280 rules as one-line imperatives**, by topic. The review checklist. |
| `references/specs.md` | **Every number** — sizes, ratios, limits — with its source table. |
| `references/platform-diffs.md` | **What changes per platform**, grouped by platform. |
| `references/api-map.md` | **HIG concept → exact API symbol** — SwiftUI, UIKit, AppKit, and 30+ other frameworks (HealthKit, PassKit, StoreKit...). |
| `references/components.md` | **One-line purpose for every page** — the fastest way to find the right component before reading anything else. |
| `references/concepts.md` | **Where guidance actually lives** for cross-cutting concerns (empty states, error handling, contrast, offline) that have no page of their own. |
| `references/assets-index.md` | **What components actually look like** — 947 screenshots from Apple's iOS 27 UI kit, every interaction state. |
| `references/pages/<slug>.md` | Full prose when a rule's *reasoning* matters. |

Grep first. `grep -A1 -i "sheet" references/rules.md` returns every sheet rule in seconds; reading `pages/sheets.md` to find the same thing costs far more context. Reach for the full page when you need the *why*, not the *what*.

## Reviewing UI

The failure mode here is dumping 40 observations of mixed importance. Scope it:

1. **Inventory what's actually there.** List the components and patterns in the code — a `TabView`, a `.sheet`, a destructive `Button`, a custom control replacing a system one. Review those, not the whole HIG.
2. **Pull their rules.** `grep -A1 -i "<component>" references/rules.md` for each. Check numbers against `specs.md`.
3. **Check the API against `api-map.md`.** A hand-rolled view where a system component already exists (a custom modal built from a `ZStack` instead of `.sheet`, a bespoke button instead of `UIButton`/`NSButton`) is itself worth flagging — Apple's guidance assumes the system component, and a reimplementation usually drifts from it silently.
4. **Check the target platforms** in `platform-diffs.md`. A layout that's right on iPhone can be wrong on Mac, and the general rule won't say so.
5. **For custom controls, compare against the real thing** in `assets-index.md`. A reimplemented toggle or button usually gets the default state right and the others wrong — check pressed and disabled specifically, since those are the ones people skip and the ones the written rules describe least.
6. **Sort findings by force**, and say which is which:
   - **Violations** — a stated rule with a number attached. *"44×44 pt minimum hit region; this is 30×30."* Objective, fix it.
   - **Guidance** — Apple says prefer/avoid without a threshold. *"Prefer a tab bar for iPad navigation."* Defensible to deviate with reason.
   - **Judgment** — the HIG is silent. Say so rather than inventing a rule to justify a preference.

Flagging a preference as a violation is the fastest way to lose the reviewer's trust in the whole review.

## Choosing a presentation

The most common design question, and Apple defines these by *purpose* — match the purpose, not the visual.

| Use | When | Source |
|---|---|---|
| **Alert** | Critical information needed right away; an uncommon, destructive, unrecoverable action | `pages/alerts.md` |
| **Action sheet** | Choices related to an action *the person just initiated* — "not an alert", explicitly | `pages/action-sheets.md` |
| **Sheet** | A scoped task closely tied to the current context | `pages/sheets.md` |
| **Popover** | A small amount of information or functionality, transient, anchored to a control | `pages/popovers.md` |
| **Full-screen modal** | In-depth content or a complex task | `pages/modality.md` |

Rules that resolve most real cases:
- **Don't alert for common, undoable destructive actions.** Deleting an email needs no confirmation. Alert when the action is uncommon *and* unrecoverable.
- **Offering choices after an intentional action → action sheet, not alert.**
- **Warnings don't belong in popovers.**
- **Only one sheet at a time** from the main interface.

## Choosing navigation

- **iPad: prefer a tab bar.** If the app has more sections than fit, use the tab bar that converts to a sidebar (`sidebarAdaptable`) rather than choosing one outright. Sidebar-only means `NavigationSplitView`, not a tab view.
- **Tab bars are for navigation, not actions.** Controls acting on the current view belong in a toolbar.
- **Keep the tab bar visible** as people navigate; a modal covering it is the exception.
- **Five or fewer tabs** when tabs are customizable, to stay consistent across size classes.

Details and platform variations: `grep -A1 -i "tab bar\|sidebar" references/rules.md`.

## Finding a component, or its API

`components.md` is a one-line purpose statement for every page, sorted alphabetically — scan it when you know roughly what you need but not the exact HIG term for it, or to confirm two components aren't the same thing before recommending one.

`api-map.md` goes the other direction: HIG concept → real API. It's organized both by component (`grep -A4 "^\*\*Sheets\*\*" api-map.md`) and by framework (`grep -A10 "^### HealthKit" api-map.md`), and covers more than the obvious three — 30+ frameworks including HealthKit, PassKit, StoreKit, WidgetKit, ClockKit. When implementing, not just designing, this is the difference between "use a sheet" and "use `sheet(item:onDismiss:content:)` in SwiftUI, or `UISheetPresentationController` in UIKit."

## Seeing what a component actually looks like

Everything else here is text. `assets-index.md` indexes 947 screenshots from Apple's iOS 27 UI kit under `assets/ui-kit/<Component>/`, covering the state matrix rather than one shot per component — light and dark, idle and pressed, on and off, enabled and disabled, plus accessibility-label variants. Detected states are tagged in the index (`[Dark, Idle, On, Enabled]`), so you can find one specific state without opening files at random.

**Read the image** with the Read tool rather than guessing from the filename — the point is seeing the actual rendering.

Reach for this when the question is visual rather than propositional:
- *"Does my custom control look right?"* — compare against the real thing, including the states people forget (disabled, pressed).
- *"What should the pressed state look like?"* — the rules rarely describe appearance in enough detail to reproduce it.
- *"Why does this feel off?"* when the specs all check out — the answer is often visual: wrong material, wrong contrast between states, missing state entirely.

Three folders use the Figma export's names rather than HIG terms, so the index maps them explicitly with a note: **System** is iPad Lock Screen widgets (→ `widgets.md`), **Face ID** is biometric authenticating/success states (→ `privacy.md`, where the HIG files biometrics), and **Empty States** is the no-content screen (→ `writing.md`, under *"Provide clear next steps on any blank screens"*).

That last one is worth internalizing as a search habit: guidance is often filed by *concern* rather than by component. Empty-state rules live under Writing, not under a component page — so when a component search comes up dry, check `concepts.md` before concluding the HIG is silent on it.

## When the topic isn't a component

`concepts.md` exists because the HIG is organized by component, and a lot of real design concerns aren't components. There's no `errors.md`, no `contrast.md`, no `empty-states.md` — but there are 16 error rules across 14 pages, and 11 rules on destructive actions across 8. Searching the page list for those finds nothing and invites the wrong conclusion.

Each entry gives the rule count, the pages holding them, and either a home page or an explicit **"no page of its own"** flag. Twelve of the thirty concepts are homeless, including error handling, contrast, permissions, safe areas, and Dynamic Type.

So: **"the HIG doesn't cover X" needs a `concepts.md` check first.** It's a claim that's easy to make and often wrong — the guidance usually exists, filed somewhere the page list doesn't suggest.

## Looking up a spec

`specs.md` is grouped by topic with the source table intact. The values people ask for most:

- **Hit region:** 44×44 pt minimum (60×60 in visionOS)
- **Text:** 17 pt default / 11 pt minimum on iOS and iPadOS — differs per platform, see the table
- **Contrast:** 4.5:1 up to 17 pt; 3:1 at 18 pt or bold

Quote the number *and* its platform. Most of these tables have a different value per platform, and quoting one row as universal is the easiest way to be confidently wrong.

## Adapting across platforms

Read the platform's section in `platform-diffs.md`, then apply the general rules underneath it — the diffs are exceptions, not a complete spec. Answering only from the diffs produces a confident, incomplete answer.

Two things that catch people out:
- **Framework:** macOS means SwiftUI or AppKit (UIKit only via Catalyst); visionOS pairs SwiftUI with RealityKit; watchOS with WatchKit. Recommending a `UI…` class for a Mac app is an obvious tell.
- **Interaction model:** tvOS has no cursor — it's a focus model driven by a remote. visionOS is eyes plus hands. Layouts that assume touch or pointer don't transfer.

When a platform has no entry for a topic, the HIG states no exception and the general rule applies. Say that; it's a real answer.

## Accuracy

- **Quote, don't paraphrase from memory.** These files carry Apple's current wording and exact numbers; the value here is not restating what the model already half-remembers.
- **Cite the page** so the claim is checkable — `pages/buttons.md`.
- **Snapshot dated 2026-08-11.** If a question turns on something a recent OS release may have changed, answer from the corpus and say it's a point-in-time copy worth confirming at developer.apple.com.
- **Images are hotlinked** to Apple's CDN, not stored locally.
