# EM-01: Export, clean and import the Mailchimp audience into Kit

- **Source document:** `.agents/email-migration-and-sequence-plan.md` (§2 "Phase 1: Pre-Migration List Hygiene"; §6 checklist Step 2)
- **Owner:** 👤 User only
- **Priority:** High
- **Status:** Unverified. The checklist box is still unticked, and the agent can't check either Mailchimp or Kit.
- **Depends on:** None (Kit was chosen as the provider; form ID `10138357` is already embedded on the site)
- **Blocks:** EM-08 (pausing Mailchimp billing)

> [!IMPORTANT]
> **User-only task: Reece needs to do this.** It needs logins for the Mailchimp and Kit accounts.

## Task
Move the roughly 2,085 subscribers from Mailchimp into Kit, without carrying over dead or unsubscribed contacts.

## Context / steps
1. In Mailchimp, go to **Audience → All contacts → Export Audience** and download the ZIP (Subscribed, Unsubscribed and Cleaned CSVs).
2. Optional but recommended: prune cold contacts, e.g. 6+ months on the list with a 0% open rate, or `Member Rating == 1`. Either send a final "Still working on your bowls game?" re-engagement email from Mailchimp first, or archive the dead contacts. Expect roughly 1,500–1,800 active contacts.
3. **Never** import the `Unsubscribed` or `Cleaned` CSVs into the active list. Import them only into Kit's suppression list, if at all.
4. Import the active contacts into Kit. Make sure imports **don't** trigger the new welcome sequence (EM-04) unless you want existing subscribers to get it.
- Kit's free Newsletter plan allows up to 10,000 subscribers, unlimited broadcasts, one visual automation and one sequence.

## Completion criteria
- [ ] Mailchimp export ZIP saved somewhere safe as a backup.
- [ ] Active subscribers imported into Kit; unsubscribed and cleaned contacts excluded (or suppressed).
- [ ] Existing subscribers aren't accidentally enrolled in the welcome sequence.
- [ ] Imported subscriber count noted here: ______
