# DP-06: Create the printable pocket scorecard and 6-week progress tracker (Bonus #1)

- **Source document:** `.agents/drill-pack-cro-plan.md` (§2 "Proposed Value Stack", Bonus #1)
- **Owner:** 🤝 Shared: agent can draft it, user publishes it
- **Priority:** Medium
- **Status:** Not started
- **Depends on:** User supplying the 20 drill names and their max scores (out of 40 or 48)

> [!NOTE]
> **User action required to finish:** Reece must check the final asset against the real drills, then attach it to the Lemon Squeezy product (or bundle it into the PDF). An agent can't access Lemon Squeezy.

## Task
Produce a one-page printable **Pocket Scorecard & 6-Week Benchmark Tracker** that turns the 20 drills into a repeatable training programme. It forms part of the higher-price value stack.

## Context
- Each drill already uses a "Goals (Out of 40 / 48): Good / Better / Best" scoring system. Drill #1 "Find The Gap" scores Good 30 / Better 35 / Best 40.
- Format options: a print-optimised HTML page in the repo (e.g., an unlisted page with `@media print` styles that the user prints to PDF), or a designed PDF. A4, works in black and white, and readable on a phone.
- Should include: drill name, max score, Good/Better/Best targets, six weekly score columns, date and green-speed notes.
- Brand palette: `#1F2B5F`, `#C89B3C`, `#F5F2EB`, `#222222`.
- If it's built as a site page, keep it out of the sitemap and search (`sitemap: false` / `noindex: true`; `head.html` already supports both) so the paid bonus doesn't leak.

## Completion criteria
- [ ] Scorecard/tracker covers all 20 real drills with correct max scores and targets.
- [ ] Prints cleanly on a single A4 page (or a clearly paginated two-pager).
- [ ] User has added it to the Lemon Squeezy product/download.
- [ ] Sales page (DP-02) lists it as a bonus with its value.
