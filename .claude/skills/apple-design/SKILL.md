---
name: apple-design
description: Design or redesign a whole product with Apple-level hierarchy, restraint, composition, and platform awareness. Use for apps, websites, dashboards, SaaS, product surfaces, and cross-platform interfaces when the task is broader than a single component. This skill acts as the design director: it determines product character, information architecture, visual hierarchy, competing spatial directions, reference set, composition, reduction, and platform authenticity before delegating exact rules to apple-hig, exact craft values to apple-ui-kit, and motion to apple-motion. Use when a design technically works but still feels generic, card-heavy, overly decorative, or insufficiently Apple-like.
---

# Apple Design Director

This skill decides what the product should feel like before it decides what components to place.

The other Apple skills are specialists:

- `apple-hig` answers platform and behavior questions.
- `apple-ui-kit` provides exact visual values and implementation recipes.
- `apple-motion` handles interaction physics and animation.
- This skill owns **art direction, composition, hierarchy, product shape, divergence, reference selection, reduction, and visual critique**.

A design can be perfectly wired, accessible, tokenized, and still look generic. This skill exists to prevent that.

## Governing principle

**Do not begin by placing components. Begin by composing information.**

Components are the final expression of hierarchy, not the starting point. Before introducing a card, panel, border, background, toolbar, floating control, or decorative effect, determine whether hierarchy can instead be communicated through position, alignment, spacing, typography, scale, grouping, progressive disclosure, motion, or context.

**If the interface still works after removing a container, remove it.**

## Workflow

Follow this order. Do not skip ahead to code or components.

### 1. Understand the product

Establish the primary user, primary job, most important recurring task, most important information on the primary screen, what must be instantly visible, what is secondary, and what can remain contextual or hidden.

If the brief is broad, infer a sensible product model rather than asking the user to make routine design decisions for you.

### 2. Classify the platform context

**Native Apple platform.** For iOS, iPadOS, macOS, watchOS, tvOS, or visionOS. Apple conventions strongly govern navigation, controls, modality, density, input, and interaction. Use `apple-hig` heavily.

**Web product with Apple sensibility.** For SaaS, dashboards, tools, web apps, account areas, and browser software. Borrow clarity, hierarchy, restraint, progressive disclosure, typography, spatial consistency, material discipline, and motion without dressing the product in iOS chrome.

**Marketing / editorial web.** The HIG is not the visual template. Use editorial discipline: strong typography, deliberate pacing, restrained color, clear narrative hierarchy, purposeful space, and carefully staged media.

**Cross-platform.** Preserve information architecture and product logic while adapting density, navigation, controls, and interaction to each platform.

### 3. Establish product character

Choose a dominant character and at most one supporting quality before styling: calm, dense, editorial, utilitarian, immersive, playful, professional, content-first, data-first, tool-like, or spatial.

Examples: finance dashboard = dense + calm; meditation = calm + immersive; developer tool = utilitarian + dense; photo editor = spatial + professional; product launch = editorial + immersive.

### 4. Build the information hierarchy

Rank contents as:

1. **Primary** — what the user came to see or do.
2. **Secondary** — context needed to understand or act on it.
3. **Tertiary** — supporting detail that can recede.
4. **Contextual** — controls or information shown only when relevant.

If everything is visually equal, the design has failed before styling begins.

Prefer stronger type instead of a box, spacing instead of a divider, alignment instead of a card, disclosure instead of persistent clutter, one dominant metric instead of equal metrics, and one clear action instead of competing CTAs.

### 5. Diverge before committing to a spatial model

Read both `references/spatial-models.md` and `references/design-divergence.md`.

Do not automatically accept the first plausible composition. For whole-product or major-screen work, consider three genuinely different structural directions when the brief permits it; use two when the architecture is strongly constrained. If only one direction is credible, record the constraint and one rejected counterfactual rather than inventing weak alternatives.

Candidate directions must differ structurally — for example dominant region, navigation model, pane relationship, persistent chrome, density, sequence vs simultaneity, or responsive transformation. Cosmetic variants do not count.

Score the candidates for primary-task fit, hierarchy clarity, information relationship, platform fit, adaptivity, restraint, and product-specific distinctiveness. Use the scores to expose trade-offs, not as an automatic winner calculation.

Explicitly reject the losing directions for product-specific reasons, then complete the commitment sentence in `references/design-divergence.md`.

The implemented starter models are:

- `workspace` — persistent destinations around sustained desktop work
- `list-detail` — collection → selection → detail
- `dashboard` — answer → context → evidence
- `document` — content/work surface → contextual tools
- `editorial` — marketing narrative
- iOS `stack` — hierarchical/task navigation
- iOS `tabs` — genuinely peer-level, frequently switched destinations

Other models remain valid even if the generator does not emit them: inspector, command surface, feed, immersive surface, dense table, multi-pane editor, or platform-specific macOS compositions.

**Never force the product into an available scaffold.** Use a scaffold for infrastructure and replace its composition if the real product model differs.

### 6. Select and inspect references

Do not design entirely from model memory when the repository already contains visual ground truth.

After drafting structural candidates, generate a small reference shortlist for the relevant task, components, states, and candidate models:

```bash
python3 select_references.py \
    --query "<primary task, components, states, navigation needs>" \
    --model <leading-spatial-model> -o ./design/REFERENCES.md
```

The selector retrieves relevant groups from `apple-hig/references/assets-index.md`, links them to HIG pages, and chooses a few contrasting visual states.

**Then inspect the actual images.** Do not infer appearance from filenames. For every useful reference, record relationships rather than adjectives:

- what reads first
- how content is grouped
- what chrome persists
- how selected/pressed/disabled states differ
- what material or tint communicates
- what should *not* transfer because the product context differs

Synthesize 3–5 relationships before composing. Good synthesis sounds like “selection is a quiet tint while content remains dominant,” not “clean Apple look.”

If reference evidence exposes a bad assumption in the leading candidate, revise the candidates before committing. References are evidence, not votes; never choose a model merely because an Apple screenshot resembles it.

The current measured visual corpus is iOS 27. For macOS-first work, use `apple-hig` for platform rules and do **not** present iOS imagery as measured macOS evidence. The reference layer is intentionally ready for a future macOS corpus.

### 7. Commit and compose before decorating

Record the winning direction, rejected alternatives, and commitment rationale in the project's `DESIGN.md` before polishing.

For each major screen decide the dominant region, secondary region, reading order, alignment system, density, content width, persistent chrome, contextual chrome, functional empty space, and what can disappear until needed.

Use the references as evidence for relationships, not as screenshots to clone.

Only after this should you select surfaces, controls, borders, blur, shadows, and motion.

## Apple restraint rules

Apple-like design is not “rounded + glass + minimal.” Avoid the common generative-UI aesthetic:

- card grids for unrelated information
- identical rounded rectangles around every section
- excessive pills
- floating containers everywhere
- decorative glass or blur
- oversized gradients
- gratuitous shadows
- center-aligned everything
- icon + title + paragraph feature cards by default
- giant headings unsupported by hierarchy
- duplicate primary actions
- unnecessary floating action buttons
- color compensating for weak hierarchy
- decorative motion

Use containers only when they communicate a real boundary, grouping, material layer, or interaction region.

## Platform authenticity

### iOS / iPadOS
Favor directness, touch ergonomics, clear navigation, strong content hierarchy, and progressive disclosure. Use tabs only when destinations are genuinely peer-level and frequently switched. **Do not infer tabs merely from a small destination count.** Verify platform rules in `apple-hig`.

### macOS
Allow higher information density. Prefer sidebars, toolbars, inspectors, tables, split views, popovers, contextual menus, and keyboard-friendly structure where the workflow demands them. Avoid inflating everything to mobile proportions.

The current scaffolder does not claim measured macOS chrome. If a product is macOS-first, use `apple-hig` for actual platform structure rather than pretending the iOS web kit is a macOS component library.

### Web apps
Respect browser expectations and desktop density. Apple principles transfer better than Apple chrome. Use persistent navigation, content grids, tables, command patterns, or sidebars when appropriate, but keep surfaces restrained.

### Marketing
Think in narrative sections, typographic pacing, product imagery, contrast, and sequence. Do not turn the page into a stack of app cards.

## Typography hierarchy

Typography should do more work than borders. Build a clear ladder using scale, weight, line-height, tracking, contrast, width, and grouping. The reading order should be understandable before interaction.

Use `apple-ui-kit` for exact native values where they apply. For marketing and web, preserve optical discipline rather than blindly reusing native text styles.

## Material discipline

Translucency, blur, vibrancy, and depth are functional materials. Use them to communicate floating chrome, hierarchy, separation, modality, depth, or focus.

A translucent surface must answer: **what is floating above what, and why?** If there is no answer, use a simpler surface.

## Motion discipline

Motion should communicate causality, continuity, spatial relationship, state change, or hierarchy. Use `apple-motion` for gesture-driven and spring-based interaction. Do not animate simply because the interface looks static.

## States are part of the design

Any data-driven screen must consider populated, loading, empty, and error. Empty has at least three meanings: first run, filtered to nothing, and deliberately cleared. Do not reuse the same empty-state copy for all three. Use `references/screens.md` for detailed state guidance.

## Reduction pass

Before implementation is considered complete, ask:

- Can any card be removed?
- Can any border become spacing?
- Can any persistent control become contextual?
- Can any label disappear because hierarchy already explains it?
- Are there competing primary actions?
- Is any blur or shadow decorative rather than structural?
- Are too many things visually equal?
- Is density appropriate to the platform?
- Is a mobile pattern being used on desktop without reason, or vice versa?
- Does the screen make sense in two seconds?

Remove unnecessary elements when they exist.

## Rendered visual review

A visual critique is not complete until the interface has been rendered and looked at.

First run the mechanical checker:

```bash
python3 check_design.py ./design
```

Then render the visual review matrix:

```bash
python3 render_review.py ./design
```

This captures:

- populated state at phone, tablet, and desktop widths
- light and dark appearance
- representative empty and error states
- DOM-derived warning signals for possible card, pill, shadow, blur, surface, centering, and overflow overuse

Those signals are **prompts, not aesthetic scores**. Open every screenshot in `.visual-review/` and inspect it directly. `render_review.py` writes `VISUAL_REVIEW.md` with required judgments covering hierarchy, composition, containers/chrome, typography/density, material/color, platform authenticity, states, reduction decisions, and the final design idea.

Read `references/visual-critique.md` while completing it.

After revising the design, rerender if the changes are visually material. Replace every `[PENDING]` judgment with evidence and set the review status to `COMPLETE`, then verify:

```bash
python3 render_review.py ./design --check
```

**Do not call the design visually reviewed or finished while this check fails.** A mechanical pass plus an uninspected screenshot directory is not a design review.

## Anti-pattern: generic card dashboard

Never default to:

`sidebar → page title → equal card grid → feature cards → more cards`

unless the information architecture genuinely requires it.

Prefer these narratives:

- dashboard: `primary answer → trend/context → supporting evidence → deeper detail`
- tool: `workspace → object/content → contextual controls`
- list: `collection → selection → detail`
- marketing: `claim → proof → demonstration → differentiation → action`

## Project tools

`new_project.py` is scaffolding, not art direction. Use it **after** product character, hierarchy, divergence, reference inspection, and spatial-model commitment are decided.

Web projects must name their model explicitly:

```bash
python3 new_project.py --name Clay --brand "#C1552E" \
    --kind web --model list-detail --character calm \
    --screens "Recipes,Plan,Settings" -o ./design
```

A summary/analytics product might instead use:

```bash
python3 new_project.py --name Pulse --brand "#5A67D8" \
    --kind web --model dashboard --character dense \
    --screens "Overview,Reports,Settings" -o ./design
```

For iOS, choose navigation deliberately rather than deriving it from destination count:

```bash
python3 new_project.py --name Clay --brand "#C1552E" \
    --kind ios --model stack --screens "Plan,Recipes,List,Settings" -o ./design
```

Use `--model tabs` only when the destination relationship justifies persistent tabs.

Marketing uses the editorial model automatically:

```bash
python3 new_project.py --name Clay --brand "#C1552E" \
    --kind marketing --character editorial --screens "Home" -o ./design
```

The generator writes `DESIGN.md`. Replace its hierarchy and rationale placeholders before polishing the generated interface, including the winning direction and rejected alternatives.

A complete project loop is:

```text
brief
→ product character + hierarchy
→ 2–3 structural directions
→ reference shortlist + inspection
→ compare / reject / commit to spatial model
→ new_project.py / composition
→ implementation + states
→ check_design.py
→ render_review.py
→ inspect screenshots
→ reduction / revision
→ rerender if needed
→ render_review.py --check
```

The generator handles infrastructure such as stylesheet order, vendored fonts, theme bridging, and reachable states. Do not let its starter markup dictate the final composition.

## Delegation

| Need | Skill |
|---|---|
| Product shape, hierarchy, divergence, composition, art direction, reference selection, critique | **apple-design** |
| Platform rules, behavior, accessibility, modality | **apple-hig** |
| Exact sizes, typography, radii, colors, tokens, CSS | **apple-ui-kit** |
| Gestures, springs, velocity, interruptibility, motion | **apple-motion** |

## Final design standard

A successful result feels Apple-like because it is clear, composed, restrained, responsive, spatially coherent, typographically disciplined, platform-aware, purposeful in motion, deliberately chosen over credible alternatives, and proven through rendered inspection — **not because it is covered in rounded glass.**