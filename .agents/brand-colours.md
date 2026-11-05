# Jack High Bowls Brand Colours & Design Tokens

This document is the definitive brand colour and design token reference for agents, designers, and developers working on the **Jack High Bowls** (`jhb`) codebase. All new pages, components, layouts, and SCSS partials must strictly adhere to these specifications.

---

## 1. Core Brand Palette

The Jack High Bowls visual identity is built upon four foundational colours, anchored by the signature Deep Blue found on the masthead and page hero (`header.masthead.page-hero`):

| Colour Name | Hex Code | RGB | HSL | Primary Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **Deep Blue** | `#1F2B5F` | `rgb(31, 43, 95)` | `hsl(229, 51%, 25%)` | Primary brand accent, primary CTA buttons, masthead/page hero gradient base, section headers, key borders |
| **Warm Gold** | `#C89B3C` | `rgb(200, 155, 60)` | `hsl(41, 56%, 51%)` | Secondary accent, badges, highlight borders, active indicators, focus rings, CTA accents |
| **Neutral Light (Cream)** | `#f8f9fa` | `rgb(248, 249, 250)` | `hsl(210, 17%, 98%)` | Card backgrounds, callout containers, soft surface fills, light text on dark backgrounds |
| **Dark Charcoal** | `#222222` | `rgb(34, 34, 34)` | `hsl(0, 0%, 13%)` | Primary body typography, high-contrast headings, announcement strip typography, footer |

---

## 2. Colour Profiles & Semantic Usage

### 2.1 Deep Blue (`#1F2B5F`)
- **Role**: Primary Brand Anchor (as used on `.masthead.page-hero` and `.home-hero`).
- **Where to use**:
  - Primary call-to-action buttons (`.btn-primary`, `.btn-brand-primary`).
  - Top mastheads, hero gradients, and feature headers (`$home-primary` / `$site-hero-gradient`).
  - Distinctive left callout borders (`border-left: 4px solid #1F2B5F`).
  - Active navigation indicators, icons, and section titles.
- **Pairing & Text Contrast**:
  - Always pair with **Neutral Light (`#f8f9fa`)** or **Pure White (`#FFFFFF`)** for text.
  - Contrast ratio against `#FFFFFF`: **13.0:1** (Exceeds WCAG AAA requirement).
  - Contrast ratio against `#f8f9fa`: **12.6:1** (Exceeds WCAG AAA requirement).
- **Hover / Active State**:
  - Hover: `darken(#1F2B5F, 7.5%)` / `#161F44`
  - Active: `darken(#1F2B5F, 12%)` / `#101734`

### 2.2 Warm Gold (`#C89B3C`)
- **Role**: Secondary Accent & Highlighting.
- **Where to use**:
  - Accent pills, category tags, and feature badges (e.g. `Structured Practice System`, `Free Download`).
  - Secondary action buttons and highlight CTAs.
  - Callout box accent borders (`border-left: 4px solid #C89B3C`).
  - Focus outlines on dark backgrounds (`outline: 3px solid #C89B3C`).
  - Star ratings, trophy/award icons, and special announcement highlights.
- **Pairing & Text Contrast**:
  - **IMPORTANT**: Never use Warm Gold as body text or small text on white or light surfaces (contrast is only ~2.4:1, failing accessibility).
  - When Warm Gold is used as a background fill, set text color to **Dark Charcoal (`#222222`)** or **Deep Blue (`#1F2B5F`)**.
  - Contrast ratio of `#222222` on `#C89B3C`: **5.6:1** (Passes WCAG AA for all text).
- **Hover / Active State**:
  - Hover: `lighten(#C89B3C, 7%)` / `#D4AB54` or `darken(#C89B3C, 5%)` / `#BA8D2E`

### 2.3 Neutral Light / Cream (`#f8f9fa`)
- **Role**: Clean Light Surface & Card Background.
- **Where to use**:
  - Background fill for feature cards, AI prompt tool builder card, drill cards, and review containers.
  - Background for quote blocks and callout panels.
  - Foreground text color when overlaid on Deep Blue (`#1F2B5F`) or Dark Charcoal (`#222222`).
- **Pairing & Text Contrast**:
  - Dark Charcoal (`#222222`) text on `#f8f9fa`: **15.1:1** (Exceeds WCAG AAA).
  - Deep Blue (`#1F2B5F`) text/links on `#f8f9fa`: **12.6:1** (Exceeds WCAG AAA).

### 2.4 Dark Charcoal (`#222222`)
- **Role**: High-Legibility Typography & Neutral Base.
- **Where to use**:
  - Site body text, paragraphs, and list items.
  - Article headings and card titles.
  - Typography and icon buttons for the top persistent announcement strip (`.promo-strip`).
  - Neutral dark elements and icon buttons.
- **Pairing & Text Contrast**:
  - Provides maximum contrast and readability across `#FFFFFF` and `#f8f9fa`.

---

## 3. Secondary & Utility Shades

These secondary tints and functional values support the primary four:

| Shade Name | Value / Definition | Purpose |
| :--- | :--- | :--- |
| **Navy Midnight** | `#19204B` | Dark gradient end-stop in `masthead.page-hero` and `home-hero` linear gradients |
| **Royal Blue Accent** | `#1D4ED8` | Radial gradient lighting accent and interactive hover highlights (`$home-secondary`) |
| **Gold Highlight** | `#D8A64E` | Gradient secondary stop for warm gold badges/buttons |
| **Accessible Muted Text** | `#595959` | Meta dates, author lines, subtitles (meets WCAG AA 4.5:1 on white) |
| **Subtle Blue Border** | `rgba(31, 43, 95, 0.12)` - `rgba(31, 43, 95, 0.16)` | Card outlines, dividers, input borders |
| **Subtle Gold Border** | `rgba(200, 155, 60, 0.45)` | Announcement strip bottom border, highlight card borders |
| **Hero Image Overlay** | `rgba(33, 37, 41, 0.5)` | Dark backdrop layer over hero photography to ensure text contrast |
| **Pure White** | `#FFFFFF` | Core page body background |

---

## 4. Accessibility & Contrast Compliance Matrix

All UI components must meet or exceed **WCAG 2.1 AA** standards (4.5:1 for normal text, 3:1 for large text / UI controls).

| Foreground | Background | Contrast Ratio | WCAG 2.1 Rating | Permitted Usage |
| :--- | :--- | :--- | :--- | :--- |
| `#f8f9fa` (Neutral Light) | `#1F2B5F` (Blue) | **12.6:1** | **AAA** (Pass) | Buttons, badges, hero text, navigation |
| `#FFFFFF` (White) | `#1F2B5F` (Blue) | **13.0:1** | **AAA** (Pass) | Hero headings, button labels |
| `#1F2B5F` (Blue) | `#f8f9fa` (Neutral Light) | **12.6:1** | **AAA** (Pass) | Text links, card headings, icons |
| `#1F2B5F` (Blue) | `#FFFFFF` (White) | **13.0:1** | **AAA** (Pass) | Text links, section titles on white |
| `#222222` (Charcoal) | `#f8f9fa` (Neutral Light) | **15.1:1** | **AAA** (Pass) | Body copy inside cards, prompt builder |
| `#222222` (Charcoal) | `#C89B3C` (Gold) | **5.6:1** | **AA** (Pass) | Badge text, button text on gold CTA |
| `#1F2B5F` (Blue) | `#C89B3C` (Gold) | **4.2:1** | **AA Large** (Pass) | Large headings / bold buttons |
| `#C89B3C` (Gold) | `#FFFFFF` (White) | **1.9:1** | **Fail** | **Do NOT use as text on white** |
| `#C89B3C` (Gold) | `#f8f9fa` (Neutral Light) | **2.4:1** | **Fail** | **Do NOT use as text on light surfaces** |

> [!CAUTION]
> **Never use Warm Gold (`#C89B3C`) as text on white or light surfaces (`#f8f9fa`)**. Use gold exclusively for filled backgrounds (with dark charcoal text), border accents, focus outlines, or graphical icons.

---

## 5. Recommended SCSS Variables

When writing or editing SCSS in `_sass/`, use standard variable tokens matching the hero masthead system:

```scss
// Brand tokens
$brand-blue: #1F2B5F;
$brand-gold: #C89B3C;
$brand-cream: #f8f9fa;
$brand-charcoal: #222222;

// Derived hero masthead gradient stops
$brand-blue-dark: #19204B;
$brand-blue-accent: #1D4ED8;
$brand-blue-hover: darken($brand-blue, 7.5%);
$brand-gold-hover: lighten($brand-gold, 7%);
$brand-border-subtle: rgba(31, 43, 95, 0.14);
$brand-gold-border: rgba(200, 155, 60, 0.45);

// Accessibility text
$text-primary: #222222;
$text-muted-accessible: #595959;
```

---

## 6. Common UI Component Patterns

### 6.1 Hero Gradient (Masthead Page-Hero Standard)
```scss
// Standard masthead & page-hero gradient ($site-hero-gradient)
.page-hero,
header.masthead.page-hero {
  background: radial-gradient(circle at top right, rgba(29, 78, 216, 0.25), transparent 60%),
              linear-gradient(135deg, #1F2B5F 0%, #19204B 100%);
  color: #FFFFFF;
}
```

### 6.2 Primary Brand Button
```scss
.btn-brand-primary {
  background-color: #1F2B5F;
  border: 1px solid #1F2B5F;
  color: #f8f9fa;
  border-radius: 999px; // Pill style
  font-weight: 700;

  &:hover, &:focus {
    background-color: darken(#1F2B5F, 7.5%);
    border-color: darken(#1F2B5F, 7.5%);
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
  color: #1F2B5F;
  font-weight: 700;

  &:hover {
    background-color: lighten(#C89B3C, 7%);
    border-color: lighten(#C89B3C, 7%);
    color: #1F2B5F;
  }
}
```

### 6.4 Callout Box / Card
```scss
.brand-callout-card {
  background-color: #f8f9fa;
  border: 1px solid rgba(31, 43, 95, 0.14);
  border-left: 4px solid #1F2B5F; // or #C89B3C for tips/drills
  border-radius: 10px;
  color: #222222;
  padding: 1.25rem 1.5rem;

  a {
    color: #1F2B5F;
    font-weight: 700;

    &:hover {
      color: darken(#1F2B5F, 10%);
      text-decoration: underline;
    }
  }
}
```

### 6.5 Announcement / Promo Strip
```scss
.promo-strip {
  background-color: #f0fa81;
  color: #222222;
  border-bottom: 1px solid rgba(34, 34, 34, 0.15);
}
```

---

## 7. Implementation Locations in Codebase

- Root Guidelines: [`AGENTS.md`](../AGENTS.md) (Style guide section)
- Styles & UI Architecture: [`.agents/styles_and_ui.md`](styles_and_ui.md)
- Hero System: [`_sass/_home.scss`](../_sass/_home.scss) and [`_sass/_page.scss`](../_sass/_page.scss)
- Global Scss & Custom Partials:
  - Mega Menu: [`_sass/_mega-menu.scss`](../_sass/_mega-menu.scss)
  - Promo Strip: [`_sass/_promo-strip.scss`](../_sass/_promo-strip.scss)
  - AI Prompt Builder: [`_sass/_ai-prompt-builder.scss`](../_sass/_ai-prompt-builder.scss)
  - 404 Error Page: [`_sass/_404.scss`](../_sass/_404.scss)
  - Post Callouts: [`_sass/_post.scss`](../_sass/_post.scss)
