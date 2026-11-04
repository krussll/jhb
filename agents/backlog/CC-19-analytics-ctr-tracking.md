# CC-19: Track click-through from the homepage hero, pathways and footer

- **Source document:** `.agents/core-content-promotion-plan.md` (§7.1 "Analytics dashboards")
- **Owner:** 🤝 Shared: agent adds event tracking, user builds the dashboard in GA4
- **Priority:** Low–Medium
- **Status:** Not started. Basic `gtag.js` page tracking exists (`_includes/google-analytics.html`, using `site.google_analytics`), but no click events are tracked.
- **Depends on:** Ideally after CC-01, CC-02 and CC-05, so the new elements exist

> [!NOTE]
> **User action required:** build the dashboard or exploration in Google Analytics 4 (and mark key events), using the event names the agent adds. An agent can't access the GA4 property.

## Task
Add consistent click tracking to promotional elements, and build a dashboard that shows CTR by placement.

## Context
- Add `data-track="hero-cta"`, `data-track="pathway-card"`, `data-track="footer-core-guides"` and similar attributes. One small delegated listener in `assets/js/analytics-events.js` sends `gtag('event', 'promo_click', {placement, link_url})`. Only send events if `gtag` exists.
- Cover: homepage hero CTAs, the pathways section, footer Core Guides links, drill pack CTAs (banner, inline callouts, footer), and the promo strip.
- Check the privacy policy covers analytics events; update it if needed.

## Completion criteria
- [ ] Click events fire with placement labels (checked in GA4 DebugView).
- [ ] User has built a GA4 report showing clicks and CTR by placement.
- [ ] `bundle exec jekyll build` completes without errors.
