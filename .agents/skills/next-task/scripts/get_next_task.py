#!/usr/bin/env python3
"""
Finds the first task in .agents/backlog (or agents/backlog) where the owner is "Agent".
Usage:
    python3 get_next_task.py [--json] [--delete FILE]
"""

import os
import sys
import re
import json

def get_backlog_dir():
    candidates = [".agents/backlog", "agents/backlog"]
    for c in candidates:
        if os.path.isdir(c):
            return c
    return None

def find_next_agent_task():
    backlog_dir = get_backlog_dir()
    if not backlog_dir:
        return None

    files = sorted(os.listdir(backlog_dir))
    for filename in files:
        if not filename.endswith(".md"):
            continue
        filepath = os.path.join(backlog_dir, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
        except OSError:
            continue

        owner_match = re.search(r"-\s+\*\*Owner:\*\*\s*(.*)", content, re.IGNORECASE)
        if owner_match:
            owner_line = owner_match.group(1).strip()
            owner_lower = owner_line.lower()
            if "agent" in owner_lower and not ("shared" in owner_lower or "user only" in owner_lower):
                # Extract title
                title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
                title = title_match.group(1).strip() if title_match else filename
                return {
                    "filename": filename,
                    "filepath": filepath,
                    "owner": owner_line,
                    "title": title,
                    "content": content
                }
    return None

def delete_backlog_file(filename):
    deleted = []
    # Check both potential backlog folders
    for b_dir in [".agents/backlog", "agents/backlog"]:
        target = os.path.join(b_dir, os.path.basename(filename))
        if os.path.exists(target):
            os.remove(target)
            deleted.append(target)
    return deleted

if __name__ == "__main__":
    if "--delete" in sys.argv:
        idx = sys.argv.index("--delete")
        if idx + 1 < len(sys.argv):
            target = sys.argv[idx + 1]
            deleted = delete_backlog_file(target)
            print(f"Deleted: {deleted}")
            sys.exit(0)

    task = find_next_agent_task()
    if not task:
        print("No pending agent tasks found in backlog.")
        sys.exit(1)

    if "--json" in sys.argv:
        print(json.dumps(task, indent=2))
    else:
        print(f"Next Agent Task: {task['filename']}")
        print(f"Title: {task['title']}")
        print(f"Owner: {task['owner']}")
        print(f"Path: {task['filepath']}")

