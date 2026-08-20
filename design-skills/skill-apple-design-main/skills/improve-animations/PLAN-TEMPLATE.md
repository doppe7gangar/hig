# Plan Template

Every plan follows this structure. The executor has zero context.

```markdown
# NNN — <Short imperative title>

- **Status**: TODO
- **Commit**: <git rev-parse --short HEAD>
- **Severity**: HIGH | MEDIUM | LOW
- **Category**: <audit category>
- **Estimated scope**: <n files>

## Problem

What is wrong, where, why it matters. Cite as `path/file:123`.

​```css
/* src/dropdown.css:14 — current */
.dropdown { transition: all 400ms ease-in; }
​```

## Target

Exact end state — curves, durations, configs.

​```css
/* target */
.dropdown {
  transition: transform 200ms var(--ease-out), opacity 200ms var(--ease-out);
  transform-origin: var(--radix-dropdown-menu-content-transform-origin);
}
​```

## Repo conventions

How the codebase already does it, with exemplar.

## Steps

1. One concrete edit per step.

## Boundaries

- Do NOT touch out-of-scope files.
- Do NOT change markup/structure.
- Do NOT add dependencies.

## Verification

- **Mechanical**: typecheck, lint, build.
- **Feel check**: trigger interaction, confirm in slow motion.
- Toggle `prefers-reduced-motion`.
```
