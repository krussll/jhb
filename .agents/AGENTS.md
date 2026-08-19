# Project Guidelines & Codebase Context (`AGENTS.md`)

This directory contains key documentation and architectural context for AI agents and developers working on the **Clean Blog Jekyll** project (`jhb`).

---

## 1. Project Overview & Tech Stack

- **Project Name**: Clean Blog Jekyll (`startbootstrap-clean-blog-jekyll` v4.0.12)
- **Description**: A stylish, responsive Medium-inspired personal blog theme built with Jekyll and Bootstrap.
- **Static Site Generator**: [Jekyll](https://jekyllrb.com/) (~> 4.0) using Ruby & Liquid Templating Engine.
- **Frontend Framework**: [Bootstrap 4.6.0](https://getbootstrap.com/) & jQuery 3.6.0.
- **Styling Architecture**: Sass / SCSS (`assets/main.scss`, `_sass/styles.scss`, `assets/vendor/startbootstrap-clean-blog/scss/`).
- **Icons & Typography**:
  - FontAwesome 5.15.3 (SVG/JS via CDN) & FontAwesome 4.7.0.
  - Headings: `Open Sans` (Google Fonts).
  - Body: `Lora` (Google Fonts serif).
- **Form Integration**: AJAX contact form validated via `jqBootstrapValidation.js` and submitted to [Formspree](https://formspree.io/).
- **Plugins**: `jekyll-feed`, `jekyll-paginate`, `jekyll-sitemap`.

---

## 2. Directory Structure

```
├── .agents/                    # Workspace agent guidelines & context documentation
│   ├── AGENTS.md               # Primary agent entry point and guidelines
│   ├── codebase_structure.md   # Architectural breakdown of layouts, includes, and config
│   ├── styles_and_ui.md        # Sass, design tokens, typography, and UI component details
│   └── content_and_posts.md    # Post schema, frontmatter spec, and page templates
├── _config.yml                 # Core Jekyll site configuration & plugins
├── Gemfile                     # Ruby gems definition
├── package.json                # Node dependencies (Bootstrap, FontAwesome, jQuery)
├── _layouts/                   # Jekyll page & post wrapper templates
│   ├── default.html            # Core HTML shell (head, navbar, footer, scripts)
│   ├── home.html               # Homepage layout with masthead & recent 5 posts
│   ├── page.html               # Standard content page layout (About, Contact, etc.)
│   └── post.html               # Single blog post layout with reading time & post nav
├── _includes/                  # Reusable Liquid partials
│   ├── head.html               # Meta tags, fonts, stylesheets, RSS feeds
│   ├── navbar.html             # Top responsive navigation bar
│   ├── footer.html             # Footer with stacked social icons & copyright
│   ├── scripts.html            # Script tags & contact form submission handler
│   ├── read_time.html          # Estimated reading time liquid snippet (~200 wpm)
│   └── google-analytics.html   # Google Analytics snippet
├── _posts/                     # Blog post entries (Markdown/HTML format)
├── posts/                      # Paginated post listing directory (`index.html`)
├── _sass/                      # Jekyll Sass inclusion root (`styles.scss`)
├── assets/                     # Transpiled assets, custom SCSS, scripts & vendor code
│   ├── main.scss               # Main SCSS entry point with Jekyll frontmatter
│   ├── scripts.js              # Custom site JS
│   └── vendor/                 # Vendor SCSS & JS (StartBootstrap Clean Blog theme)
├── img/                        # Background hero banner images and post media
├── index.html                  # Homepage entry point (uses `home` layout)
├── about.html                  # About Me page (uses `page` layout)
└── contact.html                # Contact Me page (uses `page` layout + Formspree form)
```

---

## 3. Key Conventions & Guidelines for Future Work

### 3.1 Layout & Component Conventions
- **Root Layout Shell**: All page layouts inherit from `default.html` (`layout: default`).
- **Container Boundaries**: Main content blocks use Bootstrap container rows with `col-lg-8 col-md-10 mx-auto` to maintain centered, readable column widths.
- **Masthead Headers**: Header banners rely on `page.background` frontmatter variable. If omitted, default masthead styles apply.

### 3.2 Front Matter Schema

#### Page Schema (`layout: page`)
```yaml
---
layout: page
title: "Page Title"
description: "Brief page summary/subtitle"
background: "/img/bg-about.jpg"
---
```

#### Post Schema (`layout: post`)
```yaml
---
layout: post
title: "Post Title"
subtitle: "Post subtitle or summary"
date: YYYY-MM-DD HH:MM:SS
author: "Author Name" # Optional, defaults to site.author in _config.yml
background: "/img/post-bg.jpg" # Optional hero background image
---
```

### 3.3 Style & UI Design Rules
- Primary brand color is Teal (`#0085A1`).
- Custom styles should be added in `_sass/` or integrated via `assets/vendor/startbootstrap-clean-blog/scss/`.
- Maintain clean contrast over image banners using `.overlay` dark backdrop filters (`rgba(33, 37, 41, 0.5)`).

---

## 4. Development & Build Commands

- **Install Dependencies**: `bundle install`
- **Serve Locally**: `jekyll serve` (or `bundle exec jekyll serve`) — test locally at [http://127.0.0.1:4000/jhb/](http://127.0.0.1:4000/jhb/)
- **Build Production**: `bundle exec jekyll build`
