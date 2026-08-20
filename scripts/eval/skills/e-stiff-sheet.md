Base directory for this skill: /tmp/claude-0/-home-user-apple-hig/19e48567-ea3b-518d-bd47-52b9e41c0d63/scratchpad/skilltest/work/e-stiff-sheet/.claude/skills/apple-motion

# Apple motion

The HIG covers motion as principle and stops there. Its Motion page has
92 lines on *whether* to animate — purposefully, optionally, following
the gesture — and not one spring parameter. Everything about how the
movement is actually built lives outside it, which is why this exists.

| File | What's in it |
|---|---|
| `references/motion-animation.md` | The spring vocabulary, durations, transition types, interruptibility. |
| `references/microinteractions-feedback.md` | Press states, loading, success and error feedback, haptic pairing. |
| `references/gestures-interaction.md` | Swipe, drag, pinch, edge gestures and how motion should track them. |

## Where each thing comes from

Worth being blunt about, because the three sources have very different
standing and mixing them is how motion advice becomes folklore:

- **Principles → `apple-hig`.** *"Add motion purposefully."* *"Make
  motion optional."* *"Strive for realistic feedback motion that follows
  people's gestures."* These are Apple's own words, in
  `pages/motion.md`. Quote those, not the paraphrases here.
- **Spring names and their behaviour → SwiftUI's API.** `.smooth`,
  `.snappy`, `.bouncy` are real API with real defaults. The bounce
  percentages in `motion-animation.md` are characterisations of them,
  not published constants — treat them as a starting point you tune, and
  don't quote them as Apple's specification.
- **Everything else → observation.** These references came from a
  third-party skill collection and are marked `[observed]` where the
  author inferred behaviour from shipping apps. Useful, not
  authoritative.

Nothing in here is measured the way `apple-ui-kit`'s values are. That
distinction is the point: motion is the part of this repo with the least
ground truth behind it.

## Picking a spring

The one decision that carries most of the feel:

| Spring | Bounce | Use for |
|---|---|---|
| `.smooth` | none | Sheets, modals, background transitions — anything that should settle without drawing attention |
| `.snappy` | slight | Button presses, toggles, selection — the default for direct manipulation |
| `.bouncy` | noticeable | Icon presses, arriving notifications, moments meant to feel rewarding |

Bounce is the whole signal. A sheet that bounces reads as toy-like; a
button press that doesn't reads as dead. Getting this one choice right
does more than tuning durations.

## What separates Apple motion from ordinary motion

- **Interruptible.** A gesture must be able to reverse or redirect an
  animation mid-flight rather than queueing behind it. Anything that
  finishes before it will respond feels laggy no matter how fast it is.
- **Tracks the finger, then takes over.** During a drag the surface
  follows the gesture 1:1; the spring only takes over at release,
  carrying the velocity the gesture had. This is the HIG's *"realistic
  feedback motion that follows people's gestures"* made concrete.
- **Duration is a consequence, not an input.** Springs are specified by
  physics and settle when they settle. Reaching for a fixed 300 ms
  usually means reaching for the wrong tool.
- **Position and opacity, not size and colour.** Moving and fading read
  as physical; scaling and recolouring read as effects.

## Reduce Motion is not optional

`apple-hig` states it plainly — *"Make motion optional."* On the web that
is `prefers-reduced-motion`, and it means replacing the movement, not
merely shortening it: cross-fade instead of slide, cut instead of
animate. `apple-ui-kit`'s `ios-components.css` already guards its own
transitions this way; match it.

## Boundaries

- Values — colour, type, control geometry, materials — belong to
  **apple-ui-kit**, measured from Apple's UI kit. Don't restate them
  here; a hex code in a motion file is a hex code that will go stale
  somewhere nobody looks.
- Rules about *whether* a thing should animate, which presentation to
  use, how layouts adapt — **apple-hig**, with the actual quotations.
- This skill covers how the movement itself is built.


ARGUMENTS: sheet presentation feels stiff and cheap when opening — iOS

No project files here, so I'll answer from the guidance itself.

Three things usually produce that exact feeling, and they're all fixable.

## What "stiff and cheap" actually is

**Stiff** = a fixed-duration curve instead of a spring. `easeInOut(duration: 0.3)` produces motion that arrives and stops dead — no settle, no weight. Duration should be a *consequence* of the physics, not an input you pick.

**Cheap** = the wrong bounce. A sheet that bounces reads as toy-like; a sheet with zero settle reads as a slide-show. Bounce is the single biggest signal in the whole animation.

**Also stiff** = non-interruptible. If a user can't grab the sheet and drag it back mid-flight, it feels laggy no matter how fast it is.

## The spring

For a sheet, you want `.smooth` — no bounce, on a heavyweight surface:

```swift
withAnimation(.smooth(duration: 0.38)) { isPresented = true }
```

Or explicitly, if you want to tune:

```swift
.spring(duration: 0.4, bounce: 0.0)              // iOS 17+
.spring(response: 0.45, dampingFraction: 0.85)   // iOS 14+ equivalent
```

Present ~380 ms, dismiss ~320 ms. That asymmetry is intentional — appear deliberate, disappear brisk. The user already knows where "back" is.

Don't reach for `.snappy` or `.bouncy` here. Those belong to button presses and icon taps, where a little overshoot reads as responsive. On a full-width card it reads as plastic.

## Animate the right properties

Position and opacity, not size and color. Moving and fading read as physical; scaling and recoloring read as effects.

```swift
sheetContent
    .offset(y: isPresented ? 0 : sheetHeight)   // transform — compositor
    // NOT: .frame(height: isPresented ? sheetHeight : 0)
```

Height/frame animation forces a layout pass every frame and can't be interrupted cleanly. Same rule on the web: `transform` and `opacity` only, never `top`/`height`/`margin`.

The scrim should fade in *with* the sheet, driven off the same animation — a scrim that snaps on before the card moves is half the cheapness.

## Interruptibility and gesture handoff

This is the part most custom sheets skip, and it's what separates Apple motion from ordinary motion. During a drag the sheet tracks the finger 1:1 with no animation at all. The spring only takes over at release — carrying the velocity the gesture had:

```swift
DragGesture()
    .updating($dragOffset) { value, state, _ in
        state = max(0, value.translation.height)   // 1:1, no animation
    }
    .onEnded { value in
        let velocity = value.predictedEndTranslation.height - value.translation.height
        let shouldDismiss = value.translation.height > sheetHeight * 0.3 || velocity > 200

        withAnimation(.interpolatingSpring(
            stiffness: 200, damping: 26,
            initialVelocity: velocity / sheetHeight
        )) {
            isPresented = !shouldDismiss
        }
    }
```

The velocity at release is free kinetic energy. Throw it away and snap to a fixed duration, and the interface feels dead — that's the "cheap" you're describing, in its purest form.

## Reduce Motion

Non-negotiable, and it means *replacing* the movement, not shortening it:

```swift
@Environment(\.accessibilityReduceMotion) var reduceMotion
// slide → cross-fade, keeping the same spring timing
```

---

**One thing worth checking first:** if you're using SwiftUI's built-in `.sheet(isPresented:)`, the presentation animation is system-controlled and already correct. Stiffness there is coming from something else — usually expensive view construction blocking the first frames, or content that animates in with its own bad curve after the sheet lands. Worth confirming which case you're in before rebuilding anything.

If you paste the sheet code I can point at the specific lines.