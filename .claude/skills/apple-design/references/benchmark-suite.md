# Design quality benchmark suite

Use these briefs to detect whether `apple-design` generalizes or collapses into one repeated composition.

The benchmark is intentionally architecture-focused. It does not prescribe screenshots.

## Briefs

| ID | Product | Target | Architectural pressure |
|---|---|---|---|
| analytics | support analytics | desktop web | one answer first; evidence second; avoid equal metric cards |
| mail | mail client | macOS | dense list-detail, toolbar/menu/keyboard behavior |
| photo | photo editor | macOS/iPadOS | content/canvas dominance, contextual inspector |
| finance | personal finance overview | iOS | summary hierarchy without dashboard-card wallpaper |
| plants | plant watering tracker | iOS | task hierarchy; tabs only if genuinely peer-level |
| notes | research notes | iPadOS/macOS | collection-detail/document relationship |
| devtool | API/debugging tool | desktop web/macOS | dense workspace, command/keyboard affordances |
| settings | configuration utility | macOS | grouped concerns, native controls, desktop density |
| media | music/video experience | iOS/iPadOS | immersive content, chrome recedes |
| commerce | product browsing/detail | responsive web | collection/detail and responsive transformation |
| landing | B2B product launch | marketing web | editorial narrative, no feature-card default |
| operations | incident monitoring | web | urgency/status hierarchy, tables/evidence, no decorative dashboard |
| messaging | team messaging | desktop web | channels/list/conversation, input remains primary in context |
| calendar | scheduling | iPadOS/web | temporal/spatial relationship, adaptive views |
| files | file manager | macOS | sidebar/list/detail, keyboard/context menus, multi-selection |

## Required review dimensions

For each run record:

- target platform and HIG routing performed
- candidates considered and rejected
- chosen spatial model (including custom model)
- design invariants
- persistent region count
- major container/card count
- primary-action count
- navigation strategy
- compact/wide transformation
- system components preferred or custom components justified
- interaction states covered
- accessibility considerations
- final design idea

## Regression signals

Across the suite, warn when:

- one spatial model appears in >60% of unrelated briefs
- `sidebar + card grid` appears across unrelated products
- every web product has approximately the same persistent region count
- native iOS and macOS outputs use the same navigation model without product reasons
- macOS outputs omit keyboard/menu/pointer considerations
- marketing outputs contain repeated feature-card grids
- every dashboard leads with multiple equal metric tiles
- responsive plans only say “stack” or “shrink” without architectural transformation
- custom controls are proposed without system-component lookup
- `DESIGN.md` lacks rejected alternatives or invariants

These are regression alarms, not universal design laws.

## Evaluation principle

The benchmark asks whether the **decision process and resulting structure vary appropriately with the product**.

Passing mechanical checks is necessary but not sufficient. A suite where all outputs pass `check_design.py` and all look structurally identical is a failed design skill.