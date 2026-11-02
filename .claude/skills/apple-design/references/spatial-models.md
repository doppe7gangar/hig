# Spatial models

Choose a spatial model from the user's primary task, not from aesthetic preference.

The model is the arrangement of work. Styling comes later.

## Decision order

Ask these questions in order:

1. What object or information is the user primarily working with?
2. Do they repeatedly switch between peer destinations, or stay inside one work context?
3. Is selection from a collection central to the task?
4. Is the primary screen answering a question or hosting work?
5. Does content itself need to dominate the interface?
6. Which controls need to remain persistent, and which can be contextual?

Do not choose a model because it “looks Apple.”

## `workspace`

Use when the product has persistent destinations and sustained desktop-style work.

Good fits:

- project management tools
- admin tools
- developer tools
- team workspaces
- multi-section productivity apps

Structure:

`persistent navigation → work region → contextual actions`

The work region should dominate. The sidebar is navigation, not decoration.

Avoid when:

- there is only one meaningful destination
- the product is mostly reading
- the user primarily selects an item and studies its detail
- the sidebar exists only because SaaS templates usually have one

## `list-detail`

Use when the core loop is choosing from a collection and acting on one item.

Good fits:

- mail
- files
- customers
- tickets
- recipes
- notes
- records

Structure:

`collection → selection → detail`

The list carries recognition; the detail carries understanding and actions.

Avoid loading the row with everything known about the item. If the row contains five facts, the detail view has leaked into the list.

On narrow screens the list and detail usually become sequential rather than compressed side by side.

## `dashboard`

Use when the primary job is understanding status, performance, health, or change.

Good fits:

- analytics
- operations health
- finance summaries
- activity summaries
- monitoring

Structure:

`answer → context/comparison → evidence → deeper detail`

A dashboard is not a grid of equal cards.

One result, condition, or metric should usually lead. Supporting metrics explain that answer instead of competing with it.

Do not choose dashboard merely because the product contains numbers.

## `document`

Use when the content or artifact itself is the work surface.

Good fits:

- writing
- documents
- editors
- reports
- notes
- long-form review
- lightweight creation tools

Structure:

`content/work surface → contextual tools`

The document is already a surface. Do not wrap every section inside another card.

Persistent chrome should be quiet. Controls should appear where they are useful without becoming the visual subject.

For richer creation tools this can evolve into a canvas or inspector model.

## `editorial`

Used by marketing and narrative pages.

Structure:

`claim → proof → demonstration → differentiation → action`

Each section should make one argument and earn its scroll distance.

Avoid the default generative pattern:

`hero → three feature cards → three more feature cards → testimonials → CTA`

unless the actual story requires it.

Typography, product media, pacing, and sequence create hierarchy here more than native application components do.

## iOS `stack`

Use when navigation is hierarchical or task-driven and there is no strong reason for persistent peer destinations.

This should be the conservative default for an iOS scaffold because a destination count alone does not justify a tab bar.

Structure:

`root → pushed detail/task → return`

Use sheets for temporary detours when HIG guidance supports them.

## iOS `tabs`

Use only when destinations are:

- genuinely peer-level
- important
- frequently switched
- useful to keep persistently reachable

A small number of destinations does not automatically mean tabs.

Before choosing tabs, verify the actual platform guidance in `apple-hig` rather than relying on this synthesis.

## Models not yet emitted by the scaffolder

The design director may identify a model that `new_project.py` does not generate yet. Do not force the product into an available scaffold.

Examples:

- inspector
- command surface
- feed
- immersive media/map surface
- dense table
- multi-pane editor
- macOS-specific toolbar/sidebar/inspector compositions

In those cases use the closest scaffold only for infrastructure, then replace its composition immediately. Record the real model in `DESIGN.md`.

## Model sanity check

Before implementation, complete this sentence:

> This model is appropriate because the user's main task is ________, and this arrangement keeps ________ primary while ________ remains secondary/contextual.

If the sentence is difficult to complete, the model was probably chosen by visual habit rather than product logic.