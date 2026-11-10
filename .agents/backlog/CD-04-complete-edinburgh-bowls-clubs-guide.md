# CD-04: Complete and upgrade the Edinburgh Bowls Clubs guide

- **Source document:** `.agents/club-directory-seo-plan.md` (§1, §2.1, §3.2 & §4 Phase 1 `CD-04`)
- **Owner:** 🤖 Agent (Content Curator & Frontend Implementation)
- **Priority:** High
- **Status:** Not started
- **Depends on:** CD-01, CD-02

## Task
Create `_data/clubs/edinburgh.yml` with complete A–Z Edinburgh & Lothian club data and upgrade `_posts/2022-05-02-bowls-clubs-in-edinburgh.md` to use the interactive card grid, local green-speed equipment advice, and FAQ schema.

## Context
- Currently `_posts/2022-05-02-bowls-clubs-in-edinburgh.md` stops alphabetically at the letter **E** (22 clubs from *Ardmillan* to *Edinburgh Bowling Club*), omitting all F–Z clubs (even though the intro mentions *Leith* and *Morningside*).
- **Create `_data/clubs/edinburgh.yml`**:
  - Include all existing 22 clubs (cleaning up formatting and replacing dead HTTP links like `http://www.ee.ed.ac.uk/~adr/ckbchome.htm`) plus key F–Z clubs across Edinburgh & Lothian (e.g., *Goldenacre*, *Hillside*, *Juniper Green*, *Leith*, *London Road Foundry*, *Maitland*, *Mayfield*, *Meadowmill Indoor*, *Merchiston*, *Morningside*, *Northern*, *Parkside*, *Pilrig*, *Portobello*, *Postal*, *Sighthill*, *Slateford*, *Summerside*, *Tanfield*, *Trinity*, *Wardie*, *Watsonian*, *West End*, *Willowbrae*).
  - Tag each club with `area` (Central, North/Leith, South, East, West, Lothian), `postcode`, `surfaces` (`Outdoor Grass`, `Indoor Carpet`), `beginner_friendly`, and `notes`.
- **Upgrade `_posts/2022-05-02-bowls-clubs-in-edinburgh.md`**:
  - Populate `description`, `image: "/img/posts/bowls-clubs-Edinburgh.jpg"`, `club_region: "edinburgh"`, `faqs:` (4–5 local questions covering indoor winter bowls in Edinburgh, typical outdoor season dates April–September, and beginner open days/Try Bowls), and update `last_modified_at`.
  - Render the directory via `{% include club-directory-list.html region="edinburgh" %}`.
  - Add a **"Playing Conditions & Best Bowls for Edinburgh Greens"** section explaining how Scottish outdoor grass greens (10–13 second speeds) favour mid-to-wide drawing bowls ([Taylor Ace](/review/bowls/taylor-ace-review/), [Drakes Pride Professional](/review/bowls/drakes-pride-professional-review/), [Henselite Tiger II](/review/bowls/henselite-tiger-ii-lawn-bowls-review/)), while indoor rinks at Bainfield, Meadowmill, and Balbardie reward narrower models ([Best Bowls for Indoors](/guide/best-lawn-bowls-for-indoors/)).

## Completion criteria
- [ ] `_data/clubs/edinburgh.yml` contains 35+ A–Z Edinburgh & Lothian clubs with accurate postcodes, areas, and surface tags.
- [ ] `_posts/2022-05-02-bowls-clubs-in-edinburgh.md` uses `_includes/club-directory-list.html`, removes legacy `.wp-block-columns` HTML, and includes the local green-speed & equipment section.
- [ ] Front matter includes `description`, `image`, `club_region: "edinburgh"`, `faqs`, and updated `last_modified_at`.
- [ ] `bundle exec jekyll build` completes without errors.

