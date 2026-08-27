# Design quality benchmark suite

Use these briefs to detect whether `apple-design` generalizes or collapses into one repeated composition or one repeated content treatment.

The benchmark is architecture- and content-structure-focused. It does not prescribe screenshots or pretend to score beauty.

## Briefs

| ID | Product | Target | Architectural/content pressure |
|---|---|---|---|
| analytics | support analytics | desktop web | one answer first; meaningful comparisons; charts only for analytical questions |
| mail | mail client | macOS | dense list-detail, realistic message metadata, toolbar/menu/keyboard behavior |
| photo | photo editor | macOS/iPadOS | content/canvas dominance, contextual inspector, media as primary content |
| finance | personal finance overview | iOS | summary hierarchy with units/baselines; no metric-card wallpaper |
| plants | plant watering tracker | iOS | task hierarchy; realistic schedules/status variation; tabs only if peer-level |
| notes | research notes | iPadOS/macOS | collection-detail/document relationship; long/short user text stress |
| devtool | API/debugging tool | desktop web/macOS | dense workspace, exact values/tables, command/keyboard affordances |
| settings | configuration utility | macOS | grouped concerns, explanatory copy, native controls, desktop density |
| media | music/video experience | iOS/iPadOS | immersive content, realistic metadata, chrome recedes |
| commerce | product browsing/detail | responsive web | collection/detail, realistic product copy/media, responsive transformation |
| landing | B2B product launch | marketing web | editorial narrative, concrete claims/proof, no feature-card default |
| operations | incident monitoring | web | urgency/status hierarchy, exact tables/evidence, no decorative dashboard |
| messaging | team messaging | desktop web | channels/list/conversation, varied message lengths, compose remains primary |
| calendar | scheduling | iPadOS/web | temporal/spatial relationship, realistic overlaps/durations, adaptive views |
| files | file manager | macOS | sidebar/list/detail, filenames/metadata extremes, multi-selection/context menus |

## Per-run gates

Every whole-product benchmark must pass:

```bash
python3 check_divergence.py ./design
python3 check_content.py ./design
python3 check_direction.py ./design
python3 check_design.py ./design --no-browser
```

`check_divergence.py` verifies 2–3 structural candidates, explicit differences, common comparison criteria, trade-off interpretation, rejected alternatives, and commitment evidence.

`check_content.py` verifies that important content is tied to a user question/decision, representation choices have rationale and failure risks, realistic stress cases are considered, and loading/empty/error states preserve the design idea.

The gates remain separate because strong divergence does not prove content integrity, content integrity does not prove accessibility/adaptivity evidence, and none prove the implementation is wired correctly.

## Required review dimensions

For each run record:

- target platform and HIG routing performed
- 2–3 structural candidates (or a documented hard constraint that legitimately narrows the set)
- explicit structural differences between candidates
- seven-criterion direction comparison plus written trade-off interpretation
- rejected alternatives with product consequences
- chosen spatial model (including custom model)
- content model: question/task → decision → content shape → context
- representation decisions and why they fit
- chart question/unit/comparison where charts exist
- at least three realistic content stress cases
- loading/empty/error state continuity
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

The executable evaluator derives a deliberately coarse signature from generated HTML. It includes inferred model, side/navigation regions, tables, forms, split/pane/inspector signals, and card/container count.

The signature is not a quality score. It asks whether unrelated products repeatedly receive effectively the same structure.

## Content regression signals

Across individual runs or the suite, flag when:

- `DESIGN.md` contains a very thin content model or representation rationale
- charts appear without an analytical question, unit, or comparison
- operational exact-value tasks are replaced by decorative cards/charts
- realistic extremes are not considered
- loading/empty/error states abandon the populated screen's hierarchy
- generic placeholder copy survives into final review
- dashboards show numbers without baseline/target/recency where interpretation needs them
- status is communicated only by color
- unrelated products reuse the same content pattern despite different tasks

## Structural regression signals

Warn when:

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
- chosen-direction wording repeats suspiciously across unrelated products

These are regression alarms, not universal design laws. A repeated model or representation can be correct when products genuinely share the same task/data shape.

## Hard failures vs warnings

A run is a hard failure when its required divergence, content, direction, or mechanical gate fails.

Cross-run sameness remains a warning because repetition requires contextual judgment. The evaluator must not redesign products merely to maximize diversity.

**Diversity is evidence of generalization, not a goal in itself.**

## Evaluation principle

The benchmark asks whether both **structure and content representation vary appropriately with the product**.

Passing mechanical checks is necessary but insufficient. Passing divergence and content gates is also necessary but insufficient. A suite where every output passes locally yet all outputs converge on the same structural/content formula is still evidence of a weak design skill.

Conversely, a suite that forces different layouts or charts for novelty is also weak. The target is appropriate variation driven by product logic and data/content shape.