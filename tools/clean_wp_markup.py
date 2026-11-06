#!/usr/bin/env python3
"""
tools/clean_wp_markup.py
Strips leftover WordPress Gutenberg block comments (<!-- wp:... --> and <!-- /wp:... -->)
and obsolete xmlns="http://www.w3.org/1999/xhtml" attributes from posts in _posts/,
leaving YAML front matter, Liquid tags, and visible HTML untouched.
"""

import os
import sys
import re
import glob

def clean_post_content(content):
    # Separate YAML front matter (between initial --- and ---)
    parts = content.split("---", 2)
    if len(parts) >= 3 and content.startswith("---"):
        fm = "---" + parts[1] + "---"
        body = parts[2]
    else:
        fm = ""
        body = content

    # 1. Strip <!-- wp:... --> and <!-- /wp:... --> comments (including multiline JSON attributes)
    # Match the comment and any immediate trailing whitespace on that line
    body = re.sub(r"[ \t]*<!--\s*/?wp:.*?-->[ \t]*\r?\n?", "\n", body, flags=re.DOTALL)

    # 2. Strip xmlns="http://www.w3.org/1999/xhtml"
    body = re.sub(r"""\s*xmlns=[\x27\x22]http://www.w3.org/1999/xhtml[\x27\x22]""", "", body)

    # 3. Collapse 3 or more consecutive newlines into 2
    body = re.sub(r"\n{3,}", "\n\n", body)

    return fm + body

def clean_all_posts(posts_dir="_posts"):
    files = sorted(glob.glob(os.path.join(posts_dir, "*.md")))
    updated_count = 0
    total_comments_removed = 0
    total_xmlns_removed = 0

    for filepath in files:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        comments_before = len(re.findall(r"<!--\s*/?wp:.*?-->", content, flags=re.DOTALL))
        xmlns_before = len(re.findall(r"""xmlns=[\x27\x22]http://www.w3.org/1999/xhtml[\x27\x22]""", content))

        if comments_before == 0 and xmlns_before == 0:
            continue

        cleaned = clean_post_content(content)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(cleaned)

        updated_count += 1
        total_comments_removed += comments_before
        total_xmlns_removed += xmlns_before

    print(f"Cleaned {updated_count} posts.")
    print(f"Removed {total_comments_removed} Gutenberg comments.")
    print(f"Removed {total_xmlns_removed} xmlns attributes.")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "_posts"
    clean_all_posts(target)

