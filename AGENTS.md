# Apple HIG reference — agent instructions

This repository carries Apple's Human Interface Guidelines restructured for
working use: every rule as a checklist, every spec, the API for each piece of
guidance, and real screenshots of every component state.

`AGENTS.md` is the cross-tool convention, so tools that don't read Claude
Code's `.claude/skills/` format still get the same routing. The content lives
in one place either way — this file points at it rather than duplicating it.

## When to use it

Any UI work for an Apple platform — iOS, iPadOS, macOS, tvOS, visionOS,
watchOS — including SwiftUI, UIKit, and AppKit code review. Use it whenever
an answer depends on what Apple actually specifies rather than general UI
instinct, even when nobody mentions the HIG: *is this button too small*,
*sheet or popover*, *why does this feel wrong on Mac*, *make this work on
iPad*, *is this accessible*.

The value is that model recollection of the HIG goes stale — Apple revises
sizes, contrast minimums, and component behavior every OS cycle. Quote these
files instead of recalling.

## Where things are

All paths under `.claude/skills/apple-hig/`:

| File | Answers |
|---|---|
| `references/patterns.md` | **"What do I write?"** — correct-by-default SwiftUI scaffolding |
| `references/rules.md` | 2,280 guidelines as one-line imperatives, by topic |
| `references/specs.md` | Every number — sizes, ratios, limits — with source tables |
| `references/concepts.md` | Where guidance lives for concerns that aren't components |
| `references/api-map.md` | HIG concept → exact API, 30+ frameworks |
| `references/components.md` | One-line purpose for all 169 components |
| `references/platform-diffs.md` | What changes per platform |
| `references/assets-index.md` | 947 screenshots, every interaction state |
| `references/pages/` | Full prose when a rule's reasoning matters |

## How to use it

**Grep first.** `grep -A1 -i "sheet" references/rules.md` beats reading a
page. Open full pages for the *why*, not the *what*.

**Writing new UI** → start from `patterns.md`, which already encodes the
constraints.

**Reviewing existing UI** → scope to the components actually present, pull
their rules, then sort findings into:
- **Violations** — a stated rule with a number. Objective.
- **Guidance** — prefer/avoid without a threshold. Deviable with reason.
- **Judgment** — the HIG is silent. Say so instead of inventing a rule.

Presenting a preference as a violation is the fastest way to lose trust in
the whole review.

**Before claiming Apple doesn't cover something**, check `concepts.md`. The
HIG files a lot by concern rather than component — empty-state guidance is
under *Writing*, and 12 of 30 tracked concepts have no page of their own.

## Accuracy

- Quote and cite (`pages/buttons.md`) so claims are checkable.
- Quote the number **and** its platform — most spec tables differ per
  platform, and quoting one row as universal is the easy way to be wrong.
- Snapshot dated 2026-08-11. If a question turns on something a recent OS
  release may have changed, answer from the corpus and say it's point-in-time.
- `patterns.md` is synthesis; anything marked **[not in corpus]** is not
  Apple's stated word.
