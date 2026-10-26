# apple-hig

Design, build and review apps the way Apple does, with an AI coding agent
that reads Apple's actual rules instead of half-remembering them.

Four skills for Claude Code (and any agent that reads `AGENTS.md`), plus
Apple's full Human Interface Guidelines as offline Markdown for them to
quote.

## Set up (one minute)

```bash
git clone https://github.com/doppe7gangar/hig ~/hig
mkdir -p ~/.claude/skills
cp -R ~/hig/.claude/skills/apple-* ~/.claude/skills/
```

That installs them for every project. Inside this repo they load
automatically. You don't call them by name: describe what you want and the
right one picks itself.

## What do you want to do?

| You want to… | Say something like | Skill | You get |
|---|---|---|---|
| Turn an idea into an app or site | *"I want an app for splitting bills with friends"* | `apple-design` | The screens and how they connect, a working HTML project, and a checker run before it's handed over |
| Make a web, Android, Flutter or React Native UI look like iOS | *"Make this settings page feel like an Apple app"* | `apple-ui-kit` | Apple's measured colours, type and control sizes as tokens, plus ready CSS components |
| Check a design or SwiftUI code against Apple's rules | *"Review this screen before I ship it"* | `apple-hig` | Findings sorted into hard violations, soft guidance and judgment calls, each citing the page it comes from |
| Get a straight answer | *"Sheet or popover here?"*, *"Is this button too small?"* | `apple-hig` | Apple's number or rule, quoted, with where it says so |
| Make it move right | *"This transition feels floaty"* | `apple-motion` | The spring, the timing, and the Reduce Motion fallback |

### Try it in five minutes

Open Claude Code in an empty folder and paste:

> build me a simple expense tracker web page — a list of expenses, a total
> at the top, and an add button. make it feel like an Apple app.

**It worked if** the CSS uses `var(--ios-accent)` and friends rather than raw
hex codes, and `tokens/ios-tokens.css` and `ios-components.css` were copied
in rather than reinvented. **It didn't if** you see `#007AFF` anywhere.
That's the old accent from search results; the iOS 27 accent measured from
Apple's kit is `#0088FF`.

For a whole product, ask for one and then grade what's on disk, not what
the transcript says:

```bash
python3 ~/.claude/skills/apple-design/check_design.py ./design
```

More recipes, and what good output looks like for each, are in
[TESTING.md](TESTING.md).

## The numbers you'll reach for most

From the guidelines and Apple's iOS 27 UI kit. Each one is in
`.claude/skills/apple-hig/references/specs.md` or the kit's tokens, with
its source.

| What | Value |
|---|---|
| Minimum tap target, iOS | 44×44 pt default, 28×28 pt minimum |
| Text contrast | 4.5:1 up to 17 pt; 3:1 at 18 pt or bold |
| iOS text sizes (default) | Large Title 34 · Title 1 28 · Title 2 22 · Title 3 20 · Body 17 · Subhead 15 · Footnote 13 · Caption 12 / 11 |
| Accent colour | `#0088FF` (not `#007AFF`) |
| Primary label | `#1A1A1A` (not pure black) |

## Find the guidance for what you're building

Grouped by the job in front of you rather than by Apple's chapter order.
Each link opens the full page.

| Building… | Read |
|---|---|
| A list, settings or detail screen | [Lists and tables](content/lists-and-tables.md) · [Settings](content/settings.md) · [Toggles](content/toggles.md) · [Layout](content/layout.md) |
| Navigation between screens | [Tab bars](content/tab-bars.md) · [Sidebars](content/sidebars.md) · [Split views](content/split-views.md) · [Toolbars](content/toolbars.md) |
| Asking the user to confirm or choose | [Alerts](content/alerts.md) · [Action sheets](content/action-sheets.md) · [Sheets](content/sheets.md) · [Popovers](content/popovers.md) · [Modality](content/modality.md) |
| Menus and buttons | [Buttons](content/buttons.md) · [Menus](content/menus.md) · [Context menus](content/context-menus.md) · [Pop-up buttons](content/pop-up-buttons.md) · [Pull-down buttons](content/pull-down-buttons.md) |
| Forms and data entry | [Entering data](content/entering-data.md) · [Text fields](content/text-fields.md) · [Pickers](content/pickers.md) · [Steppers](content/steppers.md) · [Segmented controls](content/segmented-controls.md) · [Virtual keyboards](content/virtual-keyboards.md) |
| Search | [Searching](content/searching.md) · [Search fields](content/search-fields.md) |
| Empty, loading and error states | [Loading](content/loading.md) · [Feedback](content/feedback.md) · [Progress indicators](content/progress-indicators.md) |
| First run, sign-in and accounts | [Launching](content/launching.md) · [Onboarding](content/onboarding.md) · [Managing accounts](content/managing-accounts.md) · [Sign in with Apple](content/sign-in-with-apple.md) · [Privacy](content/privacy.md) |
| Notifications, widgets, Live Activities | [Managing notifications](content/managing-notifications.md) · [Notifications](content/notifications.md) · [Widgets](content/widgets.md) · [Live Activities](content/live-activities.md) |
| Taking payment | [Apple Pay](content/apple-pay.md) · [In-app purchase](content/in-app-purchase.md) · [Wallet](content/wallet.md) |
| Charts and dashboards | [Charting data](content/charting-data.md) · [Charts](content/charts.md) · [Gauges](content/gauges.md) |
| The look: colour, type, icons, materials | [Color](content/color.md) · [Dark Mode](content/dark-mode.md) · [Typography](content/typography.md) · [SF Symbols](content/sf-symbols.md) · [Materials](content/materials.md) · [App icons](content/app-icons.md) |
| Motion and haptics | [Motion](content/motion.md) · [Playing haptics](content/playing-haptics.md) · [Gestures](content/gestures.md) |
| Something everyone can use | [Accessibility](content/accessibility.md) · [VoiceOver](content/voiceover.md) · [Inclusion](content/inclusion.md) · [Right to left](content/right-to-left.md) · [Writing](content/writing.md) |
| The same app on another device | [iOS](content/designing-for-ios.md) · [iPadOS](content/designing-for-ipados.md) · [macOS](content/designing-for-macos.md) · [watchOS](content/designing-for-watchos.md) · [tvOS](content/designing-for-tvos.md) · [visionOS](content/designing-for-visionos.md) · [games](content/designing-for-games.md) |
| An AI feature | [Generative AI](content/generative-ai.md) · [Machine learning](content/machine-learning.md) |

Everything else, in Apple's order: **[all 178 pages](content/README.md)**.

## Without an AI

The references are plain Markdown, so a terminal is enough:

```bash
cd ~/.claude/skills/apple-hig/references
grep -i "^- .*sheet" rules.md          # every sheet rule, one line each
grep -A12 "^## Buttons" specs.md       # the numbers
grep -A4 "^\*\*Sheets\*\*" api-map.md   # the SwiftUI / UIKit / AppKit API
```

To check an answer that quotes Apple rather than trust it:

```bash
pbpaste | python3 ~/.claude/skills/apple-hig/verify_quotes.py -
```

Every quoted span comes back as verbatim, elided, truncated or altered.

**Cursor, Windsurf, aider, Zed, Copilot** and other tools that read
`AGENTS.md`: copy [AGENTS.md](AGENTS.md) plus
`.claude/skills/apple-hig/references/` into your project. Nothing in either
is tool-specific.

## What's in here

| Path | What it is |
|---|---|
| `.claude/skills/apple-design/` | Idea → screens → scaffolded project → checked design |
| `.claude/skills/apple-ui-kit/` | Measured iOS 27 tokens for CSS, SwiftUI, Compose, Android XML, Flutter and TypeScript, plus web components and a live [example](.claude/skills/apple-ui-kit/example.html) |
| `.claude/skills/apple-hig/` | 2,326 rules as one-line imperatives, every spec table, an API map across 32 frameworks, 947 screenshots of real components in every state, and all 178 pages |
| `.claude/skills/apple-motion/` | Springs, transitions, haptic pairing, Reduce Motion |
| `content/` | The guidelines as Markdown, rebuilt from Apple's site |
| `scripts/` | The scrapers, the skill builders, and the checks |

## Keeping it current

Apple revises the guidelines every OS cycle. To pull the latest and
rebuild:

```bash
python3 scripts/scrape_hig.py               # re-crawl the guidelines into content/
python3 scripts/audit_block_coverage.py     # anything Apple now emits that isn't rendered?
python3 scripts/build_skill.py              # regenerate the skill's references
python3 scripts/doctor.py                   # every count and claim in the docs still true?
```

Run the coverage audit on the full corpus, not `--quick`. It exists because
a block type the scraper doesn't recognise is invisible to every other
check: Apple's tabbed panes went unrendered for a whole scrape, taking the
iOS Dynamic Type scale with them, and nothing downstream could notice.

The design resources and landing pages are plain HTML rather than Apple's
JSON, so they have their own scrapers:
`scripts/scrape_resources.py` (needs `beautifulsoup4`) and
`scripts/scrape_marketing_page.py <url> <out-path>`.

Testing the skills themselves: [TESTING.md](TESTING.md) for the reference
and UI-kit skills, [DESIGN_TESTING.md](DESIGN_TESTING.md) for the design
workflow, and [scripts/eval/README.md](scripts/eval/README.md) before
trusting any triggering result.

## Notes

- The guidelines and the UI-kit images belong to Apple and are here for
  offline reference.
- Diagrams in `content/` load from Apple's CDN, so they need a connection.
- SF Pro's licence covers designing for Apple platforms, not serving it as
  a webfont. `fonts/inter.css` in the UI kit is the unrestricted fallback.
