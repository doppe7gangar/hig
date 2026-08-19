# Testing these skills yourself

Four ways, cheapest first. You need nothing installed for the first one.

Paths below assume the repo is where GitHub Desktop puts it,
`~/Documents/GitHub/hig`. Adjust if you cloned somewhere else.

---

## 1. Look at it (no setup)

```bash
open ~/Documents/GitHub/hig/.claude/skills/apple-web-ui/example.html
```

Every component in one page. To check dark mode, flip
**System Settings → Appearance** while it's open — the page follows the
system, so it should switch without a reload.

What you're looking for: a grey page with white cards, capsule buttons,
green switches, separators that start at the text rather than the card
edge.

---

## 2. Test the web skill in Claude Code (the real test)

Install it once, for every project:

```bash
mkdir -p ~/.claude/skills
cp -R ~/Documents/GitHub/hig/.claude/skills/apple-web-ui ~/.claude/skills/
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

- It reads `apple-web-ui/SKILL.md` early on, before writing any CSS.
- The files it writes reference `var(--ios-accent)` and friends, not
  raw hex codes.
- It copies `ios-web-tokens.css` and `ios-web-components.css` in rather
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

155 checks in a real browser, across light, dark, and increased
contrast. It asserts computed values rather than appearance: every token
resolves, the type scale lands on the HIG's numbers to the pixel, the
switch measures 64×28 with 36px of knob travel, hit targets clear 44px,
separators skip each list's first row, and the colour pairs meet the
contrast they should.

It exits non-zero if anything fails, so it's worth running after any
edit to the CSS. Drop `-v` to see only failures.

To re-measure from the PNGs after changing the kit:

```bash
python3 scripts/extract_ui_kit_tokens.py
python3 scripts/build_web_tokens.py
python3 scripts/verify_web_ui.py
```

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
``` It grades every quoted span against the corpus:
**verbatim**, **elided** (honest `[…]`), **truncated** (ends early), or
**altered** — reworded, or two separate rules fused into one sentence
Apple never wrote. Anything reported as ALTERED is worth reading twice.

---

## What "working" does not mean

The web skill carries Apple's *appearance*, and it can't carry:

- **SF Pro** — not licensed for general web use. Pages get SF on Apple
  devices via `system-ui` and a native fallback elsewhere, so it will
  look different on Windows. That's expected.
- **Liquid Glass** — real-time refraction with no browser equivalent.
  `.ios-material` approximates the blur, not the refraction.
- **Native behaviour** — sheet physics, rubber-banding, haptics.

And in light mode Apple's own palette sits under Apple's own contrast
threshold (secondary label 3.44:1 against a required 4.5:1). That's real,
it's documented in the skill, and `prefers-contrast: more` is wired up to
fix it. Not a bug to report.
