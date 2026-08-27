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

## Design invariants

- 
- 
- 

## Candidate directions

Each credible candidate must differ structurally, not cosmetically. The `Structural differences` field must name at least two differences from the other candidates, such as pane structure, navigation, persistent chrome, sequence/simultaneity, density, or primary-action placement.

### Direction: A — <short name>

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

Score 1–5 to expose trade-offs, not to mechanically choose the highest total.

| Criterion | Direction A | Direction B | Direction C (if used) |
|---|---:|---:|---:|
| Primary-task fit | | | |
| Hierarchy clarity | | | |
| Information relationship | | | |
| Platform fit | | | |
| Adaptivity | | | |
| Restraint | | | |
| Distinctiveness through product logic | | | |

**Trade-off interpretation:** Explain what the scores reveal, which weakness matters most for this product, and why the final decision is not simply “highest total wins.”

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