---
name: apple-design
description: Design or redesign a whole product with Apple-level hierarchy, restraint, composition, platform awareness, adaptivity, accessibility, and evidence-based critique. Use for apps, websites, dashboards, SaaS, product surfaces, and cross-platform interfaces when the task is broader than a single component. This skill acts as the design director: it routes through the target platform and HIG, defines information hierarchy and invariants, compares competing spatial directions, inspects relevant references, prefers system components, plans adaptive transformations and interaction states, then validates both mechanical and rendered visual quality. Use when a design technically works but still feels generic, card-heavy, overly decorative, platform-inappropriate, or insufficiently Apple-like.
---

# Apple Design Director

This skill decides what the product should feel like before it decides what components to place.

Specialists:

- `apple-hig` — authoritative platform rules, behavior, accessibility, components, APIs
- `apple-ui-kit` — measured iOS visual values/recipes where a system palette is unavailable
- `apple-motion` — interaction physics and animation implementation
- `apple-design` — product hierarchy, platform routing, divergence, composition, invariants, adaptivity, reference selection, reduction, and critique

## Authority rule

**No measured visual kit does not mean no Apple guidance.**

For native Apple platforms use this order:

`HIG → platform differences → system APIs/components → product composition → measured visual evidence (when available) → design judgment`

The current measured visual corpus is iOS 27. macOS is still fully HIG-governed; only measured macOS appearance is absent. Never present iOS screenshots as measured macOS evidence.

Read `references/platform-routing.md` whenever platform fit matters.

## Governing principle

**Do not begin by placing components. Begin by composing information.**

Before adding a card, panel, border, toolbar, floating control, blur, or shadow, ask whether hierarchy can be communicated through position, alignment, spacing, typography, scale, grouping, progressive disclosure, motion, or context.

**If the interface still works after removing a container, remove it.**

# Required workflow

## 1. Understand the product

Establish:

- primary user
- primary recurring task
- primary object/information
- what must be instantly visible
- secondary and tertiary information
- what can remain contextual
- required platforms/widths/input methods

Infer routine design decisions when the brief is broad rather than pushing them back to the user.

## 2. Route through the platform before divergence

Read `references/platform-routing.md`.

For native Apple work, inspect `apple-hig/references/platform-diffs.md`, relevant `rules.md`, and relevant components before proposing architecture.

Before designing custom native controls, search:

1. `apple-hig/references/framework-index.md`
2. relevant HIG component/rules
3. `apple-hig/references/api-map.md`

Prefer system components unless a concrete product requirement makes them insufficient.

### macOS

macOS designs are HIG-first even without a measured Mac kit. Consider where relevant:

- windows and resizing
- sidebar/split view
- toolbar/title region
- inspector
- tables and dense lists
- menus/context menus
- keyboard commands
- pointer/hover/focus
- selection/multi-selection
- popovers/sheets
- multiwindow behavior
- drag/drop
- inactive-window states

Reject iPhone-derived assumptions such as bottom tabs, oversized touch density, giant mobile titles, or modal sheets for routine desktop choices unless HIG/task evidence supports them.

### iOS/iPadOS

Use touch-first hierarchy and HIG navigation. Tabs are not inferred from destination count alone. iPad candidates should exploit width where useful rather than merely enlarge iPhone.

### Web

Treat the browser as a platform. Transfer Apple principles, not copied iOS chrome. Preserve web semantics, keyboard/pointer behavior, responsive architecture, and browser expectations.

### Marketing

HIG is not a marketing-page template. Use editorial hierarchy and narrative structure rather than native app chrome.

## 3. Establish product character

Choose one dominant quality and at most one supporting quality:

calm, dense, editorial, utilitarian, immersive, playful, professional, content-first, data-first, tool-like, spatial.

Do not combine every adjective.

## 4. Build information hierarchy

Rank contents:

1. **Primary** — why the user is here
2. **Secondary** — context needed to understand/act
3. **Tertiary** — supporting detail
4. **Contextual** — appears only when relevant

If everything is visually equal, the design has failed before styling.

Prefer typography/spacing/alignment/disclosure over additional containers.

## 5. Define design invariants

Read `references/design-invariants.md` and record 3–5 structural invariants in `DESIGN.md`.

Examples:

- document remains the dominant work surface
- only selected objects reveal destructive actions
- today's status is always the first read
- collection remains navigation; detail does not leak into rows
- brand color identifies action/selection, not decoration

Invariants must survive responsive changes and states unless explicitly revised with evidence.

## 6. Diverge before committing

Read:

- `references/spatial-models.md`
- `references/design-divergence.md`

For major screens/products, consider 2–3 genuinely different structural directions when credible. Platform constraints come first, so do not invent obviously invalid cross-platform candidates.

Candidates must differ in structural dimensions such as dominant region, pane relationship, navigation, persistent chrome, density, sequence/simultaneity, or adaptive transformation. Color/radius/card-style variants do not count.

Compare candidates on:

- primary-task fit
- hierarchy clarity
- information relationship
- platform fit
- adaptivity
- restraint
- product-specific distinctiveness

Explicitly reject alternatives for product-specific reasons. Scores expose trade-offs; they do not choose automatically.

## 7. Select and inspect references

Generate a focused shortlist:

```bash
python3 select_references.py \
  --query "<task, components, states, navigation>" \
  --model <leading-model> -o ./design/REFERENCES.md
```

Then inspect the **actual images**. Filenames are not visual evidence.

Extract relationships:

- first read
- grouping
- persistent vs contextual chrome
- state differences
- material/tint meaning
- relationships that should not transfer to this product/platform

Synthesize 3–5 concrete relationships. If references invalidate a candidate assumption, revisit divergence.

References are evidence, not votes and not screenshots to clone.

## 8. Commit the spatial model and adaptive plan

Implemented starter models:

- `workspace`
- `list-detail`
- `dashboard`
- `document`
- `editorial`
- iOS `stack`
- iOS `tabs`

Other valid models include inspector, command surface, feed, immersive media/map, dense table, multi-pane editor, or platform-specific macOS compositions. Never force the product into an available scaffold.

Read `references/adaptivity.md` and record:

- wide/default architecture
- compact architecture
- what disappears
- what becomes sequential
- what becomes contextual
- how selection/context survives
- how pointer/keyboard assumptions change for touch

Responsive design is architectural transformation, not merely smaller CSS.

## 9. Plan interaction states and accessibility before polish

Read `references/interaction-accessibility.md`.

Build a state matrix from what each component actually supports: default, hover, keyboard focus, pressed, selected, disabled, editing, expanded/open, loading/submitting, drag/drop, destructive/undo, inactive-window where relevant.

Check applicable HIG guidance for:

- Dynamic Type/text scaling/browser zoom
- keyboard navigation/focus order
- VoiceOver/screen-reader semantics
- target size/spacing
- contrast and non-color state communication
- Reduce Motion
- Reduce Transparency
- focus visibility
- error identification/recovery

A polished default state is not a finished component.

## 10. Compose before decorating

For each screen decide:

- dominant region
- secondary region
- reading order
- alignment system
- density
- content width
- persistent chrome
- contextual chrome
- functional empty space

Only then choose surfaces, borders, materials, shadows, and motion.

# Apple restraint rules

Apple-like design is not “rounded + glass + minimal.” Avoid accidental generative-UI habits:

- card grids for unrelated information
- identical rounded rectangles around every section
- excessive pills
- floating containers everywhere
- decorative glass/blur
- gratuitous shadows/gradients
- center-aligned everything
- repeated icon + title + paragraph feature cards
- unsupported giant headings
- duplicate primary actions
- decorative motion

Use a container only when it communicates a real boundary, grouping, material layer, or interaction region.

## Material discipline

A translucent surface must answer: **what is floating above what, and why?**

Blur, vibrancy, shadow, and depth should communicate hierarchy, modality, separation, or focus. If the relationship is meaningless, simplify.

## Motion discipline

Motion should communicate causality, continuity, spatial relationship, state change, or hierarchy. Delegate gesture/spring implementation to `apple-motion`. Never animate merely to make the interface feel less static.

# Project workflow

Use `new_project.py` only after hierarchy, platform routing, divergence, reference inspection, and model commitment.

Examples:

```bash
python3 new_project.py --name Pulse --brand "#5A67D8" \
  --kind web --model dashboard --character dense \
  --screens "Overview,Reports,Settings" -o ./design

python3 new_project.py --name Clay --brand "#C1552E" \
  --kind ios --model stack --screens "Plan,Recipes,List,Settings" -o ./design
```

Marketing selects editorial automatically.

`new_project.py` provides infrastructure, not art direction. Update `DESIGN.md` so it contains actual hierarchy, candidate/rejection rationale, invariants, platform constraints, and adaptive plan before polishing.

## Mechanical gate

```bash
python3 check_design.py ./design
```

This checks wiring, resources, states, browser failures, contrast, overflow, targets, and theme integrity. It does not decide whether the design is good.

## Rendered visual gate

```bash
python3 render_review.py ./design
```

Inspect all generated screenshots. Read `references/visual-critique.md` and write findings as:

**evidence → consequence → correction**

Review hierarchy, invariants, composition, containers, typography, density, adaptive transformations, interaction states, accessibility, material/color, system-component usage, platform authenticity, states, and reduction.

After revising and rerendering where needed, replace all `[PENDING]` judgments, set review status to `COMPLETE`, then run:

```bash
python3 render_review.py ./design --check
```

Do not call a design visually reviewed or finished while this fails.

# Platform anti-patterns

`references/visual-critique.md` contains the full platform-specific smell list. Especially reject:

- **macOS:** giant touch controls/titles, bottom tabs, mobile sheets for ordinary choices, missing keyboard/menu affordances, cardified tables
- **iOS:** desktop sidebars/inspectors squeezed into phone, tiny controls, hover-dependent actions
- **web:** copied phone chrome, pseudo-native controls that harm browser expectations, glass/cards as the whole language
- **marketing:** repeated centered heading + three-card sections without narrative reason

# Design quality regression

Read `references/benchmark-suite.md` when changing this skill materially.

The benchmark suite spans analytics, mail, photo editing, finance, plant tracking, notes, developer tools, settings, media, commerce, marketing, operations, messaging, calendar, and files.

Regression warnings include:

- one spatial model dominating unrelated briefs
- sidebar + cards appearing everywhere
- identical navigation across iOS and macOS without task reasons
- macOS outputs omitting keyboard/menu/pointer thinking
- marketing reverting to feature-card wallpaper
- dashboards reverting to equal metric tiles
- responsive plans that only say shrink/stack
- custom controls without system-component lookup
- missing rejected alternatives or invariants

Mechanical correctness plus structural sameness is a failed design skill.

# Complete loop

```text
brief
→ platform/HIG routing
→ product character + hierarchy
→ design invariants
→ 2–3 credible structural directions
→ reference shortlist + image inspection
→ compare / reject / commit
→ adaptive architecture plan
→ interaction + accessibility matrix
→ scaffold / compose / implement
→ check_design.py
→ render_review.py
→ screenshot inspection
→ evidence → consequence → correction
→ reduction / revision
→ rerender
→ render_review.py --check
```

# Delegation

| Need | Skill |
|---|---|
| Product shape, platform routing, hierarchy, divergence, adaptivity, critique | **apple-design** |
| Apple rules, behavior, accessibility, platform differences, system APIs | **apple-hig** |
| Measured iOS visual values, typography, radii, colors, CSS recipes | **apple-ui-kit** |
| Gestures, springs, velocity, interruptibility, motion | **apple-motion** |

# Final standard

A successful result feels Apple-like because it is clear, composed, restrained, adaptive, accessible, platform-correct, spatially coherent, typographically disciplined, purposeful in motion, deliberately chosen over credible alternatives, and proven through rendered inspection — **not because it is covered in rounded glass.**