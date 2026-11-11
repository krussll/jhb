# CD-02: Build reusable club card grid, client-side filter component, and club page generator

- **Source document:** [`.agents/club-directory-seo-plan.md`](../club-directory-seo-plan.md) (§2, §3 & §5 Phase 1 `CD-02`)
- **Owner:** 🤖 Agent (Frontend Implementation)
- **Priority:** High
- **Status:** Not started
- **Depends on:** CD-01
- **Unblocks:** CD-03, CD-04, CD-05, CD-07, CD-08

## Task
Create the reusable Liquid card/filter component (`_includes/club-directory-list.html`), SCSS partial (`_sass/_club-directory.scss`), modular client-side filter script (`assets/js/club-directory-filter.js`), and data-to-collection sync script (`tools/generate_club_pages.py`).

## Context
- **Card Grid & Filter Partial (`_includes/club-directory-list.html`)**:
  - Accepts `region` (e.g. `"edinburgh"`, `"adelaide"`, or `"all"` for the Master Hub page).
  - Styled using the brand palette in `.agents/brand-colours.md`: Deep Blue (`#1F2B5F`), Warm Gold (`#C89B3C`), Neutral Light (`#f8f9fa`), Dark Charcoal (`#222222`).
  - Displays: club `name`, `area` & `postcode` badge, `address`, surface badges (`Outdoor Grass`, `Outdoor Synthetic`, `Indoor Carpet`, `Covered Dome`, `Short Mat`, `Crown Green`), beginner/social tags (`beginner_friendly`, `barefoot_social`, `loan_bowls`), and editorial `summary`.
  - **Dual Action Links on Each Card**:
    - Primary internal link: **"View Club Profile & Green Guide →"** (`/bowls-clubs/{{ club.city }}/{{ club.slug }}/`) when `club.profile_page` is true.
    - Direct utility links: **"Google Maps ↗"** and **"Website ↗"** (if present) so users can jump straight to directions or the club's site if desired.
- **Filter UI (`assets/js/club-directory-filter.js`)**:
  - Accessible filter pills (`All`, `Indoor`, `Outdoor`, `Beginner / Barefoot Friendly`) + live search input for club name, suburb/area, or postcode.
  - Updates a live counter (e.g., *"Showing 36 of 36 clubs"*).
- **Club Page Generator (`tools/generate_club_pages.py`)**:
  - Reads `_data/clubs/*.yml` and writes/updates markdown files in `_clubs/<city>/<slug>.md` for every club with `profile_page: true`, populating frontmatter (`layout: club`, `title`, `seo_title`, `description`, `permalink`, `city`, `city_name`, `city_url`, `faqs`, etc.) so data stays in one YAML place.

## Completion criteria
- [ ] `_includes/club-directory-list.html` supports both single-region (`region="edinburgh"`) and master all-club (`region="all"`) rendering, linking cards through to `/bowls-clubs/<city>/<slug>/`.
- [ ] `_sass/_club-directory.scss` is imported and meets WCAG AA contrast standards.
- [ ] `assets/js/club-directory-filter.js` provides instant pill filtering and text search.
- [ ] `tools/generate_club_pages.py` cleanly generates `_clubs/<city>/<slug>.md` from `_data/clubs/*.yml`.
- [ ] `bundle exec jekyll build` completes without errors.
