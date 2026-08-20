---
name: apple-hig
description: Apple Human Interface Guidelines as a working reference — review UI code or designs against Apple's actual rules, pick the right control or presentation (sheet vs popover vs alert vs full-screen, tab bar vs sidebar vs split view), look up exact specs (tap targets, type sizes, contrast ratios, icon dimensions, safe areas), find the exact SwiftUI/UIKit/AppKit/framework API for a piece of guidance, see the real system appearance of a component (light/dark, pressed/idle, on/off, enabled/disabled) from Apple's actual iOS 27 UI kit, and adapt a design across iOS, iPadOS, macOS, tvOS, visionOS, and watchOS. Contains all 2,326 HIG rules as a greppable checklist, every spec table, a component-purpose index, an API map covering 32+ Apple frameworks, 947 real component screenshots across every interaction state, and the full 178-page corpus. Use whenever building, reviewing, critiquing, or fixing UI for an Apple platform — including SwiftUI, UIKit, and AppKit code review — and whenever a question turns on what Apple actually specifies or actually looks like, rather than general UI instinct. Trigger on Apple platform UI work even when the HIG is never mentioned: "is this button too small", "should this be a sheet or a popover", "why does my Mac app feel wrong", "make this work on iPad", "is this accessible", "what SwiftUI view do I use for this", "what does a disabled toggle look like", app icons, Dark Mode, Dynamic Type, VoiceOver, SF Symbols, Liquid Glass.
---

# Apple Human Interface Guidelines

Apple's design guidance, restructured for doing work rather than browsing. Eight references, each for a different question:

| File | Use it for |
|---|---|
| `references/patterns.md` | **What to actually write** — correct-by-default SwiftUI scaffolding with the right API and numbers already in place. |
| `references/rules.md` | **2,326 rules as one-line imperatives**, by topic. The review checklist. |
| `references/specs.md` | **Every number** — sizes, ratios, limits — with its source table. |
| `references/platform-diffs.md` | **What changes per platform**, grouped by platform. |
| `references/api-map.md` | **HIG concept → exact API symbol** — SwiftUI, UIKit, AppKit, and 32+ other frameworks (HealthKit, PassKit, StoreKit...). |
| `references/components.md` | **One-line purpose for every page** — the fastest way to find the right component before reading anything else. |
| `references/concepts.md` | **Where guidance actually lives** for cross-cutting concerns (empty states, error handling, contrast, offline) that have no page of their own. |
| `references/assets-index.md` | **What components actually look like** — 947 screenshots from Apple's iOS 27 UI kit, every interaction state. |
| `references/pages/<slug>.md` | Full prose when a rule's *reasoning* matters. |

Grep first. `grep -A1 -i "sheet" references/rules.md` returns every sheet rule in seconds; reading `pages/sheets.md` to find the same thing costs far more context. Reach for the full page when you need the *why*, not the *what*.

## Writing new UI

Start from `references/patterns.md` rather than from scratch — it has correct-by-default scaffolding for the things people build most (text that scales, tappable targets, each presentation type, adaptive navigation, empty states), with the real API and real numbers already in place, each citing its source.

It also ends with a pre-ship checklist. The items on it are the violations that recur: fixed font sizes that break Dynamic Type, hit regions under 44 pt, destructive styling applied backwards, and states that only exist in the happy path.

`patterns.md` is synthesis assembled from the other references, not extracted from Apple's pages like they are. Anything it can't source is marked **[not in corpus]** — don't quote those as Apple's word.

## Reviewing UI

The failure mode here is dumping 40 observations of mixed importance. Scope it:

1. **Inventory what's actually there.** List the components and patterns in the code — a `TabView`, a `.sheet`, a destructive `Button`, a custom control replacing a system one. Review those, not the whole HIG.
2. **Pull their rules.** `grep -A1 -i "<component>" references/rules.md` for each. Check numbers against `specs.md`.
3. **Check the API against `api-map.md`.** A hand-rolled view where a system component already exists (a custom modal built from a `ZStack` instead of `.sheet`, a bespoke button instead of `UIButton`/`NSButton`) is itself worth flagging — Apple's guidance assumes the system component, and a reimplementation usually drifts from it silently.
4. **Check the target platforms** in `platform-diffs.md`. A layout that's right on iPhone can be wrong on Mac, and the general rule won't say so.
5. **For custom controls, compare against the real thing** in `assets-index.md`. A reimplemented toggle or button usually gets the default state right and the others wrong — check pressed and disabled specifically, since those are the ones people skip and the ones the written rules describe least.
6. **Sort findings by force**, and say which is which:
   - **Violations** — a stated rule with a number attached. *"4.5:1 contrast required below 17 pt; this pair is 4.05:1."* Objective, fix it. (Hit targets look like this but aren't — see *Looking up a spec*.)
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

`api-map.md` goes the other direction: HIG concept → real API. It's organized both by component (`grep -A4 "^\*\*Sheets\*\*" api-map.md`) and by framework (`grep -A10 "^### HealthKit" api-map.md`), and covers more than the obvious three — 32+ frameworks including HealthKit, PassKit, StoreKit, WidgetKit, ClockKit. When implementing, not just designing, this is the difference between "use a sheet" and "use `sheet(item:onDismiss:content:)` in SwiftUI, or `UISheetPresentationController` in UIKit."

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

- **Hit region:** 44×44 pt as the general rule (60×60 in visionOS) — but see below
- **Text:** 17 pt default / 11 pt minimum on iOS and iPadOS — differs per platform, see the table
- **Contrast:** 4.5:1 up to 17 pt; 3:1 at 18 pt or bold

Quote the number *and* its platform. Most of these tables have a different value per platform, and quoting one row as universal is the easiest way to be confidently wrong.

**Hit targets are stated twice, and the two don't say the same thing.** `pages/buttons.md`: *"As a general rule, a button needs a hit region of at least 44x44 pt — in visionOS, 60x60 pt — to ensure that people can select it easily […]"* The accessibility *Mobility* table in `specs.md` instead gives iOS/iPadOS a **44×44 default** and a **28×28 minimum**. So a 30×30 control is below the general rule and above the stated floor — whichever source you grep first decides the verdict, and reviews have gone both ways on the same button.

Both are real, so give both rather than picking the one you found first. 44×44 is the target; 28×28 is an accessibility floor, and Apple's framing around the table is *"Strive to meet the recommended minimum control size for each platform"* — clearing 28 is not the same as being fine. Where Apple explains which applies, it splits on how often the control is used: *"Make sure frequently used controls are a minimum size of 44x44 pt, and less important controls, such as menus, are a minimum size of 28x28 pt"* (`pages/game-controls.md` — a games context, the only place the split is stated outright).

So a frequently-used control at 30×30 is a real finding against the 44 pt general rule; a rarely-used one at 28×28 sits on the floor and is defensible, with spacing carrying more weight than size at that point (*"Consider spacing between controls as important as size"*). What's wrong is citing one number as though the other doesn't exist.

## Adapting across platforms

Read the platform's section in `platform-diffs.md`, then apply the general rules underneath it — the diffs are exceptions, not a complete spec. Answering only from the diffs produces a confident, incomplete answer.

Two things that catch people out:
- **Framework:** macOS means SwiftUI or AppKit (UIKit only via Catalyst); visionOS pairs SwiftUI with RealityKit; watchOS with WatchKit. Recommending a `UI…` class for a Mac app is an obvious tell.
- **Interaction model:** tvOS has no cursor — it's a focus model driven by a remote. visionOS is eyes plus hands. Layouts that assume touch or pointer don't transfer.

When a platform has no entry for a topic, the HIG states no exception and the general rule applies. Say that; it's a real answer.

## Accuracy

- **Quote, don't paraphrase from memory.** These files carry Apple's current wording and exact numbers; the value here is not restating what the model already half-remembers.
- **Quotation marks mean character-exact.** Copy the sentence from the file into the answer; don't retype it from what you just read. This is the failure that's hardest to catch by eye, because a smoothed-over quote reads *more* like Apple than the original. Measured on real answers, roughly one quote in twelve had been reworded — including `pages/toolbars.md`'s warning that without the standard highlight effect "people might think they're **broken**," quoted back as "not interactive." Different claim, same confident voice.
- **Shorten honestly.** Trailing `…` when you stop early, `[…]` when you cut from the middle. Ending a quote with a period Apple didn't write silently moves where the rule ends — Apple's "essential commands *that people use frequently*" becomes a blanket "essential commands." Never merge two rules into one set of quotation marks: square buttons, image buttons, and help buttons each have their own toolbar rule, and fusing them invents a sentence Apple never wrote.
- **Paraphrase in your own voice instead.** Outside quotation marks, summarizing is fine and often better. The rule is only that quoted text is Apple's, verbatim.
- **Cite the page** so the claim is checkable — `pages/buttons.md`.
- **Check the quotes when it matters.** `python3 verify_quotes.py -` reads a draft on stdin and grades every quoted span against the corpus: VERBATIM, ELIDED (honest `...`), TRUNCATED (ends early), ALTERED (reworded or two rules fused). Worth running before a review someone will act on, or any answer built mostly of quotations.
- **Snapshot dated 2026-08-11.** If a question turns on something a recent OS release may have changed, answer from the corpus and say it's a point-in-time copy worth confirming at developer.apple.com.
- **Images are hotlinked** to Apple's CDN, not stored locally.
