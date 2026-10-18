#!/usr/bin/env python3
"""Rewrites the repository table of profile/README.md from the organization's public repositories.

Run by the sync workflow every day, or by hand: `gh` must be logged in.
"""
import json
import pathlib
import subprocess

ORG = "erupt-io"
README = pathlib.Path(__file__).resolve().parent.parent / "profile" / "README.md"
START, END = "<!-- repos:start -->", "<!-- repos:end -->"

repos = json.loads(subprocess.check_output([
    "gh", "repo", "list", ORG, "--visibility", "public", "--no-archived", "--limit", "200",
    "--json", "name,url,description,pushedAt",
]))
repos = [r for r in repos if r["name"] != ".github"]
repos.sort(key=lambda r: r["name"])

rows = ["| Repository | What it is |", "|---|---|"]
for repo in repos:
    rows.append(f"| [{repo['name']}]({repo['url']}) | {(repo.get('description') or '').strip()} |")
table = "\n".join(rows)

text = README.read_text()
head, rest = text.split(START, 1)
_, tail = rest.split(END, 1)
README.write_text(f"{head}{START}\n{table}\n{END}{tail}")
print(f"{len(repos)} repositories")
