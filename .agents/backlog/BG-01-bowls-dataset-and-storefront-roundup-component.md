# BG-01: Create central bowls dataset, Storefront Roundup Product Grid component, and Enriched Product/Offer Schema

- **Source document:** `.agents/buyers-guides-serp-recovery-plan.md` (§3.1, §3.2, §3.3 & §5 `BG-01`)
- **Owner:** 🤖 Agent (Frontend Implementation)
- **Priority:** Highest
- **Status:** Not started
- **Depends on:** None
- **Unblocks:** BG-02, BG-03, BG-04, BG-05, BG-06

## Task
Build the foundational data, UI component, and Schema.org infrastructure so JHB's "Best X for Y" buyer's guides match ecommerce storefront scannability above the fold and emit rich `ItemList` + nested `Product` + `AggregateOffer` JSON-LD.

## Context
1. **Central Bowls Dataset (`_data/bowls_models.yml`)**:
   - Create `_data/bowls_models.yml` containing structured specifications for all major lawn bowls models reviewed on the site (Taylor Ace, Vector VS, Lazer, International, Blaze, Lignoid; Drakes Pride Professional, Pro-50, XP, d-tec, Fineline, Advantage, Crown Green; Henselite Tiger, Tiger II, Tiger Pro, Tiger EVO, Classic II, Dreamline XG; Aero Quantum, GrooVe, Sonic, Defiance, Profile, Optima).
   - Fields per model: `id`, `brand`, `name`, `slug`, `review_url`, `image`, `bias_score` (1.0–10.0), `bias_label`, `finish_profile`, `surfaces` (array), `ideal_positions` (array), `grips` (array), `small_hands_friendly` (boolean), `sizes`, `price_new_gbp`, `price_used_low_gbp`, `price_used_high_gbp`, `ebay_search_query`, `rating`.
2. **Storefront Product Cards Component (`_includes/roundup-product-grid.html` & `_sass/_roundup-cards.scss`)**:
   - Render a responsive storefront-style product grid from `page.items` (automatically merging model specs from `_data/bowls_models.yml` when `item.model_id` matches, or falling back to front matter fields `item.brand`, `item.bias`, `item.surfaces`, `item.grips`, `item.price_new`, `item.price_used`, `item.url`, `item.image`, `item.award`, `item.verdict`).
   - Follow `.agents/brand-colours.md` and `AGENTS.md` strictly:
     - Sharp square corners (`border-radius: 0;`) on cards, containers, price boxes, and CTA buttons.
     - Rounded pill geometry (`border-radius: 9999px;`) strictly reserved for award badges and spec/surface tags.
     - Brand palette: Deep Blue (`#1F2B5F`), Warm Gold (`#C89B3C`), Neutral Light (`#f8f9fa`), Dark Charcoal (`#222222`).
   - Include a visual 1–10 Bias Meter bar, New RRP vs. Typical Second-Hand (eBay) price box, `"Read Full Review"` link, and `"Check Used on eBay"` search CTA.
   - Import `_roundup-cards` in `_sass/styles.scss`.
3. **Enriched `ItemList` + `Product` + `AggregateOffer` JSON-LD (`_includes/head.html`)**:
   - Update Section 5 (`ItemList Schema for Buyer's Guides & Product Roundups`) in `_includes/head.html` so each `ListItem` nests an `"item": { "@type": "Product", ... }` object when product/pricing fields (or a matching `model_id` in `_data/bowls_models.yml`) are present, including `brand`, `description`, `image`, `url`, and `offers` (`@type: AggregateOffer`, `priceCurrency: GBP`, `lowPrice`, `highPrice`).

## Completion criteria
- [ ] `_data/bowls_models.yml` created with complete specs and 2026 new/used GBP price ranges for 20+ core models.
- [ ] `_includes/roundup-product-grid.html` and `_sass/_roundup-cards.scss` created and compliant with square-corner card geometry (`border-radius: 0`) and brand colours.
- [ ] `_includes/head.html` outputs valid `ItemList` JSON-LD with nested `Product` and `AggregateOffer` data when available.
- [ ] `bundle exec jekyll build` completes cleanly with zero Liquid or SCSS errors.

