# CD-01: Fix breadcrumbs, post layout callout, and ItemList schema for `bowls-clubs`

- **Source document:** `.agents/club-directory-seo-plan.md` (§2.3 "Template, Breadcrumb & Schema Fixes" & §4 Phase 1 `CD-01`)
- **Owner:** 🤖 Agent (Frontend Implementation)
- **Priority:** High
- **Status:** Not started
- **Depends on:** None
- **Unblocks:** CD-03, CD-04, CD-05

## Task
Update the breadcrumb navigation, `BreadcrumbList` JSON-LD schema, post hero layout callout, and `ItemList` structured data support for pages in the `bowls-clubs` category.

## Context
- Currently in `_includes/breadcrumbs.html` and `_includes/head.html`, `cat_slug == 'bowls-clubs'` is not mapped to a parent hub, so breadcrumbs on regional directory pages (`/bowls-clubs/bowls-clubs-in-edinburgh/`, `/bowls-clubs/bowls-clubs-in-adelaide-south-australia/`) fall back to `/all-posts/` ("Bowls clubs") instead of `/bowls-clubs/club-directory/` ("Club Directory").
- When viewing `/bowls-clubs/club-directory/` itself, the parent breadcrumb should remain `Home` (avoiding a self-referential breadcrumb item).
- In `_layouts/post.html` (lines 20–22), every post displays `.review-methodology-callout` (*"How we test: Every article follows our review methodology..."*), which is out of place on location directory pages. Suppress this callout when `page.categories contains 'bowls-clubs'`.
- In `_includes/head.html` (§5 "ItemList Schema"), extend the `ItemList` condition so that if a post has `page.club_region` matching `site.data.clubs[page.club_region]`, it automatically generates an `ItemList` JSON-LD block listing the clubs on that page (`name`, `description` / `address`, and `url` / `website`).

## Completion criteria
- [ ] `_includes/breadcrumbs.html` and `_includes/head.html` route `bowls-clubs` child pages to `/bowls-clubs/club-directory/` ("Club Directory") without creating a self-loop on `/bowls-clubs/club-directory/`.
- [ ] `_layouts/post.html` hides `.review-methodology-callout` when `page.categories contains 'bowls-clubs'`.
- [ ] `_includes/head.html` outputs valid `ItemList` JSON-LD when `page.club_region` is set and `site.data.clubs[page.club_region]` exists.
- [ ] `bundle exec jekyll build` completes without errors.

