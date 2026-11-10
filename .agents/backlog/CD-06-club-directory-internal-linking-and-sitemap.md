# CD-06: Wire internal links from cornerstone hubs and beginner guides to the Club Directory

- **Source document:** `.agents/club-directory-seo-plan.md` (§3.3 "Internal Linking Flywheel" & §4 Phase 1 `CD-06`)
- **Owner:** 🤖 Agent (Content Curator & Frontend Implementation)
- **Priority:** High
- **Status:** Not started
- **Depends on:** CD-03, CD-04, CD-05

## Task
Eliminate the orphan status of the Bowls Club Directory by adding prominent navigation and contextual internal links from cornerstone pages, sitewide footer navigation, and high-traffic beginner guides.

## Context
- Currently zero pages outside `/bowls-clubs/` link to `/bowls-clubs/club-directory/`, `/bowls-clubs/bowls-clubs-in-edinburgh/`, or `/bowls-clubs/bowls-clubs-in-adelaide-south-australia/`.
- **Target files to update**:
  1. `_includes/footer-nav.html`: Add a "Bowls Club Directory" link (`/bowls-clubs/club-directory/`) under the **Resources** column.
  2. `getting-started.md`: Add an action card or resource tile in Step 1 or Step 4 linking to `/bowls-clubs/club-directory/` (*"Find a local bowls club"*).
  3. `_posts/2019-08-06-barefoot-bowls.md`: Link to `/bowls-clubs/club-directory/` and `/bowls-clubs/bowls-clubs-in-adelaide-south-australia/` where finding a barefoot bowls club is discussed.
  4. `_posts/2018-03-01-guide-to-short-mat-bowls.md`: Replace the broken `<a href="#">bowls.co.uk</a>` link in `#find-a-club` with a link to `/bowls-clubs/club-directory/`.
  5. `_posts/2020-06-16-how-much-does-lawn-bowls-cost.md` & `_posts/2020-10-30-6-tips-for-beginner-lawn-bowlers.md`: Add contextual links to `/bowls-clubs/club-directory/` where club membership and visiting a local club are discussed.
- Remember to update `last_modified_at` on every modified post file and `getting-started.md`.

## Completion criteria
- [ ] `_includes/footer-nav.html` includes a link to `/bowls-clubs/club-directory/`.
- [ ] `getting-started.md` includes a resource link/card pointing to `/bowls-clubs/club-directory/`.
- [ ] Beginner posts (`2019-08-06-barefoot-bowls.md`, `2018-03-01-guide-to-short-mat-bowls.md`, `2020-06-16-how-much-does-lawn-bowls-cost.md`, `2020-10-30-6-tips-for-beginner-lawn-bowlers.md`) link to the directory hub (and relevant city guides), with `last_modified_at` updated.
- [ ] `bundle exec jekyll build` and `python3 tools/audit_links_and_404s.py` pass with zero broken links.

