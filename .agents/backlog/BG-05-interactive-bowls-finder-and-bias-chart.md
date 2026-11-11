# BG-05: Build Interactive Bowls Finder & Cross-Brand Bias Comparison Chart Widget

- **Source document:** `.agents/buyers-guides-serp-recovery-plan.md` (§2, §3.4 & §5 `BG-05`)
- **Owner:** 🤖 Agent (Frontend Implementation)
- **Priority:** High
- **Status:** Not started
- **Depends on:** BG-01
- **Unblocks:** BG-07

## Task
Create a client-side interactive **Bowls Finder & Cross-Brand Bias Comparison Chart** (`_includes/bowls-finder.html`, `assets/js/bowls-finder.js`, and `_sass/_bowls-finder.scss`) powered by `_data/bowls_models.yml`, and embed it on `reviews.md` (`/reviews/`) and core "Best Bowls" buyer's guides.

## Context
Ecommerce category pages rank well because they offer faceted filtering. However, no single retailer offers an objective, cross-brand bias comparison chart across Taylor, Henselite, Drakes Pride, and Aero alongside second-hand eBay price estimates.
1. **Component Markup (`_includes/bowls-finder.html`)**:
   - Render a clean, accessible filter panel with controls for:
     - **Playing Surface**: `All Surfaces`, `Indoor Carpet`, `Fast Outdoor`, `Slow/Heavy Outdoor`, `Crown Green`
     - **Team Position**: `All Positions`, `Lead`, `Second`, `Third`, `Skip`, `Singles`
     - **Bias Profile**: `All Biases`, `Narrow / Straight (1–3.5)`, `Mid-Bias (4–6)`, `Wide / Hook (6.5–10)`
     - **Small Hands / Deep Grip Friendly**: Checkbox/toggle filter
   - Render a visual **Cross-Brand Bias Spectrum (1–10)** plotting each matching bowl on a horizontal scale from Narrowest (`1.0`) to Widest (`10.0`).
   - Render matching model cards showing Brand, Model, Bias Score, Surface pills, Grip options, New RRP vs. Used eBay price range, and `"Read Review"` / `"Find Used"` action buttons.
2. **Client-Side Script (`assets/js/bowls-finder.js`)**:
   - Modular vanilla JavaScript (no jQuery dependency required) that filters the rendered model cards and updates the active count (`aria-live="polite"`) and Bias Spectrum markers in real time.
   - Format with Prettier per `AGENTS.md`.
3. **Styling (`_sass/_bowls-finder.scss`)**:
   - Adhere strictly to `.agents/brand-colours.md` and `AGENTS.md`:
     - Sharp square corners (`border-radius: 0;`) on the filter panel, inputs, cards, and buttons.
     - Rounded pills (`border-radius: 9999px;`) exclusively for filter/category pills.
     - Deep Blue (`#1F2B5F`), Warm Gold (`#C89B3C`), Neutral Light (`#f8f9fa`), and Dark Charcoal (`#222222`).
4. **Placement**:
   - Embed on `reviews.md` (`/reviews/`) above the individual reviews grid and in `_posts/2019-04-09-best-lawn-bowls-for-beginners.md` and `_posts/2020-10-29-best-straight-lawn-bowls.md`.

## Completion criteria
- [ ] `_includes/bowls-finder.html`, `assets/js/bowls-finder.js`, and `_sass/_bowls-finder.scss` created and integrated.
- [ ] Interactive filtering by Surface, Position, Bias, and Small-Hands compatibility works smoothly and updates `aria-live` status accessibly.
- [ ] Embedded on `/reviews/` and top buyer's guides with `border-radius: 0` card/control geometry.
- [ ] `bundle exec jekyll build` completes without errors.

