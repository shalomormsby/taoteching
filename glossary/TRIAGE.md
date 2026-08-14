# Glossary triage — harvesting the early version

*Working document. The early glossary (`process/legacy-tao-source-code.md`) holds **48 entries** written partly in this project's voice and partly in a computational/thermodynamic framework applied by an earlier AI collaborator. This file classifies all of them, sets the harvest order, and records the rules for doing it. Delete once the harvest is complete and `INDEX.md` supersedes it.*

**Frequency counts below are real** — computed against `source/chinese.md`, all 81 chapters. They are the primary priority signal, alongside whether a term blocks current work.

---

## The rules for this harvest

**1. Verify; never inherit.** The early glossary contains at least one demonstrable error — 天 titled "The Cosmos," disproven by evidence from seven chapters. The same source wrote every etymology in it. So each graph claim is re-checked against Shuowen and oracle-bone/bronze forms, and each "Laozi uses this in chapter X" is re-checked against the actual text. Nothing carries forward on trust.

**2. Extract the observation; discard the metaphor.** The framework occasionally produced a true insight in wrong clothes. 心 "is prior to the heart/mind split" is correct and valuable; "mechanical processor," "the UI where consciousness meets reality," "overheats the system" are not. Keep the first, cut the second.

**3. Reject framework-generated renderings outright.** 成 → "Compiled / The Final Build" is not a candidate to weigh. It is an artifact of the metaphor and would corrupt the lock.

**4. Why this matters beyond style.** "The universe is software" implies a programmer. The mechanistic overlay smuggles in a designer exactly as "Heaven" smuggles in a God — the same error in different clothes. The 生 entry spent 1,500 words establishing that the cosmos was *borne, not built*; an entry saying the Tao "compiles" reality quietly restores the creator it removed.

**5. Rewrite to the standard, don't patch.** Every harvested entry is rebuilt to the established form: open with a live problem → read the character as a picture changing over time → let cross-textual evidence argue → name what is set aside → leave the real tension open. Both tests apply to every sentence — the **hymn test** and the **pointing test**. The computational frame fails the second as badly as the theological frame fails the first.

**6. One entry at a time.** These are the heart of the work. Better twelve excellent entries than thirty-seven adequate ones.

---

## Tier 0 — Do not harvest

**Superseded — the repo has better versions.** 道 · 德 · 生 · 母 · 常 · 玄 · 妙 · 我/吾
*(Check the old 吾 entry, 41 lines, for any detail the pairing entry didn't absorb; likewise 吾 vs 身.)*

**Merged.** 食母 (ch 20) — already covered inside the 母 entry.

**Rejected.**

| Entry | Why |
|---|---|
| 成 (Chéng), "Compiled" | 28 framework markers, the most contaminated in the file. The etymology (戊, the battleaxe; the decisive strike ending a process) is sound and worth keeping — but as a *note*, not this entry. The rendering is an artifact. |
| 天 (Tiān), "The Cosmos" | Superseded and disproven by `tiandi-天地.md`. |

**Not glossary entries at all** — zero occurrences in the text:

| Entry | Move to |
|---|---|
| 經 (Jīng), "Book" | Companion front matter — it explains the title, not a term |
| 老子 (Lǎozi) | Companion front matter — biography |

---

## Tier 1 — Blocking current work

| # | Term | Chapters | Old state | Why first |
|---|---|---|---|---|
| ~~1~~ | ~~**為** (Wéi) — "to do / to handle"~~ | 48 | — | ✅ **DONE** → `wei-為.md`. Found: the character is a hand on an **elephant**. |
| ~~2~~ | ~~**無為** (Wúwéi) — "non-doing"~~ | 10 | — | ✅ **DONE & LOCKED** → `wuwei-無為.md`. "Non-doing," not "non-action"; Ch 63's triple parallel decided it. |
| ~~3~~ | ~~**明** (Míng) — "clear-seeing"~~ | 12 | — | ✅ **DONE & LOCKED** → `ming-明.md`. Found: the old form 朙 is **moonlight through a window**. Ch 52's 用其光，復歸其明 decided it. 16/55 already agreed. |
| ~~4~~ | ~~**自然** (Zìrán) — "the self-so"~~ | 5 | — | ✅ **DONE & LOCKED** → `ziran-自然.md`. 自 is a **nose** — the part you point at to mean "me." Ch 25's ladder terminates; it does not reach past the Tao. |
| ~~5~~ | ~~**樸** (Pǔ) — "uncarved wood"~~ | 6 | — | ✅ **DONE & LOCKED** → `pu-樸.md`. 器 (vessel) is its counter-term; carving = naming = assigning function. Ch 57's "plain" confirmed as a licensed flexion. |
| ~~5b~~ | ~~**器** (Qì) — "vessel"~~ | 9 | *(was inside `pu-樸.md`)* | ✅ **DONE & LOCKED** → `qi-器.md`. Promoted out of 樸's `covers:` to its own entry: nine chapters is too much reach to be a footnote, and Ch 41 / Ch 67 use the **capacity** sense of 器 that 樸's entry had no room for. *Shuowen*: 皿也，象器之口，犬所以守之 — a yard of pots with a dog guarding them. |
| ~~5c~~ | ~~**眾** (Zhòng) — "the crowd"~~ | 6 | — | ✅ **DONE & LOCKED** → `zhong-眾.md`. Had drifted into four Englishes, including dropped entirely in Ch 8. Oracle bone shows labourers under the **sun** (later an eye) — the many who are worked and watched. Distinguished from 民 (the governed populace) and 百姓. |

**✅ Tier 1 complete.** Next: Tier 2, beginning with **無 / 有** (*wú / yǒu* — "absence / presence"), which appears in 40 chapters and currently has an eight-line stub.

## Tier 2 — High frequency, high value

| # | Term | Chapters | Old state | Note |
|---|---|---|---|---|
| ~~6~~ | ~~**無 / 有** — "absence / presence"~~ | 40 | — | ✅ **DONE & LOCKED** → `wu-you-無有.md`. 有 is a hand holding meat; 無 was originally a **dancer**. Ch 11's 無 is a literal hole. **Absorbs the old 利/用 pairing.** |
| ~~7~~ | ~~**萬物** — "the countless things"~~ | 27/16/17 | — | ✅ **DONE & LOCKED** → `wanwu-萬物.md`. **Three entries consolidated into one.** 萬 is a scorpion; 物 is a mottled ox. |
| ~~8~~ | ~~**心** (Xīn) — "heart"~~ | 6 | — | ✅ **DONE & LOCKED** → `xin-心.md`. The character is an **anatomical drawing** of the organ. English idiom (*learn by heart*, *change of heart*) never fully split heart from mind, so no hyphen needed. **Absorbs the old 腹 entry** — 腹 = *belly*, its counter-term, not "the wise core." |
| 9 | **一** (Yī) | 8 | 37L, 14 marks | Overlay watchlist — capital-O "the One" imports Neoplatonism. In Ch 42 the Tao *gives birth to* it, so it cannot be ultimate. |

## Tier 3 — Worth writing

| # | Term | Chapters | Old state | Note |
|---|---|---|---|---|
| 10 | **名** (Míng) | 9 | 51L, 10 marks | Ch 1 and 32. Pairs conceptually with 無名/有名. |
| 11 | **始** (Shǐ) | 7 | 47L | Consider as a **pairing with 母** — beginning vs. mother, the two halves of Ch 1's second couplet. |
| ~~12~~ | ~~**信** (Xìn) — "trust"~~ | 8 | 42L | ✅ **DONE & LOCKED** → `xin-信.md`. 人 beside 言 — a person by their word — and also a **split tally** (符契), so 信 is *correspondence that can be checked*, not an inner feeling. That is why "sincerity" and "faith" both fail. Kept being given 德's word: fixed in Ch 23 and Ch 38. Ch 49's 德信 puts both characters in one compound and settles it. 忠 (loyalty) absorbed here. Ch 81's 信言 left open until that chapter is drafted. |
| 13 | **王** (Wáng) | 8 | 41L, 11 marks | **Raised in priority.** Both Mawangdui silks read 人 (human) where our base reads 王 (king) in Ch 25's four greats, and the older silk has no king in the passage. See `DISCOVERIES.md` §1 — this entry now has a real argument to make. |
| 14 | **先** (Xiān) | 6 | 42L, 13 marks | |
| ~~15a~~ | ~~**精** (Jīng) — "vital essence"~~ | 2 | 36L | ✅ **DONE & LOCKED** → `jing-精.md`. 米 (rice) + 青; *Shuowen*: **擇也**, to sift. **Hulled grain** — what is left when the bulk is removed, which is why Ch 21's "primordial mass" was the exact inversion. Written **standalone, not paired with 氣**: Ch 55 sets them against each other (精 a reserve, 氣 a current), and a paired entry would blur the distinction the chapter is built on. |
| 15b | **氣** (Qì) | 3 | 21L | **Now owed.** 精 is locked and argues against it by contrast, so 氣 needs its own entry to complete the pair. Note that "energy" cannot go on 精's forbidden list precisely because 氣 claims it in Ch 55. |
| 16 | **混** (Hùn) | 3 | 29L | Ch 25's 有物混成. |
| 17 | **反 / 復** | 4 | 6L stub | A true pairing — the movement of the Tao. Currently framed as "a thermodynamic loop"; needs full rewrite. |
| 18 | **仁** (Rén) | 5 | 21L | Overlay watchlist — Legge's "benevolence," never "charity." |

## Tier 4 — Stubs needing commission

Each is 6–14 lines; these are seeds, not drafts.

~~**事**~~ *(entry written 2026-08-12 — `shi-事.md`; a hand holding the badge of office, the second hand beside 為's elephant. 無事 left open)* · **容** (4) · **愚** (3) · **命** (2) · ~~**腹**~~ *(absorbed into `xin-心.md`)* · **敦** (1) · **芻狗** (1) · **上善** (1) · **大制** (1)

---

## Relocations — these are not glossary entries

| Entry | Destination | Why |
|---|---|---|
| **利 / 用** | `notes/translation.md` | Not what the characters mean — a choice made in English ("stripping the capitalist static"). A rendering decision. |
| ~~**公**~~ / **仁** | `notes/translation.md` | 公 has its own entry as of 2026-08-12 — `gong-公.md`; the Shuowen cites Han Feizi for its etymology. 仁 still here. |
| **經**, **老子** | Companion front matter | Zero occurrences in the text. |

---

## Pairings — the standing decision

**True lexical pairs stay in `glossary/`.** Two characters that cannot be explained apart, where the meaning lives in the seam: **我/吾**, **玄/妙**, **無/有**, **反/復**, and possibly **始/母** and **精/氣**. A glossary of a philosophical text is not a dictionary — it is a lexicon of *how this book uses words*, and some words are only usable in pairs.

**The lookup problem is solved separately**, by `glossary/INDEX.md`: every character mapped to its entry, pairings included, with the locked rendering beside it. That file also becomes the seed for `terms.yaml` in `PLAN.md`.

**The pairing standard is already written** — it heads the Pairings section of the early glossary, in this project's voice:

> *"The meaning lives in the space between the two words, not in either alone. Read the characters against each other; be honest about where the language earns the contrast and where we are supplying it; find the passage where the text itself sets the pair in tension (e.g., Zhuangzi's 吾喪我); and let the pairing open rather than close — most of all when the seam it marks is one the reader may be living from the inside."*

It needs a permanent home in `process/method.md` §6.

---

## Tally

| | Count |
|---|---|
| Entries in the early glossary | 48 |
| Already superseded or merged | 11 |
| Rejected / relocated | 6 |
| **To harvest or commission** | **~31** |
| Of those, substantial drafts | ~16 |
| Of those, stubs needing writing from scratch | ~15 |
