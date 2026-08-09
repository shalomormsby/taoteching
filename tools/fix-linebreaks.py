#!/usr/bin/env python3
"""Restore Markdown hard line breaks in the verse of chapters/*.md.

The translation is verse: every line break is deliberate. Markdown collapses a
single newline into a space, so a stanza renders as one running paragraph in
any preview (GitHub, VS Code, Marked). The fix is the CommonMark hard break —
two trailing spaces — which the working manuscript in source/ already uses.

Chapter files are generated from that manuscript, and the generation dropped
the trailing whitespace. Run this after every regeneration. It is idempotent
and touches only the `## Translation` section, never the source tables.

    python3 tools/fix-linebreaks.py          # rewrite in place
    python3 tools/fix-linebreaks.py --check  # exit 1 if any file would change
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SECTION = re.compile(r"(^## Translation\n)(.*?)(?=^## |\Z)", re.S | re.M)


def fix_verse(body: str) -> str:
    """Two trailing spaces on every verse line that has a verse line after it."""
    lines = body.split("\n")
    out = []
    for i, line in enumerate(lines):
        stripped = line.rstrip()
        nxt = lines[i + 1].strip() if i + 1 < len(lines) else ""
        # A blank next line ends the stanza, so no break marker is needed there.
        out.append(stripped + "  " if stripped and nxt else stripped)
    return "\n".join(out)


def main() -> int:
    check = "--check" in sys.argv
    changed = []
    for path in sorted((ROOT / "chapters").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        fixed = SECTION.sub(lambda m: m.group(1) + fix_verse(m.group(2)), text)
        if fixed != text:
            changed.append(path.relative_to(ROOT))
            if not check:
                path.write_text(fixed, encoding="utf-8")

    if not changed:
        print("All chapters have hard line breaks in the verse.")
        return 0
    verb = "need fixing" if check else "fixed"
    print(f"{len(changed)} file(s) {verb}:")
    for p in changed:
        print(f"  {p}")
    return 1 if check else 0


if __name__ == "__main__":
    sys.exit(main())
