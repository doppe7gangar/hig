# Visual critique and reduction

Use this after a first composition exists and before calling the design finished. This is deliberately subjective: `check_design.py` handles mechanical correctness; this file asks whether the design is actually good.

## The two-second test

Look at the screen as if you had never seen the product.

Within two seconds, you should be able to identify:

1. what this place is,
2. what matters most right now,
3. what the primary action is, if one exists.

If several regions compete for first attention, hierarchy is unresolved.

## Critique in this order

### 1. Information before styling

Describe the screen without visual vocabulary. What information is primary, secondary, tertiary, and contextual? If this cannot be stated clearly, changing colors, radii, or shadows will not fix the screen.

### 2. Composition

Ask why each region is where it is. A strong composition reflects task relationships. A weak composition reflects whichever components were easiest to arrange.

Warning signs:

- equal columns for unequal information
- grids used only because several things exist
- a sidebar whose destinations are rarely switched
- a dashboard where every metric has equal weight
- a detail screen that is really several unrelated cards
- mobile chrome enlarged onto desktop
- desktop density squeezed unchanged onto mobile

### 3. Container audit

For every card, panel, tinted background, border, or floating surface, ask what boundary it communicates.

Valid reasons include:

- separate interaction region
- separate material/elevation layer
- semantic grouping that spacing alone cannot express
- selected/focused object
- modal or transient surface

“Because it looked empty” is not a valid reason.

Try removing the container while preserving its internal alignment and spacing. If the grouping remains obvious, leave the container out.

### 4. Typography audit

Temporarily imagine every border and background removed. Can type alone still reveal the reading order?

Check:

- one unmistakable first read
- meaningful size differences rather than many nearly identical sizes
- weight used intentionally
- secondary copy actually recedes
- line length appropriate to reading purpose
- labels not repeated when context already supplies them

### 5. Density audit

Density is a product decision, not a universal aesthetic.

Higher density suits expert tools, tables, inspectors, inboxes, editing environments, and repeated operational work. Lower density suits onboarding, focus tasks, media, consumer summaries, and editorial storytelling.

Do not make a professional desktop tool spacious merely to look premium. Do not make a consumer mobile screen dense merely to fit more.

### 6. Chrome audit

Chrome exists to support content. Identify everything that remains visible while the user works: navigation, toolbar, filters, actions, tabs, inspectors, status controls.

Ask whether each element must remain persistent. Move infrequent or object-specific actions into contextual menus, inspectors, selection states, or disclosure when appropriate.

### 7. Material audit

Blur, translucency, shadow, vibrancy, and elevation must describe spatial relationships.

For every material effect ask:

- what layer is this on?
- what is beneath it?
- why must the relationship remain perceptible?

If those questions have no useful answer, simplify.

### 8. Color audit

Color should identify action, state, selection, brand, or data meaning. It should not be required to rescue weak structure.

Try imagining the interface in grayscale. The hierarchy should largely survive.

### 9. Platform authenticity

#### iPhone
Does it prioritize content and touch? Are peer destinations truly peers? Is navigation understandable without permanent desktop chrome?

#### iPad
Does it exploit width rather than simply enlarge iPhone? Would a split view, sidebar, inspector, or multi-column relationship improve continuity?

#### macOS
Is it dense enough for repeated work? Are keyboard, pointer, sidebar, toolbar, table, menu, inspector, and multiwindow conventions considered where relevant?

#### Web app
Does it behave like good browser software? Is it borrowing Apple's design principles rather than wearing copied iOS furniture?

#### Marketing
Does the page tell a visual argument? Each section should advance claim, proof, demonstration, differentiation, or action rather than repeat a feature-card pattern.

## Anti-AI visual smell

Redesign if several of these appear together:

- every region has a radius
- every region has its own background
- many pill-shaped controls
- several gradient blobs
- glass everywhere
- feature-card grids
- icon badges on every heading
- large centered heading followed by three cards, repeated section after section
- shadows on surfaces that do not need elevation
- decorative status dots
- equal metric tiles
- excessive whitespace without stronger hierarchy
- tiny gray explanatory text everywhere
- multiple blue primary-looking actions

The goal is not to ban these devices. The goal is to stop them becoming the design language by accident.

## Reduction sequence

Run these in order:

1. Remove decorative effects.
2. Remove unnecessary containers.
3. Remove redundant labels.
4. Demote secondary actions.
5. Collapse contextual controls.
6. Re-evaluate spacing after removal.
7. Strengthen typography only where hierarchy became unclear.
8. Reintroduce a surface or separator only when the relationship genuinely needs it.

Reduction is not making everything sparse. It is removing things that do not explain, enable, or orient.

## Final question

Ask: **What is the design idea of this screen?**

A good answer sounds like:

- “The document is the workspace; controls appear around the selection.”
- “Today’s status is the answer; history exists to explain it.”
- “The photo owns the screen; editing controls recede until invoked.”
- “The list is navigation; the detail pane is the work.”

A weak answer sounds like:

- “It has a sidebar and cards.”
- “It is clean and modern.”
- “It uses Apple colors and rounded corners.”

If there is no clear design idea, return to composition.