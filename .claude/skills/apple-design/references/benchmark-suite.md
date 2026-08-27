# Design quality benchmark suite

Use these briefs to detect whether `apple-design` generalizes or collapses into one repeated composition, content treatment, or interaction contract.

The benchmark is architecture-, content-, and interaction-focused. It does not prescribe screenshots or pretend to score beauty.

## Briefs

| ID | Product | Target | Architectural/content/interaction pressure |
|---|---|---|---|
| analytics | support analytics | desktop web | one answer first; meaningful comparisons; async filters/retry without losing context |
| mail | mail client | macOS | dense list-detail, realistic metadata, selection persistence, compose/save/send recovery, keyboard behavior |
| photo | photo editor | macOS/iPadOS | canvas dominance, inspector, autosave/export semantics, undo, interruption safety |
| finance | personal finance overview | iOS | summary hierarchy, units/baselines, reversible categorization/edit flows |
| plants | plant watering tracker | iOS | realistic schedules/status variation, care completion/undo, offline-safe changes |
| notes | research notes | iPadOS/macOS | collection-detail/document relationship, long text stress, autosave/conflict/resume |
| devtool | API/debugging tool | desktop web/macOS | exact values/tables, request cancel/retry, environments, command/keyboard behavior |
| settings | configuration utility | macOS | grouped concerns, native controls, immediate-vs-explicit commit clarity, reversal |
| media | music/video experience | iOS/iPadOS | immersive content, queue/playback continuity, interruption/resume behavior |
| commerce | product browsing/detail | responsive web | realistic copy/media, cart mutation/undo/error, responsive transformation |
| landing | B2B product launch | marketing web | editorial narrative, concrete proof, form submit/failure behavior, no feature-card default |
| operations | incident monitoring | web | exact evidence, selection while updates arrive, acknowledge/escalate recovery semantics |
| messaging | team messaging | desktop web | varied messages, draft/send retry, channel switching without draft loss, keyboard paths |
| calendar | scheduling | iPadOS/web | overlaps/durations, create/edit commit, drag alternative, conflict handling |
| files | file manager | macOS | filenames/metadata extremes, multi-selection, move/copy/undo, context menus, keyboard shortcuts |

## Per-run gates

Every whole-product benchmark must pass:

```bash
python3 check_divergence.py ./design
python3 check_content.py ./design
python3 check_interaction.py ./design
python3 check_direction.py ./design
python3 check_design.py ./design --no-browser
```

`check_divergence.py` verifies 2–3 structural candidates, explicit differences, common comparison criteria, trade-off interpretation, rejected alternatives, and commitment evidence.

`check_content.py` verifies that important content is tied to a user question/decision, representation choices have rationale and failure risks, realistic stress cases are considered, and loading/empty/error states preserve the design idea.

`check_interaction.py` verifies that the primary task has an entry-to-exit flow, explicit commit semantics, reversal/recovery, interruption/resumption behavior, realistic stress cases, and an alternate input path where relevant.

The gates remain separate because strong divergence does not prove content integrity, content integrity does not prove dependable interaction, interaction does not prove accessibility/adaptivity evidence, and none prove the implementation is wired correctly.

## Required review dimensions

For each run record:

- target platform and HIG routing performed
- 2–3 structural candidates (or a documented hard constraint)
- explicit structural differences between candidates
- seven-criterion direction comparison plus written trade-off interpretation
- rejected alternatives with product consequences
- chosen spatial model
- content model: question/task → decision → content shape → context
- representation decisions and why they fit
- chart question/unit/comparison where charts exist
- at least three realistic content stress cases
- loading/empty/error state continuity
- primary interaction flow: entry → act → commit → exit/continue
- commit model and exact commit point
- undo/cancel/reversal policy
- interruption/resumption behavior
- keyboard/alternate input and focus restoration
- at least three interaction stress cases
- design invariants
- persistent region count
- major container/card count
- primary-action count
- navigation strategy
- compact/wide transformation
- system components preferred or custom components justified
- component interaction states covered
- accessibility considerations
- final design idea

## Cross-run structural signature

The executable evaluator derives a deliberately coarse signature from generated HTML. It includes inferred model, side/navigation regions, tables, forms, split/pane/inspector signals, and card/container count.

The signature is not a quality score. It asks whether unrelated products repeatedly receive effectively the same structure.

## Content regression signals

Flag when:

- content/representation evidence is thin
- charts appear without an analytical question, unit, or comparison
- operational exact-value tasks are replaced by decorative cards/charts
- realistic extremes are not considered
- loading/empty/error states abandon the populated hierarchy
- generic placeholder copy survives into final review
- dashboards show numbers without baseline/target/recency where interpretation needs them
- status is communicated only by color

## Interaction regression signals

Flag when:

- the primary flow is documented only as screens rather than actions and system responses
- no exact commit point is defined
- Save and immediate-update semantics conflict
- optimistic changes have no rollback story
- destructive changes lack appropriate undo/recovery reasoning
- switching selection/navigation can silently lose in-progress work
- async completion can steal focus or mutate the wrong object
- desktop/macOS flows omit keyboard/command behavior
- drag/drop is the only path for an important task
- modal dismissal semantics are unclear
- retries reset useful context unnecessarily
- every product uses the same submit/spinner/toast interaction formula despite different task contracts

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

These are regression alarms, not universal laws. Repeated models, representations, or interaction contracts can be correct when products genuinely share the same task structure.

## Hard failures vs warnings

A run is a hard failure when its required divergence, content, interaction, direction, or mechanical gate fails.

Cross-run sameness remains a warning because repetition requires contextual judgment. The evaluator must not redesign products merely to maximize diversity.

**Diversity is evidence of generalization, not a goal in itself.**

## Evaluation principle

The benchmark asks whether **structure, content representation, and task behavior vary appropriately with the product**.

Passing mechanical checks is necessary but insufficient. Passing divergence, content, and interaction gates is also necessary but insufficient. A suite where every output passes locally yet all outputs converge on the same structural/content/interaction formula is still evidence of a weak design skill.

Conversely, forcing different layouts, charts, or interaction patterns for novelty is also weak. The target is appropriate variation driven by product logic, data/content shape, platform conventions, and task consequences.