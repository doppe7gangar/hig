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

## 5. Auditing the third-party skills in `design-skills/`

`design-skills/` holds 106 skills from six collections, several covering
the same ground as `apple-ui-kit`. Installing them alongside it means two
sources disagreeing about what systemBlue is, and the model sees both.

```bash
python3 scripts/audit_design_skills.py
```

It checks their stated Apple values against this repo's measured ones —
colours off the UI kit renderings, weights from SF Pro's `fvar` table,
tracking from the HIG's own table — and reports every contradiction with
both values.

It found 43 real disagreements — the pre-iOS-26 palette, SF's weights
given as the CSS ladder, and one stating the tracking rule backwards for
display sizes. All are now reconciled, so it should report **no
disagreements**. If it reports some again, something upstream was
re-copied over the corrections.

```bash
python3 scripts/fix_design_skills.py --dry-run   # what it would change
python3 scripts/fix_design_skills.py             # apply
```

The fixer only touches straight substitutions, and skips lines where the
old value is named as an anti-pattern — "hardcoding `#007AFF` is a
maintenance trap, use `Color.blue`" is correct advice that happens to
contain the old hex, and rewriting it would turn guidance into nonsense.
Four such lines are excluded by design. The one prose claim was edited by
hand, because rewriting an argument mechanically produces something that
reads like it means something and doesn't.

None of this made them bad skills. Those values were correct until iOS 26
and are what circulates everywhere.

### What was kept

`apple-motion` is the one addition: the HIG covers motion as principle
and has no spring parameters at all, so it was a real gap rather than a
duplicate. It defers values to `apple-ui-kit` and principles to
`apple-hig`, and says plainly which of its own claims are API fact and
which are one author's observation.

The rest of `design-skills/` stays as reference material rather than
installed skills. Installing 106 of them means several all claiming
"Apple design" and colliding on every request.
