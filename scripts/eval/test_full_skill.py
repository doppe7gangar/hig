#!/usr/bin/env python3
"""End-to-end check across every reference in the skill.

The per-feature tests each verified one addition in isolation. This runs
one realistic question per reference against the assembled skill, to catch
what isolated tests miss: a reference that works alone but is never reached
once six others compete for the same question.

Plain text output only, so answers are scored rather than skill files
echoed into the stream.
"""

import concurrent.futures as cf
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.normpath(os.path.join(HERE, "..", "..", ".claude", "skills", "apple-hig"))
MODEL = "claude-opus-5"
TIMEOUT = 600

REVIEW_CODE = '''review this SwiftUI view against Apple's guidelines:

struct SettingsRow: View {
    var body: some View {
        HStack {
            Text("Notifications").font(.system(size: 9))
            Spacer()
            Button(action: {}) { Image(systemName: "chevron.right") }
                .frame(width: 22, height: 22)
        }
    }
}'''

# (label, query, [required patterns])
CASES = [
    ("rules + specs (code review)", REVIEW_CODE,
     [r"\b44\b", r"\b11\b"]),

    ("specs (numeric lookup)",
     "what contrast ratio does apple require for body text under 17pt?",
     [r"4\.5:1"]),

    ("api-map (guidance -> API)",
     "what's the AppKit class for a macOS color well?",
     [r"NSColorWell"]),

    ("components (disambiguation)",
     "what's the difference between a panel and a sheet in Apple's terms?",
     [r"panel", r"sheet", r"macOS"]),

    ("concepts (no page of its own)",
     "does apple have guidance for empty states? my list screen has no items",
     [r"blank screen|empty state", r"writing"]),

    ("platform-diffs (adaptation)",
     "i'm porting an iPhone app to Mac. what changes for alerts specifically?",
     [r"macOS|Mac"]),

    ("assets/ui-kit (visual)",
     "i built a custom toggle. what states do i need to handle, and what "
     "does apple's real one look like when off and disabled?",
     [r"disabl", r"press|idle|on.{0,10}off"]),
]


def make_project():
    root = tempfile.mkdtemp(prefix="hig-full-")
    dst = os.path.join(root, ".claude", "skills")
    os.makedirs(dst)
    shutil.copytree(SKILL, os.path.join(dst, "apple-hig"))
    return root


def ask(query, root):
    env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
    try:
        p = subprocess.run(["claude", "-p", query, "--model", MODEL],
                           cwd=root, env=env, capture_output=True,
                           text=True, timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        return "<TIMEOUT>"
    if p.returncode != 0:
        return f"<ERROR rc={p.returncode}>"
    return p.stdout.strip()


if __name__ == "__main__":
    if not os.path.isdir(SKILL):
        sys.exit(f"skill not found at {SKILL}")
    root = make_project()
    res = {}
    with cf.ThreadPoolExecutor(max_workers=3) as ex:
        futs = {ex.submit(ask, q, root): label for label, q, _ in CASES}
        for f in cf.as_completed(futs):
            res[futs[f]] = f.result()
    shutil.rmtree(root, ignore_errors=True)

    passed = 0
    for label, _q, pats in CASES:
        ans = res[label]
        missing = [p for p in pats if not re.search(p, ans, re.I)]
        ok = not missing
        passed += ok
        print(f"\n[{'PASS' if ok else 'FAIL'}] {label}")
        if missing:
            print(f"   MISSING: {missing}")
        print(f"   {' '.join(ans.split())[:260]}")

    print(f"\n{passed}/{len(CASES)} references reachable and answering correctly")
    sys.exit(0 if passed == len(CASES) else 1)
