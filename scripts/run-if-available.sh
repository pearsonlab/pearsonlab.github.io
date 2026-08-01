#!/usr/bin/env bash
#
# Run a pre-commit hook binary, but only if it is actually installed.
#
# The image hooks (jpegoptim, oxipng, svgo) are `language: system`, meaning
# pre-commit expects the binary to already exist. When it doesn't, the hook
# fails with an opaque "Executable not found" rather than skipping — and the
# natural reaction to that is `git commit --no-verify`, which switches off
# every other check too. Skipping one image optimisation locally is a far
# smaller problem than teaching people to bypass the whole hook.
#
# CI installs these tools explicitly (see .github/workflows/pre-commit.yml),
# so enforcement is not weakened there. To be sure of that, a missing binary
# is a hard error when $CI is set.
#
# Usage: scripts/run-if-available.sh <tool> [args...]

set -euo pipefail

if [ "$#" -lt 1 ]; then
    echo "usage: $0 <tool> [args...]" >&2
    exit 2
fi

tool=$1
shift

if ! command -v "$tool" >/dev/null 2>&1; then
    if [ -n "${CI:-}" ]; then
        echo "error: '$tool' is not installed, but this is CI, where it must be." >&2
        echo "       Check the 'Install image tooling' step in the workflow." >&2
        exit 1
    fi
    echo "note: '$tool' not installed — skipping this hook locally." >&2
    echo "      CI still enforces it. Install it with: scripts/install-hooks.sh" >&2
    exit 0
fi

exec "$tool" "$@"
