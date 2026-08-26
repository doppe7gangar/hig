# Visual critique and reduction

Use this after a first composition exists and before calling the design finished. `check_design.py` handles mechanical correctness; this file asks whether the design actually works as a designed product.

Every important finding must use this form:

> **Evidence → consequence → correction**

Example:

> Five equal metric tiles compete for first attention → current status cannot be read quickly → promote SLA health to the dominant metric and move the other four into supporting evidence.

“Feels off” is not a complete finding.

## 1. Two-second hierarchy test

Within two seconds, identify:

1. what this place is
2. what matters most right now
3. the primary action, if one exists

If several regions compete for first attention, hierarchy is unresolved.

## 2. Invariant audit

Read `DESIGN.md` and `references/design-invariants.md`.

For every recorded invariant, identify visible/behavioral evidence that it survived implementation. If a revision breaks an invariant, either fix the implementation or explicitly revise the invariant with evidence.

## 3. Information before styling

Describe the screen without visual vocabulary. State primary, secondary, tertiary, and contextual information. If this is unclear, color/radius/shadow work is premature.

## 4. Composition

Ask why each region is where it is.

Warning signs:

- equal columns for unequal information
- grids used merely because several things exist
- sidebar destinations rarely switched
- equal-weight dashboard metrics
- detail screens split into unrelated cards
- controls becoming the composition instead of supporting it
- desktop simultaneity squeezed unchanged onto mobile
- mobile chrome enlarged onto desktop

Compare the result against the winning and rejected directions in `DESIGN.md`. If the implementation drifted toward a rejected generic pattern, return to composition.

## 5. Container audit

For every card, panel, border, tinted background, or floating surface, identify the boundary it communicates.

Valid reasons include:

- separate interaction region
- material/elevation layer
- semantic grouping spacing alone cannot express
- selected/focused object
- modal/transient surface

“Because it looked empty” is not valid.

Remove the container mentally while preserving alignment and spacing. If grouping remains obvious, remove it.

## 6. Typography audit

Imagine borders/backgrounds removed. Can typography still reveal the reading order?

Check:

- one unmistakable first read
- meaningful rather than tiny size differences
- intentional weight
- secondary text that actually recedes
- appropriate line length
- no redundant labels where context already explains meaning

## 7. Density audit

Density is a product/platform decision.

Higher density can suit expert tools, tables, inspectors, inboxes, editing environments, and repeated operations. Lower density can suit onboarding, focus tasks, media, consumer summaries, and editorial storytelling.

Do not make a desktop professional tool spacious merely to look premium. Do not make a touch-first consumer screen dense merely to fit more.

## 8. Chrome audit

Inventory persistent navigation, toolbar, filters, actions, tabs, inspectors, and status controls.

Ask whether each must remain visible during the core task. Move infrequent/object-specific actions into contextual menus, inspectors, selection states, or disclosure where appropriate.

## 9. Adaptive architecture audit

Read `references/adaptivity.md`.

At compact, intermediate, and wide widths, verify that architecture transforms rather than merely shrinks.

Check:

- primary content remains primary
- list-detail becomes sequential when needed
- inspectors become contextual where width is insufficient
- tables prioritize instead of crushing columns
- persistent controls condense without duplication
- selection/context survives pane collapse
- pointer-only discovery gains a touch-appropriate path

## 10. Interaction-state audit

Read `references/interaction-accessibility.md`.

Inspect applicable states: hover, keyboard focus, pressed, selected, disabled, editing, expanded/open, loading/submitting, drag/drop, destructive/undo, and inactive-window where relevant.

A correct default state with missing selected/disabled/focus behavior is not a complete component.

## 11. Accessibility audit

Verify applicable HIG guidance for:

- text scaling/Dynamic Type or browser zoom
- keyboard navigation and focus order
- VoiceOver/screen-reader semantics
- target size/spacing
- contrast and non-color communication
- Reduce Motion
- Reduce Transparency
- focus visibility
- error identification/recovery

Accessibility findings use the same evidence → consequence → correction format.

## 12. Material audit

For every blur, translucency, shadow, vibrancy, or elevated surface ask:

- what layer is this on?
- what is beneath it?
- why must that relationship remain perceptible?

No meaningful answer means simplify.

## 13. Color audit

Color should identify action, state, selection, brand, or data meaning. It should not rescue weak hierarchy.

Imagine grayscale. Most hierarchy should survive.

## 14. System-component audit

For native Apple work, identify custom controls and verify that `apple-hig/references/framework-index.md` and `api-map.md` were checked first.

If a system primitive exists, custom recreation needs a recorded product requirement. Visual similarity alone is not justification.

## 15. Platform authenticity and platform-specific smells

### iPhone

Check content priority, touch ergonomics, safe-area/navigation logic, and whether tabs are truly peer-level.

Smells:
- desktop sidebars squeezed into phone width
- tiny dense controls
- persistent inspectors
- gesture-only actions with no discoverability

### iPad

Check whether width is used for meaningful relationships rather than simple enlargement.

Smells:
- giant iPhone layout
- unused width around a single narrow column when simultaneous context would help
- desktop panes copied without touch/input adaptation

### macOS

HIG remains authoritative even without a measured macOS visual kit.

Check keyboard, pointer, window resizing, sidebars, toolbars, tables, menus, context menus, inspectors, multiwindow behavior, focus/selection, and system components where relevant.

Smells:
- oversized touch controls
- giant mobile-style titles
- excessive whitespace in repeated expert workflows
- bottom-tab navigation imported from iPhone
- mobile sheets used for ordinary desktop choices
- no keyboard commands for frequent actions
- cards replacing tables/list-detail relationships
- missing hover/focus/inactive-window states where relevant

### Web app

Check browser semantics, keyboard/pointer behavior, responsive structure, and whether Apple principles transfer without copied iOS furniture.

Smells:
- phone-like tab bars on desktop
- excessive glass/cards as the main design language
- mobile-sized controls everywhere
- custom pseudo-native controls that harm web expectations

### Marketing

Check narrative progression: claim → proof → demonstration → differentiation → action.

Smells:
- hero → three cards → three cards → testimonials → CTA by default
- repeated centered headings with icon-card grids
- decorative product mockups without evidence or story progression

## Anti-AI visual smell

Redesign when several appear together:

- every region has a radius/background
- many pills
- gradient blobs
- glass everywhere
- feature-card grids
- icon badges on every heading
- repeated centered-heading + three-card sections
- shadows without elevation meaning
- decorative status dots
- equal metric tiles
- excessive whitespace without stronger hierarchy
- tiny gray helper text everywhere
- multiple primary-looking actions

These devices are not banned. Accidental repetition is the problem.

## Reduction sequence

1. Remove decorative effects.
2. Remove unnecessary containers.
3. Remove redundant labels.
4. Demote secondary actions.
5. Collapse contextual controls.
6. Re-evaluate spacing.
7. Strengthen typography only where hierarchy became unclear.
8. Reintroduce surfaces/separators only where relationships need them.

Reduction is not sparsity. It removes things that do not explain, enable, or orient.

## Final review statement

End the review with:

- **Design idea:** one sentence
- **Strongest evidence:** what in the rendered result proves it
- **Largest remaining risk:** one concrete weakness
- **Correction made:** the most meaningful change caused by review
- **Invariant status:** which invariants were confirmed or revised

If the design idea is merely “clean,” “modern,” “Apple-like,” or “sidebar and cards,” return to composition.