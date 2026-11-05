# DP-02: Redesign the drill pack sales page as a high-converting landing page

- **Source document:** `.agents/drill-pack-cro-plan.md` (§1 audit, §3 "High-Converting Page Architecture Plan", §4 files table)
- **Owner:** 🤝 Shared: agent builds it, user supplies drill content
- **Priority:** High
- **Status:** Not started (page is still the original 72-line version)
- **Depends on:** DP-01 (final price and guarantee wording); user input listed below
- **Related:** DP-03 (schema), DP-04 (price sync), EM-07 (sample-drill email capture on this page)

> [!NOTE]
> **User input needed before the curriculum and sample drill sections can be accurate:** the names of all 20 drills, grouped into modules, plus the full content of Drill #1 "Find The Gap" (setup, equipment, rules, easier/harder variations, scoring). The agent must not invent drill names or content. They only exist in the PDF, which isn't in the repo.

## Task
Replace the minimal `lawn-bowls-downloadable-drill-pack.md` with a full sales page. Style it with a new dedicated SCSS partial.

## Context
- Page: `lawn-bowls-downloadable-drill-pack.md` (`layout: product`, `permalink: /lawn-bowls-downloadable-drill-pack/`, `hide_page_hero: true`). It currently has about 180 words of copy.
- Audit findings to fix:
  - It uses **Bootstrap 5** classes (`row g-4`, `bg-light`) on a **Bootstrap 4.6** theme.
  - The existing `.drill-pack-cta` styles in `_sass/_page.scss` (lines ~106–139) go unused; the page uses `.btn-primary` / `.btn-success` instead.
  - It doesn't name a single one of the 20 drills.
  - `img/drill-pack/inside-pages.png` is a collage where the text gets cut off.
  - There's no author or E-E-A-T proof on the page.
  - The price element still carries the WordPress class `wp-block-paragraph`.
- Sections to build, in order:
  1. **Split hero (`.dp-hero`).** Eyebrow pill, an outcome-driven H1 ("Turn Aimless Roll-Ups Into Match-Winning Consistency"), the subtitle, a price box with an anchor and "Save X%", a `.drill-pack-cta` button that opens the Lemon Squeezy modal, a micro-trust bar (secure checkout, instant PDF, refund), and the cover image with a badge and a "Preview a full sample drill ↓" jump link.
  2. **Problem → solution strip:** "The Typical Club Roll-Up" vs "The JHB Structured System".
  3. **"Look inside" sample drill card** for Drill #1: Find The Gap, shown alongside `inside-pages.png`.
  4. **20-drill curriculum grid.** Four modules: Line & Gate Control, Draw Weight & Length, Head Building & Target Zones, Weighted Shots & Pressure Conversions.
  5. **"Who this is built for"** personas: new bowlers, club leads/seconds/skips, club coaches.
  6. **Scorecard and AI companion section.** Explain the "out of 40 / 48" scoring and link to `/ai-coaching/prompt-builder/`.
  7. **Author credentials block.** Use `/img/reece-williams-jack-high-bowls.jpg`, 15+ years' experience, Club Singles Finalist / County Quarter-Finalist, and the club coach quote from the homepage (`_layouts/home.html`, `.home-quote` section). Reuse wording from `_data/authors` / `_includes/author-bio.html` where possible.
  8. **Guarantee callout and FAQ accordion.** Six FAQs using native `<details>`/`<summary>`: equipment, solo use, indoor/outdoor/short mat, delivery and printing, skill level, refunds.
  9. **Final conversion banner.**
- Brand palette: `#1F2B5F`, `#C89B3C`, `#f8f9fa`, `#222222`. Don't add new web fonts. Use the existing breakpoints and mixins.
- Create `_sass/_drill-pack.scss` and add `@import "drill-pack";` to `_sass/styles.scss`.
- Every CTA must keep the checkout URL (`https://jack-high-bowls.lemonsqueezy.com/checkout/buy/6515ca0b-b861-4530-8142-0bb075d71bb8`, or a new one from DP-01), keep `data-ls-modal="true"`, and the page must still load `https://assets.lemonsqueezy.com/lemon.js`. Move the inline `<script>` to a front-matter flag or include if that's practical (AGENTS.md says to avoid inline scripts).
- Update `last_modified_at` in front matter.

## Completion criteria
- [ ] All nine sections above are on the page, with real drill names and real Drill #1 content supplied by the user.
- [ ] No Bootstrap 5-only classes remain; layout uses Bootstrap 4.6 utilities and the new `_sass/_drill-pack.scss`.
- [ ] Primary CTAs use `.drill-pack-cta`; every buy button opens the Lemon Squeezy modal with the correct checkout URL.
- [ ] Heading hierarchy is valid (single `h1` → `h2` → `h3`); the FAQ is keyboard-accessible; all images have descriptive alt text and width/height.
- [ ] Responsive at mobile, tablet and desktop widths. Lighthouse accessibility and performance are both ≥ 90.
- [ ] `bundle exec jekyll build` completes without errors.
