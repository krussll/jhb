# CC-04: Add a "Choose Your Bowls" dropdown (mega-menu) to the main navigation

- **Source document:** `.agents/core-content-promotion-plan.md` (§2.1 "Primary navigation updates")
- **Owner:** 🤖 Agent
- **Priority:** Medium
- **Status:** Partly done. The top-level "Start Here" → `/getting-started` link **is done** (`_includes/navbar.html` line ~11). The "Choose Your Bowls" panel hasn't been built.
- **Depends on:** None

## Task
Group equipment content under a "Choose Your Bowls" dropdown or mega-menu panel, with quick links to the sizing guide, the buying guide and the reviews hub.

## Context
- Current nav items: Start Here, Guides, AI Coaching, Reviews, About, Contact (Bootstrap 4.6 `navbar-expand-lg`, jQuery and Bootstrap bundle loaded in `_includes/scripts.html`).
- Candidate links (confirm the slugs exist in `_posts/`):
  - `/guide/how-to-choose-a-set-of-lawn-bowls/` (buying guide)
  - the lawn bowls size guide post
  - `/reviews/`
  - the bias guide `/guide/lawn-bowls-bias-guide-and-trajectory-charts-2020/` (check the exact permalink)
  - "best lawn bowls for beginners"-type round-ups
- Must work with the keyboard and touch. Use Bootstrap's dropdown with correct `aria-expanded`/`aria-haspopup`, or a disclosure button pattern. It must also work inside the collapsed mobile menu.
- Decide with the user whether "Reviews" becomes the dropdown, or a new item is added. Avoid an overcrowded nav.

## Completion criteria
- [ ] "Choose Your Bowls" panel is in the nav with at least the sizing guide, buying guide and reviews hub links, all resolving.
- [ ] Fully keyboard-operable; screen-reader states are correct; works in the mobile collapsed menu.
- [ ] `bundle exec jekyll build` completes without errors.
