# QA-01: Audit and resolve 404 errors and broken internal links

- **Source document:** Quality Assurance & Site Health Audit
- **Owner:** 🤖 Agent (Quality Assurance Agent)
- **Priority:** High
- **Status:** Not started
- **Depends on:** None

> [!NOTE]
> **Audit Scope & Sources:**
> 1. **Internal Broken Links (Repo & Build):** Audit all internal links (`href="..."`) across `_posts/`, pages, layouts (`_layouts/`), includes (`_includes/`), and YAML data files (`_data/`) against generated URLs in `_site/`.
> 2. **Legacy Permalink & Redirect Errors:** Check for obsolete WordPress permalink structures (e.g. `/:year/:month/:day/:slug/` vs current `/:categories/:title/`) and broken fragment/anchor identifiers.
> 3. **404 Page Experience & Analytics:** Verify `404.html` (layout `_layouts/404.html` and styles `_sass/_404.scss`) provides proper UX, pathways to key hubs, and that 404 hits are tracked as error events in GA4 (`G-ZCQ4MKZD4S`).
> 4. **External/Crawl 404 Logs:** If available from Google Search Console or Bing Webmaster Tools, review reported 404/410 URLs and configure redirects or content aliases.

## Task
Perform a comprehensive audit of 404 errors and broken links across the site, remediate all broken internal links, and ensure the 404 error page and error tracking function properly.

## Context
- **Permalink Schema:** The site uses `permalink: /:categories/:title/` in `_config.yml`. Historical posts or older navigation links have previously suffered from 404s due to category slug mismatches, date-based permalink remnants, or malformed YAML front matter (e.g., closing `---` concatenated directly to timestamps).
- **Recent 404 Incidents:**
  - Pull Request #33 fixed broken core guide URLs on the homepage that used `/YYYY/MM/DD/slug/` instead of `/:category/:slug/`.
  - Commit `408dc3b` fixed two posts (`best-lawn-bowls-for-indoors.md`, `best-lawn-bowls-shoes.md`) where `+0000---` broke YAML parsing and caused Jekyll to skip post permalinks, producing 404s.
- **Link Auditing Tooling:** A Python script in `tools/` (e.g., `tools/audit_links_and_404s.py` or spidering `_site/`) can crawl all built HTML files, extract internal links and anchor tags, and flag any target paths that do not resolve to an existing generated file or directory index.
- **404 Page UX & Telemetry:**
  - `404.html` uses `_layouts/404.html` to present a bowling-themed 404 experience ("Bowl in the Ditch! Page Not Found") with links to `/`, `/getting-started/`, learning pathways from `_data/pathways.yml`, and quick links to Guides, Reviews, AI Coaching, and the Drill Pack.
  - Ensure the 404 page sends a dedicated event to Google Analytics (e.g., `gtag('event', 'page_view_404', { 'page_path': window.location.pathname, 'page_referrer': document.referrer })`) so 404 patterns can be monitored in GA4.
- **Rules:** When modifying any blog post files, update their `last_modified_at` timestamp.

## Completion criteria
- [ ] Automated link audit tool or test script run against the compiled `_site/` build.
- [ ] All broken internal links across posts, layouts, includes, and navigation menus identified and remediated.
- [ ] Front matter across posts checked to ensure no malformed permalinks or YAML syntax bugs cause silent 404s.
- [ ] 404 page (`404.html` & `_layouts/404.html`) verified for responsive layout, accessibility, and GA4 event logging for missing URLs.
- [ ] `last_modified_at` updated on any modified post files.
- [ ] Zero broken internal links reported on final check.
- [ ] `bundle exec jekyll build` succeeds cleanly without errors.

