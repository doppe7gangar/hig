Base directory for this skill: /tmp/claude-0/-home-user-apple-hig/19e48567-ea3b-518d-bd47-52b9e41c0d63/scratchpad/skilltest/work/f-routing/.claude/skills/apple-ui-kit

# Apple UI for the web

Apple's HIG never states a colour value. It says "system blue" and expects
you to call the semantic API and let the platform resolve it. That works
in SwiftUI and leaves you with nothing on the web — which is why
Apple-looking web pages are usually built from a hex code someone copied
off a blog in 2015.

This skill exists because the values *are* recoverable: the UI kit ships
renderings of Apple's real components, so the pixels are the palette.
Everything here was measured from those files, and every token carries
the file it came from.

| File | What it is |
|---|---|
| `tokens/` | **The measured values**, one file per target — see below. Generated; don't hand-edit. |
| `fonts/` | **Inter, bundled** (SIL OFL) — the non-Apple fallback for SF Pro, with its licence. |
| `ios-components.css` | **Web component recipes** built on the CSS tokens — buttons, switch, grouped list, field, segmented, tab bar, material. |
| `example.html` | Working reference page. Open it to see every recipe, light and dark. |
| `ui-kit-tokens.json` | **Every measurement**, 945 renderings × colours + geometry + state. Query it for anything the recipes don't cover. |

## Picking a target

| Building for | Use | Note |
|---|---|---|
| Web, any framework | `tokens/ios-tokens.css` + `ios-components.css` | Recipes included |
| React Native / JS | `tokens/tokens.ts` | Colours + metrics, typed |
| Android (Compose) | `tokens/AppleKitTokens.kt` | Light and dark objects |
| Android (views) | `tokens/colors.xml` | Light values |
| Flutter | `tokens/apple_kit_tokens.dart` | Light and dark classes |
| SwiftUI / UIKit | `tokens/AppleKitTokens.swift` | **Usually the wrong answer — read on** |
| Figma, Style Dictionary | `tokens/tokens.json` | Design Tokens format, with provenance |

**On Apple platforms, don't paste these literals.** `Color.accentColor`,
`UIColor.systemBlue`, `.primary` already resolve to the right value and
adapt to Dark Mode and Increase Contrast for free — and they'll track
whatever Apple changes next, which a hardcoded `#0088FF` won't. The Swift
export exists for the cases the semantic API can't reach: custom Core
Graphics drawing, a canvas, or matching Apple's palette deliberately. For
native work you almost certainly want **apple-hig** instead.

**On Android, think before reaching for this.** Material has its own
colour roles, its own switch, and its own conventions that users expect.
An iOS palette on Android is a legitimate choice when cross-platform
brand consistency is the deliberate goal; it is a bad default.

## Using it

For the web, copy the two CSS files in and load tokens first:

```html
<link rel="stylesheet" href="fonts/inter.css">     <!-- optional -->
<link rel="stylesheet" href="tokens/ios-tokens.css">
<link rel="stylesheet" href="ios-components.css">
```

Then use the tokens rather than literals. `var(--ios-accent)` adapts to
dark mode on its own; `#0088FF` does not.

```html
<button class="ios-btn ios-btn--filled">Continue</button>
<button class="ios-btn ios-btn--tinted">Learn More</button>
<button class="ios-btn">Cancel</button>
<button class="ios-btn ios-btn--filled ios-btn--destructive">Delete</button>

<label class="ios-switch">
  <input type="checkbox" checked><span class="ios-switch__track"></span>
</label>
```

For a framework, port the CSS as-is and keep the token layer — the
recipes are plain classes with no JS, so they drop into React, Vue,
Svelte, or Tailwind's `@layer components` unchanged.

## The values that are *not* what people think

Anyone hand-coding "iOS colours" from memory or from a search result gets
these wrong, and wrong in a way that reads as slightly-off rather than
obviously broken:

| | iOS 27 (measured) | What's usually used |
|---|---|---|
| Accent blue | `#0088FF` | `#007AFF` |
| Destructive red | `#FF383C` light / `#FF4245` dark | `#FF3B30` / `#FF453A` |
| Primary label | `#1A1A1A` light / `#F5F5F5` dark | `#000000` / `#FFFFFF` |

The measurements that *do* match Apple's published semantics are what
make the rest credible — the switch reads `#34C759` in light and
`#30D158` in dark, exactly systemGreen for each appearance, and the
secondary-label and placeholder greys land on `rgba(60,60,67,0.6)` and
`rgba(60,60,67,0.3)` to the digit.

## Details that decide whether it reads as Apple

Most "iOS-style" web UI fails on these rather than on colour:

- **Grouped backgrounds are a pair, and the order matters.** A grey page
  (`--ios-bg`) with white cards floating on it (`--ios-bg-card`), not a
  white page with grey cards. Inverting this is the single fastest way to
  look not-quite-right.
- **Separators start at the text, not the card edge**, and the last row
  has none. `.ios-list__row + .ios-list__row::before` does this; a plain
  `border-bottom` doesn't.
- **Translucent greys, not solid ones.** Apple's fills and secondary
  labels are one base grey at several opacities, so they sit correctly on
  any background. `rgba(60,60,67,0.6)` — never its flattened equivalent.
- **Capsule buttons.** iOS 26 moved to fully rounded buttons; a 8px
  radius reads as an older OS.
- **44px hit targets.** `buttons.md` states 44×44 pt as the general rule.
  The 28×28 in the accessibility table is a floor for minor controls, not
  a licence to shrink the primary action.
- **Type scale, exactly.** 17/22 body, 34/41 large title, 13/18 footnote.
  The tokens are complete `font` shorthands so `font: var(--ios-text-body)`
  is valid on its own — a shorthand without a family is invalid CSS and
  the browser silently drops it, leaving everything at 16px while still
  looking broadly plausible.

## Liquid Glass

A plain `backdrop-filter` is why most "iOS 26 style" web UI looks flat.
Measured off `Materials/_Liquid Glass` at 4×, the surface is four layers,
and the blur is the least of them:

- **Rim.** Not uniform. Light comes from above, so in dark mode the top
  edge is `#7E7E7E` against a `#1A1A1A` body — a bright specular line —
  while the sides fall to `#151515`, *darker* than the body. In light
  mode the whole rim is darker than the face (`#C5` top, `#97` sides on
  `#F9F9F9`), so it reads as an outline instead.
- **Falloff.** Just inside the rim, a band grading back to the body over
  ~1.5 pt: `#949494 → #434343 → #1F1F1F → #1A1A1A`.
- **Body.** Very slightly darker at the centre than at the edges.
- **Ambient shadow.** Wide and soft — 8% black in light, 15% in dark at
  the edge, still 3–5% sixteen points out.

```html
<button class="ios-glass ios-glass--light ios-glass-btn ios-glass--capsule">
  Focus
</button>
```

Tint variants, measured rather than invented. "Light" and "Dark" Liquid
Glass are the same neutral grey at two strengths, not a white/black pair,
and "Prominent" isn't a tint at all — it's the accent filled solid:

| Class | Value | Use |
|---|---|---|
| `.ios-glass--light` | `rgba(115,115,128,.078)` | over busy or bright content, so colour survives |
| `.ios-glass--dark` | `rgba(116,116,128,.18)` | over quiet content, where the control must separate |
| `.ios-glass--prominent` | `var(--ios-accent)`, opaque | the primary action |
| `.ios-glass--clear` | minimal tint | over vivid artwork |

`.ios-navbar` and `.ios-tabbar` are glass already.

**It only works over something.** Glass is a refraction; on a flat
background there is nothing to refract and nothing to blur, and it
collapses to a grey box. If a design has no photography, gradient, or
scrolling content behind the bars, glass is the wrong material — reach
for a plain surface rather than faking it.

`prefers-reduced-transparency` drops every glass surface to an opaque
one, which is the setting Apple's own Reduce Transparency maps to.

## Typography is where it stops looking like SF

Getting the family right is the easy half. Two things decide whether the
type actually reads as Apple, and both are counterintuitive.

**Tracking is not monotonic.** Apple publishes a per-size table
(`specs.md`, *Tracking values → SF Pro*) and the sign flips:

| Style | Size | Tracking |
|---|---|---|
| Large Title | 34 pt | **+0.012em** |
| Title 1 | 28 pt | **+0.014em** |
| Title 2 | 22 pt | −0.012em |
| Body / Headline | 17 pt | −0.026em |
| Footnote | 13 pt | −0.006em |
| Caption 2 | 11 pt | +0.006em |

Large type is tracked **looser**, not tighter. The intuition that big
text tightens is wrong here, and it is wrong on the most prominent text
on the screen. On Apple platforms the font's `trak` table applies these
automatically; browsers ignore `trak`, so they must be set as
`letter-spacing`. Use `var(--ios-track-<style>)` beside every
`var(--ios-text-<style>)`.

**SF's weight axis is not the CSS ladder.** Read off the variable font's
named instances:

| | Ultralight | Thin | Light | Regular | Medium | Semibold | Bold | Heavy | Black |
|---|---|---|---|---|---|---|---|---|---|
| `wght` | 31 | 111 | 274 | 400 | **510** | **590** | 700 | 860 | 1000 |

Medium is 510 and Semibold is 590. `font-weight: 600` asks for something
between two real weights that Apple never ships — close enough to look
fine and wrong enough to feel off. Use `var(--ios-weight-semibold)`.

Both sets are generated, not typed: the tracking is parsed out of
`specs.md` and the weights come from the font's own `fvar` table.

## Contrast: Apple's light palette does not clear Apple's own table

Worth knowing before you ship text in it. `accessibility.md` requires
**4.5:1 up to 17 pt**, 3:1 at 18 pt or bold. Measured, on the light
grouped background:

| Pair | Ratio | |
|---|---|---|
| `--ios-label` on card | **17.4:1** | fine |
| `--ios-label-secondary` on card | **3.44:1** | under 4.5 |
| `--ios-accent` as text on page | **3.15:1** | under 4.5 |
| `--ios-red` as text on card | **3.57:1** | under 4.5 |
| `--ios-label-tertiary` on card | **1.73:1** | placeholder only, never content |
| white on filled accent button | **3.52:1** | passes — the label is semibold, so 3:1 applies |

Dark mode clears 4.5:1 on every one of these. Light is where it bites.

This is a property of Apple's real values, not a mistake in the recipes,
and it is survivable on iOS because Increase Contrast adapts the system
colours at render time. Nothing does that for you on the web. So:

- **Body-size text carrying meaning → `--ios-label`.** Secondary and
  tertiary are for supporting text, and even then they are under the
  threshold in light mode.
- **Accent-coloured text** (plain buttons, links) is at 3.15–3.52:1.
  Fine for a short interactive label people expect to be blue; not fine
  for a paragraph.
- **`prefers-contrast: more` is wired up** and darkens accent, red, and
  secondary just enough to clear 4.5:1 with the hue kept. That is the
  web port of Increase Contrast — leave it in.

`scripts/verify_web_ui.py` asserts all of this in a real browser, so a
change that breaks it fails rather than merely looking fine.

## What does not transfer, and don't pretend it does

- **SF Pro — now self-hosted.** `fonts/sf.css` serves the real thing,
  built from the variable `SF-Pro.ttf` by `scripts/build_fonts.py`:
  subset to Latin and compressed to woff2, 6.1 MB becomes **212 KB**,
  smaller than Inter. It carries both of Apple's axes (`opsz 17–28`,
  `wght 1–1000`), so one file spans Text through Display and Ultralight
  through Black.

  Link it **after** `tokens/ios-tokens.css` — it overrides `--ios-font`,
  and the token sheet will otherwise overwrite it straight back.
  `-apple-system` still leads the stack, so Macs and iPhones use the
  copy they already have and download nothing; this is what Windows,
  Android and Linux get.

  Its licence covers designing and mocking up interfaces for Apple
  platforms, not webfont embedding or redistribution. Serving it from a
  public site is a call you're making, not one the licence grants.
  `fonts/inter.css` is the unrestricted alternative and is what the
  skill uses when `sf.css` isn't linked.

- **Liquid Glass — the refraction only.** The live bending of what sits
  behind the surface has no browser equivalent. Everything else about it
  does, and is built: see below.
- **Dynamic Type.** The web equivalent is `rem` plus the browser's own
  text scaling, which the tokens use. It is not the same thing — there is
  no accessibility-size ladder.
- **Native behaviour.** Sheet physics, rubber-band scrolling, haptics,
  swipe-back. Approximating these badly is worse than leaving them out.

Say so when it comes up. A page that honestly borrows Apple's visual
language beats one that claims to be indistinguishable and isn't.

## Anything the recipes don't cover

`ui-kit-tokens.json` holds every measurement, one record per rendering,
with `component`, `appearance`, `state`, `size_pt`, `radius_pt` and the
colours with their alpha and coverage share. Query it directly:

```bash
python3 - <<'EOF'
import json
rows = json.load(open("ui-kit-tokens.json"))
for r in rows:
    if r["component"] == "Sliders" and r["appearance"] == "light":
        print(r["file"], r["size_pt"], r["radius_pt"],
              [c["css"] for c in r["colours"][:3]])
EOF
```

Components measured include Alerts, Action Sheets, Tab Bars, Keyboards,
Notifications, Date & Time Pickers, Steppers, Sliders, Text Fields,
Materials, Page Controls, Pop-up Buttons, Context Menus and App Icons.

Re-measure after changing the kit, then re-verify:

```bash
python3 scripts/extract_ui_kit_tokens.py   # PNGs  -> ui-kit-tokens.json
python3 scripts/build_web_tokens.py        # JSON  -> ios-web-tokens.css
python3 scripts/verify_web_ui.py           # asserts the rendered result
```

`verify_web_ui.py` drives a real browser over `example.html` and checks
computed values, not appearance: every token resolves, the type scale
lands on the specs.md numbers to the pixel, the switch measures 64x28
with a 36px knob travel, hit targets clear 44px, separators skip each
list's first row, the grouped backgrounds are the right way round, and
every colour pair meets the contrast it should. 155 checks across light,
dark, and increased contrast.

## Rules, not just looks

This skill carries appearance. It does not carry Apple's guidance about
*when* to use what — whether a thing should be a sheet or a popover,
whether an alert is warranted, how a layout should adapt. That's the
**apple-hig** skill, which holds all 2,326 HIG rules, the spec tables, and
the platform differences. Reach for it whenever the question is about
behaviour or structure rather than pixels, and for any native SwiftUI,
UIKit, or AppKit work.


ARGUMENTS: exact colour and corner radius for a primary (filled) button in an iOS-style web app

Straight from the measured iOS 27 kit (`.claude/skills/apple-ui-kit`):

## Colour

| | Light | Dark |
|---|---|---|
| Fill | `#0088FF` | `#0091FF` |
| Label | `#FFFFFF` | `#FFFFFF` |
| Pressed fill | `color-mix(in srgb, accent 85%, #000)` | same |

**Not `#007AFF`.** That's the value that circulates online; the accent measured off Apple's actual `Text Fields/Light_Focused Text Field.png` rendering is `#0088FF`. Destructive primary is `#FF383C` light / `#FF4245` dark (not `#FF3B30`).

## Corner radius

**Fully capsule — `border-radius: 999px`.** iOS 26 moved buttons to pill shape; an 8–12px radius is the single clearest tell that a page is copying an older OS.

## The rest of the spec

```css
.ios-btn--filled {
  font: var(--ios-text-body);            /* 17px/22px */
  letter-spacing: var(--ios-track-body); /* -0.026em */
  font-weight: 590;                      /* SF Semibold — NOT 600 */
  min-height: 44px;
  padding: 11px 20px;
  border: none;
  border-radius: 999px;
  background: var(--ios-accent);
  color: #FFFFFF;
}
.ios-btn--filled:active { transform: scale(.97); background: color-mix(in srgb, var(--ios-accent) 85%, #000); }
.ios-btn:disabled { opacity: .5; }
```

Two things worth knowing:

- **`font-weight: 600` is wrong.** SF's named instances are Medium 510, Semibold 590 — 600 asks for a weight Apple doesn't ship, so the browser synthesises something between two real ones. Close enough to look fine, wrong enough to feel off.
- **Contrast:** white on `#0088FF` is 3.52:1. That passes only because the label is semibold at 17px (3:1 threshold applies). Drop the weight or the size and it fails WCAG.

Use `var(--ios-accent)` from `tokens/ios-tokens.css` rather than the literal — it flips to `#0091FF` in dark mode and darkens under `prefers-contrast: more` on its own. `ios-components.css` has the `.ios-btn` recipe ready to drop in, and `example.html` renders every variant in both appearances.