---
name: animation-vocabulary
description: Reverse-lookup glossary that turns a vague description of a web animation into its exact term. Use when the user asks "what's it called when…".
---

# Animation Vocabulary

Turn a vague description into the precise term.

## Quick Start

```
**Stagger** — Animate several items one after another with a small delay between each, creating a cascade.
```

## Instructions

1. Read for intent, not keywords.
2. Quote the glossary verbatim.
3. Disambiguate close terms.
4. When nothing matches, name the closest term.
5. Stay within this glossary.
6. Keep it tight — lead with the term.

## Examples

**Popover grows from button:**
```
**Origin-aware animation** — An element animates out of its trigger, like a popover growing from the button that opened it.
```

**One image turns into another:**
```
**Morph** — One shape smoothly turns into another shape, e.g. Dynamic Island.

Alternates:
- **Crossfade** — fade over each other in the same spot.
- **Shared element transition** — travels and transforms from one position into another.
```

**iOS rubber-band scroll:**
```
**Rubber-banding** — Resistance and snap-back when you drag past a boundary.
```

## Glossary

### Entrances & Exits
- **Fade in / Fade out** — Change opacity.
- **Slide in** — Enter from off-screen.
- **Scale in** — Grow from smaller to full size.
- **Pop in** — Appear with slight overshoot.
- **Reveal** — Uncover gradually via clip-path or mask.

### Sequencing & Timing
- **Keyframes** — Defined animation points (0%, 50%, 100%).
- **Interpolation / Tween** — In-between frames.
- **Stagger** — Delayed cascade.
- **Orchestration** — Coordinated multi-animation timing.

### Movement & Transforms
- **Translate** — Move along X or Y.
- **Scale** — Bigger or smaller.
- **Rotate** — Spin around a point.
- **3D tilt / Flip** — Rotate in 3D space.
- **Transform origin** — Anchor point for transforms.
- **Origin-aware animation** — Animate from trigger, not center.

### Transitions Between States
- **Crossfade** — Fade out one, fade in another.
- **Morph** — Shape smoothly turns into another.
- **Shared element transition** — Element travels between positions.
- **Layout animation** — Animate to new position instead of snap.
- **Accordion / Collapse** — Smooth height expand/collapse.
- **Direction-aware transition** — Slide forward/back based on direction.

### Scroll
- **Scroll reveal** — Fade/slide into viewport.
- **Scroll-driven animation** — Progress tied to scroll position.
- **Parallax** — Different speeds for depth.
- **View transition** — Browser morphs between states.

### Feedback & Interaction
- **Press / Tap feedback** — Subtle scale-down on click.
- **Hold to confirm** — Progress fill while holding.
- **Drag** — Move by grabbing, with momentum.
- **Swipe to dismiss** — Drag off-screen to close.
- **Rubber-banding** — Resistance at boundary.

### Easing
- **Ease-out** — Starts fast, ends slow. Default for UI.
- **Ease-in** — Starts slow, ends fast. Avoid.
- **Ease-in-out** — Slow, fast, slow.
- **Cubic-bezier** — Custom easing curve.
- **Asymmetric easing** — Different accel/decel rates.

### Spring Animations
- **Spring** — Physics-driven motion.
- **Stiffness** — How strongly it pulls toward target.
- **Damping** — How quickly it settles.
- **Bounce** — Overshoots and settles.
- **Momentum** — Carries velocity after drag.
- **Interruptible animation** — Redirectable mid-flight.

### Polish & Effects
- **Blur** — Soften or mask imperfections.
- **Clip-path** — Clip to shape for reveals.
- **Mask** — Soft-edge hiding/revealing.
- **Skeleton / Shimmer** — Loading placeholder.

### Performance
- **Frame rate (FPS)** — 60fps baseline, 120fps on newer displays.
- **Jank** — Visible stutter from dropped frames.
- **Compositing** — GPU-only layer animation.
- **will-change** — Hint for browser layer promotion.

### Principles
- **Purposeful animation** — Serve a function, not decorate.
- **Frequency of use** — More frequent = shorter and subtler.
- **Spatial consistency** — Keep identity across states.
- **Hardware acceleration** — `transform` and `opacity` only.
- **Reduced motion** — Respect `prefers-reduced-motion`.
