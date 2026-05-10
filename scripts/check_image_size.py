#!/usr/bin/env python3
"""Block oversized images. Runs after the compression hooks.

>1 MB blocks the commit. >500 KB warns. Paths in .image-size-overrides
are exempt from blocking (still warned).
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

WARN_BYTES = 500_000
BLOCK_BYTES = 1_000_000
OVERRIDE_FILE = Path(".image-size-overrides")


def load_overrides() -> set[str]:
    if not OVERRIDE_FILE.exists():
        return set()
    paths: set[str] = set()
    for raw in OVERRIDE_FILE.read_text().splitlines():
        line = raw.split("#", 1)[0].strip()
        if line:
            paths.add(line)
    return paths


def humanize(n: int) -> str:
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f} MB"
    return f"{n / 1_000:.0f} KB"


def main(argv: list[str]) -> int:
    overrides = load_overrides()
    blocked: list[tuple[str, int]] = []
    warned: list[tuple[str, int]] = []
    for path in argv:
        try:
            size = os.path.getsize(path)
        except OSError:
            continue
        if path in overrides:
            if size > WARN_BYTES:
                warned.append((path, size))
            continue
        if size > BLOCK_BYTES:
            blocked.append((path, size))
        elif size > WARN_BYTES:
            warned.append((path, size))

    for path, size in warned:
        print(
            f"warning: {path} is {humanize(size)} (>500 KB). "
            f"Consider downscaling.",
            file=sys.stderr,
        )

    for path, size in blocked:
        print(
            f"error: {path} is {humanize(size)} (>1 MB after compression). "
            f"Downscale the image, or add the path to .image-size-overrides "
            f"if the size is justified.",
            file=sys.stderr,
        )

    return 1 if blocked else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
