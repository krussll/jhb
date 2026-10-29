#!/usr/bin/env python3
"""
Populates descriptive alt attributes across all posts in _posts/
Transforms empty alt="" into descriptive, keyword-rich alt text for:
- Bing Visual Search & Google Images
- Screen readers (a11y)
- Multimodal AI ingestion
"""

import os
import re

POSTS_DIR = os.path.join(os.path.dirname(__file__), "..", "_posts")
MODIFIED_TIMESTAMP = "2026-10-29 15:45:00 +0000"

ICON_MAP = {
    "icon-star": "Rating star icon",
    "icon-star-half": "Half rating star icon",
    "icon-surface": "Bowls playing surface icon",
    "icon-size": "Bowls size chart icon",
    "icon-region": "Bowls region icon",
    "icons": "Bowls equipment icons",
}

def generate_alt(img_tag, post_title):
    # Check for known icons
    for icon_key, icon_alt in ICON_MAP.items():
        if icon_key in img_tag:
            return icon_alt

    # Extract image filename from tag
    fn_match = re.search(r"/img/posts/([^.\x27\" ?]+)", img_tag)
    if not fn_match:
        # Check src=
        src_match = re.search(r"src=[\x27\"]([^\x27\"]+)[\x27\"]", img_tag)
        if src_match:
            fn = os.path.basename(src_match.group(1).split("?")[0])
        else:
            fn = ""
    else:
        fn = fn_match.group(1)

    # Clean dimension suffixes like -1024x576, -300x298, -1, -scaled
    fn_clean = re.sub(r"-\d+x\d+.*$", "", fn)
    fn_clean = re.sub(r"-\d+$", "", fn_clean)
    words = fn_clean.replace("-", " ").replace("_", " ").strip()

    if "vs" in words.lower():
        words_title = " ".join([w.upper() if w.lower() in ("vs", "xp", "tx", "ii", "gtr", "sl") else w.capitalize() for w in words.split()])
        return f"{words_title} lawn bowls comparison"
    elif "review" in words.lower():
        words_title = " ".join([w.upper() if w.lower() in ("vs", "xp", "tx", "ii", "gtr", "sl") else w.capitalize() for w in words.split()])
        return f"{words_title} lawn bowl"
    elif "stance" in words.lower():
        return f"Lawn bowls delivery stance technique diagram"
    elif "reading the head" in words.lower() or "reading-the-head" in fn.lower():
        return f"Reading the head in lawn bowls tactical diagram"
    elif "building the head" in words.lower():
        return f"Building the head tactical bowls diagram"
    elif "trajectory" in words.lower() or "bias" in words.lower():
        return f"Lawn bowls trajectory bias chart"
    elif "scorecard" in words.lower():
        return f"Lawn bowls scorecard layout example"
    elif "wax" in words.lower() or "grip" in words.lower():
        return f"{words.title()} for lawn bowls"
    elif words:
        words_title = words.capitalize()
        return f"{words_title} - {post_title}"
    else:
        return f"{post_title} lawn bowls illustration"

def process_file(filepath, dry_run=False):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract post title
    title_match = re.search(r'^title:\s*["\x27]?([^"\x27\n]+)["\x27]?', content, re.M)
    post_title = title_match.group(1).strip() if title_match else "Jack High Bowls"

    # Find img tags with alt=""
    empty_alt_pattern = re.compile(r'(<img\b(?![^>]*\balt=["\x27][^"\x27]+["\x27])[^>]*?)\balt=["\x27]["\x27]([^>]*>)')
    
    matches = list(empty_alt_pattern.finditer(content))
    if not matches:
        return 0

    def replacer(match):
        prefix = match.group(1)
        suffix = match.group(2)
        full_tag = match.group(0)
        new_alt = generate_alt(full_tag, post_title)
        return f'{prefix}alt="{new_alt}"{suffix}'

    new_content = empty_alt_pattern.sub(replacer, content)

    # Update last_modified_at
    if 'last_modified_at:' in new_content:
        new_content = re.sub(r'last_modified_at:\s*[^\n]+', f'last_modified_at: {MODIFIED_TIMESTAMP}', new_content)
    else:
        # Add after title or description in frontmatter
        new_content = re.sub(r'(---.*?\n)(date:)', rf'\1last_modified_at: {MODIFIED_TIMESTAMP}\n\2', new_content, flags=re.S)

    if not dry_run:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

    return len(matches)

def main(dry_run=False):
    total_files = 0
    total_replacements = 0
    for fname in sorted(os.listdir(POSTS_DIR)):
        if not fname.endswith(".md"): continue
        fpath = os.path.join(POSTS_DIR, fname)
        count = process_file(fpath, dry_run=dry_run)
        if count > 0:
            total_files += 1
            total_replacements += count
            if dry_run and total_files <= 10:
                print(f"[Dry Run] {fname}: {count} image(s) to update")

    action = "Previewed" if dry_run else "Successfully updated"
    print(f"\n{action} {total_replacements} empty alt tags across {total_files} posts.")

if __name__ == "__main__":
    import sys
    dry_run = "--dry-run" in sys.argv
    main(dry_run=dry_run)
