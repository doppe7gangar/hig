# Cross-screen product coherence

A product can contain individually strong screens and still feel incoherent. Review the system between screens, not only each screen in isolation.

## Coherence contract

Before final visual review, define a small product-level contract that all applicable screens must obey.

### Typography roles

Name semantic roles rather than page-specific sizes: product/page title, section heading, body, secondary/meta, control label, data emphasis. The same semantic importance should not arbitrarily change scale or weight between screens.

### Spacing rhythm

Define a small spacing rhythm and distinguish structural gaps from local control spacing. Repetition should reveal grouping; do not create a unique gap value for every screen.

### Surface/material roles

Record what each surface means: base content, raised/contextual chrome, selection, modal/transient layer, grouped secondary region. A border, fill, blur, shadow, or glass treatment must keep the same semantic meaning across the product.

### Control/action placement

Recurring actions should occupy predictable regions unless the task changes their importance. Avoid moving the same action between toolbar, floating button, card footer, and context menu merely to make screens look different.

### Navigation and selection semantics

The same navigation level must behave consistently. Selection, drill-in, back behavior, inspectors, sheets/popovers, tabs, sidebars, and breadcrumbs must not change meaning screen by screen.

### Terminology and icon semantics

Use one term for one concept. Do not alternate between Edit/Modify, Delete/Remove, Favorites/Saved, Settings/Preferences unless they represent different operations. The same icon should not mean different things in adjacent contexts.

### Interaction contract

Equivalent mutations should use compatible commit/recovery semantics. If most lightweight settings update immediately, one arbitrary toggle should not suddenly require Save. If destructive actions use undo, do not introduce confirmation dialogs inconsistently without consequence-based reason.

### Density and information hierarchy

Different screens may legitimately have different density, but the product should preserve its hierarchy language. A secondary label should not become visually dominant merely because another screen was designed independently.

## Screen-family matrix

For each major screen or state family, record:

| Screen/family | Primary object/task | Title role | Primary action location | Navigation level | Selection model | Density | Surface/material notes |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Use the matrix to identify unexplained drift. Differences are allowed when the task demands them; unexplained differences are defects.

## Transition audit

Inspect at least three important transitions, not only static endpoints:

- collection → detail
- view → edit → committed view
- normal → loading/error/recovery
- wide → compact architecture
- selection → inspector/contextual action
- modal/popover → dismissal and focus return

For each transition ask:

1. What stays visually and spatially stable?
2. What changes because the task changed?
3. Does the user's object/selection/context remain legible?
4. Does focus return predictably?
5. Does terminology/action placement remain recognizable?

## Drift smells

Flag for review:

- same semantic heading rendered with unrelated size/weight across screens
- many one-off spacing values or radii without product meaning
- same action appears in unrelated locations without task reason
- same concept has multiple labels/icons
- navigation levels change behavior unexpectedly
- one screen becomes dramatically more card-heavy/glassy/shadowed than peers
- arbitrary per-screen accent colors or materials
- conflicting save/undo/delete conventions
- empty/error states introduce a different visual language
- responsive variants feel like separate products
- one screen is much denser/sparser without content reason

These are evidence prompts, not automatic style laws.

## Apple-specific principle

Coherence does not mean forcing every screen into one template. Apple-like coherence comes from stable semantics, hierarchy, system behavior, typography, spacing relationships, materials, and transitions while allowing the content/task to determine composition.

## Completion evidence

Before calling a multi-screen product coherent, `DESIGN.md` should answer:

- What are the shared typography roles?
- What spacing rhythm is used?
- What do the product's surfaces/materials mean?
- Where do recurring primary/secondary actions live?
- How do navigation and selection behave across screen families?
- Which terminology/icon meanings are invariant?
- Which interaction contracts are shared?
- Which cross-screen differences are intentional and why?
- Which transitions were inspected?

A single polished screen is not evidence of product coherence.