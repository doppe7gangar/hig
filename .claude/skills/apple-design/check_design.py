#!/usr/bin/env python3
"""Check a design directory against the things a screenshot cannot show.

The recurring failure in this skill was never ugliness. It was a page
that looked completely fine and was wrong underneath: the theme linked
before the components that overwrite it, so a careful brand palette
rendered in Apple's blue; a font CDN in the head, so it fell back to
Helvetica on a plane; three of four states missing, so the first real
empty list shipped as a blank rectangle. Every one of those survives a
screenshot review, and every one is mechanically detectable.

So this is the design equivalent of doctor.py. Static checks always run.
The browser pass needs playwright and adds the things only a real layout
engine knows -- what --ios-accent actually resolved to, whether anything
overflows at phone width, whether the fonts loaded at all.

    python3 check_design.py ./design
    python3 check_design.py ./design --no-browser

Exit status is the point: nonzero means do not ship it.
"""

import argparse
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_theme import contrast, hex_to_rgb  # noqa: E402

APPLE_BLUE = {"#0088ff", "#007aff", "#0a84ff", "#0091ff"}

PASS, FAIL, WARN = [], [], []


def ok(msg):
    PASS.append(msg)


def bad(msg):
    FAIL.append(msg)


def warn(msg):
    WARN.append(msg)


# ------------------------------------------------------------- static

def sheets_in_order(html):
    """The href of every stylesheet link, in document order."""
    return re.findall(r'<link[^>]+rel=["\']stylesheet["\'][^>]*>', html, re.I)


def href_of(tag):
    m = re.search(r'href=["\']([^"\']+)["\']', tag, re.I)
    return m.group(1) if m else ""


def check_link_order(path, html):
    hrefs = [href_of(t) for t in sheets_in_order(html)]
    name = os.path.basename(path)
    theme = [i for i, h in enumerate(hrefs) if h.endswith("theme.css")]
    comp = [i for i, h in enumerate(hrefs) if "components" in h]
    toks = [i for i, h in enumerate(hrefs) if "tokens" in h]

    if not theme:
        bad(f"{name}: links no theme.css. The brand system is not applied; "
            f"whatever palette shows is Apple's.")
        return
    if not comp and not toks:
        warn(f"{name}: links neither the tokens nor the component recipes, "
             f"so nothing here is using the measured values.")
        return
    for group, label in ((comp, "ios-components.css"), (toks, "ios-tokens.css")):
        if group and max(group) > min(theme):
            bad(f"{name}: {label} is linked AFTER theme.css. It redefines "
                f"--ios-accent and friends, so it overwrites the brand "
                f"palette -- the page renders in Apple's blue and looks "
                f"fine doing it. Move theme.css last.")
            return
    ok(f"{name}: stylesheet order correct (theme.css last)")


def check_offline(path, html):
    name = os.path.basename(path)
    ext = re.findall(r'(?:href|src)=["\'](https?://[^"\']+)["\']', html, re.I)
    ext += re.findall(r'@import\s+url\(["\']?(https?://[^"\')]+)', html, re.I)
    if ext:
        hosts = sorted({re.sub(r"https?://([^/]+).*", r"\1", u) for u in ext})
        bad(f"{name}: loads {len(ext)} remote resource(s) from "
            f"{', '.join(hosts)}. The kit ships the fonts -- vendor them, "
            f"or this renders in Helvetica for anyone offline or behind a "
            f"blocked CDN.")
    else:
        ok(f"{name}: no remote resources, opens offline")


def check_local_refs(path, html):
    name, root = os.path.basename(path), os.path.dirname(path)
    missing = []
    for ref in re.findall(r'(?:href|src)=["\']([^"\':#][^"\']*)["\']', html):
        if ref.startswith(("http", "//", "data:", "mailto:")):
            continue
        if not os.path.exists(os.path.join(root, ref.split("?")[0])):
            missing.append(ref)
    if missing:
        bad(f"{name}: {len(missing)} local reference(s) do not exist on "
            f"disk: {', '.join(missing[:4])}")
    else:
        ok(f"{name}: every local reference resolves")


# A state is present when there is *markup that renders it*, not when
# the word appears somewhere in the file. Checking for the string
# "empty" passed a page whose empty panel had been deleted, because the
# stylesheet still carried `.state--empty` and the switcher still had a
# button labelled Empty. Scaffolding is not content. So: strip <style>
# and <script>, then look for the element or for copy only that state
# would have.
STATE_SIGNS = {
    "loading": r'class="[^"]*(?:state--loading|skel)|aria-busy',
    "empty":   r'class="[^"]*state--empty|no [a-z ]{0,24}yet|nothing (?:here|to show)',
    "error":   r"class=\"[^\"]*state--error|couldn't load|couldn.t load|try again|went wrong",
}


def body_of(html):
    """The markup, minus stylesheets and scripts."""
    s = re.sub(r"<style[^>]*>.*?</style>", " ", html, flags=re.S | re.I)
    s = re.sub(r"<script[^>]*>.*?</script>", " ", s, flags=re.S | re.I)
    # The state switcher is scaffolding and names all four states.
    s = re.sub(r'<div class="demo__bar".*?</div>', " ", s, flags=re.S)
    return s


def check_states(path, html):
    name = os.path.basename(path)
    body = body_of(html).lower()
    missing = [label for label, pat in STATE_SIGNS.items()
               if not re.search(pat, body)]
    if missing:
        bad(f"{name}: no markup for the {', '.join(sorted(missing))} state"
            f"{'s' if len(missing) > 1 else ''}. Any screen that loads "
            f"anything has four, and shipping only the happy path is the "
            f"single commonest gap in real builds. references/screens.md "
            f"has the shapes.")
    else:
        ok(f"{name}: populated, loading, empty and error all present")


def check_theme(root):
    p = os.path.join(root, "theme.css")
    if not os.path.exists(p):
        bad("no theme.css. Generate one: build_theme.py '#RRGGBB' --name x")
        return None
    css = open(p, encoding="utf-8").read()

    bridge = re.findall(r"--ios-([a-z0-9-]+):\s*var\(--([a-z0-9-]+)-", css)
    if not bridge:
        bad("theme.css has no --ios-* bridge. The component recipes read "
            "--ios-accent, so without it you get a brand palette and "
            "Apple-blue buttons -- a system that looks right until you "
            "place a component. Regenerate rather than hand-edit.")
    else:
        names = sorted({b[0] for b in bridge})
        ok(f"theme.css bridges {len(names)} --ios-* names ({', '.join(names[:4])}...)")

    m = re.search(r"--[a-z0-9-]+-accent:\s*(#[0-9A-Fa-f]{6})", css)
    if not m:
        warn("theme.css defines no *-accent; cannot check contrast")
        return css
    accent = m.group(1)
    if accent.lower() in APPLE_BLUE:
        warn(f"the accent is {accent}, which is Apple's own. Fine for an "
             f"iOS-looking demo, wrong for a client with a brand.")

    on = re.search(r"--[a-z0-9-]+-on-accent:\s*(#[0-9A-Fa-f]{6})", css)
    if on:
        r = contrast(hex_to_rgb(on.group(1)), hex_to_rgb(accent))
        if r < 3.0:
            bad(f"label on the accent fill is {r:.2f}:1, under the 3:1 "
                f"Apple allows even at bold.")
        else:
            ok(f"label on accent fill {r:.2f}:1 (3:1 needed at semibold)")

    txt = re.search(r"--[a-z0-9-]+-accent-text:\s*(#[0-9A-Fa-f]{6})", css)
    if txt:
        r = contrast(hex_to_rgb(txt.group(1)), (255, 255, 255))
        if r < 4.5:
            warn(f"accent-text is {r:.2f}:1 on white, under 4.5:1 -- the "
                 f"brand hue may not reach it by lightness alone. Use it "
                 f"as a fill behind white, not as coloured text.")
        else:
            ok(f"accent-text {r:.2f}:1 on white (4.5:1 needed to 17pt)")
    return css


def project_css(path, html):
    """The page's own CSS: inline, attribute, and its local stylesheets.

    Reading only <style> left a hole wide enough to drive a project
    through -- put the CSS in app.css, as most real ones do, and every
    hard-coded colour and every overridden token went unseen. theme.css
    and vendor/ are excluded: those are generated and measured
    respectively, and neither is the page's own work.
    """
    root = os.path.dirname(path)
    css = " ".join(re.findall(r"<style[^>]*>(.*?)</style>", html, re.S | re.I))
    css += " " + " ".join(re.findall(r'style=["\']([^"\']+)["\']', html))
    for href in re.findall(r'<link[^>]+href=["\']([^"\']+\.css)["\']', html, re.I):
        if href.startswith(("http", "//")) or href.endswith("theme.css"):
            continue
        if "vendor/" in href or "ios-tokens" in href or "ios-components" in href:
            continue
        f = os.path.join(root, href.split("?")[0])
        if os.path.exists(f):
            css += " " + open(f, encoding="utf-8", errors="replace").read()
    # Strip comments. A file that documents its palette in its own header
    # -- which the good ones do, with the contrast numbers -- otherwise
    # gets every value in that header counted against it, and the check
    # ends up scolding the file for being well documented.
    return re.sub(r"/\*.*?\*/", " ", css, flags=re.S)


def check_token_overrides(path, html):
    """A page redefining --ios-* by hand has stepped around the theme."""
    name = os.path.basename(path)
    hits = sorted(set(re.findall(r"(--ios-[a-z0-9-]+)\s*:\s*(?!var\()[^;}]+",
                                 project_css(path, html))))
    if hits:
        bad(f"{name}: redefines {len(hits)} Apple token(s) with literal "
            f"values ({', '.join(hits[:4])}). That is the theme being "
            f"worked around rather than used -- the value stops following "
            f"dark mode and stops following the brand. Change the brand "
            f"colour and regenerate instead.")
    else:
        ok(f"{name}: does not override the Apple tokens by hand")


def check_hardcoded(path, html):
    """Colours written into the page instead of taken from the system."""
    name = os.path.basename(path)
    styles = project_css(path, html)
    # A hex assigned to a custom property is a token being defined, and
    # a token can be redefined for dark mode and reused everywhere. A hex
    # assigned straight to color/background/border is the thing that
    # cannot follow anything. Only the second kind is a problem.
    #
    # This distinction is not pedantry: a dashboard's chart palette is
    # necessarily its own hues -- Apple's semantic tokens hold no set of
    # mutually distinguishable series colours -- and counting a correctly
    # tokenised, light-and-dark, contrast-checked palette as 30 mistakes
    # is how a warning teaches people to stop reading warnings.
    styles = re.sub(r"--[\w-]+\s*:[^;}]*", " ", styles)
    hexes = {h.lower() for h in re.findall(r"#[0-9A-Fa-f]{6}\b|#[0-9A-Fa-f]{3}\b",
                                           styles)}
    hexes -= {"#fff", "#ffffff", "#000", "#000000"}   # on-fill text, legitimately
    if len(hexes) > 3:
        warn(f"{name}: {len(hexes)} hard-coded colours in the page's own CSS "
             f"({', '.join(sorted(hexes)[:5])}). Each one is a value that "
             f"will not follow dark mode or the brand. Use the tokens.")
    elif hexes:
        ok(f"{name}: {len(hexes)} hard-coded colour(s), within reason")
    else:
        ok(f"{name}: no hard-coded colours, all from tokens")


# ------------------------------------------------------------ browser

BROWSER_JS = r"""() => {
// Rendered contrast, measured rather than parsed. The CSS can be
// perfect and the page still unreadable -- a token overridden further
// down, a colour inherited onto a surface nobody pictured -- and only
// the layout engine knows what a run of text finally sits on. Anything
// inside an aria-hidden subtree is skipped: it is declared decorative,
// nothing announces it, and holding a monogram in an icon tile to the
// same bar as a paragraph teaches people to silence the check.
const RATIO = (a, b) => {
  const lum = c => { const f = v => (v /= 255) <= 0.03928 ? v / 12.92
        : Math.pow((v + 0.055) / 1.055, 2.4);
    return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2]); };
  const [x, y] = [lum(a), lum(b)];
  return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05);
};

// getComputedStyle does not promise rgb(). Chromium hands back
// `color(srgb 0.96 0.96 0.96)` for anything that went through
// color-mix, and those channels are 0-1. Read as 0-255 a near-white
// footer measures as near-black, which is how a perfectly legible
// marketing page came back with thirty-eight contrast failures.
function parseColor(s) {
  const n = (s.match(/[\d.]+(?:e[-+]?\d+)?/gi) || []).map(Number);
  if (n.length < 3) return null;
  const unit = /^color\(/i.test(s);
  return [n[0] * (unit ? 255 : 1), n[1] * (unit ? 255 : 1),
          n[2] * (unit ? 255 : 1), n.length > 3 ? n[3] : 1];
}

const over = (fg, bg) => [0, 1, 2].map(i => fg[i] * fg[3] + bg[i] * (1 - fg[3]));

// Composite every translucent layer down to the first opaque one.
// Apple's label ladder is one grey at several alphas -- the colours the
// system uses most are all translucent -- so dropping alpha would make
// this check meaningless for exactly the text it most needs to judge.
function surfaceOf(el) {
  const layers = [];
  let base = null;
  for (let n = el; n; n = n.parentElement) {
    const c = parseColor(getComputedStyle(n).backgroundColor);
    if (!c || c[3] === 0) continue;
    if (c[3] >= 0.999) { base = c.slice(0, 3); break; }
    layers.push(c);
  }
  if (!base) {
    for (const el2 of [document.body, document.documentElement]) {
      const c = parseColor(getComputedStyle(el2).backgroundColor);
      if (c && c[3] >= 0.999) { base = c.slice(0, 3); break; }
    }
  }
  // A transparent page borrows the viewer's ground; guessing black here
  // put white text at 1.2:1 against nothing at all.
  if (!base) base = matchMedia('(prefers-color-scheme: dark)').matches
      ? [0, 0, 0] : [255, 255, 255];
  let cur = base;
  for (let i = layers.length - 1; i >= 0; i--) cur = over(layers[i], cur);
  return cur;
}

const lowContrast = [...document.querySelectorAll(
    'p, span, a, li, h1, h2, h3, h4, button, label, td, th, div')]
  .filter(e => e.offsetParent !== null
      && !e.closest('[aria-hidden="true"]')
      && [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim()))
  .map(e => {
    const cs = getComputedStyle(e);
    const raw = parseColor(cs.color);
    if (!raw || raw[3] === 0) return null;
    const bg = surfaceOf(e);
    const fg = over(raw, bg);
    const px = parseFloat(cs.fontSize);
    // SF Pro's semibold is 590, not the CSS ladder's 600. Testing for
    // 600 classed every Apple-faithful semibold run as regular and
    // held it to 4.5:1 where the large-text allowance applies.
    const bold = parseInt(cs.fontWeight, 10) >= 590;
    // Apple and WCAG agree here: large text may sit at 3:1.
    const need = (px >= 24 || (px >= 18.66 && bold)) ? 3.0 : 4.5;
    const r = RATIO(fg, bg);
    return r + 0.01 < need
      ? {t: e.textContent.trim().slice(0, 30), r: +r.toFixed(2), need, px: Math.round(px)}
      : null;
  })
  .filter(Boolean);
  const cs = getComputedStyle(document.documentElement);
  const v = n => cs.getPropertyValue(n).trim();
  const body = getComputedStyle(document.body);
  const de = document.documentElement;
  const small = [...document.querySelectorAll(
      'button, a[href], input, select, [role=button]')]
    .filter(e => e.offsetParent !== null)
    .map(e => { const r = e.getBoundingClientRect();
                return {t: (e.textContent||e.getAttribute('aria-label')||'?')
                          .trim().slice(0, 28),
                        w: Math.round(r.width), h: Math.round(r.height)}; })
    .filter(o => o.w > 0 && o.h > 0 && Math.min(o.w, o.h) < 28);
  return {
    accent: v('--ios-accent'),
    label: v('--ios-label'),
    bg: v('--ios-bg'),
    font: body.fontFamily,
    size: body.fontSize,
    lh: body.lineHeight,
    ls: body.letterSpacing,
    overflow: de.scrollWidth - de.clientWidth,
    small: small.slice(0, 6),
    lowContrast: lowContrast.slice(0, 8),
    lowCount: lowContrast.length,
  };
}"""


def chrome_path():
    """Find a browser without pinning a build number.

    Playwright's own default works when someone has run `playwright
    install`. Some environments ship a browser under a versioned
    directory instead and set PLAYWRIGHT_BROWSERS_PATH, where the default
    lookup misses -- so glob rather than hard-code, because a pinned
    build number is a check that stops running the week it changes.
    """
    base = os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
    for pat in ("chromium-*/chrome-linux/chrome", "chromium/chrome",
                "chromium-*/chrome-mac/Chromium.app/Contents/MacOS/Chromium"):
        hits = sorted(glob.glob(os.path.join(base, pat)))
        if hits:
            return hits[-1]
    return None


def check_browser(path, brand):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        warn("playwright not installed; skipped the browser pass, which is "
             "where resolved values and overflow actually get checked")
        return

    name = os.path.basename(path)
    url = "file://" + os.path.abspath(path)
    errors, failed = [], []

    def sample(b, scheme, more):
        """Failing text runs for one appearance, optionally under IC."""
        kw = {"viewport": {"width": 390, "height": 900}, "color_scheme": scheme}
        if more:
            kw["contrast"] = "more"
        pg = b.new_page(**kw)
        try:
            pg.goto(url, wait_until="load")
            pg.wait_for_timeout(220)
            return pg.evaluate(BROWSER_JS)["lowContrast"]
        finally:
            pg.close()

    with sync_playwright() as p:
        launch = {"args": ["--no-sandbox"]}
        exe = chrome_path()
        if exe:
            launch["executable_path"] = exe
        try:
            b = p.chromium.launch(**launch)
        except Exception as e:
            warn(f"could not launch a browser ({str(e)[:70]}); skipped "
                 f"the browser pass. Run `playwright install chromium`.")
            return
        for scheme in ("light", "dark"):
            for width in (390, 430, 1280):
                pg = b.new_page(viewport={"width": width, "height": 900},
                                color_scheme=scheme)
                pg.on("console",
                      lambda m: errors.append(m.text)
                      if m.type == "error" else None)
                pg.on("requestfailed",
                      lambda r: failed.append(r.url))
                pg.goto(url, wait_until="load")
                pg.wait_for_timeout(220)
                d = pg.evaluate(BROWSER_JS)

                tag = f"{name} {scheme} {width}px"
                if d["overflow"] > 1:
                    bad(f"{tag}: the page scrolls sideways by "
                        f"{d['overflow']}px. Something has a fixed width "
                        f"wider than the viewport.")
                # Contrast is measured in BOTH appearances. It used to run
                # in light only, which is how a generator that emitted an
                # unchecked dark palette -- a navy at 1.24:1 on the dark
                # card -- came back 18/18 ready three times running.
                if width == 390:
                    # Anything Increased Contrast rescues is a different
                    # finding from anything it doesn't. Apple's own
                    # secondary label is 3.44:1 on white and their filled
                    # buttons run white at about 3.5:1 -- deliberate
                    # calls, with the accessibility setting as the
                    # remedy. Failing every Apple-faithful design on
                    # those makes the check unusable, and passing text
                    # that stays unreadable at any setting makes it
                    # pointless. So: measure both, and separate them.
                    try:
                        # Texts STILL failing once Increased Contrast is on.
                        still = {c["t"] for c in sample(b, scheme, True)}
                    except Exception:
                        still = None
                    if still is None:
                        hard, soft = d["lowContrast"], []
                    else:
                        hard = [c for c in d["lowContrast"] if c["t"] in still]
                        soft = [c for c in d["lowContrast"]
                                if c["t"] not in still]
                    if hard:
                        listed = ", ".join(
                            f"\"{c['t']}\" {c['r']}:1 (needs {c['need']}, "
                            f"{c['px']}px)" for c in hard[:4])
                        bad(f"{name} {scheme}: {len(hard)} text run(s) under "
                            f"the contrast they need, and still failing "
                            f"under Increased Contrast: {listed}")
                    if soft:
                        listed = ", ".join(
                            f"\"{c['t']}\" {c['r']}:1" for c in soft[:3])
                        warn(f"{name} {scheme}: {len(soft)} run(s) below "
                             f"4.5:1 at default settings but fixed by "
                             f"Increased Contrast -- Apple's own secondary "
                             f"label (3.44:1) and filled buttons (~3.5:1) "
                             f"are like this too: {listed}")
                    if not hard and not soft:
                        ok(f"{name} {scheme}: every text run meets its "
                           f"contrast requirement")
                    if d["accent"]:
                        got = d["accent"].lower().replace(" ", "")
                        ok(f"{name} {scheme}: --ios-accent resolves to {got}")
                    else:
                        bad(f"{name} {scheme}: --ios-accent resolves to "
                            f"nothing. The component recipes have no colour "
                            f"to use.")

                if width == 390 and scheme == "light":
                    fam = d["font"].lower()
                    if "inter" in fam or "sf pro" in fam or "-apple-system" in fam:
                        ok(f"{name}: body font resolves to {d['font'][:44]}")
                    else:
                        bad(f"{name}: body font is {d['font'][:44]} -- the "
                            f"vendored faces are not being used.")
                    got = (d["accent"] or "").lower().replace(" ", "")
                    if brand and got and got.lstrip("#") != brand.lower().lstrip("#"):
                        warn(f"{name}: --ios-accent resolves to {got} in "
                             f"light, not the brand {brand}. Check the "
                             f"bridge.")
                    if d["small"]:
                        listed = ", ".join(
                            f"{s['t']} ({s['w']}x{s['h']})" for s in d["small"])
                        warn(f"{name}: {len(d['small'])} target(s) under 28pt, "
                             f"which is Apple's accessibility floor -- the "
                             f"general rule is 44: {listed}")
                    else:
                        ok(f"{name}: every visible target clears 28pt")

                # Every state has to actually render something.
                for st in ("populated", "loading", "empty", "error"):
                    if width != 390 or scheme != "light":
                        continue
                    pg.goto(url + "?state=" + st, wait_until="load")
                    pg.wait_for_timeout(120)
                    # Painted area, not text length. A loading state is a
                    # skeleton -- shapes standing in for text it does not
                    # have yet -- so measuring characters reported the one
                    # state that is *supposed* to be wordless as empty.
                    vis = pg.evaluate(
                        "() => [...document.querySelectorAll('.state')]"
                        ".filter(e => e.offsetParent !== null)"
                        ".map(e => e.innerText.trim().length"
                        " + [...e.querySelectorAll('*')].filter(c => {"
                        "   const r = c.getBoundingClientRect();"
                        "   return r.width > 4 && r.height > 4; }).length)")
                    if not vis or not any(v > 0 for v in vis):
                        warn(f"{name}: the '{st}' state renders nothing "
                             f"visible. If the switcher was removed that is "
                             f"expected; otherwise the panel is empty.")
                    else:
                        ok(f"{name}: '{st}' state renders")
                pg.close()
        b.close()

    if errors:
        bad(f"{name}: {len(errors)} console error(s): {errors[0][:90]}")
    else:
        ok(f"{name}: no console errors")
    if failed:
        bad(f"{name}: {len(failed)} request(s) failed: {failed[0][:90]}")
    else:
        ok(f"{name}: no failed requests")


# --------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(
        description="Check a design directory before calling it done.")
    ap.add_argument("directory")
    ap.add_argument("--brand", help="expected accent, e.g. '#C1552E'")
    ap.add_argument("--no-browser", action="store_true")
    a = ap.parse_args()

    root = os.path.abspath(a.directory)
    if not os.path.isdir(root):
        sys.exit(f"not a directory: {a.directory}")

    pages = sorted(glob.glob(os.path.join(root, "**", "*.html"), recursive=True))
    pages = [p for p in pages if "vendor" not in os.path.relpath(p, root).split(os.sep)]
    if not pages:
        sys.exit(f"no .html in {a.directory}. The deliverable is a working "
                 f"screen; a directory of notes is not one.")

    css = check_theme(root)
    brand = a.brand
    if not brand and css:
        m = re.search(r"--[a-z0-9-]+-accent:\s*(#[0-9A-Fa-f]{6})", css)
        brand = m.group(1) if m else None

    for p in pages:
        html = open(p, encoding="utf-8").read()
        check_link_order(p, html)
        check_offline(p, html)
        check_local_refs(p, html)
        check_states(p, html)
        check_hardcoded(p, html)
        check_token_overrides(p, html)
        if not a.no_browser:
            check_browser(p, brand)

    for m in PASS:
        print(f"  ok   {m}")
    for m in WARN:
        print(f"  warn {m}")
    for m in FAIL:
        print(f"  FAIL {m}")

    n = len(PASS) + len(FAIL)
    print(f"\n{len(PASS)}/{n} passed, {len(WARN)} warning(s)")
    if FAIL:
        print(f"{len(FAIL)} failure(s) -- not ready to ship.")
        return 1
    print("ready.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
