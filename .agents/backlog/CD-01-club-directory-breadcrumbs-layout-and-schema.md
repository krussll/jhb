# CD-01: Configure `_clubs` collection, breadcrumbs, post layout callout, and structured data (`ItemList` & `SportsActivityLocation`)

- **Source document:** [`.agents/club-directory-seo-plan.md`](../club-directory-seo-plan.md) (§2 & §5 Phase 1 `CD-01`)
- **Owner:** 🤖 Agent (Frontend Implementation)
- **Priority:** High
- **Status:** Not started
- **Depends on:** None
- **Unblocks:** CD-02, CD-03, CD-04, CD-05

## Task
Set up the 3-tier directory foundation: configure the `clubs` Jekyll collection (`_config.yml`), create the individual club profile layout (`_layouts/club.html`), update `sitemap.xml`, and upgrade breadcrumb navigation and JSON-LD schema (`ItemList` for city guides and `SportsActivityLocation` for individual club pages).

## Context
1. **Collection Setup (`_config.yml` & `sitemap.xml`)**:
   - Add a `clubs` collection in `_config.yml` with `output: true` and `permalink: /bowls-clubs/:city/:name/` (or explicit frontmatter `permalink: /bowls-clubs/<city>/<slug>/`).
   - Update `sitemap.xml` so `site.clubs` documents (unless `sitemap == false`) are included in the XML sitemap with `<priority>0.7</priority>`.
2. **Breadcrumbs (`_includes/breadcrumbs.html` & `_includes/head.html`)**:
   - Map `cat_slug == 'bowls-clubs'` on city guide posts to parent `"Club Directory"` (`/bowls-clubs/club-directory/`), while keeping `Home` as the parent of `/bowls-clubs/club-directory/` itself.
   - For `_layouts/club.html` (`page.collection == 'clubs'`), output a 4-level breadcrumb trail: `Home` → `Club Directory` (`/bowls-clubs/club-directory/`) → `Bowls Clubs in [City]` (`page.city_url`) → `[Club Name]`.
3. **Post Layout Callout (`_layouts/post.html`)**:
   - Suppress `.review-methodology-callout` when `page.categories contains 'bowls-clubs'`.
4. **Rich Schema (`_includes/head.html`)**:
   - On regional city posts (`page.club_region`), automatically generate an `ItemList` JSON-LD block from `site.data.clubs[page.club_region]` linking to each club's internal profile URL (when `profile_page: true`) or external URL.
   - On individual club profile pages (`page.collection == 'clubs'`), output `SportsActivityLocation` JSON-LD with `name`, `description`, `address` (`PostalAddress`), `url`, `sameAs` (official club website), and surface/facility details.
5. **Club Profile Layout (`_layouts/club.html`)**:
   - Render the 5 high-value modules defined in `.agents/club-directory-seo-plan.md`:
     1. Facility & Surface Fact Box (Address, Postcode, Surfaces, Season, Rinks, Website & Google Maps buttons)
     2. Beginner, Casual & Barefoot Bowls Access checklist
     3. Dynamic "Best Bowls & Shoes for [Club Name]" equipment matchmaker based on `page.surfaces` and `page.country`
     4. "Nearby Bowls Clubs in [Area]" cross-link cards (pulling 3–4 clubs from `site.data.clubs[page.city]`)
     5. Club-specific FAQ accordion (`page.faqs`)

## Completion criteria
- [ ] `_config.yml` defines the `clubs` collection and `sitemap.xml` includes `site.clubs`.
- [ ] `_includes/breadcrumbs.html` and `_includes/head.html` support both 3-level (`bowls-clubs` city pages) and 4-level (`clubs` profile pages) breadcrumbs.
- [ ] `_layouts/post.html` hides `.review-methodology-callout` on `bowls-clubs` pages.
- [ ] `_includes/head.html` outputs valid `ItemList` JSON-LD on city guides and `SportsActivityLocation` JSON-LD on club pages.
- [ ] `_layouts/club.html` renders all 5 rich profile modules cleanly using brand colours.
- [ ] `bundle exec jekyll build` completes without errors.
