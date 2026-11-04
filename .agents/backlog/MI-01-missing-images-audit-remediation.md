# MI-01: Audit and remediate site-wide missing images across 25 posts

- **Source document:** `.agents/missing-images.md` ("Site-Wide Missing Images Audit Report")
- **Owner:** 🤝 Shared: agent can fix/remove broken tags, user provides priority images
- **Priority:** High
- **Status:** Not started (25 posts affected, 134 distinct missing image references)
- **Depends on:** User decision on missing image assets

> [!NOTE]
> **User action required:** Many missing images are historical WordPress assets, player headshots, or custom diagrams (e.g. scorecard steps, hand signals) that were never committed to the repo. The user should decide whether to:
> 1. Supply missing image files for high-priority instructional guides (scorecards, hand signals).
> 2. Clean up / remove broken image blocks and broken hex-encoded URLs where assets no longer exist.

## Task
Resolve 134 missing image file references across 25 blog posts identified in the audit report.

## Context
From `.agents/missing-images.md`:
1. **High Priority (Core Instructional Guides):**
   - `_posts/2020-09-30-how-to-fill-in-a-lawn-bowls-scorecard.md` (16 missing image references): Scorecard section crops (`scorecard.png`, `game-details.png`, etc.).
   - `_posts/2020-11-06-lawn-bowls-hand-signals.md` (11 missing images): Key visual gestures (`forehand.png`, `backhand.png`, `bowls-are-touching.png`, etc.).
   - `_posts/2019-04-24-lawn-bowls-rules-and-etiquette.md` (4 missing images): Etiquette illustration diagrams.
2. **Medium Priority (Reviews & Technical Guides):**
   - Corrupted hex-encoded URLs (e.g., `_posts/2021-04-27-best-lawn-bowl-grips.md`, `_posts/2021-04-30-taylor-gtr-lawn-bowl-review.md`, `_posts/2022-02-22-playing-lawn-bowls-in-wet-conditions.md`).
   - Trajectory charts in `_posts/2020-05-20-lawn-bowls-bias-guide-and-trajectory-charts-2020.md`.
3. **Low Priority / Candidates for Removal:**
   - `_posts/2021-02-01-jokes-about-lawn-bowls.md` (8 missing meme images).
   - `_posts/2020-11-02-world-bowls-player-profiles.md` (15 player headshots).

## Completion criteria
- [ ] Broken hex-encoded image references removed or updated with working URLs/images.
- [ ] Core guides (scorecard, hand signals) either supplied with diagrams or converted into accessible HTML tables / diagrams.
- [ ] Zero broken 404 image tags remaining in production builds across the 25 affected posts.
- [ ] `last_modified_at` updated on edited posts.
- [ ] `bundle exec jekyll build` completes cleanly without broken image asset warnings.
