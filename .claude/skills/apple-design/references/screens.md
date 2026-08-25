# Screen shapes, and the states they need

Components are solved. `apple-ui-kit` has buttons, switches, lists and
their exact values. What is missing between "here is a button" and "here
is a product" is the composition: which screens a thing needs, what goes
on each, and — the part that gets skipped — what each one looks like
before the data arrives, when it fails, and when there is nothing there.

Each shape below is the arrangement, the decisions that matter, and the
full state set. Values come from `apple-ui-kit`; rules and quotations
from `apple-hig`.

---

## The four states, first

This is the most common real-world gap, and it is not a matter of taste.
Any screen that loads anything has four states, and most builds ship one.

| State | What it is | The mistake |
|---|---|---|
| **Populated** | The happy path | The only one built |
| **Loading** | Data in flight | A spinner in the middle of a blank page, when a skeleton of the real layout would tell you more |
| **Empty** | Nothing to show | A shrug. This is the highest-leverage screen in most products |
| **Error** | It failed | A raw message, or worse, an empty state that lies |

**Empty is three different screens, not one.**

- **First run** — nothing yet *because you are new*. This is onboarding
  wearing an empty state's clothes: it should say what this screen is
  for and give exactly one action.
- **Filtered to nothing** — there is data, this query found none. Offer
  to clear the filter. Never show the first-run copy here; telling
  someone to "add your first recipe" when they have two hundred reads as
  broken.
- **Deliberately cleared** — they emptied it. Congratulate, don't
  prompt. An inbox at zero is a success state.

`apple-hig` files this under Writing, not under a component:
*"Provide clear next steps on any blank screens."* SwiftUI has
`ContentUnavailableView` for exactly this; UIKit has
`UIContentUnavailableConfiguration`. On the web there is no built-in, so
build one and reuse it.

**Error should say what to do, not what happened.** "Couldn't load your
recipes — check your connection and try again" with a Try Again button
beats "Error: NetworkError 500" every time, and both take the same
effort.

---

## List and detail

The commonest shape in software, and the default answer for anything
with a collection of things.

**Shape.** A list of rows; tapping one pushes a detail view; the detail
has its own actions. On wide screens the two sit side by side rather
than replacing each other — that is `NavigationSplitView`, and on the
web it is a two-column layout above a breakpoint.

**Decisions that matter**

- **What goes in the row.** Three elements at most: what it is, one
  distinguishing fact, and a state indicator. A row carrying five things
  is a detail view that has not admitted it yet.
- **Where the primary action lives.** Adding belongs in the navigation
  bar; acting on one item belongs in its row or its detail. A screen
  with an "Add" button *and* a floating button has two answers to one
  question.
- **Destructive actions.** Swipe or context menu, not a trash icon in
  every row — see `apple-hig` on `pages/buttons.md` for why a
  destructive control does not take the primary style.

**States.** Populated · loading (skeleton rows, not a spinner) · empty
(all three kinds) · error.

---

## Settings

Deceptively easy, and the shape most often built wrong on the web.

**Shape.** Grouped sections with headers and explanatory footers. Rows
carry a label on the left and a control or value on the right.

**Decisions that matter**

- **The footer is the interface.** A section footer explaining what a
  toggle does is worth more than the toggle's label. Most settings
  screens skip it and become a wall of ambiguous switches.
- **Group by concern, not by control type.** All toggles together is
  filing by implementation.
- **Destructive at the bottom, alone, in red.** Sign out, delete
  account. Never adjacent to an ordinary row.
- **Immediate, not saved.** A settings screen with a Save button is a
  form. Pick one.

**States.** Mostly populated — but the account section still needs
loading and error, since it usually fetches.

---

## Onboarding

**Shape.** As few screens as the product can survive. One idea each.

**Decisions that matter**

- **Earn each screen.** Three screens of value proposition before anyone
  has used anything is a toll booth. If the product can be understood by
  using it, let them.
- **Ask for permissions in context, not upfront.** Requesting
  notifications on launch is the classic error — ask when the person
  does the thing that needs it, having explained why.
  `apple-hig`'s `pages/privacy.md` is explicit about this.
- **Always skippable**, and skipping must not break anything.

**States.** Per step: idle · submitting · failed. The failure state is
skipped almost universally and is where people abandon.

---

## Dashboard / summary

**Shape.** One primary metric, then supporting detail. Not a grid of
equal cards.

**Decisions that matter**

- **One number is the hero.** If everything is the same size, nothing is
  the answer, and the person has to do the reading the screen should
  have done.
- **Comparison beats magnitude.** "68%, best week since June" tells you
  something; "68%" does not.
- **Colour carries meaning here** — which means it must not be the only
  thing that does. `apple-hig`: *"Convey information with more than
  colour alone."*

**States.** Populated · loading (skeleton preserving layout, so nothing
jumps) · **not enough data yet**, which is a real and distinct state on
any dashboard — a week-over-week comparison on day one has nothing to
compare.

---

## Form

**Decisions that matter**

- **Validate on blur, not per keystroke.** Errors appearing mid-word are
  hostile.
- **The error goes next to the field**, not summarised at the top.
- **One column.** Side-by-side fields break scanning and collapse badly.
- **Say what is optional**, rather than marking everything required.

**States.** Empty · in progress · per-field invalid · submitting
(disable the button, keep the label) · succeeded · failed as a whole.

---

## Feed

**Decisions that matter**

- **Pagination or infinite scroll is a content decision.** Infinite
  suits browsing; pagination suits finding. Infinite scroll with a
  footer is a design that fights itself.
- **New content must not move what someone is reading.** Insert above
  the fold with a "new items" affordance instead.

**States.** Populated · loading more (at the bottom, not replacing) ·
empty · error · offline with cached content, which is a distinct state:
show what you have and say it is stale.

---

## When the answer is "not an iOS shape"

A marketing page is not any of these. It has a hero, sections that argue
a case, and a call to action — the craft is editorial and typographic,
and the HIG governs none of it. Reaching for a grouped list there
produces a Settings screen with marketing copy in it.

The parts of this file that still apply anywhere: the four states, the
three empties, and errors that say what to do.
