#!/usr/bin/env python3
"""Turn the SF Pro source in Fonts/ into a webfont the skill can use.

Fonts/ holds what Apple ships: a 6.1 MB variable TrueType plus 58 static
.otf cuts, none of which belong on a web page. The variable file already
covers everything the statics do -- opsz 17-28 and wght 1-1000, so Text
through Display and Ultralight through Black -- so this takes that one
file, subsets it to the Latin ranges a UI actually sets, and compresses
it to woff2. 6.1 MB becomes 212 KB, smaller than Inter.

    python3 scripts/build_fonts.py
"""

import os
import sys

try:
    from fontTools import subset
except ImportError:
    sys.exit("needs fonttools:  pip install fonttools brotli")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
SRC = os.path.join(REPO, "Fonts", "San-Francisco-Pro-Fonts-master", "SF-Pro.ttf")
OUT = os.path.join(REPO, ".claude", "skills", "apple-ui-kit", "fonts",
                   "SF-Pro-latin.woff2")

# Latin-1, Latin Extended-A/B, general punctuation, currency, letterlike
# symbols, arrows, maths operators, and the symbol block UI labels reach
# for. Anything outside this falls through to the next font in the stack.
UNICODES = ("U+0000-00FF,U+0100-017F,U+0180-024F,U+2000-206F,"
            "U+20A0-20BF,U+2100-214F,U+2190-21BB,U+2200-22FF,"
            "U+2600-26FF,U+FB00-FB04")


def main():
    if not os.path.exists(SRC):
        sys.exit(f"SF Pro source not found: {SRC}")
    subset.main([
        SRC, f"--output-file={OUT}", "--flavor=woff2",
        f"--unicodes={UNICODES}",
        "--layout-features=*",   # keep kerning and the rest
        "--no-hinting",          # hinting is ignored by browsers here
        "--desubroutinize",
        "--name-IDs=*",
        "--drop-tables+=DSIG",
    ])
    print(f"{os.path.getsize(SRC)/1e6:.1f} MB -> "
          f"{os.path.getsize(OUT)/1024:.0f} KB  {OUT}")


if __name__ == "__main__":
    main()
