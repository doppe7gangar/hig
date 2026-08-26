#!/usr/bin/env python3
"""Render a design for visual review and generate a structured critique sheet.

This does not grade aesthetics. It captures the interface in multiple contexts,
collects a few measurable warning signals, and writes VISUAL_REVIEW.md. The
review is complete only after the screenshots have actually been inspected and
the pending judgments in that file are replaced with evidence.

    python3 render_review.py ./design
    python3 render_review.py ./design --check
"""

import argparse
import glob
import json
import os
import sys
from pathlib import Path
from urllib.parse import quote


VIEWPORTS = [
    ("phone", 390, 844),
    ("tablet", 820, 1000),
    ("desktop", 1280, 900),
]
APPEARANCES = ["light", "dark"]
CORE_STATES = ["populated"]
EXTRA_STATES = ["empty", "error"]
PENDING = "[PENDING — inspect screenshots]"

DOM_AUDIT_JS = r"""() => {
  const visible = e => {
    const s = getComputedStyle(e), r = e.getBoundingClientRect();
    return s.display !== 'none' && s.visibility !== 'hidden' && r.width > 2 && r.height > 2;
  };
  const els = [...document.querySelectorAll('body *')].filter(visible);
  const px = (v) => Number.parseFloat(v || '0') || 0;
  const bg = (s) => s.backgroundColor;
  const bodyBg = getComputedStyle(document.body).backgroundColor;
  let rounded = 0, pills = 0, shadows = 0, blur = 0, centeredText = 0;
  let bordered = 0, surfaces = 0;
  for (const e of els) {
    const s = getComputedStyle(e), r = e.getBoundingClientRect();
    const radius = Math.max(px(s.borderTopLeftRadius), px(s.borderTopRightRadius),
                            px(s.borderBottomLeftRadius), px(s.borderBottomRightRadius));
    if (radius >= 8 && r.width >= 80 && r.height >= 28) rounded++;
    if (radius >= Math.min(r.width, r.height) * .45 && r.width > r.height * 1.25) pills++;
    if (s.boxShadow && s.boxShadow !== 'none') shadows++;
    if ((s.backdropFilter && s.backdropFilter !== 'none') ||
        (s.webkitBackdropFilter && s.webkitBackdropFilter !== 'none')) blur++;
    if (s.textAlign === 'center' && (e.innerText || '').trim().length > 24) centeredText++;
    if ([s.borderTopWidth,s.borderRightWidth,s.borderBottomWidth,s.borderLeftWidth]
        .some(v => px(v) > 0)) bordered++;
    if (r.width >= 120 && r.height >= 52 && bg(s) !== 'rgba(0, 0, 0, 0)' && bg(s) !== bodyBg)
      surfaces++;
  }
  const interactives = els.filter(e => e.matches('button,a[href],input,select,textarea,[role=button]')).length;
  const headings = els.filter(e => /^H[1-6]$/.test(e.tagName)).map(e => ({
    level: e.tagName, text: (e.innerText || '').trim().slice(0,80),
    size: px(getComputedStyle(e).fontSize)
  }));
  return {
    visibleElements: els.length, interactives, rounded, pills, shadows, blur,
    centeredText, bordered, surfaces, headings,
    bodyWidth: document.body.getBoundingClientRect().width,
    scrollWidth: document.documentElement.scrollWidth
  };
}"""


def chrome_path():
    base = os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
    patterns = [
        "chromium-*/chrome-linux/chrome",
        "chromium/chrome",
        "chromium-*/chrome-mac/Chromium.app/Contents/MacOS/Chromium",
    ]
    for pat in patterns:
        hits = sorted(glob.glob(os.path.join(base, pat)))
        if hits:
            return hits[-1]
    return None


def html_target(root):
    direct = os.path.join(root, "index.html")
    if os.path.exists(direct):
        return direct
    pages = [p for p in glob.glob(os.path.join(root, "**", "*.html"), recursive=True)
             if "vendor" not in Path(p).parts]
    if not pages:
        raise FileNotFoundError("no HTML page found")
    return sorted(pages, key=len)[0]


def file_url(path, state=None):
    url = "file://" + quote(os.path.abspath(path))
    if state:
        url += "?state=" + quote(state)
    return url


def signal_summary(audit):
    signals = []
    if audit["rounded"] >= 14:
        signals.append(f"many rounded regions ({audit['rounded']}) — check for card/container overuse")
    if audit["pills"] >= 7:
        signals.append(f"many pill-like elements ({audit['pills']}) — verify each needs capsule treatment")
    if audit["shadows"] >= 8:
        signals.append(f"many shadowed elements ({audit['shadows']}) — verify elevation is structural")
    if audit["blur"] >= 5:
        signals.append(f"many backdrop-blurred elements ({audit['blur']}) — verify each describes a real layer")
    if audit["centeredText"] >= 6:
        signals.append(f"frequent centered text blocks ({audit['centeredText']}) — check for generic landing-page repetition")
    if audit["surfaces"] >= 16:
        signals.append(f"many distinct background surfaces ({audit['surfaces']}) — inspect whether spacing could replace containers")
    if audit["scrollWidth"] > audit["bodyWidth"] + 2:
        signals.append("horizontal overflow detected in this render")
    if not signals:
        signals.append("no strong automated visual-smell signal at this viewport; visual judgment is still required")
    return signals


def render(root, outdir):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        raise RuntimeError("playwright is not installed; run `pip install playwright` and `playwright install chromium`")

    page_path = html_target(root)
    captures = []
    os.makedirs(outdir, exist_ok=True)

    with sync_playwright() as p:
        launch = {"headless": True}
        exe = chrome_path()
        if exe:
            launch["executable_path"] = exe
        browser = p.chromium.launch(**launch)

        # The populated state gets the full width/appearance matrix.
        for appearance in APPEARANCES:
            for label, width, height in VIEWPORTS:
                pg = browser.new_page(viewport={"width": width, "height": height},
                                      color_scheme=appearance)
                pg.goto(file_url(page_path, "populated"), wait_until="load")
                pg.wait_for_timeout(180)
                audit = pg.evaluate(DOM_AUDIT_JS)
                name = f"{label}-{appearance}-populated.png"
                path = os.path.join(outdir, name)
                pg.screenshot(path=path, full_page=True)
                captures.append({"file": name, "viewport": label, "width": width,
                                 "appearance": appearance, "state": "populated",
                                 "audit": audit})
                pg.close()

        # Empty/error need visual inspection too, but one representative context is enough.
        for state in EXTRA_STATES:
            pg = browser.new_page(viewport={"width": 390, "height": 844}, color_scheme="light")
            pg.goto(file_url(page_path, state), wait_until="load")
            pg.wait_for_timeout(150)
            audit = pg.evaluate(DOM_AUDIT_JS)
            name = f"phone-light-{state}.png"
            path = os.path.join(outdir, name)
            pg.screenshot(path=path, full_page=True)
            captures.append({"file": name, "viewport": "phone", "width": 390,
                             "appearance": "light", "state": state, "audit": audit})
            pg.close()

        browser.close()
    return page_path, captures


def review_markdown(root, page_path, captures):
    rel_page = os.path.relpath(page_path, root)
    lines = [
        "# Visual review",
        "",
        f"**Rendered page:** `{rel_page}`",
        "",
        "This review is intentionally separate from `check_design.py`. Mechanical validity is not visual quality. Automated signals below are prompts, not verdicts.",
        "",
        "## Required inspection",
        "",
        "Open every screenshot listed below before replacing any `[PENDING]` judgment. Do not infer visual quality from DOM metrics or filenames.",
        "",
    ]

    for cap in captures:
        lines.append(f"### `{cap['file']}`")
        lines.append("")
        lines.append(f"{cap['viewport']} · {cap['appearance']} · {cap['state']}")
        lines.append("")
        lines.append("Automated signals:")
        for s in signal_summary(cap["audit"]):
            lines.append(f"- {s}")
        heads = cap["audit"].get("headings") or []
        if heads:
            hierarchy = ", ".join(f"{h['level']} {h['size']:.0f}px" for h in heads[:6])
            lines.append(f"- heading ladder seen: {hierarchy}")
        lines.append("")

    lines += [
        "## 1. Two-second hierarchy test",
        "",
        PENDING,
        "",
        "State what the eye reads first, second, and third. If that order does not match the product hierarchy in `DESIGN.md`, revise the composition.",
        "",
        "## 2. Composition",
        "",
        PENDING,
        "",
        "Explain why the major regions are arranged as they are. Flag any region that exists because a template made it convenient rather than because the task requires it.",
        "",
        "## 3. Container and chrome audit",
        "",
        PENDING,
        "",
        "Name containers/borders/persistent controls that can be removed, merged, or made contextual. If none can be removed, explain why the boundaries are real.",
        "",
        "## 4. Typography and density",
        "",
        PENDING,
        "",
        "Judge whether type alone carries hierarchy and whether density fits the platform and task. Compare phone/tablet/desktop rather than treating responsiveness as simple shrinking.",
        "",
        "## 5. Material and color",
        "",
        PENDING,
        "",
        "For every blur, glass, shadow, tint, or strong color, state its functional role. Remove effects that only signal a visual style.",
        "",
        "## 6. Platform authenticity",
        "",
        PENDING,
        "",
        "State what feels appropriate to the target platform and what feels imported from a different platform or from generic SaaS patterns.",
        "",
        "## 7. Empty and error states",
        "",
        PENDING,
        "",
        "Check whether these states preserve the same hierarchy and product character rather than becoming generic centered placeholders.",
        "",
        "## 8. Reduction decisions",
        "",
        PENDING,
        "",
        "List concrete removals/demotions/recompositions made after inspection. A visual review that changes nothing should explain why no reduction was warranted.",
        "",
        "## Final design idea",
        "",
        PENDING,
        "",
        "Complete: **The design idea of this screen is …** Avoid adjectives like clean, premium, modern, or Apple-like. Describe the relationship between content, navigation, and controls.",
        "",
        "## Review status",
        "",
        "PENDING",
        "",
        "Change this to `COMPLETE` only after all pending judgments are replaced with evidence from the rendered screenshots.",
        "",
    ]
    return "\n".join(lines)


def check_review(path):
    if not os.path.exists(path):
        print(f"FAIL no visual review: {path}")
        return 1
    text = open(path, encoding="utf-8").read()
    pending = text.count("[PENDING")
    complete = re.search(r"^COMPLETE\s*$", text, re.M) is not None
    if pending or not complete:
        print(f"FAIL visual review incomplete: {pending} pending judgment(s); status COMPLETE={complete}")
        return 1
    print("ok visual review complete")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Render screenshots and create/check VISUAL_REVIEW.md.")
    ap.add_argument("directory")
    ap.add_argument("--check", action="store_true", help="fail unless review has no pending items and status COMPLETE")
    ap.add_argument("--outdir", help="screenshot directory; default .visual-review")
    a = ap.parse_args()

    root = os.path.abspath(a.directory)
    review_path = os.path.join(root, "VISUAL_REVIEW.md")
    if a.check:
        return check_review(review_path)
    if not os.path.isdir(root):
        sys.exit(f"not a directory: {a.directory}")

    outdir = os.path.abspath(a.outdir or os.path.join(root, ".visual-review"))
    try:
        page_path, captures = render(root, outdir)
    except Exception as exc:
        sys.exit(str(exc))

    text = review_markdown(root, page_path, captures)
    with open(review_path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(os.path.join(outdir, "audit.json"), "w", encoding="utf-8") as f:
        json.dump(captures, f, indent=2)

    print(f"rendered {len(captures)} screenshot(s) to {outdir}")
    print(f"review sheet: {review_path}")
    print("next: inspect every screenshot, replace all [PENDING] judgments, set status COMPLETE, then")
    print(f"      python3 {os.path.abspath(__file__)} {root} --check")
    return 0


if __name__ == "__main__":
    sys.exit(main())