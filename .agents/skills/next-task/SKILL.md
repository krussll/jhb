---
name: next-task
description: Take the first task from the backlog (.agents/backlog) where the owner is "Agent", ask any clarifying questions, execute the task, and delete the backlog file upon completion.
---

# Next Backlog Task

This skill automates taking the next pending task from the backlog owned by the AI Agent, clarifying any questions, executing the changes, verifying the build, and removing the backlog file.

## Workflow Steps

### Step 1: Identify the Next Agent Task
1. Run the helper script to locate the next task:
   ```bash
   python3 .agents/skills/next-task/scripts/get_next_task.py --json
   ```
   Or inspect `.agents/backlog/` sorted alphabetically and find the first `.md` file whose `Owner:` field indicates `Agent` (and not `Shared` or `User only`).
2. Read the entire backlog task file. Understand its:
   - Source document & context
   - Detailed task description
   - Completion criteria
   - Dependencies

### Step 2: Clarify Requirements (Ask Questions)
1. Before modifying any code, review whether there are architectural, stylistic, or content decisions that need user input.
2. Ask any clarifying questions to the user (e.g. using the `ask_question` tool or structured plain text questions).
3. Wait for the user's response before proceeding with assumptions on ambiguous requirements.

### Step 3: Implement the Task
1. Adhere to project guidelines in `AGENTS.md` and `.agents/AGENTS.md`:
   - Follow site typography, brand colors, and Bootstrap layout conventions.
   - Prefer reusable Liquid partials and YAML data files (e.g., `_data/`) where appropriate.
   - If single post files are modified, update `last_modified_at` with current datetime.
2. Maintain documentation and code comments integrity.

### Step 4: Verification
1. Run the local Jekyll build:
   ```bash
   bundle exec jekyll build
   ```
2. Verify that there are no Liquid syntax errors, missing asset errors, or broken layout references.
3. Check the completion checklist in the backlog task to confirm all criteria are satisfied.

### Step 5: Clean Up Backlog
1. Delete the completed task file from `.agents/backlog/`:
   ```bash
   python3 .agents/skills/next-task/scripts/get_next_task.py --delete <filename>
   ```
2. Summarize the changes made and confirm the backlog task has been resolved and removed.

