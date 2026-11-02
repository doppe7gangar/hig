# Adaptive architecture

Responsive design is not merely smaller CSS. Preserve the product hierarchy while changing the architecture to fit width, input, and platform.

## Design transformations

Prefer explicit transformations over compression:

- **sidebar workspace → compact navigation** when persistent width becomes too expensive
- **list-detail → sequential navigation** on narrow screens
- **inspector → popover or sheet** when a third pane would crowd the work
- **multi-column → prioritized single column** rather than stacking every region unchanged
- **dense table → prioritized rows/details** when columns cannot remain legible
- **persistent toolbar → condensed/contextual controls** when width is limited
- **hover-revealed action → explicit discoverable action** on touch
- **pointer precision → larger touch target** when crossing to touch-first contexts
- **parallel panes → drill-in flow** when simultaneity no longer helps

Do not preserve desktop simultaneity by shrinking every pane until none is usable.

## Required adaptive plan

For every major screen, record:

- wide/default composition
- compact composition
- what disappears
- what moves
- what becomes sequential
- what becomes contextual
- how the primary action remains discoverable
- how state/selection survives the transformation

For cross-platform products, distinguish responsive width changes from actual platform changes. An iPad is not simply a 1024px browser and a Mac window is not simply a wide iPhone.

## Breakpoint principle

Choose breakpoints from **content pressure**, not device folklore. A layout should transform when relationships become crowded, labels truncate, touch targets collide, or the primary region loses dominance.

## Review questions

- Does the primary content remain primary at every tested width?
- Is anything merely squeezed that should have transformed?
- Are controls duplicated after a transformation?
- Does selection remain understandable when panes become sequential?
- Are keyboard/pointer affordances replaced appropriately for touch?
- Does compact mode preserve the user's place and task context?

## Visual review matrix

At minimum, rendered review should inspect:

- phone/compact width
- tablet/intermediate width
- desktop/wide width
- light and dark appearances where supported

Platform-native work should add platform-specific size classes or window states when meaningful.

A responsive implementation that technically fits but destroys the information relationship has failed the design.