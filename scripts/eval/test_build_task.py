#!/usr/bin/env python3
"""Can the skill be used to BUILD, not just to answer?

Everything before this tested lookups and reviews. This asks it to write
real SwiftUI and checks the output is HIG-correct by construction --
scaling fonts, adequate hit regions, the right presentation API, and
destructive styling applied the way Apple actually specifies (which is
backwards from the common instinct).

Assertions run against extracted ```swift blocks, not the whole reply.
Scanning prose produced two false failures: `.font(.system(size:))` matched
a sentence saying it had been AVOIDED, and `.alert(` matched a correct
error alert in an answer whose main flow was right. Prose discusses what
not to do; only the code says what was actually written.
"""
import concurrent.futures as cf, os, re, shutil, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.normpath(os.path.join(HERE, "..", "..", ".claude", "skills", "apple-hig"))
MODEL, TIMEOUT = "claude-opus-5", 600

CASES = [
    ("writes scaling text + adequate hit region",
     "write me a SwiftUI row for a settings screen: a label 'Notifications' "
     "and a small circular info button on the trailing side. make it "
     "HIG-correct.",
     [r"\.font\(\.(body|headline|subheadline|callout)\)", r"\b44\b"],
     [r"\.font\(\.system\(size:"]),

    ("picks confirmationDialog for post-action choices",
     "in SwiftUI, the user taps 'Share'. i want to offer Copy Link, Email, "
     "or Save to Files. write it.",
     [r"confirmationDialog|ShareLink|UIActivityViewController|activityView"],
     []),

    ("destructive styling applied per Apple's actual rule",
     "write the SwiftUI confirmation for a macOS 'Empty Trash' menu command "
     "the user explicitly chose. should the confirm button be destructive?",
     [r"(not|don't|doesn't|without|no)\W{0,20}destructive|deliberately chose"],
     []),

    ("empty state uses the right construct",
     "write a SwiftUI view for a bookmarks list that has no items yet",
     [r"ContentUnavailableView"],
     []),
]

def make_project():
    root = tempfile.mkdtemp(prefix="hig-build-")
    dst = os.path.join(root, ".claude", "skills"); os.makedirs(dst)
    shutil.copytree(SKILL, os.path.join(dst, "apple-hig"))
    return root

CODE_BLOCK = re.compile(r"```(?:swift)?\n(.*?)```", re.S)


def code_only(answer):
    """Just the Swift the model wrote. Assertions about what the code does
    must not be satisfiable by prose describing what it avoided."""
    blocks = CODE_BLOCK.findall(answer)
    return "\n".join(blocks) if blocks else ""


def ask(q, root):
    env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
    try:
        p = subprocess.run(["claude","-p",q,"--model",MODEL], cwd=root, env=env,
                           capture_output=True, text=True, timeout=TIMEOUT)
    except subprocess.TimeoutExpired:
        return "<TIMEOUT>"
    return p.stdout.strip()

if __name__ == "__main__":
    root = make_project(); res = {}
    with cf.ThreadPoolExecutor(max_workers=2) as ex:
        futs = {ex.submit(ask, q, root): lbl for lbl, q, _, _ in CASES}
        for f in cf.as_completed(futs): res[futs[f]] = f.result()
    shutil.rmtree(root, ignore_errors=True)
    passed = 0
    for lbl, _q, want, avoid in CASES:
        full = res[lbl]
        # the destructive-styling case is answered in prose, not code
        a = full if "destructive" in lbl else (code_only(full) or full)
        missing = [p for p in want if not re.search(p, a, re.I)]
        present = [p for p in avoid if re.search(p, a, re.I)]
        ok = not missing and not present
        passed += ok
        print(f"\n[{'PASS' if ok else 'FAIL'}] {lbl}")
        if missing: print(f"   MISSING: {missing}")
        if present: print(f"   SHOULD NOT APPEAR: {present}")
        print(f"   {' '.join(full.split())[:240]}")
    print(f"\n{passed}/{len(CASES)} build tasks produced HIG-correct code")
    sys.exit(0 if passed == len(CASES) else 1)
