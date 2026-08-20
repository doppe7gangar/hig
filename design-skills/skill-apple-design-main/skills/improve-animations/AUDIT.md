# Animation Audit Playbook

The eight audit categories and exact target values.

## 1. Purpose & frequency

| Frequency | Decision |
| --- | --- |
| 100+/day | No animation |
| Tens/day | Remove or reduce |
| Occasional | Standard |
| Rare/first-time | Can add delight |

## 2. Easing & duration

```css
--ease-out: cubic-bezier(0.23, 1, 0.32, 1);
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);
```

**UI animations stay under 300ms.**

## 3. Physicality & origin

- Never `scale(0)` — target `scale(0.9–0.97)` + `opacity: 0`
- Popovers scale from trigger, not center (modals exempt)
- Button press: `scale(0.97)`, `transition: transform 160ms ease-out`

## 4. Interruptibility

- Transitions retarget; keyframes restart from zero
- `@starting-style` for entry without JS
- Apple spring: `{ type: "spring", duration: 0.5, bounce: 0.2 }`
- Asymmetric timing: deliberate phases slower, responses snap

## 5. Performance

- `transform` and `opacity` only
- `transition: all` always a finding
- Framer Motion shorthands NOT hardware-accelerated
- CSS/WAAPI beat rAF under load

## 6. Accessibility

```css
@media (prefers-reduced-motion: reduce) {
  .element { animation: fade 0.2s ease; }
}
```

## 7. Cohesion & tokens

Match motion to personality. Shared tokens, not duplicated easings.

## 8. Missed opportunities

State teleports, missing spatial story, un-used delight budget.
