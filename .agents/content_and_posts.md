# Content & Post Management Documentation

This document describes how blog posts, static pages, Liquid helpers, and form handling operate within the codebase.

---

## 1. Creating Blog Posts

All blog posts are saved under the `_posts/` directory following the mandatory Jekyll file naming convention:

```
_posts/YYYY-MM-DD-title-slug.html (or .md)
```

Example filename: `_posts/2020-01-31-man-must-explore.html`

### Post Front Matter Requirements

```yaml
---
layout: post
title: "Man Must Explore"
subtitle: "Problems are created by man, defense against them is up to man."
date: 2020-01-31 12:00:00
author: "Start Bootstrap"     # Optional: defaults to site.author
background: "/img/bg-post.jpg" # Optional: header background image path
---
```

### SEO Title Tag (`seo_title`)

`_includes/head.html` builds the `<title>`, `og:title` and `twitter:title` from `seo_title` (optional) or `title`, then adds ` - Jack High Bowls` **only if the full string stays under 70 characters**. If it would go over, the brand suffix is left off. This follows Bing Webmaster Tools' "Title too long" guidance.

- Add `seo_title` straight after `title` whenever `title` (the on-page H1) is longer than about 51 characters. It changes only the title tag; the H1, listings and schema headline keep using `title`.
- Keep it unique, front-load the main keyword, and drop filler such as "| A Complete Guide" or "| A Helpful Illustrated Guide".
- 51 characters or fewer keeps the brand suffix (51 + 18 = 69).

```yaml
title: "Can You Hit The Jack In Lawn Bowls? | A Complete Guide To What Happens When The Jack Is Hit"
seo_title: "Can You Hit the Jack in Lawn Bowls? Rules Explained"
```

---

## 2. Blog Post Features & Utilities

### 2.1 Reading Time Calculation
Each post layout includes `_includes/read_time.html` which automatically computes reading time:

```liquid
{% include read_time.html content=post.content %}
```

- Words are calculated via `content | number_of_words`.
- Reading speed is assumed at **200 words per minute**.
- Outputs: `1 min read` or `N mins read`.

### 2.2 Post Pagination & Navigation
- **Homepage (`index.html`)**: Shows the 5 most recent posts via `{% for post in site.posts limit : 5 %}`.
- **Archive Page (`posts/index.html`)**: Uses `jekyll-paginate` plugin (`paginator.posts`), listing 5 posts per page with `Newer Posts` and `Older Posts` navigation buttons.
- **Post Footer**: `_layouts/post.html` renders `Previous Post` (`page.previous`) and `Next Post` (`page.next`) buttons linking to adjacent chronological posts.

---

## 3. Creating Static Pages

Static pages live in the root directory (e.g. `about.html`, `contact.html`).

### Page Front Matter Example

```yaml
---
layout: page
title: "About Me"
description: "This is what I do."
background: "/img/bg-about.jpg"
---
```

---

## 4. Contact Form & Formspree Integration

`contact.html` contains an interactive AJAX contact form:

### 4.1 HTML Structure
- Form ID: `#contactForm`
- Submit Button ID: `#sendMessageButton`
- Success/Failure Message Container: `#success`
- Inputs: Name (`#name`), Email (`#email`), Phone (`#phone`), Message (`#message`).

### 4.2 Form Handling (`_includes/scripts.html`)
- Utilizes `jqBootstrapValidation` for inline client-side validation.
- Submits an AJAX `POST` request to `//formspree.io/{{ site.email }}`.
- Displays responsive Bootstrap alert feedback (`.alert-success` or `.alert-danger`).
- Disables the submit button during submission to prevent duplicate sends.

> [!NOTE]
> Ensure the `email` variable in `_config.yml` is updated with a valid target email address verified on Formspree.
