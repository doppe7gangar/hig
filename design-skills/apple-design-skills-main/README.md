# apple-design — Apple-grade design skill family

A 9-skill family that teaches an agent (Claude Code, Codex) how to build, restyle, and
critique **Apple-grade / apple.com-class** interfaces — design philosophy (HIG), the
Liquid Glass era, layout/grid, motion, the *interaction inventory* that makes a flagship
page feel **alive** (continuous damped scroll-progress, pinned scenes, theme morph,
sticky-stack, pointer-reactive), web/marketing-page formulas, OS surfaces, delivery/media
engineering, and accessibility/brand tactics. Every non-trivial claim is confidence-labeled
(`[observed]` / `[documented]` / `[inferred]` / `[speculative]`).

It encodes a **two-axis discipline**: *restraint* (cut gratuitous decoration) × *surface*
(utility = restrained / flagship-marketing = cinematic, motion-as-substance). Alive **and**
tasteful — not slop, not a dead template.

## The skills

| Skill | Covers |
|---|---|
| `apple-design` | Hub: HIG philosophy, two-axis model, restraint/anti-slop, router |
| `apple-design-foundations` | Color, SF typography, 8pt grid, bento, layout |
| `apple-design-materials` | Liquid Glass / vibrancy, app-icon squircle, SF Symbols |
| `apple-design-motion` | Springs, continuous damped scroll-progress, pointer-reactive, gestures |
| `apple-design-web` | apple.com formula, scrollytelling, interaction inventory, media/delivery |
| `apple-design-interaction` | Navigation models, state/feedback, perceived perf, scroll-as-input |
| `apple-design-os` | iOS/iPadOS/macOS/visionOS/watchOS + UIKit/SwiftUI anatomy |
| `apple-design-backend` | Observable delivery (CDN/mzstatic/HLS) + inferred server architecture |
| `apple-design-tactics` | Accessibility/inclusive design + marketing/persuasion/brand |

## Install

Clone, then run the installer for your OS. It links each skill into **both**
`~/.claude/skills` (Claude Code) and `~/.agents/skills` (Codex) so a single `git pull`
updates every agent on the machine.

```bash
git clone <your-remote-url> apple-design-skills
cd apple-design-skills
```

**Windows (PowerShell):**
```powershell
./install.ps1
```

**macOS / Linux:**
```bash
chmod +x install.sh && ./install.sh
```

Then **restart Claude Code / Codex** so it picks up the new skills.

> The installer links (Windows directory junctions / Unix symlinks) rather than copies,
> so updates propagate. It **skips** any skill name that already exists in a target dir
> (it never clobbers). To update later: `git pull` — done.

### Manual install (if you prefer copying)
Copy the folders in `skills/` into `~/.claude/skills/` (Claude Code) and/or
`~/.agents/skills/` (Codex), then restart the agent. No build step — a skill is just a
folder with a `SKILL.md`.

## What is NOT in this repo (by design)
Dev/validation artifacts (`_validation/`, `_planning/`, `_research/`) are git-ignored.
Notably, `_research/` contained **Apple's copyrighted reference frames**, which must not be
redistributed. This repo ships only the skill docs + recipes + a licensed/sourcing guide;
the skills teach how to source or generate your own assets. Never bundle a brand's
copyrighted media. (See `apple-design-web/references/media-assets-and-delivery.md`.)
