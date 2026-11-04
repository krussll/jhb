# CC-14: Link core posts to their pathway in the `Article` structured data

- **Source document:** `.agents/core-content-promotion-plan.md` (§5.1 "Structured data")
- **Owner:** 🤖 Agent
- **Priority:** Low–Medium
- **Status:** Partly done. `Article` JSON-LD is already output for every post (`_includes/head.html` line ~275), but it has no `about` property linking the post to its pathway. (`knowsAbout` appears only on the homepage `Organization`.)
- **Depends on:** A post-to-pathway mapping (`pathway:` front matter / `_data/pathways.yml`, see CC-06)

## Task
Add an `about` property (and, if appropriate, `isPartOf` pointing to the pathway hub `CollectionPage`) to the `Article` schema for core posts.

## Context
- Example: `"about": {"@type": "Thing", "name": "Learn the essentials of lawn bowls"}`, plus `"isPartOf": {"@type": "CollectionPage", "url": "https://jackhighbowls.com/learn-the-essentials/"}` once CC-16 hubs exist.
- Only add it where `page.pathway` is set. Validate the output.

## Completion criteria
- [ ] Core posts' `Article` JSON-LD includes `about` (and `isPartOf` once the hubs exist), and validates without errors.
- [ ] Non-core posts are unchanged.
- [ ] `bundle exec jekyll build` completes without errors.
