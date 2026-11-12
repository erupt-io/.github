# AGENTS.md

This file provides guidance to coding agents (Claude Code, Codex, ...) when working with code in this repository.

This is the `.github` repository of the `erupt-io` GitHub organization: `profile/README.md` is the page shown
on the organization's profile. The erupt framework itself lives at `erupts/erupt`; this organization holds
the modules and applications built on it.

- The repository table between `<!-- repos:start -->` and `<!-- repos:end -->` is generated: do not edit it
  by hand and keep both markers. `scripts/sync-readme.py` rewrites it from the organization's public,
  non-archived repositories (name, link, description; `.github` itself excluded, sorted by name), so a wrong
  row is fixed by changing that repository's description on GitHub.
- Text outside the markers is hand-written and preserved by the script.
- `.github/workflows/sync.yml` runs the script every day (and on manual dispatch) and commits
  `profile/README.md` when it changed.

```bash
python3 scripts/sync-readme.py   # rebuild the table locally; needs a logged-in `gh`
```
