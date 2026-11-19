# CD-11: USA Club Directory Hub — Florida & Southeast USA (Southeast Division)

- **Source document:** `.agents/club-directory-seo-plan.md` & Bowls USA Southeast Division expansion
- **Owner:** 🤖 Agent (Content Curator)
- **Priority:** Medium
- **Status:** Not started
- **Depends on:** None (CD-01–CD-03 complete)

## Task
Create the **Florida & Southeast USA** lawn bowls club directory hub page, structured YAML club dataset, and individual club profile pages covering Bowls USA's Southeast Division (Florida plus neighboring Southeastern states such as North Carolina and Georgia).

## Context
- **Why a Florida & Southeast hub:** Florida is the third-largest lawn bowls state in the US (~14–16 active clubs, heavily driven by year-round sunshine and winter snowbird leagues), whereas neighboring Southeast states (e.g., North Carolina's Pinehurst Lawn Bowls Club) have only 1–2 clubs each. Grouping Florida with the broader Southeast aligns directly with Bowls USA's Southeast Division and builds a rich ~15–18 club hub without creating thin 1-club state pages.
- **Target clubs to research & verify (aim for 15–18+ verified clubs):**
  - **Central & Gulf Coast Florida:** Mount Dora LBC, Sarasota LBC, St. Petersburg LBC (historic 1916 club), Sun City Center LBC, Clearwater LBC, Lakeland LBC, Bradenton / Sun-n-Fun LBC, Maple Leaf LBC (Port Charlotte), The Villages LBC, World Parkway LBC (Clearwater).
  - **South & East Coast Florida:** Delray Beach LBC, Kings Point LBC (Delray Beach), Lake Worth / Palm Beach area clubs, Century Village / Boca Raton if active.
  - **Southeast (Non-Florida):** Pinehurst Lawn Bowls Club (Pinehurst, NC), plus any verified clubs in Georgia, South Carolina, or Tennessee.
- **Technical & editorial requirements:**
  - Create `_data/clubs/florida-southeast-usa.yml` (`country: "United States"`, `country_code: "US"`, `city: "florida-southeast-usa"`, `city_name: "Florida & Southeast USA"`, `city_url: "/bowls-clubs/bowls-clubs-in-florida-and-southeast-usa/"`, `profile_page: true`, ZIP codes in `postcode`).
  - Generate individual club profile pages in `_clubs/florida-southeast-usa/<slug>.md` using `layout: club`.
  - Create the hub post `_posts/YYYY-MM-DD-bowls-clubs-in-florida-and-southeast-usa.md` with `categories: [ bowls-clubs ]`, `club_region: florida-southeast-usa`, `seo_title`, `description`, `faqs`, `{% include club-directory-list.html region="florida-southeast-usa" %}`, and a regional playing conditions section covering Har-Tru/synthetic carpets, humid Bermuda grass greens, winter snowbird tournament season (November–April), and bowl bias recommendations linking to `/guide/best-lawn-bowls-for-usa/`.
  - Add a Featured Regional Guide card to `_posts/2022-06-01-club-directory.md` and link from `_posts/2026-11-12-best-lawn-bowls-for-usa.md`.

## Completion criteria
- [ ] `_data/clubs/florida-southeast-usa.yml` created with 15+ verified Florida & Southeast USA clubs.
- [ ] Individual `_clubs/florida-southeast-usa/<slug>.md` profile pages created for all listed clubs.
- [ ] `_posts/YYYY-MM-DD-bowls-clubs-in-florida-and-southeast-usa.md` published with `club_region`, `faqs`, interactive directory include, and regional equipment advice.
- [ ] Linked from `_posts/2022-06-01-club-directory.md` and `_posts/2026-11-12-best-lawn-bowls-for-usa.md` (with `last_modified_at` updated on modified posts).
- [ ] `bundle exec jekyll build` completes without errors.
