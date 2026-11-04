# YH-06: Add social profiles and `sameAs` entity links

- **Source document:** `.agents/yahoo-seo-visibility-plan.md` (Phase 4 item 2 "Social Profiles in `_config.yml` & `Organization` Schema (`sameAs`)")
- **Owner:** 🤝 Shared: user supplies the URLs, agent wires them in
- **Priority:** Low–Medium
- **Status:** Not started. `twitter_username`, `github_username`, `facebook_username`, `instagram_username` and `linkedin_username` are all blank in `_config.yml`, and no schema includes `sameAs`.
- **Depends on:** User input

> [!NOTE]
> **User action required:** list the official Jack High Bowls (and Reece Williams) social and profile URLs: Facebook, X/Twitter, Instagram, YouTube, LinkedIn, and any club or governing-body profile pages. If there aren't any, decide whether to create them. The agent can't create accounts.

## Task
Fill in the social profile settings and add `sameAs` arrays to the `Organization` and `Person` schema, so Bing and Yahoo can confirm the brand entity.

## Context
- Schema lives in `_includes/head.html`: `WebSite` → `publisher` `Organization` (line ~159) with a `founder` `Person`, plus `Organization`/`Person` blocks in the `Article` and `ItemList` schema (lines ~284–361).
- `_includes/footer.html` already shows social icons when `site.<network>_username` is set, so filling these in shows icons automatically. Check the footer still looks right afterwards.
- Author data may also live in `_data/authors`. Add `sameAs` for Reece there if it's present.

## Completion criteria
- [ ] Real profile values added to `_config.yml` (and author data, if relevant).
- [ ] `Organization` and `Person` JSON-LD include `sameAs` arrays with those URLs, and validate without errors.
- [ ] Footer icons render correctly with accessible labels.
- [ ] `bundle exec jekyll build` completes without errors.
