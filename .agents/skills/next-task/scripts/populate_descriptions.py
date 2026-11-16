#!/usr/bin/env python3
import glob
import re
import os

def clean_text(text):
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', text)
    # Remove markdown links
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # Remove markdown formatting characters
    text = re.sub(r'[*_#`]', '', text)
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def create_description(filepath, title, cleaned_body, categories):
    t_clean = title.split('|')[0].split(' - ')[0].split('?')[0].strip()
    
    # Specific targeted patterns based on topic
    lower_t = title.lower()
    lower_f = filepath.lower()
    
    # If the opening paragraph has a solid clean summary
    # Let's extract sentences
    sentences = re.split(r'(?<=[.!?])\s+', cleaned_body)
    candidate = ""
    for s in sentences:
        s = s.strip()
        if len(s) < 20:
            continue
        if any(bad in s.lower() for bad in ["in this article", "in this post", "read on to", "let's dive in", "read our"]):
            continue
        candidate += (" " if candidate else "") + s
        if len(candidate) >= 120:
            break
            
    if 120 <= len(candidate) <= 160:
        desc = candidate
    elif len(candidate) > 160:
        # truncate cleanly to last full word before 155 chars + period
        trimmed = candidate[:155].rsplit(' ', 1)[0]
        if not trimmed.endswith('.'):
            trimmed += '.'
        desc = trimmed
    else:
        # Fallback to synthesized summary
        if 'shoes' in lower_f or 'shoe' in lower_t:
            desc = f"Comprehensive review and buyer's guide for {t_clean}. Explore comfort, grip, sole flexibility, sizing, and durability for lawn bowls."
        elif 'grip' in lower_t:
            desc = f"In-depth guide to {t_clean}. Compare grip patterns, handling feel, wet weather control, and bowling performance."
        elif 'vs' in lower_f:
            desc = f"Compare {t_clean}: bias line, draw trajectory, running surface suitability, and price to help you choose the best model."
        elif 'crown green' in lower_t or 'crown-green' in lower_f:
            desc = f"Complete guide to {t_clean}. Understand bias, weight, density, and equipment rules for crown green bowls."
        else:
            desc = f"Everything you need to know about {t_clean}. Practical lawn bowls tips, technique advice, and rules to improve your game on the green."
            
        if len(desc) > 160:
            desc = desc[:155].rsplit(' ', 1)[0] + '.'
            
    # Clean up double quotes
    desc = desc.replace('"', "'")
    return desc

def main():
    empty_posts = []
    for f in sorted(glob.glob('_posts/*.md')):
        with open(f, 'r') as fp:
            c = fp.read()
        m = re.search(r'^description:\s*([\"\'][\"\']|\s*)$', c, re.MULTILINE)
        if m:
            tm = re.search(r'^title:\s*\"?(.*?)\"?$', c, re.MULTILINE)
            title = tm.group(1) if tm else ''
            cats_m = re.search(r'^categories:\s*\[?(.*?)\]?$', c, re.MULTILINE)
            cats = cats_m.group(1) if cats_m else ''
            parts = c.split('---', 2)
            body = parts[2] if len(parts) >= 3 else ''
            cleaned = clean_text(body)
            empty_posts.append((f, title, cleaned, cats, c))
            
    print(f"Found {len(empty_posts)} posts with empty descriptions.")
    
    for f, title, cleaned, cats, original_content in empty_posts:
        desc = create_description(f, title, cleaned, cats)
        # Verify length
        if len(desc) < 110:
            # Pad or extend
            desc = f"Expert guide to {title.split('|')[0].strip()}: essential rules, delivery technique, equipment tips, and strategies for lawn bowls players."
            if len(desc) > 160:
                desc = desc[:155].rsplit(' ', 1)[0] + '.'
        elif len(desc) > 160:
            desc = desc[:155].rsplit(' ', 1)[0] + '.'
            
        # Replace in original content
        # description: "" or description: '' or description:
        new_content = re.sub(
            r'^description:\s*([\"\'][\"\']|\s*)$',
            f'description: "{desc}"',
            original_content,
            count=1,
            flags=re.MULTILINE
        )
        
        # Also ensure last_modified_at is present/updated
        if 'last_modified_at:' in new_content:
            new_content = re.sub(
                r'^last_modified_at:\s*.*$',
                'last_modified_at: 2026-11-15 11:15:00 +0000',
                new_content,
                count=1,
                flags=re.MULTILINE
            )
        else:
            # insert before closing ---
            parts = new_content.split('---', 2)
            fm = parts[1].rstrip() + '\nlast_modified_at: 2026-11-15 11:15:00 +0000\n'
            new_content = f"---{fm}---{parts[2]}"
            
        with open(f, 'w') as fp:
            fp.write(new_content)
        print(f"Updated {f} ({len(desc)} chars): {desc}")

if __name__ == '__main__':
    main()

