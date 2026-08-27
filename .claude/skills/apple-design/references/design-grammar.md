# Project design grammar

A coherent product should accumulate a small, explicit design grammar as screens are built. This is project-local memory, not a new universal design system.

## Purpose

Extract repeated, intentional relationships from implemented screens so later work inherits the product's established language instead of starting from zero.

The grammar should record **semantic rules**, not a dump of CSS values. A value becomes a rule only when it has a stable product meaning.

## When to extract

Extract or refresh the grammar after at least two meaningful screen/state families exist, and again after a major new workflow or adaptive mode is introduced.

Do not extract a grammar from one polished hero screen.

## Grammar domains

### Typography
Record semantic roles and their relationships: product/page title, section heading, body, secondary/meta, control label, data emphasis. Prefer relationships such as “section heading is one step above body and never competes with page title” over isolated pixel sizes.

### Spacing
Record the small rhythm that repeatedly communicates grouping: page inset, section separation, row gap, control gap, compact gap. Note where density legitimately changes.

### Geometry and surfaces
Record what radii, separators, fills, elevation, blur/glass, and grouped surfaces *mean*. Do not preserve a radius merely because it appeared twice by accident.

### Navigation and selection
Record persistent navigation levels, selection appearance, drill-in behavior, inspector/detail behavior, compact transformations, and context preservation.

### Actions and controls
Record where recurring primary/secondary/contextual actions live, destructive-action treatment, control sizing, and when actions become menus/toolbars/contextual controls.

### Content representation
Record repeated conventions for values, units, baselines, status, timestamps, metadata, charts/tables/lists, missing data, and freshness.

### Interaction
Record commit models, undo/cancel behavior, optimistic updates, focus restoration, keyboard commands, drag alternatives, and recovery conventions.

### Motion
Record only purposeful repeated motion relationships: navigation transition, disclosure, selection feedback, modal presentation, loading progress. Respect Reduce Motion.

### Language and icons
Record canonical product terms and stable icon meanings.

### Adaptivity
Record how recurring structures transform across width/input classes. Preserve semantic relationships even when geometry changes.

## Evidence threshold

Classify every extracted rule:

- **established** — repeated intentionally across at least two relevant screen/state families, or explicitly required by platform/product architecture
- **provisional** — observed once but likely to recur; must not silently become a universal rule
- **exception** — intentionally differs because the task/content demands it
- **retired** — previously used but superseded; new work must not reintroduce it casually

## PROJECT_GRAMMAR.md format

```markdown
# Project design grammar

## Scope
- Product:
- Platforms:
- Last refreshed:
- Evidence screens/states:

## Established rules
| Domain | Semantic rule | Evidence | Applies to | Exceptions |
|---|---|---|---|---|
| Typography | ... | Inbox; Detail | content screens | immersive player |

## Provisional rules
| Domain | Candidate rule | Evidence needed |
|---|---|---|

## Intentional exceptions
| Screen/context | Rule diverged from | Why |
|---|---|---|

## Retired rules
| Rule | Replaced by | Reason |
|---|---|---|

## Canonical language
| Concept | Term/icon | Do not substitute |
|---|---|---|

## Adaptive transformations
| Structure | Wide/default | Compact | Invariant preserved |
|---|---|---|---|
```

## Using the grammar

Before designing a new screen:

1. read `PROJECT_GRAMMAR.md` if present;
2. identify applicable established rules;
3. inherit them by default;
4. do not force irrelevant rules onto a different task;
5. record a justified exception when the task needs divergence;
6. update provisional/established/retired status after implementation and review.

The grammar constrains **semantic consistency**, not composition. A new screen may use a different spatial model while retaining the same hierarchy language, action semantics, terminology, and interaction contract.

## Anti-patterns

Do not:
- turn every observed CSS value into a token;
- create dozens of project tokens before repeated evidence exists;
- preserve accidental inconsistencies as “rules”;
- use the grammar to prevent task-driven differences;
- copy iOS visual measurements into macOS/web as project rules;
- let provisional rules silently become established;
- retain retired rules because old code still contains them.

## Review questions

- Does each established rule have evidence or explicit architectural/platform justification?
- Can a new screen determine what to inherit without copying an old screen?
- Are exceptions explained by task/content rather than aesthetics alone?
- Are terminology and interaction semantics represented, not only visual tokens?
- Does the grammar stay small enough to understand?
- Did the latest screen reveal a better rule that should retire an older one?
