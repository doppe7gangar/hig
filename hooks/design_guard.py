#!/usr/bin/env python3
"""Before git commit or git push: stop a design taking what it mustn't along.

A design made with new_project.py can hold SF Pro and SF Symbols from the
Mac it was made on, which Apple's licence allows in a mockup on that machine
and not in a repository. Before a commit or a push, this runs
check_distribution.py on every design folder in the repository and denies
the command when a file that fails would go with it: tracked already, or
not ignored by git. Anything else it finds is left to the checks themselves.

Off with ONPLATFORM_COMMIT_GUARD=off in the environment (settings.json "env").
"""

import json
import os
import re
import shlex
import subprocess
import sys
import tempfile

ROOT = os.environ.get("CLAUDE_PLUGIN_ROOT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHECKER = os.path.join(ROOT, ".claude", "skills", "design-workflow", "check_distribution.py")
GIT_SEND = re.compile(r"(?:^|[;&|(]\s*|\s)git(?:\s+-[Cc]\s+\S+|\s+--?[\w-]+(?:=\S+)?)*\s+(commit|push)\b")
SKIP = {".git", "node_modules", ".venv", "venv", "__pycache__", "build", "dist", ".build", "DerivedData"}
MAX_DEPTH, MAX_DIRS = 6, 4000


def git(cwd, *args):
    return subprocess.run(["git", "-C", cwd, *args], capture_output=True, text=True)


def repo_root(cwd, command):
    """The repository the command acts on: -C <dir> or a leading cd, else cwd."""
    m = re.search(r"\bgit\s+-C\s+(\S+)", command) or re.match(r"\s*cd\s+(\S+)\s*&&", command)
    if m:
        target = os.path.expanduser(shlex.split(m.group(1))[0])
        cwd = target if os.path.isabs(target) else os.path.join(cwd, target)
    r = git(cwd, "rev-parse", "--show-toplevel")
    return r.stdout.strip() if r.returncode == 0 else None


def designs(root):
    """Folders new_project.py made: a vendor/manifest.json, or DESIGN.md beside vendor/."""
    found, visited = [], 0
    for dirpath, dirs, files in os.walk(root):
        visited += 1
        depth = os.path.relpath(dirpath, root).count(os.sep)
        dirs[:] = [d for d in dirs if d not in SKIP and not d.startswith(".")] if depth < MAX_DEPTH else []
        if os.path.isfile(os.path.join(dirpath, "vendor", "manifest.json")) or \
                ("DESIGN.md" in files and os.path.isdir(os.path.join(dirpath, "vendor"))):
            found.append(dirpath)
            dirs[:] = []
        if visited > MAX_DIRS:
            break
    return found


def leaving(root, path):
    """True when git would take this file along: tracked, or not ignored."""
    rel = os.path.relpath(path, root)
    if git(root, "ls-files", "--error-unmatch", "--", rel).returncode == 0:
        return True
    return git(root, "check-ignore", "-q", "--", rel).returncode == 1


def problems(root, design):
    with tempfile.TemporaryDirectory() as tmp:
        out = os.path.join(tmp, "files.json")
        subprocess.run([sys.executable, CHECKER, design, "--manifest", out, "-q"],
                       capture_output=True, text=True, timeout=50)
        report = json.load(open(out, encoding="utf-8"))
    bad = []
    failing = {f["path"] for f in report.get("files", []) if f.get("status") == "fail"}
    for message in report.get("problems", []):
        rel = message.split(":", 1)[0]
        if rel in failing and leaving(root, os.path.join(design, rel)):
            bad.append(f"{os.path.relpath(design, root)}/{message}")
    return bad


def main():
    if os.environ.get("ONPLATFORM_COMMIT_GUARD", "").lower() in ("off", "0", "false", "no"):
        return 0
    try:
        event = json.load(sys.stdin)
    except ValueError:
        return 0
    command = (event.get("tool_input") or {}).get("command") or ""
    found = GIT_SEND.search(command)
    if not found or not os.path.isfile(CHECKER):
        return 0
    root = repo_root(event.get("cwd") or os.getcwd(), command)
    if not root:
        return 0
    bad = []
    for design in designs(root):
        try:
            bad += problems(root, design)
        except (OSError, ValueError, subprocess.TimeoutExpired):
            continue
    if not bad:
        return 0
    verb = found.group(1)
    shown = "\n".join(f"- {b}" for b in bad[:8]) + (f"\n- and {len(bad) - 8} more" if len(bad) > 8 else "")
    reason = (f"git {verb} would take files along that a design mustn't publish:\n{shown}\n"
              f"Remove them, or keep them out of git (.gitignore, and git rm --cached for one "
              f"already committed), then run python3 {CHECKER} <design> to confirm. "
              f"This guard is on because the onplatform plugin is; ONPLATFORM_COMMIT_GUARD=off turns it off.")
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                             "permissionDecision": "deny",
                                             "permissionDecisionReason": reason}}))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:  # never stand in the way because the guard itself failed
        sys.exit(0)
