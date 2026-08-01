#!/usr/bin/env bash
#
# Set up the local git pre-commit hook so the checks in
# .pre-commit-config.yaml run before you commit, instead of failing in CI.
#
# Safe to re-run. Run it once per clone:
#
#     scripts/install-hooks.sh
#
# Git hooks live in the repository's common git directory, so this covers
# any worktrees too.

set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

info() { printf '  %s\n' "$*"; }

# --- the hook runner -------------------------------------------------------
# Try each installer in turn and keep going if one fails, rather than
# committing to whichever is merely present: on a network that intercepts
# TLS, uv and pipx can't reach PyPI while Homebrew still works.
if command -v pre-commit >/dev/null 2>&1; then
    info "pre-commit: already installed ($(pre-commit --version))"
else
    for installer in brew uv pipx; do
        command -v "$installer" >/dev/null 2>&1 || continue
        info "pre-commit: trying $installer"
        case $installer in
            brew) brew install pre-commit ;;
            uv) uv tool install pre-commit ;;
            pipx) pipx install pre-commit ;;
        esac && break || info "pre-commit: $installer failed, trying the next"
    done
fi

if ! command -v pre-commit >/dev/null 2>&1; then
    echo "error: could not install pre-commit automatically." >&2
    echo "       Install it yourself, then re-run: https://pre-commit.com/#install" >&2
    exit 1
fi

# --- image tooling ---------------------------------------------------------
# These back the jpegoptim/oxipng hooks. They are optional: without
# them those hooks skip locally (see scripts/run-if-available.sh) and CI
# still enforces them. Installing them just means you find image problems
# before pushing.
if command -v brew >/dev/null 2>&1; then
    for tool in jpegoptim oxipng; do
        if command -v "$tool" >/dev/null 2>&1; then
            info "$tool: already installed"
        else
            info "$tool: installing with Homebrew"
            brew install "$tool"
        fi
    done
else
    info "no Homebrew — skipping jpegoptim/oxipng (those hooks will skip locally)"
fi

# --- install the hook ------------------------------------------------------
pre-commit install
info "hook installed at $(git rev-parse --git-common-dir)/hooks/pre-commit"

cat <<'EOF'

Done. The checks now run on staged files at commit time.

Some hooks fix files rather than just complain (markdownlint --fix, trailing
whitespace, jpegoptim). When one does, the commit is aborted with the fixes
applied but unstaged — re-add and commit again:

    git add -u && git commit

To check everything, not just staged files:   pre-commit run --all-files
To bypass in an emergency:                    git commit --no-verify
EOF
