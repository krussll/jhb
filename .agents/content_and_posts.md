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
