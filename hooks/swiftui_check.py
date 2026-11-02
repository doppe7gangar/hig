#!/usr/bin/env python3
"""After a .swift file is written or edited: what the HIG would flag in it.

Runs hig-guide's check_swiftui.py on the one file and hands the findings
back to Claude as context: violations and API problems listed, guidance
counted. Says nothing when the file is clean, isn't Swift, or reports the
same findings it reported last time. Never blocks: the edit has happened,
and the findings are for fixing next.

Off with ONPLATFORM_SWIFTUI_HOOK=off in the environment (settings.json "env").
"""

import hashlib
import json
import os
import subprocess
import sys

ROOT = os.environ.get("CLAUDE_PLUGIN_ROOT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHECKER = os.path.join(ROOT, ".claude", "skills", "hig-guide", "check_swiftui.py")
SHOWN = 10


def seen_before(session, path, digest):
    """True when this file's findings are what was last reported for it."""
    data_dir = os.environ.get("CLAUDE_PLUGIN_DATA")
    if not data_dir:
        return False
    store = os.path.join(data_dir, "swiftui-hook.json")
    try:
        state = json.load(open(store, encoding="utf-8"))
    except (OSError, ValueError):
        state = {}
    if state.get("session") != session:
        state = {"session": session, "files": {}}
    if state["files"].get(path) == digest:
        return True
    state["files"][path] = digest
    try:
        os.makedirs(data_dir, exist_ok=True)
        json.dump(state, open(store, "w", encoding="utf-8"))
    except OSError:
        pass
    return False


def main():
    if os.environ.get("ONPLATFORM_SWIFTUI_HOOK", "").lower() in ("off", "0", "false", "no"):
        return 0
    try:
        event = json.load(sys.stdin)
    except ValueError:
        return 0
    path = (event.get("tool_input") or {}).get("file_path") or ""
    if not path.endswith(".swift"):
        return 0
    if not os.path.isabs(path):
        path = os.path.join(event.get("cwd") or os.getcwd(), path)
    if not (os.path.isfile(path) and os.path.isfile(CHECKER)):
        return 0
    try:
        run = subprocess.run([sys.executable, CHECKER, "--json", path],
                             capture_output=True, text=True, timeout=25)
        findings = json.loads(run.stdout or "[]")
    except (subprocess.TimeoutExpired, ValueError, OSError):
        return 0
    if not findings:
        return 0
    digest = hashlib.sha256(json.dumps(findings, sort_keys=True).encode()).hexdigest()
    if seen_before(event.get("session_id"), path, digest):
        return 0

    listed = ([f for f in findings if f.get("kind") == "violation"]
              + [f for f in findings if f.get("kind") == "api"])
    guidance = [f for f in findings if f.get("kind") == "guidance"]
    name = os.path.basename(path)
    lines = [f"HIG check on {name}: {sum(f.get('kind') == 'violation' for f in findings)} "
             f"violation(s), {sum(f.get('kind') == 'api' for f in findings)} API issue(s), "
             f"{len(guidance)} guidance note(s)."]
    for f in listed[:SHOWN]:
        link = f" ({f['page']})" if f.get("page") else ""
        lines.append(f"- {f['kind']} line {f.get('line')}: {f.get('message')}{link}")
    if len(listed) > SHOWN:
        lines.append(f"- and {len(listed) - SHOWN} more")
    if guidance:
        lines.append(f"Guidance is advice, not a rule; the whole report: python3 {CHECKER} {path}")
    if listed:
        lines.append("Fix the violations before calling this done, or say why one doesn't apply here.")
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse",
                                             "additionalContext": "\n".join(lines)}}))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:  # a hook must never get in the way of the edit
        sys.exit(0)
