# CC-08: Build reusable action cards for core articles

- **Source document:** `.agents/core-content-promotion-plan.md` (§3.2 "Action cards")
- **Owner:** 🤖 Agent
- **Priority:** Medium
- **Status:** Not started. Getting Started uses `.gs-resource` articles with a title and description, but no reading time, skill level or next step.
- **Depends on:** Skill-level and next-step data for the core posts (front matter)

## Task
Create a reusable Liquid include, e.g. `_includes/action-card.html`, that renders a core article card with **estimated reading time**, **skill level** and the **next recommended step**. Use it on Getting Started and elsewhere.

## Context
- Reading time: reuse `_includes/read_time.html` (200 words per minute), passing the target post's content.
- Add front-matter keys to core posts, e.g. `skill_level: Beginner|Intermediate|Advanced` and `next_step: /path/to/next-post/`. Keep key order tidy (AGENTS.md) and update `last_modified_at` on edited posts.
- The include takes a post URL or slug, looks the post up in `site.posts`, and renders the card.
- Can be used by CC-07 (tabs), CC-12 (end-of-post CTA) and CC-16 (cluster pages).

## Completion criteria
- [ ] `_includes/action-card.html` exists and renders title, excerpt, reading time, skill level and next-step link.
- [ ] Getting Started uses action cards for its core articles.
- [ ] Core posts have `skill_level` and `next_step` front matter.
- [ ] `bundle exec jekyll build` completes without errors.
