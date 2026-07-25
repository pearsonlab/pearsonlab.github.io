#!/usr/bin/env python3
"""
Scrape Google Scholar publications and update publications.yaml
"""

import os
import yaml
import sys
import re
import time
from datetime import date
from scholarly import scholarly, ProxyGenerator

# Force unbuffered output for GitHub Actions
sys.stdout.reconfigure(line_buffering=True)

def create_id_from_publication(first_author_last, year, title):
    """
    Create a unique ID in the format: lastname+year+firstword
    e.g., hayden2009fictive
    """
    # Get first significant word from title (skip common words)
    skip_words = {'the', 'a', 'an', 'in', 'on', 'at', 'of', 'for', 'to', 'and', 'or'}
    title_words = re.findall(r'\w+', title.lower())
    first_word = next((word for word in title_words if word not in skip_words), title_words[0] if title_words else 'paper')

    # Clean and combine
    pub_id = f"{first_author_last.lower()}{year}{first_word}"
    # Remove any non-alphanumeric characters
    pub_id = re.sub(r'[^a-z0-9]', '', pub_id)
    return pub_id

def parse_authors(author_string):
    """
    Parse author string into list of family/given name dictionaries
    """
    if not author_string:
        return []

    authors = []
    # Split by 'and' or commas
    author_list = re.split(r'\s+and\s+|,\s*(?![^,]*,)', author_string)

    for author in author_list:
        author = author.strip()
        if not author:
            continue

        # Try to split into given and family names
        parts = author.split()
        if len(parts) >= 2:
            # Assume last part is family name, rest is given name
            authors.append({
                'family': parts[-1],
                'given': ' '.join(parts[:-1])
            })
        else:
            # Single name, treat as family name
            authors.append({
                'family': author,
                'given': ''
            })

    return authors

def extract_journal_from_citation(citation):
    """
    Try to extract journal name from citation string.
    Google Scholar citations typically start with the journal name.
    Format: "Journal Name, Volume, Pages, Year" or "Journal Name Volume (Issue), Year"
    """
    if not citation:
        return None

    # Split by comma to get the first part (journal name)
    parts = citation.split(',')

    if parts:
        journal = parts[0].strip()

        # Clean up common artifacts - remove trailing volume numbers
        journal = re.sub(r'\s+\d+\s*$', '', journal)

        # Remove year at the end if present
        journal = re.sub(r'\s+\d{4}\s*$', '', journal)

        # Check if reasonable journal name
        if len(journal) > 3 and not re.match(r'^\d+$', journal):
            return journal

    return None

def setup_proxy():
    """
    Configure scholarly to route through a rotating free proxy.

    Google Scholar blocks based on client IP, so each call builds a fresh
    ProxyGenerator (and thus a different proxy). Returns True on success;
    on failure we continue without a proxy (which usually gets blocked,
    prompting the caller to retry with a new proxy).
    """
    try:
        print("Setting up proxy to avoid rate limiting...", flush=True)
        pg = ProxyGenerator()
        pg.FreeProxies()
        scholarly.use_proxy(pg)
        print("Proxy configured successfully", flush=True)
        return True
    except Exception as e:
        print(f"Warning: Could not set up proxy: {e}", flush=True)
        print("Continuing without proxy (may be slower)...", flush=True)
        return False

def normalize_title(title):
    """
    Normalize a title for matching against existing entries: lowercase,
    drop punctuation, collapse whitespace. Used to decide whether a
    publication is already in publications.yaml without relying on the
    generated id (which depends on author data missing from the Scholar
    publication preview).
    """
    return re.sub(r'\s+', ' ', re.sub(r'[^\w\s]', ' ', (title or '').lower())).strip()

def get_publication_stubs(scholar_id):
    """
    Fetch the author's publication list (lightweight previews, not full
    details). Returns the list of publication stubs, or None on failure.
    Assumes a proxy has already been configured.
    """
    try:
        print("Searching for author...", flush=True)
        author = scholarly.search_author_id(scholar_id)
        print("Filling author publications...", flush=True)
        author = scholarly.fill(author, sections=['publications'])
        return author['publications']
    except Exception as e:
        print(f"Error fetching publication list: {e}", flush=True)
        return None

def build_pub_data(pub):
    """
    Fill a single publication's details from Google Scholar and convert it
    to a CSL-style dict. Returns None if the fetch fails (e.g. blocked).
    """
    try:
        filled_pub = scholarly.fill(pub)
        bib = filled_pub['bib']

        # Parse authors
        authors = parse_authors(bib.get('author', ''))

        # Get year
        year = None
        if bib.get('pub_year'):
            try:
                year = int(bib['pub_year'])
            except (ValueError, TypeError):
                pass

        # Create ID
        first_author_last = authors[0]['family'] if authors else 'unknown'
        title = bib.get('title', 'untitled')
        pub_id = create_id_from_publication(first_author_last, year or 0, title)

        # Build publication entry in CSL format
        pub_data = {
            'id': pub_id,
            'type': 'article-journal',
            'author': authors,
            'issued': [{'year': year}] if year else [],
            'title': bib.get('title', ''),
        }

        # Add optional fields if they exist
        # Try multiple possible fields for journal/venue
        container_title = (bib.get('journal') or
                         bib.get('venue') or
                         bib.get('conference') or
                         bib.get('booktitle'))

        # If still no journal, try parsing from citation string
        if not container_title and bib.get('citation'):
            container_title = extract_journal_from_citation(bib['citation'])

        if container_title:
            pub_data['container-title'] = container_title

        if bib.get('publisher'):
            pub_data['publisher'] = bib['publisher']

        if bib.get('pages'):
            pub_data['page'] = bib['pages']

        if bib.get('volume'):
            pub_data['volume'] = str(bib['volume'])

        if bib.get('number') or bib.get('issue'):
            pub_data['issue'] = str(bib.get('number') or bib.get('issue'))

        # Add URL if available
        if filled_pub.get('pub_url'):
            pub_data['URL'] = filled_pub['pub_url']

        print(f"  - Added: {pub_id}", flush=True)
        return pub_data

    except Exception as e:
        print(f"  - Error processing publication: {e}", flush=True)
        return None

def fetch_new_publications(scholar_id, existing_titles, max_attempts=5, wait_between=15):
    """
    Phase 1: fetch full details for publications NOT already in the YAML.

    This is the important fetch (it's how genuinely new papers get added),
    so it retries up to max_attempts times, each with a fresh proxy.

    Returns (stubs, new_pubs):
      - stubs: the full publication-stub list (reused by phase 2)
      - new_pubs: CSL dicts for new publications (empty if none are new)
    On total failure (couldn't get the publication list, or there were new
    entries but every detail fetch was blocked), returns (None, None).
    """
    for attempt in range(1, max_attempts + 1):
        print(f"\n=== New-publication fetch, attempt {attempt}/{max_attempts} ===", flush=True)

        # If we can't get a proxy, don't bother hitting Scholar unproxied:
        # it just gets blocked after a long timeout. Retry for a fresh proxy.
        if not setup_proxy():
            if attempt < max_attempts:
                print(f"Proxy setup failed; retrying in {wait_between}s with a fresh proxy...", flush=True)
                time.sleep(wait_between)
            continue

        stubs = get_publication_stubs(scholar_id)

        if stubs is None:
            if attempt < max_attempts:
                print(f"Could not fetch publication list; retrying in {wait_between}s with a fresh proxy...", flush=True)
                time.sleep(wait_between)
            continue

        new_stubs = [p for p in stubs
                     if normalize_title(p.get('bib', {}).get('title', '')) not in existing_titles]
        print(f"{len(new_stubs)} of {len(stubs)} publications are not yet in the YAML", flush=True)

        if not new_stubs:
            # Got the list; nothing new to add. Success.
            return stubs, []

        new_pubs = []
        for idx, pub in enumerate(new_stubs, 1):
            print(f"Fetching new publication {idx}/{len(new_stubs)}...", flush=True)
            data = build_pub_data(pub)
            if data:
                new_pubs.append(data)

        if new_pubs:
            return stubs, new_pubs

        # Had new publications but couldn't fetch any details (blocked).
        if attempt < max_attempts:
            print(f"Could not fetch any new publication details; retrying in {wait_between}s with a fresh proxy...", flush=True)
            time.sleep(wait_between)

    return None, None

def needs_refresh(entry, today_year=None):
    """
    True if a stored publication could still plausibly change on Scholar.

    Phase 2 used to refetch every entry, which meant one scholarly.fill()
    per publication per run through free proxies. Scholar rate-limits well
    before that many requests, and since phase 2 has no retry, whatever
    falls after the cutoff is silently never refreshed — the failure looks
    identical to "nothing changed". Narrowing the pass to entries that can
    actually change keeps it short enough to finish, and targets exactly
    the preprint-to-journal transition.

    A paper that has sat in the same journal for years has nothing left to
    learn from another fetch.
    """
    if today_year is None:
        today_year = date.today().year

    venue = (entry.get('container-title') or '').strip()
    if not venue:
        return True                       # no venue recorded yet
    if is_preprint_venue(venue):
        return True                       # may since have been published

    issued = entry.get('issued') or []
    year = issued[0].get('year') if issued and isinstance(issued[0], dict) else None
    if not year:
        return True                       # unknown year; keep checking it
    return year >= today_year - 1         # recent enough to still be in flux

def update_existing_publications(stubs, existing_by_title):
    """
    Phase 2: best-effort refresh of publications already in the YAML.

    Updates are nice-to-have (correcting metadata on known papers), so this
    is a single pass with no retry, reusing the proxy from phase 1. Any
    publication that fails to fetch is left as-is (merge_publications keeps
    the existing entry). Only entries selected by needs_refresh are
    refetched. Returns the list of refreshed CSL dicts.
    """
    candidates = []
    skipped = 0
    for pub in stubs:
        entry = existing_by_title.get(normalize_title(pub.get('bib', {}).get('title', '')))
        if entry is None:
            continue                      # not an existing entry; phase 1 owns it
        if needs_refresh(entry):
            candidates.append(pub)
        else:
            skipped += 1

    print(f"\n=== Updating {len(candidates)} existing publications, "
          f"skipping {skipped} settled ones (no retry) ===", flush=True)

    updated = []
    failed = 0
    for idx, pub in enumerate(candidates, 1):
        print(f"Refreshing existing publication {idx}/{len(candidates)}...", flush=True)
        data = build_pub_data(pub)
        if data:
            updated.append(data)
        else:
            failed += 1

    # Make a truncated pass visible. Without this a rate-limited run and a
    # run where genuinely nothing changed produce identical output.
    if failed:
        print(f"WARNING: {failed}/{len(candidates)} refresh fetches failed "
              f"(likely rate-limited); those entries keep their stored data",
              flush=True)
    return updated

def load_existing_yaml(path):
    """
    Load existing publications YAML so we can preserve entries when fetches fail.
    Returns [] if the file is missing or empty.
    """
    if not os.path.exists(path):
        print(f"No existing YAML at {path}; starting fresh", flush=True)
        return []
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f) or []
    print(f"Loaded {len(data)} existing publications from {path}", flush=True)
    return data

# Venue strings that name a preprint server rather than a journal.
PREPRINT_VENUE_RE = re.compile(
    r'\b(biorxiv|medrxiv|arxiv|preprint|ssrn|psyarxiv|osf)\b', re.I)

def is_preprint_venue(venue):
    """True if a container-title names a preprint server, not a journal."""
    return bool(PREPRINT_VENUE_RE.search(venue or ''))

def looks_truncated(new, old):
    """
    True if `new` is a shortened form of `old` rather than a real retitling.

    Scholar intermittently returns titles cut off mid-phrase. Storing one
    corrupts the title *and* breaks title matching on the next run, so the
    paper would come back as a duplicate rather than an update.
    """
    n, o = normalize_title(new), normalize_title(old)
    return bool(n) and bool(o) and n != o and o.startswith(n)

def merge_entry_fields(old, new):
    """
    Field-level merge of a freshly fetched entry onto the stored one.

    Scholar usually wins, but not unconditionally: a refresh must not be
    allowed to replace good data with worse. Returns a new dict.
    """
    merged = dict(old)
    for key, value in new.items():
        # Never let a missing value clobber something we already have.
        if value in (None, '', [], {}):
            continue

        if key == 'title' and looks_truncated(value, old.get('title', '')):
            print(f"    ! keeping stored title; fetched copy is truncated", flush=True)
            continue

        if key == 'container-title':
            old_venue = old.get('container-title') or ''
            # A published paper must never be demoted back to a preprint.
            if old_venue and not is_preprint_venue(old_venue) and is_preprint_venue(value):
                print(f"    ! keeping '{old_venue}' over preprint venue '{value}'", flush=True)
                continue
            # Ignore trailing volume/issue noise, e.g. "Journal, 46 (0)".
            if old_venue and re.fullmatch(
                    re.escape(old_venue) + r'[,\s]+\d+\s*\(\d+\)', value.strip()):
                print(f"    ! keeping '{old_venue}' over '{value}'", flush=True)
                continue

        merged[key] = value
    return merged

def recompute_id(pub):
    """Rebuild an entry's id from its own current author, year, and title."""
    authors = pub.get('author') or []
    first_author_last = (authors[0].get('family') if authors else None) or 'unknown'
    year = 0
    issued = pub.get('issued') or []
    if issued and isinstance(issued[0], dict) and issued[0].get('year'):
        year = issued[0]['year']
    return create_id_from_publication(first_author_last, year, pub.get('title') or 'untitled')

def reconcile_ids(publications):
    """
    Rewrite every id from the entry's own final data.

    ids embed the publication year, so an entry stored while it was a
    preprint keeps a stale id once the paper appears in a journal. Nothing
    in the site templates references ids, so rewriting them is safe and
    keeps each id consistent with the row it labels.
    """
    seen = set()
    changed = 0
    for pub in publications:
        new_id = recompute_id(pub)
        # Disambiguate a genuine collision rather than emitting two rows
        # that share an id.
        if new_id in seen:
            suffix = 'b'
            while f"{new_id}{suffix}" in seen:
                suffix = chr(ord(suffix) + 1)
            new_id = f"{new_id}{suffix}"
        seen.add(new_id)
        if pub.get('id') != new_id:
            print(f"  id: {pub.get('id')} -> {new_id}", flush=True)
            changed += 1
            pub['id'] = new_id
    if changed:
        print(f"Rewrote {changed} publication id(s)", flush=True)
    return publications

def merge_publications(existing, fetched):
    """
    Merge freshly-fetched pubs into the existing list.

    Matching is by normalized title, not by id. ids embed the publication
    year, so a preprint that appears in a journal builds a *different* id;
    the old id-keyed merge therefore appended it as a second entry and left
    the stale preprint row in place, which is why such papers kept
    rendering with a preprint badge. Falls back to id, then to a prefix
    match, so a title Scholar has truncated or expanded still lands on the
    right row instead of forking one.

    Existing entries with no matching fetch are preserved verbatim, so a
    transient fetch failure never drops a publication from the site.
    """
    merged = [dict(p) for p in existing]

    title_index = {}
    id_index = {}
    for i, pub in enumerate(merged):
        title = normalize_title(pub.get('title', ''))
        if title:
            title_index.setdefault(title, i)
        if pub.get('id'):
            id_index.setdefault(pub['id'], i)

    def find_match(pub):
        title = normalize_title(pub.get('title', ''))
        if title and title in title_index:
            return title_index[title]
        if pub.get('id') and pub['id'] in id_index:
            return id_index[pub['id']]
        # Catch titles Scholar has truncated or expanded. Require a decent
        # length so short titles don't collide with unrelated papers.
        if len(title) >= 30:
            for other, i in title_index.items():
                if other.startswith(title) or title.startswith(other):
                    return i
        return None

    updated = 0
    added = 0
    for pub in fetched:
        idx = find_match(pub)
        if idx is None:
            merged.append(pub)
            title = normalize_title(pub.get('title', ''))
            if title:
                title_index.setdefault(title, len(merged) - 1)
            if pub.get('id'):
                id_index.setdefault(pub['id'], len(merged) - 1)
            added += 1
        else:
            merged[idx] = merge_entry_fields(merged[idx], pub)
            updated += 1

    kept = len(existing) - updated
    print(
        f"Merge summary: kept {kept}, updated {updated}, added {added} "
        f"(fetched {len(fetched)} successful, existing {len(existing)})",
        flush=True,
    )
    return reconcile_ids(merged)

def save_to_yaml(publications, output_file):
    """
    Save publications to YAML file in CSL format
    """
    # Sort by year (descending) and then by ID
    publications.sort(key=lambda x: (
        -(x['issued'][0]['year'] if x.get('issued') and x['issued'] else 0),
        x.get('id', '')
    ))

    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(publications, f, default_flow_style=False, allow_unicode=True,
                  sort_keys=False, width=1000, indent=2)

    print(f"\nSuccessfully wrote {len(publications)} publications to {output_file}", flush=True)

if __name__ == "__main__":
    # Configuration
    SCHOLAR_ID = "4whjDosAAAAJ"
    OUTPUT_FILE = "_data/publications.yaml"

    print("Starting publication update...", flush=True)
    existing = load_existing_yaml(OUTPUT_FILE)
    existing_by_title = {normalize_title(p.get('title', '')): p for p in existing}
    existing_titles = set(existing_by_title)

    # Phase 1: fetch genuinely new publications (retried with fresh proxies).
    stubs, new_pubs = fetch_new_publications(SCHOLAR_ID, existing_titles)

    if stubs is None:
        # Couldn't reach Google Scholar at all. Leave publications.yaml
        # untouched (no diff, nothing committed) and exit cleanly so a
        # transient block doesn't fail the workflow; the next run retries.
        print(
            "Could not fetch from Google Scholar after retries; leaving "
            "existing publications unchanged and exiting without error.",
            flush=True,
        )
        sys.exit(0)

    # Phase 2: best-effort refresh of existing entries (not retried).
    updated_pubs = update_existing_publications(stubs, existing_by_title)

    fetched = new_pubs + updated_pubs
    print(f"\nFetched {len(new_pubs)} new and {len(updated_pubs)} updated publications.", flush=True)
    merged = merge_publications(existing, fetched)
    save_to_yaml(merged, OUTPUT_FILE)
    print("Done!", flush=True)
