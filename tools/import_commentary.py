#!/usr/bin/env python3
"""
import_commentary.py — vendor a classical commentary into sources/, verifiably.

    python3 tools/import_commentary.py --fetch          # download the wikitext
    python3 tools/import_commentary.py --report         # parse and report, write nothing
    python3 tools/import_commentary.py --write          # write sources/commentaries/wangbi/

Why this exists as a tool rather than a one-off paste: **provenance means
reproducible.** Anyone can re-run this and get byte-identical files, and the
fidelity check below is what lets the result be trusted at all.

WHY IT IS SAFE TO VENDOR THIS TEXT. Three independent grounds, each sufficient:

  1. Wang Bi died in 249 CE. The work is public domain by age everywhere.
  2. The transcription is of the 欽定四庫全書 (Siku Quanshu, imperially
     commissioned 1773-1782) — a printing older than any copyright term.
  3. Chinese Wikisource, the transcription's host, states in its own copyright
     policy that "the transcription of a work on Wikisource does not create a
     new copyright, so if the original work has entered the public domain the
     transcription here is also public domain," and that the site-wide CC BY-SA
     default "never comes into play for mainspace content." The page also
     carries {{PD-old}}.

And the one layer that COULD carry a claim is absent by that page's own
editorial policy. Its wikitext opens:

    請根據四庫全書掃描版校對本頁 … 加標點請另外建立頁面
    "Proofread this page against the Siku Quanshu scan … to add punctuation,
     create a separate page."

So the transcription is unpunctuated — the authorial layer only. See
sources/PROVENANCE.md.

THE FIDELITY CHECK, which is the point. The source interleaves Laozi lemmas
with Wang Bi's comment on each. Every lemma line is matched against our own
source/chinese.md for that chapter. If a line matches, the transcription is
faithful there, which is direct evidence that the commentary lines around it
were carried across intact too. Lines that do not match are reported, never
silently normalized: some are Siku glyph forms (handled below) and the rest are
genuine textual variants worth logging in sources/variants.yaml.
"""

import argparse
import difflib
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.corpus import ROOT, load_chapters  # noqa: E402

SCRATCH = ROOT / "sources" / ".cache"
OUT = ROOT / "sources" / "commentaries" / "wangbi"

SOURCE = {
    "title": "老子道徳經 (四庫全書本)",
    "work": "老子道徳經注",
    "author": "王弼",
    "author_dates": "226–249 CE",
    "edition": "欽定四庫全書 (Siku Quanshu), 子部十四 · 道家類",
    "edition_dates": "commissioned 1773, completed 1782",
    "host": "Chinese Wikisource, mainspace, tagged {{PD-old}}",
    "url": "https://zh.wikisource.org/zh-hant/老子道徳經_(四庫全書本)",
    "punctuation": "none — the page's editorial policy excludes it",
}

# Orthographic variants: the Siku printing's glyph forms for characters our base
# text writes differently. Harvested empirically by aligning every non-matching
# lemma line against our base text and collecting single-character
# substitutions, then filtered by hand to forms that are the SAME WORD.
# Applied for matching only — the vendored text always keeps the original glyph.
ORTHOGRAPHIC = {
    "徳": "德", "强": "強", "争": "爭", "𤣥": "玄", "衆": "眾", "静": "靜",
    "髙": "高", "盗": "盜", "徃": "往", "逺": "遠", "兊": "兌", "竒": "奇",
    "虚": "虛", "緜": "綿", "乗": "乘", "㣲": "微", "舍": "捨", "饑": "飢",
    "巳": "已", "絶": "絕", "况": "況", "賔": "賓", "氾": "汎", "隐": "隱",
    "隂": "陰", "沒": "没", "寳": "寶", "刋": "刊", "㝠": "冥", "㫖": "旨",
    "劔": "劍", "隣": "鄰", "耶": "邪",   # 耶/邪 are interchangeable final particles
}

# Include CJK Extension B: the Siku form of 玄 is 𤣥 (U+24465), outside the BMP.
# Omitting it silently deletes the character, which turned 玄德 into 徳 and
# 玄牝 into 牝 on the first pass through this data.
CJK = r"[㐀-鿿豈-﫿\U00020000-\U0002ebef]"

_NUM = {c: i for i, c in enumerate("〇一二三四五六七八九")}


def cn2int(s):
    if "十" not in s:
        return sum(_NUM[c] for c in s)
    a, _, b = s.partition("十")
    return (_NUM[a] if a else 1) * 10 + (sum(_NUM[c] for c in b) if b else 0)


def cjk(s):
    return "".join(re.findall(CJK, s))


def fold(s):
    """Normalize Siku glyph forms, for comparison only.

    Strips 〔…〕 first. Those are the Siku compilers' collation notes, and
    folding their characters into the comparison probe makes the lemma they
    annotate fail to match — which silently reclassified 揣而梲之 (a real
    variant against our 揣而銳之) as commentary on the first run.
    """
    return "".join(ORTHOGRAPHIC.get(c, c) for c in cjk(re.sub(r"〔[^〕]*〕", "", s)))


def strip_markup(line):
    """Drop wiki markup, keeping the Siku editors' own collation notes visible.

    {{SK notes|案…}} are the 18th-century compilers' notes ("originally X, now
    corrected per the Yongle Encyclopedia"). They are part of the Siku edition
    and public domain by age, so they are preserved, marked with 〔〕.
    {{SKchar|N}} stands for a glyph the transcribers could not encode; it
    becomes □ so that a gap is never mistaken for text.
    """
    line = re.sub(r"{{SK notes\|([^}]*)}}", r"〔\1〕", line)
    line = re.sub(r"{{SKchar\|\d+}}", "□", line)
    line = re.sub(r"{{[^}]*}}", "", line)
    line = re.sub(r"<[^>]*>", "", line)
    line = re.sub(r"\[\[[^\]|]*\|([^\]]*)\]\]", r"\1", line)
    line = re.sub(r"\[\[([^\]]*)\]\]", r"\1", line)
    return line.replace("　", "").strip()


def fetch():
    SCRATCH.mkdir(parents=True, exist_ok=True)
    dest = SCRATCH / "wangbi-sikuquanshu.wikitext"
    url = ("https://zh.wikisource.org/w/index.php?title="
           + urllib.parse.quote("老子道徳經 (四庫全書本)") + "&action=raw")
    req = urllib.request.Request(url, headers={
        "User-Agent": "taoteching-research/1.0 (CC0 translation project)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    dest.write_bytes(data)
    print(f"fetched {len(data):,} bytes → {dest.relative_to(ROOT)}")
    return dest


def parse(path):
    """Split into chapters, then classify each line as lemma or commentary."""
    raw = path.read_text(encoding="utf-8")
    blocks, cur, num = {}, [], None
    for line in raw.split("\n"):
        m = re.match(r"^　　([一二三四五六七八九十]+)章", line)
        if m:
            if num:
                blocks[num] = cur
            num, cur = cn2int(m.group(1)), []
            continue
        if num and line.startswith("　　"):
            cur.append(line)
    if num:
        blocks[num] = cur

    chapters = load_chapters()
    parsed, residual = {}, []
    for n, lines in sorted(blocks.items()):
        base = fold(chapters[n].chinese)
        rows, lemma_ok, lemma_var = [], 0, 0
        for line in lines:
            text = strip_markup(line)
            if not text:
                continue
            probe = fold(text)
            if not probe:
                continue
            if probe in base:
                rows.append(("lemma", text))
                lemma_ok += 1
                continue
            # Near-miss: a lemma carrying a genuine textual variant. Report it,
            # never fold it away.
            best = (0.0, "")
            for i in range(max(1, len(base) - len(probe) + 1)):
                w = base[i:i + len(probe)]
                r = difflib.SequenceMatcher(None, probe, w).ratio()
                if r > best[0]:
                    best = (r, w)
            if best[0] > 0.80 and len(probe) < 60:
                rows.append(("lemma*", text))
                lemma_var += 1
                residual.append((n, probe, best[1], best[0]))
            else:
                rows.append(("comment", text))
        parsed[n] = {"rows": rows, "lemma_ok": lemma_ok, "lemma_var": lemma_var}
    return parsed, residual


def write(parsed):
    OUT.mkdir(parents=True, exist_ok=True)
    for n, d in sorted(parsed.items()):
        body = [
            "---",
            f'work: "{SOURCE["work"]}"',
            f'author: "{SOURCE["author"]}"   # {SOURCE["author_dates"]}',
            f"chapter: {n}",
            f'edition: "{SOURCE["edition"]}"',
            f'edition_dates: "{SOURCE["edition_dates"]}"',
            f'transcription: "{SOURCE["host"]}"',
            f'obtained: "{SOURCE["url"]}"',
            f'punctuation: "{SOURCE["punctuation"]}"',
            'rights: "public domain by age (author d. 249 CE); printing 1782"',
            'imported_by: "tools/import_commentary.py"',
            "---",
            "",
            f"# 老子道徳經注 — 王弼 — 第{n}章",
            "",
            "*Wang Bi's commentary, interleaved. Each **lemma** is the Laozi text he is "
            "commenting on; the line under it is his comment. Lemmas marked `*` differ from "
            "our base text — see `sources/variants.yaml`. 〔…〕 are the Siku compilers' own "
            "collation notes. □ is a glyph the transcribers could not encode.*",
            "",
        ]
        for kind, text in d["rows"]:
            if kind == "lemma":
                body += [f"**{text}**", ""]
            elif kind == "lemma*":
                body += [f"**{text}** `*`", ""]
            else:
                body += [f"> {text}", ""]
        (OUT / f"{n:03d}.md").write_text("\n".join(body).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {len(parsed)} files → {OUT.relative_to(ROOT)}")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--fetch", action="store_true")
    p.add_argument("--report", action="store_true")
    p.add_argument("--write", action="store_true")
    args = p.parse_args()

    src = SCRATCH / "wangbi-sikuquanshu.wikitext"
    if args.fetch or not src.exists():
        src = fetch()

    parsed, residual = parse(src)
    have = sorted(parsed)
    missing = [n for n in range(1, 82) if n not in parsed]
    ok = sum(d["lemma_ok"] for d in parsed.values())
    var = sum(d["lemma_var"] for d in parsed.values())
    com = sum(1 for d in parsed.values() for k, _ in d["rows"] if k == "comment")

    print(f"\nchapters:   {len(have)}/81 present"
          + (f", missing {missing}" if missing else ""))
    print(f"lemma lines: {ok} matched our base text exactly, {var} with variants "
          f"({ok / (ok + var):.0%} exact)")
    print(f"commentary lines: {com}")

    if residual:
        print(f"\ncandidate textual variants ({len(residual)}) — Siku Wang Bi against our base:")
        for n, mine, theirs, r in residual:
            diff = [(a, b) for op, i1, i2, j1, j2 in
                    difflib.SequenceMatcher(None, mine, theirs).get_opcodes()
                    if op == "replace" and i2 - i1 == j2 - j1
                    for a, b in zip(mine[i1:i2], theirs[j1:j2])]
            if diff:
                pairs = " ".join(f"{a}/{b}" for a, b in diff)
                print(f"   ch{n:>2}  {pairs}")
        print("\n   Review these by hand; real forks belong in sources/variants.yaml as "
              "witness `siku-wangbi`. Glyph-only pairs belong in ORTHOGRAPHIC above.")

    if args.write:
        print()
        write(parsed)
    elif not args.report:
        print("\n(nothing written — pass --write)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
