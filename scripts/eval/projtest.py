#!/usr/bin/env python3
"""Grade the design skill on whole briefs, by running its own checker.

Every earlier round of this graded by reading the transcript, which is
how three runs in a row got called "works" while the thing on disk had
a font CDN in it, or no bridge, or only the happy path. Reading is not
grading.

check_design.py changed that. The score is now its exit code against
whatever the run actually produced: a design that passes is wired
correctly whatever the transcript said, and one that fails says exactly
which of the four silent failures happened.

The briefs are deliberately unlike the one the skill was built against
-- different kinds, different domains, one that must NOT come out
looking like iOS -- because a skill that only works on the example it
was written for is a skill that does not work.

    python3 scripts/eval/projtest.py            # all briefs
    python3 scripts/eval/projtest.py p-dash     # one
"""

import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.abspath(os.path.join(HERE, "..", ".."))
SKILLS = os.path.join(BUILD, ".claude", "skills")
CHECK = os.path.join(SKILLS, "apple-design", "check_design.py")
MODEL = "claude-opus-5"

BRIEFS = {
    # Web app: structure transfers, iOS chrome does not.
    "p-dash": dict(
        prompt="We're building an internal analytics dashboard for our "
               "support team — ticket volume, response times, who's on "
               "shift. Web only, desktop first. Our brand colour is "
               "#1F6FEB. Design it for me.",
        want="web shape, no tab bar, brand blue not Apple blue"),

    # The one that must not look like a Settings screen.
    "p-landing": dict(
        prompt="I need a landing page for Tally, a B2B time-tracking tool "
               "we're launching. Brand green is #0F7B4F. Make it good.",
        want="marketing shape, editorial not iOS chrome, form states"),

    # Native-ish app, a domain nothing was built against.
    "p-plants": dict(
        prompt="Design me an iOS app for tracking when my house plants "
               "need watering. Brand colour #4C8C3F.",
        want="ios shape, tabs under five, all four states"),
}


def install(dst):
    d = os.path.join(dst, ".claude", "skills")
    os.makedirs(d, exist_ok=True)
    for name in ("apple-hig", "apple-ui-kit", "apple-motion", "apple-design"):
        shutil.copytree(os.path.join(SKILLS, name), os.path.join(d, name),
                        ignore=shutil.ignore_patterns("assets", "__pycache__"))


def run(name, spec):
    root = os.path.join(HERE, "pwork", name)
    shutil.rmtree(root, ignore_errors=True)
    os.makedirs(root)
    install(root)

    env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
    p = subprocess.run(
        ["claude", "-p", spec["prompt"], "--output-format", "stream-json",
         "--verbose", "--model", MODEL,
         # The skill's whole method is "run the generator, then the
         # checker", so Bash has to be granted. Under plain acceptEdits
         # the first run stopped and asked for it -- correctly; it
         # declined to hand over a build it could not verify -- and
         # graded as a failure it had not committed. bypassPermissions
         # is refused outright when running as root, so grant the tools
         # by name instead.
         "--permission-mode", "acceptEdits",
         "--allowedTools", "Bash,Read,Write,Edit,Glob,Grep,Skill,WebFetch"],
        cwd=root, env=env, capture_output=True, text=True, timeout=2400)

    parts, skills, ran = [], set(), set()
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
                    for s in ("apple-hig", "apple-ui-kit", "apple-motion",
                              "apple-design"):
                        if s in blob:
                            skills.add(s)
                    for t in ("new_project.py", "check_design.py",
                              "build_theme.py"):
                        if t in blob:
                            ran.add(t)
        if ev.get("type") == "result" and isinstance(ev.get("result"), str):
            parts.append(ev["result"])

    text = "\n\n".join(dict.fromkeys(parts))
    os.makedirs(os.path.join(HERE, "pout"), exist_ok=True)
    open(os.path.join(HERE, "pout", name + ".md"), "w").write(text)
    return text, sorted(skills), sorted(ran), root


def grade(root):
    """Find what the run produced and put the checker on it."""
    cands = []
    for dirpath, dirnames, files in os.walk(root):
        dirnames[:] = [d for d in dirnames
                       if d not in (".claude", "vendor", "node_modules")]
        if any(f.endswith(".html") for f in files):
            cands.append(dirpath)
    if not cands:
        return None, "produced no .html at all -- a brief, not a design"
    target = min(cands, key=lambda p: len(os.path.relpath(p, root)))
    r = subprocess.run([sys.executable, CHECK, target],
                       capture_output=True, text=True, timeout=900)
    return r.returncode, r.stdout.strip()


if __name__ == "__main__":
    only = sys.argv[1:] or list(BRIEFS)
    for name in only:
        if name not in BRIEFS:
            continue
        spec = BRIEFS[name]
        text, skills, ran, root = run(name, spec)
        if "session limit" in text or "usage limit" in text:
            print(f"{name:12} QUOTA-HIT -- stopping; later runs would be noise")
            break
        code, report = grade(root)
        print(f"\n=== {name} === want: {spec['want']}")
        print(f"  skills : {','.join(skills) or 'NONE'}")
        print(f"  tools  : {','.join(ran) or 'NONE'}")
        print(f"  verdict: {'PASS' if code == 0 else 'FAIL'}")
        for line in (report or "").splitlines():
            t = line.strip()
            if t.startswith(("FAIL", "warn")) or "passed" in t or code is None:
                print("           " + t)
