# Numbers: the figures reached for most

The handful of figures design and review keep needing, gathered in one
place and laid out by question. Each section links the page they come from;
for anything not here — icon grids, widget sizes, the full Dynamic Type
ladder at every setting — read the table on Apple's page with
`python3 ../hig_page.py <page> --grep <word>`.

Quote a figure **with its platform**: almost every one differs per
platform, and one row quoted as universal is the easiest way to be wrong.

## How big must text be?

From [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility).

| Platform | Default | Smallest |
|---|---|---|
| iOS, iPadOS | 17 pt | 11 pt |
| macOS | 13 pt | 10 pt |
| visionOS | 17 pt | 12 pt |
| watchOS | 16 pt | 12 pt |
| tvOS | 29 pt | 23 pt |

## How much contrast does text need?

From [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility).

| Text | Ratio against its background |
|---|---|
| 17 pt or smaller, any weight | at least 4.5:1 |
| 18 pt or larger | at least 3:1 |
| Bold, any size | at least 3:1 |

## How big must something you tap or click be?

From [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)
and [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons).
Aim for the first column; the second is the floor. Buttons are held to 44×44 pt
(60×60 pt in visionOS) as the general rule; `../SKILL.md` explains when the
floor is defensible.

| Platform | Aim for | Never below |
|---|---|---|
| iOS, iPadOS | 44×44 pt | 28×28 pt |
| macOS | 28×28 pt | 20×20 pt |
| visionOS | 60×60 pt | 28×28 pt |
| watchOS | 44×44 pt | 28×28 pt |
| tvOS | 66×66 pt | 56×56 pt |

## What sizes are the iPhone and iPad text styles?

At the default (Large) text size, from
[Typography](https://developer.apple.com/design/human-interface-guidelines/typography).
Size and line height in points; every style also has an emphasized weight.

| Style | Size / line | Weight |
|---|---|---|
| Large Title | 34 / 41 | Regular |
| Title 1 | 28 / 34 | Regular |
| Title 2 | 22 / 28 | Regular |
| Title 3 | 20 / 25 | Regular |
| Headline | 17 / 22 | Semibold |
| Body | 17 / 22 | Regular |
| Callout | 16 / 21 | Regular |
| Subheadline | 15 / 20 | Regular |
| Footnote | 13 / 18 | Regular |
| Caption 1 | 12 / 16 | Regular |
| Caption 2 | 11 / 13 | Regular |

The tracking for each size is in `../../ui-kit-for-apple-platforms/tokens/sf-pro-tracking.json`.

## And on the Mac?

From [Typography](https://developer.apple.com/design/human-interface-guidelines/typography).
Mac text styles don't scale with a text-size setting.

| Style | Size / line | Weight |
|---|---|---|
| Large Title | 26 / 32 | Regular |
| Title 1 | 22 / 26 | Regular |
| Title 2 | 17 / 22 | Regular |
| Title 3 | 15 / 20 | Regular |
| Headline | 13 / 16 | Bold |
| Body | 13 / 16 | Regular |
| Callout | 12 / 15 | Regular |
| Subheadline | 11 / 14 | Regular |
| Footnote | 10 / 13 | Regular |

## What does an iOS 27 screen measure?

Measured from Apple's iOS and iPadOS 27 design kit, not stated in the
guidelines; `../../ui-kit-for-apple-platforms/verify_ios_screens.py` holds the kit's
screens to these.

| Part | Measure |
|---|---|
| Status bar | 62 pt tall |
| Controls under it (back, actions) | 44 pt tall, from y 62, 16 pt from the edges |
| Large title | 34 pt Bold, 41 pt line, at y 116 |
| Inset list | 20 pt from each edge, 26 pt corners, starting 16 pt under the title |
| List rows | 52 pt; 68 pt with a subtitle |
| Tab bar | 62 pt tall, 21 pt from the sides and the bottom |
| Accent colour | `#0088FF` |
