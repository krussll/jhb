# CC-06: Show breadcrumbs that map posts back to their pathway hub

- **Source document:** `.agents/core-content-promotion-plan.md` (§2.3 "Breadcrumb adjustments")
- **Owner:** 🤖 Agent
- **Priority:** Medium
- **Status:** Not started. `_includes/head.html` outputs `BreadcrumbList` JSON-LD that maps categories to `/reviews`, `/guides` or `/help-and-support` (falling back to `/all-posts`), but no visible breadcrumb exists and nothing maps to the pathways.
- **Depends on:** CC-16 (pathway hub pages) and a post-to-pathway mapping (e.g., `pathway:` front matter or `_data/pathways.yml`)

## Task
Add a visible, accessible breadcrumb trail to posts in the four goal categories, and keep the JSON-LD in step with it.

## Context
- Breadcrumb pattern: `<nav aria-label="Breadcrumb"><ol>…</ol></nav>`, with `aria-current="page"` on the last item.
- Put it in `_layouts/post.html` near the `.post-hero`.
- Mapping: add an optional `pathway:` front-matter key (e.g., `learn-the-essentials`) to core posts. If it's missing, fall back to the existing category logic.
- AGENTS.md rule: update `last_modified_at` on edited posts.

## Completion criteria
- [ ] Core pathway posts show Home › Pathway hub › Post; other posts show Home › Category hub › Post.
- [ ] Visible breadcrumbs and `BreadcrumbList` JSON-LD match on sampled pages, and the schema validates.
- [ ] Accessible markup (labelled nav, ordered list, `aria-current`).
- [ ] `bundle exec jekyll build` completes without errors.
