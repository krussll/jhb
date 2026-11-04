# CC-09: Add an email capture block to the Getting Started hub

- **Source document:** `.agents/core-content-promotion-plan.md` (§3.3 "Conversion blocks", email capture)
- **Owner:** 🤖 Agent (user decision needed on the offer)
- **Priority:** Medium
- **Status:** Not started. `getting-started.md` has no newsletter or lead-magnet block.
- **Depends on:** EM-06 (on-brand Kit form include)

> [!NOTE]
> **User decision needed:** the plan says to offer "the drill pack in exchange for subscribing", but the drill pack is a **paid** product (£2.99, possibly more after DP-01). Choose the incentive: the free Weight Control Playbook (what the sitewide form already promises), a free sample drill (EM-07), or a discount code for the pack.

## Task
Add a newsletter capture block to `/getting-started/` with the incentive the user chooses.

## Context
- Reuse `_includes/lead-magnet.html` (already used at the bottom of posts with `section_class="home-lead post-lead"`), which wraps the Kit form include (`_includes/mailchimp-form.html`, form `10138357`).
- Good placement: after step 3 ("Build core skills") or in the `.gs-next-steps` section.
- Copy must match what Kit actually delivers (EM-03/EM-04).

## Completion criteria
- [ ] Capture block is live on `/getting-started/`, with copy matching the incentive Kit delivers.
- [ ] A test signup from the page appears in Kit.
- [ ] `bundle exec jekyll build` completes without errors.
