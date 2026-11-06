# MI-01: Audit and remediate site-wide missing images across 25 posts

- **Source document:** `.agents/missing-images.md` ("Site-Wide Missing Images Audit Report")
- **Owner:** 🤝 Shared: agent can fix/remove broken tags, user provides priority images
- **Priority:** High
- **Status:** Not started (24 posts active, 1 resolved; 130 current missing image references)
- **Depends on:** User decision on missing image assets

> [!NOTE]
> **User action required:** Many missing images are historical WordPress assets, player headshots, or custom diagrams (e.g. scorecard steps, hand signals) that were never committed to the repo. The user should decide whether to:
> 1. Supply missing image files for high-priority instructional guides (scorecards, hand signals).
> 2. Clean up / remove broken image blocks and broken hex-encoded URLs where assets no longer exist.

## Task
Resolve 130 missing image file references across the 24 remaining affected blog posts identified in the audit report (1 of the original 25 posts is already fully resolved).

## Table of URLs with Missing Images

| # | Page Title | Published URL | Source Post File | Missing Images | Priority / Category |
| :--- | :--- | :--- | :--- | :---: | :--- |
| 1 | How To Fill In A Lawn Bowls Scorecard | [https://jackhighbowls.com/help/how-to-fill-in-a-lawn-bowls-scorecard/](https://jackhighbowls.com/help/how-to-fill-in-a-lawn-bowls-scorecard/) | [`_posts/2020-09-30-how-to-fill-in-a-lawn-bowls-scorecard.md`](file:///home/reecewilliams8/dev%20work/jhb/_posts/2020-09-30-how-to-fill-in-a-lawn-bowls-scorecard.md) | **16** | 🔴 High (scorecard step crops) |
| 2 | Best Lawn and Indoor Bowlers In The World | [https://jackhighbowls.com/help/world-bowls-player-profiles/](https://jackhighbowls.com/help/world-bowls-player-profiles/) | [`_posts/2020-11-02-world-bowls-player-profiles.md`](file:///home/reecewilliams8/dev%20work/jhb/_posts/2020-11-02-world-bowls-player-profiles.md) | **15** | 🟢 Low (player portrait headshots) |
| 3 | Lawn Bowls Hand Signals | [https://jackhighbowls.com/help/lawn-bowls-hand-signals/](https://jackhighbowls.com/help/lawn-bowls-hand-signals/) | [`_posts/2020-11-06-lawn-bowls-hand-signals.md`](file:///home/reecewilliams8/dev%20work/jhb/_posts/2020-11-06-lawn-bowls-hand-signals.md) | **11** | 🔴 High (gestures & signaling diagrams) |
| 4 | The History Of Lawn Bowls | [https://jackhighbowls.com/help/history-of-lawn-bowls/](https://jackhighbowls.com/help/history-of-lawn-bowls/) | [`_posts/2020-10-23-history-of-lawn-bowls.md`](file:///home/reecewilliams8/dev%20work/jhb/_posts/2020-10-23-history-of-lawn-bowls.md) | **10** | 🟡 Medium (historical portraits & paintings) |
| 5 | Aero GrooVe Lawn Bowls Review | [https://jackhighbowls.com/review/bowls/aero-groove-lawn-bowls-review/](https://jackhighbowls.com/review/bowls/aero-groove-lawn-bowls-review/) | [`_posts/2020-09-12-aero-groove-lawn-bowls-review.md`](file:///home/reecewilliams8/dev%20work/jhb/_posts/2020-09-12-aero-groove-lawn-bowls-review.md) | **8** | 🟡 Medium (bowl photos & grip details) |
| 6 | Jokes About Lawn Bowls | [https://jackhighbowls.com/help/jokes-about-lawn-bowls/](https://jackhighbowls.com/help/jokes-about-lawn-bowls/) | [`_posts/2021-02-01-jokes-about-lawn-bowls.md`](file:///home/reecewilliams8/dev%20work/jhb/_posts/2021-02-01-jokes-about-lawn-bowls.md) | **8** | 🟢 Low (humour meme illustrations) |
| 7 | Best Lawn Bowls Shoes | [https://jackhighbowls.com/guide/best-lawn-bowls-shoes/](https://jackhighbowls.com/guide/best-lawn-bowls-shoes/) | [`_posts/2020-09-17-best-lawn-bowls-shoes.md`](file:///home/reecewilliams8/dev%20work/jhb/_posts/2020-09-17-best-lawn-bowls-shoes.md) | **6** | 🟡 Medium (shoe model photos) |
| 8 | Used Aero Bowls For Sale | [https://jackhighbowls.com/guide/used-aero-bowls-for-sale/](https://jackhighbowls.com/guide/used-aero-bowls-for-sale/) | [`_posts/2019-05-20-used-aero-bowls-for-sale.md`](file:///home/reecewilliams8/dev%20work/jhb/_posts/2019-05-20-used-aero-bowls-for-sale.md) | **6** | 🟡 Medium (Aero model photos) |
| 9 | What The Stamp Means On Lawn Bowls | [https://jackhighbowls.com/help/what-the-stamp-means-on-lawn-bowls/](https://jackhighbowls.com/help/what-the-stamp-means-on-lawn-bowls/) | [`_posts/2020-09-30-what-the-stamp-means-on-lawn-bowls.md`](file:///home/reecewilliams8/dev%20work/jhb/_posts/2020-09-30-what-the-stamp-means-on-lawn-bowls.md) | **6** | 🔴 High (WB stamp section diagrams) |
| 10 | Aero Quantum Lawn Bowls Review | [https://jackhighbowls.com/review/bowls/aero-quantum-review/](https://jackhighbowls.com/review/bowls/aero-quantum-review/) | [`_posts/2021-05-18-aero-quantum-review.md`](file:///home/reecewilliams8/dev%20work/jhb/_posts/2021-05-18-aero-quantum-review.md) | **5** | 🟡 Medium (review photos; trajectory fixed) |
| 11 | Lawn Bowls Rules And Etiquette | [https://jackhighbowls.com/help/lawn-bowls-rules-and-etiquette/](https://jackhighbowls.com/help/lawn-bowls-rules-and-etiquette/) | [`_posts/2019-04-24-lawn-bowls-rules-and-etiquette.md`](file:///home/reecewilliams8/dev%20work/jhb/_posts/2019-04-24-lawn-bowls-rules-and-etiquette.md) | **4** | 🔴 High (etiquette illustration diagrams) |
| 12 | Best Lawn Bowls Grip Enhancers | [https://jackhighbowls.com/guide/best-lawn-bowls-grip-enhancers/](https://jackhighbowls.com/guide/best-lawn-bowls-grip-enhancers/) | [`_posts/2020-07-01-best-lawn-bowls-grip-enhancers.md`](file:///home/reecewilliams8/dev%20work/jhb/_posts/2020-07-01-best-lawn-bowls-grip-enhancers.md) | **4** | 🟡 Medium (wax/grip product images) |
| 13 | Best Junior Lawn Bowls | [https://jackhighbowls.com/guide/best-junior-lawn-bowls/](https://jackhighbowls.com/guide/best-junior-lawn-bowls/) | [`_posts/2020-10-01-best-junior-lawn-bowls.md`](file:///home/reecewilliams8/dev%20work/jhb/_posts/2020-10-01-best-junior-lawn-bowls.md) | **4** | 🟡 Medium (junior bowl model images) |
| 14 | Best Yellow Lawn Bowls | [https://jackhighbowls.com/guide/best-yellow-lawn-bowls/](https://jackhighbowls.com/guide/best-yellow-lawn-bowls/) | [`_posts/2022-04-06-best-yellow-lawn-bowls.md`](file:///home/reecewilliams8/dev%20work/jhb/_posts/2022-04-06-best-yellow-lawn-bowls.md) | **4** | 🟡 Medium (yellow bowl product images) |
| 15 | Lawn Bowls vs Bocce (9 Similarities and Differences) | [https://jackhighbowls.com/help/lawn-bowls-vs-bocce/](https://jackhighbowls.com/help/lawn-bowls-vs-bocce/) | [`_posts/2019-02-19-lawn-bowls-vs-bocce.md`](file:///home/reecewilliams8/dev%20work/jhb/_posts/2019-02-19-lawn-bowls-vs-bocce.md) | **3** | 🟡 Medium (sport comparison diagrams) |
| 16 | Lawn Bowls Reading The Head For Beginners | [https://jackhighbowls.com/help/lawn-bowls-how-to-read-the-head/](https://jackhighbowls.com/help/lawn-bowls-how-to-read-the-head/) | [`_posts/2019-09-30-lawn-bowls-how-to-read-the-head.md`](file:///home/reecewilliams8/dev%20work/jhb/_posts/2019-09-30-lawn-bowls-how-to-read-the-head.md) | **3** | 🔴 High (head scenario photos) |
| 17 | Taylor Blaze Lawn Bowls Review | [https://jackhighbowls.com/review/bowls/taylor-blaze-lawn-bowls-review/](https://jackhighbowls.com/review/bowls/taylor-blaze-lawn-bowls-review/) | [`_posts/2020-09-01-taylor-blaze-lawn-bowls-review.md`](file:///home/reecewilliams8/dev%20work/jhb/_posts/2020-09-01-taylor-blaze-lawn-bowls-review.md) | **3** | 🟡 Medium (grip option diagrams) |
| 18 | 7 Best Straight Lawn Bowls | [https://jackhighbowls.com/guide/best-straight-lawn-bowls/](https://jackhighbowls.com/guide/best-straight-lawn-bowls/) | [`_posts/2020-10-29-best-straight-lawn-bowls.md`](file:///home/reecewilliams8/dev%20work/jhb/_posts/2020-10-29-best-straight-lawn-bowls.md) | **3** | 🟡 Medium (bowl display photos) |
| 19 | The Best Lawn Bowl Grips | [https://jackhighbowls.com/guide/best-lawn-bowl-grips/](https://jackhighbowls.com/guide/best-lawn-bowl-grips/) | [`_posts/2021-04-27-best-lawn-bowl-grips.md`](file:///home/reecewilliams8/dev%20work/jhb/_posts/2021-04-27-best-lawn-bowl-grips.md) | **3** | 🟡 Medium (corrupted hex camo URLs) |
| 20 | Taylor International Lawn Bowls Review | [https://jackhighbowls.com/review/bowls/taylor-international-lawn-bowls-review/](https://jackhighbowls.com/review/bowls/taylor-international-lawn-bowls-review/) | [`_posts/2021-04-27-taylor-international-lawn-bowls-review.md`](file:///home/reecewilliams8/dev%20work/jhb/_posts/2021-04-27-taylor-international-lawn-bowls-review.md) | **3** | 🟡 Medium (bowl review photos) |
| 21 | Best Crown Green Bowls for Beginners | [https://jackhighbowls.com/crown-green-bowls/best-crown-green-bowls-for-beginners-a-complete-buyers-guide/](https://jackhighbowls.com/crown-green-bowls/best-crown-green-bowls-for-beginners-a-complete-buyers-guide/) | [`_posts/2022-06-07-best-crown-green-bowls-for-beginners-a-complete-buyers-guide.md`](file:///home/reecewilliams8/dev%20work/jhb/_posts/2022-06-07-best-crown-green-bowls-for-beginners-a-complete-buyers-guide.md) | **2** | 🟡 Medium (corrupted hex camo URLs) |
| 22 | Taylor GTR Lawn Bowls Review | [https://jackhighbowls.com/review/bowls/taylor-gtr-lawn-bowl-review/](https://jackhighbowls.com/review/bowls/taylor-gtr-lawn-bowl-review/) | [`_posts/2021-04-30-taylor-gtr-lawn-bowl-review.md`](file:///home/reecewilliams8/dev%20work/jhb/_posts/2021-04-30-taylor-gtr-lawn-bowl-review.md) | **1** | 🟡 Medium (corrupted hex camo URL) |
| 23 | Is Lawn Bowls Is A Dying Sport? | [https://jackhighbowls.com/help/is-lawn-bowls-a-dying-sport/](https://jackhighbowls.com/help/is-lawn-bowls-a-dying-sport/) | [`_posts/2021-01-28-is-lawn-bowls-a-dying-sport.md`](file:///home/reecewilliams8/dev%20work/jhb/_posts/2021-01-28-is-lawn-bowls-a-dying-sport.md) | **1** | 🟢 Low (club header photo) |
| 24 | Playing Lawn Bowls In Wet Conditions | [https://jackhighbowls.com/help/playing-lawn-bowls-in-wet-conditions/](https://jackhighbowls.com/help/playing-lawn-bowls-in-wet-conditions/) | [`_posts/2022-02-22-playing-lawn-bowls-in-wet-conditions.md`](file:///home/reecewilliams8/dev%20work/jhb/_posts/2022-02-22-playing-lawn-bowls-in-wet-conditions.md) | **1** | 🟡 Medium (corrupted hex camo URL) |
| 25 | Lawn Bowls Bias Guide And Trajectory Charts | [https://jackhighbowls.com/guide/lawn-bowls-bias-guide-and-trajectory-charts-2020/](https://jackhighbowls.com/guide/lawn-bowls-bias-guide-and-trajectory-charts-2020/) | [`_posts/2020-05-20-lawn-bowls-bias-guide-and-trajectory-charts-2020.md`](file:///home/reecewilliams8/dev%20work/jhb/_posts/2020-05-20-lawn-bowls-bias-guide-and-trajectory-charts-2020.md) | **0** | 🟢 **Resolved ✅** (all assets supplied & linked) |
| **Total** | **25 Posts (24 Active, 1 Resolved)** | | | **130** | |

## Context
From `.agents/missing-images.md`:
1. **High Priority (Core Instructional Guides - 40 images total):**
   - `_posts/2020-09-30-how-to-fill-in-a-lawn-bowls-scorecard.md` (16 missing image references): Scorecard section crops (`scorecard.png`, `game-details.png`, etc.).
   - `_posts/2020-11-06-lawn-bowls-hand-signals.md` (11 missing images): Key visual gestures (`forehand.png`, `backhand.png`, `bowls-are-touching.png`, etc.).
   - `_posts/2020-09-30-what-the-stamp-means-on-lawn-bowls.md` (6 missing images): World Bowls stamp element diagrams (`new-stamp.png`, `old-stamp.png`, etc.).
   - `_posts/2019-04-24-lawn-bowls-rules-and-etiquette.md` (4 missing images): Etiquette illustration diagrams.
   - `_posts/2019-09-30-lawn-bowls-how-to-read-the-head.md` (3 missing images): Tactical head scenario diagrams (`holding`, `down`, `balanced`).
2. **Medium Priority (Reviews & Technical Guides - 66 images total):**
   - Corrupted hex-encoded URLs (7 images across 4 posts: `best-lawn-bowl-grips.md`, `taylor-gtr-lawn-bowl-review.md`, `playing-lawn-bowls-in-wet-conditions.md`, `best-crown-green-bowls-for-beginners-a-complete-buyers-guide.md`).
   - Bowl model & review photos (e.g. Aero GrooVe, Aero Quantum, Taylor Blaze, Taylor International, Used Aero, Straight Bowls, Yellow Bowls, Shoes, Grip Enhancers, Junior Bowls, Bocce comparison).
3. **Low Priority / Candidates for Removal (24 images total):**
   - `_posts/2021-02-01-jokes-about-lawn-bowls.md` (8 missing meme images).
   - `_posts/2020-11-02-world-bowls-player-profiles.md` (15 player headshots).
   - `_posts/2021-01-28-is-lawn-bowls-a-dying-sport.md` (1 club header photo).
4. **Resolved Posts (1 post):**
   - `_posts/2020-05-20-lawn-bowls-bias-guide-and-trajectory-charts-2020.md` (0 missing; charts optimized and committed).

## Completion criteria
- [ ] Broken hex-encoded image references removed or updated with working URLs/images.
- [ ] Core guides (scorecard, hand signals) either supplied with diagrams or converted into accessible HTML tables / diagrams.
- [ ] Zero broken 404 image tags remaining in production builds across the 24 active affected posts.
- [ ] `last_modified_at` updated on edited posts.
- [ ] `bundle exec jekyll build` completes cleanly without broken image asset warnings.
