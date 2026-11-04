# YH-02: Strip leftover WordPress HTML from `_posts/`

- **Source document:** `.agents/yahoo-seo-visibility-plan.md` (§2 issue #6; Phase 3 item 2; §4 files table)
- **Owner:** 🤖 Agent
- **Priority:** Medium
- **Status:** Not started
- **Depends on:** None. Coordinate with the MI-* missing-image tasks, which edit some of the same files.

## Task
Remove Gutenberg block comments and invalid `xmlns` attributes from the post sources, so crawlers parse clean HTML5 with a better signal-to-noise ratio.

## Context
Counts on 2026-11-04:
- `<!-- wp:... -->` comments: **11,897 occurrences across 344 of 347 posts** (including closing `<!-- /wp:... -->` comments).
- `<p xmlns="http://www.w3.org/1999/xhtml">`: **340 posts**.

Suggested approach: a one-off script under `tools/`, e.g. `tools/clean_wp_markup.py`.
- Remove `<!-- wp:* -->` and `<!-- /wp:* -->` comments (they can include JSON attributes and span the whole tag).
- Remove only the `xmlns="http://www.w3.org/1999/xhtml"` attribute.
- Collapse the blank lines left behind.
- Leave classes like `wp-block-image` alone, unless their CSS is confirmed unused (search `_sass/` first).
- **Don't touch YAML front matter or Liquid tags.**

Diff a sample of the built HTML before and after, to confirm nothing changes visually. The AGENTS.md `last_modified_at` rule technically applies to every edited post. **Ask the user** whether a markup-only cleanup should bump `last_modified_at`, since that changes the visible "Last updated" date and the `dateModified` schema on every post.

## Completion criteria
- [ ] `grep -c "<!-- wp:" _posts/*` and `grep -l 'xmlns="http://www.w3.org/1999/xhtml"' _posts/*` both return zero.
- [ ] Spot-checked posts (including a review, a guide and a post with figures) render the same as before.
- [ ] `last_modified_at` handled as the user decides.
- [ ] `bundle exec jekyll build` completes without errors.
