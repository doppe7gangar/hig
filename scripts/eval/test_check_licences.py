#!/usr/bin/env python3
"""check_licences.py passes the repo as it is, and fails each way it can go wrong.

Copies the repo's files into a scratch checkout, checks it passes, then
breaks one thing at a time: a licence reworded, a skill without its
LICENSE, an image nobody listed, a font swapped for another family, NOTICE
dropping a component, a licence file for something unlisted.

Needs fontTools and brotli, like the check itself.
"""

import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
FAILED = []


def copy_repo(dst):
    files = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard"],
                           cwd=ROOT, capture_output=True, text=True, check=True).stdout.split("\n")
    for rel in filter(None, files):
        src = os.path.join(ROOT, rel)
        if os.path.isfile(src):
            os.makedirs(os.path.dirname(os.path.join(dst, rel)), exist_ok=True)
            shutil.copy2(src, os.path.join(dst, rel))
    subprocess.run(["git", "init", "-q", dst], check=True)
    subprocess.run(["git", "-C", dst, "add", "-A"], check=True)


def check(repo, label, code, needle=None):
    p = subprocess.run([sys.executable, os.path.join(repo, "scripts", "check_licences.py")],
                       capture_output=True, text=True)
    out = p.stdout + p.stderr
    ok = p.returncode == code and (needle is None or needle in out)
    print(f"  {'ok  ' if ok else 'FAIL'} {label}")
    if not ok:
        FAILED.append(label)
        print("       " + out.strip().replace("\n", "\n       ")[-1200:])


def main():
    base = tempfile.mkdtemp(prefix="licences-")
    try:
        def fresh():
            d = os.path.join(base, str(len(os.listdir(base))))
            copy_repo(d)
            return d

        d = fresh()
        check(d, "the repo as it is passes", 0, "0 problem(s)")

        d = fresh()
        p = os.path.join(d, ".claude/skills/apple-ui-kit/fonts/LICENSE-Inter.txt")
        open(p, "w").write(open(p).read().replace("free of charge", "for a fee", 1))
        check(d, "a reworded OFL fails", 1, "not the OFL-1.1 text")

        d = fresh()
        p = os.path.join(d, ".claude/skills/android-ui-kit/icons/LICENSE-Material-Symbols.txt")
        open(p, "w").write(open(p).read().replace("perpetual, worldwide", "revocable", 1))
        check(d, "a reworded Apache text fails", 1, "not the Apache-2.0 text")

        d = fresh()
        os.remove(os.path.join(d, ".claude/skills/apple-hig/LICENSE"))
        subprocess.run(["git", "-C", d, "add", "-A"], check=True)
        check(d, "a skill without its LICENSE fails", 1, "apple-hig/LICENSE: missing")

        d = fresh()
        shutil.copy(os.path.join(d, "docs/iphone.png"), os.path.join(d, "docs/extra.png"))
        subprocess.run(["git", "-C", d, "add", "-A"], check=True)
        check(d, "an image no component covers fails", 1, "docs/extra.png: a font, image or icon")

        d = fresh()
        shutil.copy(os.path.join(d, ".claude/skills/apple-ui-kit/fonts/InterVariable.woff2"),
                    os.path.join(d, ".claude/skills/android-ui-kit/fonts/roboto-greek-wght-normal.woff2"))
        check(d, "a font swapped for another family fails", 1, "not Roboto")

        d = fresh()
        p = os.path.join(d, "NOTICE")
        open(p, "w").write(open(p).read().replace("Material Symbols", "Icons"))
        check(d, "NOTICE dropping a component fails", 1, "NOTICE doesn't mention Material Symbols")

        d = fresh()
        open(os.path.join(d, ".claude/skills/apple-ui-kit/LICENSE-Other.txt"), "w").write("MIT\n")
        subprocess.run(["git", "-C", d, "add", "-A"], check=True)
        check(d, "a licence file for something unlisted fails", 1, "a licence file for something")
    finally:
        shutil.rmtree(base, ignore_errors=True)
    if FAILED:
        print(f"\n{len(FAILED)} failed")
        return 1
    print("\nall passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
