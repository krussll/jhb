# CD-03: Rebuild the Club Directory Hub page (`2022-06-01-club-directory.md`)

- **Source document:** `.agents/club-directory-seo-plan.md` (§1, §3 & §4 Phase 1 `CD-03`)
- **Owner:** 🤖 Agent (Content Curator)
- **Priority:** High
- **Status:** Not started
- **Depends on:** CD-01
- **Unblocks:** CD-06

## Task
Overhaul `_posts/2022-06-01-club-directory.md` (`/bowls-clubs/club-directory/`) from a sparse placeholder with empty country headings into a comprehensive, high-utility Bowls Club Directory & Beginner's Club Joining Hub.

## Context
- Currently `_posts/2022-06-01-club-directory.md` has `description: ""`, uses unstyled `.wp-block-columns`, links only to Edinburgh and Adelaide, and displays empty `<h2>` headings for *England*, *Wales*, *Ireland*, and *New Zealand*.
- **Preserve the permalink** (`/bowls-clubs/club-directory/`).
- Update front matter:
  - Add a compelling `seo_title` (≤ 65 chars with or without suffix) and `description` (140–160 chars).
  - Add `image: "/img/posts/Club-Directory-1024x576.jpg"`.
  - Add `faqs:` front matter (4–5 common questions: e.g., *"Can I try lawn bowls at a club without buying my own bowls?"*, *"How much does it cost to join a local bowls club?"*, *"What is the difference between flat green, crown green, and indoor bowls clubs?"*, *"What shoes do I need for my first club roll-up?"*).
  - Update `last_modified_at` to the current datetime.
- Replace empty country headings with:
  1. **Featured Regional Club Guides** (styled cards linking to Edinburgh, Adelaide, and future city guides with club counts and surface highlights).
  2. **Official National Governing Body (NGB) Club Finders by Country** (helpful table/cards linking readers in England, Scotland, Wales, Ireland, Australia, New Zealand, USA, and Canada to official Bowls England, BCGBA, EIBA, Bowls Scotland, Bowls Australia, and Bowls NZ finders for regions not yet covered by a dedicated JHB city guide).
  3. **How to Choose & Visit Your First Bowls Club** (practical E-E-A-T guide covering open days/taster sessions, indoor vs. outdoor vs. crown green vs. short mat, borrowing club bowls, typical membership fees, and links to [Lawn Bowls Dress Code](/help/lawn-bowls-dress-code/), [How Much Does Lawn Bowls Cost](/help/how-much-does-lawn-bowls-cost/), [Best Lawn Bowls for Beginners](/guide/best-lawn-bowls-for-beginners/), and [Bowl Size Guide](/help/what-size-lawn-bowl-should-i-use/)).

## Completion criteria
- [ ] No empty country headings or `.wp-block-columns` markup remain in `_posts/2022-06-01-club-directory.md`.
- [ ] Front matter includes `seo_title`, `description`, `image`, `faqs`, and updated `last_modified_at`.
- [ ] Includes Featured Regional Guides, NGB Club Finder directory table, and First-Time Club Visitor checklist with contextual internal links.
- [ ] `bundle exec jekyll build` completes without errors.

