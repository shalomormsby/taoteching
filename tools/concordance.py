#!/usr/bin/env python3
"""
concordance.py — a character in, the evidence out.

The counterpart to check_locks.py, and the opposite kind of tool. The checker
optimizes precision: it must not cry wolf, and it exits non-zero. This optimizes
recall: it shows everything remotely relevant, judges nothing, and never fails.
Do not merge them — a tool that gates and searches at once ends up too noisy to
gate and too quiet to search.

    python3 tools/concordance.py 明                 # every chapter, line, rendering
    python3 tools/concordance.py --english "mystery"   # the reverse direction
    python3 tools/concordance.py --pairs 我 吾        # two terms side by side
    python3 tools/concordance.py --formulas          # every repeated segment
    python3 tools/concordance.py 常 --json           # for pulling into a session

This replaces the ad-hoc greps the method has been running by hand. The 天地
entry was built that way, and the finding that 陰 appears exactly once in the
whole book came out of exactly this kind of sweep.
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.corpus import load_chapters, load_terms  # noqa: E402

BOLD, DIM, OFF = "\033[1m", "\033[2m", "\033[0m"


def _plain(text):
    """Strip the literal gloss's bracketed pinyin apparatus."""
    return re.sub(r"\s+", " ", re.sub(r"\\?\[[^\]]*\\?\]", "", text)).strip()


def lock_for(term, terms):
    for t in terms:
        if term in t.characters or term == t.term:
            return t
    return None


# ------------------------------------------------------------------ occurrences

def occurrences(term, chapters):
    """Every chapter containing the term, with its lines and the chapter's verse."""
    out = []
    for n in sorted(chapters):
        ch = chapters[n]
        rows = [r for r in ch.source_rows if term in r.chinese]
        if rows:
            out.append((ch, rows))
    return out


def show_term(term, chapters, terms, quiet=False):
    hits = occurrences(term, chapters)
    lock = lock_for(term, terms)

    print(f"\n{BOLD}{term}{OFF}", end="")
    if lock:
        print(f"  ({lock.pinyin}) → {lock.render}", end="")
        if lock.forbidden:
            print(f"   never: {', '.join(lock.forbidden)}", end="")
        print(f"\n{DIM}{lock.entry}{OFF}")
    else:
        print(f"   {DIM}no glossary entry yet — see glossary/TRIAGE.md{OFF}")

    total = sum(len(rows) for _, rows in hits)
    drafted = [ch for ch, _ in hits if ch.drafted]
    print(f"{len(hits)} chapters, {total} lines "
          f"({len(drafted)} drafted, {len(hits) - len(drafted)} not yet)\n")

    for ch, rows in hits:
        flag = "" if ch.drafted else f"  {DIM}[{ch.status}]{OFF}"
        print(f"  {BOLD}ch {ch.number}{OFF}{flag}")
        for r in rows:
            print(f"    {r.chinese}")
            if not quiet:
                print(f"      {DIM}{_plain(r.literal)}{OFF}")
        if ch.drafted and not quiet:
            for _, line in ch.verse:
                print(f"      │ {line.strip()}")
        print()
    return hits


# ------------------------------------------------------- the reverse direction

def show_english(phrase, chapters, terms, quiet=False):
    """Which chapters use this English, and is each use backed by its character?

    The higher-value direction, and the half the Chinese cannot answer. A lock
    is a two-way claim — every 明 renders as clear-seeing, AND every
    clear-seeing renders 明 — and only this direction catches the second half:
    a rendering applied where the character licensing it is absent.
    """
    lock = None
    for t in terms:
        if phrase.lower() in t.render.lower() or any(
                phrase.lower() == f.lower() for f in t.forbidden):
            lock = t
            break

    print(f'\n{BOLD}"{phrase}"{OFF}', end="")
    if lock:
        kind = "forbidden for" if any(phrase.lower() == f.lower() for f in lock.forbidden) \
            else "the rendering of"
        print(f"  — {kind} {lock.term} ({lock.pinyin})\n{DIM}{lock.entry}{OFF}")
    else:
        print(f"   {DIM}not tied to any locked term{OFF}")

    backed, unbacked = [], []
    for n in sorted(chapters):
        ch = chapters[n]
        if not ch.drafted:
            continue
        for ln, line in ch.verse:
            if phrase.lower() in line.lower():
                has = lock and any(ch.has(c) for c in lock.characters)
                (backed if has else unbacked).append((ch, ln, line.strip()))

    print(f"{len(backed) + len(unbacked)} lines"
          + (f" — {len(backed)} backed by {lock.term}, {len(unbacked)} not" if lock else "")
          + "\n")

    for label, group in (("backed", backed), ("not backed", unbacked)):
        if not group or (not lock and label == "backed"):
            continue
        if lock:
            print(f"  {BOLD}{label}{OFF}")
        for ch, ln, line in group:
            print(f"    ch {ch.number}:{ln}  {line}")
            if lock and label == "not backed" and not quiet:
                print(f"      {DIM}no {'/'.join(lock.characters)} in this chapter{OFF}")
        print()

    if lock and unbacked:
        print(f'  {DIM}"{phrase}" without {lock.term} is either an ordinary English word '
              f"or a rendering that outran its character. Check each.{OFF}\n")
    return backed, unbacked


# ----------------------------------------------------------------------- pairs

def show_pairs(a, b, chapters, terms, quiet=False):
    """Two terms across the book — the 我/吾, 玄/妙, 正/奇 work."""
    ha = {ch.number: rows for ch, rows in occurrences(a, chapters)}
    hb = {ch.number: rows for ch, rows in occurrences(b, chapters)}
    both = sorted(set(ha) & set(hb))
    only_a = sorted(set(ha) - set(hb))
    only_b = sorted(set(hb) - set(ha))

    print(f"\n{BOLD}{a}{OFF} and {BOLD}{b}{OFF}\n")
    print(f"  together in {len(both)}: {', '.join(map(str, both)) or '—'}")
    print(f"  {a} alone in {len(only_a)}: {', '.join(map(str, only_a)) or '—'}")
    print(f"  {b} alone in {len(only_b)}: {', '.join(map(str, only_b)) or '—'}\n")

    for n in both:
        ch = chapters[n]
        print(f"  {BOLD}ch {ch.number}{OFF}" + ("" if ch.drafted else f"  {DIM}[{ch.status}]{OFF}"))
        for label, rows in ((a, ha[n]), (b, hb[n])):
            for r in rows:
                print(f"    {label}  {r.chinese}")
                if not quiet:
                    print(f"        {DIM}{_plain(r.literal)}{OFF}")
        print()
    return both, only_a, only_b


# -------------------------------------------------------------------- formulas

def show_formulas(chapters, min_len=4):
    """Every Chinese comma-segment appearing in more than one chapter.

    The index behind check_locks.py's repeated-formula rule, shown in full and
    without a verdict. Segments are the unit a formula lives in — 物壯則老,
    不道早已, 是謂玄德 — so this is where you look before deciding whether two
    chapters agree.
    """
    index = defaultdict(set)
    for ch in chapters.values():
        for row in ch.source_rows:
            for seg in re.split(r"[，。；、]", row.chinese):
                seg = "".join(re.findall(r"[㐀-鿿]+", seg))
                if len(seg) >= min_len:
                    index[seg].add(ch.number)

    shared = {s: sorted(c) for s, c in index.items() if len(c) > 1}
    grammar = {s: c for s, c in shared.items() if len(c) > 3}
    formulas = {s: c for s, c in shared.items() if len(c) <= 3}

    print(f"\n{BOLD}repeated segments{OFF}")
    print(f"  {len(formulas)} formulas (2-3 chapters) · {len(grammar)} common "
          f"constructions (4+)\n")

    for seg, nums in sorted(formulas.items(), key=lambda kv: (-len(kv[0]), kv[1])):
        drafted = [n for n in nums if chapters[n].drafted]
        mark = "" if len(drafted) == len(nums) else f"  {DIM}({len(drafted)}/{len(nums)} drafted){OFF}"
        print(f"  {seg}   ch {', '.join(str(n) for n in nums)}{mark}")

    if grammar:
        print(f"\n  {DIM}common constructions, not formulas:{OFF}")
        for seg, nums in sorted(grammar.items(), key=lambda kv: -len(kv[1])):
            print(f"    {DIM}{seg}   {len(nums)} chapters{OFF}")
    print()
    return formulas


# -------------------------------------------------------------------------- cli

def main():
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("term", nargs="?", help="a character or compound, e.g. 明 or 天地")
    p.add_argument("--english", metavar="PHRASE",
                   help="reverse lookup: which chapters use this English, and is it backed")
    p.add_argument("--pairs", nargs=2, metavar=("A", "B"),
                   help="two terms across the book")
    p.add_argument("--formulas", action="store_true",
                   help="every Chinese segment shared by more than one chapter")
    p.add_argument("-q", "--quiet", action="store_true",
                   help="lines only — omit glosses and surrounding verse")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()

    chapters = load_chapters()
    terms = load_terms()

    if args.json:
        payload = {}
        if args.term:
            payload["term"] = args.term
            payload["chapters"] = [
                {"chapter": ch.number, "status": ch.status,
                 "lines": [{"chinese": r.chinese, "literal": _plain(r.literal)} for r in rows],
                 "verse": [t.strip() for _, t in ch.verse]}
                for ch, rows in occurrences(args.term, chapters)]
        if args.english:
            backed, unbacked = [], []
            lock = next((t for t in terms if args.english.lower() in t.render.lower()), None)
            for n in sorted(chapters):
                ch = chapters[n]
                if not ch.drafted:
                    continue
                for ln, line in ch.verse:
                    if args.english.lower() in line.lower():
                        has = lock and any(ch.has(c) for c in lock.characters)
                        (backed if has else unbacked).append(
                            {"chapter": ch.number, "line": ln, "text": line.strip()})
            payload["english"] = {"phrase": args.english, "backed": backed,
                                  "unbacked": unbacked}
        if args.formulas:
            index = defaultdict(set)
            for ch in chapters.values():
                for row in ch.source_rows:
                    for seg in re.split(r"[，。；、]", row.chinese):
                        seg = "".join(re.findall(r"[㐀-鿿]+", seg))
                        if len(seg) >= 4:
                            index[seg].add(ch.number)
                payload.setdefault("formulas", {})
            payload["formulas"] = {s: sorted(c) for s, c in index.items()
                                   if 2 <= len(c) <= 3}
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return 0

    did = False
    if args.formulas:
        show_formulas(chapters)
        did = True
    if args.pairs:
        show_pairs(args.pairs[0], args.pairs[1], chapters, terms, args.quiet)
        did = True
    if args.english:
        show_english(args.english, chapters, terms, args.quiet)
        did = True
    if args.term:
        show_term(args.term, chapters, terms, args.quiet)
        did = True

    if not did:
        p.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
