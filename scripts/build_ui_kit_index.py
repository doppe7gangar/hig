#!/usr/bin/env python3
"""Fold the Apple UI-kit screenshot library into the skill.

ios-27-ui-kit_assets/ (at the repo root, added separately from a Figma
export) has 949 PNGs across 27 component folders -- Buttons, Toggles,
Alerts, Windows, etc. -- each with real interaction-state variants (light/
dark, idle/pressed, on/off, enabled/disabled, some with accessibility-label
variants), parseable straight out of the filenames Figma exports.

That's visual ground truth the skill has never had; everything in it so far
is text. But 949 files across 27 folders is unusable without an index --
nobody's going to `ls` their way to "disabled dark-mode toggle." This:

  1. Copies the images into .claude/skills/apple-hig/assets/ui-kit/, so the
     skill stays self-contained (same reasoning as copying content/ into
     references/pages/ rather than pointing outside the skill folder).
  2. Builds assets-index.md: one entry per image, with state tags pulled
     from the filename (best-effort -- Figma's naming isn't perfectly
     uniform across folders, so this reports what it can detect rather
     than forcing a rigid schema), and cross-referenced to the matching
     rules.md / components.md / pages/ entry where one exists honestly --
     several folders (Face ID, Empty States, System) have no matching HIG
     page, and the index says so rather than inventing a link.
"""

import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
SRC = os.path.join(REPO, "ios-27-ui-kit_assets")
SKILL = os.path.join(REPO, ".claude", "skills", "apple-hig")
ASSETS_OUT = os.path.join(SKILL, "assets", "ui-kit")
REFS = os.path.join(SKILL, "references")
CONTENT = os.path.join(REPO, "content")

# UI-kit folder name -> HIG page slug(s) it corresponds to. Built by hand
# against the actual page list, not guessed -- verified each slug exists in
# content/ before including it. Folders with no entry get an honest note
# in the index rather than a forced link.
PAGE_MAP = {
    "Action Sheets": ["action-sheets"],
    "Activity View": ["activity-views"],
    "Alerts": ["alerts"],
    "App Icons": ["app-icons"],
    "Buttons": ["buttons"],
    "Color Pickers": ["color-wells", "pickers"],
    "Colors": ["color"],
    "Contextual Menus": ["context-menus"],
    "Date & Time Pickers": ["pickers"],
    "Edit Menu": ["edit-menus"],
    "Keyboards": ["keyboards", "virtual-keyboards"],
    "List": ["lists-and-tables"],
    "Materials": ["materials"],
    "Notifications": ["notifications"],
    "Page Controls": ["page-controls"],
    "Pop-up Buttons": ["pop-up-buttons"],
    "Sliders": ["sliders"],
    "Status Bars and Menu Bars": ["status-bars", "the-menu-bar"],
    "Steppers": ["steppers"],
    "Tab Bars": ["tab-bars"],
    "Text Fields": ["text-fields"],
    "Toggles": ["toggles"],
    "Windows": ["windows"],
    # These three aren't named after a HIG page, so their contents were
    # inspected rather than guessed from the folder name:
    #   System    -> Lock Screen Widgets (nested 3 levels down), covered by
    #                widgets.md, which discusses the Lock Screen directly.
    #   Face ID   -> biometric authenticating/success states; the HIG treats
    #                biometrics under privacy.md rather than as a component.
    "System": ["widgets", "complications"],
    "Face ID": ["privacy"],
    #   Empty States -> the guidance lives in writing.md ("Provide clear next
    #                steps on any blank screens"), not on any component page.
    #                Easy to miss by grepping component pages only.
    "Empty States": ["writing"],
}

UNMAPPED_NOTES = {}

# Extra context for folders whose guidance isn't where you'd expect, or
# whose implementing API the corpus doesn't name. Appended under the
# normal page links rather than replacing them.
FOLDER_NOTES = {
    "Empty States": (
        "The screen shown when a list or container has no content — a "
        "message, description, and a next-step action, instead of blank "
        "space that reads as broken. The rule is **\"Provide clear next "
        "steps on any blank screens\"** in `pages/writing.md` (also in "
        "`rules.md` under Writing) — it's filed under writing rather than "
        "as a component, which is easy to miss. Key points: guide people "
        "to an action and give them a button or link to take it, and "
        "don't put crucial information here, since empty states are "
        "temporary by definition. SwiftUI implements this as "
        "`ContentUnavailableView`, which the HIG corpus doesn't name."
    ),
    "Face ID": (
        "Biometric authentication states (authenticating, success). The "
        "HIG treats biometrics under privacy rather than as a component, "
        "so there's no Face ID page to cite."
    ),
    "System": (
        "iPad Lock Screen widgets — the folder name is the Figma export's, "
        "not a HIG term. Contents sit at "
        "`System/Lock Screen Widgets/Examples/`."
    ),
}

# Substrings worth surfacing as tags when present in a filename, checked
# case-insensitively. Best-effort: Apple's Figma export naming isn't
# perfectly consistent across all 27 folders, so this reports what it can
# detect rather than asserting every file has every attribute.
TAG_PATTERNS = [
    (r"\bdark\b", "Dark"),
    (r"\blight\b", "Light"),
    (r"\bidle\b", "Idle"),
    (r"\bpressed\b", "Pressed"),
    (r"\bactive\b", "Active"),
    (r"\binactive\b", "Inactive"),
    (r"\bis on\b", "On"),
    (r"\bis off\b", "Off"),
    (r"\bis enabled\b", "Enabled"),
    (r"\bis disabled\b", "Disabled"),
    (r"\bshow ax label\b|\bax label\b", "AX label variant"),
    (r"\bipad\b", "iPad"),
    (r"\biphone\b", "iPhone"),
    (r"\bdestructive\b", "Destructive"),
]


def detect_tags(name):
    # \b doesn't fire at an underscore/hyphen boundary (both count as \w in
    # Python regex), and these filenames use underscores as their primary
    # field separator -- "Dark_1 Storey..." would otherwise never match
    # \bdark\b. Normalize separators to spaces before matching.
    low = re.sub(r"[_\-/]", " ", name.lower())
    return [label for pat, label in TAG_PATTERNS if re.search(pat, low)]


def page_title(slug):
    p = os.path.join(CONTENT, slug + ".md")
    if not os.path.exists(p):
        return None
    return open(p, encoding="utf-8").readline().lstrip("# ").strip()


def clean_label(filename):
    base = re.sub(r"\.(png|svg|jpg)$", "", filename, flags=re.I)
    base = base.replace("_", " · ").replace("  ", " ")
    return " ".join(base.split())


def build():
    if not os.path.isdir(SRC):
        print(f"no {SRC} found -- nothing to index", file=sys.stderr)
        return

    if os.path.isdir(ASSETS_OUT):
        shutil.rmtree(ASSETS_OUT)
    shutil.copytree(SRC, ASSETS_OUT, ignore=shutil.ignore_patterns(".DS_Store"))

    folders = sorted(
        d for d in os.listdir(SRC)
        if os.path.isdir(os.path.join(SRC, d))
    )

    total_files = 0
    unmapped = []
    out = [
        "# UI kit: visual reference for iOS 27 components",
        "",
        "949 screenshots from Apple's iOS 27 Figma UI kit, under "
        "`assets/ui-kit/`, organized by component. Each includes real "
        "interaction-state variants — light/dark appearance, idle/pressed, "
        "on/off, enabled/disabled, and some accessibility-label variants — "
        "not just one static shot per component.",
        "",
        "Everything else in this skill is text. This is the visual ground "
        "truth: use it when a question turns on how something actually "
        "*looks* rather than what the rules *say* — comparing a screenshot "
        "against the real system appearance, checking whether a custom "
        "control's states match Apple's, or when 'why does this feel "
        "wrong' needs a visual answer rather than a spec.",
        "",
        "Read an image directly with the Read tool — "
        "`assets/ui-kit/<Folder>/<file>.png` — rather than trying to infer "
        "appearance from the filename alone.",
        "",
        "---",
        "",
    ]

    for folder in folders:
        folder_path = os.path.join(SRC, folder)
        files = sorted(
            f for f in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, f)) and not f.startswith(".")
        )
        subdirs = sorted(
            d for d in os.listdir(folder_path)
            if os.path.isdir(os.path.join(folder_path, d))
        )

        pages = PAGE_MAP.get(folder, [])
        page_links = []
        for slug in pages:
            title = page_title(slug)
            if title:
                page_links.append(f"[{title}](pages/{slug}.md) "
                                  f"(`rules.md`/`components.md` under \"{title}\")")
        if not pages:
            unmapped.append(folder)

        # Full recursive walk -- several folders (Keyboards, List) nest 4+
        # levels deep, so anything shallower silently drops most of the
        # files. relpath is used both as the index key and as the tag
        # source, since some folders (Keyboards) encode state in directory
        # names ("Dark/.../iPhone/Keys/...") rather than the filename.
        entries = []
        for root, _, fnames in os.walk(folder_path):
            for fn in sorted(fnames):
                if fn.startswith("."):
                    continue
                full = os.path.join(root, fn)
                rel = os.path.relpath(full, folder_path)
                entries.append(rel)
        entries.sort()

        out.append(f"## {folder}")
        out.append(f"<sub>`assets/ui-kit/{folder}/` — {len(entries)} file(s)</sub>")
        out.append("")
        if page_links:
            out.append("Matching HIG guidance: " + "; ".join(page_links))
        elif folder in UNMAPPED_NOTES:
            out.append(f"*{UNMAPPED_NOTES[folder]}*")
        else:
            out.append("*No corresponding page in the HIG corpus — visual "
                       "reference only, not backed by written guidance.*")
        if folder in FOLDER_NOTES:
            out.append("")
            out.append(f"> {FOLDER_NOTES[folder]}")
        out.append("")

        for rel in entries:
            tags = detect_tags(rel)
            tag_str = f" `[{', '.join(tags)}]`" if tags else ""
            out.append(f"- `{rel}`{tag_str}")
            total_files += 1

        out.append("")

    out.append("---")
    out.append("")
    if unmapped:
        out.append(f"<sub>{len(unmapped)} folder(s) with no matching HIG "
                   "page: " + ", ".join(unmapped) + ". Each carries a note "
                   "above explaining what the component is and where the "
                   "nearest written guidance sits — an absent page means "
                   "Apple documents no dedicated rules for it, not that the "
                   "component is unidentified.</sub>")
    else:
        out.append("<sub>Every folder maps to at least one HIG page.</sub>")

    os.makedirs(REFS, exist_ok=True)
    with open(os.path.join(REFS, "assets-index.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(out).rstrip() + "\n")

    def du(path):
        total = 0
        for root, _, files in os.walk(path):
            for f in files:
                total += os.path.getsize(os.path.join(root, f))
        return total // (1024 * 1024)

    print(f"assets-index.md   {total_files} images indexed across {len(folders)} folders")
    print(f"assets/ui-kit/    {du(ASSETS_OUT)} MB copied into skill")
    print(f"unmapped folders: {', '.join(unmapped)}")


if __name__ == "__main__":
    build()
