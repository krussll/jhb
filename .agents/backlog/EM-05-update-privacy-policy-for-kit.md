# EM-05: Update the privacy policy to name Kit instead of Mailchimp

- **Source document:** `.agents/email-migration-and-sequence-plan.md` (§4 item 3 "Update GDPR Disclosures in privacy.html"; §6 checklist Step 4)
- **Owner:** 🤖 Agent
- **Priority:** High (GDPR accuracy; the live form already sends data to Kit)
- **Status:** Not started
- **Depends on:** None (Kit is confirmed: the form posts to `https://app.kit.com/forms/10138357/subscriptions`)

## Task
Replace every Mailchimp reference in `privacy.html` with Kit, so the policy matches the data processor actually in use.

## Context
Mailchimp mentions found on 2026-11-04:
- `privacy.html` lines ~95–98 (§3.2): "managed through **Mailchimp** (The Rocket Science Group LLC / Intuit)..."
- `privacy.html` line ~205 (§6 third-party processors): "**Mailchimp:** Secure distribution of our newsletter and playbook emails."
- `privacy.html` line ~219 (§7 retention): "remains in our secure Mailchimp audience list..."

Replace with **Kit (Kit, Inc.)**, formerly ConvertKit. Also mention that the signup form loads Kit's script (`https://f.convertkit.com/ckjs/ck.5.js`) from a third-party domain. Mention any international data transfer (Kit is US-based). Update the policy's "last updated" date if it has one.

## Completion criteria
- [ ] `grep -in mailchimp privacy.html` returns nothing.
- [ ] Kit is named as the newsletter processor in §3.2, §6 and §7, with accurate wording.
- [ ] The policy's last-updated date is refreshed.
- [ ] `bundle exec jekyll build` completes without errors.
