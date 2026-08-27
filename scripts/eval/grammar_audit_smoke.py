#!/usr/bin/env python3
"""Smoke-test implementation-to-grammar extraction without model/browser calls."""

import os
import subprocess
import sys
import tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
AUDIT = os.path.join(ROOT, ".claude", "skills", "apple-design", "audit_grammar.py")


def run(args, expect=0):
    p = subprocess.run(args, capture_output=True, text=True)
    if p.returncode != expect:
        raise RuntimeError(f"expected {expect}, got {p.returncode}: {' '.join(args)}\n{p.stdout}\n{p.stderr}")
    return p


def main():
    if not os.path.exists(AUDIT):
        raise RuntimeError("missing audit_grammar.py")
    with tempfile.TemporaryDirectory(prefix="grammar-audit-") as root:
        open(os.path.join(root, "index.html"), "w", encoding="utf-8").write('''<!doctype html><style>
        .title{font-size:32px;margin:0 0 24px}.panel{border-radius:12px;padding:16px;gap:8px}
        .panel-alt{border-radius:12px;padding:16px;gap:8px}.odd{border-radius:17px;font-size:19px}
        </style><main><h1 class="title">Inbox</h1><button>Save</button><button>Save</button>
        <section class="panel">A</section><section class="panel-alt">B</section><section class="odd">C</section></main>''')
        open(os.path.join(root, "PROJECT_GRAMMAR.md"), "w", encoding="utf-8").write('''# Project design grammar
## Scope
- Product: Mail
- Platforms: web
- Evidence screens/states: inbox; detail
## Established rules
| Domain | Semantic rule | Evidence | Applies to | Exceptions |
|---|---|---|---|---|
| Typography | Page titles lead screen hierarchy | Inbox; Detail screens | content screens | player |
| Spacing | Section groups use stable rhythm | Inbox; Detail screens | content screens | compact table |
| Geometry | Group surfaces share one radius family | Inbox; Detail screens | grouped surfaces | modal |
| Actions | Save remains in editing action region | Compose; Settings screens | editing flows | autosave |
| Navigation | Selection remains visible in split navigation | Inbox; Detail screens | split layouts | phone stack |
## Provisional rules
| Domain | Candidate rule | Evidence needed |
|---|---|---|
## Intentional exceptions
| Screen/context | Rule diverged from | Why |
|---|---|---|
## Retired rules
| Rule | Replaced by | Reason |
|---|---|---|
## Canonical language
| Concept | Term/icon | Do not substitute |
|---|---|---|
| save action | Save | Apply |
## Adaptive transformations
| Structure | Wide/default | Compact | Invariant preserved |
|---|---|---|---|
| split view | list + detail | sequential detail | selection context |
''')
        run([sys.executable, AUDIT, root])
        report = open(os.path.join(root, "IMPLEMENTATION_GRAMMAR_AUDIT.md"), encoding="utf-8").read()
        if "`12px` — 2 occurrences" not in report or "Save ×2" not in report:
            raise RuntimeError("audit failed to extract repeated implementation evidence")
        if "`17px`" not in report:
            raise RuntimeError("audit failed to surface one-off geometry evidence")
        run([sys.executable, AUDIT, root, "--check"], expect=1)
        report = report.replace("[PENDING]", "Reviewed:").replace("\nPENDING\n", "\nCOMPLETE\n")
        open(os.path.join(root, "IMPLEMENTATION_GRAMMAR_AUDIT.md"), "w", encoding="utf-8").write(report)
        run([sys.executable, AUDIT, root, "--check"])
    print("implementation grammar audit smoke test passed")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print("FAIL " + str(exc), file=sys.stderr)
        sys.exit(1)
