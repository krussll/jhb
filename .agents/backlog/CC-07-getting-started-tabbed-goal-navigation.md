# CC-07: Add tabbed goal navigation to the Getting Started hero

- **Source document:** `.agents/core-content-promotion-plan.md` (§3.1 "Modular hero")
- **Owner:** 🤖 Agent
- **Priority:** Medium
- **Status:** Not started. `getting-started.md` has a hero with anchor jump links to `#step-1` to `#step-4`, but no tabs that preview the key articles.
- **Depends on:** None

## Task
Let visitors preview the key articles for each of the four goals inside the hero, through an accessible tab interface, without scrolling.

## Context
- File: `getting-started.md` (`layout: default`, custom `.gs-*` markup). Styles are in `_sass/_getting-started.scss`.
- Steps and goals on the page: step-1 "Learn the rules and rhythm of play", step-2 "Pick your first set of bowls", step-3 "Build core skills and repeatable delivery", step-4 "Play your first competitive games".
- Use the WAI-ARIA Tabs pattern (`role="tablist"`/`tab`/`tabpanel`, arrow-key navigation, `aria-selected`, roving `tabindex`). Without JS, the content must stay readable (progressive enhancement: the anchor links still work).
- JS goes in a module under `assets/js/` (e.g., `assets/js/tabs.js`), loaded with `defer`. No inline scripts. Add tests if a JS test setup exists (`npm test`).
- Can reuse the action cards from CC-08 inside each panel.

## Completion criteria
- [ ] Four tabs, one per goal, each previewing two or three key articles with links.
- [ ] Meets the ARIA tabs pattern (keyboard arrows, Home/End, focus management); works without JS.
- [ ] Lighthouse accessibility ≥ 90 on `/getting-started/`.
- [ ] `bundle exec jekyll build` completes without errors.
