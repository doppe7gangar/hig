# Design divergence

Use this after information hierarchy is established and before committing to a spatial composition.

The purpose is not to generate cosmetic variants. It is to prevent first-idea anchoring by comparing genuinely different ways to organize the work.

## Required divergence

For a whole-product or major-screen design, consider **three candidate directions** when the brief permits meaningful alternatives. Use two only when the task strongly constrains the architecture. Skip divergence for trivial component-only work.

Each candidate must differ in at least two structural dimensions:

- dominant region
- navigation model
- persistent vs contextual chrome
- information density
- sequence vs simultaneity
- collection/detail relationship
- content width or pane structure
- where the primary action lives

Changing radius, color, typography, card style, or sidebar width does **not** create a new direction.

## Candidate format

For each direction write:

### Direction: <short name>

- **Model:** workspace / list-detail / dashboard / document / editorial / stack / tabs / other
- **Design idea:** one sentence describing what owns the screen
- **Primary region:** what receives first attention
- **Secondary/contextual regions:** what recedes and when it appears
- **Persistent chrome:** only what remains visible during the core task
- **Transformation on narrow screens:** architectural change, not merely smaller dimensions
- **Strength:** what user behavior this arrangement serves best
- **Risk:** the most likely way this direction could fail

A valid design idea sounds like “the selected customer owns the work surface; the account list is navigation.”

An invalid one sounds like “clean layout with a modern sidebar.”

## Score the candidates

Score each direction from 1–5 on these criteria:

1. **Primary-task fit** — does the arrangement make the recurring job easier?
2. **Hierarchy clarity** — is first/second/third attention obvious?
3. **Information relationship** — does spatial placement explain how information relates?
4. **Platform fit** — does it respect the input, density, navigation, and window model of the target platform?
5. **Adaptivity** — can it transform coherently across required widths or devices?
6. **Restraint** — does it avoid unnecessary persistent chrome and containers?
7. **Distinctiveness through product logic** — does the composition arise from this product rather than a generic SaaS habit?

Do not total the scores mechanically and obey the largest number. Scores expose trade-offs; the written rationale chooses the direction.

## Rejection requirement

Before committing, explicitly reject the alternatives.

For each rejected direction state one product-specific reason. Examples:

- “Rejected dashboard: the user spends most of the session editing one record, not monitoring status.”
- “Rejected persistent sidebar: there are only two infrequently switched destinations, so it would consume space without supporting the core loop.”
- “Rejected list-detail on phone: simultaneous panes collapse the hierarchy; use sequential navigation instead.”

Do not reject a direction because it is “less Apple-like,” “less modern,” or “less clean.”

## Reference timing

Divergence and reference selection inform each other:

1. establish hierarchy
2. draft structural candidates
3. shortlist relevant HIG/UI-kit references for the candidates
4. inspect references
5. revise candidate assumptions if the evidence changes them
6. choose and record the winning direction

References are evidence, not votes. Do not choose a spatial model merely because Apple has a screenshot that resembles it.

## When one direction clearly dominates

Some briefs genuinely have an obvious architecture. Do not invent bad alternatives to satisfy a ritual.

If only one direction is credible, record:

- the obvious direction
- the constraint that eliminates alternatives
- one counterfactual you considered and why it fails

This preserves deliberate reasoning without wasting effort.

## Final commitment sentence

Complete this before implementation:

> We chose ________ because the user's recurring task is ________. It keeps ________ primary, makes ________ available without competing for attention, and transforms to ________ when space/input changes.

If this sentence cannot be completed concretely, the composition is not ready.