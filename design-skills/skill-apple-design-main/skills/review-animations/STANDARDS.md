# Animation Standards Reference

The precise values, curves, and rules behind the review.

## Easing

```css
--ease-out: cubic-bezier(0.23, 1, 0.32, 1);
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);
```

## Duration

| Element | Duration |
| --- | --- |
| Button press | 100–160ms |
| Tooltips | 125–200ms |
| Dropdowns | 150–250ms |
| Modals/drawers | 200–500ms |

## Springs

```js
{ type: "spring", duration: 0.5, bounce: 0.2 }
{ type: "spring", mass: 1, stiffness: 100, damping: 10 }
```

## Performance

- `transform` and `opacity` only
- Framer Motion shorthands NOT hardware-accelerated
- CSS animations beat JS under load
- WAAPI for programmatic CSS

## Gestures

- Momentum: dismiss on `velocity > ~0.11`
- Damping at boundaries
- Pointer capture for drag
- Multi-touch protection
- Friction over hard stops

## Accessibility

```css
@media (prefers-reduced-motion: reduce) {
  .element { animation: fade 0.2s ease; }
}
@media (hover: hover) and (pointer: fine) {
  .element:hover { transform: scale(1.05); }
}
```
