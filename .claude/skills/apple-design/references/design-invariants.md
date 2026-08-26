# Design invariants

Design invariants are the product relationships that must survive implementation, responsive changes, state changes, and visual polish.

Record 3–5 invariants in `DESIGN.md` before implementation.

Good invariants are structural and testable:

- the document remains the dominant surface; controls never become the composition
- only the selected object exposes destructive actions
- today's status is always the first read on the overview
- the collection remains navigation; details do not leak into every row
- brand color identifies action/selection, not decoration
- the sidebar is navigation, never a container for unrelated status cards
- compact mode preserves the selected object's context when panes become sequential

Weak invariants are aesthetic adjectives:

- clean
- premium
- modern
- Apple-like
- minimal

## Use during review

For every meaningful revision ask:

1. Does this preserve all invariants?
2. If an invariant changed, did the product understanding change or did implementation drift?
3. Does responsive/compact mode preserve the same hierarchy even when the spatial arrangement changes?
4. Do loading, empty, error, selected, and disabled states preserve the product character and primary relationship?

## Breaking an invariant

An invariant may be changed deliberately. Record:

- previous invariant
- evidence that made it wrong
- replacement invariant
- screens/states affected

Do not silently let implementation convenience rewrite the design direction.

## Completion test

A finished review should cite evidence for each invariant from the rendered screens or interaction behavior. If an invariant cannot be observed or tested, rewrite it to be more concrete.