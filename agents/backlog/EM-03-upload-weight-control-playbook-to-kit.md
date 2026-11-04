# EM-03: Upload the Weight Control Playbook as the Kit incentive

- **Source document:** `.agents/email-migration-and-sequence-plan.md` (§3 item 3 "Upload the Lead Magnet")
- **Owner:** 👤 User only
- **Priority:** High
- **Status:** Unverified (the agent can't access Kit)
- **Depends on:** None
- **Blocks:** EM-04 (Email 1 needs the playbook link)

> [!IMPORTANT]
> **User-only task: Reece needs to do this.** The playbook PDF isn't in the repo, and uploading it needs the Kit account.

## Task
Make sure every new subscriber gets the **Weight Control Playbook** PDF within about a minute of signing up.

## Context
- The site promises it in `_includes/newsletter-modal.html` and `_includes/lead-magnet.html` / `lead-magnet-backup.html`: "the **Weight Control Playbook**: ten quick wins to sharpen your draw weight today".
- The embedded Kit form (`_includes/mailchimp-form.html`, form `10138357`) currently shows the success message "Success! Now check your email to confirm your subscription." That suggests double opt-in, so the incentive email should carry the PDF link.
- Either attach the PDF to Kit's **Incentive Email** for form `10138357`, or link it in Email 1 of the sequence (EM-04) via the `YOUR_PLAYBOOK_LINK` placeholder.

## Completion criteria
- [ ] Signing up with a test address delivers the playbook PDF (or a working download link) within 60 seconds of confirming.
- [ ] The playbook link URL is recorded here so EM-04 can use it: ______
