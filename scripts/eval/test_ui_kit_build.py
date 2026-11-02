#!/usr/bin/env python3
"""Does apple-ui-kit get used when someone builds a web page, and used right?

TESTING.md's manual check, automated: ask for an ordinary page that should
feel like an Apple app, then grade what landed on disk rather than what the
transcript says. The tells are the ones TESTING.md lists -- the kit's files
copied in rather than reinvented, colours through var(--ios-*) rather than
raw hex, and no #007AFF, the pre-iOS 26 accent that search results still
hand out.

Either skill may take the request. A product brief belongs to apple-design,
which brings the kit in by scaffolding; a bare restyle belongs to
apple-ui-kit. The first run went through apple-design, skipped the scaffold,
and hand-built every component around correctly copied colours -- which is
why the kit's component classes are checked, not just its tokens.

The page is then rendered, light and dark, and any console error fails it.

    python3 scripts/eval/test_ui_kit_build.py
    python3 scripts/eval/test_ui_kit_build.py --save /tmp/uikit   # keep the output
    python3 scripts/eval/test_ui_kit_build.py --grade ./design    # grade an existing build

A request that goes through apple-design runs its whole workflow, gates
included, and took 30 minutes and more in testing. A run that hits the
limit is still graded on what it had written, so a slow build and a
broken one don't look the same.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
SKILLS = os.path.normpath(os.path.join(HERE, "..", "..", ".claude", "skills"))
MODEL, TIMEOUT = "claude-opus-5", 3600

PROMPT = ("build me a simple expense tracker web page -- a list of expenses, "
          "a total at the top, and an add button. make it feel like an Apple "
          "app. plain html/css/js, no build step.")

KIT_FILES = ("ios-tokens.css", "ios-components.css")
HEX = re.compile(r"#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b")
# The kit's own header says "the accent is #0088FF, not #007AFF", and a
# page that copies that comment is quoting the warning, not breaking it.
COMMENT = re.compile(r"/\*.*?\*/|<!--.*?-->", re.S)


def project():
    root = tempfile.mkdtemp(prefix="hig-uikit-")
    dst = os.path.join(root, ".claude", "skills")
    os.makedirs(dst)
    for d in sorted(os.listdir(SKILLS)):
        if d.startswith("apple-"):
            shutil.copytree(os.path.join(SKILLS, d), os.path.join(dst, d),
                            ignore=shutil.ignore_patterns("__pycache__"))
    return root


def build(root):
    env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
    try:
        p = subprocess.run(
            ["claude", "-p", PROMPT, "--output-format", "stream-json",
             "--verbose", "--model", MODEL, "--permission-mode", "acceptEdits",
             "--allowedTools", "Bash,Read,Write,Edit,Glob,Grep,Skill"],
            cwd=root, env=env, capture_output=True, text=True, timeout=TIMEOUT)
        out, finished = p.stdout, True
    except subprocess.TimeoutExpired as e:
        out, finished = e.stdout or "", False
        if isinstance(out, bytes):
            out = out.decode("utf-8", "replace")
    skills = []
    for line in out.splitlines():
        try:
            m = json.loads(line).get("message")
        except Exception:
            continue
        for b in (m.get("content") or []) if isinstance(m, dict) else []:
            if isinstance(b, dict) and b.get("type") == "tool_use" and b.get("name") == "Skill":
                s = str(b.get("input", {}).get("skill", ""))
                if s and s not in skills:
                    skills.append(s)
    return skills, finished


def produced(root):
    out = []
    for dirpath, dirnames, files in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in (".claude", "node_modules")]
        out += [os.path.join(dirpath, f) for f in files
                if f.endswith((".html", ".css", ".js"))]
    return out


def render(page, save):
    """Console errors across light and dark; screenshots when saving."""
    from playwright.sync_api import sync_playwright
    errors = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        for scheme in ("light", "dark"):
            ctx = browser.new_context(viewport={"width": 430, "height": 932},
                                      color_scheme=scheme, device_scale_factor=2)
            tab = ctx.new_page()
            tab.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
            tab.on("pageerror", lambda e: errors.append(str(e)))
            tab.goto("file://" + page)
            tab.wait_for_timeout(500)
            if save:
                tab.screenshot(path=os.path.join(save, f"{scheme}.png"), full_page=True)
            ctx.close()
        browser.close()
    return errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--save", metavar="DIR", help="copy the build and screenshots here")
    ap.add_argument("--grade", metavar="DIR", help="grade an existing build; no model run")
    a = ap.parse_args()

    if a.grade:
        root, skills, finished = os.path.abspath(a.grade), None, True
    else:
        root = project()
        started = time.time()
        skills, finished = build(root)
        minutes = (time.time() - started) / 60
    files = produced(root)
    pages = [f for f in files if f.endswith(".html")]
    own = [f for f in files if os.path.basename(f) not in KIT_FILES
           and "/vendor/" not in f]
    text = {f: COMMENT.sub("", open(f, encoding="utf-8", errors="replace").read())
            for f in files}
    own_text = "\n".join(text[f] for f in own)
    uses = len(re.findall(r"var\(--ios-", own_text))
    raw = HEX.findall(own_text)
    markup = "\n".join(text[f] for f in pages)
    components = sorted({c for attr in re.findall(r'class="([^"]*)"', markup)
                         for c in attr.split() if re.fullmatch(r"ios-[a-z]+", c)})

    if a.save:
        shutil.rmtree(a.save, ignore_errors=True)
        shutil.copytree(root, a.save, ignore=shutil.ignore_patterns(".claude"))

    checks = []
    if skills is not None:
        checks += [
            (f"finished within {TIMEOUT // 60} minutes", finished,
             f"{minutes:.0f} min" if finished
             else "graded on what it had written"),
            ("apple-ui-kit or apple-design was consulted",
             bool({"apple-ui-kit", "apple-design"} & set(skills)),
             ",".join(skills) or "no skill"),
        ]
    checks += [
        ("a page was built", bool(pages), f"{len(pages)} html"),
        ("the kit's files were copied in, not reinvented",
         all(any(os.path.basename(f) == k for f in files) for k in KIT_FILES),
         ", ".join(sorted({os.path.basename(f) for f in files}))),
        ("the kit's components are used, not hand-built",
         len(components) >= 3, ", ".join(components) or "none"),
        ("colours go through var(--ios-*)",
         uses >= 5, f"{uses} uses"),
        ("no #007AFF anywhere", not re.search(r"#007aff", "\n".join(text.values()), re.I), ""),
    ]
    if pages:
        errs = render(max(pages, key=os.path.getsize), a.save)
        checks.append(("renders light and dark without console errors",
                       not errs, "; ".join(errs[:3])))

    for label, ok, note in checks:
        print(f"[{'ok  ' if ok else 'FAIL'}] {label}" + (f"  ({note})" if note else ""))
    print(f"       raw hex in the page's own files: {len(raw)}"
          + (f" ({', '.join(sorted(set(raw))[:8])})" if raw else ""))
    if not a.grade:
        shutil.rmtree(root, ignore_errors=True)
    passed = sum(ok for _, ok, _ in checks)
    print(f"\n{passed}/{len(checks)} checks passed")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
