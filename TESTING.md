# Testing these skills yourself

Four ways, cheapest first. You need nothing installed for the first one.

Paths below assume the repo is where GitHub Desktop puts it,
`~/Documents/GitHub/hig`. Adjust if you cloned somewhere else.

---

## 1. Look at it (no setup)

```bash
open ~/Documents/GitHub/hig/.claude/skills/apple-ui-kit/example.html
```

One screen, using every recipe the way a real app would rather than
lining them up for inspection. To check dark mode, flip
**System Settings → Appearance** while it's open — the page follows the
system, so it should switch without a reload.

What you're looking for: a grey page with white cards, capsule buttons,
green switches, separators that start at the text rather than the card
edge.

On a Mac the type renders in SF Pro from your own system copy, because
`-apple-system` finds it first. Everywhere else it loads the bundled
SF Pro webfont, falling back to Inter if `fonts/sf.css` isn't linked.

---

## 2. Test the UI-kit skill in Claude Code (the real test)

Install it once, for every project:

```bash
mkdir -p ~/.claude/skills
cp -R ~/Documents/GitHub/hig/.claude/skills/apple-ui-kit ~/.claude/skills/
```

Then in any empty folder:

```bash
mkdir ~/Desktop/skill-test && cd ~/Desktop/skill-test
claude
```

Ask for something ordinary:

> build me a simple expense tracker web page — a list of expenses, a
> total at the top, and an add button. make it feel like an Apple app.

**What tells you it worked:**

- It reads `apple-ui-kit/SKILL.md` early on, before writing any CSS.
- The files it writes reference `var(--ios-accent)` and friends, not
  raw hex codes.
- It copies `tokens/ios-tokens.css` and `ios-components.css` in rather
  than reinventing them.

**What tells you it didn't:** hardcoded `#007AFF` anywhere. That's the
old palette from search results — the measured iOS 27 accent is
`#0088FF`. It's the clearest single tell.

Open the result and compare it against `example.html` side by side.

---

## 3. Run the automated checks

One-time setup:

```bash
pip3 install playwright pillow
python3 -m playwright install chromium
```

Then:

```bash
cd ~/Documents/GitHub/hig
python3 scripts/verify_web_ui.py -v
```

167 checks in a real browser, across light, dark, and increased
contrast. It asserts computed values rather than appearance: every token
resolves, the type scale lands on the HIG's numbers to the pixel, the
switch measures 64×28 with 36px of knob travel, hit targets clear 44px,
separators skip each list's first row, the colour pairs meet the contrast
they should, and a bundled face actually renders rather than silently
falling through to whatever the platform substitutes.

It exits non-zero if anything fails, so it's worth running after any
edit to the CSS. Drop `-v` to see only failures.

To re-measure from the PNGs after changing the kit:

```bash
python3 scripts/extract_ui_kit_tokens.py   # PNGs -> measurements
python3 scripts/build_design_tokens.py     # -> CSS, Swift, Kotlin, XML,
                                           #    Dart, TS, Design Tokens JSON
python3 scripts/verify_web_ui.py           # asserts the rendered result
```

The exports all come from the same measurements, so a value can't drift
between platforms. Each one names the file it was measured from.

---

## 4. Test the HIG reference skill

```bash
cp -R ~/Documents/GitHub/hig/.claude/skills/apple-hig ~/.claude/skills/
```

Ask questions where you can check the answer:

> what's the minimum tap target on iOS, and where does Apple say it?

A working answer gives **both** numbers and says they disagree — 44×44 pt
as the general rule from `pages/buttons.md`, 28×28 pt as the floor in the
accessibility table — rather than confidently quoting one. That specific
question used to produce opposite answers on different runs, so it's a
good canary.

> 設計一個 iOS 設定畫面的文字階層，給我實際的 pt 數值

Non-English works; the corpus is English but retrieval doesn't care. You
should get 34/41 for Large Title, 17/22 body, 13/18 footnote.

Or paste real SwiftUI and ask for a review before shipping.

### Checking an answer rather than trusting it

Any answer that quotes Apple can be verified:

Copy the answer, then from whatever folder your code is in:

```bash
pbpaste | python3 ~/.claude/skills/apple-hig/verify_quotes.py -
```

It grades every quoted span against the corpus:
**verbatim**, **elided** (honest `[…]`), **truncated** (ends early), or
**altered** — reworded, or two separate rules fused into one sentence
Apple never wrote. Anything reported as ALTERED is worth reading twice.

---

## What "working" does not mean

`apple-ui-kit` carries Apple's *appearance* to platforms that have no
system palette to ask. On the web specifically it can't carry:

- **Liquid Glass** — the live refraction has no browser equivalent. The
  rim, falloff, tint variants and ambient shadow are all measured and
  built; only the bending of what's behind the surface is missing. It
  needs something behind it to work at all — over a flat background it
  collapses to a grey box, which is a property of the material, not a
  bug.
- **Native behaviour** — sheet physics, rubber-banding, haptics.

**SF Pro is no longer on that list.** It is self-hosted from
`fonts/sf.css` — a 212 KB Latin subset of the variable file — and Apple
devices still use their own copy via `-apple-system` without
downloading it. The remaining question there is licensing, not
capability: the licence covers designing for Apple platforms, not
webfont serving, so shipping it on a public site is your call.
`fonts/inter.css` is the unrestricted fallback.

And in light mode Apple's own palette sits under Apple's own contrast
threshold (secondary label 3.44:1 against a required 4.5:1). That's real,
it's documented in the skill, and `prefers-contrast: more` is wired up to
fix it. Not a bug to report.

---

## 5. Test the design skill on a whole brief

The other three answer questions. `apple-design` starts projects, so it
needs testing differently: not "is the answer right" but "is the thing
on disk actually wired up".

Ask for a product rather than a control. Anything works —
*"an internal analytics dashboard for our support team, web only, brand
colour #1F6FEB"*, *"a landing page for a B2B time-tracking tool"*,
*"an iOS app for tracking when my house plants need watering"*.

What should happen: it names the kind first, lists the screens, runs
`new_project.py` to scaffold, replaces the placeholder content with the
real design, and runs `check_design.py` before handing it over.

### Grade it with the checker, not by reading

```bash
python3 .claude/skills/apple-design/check_design.py ./design
```

This is the part worth insisting on. Three earlier rounds of this were
graded by reading the transcript, and all three were called working
while the thing on disk had a font CDN in it, or no `--ios-*` bridge, or
only the happy path. Every one of those survives a screenshot and a
confident summary. The exit code doesn't care about either.

Nonzero means don't ship it. It checks stylesheet order, remote
resources, the bridge surviving, all four states, dead local references,
hand-overridden tokens, contrast, sideways overflow at phone width,
targets under Apple's floor, console errors, and what `--ios-accent`
actually resolved to in a browser.

### Prove the checker isn't just agreeing with you

A checker that only ever passes is worth nothing. Break something and
confirm it fails:

```bash
cp -r design broken
sed -i 's|vendor/fonts/inter.css|https://fonts.googleapis.com/css2?family=Inter|' broken/index.html
python3 .claude/skills/apple-design/check_design.py broken   # must exit 1
```

Moving `theme.css` above the component sheet, deleting the empty and
error panels, or cutting the bridge off the end of `theme.css` should
each fail too — those are the four failures this was built from.

### The whole thing, automated

```bash
python3 scripts/eval/projtest.py
```

Runs three briefs of different kinds through a fresh agent with all four
skills installed, and grades each by running the checker on whatever it
produced.

---

## 6. One command that checks the rest

```bash
python3 scripts/doctor.py
```

Every number and path in this repo that can be resolved against reality
gets resolved: rule and page and screenshot counts against the corpus,
framework counts against `api-map.md`, the check total against a real run
of the verifier, every `scripts/*.py` named in a doc, every file a skill
promises it will have once installed, leftover placeholders, and
truncated Apple quotes in the skills' own prose.

It exists because the same class of bug turned up four rounds running and
was found by hand each time — a hardcoded 949 against 947 files, a
SKILL.md claiming 2,280 rules after a re-scrape made it 2,326,
instructions naming a script renamed weeks earlier. All four are numbers
or paths a machine can resolve.

`build_skill.py` and `build_design_tokens.py` run `--fast` (everything
but the browser pass) at the end of every build, so a regenerated file
that no longer matches what the docs claim fails immediately rather than
months later.

What it will **not** catch: whether the values are right. A confidently
wrong measurement stated consistently everywhere passes cleanly. That's
what `verify_web_ui.py` and the eval runs are for.

---

## 7. Where `apple-motion` comes from

`apple-motion` fills a real gap: the HIG covers motion as principle
and has no spring parameters at all. It defers values to `apple-ui-kit` and principles to
`apple-hig`, and says plainly which of its own claims are API fact and
which are one author's observation.

Its references are adapted from the MIT-licensed apple-design-skills
collection, with Apple values reconciled against `apple-ui-kit`'s
measurements; the notice is in `.claude/skills/apple-motion/LICENSE.txt`.
