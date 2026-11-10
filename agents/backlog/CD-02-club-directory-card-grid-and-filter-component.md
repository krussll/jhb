# CD-02: Build reusable club card grid and client-side filter component

- **Source document:** `.agents/club-directory-seo-plan.md` (§2.1–2.2 "Structured Data-Driven Club Listings & Reusable Card Grid" & §4 Phase 1 `CD-02`)
- **Owner:** 🤖 Agent (Frontend Implementation)
- **Priority:** High
- **Status:** Not started
- **Depends on:** None
- **Unblocks:** CD-04, CD-05, CD-07, CD-08

## Task
Create a reusable Liquid component (`_includes/club-directory-list.html`), SCSS partial (`_sass/_club-directory.scss`), and modular client-side filter script (`assets/js/club-directory-filter.js`) to render structured club listings from `_data/clubs/<region>.yml`.

## Context
- Existing club directory posts use unstyled WordPress Gutenberg markup (`<div class="wp-block-columns">`), which has no CSS rules in `_sass/` and stacks as plain text.
- The new `_includes/club-directory-list.html` partial should accept a `region` parameter (or read `page.club_region`) and iterate over `site.data.clubs[region]`.
- **Card UI**:
  - Styled using the brand palette in `.agents/brand-colours.md`: Deep Blue (`#1F2B5F`), Warm Gold (`#C89B3C`), Neutral Light (`#f8f9fa`), Dark Charcoal (`#222222`).
  - Displays: club `name`, `area` / `postcode` badge, `address`, surface badges (`surfaces` array: e.g., `Outdoor Grass`, `Outdoor Synthetic`, `Indoor Carpet`, `Short Mat`, `Crown Green`), beginner/social tags (`beginner_friendly`, `barefoot_social`, `loan_bowls`), short editorial `notes`, verified `website` link (if present), and a "View on Google Maps" link (`https://www.google.com/maps/search/?api=1&query={{ club.maps_query | default: club.name | uri_escape }}`).
- **Filter UI (`assets/js/club-directory-filter.js`)**:
  - Accessible filter buttons (`All`, `Indoor`, `Outdoor`, `Beginner / Social Friendly`) and a text search input to filter by club name, suburb/area, or postcode in real time.
  - Displays a live count of matching clubs (e.g., *"Showing 28 of 28 clubs"*).

## Completion criteria
- [ ] `_includes/club-directory-list.html` renders a responsive 2-column Bootstrap card grid from `site.data.clubs[region]`.
- [ ] `_sass/_club-directory.scss` is imported in `_sass/styles.scss` or `assets/main.scss` and adheres to WCAG AA contrast requirements in `.agents/brand-colours.md`.
- [ ] `assets/js/club-directory-filter.js` provides keyboard-accessible pill filtering and instant text search without inline JS.
- [ ] `bundle exec jekyll build` completes without errors.

