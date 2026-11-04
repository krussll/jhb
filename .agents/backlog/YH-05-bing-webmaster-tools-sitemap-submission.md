# YH-05: Confirm Bing Webmaster Tools verification and submit the sitemap

- **Source document:** `.agents/yahoo-seo-visibility-plan.md` (Phase 4 item 1)
- **Owner:** 👤 User only
- **Priority:** Medium
- **Status:** Partly done. The `msvalidate.01` verification meta tag is live in `_includes/head.html` (line ~101), from commits "Bing validation" and "Fix bing issues". Sitemap submission can't be verified by the agent.
- **Depends on:** None

> [!IMPORTANT]
> **User-only task: Reece needs to do this.** It needs the Bing Webmaster Tools account.

## Task
Make sure `jackhighbowls.com` (not just the old `krussll.github.io/jhb`) is verified in Bing Webmaster Tools, and that the sitemap has been submitted and processed. Bing's index powers Yahoo's organic results.

## Context
- Sitemap URL: `https://jackhighbowls.com/sitemap.xml` (custom template at the repo root; the `jekyll-sitemap` plugin is disabled in `_config.yml`).
- IndexNow is already wired up: `tools/submit_indexnow.py` with key `35a0d3118063498b9485b529131cacd8`, and `.github/workflows/indexnow.yml` runs on pushes to `main`/`gh-pages`. Check the IndexNow report in Bing Webmaster Tools to confirm submissions are accepted (no 403/422 errors).
- If the old `krussll.github.io/jhb` property still exists, consider setting up a site move or removing it.

## Completion criteria
- [ ] `jackhighbowls.com` shows as verified in Bing Webmaster Tools.
- [ ] `https://jackhighbowls.com/sitemap.xml` is submitted with status "Success" and the discovered URL count is roughly the number of posts and pages.
- [ ] The IndexNow section in Bing Webmaster Tools shows recent successful submissions.
