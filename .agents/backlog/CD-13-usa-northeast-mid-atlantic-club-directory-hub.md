# CD-13: USA Club Directory Hub — Northeast & Mid-Atlantic USA (Northeast Division)

- **Source document:** `.agents/club-directory-seo-plan.md` & Bowls USA Northeast Division expansion
- **Owner:** 🤖 Agent (Content Curator)
- **Priority:** Medium
- **Status:** Not started
- **Depends on:** None (CD-01–CD-03 complete)

## Task
Create the **Northeast & Mid-Atlantic USA** lawn bowls club directory hub page, structured YAML club dataset, and individual club profile pages covering Bowls USA's Northeast Division (New York, New Jersey, Pennsylvania, New England, Maryland, and Virginia).

## Context
- **Why a Northeast & Mid-Atlantic hub:** Individual Northeastern states each contain between 1 and 4 lawn bowling clubs—too few to justify standalone state hubs without thin content. Grouping New York, New Jersey, Pennsylvania, New England, and the Mid-Atlantic into one regional hub mirrors Bowls USA's Northeast Division and brings together ~10–14 historic public park and resort greens (from Central Park in Manhattan to Frick Park in Pittsburgh).
- **Target clubs to research & verify (aim for 10–14 verified clubs):**
  - **New York:** New York Lawn Bowling Club (Central Park, Manhattan), Fernleigh LBC / Upstate NY clubs (e.g., Rochester / Buffalo / Saratoga if active).
  - **New Jersey:** Essex County Lawn Bowling Club (Bloomfield / Watsessing Park).
  - **Pennsylvania:** Frick Park Lawn Bowling Club (Pittsburgh), Buck Hill Falls LBC (Poconos), Skytop LBC (Poconos), Philadelphia / Main Line clubs if active.
  - **New England:** Thistle Lawn Bowling Club (Elizabeth Park, West Hartford, CT), Boston / Massachusetts, Maine (e.g., Camden / Bar Harbor), Vermont / New Hampshire if active.
  - **Mid-Atlantic:** Chesapeake Bay LBC (Maryland/Virginia), Williamsburg / Virginia clubs if active.
- **Technical & editorial requirements:**
  - Create `_data/clubs/northeast-mid-atlantic-usa.yml` (`country: "United States"`, `country_code: "US"`, `city: "northeast-mid-atlantic-usa"`, `city_name: "Northeast & Mid-Atlantic USA"`, `city_url: "/bowls-clubs/bowls-clubs-in-northeast-and-mid-atlantic-usa/"`, `profile_page: true`, ZIP codes in `postcode`).
  - Generate individual club profile pages in `_clubs/northeast-mid-atlantic-usa/<slug>.md` using `layout: club`.
  - Create the hub post `_posts/YYYY-MM-DD-bowls-clubs-in-northeast-and-mid-atlantic-usa.md` with `categories: [ bowls-clubs ]`, `club_region: northeast-mid-atlantic-usa`, `seo_title`, `description`, `faqs`, `{% include club-directory-list.html region="northeast-mid-atlantic-usa" %}`, and a regional playing conditions section covering May–October seasonal bentgrass/Har-Tru greens (10–13s), historic public park access, and mid-to-wide bias bowl recommendations linking to `/guide/best-lawn-bowls-for-usa/`.
  - Add a Featured Regional Guide card to `_posts/2022-06-01-club-directory.md` and link from `_posts/2026-11-12-best-lawn-bowls-for-usa.md`.

## Completion criteria
- [ ] `_data/clubs/northeast-mid-atlantic-usa.yml` created with 10+ verified Northeast & Mid-Atlantic clubs.
- [ ] Individual `_clubs/northeast-mid-atlantic-usa/<slug>.md` profile pages created for all listed clubs.
- [ ] `_posts/YYYY-MM-DD-bowls-clubs-in-northeast-and-mid-atlantic-usa.md` published with `club_region`, `faqs`, interactive directory include, and regional equipment advice.
- [ ] Linked from `_posts/2022-06-01-club-directory.md` and `_posts/2026-11-12-best-lawn-bowls-for-usa.md` (with `last_modified_at` updated on modified posts).
- [ ] `bundle exec jekyll build` completes without errors.
