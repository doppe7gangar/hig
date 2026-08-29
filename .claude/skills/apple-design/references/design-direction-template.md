# Design direction template

Use this structure to replace/expand the scaffolded `DESIGN.md` before visual polish.

# Design direction

## Product character

- Dominant:
- Supporting (optional):

## Platform constraints

- Target platform(s):
- Input model(s):
- Window/viewport model:
- HIG/platform-diff evidence checked:
- Patterns ruled out by platform fit:

## Information hierarchy

1. **Primary:**
2. **Secondary:**
3. **Tertiary:**
4. **Contextual:**

## Content model

| Content | User question/task | Decision enabled | Content shape | Required context |
|---|---|---|---|---|
| | | | | |

## Representation decisions

| Content | Representation | Why this representation | Failure/misreading risk |
|---|---|---|---|
| | | | |

If a chart is used, record its analytical question, unit, comparison/baseline, time/population window, and missing-data behavior.

## Content stress cases

- 
- 
- 

## State continuity

- **Invariant design idea:**
- **Loading:**
- **Empty:**
- **Error:**
- **Offline / not-enough-data / stale (if applicable):**

## Design invariants

- 
- 
- 

## Candidate directions

Each credible candidate must differ structurally, not cosmetically. Name at least two structural differences.

### Direction: A — <short name>
- **Frame:** standalone app
- **Model:**
- **Design idea:**
- **Primary region:**
- **Secondary/contextual regions:**
- **Persistent chrome:**
- **Compact transformation:**
- **Strength:**
- **Risk:**
- **Structural differences:** ______; ______

### Direction: B — <short name>
- **Frame:** the conversation — it lives in the thread
- **Model:**
- **Design idea:**
- **Primary region:**
- **Secondary/contextual regions:**
- **Persistent chrome:**
- **Compact transformation:**
- **Strength:**
- **Risk:**
- **Structural differences:** ______; ______

### Direction: C — <short name> (when credible)
- **Frame:** a glanceable surface — a widget on the Home Screen
- **Model:**
- **Design idea:**
- **Primary region:**
- **Secondary/contextual regions:**
- **Persistent chrome:**
- **Compact transformation:**
- **Strength:**
- **Risk:**
- **Structural differences:** ______; ______

## Direction comparison

| Criterion | Direction A | Direction B | Direction C (if used) |
|---|---:|---:|---:|
| Primary-task fit | | | |
| Hierarchy clarity | | | |
| Information relationship | | | |
| Platform fit | | | |
| Adaptivity | | | |
| Restraint | | | |
| Distinctiveness through product logic | | | |

**Trade-off interpretation:**

## Rejected directions

- Rejected ______ because ______; the consequence would be ______.
- Rejected ______ because ______; the consequence would be ______.

## Chosen direction

> We chose ______ because the user's recurring task is ______. It keeps ______ primary, makes ______ available without competing for attention, and transforms to ______ when space/input changes.

## Reference synthesis

- Reference relationship 1:
- Reference relationship 2:
- Reference relationship 3:
- What must not transfer from the references:

## Adaptive architecture

### Wide/default
- 

### Compact/narrow
- 

### Transformation
- disappears:
- becomes sequential:
- becomes contextual:
- selection/context preservation:
- pointer/keyboard → touch changes:

## Primary interaction flow

| Stage | User action | System response | State/context preserved | Failure/recovery |
|---|---|---|---|---|
| Entry | | | | |
| Act | | | | |
| Commit | | | | |
| Exit/continue | | | | |

## Commit model

- **Frame:** standalone app
- **Model:** immediate / explicit / autosave-continuous
- **When the change becomes real:**
- **Undo/cancel/reversal policy:**
- **Dirty/saving/saved state if applicable:**
- **Post-completion focus/selection/context:**

## Recovery and interruption

- **Failure condition:**
- **Interruption/resumption case:**
- **What is preserved:**
- **Retry/rollback/restore behavior:**
- **Conflict/stale-data handling if applicable:**

## Interaction stress cases

- 
- 
- 

## Keyboard and alternate input

- **Keyboard/command path where expected:**
- **Escape/cancel and Return/commit semantics:**
- **Focus restoration:**
- **Touch/pointer alternative:**
- **Drag/drop path and non-drag alternative if applicable:**

## Product coherence contract

- **Typography roles:**
- **Spacing rhythm:**
- **Surface/material roles:**
- **Action placement:**
- **Navigation/selection semantics:**
- **Terminology/icon semantics:**
- **Shared interaction contracts:**

## Screen-family coherence matrix

| Screen/family | Primary object/task | Title role | Primary action location | Navigation level | Selection model | Density | Surface/material notes |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |

## Intentional differences

- ______ differs from ______ because ______; this difference supports ______.

## Cross-screen transition audit

| Transition | What stays stable | What changes intentionally | Context/focus preservation | Terminology/action continuity |
|---|---|---|---|---|
| | | | | |
| | | | | |

## Coherence drift review

- 
- 

Check typography roles, spacing rhythm, radii/surfaces, action placement, navigation semantics, terminology/icons, commit/recovery conventions, density, states, and responsive variants for unexplained drift.

## Interaction states

| Component/pattern | Applicable states | Evidence/test |
|---|---|---|
| | | |

## Accessibility

- text scaling / Dynamic Type / zoom:
- keyboard/focus order:
- VoiceOver/screen-reader semantics:
- target size/spacing:
- contrast/non-color state:
- Reduce Motion:
- Reduce Transparency:
- error recovery:

## System component decisions

| Need | System component/API considered | Decision / reason |
|---|---|---|
| | | |

## Reduction pass

- container removed/demoted:
- persistent control made contextual:
- redundant label removed:
- decorative material/effect removed:
- hierarchy strengthened after reduction:

## Final design idea

One concrete sentence describing what owns the screen and what recedes.