# CC-18: Offer the drill pack on exit intent or after time on page (practice pages)

- **Source document:** `.agents/core-content-promotion-plan.md` (§6.3 "On-site messaging")
- **Owner:** 🤖 Agent
- **Priority:** Low
- **Status:** Not started
- **Depends on:** EM-06. The Kit embed is currently set to `data-format="modal"` with a 5-second timer, and posts already include `_includes/newsletter-modal.html`. Sort out the popup behaviour first, so visitors never see two popups.

## Task
On practice-related pages only, show a drill pack offer when the visitor shows exit intent (desktop) or after enough time on the page or scroll depth (mobile). Throttle it so it never stacks with the newsletter modal.

## Context
- Target pages: posts with practice, drill, weight-control or delivery topics (use a `pathway: practice-smarter` front-matter flag or a category/tag test).
- One popup per session at most, across *all* popups (newsletter and drill pack). Share a single `localStorage`/`sessionStorage` flag with the newsletter modal logic.
- Accessibility: use the native `<dialog>` element (focus trap, Esc to close, return focus). Don't auto-open on page load. Respect `prefers-reduced-motion`.
- JS goes in `assets/js/` (modular, deferred). No inline scripts.
- Mobile intrusive-interstitial guidelines: keep it small, or show it after meaningful engagement.

## Completion criteria
- [ ] Offer appears only on practice-related pages, at most once per session, and never alongside the newsletter modal.
- [ ] Fully accessible dialog (keyboard, screen reader, Esc).
- [ ] No Lighthouse accessibility or performance regression (≥ 90).
- [ ] `bundle exec jekyll build` completes without errors.
