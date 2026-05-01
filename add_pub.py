#!/usr/bin/env python3
"""
Add a new publication entry to _data/publications.yml.

Usage:
    python3 add_pub.py

Requires ruamel.yaml for in-place editing:
    pip install ruamel.yaml

Falls back to printing a YAML snippet if ruamel.yaml is not installed.
"""

import os
import sys
from datetime import date

DATA_FILE = os.path.join(os.path.dirname(__file__), "_data", "publications.yml")


def prompt(label, default=None, hint=None):
    display = label
    if hint:
        display += f" [{hint}]"
    if default:
        display += f" (default: {default})"
    display += ": "
    value = input(display).strip()
    if not value and default:
        return default
    return value


def build_entry(fields):
    return {
        "title": fields["title"],
        "authors": fields["authors"],
        "pub_date": fields["pub_date"],
        "date": fields["pub_date"],
        "venue": fields["venue"],
        "citation": "",
        "paper_url": fields["paper_url"],
        "slides_url": fields["slides_url"],
        "code_url": fields["code_url"],
        "teaser_img": f"../images/title_img/{fields['teaser_img']}" if fields["teaser_img"] else None,
        "category": fields["category"],
        "permalink": f"/publication/{fields['pub_date']}-{fields['slug']}",
        "excerpt": None,
        "arxiv_icon": None,
        "github_icon": None,
    }


def print_yaml_snippet(entry):
    print("\n── YAML snippet to paste at the top of _data/publications.yml ──\n")
    print(f"- title: {entry['title']}")
    print(f"  authors: {entry['authors']}")
    print(f"  pub_date: '{entry['pub_date']}'")
    print(f"  date: '{entry['date']}'")
    print(f"  venue: {entry['venue']}")
    print(f"  citation: ''")
    print(f"  paper_url: {entry['paper_url'] or ''}")
    print(f"  slides_url: {entry['slides_url'] or ''}")
    print(f"  code_url: {entry['code_url'] or ''}")
    print(f"  teaser_img: {entry['teaser_img'] or ''}")
    print(f"  category: {entry['category']}")
    print(f"  permalink: {entry['permalink']}")
    print(f"  excerpt: null")
    print(f"  arxiv_icon: null")
    print(f"  github_icon: null")
    print()


def write_with_ruamel(entry):
    from ruamel.yaml import YAML
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.width = 4096

    with open(DATA_FILE, "r") as f:
        data = yaml.load(f)

    if data is None:
        data = []

    data.insert(0, entry)

    with open(DATA_FILE, "w") as f:
        yaml.dump(data, f)

    print(f"\nPrepended entry to {DATA_FILE}")


def main():
    print("=== Add Publication ===\n")
    print("Tip: wrap your own name in <strong>...</strong> in the authors field.\n")

    fields = {
        "title": prompt("Title"),
        "authors": prompt("Authors", hint="use <strong>Your Name</strong> for yourself"),
        "pub_date": prompt("Publication date", default=str(date.today()), hint="YYYY-MM-DD"),
        "venue": prompt("Venue", hint="e.g. 'In NeurIPS, 2025' or 'arXiv, 2025'"),
        "paper_url": prompt("Paper URL (arXiv)", default=""),
        "slides_url": prompt("Project page URL", default=""),
        "code_url": prompt("Code URL (GitHub)", default=""),
        "teaser_img": prompt("Teaser image filename", hint="e.g. MyPaper.png — drop it in images/title_img/", default=""),
        "category": prompt("Category", default="conferences", hint="conferences / preprints"),
        "slug": prompt("URL slug", hint="e.g. MyPaper — used in permalink"),
    }

    entry = build_entry(fields)

    try:
        write_with_ruamel(entry)
    except ImportError:
        print("\nruamel.yaml not found. Install it with: pip install ruamel.yaml")
        print_yaml_snippet(entry)
        return

    if fields["teaser_img"]:
        print(f"  → Drop the teaser image at: images/title_img/{fields['teaser_img']}")
    print("  → Then: git add . && git push")


if __name__ == "__main__":
    main()
