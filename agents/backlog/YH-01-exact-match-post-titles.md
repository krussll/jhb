# YH-01: Rewrite post titles as exact-match titles that don't truncate

- **Source document:** `.agents/yahoo-seo-visibility-plan.md` (Phase 3 item 1 "Exact-Match Title & H1 Alignment")
- **Owner:** 🤖 Agent (Content Curator); the user should review the priority list
- **Priority:** Medium
- **Status:** Not started
- **Depends on:** None

## Task
Tighten `title:` front matter on posts, starting with "Best X for Y" and "X vs Y" buyer/comparison pages. Each title should front-load the exact search query and fit within about 65 characters, including the site suffix.

## Context
- `_includes/head.html` renders `<title>` as `{{ page.title }} - Jack High Bowls`. The suffix adds **18 characters**.
- On 2026-11-04, **249 of the 347 posts** have a title longer than 65 characters once the suffix is added.
- Bing and Yahoo weight exact-match keywords in `<title>`, `<h1>`, `<h2>` and URL slugs more heavily than Google does.
- Example from the plan: *"Best Lawn Bowls for Beginners (2026 UK Buyer's Guide)"*.
- **Don't change permalinks or slugs.** That would break inbound links and indexed URLs.
- Options: (a) shorten titles; (b) add an optional `seo_title:` front-matter key used only in `<title>`/`og:title` and keep the longer on-page H1; (c) drop the suffix when the title is already long. Agree on the approach with the user before bulk editing.
- Add year modifiers only where the content really has been refreshed for that year.
- AGENTS.md rule: update `last_modified_at` on every post file changed.

## Completion criteria
- [ ] Approach agreed (shorten vs `seo_title` vs suffix logic).
- [ ] All "best", "vs" and "review" posts have a rendered `<title>` of 65 characters or fewer, starting with the target query.
- [ ] H1s stay consistent with the title intent; no permalinks changed.
- [ ] `last_modified_at` updated on edited posts.
- [ ] `bundle exec jekyll build` completes without errors.
