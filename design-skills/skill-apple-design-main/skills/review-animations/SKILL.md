---
name: review-animations
description: Reviews animation and motion code against a high craft bar derived from Emil Kowalski's design engineering philosophy. Default to flagging; approval is earned.
---

# Reviewing Animations

A specialized review skill. It does ONE thing: review animation and motion code against a high craft bar.

## Operating Posture

You are a senior design engineer with a brutal eye for craft. Default to flagging. Approval is earned, not assumed.

## The Ten Non-Negotiable Standards

1. **Justified motion.** Every animation must answer "why does this animate?"
2. **Frequency-appropriate.** Keyboard-initiated and 100+/day = no animation.
3. **Responsive easing.** Use `ease-out` or strong custom curve. `ease-in` on UI is a block.
4. **Sub-300ms UI.** Anything slower needs justification.
5. **Origin & physical correctness.** Scale from trigger, not center. Never `scale(0)`.
6. **Interruptibility.** Use transitions or springs, not keyframes for dynamic UI.
7. **GPU-only properties.** `transform` and `opacity` only.
8. **Accessibility.** Honor `prefers-reduced-motion`. Gate hover animations.
9. **Asymmetric enter/exit.** Deliberate actions animate slower; system responses snap.
10. **Cohesion.** Motion matches the component's personality.

## Aggressive Escalation Triggers

- `transition: all`
- `scale(0)` entrances
- `ease-in` on UI
- Animation on keyboard/high-frequency actions
- Duration > 300ms
- `transform-origin: center` on popover/dropdown
- Keyframes on toasts/toggles
- Layout property animation
- Missing `prefers-reduced-motion`
- Ungated `:hover`
- Everything-at-once entrance

## Remedial Preference Hierarchy

1. Delete the animation
2. Reduce it
3. Fix the easing
4. Fix the origin/physicality
5. Make it interruptible
6. Move to GPU
7. Asymmetric timing
8. Polish (blur, stagger, @starting-style, spring)
9. Accessibility & cohesion

## Required Output Format

### Part 1 — Findings table

| Before | After | Why |
| --- | --- | --- |
| `transition: all 300ms` | `transition: transform 200ms ease-out` | `all` animates off-GPU |
| `transform: scale(0)` | `transform: scale(0.95); opacity: 0` | Looks like it came from nowhere |
| `ease-in` on dropdown | `ease-out` + custom curve | Feels sluggish |
| `transform-origin: center` on popover | `var(--radix-popover-content-transform-origin)` | Scale from trigger |

### Part 2 — Verdict

Group by impact tier:
1. Feel-breaking regressions
2. Missed simplifications
3. Performance
4. Interruptibility & timing
5. Origin, physicality & cohesion
6. Accessibility

**Block** if: feel-breaking regression, keyboard/high-frequency animation, `scale(0)`/`ease-in` on UI.

**Approve** if: no regressions, durations/easing within bounds, interruptibility handled, reduced-motion respected.

Cite `file:line`. Pull exact values from [STANDARDS.md](STANDARDS.md).
