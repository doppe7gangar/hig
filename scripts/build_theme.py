#!/usr/bin/env python3
"""Repo-side entry point for the theme generator.

The implementation lives inside the skill, at
.claude/skills/apple-design/build_theme.py, so that someone who copies
the skill into ~/.claude/skills/ gets a generator that still runs. The
skill's own instructions tell you to run it; those instructions travel
with the skill, so the code has to as well. This shim keeps the
documented `python3 scripts/build_theme.py` working from the repo root
without a second copy drifting out of step.
"""

import os
import runpy
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REAL = os.path.join(os.path.dirname(HERE), ".claude", "skills",
                    "apple-design", "build_theme.py")

if not os.path.exists(REAL):
    sys.exit(f"generator not found at {REAL}")

runpy.run_path(REAL, run_name="__main__")
