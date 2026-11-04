# DP-08: Build the AI coaching score-tracker integration (Bonus #3)

- **Source document:** `.agents/drill-pack-cro-plan.md` (§2 Bonus #3; §3 item 6)
- **Owner:** 🤖 Agent
- **Priority:** Low–Medium
- **Status:** Not started
- **Depends on:** None (better once the drill names from DP-02 are known)

## Task
Show buyers how to paste their drill scores (out of 40) into ChatGPT to work out whether forehand, backhand or weight control is costing them shots. Ideally build this into the existing AI Prompt Builder.

## Context
- The Prompt Builder already exists: `ai-prompt-builder.md` (`/ai-coaching/prompt-builder/`), `_includes/ai-prompt-builder.html`, `assets/js/ai-prompt-builder.js` and `_sass/_ai-prompt-builder.scss`. It has three coaching modes: `rollup`, `tactics`, `fault`.
- Options:
  - (a) Add a fourth mode, e.g. `scores` / "Drill Score Analyser", with inputs for several drill scores. The JS turns them into a structured analysis prompt.
  - (b) Write a short guide section on `/ai-coaching/` and the sales page with a copy-ready prompt template.
- Follow the builder's existing conventions:
  - Vanilla JS in the IIFE, handling every `[data-ai-prompt-builder]` instance.
  - Use `textContent` / `setAttribute` only (no `innerHTML`, to avoid XSS).
  - Keep the `chatgpt.com/?q=` deep link.
  - Labels above controls, `min-height: 48px`, `font-size: 1rem`.
- AGENTS.md asks for tests for JS modules (`npm test` if applicable).

## Completion criteria
- [ ] A bowler can enter drill scores and get a ready-to-paste or one-tap ChatGPT prompt that analyses them.
- [ ] The feature is linked from the drill pack sales page (DP-02) and listed as a bonus.
- [ ] Keyboard and screen-reader accessible; Lighthouse accessibility ≥ 90 on `/ai-coaching/prompt-builder/`.
- [ ] `llms.txt` updated if a new mode or page is added.
- [ ] `bundle exec jekyll build` completes without errors.
