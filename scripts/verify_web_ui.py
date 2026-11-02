#!/usr/bin/env python3
"""Repo-side entry point for the ui-kit-for-apple-platforms browser checks.

The implementation lives inside the skill, at
.claude/skills/ui-kit-for-apple-platforms/verify_web_ui.py, so that someone who copies
the skill into ~/.claude/skills/ gets a checker that still runs -- the
same arrangement hig-guide uses for check_swiftui.py. This is a shim so
the documented `python3 scripts/verify_web_ui.py` keeps working from the
repo root without a second copy of the code drifting out of step with
the first.
"""

import os
import runpy
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REAL = os.path.join(os.path.dirname(HERE), ".claude", "skills",
                    "ui-kit-for-apple-platforms", "verify_web_ui.py")

if not os.path.exists(REAL):
    sys.exit(f"checker not found at {REAL}")

runpy.run_path(REAL, run_name="__main__")
