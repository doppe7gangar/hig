#!/usr/bin/env python3
"""Scaffold a working project: vendored kit, brand theme, real screens.

Every failure this skill has had was the same failure. The instructions
said run the generator, vendor the fonts, link the theme last, build all
four states -- and each run followed some of that and quietly dropped the
rest. Prose is advisory. A run that hand-writes its own token file, links
a font CDN, or ships only the happy path is not disobeying so much as
reconstructing infrastructure from a description, badly, while thinking
about the design.

So stop describing the setup and emit it. What comes out of this already
links in the order that works, already has the fonts on disk, already
carries the empty and error states, and already reads the brand palette
through the bridge. What is left to do is the design -- the content, the
copy, the hierarchy -- which is the part worth a designer's attention and
the part a generator cannot do.

    python3 new_project.py --name Clay --brand "#C1552E" \
        --kind ios --screens "Plan,Recipes,List,Settings" -o ./design

Kinds decide the shape, and deliberately differ: `marketing` gets no tab
bar and no grouped list, because the commonest way this goes wrong is a
brand site built to iOS chrome.
"""

import argparse
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILLS = os.path.dirname(HERE)
KIT = os.path.join(SKILLS, "apple-ui-kit")

sys.path.insert(0, HERE)
import build_theme  # noqa: E402


# ---------------------------------------------------------------- pieces

HEAD = """<!doctype html>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__NAME__</title>

<!-- Order is load-bearing. Fonts, then Apple's measured tokens, then the
     component recipes, then the brand theme LAST so its bridge wins. -->
<link rel="stylesheet" href="vendor/fonts/inter.css">
<link rel="stylesheet" href="vendor/fonts/sf.css">
<link rel="stylesheet" href="vendor/ios-tokens.css">
<link rel="stylesheet" href="vendor/ios-components.css">
<link rel="stylesheet" href="theme.css">
"""

# The state machinery is the same for every kind: one screen, four
# panels, a switcher that lives outside the design so it is obviously
# scaffolding rather than a component someone might ship.
STATE_CSS = """
  /* --- state switcher: scaffolding, not part of the design --- */
  .demo { min-height: 100vh; display: flex; flex-direction: column;
          background: var(--ios-bg);
          font: var(--ios-text-body); color: var(--ios-label); }
  .demo > :not(.demo__bar) { flex: 1; min-height: 0; }
  .demo__bar { display: flex; gap: 6px; flex-wrap: wrap;
               padding: 10px 16px; border-bottom: 1px solid var(--ios-separator);
               background: var(--ios-bg-card); }
  .demo__bar button { font: var(--ios-text-footnote); padding: 6px 12px;
                      min-height: 32px; border-radius: 999px; cursor: pointer;
                      border: 1px solid var(--ios-separator);
                      background: transparent; color: var(--ios-label-secondary); }
  /* Was white on the accent fill at 13px: 4.12:1, under the 4.5:1 that
     small text needs. A tint with text-safe ink clears it and is the
     same move the design should make anywhere it wants a selected chip
     below button-label size. */
  .demo__bar button[aria-pressed="true"] {
      background: color-mix(in srgb, var(--ios-accent) 16%, transparent);
      border-color: color-mix(in srgb, var(--ios-accent) 45%, transparent);
      color: var(--ios-label); font-weight: 590; }

  .state { display: none; }
  [data-state="populated"] .state--populated,
  [data-state="loading"]   .state--loading,
  [data-state="empty"]     .state--empty,
  [data-state="error"]     .state--error { display: block; }

  /* Skeletons keep the real layout so nothing jumps when data lands. */
  .skel { background: var(--ios-fill-control); border-radius: 6px;
          height: 1em; animation: skel 1.4s ease-in-out infinite; }
  @keyframes skel { 0%,100% { opacity: .55 } 50% { opacity: .25 } }
  @media (prefers-reduced-motion: reduce) { .skel { animation: none } }

  /* The empty/error block. SwiftUI calls this ContentUnavailableView;
     the web has no built-in, so this is the one to reuse. */
  .unavailable { text-align: center; padding: 48px 32px; }
  .unavailable__glyph { font-size: 44px; line-height: 1;
                        color: var(--ios-label-tertiary); }
  .unavailable__title { font: var(--ios-text-headline);
                        letter-spacing: var(--ios-track-headline);
                        margin: 14px 0 4px; }
  .unavailable__body { font: var(--ios-text-subhead);
                       color: var(--ios-label-secondary);
                       margin: 0 auto 20px; max-width: 30ch; }
"""

STATE_JS = """
<script>
  // Scaffolding: flips the panel so every state is reachable without a
  // backend. Delete when the real data layer arrives -- the four panels
  // are the part worth keeping.
  const root = document.querySelector('[data-state]');
  const initial = new URLSearchParams(location.search).get('state');
  if (initial) root.dataset.state = initial;
  for (const b of document.querySelectorAll('.demo__bar button')) {
    b.addEventListener('click', () => {
      root.dataset.state = b.dataset.set;
      for (const o of document.querySelectorAll('.demo__bar button'))
        o.setAttribute('aria-pressed', String(o === b));
    });
    b.setAttribute('aria-pressed', String(b.dataset.set === root.dataset.state));
  }
</script>
"""

SWITCHER = """<div class="demo__bar" role="group" aria-label="Preview state">
  <button data-set="populated">Populated</button>
  <button data-set="loading">Loading</button>
  <button data-set="empty">Empty</button>
  <button data-set="error">Error</button>
</div>
"""

ERROR_PANEL = """      <section class="state state--error">
        <div class="unavailable">
          <div class="unavailable__glyph" aria-hidden="true">!</div>
          <h2 class="unavailable__title">Couldn't load __THING__</h2>
          <!-- Say what to do, not what happened. "NetworkError 500" tells
               nobody anything they can act on. -->
          <p class="unavailable__body">Check your connection and try again.</p>
          <button class="ios-btn ios-btn--filled">Try Again</button>
        </div>
      </section>
"""

EMPTY_PANEL = """      <section class="state state--empty">
        <div class="unavailable">
          <div class="unavailable__glyph" aria-hidden="true">+</div>
          <h2 class="unavailable__title">No __THING__ yet</h2>
          <!-- FIRST-RUN empty. Filtered-to-nothing and deliberately-cleared
               are different screens with different copy -- see
               references/screens.md. Reusing this copy for a filtered list
               tells someone with 200 items to add their first, which reads
               as broken. -->
          <p class="unavailable__body">__EMPTY_BODY__</p>
          <button class="ios-btn ios-btn--filled">__EMPTY_CTA__</button>
        </div>
      </section>
"""


# ------------------------------------------------------------------ ios

IOS_CSS = """
  .phone { max-width: 430px; width: 100%; margin: 0 auto;
           display: flex; flex-direction: column;
           background: var(--ios-bg); }
  .screen { flex: 1; padding: 16px var(--ios-gutter, 16px) 24px; }
  .rowicon { width: 29px; height: 29px; border-radius: 7px; flex: none;
             display: grid; place-items: center;
             font: var(--ios-text-footnote);
             font-weight: var(--ios-weight-semibold);
             background: var(--ios-accent); color: #fff; }
  .ios-list { margin: 0 0 22px; }
  /* An 11pt tab label is small text, so it needs 4.5:1 -- and the raw
     accent is tuned for fills, which only need 3:1. The generator emits
     a text-safe variant for exactly this; the component recipes have no
     way to know it exists, so the wiring belongs here. */
  .ios-tabbar__item[aria-selected="true"] { color: var(--accent-text-safe); }
  /* Same reasoning for a tinted button: its label is accent-coloured
     text, not a fill, so it needs the text-safe variant too. */
  .ios-btn--tinted { color: var(--accent-text-safe); }
  .sectionhead { font: var(--ios-text-footnote);
                 letter-spacing: var(--ios-track-footnote);
                 text-transform: uppercase;
                 color: var(--ios-label-secondary);
                 margin: 0 0 7px 16px; }
"""

IOS_BODY = """<div class="demo">
__SWITCHER__
  <div class="phone" data-state="populated">
    <nav class="ios-navbar">
      <span class="ios-navbar__title">__SCREEN1__</span>
      <button class="ios-btn ios-navbar__action" aria-label="Add __THING__">
        <svg viewBox="0 0 24 24" width="22" height="22" fill="none"
             stroke="currentColor" stroke-width="2" stroke-linecap="round"
             aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>
      </button>
    </nav>

    <main class="screen">
      <section class="state state--populated">
        <p class="sectionhead">Today</p>
        <ul class="ios-list">
__ROWS__
        </ul>
      </section>

      <section class="state state--loading">
        <p class="sectionhead">Today</p>
        <ul class="ios-list">
__SKELROWS__
        </ul>
      </section>

__EMPTY__
__ERROR__
    </main>

    <nav class="ios-tabbar">
__TABS__
    </nav>
  </div>
</div>
"""


# ------------------------------------------------------------------ web

WEB_CSS = """
  .app { display: grid; grid-template-columns: 244px 1fr;
         min-height: 100vh; }
  .side { background: var(--ios-bg-card); padding: 20px 12px;
          border-right: 1px solid var(--ios-separator); }
  .side__brand { font: var(--ios-text-headline);
                 letter-spacing: var(--ios-track-headline);
                 padding: 0 12px 16px; }
  .side a { display: block; padding: 9px 12px; border-radius: 8px;
            min-height: var(--ios-hit-target, 44px); box-sizing: border-box;
            font: var(--ios-text-subhead); text-decoration: none;
            color: var(--ios-label); }
  .side a[aria-current="page"] { background: var(--ios-accent); color: #fff; }
  .main { padding: 28px 32px; max-width: 900px; }
  .main h1 { font: var(--ios-text-title1);
             letter-spacing: var(--ios-track-title1); margin: 0 0 20px; }
  .card { background: var(--ios-bg-card);
          border-radius: var(--ios-radius-card, 12px);
          padding: 18px 20px; margin-bottom: 12px;
          border: 1px solid var(--ios-separator); }
  .card__title { font: var(--ios-text-headline);
                 letter-spacing: var(--ios-track-headline); margin: 0 0 4px; }
  .card__meta { font: var(--ios-text-footnote);
                color: var(--ios-label-secondary); margin: 0; }

  /* A web app is not a phone. The structure transfers -- navigation,
     modality, states, hit targets -- the chrome does not, so there is
     no tab bar here on purpose. */
  @media (max-width: 720px) {
    .app { grid-template-columns: 1fr; }
    .side { border-right: 0; border-bottom: 1px solid var(--ios-separator);
            display: flex; gap: 4px; overflow-x: auto; }
    .side__brand { display: none; }
    .main { padding: 20px 16px; }
  }
"""

WEB_BODY = """<div class="demo">
__SWITCHER__
  <div class="app" data-state="populated">
    <aside class="side">
      <div class="side__brand">__NAME__</div>
__NAVLINKS__
    </aside>

    <main class="main">
      <h1>__SCREEN1__</h1>

      <section class="state state--populated">
__CARDS__
      </section>

      <section class="state state--loading">
__SKELCARDS__
      </section>

__EMPTY__
__ERROR__
    </main>
  </div>
</div>
"""


# ------------------------------------------------------------ marketing

MKT_CSS = """
  /* Deliberately not iOS. The HIG does not govern apple.com, and a
     marketing page built to it becomes a Settings screen with marketing
     copy in it. What carries over is the craft -- the optical sizing,
     the tracking, the contrast pass -- not the chrome. */
  .demo { background: var(--ios-bg-card); }
  .page { max-width: 1080px; margin: 0 auto; padding: 0 24px; }
  .hero { padding: 96px 0 72px; }
  .hero h1 { max-width: 15ch; font-size: clamp(44px, 8vw, 84px); line-height: 1.03;
             letter-spacing: -0.03em; font-weight: var(--ios-weight-semibold);
             font-optical-sizing: auto; margin: 0 0 20px; }
  .hero p { font-size: clamp(19px, 2.2vw, 24px); line-height: 1.45;
            letter-spacing: -0.01em; color: var(--ios-label-secondary);
            max-width: 34ch; margin: 0 0 32px; }
  .row { display: flex; gap: 12px; flex-wrap: wrap; }
  .ios-btn--tinted { color: var(--accent-text-safe); }
  /* A marketing CTA carries more weight than a list-row button. */
  .hero .ios-btn { min-height: 52px; padding: 0 26px;
                   font: var(--ios-text-headline);
                   letter-spacing: var(--ios-track-headline); }
  .sec { padding: 64px 0; border-top: 1px solid var(--ios-separator); }
  .sec h2 { font-size: clamp(30px, 4vw, 44px); line-height: 1.1;
            letter-spacing: -0.02em; font-weight: var(--ios-weight-semibold);
            margin: 0 0 14px; max-width: 18ch; }
  .sec p { font-size: 18px; line-height: 1.55; max-width: 58ch;
           color: var(--ios-label-secondary); margin: 0; }
  .grid { display: grid; gap: 28px; margin-top: 36px;
          grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); }
  .grid h3 { font: var(--ios-text-headline);
             letter-spacing: var(--ios-track-headline); margin: 0 0 6px; }
  .grid p { font: var(--ios-text-subhead); }

  /* Even a marketing page has states: the one form on it. */
  .signup { padding: 64px 0 96px; border-top: 1px solid var(--ios-separator); }
  .signup form { display: flex; gap: 10px; flex-wrap: wrap;
                 max-width: 440px; margin-top: 18px; }
  .signup .ios-field { flex: 1 1 220px; }
"""

MKT_BODY = """<div class="demo">
__SWITCHER__
  <div data-state="populated">
    <div class="page">
      <section class="hero">
        <h1>__HEADLINE__</h1>
        <p>__SUB__</p>
        <div class="row">
          <button class="ios-btn ios-btn--filled">__EMPTY_CTA__</button>
          <button class="ios-btn ios-btn--tinted">See how it works</button>
        </div>
      </section>

      <section class="sec">
        <h2>The argument this section makes</h2>
        <p>One idea per section, and each one earns its scroll. Replace
          this with the actual case -- what changes for someone using
          __NAME__ that did not before.</p>
        <div class="grid">
          <div><h3>First point</h3><p>Concrete, not adjectival.</p></div>
          <div><h3>Second point</h3><p>Something a competitor cannot say.</p></div>
          <div><h3>Third point</h3><p>The objection, answered.</p></div>
        </div>
      </section>

      <section class="signup">
        <h2>__EMPTY_CTA__</h2>
        <section class="state state--populated">
          <form onsubmit="return false">
            <input class="ios-field" type="email" placeholder="you@example.com"
                   aria-label="Email address">
            <button class="ios-btn ios-btn--filled">Sign up</button>
          </form>
        </section>

        <section class="state state--loading">
          <form onsubmit="return false">
            <input class="ios-field" type="email" value="you@example.com" disabled
                   aria-label="Email address">
            <!-- Keep the label on a submitting button. Swapping it for a
                 spinner loses the only thing that says what is happening. -->
            <button class="ios-btn ios-btn--filled" disabled>Signing up...</button>
          </form>
        </section>

__EMPTY__
__ERROR__
      </section>
    </div>
  </div>
</div>
"""


# ------------------------------------------------------------- assembly

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "brand"


def rows(screen, thing):
    demo = [("Overnight oats", "12 min"), ("Sheet-pan chicken", "35 min"),
            ("Miso soup", "8 min")]
    out = []
    for title, value in demo:
        out.append(
            '          <li class="ios-list__row ios-list__row--tappable">\n'
            f'            <span class="rowicon" aria-hidden="true">'
            f'{title[0].upper()}</span>\n'
            f'            <span class="ios-list__title">{title}</span>\n'
            f'            <span class="ios-list__value">{value}</span>\n'
            '            <span class="ios-list__chevron" aria-hidden="true">'
            '&rsaquo;</span>\n'
            '          </li>')
    return "\n".join(out)


def skel_rows(n=3):
    out = []
    for i in range(n):
        w = (72, 54, 63)[i % 3]
        out.append(
            '          <li class="ios-list__row" aria-hidden="true">\n'
            '            <span class="skel" style="width:29px;height:29px;'
            'border-radius:7px;flex:none"></span>\n'
            f'            <span class="skel" style="width:{w}%"></span>\n'
            '          </li>')
    return "\n".join(out)


def cards():
    demo = [("Overnight oats", "12 min - 4 servings"),
            ("Sheet-pan chicken", "35 min - 2 servings"),
            ("Miso soup", "8 min - 2 servings")]
    return "\n".join(
        f'        <article class="card">\n'
        f'          <h2 class="card__title">{t}</h2>\n'
        f'          <p class="card__meta">{m}</p>\n'
        f'        </article>' for t, m in demo)


def skel_cards(n=3):
    return "\n".join(
        '        <div class="card" aria-hidden="true">\n'
        f'          <div class="skel" style="width:{(46,58,38)[i%3]}%;'
        'height:1.2em;margin-bottom:8px"></div>\n'
        '          <div class="skel" style="width:30%;height:.9em"></div>\n'
        '        </div>' for i in range(n))


# Placeholder tab glyphs. Drawn rather than set in a font, because SF
# Symbols is not licensed for the web and a lone "o" in every slot reads
# as a missing icon rather than a stand-in -- which invites leaving it
# there. currentColor so the selected tab tints with the rest.
TAB_GLYPHS = [
    '<path d="M3 10.5 12 4l9 6.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
    '<path d="M4 6h16M4 12h16M4 18h16"/>',
    '<path d="M5 4h14v16l-7-4-7 4z"/>',
    '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4.4 3.6-7 8-7s8 2.6 8 7"/>',
    '<circle cx="12" cy="12" r="3.2"/><path d="M12 2v3m0 14v3M2 12h3m14 0h3'
    'M4.9 4.9l2.1 2.1m10 10 2.1 2.1m0-14.2-2.1 2.1m-10 10-2.1 2.1"/>',
]


def tabs(screens):
    out = []
    for i, s in enumerate(screens):
        sel = ' aria-selected="true"' if i == 0 else ""
        g = TAB_GLYPHS[i % len(TAB_GLYPHS)]
        icon = (f'<svg viewBox="0 0 24 24" width="25" height="25" '
                f'fill="none" stroke="currentColor" stroke-width="1.8" '
                f'stroke-linecap="round" stroke-linejoin="round" '
                f'aria-hidden="true">{g}</svg>')
        out.append(f'      <button class="ios-tabbar__item"{sel}>'
                   f'{icon}{s}</button>')
    return "\n".join(out)


def navlinks(screens):
    out = []
    for i, s in enumerate(screens):
        cur = ' aria-current="page"' if i == 0 else ""
        out.append(f'      <a href="#"{cur}>{s}</a>')
    return "\n".join(out)


def compose(kind, name, screens, thing):
    empty_cta = f"Add your first {thing.rstrip('s')}"
    empty_body = (f"Everything you save shows up here. "
                  f"Start with one and the rest gets easier.")

    empty = (EMPTY_PANEL.replace("__THING__", thing)
             .replace("__EMPTY_BODY__", empty_body)
             .replace("__EMPTY_CTA__", empty_cta))
    error = ERROR_PANEL.replace("__THING__", thing)

    if kind == "marketing":
        css, body = MKT_CSS, MKT_BODY
        body = (body.replace("__HEADLINE__", f"{name}, without the faff.")
                .replace("__SUB__",
                         "One sentence that says what it is and who it is "
                         "for. Replace this before anyone sees it."))
    elif kind == "web":
        css, body = WEB_CSS, WEB_BODY
        body = (body.replace("__NAVLINKS__", navlinks(screens))
                .replace("__CARDS__", cards())
                .replace("__SKELCARDS__", skel_cards()))
    else:
        css, body = IOS_CSS, IOS_BODY
        body = (body.replace("__ROWS__", rows(screens[0], thing))
                .replace("__SKELROWS__", skel_rows())
                .replace("__TABS__", tabs(screens)))

    body = (body.replace("__SWITCHER__", SWITCHER)
            .replace("__EMPTY__", empty)
            .replace("__ERROR__", error)
            .replace("__SCREEN1__", screens[0])
            .replace("__EMPTY_CTA__", empty_cta)
            .replace("__NAME__", name))

    head = HEAD.replace("__NAME__", name)
    return (head + "\n<style>" + STATE_CSS + css + "</style>\n\n"
            + body + STATE_JS)


README = """# __NAME__

Scaffolded by `apple-design`'s `new_project.py`. What is here already
works: open `index.html` with no server and no network.

    index.html      one screen, four states, switcher at the top
    theme.css       generated from __BRAND__ -- regenerate, do not hand-edit
    vendor/         Apple's measured tokens, the component recipes, the fonts

## What to change

The content. The rows, the copy, the hierarchy, which screen comes
first -- that is the design, and it is the part no generator does.

## What not to change

**The link order in `index.html`.** Fonts, tokens, components, then
`theme.css` last. Move the theme earlier and the component recipes
overwrite the brand palette; the page still renders, in Apple's blue,
which is why this is worth a line of its own.

**`theme.css` by hand.** Regenerate it:

    python3 build_theme.py "__BRAND__" --name __SLUG__ -o theme.css

It ends with a bridge aliasing the brand tokens onto the `--ios-*` names
the recipes read. Hand-editing loses the bridge and you get a brand
palette next to Apple-blue buttons.

## Before calling it done

    python3 check_design.py __OUT__

That checks what a screenshot cannot: link order, the bridge surviving,
no CDN, every state present, contrast, and no overflow at phone width.
"""


def main():
    ap = argparse.ArgumentParser(
        description="Scaffold a working project in Apple's structure.")
    ap.add_argument("--name", required=True, help="product name")
    ap.add_argument("--brand", required=True, help='brand colour, "#C1552E"')
    ap.add_argument("--kind", default="ios",
                    choices=["ios", "web", "marketing", "cross"],
                    help="decides the shape; marketing gets no iOS chrome")
    ap.add_argument("--screens", default="Home,Browse,Settings",
                    help="comma-separated, first one is shown")
    ap.add_argument("--thing", default="recipes",
                    help='what the app holds, for empty-state copy')
    ap.add_argument("-o", "--out", required=True, help="output directory")
    a = ap.parse_args()

    if not os.path.isdir(KIT):
        sys.exit(f"apple-ui-kit not found next to this skill ({KIT}).\n"
                 "Both skills need to be installed; the vendored tokens, "
                 "components and fonts come from there.")

    screens = [s.strip() for s in a.screens.split(",") if s.strip()]
    if not screens:
        sys.exit("--screens needs at least one name")
    if len(screens) > 5 and a.kind in ("ios", "cross"):
        print(f"note: {len(screens)} tabs. Apple's own limit is five; past "
              f"that they are not all top-level, or it wants a sidebar.",
              file=sys.stderr)

    out = os.path.abspath(a.out)
    vendor = os.path.join(out, "vendor")
    os.makedirs(os.path.join(vendor, "fonts"), exist_ok=True)

    shutil.copy2(os.path.join(KIT, "tokens", "ios-tokens.css"), vendor)
    shutil.copy2(os.path.join(KIT, "ios-components.css"), vendor)
    for f in os.listdir(os.path.join(KIT, "fonts")):
        shutil.copy2(os.path.join(KIT, "fonts", f),
                     os.path.join(vendor, "fonts", f))

    name = slug(a.name)
    try:
        css, notes = build_theme.build(a.brand, name)
    except ValueError as e:
        sys.exit(str(e))
    open(os.path.join(out, "theme.css"), "w", encoding="utf-8").write(css)

    kind = "ios" if a.kind == "cross" else a.kind
    html = compose(kind, a.name, screens, a.thing)
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(html)

    open(os.path.join(out, "README.md"), "w", encoding="utf-8").write(
        README.replace("__NAME__", a.name).replace("__BRAND__", a.brand)
        .replace("__SLUG__", name).replace("__OUT__", a.out))

    # relpath is friendly from inside the project and absurd from
    # anywhere else ("../../../../tmp/x/y/proj"), so take whichever
    # actually reads as a path someone could retype.
    rel = min(os.path.relpath(out), out, key=len)
    check = os.path.join(HERE, "check_design.py")
    check_rel = min(os.path.relpath(check), check, key=len)
    print(f"scaffolded {rel}/")
    print(f"  index.html   {a.kind} shape, {len(screens)} screens, 4 states")
    print(f"  theme.css    {a.brand} -> {name}-*, bridged to --ios-*")
    print(f"  vendor/      tokens, components, fonts (offline)")
    print()
    for n in notes:
        print("  contrast: " + n)
    print()
    print(f"next: edit the content in {rel}/index.html, then")
    print(f"      python3 {check_rel} {rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
