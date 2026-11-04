# CC-01: Refresh the homepage hero to promote Getting Started and the four pathways

- **Source document:** `.agents/core-content-promotion-plan.md` (§1.1 "Hero module refresh"; Phase 1)
- **Owner:** 🤖 Agent
- **Priority:** High
- **Status:** Not started. The hero's only CTA is "Explore reviews"; the "Start your journey" → `/getting-started` button is **commented out** in `_layouts/home.html` (line ~13).
- **Depends on:** None

> [!NOTE]
> Before starting, ask the user why the Getting Started CTA was commented out. It may have been a deliberate choice.

## Task
Turn the homepage hero into a launchpad: the main CTA goes to `/getting-started/`, the four newcomer pathways are visible as clear CTAs, and a secondary CTA jumps straight to "Learn the essentials".

## Context
- The homepage is `index.html` (front matter only), using `_layouts/home.html`. The hero is the `.home-hero` header at the top of the layout. Styles are in `_sass/_home.scss`.
- The four pathways (goals) are: **Learn the essentials**, **Choose your bowls**, **Practice smarter**, **Compete with confidence**.
- Getting Started already has anchors for each step: `/getting-started/#step-1` (rules), `#step-2` (bowls), `#step-3` (skills), `#step-4` (competitive games).
- Keep the LCP image fast: don't lazy-load the hero image, and keep its width/height set.
- Use the brand palette; no new fonts.

## Completion criteria
- [ ] Primary hero CTA links to `/getting-started/`; secondary CTA links to the "Learn the essentials" pathway (`/getting-started/#step-1`, or the CC-16 cluster page once it exists).
- [ ] All four pathways are linked from the hero (pills or mini-cards).
- [ ] Hero works at mobile, tablet and desktop widths. Lighthouse performance and accessibility ≥ 90 on `/`.
- [ ] `bundle exec jekyll build` completes without errors.
