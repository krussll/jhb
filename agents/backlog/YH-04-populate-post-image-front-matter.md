# YH-04: Add `image:` front matter to posts (optional permanent cleanup)

- **Source document:** `.agents/yahoo-seo-visibility-plan.md` (Phase 2 item 1, "we can also run a quick Python script to populate `image:`"; §4 table, `_posts/*.md` row)
- **Owner:** 🤖 Agent
- **Priority:** Low (the runtime fallback already works)
- **Status:** Not started. The runtime first-`<img>` extraction in `_includes/head.html` (lines ~49–75) **is done**. Only 2 of 347 posts have `image:` or `background:` front matter.
- **Depends on:** Best done after the MI-* missing-image tasks, so no post points at a missing image.

## Task
Write an explicit `image:` key into each post's front matter, using the first valid local image in the post body.

## Context
- `head.html` currently uses `page.background`, then `page.image`, then `page.header_image`, then the first `<img src>` in the content, then `/img/posts/jack-high-bowls-success.png`. Explicit front matter is more predictable, and lets other templates (cards, feeds, `llms.txt`) use the image.
- Many image `src` values are Liquid expressions, e.g. `{{ '/img/posts/x.png' | prepend: site.baseurl | replace: '//', '/' }}`. Extract the literal `/img/...` path.
- **Skip images that don't exist on disk.** About 135 references are missing; see the MI-* tasks.
- Keep YAML key order tidy (AGENTS.md: `layout`, `title`, `description`, `date`, …). Ask the user whether bumping `last_modified_at` is wanted for a metadata-only change.

## Completion criteria
- [ ] Every post with at least one valid local image has an `image:` key pointing to an existing file.
- [ ] Built `og:image` values are unchanged or improved (spot-check 10 posts).
- [ ] `bundle exec jekyll build` completes without errors.
