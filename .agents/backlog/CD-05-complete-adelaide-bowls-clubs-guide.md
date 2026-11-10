# CD-05: Complete and upgrade the Adelaide Bowls Clubs guide

- **Source document:** `.agents/club-directory-seo-plan.md` (§1, §2.1, §3.2 & §4 Phase 1 `CD-05`)
- **Owner:** 🤖 Agent (Content Curator & Frontend Implementation)
- **Priority:** High
- **Status:** Not started
- **Depends on:** CD-01, CD-02

## Task
Create `_data/clubs/adelaide.yml` expanding coverage to 25+ metropolitan Adelaide clubs and upgrade `_posts/2022-05-02-bowls-clubs-in-adelaide-south-australia.md` with Night Owls / Barefoot Bowls highlights, covered dome green callouts, and Australian fast-green bowl bias recommendations.

## Context
- Currently `_posts/2022-05-02-bowls-clubs-in-adelaide-south-australia.md` lists only 7 clubs (mostly starting with "Adelaide"), has `description: ""`, and contains dead HTTP links (`http://my.webzone.net.au/~hvhornets`).
- **Create `_data/clubs/adelaide.yml`**:
  - Expand to 25+ major metro Adelaide clubs across CBD/Parklands, Eastern Suburbs, Western/Coastal, Northern, and Southern suburbs (including *Adelaide Bowling Club*, *Adelaide Oval*, *Ascot Park*, *Beaumont*, *Brighton*, *Clearview*, *Colonel Light Gardens*, *Edwardstown*, *Gawler*, *Glenelg*, *Grange*, *Hawthorn*, *Henley*, *Holdfast Bay*, *Hope Valley*, *Kensington Marryatville*, *Lockleys*, *Marion*, *Modbury*, *Morphett Vale*, *Norwood*, *Payneham*, *Port Adelaide*, *Prospect Broadview*, *Salisbury*, *Semaphore*, *Somerton*, *Sturt*, *Tranmere*, *Walkerville*, *West Lakes*).
  - Tag clubs with `area`, `postcode`, `surfaces` (`Outdoor Grass`, `Outdoor Synthetic`, `Covered Dome`), `barefoot_social` (Night Owls / Barefoot Bowls), and `notes`.
- **Upgrade `_posts/2022-05-02-bowls-clubs-in-adelaide-south-australia.md`**:
  - Populate `description`, `image: "/img/posts/bowls-clubs-Adelaide.jpg"`, `club_region: "adelaide"`, `faqs:` (covering Adelaide Night Owls / barefoot bowls, covered dome facilities like Marion/Modbury/Tranmere, and Bowls SA Pennant season dates), and update `last_modified_at`.
  - Render the directory via `{% include club-directory-list.html region="adelaide" %}`.
  - Add a **"Green Speeds & Best Bowls for Adelaide Conditions"** section linking to [Best Lawn Bowls for Fast Greens](/guide/best-lawn-bowls-for-fast-greens/), [Henselite Tiger Review](/review/bowls/henselite-tiger-lawn-bowls-review/), [Aero Groove Review](/review/bowls/aero-groove-lawn-bowls-review/), and [Barefoot Bowls Guide](/guide/barefoot-bowls/).

## Completion criteria
- [ ] `_data/clubs/adelaide.yml` contains 25+ metropolitan Adelaide clubs with accurate postcodes, surface types, and Night Owls / Barefoot Bowls tags.
- [ ] `_posts/2022-05-02-bowls-clubs-in-adelaide-south-australia.md` uses `_includes/club-directory-list.html`, removes legacy `.wp-block-columns` HTML, and includes fast-green equipment advice.
- [ ] Front matter includes `description`, `image`, `club_region: "adelaide"`, `faqs`, and updated `last_modified_at`.
- [ ] `bundle exec jekyll build` completes without errors.

