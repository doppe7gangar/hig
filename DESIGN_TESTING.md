# Testing the apple-design workflow

The design skill now has three different quality gates:

1. **direction evidence** — platform routing, hierarchy, invariants, divergence, adaptivity, interaction/accessibility, system-component decisions
2. **mechanical correctness** — files, tokens, states, contrast, overflow, targets, browser errors
3. **rendered visual judgment** — hierarchy, composition, density, restraint, platform fit, and reduction

Do not substitute one for another.

## 1. Smoke-test deterministic infrastructure

```bash
python3 scripts/eval/design_workflow_smoke.py
```

It checks reference retrieval, emitted spatial models, scaffold output, and `check_design.py --no-browser` without calling a model.

To include screenshot rendering:

```bash
python3 scripts/eval/design_workflow_smoke.py --browser
```

## 2. Test platform-aware reference selection

### iOS / measured visual evidence

```bash
python3 .claude/skills/apple-design/select_references.py \
  --query "plant watering list detail add edit" \
  --model stack --platform ios \
  -o /tmp/REFERENCES-ios.md
```

Expected: HIG provenance plus real `apple-hig/assets/ui-kit/` image paths.

### macOS / HIG-first, no fake measured Mac visuals

```bash
python3 .claude/skills/apple-design/select_references.py \
  --query "mail sidebar toolbar search list detail menus" \
  --model list-detail --platform macos \
  -o /tmp/REFERENCES-macos.md
```

Expected:

- relevant HIG/component vocabulary
- an explicit statement that no measured macOS visual corpus is registered
- **no claim that iOS screenshots are measured macOS appearance**
- pointers to platform differences, rules, framework index, and API map

The selector is retrieval only. A design run still has to inspect available evidence and synthesize relationships.

## 3. Complete the design-direction evidence

Use `references/design-direction-template.md` to expand/replace the scaffolded `DESIGN.md`.

Then run:

```bash
python3 .claude/skills/apple-design/check_direction.py ./design
```

It should fail until `DESIGN.md` contains:

- platform constraints
- real information hierarchy
- at least three design invariants
- candidate directions
- product-specific rejection rationale
- chosen direction
- adaptive architecture
- interaction-state plan
- accessibility plan
- system-component decisions

Do not treat a mechanically valid project with a placeholder `DESIGN.md` as designed.

## 4. Test one complete product

Example:

```bash
python3 .claude/skills/apple-design/new_project.py \
  --name Pulse --brand "#5A67D8" \
  --kind web --model dashboard --character dense \
  --screens "Overview,Reports,Settings" \
  -o /tmp/pulse-design
```

Fill `DESIGN.md`, select/inspect references, then recompose the starter page around the actual hierarchy.

Direction gate:

```bash
python3 .claude/skills/apple-design/check_direction.py /tmp/pulse-design
```

Mechanical gate:

```bash
python3 .claude/skills/apple-design/check_design.py /tmp/pulse-design
```

Rendered review:

```bash
python3 .claude/skills/apple-design/render_review.py /tmp/pulse-design
```

Inspect every image under `.visual-review/`. Write findings as:

**evidence → consequence → correction**

Fill `VISUAL_REVIEW.md`, revise, rerender when needed, replace every `[PENDING]`, set status to `COMPLETE`, then:

```bash
python3 .claude/skills/apple-design/render_review.py /tmp/pulse-design --check
```

## 5. What to inspect in screenshots

Use `references/visual-critique.md` and verify:

- two-second reading hierarchy
- design invariants survived implementation
- winning direction did not drift into a rejected generic pattern
- unnecessary containers/persistent chrome were reduced
- typography carries hierarchy without boxes
- density fits platform/task
- compact/wide layouts transform architecturally rather than merely shrink
- applicable hover/focus/pressed/selected/disabled/editing states exist
- accessibility settings and keyboard/focus behavior were considered
- system components were preferred on Apple platforms unless custom behavior is justified
- blur/shadow/glass describe real layers
- platform-specific anti-patterns are absent
- empty/error states preserve the product character

DOM signals in `VISUAL_REVIEW.md` are warnings only; screenshots are the evidence.

## 6. Run the cross-product quality benchmark

The benchmark suite covers 15 unlike products and is designed to catch structural sameness:

```bash
python3 scripts/eval/design_quality_eval.py
```

Or run a smaller subset:

```bash
python3 scripts/eval/design_quality_eval.py analytics mail landing plants
```

It calls the design agent, runs both `check_direction.py` and `check_design.py --no-browser`, records basic structural metrics, and warns when unrelated products collapse toward the same composition.

The benchmark criteria live in:

```text
.claude/skills/apple-design/references/benchmark-suite.md
```

A suite where every build is mechanically valid but every product uses the same sidebar/card architecture is a failed design system.

## 7. Platform boundary

The current measured visual ground truth is the **iOS 27** UI-kit corpus.

- iOS/iPadOS: measured visuals + HIG where applicable
- macOS: **HIG/platform/system APIs are still authoritative**; measured Mac appearance is simply not yet registered
- web/marketing: iOS visual corpus can be comparative evidence, never a native web specification
- future platform corpora plug into `select_references.py`'s `CORPORA` registry without changing the workflow

No visual kit available never means “design from generic instinct.”