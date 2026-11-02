#!/usr/bin/env python3
"""check_quotes.py grades quotes against the pages an answer links.

Offline: a stand-in page, written in our own words, goes into a temporary
cache where hig_page.py looks first, so nothing is fetched and none of
Apple's text is involved. Checks each verdict the checker can give.
"""

import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK = os.path.join(HERE, "..", "..", ".claude", "skills", "hig-guide", "check_quotes.py")
URL = "https://developer.apple.com/design/human-interface-guidelines/stand-in-page"
PAGE = """# Stand-in page

Keep every primary control within easy reach, so the main task never needs a stretch.

## Best practices

Group related settings together, and put the ones people change most at the top of the list.
"""


def run(answer, cache):
    env = dict(os.environ, XDG_CACHE_HOME=cache)
    p = subprocess.run([sys.executable, CHECK, "-", "--project", os.devnull],
                       input=answer, capture_output=True, text=True, env=env)
    return p.returncode, p.stdout


def main():
    cache = tempfile.mkdtemp(prefix="quotes-")
    os.makedirs(os.path.join(cache, "hig-guide", "pages"))
    open(os.path.join(cache, "hig-guide", "pages", "stand-in-page.md"), "w").write(PAGE)
    bad = []

    code, out = run(f'Per [the page]({URL}), "Keep every primary control within easy reach, '
                    f'so the main task never needs a stretch."', cache)
    if code != 0 or "verbatim 1" not in out:
        bad.append("an exact quote should pass as verbatim:\n" + out)

    code, out = run(f'Per [the page]({URL}), "Group related settings together [...] at the top '
                    f'of the list."', cache)
    if code != 0 or "elided 1" not in out:
        bad.append("an honestly shortened quote should pass as elided:\n" + out)

    code, out = run(f'Per [the page]({URL}), "Always keep every control within easy reach of '
                    f'the thumb on every screen."', cache)
    if code == 0 or "altered 1" not in out:
        bad.append("a reworded quote should fail as altered:\n" + out)

    code, out = run('Apple says "Keep every primary control within easy reach, so the main '
                    'task never needs a stretch."', cache)
    if code == 0 or "unlinked 1" not in out:
        bad.append("a quote with no page linked should fail as unlinked:\n" + out)

    code, out = run(f'From [the page]({URL}):\n\n> "Group related settings together, and put '
                    f'the ones people change most at the top of the list."\n', cache)
    if code != 0 or "verbatim 1" not in out:
        bad.append("a block quote, even one wrapped in quotation marks, should pass:\n" + out)

    code, out = run(f'From [the page]({URL}):\n\n> Put every setting people change at the very '
                    f'top of every list you show.\n', cache)
    if code == 0 or "altered 1" not in out:
        bad.append("a reworded block quote should fail as altered:\n" + out)

    for b in bad:
        print("FAIL", b)
    print("check_quotes test " + ("failed" if bad else "passed"))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
