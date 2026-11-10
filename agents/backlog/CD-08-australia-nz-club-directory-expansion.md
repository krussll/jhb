# CD-08: Phase 3 — Create Australian and New Zealand metro club & barefoot bowls guides

- **Source document:** `.agents/club-directory-seo-plan.md` (§3.1 & §4 Phase 3 "Australian & NZ Metro Expansion")
- **Owner:** 🤖 Agent (Content Curator)
- **Priority:** Medium
- **Status:** Not started
- **Depends on:** CD-01, CD-02, CD-03, CD-05

## Task
Publish 5 Australian and New Zealand metropolitan bowls club guides targeting dual search intent (*"lawn bowls clubs in [city]"* and *"barefoot bowls in [city]"*) backed by structured `_data/clubs/<region>.yml` data files.

## Context
- Target the 5 highest-volume Southern Hemisphere metro hubs to complement the Adelaide guide:
  1. **Melbourne** (`_data/clubs/melbourne.yml` + `_posts/YYYY-MM-DD-bowls-clubs-in-melbourne.md`) — Covering iconic barefoot/social venues (St Kilda, Fitzroy Victoria, Middle Park, Richmond Union, Northcote) and major competitive clubs (Melbourne, Moonee Ponds, Clayton, Darebin, Dandenong).
  2. **Sydney** (`_data/clubs/sydney.yml` + `_posts/YYYY-MM-DD-bowls-clubs-in-sydney.md`) — Covering Bondi, Clovelly, Coogee, Petersham, Marrickville, Neutral Bay, Paddington, St Johns Park, Cabramatta, Merrylands.
  3. **Brisbane & Gold Coast** (`_data/clubs/brisbane-gold-coast.yml` + `_posts/YYYY-MM-DD-bowls-clubs-in-brisbane-and-gold-coast.md`) — Covering Merthyr, New Farm, Booobarran/Booroodabin, Broadbeach, Helensvale, Musgrave Hill, Pine Rivers.
  4. **Perth** (`_data/clubs/perth.yml` + `_posts/YYYY-MM-DD-bowls-clubs-in-perth.md`) — Covering South Perth, Subiaco, Leederville, North Beach, Kardinya, Manning, Sorrento, Osborne Park.
  5. **Auckland** (`_data/clubs/auckland.yml` + `_posts/YYYY-MM-DD-bowls-clubs-in-auckland-new-zealand.md`) — Covering Carlton Cornwall, Remuera, Ponsonby, Royal Oak, Howick, Takapuna, Blockhouse Bay.
- Each guide must:
  - Use `categories: [ bowls-clubs ]` and `club_region: "<region>"`.
  - Render `_includes/club-directory-list.html` with `barefoot_social` and surface (`Outdoor Grass`, `Outdoor Synthetic`, `Covered Dome`) tags.
  - Include fast-green (15–19 second) bowl bias recommendations ([Best Lawn Bowls for Fast Greens](/guide/best-lawn-bowls-for-fast-greens/)) and link from `_posts/2019-08-06-barefoot-bowls.md` and `_posts/2022-06-01-club-directory.md`.

## Completion criteria
- [ ] All 5 `_data/clubs/<region>.yml` files created with 20+ verified clubs each.
- [ ] All 5 metro guide posts created with `seo_title`, `description`, `club_region`, `faqs`, and fast-green equipment advice.
- [ ] Linked from `_posts/2022-06-01-club-directory.md` and `_posts/2019-08-06-barefoot-bowls.md`.
- [ ] `bundle exec jekyll build` completes without errors.

