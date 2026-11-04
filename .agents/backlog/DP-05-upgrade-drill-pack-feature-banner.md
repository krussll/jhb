# DP-05: Upgrade the in-article drill pack promo banner

- **Source document:** `.agents/drill-pack-cro-plan.md` (§4 files table: `_includes/drill-pack-feature.html`)
- **Owner:** 🤖 Agent
- **Priority:** Medium
- **Status:** Not started
- **Depends on:** Better after DP-01/DP-02 so the bullets match the final offer, but can start now

## Task
Strengthen `_includes/drill-pack-feature.html`, the promo shown at the bottom of every blog post (`_layouts/post.html` line ~115), to push more clicks through to the sales page.

## Context
- Current banner: an H2 "Get The Complete Lawn Bowls Drill Pack", two generic sentences, a "Win More Games Today >>" button and an image.
- Problems spotted:
  - The `<img>` (`/img/drill-pack.png`) has **no `alt` text, width/height or `loading="lazy"`**, which hurts accessibility and CLS.
  - It links with `{{ site.baseurl }}/lawn-bowls-downloadable-drill-pack` instead of `relative_url`.
  - The copy has no value bullets.
- Add three or four concrete value bullets: 20 scored drills, Good/Better/Best targets, solo and pairs, club-shed equipment only, instant PDF. Add an optional price/anchor from the DP-04 data source and a `.drill-pack-cta`-styled button.
- Use the brand palette and existing `.pack-feature` styles (find them in `_sass/`).

## Completion criteria
- [ ] Banner shows value bullets and a clear CTA that links to `/lawn-bowls-downloadable-drill-pack/` via `relative_url`.
- [ ] Image has descriptive alt text, width/height and lazy loading.
- [ ] Looks right at mobile, tablet and desktop widths on a sample post.
- [ ] `bundle exec jekyll build` completes without errors.
