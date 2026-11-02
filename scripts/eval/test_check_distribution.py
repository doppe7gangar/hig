#!/usr/bin/env python3
"""check_distribution.py catches what mustn't leave a design, and passes what may.

Scaffolds every kind of design new_project.py makes and checks each passes
--purpose publish as generated. Then plants, one at a time, what a design
can pick up along the way -- SF Pro under its own name and renamed, SF Pro
embedded in a Figma export, SF Symbols from sf_icons.py, an SF Symbols
template, Apple's design-resource renderings, hot-links, an SF Pro webfont,
an image nobody recorded, a font licence gone missing -- and checks each
fails where it should and passes where it may.

Needs fontTools, to make stand-in fonts; no browser, no Mac.
"""

import base64
import json
import os
import shutil
import struct
import subprocess
import sys
import tempfile
import zlib

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DESIGN = os.path.join(ROOT, ".claude", "skills", "apple-design")
KIT = os.path.join(ROOT, ".claude", "skills", "apple-ui-kit")
SCAFFOLD = os.path.join(DESIGN, "new_project.py")
CHECK = os.path.join(DESIGN, "check_distribution.py")
SF_ICONS = os.path.join(KIT, "sf_icons.py")

FAILED = []


def run(args, cwd=None):
    p = subprocess.run([sys.executable] + args, capture_output=True, text=True, cwd=cwd)
    return p.returncode, p.stdout + p.stderr


def audit(design, purpose="mockup", *extra):
    return run([CHECK, design, "--purpose", purpose, *extra])


def expect(label, got, code, needle=None):
    rc, out = got
    ok = rc == code and (needle is None or needle.lower() in out.lower())
    print(f"  {'ok  ' if ok else 'FAIL'} {label}")
    if not ok:
        FAILED.append(label)
        print("       expected exit", code, f"and {needle!r}" if needle else "", "got", rc)
        print("       " + out.strip().replace("\n", "\n       ")[-1500:])


SEQ = [0]


def scaffold(base, kind, model=None, sf=None):
    SEQ[0] += 1
    out = os.path.join(base, f"{SEQ[0]:02d}-{kind}-{model or 'default'}{'-sf' if sf else ''}")
    args = [SCAFFOLD, "--name", "Pantry", "--brand", "#C1552E", "--kind", kind, "-o", out]
    if model:
        args += ["--model", model]
    if sf:
        args += ["--sf", sf]
    rc, text = run(args)
    if rc != 0:
        raise SystemExit(f"scaffold {kind} failed:\n{text}")
    return out


def fake_font(path, family, copyright_line, licence=""):
    """A tiny TrueType font with the given names, standing in for the real thing."""
    from fontTools.fontBuilder import FontBuilder
    from fontTools.pens.ttGlyphPen import TTGlyphPen
    fb = FontBuilder(1000, isTTF=True)
    fb.setupGlyphOrder([".notdef", "A"])
    fb.setupCharacterMap({65: "A"})
    pen = TTGlyphPen(None)
    pen.moveTo((0, 0)); pen.lineTo((500, 700)); pen.lineTo((1000, 0)); pen.closePath()
    glyph = pen.glyph()
    fb.setupGlyf({".notdef": glyph, "A": glyph})
    fb.setupHorizontalMetrics({".notdef": (1000, 0), "A": (1000, 0)})
    fb.setupHorizontalHeader(ascent=800, descent=-200)
    names = {"familyName": family, "styleName": "Regular", "copyright": copyright_line,
             "manufacturer": "Apple Inc." if "Apple" in copyright_line else "Someone"}
    if licence:
        names["licenseDescription"] = licence
    fb.setupNameTable(names)
    fb.setupOS2()
    fb.setupPost()
    fb.save(path)
    return path


def png(path, size=64, noise=False):
    """A real, small PNG: a black square on transparent, or noise, which doesn't compress."""
    raw = b"".join(b"\x00" + (os.urandom(4 * size) if noise else b"\x00\x00\x00\xff" * size)
                   for _ in range(size))
    def chunk(tag, data):
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data))
    data = (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(raw)) + chunk(b"IEND", b""))
    if path:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "wb").write(data)
    return data


def append(path, text):
    with open(path, "a", encoding="utf-8") as f:
        f.write(text)


def main():
    try:
        import fontTools  # noqa: F401
    except ImportError:
        sys.exit("needs fontTools: pip install fonttools brotli")
    base = tempfile.mkdtemp(prefix="dist-")
    try:
        print("as generated, every kind passes --purpose publish:")
        made = {}
        for kind, model in [("ios", "tabs"), ("ios", "stack"), ("ipados", "sidebar"),
                            ("macos", "sidebar"), ("android", "tabs"), ("web", "dashboard"),
                            ("marketing", None), ("cross", None)]:
            d = scaffold(base, kind, model)
            made[kind] = made.get(kind, d)
            expect(f"{kind} {model or ''}", audit(d, "publish"), 0, "nothing found")
        expect("android carries the Material Symbols licence",
               (0 if os.path.isfile(os.path.join(made["android"], "vendor/icons/"
                                                 "LICENSE-Material-Symbols.txt")) else 1, ""), 0)
        manifest = json.load(open(os.path.join(made["ios"], "vendor", "manifest.json")))
        expect("vendor/manifest.json records each copied file's origin",
               (0 if manifest["files"]["vendor/ios-components.css"]["origin"]
                == "apple-ui-kit/ios-components.css" else 1, ""), 0)

        print("SF Pro:")
        sf = fake_font(os.path.join(base, "SF-Pro.ttf"), "SF Pro",
                       "Copyright © 2015-2026 Apple Inc. All rights reserved.")
        d = scaffold(base, "ios", "tabs", sf=sf)
        expect("your own SF Pro in an iOS mockup, ignored by git: allowed", audit(d), 0, "fine in this mockup")
        expect("...but not published", audit(d, "publish"), 1, "Apple's font SF Pro")
        gi = os.path.join(d, ".gitignore")
        open(gi, "w").write("")
        expect("...nor left out of .gitignore", audit(d), 1, "not in .gitignore")
        d2 = scaffold(base, "web", "dashboard")
        shutil.copy(sf, os.path.join(d2, "vendor", "fonts", "brand-display.woff2"))
        expect("SF Pro renamed is still SF Pro (read from its name table)", audit(d2, "publish"), 1,
               "Apple's font SF Pro")
        expect("...and fails a web mockup too", audit(d2), 1, "web design")
        from fontTools.ttLib import TTFont
        woff = os.path.join(base, "sf.woff")
        f = TTFont(sf); f.flavor = "woff"; f.save(woff)
        sys.path.insert(0, DESIGN)
        import check_distribution as cd
        names = cd._sfnt_names(open(woff, "rb").read())
        expect("without fontTools, the WOFF name table still reads",
               (0 if names and names.get(1) == "SF Pro" else 1, str(names)), 0)

        print("Figma exports:")
        d = scaffold(base, "ios", "stack")
        fig = os.path.join(d, "figma")
        os.makedirs(fig)
        data = base64.b64encode(open(sf, "rb").read()).decode()
        open(os.path.join(fig, "figma-light-1.html"), "w").write(
            f'<style>@font-face {{ font-family: "SF Pro"; src: url("data:font/ttf;base64,{data}"); }}'
            f'</style><div class="figma-frame"></div>')
        expect("an export embedding SF Pro, not ignored: fails", audit(d), 1, "embedded")
        append(os.path.join(d, ".gitignore"), "figma/\n")
        expect("...ignored by git: allowed as a mockup", audit(d), 0, "fine in this mockup")
        expect("...never published", audit(d, "publish"), 1, "embedded")

        print("SF Symbols:")
        sys.path.insert(0, KIT)
        import sf_icons
        d = scaffold(base, "ipados", "tabs")
        mask = os.path.join(base, "house.fill.png")
        png(mask)
        os.makedirs(os.path.join(d, "vendor"), exist_ok=True)
        open(os.path.join(d, "vendor", "sf-symbols.css"), "w").write(
            sf_icons.stylesheet({"house.fill": mask, "gearshape": mask}))
        sf_icons.link(d)
        expect("sf_icons.py output in an iPad mockup: allowed", audit(d), 0, "2 SF Symbol drawing")
        expect("...not published", audit(d, "publish"), 1, "SF Symbol drawing")
        d = scaffold(base, "android", "tabs")
        open(os.path.join(d, "vendor", "sf-symbols.css"), "w").write(
            sf_icons.stylesheet({"house.fill": mask}))
        append(os.path.join(d, ".gitignore"), "vendor/sf-symbols.css\n")
        expect("SF Symbols in an Android design: fail, even ignored", audit(d), 1, "android design")
        page = os.path.join(d, "index.html")
        append(page, '<span data-sf-symbol="house.fill"></span>\n')
        rc, out = run([SF_ICONS, d])
        expect("sf_icons.py won't draw into an Android design",
               (0 if "android design" in out and rc == 0 else 1, out), 0)
        d = scaffold(base, "ios", "tabs")
        open(os.path.join(d, "house.svg"), "w").write(
            '<svg xmlns="http://www.w3.org/2000/svg"><!--Generator: Apple Native CoreSVG 341-->'
            '<g id="Notes"><text>Template v.6.0</text><text>Requires Xcode 16 or greater</text>'
            '<text>Generated from house</text></g></svg>')
        expect("an SF Symbols template from Apple's app, not ignored: fails", audit(d), 1,
               "SF Symbols template")
        os.remove(os.path.join(d, "house.svg"))
        png(os.path.join(d, "icons", "heart.fill.png"))
        expect("a PNG named like an SF Symbol: treated as one", audit(d, "publish"), 1,
               "SF Symbol drawing (heart.fill)")

        print("Apple's assets:")
        d = scaffold(base, "ios", "tabs")
        png(os.path.join(d, "reference", "Toggles", "Light_Idle_Is On.png"))
        expect("a design-resource rendering copied in: fails", audit(d), 1, "design-resource")
        d = scaffold(base, "ios", "tabs")
        page = os.path.join(d, "index.html")
        open(page, "a").write('<img src="https://docs-assets.developer.apple.com/published/'
                              'abc/buttons-hero@2x.png">\n')
        expect("a hot-linked Apple image: a warning in a mockup", audit(d), 0, "hot-link")
        expect("...a failure when published", audit(d, "publish"), 1, "hot-link")
        d = scaffold(base, "web", "dashboard")
        open(os.path.join(d, "index.html"), "a").write(
            '<link rel="stylesheet" href="https://fonts.cdnfonts.com/css/sf-pro-display">\n')
        expect("SF Pro from a webfont host: always fails", audit(d), 1, "loads SF Pro")

        print("Your own images and fonts:")
        d = scaffold(base, "ios", "tabs")
        png(os.path.join(d, "img", "hero.png"))
        expect("an unrecorded image: a warning in a mockup", audit(d), 0, "origin unknown")
        expect("...a failure when published", audit(d, "publish"), 1, "origin unknown")
        json.dump({"img/hero.png": {"source": "our own shoot", "licence": "own work"}},
                  open(os.path.join(d, "assets.json"), "w"))
        expect("...passes once assets.json records it", audit(d, "publish"), 0, "nothing found")
        os.makedirs(os.path.join(d, "fonts"))
        fake_font(os.path.join(d, "fonts", "Brand.ttf"), "Brand Sans", "Copyright 2026 Pantry Ltd")
        expect("an unrecorded font fails when published", audit(d, "publish"), 1, "a font (Brand Sans")
        d = scaffold(base, "ios", "tabs")
        open(os.path.join(d, "index.html"), "a").write(
            f'<img src="data:image/png;base64,{base64.b64encode(png(None, 40, noise=True)).decode()}">\n')
        expect("an embedded image nobody recorded fails when published", audit(d, "publish"), 1,
               "embedded image/png")

        print("Licences that must travel:")
        d = scaffold(base, "ios", "tabs")
        os.remove(os.path.join(d, "vendor", "fonts", "LICENSE-Inter.txt"))
        expect("Inter without its OFL text fails when published", audit(d, "publish"), 1,
               "Inter Variable (SIL OFL) without its licence")
        d = scaffold(base, "android", "tabs")
        os.remove(os.path.join(d, "vendor", "icons", "LICENSE-Material-Symbols.txt"))
        os.remove(os.path.join(d, "vendor", "LICENSE-hig.txt"))
        expect("Material Symbols and the kit without the Apache text fail when published",
               audit(d, "publish"), 1, "Material Symbols icon(s)")

        print("Git and the rest:")
        d = scaffold(base, "macos", "sidebar", sf=sf)
        subprocess.run(["git", "init", "-q", d])
        subprocess.run(["git", "-C", d, "add", "-f", "vendor/fonts/SF-Pro.ttf"])
        expect("SF Pro already committed: fails even in a mockup", audit(d), 1, "committed to git")
        d = scaffold(base, "ios", "tabs")
        os.makedirs(os.path.join(d, "node_modules", "left-pad"))
        out = os.path.join(base, "files.json")
        expect("node_modules is named, not audited", audit(d, "publish", "--manifest", out), 0,
               "not audited")
        m = json.load(open(out))
        kit = [f for f in m["files"] if f["origin"] == "apple-ui-kit/ios-components.css"]
        expect("--manifest lists each file with its origin, licence and hash",
               (0 if kit and kit[0]["licence"] == "Apache-2.0" and len(kit[0]["sha256"]) == 64
                else 1, json.dumps(m)[:400]), 0)
    finally:
        shutil.rmtree(base, ignore_errors=True)

    if FAILED:
        print(f"\n{len(FAILED)} failed")
        return 1
    print("\nall passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
