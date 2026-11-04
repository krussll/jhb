# YH-03: Add `FAQPage` structured data to key buyer guides

- **Source document:** `.agents/yahoo-seo-visibility-plan.md` (Phase 3 item 3)
- **Owner:** 🤖 Agent
- **Priority:** Medium
- **Status:** Not started. No `FAQPage` schema exists anywhere in the repo, and no posts have `faq:` front matter.
- **Depends on:** None. Can reuse the `faqs:` rendering built for DP-03 (drill pack `Product`/`FAQPage` schema).

## Task
Add `FAQPage` JSON-LD to the most important buyer guides, generated from front matter so the schema always matches the visible FAQ.

## Context
- Bing and Yahoo use `FAQPage` to fill "People Also Ask"-style panels.
- Candidate pages: the cornerstone buyer guides, e.g. `/guide/how-to-choose-a-set-of-lawn-bowls/` and the "best lawn bowls for…" round-ups that already output `ItemList` schema in `_includes/head.html`. Confirm the target list with the user or with search data.
- Implementation:
  - Add a `faqs:` list (question/answer) to the post front matter.
  - Add a conditional `FAQPage` block to `head.html`.
  - Render a visible FAQ section in `_layouts/post.html` (native `<details>`/`<summary>`) from the same data.
- Answers must be accurate and genuinely useful (E-E-A-T). Use content already in the post where possible.
- AGENTS.md rule: update `last_modified_at` on edited posts.

## Completion criteria
- [ ] At least five priority buyer guides have `faqs:` front matter, a visible FAQ and valid `FAQPage` JSON-LD.
- [ ] Rich Results Test / Schema validator show no errors for those pages.
- [ ] Posts without `faqs:` output no FAQ markup.
- [ ] `bundle exec jekyll build` completes without errors.
