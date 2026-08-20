# Real-life test — results

Skill taken from a **fresh clone** of `origin/main` (9b146eb), installed into
a SwiftUI project, driven by prompts that never say Apple, HIG, design, or
guidelines.

| | Review run | iPad run |
|---|---|---|
| Prompt | "i'm about to ship this. can you look over the UI code and tell me what i should fix first?" | "does this work properly on iPad, or do i need to change anything?" |
| Skill triggered unprompted | yes | yes |
| References used | rules, specs, api-map, concepts | platform-diffs, rules, patterns, pages, specs |
| Apple quotes verbatim | 12/12 | 12/12 |

## Recall

Nine of the eleven seeded defects were found. Both apparent misses were
**errors in the ground truth**, not the skill's:

- **Accessibility labels on icon-only buttons.** The corpus rule is
  *"Provide alternative text labels for custom interface icons"* — the app
  uses `Image(systemName:)` throughout, and SwiftUI labels SF Symbols
  automatically. The rule doesn't apply. Staying silent was right.
- **Chart series distinguished by colour alone.** Each bar in `StatsView`
  has `Text(habit.name)` beside it, so colour isn't the sole channel.
  Also not a violation.

So: **9 of 9 sound seeded defects found, and the skill declined two
false positives I had scored as findings.**

## Precision

Zero false positives. Nothing from the "correct code" list was flagged —
the 44×44 toggle, the `.sheet`, the toolbar placements, the semantic text
styles all passed unmentioned.

The out-of-scope items were handled the way the skill asks for: the
`.constant()` binding bug was reported and explicitly labelled
*(correctness)*, kept apart from the HIG findings.

## Calibration

The review declined to call 30×30 toolbar buttons a violation, citing the
28×28 floor — correct. The iPad run called the same buttons a violation
citing `buttons.md`'s 44×44 general rule. **Both quoted Apple accurately
and reached opposite verdicts**, decided by which file got grepped first.
Fixed in 39e050c: SKILL.md now carries both numbers and how to choose.

## Findings beyond the seeded set (all verified real)

- Leading toolbar button collides with iPadOS window controls —
  `rules.md`: *"Make sure window controls don't overlap toolbar items."* `[iPadOS]`
- Delete alert's message understates what it does; `delete()` drops
  `completedCount` and `streak`, the message says "from today's list"
- Blank Today screen after `resetAll()` — cited `pages/writing.md`
- Chart bar width `completedCount * 8` is unbounded, runs off-screen
- `firstIndex(of:)` compares all fields on a mutated struct
- `completedCount` decrements on un-toggle, so totals can be driven down
- "Hide completed" toggle duplicated in Settings and the custom overlay
- Reminders and Awards tabs are empty stubs

## What this run fixed in the skill

1. `verify_quotes.py` reported a review's quotes of **its own app's
   strings** as altered Apple quotes — 4 false alarms. Now checked
   against the source tree and reported as SOURCE.
2. The quote-pairing ambiguity resurfaced; both pairings are now tried
   and the better-grounded one wins.
3. The checker didn't understand `[…]`, the elision mark SKILL.md itself
   asks for. iPad run went 9/12 → 12/12 once taught.
4. The 44 vs 28 contradiction above.
5. Dogfooding the checker on SKILL.md caught a quote I had closed with a
   period Apple doesn't have.

---

# Verification of the hit-target fix

Re-ran the same prompt against the same fixture with the corrected build.

**Before** — the two runs cited different sources and reached different
verdicts on the same buttons:

> *review run:* "the trash button is 28×28. That's exactly the iOS floor
> (`specs.md`: 44×44 default, 28×28 minimum), **so not strictly a
> violation**"

> *iPad run, under `## Violations`:* "**Toolbar buttons are 30×30 pt.**
> […] 'A button needs a hit region of at least 44x44 pt'" — and it lumped
> the 28×28 trash button in with them.

**After** — one run, both sources, and a verdict that separates the two
controls:

> "**Hit targets.** Two sources apply and they don't agree, so both:
> `pages/buttons.md` says […] while the accessibility table gives iOS a
> 44×44 default and 28×28 minimum, split by frequency […]
> (`pages/game-controls.md`).
> - Toolbar buttons at 30×30 — below the 44 target, above the floor.
> - Delete at 28×28 — sitting exactly on the accessibility floor,
>   immediately beside a 44×44 toggle. That adjacency is the concern."

Quotes: **19/19 sound, zero altered.**

The re-run also picked up two findings the earlier one missed —
accessibility labels on icon-only buttons, and empty states after
`resetAll()` — and kept the alert-role nuance (Apple's destructive style
is for actions people *didn't* deliberately choose).

## Both prompts, after the fix

The iPad prompt was re-run once quota allowed. It now reconciles the two
sources the same way, from the other direction -- it had been the run
that filed the buttons flatly under `## Violations`:

> "There is a lower accessibility floor of 28x28, but Apple splits it by
> frequency: 'Make sure frequently used controls are a minimum size of
> 44x44 pt, and less important controls, such as menus, are a minimum
> size of 28x28 pt' (`pages/game-controls.md`). A trash button on every
> row is frequently used, so 44 applies. The toolbar buttons at 30x30
> are below the general rule and above the floor -- defensible only if
> you consider them rarely used."

The two runs still weigh the trash button differently -- the review run
leads with its adjacency to a 44 pt toggle, the iPad run argues
frequency of use puts it at 44. That is a reasoned difference over the
same two facts, which is what was wanted; before the fix they disagreed
because each had seen only one of them.

Quotes across both runs: **31/31 sound, zero altered, zero truncated.**

`rules.md` was the only generated file that truncated; specs.md,
platform-diffs.md, api-map.md, components.md and concepts.md carry no
truncated bodies, so the fix covers the whole exposure.
