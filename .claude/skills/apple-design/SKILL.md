---
name: apple-design
description: Design a whole product, not a component — the entry point for "I'm building an app/website/dashboard, help me design it". Works out what kind of thing it is, what screens it needs and how they connect, generates a design system from the client's brand colour in Apple's structure, composes real screens with every state they need (empty, loading, error, first-run), and hands off to the reference skills for exact values. Use at the start of any design project, when someone describes what they're building rather than asking about a specific control, when a project needs a design system or brand palette, when deciding what screens exist or how navigation should work, or when a build is missing its empty and error states. Covers websites and marketing pages as well as apps, and is explicit about where Apple's guidance stops applying. For a specific rule or spec use apple-hig; for exact iOS values and CSS use apple-ui-kit; for animation use apple-motion.
---

# Designing a product

The other three skills answer questions. This one starts projects.

They are reference-shaped — *is this button too small*, *what colour is
the accent*, *how should this animate*. Handed a brief instead —
*"a meal-planning app for families, web first, iOS later"* — none of them
fires, because a brief is not a lookup. This is the skill for that, and
it delegates to them the moment a real value is needed.

## The order that matters

Most design work goes wrong before any pixel is chosen, by deciding the
visual language first and discovering the structure later. Work in this
order and each decision narrows the next.

### 1. What kind of thing is this?

The single most consequential question, because it decides how much of
Apple's guidance applies at all.

| Kind | Apple's guidance | What actually governs it |
|---|---|---|
| **iOS / macOS app** | Fully. This is what the HIG is for. | `apple-hig` end to end |
| **App-like web product** (dashboard, tool, admin) | The *structure* transfers — navigation, modality, states, hit targets. The *chrome* mostly doesn't: a web app with an iOS tab bar looks like a costume. | `apple-hig` for structure, `apple-ui-kit` for craft |
| **Marketing / brand website** | Barely. apple.com and iOS are different design languages; the HIG governs neither. | Editorial and typographic craft, not the HIG |
| **Cross-platform app** (RN, Flutter) | Structure yes, appearance per platform. | `apple-ui-kit` exports, plus the platform's own rules |

Say which one it is before going further. A marketing site built to iOS
guidelines is the most common way this goes wrong, and it is invisible
until the whole thing looks like a Settings screen.

### 2. What screens exist, and how do they connect?

Before any visual decision. Two questions settle most of it:

- **How many top-level places are there?** Under five and they are tabs.
  More, and either they are not all top-level, or it is a sidebar.
  `apple-hig`'s `pages/tab-bars.md` and `pages/navigation-bars.md` carry
  the rules; `references/screens.md` here carries the shapes.
- **What is a detour rather than a destination?** Anything the person
  comes back from — compose, edit, a picker, settings — is a sheet or a
  modal, not a tab. Getting this wrong produces apps where everything is
  a tab and nothing feels finished.

Write the screen list down before styling anything. Four to six screens
is a normal first version; if the list has fifteen, the product is not
scoped yet and no amount of design will fix that.

### 3. The system, in the client's colour

Real projects have their own brand. Apple's blue belongs to Apple.

**Run the generator. Do not hand-write the token file.**

```bash
python3 scripts/build_theme.py "#7A5AF8" --name violet -o theme.css
```

This is not a formatting preference. Hand-writing a perfectly reasonable
brand ramp — and a 100–900 ramp *is* reasonable — loses three things
that are easy to miss and expensive to discover later:

1. **The `--ios-*` bridge.** The generator ends by aliasing the brand
   tokens onto the names `apple-ui-kit`'s recipes actually read. Without
   it you get a brand palette *and* Apple-blue buttons, because
   `.ios-btn` is still reading `--ios-accent`. This has happened; it is
   the failure that looks like the system works until you place a
   component.
2. **The label ladder.** Apple's secondary and tertiary text is one grey
   at several opacities, not separate hexes, so it composites correctly
   on a card, on the page, and on a tinted surface. A ramp gives you one
   grey per step that is right on exactly one background.
3. **The contrast pass.** It reports where the brand colour cannot carry
   text and emits a darkened variant for that use.

If a ramp is wanted as well, generate first and add the ramp on top.
The order matters; the bridge has to survive.

Expect this: most saturated brand colours do not clear 4.5:1 as text on
white. Apple's own accent is 3.52:1. The generator emits a darkened
`--brand-accent-text` for coloured text and leaves the brand colour for
fills. Use both.

### 4. Compose the screens — with the states

**Read `references/screens.md` before composing anything.** It carries
the shapes — list-and-detail, settings, onboarding, dashboard, form,
feed — and, more importantly, the state sets. Working from memory here
reliably produces the happy path and nothing else.

**Every screen that loads data has four states, and most builds ship one.**
Empty, loading, error, and populated. First-run empty is a different
screen from filtered-empty, and both are different from failed-to-load.
`apple-hig`'s `pages/writing.md` covers the words; `references/screens.md`
covers the shape.

**The deliverable is a working screen, not a document about one.**

A brief that describes the design, in its own editorial typeface, that
never loads the theme it just generated, is a deliverable nobody can
build on — and it is the default thing to produce, because writing about
a design is easier than building one. This has happened: a handsome
`brief.html` next to a correct `theme.css`, with no link between them.

So end step 4 with at least one real screen that:

- links `theme.css` and the vendored `ios-tokens.css` /
  `ios-components.css`, in that order
- shows the populated state *and* at least the empty one
- opens offline — vendor the fonts, don't link a CDN
  (`apple-ui-kit`'s `fonts/` has them)

Write the brief too if it helps. Just don't let it be the only artefact.

### 5. Verify rather than admire

```bash
python3 scripts/doctor.py            # the repo's own claims
python3 scripts/verify_web_ui.py     # computed values in a real browser
```

Then read it on a phone-width viewport in both appearances. A design
that has only been seen at desktop width in light mode is half-checked.

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
- **Substitute for looking at it.** Every value here can be right and the
  result still poor. The measured tokens fix correctness, not judgment.
