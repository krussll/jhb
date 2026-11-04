# EM-04: Build and switch on the 4-part automated intro sequence in Kit

- **Source documents:** `.agents/email-migration-and-sequence-plan.md` (§5 "Phase 4: The 4-Part Automated Intro Sequence"; §6 checklist Step 3). This also covers `.agents/core-content-promotion-plan.md` §6.1 "Email onboarding series".
- **Owner:** 👤 User only (an agent can proofread and correct the copy first if asked)
- **Priority:** High
- **Status:** Unverified (checklist box unticked; the agent can't access Kit)
- **Depends on:** EM-02 (deliverability), EM-03 (playbook link)

> [!IMPORTANT]
> **User-only task: Reece needs to do this.** Building the sequence in Kit needs the account. An agent can prepare the corrected copy (see the issues below) if you want.

## Task
Load the four emails into a Kit **Sequence**, triggered when someone submits the site signup form (form `10138357`), and switch it on.

## Context
- The full ready-to-use copy (subjects, preview text and bodies) is in `.agents/email-migration-and-sequence-plan.md` §5. That source plan stays in place until this task is done.
- Timing: Email 1 at Day 0 (playbook delivery and a "reply with your position and biggest struggle" ask); Email 2 at Day 2 (the "Roll-Up Trap" and a free length-ladder drill); Email 3 at Day 4 (bias, green speed and three cornerstone guides); Email 4 at Day 7 (drill pack pitch).
- **Copy issues to fix before loading:**
  - **Email 4 says the pack has "7 Progressive Skill Drills" and "30-Minute & 60-Minute Session Templates".** The sales page says **20 drills**, and the session templates only exist if DP-07 is completed. Make it match the real product and price (DP-01).
  - The sequence table calls the Email 2 drill the "3-Length Ladder Drill", but the email body calls it the "4-Bowl Length Ladder". Pick one name.
  - Email 1 typo: "a free blocker to hides behind" should be "to hide behind".
  - Check that the personalisation tag syntax (`{{ subscriber.first_name | default: "there" }}`) matches Kit's current Liquid syntax.
  - Check all links still resolve: `/ai-coaching/`, `/guide/how-to-choose-a-set-of-lawn-bowls/`, `/help/how-to-get-better-at-lawn-bowls/`, `/help/ultimate-guide-to-lawn-bowls-singles-tactics/`, `/lawn-bowls-downloadable-drill-pack/`.
- The core-content plan's separate "four-email welcome flow, one per pathway" idea is covered by this sequence. Kit's free plan allows only one sequence.

## Completion criteria
- [ ] All four emails are in Kit with the corrected copy and the right delays (0, +2, +4, +7 days).
- [ ] The sequence triggers on form `10138357` submissions only (not on bulk imports).
- [ ] A test subscriber receives all four emails with working links and correct personalisation.
- [ ] Email 4's product description matches the live sales page.
