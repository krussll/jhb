# DP-04: Sync the drill pack price across the site

- **Source document:** `.agents/drill-pack-cro-plan.md` (§3 item 9, §4 files table)
- **Owner:** 🤖 Agent
- **Priority:** Medium
- **Status:** Not started
- **Depends on:** DP-01 (new price must be decided and live in Lemon Squeezy first)

## Task
Replace every hardcoded `£2.99` mention with the new price, and ideally centralise it so this never has to be done by hand again.

## Context
Current hardcoded mentions (found 2026-11-04):
- `ai-coaching.md` line ~41: `View 20-Drill Pack (£2.99)`
- `ai-coaching.md` line ~148: `... Drill Pack</strong> (£2.99) ...`
- `_includes/ai-prompt-builder.html` line ~133: `Get the 20-Drill Pack (£2.99)`
- `lawn-bowls-downloadable-drill-pack.md` price box (gets replaced in DP-02)

Recommended: add a `drill_pack:` block to `_config.yml` or `_data/` (price, anchor price, checkout URL) and reference it from Liquid everywhere, including the DP-03 schema. Search the whole repo (`_posts/`, `_includes/`, root pages, `llms.txt`) for `2.99`, `24.99` and the checkout URL before finishing. Also check the email sequence copy (EM-04) for price mentions.

## Completion criteria
- [ ] `grep -rn "2\.99" --exclude-dir=_site --exclude-dir=vendor .` returns no stale price mentions (excluding `.agents/` docs).
- [ ] Price and checkout URL come from one data source referenced by every CTA.
- [ ] `last_modified_at` updated on any post files changed.
- [ ] `bundle exec jekyll build` completes without errors.
