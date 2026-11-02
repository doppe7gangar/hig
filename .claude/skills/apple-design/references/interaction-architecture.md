# Interaction architecture

Use this after the spatial model and content model are known, before visual polish.

Component states answer **how one control behaves**. Interaction architecture answers **how a person completes work across controls, views, states, interruptions, and recovery**.

A polished static mockup is not a finished product if the task flow is unresolved.

## Model the core loop

For each primary task, record:

1. **Entry** — how the person arrives at the task.
2. **Orientation** — what tells them where they are and what is selected/current.
3. **Action** — the direct manipulation, command, form, gesture, or choice.
4. **System response** — immediate feedback, optimistic update, progress, or transition.
5. **Commit point** — when the change becomes real/persistent.
6. **Recovery** — undo, cancel, retry, restore, or safe fallback.
7. **Exit/continuation** — where focus/selection/context goes next.

The loop should preserve context unless the task itself requires a reset.

## Selection is state, not decoration

For products with selectable objects, define:

- single vs multi-selection
- default selection on entry
- whether selection survives refresh/filter/navigation
- what happens when the selected item disappears
- what actions become available with selection
- keyboard/pointer/touch selection paths
- whether selection and focus are visually distinct where the platform requires it

Do not use selection tint merely as styling. It represents an object relationship.

## Editing and commit semantics

Every edit flow must choose a commit model deliberately:

### Immediate
Use when changes are lightweight, reversible, and expected to apply as they are made.

Examples: many settings, sorting, filtering.

Need: visible state change and undo/reversal where appropriate.

### Explicit commit
Use when the person is constructing a meaningful unit of work or validation spans multiple fields.

Examples: compose, complex form, document metadata batch edit.

Need: dirty state, save/submit affordance, cancel behavior, validation timing, unsaved-change policy.

### Continuous/autosave
Use when work is ongoing and explicit save would interrupt flow.

Examples: documents, notes, editors.

Need: save status, failure/retry behavior, conflict policy, offline behavior, and confidence that leaving the view is safe.

Do not mix models accidentally. A form that updates immediately but still has a Save button communicates two incompatible contracts.

## Destructive actions

For each destructive path classify:

- reversible vs irreversible
- common vs uncommon
- local vs broad scope
- immediate consequence vs delayed consequence

Prefer undo for common reversible actions. Confirmation should be reserved for cases where platform/HIG guidance and consequence justify interruption.

Record:

- trigger
- confirmation if any
- destructive styling
- post-action feedback
- undo window or recovery path
- what receives focus/selection afterward

## Async and optimistic work

For networked or long-running actions define:

- what changes immediately
- what remains interactive
- progress indication
- duplicate-submit prevention
- cancellation if meaningful
- success feedback
- partial failure behavior
- retry behavior
- stale-data handling
- conflict handling

Optimistic UI must have a rollback story. A spinner must not erase useful context if work can continue around it.

## Interruption and resumption

Consider realistic interruptions:

- navigation away mid-edit
- app/window loses focus
- sheet/popover dismissed
- incoming data invalidates current selection
- network drops
- app/background suspension on mobile
- another window edits the same object
- permissions denied mid-flow

Record what is preserved, what is discarded, what is confirmed, and how the user resumes.

A good flow lets the person answer: **Did my work save, and where am I now?**

## Keyboard and command architecture

On platforms where keyboard use is expected, define more than Tab order.

Consider:

- primary command shortcuts
- command discoverability in menus/help
- Return/Enter semantics
- Escape/cancel semantics
- arrow-key movement where conventional
- selection extension/modifier behavior
- delete/backspace behavior
- command availability by state
- focus restoration after modal/transient UI

A shortcut is not a replacement for a visible path. It is an additional efficient path.

## Drag and drop

Where drag/drop is useful, define:

- draggable object
- valid targets
- invalid target feedback
- copy vs move semantics
- insertion/reordering position
- autoscroll if needed
- keyboard/non-drag alternative
- drop success/failure feedback
- undo where appropriate

Do not add drag because it feels desktop-like; it must shorten a real task.

## Modal/transient architecture

For sheet, popover, alert, menu, context menu, or full-screen modal, define:

- why the task is transient rather than part of the main hierarchy
- what context remains visible
- dismissal paths
- commit/cancel semantics
- focus restoration
- whether reopening restores prior transient state

Use `apple-hig` to choose the correct presentation on Apple platforms.

## Flow stress cases

At minimum test the core task under three of these where applicable:

- double activation / repeated submit
- change selection while action is pending
- navigate away with unsaved changes
- action succeeds after the view is gone
- action fails after optimistic UI changed
- selected object deleted remotely
- stale data / conflict
- permission denial
- offline then reconnect
- undo after changing selection
- keyboard-only completion
- touch-only completion
- modal dismissed without committing

The goal is not to enumerate every edge case. It is to expose where the interaction contract is ambiguous.

## Record in DESIGN.md

For at least one primary flow include:

| Stage | User action | System response | State/context preserved | Failure/recovery |
|---|---|---|---|---|
| Entry | | | | |
| Act | | | | |
| Commit | | | | |
| Exit/continue | | | | |

Also record:

- commit model: immediate / explicit / autosave
- undo/cancel policy
- interruption/resumption behavior
- keyboard/command path where applicable
- drag/drop path where applicable
- focus/selection destination after completion

## Quality test

A flow is unresolved if any of these questions have no answer:

- When exactly does the change become real?
- Can the person reverse or cancel it?
- What happens if it fails halfway through?
- What happens to selection/focus afterward?
- Can the person safely leave and come back?
- Is there an alternate input path where the platform expects one?

Interaction architecture should make the product feel dependable, not merely animated.