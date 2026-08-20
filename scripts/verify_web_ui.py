#!/usr/bin/env python3
"""Repo-side entry point for the apple-ui-kit browser checks.

The implementation lives inside the skill, at
.claude/skills/apple-ui-kit/verify_web_ui.py, so that someone who copies
the skill into ~/.claude/skills/ gets a checker that still runs -- the
same arrangement apple-hig uses for verify_quotes.py. This is a shim so
the documented `python3 scripts/verify_web_ui.py` keeps working from the
repo root without a second copy of the code drifting out of step with
the first.
"""

import os
import runpy
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REAL = os.path.join(os.path.dirname(HERE), ".claude", "skills",
                    "apple-ui-kit", "verify_web_ui.py")

if not os.path.exists(REAL):
    sys.exit(f"checker not found at {REAL}")

runpy.run_path(REAL, run_name="__main__")
