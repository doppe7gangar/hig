#!/usr/bin/env python3
"""Do the kit's Tailwind themes compile, and follow the kit into Dark Mode?

1. The committed themes match what build_tailwind.py generates now.
2. Real Tailwind v4 and v3 compile a page using them, and every class
   the theme promises comes out (v3 has no opacity modifiers on
   variable colours, and the preset says so).
3. Rendered light and dark, each utility resolves to the colour the
   kit's own variable has in that appearance, so a Tailwind page and a
   kit page can't disagree.

Needs node and npm. The first run installs Tailwind v4 and v3 into
scripts/eval/out/tailwind-deps (ignored by git).

    python3 scripts/eval/test_tailwind_theme.py
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
KIT = os.path.join(REPO, ".claude", "skills", "apple-ui-kit")
DEPS = os.path.join(HERE, "out", "tailwind-deps")
VERSIONS = {"v4": ["tailwindcss@4.0.14", "@tailwindcss/cli@4.0.14"], "v3": ["tailwindcss@3.4.17"]}

CLASSES = ["bg-ios-accent", "text-ios-label-secondary", "bg-ios-bg-card", "bg-ios-bg",
           "text-ios-red", "border-ios-separator", "rounded-ios-card", "rounded-ios-control",
           "px-ios-gutter", "size-ios-hit", "font-ios", "font-ios-semibold",
           "ios-text-body", "ios-text-headline", "ios-text-large-title"]
V4_ONLY = ["bg-ios-accent/50"]
# utility -> (CSS property it sets, the kit variable it must equal)
COLOURS = {"bg-ios-accent": ("background-color", "--ios-accent"),
           "bg-ios-bg-card": ("background-color", "--ios-bg-card"),
           "bg-ios-bg": ("background-color", "--ios-bg"),
           "text-ios-label-secondary": ("color", "--ios-label-secondary"),
           "text-ios-red": ("color", "--ios-red")}


def install():
    for ver, pkgs in VERSIONS.items():
        d = os.path.join(DEPS, ver)
        if os.path.isdir(os.path.join(d, "node_modules", "tailwindcss")) and \
                (ver == "v3" or os.path.isdir(os.path.join(d, "node_modules", "@tailwindcss", "cli"))):
            continue
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "package.json"), "w").write('{"private": true}\n')
        subprocess.run(["npm", "install", "--silent", "--no-audit", "--no-fund", *pkgs],
                       cwd=d, check=True)


def compile_v4(work, page):
    shutil.copy(os.path.join(KIT, "tailwind", "theme.css"), work)
    open(os.path.join(work, "in.css"), "w").write(
        '@import "tailwindcss";\n@import "./theme.css";\n@source "./page.html";\n')
    subprocess.run([os.path.join(DEPS, "v4", "node_modules", ".bin", "tailwindcss"),
                    "-i", "in.css", "-o", "v4.css"], cwd=work, check=True, capture_output=True)
    return open(os.path.join(work, "v4.css")).read()


def compile_v3(work, page):
    shutil.copy(os.path.join(KIT, "tailwind", "preset.cjs"), work)
    open(os.path.join(work, "tailwind.config.js"), "w").write(
        "module.exports = { presets: [require('./preset.cjs')], content: ['./page.html'] };\n")
    open(os.path.join(work, "in3.css"), "w").write("@tailwind utilities;\n")
    subprocess.run([os.path.join(DEPS, "v3", "node_modules", ".bin", "tailwindcss"),
                    "-c", "tailwind.config.js", "-i", "in3.css", "-o", "v3.css"],
                   cwd=work, check=True, capture_output=True)
    return open(os.path.join(work, "v3.css")).read()


def has(css, cls):
    sel = "." + re.escape(cls).replace("/", "\\\\/")
    return re.search(r"(^|\s)" + sel.replace("\\\\\\\\", "\\\\") + r"[\s{,:>]", css, re.M) is not None


def main():
    failures = []

    def check(ok, label, detail=""):
        print(("ok   " if ok else "FAIL ") + label + ("" if ok or not detail else f": {detail}"))
        if not ok:
            failures.append(label)

    p = subprocess.run([sys.executable, os.path.join(REPO, "scripts", "build_tailwind.py"), "--check"],
                       capture_output=True, text=True)
    check(p.returncode == 0, "the committed themes are what build_tailwind.py generates",
          p.stdout.strip())
    if not shutil.which("npm"):
        print("needs node and npm for the rest; skipped")
        return 1 if failures else 0
    install()

    # Inside the v4 install: v4 resolves @import "tailwindcss" from the
    # input file's folder upward.
    work = tempfile.mkdtemp(prefix="run-", dir=os.path.join(DEPS, "v4"))
    try:
        page = os.path.join(work, "page.html")
        body = "".join(f'<div id="c{i}" class="{c}">x</div>\n' for i, c in enumerate(CLASSES + V4_ONLY))
        open(page, "w").write(body)
        v4, v3 = compile_v4(work, page), compile_v3(work, page)
        missing4 = [c for c in CLASSES + V4_ONLY if not has(v4, c)]
        missing3 = [c for c in CLASSES if not has(v3, c)]
        check(not missing4, f"Tailwind v4 emits all {len(CLASSES + V4_ONLY)} classes", missing4)
        check(not missing3, f"Tailwind v3 emits all {len(CLASSES)} classes", missing3)

        from playwright.sync_api import sync_playwright
        for ver in ("v4", "v3"):
            html = os.path.join(work, f"render-{ver}.html")
            shutil.copy(os.path.join(KIT, "tokens", "ios-tokens.css"), work)
            shutil.copy(os.path.join(KIT, "ios-components.css"), work)
            open(html, "w").write(
                '<!doctype html><link rel="stylesheet" href="ios-tokens.css">'
                '<link rel="stylesheet" href="ios-components.css">'
                f'<link rel="stylesheet" href="{ver}.css"><body>'
                + "".join(f'<div class="{u}" data-var="{v}" data-prop="{prop}">x</div>'
                          for u, (prop, v) in COLOURS.items()) + "</body>")
            with sync_playwright() as pw:
                b = pw.chromium.launch()
                for scheme in ("light", "dark"):
                    pg = b.new_page(color_scheme=scheme)
                    pg.goto("file://" + html)
                    bad = pg.evaluate("""() => [...document.querySelectorAll('[data-var]')].flatMap(el => {
                        const probe = document.createElement('div');
                        probe.style.color = 'var(' + el.dataset.var + ')';
                        document.body.appendChild(probe);
                        const want = getComputedStyle(probe).color;
                        probe.remove();
                        const got = getComputedStyle(el)[el.dataset.prop === 'color' ? 'color' : 'backgroundColor'];
                        return got === want ? [] : [el.className + ': ' + got + ' != ' + want];
                    })""")
                    check(not bad, f"{ver}, {scheme}: utilities resolve to the kit's own colours", bad)
                b.close()
    finally:
        shutil.rmtree(work, ignore_errors=True)

    print("\ntailwind test " + ("passed" if not failures else f"failed: {len(failures)} problems"))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
