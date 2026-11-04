# CC-11: Add a sticky sidebar widget to long-form guides

- **Source document:** `.agents/core-content-promotion-plan.md` (§4.1 "Contextual sidebars")
- **Owner:** 🤖 Agent
- **Priority:** Low–Medium
- **Status:** Not started. `_layouts/post.html` is a single centred column with no sidebar.
- **Depends on:** A post-to-pathway mapping (see CC-06 / CC-02 `_data/pathways.yml`)

## Task
On long-form guides, show a sticky sidebar (desktop) linking to the related pathway's pillar content. On smaller screens, show it as an inline block.

## Context
- Only enable it for long posts: an opt-in front-matter flag (`sidebar: true`), or a word-count threshold calculated as in `_includes/read_time.html`.
- Desktop: `position: sticky` in a `col-lg-3` next to a `col-lg-8` article. Don't hurt reading width. Mobile: show it after the intro or at the end, never as an overlay.
- Content: pathway name, three to five pillar links, and an optional drill pack mini-CTA.
- Must not cause CLS or overlap the fixed navbar (`#mainNav`).

## Completion criteria
- [ ] Sidebar appears on eligible long-form guides, sticky on desktop and inline on mobile.
- [ ] Links point to the right pathway's pillar posts.
- [ ] Lighthouse accessibility and performance ≥ 90 on a sample guide.
- [ ] `bundle exec jekyll build` completes without errors.
