# CD-15: USA Club Directory Hub — Pacific Northwest (Washington, Oregon & Northwest Division)

- **Source document:** `.agents/club-directory-seo-plan.md` & Bowls USA Northwest Division expansion
- **Owner:** 🤖 Agent (Content Curator)
- **Priority:** Medium
- **Status:** Not started
- **Depends on:** None (CD-01–CD-03 complete)

## Task
Create the **Pacific Northwest (Washington & Oregon)** lawn bowls club directory hub page, structured YAML club dataset, and individual club profile pages covering Bowls USA's Northwest Division.

## Context
- **Why a Pacific Northwest hub:** Washington and Oregon together form Bowls USA's Northwest Division, with ~6–10 active clubs concentrated around Seattle, Tacoma, Spokane, and Portland. Grouping Washington, Oregon, and neighboring Northwest states (Idaho/Montana/Alaska if any active greens exist) creates a focused regional hub tailored to cooler, moisture-rich Pacific Northwest grass greens—very different from California or Arizona.
- **Target clubs to research & verify (aim for 6–10 verified clubs, including any social/public greens):**
  - **Washington:** Jefferson Park Lawn Bowling Club (Seattle), Tacoma Lawn Bowling Club (Wright Park, Tacoma), Spokane Lawn Bowling Club (Spokane), plus any verified clubs in Bellingham, Olympia, or Bellevue/Eastside.
  - **Oregon:** Portland Lawn Bowling Club (Westmoreland Park, Portland), King City Lawn Bowling Club (Tigard / King City), plus any verified clubs in Eugene, Bend, or Salem.
  - **Broader Northwest:** Verify whether any clubs operate in Idaho, Montana, Wyoming, or Alaska.
- **Technical & editorial requirements:**
  - Create `_data/clubs/pacific-northwest-usa.yml` (`country: "United States"`, `country_code: "US"`, `city: "pacific-northwest-usa"`, `city_name: "Pacific Northwest (WA & OR)"`, `city_url: "/bowls-clubs/bowls-clubs-in-pacific-northwest-usa/"`, `profile_page: true`, ZIP codes in `postcode`).
  - Generate individual club profile pages in `_clubs/pacific-northwest-usa/<slug>.md` using `layout: club`.
  - Create the hub post `_posts/YYYY-MM-DD-bowls-clubs-in-pacific-northwest-usa.md` with `categories: [ bowls-clubs ]`, `club_region: pacific-northwest-usa`, `seo_title`, `description`, `faqs`, `{% include club-directory-list.html region="pacific-northwest-usa" %}`, and a regional playing conditions section covering lush coastal bentgrass/rye greens (10–13s, often heavier in spring/autumn), cross-border proximity to British Columbia (Canada) tournaments, and mid-to-wide bias bowl recommendations linking to `/guide/best-lawn-bowls-for-usa/`.
  - Add a Featured Regional Guide card to `_posts/2022-06-01-club-directory.md` and link from `_posts/2026-11-12-best-lawn-bowls-for-usa.md`.

## Completion criteria
- [ ] `_data/clubs/pacific-northwest-usa.yml` created with all verified Washington, Oregon & Pacific Northwest clubs.
- [ ] Individual `_clubs/pacific-northwest-usa/<slug>.md` profile pages created for all listed clubs.
- [ ] `_posts/YYYY-MM-DD-bowls-clubs-in-pacific-northwest-usa.md` published with `club_region`, `faqs`, interactive directory include, and regional equipment advice.
- [ ] Linked from `_posts/2022-06-01-club-directory.md` and `_posts/2026-11-12-best-lawn-bowls-for-usa.md` (with `last_modified_at` updated on modified posts).
- [ ] `bundle exec jekyll build` completes without errors.
