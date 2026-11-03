#!/usr/bin/env bash
# The seeded habit tracker the SwiftUI checker's own test grades against.
set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp "$here"/../../scripts/eval/reallife/fixture/*.swift .
