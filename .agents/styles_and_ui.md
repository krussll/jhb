# Styles & UI System Documentation

This document covers the styling architecture, Sass setup, design tokens, typography, color palette, responsive breakpoints, and UI component standards used across the site.

---

## 1. SCSS Pipeline & Architecture

The stylesheet pipeline is compiled by Jekyll's Sass engine into `/assets/main.css`:

```
assets/main.scss (Front matter wrapper)
    └── _sass/styles.scss
            └── assets/vendor/startbootstrap-clean-blog/scss/styles.scss
                    ├── variables/ (_colors.scss, _typography.scss)
                    ├── bootstrap/scss/bootstrap.scss (Bootstrap 4.6)
                    ├── global.scss
                    ├── components/ (_buttons.scss, _navbar.scss)
                    └── sections/ (_contact.scss, _footer.scss, _masthead.scss, _post.scss)
```

---

## 2. Color Palette & Design Tokens

> **Full Specification**: Refer to [`.agents/brand-colours.md`](brand-colours.md) for full color definitions, WCAG 2.1 contrast matrix, and UI component usage patterns.

| Token | Hex Value / CSS Definition | Purpose |
| :--- | :--- | :--- |
| **Deep Green** (`$brand-green`) | `#0F3D1F` | Primary brand accent, primary CTA buttons, hero banner gradients, headers, key borders |
| **Warm Gold** (`$brand-gold`) | `#C89B3C` | Secondary accent, badges, highlight borders, focus rings, CTA accents |
| **Neutral Light / Cream** (`$brand-cream`) | `#F5F2EB` | Card backgrounds, callout containers, soft surface fills, light text on dark backgrounds |
| **Dark Charcoal** (`$brand-charcoal`) | `#222222` | Primary body typography, high-contrast headings, announcement strip background |
| `$white` | `#ffffff` | Page background, masthead text color |
| Overlay Dark | `rgba(33, 37, 41, 0.5)` | Hero image backdrop filter for text legibility |
| Accessible Muted Text | `#595959` | Meta dates, author lines, subtitles (meets WCAG AA on white) |

---

## 3. Typography Rules

The typography system combines Google Fonts to establish clear visual contrast between headlines and long-form narrative body text:

- **Body Font (`$font-family-base`)**:
  - Font: `"Lora", serif`
  - Fallbacks: `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif`
  - Purpose: Body text, paragraph content, post articles for high readability.

- **Headings Font (`$headings-font-family`)**:
  - Font: `"Open Sans", sans-serif`
  - Weights: `300` (Light), `400` (Normal), `600` (Semi-bold), `700` (Bold), `800` (Extra Bold)
  - Purpose: Page titles, section headings, navbar branding, post titles.

---

## 4. Primary UI Components

### 4.1 Masthead Header (`.masthead`)
- Full-width hero banner element with background image overlay.
- Uses background positioning (`background-size: cover`, `background-position: center`).
- `.overlay`: Dark semi-transparent absolute positioned layer ensuring readable text contrast against dynamic hero background images.

### 4.2 Navbar (`#mainNav`)
- Fixed-top responsive Bootstrap 4 navbar (`navbar navbar-expand-lg navbar-light fixed-top`).
- Dynamic behavior: Translucent on hero section, becomes solid with shadow on scroll.
- Responsive toggle button with `fa fa-bars` icon.

### 4.3 Post Preview (`.post-preview`)
- Article preview card used on homepage and post archive listing.
- Elements:
  - `.post-title`: Bold main heading (`<h2>`).
  - `.post-subtitle`: Light secondary headline or truncated excerpt (`<h3>`).
  - `.post-meta`: Meta line displaying author name, published date, and estimated read time.

### 4.4 Form Controls & Floating Labels (`.floating-label-form-group`)
- Contact form inputs utilize floating labels.
- Styled using `.form-group.floating-label-form-group.controls`.
- Interactive validation highlights error fields with `.text-danger` and display success alerts on AJAX response.

### 4.5 Social Media Footer Icons
- FontAwesome stacked icons (`.fa-stack.fa-lg`).
- Outer element: Dark solid circle (`.fas.fa-circle.fa-stack-2x`).
- Inner element: Inverse brand icon (`.fab.fa-twitter`, `.fab.fa-github`, etc., `.fa-inverse`).
