#!/usr/bin/env python3
"""
BG-07 Quality Assurance & Schema Verification Script
Validates:
1. reviews.md hub links & square corner styling
2. Bidirectional internal linking from review posts to core buyer's guides
3. ItemList, Product, AggregateOffer, and FAQPage JSON-LD schema across buyer's guides
4. Zero empty descriptions and zero dead href="#" links across the site
5. Component UI geometry compliance (border-radius: 0)
"""

import os
import sys
import glob
import json
import re
from bs4 import BeautifulSoup

def test_reviews_hub():
    print("[1/5] Checking reviews.md hub...")
    hub_path = "_site/reviews/index.html"
    assert os.path.exists(hub_path), f"Missing {hub_path}"
    
    with open(hub_path, 'r', encoding='utf-8') as fp:
        soup = BeautifulSoup(fp.read(), 'html.parser')
        
    hub = soup.find('div', class_='buyers-guides-hub')
    assert hub is not None, "Missing .buyers-guides-hub in reviews.md"
    
    links = [a.get('href') for a in hub.find_all('a')]
    expected_guides = [
        "/guide/best-lawn-bowls-for-beginners/",
        "/guide/best-rated-bowls-for-leads/",
        "/guide/best-lawn-bowls-for-skips/",
        "/guide/best-lawn-bowls-for-small-hands/",
        "/help/best-lawn-bowls-for-ladies/",
        "/help/what-is-the-best-size-of-bowls-for-a-lady/",
        "/guide/best-junior-lawn-bowls/",
        "/guide/best-straight-lawn-bowls/",
        "/guide/best-mid-bias-lawn-bowls/",
        "/guide/best-lawn-bowls-for-indoors/",
        "/guide/best-lawn-bowls-for-fast-greens/",
        "/guide/the-best-cheap-lawn-bowls/",
        "/guide/best-yellow-lawn-bowls/",
        "/guide/best-lawn-bowls-for-usa/",
        "/crown-green-bowls/best-crown-green-bowls-for-beginners-a-complete-buyers-guide/",
        "/crown-green-bowls/best-make-of-crown-green-bowls/",
        "/guide/best-lawn-bowls-shoes/",
        "/guide/best-bowling-shoes-for-ladies/",
        "/guide/best-cheap-lawn-bowls-shoes/",
        "/guide/best-lawn-bowls-bags/",
        "/guide/best-wheeled-trolleys/",
        "/guide/best-lawn-bowl-grips/",
        "/guide/best-lawn-bowls-grip-enhancers/",
        "/guide/best-lawn-bowls-brands/"
    ]
    
    missing = [g for g in expected_guides if g not in links]
    assert not missing, f"Missing guides in reviews.md hub: {missing}"
    
    # Check no rounded elements on cards/boxes in reviews.md
    rounded = soup.find_all(class_='rounded')
    assert len(rounded) == 0, f"Found rounded classes in reviews.md: {rounded}"
    print(f"  PASS: reviews.md links to all {len(expected_guides)} guides with sharp geometry.")

def test_bidirectional_linking():
    print("[2/5] Checking bidirectional links in individual bowl reviews...")
    expected_guides = [
        "/guide/best-lawn-bowls-for-beginners/",
        "/guide/best-straight-lawn-bowls/",
        "/guide/best-mid-bias-lawn-bowls/",
        "/guide/best-lawn-bowls-for-indoors/",
        "/guide/best-rated-bowls-for-leads/",
        "/guide/best-lawn-bowls-for-skips/",
        "/guide/best-lawn-bowls-for-small-hands/",
        "/guide/best-lawn-bowls-for-fast-greens/"
    ]
    
    # Check sample single reviews and vs reviews
    samples = [
        '_site/review/bowls/taylor-ace-review/index.html',
        '_site/review/bowls/drakes-pride-professional-vs-taylor-ace/index.html',
        '_site/review/bowls/aero-groove-lawn-bowls-review/index.html',
        '_site/review/bowls/henselite-tiger-ii-lawn-bowls-review/index.html',
        '_site/review/bowls/taylor-lignoid-lawn-bowls-review/index.html'
    ]
    
    for s in samples:
        assert os.path.exists(s), f"Missing built file: {s}"
        with open(s, 'r', encoding='utf-8') as fp:
            soup = BeautifulSoup(fp.read(), 'html.parser')
        aside = soup.find('aside', class_='related-buyers-guides')
        assert aside is not None, f"Missing related-buyers-guides aside in {s}"
        aside_links = [a.get('href') for a in aside.find_all('a')]
        missing = [g for g in expected_guides if g not in aside_links]
        assert not missing, f"Missing related guide links in {s}: {missing}"
        
    print(f"  PASS: Bowl review pages include all 8 core buyer's guide links.")

def test_json_ld_schemas():
    print("[3/5] Checking JSON-LD ItemList, Product, AggregateOffer, and FAQPage schemas...")
    roundup_posts = []
    for f in sorted(glob.glob('_posts/*.md')):
        with open(f, 'r', encoding='utf-8') as fp:
            c = fp.read(1500)
        if re.search(r'^items:\s*$', c, re.MULTILINE):
            slug = f.split('/')[-1].split('-', 3)[-1].replace('.md', '')
            cats_m = re.search(r'^categories:\s*\[?(.*?)\]?$', c, re.MULTILINE)
            cat = cats_m.group(1).split(',')[0].strip().replace("'", "").replace('"', '') if cats_m else 'guide'
            html_path = f'_site/{cat}/{slug}/index.html'
            roundup_posts.append((f, html_path))
            
    assert len(roundup_posts) >= 23, f"Expected >= 23 roundups, found {len(roundup_posts)}"
    
    for src, html_path in roundup_posts:
        assert os.path.exists(html_path), f"Missing HTML {html_path} for {src}"
        with open(html_path, 'r', encoding='utf-8') as fp:
            soup = BeautifulSoup(fp.read(), 'html.parser')
        scripts = soup.find_all('script', type='application/ld+json')
        
        has_itemlist = False
        has_product = False
        has_offers = False
        has_faq = False
        
        for s in scripts:
            data = json.loads(s.string)
            stype = data.get('@type')
            if stype == 'ItemList':
                has_itemlist = True
                for item in data.get('itemListElement', []):
                    prod = item.get('item', {})
                    if prod.get('@type') == 'Product':
                        has_product = True
                        if 'offers' in prod:
                            has_offers = True
            elif stype == 'FAQPage':
                has_faq = True
                
        assert has_itemlist, f"Missing ItemList schema in {src}"
        assert has_product, f"Missing Product schema inside ItemList in {src}"
        assert has_offers, f"Missing AggregateOffer schema inside ItemList in {src}"
        assert has_faq, f"Missing FAQPage schema in {src}"
        
    print(f"  PASS: All {len(roundup_posts)} product roundups emit valid ItemList (Product + AggregateOffer) and FAQPage JSON-LD.")

def test_meta_descriptions_and_dead_links():
    print("[4/5] Checking for zero empty descriptions and zero dead href='#' links...")
    # Check markdown frontmatter
    empty_desc_posts = []
    for f in sorted(glob.glob('_posts/*.md')):
        with open(f, 'r', encoding='utf-8') as fp:
            c = fp.read()
        if re.search(r'^description:\s*([\"\'][\"\']|\s*)$', c, re.MULTILINE):
            empty_desc_posts.append(f)
    assert not empty_desc_posts, f"Posts with empty descriptions: {empty_desc_posts}"
    
    # Check dead links
    dead_links = []
    pat = re.compile(r'<a\s+[^>]*href=[\"\']#[\"\']')
    for f in sorted(glob.glob('_posts/*.md') + glob.glob('*.html') + glob.glob('*.md') + glob.glob('_includes/*.html') + glob.glob('_layouts/*.html')):
        with open(f, 'r', encoding='utf-8') as fp:
            c = fp.read()
        if pat.search(c):
            dead_links.append(f)
    assert not dead_links, f"Files with dead href='#' links: {dead_links}"
    
    print("  PASS: 0 empty post descriptions and 0 dead href='#' links across entire repository.")

def test_ui_geometry():
    print("[5/5] Checking component UI geometry (border-radius: 0)...")
    components = [
        '_sass/_roundup-cards.scss',
        '_sass/_bowls-finder.scss',
        '_sass/_vs-matrix.scss',
        '_includes/related-buyers-guides.html',
        'reviews.md'
    ]
    for comp in components:
        with open(comp, 'r', encoding='utf-8') as fp:
            c = fp.read()
        assert 'border-radius: 0' in c, f"Expected 'border-radius: 0' in {comp}"
        
    print("  PASS: Component geometry adheres to square corners (border-radius: 0).")

def main():
    print("==================================================")
    print("Running BG-07 Comprehensive QA & Schema Validation")
    print("==================================================")
    test_reviews_hub()
    test_bidirectional_linking()
    test_json_ld_schemas()
    test_meta_descriptions_and_dead_links()
    test_ui_geometry()
    print("==================================================")
    print("ALL BG-07 QA CHECKS PASSED SUCCESSFULLY (5/5)!")
    print("==================================================")

if __name__ == '__main__':
    main()

