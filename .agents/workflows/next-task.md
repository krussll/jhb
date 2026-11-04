---
description: Run the first task in the backlog owned by the Agent, ask clarifying questions, execute it, and delete the backlog file.
---

# Workflow: Next Backlog Task

1. Identify the first task in `.agents/backlog/` where `Owner` is `Agent` using:
   ```bash
   python3 .agents/skills/next-task/scripts/get_next_task.py
   ```
2. Read the task requirements and completion criteria in full.
3. Ask the user any clarifying questions needed regarding design, content, or implementation options.
4. Execute the implementation according to `AGENTS.md` guidelines.
5. Verify with `bundle exec jekyll build`.
6. Once complete, delete the backlog file using:
   ```bash
   python3 .agents/skills/next-task/scripts/get_next_task.py --delete <task-filename>
   ```

