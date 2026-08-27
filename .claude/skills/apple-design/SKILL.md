---
name: apple-design
description: Design or redesign a whole product with Apple-level hierarchy, restraint, composition, platform awareness, adaptivity, accessibility, content integrity, interaction architecture, cross-screen coherence, project design grammar, and evidence-based critique. Use for apps, websites, dashboards, SaaS, product surfaces, and cross-platform interfaces when the task is broader than a single component.
---

# Apple Design Director

This skill decides what the product should feel like before it decides what components to place.

Specialists:
- `apple-hig` — authoritative platform rules, behavior, accessibility, components, APIs
- `apple-ui-kit` — measured iOS visual values/recipes where system appearance is not available
- `apple-motion` — interaction physics and animation implementation
- `apple-design` — hierarchy, content, divergence, composition, adaptivity, interaction architecture, product coherence, project grammar, reference selection, reduction, and critique

## Authority rule
For native Apple platforms use:
`HIG → platform differences → system APIs/components → product composition → measured visual evidence (when available) → project grammar → design judgment`

The current measured visual corpus is iOS 27. macOS remains HIG-governed; never present iOS screenshots as measured macOS evidence.

## Governing principle
**Do not begin by placing components. Begin by composing information.** Prefer position, alignment, spacing, typography, scale, grouping, progressive disclosure, motion, or context over unnecessary containers.

# Required workflow

## 1. Understand the product
Establish the primary user, recurring task, primary object/information, instant-read needs, secondary/contextual information, platforms, widths, and input methods.

## 2. Route through platform/HIG
Read `references/platform-routing.md`. For native Apple work inspect platform differences, relevant HIG rules/components, framework index, and API map. Prefer system components unless a concrete requirement makes them insufficient. Reject cross-platform mimicry.

## 3. Establish product character
Choose one dominant and at most one supporting quality: calm, dense, editorial, utilitarian, immersive, playful, professional, content-first, data-first, tool-like, spatial.

## 4. Build information hierarchy
Rank Primary, Secondary, Tertiary, Contextual. If everything is visually equal, the design has failed before styling.

## 5. Build the content model
Read `references/content-hierarchy.md`. Tie each important region to a user question/task, decision, content shape, required context, representation rationale, and possible misreading. Use realistic content and stress cases. Loading/empty/error/stale states must preserve the populated design idea.

## 6. Define design invariants
Read `references/design-invariants.md`. Record 3–5 structural invariants that survive implementation, responsive changes, and states.

## 7. Diverge before committing
Read `references/spatial-models.md` and `references/design-divergence.md`. Consider 2–3 credible structural directions, compare them on the same seven criteria, and reject alternatives for product-specific reasons. Do not use arithmetic alone to choose.

## 8. Select and inspect references
Use `select_references.py` with task, model, and platform. Inspect actual images when available. Extract first-read hierarchy, grouping, persistent/contextual chrome, state differences, material meaning, and what must not transfer. References are evidence, not templates to clone.

## 9. Commit model and adaptive architecture
Read `references/adaptivity.md`. Record wide/default and compact architecture, what disappears/becomes sequential/contextual, selection preservation, and input-model changes. Responsive design is architectural transformation, not smaller CSS.

## 10. Design the interaction architecture
Read `references/interaction-architecture.md`. Model the primary task as `entry → orientation → action → system response → commit → recovery → exit/continuation`. Record commit semantics, undo/cancel/reversal, post-completion context, interruptions, async failure, stale/conflicting data, keyboard commands, focus restoration, and non-drag alternatives where relevant.

## 11. Define cross-screen product coherence
Read `references/product-coherence.md`. Define semantic typography roles, spacing rhythm, surface/material roles, recurring action placement, navigation/selection semantics, terminology/icon semantics, and shared interaction contracts. Build the screen-family matrix and audit important transitions. Differences are allowed when the task demands them; unexplained drift is a defect.

## 12. Extract or inherit the project design grammar
Read `references/design-grammar.md`.

If `PROJECT_GRAMMAR.md` already exists, read it **before designing a new screen**. Inherit applicable established rules by default, while allowing justified task-driven exceptions.

After at least two meaningful screen/state families exist, create or refresh `PROJECT_GRAMMAR.md` from reviewed evidence. Classify rules as established, provisional, exception, or retired. Capture semantic typography, spacing, geometry/material meaning, navigation/selection, action placement, content representation, interaction, language/icons, motion where relevant, and adaptive transformations.

Do not turn accidental CSS repetition into a rule. Do not turn the grammar into a giant token dump. The grammar is project-local memory of design semantics.

When a new screen reveals a better convention, update the grammar deliberately: promote, revise, retire, or record an exception rather than silently drifting.

## 13. Plan component states and accessibility
Read `references/interaction-accessibility.md`. Build the applicable state matrix and check text scaling/zoom, keyboard/focus order, assistive semantics, target size, contrast/non-color communication, Reduce Motion/Transparency, focus visibility, and error recovery.

## 14. Compose before decorating
Decide dominant/secondary regions, reading order, alignment, density, content width, persistent/contextual chrome, and functional empty space. Only then choose surfaces, borders, materials, shadows, and motion.

# Restraint
Avoid unrelated card grids, rounded boxes around every region, excessive pills, floating containers everywhere, decorative glass/blur, gratuitous shadows/gradients, repeated centered feature-card sections, unsupported giant headings, duplicate primary actions, and decorative motion.

# Project gates
Use `references/design-direction-template.md` for `DESIGN.md` evidence.

```bash
python3 check_divergence.py ./design
python3 check_content.py ./design
python3 check_interaction.py ./design
python3 check_coherence.py ./design
python3 check_grammar.py ./design
python3 check_direction.py ./design
python3 check_design.py ./design
```

`check_grammar.py` applies once a multi-screen product has enough evidence to establish a grammar. Do not fake established rules just to satisfy the gate.

Rendered review:
```bash
python3 render_review.py ./design
```

Read `references/visual-critique.md`. Findings use **evidence → consequence → correction**. Review hierarchy, representation, invariants, composition, task flow, cross-screen coherence, project grammar adherence, commit/recovery behavior, containers, typography, density, adaptivity, component states, accessibility, material/color, system-component usage, platform authenticity, state continuity, transitions, and reduction.

After revision/rerender:
```bash
python3 render_review.py ./design --check
```

# Regression testing
Read `references/benchmark-suite.md` and run `python3 scripts/eval/design_quality_eval.py`.

Mechanical validity plus repeated architecture is a failed design skill. Strong architecture with arbitrary content is also a failure. A polished static mockup with unresolved recovery is a failure. Individually polished screens with unexplained drift are a failure. A mature multi-screen product that repeatedly reinvents already-established semantics instead of inheriting its project grammar is also a failure.

# Complete loop

```text
brief
→ platform/HIG routing
→ read existing PROJECT_GRAMMAR.md when present
→ hierarchy + content model
→ invariants
→ structural divergence
→ reference inspection
→ commit + adaptivity
→ interaction architecture
→ cross-screen coherence contract + transition audit
→ extract/update project grammar when evidence exists
→ component states + accessibility
→ compose / implement realistic content
→ divergence gate
→ content gate
→ interaction gate
→ coherence gate
→ grammar gate when applicable
→ direction gate
→ mechanical gate
→ rendered review
→ evidence → consequence → correction
→ update grammar after validated change
→ reduction / revision
→ rerender / completion check
```

# Final standard
A successful result feels Apple-like because it is clear, composed, restrained, adaptive, accessible, platform-correct, content-aware, behaviorally dependable, coherent across screens and transitions, able to preserve its own emerging design language, spatially and typographically disciplined, purposeful in motion, deliberately chosen over credible alternatives, and proven through rendered inspection—not because it is covered in rounded glass.