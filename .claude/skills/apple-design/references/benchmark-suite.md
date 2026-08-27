# Design quality benchmark suite

Use these briefs to detect whether `apple-design` generalizes or collapses into one repeated composition.

The benchmark is intentionally architecture-focused. It does not prescribe screenshots or pretend to score beauty.

## Briefs

| ID | Product | Target | Architectural pressure |
|---|---|---|---|
| analytics | support analytics | desktop web | one answer first; evidence second; avoid equal metric cards |
| mail | mail client | macOS | dense list-detail, toolbar/menu/keyboard behavior |
| photo | photo editor | macOS/iPadOS | content/canvas dominance, contextual inspector |
| finance | personal finance overview | iOS | summary hierarchy without dashboard-card wallpaper |
| plants | plant watering tracker | iOS | task hierarchy; tabs only if genuinely peer-level |
| notes | research notes | iPadOS/macOS | collection-detail/document relationship |
| devtool | API/debugging tool | desktop web/macOS | dense workspace, command/keyboard affordances |
| settings | configuration utility | macOS | grouped concerns, native controls, desktop density |
| media | music/video experience | iOS/iPadOS | immersive content, chrome recedes |
| commerce | product browsing/detail | responsive web | collection/detail and responsive transformation |
| landing | B2B product launch | marketing web | editorial narrative, no feature-card default |
| operations | incident monitoring | web | urgency/status hierarchy, tables/evidence, no decorative dashboard |
| messaging | team messaging | desktop web | channels/list/conversation, input remains primary in context |
| calendar | scheduling | iPadOS/web | temporal/spatial relationship, adaptive views |
| files | file manager | macOS | sidebar/list/detail, keyboard/context menus, multi-selection |

## Per-run gates

Every whole-product benchmark must pass:

```bash
python3 check_divergence.py ./design
python3 check_direction.py ./design
python3 check_design.py ./design --no-browser
```

`check_divergence.py` exists separately because a complete-looking `DESIGN.md` can still hide first-idea anchoring. It verifies 2–3 structural candidates, explicit differences, common comparison criteria, trade-off interpretation, rejected alternatives, and commitment evidence.

The direction and mechanical gates remain separate because good divergence does not prove accessibility/adaptivity evidence, and none of those prove the implementation is wired correctly.

## Required review dimensions

For each run record:

- target platform and HIG routing performed
- 2–3 structural candidates (or a documented hard constraint that legitimately narrows the set)
- explicit structural differences between candidates
- seven-criterion direction comparison plus written trade-off interpretation
- rejected alternatives with product consequences
- chosen spatial model (including custom model)
- design invariants
- persistent region count
- major container/card count
- primary-action count
- navigation strategy
- compact/wide transformation
- system components preferred or custom components justified
- interaction states covered
- accessibility considerations
- final design idea

## Cross-run structural signature

The executable evaluator derives a deliberately coarse signature from generated HTML. It includes:

- inferred model (`workspace`, `list-detail`, `dashboard`, `document`, `editorial`, iOS stack/tabs, or custom/unknown)
- presence/buckets for side regions
- navigation regions
- tables
- forms
- split/pane/inspector signals
- card/container count

The signature is not a quality score. It exists to answer a different question:

> Are unrelated products repeatedly being solved with effectively the same structure?

Small content differences should not defeat this check, which is why noisy counts are bucketed rather than compared exactly.

## Regression signals

Across the suite, warn when:

- one inferred spatial model appears in >60% of unrelated briefs
- a near-identical structural signature appears in a large share of unrelated products
- `sidebar + card grid` appears across unrelated products
- many products become card-heavy even when their tasks differ
- whole-product runs record fewer than two candidate directions without a hard constraint
- native iOS and macOS outputs use the same navigation model without product reasons
- macOS outputs emit mobile-style tab/stack navigation
- marketing output regresses to feature-card wallpaper
- responsive plans only say “stack” or “shrink” without architectural transformation
- custom controls are proposed without system-component lookup
- `DESIGN.md` lacks rejected alternatives or invariants
- chosen-direction wording repeats suspiciously across unrelated products

These are regression alarms, not universal design laws. A repeated model can be correct when the products genuinely share a task structure. The warning exists so a reviewer asks why rather than assuming repetition is automatically wrong.

## Hard failures vs warnings

A run is a hard failure when its required divergence, direction, or mechanical gate fails.

Cross-run sameness remains a warning because architectural repetition requires contextual judgment. The evaluator must not redesign products merely to maximize diversity.

This distinction matters: **diversity is evidence of generalization, not a goal in itself.**

## Evaluation principle

The benchmark asks whether the **decision process and resulting structure vary appropriately with the product**.

Passing mechanical checks is necessary but insufficient. Passing divergence gates is also necessary but insufficient. A suite where every output passes locally yet all outputs converge on the same structural signature is still evidence of a weak design skill.

Conversely, a suite that forces different layouts for the sake of novelty is also weak. The target is appropriate variation driven by product logic.