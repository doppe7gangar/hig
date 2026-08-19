#!/usr/bin/env python3
"""End-to-end test of both skills, installed together.

Installing both is deliberate: picking the right one is part of what is
under test. apple-ui-kit carries appearance for targets with no system
palette; apple-hig carries the rules and the native APIs. A SwiftUI
question that comes back with a pasted hex is a failure even though the
hex is correct.

Each case says what would count as passing before it runs, so the result
is graded rather than admired. Serial, because parallel runs tripped the
session quota, and each result is checked for the quota message so a
quota failure is never scored as a skill failure.
"""

import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.abspath(os.path.join(HERE, "..", "hig-build"))
SKILLS = os.path.join(BUILD, ".claude", "skills")
MODEL = "claude-opus-5"

CASES = {
    # Does it build a real page with the measured tokens?
    "a-web-app": dict(
        prompt="build me a small expense tracker web page — a list of "
               "expenses with amounts, a total at the top, and an add "
               "button. make it feel like an Apple app.",
        want=["uses apple-ui-kit", "copies the token CSS",
              "no #007AFF anywhere"]),

    # Cross-platform: right file, and the Material caution surfaced.
    "b-compose": dict(
        prompt="i'm building an Android app in Jetpack Compose and it "
               "should match our iOS app's look. set up the colours for me.",
        want=["points at AppleKitTokens.kt", "raises the Material tradeoff"]),

    # The caution compiled into the Swift export: don't paste literals.
    "c-swiftui-accent": dict(
        prompt="in my SwiftUI app, what colour should I use for the accent "
               "and for secondary text?",
        want=["recommends semantic APIs", "does NOT paste #0088FF as the fix"]),

    # The canary: two sources that disagree.
    "d-hit-target": dict(
        prompt="what's the minimum tap target on iOS, and where does Apple "
               "say it?",
        want=["gives both 44 and 28", "names both sources"]),
}


def install(dst):
    d = os.path.join(dst, ".claude", "skills")
    os.makedirs(d, exist_ok=True)
    for name in ("apple-hig", "apple-ui-kit"):
        shutil.copytree(os.path.join(SKILLS, name), os.path.join(d, name),
                        ignore=shutil.ignore_patterns("assets"))


def run(name, spec):
    root = os.path.join(HERE, "work", name)
    shutil.rmtree(root, ignore_errors=True)
    os.makedirs(root)
    install(root)

    env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
    p = subprocess.run(
        ["claude", "-p", spec["prompt"], "--output-format", "stream-json",
         "--verbose", "--model", MODEL, "--permission-mode", "acceptEdits"],
        cwd=root, env=env, capture_output=True, text=True, timeout=1800)

    parts, skills = [], set()
    for line in p.stdout.splitlines():
        try:
            ev = json.loads(line)
        except Exception:
            continue
        m = ev.get("message")
        if isinstance(m, dict):
            for b in m.get("content") or []:
                if not isinstance(b, dict):
                    continue
                if b.get("type") == "text" and b.get("text"):
                    parts.append(b["text"])
                if b.get("type") == "tool_use":
                    blob = json.dumps(b.get("input", {}))
                    for s in ("apple-hig", "apple-ui-kit"):
                        if s in blob:
                            skills.add(s)
        if ev.get("type") == "result" and isinstance(ev.get("result"), str):
            parts.append(ev["result"])

    seen, out = set(), []
    for t in parts:
        if t not in seen:
            seen.add(t)
            out.append(t)
    text = "\n\n".join(out)
    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    open(os.path.join(HERE, "out", name + ".md"), "w").write(text)
    return text, sorted(skills), root


if __name__ == "__main__":
    only = sys.argv[1:] or list(CASES)
    for name in only:
        if name not in CASES:
            continue
        spec = CASES[name]
        text, skills, root = run(name, spec)
        if "session limit" in text:
            print(f"{name:18} QUOTA-HIT — stopping, later runs would be noise")
            break
        files = [f for f in os.listdir(root) if not f.startswith(".")]
        print(f"{name:18} {len(text):6} chars  skills={','.join(skills) or 'NONE'}"
              f"  files={files}")
        print(f"{'':18} want: {'; '.join(spec['want'])}")
