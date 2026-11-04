# CC-20: Set up heatmaps and session recordings

- **Source document:** `.agents/core-content-promotion-plan.md` (§7.2 "Heatmaps & session recordings")
- **Owner:** 🤝 Shared: user picks the tool and creates the account, agent adds the snippet
- **Priority:** Low
- **Status:** Not started
- **Depends on:** Ideally after CC-01 and CC-07, so the new hero and tab modules exist

> [!NOTE]
> **User action required:** pick a tool (e.g., Microsoft Clarity, which is free, or Hotjar) and create the project, then give the agent the project ID. Decide on cookie consent: UK GDPR/PECR may require consent before recording.

## Task
Monitor how visitors interact with the homepage hero and the Getting Started tab modules, to check the layout works.

## Context
- Add the tracking snippet through a dedicated include (e.g., `_includes/clarity.html`), controlled by a `_config.yml` key. Load it only in production (`jekyll.environment == "production"`).
- Update `privacy.html` to name the tool and explain what it records.
- Mask form inputs (the Kit email field).

## Completion criteria
- [ ] Tool installed and recording on production only.
- [ ] Privacy policy updated; consent handled appropriately.
- [ ] User has reviewed at least one heatmap of `/` and `/getting-started/` and noted findings.
