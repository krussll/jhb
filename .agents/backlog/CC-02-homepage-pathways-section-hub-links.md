# CC-02: Finish the homepage "featured pathways" section (add hub links)

- **Source document:** `.agents/core-content-promotion-plan.md` (§1.2 "Featured pathways section")
- **Owner:** 🤖 Agent
- **Priority:** Medium
- **Status:** Partly done. `_layouts/home.html` has a "Core guides every bowler should read" section (`.home-core-guides`) with four icon cards (rules, choosing bowls, getting better, singles tactics). Each links to one article only.
- **Depends on:** CC-16 (topic cluster pages) for the best hub targets; until then, use existing hubs

## Task
Line the four homepage cards up with the four named pathways, and give each card a link to its relevant hub alongside the top article.

## Context
- Pathway names: Learn the essentials, Choose your bowls, Practice smarter, Compete with confidence. The current card titles are "Learn the rules", etc.
- Interim hub targets:
  - Learn the essentials → `/getting-started/#step-1` or `/guides/`
  - Choose your bowls → `/reviews/`
  - Practice smarter → `/lawn-bowls-downloadable-drill-pack/` and `/ai-coaching/`
  - Compete with confidence → `/help-and-support/` or a tactics hub
- Switch to the CC-16 cluster pages once they exist.
- Add a short benefit statement to each card (the plan asks for "brief benefit statements").
- The same four-card block is repeated at the bottom of posts (`.post-cornerstone` in `_layouts/post.html`). Consider pulling the card data into `_data/pathways.yml` so both stay in sync. CC-04, CC-05, CC-06, CC-12 and CC-16 can reuse it too.

## Completion criteria
- [ ] Section headings and cards use the four pathway names.
- [ ] Each card has a top-article link and a hub link.
- [ ] Card data comes from one shared source (recommended: `_data/pathways.yml`).
- [ ] `bundle exec jekyll build` completes without errors.
