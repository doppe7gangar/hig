# Interaction states and accessibility gate

Accessibility and interaction states are part of the design, not a final compliance sweep.

## State inventory

For every interactive component, determine which states actually apply:

- default
- hover
- keyboard focus
- pointer focus/highlight where applicable
- pressed
- selected
- disabled
- editing
- expanded/open
- loading/submitting
- dragging/drop target
- destructive confirmation or undo state
- inactive-window state on macOS where relevant

Do not demand every state from every component. Build the matrix from the component's behavior and platform.

For custom controls, compare relevant states against the HIG visual corpus when that platform/state exists. Default appearance alone is insufficient evidence.

## Accessibility pass before polish

Check the HIG corpus for applicable rules and verify:

- text scaling / Dynamic Type or web zoom behavior
- keyboard access and logical focus order
- VoiceOver/screen-reader names, roles, values, and state changes
- target size and spacing
- contrast and non-color state communication
- Reduce Motion behavior
- Reduce Transparency behavior
- sufficient cues for hover-independent/touch use
- focus visibility
- error identification and recovery
- content order that remains meaningful without visual positioning

For native Apple platforms, use system semantic colors, text styles, controls, and accessibility APIs where possible instead of reproducing them manually.

## Input-model differences

### Pointer/keyboard
Desktop interfaces may reveal secondary actions on hover, support precise targets, context menus, multi-selection, shortcuts, drag/drop, and dense tables. Important actions must still be discoverable without accidental hover dependence.

### Touch
Increase target generosity, avoid hover-only discovery, and make gesture-only actions discoverable or provide an alternate path where required.

### Focus/remote
For tvOS and similar focus systems, selection/focus movement is the navigation model. Pointer assumptions do not transfer.

### Eyes/hands
For visionOS, follow platform-specific HIG guidance rather than translating touch targets literally.

## System component preference

Before creating a custom interactive primitive on an Apple platform:

1. search `apple-hig/references/framework-index.md`
2. inspect the relevant HIG component/rules
3. check `api-map.md` for implementation symbols
4. use the system primitive unless the product has a concrete requirement it cannot satisfy

If custom behavior is justified, record why and identify which native states/semantics must be reproduced.

A custom component is not more Apple-like merely because it visually resembles one.

## Completion evidence

The design review should be able to answer:

- Which states were tested?
- Which accessibility settings change the result?
- Can the core task be completed by keyboard where the platform expects it?
- Is state conveyed without relying on color alone?
- Which custom controls exist, and why were system controls insufficient?

If these answers are unknown, visual polish is premature.