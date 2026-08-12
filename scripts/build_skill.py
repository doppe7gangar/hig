#!/usr/bin/env python3
"""Sync the apple-hig Claude Code skill's references/ with content/.

The skill under .claude/skills/apple-hig/ ships its own copy of the scraped
pages so it stays self-contained — it can be dropped into any project's or
user's .claude/skills/ directory without this repo. That copy has to be
refreshed whenever the scrapers re-run, or the skill silently serves stale
guidance while content/ moves on.

This copies content/*.md into the skill, reports what changed, and verifies
that SKILL.md's reference index still matches what's actually on disk (so a
newly scraped page can't end up invisible to the skill, and a removed one
can't linger as a broken pointer).

Usage:
    python3 scripts/build_skill.py           # sync, then verify
    python3 scripts/build_skill.py --check   # verify only, no writes
"""

import filecmp
import os
import re
import shutil
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(REPO, "content")
SKILL_DIR = os.path.join(REPO, ".claude", "skills", "apple-hig")
REFS = os.path.join(SKILL_DIR, "references")
SKILL_MD = os.path.join(SKILL_DIR, "SKILL.md")

PLATFORM_SUFFIXES = ("ios", "ipados", "macos", "tvos", "visionos", "watchos", "games")


def sync():
    os.makedirs(REFS, exist_ok=True)
    src = {f for f in os.listdir(CONTENT) if f.endswith(".md")}
    dst = {f for f in os.listdir(REFS) if f.endswith(".md")}

    added, updated = [], []
    for name in sorted(src):
        s, d = os.path.join(CONTENT, name), os.path.join(REFS, name)
        if name not in dst:
            added.append(name)
        elif not filecmp.cmp(s, d, shallow=False):
            updated.append(name)
        else:
            continue
        shutil.copy2(s, d)

    removed = sorted(dst - src)
    for name in removed:
        os.remove(os.path.join(REFS, name))

    print(f"synced {len(src)} pages -> {os.path.relpath(REFS, REPO)}")
    for label, items in (("added", added), ("updated", updated), ("removed", removed)):
        if items:
            preview = ", ".join(items[:8]) + (" ..." if len(items) > 8 else "")
            print(f"  {label} ({len(items)}): {preview}")
    if not (added or updated or removed):
        print("  no changes")
    return added, removed


def index_names():
    """Page names referenced by SKILL.md's index section."""
    body = open(SKILL_MD, encoding="utf-8").read().split("## Reference index", 1)[1]
    names = {
        t[:-3] if t.endswith(".md") else t
        for t in re.findall(r"`([a-z0-9][a-z0-9-]*(?:\.md)?)`", body)
    }
    # the index writes the platform pages as "designing-for- + ios, ipados, ..."
    names |= {f"designing-for-{s}" for s in PLATFORM_SUFFIXES}
    return names - set(PLATFORM_SUFFIXES) - {"designing-for-"}


def verify():
    actual = {f[:-3] for f in os.listdir(REFS) if f.endswith(".md")}
    named = index_names()
    missing = sorted(actual - named)
    phantom = sorted(named - actual)

    if missing:
        print(f"\nERROR: {len(missing)} page(s) on disk but absent from the SKILL.md "
              f"index — the skill can't route to them:\n  {', '.join(missing)}")
    if phantom:
        print(f"\nERROR: {len(phantom)} name(s) in the SKILL.md index with no such "
              f"file:\n  {', '.join(phantom)}")
    if missing or phantom:
        print("\nUpdate the 'Reference index' section of "
              f"{os.path.relpath(SKILL_MD, REPO)} to match.")
        return False

    print(f"index OK: all {len(actual)} pages reachable from SKILL.md")
    return True


if __name__ == "__main__":
    check_only = "--check" in sys.argv
    if not check_only:
        sync()
    sys.exit(0 if verify() else 1)
