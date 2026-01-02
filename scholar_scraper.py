#!/usr/bin/env python3
"""
Scrape Google Scholar publications and update publications.yaml
"""

import yaml
import sys
import re
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

def get_author_publications(scholar_id):
    """
    Fetch publications from Google Scholar for a given author ID
    """
    print(f"Fetching publications for scholar ID: {scholar_id}", flush=True)
    
    # Set up a proxy generator to avoid rate limiting
    try:
        print("Setting up proxy to avoid rate limiting...", flush=True)
        pg = ProxyGenerator()
        pg.FreeProxies()
        scholarly.use_proxy(pg)
        print("Proxy configured successfully", flush=True)
    except Exception as e:
        print(f"Warning: Could not set up proxy: {e}", flush=True)
        print("Continuing without proxy (may be slower)...", flush=True)
    
    try:
        # Search for author by ID
        print("Searching for author...", flush=True)
        author = scholarly.search_author_id(scholar_id)
        print("Filling author publications...", flush=True)
        author = scholarly.fill(author, sections=['publications'])
        
        publications = []
        total_pubs = len(author['publications'])
        print(f"Found {total_pubs} publications to process", flush=True)
        
        for idx, pub in enumerate(author['publications'], 1):
            try:
                print(f"Processing publication {idx}/{total_pubs}...", flush=True)
                # Fill in publication details
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
                
                publications.append(pub_data)
                print(f"  - Added: {pub_id}", flush=True)
                
            except Exception as e:
                print(f"  - Error processing publication: {e}", flush=True)
                continue
        
        return publications
        
    except Exception as e:
        print(f"Error fetching author publications: {e}", flush=True)
        sys.exit(1)

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
    publications = get_author_publications(SCHOLAR_ID)
    save_to_yaml(publications, OUTPUT_FILE)
    print("Done!", flush=True)
