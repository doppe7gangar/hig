---
name: apple-design
description: Design or redesign a whole product with Apple-level hierarchy, restraint, composition, platform awareness, adaptivity, accessibility, content integrity, and evidence-based critique. Use for apps, websites, dashboards, SaaS, product surfaces, and cross-platform interfaces when the task is broader than a single component. This skill acts as the design director: it routes through platform/HIG guidance, defines information and content hierarchy, compares structural directions, inspects references, prefers system components, plans adaptive transformations and interaction states, validates representation choices, then checks direction evidence, implementation quality, and rendered visual results.
---

# Apple Design Director

This skill decides what the product should feel like before it decides what components to place.

Specialists:

- `apple-hig` — authoritative platform rules, behavior, accessibility, components, APIs
- `apple-ui-kit` — measured iOS visual values/recipes where system appearance is not available
- `apple-motion` — interaction physics and animation implementation
- `apple-design` — product hierarchy, content hierarchy, platform routing, divergence, composition, invariants, adaptivity, reference selection, reduction, and critique

## Authority rule

**No measured visual kit does not mean no Apple guidance.**

For native Apple platforms use:

`HIG → platform differences → system APIs/components → product composition → measured visual evidence (when available) → design judgment`

The current measured visual corpus is iOS 27. macOS remains fully HIG-governed; measured macOS appearance is simply not registered yet. Never present iOS screenshots as measured macOS evidence.

Read `references/platform-routing.md` whenever platform fit matters.

## Governing principle

**Do not begin by placing components. Begin by composing information.**

Before adding a card, panel, border, toolbar, floating control, blur, or shadow, ask whether hierarchy can instead be communicated through position, alignment, spacing, typography, scale, grouping, progressive disclosure, motion, or context.

If the interface still works after removing a container, remove it.

# Required workflow

## 1. Understand the product

Establish the primary user, recurring task, primary object/information, what must be instantly visible, secondary/tertiary information, contextual information, required platforms, widths, and input methods.

## 2. Route through platform/HIG before divergence

Read `references/platform-routing.md`.

For native Apple work inspect `apple-hig/references/platform-diffs.md` and relevant `rules.md`/components before proposing architecture.

Before creating a custom native control, search:

1. `apple-hig/references/framework-index.md`
2. relevant HIG component/rules
3. `apple-hig/references/api-map.md`

Prefer system components unless a concrete product requirement makes them insufficient.

### macOS

Even without a measured Mac visual kit, follow HIG and consider where relevant: windows/resizing, sidebars/split views, toolbar/title region, inspectors, dense lists/tables, menus/context menus, keyboard commands, pointer/hover/focus, selection/multi-selection, popovers/sheets, multiwindow behavior, drag/drop, inactive-window states.

Reject imported iPhone assumptions—bottom tabs, giant touch controls/titles, excessive mobile sheets—unless task/HIG evidence supports them.

### iOS/iPadOS

Use touch-first hierarchy and HIG navigation. Tabs are not inferred from destination count. iPad should exploit width where useful rather than simply enlarge iPhone.

### Web

Treat the browser as a platform. Transfer Apple principles, not copied iOS chrome. Preserve web semantics, keyboard/pointer behavior, responsive architecture, and browser expectations.

### Marketing

HIG is not a marketing-page template. Use editorial hierarchy and narrative structure.

## 3. Establish product character

Choose one dominant quality and at most one supporting quality: calm, dense, editorial, utilitarian, immersive, playful, professional, content-first, data-first, tool-like, spatial.

## 4. Build information hierarchy

Rank:

1. Primary
2. Secondary
3. Tertiary
4. Contextual

If everything is visually equal, the design has failed before styling. Prefer typography, spacing, alignment, and disclosure over extra containers.

## 5. Build the content model

Read `references/content-hierarchy.md`.

For each important content region record:

- the user question/task
- the decision it enables
- the content/data shape
- required context such as comparison, unit, target, recency, source, or none
- the chosen representation
- why that representation fits
- how it could mislead or fail

Do not choose a chart, table, metric, timeline, card, or media treatment because it looks appropriate to the genre.

Use realistic content before final review: realistic ranges, names, units, statuses, dates, long/short labels, exceptional values, and enough rows/items to expose density assumptions.

Test applicable stress cases such as zero/negative values, missing or stale data, long labels, large collections, one-item collections, urgent states, and user-generated text.

Loading, empty, error, stale/offline, and not-enough-data states must preserve the populated screen's design idea rather than becoming unrelated fallback screens.

## 6. Define design invariants

Read `references/design-invariants.md`. Record 3–5 structural invariants in `DESIGN.md` that must survive implementation, responsive changes, and states.

## 7. Diverge before committing

Read `references/spatial-models.md` and `references/design-divergence.md`.

Consider 2–3 genuinely different structural directions when credible. Platform constraints come first; do not invent obviously invalid candidates. Candidates must differ structurally, not cosmetically.

Compare task fit, hierarchy, information relationship, platform fit, adaptivity, restraint, and product-specific distinctiveness. Explicitly reject alternatives for product-specific reasons.

## 8. Select and inspect references

Use a platform-aware shortlist:

```bash
python3 select_references.py \
  --query "<task, components, states, navigation>" \
  --model <leading-model> --platform <ios|ipados|macos|web|marketing|...> \
  -o ./design/REFERENCES.md
```

For platforms without a registered measured corpus, the selector provides HIG/component guidance and explicitly suppresses fake visual evidence. For macOS, this means HIG-first with no iOS screenshots claimed as measured Mac appearance.

Inspect actual images when available. Extract concrete relationships: first read, grouping, persistent/contextual chrome, state differences, material meaning, and what must not transfer. References are evidence, not votes or screenshots to clone.

## 9. Commit model and adaptive architecture

Starter scaffolds: `workspace`, `list-detail`, `dashboard`, `document`, `editorial`, iOS `stack`, iOS `tabs`. Other models remain valid: inspector, command surface, feed, immersive media/map, dense table, multi-pane editor, macOS-specific compositions.

Read `references/adaptivity.md`. Record wide/default and compact architecture, what disappears, what becomes sequential/contextual, how selection survives, and how pointer/keyboard assumptions change for touch.

Responsive design is architectural transformation, not smaller CSS.

## 10. Plan interaction states and accessibility before polish

Read `references/interaction-accessibility.md`.

Build an applicable state matrix: default, hover, keyboard focus, pressed, selected, disabled, editing, expanded/open, loading/submitting, drag/drop, destructive/undo, inactive-window where relevant.

Check applicable HIG guidance for Dynamic Type/text scaling/zoom, keyboard/focus order, VoiceOver/screen-reader semantics, target size/spacing, contrast/non-color state communication, Reduce Motion, Reduce Transparency, focus visibility, and error recovery.

## 11. Compose before decorating

Decide dominant/secondary regions, reading order, alignment, density, content width, persistent chrome, contextual chrome, and functional empty space. Only then select surfaces, borders, materials, shadows, and motion.

# Restraint

Avoid accidental generative-UI habits: unrelated card grids, rounded boxes around every region, excessive pills, floating containers everywhere, decorative glass/blur, gratuitous shadows/gradients, repeated centered feature-card sections, unsupported giant headings, duplicate primary actions, decorative motion.

A translucent surface must answer: **what is floating above what, and why?**

# Project gates

Use `references/design-direction-template.md` to expand/replace the scaffolded `DESIGN.md` with real evidence.

Divergence gate:

```bash
python3 check_divergence.py ./design
```

Content gate:

```bash
python3 check_content.py ./design
```

Direction gate:

```bash
python3 check_direction.py ./design
```

Mechanical gate:

```bash
python3 check_design.py ./design
```

Do not proceed as if a product has a resolved design while any applicable evidence gate fails.

Rendered review:

```bash
python3 render_review.py ./design
```

Read `references/visual-critique.md`. Every meaningful finding must use:

**evidence → consequence → correction**

Review hierarchy, content/representation fit, invariants, composition, containers, typography, density, adaptive transformations, interaction states, accessibility, material/color, system-component usage, platform authenticity, state continuity, and reduction.

After revision/rerender, complete `VISUAL_REVIEW.md` and verify:

```bash
python3 render_review.py ./design --check
```

Do not call the design finished while any required gate fails.

# Platform anti-patterns

The full list is in `references/visual-critique.md`. Especially reject:

- macOS: giant touch controls/titles, bottom tabs, mobile sheets for ordinary choices, missing keyboard/menu affordances, cardified tables
- iOS: desktop sidebars/inspectors squeezed into phone, tiny controls, hover-dependent actions
- web: copied phone chrome, pseudo-native controls that hurt browser expectations, glass/cards as the entire language
- marketing: repeated centered heading + three-card sections without narrative reason

# Regression testing

Read `references/benchmark-suite.md` and run:

```bash
python3 scripts/eval/design_quality_eval.py
```

The 15-product suite looks for structural sameness across analytics, mail, photo editing, finance, plants, notes, developer tools, settings, media, commerce, marketing, operations, messaging, calendar, and files.

Mechanical validity plus repeated architecture is a failed design skill. Strong architecture filled with arbitrary placeholder content is also a failed design skill.

# Complete loop

```text
brief
→ platform/HIG routing
→ product character + information hierarchy
→ content model + representation decisions + stress cases
→ design invariants
→ 2–3 credible structural directions
→ platform-aware reference shortlist + inspection
→ compare / reject / commit
→ adaptive architecture plan
→ interaction + accessibility matrix
→ scaffold / compose / implement realistic content
→ check_divergence.py
→ check_content.py
→ check_direction.py
→ check_design.py
→ render_review.py
→ screenshot inspection
→ evidence → consequence → correction
→ reduction / revision
→ rerender
→ render_review.py --check
```

# Final standard

A successful result feels Apple-like because it is clear, composed, restrained, adaptive, accessible, platform-correct, content-aware, spatially coherent, typographically disciplined, purposeful in motion, deliberately chosen over credible alternatives, and proven through rendered inspection—not because it is covered in rounded glass.