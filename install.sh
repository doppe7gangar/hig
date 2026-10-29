#!/usr/bin/env bash
# Installs the skills into ~/.claude/skills, for every Claude Code project.
#
#     curl -fsSL https://raw.githubusercontent.com/doppe7gangar/hig/main/install.sh | bash
#
# Run it again to update. It keeps a copy of the repo in ~/.hig (set
# HIG_DIR to use another folder, or an existing clone) and replaces only
# the five skill folders, so other skills you have stay as they are.
# Add --checks to also install what the design checks need (Playwright).

set -euo pipefail

REPO="https://github.com/doppe7gangar/hig"
SRC="${HIG_DIR:-$HOME/.hig}"
DEST="$HOME/.claude/skills"
SKILLS="android-ui-kit apple-design apple-hig apple-motion apple-ui-kit"

command -v git >/dev/null || { echo "git is needed. On a Mac: xcode-select --install"; exit 1; }

if [ -d "$SRC/.git" ]; then
  echo "Updating $SRC"
  git -C "$SRC" pull --ff-only --quiet
else
  echo "Downloading to $SRC"
  git clone --depth 1 --quiet "$REPO" "$SRC"
fi

mkdir -p "$DEST"
for s in $SKILLS; do
  rm -rf "${DEST:?}/$s"
  cp -R "$SRC/.claude/skills/$s" "$DEST/$s"
  echo "  installed $s"
done

if [ "${1:-}" = "--checks" ]; then
  echo "Installing Playwright for the design checks"
  if python3 -m pip install --quiet playwright pillow 2>/dev/null \
     || python3 -m pip install --quiet --user playwright pillow 2>/dev/null; then
    python3 -m playwright install chromium
  else
    echo "pip refused (common with Homebrew's Python). Use a virtual environment:"
    echo "  python3 -m venv ~/.hig-env && source ~/.hig-env/bin/activate"
    echo "  pip install playwright pillow && python -m playwright install chromium"
  fi
fi

echo
echo "Done. Start Claude Code in any folder (claude) and describe what you want."
echo "To update later, run the same command again."
