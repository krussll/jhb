# EM-07: Add a "free sample drill" email capture block to the drill pack page

- **Source document:** `.agents/email-migration-and-sequence-plan.md` (§4 item 2 "Bonus Conversion Hook")
- **Owner:** 🤝 Shared: agent builds the block, user provides the sample PDF and Kit setup
- **Priority:** Medium
- **Status:** Not started
- **Depends on:** EM-06 (on-brand form markup); DP-02 (new page layout); user input below

> [!NOTE]
> **User action required:** create a one-drill sample PDF (e.g., Drill #1 "Find The Gap"). Then decide whether it's delivered through the existing Kit form/incentive or through a separate Kit form or tag. Kit's free plan has only one sequence and one visual automation, so a tag on the existing form may be the only option.

## Task
Give hesitant visitors on `/lawn-bowls-downloadable-drill-pack/` a free alternative: "Download 1 free sample drill + get the Weight Control Playbook". Signing up puts them into the 4-part sequence (EM-04), which ends with the drill pack pitch.

## Context
- Reuse the form include from EM-06 (`{% include mailchimp-form.html button_text="Send me the free drill" %}` or the renamed include).
- Place it below the FAQ / above the final CTA so it doesn't compete with the buy button above the fold.
- Copy must say exactly what the subscriber gets, and link to `/privacy/`.

## Completion criteria
- [ ] Capture block is on the drill pack page and styled to match the page.
- [ ] A test signup gets the sample drill and the playbook, and enters the intro sequence.
- [ ] The block doesn't push the primary buy CTA below the fold on mobile.
- [ ] `bundle exec jekyll build` completes without errors.
