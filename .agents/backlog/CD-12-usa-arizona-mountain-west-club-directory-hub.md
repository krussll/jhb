# CD-12: USA Club Directory Hub — Arizona & Mountain West (South Central Division)

- **Source document:** `.agents/club-directory-seo-plan.md` & Bowls USA South Central Division expansion
- **Owner:** 🤖 Agent (Content Curator)
- **Priority:** Medium
- **Status:** Not started
- **Depends on:** None (CD-01–CD-03 complete)

## Task
Create the **Arizona & Mountain West** lawn bowls club directory hub page, structured YAML club dataset, and individual club profile pages covering Bowls USA's South Central Division (Greater Phoenix / Sun City, Mesa, Tucson, and Colorado / Mountain West).

## Context
- **Why an Arizona & Mountain West hub:** Arizona is one of America's premier competitive lawn bowls strongholds—hosting Bowls USA National Championships on fast desert synthetic greens across Sun City, Sun City West, and Sun City Grand—while neighboring Mountain West states (e.g., Colorado's Washington Park LBC in Denver, plus Utah/Nevada/New Mexico) have 1–2 clubs each. Combining Arizona with the Mountain West creates a cohesive ~12–15 club hub with shared dry-climate, fast-green playing characteristics.
- **Target clubs to research & verify (aim for 12–15 verified clubs):**
  - **Sun City & Sun City West (Phoenix Metro):** Bell LBC, Lakeview LBC, Mountain View LBC, Oakmont LBC, Fairway LBC (Sun City); Johnson LBC (Sun City West); The Grand / Sun City Grand LBC (Surprise).
  - **East Valley & Southern Arizona:** Leisure World LBC (Mesa), Sun Lakes LBC, Green Valley / Tucson area clubs, Scottsdale / Phoenix clubs if active.
  - **Mountain West:** Washington Park Lawn Bowling Club (Denver, CO), plus any verified clubs in Nevada, Utah, or New Mexico.
- **Technical & editorial requirements:**
  - Create `_data/clubs/arizona-mountain-west.yml` (`country: "United States"`, `country_code: "US"`, `city: "arizona-mountain-west"`, `city_name: "Arizona & Mountain West"`, `city_url: "/bowls-clubs/bowls-clubs-in-arizona-and-mountain-west/"`, `profile_page: true`, ZIP codes in `postcode`).
  - Generate individual club profile pages in `_clubs/arizona-mountain-west/<slug>.md` using `layout: club`.
  - Create the hub post `_posts/YYYY-MM-DD-bowls-clubs-in-arizona-and-mountain-west.md` with `categories: [ bowls-clubs ]`, `club_region: arizona-mountain-west`, `seo_title`, `description`, `faqs`, `{% include club-directory-list.html region="arizona-mountain-west" %}`, and a regional playing conditions section covering ultra-fast desert synthetic carpets (15–18s in Arizona) vs. high-altitude grass in Denver, peak winter playing season, and narrow-bias bowl recommendations linking to `/guide/best-lawn-bowls-for-usa/` and `/guide/best-lawn-bowls-for-fast-greens/`.
  - Add a Featured Regional Guide card to `_posts/2022-06-01-club-directory.md` and link from `_posts/2026-11-12-best-lawn-bowls-for-usa.md`.

## Completion criteria
- [ ] `_data/clubs/arizona-mountain-west.yml` created with 12+ verified Arizona & Mountain West clubs.
- [ ] Individual `_clubs/arizona-mountain-west/<slug>.md` profile pages created for all listed clubs.
- [ ] `_posts/YYYY-MM-DD-bowls-clubs-in-arizona-and-mountain-west.md` published with `club_region`, `faqs`, interactive directory include, and regional equipment advice.
- [ ] Linked from `_posts/2022-06-01-club-directory.md` and `_posts/2026-11-12-best-lawn-bowls-for-usa.md` (with `last_modified_at` updated on modified posts).
- [ ] `bundle exec jekyll build` completes without errors.
