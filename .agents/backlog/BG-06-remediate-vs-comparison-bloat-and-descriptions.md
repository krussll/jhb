# BG-06: Remediate 175 "X vs Y" Comparison Posts (Meta Descriptions, De-Cannibalized Titles & Automated Spec Matrix)

- **Source document:** `.agents/buyers-guides-serp-recovery-plan.md` (§1 Issue 5, §3.5 & §5 `BG-06`)
- **Owner:** 🤖 Agent (Content Curator)
- **Priority:** Medium
- **Status:** Not started
- **Depends on:** BG-01
- **Unblocks:** BG-07

## Task
Eliminate sitewide thin-content drag and `"Best"` keyword cannibalization across the ~175 head-to-head comparison posts (`_posts/*-vs-*-which-is-best.md`) by populating all empty meta descriptions, adding differentiated `seo_title` front matter, and auto-injecting a data-driven side-by-side specification table from `_data/bowls_models.yml`.

## Context
1. **Audit Findings**:
   - ~165 of the 175 `_posts/2023-03-*-vs-*-which-is-best.md` posts have `description: ""` (empty meta description).
   - Every post appends `| Which is Best?` to the title, competing with JHB's core `"Best X for Y"` guides while containing only generic text paragraphs and zero quantitative spec tables.
2. **Automated Side-by-Side Comparison Matrix (`_includes/vs-comparison-matrix.html`)**:
   - Create `_includes/vs-comparison-matrix.html` and include it automatically in `_layouts/post.html` whenever `page.title contains ' vs '` (or when `page.model_a` and `page.model_b` are matched from `_data/bowls_models.yml`).
   - Display a structured, square-corner (`border-radius: 0`) comparison table comparing Model A and Model B across:
     - **Brand**
     - **Bias Score (1–10) & Trajectory Profile**
     - **Best Surfaces**
     - **Ideal Team Positions**
     - **Available Grips**
     - **Sizes Available**
     - **New RRP vs. Typical Second-Hand Price (GBP)**
     - **Direct Links to Full Individual Reviews** (`model_a.review_url` & `model_b.review_url`)
3. **Front Matter Remediation across `_posts/*-vs-*.md`**:
   - Populate every empty `description: ""` with a unique, informative 140–160 character meta description summarizing the bias, surface suitability, and price difference between the two models.
   - Add `seo_title` (e.g., `"Taylor Ace vs Henselite Tiger Pro: Bias, Grip & Price Comparison"`) so head-to-head pages rank for `"X vs Y"` searches without cannibalizing `"Best Bowls"` roundup intent.
   - Populate `model_a` and `model_b` slugs in front matter so `_includes/vs-comparison-matrix.html` binds cleanly to `_data/bowls_models.yml`.

## Completion criteria
- [ ] Zero `_posts/*-vs-*.md` files have an empty `description: ""`.
- [ ] All `_posts/*-vs-*.md` files include `model_a`, `model_b`, and a non-cannibalizing `seo_title`.
- [ ] `_includes/vs-comparison-matrix.html` renders a side-by-side spec, bias, and New/Used price comparison table on every `vs` post via `_layouts/post.html`.
- [ ] `bundle exec jekyll build` completes without errors.

