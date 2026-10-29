#!/usr/bin/env python3
"""
IndexNow Submission Utility for Jack High Bowls
Submits site URLs to IndexNow (Bing, Yandex, Seznam, Naver) for instant crawl and indexation.
"""

import sys
import os
import json
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET

INDEXNOW_KEY = "e3d7a858cb5d4380a133c9475c4eb18c"
HOST = "krussll.github.io"
KEY_LOCATION = f"https://{HOST}/jhb/{INDEXNOW_KEY}.txt"
API_ENDPOINT = "https://api.indexnow.org/indexnow"

def get_sitemap_urls(sitemap_path):
    if not os.path.exists(sitemap_path):
        print(f"Error: Sitemap not found at {sitemap_path}. Build the site first.")
        sys.exit(1)

    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    # Handle XML namespace
    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    urls = []
    for url_elem in root.findall('ns:url', namespace):
        loc = url_elem.find('ns:loc', namespace)
        if loc is not None and loc.text:
            url = loc.text.strip().replace("http://localhost:4000", f"https://{HOST}")
            urls.append(url)
    return urls

def submit_urls(urls, dry_run=False):
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls[:10000] # IndexNow max per batch is 10,000
    }

    print(f"Found {len(urls)} URLs to submit.")
    if dry_run:
        print("[Dry Run] Prepared IndexNow payload:")
        print(json.dumps(payload, indent=2)[:500] + "... (truncated)")
        return

    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        API_ENDPOINT,
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8"}
    )

    try:
        with urllib.request.urlopen(req) as resp:
            print(f"IndexNow API response status: {resp.status} ({resp.reason})")
            if resp.status in (200, 202):
                print(f"Successfully submitted {len(payload['urlList'])} URLs to IndexNow!")
    except urllib.error.HTTPError as e:
        print(f"IndexNow HTTP Error: {e.code} - {e.read().decode('utf-8', errors='replace')}")
    except Exception as e:
        print(f"Submission failed: {e}")

if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    sitemap_file = os.path.join(repo_root, "_site", "sitemap.xml")

    print(f"Reading sitemap from {sitemap_file}...")
    urls = get_sitemap_urls(sitemap_file)
    submit_urls(urls, dry_run=dry_run)
