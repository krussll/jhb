# Codebase Architecture & Structure Documentation

This document provides a technical dive into the architecture, Liquid templating system, site configuration, and file structure of the **Clean Blog Jekyll** project.

---

## 1. Core Configuration (`_config.yml`)

The `_config.yml` file defines global metadata, social handles, build parameters, and active plugins:

| Key | Description / Value |
| :--- | :--- |
| `title` | Site header title (`Clean Blog`) |
| `description` | Site tagline (`A Blog Theme by Start Bootstrap`) |
| `author` | Default post & site author (`Start Bootstrap`) |
| `baseurl` | Subpath base URL (`"/startbootstrap-clean-blog-jekyll"`) |
| `url` | Production site base URL (`"https://startbootstrap.github.io"`) |
| `markdown` | Markdown rendering engine (`kramdown`) |
| `paginate` | Number of posts per page on `/posts/` (`5`) |
| `paginate_path` | Pagination URI template (`"/posts/page:num/"`) |
| `plugins` | `jekyll-feed`, `jekyll-paginate`, `jekyll-sitemap` |

---

## 2. Layouts Pipeline (`_layouts/`)

Jekyll processes templates hierarchically through the frontmatter `layout` property:

```
[default.html]
   ├── [home.html]    --> Used by index.html (Homepage)
   ├── [page.html]    --> Used by about.html, contact.html, posts/index.html
   └── [post.html]    --> Used by blog entries in _posts/
```

### Layout Breakdown

1. **`default.html`**:
   - Acts as the top-level HTML document shell.
   - Includes `head.html`, `navbar.html`, `{{ content }}`, `footer.html`, `scripts.html`, and `google-analytics.html`.

2. **`home.html`**:
   - Header: Masthead banner rendering `site.title` and `site.description`.
   - Content: Custom HTML/markdown from `index.html`.
   - Post Stream: Iterates through the 5 most recent posts (`{% for post in site.posts limit:5 %}`).
   - Navigation: Renders post title, subtitle (or truncated excerpt), author, date, reading time, and a "View All Posts" button linking to `/posts`.

3. **`page.html`**:
   - Header: Banner rendering `page.title` and `page.description` against `page.background`.
   - Body: Wraps `{{ content }}` in `.container > .row > .col-lg-8.col-md-10.mx-auto`.

4. **`post.html`**:
   - Header: Masthead with post title, subtitle, author metadata, date, and estimated reading time.
   - Body: Renders `{{ content }}` with horizontal rule divider.
   - Post Navigation: Previous/Next post pagination buttons using `page.previous` and `page.next`.

---

## 3. Includes & Components (`_includes/`)

Reusable components engineered with Liquid templating:

- **`head.html`**: Sets viewport metadata, dynamic `<title>`, Google Fonts (`Lora` & `Open Sans`), FontAwesome 5.15.3 CDN JS, main SCSS compiled stylesheet (`/assets/main.css`), canonical link, and RSS feed (`/feed.xml`).
- **`navbar.html`**: Fixed top navbar (`#mainNav`) with responsive Bootstrap collapsible hamburger menu. Links are dynamically built using `relative_url` filter (`/`, `/about`, `/posts`, `/contact`).
- **`footer.html`**: Renders stacked circle social media icons based on conditional site variables (`site.twitter_username`, `site.github_username`, `site.facebook_username`, `site.linkedin_username`, `site.instagram_username`, `site.email`). Automatically updates the copyright year using `{{ 'now' | date: "%Y" }}`.
- **`read_time.html`**: Liquid utility snippet that counts words in `content` and calculates estimated reading time (assuming 200 words per minute).
- **`scripts.html`**: Loads jQuery 3.5.1, Bootstrap 4.6.0 bundle, theme JS, and contains conditional Formspree AJAX validation & handling script when `page.url contains 'contact'`.

---

## 4. Dependencies & Asset Management

- **Gemfile**:
  - `gem "jekyll", "~> 4.0"`
  - `gem "jekyll-feed"` (generates `/feed.xml`)
  - `gem "jekyll-paginate"` (handles paginated archive pages)
  - `gem "jekyll-sitemap"` (generates XML sitemap)
  - `gem "jekyll-theme-clean-blog"` (theme gem packaging)

- **package.json**:
  - `bootstrap`: `4.6.0`
  - `font-awesome`: `4.7.0`
  - `jquery`: `3.6.0`
  - `startbootstrap-clean-blog`: `5.1.0`
  - `browser-sync`: `2.26.14` (for live reloading local dev server)
