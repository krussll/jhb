#!/usr/bin/env python3
"""
tools/audit_links_and_404s.py
Crawls the compiled _site/ directory, extracts all internal links,
and validates that each href resolves to a valid static file or directory index.
Exits with 0 if no broken links are found; exits with 1 otherwise.
"""

import os
import sys
import re
import urllib.parse

def audit_links(site_dir="_site"):
    if not os.path.isdir(site_dir):
        print(f"Error: {site_dir} directory does not exist. Run 'bundle exec jekyll build' first.")
        return 1

    internal_domains = ["jackhighbowls.com", "krussll.github.io/jhb", "localhost:4000", "127.0.0.1:4000"]

    generated_files = set()
    for root, dirs, files in os.walk(site_dir):
        for f in files:
            rel = os.path.relpath(os.path.join(root, f), site_dir)
            generated_files.add(rel)
            if f == "index.html":
                dir_rel = os.path.relpath(root, site_dir)
                if dir_rel == ".":
                    generated_files.add("")
                    generated_files.add("/")
                else:
                    generated_files.add(dir_rel)
                    generated_files.add(dir_rel + "/")
                    generated_files.add("/" + dir_rel)
                    generated_files.add("/" + dir_rel + "/")

    href_pattern = re.compile(r"""href=[\x27\x22]([^\x27\x22>]+)[\x27\x22]""", re.IGNORECASE)

    issues = {}
    total_links_checked = 0

    for root, dirs, files in os.walk(site_dir):
        for f in files:
            if not f.endswith(".html"):
                continue
            filepath = os.path.join(root, f)
            doc_rel = os.path.relpath(filepath, site_dir)
            doc_dir = os.path.dirname(doc_rel)

            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as fp:
                    content = fp.read()
            except OSError as e:
                print(f"Could not read {filepath}: {e}")
                continue

            for match in href_pattern.finditer(content):
                href = match.group(1).strip()
                if href.startswith(("mailto:", "tel:", "javascript:", "#")):
                    continue

                parsed = urllib.parse.urlparse(href)
                if parsed.netloc:
                    is_internal = False
                    for d in internal_domains:
                        if d in href:
                            is_internal = True
                            break
                    if not is_internal:
                        continue
                    path = parsed.path
                    if "krussll.github.io/jhb" in href:
                        path = path.replace("/jhb", "")
                else:
                    path = parsed.path

                if not path:
                    continue

                total_links_checked += 1
                clean_path = path.split("?")[0].split("#")[0]
                clean_path = urllib.parse.unquote(clean_path)

                if not clean_path.startswith("/"):
                    target = os.path.normpath(os.path.join(doc_dir, clean_path))
                else:
                    target = os.path.normpath(clean_path.lstrip("/"))

                if target == ".":
                    target = ""

                found = False
                for cand in [target, target + "/index.html", target + ".html", target + "/" if target else ""]:
                    if cand in generated_files:
                        found = True
                        break

                if not found:
                    if clean_path not in issues:
                        issues[clean_path] = []
                    issues[clean_path].append((doc_rel, href))

    print(f"Total internal links audited: {total_links_checked}")
    print(f"Total unique broken link targets: {len(issues)}")

    if issues:
        for target, sources in sorted(issues.items()):
            print(f"\n[BROKEN] Target: {target} (count: {len(sources)})")
            for src, raw in sources[:5]:
                print(f"  Source: {src} -> {raw}")
        return 1
    else:
        print("Success: Zero broken internal links found across the site.")
        return 0

if __name__ == "__main__":
    site = sys.argv[1] if len(sys.argv) > 1 else "_site"
    sys.exit(audit_links(site))

