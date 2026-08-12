#!/usr/bin/env python3
"""Generate per-platform Claude Code skills from the scraped HIG.

The HIG is written cross-platform: one `buttons.md` covers every platform,
with the divergences tucked into a "Platform considerations" section. That
shape is fine for browsing and bad for building, because when you're writing
a Mac app the Mac rules are the ones scattered across 46 different files.

Each generated skill concentrates one platform:

  references/platform-notes.md  every platform-specific rule for this
                                platform, lifted from every page that has
                                one, in one file. This is the artifact that
                                doesn't exist upstream.
  references/designing-for-*.md the platform's own overview page, verbatim.
  references/<page>.md          pages Apple marks as this platform only
                                (panels and dock-menus for macOS, ornaments
                                and eyes for visionOS, and so on), verbatim.

General guidance that doesn't vary by platform deliberately stays out — the
full `apple-hig` skill holds all 178 pages, and duplicating them six times
would bloat the repo while making each skill worse at the one job it has.

Usage:
    python3 scripts/build_platform_skills.py            # build
    python3 scripts/build_platform_skills.py --check    # verify, no writes
"""

import json
import os
import re
import shutil
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(REPO, "content")
SKILLS = os.path.join(REPO, ".claude", "skills")
META = os.path.join(os.path.dirname(os.path.abspath(__file__)), "platform_metadata.json")

# key -> (display name, skill slug, what makes designing for it different)
PLATFORMS = {
    "ios": ("iOS", "apple-hig-ios",
            "a handheld, touch-first, mostly one-app-at-a-time device where "
            "screen space is scarce and thumbs are the primary input"),
    "ipados": ("iPadOS", "apple-hig-ipados",
               "a large touch display that also handles pointer, keyboard, and "
               "Apple Pencil input, runs apps side by side, and spans a wide "
               "range of window sizes"),
    "macos": ("macOS", "apple-hig-macos",
              "a pointer-driven, multi-window desktop with a menu bar, where "
              "apps are expected to support keyboard navigation, resizing, and "
              "many simultaneous documents"),
    "tvos": ("tvOS", "apple-hig-tvos",
             "a shared, ten-foot screen navigated by remote through a focus "
             "model rather than direct manipulation, with no cursor and no touch"),
    "visionos": ("visionOS", "apple-hig-visionos",
                 "a spatial display where windows exist in three dimensions "
                 "around the wearer and the primary input is eyes plus hands"),
    "watchos": ("watchOS", "apple-hig-watchos",
                "a very small, glanceable screen worn on the wrist, built for "
                "interactions measured in seconds, with the Digital Crown as a "
                "key input"),
}

# "### iOS, iPadOS" -> the platform keys it covers
DISPLAY_TO_KEY = {d: k for k, (d, _, _) in PLATFORMS.items()}


def heading_platforms(heading):
    """Platform keys named by a '### ...' heading under Platform considerations."""
    keys = set()
    for token in re.split(r"[,/]| and ", heading):
        token = token.strip()
        if token in DISPLAY_TO_KEY:
            keys.add(DISPLAY_TO_KEY[token])
    return keys


def page_title(text):
    first = text.lstrip().split("\n", 1)[0]
    return first.lstrip("# ").strip()


def platform_sections(text):
    """{platform key: section body} from a page's Platform considerations."""
    if "## Platform considerations" not in text:
        return {}
    sec = text.split("## Platform considerations", 1)[1].split("\n## ", 1)[0]
    out = {}
    for chunk in re.split(r"\n### ", sec)[1:]:
        heading, _, body = chunk.partition("\n")
        body = body.strip()
        if not body:
            continue
        for key in heading_platforms(heading):
            out.setdefault(key, []).append((heading.strip(), body))
    return out


def build_platform_notes(key, display, pages):
    """Concentrated per-platform extract across the whole corpus."""
    lines = [
        f"# {display}-specific guidance, collected",
        "",
        f"Every place the HIG states a rule specific to {display}, lifted from the "
        f"page it lives on. Sections appear alphabetically by page.",
        "",
        f"A heading like `### {display}, iPadOS` upstream means the rule is shared; "
        "it's reproduced here in full so you don't have to go looking. Each entry "
        "links to the complete page, which also carries the cross-platform guidance "
        "this file deliberately omits.",
        "",
        "---",
        "",
    ]
    count = 0
    for slug in sorted(pages):
        text = open(os.path.join(CONTENT, slug + ".md"), encoding="utf-8").read()
        sections = platform_sections(text).get(key)
        if not sections:
            continue
        count += 1
        title = page_title(text)
        url = f"https://developer.apple.com/design/human-interface-guidelines/{slug}"
        lines.append(f"## {title}")
        lines.append("")
        lines.append(f"Full page: `references/{slug}.md` in the `apple-hig` skill — {url}")
        lines.append("")
        for heading, body in sections:
            if heading != display:
                lines.append(f"*(upstream heading: {heading})*")
                lines.append("")
            lines.append(body)
            lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n", count


def build_skill(key, meta, check_only=False):
    display, slug, character = PLATFORMS[key]
    skill_dir = os.path.join(SKILLS, slug)
    refs = os.path.join(skill_dir, "references")

    all_pages = sorted(f[:-3] for f in os.listdir(CONTENT) if f.endswith(".md"))
    # Apple marks this page as applying only to this platform
    exclusive = sorted(s for s, p in meta.items() if p == [key])
    overview = f"designing-for-{key}"
    if not os.path.exists(os.path.join(CONTENT, overview + ".md")):
        overview = None

    notes, notes_pages = build_platform_notes(key, display, all_pages)

    if check_only:
        return {"skill": slug, "notes_pages": notes_pages,
                "exclusive": len(exclusive), "exists": os.path.isdir(skill_dir)}

    os.makedirs(refs, exist_ok=True)
    for stale in os.listdir(refs):
        os.remove(os.path.join(refs, stale))

    with open(os.path.join(refs, "platform-notes.md"), "w", encoding="utf-8") as f:
        f.write(notes)
    copied = []
    for s in ([overview] if overview else []) + exclusive:
        shutil.copy2(os.path.join(CONTENT, s + ".md"), os.path.join(refs, s + ".md"))
        copied.append(s)

    excl_titles = []
    for s in exclusive:
        t = page_title(open(os.path.join(CONTENT, s + ".md"), encoding="utf-8").read())
        excl_titles.append(f"`{s}` ({t})")

    frameworks = {
        "ios": "SwiftUI and UIKit",
        "ipados": "SwiftUI and UIKit",
        "tvos": "SwiftUI and UIKit",
        "macos": "SwiftUI and AppKit, or UIKit under Mac Catalyst",
        "visionos": "SwiftUI and RealityKit",
        "watchos": "SwiftUI and WatchKit",
    }[key]

    desc = (
        f"{display} design guidance from Apple's Human Interface Guidelines — "
        f"the conventions, component behavior, and layout rules that are specific to "
        f"{display} rather than shared across Apple platforms. Covers how standard UI "
        f"differs on {display} and the interactions unique to it. Use this whenever "
        f"building, designing, reviewing, or debugging the UI of a {display} app — "
        f"including {frameworks} code review — and especially when "
        f"deciding how something should look or behave on {display} specifically, or "
        f"how a shared design needs to change to feel native there. Trigger on mentions "
        f"of {display}"
        + (", Mac apps, or the Mac" if key == "macos" else
           ", iPhone apps, or the iPhone" if key == "ios" else
           ", iPad apps, or the iPad" if key == "ipados" else
           ", Apple TV apps, or the TV app experience" if key == "tvos" else
           ", Apple Vision Pro, or spatial apps" if key == "visionos" else
           ", Apple Watch apps, watch faces, or complications")
        + f", even when Apple's guidelines are never named."
    )

    body = [
        "---",
        f"name: {slug}",
        f"description: {desc}",
        "---",
        "",
        f"# Designing for {display}",
        "",
        f"{display} is {character}. Guidance that holds across every Apple platform "
        f"lives in the general `apple-hig` skill; this skill carries what's specific "
        f"to {display}, so you can answer platform questions without reading around "
        f"the other five.",
        "",
        "## What's here",
        "",
        f"- **`references/platform-notes.md`** — every {display}-specific rule in the "
        f"HIG, collected from the {notes_pages} pages that state one. Upstream these "
        f"are scattered one section at a time across the whole corpus; this is the "
        f"only place they sit together. **Start here** for \"how should this component "
        f"behave on {display}\".",
    ]
    if overview:
        body.append(f"- **`references/{overview}.md`** — Apple's {display} overview: "
                    f"the platform's character, its conventions, and what to prioritize.")
    if excl_titles:
        body.append(f"- **{len(excl_titles)} {display}-only pages**, in full — "
                    + ", ".join(excl_titles) + ". Apple marks these as applying to "
                    f"{display} alone, so the whole page is {display} guidance.")
    body += [
        "",
        "## How to use it",
        "",
        f"1. **Grep `references/platform-notes.md` first.** It's organized by page "
        f"under `## <Page Title>` headings, so `grep -n -A20 '^## Sheets' "
        f"references/platform-notes.md` gets you straight to the {display} rules for "
        f"sheets. If a component isn't in there, the HIG states no {display}-specific "
        f"rule for it — which is a real answer worth giving.",
        "",
        f"2. **Remember what this skill omits.** platform-notes.md holds only the "
        f"{display} deltas. The general rules still apply and often matter more — a "
        f"button's minimum hit region, an alert's button wording. When a question "
        f"needs both, pull the general rule from the `apple-hig` skill's full page "
        f"(each entry links to it) and layer the {display} specifics on top. Answering "
        f"purely from the deltas gives a confidently incomplete answer.",
        "",
        f"3. **Say when {display} genuinely doesn't differ.** Many components behave "
        f"identically everywhere, and Apple often says so outright. \"The HIG gives no "
        f"{display}-specific rule here, so the general guidance applies\" is more "
        f"useful than inventing a platform quirk to justify the lookup.",
        "",
        f"4. **Match the API layer to the platform.** The full pages list SwiftUI, "
        f"UIKit, and AppKit symbols; "
        + ("macOS work usually means AppKit or SwiftUI, not UIKit — recommending a "
           "`UI...` class for a Mac app is a common and obvious miss."
           if key == "macos" else
           f"reach for the framework that actually ships on {display}.")
        + "",
        "",
        "---",
        "",
        f"Scraped from developer.apple.com on 2026-08-11. Regenerate with "
        f"`python3 scripts/build_platform_skills.py`. Point-in-time snapshot — if a "
        f"question turns on something that may have shifted with a new OS release, say "
        f"so rather than presenting the snapshot as certainly current.",
    ]

    with open(os.path.join(skill_dir, "SKILL.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(body) + "\n")

    return {"skill": slug, "notes_pages": notes_pages, "exclusive": len(exclusive),
            "copied": copied}


if __name__ == "__main__":
    check = "--check" in sys.argv
    meta = json.load(open(META))
    print(f"{'checking' if check else 'building'} {len(PLATFORMS)} platform skills\n")
    ok = True
    for key in PLATFORMS:
        r = build_skill(key, meta, check_only=check)
        if check and not r["exists"]:
            ok = False
            print(f"  {r['skill']:22} MISSING — run without --check")
            continue
        print(f"  {r['skill']:22} platform-notes from {r['notes_pages']:3} pages, "
              f"{r['exclusive']} exclusive page(s)")
    sys.exit(0 if ok else 1)
