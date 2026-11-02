#!/usr/bin/env python3
"""Check SF Symbol names against your own Mac's list.

A misspelt or invented symbol name fails silently: Image(systemName:)
draws nothing, and nothing warns you. So does a real name on an OS
older than the symbol. The name list can't ship with these skills, but
every Mac already has it, and Xcode's iOS simulator runtime has a copy
as new as its SDK. Run this once on a Mac:

    python3 sf_symbols.py --install

It copies names, renames and the OS each symbol arrived in -- not a
single glyph -- into ~/.cache/apple-hig/sf-symbols.json, outside any
repository. check_swiftui.py and apple-design's check_design.py read
that file when it exists and skip the check when it doesn't.

    python3 sf_symbols.py --check fork.knife cart.fill receipt.expense
    python3 sf_symbols.py --where

Where the list comes from, newest first: the iOS simulator runtimes
Xcode installs, then /System/Library/CoreServices/CoreGlyphs.bundle.
--from DIR reads a folder holding name_availability.plist instead.
"""

import argparse
import difflib
import glob
import json
import os
import plistlib
import re
import sys

GLYPHS = "System/Library/CoreServices/CoreGlyphs.bundle/Contents/Resources"
SOURCES = [
    "/Library/Developer/CoreSimulator/Volumes/iOS_*/Library/Developer/CoreSimulator/"
    "Profiles/Runtimes/*.simruntime/Contents/Resources/RuntimeRoot/" + GLYPHS,
    "/Applications/Xcode*.app/Contents/Developer/Platforms/iPhoneOS.platform/Library/"
    "Developer/CoreSimulator/Profiles/Runtimes/iOS.simruntime/Contents/Resources/"
    "RuntimeRoot/" + GLYPHS,
    "/" + GLYPHS,
]


def cache_path():
    if os.environ.get("APPLE_HIG_SF_SYMBOLS"):
        return os.environ["APPLE_HIG_SF_SYMBOLS"]
    base = os.environ.get("XDG_CACHE_HOME") or os.path.expanduser("~/.cache")
    return os.path.join(base, "apple-hig", "sf-symbols.json")


def read_strings(path):
    """A .strings file, binary or text: {"old": "new"}."""
    data = open(path, "rb").read()
    try:
        return {str(k): str(v) for k, v in plistlib.loads(data).items()}
    except Exception:
        pass
    for enc in ("utf-8", "utf-16"):
        try:
            text = data.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    else:
        return {}
    return dict(re.findall(r'"((?:[^"\\]|\\.)*)"\s*=\s*"((?:[^"\\]|\\.)*)"\s*;', text))


def read_source(folder):
    """Names, renames and releases from one CoreGlyphs Resources folder."""
    with open(os.path.join(folder, "name_availability.plist"), "rb") as fh:
        plist = plistlib.load(fh)
    aliases = os.path.join(folder, "name_aliases.strings")
    return {
        "source": folder,
        "symbols": dict(plist["symbols"]),
        "releases": dict(plist["year_to_release"]),
        "aliases": read_strings(aliases) if os.path.exists(aliases) else {},
    }


def install(folder=None):
    folders = [folder] if folder else [p for pattern in SOURCES for p in sorted(glob.glob(pattern))]
    found = []
    for f in folders:
        try:
            found.append(read_source(f))
        except (OSError, KeyError, plistlib.InvalidFileException):
            continue
    if not found:
        sys.exit("No SF Symbols list found. This needs a Mac; tried:\n  " +
                 "\n  ".join(folders or SOURCES))
    best = max(found, key=lambda d: len(d["symbols"]))       # the newest list
    path = cache_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(best, fh)
    newest = max(best["releases"], key=lambda y: [int(p) for p in y.split(".")])
    print(f"{len(best['symbols'])} symbols, {len(best['aliases'])} renames, up to "
          f"iOS {best['releases'][newest].get('iOS', '?')}\nfrom {best['source']}\nto   {path}")
    return path


def load():
    """The cached list, or None when nobody has run --install."""
    try:
        with open(cache_path(), encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return None


def version(v):
    """26, "26.0" and "26.0.0" are the same version: pad before comparing."""
    parts = [int(p) for p in re.findall(r"\d+", str(v))]
    return tuple(parts + [0] * (3 - len(parts)))


def lookup(db, name, ios=None):
    """("ok"|"renamed"|"too-new"|"unknown", detail) for one symbol name.

    A renamed symbol keeps answering to its old name, so the old one is
    only worth changing once the new one exists on every OS you support."""
    new = db["aliases"].get(name)
    year = db["symbols"].get(name)
    if year is None and new is None:
        close = difflib.get_close_matches(name, db["symbols"].keys(), n=1, cutoff=0.75)
        return "unknown", close[0] if close else None
    if year is None:
        return "renamed", new
    first = db["releases"].get(year, {}).get("iOS")
    if ios and first and version(first) > version(ios):
        return "too-new", first
    if new and ios:
        since = db["releases"].get(db["symbols"].get(new), {}).get("iOS")
        if since and version(since) <= version(ios):
            return "renamed", new
    return "ok", first


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--install", action="store_true", help="copy the list from this Mac")
    ap.add_argument("--from", dest="source", metavar="DIR",
                    help="a folder with name_availability.plist, instead of searching")
    ap.add_argument("--check", nargs="+", metavar="NAME", help="look names up")
    ap.add_argument("--ios", help="deployment target, e.g. 17, for --check")
    ap.add_argument("--where", action="store_true", help="say where the list is")
    a = ap.parse_args()

    if a.install:
        install(a.source)
    if a.where:
        db = load()
        print(f"{cache_path()}: " + (f"{len(db['symbols'])} symbols from {db['source']}"
                                     if db else "not installed; run --install on a Mac"))
    if a.check:
        db = load()
        if not db:
            sys.exit("No list yet: run  python3 sf_symbols.py --install  on a Mac.")
        bad = 0
        for name in a.check:
            status, detail = lookup(db, name, a.ios)
            bad += status in ("unknown", "too-new")
            note = {"ok": f"since iOS {detail}", "renamed": f"renamed to {detail}",
                    "too-new": f"needs iOS {detail}",
                    "unknown": f"no such symbol" + (f"; did you mean {detail}?" if detail else "")}
            print(f"{status:8} {name:32} {note[status]}")
        return 1 if bad else 0
    if not (a.install or a.where or a.check):
        ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
