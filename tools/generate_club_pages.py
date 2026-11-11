#!/usr/bin/env python3
"""
tools/generate_club_pages.py

Generates and syncs Jekyll collection markdown files (_clubs/<city>/<slug>.md)
from YAML data files (_data/clubs/*.yml) for clubs with profile_page: true.

Usage:
    python3 tools/generate_club_pages.py [--dry-run] [--force]
"""

import argparse
import datetime
import json
import os
import subprocess
import sys


def load_yaml_file(file_path):
    """Loads a YAML file using PyYAML if available, or falls back to system Ruby."""
    try:
        import yaml
        with open(file_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except ImportError:
        pass

    # Fallback to Ruby's built-in YAML and JSON parsers
    cmd = [
        "ruby",
        "-ryaml",
        "-rjson",
        "-e",
        "puts JSON.dump(YAML.load(File.read(ARGV[0])))",
        file_path,
    ]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.PIPE)
        return json.loads(output.decode("utf-8"))
    except Exception as e:
        print(f"Error reading YAML file '{file_path}': {e}", file=sys.stderr)
        return None


def quote_str(s):
    """Escapes and double-quotes a string for YAML."""
    if s is None:
        return '""'
    s_str = str(s).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{s_str}"'


def format_yaml_value(value, indent_level=0):
    """Formats a python value into clean YAML string."""
    indent = "  " * indent_level
    if value is None:
        return '""'
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, list):
        if not value:
            return "[]"
        lines = []
        for item in value:
            if isinstance(item, dict):
                first = True
                for k, v in item.items():
                    if first:
                        lines.append(f"{indent}- {k}: {format_yaml_value(v, indent_level + 1)}")
                        first = False
                    else:
                        lines.append(f"{indent}  {k}: {format_yaml_value(v, indent_level + 1)}")
            elif isinstance(item, str):
                lines.append(f"{indent}- {quote_str(item)}")
            else:
                lines.append(f"{indent}- {item}")
        return "\n" + "\n".join(lines)
    if isinstance(value, dict):
        lines = []
        for k, v in value.items():
            lines.append(f"{indent}{k}: {format_yaml_value(v, indent_level + 1)}")
        return "\n" + "\n".join(lines)

    str_val = str(value).strip()
    if "\n" in str_val or len(str_val) > 80:
        clean_lines = [line.strip() for line in str_val.splitlines() if line.strip()]
        body = ("\n" + indent + "  ").join(clean_lines)
        return f">\n{indent}  {body}"
    return quote_str(str_val)


def generate_frontmatter(club, city_key):
    """Builds clean frontmatter string for a club."""
    city = club.get("city") or city_key
    city_name = club.get("city_name") or city.replace("-", " ").title()
    slug = club.get("slug")
    name = club.get("name") or slug.replace("-", " ").title()
    permalink = f"/bowls-clubs/{city}/{slug}/"
    city_url = club.get("city_url") or f"/bowls-clubs/bowls-clubs-in-{city}/"

    lines = [
        "---",
        "layout: club",
        f"title: {quote_str(name)}",
        f"name: {quote_str(name)}",
        f"permalink: {permalink}",
        f"city: {quote_str(city)}",
        f"city_name: {quote_str(city_name)}",
        f"city_url: {quote_str(city_url)}",
    ]

    optional_keys = [
        ("country", club.get("country")),
        ("country_code", club.get("country_code")),
        ("area", club.get("area")),
        ("address", club.get("address")),
        ("postcode", club.get("postcode")),
        ("surfaces", club.get("surfaces")),
        ("formats", club.get("formats")),
        ("season", club.get("season")),
        ("rinks_info", club.get("rinks_info")),
        ("beginner_friendly", club.get("beginner_friendly")),
        ("barefoot_social", club.get("barefoot_social")),
        ("loan_bowls", club.get("loan_bowls")),
        ("bar_clubhouse", club.get("bar_clubhouse")),
        ("website", club.get("website")),
        ("maps_query", club.get("maps_query")),
        ("telephone", club.get("telephone") or club.get("phone")),
        ("email", club.get("email")),
        ("summary", club.get("summary")),
        ("about", club.get("about")),
        ("faqs", club.get("faqs")),
    ]

    for key, val in optional_keys:
        if val is not None and val != "" and val != []:
            formatted = format_yaml_value(val)
            if formatted.startswith("\n"):
                lines.append(f"{key}:{formatted}")
            elif formatted.startswith(">\n"):
                lines.append(f"{key}: {formatted}")
            else:
                lines.append(f"{key}: {formatted}")

    now_iso = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S +0000")
    lines.append(f"last_modified_at: {now_iso}")
    lines.append("---\n")
    return "\n".join(lines)


def process_clubs(data_dir, output_dir, dry_run=False, force=False):
    """Processes all club YAML files in data_dir and generates markdown files in output_dir."""
    if not os.path.exists(data_dir):
        print(f"Error: Data directory not found at '{data_dir}'", file=sys.stderr)
        return 1

    total_clubs = 0
    generated_count = 0
    skipped_count = 0
    updated_count = 0

    for root, _, files in sorted(os.walk(data_dir)):
        for file in sorted(files):
            if not (file.endswith(".yml") or file.endswith(".yaml")):
                continue

            file_path = os.path.join(root, file)
            city_key = os.path.splitext(file)[0].lower()

            data = load_yaml_file(file_path)
            if not isinstance(data, list):
                continue

            for club in data:
                total_clubs += 1
                slug = club.get("slug")
                if not slug:
                    print(f"Warning: Club without slug in {file_path}: {club.get('name')}", file=sys.stderr)
                    continue

                if not club.get("profile_page"):
                    skipped_count += 1
                    continue

                city = (club.get("city") or city_key).lower()
                dest_dir = os.path.join(output_dir, city)
                dest_path = os.path.join(dest_dir, f"{slug}.md")

                new_content = generate_frontmatter(club, city)
                if club.get("content"):
                    new_content += club["content"].strip() + "\n"

                file_exists = os.path.exists(dest_path)
                if file_exists and not force:
                    with open(dest_path, "r", encoding="utf-8") as existing_file:
                        existing_content = existing_file.read()
                    # Check if only timestamp changed
                    content_without_timestamp = "\n".join(
                        line for line in new_content.splitlines() if not line.startswith("last_modified_at:")
                    )
                    existing_without_timestamp = "\n".join(
                        line for line in existing_content.splitlines() if not line.startswith("last_modified_at:")
                    )
                    if content_without_timestamp == existing_without_timestamp:
                        continue
                    updated_count += 1
                else:
                    generated_count += 1

                prefix = "[DRY-RUN] Would write" if dry_run else "Wrote"
                action = "update" if file_exists else "create"
                print(f"{prefix} ({action}): {dest_path}")

                if not dry_run:
                    os.makedirs(dest_dir, exist_ok=True)
                    with open(dest_path, "w", encoding="utf-8") as out:
                        out.write(new_content)

    print("\n--- Club Page Generation Summary ---")
    print(f"Total clubs in data:     {total_clubs}")
    print(f"Generated (new):         {generated_count}")
    print(f"Updated:                 {updated_count}")
    print(f"Skipped (no profile):    {skipped_count}")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Generate club collection profile pages from YAML data.")
    parser.add_argument("--data-dir", default="_data/clubs", help="Path to clubs data directory")
    parser.add_argument("--output-dir", default="_clubs", help="Path to _clubs collection directory")
    parser.add_argument("--dry-run", action="store_true", help="Preview output without writing files")
    parser.add_argument("--force", action="store_true", help="Force overwrite all existing files")

    args = parser.parse_args()
    return process_clubs(args.data_dir, args.output_dir, dry_run=args.dry_run, force=args.force)


if __name__ == "__main__":
    sys.exit(main())
