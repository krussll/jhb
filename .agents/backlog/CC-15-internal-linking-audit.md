# CC-15: Internal linking audit: point top posts at the core articles

- **Source document:** `.agents/core-content-promotion-plan.md` (§5.2 "Internal linking audit"; "Ongoing")
- **Owner:** 🤝 Shared: user supplies traffic data, agent edits the content
- **Priority:** Medium
- **Status:** Not started
- **Depends on:** User input

> [!NOTE]
> **User action required:**
> 1. Export the top 20–30 posts by organic traffic from Google Analytics / Search Console (and Bing Webmaster Tools).
> 2. Confirm the list of the **"twelve core articles"**. The plan mentions them but never lists them. Candidates are the resources on `/getting-started/` and the four cornerstone cards (rules, choosing bowls, how to get better, singles tactics).

## Task
Add contextual links with descriptive anchor text from the best-performing posts to the core twelve articles.

## Context
- Prefer natural, descriptive anchors ("how to choose a set of lawn bowls"), not "click here". Two or three links per post at most, placed where they're relevant.
- A helper script (e.g., in `tools/`) can list which top posts already link to each core article, so you can find the gaps.
- AGENTS.md rule: update `last_modified_at` on edited posts.

## Completion criteria
- [ ] The core-twelve list is recorded in this file (or in `_data/pathways.yml`).
- [ ] Every top-traffic post links to at least one relevant core article with descriptive anchor text.
- [ ] No broken internal links introduced (run a link check on the built site).
- [ ] `bundle exec jekyll build` completes without errors.
