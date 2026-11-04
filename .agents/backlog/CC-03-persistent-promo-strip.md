# CC-03: Add a persistent promo strip (drill pack and bowl-buying guides)

- **Source document:** `.agents/core-content-promotion-plan.md` (§1.3 "Persistent promo strip")
- **Owner:** 🤖 Agent
- **Priority:** Low–Medium
- **Status:** Not started
- **Related:** CC-22 (seasonal content swaps, user-owned); CC-18 (exit-intent). Don't stack too many promotional layers.

## Task
Add a slim, dismissible banner, visible on desktop and mobile, that rotates between drill pack and bowl-buying-guide highlights.

## Context
- Put it in `_layouts/default.html`, above or below the navbar (`_includes/navbar.html`, which is a fixed-top Bootstrap 4 navbar). Watch for overlap with the fixed navbar and the masthead padding.
- Drive the content from data (e.g., `_data/promos.yml` with message, link, start/end dates) so seasonal swaps (CC-22) need no code changes.
- Rotation: prefer a CSS/JS rotation that respects `prefers-reduced-motion`, or show a single promo chosen at build time. Avoid auto-rotating carousels that fail WCAG 2.2.2 (pause/stop/hide).
- JS goes in `assets/js/` (no inline scripts). Store dismissal in `localStorage`.
- Mustn't cause layout shift (CLS). Reserve the space, or render it server-side at a fixed height.

## Completion criteria
- [ ] Strip shows on all pages, can be dismissed with the keyboard, and stays dismissed.
- [ ] Content comes from a data file; at least the drill pack and the buying guide (`/guide/how-to-choose-a-set-of-lawn-bowls/`) are included.
- [ ] No CLS regression; Lighthouse accessibility and performance ≥ 90 on `/` and a sample post.
- [ ] `bundle exec jekyll build` completes without errors.
