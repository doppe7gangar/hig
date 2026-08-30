#!/usr/bin/env python3
"""Scaffold a working design project without choosing its composition by accident.

The generator owns infrastructure:
- vendored fonts and measured UI-kit files
- brand theme + --ios-* bridge
- reachable populated/loading/empty/error states
- a starter composition chosen explicitly by spatial model

It does not own art direction. The caller chooses the spatial model after the
product hierarchy is understood. Web projects therefore require --model
instead of silently defaulting to "sidebar + cards".
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


HEAD = """<!doctype html>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__NAME__</title>

<!-- Order is load-bearing: fonts, measured tokens, component recipes,
     then the brand theme LAST so its bridge wins. -->
<link rel="stylesheet" href="vendor/fonts/inter.css">
<link rel="stylesheet" href="vendor/fonts/sf.css">
<link rel="stylesheet" href="vendor/ios-tokens.css">
<link rel="stylesheet" href="vendor/ios-components.css">
<link rel="stylesheet" href="theme.css">
"""

STATE_CSS = """
  .demo { min-height: 100vh; display: flex; flex-direction: column;
          background: var(--ios-bg); color: var(--ios-label);
          font: var(--ios-text-body); }
  .demo > :not(.demo__bar) { flex: 1; min-height: 0; }
  .demo__bar { display: flex; gap: 6px; flex-wrap: wrap; padding: 10px 16px;
               border-bottom: 1px solid var(--ios-separator);
               background: var(--ios-bg-card); }
  .demo__bar button { min-height: 32px; padding: 6px 12px; border-radius: 999px;
                      border: 1px solid var(--ios-separator); background: transparent;
                      color: var(--ios-label-secondary); cursor: pointer;
                      font: var(--ios-text-footnote); }
  .demo__bar button[aria-pressed="true"] {
      background: color-mix(in srgb, var(--ios-accent) 16%, transparent);
      border-color: color-mix(in srgb, var(--ios-accent) 45%, transparent);
      color: var(--ios-label); font-weight: 590; }

  /* Any button that is not filled is accent-coloured *text* -- plain,
     tinted, a bare navigation-bar action -- so it needs 4.5:1, while
     --ios-accent is tuned for the 3:1 a fill needs. Scoping this to
     --tinted alone left a navigation-bar "+" at 3.73:1 on a dark brand.
     Shared, so a new spatial model cannot be written without it. */
  .ios-btn:not(.ios-btn--filled):not(.ios-btn--destructive) {
      color: var(--accent-text-safe); }
  /* And a filled button takes the label the contrast pass chose, rather
     than the kit's hard-coded white. */
  .ios-btn--filled:not(.ios-btn--destructive) { color: var(--ios-on-accent); }

  .state { display: none; }
  [data-state="populated"] .state--populated,
  [data-state="loading"] .state--loading,
  [data-state="empty"] .state--empty,
  [data-state="error"] .state--error { display: block; }

  .skel { height: 1em; border-radius: 6px; background: var(--ios-fill-control);
          animation: skel 1.4s ease-in-out infinite; }
  @keyframes skel { 0%,100% { opacity: .55 } 50% { opacity: .25 } }
  @media (prefers-reduced-motion: reduce) { .skel { animation: none; } }

  .unavailable { max-width: 460px; margin: 0 auto; padding: 72px 28px;
                 text-align: center; }
  .unavailable__glyph { font-size: 42px; line-height: 1;
                        color: var(--ios-label-tertiary); }
  .unavailable__title { margin: 14px 0 5px; font: var(--ios-text-headline); }
  .unavailable__body { max-width: 34ch; margin: 0 auto 20px;
                       color: var(--ios-label-secondary);
                       font: var(--ios-text-subhead); }
"""

STATE_JS = """
<script>
  // The large title collapses into the bar on scroll, the way the
  // platform does it. Shown rather than described, because "it
  // collapses" is the sort of claim a static mockup makes and never has
  // to honour.
  for (const ph of document.querySelectorAll('.phone')) {
    const dev = ph.closest('.device');
    if (!dev) continue;
    const sync = () => { dev.dataset.scrolled = ph.scrollTop > 24 ? '1' : '0'; };
    ph.addEventListener('scroll', sync, {passive: true});
    sync();
  }

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
</div>"""

EMPTY_PANEL = """      <section class="state state--empty">
        <div class="ios-empty">
          <div class="ios-empty__glyph" data-sf-symbol="tray"
               aria-hidden="true">
            <svg viewBox="0 0 24 24" width="38" height="38" fill="none"
                 stroke="currentColor" stroke-width="1.4" stroke-linecap="round"
                 stroke-linejoin="round"><path d="M3 13h5l2 3h4l2-3h5"/><path d="M5 5l-2 8v5a1 1 0 0 0 1 1h16a1 1 0 0 0 1-1v-5l-2-8z"/></svg>
          </div>
          <h2 class="ios-empty__title">No __THING__ yet</h2>
          <p class="ios-empty__body">__EMPTY_BODY__</p>
          <button class="ios-btn ios-btn--filled ios-empty__action">__EMPTY_CTA__</button>
        </div>
      </section>
"""

ERROR_PANEL = """      <section class="state state--error">
        <div class="ios-empty">
          <div class="ios-empty__glyph" data-sf-symbol="exclamationmark.triangle"
               aria-hidden="true">
            <svg viewBox="0 0 24 24" width="38" height="38" fill="none"
                 stroke="currentColor" stroke-width="1.4" stroke-linecap="round"
                 stroke-linejoin="round"><path d="M12 3 2 20h20z"/><path d="M12 9v5m0 3v.5"/></svg>
          </div>
          <h2 class="ios-empty__title">Couldn't load __THING__</h2>
          <p class="ios-empty__body">Check your connection and try again.</p>
          <button class="ios-btn ios-btn--filled ios-empty__action">Try Again</button>
        </div>
      </section>
"""


# ---------------------------------------------------------------- iOS

IOS_CSS = """
  /* The deliverable is an app screen, not a board of artboards. The same
     markup shown as a stack of panels with commentary between them reads
     as a specification; shown once, in a device, with a status bar, it
     reads as the product. Nothing about the design changes -- only what
     a reviewer is looking at, which turned out to be a large share of
     why finished work did not look like iOS. The commentary belongs in
     DESIGN.md, where it already lives. */
  .stage { min-height: 100vh; display: grid; place-items: center;
           padding: 32px 16px; background: #0E0E10; }
  .device { width: 393px; max-width: 100%; height: 852px; position: relative;
            display: flex; flex-direction: column; overflow: hidden;
            border-radius: 52px; background: var(--ios-bg);
            box-shadow: 0 0 0 11px #1C1C1E, 0 0 0 13px #3A3A3C,
                        0 26px 60px rgba(0,0,0,.45); }
  .statusbar { flex: none; height: 54px; display: flex; align-items: flex-end;
               justify-content: space-between; padding: 0 30px 6px;
               font: var(--ios-text-footnote); color: var(--ios-label);
               font-weight: var(--ios-weight-semibold); }
  .statusbar__glyphs { letter-spacing: 1px; }
  .phone { flex: 1; min-height: 0; width: 100%; display: flex;
           flex-direction: column; background: var(--ios-bg);
           overflow-y: auto; }
  @media (max-width: 460px) {
    /* On a real phone the device frame is a costume: the browser is
       already the frame. Shed it rather than draw a phone in a phone. */
    .stage { padding: 0; background: var(--ios-bg); place-items: stretch; }
    .device { width: 100%; height: 100vh; border-radius: 0; box-shadow: none; }
    .statusbar { display: none; }
  }
  .screen { flex: 1; padding: 16px var(--ios-gutter, 16px) 88px; }
  /* The kit's 11px row padding is measured for a text row: a 22px line
     box plus 11 above and below is exactly the 44pt target. A 29px icon
     does not fit that arithmetic and pushed every row to 51. iOS keeps
     the row at 44 and lets the icon take the padding, so the row with
     an icon gets 7px and lands back on the measured height. */
  .ios-list__row:has(.rowicon) { padding-top: 7px; padding-bottom: 7px; }
  /* A tinted symbol on nothing, which is what Apple's rows carry --
     Tips, Maps, Health all show a coloured glyph with no plate behind
     it. A filled tile with a letter in it is a Notion habit and reads
     as one. Replace the glyph with the real symbol when you have it. */
  .rowicon { width: 29px; height: 29px; flex: none; display: grid;
             place-items: center; color: var(--accent-text-safe);
             font: var(--ios-text-title3); }
  /* iOS 26 sets a section header as a title, not as a caption: 22pt
     bold, primary label, sentence case. The small uppercase grey
     footnote is the previous generation's grouped-list header -- see
     Tips ("Get Started", "Next Steps") and Pages ("Included with Apple
     Creator Studio"), all large and white. Getting this wrong makes a
     screen read as a settings pane whatever else is right. */
  .sectionhead { display: flex; align-items: baseline;
                 justify-content: space-between; gap: 12px;
                 margin: 22px 4px 8px; color: var(--ios-label);
                 font: var(--ios-text-title2);
                 font-weight: var(--ios-weight-bold);
                 letter-spacing: var(--ios-track-title2); }
  /* Apple pairs the header with an accent action rather than burying the
     rest of the list behind a chevron on the last row. */
  .sectionhead__action { font: var(--ios-text-body);
                         font-weight: var(--ios-weight-regular);
                         color: var(--accent-text-safe);
                         text-decoration: none;
                         /* An inline link is 15px tall and reads as text
                            rather than a control. Padded to the target
                            and pulled back out with a negative margin so
                            the baseline still lines up with the title. */
                         display: inline-flex; align-items: center;
                         min-height: var(--ios-hit-target);
                         padding: 0 4px; margin: -14px -4px; }
  /* The large title is the most recognisable thing about an iOS screen
     and the scaffold did not have one: a 17pt headline in the bar is the
     *collapsed* state, which is what you see after scrolling, not what a
     screen opens as. 34pt bold, left, under the bar, with the compact
     title in the bar hidden until it is earned. Real iOS swaps them on
     scroll; the script below does that so the collapse is visible rather
     than described. */
  /* At rest the bar carries no material: the large title is the screen's
     title and the area above it is just background, which is why Calendar
     and Health show content running straight up to the status bar. The
     glass arrives together with the compact title on scroll, so the bar
     appears exactly when it has something to hold. */
  .device:not([data-scrolled="1"]) .ios-navbar {
      background: none; backdrop-filter: none; border-color: transparent;
      /* The rim is drawn as a box-shadow, so clearing the border alone
         left the hairline exactly where the bar was meant to vanish. */
      box-shadow: none; }
  .device:not([data-scrolled="1"]) .ios-navbar::before { opacity: 0; }
  .ios-navbar { transition: background .18s ease;
                padding-top: 6px; padding-bottom: 6px; }
  /* Calendar and Pages float their actions rather than seating them in a
     bar: the capsule carries the material, the bar behind it is only
     there to hold the compact title once the large one has gone. */
  .ios-navbar .ios-controls { margin-left: auto; }
  .ios-navbar__title { opacity: 0; transition: opacity .18s ease; }
  .device[data-scrolled="1"] .ios-navbar__title { opacity: 1; }
  .largetitle { margin: 4px var(--ios-gutter, 16px) 8px;
                font: var(--ios-text-large-title);
                font-weight: var(--ios-weight-bold);
                letter-spacing: var(--ios-track-large-title);
                color: var(--ios-label); }
  .ios-list { margin: 0 0 22px; }
  .ios-tabbar__item[aria-selected="true"] { color: var(--accent-text-safe); }
"""

IOS_BODY = """<div class="demo">
__SWITCHER__
 <div class="stage">
  <div class="device" data-state="populated">
   <div class="statusbar" aria-hidden="true">
     <span>9:41</span>
     <span class="statusbar__glyphs">&#9679;&#9679;&#9679; &#9207; &#9632;</span>
   </div>
   <div class="phone">
    <nav class="ios-navbar">
      <span class="ios-navbar__title">__SCREEN1__</span>
      <div class="ios-glass ios-controls">
        <button class="ios-controls__item" data-sf-symbol="line.3.horizontal.decrease"
                aria-label="Filter __THING__">
          <svg viewBox="0 0 24 24" width="19" height="19" fill="none"
               stroke="currentColor" stroke-width="1.9" stroke-linecap="round"
               aria-hidden="true"><path d="M4 7h16M7 12h10M10 17h4"/></svg>
        </button>
        <button class="ios-controls__item" data-sf-symbol="plus"
                aria-label="Add __THING__">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="none"
               stroke="currentColor" stroke-width="2" stroke-linecap="round"
               aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>
        </button>
      </div>
    </nav>
    <h1 class="largetitle">__SCREEN1__</h1>
    <main class="screen">
      <section class="state state--populated">
        <p class="sectionhead">Today<a class="sectionhead__action" href="#">See All</a></p>
        <ul class="ios-list">
__ROWS__
        </ul>
      </section>
      <section class="state state--loading">
        <p class="sectionhead">Today<a class="sectionhead__action" href="#">See All</a></p>
        <ul class="ios-list">
__SKELROWS__
        </ul>
      </section>
__EMPTY__
__ERROR__
    </main>
__TABBAR__
   </div>
  </div>
 </div>
</div>
"""


# ------------------------------------------------------------ web models

WEB_BASE_CSS = """
  .web-shell { min-height: 100vh; background: var(--ios-bg-card); }
  .web-main { min-width: 0; }
  .eyebrow { margin: 0 0 7px; color: var(--ios-label-secondary);
             font: var(--ios-text-footnote); text-transform: uppercase;
             letter-spacing: .04em; }
  .page-title { margin: 0; font: var(--ios-text-title1);
                letter-spacing: var(--ios-track-title1); }
  .page-intro { max-width: 58ch; margin: 8px 0 0; color: var(--ios-label-secondary);
                font: var(--ios-text-subhead); }
  .rule { height: 1px; background: var(--ios-separator); }
  .meta { color: var(--ios-label-secondary); font: var(--ios-text-footnote); }
  .action-link { color: var(--accent-text-safe); text-decoration: none; }
  .action-link:hover { text-decoration: underline; }
  @media (max-width: 760px) {
    .page-title { font: var(--ios-text-title2); }
  }
"""

WORKSPACE_CSS = """
  .workspace { display: grid; grid-template-columns: 236px minmax(0, 1fr);
               min-height: 100vh; }
  .workspace__side { padding: 22px 12px; border-right: 1px solid var(--ios-separator);
                     background: color-mix(in srgb, var(--ios-bg) 76%, transparent); }
  .workspace__brand { padding: 0 10px 18px; font: var(--ios-text-headline); }
  .workspace__nav { display: grid; gap: 3px; }
  .workspace__nav a { min-height: 38px; display: flex; align-items: center;
                      padding: 0 10px; border-radius: 8px; color: var(--ios-label);
                      text-decoration: none; font: var(--ios-text-subhead); }
  .workspace__nav a[aria-current="page"] {
      background: color-mix(in srgb, var(--ios-accent) 14%, transparent);
      color: var(--ios-label); font-weight: 590; }
  .workspace__content { max-width: 980px; padding: 34px 42px 56px; }
  .workspace__head { margin-bottom: 30px; }
  .record-list { border-top: 1px solid var(--ios-separator); }
  .record { display: grid; grid-template-columns: minmax(0,1fr) auto;
            gap: 22px; padding: 17px 2px;
            border-bottom: 1px solid var(--ios-separator); }
  .record h2 { margin: 0 0 4px; font: var(--ios-text-headline); }
  .record p { margin: 0; color: var(--ios-label-secondary);
              font: var(--ios-text-footnote); }
  @media (max-width: 760px) {
    .workspace { grid-template-columns: 1fr; }
    .workspace__side { border-right: 0; border-bottom: 1px solid var(--ios-separator);
                       padding: 10px 12px; overflow-x: auto; }
    .workspace__brand { display: none; }
    .workspace__nav { display: flex; width: max-content; }
    .workspace__content { padding: 24px 18px 44px; }
  }
"""

WORKSPACE_BODY = """<div class="demo">
__SWITCHER__
  <div class="web-shell workspace" data-state="populated">
    <aside class="workspace__side">
      <div class="workspace__brand">__NAME__</div>
      <nav class="workspace__nav">__NAVLINKS__</nav>
    </aside>
    <main class="web-main workspace__content">
      <header class="workspace__head">
        <p class="eyebrow">Workspace</p>
        <h1 class="page-title">__SCREEN1__</h1>
        <p class="page-intro">The primary work belongs here. Secondary controls should remain contextual.</p>
      </header>
      <section class="state state--populated">
        <div class="record-list">__RECORDS__</div>
      </section>
      <section class="state state--loading">
        <div class="record-list">__SKELRECORDS__</div>
      </section>
__EMPTY__
__ERROR__
    </main>
  </div>
</div>
"""

LIST_DETAIL_CSS = """
  .listdetail { display: grid; grid-template-columns: minmax(280px, 34%) minmax(0, 1fr);
                min-height: 100vh; }
  .collection { border-right: 1px solid var(--ios-separator);
                background: color-mix(in srgb, var(--ios-bg) 72%, transparent); }
  .collection__head { padding: 28px 24px 18px; }
  .collection__items { border-top: 1px solid var(--ios-separator); }
  .collection__item { display: block; padding: 15px 24px;
                      border-bottom: 1px solid var(--ios-separator);
                      color: var(--ios-label); text-decoration: none; }
  .collection__item[aria-current="true"] {
      background: color-mix(in srgb, var(--ios-accent) 12%, transparent); }
  .collection__item[aria-current="true"] span { color: var(--ios-label); }
  .collection__item strong { display: block; font: var(--ios-text-headline); }
  .collection__item span { display: block; margin-top: 3px;
                           color: var(--ios-label-secondary);
                           font: var(--ios-text-footnote); }
  .detail { max-width: 780px; padding: 52px 54px; }
  .detail__hero { margin-bottom: 34px; }
  .detail__value { margin: 16px 0 2px; font-size: clamp(42px, 8vw, 74px);
                   line-height: .98; letter-spacing: -.045em; font-weight: 650; }
  .detail__section { max-width: 62ch; padding-top: 24px;
                     border-top: 1px solid var(--ios-separator); }
  .detail__section h2 { margin: 0 0 8px; font: var(--ios-text-headline); }
  .detail__section p { margin: 0; color: var(--ios-label-secondary); line-height: 1.55; }
  @media (max-width: 760px) {
    .listdetail { grid-template-columns: 1fr; }
    .collection { border-right: 0; }
    .detail { display: none; }
  }
"""

LIST_DETAIL_BODY = """<div class="demo">
__SWITCHER__
  <div class="web-shell listdetail" data-state="populated">
    <aside class="collection">
      <header class="collection__head">
        <p class="eyebrow">Collection</p>
        <h1 class="page-title">__SCREEN1__</h1>
      </header>
      <section class="state state--populated">
        <nav class="collection__items">__COLLECTION__</nav>
      </section>
      <section class="state state--loading">
        <div class="collection__items">__SKELCOLLECTION__</div>
      </section>
__EMPTY__
__ERROR__
    </aside>
    <main class="detail state state--populated">
      <div class="detail__hero">
        <p class="eyebrow">Selected item</p>
        <h2 class="page-title">Overnight oats</h2>
        <div class="detail__value">12 min</div>
        <p class="meta">4 servings · updated today</p>
      </div>
      <section class="detail__section">
        <h2>What matters</h2>
        <p>Put the selected object's important information here. Actions belong close to the object, not duplicated globally.</p>
      </section>
    </main>
  </div>
</div>
"""

DASHBOARD_CSS = """
  .summary { max-width: 1080px; margin: 0 auto; padding: 42px 30px 64px; }
  .summary__head { max-width: 720px; margin-bottom: 44px; }
  .hero-metric { padding: 10px 0 38px; }
  .hero-metric__value { margin: 0; font-size: clamp(64px, 11vw, 126px);
                        line-height: .88; letter-spacing: -.065em; font-weight: 650; }
  .hero-metric__context { margin: 15px 0 0; color: var(--ios-label-secondary);
                          font-size: 18px; line-height: 1.45; }
  .evidence { display: grid; grid-template-columns: 1.3fr .7fr; gap: 42px;
              padding-top: 28px; border-top: 1px solid var(--ios-separator); }
  .evidence h2 { margin: 0 0 14px; font: var(--ios-text-headline); }
  .trend { min-height: 210px; display: flex; align-items: end; gap: 8px; }
  .trend span { flex: 1; min-width: 8px; border-radius: 5px 5px 0 0;
                background: color-mix(in srgb, var(--ios-accent) 70%, transparent); }
  .facts { margin: 0; padding: 0; list-style: none; }
  .facts li { display: flex; justify-content: space-between; gap: 18px;
              padding: 12px 0; border-bottom: 1px solid var(--ios-separator); }
  .facts strong { font-weight: 590; }
  @media (max-width: 760px) {
    .summary { padding: 28px 18px 48px; }
    .evidence { grid-template-columns: 1fr; }
  }
"""

DASHBOARD_BODY = """<div class="demo">
__SWITCHER__
  <main class="web-shell summary" data-state="populated">
    <header class="summary__head">
      <p class="eyebrow">Summary</p>
      <h1 class="page-title">__SCREEN1__</h1>
      <p class="page-intro">Lead with the answer. Supporting metrics exist to explain it, not compete with it.</p>
    </header>
    <section class="state state--populated">
      <div class="hero-metric">
        <p class="hero-metric__value">68%</p>
        <p class="hero-metric__context">Best week since June · up 9 points from last week</p>
      </div>
      <div class="evidence">
        <section>
          <h2>Trend</h2>
          <div class="trend" aria-label="Seven-period trend">
            <span style="height:35%"></span><span style="height:46%"></span>
            <span style="height:43%"></span><span style="height:58%"></span>
            <span style="height:54%"></span><span style="height:64%"></span>
            <span style="height:78%"></span>
          </div>
        </section>
        <section>
          <h2>Supporting evidence</h2>
          <ul class="facts">
            <li><span>Completed</span><strong>34</strong></li>
            <li><span>Average time</span><strong>18 min</strong></li>
            <li><span>Change</span><strong>+9 pts</strong></li>
          </ul>
        </section>
      </div>
    </section>
    <section class="state state--loading">
      <div class="hero-metric"><div class="skel" style="width:42%;height:7em"></div></div>
      <div class="rule"></div>
      <div class="skel" style="width:100%;height:15em;margin-top:28px"></div>
    </section>
__EMPTY__
__ERROR__
  </main>
</div>
"""

DOCUMENT_CSS = """
  .document-shell { min-height: 100vh; }
  .document-top { position: sticky; top: 0; z-index: 3; display: flex;
                  justify-content: space-between; align-items: center; gap: 20px;
                  min-height: 52px; padding: 0 22px;
                  border-bottom: 1px solid var(--ios-separator);
                  background: color-mix(in srgb, var(--ios-bg-card) 88%, transparent);
                  backdrop-filter: blur(20px) saturate(150%); }
  .document-top strong { font: var(--ios-text-headline); }
  .document-actions { display: flex; gap: 8px; }
  .document { max-width: 760px; margin: 0 auto; padding: 76px 32px 120px; }
  .document h1 { max-width: 16ch; margin: 0 0 22px;
                 font-size: clamp(38px, 7vw, 64px); line-height: 1.02;
                 letter-spacing: -.04em; font-weight: 650; }
  .document .lede { max-width: 46ch; margin: 0 0 52px; color: var(--ios-label-secondary);
                    font-size: 20px; line-height: 1.5; }
  .document section { max-width: 64ch; margin-top: 34px; }
  .document h2 { margin: 0 0 9px; font: var(--ios-text-title3); }
  .document p { margin: 0; line-height: 1.7; }
  @media (max-width: 760px) {
    .document { padding: 54px 20px 90px; }
    .document-top { padding: 0 14px; }
  }
"""

DOCUMENT_BODY = """<div class="demo">
__SWITCHER__
  <div class="web-shell document-shell" data-state="populated">
    <header class="document-top">
      <strong>__NAME__</strong>
      <div class="document-actions">
        <button class="ios-btn ios-btn--tinted">Share</button>
        <button class="ios-btn ios-btn--filled">Done</button>
      </div>
    </header>
    <main class="document">
      <section class="state state--populated">
        <p class="eyebrow">__SCREEN1__</p>
        <h1>Put the work itself at the center.</h1>
        <p class="lede">A document or canvas interface should make the content dominant and keep controls available without turning them into the composition.</p>
        <section>
          <h2>First section</h2>
          <p>Use a clear reading column, strong type hierarchy, and contextual actions. The interface recedes until the user needs it.</p>
        </section>
        <section>
          <h2>Second section</h2>
          <p>Do not wrap every paragraph or tool in a card. The document is already the surface.</p>
        </section>
      </section>
      <section class="state state--loading">
        <div class="skel" style="width:58%;height:3.8em;margin-bottom:24px"></div>
        <div class="skel" style="width:86%;height:1.4em;margin-bottom:12px"></div>
        <div class="skel" style="width:70%;height:1.4em"></div>
      </section>
__EMPTY__
__ERROR__
    </main>
  </div>
</div>
"""

WEB_MODELS = {
    "workspace": (WORKSPACE_CSS, WORKSPACE_BODY),
    "list-detail": (LIST_DETAIL_CSS, LIST_DETAIL_BODY),
    "dashboard": (DASHBOARD_CSS, DASHBOARD_BODY),
    "document": (DOCUMENT_CSS, DOCUMENT_BODY),
}


# -------------------------------------------------------------- marketing

MKT_CSS = """
  .marketing { background: var(--ios-bg-card); }
  .mkt-nav { max-width: 1120px; margin: 0 auto; padding: 18px 28px;
             display: flex; justify-content: space-between; align-items: center; }
  .mkt-nav strong { font: var(--ios-text-headline); }
  .mkt-page { max-width: 1120px; margin: 0 auto; padding: 0 28px; }
  .hero { padding: 104px 0 88px; }
  .hero h1 { max-width: 13ch; margin: 0 0 22px; font-size: clamp(48px, 9vw, 96px);
             line-height: .98; letter-spacing: -.055em; font-weight: 650; }
  .hero p { max-width: 34ch; margin: 0 0 30px; color: var(--ios-label-secondary);
            font-size: clamp(20px, 2.2vw, 26px); line-height: 1.42; }
  .mkt-actions { display: flex; gap: 10px; flex-wrap: wrap; }
  .mkt-actions .ios-btn { min-height: 50px; padding: 0 24px; }
  .story { display: grid; grid-template-columns: .75fr 1.25fr; gap: 80px;
           padding: 72px 0; border-top: 1px solid var(--ios-separator); }
  .story h2 { margin: 0; font-size: clamp(30px, 4vw, 46px);
              line-height: 1.08; letter-spacing: -.03em; }
  .story__body { max-width: 58ch; }
  .story__body p { margin: 0 0 22px; color: var(--ios-label-secondary);
                   font-size: 18px; line-height: 1.65; }
  .proof { margin: 26px 0 0; padding: 0; list-style: none; }
  .proof li { padding: 14px 0; border-top: 1px solid var(--ios-separator); }
  .signup { padding: 72px 0 100px; border-top: 1px solid var(--ios-separator); }
  .signup form { display: flex; gap: 10px; max-width: 460px; flex-wrap: wrap; }
  .signup .ios-field { flex: 1 1 230px; }
  @media (max-width: 760px) {
    .mkt-nav, .mkt-page { padding-left: 20px; padding-right: 20px; }
    .hero { padding: 72px 0 62px; }
    .story { grid-template-columns: 1fr; gap: 24px; padding: 54px 0; }
  }
"""

MKT_BODY = """<div class="demo">
__SWITCHER__
  <div class="marketing" data-state="populated">
    <nav class="mkt-nav"><strong>__NAME__</strong><a class="action-link" href="#signup">Get started</a></nav>
    <main class="mkt-page">
      <section class="hero">
        <p class="eyebrow">A clear category or promise</p>
        <h1>__HEADLINE__</h1>
        <p>__SUB__</p>
        <div class="mkt-actions">
          <button class="ios-btn ios-btn--filled">__EMPTY_CTA__</button>
          <button class="ios-btn ios-btn--tinted">See how it works</button>
        </div>
      </section>
      <section class="story">
        <h2>Make one argument per section.</h2>
        <div class="story__body">
          <p>Marketing is narrative, not a grid of feature cards. State the claim, show proof, answer the objection, then move to the next idea.</p>
          <ul class="proof">
            <li>Concrete proof point</li>
            <li>Product demonstration or evidence</li>
            <li>Meaningful differentiation</li>
          </ul>
        </div>
      </section>
      <section class="signup" id="signup">
        <h2>__EMPTY_CTA__</h2>
        <section class="state state--populated">
          <form onsubmit="return false">
            <input class="ios-field" type="email" placeholder="you@example.com" aria-label="Email address">
            <button class="ios-btn ios-btn--filled">Sign up</button>
          </form>
        </section>
        <section class="state state--loading">
          <form onsubmit="return false">
            <input class="ios-field" type="email" value="you@example.com" disabled aria-label="Email address">
            <button class="ios-btn ios-btn--filled" disabled>Signing up...</button>
          </form>
        </section>
__EMPTY__
__ERROR__
      </section>
    </main>
  </div>
</div>
"""


# ---------------------------------------------------------------- helpers

def _camel_file(name):
    """HarborColor.swift rather than harbor-color.swift."""
    parts = re.split(r"[^A-Za-z0-9]+", name)
    return "".join(p[:1].upper() + p[1:] for p in parts if p) or "Brand"


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "brand"


def navlinks(screens):
    out = []
    for i, screen in enumerate(screens):
        cur = ' aria-current="page"' if i == 0 else ""
        out.append(f'<a href="#"{cur}>{screen}</a>')
    return "\n".join(out)


def rows(thing):
    demo = [("Overnight oats", "12 min"), ("Sheet-pan chicken", "35 min"),
            ("Miso soup", "8 min")]
    out = []
    for title, value in demo:
        out.append(
            '          <li class="ios-list__row ios-list__row--tappable">\n'
            f'            <span class="rowicon" data-sf-symbol="fork.knife"'
            f' aria-hidden="true">{title[0]}</span>\n'
            f'            <span class="ios-list__title">{title}</span>\n'
            f'            <span class="ios-list__value">{value}</span>\n'
            '            <span class="ios-list__chevron" aria-hidden="true">&rsaquo;</span>\n'
            '          </li>')
    return "\n".join(out)


def skel_rows(n=3):
    return "\n".join(
        '          <li class="ios-list__row" aria-hidden="true">\n'
        '            <span class="skel" style="width:29px;height:29px;flex:none"></span>\n'
        f'            <span class="skel" style="width:{(72,54,63)[i%3]}%"></span>\n'
        '          </li>' for i in range(n))


# The symbol each placeholder stands for. SF Symbols cannot ship here --
# Apple's licence covers use inside apps running on Apple platforms, not
# extraction into a web kit, and the library is not in this repo -- so
# the drawing is a stand-in and the *name* is the deliverable. An
# engineer reading this markup gets Image(systemName: "house.fill"),
# which is the part that has to be exact.
TAB_SYMBOLS = ["house.fill", "list.bullet", "bookmark.fill",
               "person.crop.circle", "gearshape.fill"]

TAB_GLYPHS = [
    '<path d="M3 10.5 12 4l9 6.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
    '<path d="M4 6h16M4 12h16M4 18h16"/>',
    '<path d="M5 4h14v16l-7-4-7 4z"/>',
    '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4.4 3.6-7 8-7s8 2.6 8 7"/>',
    '<circle cx="12" cy="12" r="3.2"/><path d="M12 2v3m0 14v3M2 12h3m14 0h3"/>',
]


def tabs(screens):
    out = []
    for i, screen in enumerate(screens):
        selected = ' aria-selected="true"' if i == 0 else ""
        glyph = TAB_GLYPHS[i % len(TAB_GLYPHS)]
        sym = TAB_SYMBOLS[i % len(TAB_SYMBOLS)]
        icon = (f'<svg data-sf-symbol="{sym}" viewBox="0 0 24 24" width="25" height="25" fill="none" '
                f'stroke="currentColor" stroke-width="1.8" aria-hidden="true">{glyph}</svg>')
        out.append(f'      <button class="ios-tabbar__item"{selected}>{icon}{screen}</button>')
    return "\n".join(out)


def records():
    demo = [("Overnight oats", "12 min · 4 servings"),
            ("Sheet-pan chicken", "35 min · 2 servings"),
            ("Miso soup", "8 min · 2 servings")]
    return "\n".join(
        f'<article class="record"><div><h2>{title}</h2><p>{meta}</p></div>'
        f'<a class="action-link" href="#">Open</a></article>'
        for title, meta in demo)


def skel_records(n=3):
    return "\n".join(
        '<article class="record" aria-hidden="true"><div>'
        f'<div class="skel" style="width:{(44,58,36)[i%3]}%;height:1.2em;margin-bottom:8px"></div>'
        '<div class="skel" style="width:30%;height:.9em"></div></div></article>'
        for i in range(n))


def collection_items():
    demo = [("Overnight oats", "12 min · 4 servings"),
            ("Sheet-pan chicken", "35 min · 2 servings"),
            ("Miso soup", "8 min · 2 servings")]
    # The attribute is built outside the f-string: an expression part
    # cannot contain a backslash before Python 3.12, and this file has to
    # import on the interpreter people actually have.
    out = []
    for i, (title, meta) in enumerate(demo):
        cur = ' aria-current="true"' if i == 0 else ''
        out.append(f'<a class="collection__item" href="#"{cur}>'
                   f'<strong>{title}</strong><span>{meta}</span></a>')
    return "\n".join(out)


def skel_collection(n=3):
    return "\n".join(
        '<div class="collection__item" aria-hidden="true">'
        f'<div class="skel" style="width:{(58,72,46)[i%3]}%;height:1.2em;margin-bottom:8px"></div>'
        '<div class="skel" style="width:38%;height:.9em"></div></div>'
        for i in range(n))


def panels(thing):
    singular = thing.rstrip("s")
    empty_cta = f"Add your first {singular}"
    empty_body = f"Everything you save shows up here. Start with one and build from there."
    empty = (EMPTY_PANEL.replace("__THING__", thing)
             .replace("__EMPTY_BODY__", empty_body)
             .replace("__EMPTY_CTA__", empty_cta))
    error = ERROR_PANEL.replace("__THING__", thing)
    return empty_cta, empty, error


def compose(kind, model, name, screens, thing):
    empty_cta, empty, error = panels(thing)

    if kind == "marketing":
        css = WEB_BASE_CSS + MKT_CSS
        body = (MKT_BODY.replace("__HEADLINE__", f"{name}, with less in the way.")
                .replace("__SUB__", "One sentence that says what changes for the person using it."))
        chosen_model = "editorial"
    elif kind == "web":
        css_model, body = WEB_MODELS[model]
        css = WEB_BASE_CSS + css_model
        body = (body.replace("__NAVLINKS__", navlinks(screens))
                .replace("__RECORDS__", records())
                .replace("__SKELRECORDS__", skel_records())
                .replace("__COLLECTION__", collection_items())
                .replace("__SKELCOLLECTION__", skel_collection()))
        chosen_model = model
    else:
        css = IOS_CSS
        body = (IOS_BODY.replace("__ROWS__", rows(thing))
                .replace("__SKELROWS__", skel_rows()))
        if model == "tabs":
            if len(screens) > 5:
                raise ValueError("tabs chosen with more than five screens; reconsider hierarchy or use --model stack")
            tabbar = '    <nav class="ios-tabbar">\n' + tabs(screens) + '\n    </nav>'
        else:
            tabbar = ""
        body = body.replace("__TABBAR__", tabbar)
        chosen_model = model

    body = (body.replace("__SWITCHER__", SWITCHER)
            .replace("__EMPTY__", empty)
            .replace("__ERROR__", error)
            .replace("__SCREEN1__", screens[0])
            .replace("__EMPTY_CTA__", empty_cta)
            .replace("__NAME__", name)
            .replace("__THING__", thing))

    head = HEAD.replace("__NAME__", name)
    html = head + "\n<style>" + STATE_CSS + css + "</style>\n\n" + body + STATE_JS
    return html, chosen_model


README = """# __NAME__

This scaffold deliberately separates **design direction** from infrastructure.

    index.html      starter composition + four reachable states
    DESIGN.md       rationale to replace before polishing
    theme.css       generated from __BRAND__; regenerate, do not hand-edit
    vendor/         measured tokens, component recipes, local fonts

## Chosen direction

- kind: `__KIND__`
- spatial model: `__MODEL__`
- character: `__CHARACTER__`

The scaffold is not the design. Replace its sample content and recompose it
around your own hierarchy -- but keep the ios-* recipes it uses; they carry
the measured metrics, and hand-rolling them is what makes a build read as
almost-iOS
around the real hierarchy. Do not preserve a region merely because the
generator emitted it.

## Infrastructure not to break

Keep `theme.css` last in the stylesheet order. Keep fonts local. Regenerate
`theme.css` instead of editing its bridge by hand:

    python3 build_theme.py "__BRAND__" --name __SLUG__ -o theme.css

## Before calling it done

    python3 check_design.py __OUT__

After the mechanical check passes, read
`references/visual-critique.md` and perform the reduction pass. A mechanically
valid interface can still be visually generic.
"""

DESIGN = """# Design direction

## Product character

**Dominant:** __CHARACTER__

Write one supporting quality only if it clarifies the direction.

## Platform mode

`__KIND__`

For web, transfer Apple principles rather than iOS chrome. For native Apple
platform work, verify behavior and platform claims against `apple-hig`.

## Spatial model

`__MODEL__`

Why this model matches the user's primary task:

> Replace this with one sentence before polishing the interface.

## Information hierarchy

1. **Primary** — what the user came here to see or do.
2. **Secondary** — context needed to understand or act on the primary.
3. **Tertiary** — supporting detail that can recede.
4. **Contextual** — controls shown only when relevant.

Replace those placeholders with actual product content.

## Reduction pass

Before polish:
- remove containers that do not communicate a boundary or grouping
- turn unnecessary borders into spacing
- make secondary controls contextual where possible
- confirm one primary action
- confirm density fits the platform
- remove decorative glass, blur, shadows, pills, and motion
- check that typography still carries hierarchy with containers mentally removed

Then run `check_design.py` and the visual critique.
"""


def main():
    ap = argparse.ArgumentParser(
        description="Scaffold design infrastructure after choosing a spatial model.")
    ap.add_argument("--name", required=True, help="product name")
    ap.add_argument("--brand", required=True, help='brand colour, e.g. "#C1552E"')
    ap.add_argument("--kind", default="ios",
                    choices=["ios", "web", "marketing", "cross"],
                    help="platform context")
    ap.add_argument("--model",
                    choices=["tabs", "stack", "workspace", "list-detail", "dashboard", "document"],
                    help="spatial model; required for web, tabs/stack for ios")
    ap.add_argument("--character", default="calm",
                    help='dominant product character, e.g. "dense", "editorial", "utilitarian"')
    ap.add_argument("--screens", default="Home,Browse,Settings",
                    help="comma-separated screen/destination names")
    ap.add_argument("--thing", default="recipes",
                    help="what the product holds, for sample empty-state copy")
    ap.add_argument("--sf", action="store_true",
                    help="use the bundled SF Pro rather than Inter on "
                         "non-Apple platforms. Apple's licence covers "
                         "mocking up interfaces for Apple platforms; it "
                         "does not cover serving the face from a public "
                         "site, so this is opt-in.")
    ap.add_argument("-o", "--out", required=True, help="output directory")
    a = ap.parse_args()

    if not os.path.isdir(KIT):
        sys.exit(f"apple-ui-kit not found next to this skill ({KIT}).")

    screens = [s.strip() for s in a.screens.split(",") if s.strip()]
    if not screens:
        sys.exit("--screens needs at least one name")

    kind = "ios" if a.kind == "cross" else a.kind

    if kind == "web" and not a.model:
        sys.exit("--kind web requires --model: workspace, list-detail, dashboard, or document")
    if kind == "web" and a.model not in WEB_MODELS:
        sys.exit("--kind web supports --model workspace, list-detail, dashboard, or document")
    if kind == "marketing":
        model = "editorial"
    elif kind == "ios":
        model = a.model or "stack"
        if model not in ("tabs", "stack"):
            sys.exit("--kind ios/cross supports --model tabs or stack")
    else:
        model = a.model

    out = os.path.abspath(a.out)
    vendor = os.path.join(out, "vendor")
    os.makedirs(os.path.join(vendor, "fonts"), exist_ok=True)

    shutil.copy2(os.path.join(KIT, "tokens", "ios-tokens.css"), vendor)
    shutil.copy2(os.path.join(KIT, "ios-components.css"), vendor)
    for filename in os.listdir(os.path.join(KIT, "fonts")):
        shutil.copy2(os.path.join(KIT, "fonts", filename),
                     os.path.join(vendor, "fonts", filename))

    theme_name = slug(a.name)
    try:
        css, notes, values = build_theme.build(a.brand, theme_name)
    except ValueError as exc:
        sys.exit(str(exc))
    if a.sf:
        css += (
            "\n/* --sf: the bundled SF Pro ahead of Inter, for platforms\n"
            "   where -apple-system finds nothing. Licence covers mockups,\n"
            "   not public serving -- see fonts/sf.css. */\n"
            ":root {\n"
            "  --ios-font: -apple-system, BlinkMacSystemFont, 'SF Pro',\n"
            "      'Inter', system-ui, 'Segoe UI', Roboto, sans-serif;\n"
            "}\n")
    with open(os.path.join(out, "theme.css"), "w", encoding="utf-8") as f:
        f.write(css)

    # --kind cross used to be a synonym for ios: it accepted the flag,
    # emitted a web page, and left the native teams to copy hex codes out
    # of a stylesheet by hand. The contrast pass has already resolved
    # every value for both appearances, so the honest thing is to hand
    # them over in the form each platform reads. The web build stays --
    # it is the shared prototype the three platforms argue over.
    native = []
    if a.kind == "cross":
        tokens_dir = os.path.join(out, "tokens")
        os.makedirs(tokens_dir, exist_ok=True)
        exports = {
            _camel_file(theme_name) + "Color.swift": "swift",
            _camel_file(theme_name) + "Colors.kt": "kotlin",
            "colors.xml": "xml",
        }
        for filename, fmt in exports.items():
            emitter = build_theme.FORMATS[fmt]
            with open(os.path.join(tokens_dir, filename), "w",
                      encoding="utf-8") as f:
                f.write(emitter(values, theme_name, a.brand))
            native.append(filename)

    try:
        html, chosen_model = compose(kind, model, a.name, screens, a.thing)
    except ValueError as exc:
        sys.exit(str(exc))
    with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

    readme = (README.replace("__NAME__", a.name)
              .replace("__BRAND__", a.brand)
              .replace("__KIND__", a.kind)
              .replace("__MODEL__", chosen_model)
              .replace("__CHARACTER__", a.character)
              .replace("__SLUG__", theme_name)
              .replace("__OUT__", a.out))
    with open(os.path.join(out, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme)

    design = (DESIGN.replace("__CHARACTER__", a.character)
              .replace("__KIND__", a.kind)
              .replace("__MODEL__", chosen_model))
    with open(os.path.join(out, "DESIGN.md"), "w", encoding="utf-8") as f:
        f.write(design)

    rel = min(os.path.relpath(out), out, key=len)
    check = os.path.join(HERE, "check_design.py")
    check_rel = min(os.path.relpath(check), check, key=len)

    print(f"scaffolded {rel}/")
    print(f"  index.html   {a.kind} / {chosen_model}, 4 states")
    print(f"  DESIGN.md    character={a.character}; replace hierarchy placeholders")
    print(f"  theme.css    {a.brand} -> {theme_name}-*, bridged to --ios-*")
    print("  vendor/      tokens, components, fonts (offline)")
    if native:
        print(f"  tokens/      {', '.join(native)} -- same values, "
              f"both appearances")
    if notes:
        print()
        for note in notes:
            print("  contrast: " + note)
    print()
    print("next: replace DESIGN.md placeholders, recompose index.html around")
    print("      that hierarchy -- keeping the ios-* recipes, which carry the")
    print("      measured metrics -- then")
    print(f"      python3 {check_rel} {rel}")
    print("      perform references/visual-critique.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())