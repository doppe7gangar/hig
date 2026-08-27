# Design divergence

Use this after information hierarchy is established and before committing to a spatial composition.

The purpose is not to generate cosmetic variants. It is to prevent first-idea anchoring by comparing genuinely different ways to organize the work.

## Required divergence

For a whole-product or major-screen design, consider **three candidate directions** when the brief permits meaningful alternatives. Use two when platform/task constraints narrow the credible set. Skip divergence only for trivial component-only work.

Never invent a knowingly bad candidate just to make the count.

Each candidate must differ from the others in **at least two structural dimensions**:

- dominant region
- navigation model
- persistent vs contextual chrome
- information density
- sequence vs simultaneity
- collection/detail relationship
- content width or pane structure
- where the primary action lives
- selection/context persistence
- wide-to-compact transformation

Changing radius, color, typography, card style, icon treatment, or sidebar width does **not** create a new direction.

Record the differences explicitly in the candidate's `Structural differences` field. Do not make the checker infer them from vague prose.

## Candidate format

For each direction write:

### Direction: <short name>

- **Model:** workspace / list-detail / dashboard / document / editorial / stack / tabs / other
- **Design idea:** one sentence describing what owns the screen
- **Primary region:** what receives first attention
- **Secondary/contextual regions:** what recedes and when it appears
- **Persistent chrome:** only what remains visible during the core task
- **Compact transformation:** architectural change, not merely smaller dimensions
- **Strength:** what user behavior this arrangement serves best
- **Risk:** the most likely way this direction could fail
- **Structural differences:** at least two concrete differences from the other candidates

A valid design idea sounds like “the selected customer owns the work surface; the account list is navigation.”

An invalid one sounds like “clean layout with a modern sidebar.”

## Compare on the same seven criteria

Use a single comparison table and score every credible direction from 1–5 on:

1. **Primary-task fit** — does the arrangement make the recurring job easier?
2. **Hierarchy clarity** — is first/second/third attention obvious?
3. **Information relationship** — does spatial placement explain how information relates?
4. **Platform fit** — does it respect input, density, navigation, and window model?
5. **Adaptivity** — can it transform coherently across required widths/devices?
6. **Restraint** — does it avoid unnecessary persistent chrome and containers?
7. **Distinctiveness through product logic** — does the composition arise from this product rather than a generic SaaS habit?

The table exists to expose trade-offs, not to create a design algorithm. **Do not total the scores and obey the largest number.**

After the table, write a `Trade-off interpretation` paragraph explaining:

- which trade-off matters most for this product
- which candidate weakness is most costly
- whether a lower-scoring dimension is acceptable and why
- why the chosen direction wins despite any score it does not lead

## Rejection requirement

Before committing, explicitly reject every losing candidate.

For each rejected direction state a **product-specific reason and consequence**. Examples:

- “Rejected dashboard because the user spends most of the session editing one record; monitoring-first hierarchy would bury the actual work.”
- “Rejected persistent sidebar because the two destinations are infrequently switched; it would consume width without supporting the core loop.”
- “Rejected simultaneous panes on phone because preserving both compresses the selected content; compact mode becomes sequential navigation instead.”

Do not reject a direction because it is “less Apple-like,” “less modern,” or “less clean.” Those are aesthetic labels, not product consequences.

## Reference timing

Divergence and reference selection inform each other:

1. establish hierarchy
2. draft structural candidates
3. shortlist relevant HIG/UI-kit references for the candidates
4. inspect references
5. revise candidate assumptions if the evidence changes them
6. score and interpret trade-offs
7. reject losing directions
8. choose and record the winner

References are evidence, not votes. Do not choose a spatial model merely because Apple has a screenshot that resembles it.

## When one direction clearly dominates

Some briefs genuinely have an obvious architecture. Do not invent bad alternatives to satisfy a ritual.

If only one direction is credible, divergence is waived only when the design record states:

- the dominant direction
- the hard platform/task constraint eliminating alternatives
- one credible counterfactual considered
- the concrete reason that counterfactual fails

For ordinary whole-product work, two candidates remain the minimum.

## Divergence gate

Before committing to implementation, run:

```bash
python3 check_divergence.py ./design
```

The gate checks that:

- there are 2–3 candidate directions
- every candidate contains the required structural fields
- every candidate declares at least two structural differences
- candidates are not all the same named model without explanation
- all seven comparison criteria are scored 1–5
- the comparison includes written trade-off interpretation
- each losing candidate has a product-specific rejection
- the chosen direction explains task fit, primary hierarchy, and transformation

The checker validates evidence structure, not design taste. Passing it does not prove the winner is good; it proves the decision was actually made visible enough to review.

## Final commitment sentence

Complete this before implementation:

> We chose ________ because the user's recurring task is ________. It keeps ________ primary, makes ________ available without competing for attention, and transforms to ________ when space/input changes.

If this sentence cannot be completed concretely, the composition is not ready.