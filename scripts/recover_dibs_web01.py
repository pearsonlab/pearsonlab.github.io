#!/usr/bin/env python3
"""Download images currently hosted on dibs-web01.vm.duke.edu into the repo.

Tracked by issue #33. Run from the repo root:

    python3 scripts/recover_dibs_web01.py

For each URL, tries the live host first, then falls back to the most
recent Wayback Machine snapshot. Files land under images/ with the
target path shown below. After this finishes, commit the new images
and a separate URL-replacement commit will swap the source files to
the local paths.

Exit code is the number of URLs that couldn't be recovered.
"""

from __future__ import annotations

import os
import sys
import time
import urllib.request
import urllib.error
import urllib.parse


# Mapping of dibs-web01 URLs to the local path we want them at.
# Picked to mirror the categorization in the URL itself.
URLS: dict[str, str] = {
    # Building entrances (location.md)
    "http://dibs-web01.vm.duke.edu/pearson/assets/images/website/admin_ent.jpg":
        "images/location/admin_ent.jpg",
    "http://dibs-web01.vm.duke.edu/pearson/assets/images/website/bryan_ent.jpg":
        "images/location/bryan_ent.jpg",
    "http://dibs-web01.vm.duke.edu/pearson/assets/images/website/bryan_ext.jpg":
        "images/location/bryan_ext.jpg",
    "http://dibs-web01.vm.duke.edu/pearson/assets/images/website/ctn_ent.jpg":
        "images/location/ctn_ent.jpg",
    # People photos (people.html)
    "https://dibs-web01.vm.duke.edu/pearson/assets/images/website/Trevor.jpg":
        "images/Trevor.jpg",
    "https://dibs-web01.vm.duke.edu/pearson/assets/images/website/shiyang.jpg":
        "images/shiyang.jpg",
    # Duke School of Medicine Neurobio Dept logo (_layouts/home.html)
    "https://dibs-web01.vm.duke.edu/pearson/assets/images/website/DUSOM_Dept_Neurobio_stack.jpg":
        "images/DUSOM_Dept_Neurobio_stack.jpg",
    # Research figures (research.md)
    "https://dibs-web01.vm.duke.edu/pearson/assets/images/fmri/website_VAEGAM_fig.png":
        "images/research/website_VAEGAM_fig.png",
    "https://dibs-web01.vm.duke.edu/pearson/assets/images/vocal/vae_finch.png":
        "images/research/vae_finch.png",
    "https://dibs-web01.vm.duke.edu/pearson/assets/images/zebrafish/colorFish.png":
        "images/research/colorFish.png",
    "https://dibs-web01.vm.duke.edu/pearson/assets/images/zebrafish/pipelineNewpng3.png":
        "images/research/pipelineNewpng3.png",
    # Blog post images (_posts/*)
    "https://dibs-web01.vm.duke.edu/pearson/assets/images/website/ava_preprint.png":
        "images/blog/ava_preprint.png",
    "https://dibs-web01.vm.duke.edu/pearson/assets/images/website/raymond_poster.jpg":
        "images/blog/raymond_poster.jpg",
}

WAYBACK_API = "https://archive.org/wayback/available?url="
USER_AGENT = "Mozilla/5.0 (compatible; pearsonlab-recover-script)"
TIMEOUT = 30


def fetch(url: str) -> bytes | None:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            if resp.status == 200:
                data = resp.read()
                if len(data) > 100:  # filter out tiny error pages
                    return data
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError):
        pass
    return None


def wayback_lookup(url: str) -> str | None:
    """Find the most recent Wayback snapshot URL for a given URL."""
    import json
    api_url = WAYBACK_API + urllib.parse.quote(url, safe="")
    try:
        req = urllib.request.Request(api_url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            payload = json.loads(resp.read())
        snapshot = payload.get("archived_snapshots", {}).get("closest")
        if snapshot and snapshot.get("available"):
            return snapshot["url"]
    except Exception:
        pass
    return None


def recover(url: str, dest: str) -> bool:
    print(f"\n[*] {url}")
    print(f"    -> {dest}")
    if os.path.exists(dest):
        print(f"    already exists, skipping")
        return True
    os.makedirs(os.path.dirname(dest), exist_ok=True)

    # Try live host first.
    data = fetch(url)
    source = "dibs-web01" if data else None

    # Fall back to Wayback.
    if not data:
        snapshot_url = wayback_lookup(url)
        if snapshot_url:
            print(f"    trying Wayback: {snapshot_url}")
            data = fetch(snapshot_url)
            if data:
                source = "wayback"

    if not data:
        print(f"    FAILED: not reachable on live host or Wayback")
        return False

    with open(dest, "wb") as f:
        f.write(data)
    size_kb = len(data) / 1024
    print(f"    saved ({size_kb:.0f} KB, source: {source})")
    return True


def main() -> int:
    failed: list[str] = []
    for url, dest in URLS.items():
        if not recover(url, dest):
            failed.append(url)
        time.sleep(0.5)  # be polite

    print(f"\n{'='*60}")
    print(f"Done. Recovered {len(URLS) - len(failed)}/{len(URLS)} images.")
    if failed:
        print(f"\nFailed URLs ({len(failed)}):")
        for url in failed:
            print(f"  - {url}")
        print("\nFor these, options are:")
        print("  - Ask the original author for the file")
        print("  - Manually paste a screenshot or alternate version into the repo")
        print("  - Remove the reference from the source HTML/markdown")
    return len(failed)


if __name__ == "__main__":
    sys.exit(main())
