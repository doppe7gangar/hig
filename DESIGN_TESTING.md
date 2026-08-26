# Testing the apple-design workflow

The design skill has two different quality gates:

1. **mechanical correctness** — files, tokens, states, contrast, overflow, targets, browser errors
2. **visual judgment** — hierarchy, composition, density, restraint, platform fit, and reduction

Do not substitute one for the other.

## 1. Smoke-test the deterministic workflow

This does not call a model:

```bash
python3 scripts/eval/design_workflow_smoke.py
```

It checks that:

- `select_references.py` can retrieve HIG + visual provenance
- every emitted web model scaffolds: `workspace`, `list-detail`, `dashboard`, `document`
- iOS `stack` and `tabs` scaffold
- marketing emits the editorial model
- each scaffold writes `DESIGN.md`
- each scaffold passes `check_design.py --no-browser`

To include the screenshot/review path:

```bash
python3 scripts/eval/design_workflow_smoke.py --browser
```

That additionally confirms `render_review.py` can render screenshots and that a fresh review correctly **fails** `--check` while its judgments are still pending.

## 2. Test reference selection directly

```bash
python3 .claude/skills/apple-design/select_references.py \
  --query "support analytics dashboard filters search settings" \
  --model dashboard \
  -o /tmp/REFERENCES.md
```

The output should contain:

- a small component shortlist rather than the whole corpus
- HIG page provenance
- real `apple-hig/assets/ui-kit/` image paths
- multiple states where available
- a synthesis section

The selector is only retrieval. A design run still has to open the actual images and record relationships learned from them.

## 3. Test a whole design manually

Example:

```bash
python3 .claude/skills/apple-design/new_project.py \
  --name Pulse --brand "#5A67D8" \
  --kind web --model dashboard --character dense \
  --screens "Overview,Reports,Settings" \
  -o /tmp/pulse-design
```

Replace the placeholders in `DESIGN.md`, select and inspect references, then recompose the sample page around the actual hierarchy.

Run the mechanical gate:

```bash
python3 .claude/skills/apple-design/check_design.py /tmp/pulse-design
```

Then create the rendered review:

```bash
python3 .claude/skills/apple-design/render_review.py /tmp/pulse-design
```

Inspect every image under `.visual-review/`. Fill `VISUAL_REVIEW.md`, revise the interface, rerender when needed, replace every `[PENDING]`, and set the status to `COMPLETE`.

Finally:

```bash
python3 .claude/skills/apple-design/render_review.py /tmp/pulse-design --check
```

A design is not visually reviewed while this command fails.

## 4. What to inspect in the screenshots

Use `apple-design/references/visual-critique.md` and check, in order:

- the two-second reading hierarchy
- whether the spatial model still matches the real task
- unnecessary containers and persistent chrome
- typography without relying on boxes
- density at phone, tablet, and desktop widths
- blur/shadow/glass only where they describe a layer
- platform authenticity
- empty/error states retaining the same product character
- concrete reduction decisions after inspection

The DOM signals in `VISUAL_REVIEW.md` are warnings only. A high rounded-surface count can be legitimate; a low one does not make a design good. The screenshots are the evidence.

## 5. Reference boundary

The current visual ground truth is the **iOS 27** UI-kit corpus. It is valid evidence for iOS visual relationships and useful comparative evidence for Apple sensibility on the web.

It is **not** a measured macOS kit. For macOS-first work, use `apple-hig` for platform structure and behavior until a macOS visual corpus is added. The selector and review workflow are intentionally platform-extensible so that corpus can be added later without changing the design process.