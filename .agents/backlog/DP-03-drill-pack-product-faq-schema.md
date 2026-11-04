# DP-03: Add `Product` and `FAQPage` JSON-LD to the drill pack page

- **Source documents:** `.agents/drill-pack-cro-plan.md` (§1 gap #6, §3 item 9, §5.3) and `.agents/yahoo-seo-visibility-plan.md` (Phase 3 item 3)
- **Owner:** 🤖 Agent
- **Priority:** High
- **Status:** Not started
- **Depends on:** DP-01 (final price); DP-02 (the FAQ copy should match the visible FAQ)

## Task
Output valid `Product` (with `Offer`) and `FAQPage` structured data on `/lawn-bowls-downloadable-drill-pack/`.

## Context
- `_includes/head.html` already outputs `WebSite`, `BreadcrumbList`, `Article`, `Review` and `ItemList` JSON-LD, but there's no `Product` or `FAQPage` schema anywhere.
- Bing powers Yahoo's organic results. Both Bing and Google use `Product` and `FAQPage` for rich results (price and availability on product cards; "People Also Ask").
- Recommended approach: drive the schema from front matter, e.g. a `product:` block (name, price, currency `GBP`, availability, image, checkout URL) plus an `faqs:` list. Add a conditional block to `head.html` (or a new include) that renders it. The visible FAQ in DP-02 should loop over the same `faqs:` data so the two never drift apart.
- Don't add `aggregateRating` or `review` properties unless genuine, verifiable reviews exist.

## Completion criteria
- [ ] The built `_site/lawn-bowls-downloadable-drill-pack/index.html` contains one valid `Product` block (with an `Offer` showing the current price in GBP) and one valid `FAQPage` block.
- [ ] Both validate with no errors in the Schema.org validator and Google's Rich Results Test.
- [ ] FAQ questions and answers in the schema match the visible on-page FAQ exactly.
- [ ] No other pages pick up the new schema by accident.
- [ ] `bundle exec jekyll build` completes without errors.
