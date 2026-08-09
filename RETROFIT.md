# RETROFIT — consistency debt

*Decisions settled later in the book that oblige changes to chapters already drafted. Work this list during the **editing pass**, not before — finishing the first draft comes first.*

Generated from an automated scan of the drafted chapters (1–60, 65) against the locked renderings. Each chapter file carries its own debt in frontmatter (`retrofit: [...]`), so this list can be regenerated mechanically once `tools/check_locks.py` exists.

**Two locks holding clean across the whole draft:** 德 → *integrity* (zero occurrences of "virtue") and the Sage pronoun rule (zero occurrences of "he/his/him" near the Sage). Those principles are working.

---

## 天地 / 天 → "sky and earth" · "nature" *(never "the cosmos")*

**12 chapters: 9, 10, 16, 22, 23, 25, 32, 37, 39, 40, 47, 59** — the largest single debt.

> ch 9 — "This is the way of the cosmos." → *the way of nature*
> ch 10 — "As the gates of the cosmos open and close" (天門)
> ch 16 — "Sovereignty leads to the cosmos." (王乃天)
> ch 22 — "no one in the cosmos can compete with them" (天下 → **the world**)
> ch 23 — "If the cosmos can't sustain intensity for long" (天地)
> ch 25 — "before the cosmos was born" (先天地生)
> ch 32 — "The dual nature of the cosmos unites to create sweet dew." (天地相合)
> ch 37, 39, 40, 47, 59 — same pattern

Note these are **three different words** flattened to one English term: 天地 (sky and earth), 天下 (the world), and 天 alone (nature). Separate them during the sweep.
*Ruling: `glossary/tiandi-天地.md`; standing principle in `notes/translation.md`.*

## 萬物 → "the ten-thousand things" *(never "all things" / "the myriad things")*

**11 chapters: 1, 8, 10, 30, 32, 34, 37, 39, 41, 42, 51.**

> ch 1 — "the mother of all things" → *the mother of the ten-thousand things*
> ch 32, 34, 37 — "the myriad things"

Frequent and mechanical; a good first sweep.

## 玄 → "dark / profound" *(never "mystery")*

**6 chapters: 4, 6, 10, 15, 51, 65.**

> ch 4 — "its source is a mystery that's older than god" — **also flag "god"** (象帝之先; 帝 is the high ancestor, not a deity in the Western sense)
> ch 6 — "the mysterious womb of creation" (玄牝) → *the dark female*
> ch 10 — "the mysterious mirror" (玄覽)
> ch 15 — "subtle, mysterious, profound, and penetrating" (微妙玄通) — the one place 妙 and 玄 sit side by side; they must read as *different* qualities
> ch 51, 65 — "mysterious integrity" (玄德) → *profound integrity*

*Ruling: `glossary/xuan-miao-玄妙.md`.*

## 常 → "the ever-present" *(never "eternal" / "everlasting")*

**4 chapters: 7, 16, 22, 46.**

> ch 7 — "The earth is everlasting." (天長地久)
> ch 16 — "Returning to your original nature is called the eternal." (復命曰常)
> ch 22 — "therefore is eternal"
> ch 46 — "eternal contentment"

*Ruling: `glossary/chang-常.md`. Chapter 1 is already clean.*

## 一 → lowercase "the one" / "unity" *(never capital-O "the One")*

**4 chapters: 10, 22, 39, 42.** Capital-O imports Neoplatonism and monotheism. In 42 the Tao *gives birth to* it, so it cannot be ultimate.

## 義 → "duty / rightness" *(never "righteousness")*

**3 chapters: 18, 19, 38.** "Righteousness" is Pauline. Also review **仁** in the same lines — "benevolence" is Legge's Victorian moralism; *humaneness* or *kindness* is closer.

## 知足 → "knowing you have enough" *(never "fulfilled")*

**Chapter 33** — "One who is fulfilled is truly wealthy."
*Ruling: `glossary/zhizu-知足.md`.*

---

## Undecided — settle these *before* sweeping

**明** — 知常曰明 is a *repeated formula*, verbatim in **16** and **55**. Currently rendered differently in each. Lock it, then make both identical. Candidates: *clear-seeing* · *illumination*.

**無為** — "non-action" leads. Lock it where the paradox lives, then sweep.

**正 / 奇** — threaded *straight / crooked* across **57–58**; confirm the thread holds, since 58 deliberately dissolves 57 (正復為奇).

---

## Structural

**`process/legacy-tao-source-code.md`** — the original "Tao Source Code" glossary, archived for provenance. Contains renderings since retired (**德 as "Virtue"**, **天 as "The Cosmos"**) and the "operating system" framing now demoted to a commentary lens. Supersede entry by entry into `glossary/`, or leave clearly marked as historical.

**`chapters/tao-opencosmos.code-workspace`** — an editor workspace file sitting inside `chapters/`; move it to the repo root or delete it, so `chapters/` contains only chapter files.

**Chapters 1–38 generally** — drafted before most locks. Treat as a single sweep rather than chapter-by-chapter spot fixes.
