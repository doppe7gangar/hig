Base directory for this skill: /tmp/claude-0/-home-user-apple-hig/19e48567-ea3b-518d-bd47-52b9e41c0d63/scratchpad/skilltest/work/b-compose/.claude/skills/apple-ui-kit

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


Read the measured token export. Setting it up now.

Set up at `app/src/main/java/design/applekit/`:

**`AppleKitTokens.kt`** — the raw measured iOS 27 values, copied verbatim from the UI-kit export (light + dark objects, plus control geometry). Generated file, so don't hand-edit it.

**`AppleColors.kt`** — the layer you actually code against: an `AppleColors` data class, light/dark instances, and an `AppleTheme { }` wrapper exposing `AppleTheme.colors.accent` etc.

```kotlin
AppleTheme {
    Text("Continue", color = AppleTheme.colors.accent)
}
```

Three things worth knowing:

**The values aren't the ones that circulate online.** The accent is `#0088FF`, not `#007AFF`; the primary label is `#1A1A1A`, not black; destructive red is `#FF383C`. If your iOS app hardcodes the older numbers anywhere, that's where the two will drift apart — worth a check.

**I bridged the palette into Material 3's colour roles** so stock Compose components inherit the tint rather than defaulting to Material purple. That covers colour only — a Material `Switch` still has Material's shape and animation. `AppleKitMetric` has the measured geometry (64×28 switch, 44dp hit target) for when you build iOS-shaped controls.

**Light mode doesn't clear Apple's own contrast bar.** On the grouped background, `labelSecondary` measures 3.44:1 and accent-as-text 3.15:1, against the 4.5:1 Apple requires up to 17pt. iOS survives this because Increase Contrast adapts system colours at render time; Android won't do that for you. I included `AppleLightColorsHighContrast` with the darkened values and a comment showing how to wire it to `isHighTextContrastEnabled`. Dark mode passes everywhere, so keep body-size text on `label`.

One flag on the premise, since you didn't ask: an iOS palette on Android is a real choice when cross-platform brand consistency is the goal, but Android users expect Material's roles and switch. Colour is the least jarring part to borrow — if this extends to controls and navigation later, that's where it starts feeling foreign. Also note the grouped backgrounds (`background`/`groupedCard`) are the one set of values not measured — the kit exports components on transparent backgrounds, so those are iOS Settings' grey-page/white-cards pairing. Keep that order; inverting it is the fastest tell.