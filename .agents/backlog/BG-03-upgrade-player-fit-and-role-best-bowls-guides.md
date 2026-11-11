# BG-03: Upgrade Player Fit, Role & Crown Green "Best Lawn Bowls" Buyer's Guides

- **Source document:** `.agents/buyers-guides-serp-recovery-plan.md` (§4 Cluster B & §5 `BG-03`)
- **Owner:** 🤖 Agent (Content Curator)
- **Priority:** High
- **Status:** Not started
- **Depends on:** BG-01
- **Unblocks:** BG-07

## Task
Upgrade the 9 Player Fit, Team Position, and Crown Green "Best Lawn Bowls" buyer's guides with `items:` and `faqs:` schema front matter, above-the-fold Storefront Product Grids (`{% include roundup-product-grid.html %}`), and 2026 New vs. Used pricing.

## Context
Target posts in this batch:
1. `_posts/2019-04-09-best-lawn-bowls-for-beginners.md` — Enrich `items:` with `model_id`/pricing, embed `{% include roundup-product-grid.html %}`, and remove `.rounded` class from the Quick Verdict alert box to comply with `AGENTS.md`.
2. `_posts/2018-01-12-best-rated-bowls-for-leads.md` — Enrich `items:` with `model_id`/pricing, embed `{% include roundup-product-grid.html %}`, and ensure square-corner alert styling.
3. `_posts/2022-04-01-best-lawn-bowls-for-skips.md` — Enrich `items:` with `model_id`/pricing, embed `{% include roundup-product-grid.html %}`, and ensure square-corner alert styling.
4. `_posts/2019-07-10-best-lawn-bowls-for-small-hands.md` — Add `items:` (highlighting Aero Z-Scoop, Taylor Xtreme/Progrip, Henselite Mega Grip, Drakes Pride Pro-50) and `faqs:` front matter, Quick Verdict box, and `{% include roundup-product-grid.html %}`.
5. `_posts/2020-07-11-best-lawn-bowls-for-ladies.md` — Add `items:` and `faqs:` front matter, Quick Verdict box, `{% include roundup-product-grid.html %}`, and a size/grip comparison matrix.
6. `_posts/2022-10-14-what-is-the-best-size-of-bowls-for-a-lady.md` — Add `faqs:` front matter, a structured Bowl Size (0000 to 5) diameter/weight table, and clear internal links to `best-lawn-bowls-for-ladies` and `best-lawn-bowls-for-small-hands`.
7. `_posts/2020-10-01-best-junior-lawn-bowls.md` — Add `items:` and `faqs:` front matter, Quick Verdict box, and `{% include roundup-product-grid.html %}` covering size 0000–0 options and second-hand junior sets.
8. `_posts/2022-06-07-best-crown-green-bowls-for-beginners-a-complete-buyers-guide.md` — Add `items:` (Drakes Pride Standard/Deluxe, Taylor Lignoid, Thomas Taylor) and `faqs:` front matter, Quick Verdict box, and `{% include roundup-product-grid.html %}`.
9. `_posts/2022-05-16-best-make-of-crown-green-bowls.md` — Add `items:` and `faqs:` front matter, comparison table (standard vs. high density, 2 bias vs. 2 full bias), and `{% include roundup-product-grid.html %}`.

Update `last_modified_at` on all modified posts.

## Completion criteria
- [ ] All 9 posts include structured `faqs:` and (where products are ranked) `items:` front matter with pricing metadata.
- [ ] Storefront product grids (`{% include roundup-product-grid.html %}`) and Quick Verdict callouts appear above the fold on all product roundups in this cluster.
- [ ] All UI callouts and tables adhere to `border-radius: 0` geometry and brand palette tokens.
- [ ] `bundle exec jekyll build` completes without errors.

