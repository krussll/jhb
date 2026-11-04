# CC-22: Plan and run seasonal promo strip swaps

- **Source document:** `.agents/core-content-promotion-plan.md` (§1.3 "Schedule seasonal swaps (e.g., preseason tactics)"; "Ongoing: Seasonal promo updates")
- **Owner:** 👤 User only (recurring); an agent can make the data edits on request
- **Priority:** Low (recurring)
- **Status:** Not started
- **Depends on:** CC-03 (promo strip driven by `_data/promos.yml`)

> [!IMPORTANT]
> **User-only, recurring task: Reece needs to do this.** Choosing seasonal campaigns is an editorial and commercial call.

## Task
Keep a seasonal calendar of promo strip messages, e.g. pre-season practice (March–April), outdoor season tactics (May–August), indoor season kit (September–October) and gift guides (November–December). Swap them in on time without losing the core focus on the drill pack and buying guides.

## Context
- Once CC-03 is built, each swap is just a `_data/promos.yml` edit (message, URL, start/end dates). Date-bounded entries can switch automatically at build time. Note that GitHub Pages only rebuilds on push, so a scheduled rebuild may be needed.

## Completion criteria
- [ ] Seasonal promo calendar written down (this file or `_data/promos.yml` comments).
- [ ] First seasonal swap is live.
