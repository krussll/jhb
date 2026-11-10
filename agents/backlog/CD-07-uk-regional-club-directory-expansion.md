# CD-07: Phase 2 — Create UK high-intent regional club directory guides

- **Source document:** `.agents/club-directory-seo-plan.md` (§3.1 & §4 Phase 2 "UK High-Intent Regional Expansion")
- **Owner:** 🤖 Agent (Content Curator)
- **Priority:** Medium
- **Status:** Not started
- **Depends on:** CD-01, CD-02, CD-03

## Task
Publish 5 high-depth UK regional bowls club guides targeting high-intent surface/code modifiers (Indoor, Outdoor Flat Green, Crown Green, and Short Mat) backed by structured `_data/clubs/<region>.yml` data files.

## Context
- Rather than publishing dozens of thin county pages, build 5 comprehensive regional hubs where `jackhighbowls.com` has strong UK readership and equipment relevance:
  1. **Glasgow & West of Scotland** (`_data/clubs/glasgow.yml` + `_posts/YYYY-MM-DD-bowls-clubs-in-glasgow.md`) — Outdoor grass & indoor centres (e.g., West of Scotland Indoor, Kelvingrove, Queen's Park, Mount Florida, Titwood).
  2. **London** (`_data/clubs/london.yml` + `_posts/YYYY-MM-DD-bowls-clubs-in-london.md`) — Casual/social greens, historic park clubs, and winter indoor rinks (e.g., Crystal Palace Indoor, Paddington, Finsbury Circus, Battersea Park, Dulwich, Parsons Green, Ravenscourt Park).
  3. **Bristol, Bath, Somerset & Wiltshire** (`_data/clubs/bristol-somerset-wiltshire.yml` + `_posts/YYYY-MM-DD-bowls-clubs-in-bristol-bath-somerset-wiltshire.md`) — Outdoor, indoor (Clarrie Dunbar, City & County of Bristol Indoor, North Wilts Indoor), and short mat clubs.
  4. **Greater Manchester & Lancashire** (`_data/clubs/manchester-lancashire.yml` + `_posts/YYYY-MM-DD-bowls-clubs-in-manchester-and-lancashire.md`) — Explicitly distinguishing **Crown Green** vs. **Flat Green** & **Indoor** clubs.
  5. **Yorkshire** (`_data/clubs/yorkshire.yml` + `_posts/YYYY-MM-DD-bowls-clubs-in-yorkshire.md`) — Crown Green, Flat Green, and Indoor stadiums (York & District Indoor, Leeds, Sheffield, Harrogate).
- Each guide must:
  - Use `categories: [ bowls-clubs ]` and `club_region: "<region>"`.
  - Render `_includes/club-directory-list.html`.
  - Include a regional green-speed and bowl bias recommendation section + `faqs:` front matter.
  - Be added to the Featured Regional Guides section on `_posts/2022-06-01-club-directory.md`.

## Completion criteria
- [ ] All 5 `_data/clubs/<region>.yml` files created with 20+ verified clubs each.
- [ ] All 5 regional guide posts created with `seo_title`, `description`, `club_region`, `faqs`, and regional equipment advice.
- [ ] `_posts/2022-06-01-club-directory.md` updated to link to all 5 new UK regional guides.
- [ ] `bundle exec jekyll build` completes without errors.

