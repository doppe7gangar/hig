---
description: Review SwiftUI, UIKit or AppKit code, or a design folder, against Apple's Human Interface Guidelines, with each finding sorted into violation, guidance or judgment and linked to Apple's page.
argument-hint: "[files or folder]"
disable-model-invocation: true
---

# Review against the HIG

What to review: $ARGUMENTS

If nothing was named, review the Apple-platform UI this branch changed:
`git diff --name-only $(git merge-base HEAD origin/HEAD 2>/dev/null || echo HEAD~1)`,
keeping `.swift` files and design folders (an `index.html` beside a `vendor/`
folder).

Hand the reading to the `onplatform:reviewer` agent. Give it the paths, the target
platforms if you know them, and what each screen is for. It reads Apple's
pages in its own context and returns the findings. If the agent isn't
available, follow its method yourself: `${CLAUDE_PLUGIN_ROOT}/agents/reviewer.md`.

Present what comes back in three groups, each finding with its link:

- **Violations:** Apple states a rule with a number and the code misses it.
  Give the line and the fix.
- **Guidance:** Apple prefers or advises against, with no threshold.
  Deviating is defensible with a reason.
- **Judgment:** the HIG doesn't address it. Say so, rather than inventing a
  rule.

Never present guidance as a violation. Then offer to fix the violations.
