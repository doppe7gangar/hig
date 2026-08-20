---
name: apple-design
description: Apple's approach to interface design and fluid, physical motion, translated for the web. Use when building or reviewing gesture-driven UI, spring animations, drag/swipe/sheet interactions, momentum and interruptible transitions, translucent materials and depth, typography (optical sizing, tracking, leading), reduced-motion, or the design foundations (feedback, spatial consistency, restraint) behind Apple-style interfaces.
---

# Apple Design

How Apple builds interfaces that stop feeling like a computer and start feeling like an extension of you. This knowledge comes from Apple's WWDC design talks — chiefly *Designing Fluid Interfaces* (WWDC 2018) — distilled and translated into the web platform (CSS, Pointer Events, `requestAnimationFrame`, spring libraries like Motion/Framer Motion).

The through-line: **an interface feels alive when motion starts from the current on-screen value, inherits the user's velocity, projects momentum forward, and can be grabbed and reversed at any instant.** Springs are the tool that makes all of this natural, because they are inherently interruptible and velocity-aware.

## The Core Idea

> "When we align the interface to the way we think and move, something magical happens — it stops feeling like a computer and starts feeling like a seamless extension of us."

An interface is fluid when it behaves like the physical world: things respond instantly, move continuously, carry momentum, resist at boundaries, and can be redirected mid-motion. Everything below is a way to get closer to that.

Apple frames design as serving four human needs: **safety/predictability, understanding, achievement, and joy.** Every rule here serves one of them.

## 1. Response — kill latency

The moment lag appears, the feeling of directness "falls off a cliff." Response is the foundation everything else is built on.

- **Respond on pointer-down, not on release.** Highlight a button the instant it's pressed. Waiting for `click`/touch-up to show feedback feels dead.
- **Be vigilant about every latency.** Audit debounces, artificial timers, transition waits, and the ~300ms tap delay. Anything on the input path that isn't essential is a regression.
- **Feedback must be continuous *during* the interaction, not just at the end.** For a drag, slider, or drawer, update the UI 1:1 with the pointer the whole way through — never animate only when the gesture completes.

```css
/* Feedback lives on the press, and it's instant */
.button:active {
  transform: scale(0.97);
  transition: transform 100ms ease-out;
}
```

## 2. Direct manipulation — 1:1 tracking

> "Touch and content should move together."

When the user drags something, it must stay glued to the finger — and respect the offset from *where they grabbed it*. Snapping to the element's center on grab breaks the illusion immediately.

- Use Pointer Events with `setPointerCapture` so tracking continues even when the pointer leaves the element's bounds.
- Track a short **velocity/position history** (last few `pointermove` events), not just the current point — you'll need velocity at release.

```js
el.addEventListener('pointerdown', (e) => {
  el.setPointerCapture(e.pointerId);
  const grabOffset = e.clientY - el.getBoundingClientRect().top;
});
```

## 3. Interruptibility — the single most important principle

> "The thought and the gesture happen in parallel."

Every animation must be interruptible and redirectable at any moment. A user must be able to grab a moving element mid-flight and reverse it without waiting for the animation to finish.

- **Never lock out input during a transition.**
- **Always animate from the *presentation* (current) value, never the target value.**
- **Avoid CSS `@keyframes` for anything gesture-driven** — springs animate from the current value by default.
- **When a gesture reverses, blend velocity — don't hard-cut it.**
- **Decompose 2D motion into independent X and Y springs.**

## 4. Behavior over animation — use springs

> "Think of animation as a conversation between you and the object, not something prescribed by the interface."

A pre-scripted, fixed-duration animation can't respond to new input. A spring can — new input just changes the target, and the motion stays continuous.

- **Damping ratio** — `1.0` = critically damped, no bounce. `< 1.0` = overshoots. Lower = bouncier.
- **Response** — how quickly the value reaches the target, in seconds. Not "duration" — a spring has no fixed duration.

**Defaults:**
- Start most UI at **damping `1.0`** — graceful and non-distracting.
- Add bounce (**damping ~`0.8`**) **only when the gesture itself carried momentum**.

**Concrete values Apple ships:**

| Interaction | Damping | Response |
| --- | --- | --- |
| Move / reposition | `1.0` | `0.4` |
| Rotation | `0.8` | `0.4` |
| Drawer / sheet | `0.8` | `0.3` |

```js
import { animate } from 'motion';

// Critically damped default
animate(el, { y: 0 }, { type: 'spring', bounce: 0, duration: 0.4 });

// Momentum interaction
animate(el, { y: target }, { type: 'spring', bounce: 0.2, duration: 0.4 });
```

## 5. Velocity handoff — the seam between drag and animation

When a gesture ends, the animation must **continue at the finger's exact velocity**. Pass the pointer's release velocity as the spring's initial velocity.

```
relativeVelocity = gestureVelocity / (targetValue − currentValue)
```

## 6. Momentum projection — animate to where the gesture is *going*

> "Take a small input and make a big output."

Don't snap to the nearest boundary from the *release point*. Use velocity to **project the resting position**, then snap to the target nearest that projected point.

```js
function project(initialVelocity, decelerationRate = 0.998) {
  return (initialVelocity / 1000) * decelerationRate / (1 - decelerationRate);
}
```

## 7. Spatial consistency — symmetric paths, anchored origins

> "If something disappears one way, we expect it to emerge from where it came."

- **Enter and exit along the same path.**
- **Anchor interactions to their source.** Set `transform-origin` to the trigger.
- **Mirror the easing on reversible transitions.**

## 8. Hint in the direction of the gesture

Intermediate motion should telegraph where things are going — make the in-between frames point at the outcome, not just interpolate blindly.

## 9. Rubber-banding — soft boundaries

At an edge, resist progressively instead of stopping hard.

```js
function rubberband(overshoot, dimension, constant = 0.55) {
  return (overshoot * dimension * constant) / (dimension + constant * Math.abs(overshoot));
}
```

## 10. Gesture design details

- **Tap:** highlight on touch-*down* (instant), commit on touch-*up*. Add ~10px hysteresis.
- **Drag/swipe:** require a small movement threshold (~10px) before committing.
- **Detect all plausible gestures in parallel from the first move.**
- **Minimize disambiguation delays.**

## 11. Frame-level smoothness

- Keep per-frame positional change below the perception threshold.
- `requestAnimationFrame` is the web's display-synced clock. Animate only `transform` and `opacity`.

## 12. Materials & depth — translucency conveys hierarchy

- **Build nav/toolbars/sheets as translucent layers** (`backdrop-filter: blur()`) with content scrolling underneath.
- **Material weight encodes hierarchy.** Never stack a light translucent surface on another.
- **Dim to focus, separate to keep flow.**

```css
.toolbar {
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(20px) saturate(180%);
}
```

## 13. Multimodal feedback

1. **Causality** — trigger on the actual causal event.
2. **Harmony** — visual, sound, and haptic fire on the **same frame**.
3. **Utility** — reserve for meaningful moments only.

## 14. Reduced motion & accessibility

- **`prefers-reduced-motion: reduce`** — replace slides/springs with opacity cross-fades.
- **`prefers-reduced-transparency: reduce`** — raise background opacity, drop blur.
- **`prefers-contrast: more`** — near-solid backgrounds with defined borders.

```css
@media (prefers-reduced-motion: reduce) {
  .sheet { transition: opacity 200ms ease; transform: none !important; }
}
```

## 15. Typography — optical sizing, tracking, leading

- **Tracking is size-specific** — large text wants *negative* tracking; small text wants *positive*.
- **Leading tracks size inversely** — tight on large headings, looser on body copy.
- **Build hierarchy from weight + size + leading as a set.**
- **Respect the user's text-size setting.**
- **Default to the platform's system font.**

```css
.display {
  font-size: clamp(2rem, 5vw, 4rem);
  line-height: 1.05;
  letter-spacing: -0.02em;
  font-optical-sizing: auto;
}
```

## 16. Design foundations — the eight principles

1. **Purpose.** Make with intention; decide what *not* to build.
2. **Agency.** Keep people in control; offer choices.
3. **Responsibility.** Act in the user's interest.
4. **Familiarity.** Build on what people already know.
5. **Flexibility.** Design for different contexts and abilities.
6. **Simplicity — not minimalism.** Strip the unnecessary so the core purpose shines.
7. **Craft.** Uncompromising attention to detail builds trust.
8. **Delight.** The result of getting the other seven right.

## 17. Process

- **Prototype interactively.**
- **Design interaction and visuals together.**
- **Test with real people in real context.**

## Quick Reference

| Need | Technique | Concrete value |
| --- | --- | --- |
| Default UI spring | Critically damped | `damping 1.0`, `response 0.3–0.4` |
| Momentum spring | Under-damped | `damping ~0.8`, `response 0.3–0.4` |
| Flick landing | Project momentum | `current + (v/1000)·d/(1−d)`, `d ≈ 0.998` |
| Interrupt | Start from live value | read the on-screen transform |
| Feedback | On pointer-down | never only at the end |
| Boundary | Rubber-band | progressive resistance |
| Translucent chrome | `backdrop-filter` | content scrolls under |
| Type tracking | Size-specific | tighten large (`-0.02em`), body `0` |
| Reduced motion | Cross-fade | `@media (prefers-reduced-motion)` |
