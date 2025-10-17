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

# Guidelines
- When adding or modifying components, ensure semantic HTML, ARIA attributes where necessary, and responsive breakpoints consistent with existing SCSS mixins.
- Update or add relevant unit or integration tests (e.g., for JavaScript modules) and run `npm test` if applicable.
- Validate generated pages with Lighthouse, focusing on accessibility and performance scores of 90+.
- Review content for E-E-A-T compliance: include expertise indicators, cite authoritative sources, and maintain a helpful, trustworthy tone.
- Confirm responsive formatting using browser dev tools across mobile, tablet, and desktop widths.
- Before committing, build the site locally with `bundle exec jekyll build` to catch Liquid or Markdown issues.
