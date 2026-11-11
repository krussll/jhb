# CD-04: Complete Edinburgh Bowls Clubs guide and generate rich club profile pages

- **Source document:** [`.agents/club-directory-seo-plan.md`](../club-directory-seo-plan.md) (§2, §3 & §5 Phase 1 `CD-04`)
- **Owner:** 🤖 Agent (Content Curator & Frontend Implementation)
- **Priority:** High
- **Status:** Not started
- **Depends on:** CD-01, CD-02

## Task
Create `_data/clubs/edinburgh.yml` with complete A–Z Edinburgh & Lothian club data, generate individual `_clubs/edinburgh/*.md` club profile pages, and upgrade `_posts/2022-05-02-bowls-clubs-in-edinburgh.md`.

## Context
- Currently `_posts/2022-05-02-bowls-clubs-in-edinburgh.md` stops alphabetically at the letter **E** (22 clubs from *Ardmillan* to *Edinburgh Bowling Club*), omitting all F–Z clubs (even though the intro mentions *Leith* and *Morningside*).
- **Create `_data/clubs/edinburgh.yml`**:
  - Include all existing 22 clubs (cleaning up formatting and replacing dead HTTP links like `http://www.ee.ed.ac.uk/~adr/ckbchome.htm`) plus key F–Z clubs across Edinburgh & Lothian (e.g., *Goldenacre*, *Hillside*, *Juniper Green*, *Leith*, *London Road Foundry*, *Maitland*, *Mayfield*, *Meadowmill Indoor*, *Merchiston*, *Morningside*, *Northern*, *Parkside*, *Pilrig*, *Portobello*, *Postal*, *Sighthill*, *Slateford*, *Summerside*, *Tanfield*, *Trinity*, *Wardie*, *Watsonian*, *West End*, *Willowbrae*).
  - Populate rich fields (`slug`, `area`, `postcode`, `surfaces`, `season`, `beginner_friendly`, `loan_bowls`, `summary`, `about`, `profile_page: true`) and run `python3 tools/generate_club_pages.py` to generate individual club profile pages under `/bowls-clubs/edinburgh/<slug>/`.
- **Upgrade `_posts/2022-05-02-bowls-clubs-in-edinburgh.md`**:
  - Populate `description`, `image: "/img/posts/bowls-clubs-Edinburgh.jpg"`, `club_region: "edinburgh"`, `faqs:`, and update `last_modified_at`.
  - Render the directory via `{% include club-directory-list.html region="edinburgh" %}` so every club card links through to its dedicated profile page.
  - Add a **"Playing Conditions & Best Bowls for Edinburgh Greens"** section connecting Scottish outdoor grass speeds (10–13s) and indoor rinks (Bainfield, Meadowmill, Balbardie) to recommended bowl biases.

## Completion criteria
- [ ] `_data/clubs/edinburgh.yml` contains 35+ A–Z Edinburgh & Lothian clubs with rich metadata.
- [ ] Individual club profile pages are generated in `_clubs/edinburgh/` and linked from the Edinburgh city page.
- [ ] `_posts/2022-05-02-bowls-clubs-in-edinburgh.md` uses `_includes/club-directory-list.html`, removes legacy `.wp-block-columns` HTML, and includes the local green-speed & equipment section + `faqs`.
- [ ] `bundle exec jekyll build` completes without errors.
