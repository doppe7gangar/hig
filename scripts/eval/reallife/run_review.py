#!/usr/bin/env python3
"""Run the skill the way it would actually be used: on a real project.

Every earlier stress task ran in an empty directory, so the skill was
answering design questions from its own references and nothing else --
one of them said so outright ("the working directory is empty, so this
is a design-reference answer rather than a code review"). That tests it
as an oracle, not as the thing people install it for.

This copies the skill out of a fresh clone of what's actually pushed,
drops it into a SwiftUI project with known seeded defects, and asks the
way a developer would -- no mention of Apple, HIG, design, or
guidelines, so skill triggering is part of what's under test.
"""

import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CLONE_SKILL = os.path.join(HERE, "clone", ".claude", "skills", "apple-hig")
PROJECT = os.path.join(HERE, "HabitApp")
MODEL = "claude-opus-5"

PROMPTS = {
    "review": "i'm about to ship this. can you look over the UI code and "
              "tell me what i should fix first?",
    "ipad": "does this work properly on iPad, or do i need to change "
            "anything?",
}


def install_skill():
    dst = os.path.join(PROJECT, ".claude", "skills", "apple-hig")
    if os.path.isdir(dst):
        return
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    # Skip the 96 MB of UI-kit PNGs; this run is about the text references
    # and nothing in a code review reads a screenshot. Everything else is
    # copied exactly as the clone has it.
    shutil.copytree(CLONE_SKILL, dst,
                    ignore=shutil.ignore_patterns("assets"))


def run(name, prompt):
    env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
    p = subprocess.run(
        ["claude", "-p", prompt, "--output-format", "stream-json",
         "--verbose", "--model", MODEL],
        cwd=PROJECT, env=env, capture_output=True, text=True, timeout=1800)

    parts, refs, used_skill = [], [], False
    for line in p.stdout.splitlines():
        try:
            ev = json.loads(line)
        except Exception:
            continue
        msg = ev.get("message")
        if isinstance(msg, dict):
            for b in msg.get("content") or []:
                if not isinstance(b, dict):
                    continue
                if b.get("type") == "text" and b.get("text"):
                    parts.append(b["text"])
                if b.get("type") == "tool_use":
                    blob = json.dumps(b.get("input", {}))
                    if "apple-hig" in blob:
                        used_skill = True
                    for r in ("rules.md", "specs.md", "platform-diffs.md",
                              "api-map.md", "components.md", "concepts.md",
                              "assets-index.md", "patterns.md", "pages/"):
                        if r in blob and r not in refs:
                            refs.append(r)
        if ev.get("type") == "result" and isinstance(ev.get("result"), str):
            parts.append(ev["result"])

    seen, out = set(), []
    for t in parts:
        if t not in seen:
            seen.add(t)
            out.append(t)
    return "\n\n".join(out), refs, used_skill


if __name__ == "__main__":
    install_skill()
    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    for name in (sys.argv[1:] or list(PROMPTS)):
        text, refs, used = run(name, PROMPTS[name])
        path = os.path.join(HERE, "out", name + ".md")
        open(path, "w").write(text)
        flag = "QUOTA-HIT" if "session limit" in text else "ok"
        print(f"{name:10} {len(text):6} chars  {flag}  skill={used}  "
              f"refs: {', '.join(refs) or 'NONE'}", flush=True)
        if flag == "QUOTA-HIT":
            break
