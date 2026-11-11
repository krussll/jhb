# BG-02: Upgrade Bias & Surface "Best Lawn Bowls" Buyer's Guides

- **Source document:** `.agents/buyers-guides-serp-recovery-plan.md` (§4 Cluster A & §5 `BG-02`)
- **Owner:** 🤖 Agent (Content Curator)
- **Priority:** Highest
- **Status:** Not started
- **Depends on:** BG-01
- **Unblocks:** BG-07

## Task
Overhaul the 6 core Bias & Surface "Best Lawn Bowls" buyer's guides so they feature exact-match commercial title/H1 modifiers, above-the-fold Storefront Product Grids (`{% include roundup-product-grid.html %}`), updated 2026 New vs. Used GBP pricing, `items:` schema front matter, and `faqs:` front matter.

## Context
Target posts in this batch:
1. `_posts/2020-10-29-best-straight-lawn-bowls.md`
   - Update `title` / `seo_title` to capture **"Best Narrow Bowls"** & **"Best Straight Lawn Bowls"** (e.g. `"7 Best Narrow & Straight Lawn Bowls (2026 Bias Guide)"`).
   - Add `items:` (with `model_id` / pricing fields) and `faqs:` front matter.
   - Replace unstyled `.wp-block-table` and dead `<a href="#">` image links with a Quick Verdict box, `{% include roundup-product-grid.html %}`, and a full 2026 comparison table including New vs. Used eBay prices.
2. `_posts/2022-04-22-best-mid-bias-lawn-bowls.md`
   - Add `items:` and `faqs:` front matter.
   - Update outdated 2022 prices (£285–£295) to accurate 2026 New vs. Second-Hand prices.
   - Add Quick Verdict box, `{% include roundup-product-grid.html %}`, and updated comparison table.
3. `_posts/2020-08-05-best-lawn-bowls-for-indoors.md`
   - Add `items:` and `faqs:` front matter.
   - Replace outdated 2020 prices (£219–£299) with 2026 New vs. Used pricing, Quick Verdict box, and `{% include roundup-product-grid.html %}`.
4. `_posts/2019-07-25-best-lawn-bowls-for-fast-greens.md`
   - Enrich existing `items:` front matter with `model_id` / pricing metadata and embed `{% include roundup-product-grid.html %}` above the fold.
5. `_posts/2022-04-18-the-best-cheap-lawn-bowls.md`
   - Add `items:` and `faqs:` front matter focusing on best-value second-hand models (Drakes Pride Professional, Taylor Ace, Henselite Classic II, Taylor Vector VS) with World Bowls stamp verification tips and `{% include roundup-product-grid.html %}`.
6. `_posts/2022-04-06-best-yellow-lawn-bowls.md`
   - Add `items:` and `faqs:` front matter, remove any broken links or legacy WP blocks, and include `{% include roundup-product-grid.html %}`.

Ensure all boxes/buttons use `border-radius: 0` (no Bootstrap `.rounded` on alert or card boxes) and update `last_modified_at` on every modified post.

## Completion criteria
- [ ] All 6 posts have complete `items:` (with `model_id` / pricing) and `faqs:` front matter and updated `last_modified_at`.
- [ ] `_posts/2020-10-29-best-straight-lawn-bowls.md` explicitly targets both "Narrow" and "Straight" bowls in its title, H1, description, and comparison table.
- [ ] Every post renders `{% include roundup-product-grid.html %}` near the top of the article and contains zero dead `<a href="#">` links or unstyled `.wp-block-table` markup.
- [ ] `bundle exec jekyll build` succeeds without errors.

