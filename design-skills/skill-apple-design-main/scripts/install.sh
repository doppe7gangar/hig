#!/bin/bash
# One-click install all Apple Design skills to your project
# Usage: bash scripts/install.sh [target_dir]
#
# This copies all skills into <target_dir>/.claude/skills/
# or <target_dir>/.mimocode/skills/ (auto-detected)

set -e

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="${1:-.}"

# Detect agent platform
if [ -d "$TARGET/.claude" ] || [ -f "$TARGET/.claude/settings.json" ]; then
  SKILLS_DIR="$TARGET/.claude/skills"
elif [ -d "$TARGET/.mimocode" ] || [ -f "$TARGET/.mimocode/config.json" ]; then
  SKILLS_DIR="$TARGET/.mimocode/skills"
else
  # Default to .claude/skills (most common)
  SKILLS_DIR="$TARGET/.claude/skills"
fi

echo "Installing Apple Design skills to: $SKILLS_DIR"
echo ""

mkdir -p "$SKILLS_DIR"

for skill_dir in "$REPO_DIR"/skills/*/; do
  skill_name=$(basename "$skill_dir")
  echo "  -> $skill_name"
  cp -r "$skill_dir" "$SKILLS_DIR/$skill_name"
done

echo ""
echo "Done! Installed $(ls -d "$SKILLS_DIR"/*/ 2>/dev/null | wc -l | tr -d ' ') skills."
echo ""
echo "Skills installed:"
ls -1 "$SKILLS_DIR"
