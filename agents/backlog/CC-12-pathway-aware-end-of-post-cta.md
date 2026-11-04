# CC-12: Make the end-of-post CTA send readers to the next article in their pathway

- **Source document:** `.agents/core-content-promotion-plan.md` (§4.2 "End-of-post CTAs")
- **Owner:** 🤖 Agent
- **Priority:** Medium
- **Status:** Partly done. Every post ends with a standard "Cornerstone guides to explore next" block (`.post-cornerstone` in `_layouts/post.html`), but it always shows the same four static cards. It doesn't suggest the *next* article in the reader's pathway.
- **Depends on:** `next_step` / `pathway` front matter (CC-08 / CC-06)

## Task
Add a "Next in this pathway" block above or instead of the static cards. It should recommend the next article for the current post's pathway, with a fallback to the static cornerstone cards.

## Context
- Logic: if `page.next_step` is set, render it, ideally with the CC-08 action card. Otherwise, if `page.pathway` is set, pick the next post in that pathway's ordered list (from `_data/pathways.yml`). Otherwise show the current cornerstone block.
- Keep the drill pack feature (`_includes/drill-pack-feature.html`) and lead magnet ordering sensible. Don't stack three CTAs in a row without visual separation.

## Completion criteria
- [ ] Core pathway posts show a "Next in this pathway" recommendation pointing to the right next article.
- [ ] Posts without pathway data fall back to the existing cornerstone cards.
- [ ] `bundle exec jekyll build` completes without errors.
