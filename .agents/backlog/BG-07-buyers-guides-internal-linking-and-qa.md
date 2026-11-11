# BG-07: Buyer's Guide Hub Integration, Bidirectional Review Cross-Linking & Schema/Build Verification

- **Source document:** `.agents/buyers-guides-serp-recovery-plan.md` (§4 & §5 `BG-07`)
- **Owner:** 🤖 Agent (Quality Assurance)
- **Priority:** Medium
- **Status:** Not started
- **Depends on:** BG-02, BG-03, BG-04, BG-05, BG-06
- **Unblocks:** None

## Task
Consolidate internal link equity into the upgraded "Best X for Y" buyer's guides from `reviews.md`, `guides.md`, `getting-started.md`, and individual bowl review posts, and verify JSON-LD schema and UI compliance across all 26 buyer's guides.

## Context
1. **Hub Page Upgrades (`reviews.md` & `guides.md`)**:
   - Update `reviews.md` (`/reviews/`) so the "Recommended Buyer's Guides & 'Best Of' Roundups" directory includes all upgraded guides (including **Best Narrow & Straight Bowls**, **Best Crown Green Bowls**, **Best Lawn Bowl Grips**, and **Best Lawn Bowls Brands**), and replace any `.rounded` classes on cards/boxes in `reviews.md` with sharp square corners (`border-radius: 0;`) per `AGENTS.md`.
2. **Bidirectional Linking from Individual Model Reviews**:
   - In `_layouts/post.html` (or via a reusable partial `_includes/related-buyers-guides.html`), ensure individual bowl reviews (`categories contains 'review'` and `categories contains 'bowls'`) link back to the primary commercial roundups (*Best Bowls for Beginners*, *Best Narrow & Straight Bowls*, *Best Mid-Bias Bowls*, *Best Bowls for Indoors*, *Best Bowls for Fast Greens*, *Best Bowls for Small Hands*, *Best Bowls for Leads*, and *Best Bowls for Skips*) with descriptive anchor text.
3. **Sitewide Schema & Quality Audit**:
   - Run an automated verification script across the built `_site/` output to confirm:
     - All 24+ product roundup posts emit valid `ItemList` JSON-LD with nested `Product` and `AggregateOffer` schema and `FAQPage` JSON-LD.
     - Zero posts have empty `description: ""` front matter or dead `<a href="#">` links.
     - All new components (`roundup-product-grid.html`, `bowls-finder.html`, `vs-comparison-matrix.html`) adhere to `border-radius: 0` on boxes/cards/buttons and `.agents/brand-colours.md`.

## Completion criteria
- [ ] `reviews.md` links to all upgraded "Best X for Y" buyer's guides and uses square-corner card geometry (`border-radius: 0`).
- [ ] Individual bowl review pages include contextual internal links back to the core "Best Bowls" buyer's guides.
- [ ] Automated check confirms valid JSON-LD (`ItemList`, `Product`, `FAQPage`) and zero empty meta descriptions across `_site/`.
- [ ] `bundle exec jekyll build` succeeds cleanly.

