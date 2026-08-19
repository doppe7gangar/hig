---
name: apple-web-ui
description: Build web and cross-platform UI that genuinely looks and behaves like Apple's — iOS 27 colours, type scale, control geometry and states, as CSS custom properties and ready component recipes (buttons, switches, grouped lists, text fields, segmented controls, tab bars, materials). Use whenever someone wants a web app, landing page, dashboard, React/Vue/Svelte component, or design system that should feel like iOS or macOS, whether they say "make it look like Apple", "iOS style", "Apple aesthetic", "clean like an Apple app", or just ask for a polished app UI and Apple is the obvious reference. Values are measured from Apple's real iOS 27 UI kit renderings, not remembered — the accent is #0088FF, not the #007AFF that circulates online, and the primary label is #1A1A1A, not black. Also use when reviewing a web UI that is trying to look Apple-like and getting details wrong. For native Apple platform work (SwiftUI, UIKit, AppKit) and for the actual HIG rules, use the apple-hig skill instead.
---

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
| `ios-web-tokens.css` | **Measured values** as custom properties — colour, type scale, control geometry. Generated; don't hand-edit. |
| `ios-web-components.css` | **Component recipes** built on those tokens — buttons, switch, grouped list, field, segmented, tab bar, material. |
| `ui-kit-tokens.json` | **Every measurement**, 945 renderings × colours + geometry + state. Query it for anything the recipes don't cover. |

## Using it

Copy both CSS files into the project and load tokens first:

```html
<link rel="stylesheet" href="ios-web-tokens.css">
<link rel="stylesheet" href="ios-web-components.css">
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

## What does not transfer, and don't pretend it does

- **SF Pro.** Its licence does not cover general web use. `--ios-font`
  starts with `system-ui`, which gets you SF on Apple devices and a sane
  native face elsewhere. Don't self-host SF Pro; don't tell someone a page
  will look identical on Windows.
- **Liquid Glass.** A real-time refraction the browser has no equivalent
  for. `.ios-material` gets the blur and saturation lift via
  `backdrop-filter`, which is the part that reads at a glance. Put it over
  content that actually scrolls behind it or it's just flat grey.
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

Re-measure after changing the kit:

```bash
python3 scripts/extract_ui_kit_tokens.py   # PNGs  -> ui-kit-tokens.json
python3 scripts/build_web_tokens.py        # JSON  -> ios-web-tokens.css
```

## Rules, not just looks

This skill carries appearance. It does not carry Apple's guidance about
*when* to use what — whether a thing should be a sheet or a popover,
whether an alert is warranted, how a layout should adapt. That's the
**apple-hig** skill, which holds all 2,326 HIG rules, the spec tables, and
the platform differences. Reach for it whenever the question is about
behaviour or structure rather than pixels, and for any native SwiftUI,
UIKit, or AppKit work.
