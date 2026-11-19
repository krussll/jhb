# CD-14: USA Club Directory Hub — Midwest & Central USA (Central Division)

- **Source document:** `.agents/club-directory-seo-plan.md` & Bowls USA Central Division expansion
- **Owner:** 🤖 Agent (Content Curator)
- **Priority:** Medium
- **Status:** Not started
- **Depends on:** None (CD-01–CD-03 complete)

## Task
Create the **Midwest & Central USA** lawn bowls club directory hub page, structured YAML club dataset, and individual club profile pages covering Bowls USA's Central Division (Minnesota, Illinois, Wisconsin, Ohio, Michigan, and surrounding Central states).

## Context
- **Why a Midwest & Central USA hub:** Midwest states typically have 1–4 clubs each, making a single **Midwest & Central USA** hub (~10–14 clubs) far stronger for SEO and user discovery than fragmented state pages. The region also features some of America's most famous social and rooftop/pub lawn bowling venues (such as Brit's Pub in downtown Minneapolis) alongside historic park clubs in Chicago, Milwaukee, and Cincinnati.
- **Target clubs to research & verify (aim for 10–14 verified clubs):**
  - **Minnesota:** Brit's Pub Lawn Bowling (Minneapolis — rooftop social & league greens), Centennial Lakes Park Lawn Bowling (Edina), Brookview Golf & Lawn Bowling Club (Golden Valley), Madden's on Gull Lake (Brainerd).
  - **Illinois:** Chicago Lakeside Lawn Bowling Club (Jackson Park, Chicago).
  - **Wisconsin:** Milwaukee Lake Park Lawn Bowling Club (Milwaukee).
  - **Ohio:** Cincinnati Lawn Bowling Club (Little Miami / Hyde Park), Lakeview Park Lawn Bowling Club (Lorain).
  - **Other Central States:** Any verified active clubs in Michigan, Indiana, Missouri, Iowa, or Texas (e.g., Dallas/Austin/Houston if active).
- **Technical & editorial requirements:**
  - Create `_data/clubs/midwest-central-usa.yml` (`country: "United States"`, `country_code: "US"`, `city: "midwest-central-usa"`, `city_name: "Midwest & Central USA"`, `city_url: "/bowls-clubs/bowls-clubs-in-midwest-and-central-usa/"`, `profile_page: true`, ZIP codes in `postcode`).
  - Generate individual club profile pages in `_clubs/midwest-central-usa/<slug>.md` using `layout: club`.
  - Create the hub post `_posts/YYYY-MM-DD-bowls-clubs-in-midwest-and-central-usa.md` with `categories: [ bowls-clubs ]`, `club_region: midwest-central-usa`, `seo_title`, `description`, `faqs`, `{% include club-directory-list.html region="midwest-central-usa" %}`, and a regional playing conditions section covering May–September summer grass greens (10–13s), social/pub bowling culture (flagging `barefoot_social: true` where applicable), and mid-bias bowl recommendations linking to `/guide/best-lawn-bowls-for-usa/` and `/barefoot-bowls/`.
  - Add a Featured Regional Guide card to `_posts/2022-06-01-club-directory.md` and link from `_posts/2026-11-12-best-lawn-bowls-for-usa.md`.

## Completion criteria
- [ ] `_data/clubs/midwest-central-usa.yml` created with 10+ verified Midwest & Central USA clubs.
- [ ] Individual `_clubs/midwest-central-usa/<slug>.md` profile pages created for all listed clubs.
- [ ] `_posts/YYYY-MM-DD-bowls-clubs-in-midwest-and-central-usa.md` published with `club_region`, `faqs`, interactive directory include, and regional equipment advice.
- [ ] Linked from `_posts/2022-06-01-club-directory.md` and `_posts/2026-11-12-best-lawn-bowls-for-usa.md` (with `last_modified_at` updated on modified posts).
- [ ] `bundle exec jekyll build` completes without errors.
