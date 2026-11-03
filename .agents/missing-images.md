# Site-Wide Missing Images Audit Report

This document provides an inventory of all images across the Jack High Bowls website that are referenced in published pages and posts but are currently missing from the repository (`img/` and `_site/`).

## Summary Statistics

- **Total Affected Pages:** 25
- **Total Missing Image References:** 132
- **Distinct Missing Image Files:** 131
- **Audit Date:** 30 October 2026

## Overview of Issues

1. **WordPress Import Placeholders:** When content was migrated from WordPress, Markdown posts retained WordPress block markup (`<!-- wp:image -->`) pointing to `/img/posts/<filename>`. While the post markdown was imported, the image assets themselves were never committed to the repository.
2. **Hex-Encoded Camo URLs:** Several posts (such as `best-lawn-bowl-grips` and `playing-lawn-bowls-in-wet-conditions`) contain corrupted image paths where external image URLs were converted into hex strings (e.g., `68747470733a2f2f...`), leading to broken `/img/posts/6874...` references.
3. **Scorecard & Hand Signals Diagrams:** High-value instructional guides (e.g., `how-to-fill-in-a-lawn-bowls-scorecard` and `lawn-bowls-hand-signals`) have multiple sequential missing step-by-step diagram assets.

## Breakdown by Page

### 1. How To Fill In A Lawn Bowls Scorecard | A Helpful Illustrated Guide
- **Published URL:** [https://krussll.github.io/jhb/help/how-to-fill-in-a-lawn-bowls-scorecard](https://krussll.github.io/jhb/help/how-to-fill-in-a-lawn-bowls-scorecard)
- **Local Dev URL:** [http://127.0.0.1:4000/jhb/help/how-to-fill-in-a-lawn-bowls-scorecard](http://127.0.0.1:4000/jhb/help/how-to-fill-in-a-lawn-bowls-scorecard)
- **Source File:** [`_posts/2020-09-30-how-to-fill-in-a-lawn-bowls-scorecard.md`](file:///home/reecewilliams8/dev work/jhb/_posts/2020-09-30-how-to-fill-in-a-lawn-bowls-scorecard.md)
- **Missing Images Count:** 16

| # | Image Filename | Referenced Path | Source Line |
| :--- | :--- | :--- | :--- |
| 1 | `scorecard.png` | `/img/posts/scorecard.png` | Line 26 |
| 2 | `game-details.png` | `/img/posts/game-details.png` | Line 42 |
| 3 | `team-details.png` | `/img/posts/team-details.png` | Line 54 |
| 4 | `shots-details.png` | `/img/posts/shots-details.png` | Line 66 |
| 5 | `result-details.png` | `/img/posts/result-details.png` | Line 82 |
| 6 | `game-details-completed.png` | `/img/posts/game-details-completed.png` | Line 112 |
| 7 | `team-details-completed.png` | `/img/posts/team-details-completed.png` | Line 116 |
| 8 | `scores-details-end1.png` | `/img/posts/scores-details-end1.png` | Line 128 |
| 9 | `scores-details-end2.png` | `/img/posts/scores-details-end2.png` | Line 144 |
| 10 | `scores-details-end3.png` | `/img/posts/scores-details-end3.png` | Line 160 |
| 11 | `scores-details-end4.png` | `/img/posts/scores-details-end4.png` | Line 176 |
| 12 | `scores-details-end5.png` | `/img/posts/scores-details-end5.png` | Line 192 |
| 13 | `scores-details-end6.png` | `/img/posts/scores-details-end6.png` | Line 208 |
| 14 | `scores-details-end7.png` | `/img/posts/scores-details-end7.png` | Line 224 |
| 15 | `result-details-completed.png` | `/img/posts/result-details-completed.png` | Line 240 |
| 16 | `scorecard-completed.png` | `/img/posts/scorecard-completed.png` | Line 252 |


### 2. Best Lawn and Indoor Bowlers In The World | A Helpful Guide
- **Published URL:** [https://krussll.github.io/jhb/help/world-bowls-player-profiles](https://krussll.github.io/jhb/help/world-bowls-player-profiles)
- **Local Dev URL:** [http://127.0.0.1:4000/jhb/help/world-bowls-player-profiles](http://127.0.0.1:4000/jhb/help/world-bowls-player-profiles)
- **Source File:** [`_posts/2020-11-02-world-bowls-player-profiles.md`](file:///home/reecewilliams8/dev work/jhb/_posts/2020-11-02-world-bowls-player-profiles.md)
- **Missing Images Count:** 15

| # | Image Filename | Referenced Path | Source Line |
| :--- | :--- | :--- | :--- |
| 1 | `stewart-anderson.jpg` | `/img/posts/stewart-anderson.jpg` | Line 29 |
| 2 | `nicky-brett.jpg` | `/img/posts/nicky-brett.jpg` | Line 85 |
| 3 | `mark-dawes.jpg` | `/img/posts/mark-dawes.jpg` | Line 153 |
| 4 | `julie-forrest.jpg` | `/img/posts/julie-forrest.jpg` | Line 205 |
| 5 | `paul-foster.jpg` | `/img/posts/paul-foster.jpg` | Line 257 |
| 6 | `les-gillett.jpg` | `/img/posts/les-gillett.jpg` | Line 377 |
| 7 | `greg-harlow.jpg` | `/img/posts/greg-harlow.jpg` | Line 429 |
| 8 | `mervyn-king.jpg` | `/img/posts/mervyn-king.jpg` | Line 489 |
| 9 | `barrie-lester.jpg` | `/img/posts/barrie-lester.jpg` | Line 549 |
| 10 | `alex-marshall.jpg` | `/img/posts/alex-marshall.jpg` | Line 589 |
| 11 | `karen-murphy.jpg` | `/img/posts/karen-murphy.jpg` | Line 741 |
| 12 | `robert-paxton.jpg` | `/img/posts/robert-paxton.jpg` | Line 817 |
| 13 | `katherine-rednall.jpg` | `/img/posts/katherine-rednall.jpg` | Line 885 |
| 14 | `aron-sherriff.jpg` | `/img/posts/aron-sherriff.jpg` | Line 945 |
| 15 | `brett-wilkie.jpg` | `/img/posts/brett-wilkie.jpg` | Line 1001 |


### 3. Lawn Bowls Hand Signals | A Helpful Illustrated Guide
- **Published URL:** [https://krussll.github.io/jhb/help/lawn-bowls-hand-signals](https://krussll.github.io/jhb/help/lawn-bowls-hand-signals)
- **Local Dev URL:** [http://127.0.0.1:4000/jhb/help/lawn-bowls-hand-signals](http://127.0.0.1:4000/jhb/help/lawn-bowls-hand-signals)
- **Source File:** [`_posts/2020-11-06-lawn-bowls-hand-signals.md`](file:///home/reecewilliams8/dev work/jhb/_posts/2020-11-06-lawn-bowls-hand-signals.md)
- **Missing Images Count:** 11

| # | Image Filename | Referenced Path | Source Line |
| :--- | :--- | :--- | :--- |
| 1 | `forehand.png` | `/img/posts/forehand.png` | Line 90 |
| 2 | `backhand.png` | `/img/posts/backhand.png` | Line 110 |
| 3 | `bowl-to-a-spot.png` | `/img/posts/bowl-to-a-spot.png` | Line 130 |
| 4 | `our-bowl.png` | `/img/posts/our-bowl.png` | Line 154 |
| 5 | `their-bowl.png` | `/img/posts/their-bowl.png` | Line 174 |
| 6 | `bowls-are-touching.png` | `/img/posts/bowls-are-touching.png` | Line 194 |
| 7 | `where-is-the-jack.png` | `/img/posts/where-is-the-jack.png` | Line 214 |
| 8 | `distance-to-jack.png` | `/img/posts/distance-to-jack.png` | Line 234 |
| 9 | `shots-for-us.png` | `/img/posts/shots-for-us.png` | Line 278 |
| 10 | `shots-against-us.png` | `/img/posts/shots-against-us.png` | Line 298 |
| 11 | `measure-for-shot.png` | `/img/posts/measure-for-shot.png` | Line 318 |


### 4. The History Of Lawn Bowls | A Helpful Guide
- **Published URL:** [https://krussll.github.io/jhb/help/history-of-lawn-bowls](https://krussll.github.io/jhb/help/history-of-lawn-bowls)
- **Local Dev URL:** [http://127.0.0.1:4000/jhb/help/history-of-lawn-bowls](http://127.0.0.1:4000/jhb/help/history-of-lawn-bowls)
- **Source File:** [`_posts/2020-10-23-history-of-lawn-bowls.md`](file:///home/reecewilliams8/dev work/jhb/_posts/2020-10-23-history-of-lawn-bowls.md)
- **Missing Images Count:** 10

| # | Image Filename | Referenced Path | Source Line |
| :--- | :--- | :--- | :--- |
| 1 | `bocce-ancient-rome.jpg` | `/img/posts/bocce-ancient-rome.jpg` | Line 38 |
| 2 | `edward-iii.png` | `/img/posts/edward-iii.png` | Line 54 |
| 3 | `henry-VIII.png` | `/img/posts/henry-VIII.png` | Line 66 |
| 4 | `queen-mary.png` | `/img/posts/queen-mary.png` | Line 74 |
| 5 | `shakespeare.png` | `/img/posts/shakespeare.png` | Line 86 |
| 6 | `francis-drake-lawn-bowls.png` | `/img/posts/francis-drake-lawn-bowls.png` | Line 102 |
| 7 | `sandy-bay-tasmania.png` | `/img/posts/sandy-bay-tasmania.png` | Line 114 |
| 8 | `usa-lawn-bowls.png` | `/img/posts/usa-lawn-bowls.png` | Line 122 |
| 9 | `edwin-beard-budding.png` | `/img/posts/edwin-beard-budding.png` | Line 142 |
| 10 | `royal-victorian-bowling-association.png` | `/img/posts/royal-victorian-bowling-association.png` | Line 178 |


### 5. Aero GrooVe Lawn Bowls Review
- **Published URL:** [https://krussll.github.io/jhb/bowls/review/aero-groove-lawn-bowls-review](https://krussll.github.io/jhb/bowls/review/aero-groove-lawn-bowls-review)
- **Local Dev URL:** [http://127.0.0.1:4000/jhb/bowls/review/aero-groove-lawn-bowls-review](http://127.0.0.1:4000/jhb/bowls/review/aero-groove-lawn-bowls-review)
- **Source File:** [`_posts/2020-09-12-aero-groove-lawn-bowls-review.md`](file:///home/reecewilliams8/dev work/jhb/_posts/2020-09-12-aero-groove-lawn-bowls-review.md)
- **Missing Images Count:** 8

| # | Image Filename | Referenced Path | Source Line |
| :--- | :--- | :--- | :--- |
| 1 | `aero-groove-set-of-four.jpg` | `/img/posts/aero-groove-set-of-four.jpg` | Line 133 |
| 2 | `aero-groove-set-of-four-running-surface.jpg` | `/img/posts/aero-groove-set-of-four-running-surface.jpg` | Line 167 |
| 3 | `aero-groove-set-of-four-colour.jpg` | `/img/posts/aero-groove-set-of-four-colour.jpg` | Line 183 |
| 4 | `z-scoop-grip-aero.png` | `/img/posts/z-scoop-grip-aero.png` | Line 209 |
| 5 | `aero-groove-grip.jpg` | `/img/posts/aero-groove-grip.jpg` | Line 221 |
| 6 | `zig-zag-grip-aero.png` | `/img/posts/zig-zag-grip-aero.png` | Line 229 |
| 7 | `dentations-grip-aero.png` | `/img/posts/dentations-grip-aero.png` | Line 241 |
| 8 | `aero-groove-set-of-four-tertiary.jpg` | `/img/posts/aero-groove-set-of-four-tertiary.jpg` | Line 257 |


### 6. Jokes About Lawn Bowls
- **Published URL:** [https://krussll.github.io/jhb/help/jokes-about-lawn-bowls](https://krussll.github.io/jhb/help/jokes-about-lawn-bowls)
- **Local Dev URL:** [http://127.0.0.1:4000/jhb/help/jokes-about-lawn-bowls](http://127.0.0.1:4000/jhb/help/jokes-about-lawn-bowls)
- **Source File:** [`_posts/2021-02-01-jokes-about-lawn-bowls.md`](file:///home/reecewilliams8/dev work/jhb/_posts/2021-02-01-jokes-about-lawn-bowls.md)
- **Missing Images Count:** 8

| # | Image Filename | Referenced Path | Source Line |
| :--- | :--- | :--- | :--- |
| 1 | `joke-1.jpg` | `/img/posts/joke-1.jpg` | Line 22 |
| 2 | `joke-3.jpg` | `/img/posts/joke-3.jpg` | Line 82 |
| 3 | `joke-4.jpg` | `/img/posts/joke-4.jpg` | Line 138 |
| 4 | `joke-5.jpg` | `/img/posts/joke-5.jpg` | Line 142 |
| 5 | `joke-7.jpg` | `/img/posts/joke-7.jpg` | Line 182 |
| 6 | `joke-8.jpg` | `/img/posts/joke-8.jpg` | Line 186 |
| 7 | `joke-9.jpg` | `/img/posts/joke-9.jpg` | Line 190 |
| 8 | `joke-10.jpg` | `/img/posts/joke-10.jpg` | Line 194 |


### 7. Aero Quantum Lawn Bowls Review
- **Published URL:** [https://krussll.github.io/jhb/bowls/review/aero-quantum-review](https://krussll.github.io/jhb/bowls/review/aero-quantum-review)
- **Local Dev URL:** [http://127.0.0.1:4000/jhb/bowls/review/aero-quantum-review](http://127.0.0.1:4000/jhb/bowls/review/aero-quantum-review)
- **Source File:** [`_posts/2021-05-18-aero-quantum-review.md`](file:///home/reecewilliams8/dev work/jhb/_posts/2021-05-18-aero-quantum-review.md)
- **Missing Images Count:** 6

| # | Image Filename | Referenced Path | Source Line |
| :--- | :--- | :--- | :--- |
| 1 | `aero-quantum-set.jpg` | `/img/posts/aero-quantum-set.jpg` | Line 136 |
| 2 | `aero-indoor-uk-trajectory-guide-2020.png` | `/img/posts/aero-indoor-uk-trajectory-guide-2020.png` | Line 150 |
| 3 | `aero-quantum-single.jpg` | `/img/posts/aero-quantum-single.jpg` | Line 180 |
| 4 | `aero-quantum-side.jpg` | `/img/posts/aero-quantum-side.jpg` | Line 226 |
| 5 | `aero-quantum-grip.jpg` | `/img/posts/aero-quantum-grip.jpg` | Line 272 |
| 6 | `aero-quantum-surface.jpg` | `/img/posts/aero-quantum-surface.jpg` | Line 322 |


### 8. Best Lawn Bowls Shoes
- **Published URL:** [https://krussll.github.io/jhb/guide/best-lawn-bowls-shoes](https://krussll.github.io/jhb/guide/best-lawn-bowls-shoes)
- **Local Dev URL:** [http://127.0.0.1:4000/jhb/guide/best-lawn-bowls-shoes](http://127.0.0.1:4000/jhb/guide/best-lawn-bowls-shoes)
- **Source File:** [`_posts/2020-09-17-best-lawn-bowls-shoes.md`](file:///home/reecewilliams8/dev work/jhb/_posts/2020-09-17-best-lawn-bowls-shoes.md)
- **Missing Images Count:** 6

| # | Image Filename | Referenced Path | Source Line |
| :--- | :--- | :--- | :--- |
| 1 | `henselite-hm74.png` | `/img/posts/henselite-hm74.png` | Line 149 |
| 2 | `henselite-blade34.png` | `/img/posts/henselite-blade34.png` | Line 177 |
| 3 | `aero-sprint.png` | `/img/posts/aero-sprint.png` | Line 205 |
| 4 | `henselite-moccasin.png` | `/img/posts/henselite-moccasin.png` | Line 233 |
| 5 | `henselite-hm75.png` | `/img/posts/henselite-hm75.png` | Line 253 |
| 6 | `drakes-pride-astro.png` | `/img/posts/drakes-pride-astro.png` | Line 277 |


### 9. Used Aero Bowls For Sale
- **Published URL:** [https://krussll.github.io/jhb/guide/used-aero-bowls-for-sale](https://krussll.github.io/jhb/guide/used-aero-bowls-for-sale)
- **Local Dev URL:** [http://127.0.0.1:4000/jhb/guide/used-aero-bowls-for-sale](http://127.0.0.1:4000/jhb/guide/used-aero-bowls-for-sale)
- **Source File:** [`_posts/2019-05-20-used-aero-bowls-for-sale.md`](file:///home/reecewilliams8/dev work/jhb/_posts/2019-05-20-used-aero-bowls-for-sale.md)
- **Missing Images Count:** 6

| # | Image Filename | Referenced Path | Source Line |
| :--- | :--- | :--- | :--- |
| 1 | `aero-groove.jpg` | `/img/posts/aero-groove.jpg` | Line 42 |
| 2 | `aero-sonic.jpg` | `/img/posts/aero-sonic.jpg` | Line 58 |
| 3 | `aero-quantum.jpg` | `/img/posts/aero-quantum.jpg` | Line 74 |
| 4 | `aero-maxim.jpg` | `/img/posts/aero-maxim.jpg` | Line 90 |
| 5 | `aero-profile.jpg` | `/img/posts/aero-profile.jpg` | Line 106 |
| 6 | `aero-defiance.jpg` | `/img/posts/aero-defiance.jpg` | Line 122 |


### 10. What The Stamp Means On Lawn Bowls | A Helpful Illustrated Guide
- **Published URL:** [https://krussll.github.io/jhb/help/what-the-stamp-means-on-lawn-bowls](https://krussll.github.io/jhb/help/what-the-stamp-means-on-lawn-bowls)
- **Local Dev URL:** [http://127.0.0.1:4000/jhb/help/what-the-stamp-means-on-lawn-bowls](http://127.0.0.1:4000/jhb/help/what-the-stamp-means-on-lawn-bowls)
- **Source File:** [`_posts/2020-09-30-what-the-stamp-means-on-lawn-bowls.md`](file:///home/reecewilliams8/dev work/jhb/_posts/2020-09-30-what-the-stamp-means-on-lawn-bowls.md)
- **Missing Images Count:** 6

| # | Image Filename | Referenced Path | Source Line |
| :--- | :--- | :--- | :--- |
| 1 | `new-stamp.png` | `/img/posts/new-stamp.png` | Line 34 |
| 2 | `old-stamp.png` | `/img/posts/old-stamp.png` | Line 38 |
| 3 | `new-stamp-expiry.png` | `/img/posts/new-stamp-expiry.png` | Line 78 |
| 4 | `new-stamp-registered.png` | `/img/posts/new-stamp-registered.png` | Line 94 |
| 5 | `new-stamp-standard.png` | `/img/posts/new-stamp-standard.png` | Line 122 |
| 6 | `new-stamp-tester.png` | `/img/posts/new-stamp-tester.png` | Line 138 |


### 11. Best Junior Lawn Bowls
- **Published URL:** [https://krussll.github.io/jhb/guide/best-junior-lawn-bowls](https://krussll.github.io/jhb/guide/best-junior-lawn-bowls)
- **Local Dev URL:** [http://127.0.0.1:4000/jhb/guide/best-junior-lawn-bowls](http://127.0.0.1:4000/jhb/guide/best-junior-lawn-bowls)
- **Source File:** [`_posts/2020-10-01-best-junior-lawn-bowls.md`](file:///home/reecewilliams8/dev work/jhb/_posts/2020-10-01-best-junior-lawn-bowls.md)
- **Missing Images Count:** 4

| # | Image Filename | Referenced Path | Source Line |
| :--- | :--- | :--- | :--- |
| 1 | `junior-bowlers.png` | `/img/posts/junior-bowlers.png` | Line 62 |
| 2 | `junior-taylor-ace.png` | `/img/posts/junior-taylor-ace.png` | Line 86 |
| 3 | `junior-taylor-ace-colours.png` | `/img/posts/junior-taylor-ace-colours.png` | Line 94 |
| 4 | `junior-drakes-pride-professional.png` | `/img/posts/junior-drakes-pride-professional.png` | Line 106 |


### 12. Best Lawn Bowls Grip Enhancers
- **Published URL:** [https://krussll.github.io/jhb/guide/best-lawn-bowls-grip-enhancers](https://krussll.github.io/jhb/guide/best-lawn-bowls-grip-enhancers)
- **Local Dev URL:** [http://127.0.0.1:4000/jhb/guide/best-lawn-bowls-grip-enhancers](http://127.0.0.1:4000/jhb/guide/best-lawn-bowls-grip-enhancers)
- **Source File:** [`_posts/2020-07-01-best-lawn-bowls-grip-enhancers.md`](file:///home/reecewilliams8/dev work/jhb/_posts/2020-07-01-best-lawn-bowls-grip-enhancers.md)
- **Missing Images Count:** 4

| # | Image Filename | Referenced Path | Source Line |
| :--- | :--- | :--- | :--- |
| 1 | `grip-it-lawn-bowls-wax.jpg` | `/img/posts/grip-it-lawn-bowls-wax.jpg` | Line 70 |
| 2 | `grippo.jpg` | `/img/posts/grippo.jpg` | Line 102 |
| 3 | `crack-a-jack-lawn-bowls-wax.jpg` | `/img/posts/crack-a-jack-lawn-bowls-wax.jpg` | Line 130 |
| 4 | `bulldog.jpg` | `/img/posts/bulldog.jpg` | Line 154 |


### 13. Lawn Bowls Bias Guide And Trajectory Charts | A Helpful Illustrated Guide
- **Published URL:** [https://krussll.github.io/jhb/guide/lawn-bowls-bias-guide-and-trajectory-charts-2020](https://krussll.github.io/jhb/guide/lawn-bowls-bias-guide-and-trajectory-charts-2020)
- **Local Dev URL:** [http://127.0.0.1:4000/jhb/guide/lawn-bowls-bias-guide-and-trajectory-charts-2020](http://127.0.0.1:4000/jhb/guide/lawn-bowls-bias-guide-and-trajectory-charts-2020)
- **Source File:** [`_posts/2020-05-20-lawn-bowls-bias-guide-and-trajectory-charts-2020.md`](file:///home/reecewilliams8/dev work/jhb/_posts/2020-05-20-lawn-bowls-bias-guide-and-trajectory-charts-2020.md)
- **Missing Images Count:** 4

| # | Image Filename | Referenced Path | Source Line |
| :--- | :--- | :--- | :--- |
| 1 | `aero-outdoor-uk-trajectory-guide-2020.png` | `/img/posts/aero-outdoor-uk-trajectory-guide-2020.png` | Line 66 |
| 2 | `aero-indoor-uk-trajectory-guide-2020.png` | `/img/posts/aero-indoor-uk-trajectory-guide-2020.png` | Line 70 |
| 3 | `drakes-pride-trajectory-guide-2020.png` | `/img/posts/drakes-pride-trajectory-guide-2020.png` | Line 100 |
| 4 | `thomas-taylor-trajectory-guide-2020.png` | `/img/posts/thomas-taylor-trajectory-guide-2020.png` | Line 152 |


### 14. Lawn Bowls Rules And Etiquette
- **Published URL:** [https://krussll.github.io/jhb/help/lawn-bowls-rules-and-etiquette](https://krussll.github.io/jhb/help/lawn-bowls-rules-and-etiquette)
- **Local Dev URL:** [http://127.0.0.1:4000/jhb/help/lawn-bowls-rules-and-etiquette](http://127.0.0.1:4000/jhb/help/lawn-bowls-rules-and-etiquette)
- **Source File:** [`_posts/2019-04-24-lawn-bowls-rules-and-etiquette.md`](file:///home/reecewilliams8/dev work/jhb/_posts/2019-04-24-lawn-bowls-rules-and-etiquette.md)
- **Missing Images Count:** 4

| # | Image Filename | Referenced Path | Source Line |
| :--- | :--- | :--- | :--- |
| 1 | `lawn_bowls_etiquette_one.jpg` | `/img/posts/lawn_bowls_etiquette_one.jpg` | Line 50 |
| 2 | `lawn_bowls_etiquette_two.jpg` | `/img/posts/lawn_bowls_etiquette_two.jpg` | Line 78 |
| 3 | `lawn_bowls_etiquette_three.jpg` | `/img/posts/lawn_bowls_etiquette_three.jpg` | Line 106 |
| 4 | `lawn_bowls_etiquette_four.jpg` | `/img/posts/lawn_bowls_etiquette_four.jpg` | Line 134 |


### 15. Taylor Blaze Lawn Bowls Review
- **Published URL:** [https://krussll.github.io/jhb/bowls/review/taylor-blaze-lawn-bowls-review](https://krussll.github.io/jhb/bowls/review/taylor-blaze-lawn-bowls-review)
- **Local Dev URL:** [http://127.0.0.1:4000/jhb/bowls/review/taylor-blaze-lawn-bowls-review](http://127.0.0.1:4000/jhb/bowls/review/taylor-blaze-lawn-bowls-review)
- **Source File:** [`_posts/2020-09-01-taylor-blaze-lawn-bowls-review.md`](file:///home/reecewilliams8/dev work/jhb/_posts/2020-09-01-taylor-blaze-lawn-bowls-review.md)
- **Missing Images Count:** 3

| # | Image Filename | Referenced Path | Source Line |
| :--- | :--- | :--- | :--- |
| 1 | `premier-grip-taylor.png` | `/img/posts/premier-grip-taylor.png` | Line 175 |
| 2 | `progrip-grip-taylor.png` | `/img/posts/progrip-grip-taylor.png` | Line 191 |
| 3 | `xtreme-grip-taylor.png` | `/img/posts/xtreme-grip-taylor.png` | Line 211 |


### 16. Taylor International Lawn Bowls Review
- **Published URL:** [https://krussll.github.io/jhb/bowls/review/taylor-international-lawn-bowls-review](https://krussll.github.io/jhb/bowls/review/taylor-international-lawn-bowls-review)
- **Local Dev URL:** [http://127.0.0.1:4000/jhb/bowls/review/taylor-international-lawn-bowls-review](http://127.0.0.1:4000/jhb/bowls/review/taylor-international-lawn-bowls-review)
- **Source File:** [`_posts/2021-04-27-taylor-international-lawn-bowls-review.md`](file:///home/reecewilliams8/dev work/jhb/_posts/2021-04-27-taylor-international-lawn-bowls-review.md)
- **Missing Images Count:** 3

| # | Image Filename | Referenced Path | Source Line |
| :--- | :--- | :--- | :--- |
| 1 | `taylor-international.jpg` | `/img/posts/taylor-international.jpg` | Line 127 |
| 2 | `taylor-international-colour.jpg` | `/img/posts/taylor-international-colour.jpg` | Line 151 |
| 3 | `taylor-international-grip.jpg` | `/img/posts/taylor-international-grip.jpg` | Line 175 |


### 17. The Best Lawn Bowl Grips  | A Helpful Illustrated Guide
- **Published URL:** [https://krussll.github.io/jhb/guide/best-lawn-bowl-grips](https://krussll.github.io/jhb/guide/best-lawn-bowl-grips)
- **Local Dev URL:** [http://127.0.0.1:4000/jhb/guide/best-lawn-bowl-grips](http://127.0.0.1:4000/jhb/guide/best-lawn-bowl-grips)
- **Source File:** [`_posts/2021-04-27-best-lawn-bowl-grips.md`](file:///home/reecewilliams8/dev work/jhb/_posts/2021-04-27-best-lawn-bowl-grips.md)
- **Missing Images Count:** 3

| # | Image Filename | Referenced Path | Source Line |
| :--- | :--- | :--- | :--- |
| 1 | `68747470733a2f2f63726f776e67...702d636f6d62696e65642e6a7067` | `/img/posts/68747470733a2f2f63726f776e677265656e6b696e672e66696c65732e776f726470726573732e636f6d2f323031322f30392f636c61772d677269702d636f6d62696e65642e6a7067` | Line 118 |
| 2 | `68747470733a2f2f63726f776e67...702d636f6d62696e65642e6a7067` | `/img/posts/68747470733a2f2f63726f776e677265656e6b696e672e66696c65732e776f726470726573732e636f6d2f323031322f30392f637261646c652d677269702d636f6d62696e65642e6a7067` | Line 134 |
| 3 | `68747470733a2f2f69312e77702e...2d322d352e6a70673f773d373130` | `/img/posts/68747470733a2f2f69312e77702e636f6d2f7777772e77696e6e696e67626f776c732e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031322f30382f332d322d352e6a70673f773d373130` | Line 150 |


### 18. 7 Best Straight Lawn Bowls | A Helpful Guide
- **Published URL:** [https://krussll.github.io/jhb/guide/best-straight-lawn-bowls](https://krussll.github.io/jhb/guide/best-straight-lawn-bowls)
- **Local Dev URL:** [http://127.0.0.1:4000/jhb/guide/best-straight-lawn-bowls](http://127.0.0.1:4000/jhb/guide/best-straight-lawn-bowls)
- **Source File:** [`_posts/2020-10-29-best-straight-lawn-bowls.md`](file:///home/reecewilliams8/dev work/jhb/_posts/2020-10-29-best-straight-lawn-bowls.md)
- **Missing Images Count:** 3

| # | Image Filename | Referenced Path | Source Line |
| :--- | :--- | :--- | :--- |
| 1 | `aero-defiance-display.jpg` | `/img/posts/aero-defiance-display.jpg` | Line 144 |
| 2 | `henselite-classic-ii-display.jpg` | `/img/posts/henselite-classic-ii-display.jpg` | Line 184 |
| 3 | `aero-profile-display.jpg` | `/img/posts/aero-profile-display.jpg` | Line 214 |


### 19. Lawn Bowls Reading The Head For Beginners
- **Published URL:** [https://krussll.github.io/jhb/help/lawn-bowls-how-to-read-the-head](https://krussll.github.io/jhb/help/lawn-bowls-how-to-read-the-head)
- **Local Dev URL:** [http://127.0.0.1:4000/jhb/help/lawn-bowls-how-to-read-the-head](http://127.0.0.1:4000/jhb/help/lawn-bowls-how-to-read-the-head)
- **Source File:** [`_posts/2019-09-30-lawn-bowls-how-to-read-the-head.md`](file:///home/reecewilliams8/dev work/jhb/_posts/2019-09-30-lawn-bowls-how-to-read-the-head.md)
- **Missing Images Count:** 3

| # | Image Filename | Referenced Path | Source Line |
| :--- | :--- | :--- | :--- |
| 1 | `reading-the-head-example-holding.jpg` | `/img/posts/reading-the-head-example-holding.jpg` | Line 274 |
| 2 | `reading-the-head-example-down.jpg` | `/img/posts/reading-the-head-example-down.jpg` | Line 330 |
| 3 | `reading-the-head-example-balanced.jpg` | `/img/posts/reading-the-head-example-balanced.jpg` | Line 382 |


### 20. Lawn Bowls vs Bocce (9 Similarities and Differences) | A Simple Illustrated Guide
- **Published URL:** [https://krussll.github.io/jhb/help/lawn-bowls-vs-bocce](https://krussll.github.io/jhb/help/lawn-bowls-vs-bocce)
- **Local Dev URL:** [http://127.0.0.1:4000/jhb/help/lawn-bowls-vs-bocce](http://127.0.0.1:4000/jhb/help/lawn-bowls-vs-bocce)
- **Source File:** [`_posts/2019-02-19-lawn-bowls-vs-bocce.md`](file:///home/reecewilliams8/dev work/jhb/_posts/2019-02-19-lawn-bowls-vs-bocce.md)
- **Missing Images Count:** 3

| # | Image Filename | Referenced Path | Source Line |
| :--- | :--- | :--- | :--- |
| 1 | `bocce.png` | `/img/posts/bocce.png` | Line 130 |
| 2 | `lawn-bowls-ditch.png` | `/img/posts/lawn-bowls-ditch.png` | Line 178 |
| 3 | `guide-to-bocce.png` | `/img/posts/guide-to-bocce.png` | Line 194 |


### 21. Best Crown Green Bowls for Beginners | A Complete Buyers Guide
- **Published URL:** [https://krussll.github.io/jhb/crown-green-bowls/best-crown-green-bowls-for-beginners-a-complete-buyers-guide](https://krussll.github.io/jhb/crown-green-bowls/best-crown-green-bowls-for-beginners-a-complete-buyers-guide)
- **Local Dev URL:** [http://127.0.0.1:4000/jhb/crown-green-bowls/best-crown-green-bowls-for-beginners-a-complete-buyers-guide](http://127.0.0.1:4000/jhb/crown-green-bowls/best-crown-green-bowls-for-beginners-a-complete-buyers-guide)
- **Source File:** [`_posts/2022-06-07-best-crown-green-bowls-for-beginners-a-complete-buyers-guide.md`](file:///home/reecewilliams8/dev work/jhb/_posts/2022-06-07-best-crown-green-bowls-for-beginners-a-complete-buyers-guide.md)
- **Missing Images Count:** 2

| # | Image Filename | Referenced Path | Source Line |
| :--- | :--- | :--- | :--- |
| 1 | `9UUadFHvGfv_sK8Dp4udZCMGEmWD...mX5P5ltwg6X88Q2Zu7B4F6ovl1DW` | `/img/posts/9UUadFHvGfv_sK8Dp4udZCMGEmWDr87elIe9NkG8Ujil0Ii4cJKdCOMbpg7foIE9joQ8lUXLinSqBCqBSayhM7l7jHT3djcKYVNDKk_xVwgY0BtX5_rNmX5P5ltwg6X88Q2Zu7B4F6ovl1DW` | Line 34 |
| 2 | `tbp77ONShXNEq_RlNN3px79IrUbN...Gm_2yoGD9pkGWGb2QabRejqTb19q` | `/img/posts/tbp77ONShXNEq_RlNN3px79IrUbNzF53T2WrI0VV0vQBzVUJFgbNlNbmGFGeiJnqX0THG0tCvzRekIh533_lqxkVTb7VRvwlPWFyWjeL3UEGsPmT4OMNGm_2yoGD9pkGWGb2QabRejqTb19q` | Line 86 |


### 22. Taylor GTR Lawn Bowls Review
- **Published URL:** [https://krussll.github.io/jhb/bowls/review/taylor-gtr-lawn-bowl-review](https://krussll.github.io/jhb/bowls/review/taylor-gtr-lawn-bowl-review)
- **Local Dev URL:** [http://127.0.0.1:4000/jhb/bowls/review/taylor-gtr-lawn-bowl-review](http://127.0.0.1:4000/jhb/bowls/review/taylor-gtr-lawn-bowl-review)
- **Source File:** [`_posts/2021-04-30-taylor-gtr-lawn-bowl-review.md`](file:///home/reecewilliams8/dev work/jhb/_posts/2021-04-30-taylor-gtr-lawn-bowl-review.md)
- **Missing Images Count:** 1

| # | Image Filename | Referenced Path | Source Line |
| :--- | :--- | :--- | :--- |
| 1 | `68747470733a2f2f7777772e626f...4754525f626961732d322e6a7067` | `/img/posts/68747470733a2f2f7777772e626f776c65727370617261646973652e636f6d2e61752f73686f702f696d616765732f542f4754525f626961732d322e6a7067` | Line 184 |


### 23. Best Yellow Lawn Bowls | Yellow Bowls Options From All Major Brands | A Complete Guide
- **Published URL:** [https://krussll.github.io/jhb/guide/best-yellow-lawn-bowls](https://krussll.github.io/jhb/guide/best-yellow-lawn-bowls)
- **Local Dev URL:** [http://127.0.0.1:4000/jhb/guide/best-yellow-lawn-bowls](http://127.0.0.1:4000/jhb/guide/best-yellow-lawn-bowls)
- **Source File:** [`_posts/2022-04-06-best-yellow-lawn-bowls.md`](file:///home/reecewilliams8/dev work/jhb/_posts/2022-04-06-best-yellow-lawn-bowls.md)
- **Missing Images Count:** 1

| # | Image Filename | Referenced Path | Source Line |
| :--- | :--- | :--- | :--- |
| 1 | `T170F-L.jpg` | `/img/posts/T170F-L.jpg` | Line 160 |


### 24. Is Lawn Bowls Is A Dying Sport? Or Does It Just Need Reviving? | A Complete Guide
- **Published URL:** [https://krussll.github.io/jhb/help/is-lawn-bowls-a-dying-sport](https://krussll.github.io/jhb/help/is-lawn-bowls-a-dying-sport)
- **Local Dev URL:** [http://127.0.0.1:4000/jhb/help/is-lawn-bowls-a-dying-sport](http://127.0.0.1:4000/jhb/help/is-lawn-bowls-a-dying-sport)
- **Source File:** [`_posts/2021-01-28-is-lawn-bowls-a-dying-sport.md`](file:///home/reecewilliams8/dev work/jhb/_posts/2021-01-28-is-lawn-bowls-a-dying-sport.md)
- **Missing Images Count:** 1

| # | Image Filename | Referenced Path | Source Line |
| :--- | :--- | :--- | :--- |
| 1 | `cramlington-bowling-club-law...humberland-header2-250px.jpg` | `/img/posts/cramlington-bowling-club-lawn-bowls-northumberland-header2-250px.jpg` | Line 109 |


### 25. The Ultimate Guide To Playing Lawn Bowls In Wet Conditions | A Helpful Illustrated Guide
- **Published URL:** [https://krussll.github.io/jhb/help/playing-lawn-bowls-in-wet-conditions](https://krussll.github.io/jhb/help/playing-lawn-bowls-in-wet-conditions)
- **Local Dev URL:** [http://127.0.0.1:4000/jhb/help/playing-lawn-bowls-in-wet-conditions](http://127.0.0.1:4000/jhb/help/playing-lawn-bowls-in-wet-conditions)
- **Source File:** [`_posts/2022-02-22-playing-lawn-bowls-in-wet-conditions.md`](file:///home/reecewilliams8/dev work/jhb/_posts/2022-02-22-playing-lawn-bowls-in-wet-conditions.md)
- **Missing Images Count:** 1

| # | Image Filename | Referenced Path | Source Line |
| :--- | :--- | :--- | :--- |
| 1 | `68747470733a2f2f7777772e6a61...7261646c652d477269702e6a7067` | `/img/posts/68747470733a2f2f7777772e6a616d657367617264656e736c62632e63612f496d616765732f437261646c652d477269702e6a7067` | Line 154 |


## Master Table of All Missing Images

| # | Image Name | Page URL | Source File |
| :--- | :--- | :--- | :--- |
| 1 | `scorecard.png` | [help/how-to-fill-in-a-lawn-bowls-scorecard](https://krussll.github.io/jhb/help/how-to-fill-in-a-lawn-bowls-scorecard) | `2020-09-30-how-to-fill-in-a-lawn-bowls-scorecard.md` |
| 2 | `game-details.png` | [help/how-to-fill-in-a-lawn-bowls-scorecard](https://krussll.github.io/jhb/help/how-to-fill-in-a-lawn-bowls-scorecard) | `2020-09-30-how-to-fill-in-a-lawn-bowls-scorecard.md` |
| 3 | `team-details.png` | [help/how-to-fill-in-a-lawn-bowls-scorecard](https://krussll.github.io/jhb/help/how-to-fill-in-a-lawn-bowls-scorecard) | `2020-09-30-how-to-fill-in-a-lawn-bowls-scorecard.md` |
| 4 | `shots-details.png` | [help/how-to-fill-in-a-lawn-bowls-scorecard](https://krussll.github.io/jhb/help/how-to-fill-in-a-lawn-bowls-scorecard) | `2020-09-30-how-to-fill-in-a-lawn-bowls-scorecard.md` |
| 5 | `result-details.png` | [help/how-to-fill-in-a-lawn-bowls-scorecard](https://krussll.github.io/jhb/help/how-to-fill-in-a-lawn-bowls-scorecard) | `2020-09-30-how-to-fill-in-a-lawn-bowls-scorecard.md` |
| 6 | `game-details-completed.png` | [help/how-to-fill-in-a-lawn-bowls-scorecard](https://krussll.github.io/jhb/help/how-to-fill-in-a-lawn-bowls-scorecard) | `2020-09-30-how-to-fill-in-a-lawn-bowls-scorecard.md` |
| 7 | `team-details-completed.png` | [help/how-to-fill-in-a-lawn-bowls-scorecard](https://krussll.github.io/jhb/help/how-to-fill-in-a-lawn-bowls-scorecard) | `2020-09-30-how-to-fill-in-a-lawn-bowls-scorecard.md` |
| 8 | `scores-details-end1.png` | [help/how-to-fill-in-a-lawn-bowls-scorecard](https://krussll.github.io/jhb/help/how-to-fill-in-a-lawn-bowls-scorecard) | `2020-09-30-how-to-fill-in-a-lawn-bowls-scorecard.md` |
| 9 | `scores-details-end2.png` | [help/how-to-fill-in-a-lawn-bowls-scorecard](https://krussll.github.io/jhb/help/how-to-fill-in-a-lawn-bowls-scorecard) | `2020-09-30-how-to-fill-in-a-lawn-bowls-scorecard.md` |
| 10 | `scores-details-end3.png` | [help/how-to-fill-in-a-lawn-bowls-scorecard](https://krussll.github.io/jhb/help/how-to-fill-in-a-lawn-bowls-scorecard) | `2020-09-30-how-to-fill-in-a-lawn-bowls-scorecard.md` |
| 11 | `scores-details-end4.png` | [help/how-to-fill-in-a-lawn-bowls-scorecard](https://krussll.github.io/jhb/help/how-to-fill-in-a-lawn-bowls-scorecard) | `2020-09-30-how-to-fill-in-a-lawn-bowls-scorecard.md` |
| 12 | `scores-details-end5.png` | [help/how-to-fill-in-a-lawn-bowls-scorecard](https://krussll.github.io/jhb/help/how-to-fill-in-a-lawn-bowls-scorecard) | `2020-09-30-how-to-fill-in-a-lawn-bowls-scorecard.md` |
| 13 | `scores-details-end6.png` | [help/how-to-fill-in-a-lawn-bowls-scorecard](https://krussll.github.io/jhb/help/how-to-fill-in-a-lawn-bowls-scorecard) | `2020-09-30-how-to-fill-in-a-lawn-bowls-scorecard.md` |
| 14 | `scores-details-end7.png` | [help/how-to-fill-in-a-lawn-bowls-scorecard](https://krussll.github.io/jhb/help/how-to-fill-in-a-lawn-bowls-scorecard) | `2020-09-30-how-to-fill-in-a-lawn-bowls-scorecard.md` |
| 15 | `result-details-completed.png` | [help/how-to-fill-in-a-lawn-bowls-scorecard](https://krussll.github.io/jhb/help/how-to-fill-in-a-lawn-bowls-scorecard) | `2020-09-30-how-to-fill-in-a-lawn-bowls-scorecard.md` |
| 16 | `scorecard-completed.png` | [help/how-to-fill-in-a-lawn-bowls-scorecard](https://krussll.github.io/jhb/help/how-to-fill-in-a-lawn-bowls-scorecard) | `2020-09-30-how-to-fill-in-a-lawn-bowls-scorecard.md` |
| 17 | `stewart-anderson.jpg` | [help/world-bowls-player-profiles](https://krussll.github.io/jhb/help/world-bowls-player-profiles) | `2020-11-02-world-bowls-player-profiles.md` |
| 18 | `nicky-brett.jpg` | [help/world-bowls-player-profiles](https://krussll.github.io/jhb/help/world-bowls-player-profiles) | `2020-11-02-world-bowls-player-profiles.md` |
| 19 | `mark-dawes.jpg` | [help/world-bowls-player-profiles](https://krussll.github.io/jhb/help/world-bowls-player-profiles) | `2020-11-02-world-bowls-player-profiles.md` |
| 20 | `julie-forrest.jpg` | [help/world-bowls-player-profiles](https://krussll.github.io/jhb/help/world-bowls-player-profiles) | `2020-11-02-world-bowls-player-profiles.md` |
| 21 | `paul-foster.jpg` | [help/world-bowls-player-profiles](https://krussll.github.io/jhb/help/world-bowls-player-profiles) | `2020-11-02-world-bowls-player-profiles.md` |
| 22 | `les-gillett.jpg` | [help/world-bowls-player-profiles](https://krussll.github.io/jhb/help/world-bowls-player-profiles) | `2020-11-02-world-bowls-player-profiles.md` |
| 23 | `greg-harlow.jpg` | [help/world-bowls-player-profiles](https://krussll.github.io/jhb/help/world-bowls-player-profiles) | `2020-11-02-world-bowls-player-profiles.md` |
| 24 | `mervyn-king.jpg` | [help/world-bowls-player-profiles](https://krussll.github.io/jhb/help/world-bowls-player-profiles) | `2020-11-02-world-bowls-player-profiles.md` |
| 25 | `barrie-lester.jpg` | [help/world-bowls-player-profiles](https://krussll.github.io/jhb/help/world-bowls-player-profiles) | `2020-11-02-world-bowls-player-profiles.md` |
| 26 | `alex-marshall.jpg` | [help/world-bowls-player-profiles](https://krussll.github.io/jhb/help/world-bowls-player-profiles) | `2020-11-02-world-bowls-player-profiles.md` |
| 27 | `karen-murphy.jpg` | [help/world-bowls-player-profiles](https://krussll.github.io/jhb/help/world-bowls-player-profiles) | `2020-11-02-world-bowls-player-profiles.md` |
| 28 | `robert-paxton.jpg` | [help/world-bowls-player-profiles](https://krussll.github.io/jhb/help/world-bowls-player-profiles) | `2020-11-02-world-bowls-player-profiles.md` |
| 29 | `katherine-rednall.jpg` | [help/world-bowls-player-profiles](https://krussll.github.io/jhb/help/world-bowls-player-profiles) | `2020-11-02-world-bowls-player-profiles.md` |
| 30 | `aron-sherriff.jpg` | [help/world-bowls-player-profiles](https://krussll.github.io/jhb/help/world-bowls-player-profiles) | `2020-11-02-world-bowls-player-profiles.md` |
| 31 | `brett-wilkie.jpg` | [help/world-bowls-player-profiles](https://krussll.github.io/jhb/help/world-bowls-player-profiles) | `2020-11-02-world-bowls-player-profiles.md` |
| 32 | `forehand.png` | [help/lawn-bowls-hand-signals](https://krussll.github.io/jhb/help/lawn-bowls-hand-signals) | `2020-11-06-lawn-bowls-hand-signals.md` |
| 33 | `backhand.png` | [help/lawn-bowls-hand-signals](https://krussll.github.io/jhb/help/lawn-bowls-hand-signals) | `2020-11-06-lawn-bowls-hand-signals.md` |
| 34 | `bowl-to-a-spot.png` | [help/lawn-bowls-hand-signals](https://krussll.github.io/jhb/help/lawn-bowls-hand-signals) | `2020-11-06-lawn-bowls-hand-signals.md` |
| 35 | `our-bowl.png` | [help/lawn-bowls-hand-signals](https://krussll.github.io/jhb/help/lawn-bowls-hand-signals) | `2020-11-06-lawn-bowls-hand-signals.md` |
| 36 | `their-bowl.png` | [help/lawn-bowls-hand-signals](https://krussll.github.io/jhb/help/lawn-bowls-hand-signals) | `2020-11-06-lawn-bowls-hand-signals.md` |
| 37 | `bowls-are-touching.png` | [help/lawn-bowls-hand-signals](https://krussll.github.io/jhb/help/lawn-bowls-hand-signals) | `2020-11-06-lawn-bowls-hand-signals.md` |
| 38 | `where-is-the-jack.png` | [help/lawn-bowls-hand-signals](https://krussll.github.io/jhb/help/lawn-bowls-hand-signals) | `2020-11-06-lawn-bowls-hand-signals.md` |
| 39 | `distance-to-jack.png` | [help/lawn-bowls-hand-signals](https://krussll.github.io/jhb/help/lawn-bowls-hand-signals) | `2020-11-06-lawn-bowls-hand-signals.md` |
| 40 | `shots-for-us.png` | [help/lawn-bowls-hand-signals](https://krussll.github.io/jhb/help/lawn-bowls-hand-signals) | `2020-11-06-lawn-bowls-hand-signals.md` |
| 41 | `shots-against-us.png` | [help/lawn-bowls-hand-signals](https://krussll.github.io/jhb/help/lawn-bowls-hand-signals) | `2020-11-06-lawn-bowls-hand-signals.md` |
| 42 | `measure-for-shot.png` | [help/lawn-bowls-hand-signals](https://krussll.github.io/jhb/help/lawn-bowls-hand-signals) | `2020-11-06-lawn-bowls-hand-signals.md` |
| 43 | `bocce-ancient-rome.jpg` | [help/history-of-lawn-bowls](https://krussll.github.io/jhb/help/history-of-lawn-bowls) | `2020-10-23-history-of-lawn-bowls.md` |
| 44 | `edward-iii.png` | [help/history-of-lawn-bowls](https://krussll.github.io/jhb/help/history-of-lawn-bowls) | `2020-10-23-history-of-lawn-bowls.md` |
| 45 | `henry-VIII.png` | [help/history-of-lawn-bowls](https://krussll.github.io/jhb/help/history-of-lawn-bowls) | `2020-10-23-history-of-lawn-bowls.md` |
| 46 | `queen-mary.png` | [help/history-of-lawn-bowls](https://krussll.github.io/jhb/help/history-of-lawn-bowls) | `2020-10-23-history-of-lawn-bowls.md` |
| 47 | `shakespeare.png` | [help/history-of-lawn-bowls](https://krussll.github.io/jhb/help/history-of-lawn-bowls) | `2020-10-23-history-of-lawn-bowls.md` |
| 48 | `francis-drake-lawn-bowls.png` | [help/history-of-lawn-bowls](https://krussll.github.io/jhb/help/history-of-lawn-bowls) | `2020-10-23-history-of-lawn-bowls.md` |
| 49 | `sandy-bay-tasmania.png` | [help/history-of-lawn-bowls](https://krussll.github.io/jhb/help/history-of-lawn-bowls) | `2020-10-23-history-of-lawn-bowls.md` |
| 50 | `usa-lawn-bowls.png` | [help/history-of-lawn-bowls](https://krussll.github.io/jhb/help/history-of-lawn-bowls) | `2020-10-23-history-of-lawn-bowls.md` |
| 51 | `edwin-beard-budding.png` | [help/history-of-lawn-bowls](https://krussll.github.io/jhb/help/history-of-lawn-bowls) | `2020-10-23-history-of-lawn-bowls.md` |
| 52 | `royal-victorian-bowling-association.png` | [help/history-of-lawn-bowls](https://krussll.github.io/jhb/help/history-of-lawn-bowls) | `2020-10-23-history-of-lawn-bowls.md` |
| 53 | `aero-groove-set-of-four.jpg` | [bowls/review/aero-groove-lawn-bowls-review](https://krussll.github.io/jhb/bowls/review/aero-groove-lawn-bowls-review) | `2020-09-12-aero-groove-lawn-bowls-review.md` |
| 54 | `aero-groove-set-of...unning-surface.jpg` | [bowls/review/aero-groove-lawn-bowls-review](https://krussll.github.io/jhb/bowls/review/aero-groove-lawn-bowls-review) | `2020-09-12-aero-groove-lawn-bowls-review.md` |
| 55 | `aero-groove-set-of-four-colour.jpg` | [bowls/review/aero-groove-lawn-bowls-review](https://krussll.github.io/jhb/bowls/review/aero-groove-lawn-bowls-review) | `2020-09-12-aero-groove-lawn-bowls-review.md` |
| 56 | `z-scoop-grip-aero.png` | [bowls/review/aero-groove-lawn-bowls-review](https://krussll.github.io/jhb/bowls/review/aero-groove-lawn-bowls-review) | `2020-09-12-aero-groove-lawn-bowls-review.md` |
| 57 | `aero-groove-grip.jpg` | [bowls/review/aero-groove-lawn-bowls-review](https://krussll.github.io/jhb/bowls/review/aero-groove-lawn-bowls-review) | `2020-09-12-aero-groove-lawn-bowls-review.md` |
| 58 | `zig-zag-grip-aero.png` | [bowls/review/aero-groove-lawn-bowls-review](https://krussll.github.io/jhb/bowls/review/aero-groove-lawn-bowls-review) | `2020-09-12-aero-groove-lawn-bowls-review.md` |
| 59 | `dentations-grip-aero.png` | [bowls/review/aero-groove-lawn-bowls-review](https://krussll.github.io/jhb/bowls/review/aero-groove-lawn-bowls-review) | `2020-09-12-aero-groove-lawn-bowls-review.md` |
| 60 | `aero-groove-set-of-four-tertiary.jpg` | [bowls/review/aero-groove-lawn-bowls-review](https://krussll.github.io/jhb/bowls/review/aero-groove-lawn-bowls-review) | `2020-09-12-aero-groove-lawn-bowls-review.md` |
| 61 | `joke-1.jpg` | [help/jokes-about-lawn-bowls](https://krussll.github.io/jhb/help/jokes-about-lawn-bowls) | `2021-02-01-jokes-about-lawn-bowls.md` |
| 62 | `joke-3.jpg` | [help/jokes-about-lawn-bowls](https://krussll.github.io/jhb/help/jokes-about-lawn-bowls) | `2021-02-01-jokes-about-lawn-bowls.md` |
| 63 | `joke-4.jpg` | [help/jokes-about-lawn-bowls](https://krussll.github.io/jhb/help/jokes-about-lawn-bowls) | `2021-02-01-jokes-about-lawn-bowls.md` |
| 64 | `joke-5.jpg` | [help/jokes-about-lawn-bowls](https://krussll.github.io/jhb/help/jokes-about-lawn-bowls) | `2021-02-01-jokes-about-lawn-bowls.md` |
| 65 | `joke-7.jpg` | [help/jokes-about-lawn-bowls](https://krussll.github.io/jhb/help/jokes-about-lawn-bowls) | `2021-02-01-jokes-about-lawn-bowls.md` |
| 66 | `joke-8.jpg` | [help/jokes-about-lawn-bowls](https://krussll.github.io/jhb/help/jokes-about-lawn-bowls) | `2021-02-01-jokes-about-lawn-bowls.md` |
| 67 | `joke-9.jpg` | [help/jokes-about-lawn-bowls](https://krussll.github.io/jhb/help/jokes-about-lawn-bowls) | `2021-02-01-jokes-about-lawn-bowls.md` |
| 68 | `joke-10.jpg` | [help/jokes-about-lawn-bowls](https://krussll.github.io/jhb/help/jokes-about-lawn-bowls) | `2021-02-01-jokes-about-lawn-bowls.md` |
| 69 | `aero-quantum-set.jpg` | [bowls/review/aero-quantum-review](https://krussll.github.io/jhb/bowls/review/aero-quantum-review) | `2021-05-18-aero-quantum-review.md` |
| 70 | `aero-indoor-uk-trajectory-guide-2020.png` | [bowls/review/aero-quantum-review](https://krussll.github.io/jhb/bowls/review/aero-quantum-review) | `2021-05-18-aero-quantum-review.md` |
| 71 | `aero-quantum-single.jpg` | [bowls/review/aero-quantum-review](https://krussll.github.io/jhb/bowls/review/aero-quantum-review) | `2021-05-18-aero-quantum-review.md` |
| 72 | `aero-quantum-side.jpg` | [bowls/review/aero-quantum-review](https://krussll.github.io/jhb/bowls/review/aero-quantum-review) | `2021-05-18-aero-quantum-review.md` |
| 73 | `aero-quantum-grip.jpg` | [bowls/review/aero-quantum-review](https://krussll.github.io/jhb/bowls/review/aero-quantum-review) | `2021-05-18-aero-quantum-review.md` |
| 74 | `aero-quantum-surface.jpg` | [bowls/review/aero-quantum-review](https://krussll.github.io/jhb/bowls/review/aero-quantum-review) | `2021-05-18-aero-quantum-review.md` |
| 75 | `henselite-hm74.png` | [guide/best-lawn-bowls-shoes](https://krussll.github.io/jhb/guide/best-lawn-bowls-shoes) | `2020-09-17-best-lawn-bowls-shoes.md` |
| 76 | `henselite-blade34.png` | [guide/best-lawn-bowls-shoes](https://krussll.github.io/jhb/guide/best-lawn-bowls-shoes) | `2020-09-17-best-lawn-bowls-shoes.md` |
| 77 | `aero-sprint.png` | [guide/best-lawn-bowls-shoes](https://krussll.github.io/jhb/guide/best-lawn-bowls-shoes) | `2020-09-17-best-lawn-bowls-shoes.md` |
| 78 | `henselite-moccasin.png` | [guide/best-lawn-bowls-shoes](https://krussll.github.io/jhb/guide/best-lawn-bowls-shoes) | `2020-09-17-best-lawn-bowls-shoes.md` |
| 79 | `henselite-hm75.png` | [guide/best-lawn-bowls-shoes](https://krussll.github.io/jhb/guide/best-lawn-bowls-shoes) | `2020-09-17-best-lawn-bowls-shoes.md` |
| 80 | `drakes-pride-astro.png` | [guide/best-lawn-bowls-shoes](https://krussll.github.io/jhb/guide/best-lawn-bowls-shoes) | `2020-09-17-best-lawn-bowls-shoes.md` |
| 81 | `aero-groove.jpg` | [guide/used-aero-bowls-for-sale](https://krussll.github.io/jhb/guide/used-aero-bowls-for-sale) | `2019-05-20-used-aero-bowls-for-sale.md` |
| 82 | `aero-sonic.jpg` | [guide/used-aero-bowls-for-sale](https://krussll.github.io/jhb/guide/used-aero-bowls-for-sale) | `2019-05-20-used-aero-bowls-for-sale.md` |
| 83 | `aero-quantum.jpg` | [guide/used-aero-bowls-for-sale](https://krussll.github.io/jhb/guide/used-aero-bowls-for-sale) | `2019-05-20-used-aero-bowls-for-sale.md` |
| 84 | `aero-maxim.jpg` | [guide/used-aero-bowls-for-sale](https://krussll.github.io/jhb/guide/used-aero-bowls-for-sale) | `2019-05-20-used-aero-bowls-for-sale.md` |
| 85 | `aero-profile.jpg` | [guide/used-aero-bowls-for-sale](https://krussll.github.io/jhb/guide/used-aero-bowls-for-sale) | `2019-05-20-used-aero-bowls-for-sale.md` |
| 86 | `aero-defiance.jpg` | [guide/used-aero-bowls-for-sale](https://krussll.github.io/jhb/guide/used-aero-bowls-for-sale) | `2019-05-20-used-aero-bowls-for-sale.md` |
| 87 | `new-stamp.png` | [help/what-the-stamp-means-on-lawn-bowls](https://krussll.github.io/jhb/help/what-the-stamp-means-on-lawn-bowls) | `2020-09-30-what-the-stamp-means-on-lawn-bowls.md` |
| 88 | `old-stamp.png` | [help/what-the-stamp-means-on-lawn-bowls](https://krussll.github.io/jhb/help/what-the-stamp-means-on-lawn-bowls) | `2020-09-30-what-the-stamp-means-on-lawn-bowls.md` |
| 89 | `new-stamp-expiry.png` | [help/what-the-stamp-means-on-lawn-bowls](https://krussll.github.io/jhb/help/what-the-stamp-means-on-lawn-bowls) | `2020-09-30-what-the-stamp-means-on-lawn-bowls.md` |
| 90 | `new-stamp-registered.png` | [help/what-the-stamp-means-on-lawn-bowls](https://krussll.github.io/jhb/help/what-the-stamp-means-on-lawn-bowls) | `2020-09-30-what-the-stamp-means-on-lawn-bowls.md` |
| 91 | `new-stamp-standard.png` | [help/what-the-stamp-means-on-lawn-bowls](https://krussll.github.io/jhb/help/what-the-stamp-means-on-lawn-bowls) | `2020-09-30-what-the-stamp-means-on-lawn-bowls.md` |
| 92 | `new-stamp-tester.png` | [help/what-the-stamp-means-on-lawn-bowls](https://krussll.github.io/jhb/help/what-the-stamp-means-on-lawn-bowls) | `2020-09-30-what-the-stamp-means-on-lawn-bowls.md` |
| 93 | `junior-bowlers.png` | [guide/best-junior-lawn-bowls](https://krussll.github.io/jhb/guide/best-junior-lawn-bowls) | `2020-10-01-best-junior-lawn-bowls.md` |
| 94 | `junior-taylor-ace.png` | [guide/best-junior-lawn-bowls](https://krussll.github.io/jhb/guide/best-junior-lawn-bowls) | `2020-10-01-best-junior-lawn-bowls.md` |
| 95 | `junior-taylor-ace-colours.png` | [guide/best-junior-lawn-bowls](https://krussll.github.io/jhb/guide/best-junior-lawn-bowls) | `2020-10-01-best-junior-lawn-bowls.md` |
| 96 | `junior-drakes-pride-professional.png` | [guide/best-junior-lawn-bowls](https://krussll.github.io/jhb/guide/best-junior-lawn-bowls) | `2020-10-01-best-junior-lawn-bowls.md` |
| 97 | `grip-it-lawn-bowls-wax.jpg` | [guide/best-lawn-bowls-grip-enhancers](https://krussll.github.io/jhb/guide/best-lawn-bowls-grip-enhancers) | `2020-07-01-best-lawn-bowls-grip-enhancers.md` |
| 98 | `grippo.jpg` | [guide/best-lawn-bowls-grip-enhancers](https://krussll.github.io/jhb/guide/best-lawn-bowls-grip-enhancers) | `2020-07-01-best-lawn-bowls-grip-enhancers.md` |
| 99 | `crack-a-jack-lawn-bowls-wax.jpg` | [guide/best-lawn-bowls-grip-enhancers](https://krussll.github.io/jhb/guide/best-lawn-bowls-grip-enhancers) | `2020-07-01-best-lawn-bowls-grip-enhancers.md` |
| 100 | `bulldog.jpg` | [guide/best-lawn-bowls-grip-enhancers](https://krussll.github.io/jhb/guide/best-lawn-bowls-grip-enhancers) | `2020-07-01-best-lawn-bowls-grip-enhancers.md` |
| 101 | `aero-outdoor-uk-tr...ory-guide-2020.png` | [guide/lawn-bowls-bias-guide-and-trajectory-charts-2020](https://krussll.github.io/jhb/guide/lawn-bowls-bias-guide-and-trajectory-charts-2020) | `2020-05-20-lawn-bowls-bias-guide-and-trajectory-charts-2020.md` |
| 102 | `aero-indoor-uk-trajectory-guide-2020.png` | [guide/lawn-bowls-bias-guide-and-trajectory-charts-2020](https://krussll.github.io/jhb/guide/lawn-bowls-bias-guide-and-trajectory-charts-2020) | `2020-05-20-lawn-bowls-bias-guide-and-trajectory-charts-2020.md` |
| 103 | `drakes-pride-trajectory-guide-2020.png` | [guide/lawn-bowls-bias-guide-and-trajectory-charts-2020](https://krussll.github.io/jhb/guide/lawn-bowls-bias-guide-and-trajectory-charts-2020) | `2020-05-20-lawn-bowls-bias-guide-and-trajectory-charts-2020.md` |
| 104 | `thomas-taylor-trajectory-guide-2020.png` | [guide/lawn-bowls-bias-guide-and-trajectory-charts-2020](https://krussll.github.io/jhb/guide/lawn-bowls-bias-guide-and-trajectory-charts-2020) | `2020-05-20-lawn-bowls-bias-guide-and-trajectory-charts-2020.md` |
| 105 | `lawn_bowls_etiquette_one.jpg` | [help/lawn-bowls-rules-and-etiquette](https://krussll.github.io/jhb/help/lawn-bowls-rules-and-etiquette) | `2019-04-24-lawn-bowls-rules-and-etiquette.md` |
| 106 | `lawn_bowls_etiquette_two.jpg` | [help/lawn-bowls-rules-and-etiquette](https://krussll.github.io/jhb/help/lawn-bowls-rules-and-etiquette) | `2019-04-24-lawn-bowls-rules-and-etiquette.md` |
| 107 | `lawn_bowls_etiquette_three.jpg` | [help/lawn-bowls-rules-and-etiquette](https://krussll.github.io/jhb/help/lawn-bowls-rules-and-etiquette) | `2019-04-24-lawn-bowls-rules-and-etiquette.md` |
| 108 | `lawn_bowls_etiquette_four.jpg` | [help/lawn-bowls-rules-and-etiquette](https://krussll.github.io/jhb/help/lawn-bowls-rules-and-etiquette) | `2019-04-24-lawn-bowls-rules-and-etiquette.md` |
| 109 | `premier-grip-taylor.png` | [bowls/review/taylor-blaze-lawn-bowls-review](https://krussll.github.io/jhb/bowls/review/taylor-blaze-lawn-bowls-review) | `2020-09-01-taylor-blaze-lawn-bowls-review.md` |
| 110 | `progrip-grip-taylor.png` | [bowls/review/taylor-blaze-lawn-bowls-review](https://krussll.github.io/jhb/bowls/review/taylor-blaze-lawn-bowls-review) | `2020-09-01-taylor-blaze-lawn-bowls-review.md` |
| 111 | `xtreme-grip-taylor.png` | [bowls/review/taylor-blaze-lawn-bowls-review](https://krussll.github.io/jhb/bowls/review/taylor-blaze-lawn-bowls-review) | `2020-09-01-taylor-blaze-lawn-bowls-review.md` |
| 112 | `taylor-international.jpg` | [bowls/review/taylor-international-lawn-bowls-review](https://krussll.github.io/jhb/bowls/review/taylor-international-lawn-bowls-review) | `2021-04-27-taylor-international-lawn-bowls-review.md` |
| 113 | `taylor-international-colour.jpg` | [bowls/review/taylor-international-lawn-bowls-review](https://krussll.github.io/jhb/bowls/review/taylor-international-lawn-bowls-review) | `2021-04-27-taylor-international-lawn-bowls-review.md` |
| 114 | `taylor-international-grip.jpg` | [bowls/review/taylor-international-lawn-bowls-review](https://krussll.github.io/jhb/bowls/review/taylor-international-lawn-bowls-review) | `2021-04-27-taylor-international-lawn-bowls-review.md` |
| 115 | `68747470733a2f2f63...62696e65642e6a7067` | [guide/best-lawn-bowl-grips](https://krussll.github.io/jhb/guide/best-lawn-bowl-grips) | `2021-04-27-best-lawn-bowl-grips.md` |
| 116 | `68747470733a2f2f63...62696e65642e6a7067` | [guide/best-lawn-bowl-grips](https://krussll.github.io/jhb/guide/best-lawn-bowl-grips) | `2021-04-27-best-lawn-bowl-grips.md` |
| 117 | `68747470733a2f2f69...6a70673f773d373130` | [guide/best-lawn-bowl-grips](https://krussll.github.io/jhb/guide/best-lawn-bowl-grips) | `2021-04-27-best-lawn-bowl-grips.md` |
| 118 | `aero-defiance-display.jpg` | [guide/best-straight-lawn-bowls](https://krussll.github.io/jhb/guide/best-straight-lawn-bowls) | `2020-10-29-best-straight-lawn-bowls.md` |
| 119 | `henselite-classic-ii-display.jpg` | [guide/best-straight-lawn-bowls](https://krussll.github.io/jhb/guide/best-straight-lawn-bowls) | `2020-10-29-best-straight-lawn-bowls.md` |
| 120 | `aero-profile-display.jpg` | [guide/best-straight-lawn-bowls](https://krussll.github.io/jhb/guide/best-straight-lawn-bowls) | `2020-10-29-best-straight-lawn-bowls.md` |
| 121 | `reading-the-head-example-holding.jpg` | [help/lawn-bowls-how-to-read-the-head](https://krussll.github.io/jhb/help/lawn-bowls-how-to-read-the-head) | `2019-09-30-lawn-bowls-how-to-read-the-head.md` |
| 122 | `reading-the-head-example-down.jpg` | [help/lawn-bowls-how-to-read-the-head](https://krussll.github.io/jhb/help/lawn-bowls-how-to-read-the-head) | `2019-09-30-lawn-bowls-how-to-read-the-head.md` |
| 123 | `reading-the-head-example-balanced.jpg` | [help/lawn-bowls-how-to-read-the-head](https://krussll.github.io/jhb/help/lawn-bowls-how-to-read-the-head) | `2019-09-30-lawn-bowls-how-to-read-the-head.md` |
| 124 | `bocce.png` | [help/lawn-bowls-vs-bocce](https://krussll.github.io/jhb/help/lawn-bowls-vs-bocce) | `2019-02-19-lawn-bowls-vs-bocce.md` |
| 125 | `lawn-bowls-ditch.png` | [help/lawn-bowls-vs-bocce](https://krussll.github.io/jhb/help/lawn-bowls-vs-bocce) | `2019-02-19-lawn-bowls-vs-bocce.md` |
| 126 | `guide-to-bocce.png` | [help/lawn-bowls-vs-bocce](https://krussll.github.io/jhb/help/lawn-bowls-vs-bocce) | `2019-02-19-lawn-bowls-vs-bocce.md` |
| 127 | `9UUadFHvGfv_sK8Dp4...X88Q2Zu7B4F6ovl1DW` | [crown-green-bowls/best-crown-green-bowls-for-beginners-a-complete-buyers-guide](https://krussll.github.io/jhb/crown-green-bowls/best-crown-green-bowls-for-beginners-a-complete-buyers-guide) | `2022-06-07-best-crown-green-bowls-for-beginners-a-complete-buyers-guide.md` |
| 128 | `tbp77ONShXNEq_RlNN...kGWGb2QabRejqTb19q` | [crown-green-bowls/best-crown-green-bowls-for-beginners-a-complete-buyers-guide](https://krussll.github.io/jhb/crown-green-bowls/best-crown-green-bowls-for-beginners-a-complete-buyers-guide) | `2022-06-07-best-crown-green-bowls-for-beginners-a-complete-buyers-guide.md` |
| 129 | `68747470733a2f2f77...6961732d322e6a7067` | [bowls/review/taylor-gtr-lawn-bowl-review](https://krussll.github.io/jhb/bowls/review/taylor-gtr-lawn-bowl-review) | `2021-04-30-taylor-gtr-lawn-bowl-review.md` |
| 130 | `T170F-L.jpg` | [guide/best-yellow-lawn-bowls](https://krussll.github.io/jhb/guide/best-yellow-lawn-bowls) | `2022-04-06-best-yellow-lawn-bowls.md` |
| 131 | `cramlington-bowlin...-header2-250px.jpg` | [help/is-lawn-bowls-a-dying-sport](https://krussll.github.io/jhb/help/is-lawn-bowls-a-dying-sport) | `2021-01-28-is-lawn-bowls-a-dying-sport.md` |
| 132 | `68747470733a2f2f77...2d477269702e6a7067` | [help/playing-lawn-bowls-in-wet-conditions](https://krussll.github.io/jhb/help/playing-lawn-bowls-in-wet-conditions) | `2022-02-22-playing-lawn-bowls-in-wet-conditions.md` |

## Recommended Remediation Priorities

1. **High Priority (Core Instructional Guides):**
   - [`how-to-fill-in-a-lawn-bowls-scorecard`](file:///home/reecewilliams8/dev work/jhb/_posts/2020-09-30-how-to-fill-in-a-lawn-bowls-scorecard.md) (16 images): Add actual scorecard section crops or replace with a single annotated scorecard diagram.
   - [`lawn-bowls-hand-signals`](file:///home/reecewilliams8/dev work/jhb/_posts/2020-11-06-lawn-bowls-hand-signals.md) (11 images): Key visual gestures (forehand, backhand, touchers, distance to jack).
   - [`lawn-bowls-rules-and-etiquette`](file:///home/reecewilliams8/dev work/jhb/_posts/2019-04-24-lawn-bowls-rules-and-etiquette.md) (4 images): Etiquette illustration diagrams.
2. **Medium Priority (Reviews & Bias Guides):**
   - Fix hex-encoded Camo URLs in `best-lawn-bowl-grips.md` and `playing-lawn-bowls-in-wet-conditions.md`.
   - Trajectory charts in `lawn-bowls-bias-guide-and-trajectory-charts-2020.md`.
3. **Low Priority / Candidates for Removal:**
   - `jokes-about-lawn-bowls.md` (8 images): Generic meme/joke images that can either be replaced or simply removed without loss of editorial substance.
   - `world-bowls-player-profiles.md` (15 player headshots): Outdated player headshots; consider removing individual image embeds or adding modern headshots.