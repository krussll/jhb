# Overview
This repository contains the source for the JHB lawn bowls information site, a Jekyll-based static website that publishes comparisons, reviews, and guides for lawn bowls equipment and technique.

# Agents
- **Content Curator Agent**: Focuses on maintaining accurate, well-researched written content and metadata for posts and pages.
- **Frontend Implementation Agent**: Handles HTML, SCSS, Liquid templates, and asset pipeline tasks for the Jekyll site.
- **Quality Assurance Agent**: Runs automated and manual checks to ensure accessibility, performance, and editorial standards are met.

# Collaboration rules
- Share progress regularly through concise commit messages and pull request summaries.
- Request clarification in-code using TODO comments sparingly; prefer updating documentation or AGENTS.md instead.
- Resolve merge conflicts promptly and document any major architectural decisions in the repository.

# Style guide
- **Fonts**: Use the configured site typography—primary font family is the theme default (Merriweather/Helvetica stack). Do not introduce new web fonts without approval.
- **Brand colours**: Retain the existing palette of deep green (#0F3D1F), warm gold (#C89B3C), neutral light (#F5F2EB), and dark charcoal (#222222). New UI elements should harmonise with these hues.
- **Imagery**: Use high-quality lawn-bowls-related imagery. Optimise images for web (compressed, responsive sizes) and include descriptive alt text.

# Coding conventions
- Site built with Jekyll; prefer Liquid templates, Markdown content files, and SCSS partials under `_sass`.
- Follow existing HTML structure conventions found in `_layouts` and `_includes`.
- JavaScript should be modular and placed under `assets/js`; avoid inline scripts when possible.
- Use Prettier (configured via `package.json`) for formatting JavaScript and JSON, and adhere to SCSS linting patterns already present.
- Keep YAML front matter tidy, with consistent key ordering (`layout`, `title`, `description`, `date`, etc.).

# Cornerstone pages

| Page                               | File location                           | Published URL*                                                                                                                         | Why it matters                                                                                                                                                                                                                                                   |
| ---------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Home (entry point)                 | `index.html`                            | [https://krussll.github.io/jhb/](https://krussll.github.io/jhb/)                                                                       | The site opens here, and the content plan calls for the homepage hero to surface the key pathways for newcomers, making it the central launchpad for the rest of the experience.:codex-file-citation:codex-file-citation:codex-file-citation                     |
| Getting Started hub                | `getting-started.md`                    | [https://krussll.github.io/jhb/getting-started/](https://krussll.github.io/jhb/getting-started/)                                       | Dedicated hub with a custom layout, hero modules, and curated tiles that route visitors to the main pathways; the navigation plan elevates it as the “Start Here” destination.:codex-file-citation:codex-file-citation:codex-file-citation                       |
| Guides library                     | `guides.md`                             | [https://krussll.github.io/jhb/guides/](https://krussll.github.io/jhb/guides/)                                                         | Aggregates every “guide” category article in a masonry listing and is featured as the first quick link from the Getting Started hero, underscoring its role in teaching fundamentals.:codex-file-citation:codex-file-citation:codex-file-citation                |
| Bowls & equipment reviews hub      | `reviews.md`                            | [https://krussll.github.io/jhb/reviews/](https://krussll.github.io/jhb/reviews/)                                                       | Central listing for all gear reviews, repeatedly promoted from the Getting Started hub and cited in the content plan as one of the foundational evergreen resources.:codex-file-citation:codex-file-citation:codex-file-citation:codex-file-citation             |
| Lawn bowls drill pack landing page | `lawn-bowls-downloadable-drill-pack.md` | [https://krussll.github.io/jhb/lawn-bowls-downloadable-drill-pack/](https://krussll.github.io/jhb/lawn-bowls-downloadable-drill-pack/) | Detailed sales and benefits page for the downloadable drill pack; the promotion plan spotlights it as a core evergreen asset and the Getting Started hub links to it repeatedly.:codex-file-citation:codex-file-citation:codex-file-citation:codex-file-citation |
| Help & Support hub                 | `help-and-support.md`                   | [https://krussll.github.io/jhb/help-and-support/](https://krussll.github.io/jhb/help-and-support/)                                     | Collects all “help” category content and is surfaced in the Getting Started support block as the place to find additional assistance, making it a cornerstone for problem-solving readers.:codex-file-citation:codex-file-citation:codex-file-citation           |


# Guidelines
- When adding or modifying components, ensure semantic HTML, ARIA attributes where necessary, and responsive breakpoints consistent with existing SCSS mixins.
- Update or add relevant unit or integration tests (e.g., for JavaScript modules) and run `npm test` if applicable.
- Validate generated pages with Lighthouse, focusing on accessibility and performance scores of 90+.
- Review content for E-E-A-T compliance: include expertise indicators, cite authoritative sources, and maintain a helpful, trustworthy tone.
- Confirm responsive formatting using browser dev tools across mobile, tablet, and desktop widths.
- To test locally, run `jekyll serve` and navigate to [http://127.0.0.1:4000/jhb/](http://127.0.0.1:4000/jhb/).
- Before committing, build the site locally with `bundle exec jekyll build` to catch Liquid or Markdown issues.
- If a post file is updated, set the "last_modified_at" value to the current datetime
