# EM-06: Restyle the Kit signup form to match the site and fix how it's embedded

- **Source document:** `.agents/email-migration-and-sequence-plan.md` (§4 item 1: "Keep your exact `.home-lead__form`, `.form-group`, and `.form-control` classes so the modal and inline forms look identical")
- **Owner:** 🤖 Agent
- **Priority:** High
- **Status:** Partly done. The form was swapped to Kit (commit `c86f656`), but Kit's raw embed was pasted in rather than the site's own styled markup.
- **Depends on:** None

## Task
Rework `_includes/mailchimp-form.html` so the Kit form uses the site's existing lead-form markup and brand styles, keeps working with Kit, and doesn't clash with the site's own modal.

## Context
- The current include is about 634 lines of Kit's default embed:
  - Inline `<style>` block of roughly 600 lines.
  - Blue `rgb(22,119,190)` button.
  - Generic "Join the Newsletter / Subscribe to get our latest content" copy that doesn't mention the Weight Control Playbook.
  - "Built with Kit" branding.
  - It ignores the `button_text` include parameter (e.g., `newsletter-modal.html` passes `button_text="Email me the playbook"`).
- It's included by `_includes/newsletter-modal.html`, `_includes/lead-magnet.html` (used in `_layouts/post.html` line ~120) and `_includes/lead-magnet-backup.html`. **On every post the form renders twice**, once inline and once in the modal, with the same `data-uid="b3c7fe064b"`.
- The embed has `data-format="modal"`, and its `data-options` include a 5-second timer trigger. Check whether Kit's `ck.5.js` turns it into a **second popup** on top of the site's own `newsletter-modal`. If it does, switch to an inline format or a plain HTML POST.
- Simplest robust approach: a plain `<form action="https://app.kit.com/forms/10138357/subscriptions" method="post">` with `name="email_address"` and optional `name="fields[first_name]"`, using the existing `.home-lead__form`, `.form-group` and `.form-control` classes, and honouring `include.button_text`. Drop `ck.5.js` if it isn't needed, or load it once, deferred, from `assets/js` per AGENTS.md.
- Optionally rename the include to `newsletter-form.html` and update the three includes that use it.
- Brand palette: `#1F2B5F`, `#C89B3C`, `#f8f9fa`, `#222222`. Make sure inputs have proper `<label>`s (not just `aria-label` or a placeholder).

## Completion criteria
- [ ] The inline lead block and the modal look on-brand and identical to each other; the button text comes from `include.button_text`.
- [ ] A test signup from both the inline block and the modal appears in Kit and triggers the incentive email.
- [ ] No duplicate or extra Kit popup appears on post pages.
- [ ] The form is accessible (visible labels, focus styles, error and success messages announced).
- [ ] Lighthouse accessibility and performance on a sample post are ≥ 90.
- [ ] `bundle exec jekyll build` completes without errors.
