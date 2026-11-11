# BG-04: Upgrade Footwear, Bags, Trolleys & Grip Accessories "Best Of" Roundups

- **Source document:** `.agents/buyers-guides-serp-recovery-plan.md` (§4 Cluster C & §5 `BG-04`)
- **Owner:** 🤖 Agent (Content Curator)
- **Priority:** High
- **Status:** Not started
- **Depends on:** BG-01
- **Unblocks:** BG-07

## Task
Upgrade the 8 Footwear, Bags, Trolleys, Grips, and Brand "Best Of" buyer's guides with `items:` (`Product` + `AggregateOffer` schema), `faqs:`, Quick Verdict callouts, and Storefront Product Grids (`{% include roundup-product-grid.html %}`).

## Context
Ecommerce retailers dominate equipment accessory SERPs (`"best lawn bowls shoes"`, `"best lawn bowls bags"`, `"best wheeled bowls trolley"`) because informational posts lack above-the-fold product cards and price ranges.
Target posts in this batch:
1. `_posts/2020-09-17-best-lawn-bowls-shoes.md` — Add `items:` (with `brand`, `price_low`, `price_high`, `award`, `verdict`), `faqs:`, Quick Verdict box, `{% include roundup-product-grid.html %}`, and a structured comparison table (Sole Regulation Compliance, Fastening Type, Width Fit, Price).
2. `_posts/2020-07-11-best-bowling-shoes-for-ladies.md` — Add `items:`, `faqs:`, Quick Verdict box, and `{% include roundup-product-grid.html %}`.
3. `_posts/2022-06-07-best-cheap-lawn-bowls-shoes.md` — Add `items:`, `faqs:`, Quick Verdict box, and `{% include roundup-product-grid.html %}`.
4. `_posts/2019-05-01-best-lawn-bowls-bags.md` — Add `items:`, `faqs:`, Quick Verdict box, and `{% include roundup-product-grid.html %}` comparing 2-bowl, 4-bowl, and locker bags.
5. `_posts/2019-09-07-best-wheeled-trolleys.md` — Add `items:`, `faqs:`, Quick Verdict box, and `{% include roundup-product-grid.html %}`.
6. `_posts/2020-07-01-best-lawn-bowls-grip-enhancers.md` — Add `items:`, `faqs:`, Quick Verdict box, and `{% include roundup-product-grid.html %}` comparing Grippo, Taylor Touch, WilGrip, and Henselite Grippit.
7. `_posts/2021-04-27-best-lawn-bowl-grips.md` — Add `items:`, `faqs:`, Quick Verdict box, and a brand-by-brand Grip Depth & Ergonomics comparison table (Aero Z-Scoop, Drakes Pride Pro-50, Taylor Xtreme/Progrip, Henselite Mega Grip).
8. `_posts/2020-06-10-best-lawn-bowls-brands.md` — Add `items:`, `faqs:`, Quick Verdict box, and a comprehensive Brand Comparison Table (Taylor, Drakes Pride, Henselite, Aero) linking directly to each brand's flagship model reviews.

Remove any legacy `.wp-block-*` markup or dead `#` links, and update `last_modified_at` on all 8 posts.

## Completion criteria
- [ ] All 8 posts have `items:` and `faqs:` front matter and updated `last_modified_at`.
- [ ] Product roundups display `{% include roundup-product-grid.html %}` and Quick Verdict boxes above the fold.
- [ ] Legacy `.wp-block-*` markup and broken `#` anchor links are removed.
- [ ] `bundle exec jekyll build` completes without errors.

