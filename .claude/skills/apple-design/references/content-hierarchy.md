# Content hierarchy and representation

Use this after information hierarchy is known and before visual polish.

A strong layout can still feel fake when the content inside it is generic, unrealistic, or represented in the wrong form. This reference treats content as part of the design system.

## Start with decisions, not widgets

For every important content block, complete:

- **Question/task:** what does the user need to know or do?
- **Decision enabled:** what can they decide after seeing this?
- **Data/content shape:** single value, ordered list, time series, distribution, relationship, status, narrative, editable object, comparison, or mixed.
- **Required context:** baseline, target, previous period, units, owner, timestamp, confidence, freshness, source, or none.
- **Representation:** prose, number, row/list, table, chart, timeline, image/media, form/control, canvas, map, or custom.
- **Why this representation:** one concrete sentence.
- **Failure mode:** how this representation could mislead, overload, or hide important context.

Do not choose representation by aesthetic preference.

## Representation rules of thumb

### Number / metric

Use when one current value genuinely answers the primary question.

A number without context is rarely enough. Add the comparison that changes interpretation: target, prior period, range, status, or recency.

Bad: `68%`

Better: `68% · best week since June · +9 pts vs last week`

### Table

Use when people need exact values, scanning across attributes, sorting, comparison across many records, or repeated operational work.

Do not replace a table with cards merely to look more visual. Do not replace exact operational values with charts when users must act on individual rows.

### List

Use for recognition and selection when one or two distinguishing facts per item are enough. If each item needs many comparable fields, consider a table. If the user must deeply understand one selected item, pair the collection with detail.

### Chart

Use when shape, trend, distribution, correlation, or relative comparison matters more than exact lookup.

Every chart must state its analytical question. Examples:

- line: how did this change over time?
- bar: how do discrete categories compare?
- stacked bar/area: how does composition contribute to a total, and is that actually the question?
- scatter: are two numeric variables related?
- histogram: how is a numeric variable distributed?

Avoid decorative charts that repeat a number already obvious in text.

Avoid pie/donut charts when precise comparison matters or there are many categories. Do not use gauges merely to make a dashboard feel technical.

### Timeline

Use when sequence and temporal causality matter: incidents, activity, history, workflow progress. A timeline should expose meaningful events, not every log line.

### Prose / editorial copy

Use when explanation, persuasion, instruction, or interpretation is the job. Do not turn explanatory text into feature cards by default.

### Image/media

Use when the visual object is itself content: photography, products, artwork, maps, video, design assets. Media can own the hierarchy; chrome should recede.

### Form/control

Use when the user is changing system state. Labels, helper text, validation, defaults, and grouping are content decisions, not implementation details.

## Realistic content requirement

Before final review, replace generic scaffold content with content that has realistic:

- names and labels
- units
- value ranges
- text lengths
- timestamps/dates when relevant
- status variation
- exceptional cases
- enough rows/items to expose density
- long and short labels where the real product will have them

The goal is not fake realism for decoration. It is to expose layout assumptions that placeholders hide.

Avoid obvious lorem ipsum, `Item 1`, repeated identical values, perfectly uniform names, and every status being healthy.

## Content stress cases

Test at least the applicable cases:

- longest plausible title/label
- shortest plausible title/label
- large number / small number / zero
- negative or worsening change
- missing/unknown value
- stale value
- unusually many rows/items
- only one row/item
- long user-generated text
- localization expansion where relevant
- destructive/urgent status

If the design only works with ideal content, it is not finished.

## State continuity

Loading, empty, error, offline, and not-enough-data states must preserve the same **design idea** as the populated state.

Examples:

- If the populated dashboard says “today's operational status is the answer,” loading should skeleton that hierarchy rather than replace it with a centered spinner.
- If the populated list-detail design makes the selected object primary, an error loading detail should stay in the detail region rather than replace the entire product shell.
- If media owns the screen, loading should reserve the media's space so chrome does not suddenly become dominant.

For each major state record:

- what remains invariant
- what disappears because data is unavailable
- what replaces it
- what action/recovery becomes primary

## Copy hierarchy

Copy is part of visual hierarchy.

Prefer labels that identify meaning over implementation. Prefer action labels that say what happens. Secondary explanation should answer a real ambiguity, not fill empty space.

Audit:

- repeated headings that add no information
- vague labels such as “Overview”, “Details”, “Information” where a specific label is possible
- empty-state copy that ignores why the screen is empty
- raw system errors
- helper text explaining obvious controls
- multiple paragraphs saying the same thing
- status communicated only by color

## Chart and data integrity

For every chart or computed metric, document:

- measure definition
- unit
- time/window or population
- comparison/baseline
- whether higher/lower is good, when applicable
- missing-data behavior
- source/freshness if operationally important

Do not imply precision the underlying data does not support.

## Final content question

Ask:

> If all styling were removed, would the content structure still help the user make the right decision or complete the right task?

If not, visual polish is hiding a content-design problem.