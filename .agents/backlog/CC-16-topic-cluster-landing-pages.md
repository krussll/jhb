# CC-16: Create topic cluster landing pages for the four pathways

- **Source document:** `.agents/core-content-promotion-plan.md` (§5.3 "Topic clusters")
- **Owner:** 🤖 Agent (Content Curator and Frontend)
- **Priority:** Medium
- **Status:** Not started. No pages like `/learn-the-essentials/` exist yet. Existing hubs are `/guides/`, `/reviews/`, `/help-and-support/`, `/getting-started/` and `/ai-coaching/`.
- **Depends on:** A post-to-pathway mapping (agree it with the user, or use the Getting Started step groupings)
- **Unblocks:** CC-02, CC-05, CC-06, CC-11, CC-12, CC-14

## Task
Create four pathway landing pages that pull together the relevant posts, each with a helpful, descriptive introduction.

## Context
- Suggested URLs: `/learn-the-essentials/`, `/choose-your-bowls/`, `/practice-smarter/`, `/compete-with-confidence/`.
- Pattern to follow: `guides.md` and `help-and-support.md` (category listings), `getting-started.md` (custom hub layout).
- Membership: add `pathway:` front matter to posts and list them with `where`, or keep a curated, ordered list in `_data/pathways.yml` (preferred, because the order matters for "next article").
- Each page should have a unique title and meta description, an intro written with real expertise (E-E-A-T), and `CollectionPage`/`ItemList` schema. Add them to `sitemap.xml` (the custom template already sets `weekly` for hub-like URLs; extend its conditions) and to `llms.txt`.
- Update AGENTS.md's cornerstone table if these become cornerstone pages.

## Completion criteria
- [ ] Four pathway pages live at agreed URLs, each listing its posts with an intro of at least 150 words.
- [ ] Pages included in `sitemap.xml` and `llms.txt`, with valid structured data.
- [ ] Linked from Getting Started and the homepage pathways section.
- [ ] Lighthouse accessibility and performance ≥ 90.
- [ ] `bundle exec jekyll build` completes without errors.
