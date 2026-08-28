---
name: apple-design
description: Design or redesign a whole product with Apple-level hierarchy, restraint, composition, platform awareness, adaptivity, accessibility, content integrity, interaction architecture, cross-screen coherence, project design grammar, implementation-derived grammar evidence, and rendered critique. Use whenever someone describes a product they want rather than asking about a specific control — "I want an app for splitting bills", "I'm building a dashboard for our support team", "we need a landing page", "help me make a tool that…", "can you build me…" — with or without the word design, and with or without a platform or brand colour named. Also for: starting any app, website, dashboard, marketing page or cross-platform project; deciding what screens exist and how they connect; generating a design system or brand palette; and fixing a build that ships only its happy path. If the request names a product and not a component, this skill runs first. For a specific rule or spec use apple-hig; for exact iOS values and CSS use apple-ui-kit; for animation use apple-motion.
---

# Apple Design Director

Specialists:
- `apple-hig` — authoritative platform rules, behavior, accessibility, components, APIs
- `apple-ui-kit` — measured iOS visual values/recipes where system appearance is not available
- `apple-motion` — interaction physics and animation
- `apple-design` — hierarchy, content, divergence, composition, adaptivity, interaction architecture, coherence, project grammar, implementation audit, reduction, and critique

## Authority rule
Use `HIG → platform differences → system APIs/components → product composition → measured visual evidence (when available) → project grammar → design judgment`.

The measured visual corpus is currently iOS 27. Never present iOS screenshots as measured macOS evidence.

## Governing principle
**Do not begin by placing components. Begin by composing information.** Prefer hierarchy through position, alignment, spacing, typography, scale, grouping, disclosure, motion, or context over unnecessary containers.

# Required workflow

## 1–11. Product reasoning
Follow these references in order as applicable:

1. `references/platform-routing.md` — platform/HIG routing and system-component preference
2. `references/content-hierarchy.md` — question/task → decision → representation
3. `references/design-invariants.md` — structural invariants
4. `references/spatial-models.md` + `references/design-divergence.md` — 2–3 credible directions
5. `select_references.py` — platform-aware evidence shortlist and inspection
6. `references/adaptivity.md` — architectural transformation across widths/input
7. `references/interaction-architecture.md` — entry → action → commit → recovery → continuation
8. `references/product-coherence.md` — cross-screen semantics and transition audit

Use realistic content, stress cases, explicit commit/recovery behavior, and task-driven differences rather than genre defaults.

## 12. Extract or inherit the project design grammar
Read `references/design-grammar.md`.

If `PROJECT_GRAMMAR.md` exists, read it before designing new screens. Inherit applicable **established** rules by default. Allow justified exceptions when task, content, platform, or input model requires them.

After at least two meaningful screen/state families exist, create or refresh `PROJECT_GRAMMAR.md`. Classify rules as **established**, **provisional**, **exception**, or **retired**. Capture semantic typography, spacing, geometry/material meaning, navigation/selection, action placement, content representation, interaction, language/icons, useful repeated motion, and adaptive transformations.

Do not convert accidental repetition into a rule. Do not turn the grammar into a token dump.

## 13. Audit the implementation against the grammar
Once implementation exists, run:

```bash
python3 audit_grammar.py ./design
```

This creates `IMPLEMENTATION_GRAMMAR_AUDIT.md` from actual HTML/CSS evidence. It extracts repeated and one-off typography, spacing, geometry, surface/material patterns, semantic element usage, recurring labels, and repeated implementation classes.

**Observations are evidence, not automatic rules.** Review every generated prompt and decide whether the observation:

- confirms an established grammar rule;
- should remain provisional;
- is an intentional exception that needs documentation;
- is accidental drift/refactoring debt;
- contradicts or retires an older rule.

Set the audit status to `COMPLETE`, then verify:

```bash
python3 audit_grammar.py ./design --check
```

If implementation evidence changes the grammar, update `PROJECT_GRAMMAR.md` deliberately and rerun `check_grammar.py`. Never let code silently redefine the design system.

## 14. Plan component states and accessibility
Read `references/interaction-accessibility.md`. Check applicable focus, hover, pressed, selected, disabled, editing, loading, drag/drop, destructive/undo and inactive-window states plus scaling/zoom, assistive semantics, targets, non-color communication, Reduce Motion/Transparency, focus visibility, and recovery.

## 15. Compose and review
Compose regions, reading order, density, persistent/contextual chrome, and functional empty space before decorative material choices. Avoid card wallpaper, excessive pills, decorative glass/blur, gratuitous shadows, unsupported giant headings, duplicate primary actions, and decorative motion.

# Project gates

```bash
python3 check_divergence.py ./design
# All of them at once, in the order the evidence appears:
python3 grade.py ./design            # add --quick to skip the browser pass

# Or one at a time, when you want the full list of what a gate wants:
python3 check_content.py ./design
python3 check_interaction.py ./design
python3 check_coherence.py ./design
python3 check_grammar.py ./design          # once grammar is applicable
python3 audit_grammar.py ./design --check # after implementation audit is completed
python3 check_direction.py ./design
python3 check_design.py ./design
```

Rendered review:

```bash
python3 render_review.py ./design
```

Use `references/visual-critique.md` and record findings as **evidence → consequence → correction**. Review project-grammar adherence and implementation-audit findings alongside hierarchy, content, interaction, coherence, typography, density, adaptivity, accessibility, materials, platform authenticity, states, transitions, and reduction.

After revision:

```bash
python3 render_review.py ./design --check
```

# Complete loop

```text
brief
→ platform/HIG
→ read existing project grammar
→ hierarchy + content + invariants
→ divergence + reference inspection
→ adaptivity + interaction architecture
→ cross-screen coherence
→ extract/update project grammar
→ implement
→ implementation grammar audit
→ classify observed repetition/drift
→ update grammar deliberately if warranted
→ evidence gates + mechanical gate
→ rendered review
→ correction / reduction
→ rerender + completed audit checks
```

# Final standard
A successful result feels Apple-like because it is clear, restrained, adaptive, accessible, platform-correct, content-aware, behaviorally dependable, coherent across screens and transitions, and capable of maintaining its own evidence-backed design grammar—not because repeated CSS or rounded glass accidentally became the design system.