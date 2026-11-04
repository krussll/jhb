# CC-05: Add a "Core Guides" footer column and a persistent drill pack CTA

- **Source document:** `.agents/core-content-promotion-plan.md` (§2.2 "Secondary navigation / footer")
- **Owner:** 🤖 Agent
- **Priority:** Medium
- **Status:** Partly done. The footer nav (`_includes/footer-nav.html`) has a plain "Downloadable Drill Pack" text link alongside the legal and help links. There's no "Core Guides" column and no styled CTA.
- **Depends on:** None (CC-02's `_data/pathways.yml` can feed it)

## Task
Add a footer column listing the four goal-based pathways, and a visually distinct, always-visible drill pack CTA.

## Context
- Footer files: `_includes/footer.html` (social icons and copyright) and `_includes/footer-nav.html` (inline link list). Styles are in `_sass/_footer.scss`.
- Pathways: Learn the essentials, Choose your bowls, Practice smarter, Compete with confidence.
- Restructure into columns (e.g., Core Guides | Resources | Legal) that stack on mobile. Wrap the column in `<nav aria-label="Core guides">`.
- Use `.drill-pack-cta` (`_sass/_page.scss`) or a footer variant for the CTA.

## Completion criteria
- [ ] Footer shows a "Core Guides" column with four pathway links that all resolve.
- [ ] A styled drill pack CTA appears in the footer on every page.
- [ ] Responsive stacking works on mobile; link contrast meets WCAG AA on the footer background.
- [ ] `bundle exec jekyll build` completes without errors.
