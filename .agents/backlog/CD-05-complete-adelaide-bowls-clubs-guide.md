# CD-05: Complete Adelaide Bowls Clubs guide and generate rich club profile pages

- **Source document:** [`.agents/club-directory-seo-plan.md`](../club-directory-seo-plan.md) (§2, §3 & §5 Phase 1 `CD-05`)
- **Owner:** 🤖 Agent (Content Curator & Frontend Implementation)
- **Priority:** High
- **Status:** Not started
- **Depends on:** CD-01, CD-02

## Task
Create `_data/clubs/adelaide.yml` expanding coverage to 25+ metropolitan Adelaide clubs, generate individual `_clubs/adelaide/*.md` club profile pages, and upgrade `_posts/2022-05-02-bowls-clubs-in-adelaide-south-australia.md`.

## Context
- Currently `_posts/2022-05-02-bowls-clubs-in-adelaide-south-australia.md` lists only 7 clubs, has `description: ""`, and contains dead HTTP links (`http://my.webzone.net.au/~hvhornets`).
- **Create `_data/clubs/adelaide.yml`**:
  - Expand to 25+ major metro Adelaide clubs across CBD/Parklands, Eastern Suburbs, Western/Coastal, Northern, and Southern suburbs (including *Adelaide Bowling Club*, *Adelaide Oval*, *Ascot Park*, *Beaumont*, *Brighton*, *Clearview*, *Colonel Light Gardens*, *Edwardstown*, *Glenelg*, *Grange*, *Hawthorn*, *Henley*, *Holdfast Bay*, *Hope Valley*, *Kensington Marryatville*, *Lockleys*, *Marion*, *Modbury*, *Morphett Vale*, *Norwood*, *Payneham*, *Port Adelaide*, *Prospect Broadview*, *Salisbury*, *Semaphore*, *Somerton*, *Sturt*, *Tranmere*, *Walkerville*, *West Lakes*).
  - Populate rich fields (`slug`, `area`, `postcode`, `surfaces` including `Covered Dome` and `Outdoor Synthetic`, `barefoot_social` for Night Owls / Barefoot Bowls, `summary`, `about`, `profile_page: true`) and run `python3 tools/generate_club_pages.py` to generate `/bowls-clubs/adelaide/<slug>/` profile pages.
- **Upgrade `_posts/2022-05-02-bowls-clubs-in-adelaide-south-australia.md`**:
  - Populate `description`, `image: "/img/posts/bowls-clubs-Adelaide.jpg"`, `club_region: "adelaide"`, `faqs:`, and update `last_modified_at`.
  - Render the directory via `{% include club-directory-list.html region="adelaide" %}` so every club card links through to its dedicated profile page.
  - Add a **"Green Speeds & Best Bowls for Adelaide Conditions"** section linking to [Best Lawn Bowls for Fast Greens](/guide/best-lawn-bowls-for-fast-greens/), [Henselite Tiger Review](/review/bowls/henselite-tiger-lawn-bowls-review/), [Aero Groove Review](/review/bowls/aero-groove-lawn-bowls-review/), and [Barefoot Bowls Guide](/guide/barefoot-bowls/).

## Completion criteria
- [ ] `_data/clubs/adelaide.yml` contains 25+ metropolitan Adelaide clubs with accurate postcodes, surface types, and Night Owls / Barefoot Bowls tags.
- [ ] Individual club profile pages are generated in `_clubs/adelaide/` and linked from the Adelaide city page.
- [ ] `_posts/2022-05-02-bowls-clubs-in-adelaide-south-australia.md` uses `_includes/club-directory-list.html`, removes legacy `.wp-block-columns` HTML, and includes fast-green equipment advice + `faqs`.
- [ ] `bundle exec jekyll build` completes without errors.
