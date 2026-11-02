---
description: Design an app, site or dashboard from a brief to a working prototype that reads as native on iPhone, iPad, Mac or Android, checked in a real browser before it's handed over.
argument-hint: "<what you want to build>"
disable-model-invocation: true
---

# Design it

The brief: $ARGUMENTS

If no brief came with the command, ask for one in a sentence and stop.

Scripts live in `${CLAUDE_PLUGIN_ROOT}/.claude/skills/apple-design/`; below, `D` stands for that folder.

1. **Load the method.** Invoke the `hig:apple-design` skill and follow it. It
   brings in `hig:apple-hig`, `hig:apple-ui-kit`, `hig:apple-motion` and
   `hig:android-ui-kit` as the work needs them. For a one-screen request,
   take its short path.
2. **Settle the brief before drawing:** the platform, who it's for, the
   screens and the states each one has. Ask only what can't be inferred, and
   say what you assumed.
3. **Scaffold, don't hand-roll:**
   `python3 D/new_project.py --name "<name>" --brand "<#hex>" --kind <ios|ipados|macos|android|web> --model <model> -o ./design`
4. **Build on the scaffold** with real content and the loading, empty and
   error states, keeping the kit's recipes. They carry the measured metrics.
5. **Check until it passes:** `python3 D/check_design.py ./design`. It taps
   every control and fails the ones that do nothing. Then render it with
   `python3 D/render_review.py ./design` and work through the review. For a
   second pair of eyes, hand the folder to the `hig:design-critic` agent.
6. **Licences:** `python3 D/check_distribution.py ./design`.
7. **Hand over:** what you built, how to open it (`open design/index.html`),
   what passed, what you assumed, and what comes next: `/hig:figma` to send
   it to Figma, `/hig:handoff` for SwiftUI, and `/hig:ship` before it's
   shared or published.
