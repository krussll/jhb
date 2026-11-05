# Jack High Bowls Brand Colours & Design Tokens

This document is the definitive brand colour and design token reference for agents, designers, and developers working on the **Jack High Bowls** (`jhb`) codebase. All new pages, components, layouts, and SCSS partials must strictly adhere to these specifications.

---

## 1. Core Brand Palette

The Jack High Bowls visual identity is built upon four foundational colours:

| Colour Name | Hex Code | RGB | HSL | Primary Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **Deep Green** | `#0F3D1F` | `rgb(15, 61, 31)` | `hsl(141, 61%, 15%)` | Primary brand accent, primary CTA buttons, hero banner gradients, headers, key borders |
| **Warm Gold** | `#C89B3C` | `rgb(200, 155, 60)` | `hsl(41, 56%, 51%)` | Secondary accent, badges, highlight borders, active indicators, focus rings, CTA accents |
| **Neutral Light (Cream)** | `#F5F2EB` | `rgb(245, 242, 235)` | `hsl(42, 33%, 94%)` | Card backgrounds, callout containers, soft surface fills, light text on dark backgrounds |
| **Dark Charcoal** | `#222222` | `rgb(34, 34, 34)` | `hsl(0, 0%, 13%)` | Primary body typography, high-contrast headings, announcement strip background, footer |

---

## 2. Colour Profiles & Semantic Usage

### 2.1 Deep Green (`#0F3D1F`)
- **Role**: Primary Brand Anchor.
- **Where to use**:
  - Primary call-to-action buttons (`.btn-success`, custom CTAs).
  - Top mastheads, hero gradients, and feature headers.
  - Distinctive left callout borders (`border-left: 4px solid #0F3D1F`).
  - Active navigation indicators and section titles.
- **Pairing & Text Contrast**:
  - Always pair with **Neutral Light (`#F5F2EB`)** or **Pure White (`#FFFFFF`)** for text.
  - Contrast ratio against `#F5F2EB`: **10.4:1** (Exceeds WCAG AAA requirement).
- **Hover / Active State**:
  - Hover: `darken(#0F3D1F, 7.5%)` / `#0A2B15`
  - Active: `darken(#0F3D1F, 12%)` / `#061C0D`

### 2.2 Warm Gold (`#C89B3C`)
- **Role**: Secondary Accent & Highlighting.
- **Where to use**:
  - Accent pills, category tags, and feature badges (e.g. `Structured Practice System`, `Free Download`).
  - Secondary action buttons and highlight CTAs.
  - Callout box accent borders (`border-left: 4px solid #C89B3C`).
  - Focus outlines on dark backgrounds (`outline: 3px solid #C89B3C`).
  - Star ratings, trophy/award icons, and special announcement highlights.
- **Pairing & Text Contrast**:
  - **IMPORTANT**: Never use Warm Gold as body text or small text on white or cream backgrounds (contrast is only ~1.8:1, failing accessibility).
  - When Warm Gold is used as a background fill, set text color to **Dark Charcoal (`#222222`)** or **Deep Green (`#0F3D1F`)**.
  - Contrast ratio of `#222222` on `#C89B3C`: **5.6:1** (Passes WCAG AA for all text).
- **Hover / Active State**:
  - Hover: `lighten(#C89B3C, 7%)` / `#D4AB54` or `darken(#C89B3C, 5%)` / `#BA8D2E`

### 2.3 Neutral Light / Cream (`#F5F2EB`)
- **Role**: Warm Surface & Card Background.
- **Where to use**:
  - Background fill for feature cards, AI prompt tool builder card, drill cards, and review containers.
  - Background for quote blocks and callout panels.
  - Foreground text color when overlaid on Deep Green (`#0F3D1F`) or Dark Charcoal (`#222222`).
- **Pairing & Text Contrast**:
  - Dark Charcoal (`#222222`) text on `#F5F2EB`: **13.8:1** (Exceeds WCAG AAA).
  - Deep Green (`#0F3D1F`) text/links on `#F5F2EB`: **10.4:1** (Exceeds WCAG AAA).

### 2.4 Dark Charcoal (`#222222`)
- **Role**: High-Legibility Typography & Neutral Base.
- **Where to use**:
  - Site body text, paragraphs, and list items.
  - Article headings and card titles.
  - Background for the top persistent announcement strip (`.promo-strip`).
  - Neutral dark elements and icon buttons.
- **Pairing & Text Contrast**:
  - Provides maximum contrast and readability across `#FFFFFF` and `#F5F2EB`.

---

## 3. Secondary & Utility Shades

These secondary tints and functional values support the primary four:

| Shade Name | Value / Definition | Purpose |
| :--- | :--- | :--- |
| **Forest Night** | `#092613` | Dark end-stop in hero linear/radial gradients |
| **Mid Forest** | `#14562B` / `#17522C` | Mid-gradient transition tones for depth |
| **Gold Highlight** | `#D8A64E` | Gradient secondary stop for warm gold badges/buttons |
| **Accessible Muted Text** | `#595959` | Meta dates, author lines, subtitles (meets WCAG AA 4.5:1 on white) |
| **Subtle Green Border** | `rgba(15, 61, 31, 0.12)` - `rgba(15, 61, 31, 0.16)` | Card outlines, dividers, input borders |
| **Subtle Gold Border** | `rgba(200, 155, 60, 0.45)` | Announcement strip bottom border, highlight card borders |
| **Hero Image Overlay** | `rgba(33, 37, 41, 0.5)` | Dark backdrop layer over hero photography to ensure text contrast |
| **Pure White** | `#FFFFFF` | Core page body background |

---

## 4. Accessibility & Contrast Compliance Matrix

All UI components must meet or exceed **WCAG 2.1 AA** standards (4.5:1 for normal text, 3:1 for large text / UI controls).

| Foreground | Background | Contrast Ratio | WCAG 2.1 Rating | Permitted Usage |
| :--- | :--- | :--- | :--- | :--- |
| `#F5F2EB` (Cream) | `#0F3D1F` (Green) | **10.4:1** | **AAA** (Pass) | Buttons, badges, hero text, navigation |
| `#FFFFFF` (White) | `#0F3D1F` (Green) | **11.1:1** | **AAA** (Pass) | Hero headings, button labels |
| `#0F3D1F` (Green) | `#F5F2EB` (Cream) | **10.4:1** | **AAA** (Pass) | Text links, card headings, icons |
| `#222222` (Charcoal) | `#F5F2EB` (Cream) | **13.8:1** | **AAA** (Pass) | Body copy inside cards, prompt builder |
| `#222222` (Charcoal) | `#C89B3C` (Gold) | **5.6:1** | **AA** (Pass) | Badge text, button text on gold CTA |
| `#0F3D1F` (Green) | `#C89B3C` (Gold) | **4.2:1** | **AA Large** (Pass) | Large headings / bold buttons |
| `#C89B3C` (Gold) | `#FFFFFF` (White) | **1.9:1** | **Fail** | **Do NOT use as text on white** |
| `#C89B3C` (Gold) | `#F5F2EB` (Cream) | **1.8:1** | **Fail** | **Do NOT use as text on cream** |

> [!CAUTION]
> **Never use Warm Gold (`#C89B3C`) as text on white or light cream surfaces**. Use gold exclusively for filled backgrounds (with dark charcoal text), border accents, focus outlines, or graphical icons.

---

## 5. Recommended SCSS Variables

When writing or editing SCSS in `_sass/`, use standard variable tokens:

```scss
// Brand tokens
$brand-green: #0F3D1F;
$brand-gold: #C89B3C;
$brand-cream: #F5F2EB;
$brand-charcoal: #222222;

// Derived states
$brand-green-dark: #092613;
$brand-green-hover: darken($brand-green, 7.5%);
$brand-gold-hover: lighten($brand-gold, 7%);
$brand-border-subtle: rgba(15, 61, 31, 0.14);
$brand-gold-border: rgba(200, 155, 60, 0.45);

// Accessibility text
$text-primary: #222222;
$text-muted-accessible: #595959;
```

---

## 6. Common UI Component Patterns

### 6.1 Hero Gradient
```scss
.site-hero {
  background: radial-gradient(circle at top right, rgba(200, 155, 60, 0.22), transparent 55%),
              linear-gradient(135deg, #0F3D1F 0%, #092613 100%);
  color: #F5F2EB;
}
```

### 6.2 Primary Brand Button
```scss
.btn-brand-primary {
  background-color: #0F3D1F;
  border: 1px solid #0F3D1F;
  color: #F5F2EB;
  border-radius: 999px; // Pill style
  font-weight: 700;

  &:hover, &:focus {
    background-color: darken(#0F3D1F, 7.5%);
    border-color: darken(#0F3D1F, 7.5%);
    color: #FFFFFF;
  }

  &:focus {
    outline: 3px solid #C89B3C;
    outline-offset: 2px;
  }
}
```

### 6.3 Warm Gold Accent Button / Badge
```scss
.badge-gold {
  background-color: #C89B3C;
  color: #222222;
  font-weight: 700;
  border-radius: 6px;
  padding: 0.35rem 0.65rem;
}

.btn-brand-gold {
  background-color: #C89B3C;
  border: 1px solid #C89B3C;
  color: #0F3D1F;
  font-weight: 700;

  &:hover {
    background-color: lighten(#C89B3C, 7%);
    border-color: lighten(#C89B3C, 7%);
    color: #0F3D1F;
  }
}
```

### 6.4 Callout Box / Card
```scss
.brand-callout-card {
  background-color: #F5F2EB;
  border: 1px solid rgba(15, 61, 31, 0.14);
  border-left: 4px solid #0F3D1F; // or #C89B3C for tips/drills
  border-radius: 10px;
  color: #222222;
  padding: 1.25rem 1.5rem;

  a {
    color: #0F3D1F;
    font-weight: 700;

    &:hover {
      color: darken(#0F3D1F, 10%);
      text-decoration: underline;
    }
  }
}
```

### 6.5 Announcement / Promo Strip
```scss
.promo-strip {
  background-color: #222222;
  color: #F5F2EB;
  border-bottom: 1px solid rgba(200, 155, 60, 0.45);
}
```

---

## 7. Implementation Locations in Codebase

- Root Guidelines: [`AGENTS.md`](../AGENTS.md) (Style guide section)
- Styles & UI Architecture: [`.agents/styles_and_ui.md`](styles_and_ui.md)
- Global Scss & Custom Partials:
  - Mega Menu: [`_sass/_mega-menu.scss`](../_sass/_mega-menu.scss)
  - Promo Strip: [`_sass/_promo-strip.scss`](../_sass/_promo-strip.scss)
  - AI Prompt Builder: [`_sass/_ai-prompt-builder.scss`](../_sass/_ai-prompt-builder.scss)
  - 404 Error Page: [`_sass/_404.scss`](../_sass/_404.scss)
  - Post Callouts: [`_sass/_post.scss`](../_sass/_post.scss)
  - Page Templates: [`_sass/_page.scss`](../_sass/_page.scss)

