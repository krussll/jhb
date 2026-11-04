# EM-02: Set up the Kit sender identity and DNS authentication (SPF, DKIM, DMARC)

- **Source document:** `.agents/email-migration-and-sequence-plan.md` (§3 "Phase 2: Account, DNS & Deliverability Setup")
- **Owner:** 👤 User only
- **Priority:** High
- **Status:** Unverified (the agent can't access Kit or the domain's DNS manager)
- **Depends on:** None

> [!IMPORTANT]
> **User-only task: Reece needs to do this.** It needs the Kit account and the DNS provider for `jackhighbowls.com`.

## Task
Make sure emails from Kit are authenticated so they land in the inbox. Many bowlers use strict ISP inboxes: BT Internet, Sky, TalkTalk, Yahoo, Gmail.

## Context / steps
1. In Kit, set the "From" name to `Reece at Jack High Bowls` and the sending address to `reece@jackhighbowls.com`. Never send bulk email from a free `@gmail.com` address.
2. Verify `jackhighbowls.com` as a sending domain in Kit, and add the **DKIM** and **SPF** records Kit provides to the DNS manager.
3. Add or confirm a **DMARC** record at `_dmarc.jackhighbowls.com`:
   ```txt
   v=DMARC1; p=none; rua=mailto:reece@jackhighbowls.com
   ```
4. Keep any existing SPF include for other services. A domain must have only **one** SPF TXT record; merge the includes into it.

## Completion criteria
- [ ] Kit shows the domain as verified/authenticated.
- [ ] SPF, DKIM and DMARC records resolve publicly (check with MXToolbox or `dig TXT`).
- [ ] A test broadcast to a Gmail and a Yahoo inbox shows `spf=pass`, `dkim=pass` and `dmarc=pass` in the message headers.
