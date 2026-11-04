# CC-10: Add social proof (testimonials or reader quotes) near the tactics pathway

- **Source document:** `.agents/core-content-promotion-plan.md` (§3.3 "Conversion blocks", social proof)
- **Owner:** 🤝 Shared: user supplies genuine quotes, agent builds the component
- **Priority:** Low–Medium
- **Status:** Not started
- **Depends on:** User input

> [!IMPORTANT]
> **User action required:** provide **genuine** testimonials or reader quotes, with permission and attribution details (name or initials, club, position). The agent must not invent testimonials. That would break E-E-A-T and UK consumer protection rules (CMA guidance on fake reviews).

## Task
Add a testimonial/quote component near the tactics pathway (step 4, "Play your first competitive games") on `/getting-started/`. Optionally reuse it on the drill pack page (DP-02).

## Context
- Store quotes in `_data/testimonials.yml` (quote, name, club, role, consent date) and render them with an include such as `_includes/testimonial.html`, using `<figure><blockquote>…</blockquote><figcaption>…</figcaption></figure>`.
- The homepage already has a club coach quote section (`.home-quote` in `_layouts/home.html`). Match its styling.

## Completion criteria
- [ ] At least two genuine, attributed quotes stored in `_data/testimonials.yml`.
- [ ] Testimonial component appears beside the tactics pathway on `/getting-started/`.
- [ ] Semantic markup and good contrast.
- [ ] `bundle exec jekyll build` completes without errors.
