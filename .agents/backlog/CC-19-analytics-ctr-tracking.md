# CC-19: Track click-through from the homepage hero, pathways and footer

- **Source document:** `.agents/core-content-promotion-plan.md` (§7.1 "Analytics dashboards")
- **Owner:** 🤝 Shared: agent adds event tracking, user builds the dashboard in GA4
- **Priority:** Low–Medium
- **Status:** In progress (Agent data tracking complete; awaiting user GA4 custom definitions & dashboard setup)
- **Depends on:** Ideally after CC-01, CC-02 and CC-05, so the new elements exist

> [!NOTE]
> **User action required:** Build the dashboard or exploration in Google Analytics 4 (and register custom dimensions), using the event parameters below.

## Task
Add consistent click tracking to promotional elements, and build a dashboard that shows CTR by placement.

## Implemented Data Specifications

### 1. GA4 Event Payload
- **Event Name:** `promo_click`
- **Parameters:**
  - `placement` (String): Identifier of the clicked element / UI location.
  - `link_url` (String): The target destination URL of the clicked element.

### 2. Configured Placements (`placement` values)

| Placement Value | UI Location / Component | Source Template / Partial |
| :--- | :--- | :--- |
| `hero-cta` | Homepage hero primary & secondary action buttons ("Start your journey", "Learn the essentials") | `_layouts/home.html` |
| `hero-pathways` | Homepage hero pathway quick-filter pills | `_layouts/home.html` |
| `pathway-card` | Core guide cards (both article and hub links) on homepage & post cornerstone section | `_layouts/home.html`, `_layouts/post.html` |
| `footer-core-guides` | Footer navigation column 1 links for Core Guides | `_includes/footer-nav.html` |
| `drill-pack-banner` | Downloadable drill pack feature banner at post bottoms | `_includes/drill-pack-feature.html` |
| `drill-pack-callout` | Post inline callout cards for the drill pack (`type="drill-pack"`) | `_includes/callout.html` |
| `drill-pack-footer` | Persistent drill pack banner above the site footer | `_includes/footer.html` |
| `drill-pack-service-card` | Homepage services grid card link for the drill pack | `_layouts/home.html` |
| `drill-pack-checkout` | Direct Lemon Squeezy buy/checkout buttons on the drill pack sales page | `lawn-bowls-downloadable-drill-pack.md` |
| `promo-strip` | Top site promotional announcement banner CTA | `_includes/promo-strip.html` |
| `inline-callout` | Other inline callout cards (e.g., buyer's guide callouts in reviews) | `_includes/callout.html` |
| `home-services` | Other service cards in homepage grid ("Browse reviews", "Read guides") | `_layouts/home.html` |
| `home-cta` | Bottom homepage conversion section CTA buttons ("Start here", "Talk to us") | `_layouts/home.html` |

### 3. Implementation Files
- **Tracking Listener:** `assets/js/analytics-events.js` (delegated listener on `document` checking `[data-track]`, safe `typeof window.gtag === 'function'` guard).
- **Script Inclusion:** `_includes/scripts.html` (loaded with `defer`).
- **Privacy Policy:** `privacy.html` (§3.3 updated to cover pseudonymous engagement and promotional click event tracking).

---

## Instructions for Building the GA4 Dashboard

### Step 1: Register Custom Dimensions in GA4
Before custom event parameters can be used in standard reports and explorations, register them in your GA4 property:
1. Navigate to **Admin** (gear icon at bottom left) &rarr; **Data display** &rarr; **Custom definitions**.
2. Click **Create custom dimension**:
   - **Dimension name:** `Placement`
   - **Scope:** `Event`
   - **Description:** `Promotional placement / CTA location identifier`
   - **Event parameter:** `placement`
3. Click **Create custom dimension** again:
   - **Dimension name:** `Link URL`
   - **Scope:** `Event`
   - **Description:** `Target destination URL of promotional link`
   - **Event parameter:** `link_url`

### Step 2: Test in GA4 DebugView
1. Open the site in Chrome with the **Google Analytics Debugger** extension enabled (or append `?_dbg=1` / use Tag Assistant).
2. Click any tracked button or link (e.g. Hero CTA, Promo strip, or Drill Pack footer).
3. In GA4, go to **Admin** &rarr; **Data display** &rarr; **DebugView**.
4. Confirm `promo_click` events appear with `placement` and `link_url` parameters populated.

### Step 3: Create Exploration (Dashboard / CTR by Placement)
1. Go to **Explore** &rarr; **Blank Exploration**.
2. Under **Variables**:
   - **Dimensions:** Import `Event name`, `Placement`, and `Page path and screen class` (or `Page location`).
   - **Metrics:** Import `Event count`, `Total users`, and `Sessions`.
3. Under **Tab Settings**:
   - Set **Rows** to `Placement`.
   - Set **Values** to `Event count` (and `Total users`).
   - Add a **Filter**: `Event name` exactly matches `promo_click`.
4. (Optional CTR calculation):
   - To compute click-through rates relative to views, compare `promo_click` counts for a placement against `page_view` counts for the corresponding host pages (e.g. homepage views for `hero-cta`).

---

## Completion criteria
- [x] Click tracking attributes (`data-track`) added across all promotional and pathway elements.
- [x] Delegated event listener created in `assets/js/analytics-events.js` and loaded in `_includes/scripts.html`.
- [x] Privacy policy updated to cover interaction and promotional analytics events.
- [x] `bundle exec jekyll build` completes without errors.
- [ ] User action: Click events verified in GA4 DebugView.
- [ ] User action: User has built a GA4 report showing clicks and CTR by placement.
