# Skills

Reusable, machine-readable procedures for this project. Each is a folder containing a
`SKILL.md` with YAML frontmatter, in the format used by Claude Code and Cowork.

They live here — in the repository, under CC0 — rather than only in a local config, so
that the method travels with the work: version-controlled, reviewable, portable between
AI collaborators, and available to anyone who clones the repo.

| Skill | Use when |
|---|---|
| `glossary-entry/` | Adding or revising a term in `glossary/`, or locking a rendering |

## To activate

Copy (or symlink) into the agent's skills directory:

```bash
cp -r process/skills/glossary-entry ~/.claude/skills/
# or, to keep them in sync:
ln -s "$(pwd)/process/skills/glossary-entry" ~/.claude/skills/glossary-entry
```

## Why these exist

`process/method.md` describes how the work is done. A skill makes a piece of that method
**executable** — loaded automatically when the task arises, rather than depending on
someone remembering to read the guide. It is also how the method transfers intact to a
different or more capable model later.
