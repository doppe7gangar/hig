---
name: apple-design
description: Design a whole product, not a component — the entry point for "I'm building an app/website/dashboard, help me design it". Scaffolds a working project with new_project.py (brand theme, vendored kit, real screens with every state), then checks it with check_design.py before it ships. Use at the start of any design project, when someone describes what they're building rather than asking about a specific control, when a project needs a design system or brand palette, when deciding what screens exist or how navigation should work, or when a build is missing its empty and error states. Covers websites and marketing pages as well as apps, and is explicit about where Apple's guidance stops applying. For a specific rule or spec use apple-hig; for exact iOS values and CSS use apple-ui-kit; for animation use apple-motion.
---

# Designing a product

The other three skills answer questions. This one starts projects.

They are reference-shaped — *is this button too small*, *what colour is
the accent*, *how should this animate*. Handed a brief instead —
*"a meal-planning app for families, web first, iOS later"* — none of them
fires, because a brief is not a lookup. This is the skill for that.

## Two commands

Everything below hangs off these. Run them from this skill's directory,
or give the full path to it.

```bash
python3 new_project.py --name Clay --brand "#C1552E" \
    --kind ios --screens "Plan,Recipes,List,Settings" -o ./design

python3 check_design.py ./design
```

**Use the scaffolder rather than assembling this by hand.** Not a style
preference — the setup has four pieces that each fail silently:
stylesheet order, the `--ios-*` bridge, vendored fonts, and the four
states. A hand-built page gets some of them and looks completely fine
without the rest. The scaffolder emits all four and the checker fails
the build if any regress. What is left for you is the design, which is
the part worth the attention.

## The order that matters

### 1. What kind of thing is this?

Decides how much of Apple's guidance applies at all, and it is the
`--kind` flag, so answer it before running anything.

| `--kind` | Apple's guidance | What actually governs it |
|---|---|---|
| `ios` | Fully. This is what the HIG is for. | `apple-hig` end to end |
| `web` (dashboard, tool, admin) | The *structure* transfers — navigation, modality, states, hit targets. The *chrome* mostly doesn't: a web app with an iOS tab bar looks like a costume. | `apple-hig` for structure, `apple-ui-kit` for craft |
| `marketing` | Barely. apple.com and iOS are different design languages; the HIG governs neither. | Editorial and typographic craft, not the HIG |
| `cross` (RN, Flutter) | Structure yes, appearance per platform. | `apple-ui-kit` exports, plus the platform's own rules |

The kinds produce deliberately different shapes. `marketing` gets no tab
bar, no grouped list, and a white ground rather than iOS's grouped grey
— a brand site built to iOS chrome is the commonest way this goes wrong,
and it is invisible until the whole thing looks like a Settings screen.

### 2. What screens exist, and how do they connect?

Before any visual decision. They become `--screens`.

- **How many top-level places?** Under five and they are tabs. More, and
  either they are not all top-level, or it is a sidebar. The scaffolder
  says so if you pass more than five. `apple-hig`'s `pages/tab-bars.md`
  and `pages/navigation-bars.md` carry the rules; `references/screens.md`
  here carries the shapes.
- **What is a detour rather than a destination?** Anything the person
  comes back from — compose, edit, a picker, settings — is a sheet, not
  a tab. Get this wrong and everything is a tab and nothing feels
  finished.

Four to six screens is a normal first version. If the list has fifteen,
the product is not scoped yet and no amount of design fixes that.

### 3. Scaffold it

`--brand` is the client's colour. Apple's blue belongs to Apple.

The generator derives a whole system from that one colour, keeping
Apple's *relationships* and replacing only the hue: the label ladder as
one grey at several opacities so text composites correctly on any
surface, translucent fills, the grouped-background pair, and a contrast
pass that emits a darkened variant where the brand colour cannot carry
text. Expect that last one — most saturated brands do not clear 4.5:1 on
white, Apple's own accent included at 3.52:1. Use the brand colour for
fills and `--brand-accent-text` for coloured text.

It also writes the `--ios-*` bridge, which is what lets
`apple-ui-kit`'s recipes render in the brand palette without being
rewritten. **Regenerate rather than hand-edit `theme.css`** — editing it
by hand is how the bridge gets lost, and the result is a brand palette
next to Apple-blue buttons.

### 4. Design — replace the content, keep the structure

The scaffold is scaffolding. The rows, the copy, the hierarchy, which
screen leads, what a row actually carries — that is the design, and it
is the whole job now that the plumbing is handled.

**Read `references/screens.md` before composing.** It has the shapes —
list-and-detail, settings, onboarding, dashboard, form, feed — and the
state sets. Working from memory here reliably produces the happy path
and nothing else.

The scaffold gives you first-run empty. **Filtered-to-nothing and
deliberately-cleared are different screens with different copy** — tell
someone with two hundred items to "add your first" and it reads as
broken. `references/screens.md` covers all three.

**The accent has two jobs and two values.** As a *fill* it needs 3:1
against the surface, and `--ios-accent` is tuned for that. As *text* --
a tinted button's label, a selected tab, a link, a chart legend -- it is
small text and needs 4.5:1, which the fill value usually misses. The
generator emits `--accent-text-safe` for exactly this. Every design
tested so far reached for `--ios-accent` and got a label at 3.05:1;
it is the single commonest contrast defect here, and it costs one
token to avoid.

Two things not to undo:

- **`theme.css` stays last** in the stylesheet order. Move it earlier
  and the component recipes overwrite the brand palette; the page still
  renders, in Apple's blue, which is why it needs saying.
- **Fonts stay vendored.** The kit ships them. Swap in a CDN link and it
  renders in Helvetica for anyone offline.

### 5. Check it

```bash
python3 check_design.py ./design
```

Nonzero means do not ship it. It catches what a screenshot cannot:
stylesheet order, the bridge surviving, remote resources, missing
states, dead local references, sideways overflow at phone width, hit
targets under Apple's floor, console errors, and what `--ios-accent`
actually resolved to in a browser.

Contrast is measured on the rendered page in **both appearances**, and
split in two. A run that Increased Contrast rescues is a warning, and
names the fact that Apple's own secondary label (3.44:1) and filled
buttons (~3.5:1) sit there too. A run still failing with that setting on
is a failure, because nothing the person can turn on will fix it.

Then look at it — at phone width, in both appearances. Every value can
be right and the result still poor.

To re-check the kit's own measured values against a browser:

```bash
python3 ../apple-ui-kit/verify_web_ui.py
```

## Where to send each question

| Question | Skill |
|---|---|
| Should this be a sheet or a popover? Is this accessible? What does Apple say? | **apple-hig** |
| What exact colour, size, radius, weight, tracking? Give me the CSS. | **apple-ui-kit** |
| How should this move? Why does it feel stiff? | **apple-motion** |
| What am I building, what screens, what system? | here |

Don't restate their values here. A hex code in this file is a hex code
that will go stale somewhere nobody looks.

## What this cannot do for you

- **Decide the product.** If the screen list is fifteen items, that is a
  scoping problem wearing a design problem's clothes.
- **Make a marketing site Apple-like.** The HIG does not govern
  apple.com, and applying it there produces a Settings screen with
  marketing copy in it.
- **Substitute for looking at it.** The checker proves the system is
  wired correctly. It has no opinion on whether the design is any good.
