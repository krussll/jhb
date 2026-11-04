# CC-13: Add inline callouts promoting the drill pack and buying guide

- **Source document:** `.agents/core-content-promotion-plan.md` (§4.3 "Inline callouts")
- **Owner:** 🤖 Agent (Content Curator)
- **Priority:** Medium
- **Status:** Not started. Only **3 posts** link to the drill pack in their body; the rest rely on the generic footer banner.
- **Depends on:** None (better after DP-01 so callout copy and price are final)

## Task
Create a reusable callout include, and place it in context: the drill pack inside practice-focused articles, and the buying guide inside gear and review content.

## Context
- Create `_includes/callout.html` with parameters such as `type` (drill-pack | buying-guide), `title`, `text`, `url`, styled with the brand palette. Use `<aside>` with an accessible label.
- Practice-focused posts: search `_posts/` for drill, practice, roll-up, weight control, draw shot (e.g., `2019-04-05-ultimate-guide-to-weight-control.md`, `2022-06-29-how-do-i-stop-my-lawn-bowl-from-dumping.md`).
- Gear posts: categories `review`/`guide` about bowls, shoes and accessories. Link to `/guide/how-to-choose-a-set-of-lawn-bowls/`.
- Put the callout after a relevant paragraph, not at the very top. One per post.
- AGENTS.md rule: update `last_modified_at` on every edited post.

## Completion criteria
- [ ] `_includes/callout.html` exists and is styled.
- [ ] At least 15 practice posts have a contextual drill pack callout, and at least 15 gear posts have a buying-guide callout.
- [ ] `last_modified_at` updated on edited posts.
- [ ] `bundle exec jekyll build` completes without errors.
