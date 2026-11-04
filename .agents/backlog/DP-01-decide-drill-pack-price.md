# DP-01: Decide the drill pack price and update Lemon Squeezy

- **Source document:** `.agents/drill-pack-cro-plan.md` (§2 "Value-Stack Strategy" → "Recommended Pricing Architecture")
- **Owner:** 👤 User only
- **Priority:** High
- **Status:** Not started
- **Depends on:** None
- **Blocks:** DP-02 (price box copy), DP-03 (`Product` schema price), DP-04 (sitewide price sync)

> [!IMPORTANT]
> **User-only task: Reece needs to do this.** It's a commercial decision and needs access to the Lemon Squeezy dashboard. An agent can't make or apply it.

## Task
Pick the new price structure for the Downloadable Lawn Bowls Drill Pack and set it in Lemon Squeezy.

## Context
- Current live price: **£2.99**, with a **£24.99** strikethrough anchor (shown on `lawn-bowls-downloadable-drill-pack.md`).
- The CRO plan argues that £2.99 signals a "thin pamphlet". It proposes moving the product to £9.99–£14.99 and repositioning it as a "Complete Lawn Bowls Practice System".
- Options proposed:
  - **Option A: single price.** £9.99 (or £11.99) with a £24.99 anchor. Simplest: change the price on the existing Lemon Squeezy product.
  - **Option B: two tiers.** £7.99 Standard (20-drill PDF only) vs £14.99 "Complete System" (PDF, printable scorecards, 6-week plan and AI prompt templates). Option B needs a second Lemon Squeezy product/variant and new checkout URL(s), and depends on the bonus assets in DP-06 and DP-07 existing.
- Current checkout URL (must stay valid or be replaced everywhere): `https://jack-high-bowls.lemonsqueezy.com/checkout/buy/6515ca0b-b861-4530-8142-0bb075d71bb8`
- Decide the refund promise too. The page currently says "No questions asked refund policy"; the plan proposes a "30-Day Try It On The Green" guarantee.

## Completion criteria
- [ ] Option A or Option B chosen, with exact price(s) and anchor/strikethrough value recorded in this file (or passed to the agent).
- [ ] Lemon Squeezy product(s) updated to the new price; any new checkout URLs recorded.
- [ ] Refund/guarantee wording confirmed (e.g., "30-day no-questions refund").
