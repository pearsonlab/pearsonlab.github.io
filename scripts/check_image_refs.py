#!/usr/bin/env python3
"""Verify image references in staged HTML and Markdown resolve to local files.

External URLs (http://, https://, //) and Liquid-templated paths are skipped —
lychee covers those in CI. This hook focuses on internal refs, which is where
the value-add is: it catches typos, deleted images that someone forgot to
update, and the "broken /images/foo.jpg" failure mode that just hit us with
the dibs-web01 migration.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Catches src="...", image="...", and Markdown ![alt](url).
# Single-line only; multi-line attribute values are exotic and not worth the
# regex complexity.
URL_PATTERNS = [
    re.compile(r'(?:src|image)=["\']([^"\']+)["\']'),
    re.compile(r'!\[[^\]]*\]\(([^)\s]+)'),
]

IMG_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico", ".bmp"}
EXTERNAL_PREFIXES = ("http://", "https://", "//", "data:", "mailto:")
LIQUID_PAT = re.compile(r"\{[%{]")


def is_skippable(url: str) -> bool:
    if url.startswith(EXTERNAL_PREFIXES):
        return True
    if LIQUID_PAT.search(url):
        return True
    return False


def is_image_path(url: str) -> bool:
    return Path(url.split("?")[0].split("#")[0]).suffix.lower() in IMG_EXTS


def resolve(url: str, repo_root: Path) -> Path:
    """Resolve a root-relative URL to a filesystem path under repo root."""
    clean = url.split("?")[0].split("#")[0].lstrip("/")
    return repo_root / clean


def line_of(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def check_file(path: Path, repo_root: Path) -> list[tuple[int, str, Path]]:
    text = path.read_text(errors="replace")
    failures: list[tuple[int, str, Path]] = []
    for pattern in URL_PATTERNS:
        for match in pattern.finditer(text):
            url = match.group(1)
            if is_skippable(url) or not is_image_path(url):
                continue
            if not url.startswith("/"):
                # Non-leading-slash relative paths are ambiguous under Jekyll
                # (depends on the served URL of the page). Skip them rather
                # than risk false positives — lychee will catch them in CI
                # via the built _site/.
                continue
            target = resolve(url, repo_root)
            if not target.exists():
                failures.append((line_of(text, match.start()), url, target))
    return failures


def main(argv: list[str]) -> int:
    repo_root = Path.cwd()
    total = 0
    for arg in argv:
        path = Path(arg)
        for line, url, target in check_file(path, repo_root):
            rel = target.relative_to(repo_root) if target.is_absolute() else target
            print(
                f"{path}:{line}: broken image ref {url!r} "
                f"(looked for {rel})",
                file=sys.stderr,
            )
            total += 1
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
