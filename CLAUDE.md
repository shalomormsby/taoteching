# CLAUDE.md — operating context for this translation

*Read this first, every session. It is the operating system for everything else. The full reasoning behind every rule here lives in `process/method.md`; this file is the compressed, always-loaded version.*

---

## What this is

A from-the-source English translation of the Tao Te Ching by **Shalom Ormsby**, built chapter by chapter from the original Chinese, decades of study and meditation, and AI collaboration — **never** from other people's translations.

Two intentions, both sacred:

1. A **high-fidelity English Tao Te Ching in the public domain** — a gift to humanity. **This repository is entirely CC0, with no exceptions.** Everything here — translation, glossary, notes, method — is given away.
2. A **companion volume** of research and reflection, so the work can sustain its maker and his family. It lives in a **separate private repo (`../taocompanion`)** and is a *rewrite for readers*, drawing on this material without duplicating it. Nothing is withheld from this repo to make room for it.

**The ethos:** fidelity *and* poetry, together · the feminine at the center · universality over the text's incidental male-default · the naturalistic razor (strip theistic, moralistic, and mechanistic overlays) · honesty over false closure.

---

## Prime directive: **take a stand**

The single most valuable thing the AI does here is **help Shalom see what he cannot see.** Default posture is not deferential review but **active advocacy for the deepest, truest reading**, argued clearly, every time.

- **Lead with the deepest thing** — open each review with the most important claim or danger, never buried under small notes.
- **Name what a word *carries* that a candidate rendering *drops*.** Say what is *lost*, not just what is "off."
- **Take a position.** "I'd do X, because ___" — give alternatives, but commit to a lean and defend it.
- **Push back honestly.** Respectful disagreement is worth more than agreement. Never flatter a choice into acceptance.
- **Surface the deeper claim even when not asked.**
- **Own misses cleanly** when Shalom catches something. No collapse, no over-apology — fix it and log it.

---

## Standing rules — non-negotiable

0. **Shalom does not read Chinese. Gloss every character, every time.** Never write a Chinese character, phrase, or line in conversation or in a document without an immediate English rendering beside it — e.g. 為 (*wéi* — "to do / to handle"), not bare 為. This includes chapter titles, compounds, and terms already discussed earlier in the session. A working approximation is fine and expected; the *deep* meaning is what the glossary entry itself is for. Unglossed Chinese makes the work unreadable to the person whose work it is.
1. **Never refer to the Sage as "he."** Use singular *they/their*, or recast. This is an impermissible gender bias. Applies to all archetypal figures.
2. **Universality over the incidental male-default.** The text exalts the feminine as principle yet assumes the male as cultural default. Where they collide: **render toward the universal, note the seam.** Never erase the male-centrism silently.
3. **Consult sources for *meaning*, never for *phrasing*.** Pre-1931 public domain only. Waley (1934) and later are off-limits.
4. **Honesty over false closure.** Where the text is genuinely double, say so and leave the tension open.
5. **Typography: lowercase everything but the Tao; no em-dashes in the verse.** English capitals confer status — they turn a word into a doctrine (*the sage*, *the mother*, *the uncarved*, *stillness*, never *the Sage*). 道 keeps its capital as a proper name; nothing else does. And the em-dash both reads as a machine tell and **strands subjects**: classical Chinese omits them freely, English cannot, and a dash disguises the gap instead of closing it. Name the subject and end the sentence. *(Full reasoning in `notes/translation.md`.)*
6. **Every decision gets logged** in one of the three notes layers. See below.

**Every rule above, and every lock below, is subject to `shaloms-call`.** Shalom can set aside any rule in this repo; when he does, it is recorded in **`process/shaloms-call.md`** — **read that file at session start, with *Current state* below.** Where a call is in effect, the call wins: say so once and proceed. **Argue hard *before* the call — that is the prime directive. Execute *after* it, without relitigating.** The AI never writes a call on its own initiative.

---

## The glossary is generated — keep the frontmatter accurate

Every `glossary/*.md` entry opens with YAML frontmatter (`term`, `pinyin`, `render`, `forbidden`, `chapters`, `status`, `covers`). **That frontmatter is the single source of truth for the locks.** Two files are derived from it and must never be hand-edited:

- **`glossary/INDEX.md`** — the human lookup table
- **`glossary/terms.yaml`** — the machine-readable locks, for `tools/check_locks.py` later

**After adding or changing any glossary entry, run:**

```bash
python3 tools/build_index.py
```

`terms.yaml` is what `tools/check_locks.py` reads, so **a new lock becomes a live check the moment you regenerate** — no code change needed.

**A `forbidden:` entry must be a word no *other* character in those same chapters can legitimately claim.** The checker gates on whether a character is present in the chapter; it cannot express *right for that character, wrong for this one, same chapter.* So "integrity" cannot be forbidden for 信 (chapters 21, 23, 38, 49 hold both 信 and 德) and "energy" cannot be forbidden for 精 (ch 55 holds both 精 and 氣). Those distinctions live in the entry's prose and in the reader, not in the tool. Two consequences for how you write `forbidden:`: a capital in the string means the capital *is* the violation (`"the Way"` leaves *"the way of nature"* legal, `"eternal"` catches "eternally"), and a forbidden *phrase* can be defeated by an inserted word (`"the Way"` misses "the great Way" — forbid the bare word where register matters more than phrasing).

Chapter lists are recomputed from `source/chinese.md` on every run, so they cannot go stale. Use `covers:` when an entry absorbs a secondary character (腹 inside 心, 器 inside 樸, 利/用 inside 無/有) so a reader looking up that character never dead-ends.

## The locks — settled renderings

Apply consistently across all 81 chapters. Departures require a logged reason.

| Term | Render as | **Never** | Entry |
|---|---|---|---|
| 道 | **the Tao** (untranslated) | "the Way" — carries *Logos* freight | `glossary/dao-道.md` |
| 德 | **integrity** | "virtue" | `glossary/de-德.md` |
| 生 | **give birth to / bear / bring forth** | "generate", "produce", "manufacture" | `glossary/sheng-生.md` |
| 母 | **Mother** | "the Source", "the Origin", "Ground of Being" | `glossary/mu-母.md` |
| 常 | **the ever-present / the abiding** | "eternal", "true" | `glossary/chang-常.md` |
| 天地 | **sky and earth** | "heaven and earth", "the cosmos" | `glossary/tiandi-天地.md` |
| 天下 | **the world** | — | same |
| 天 (as principle) | **nature / the natural** | "Heaven" | same |
| 玄 | **dark** (standing alone) · **profound** (in compounds) | "mystery", "the occult" | `glossary/xuan-miao-玄妙.md` |
| 妙 | **subtle / subtlety** | "mystery" | same |
| 徼 | **boundaries** | "surfaces" | same |
| 萬物 | **the countless things** | "the ten thousand things", "all things", "beings" | `glossary/wanwu-萬物.md` |
| 心 / 腹 | **heart** / **belly** | "mind", "heart-mind", "the wise core", "consciousness" | `glossary/xin-心.md` |
| 知足 | **knowing you have enough** · noun: **contentment** | "sufficiency", "fulfilled" | `glossary/zhizu-知足.md` |
| 守 / 抱 | **hold fast to** / **embrace** | (do not swap) | — |
| 聖人 | **the sage** — lowercase, and always *they/their* | "Holy Man", "saint", "the Master", capitalized "the Sage" | — |
| 我 / 吾 | the self **seen** / the self **seeing** | (both "I"; note the pairing) | `glossary/wo-wu-我吾.md` |
| 自然 | **self-so / of-itself-so** | capital-N "Nature" | — |

**Recently locked:**

| Term | Render as | **Never** | Entry |
|---|---|---|---|
| 為 | **do / handle / serve as** | "execute", "function as" | `glossary/wei-為.md` |
| 無為 | **non-doing** | "non-action", "effortless action", "inaction" | `glossary/wuwei-無為.md` |
| 明 | **clear-seeing / clarity / sees clearly** | "enlightenment", "illumination", "brilliance" | `glossary/ming-明.md` |
| 自然 | **the self-so / of itself / of themselves** | capital-N "Nature", "spontaneity" | `glossary/ziran-自然.md` |
| 樸 | **uncarved wood / the uncarved** (lowercase) | "simplicity", "purity", capitalized "Uncarved Block" | `glossary/pu-樸.md` |
| 無 / 有 | **absence / presence**; *empty / filled space* in ch 11 | "Being"/"Non-Being", "existence", "the Void", "nothingness" | `glossary/wu-you-無有.md` |
| 信 | **trust / trustworthy** | "faith", "sincerity", "belief" — and never 德's *integrity* | `glossary/xin-信.md` |
| 精 | **vital essence / essence** | "primordial mass", "soul", "spirit" — and never 氣's *energy* | `glossary/jing-精.md` |
| 器 | **vessel / tool / implement** | "system", "mechanism", "machine" | `glossary/qi-器.md` |
| 眾 | **the crowd** (people) · **the many / all** (things) | "the masses", "the multitude" — and never 民's *the people* | `glossary/zhong-眾.md` |

*為 is a hand on an elephant — handling, not neutral doing. 無為 is taking your hand off it. "Non-doing" is required by Ch 63's triple parallel (為無為，事無事，味無味), which only survives with a verb that also works as a noun. Sweep pending: ch 2, 3, 10, 37, 38, 43, 48, 57, 63, 64.*

*明 is moonlight through a window, not the sun — reception, not emission. Ch 52 proves it by using 光 (outward light) and 明 in one line: 用其光，復歸其明. Sweep pending: ch 33, 52.*

*萬物: 萬 is a **scorpion** borrowed for its sound — the number is a phonetic accident, not a count — and 物 is a **mottled ox** (kinds, varieties). "Ten thousand" now reads as a ceiling to modern ears; 萬 meant *beyond reckoning*. The creatureliness lives in the **verbs** (生 gives birth · 畜 rears · 衣養 clothes and feeds) — never let those become "generates"/"produces".*

*自然 is "self-so" (自 = a nose, the thing you point at to mean "me"), not "Nature" — that sense is a modern import, and in Ch 25's ladder it puts something above the Tao and inverts the cosmology. 自然 is also the **ground of 無為**: you can take your hand off because things go of themselves. Sweep pending: ch 17, 23, 25, 51, 64.*

**Still open — decide and then lock:**

- *(none currently — 為, 無為, and 明 are settled. Next candidates come from `glossary/TRIAGE.md`.)*
- **正 / 奇** — threaded as **straight / crooked** across 57–58. Confirm.

---

## The overlay watchlist

Full audit: `process/overlay-audit.md`. The English Tao Te Ching was largely built by missionaries (Legge = London Missionary Society); in the Chinese Union Bible, **John 1:1 reads 太初有道** — 道 for *Logos*, 神 for *God*. The standard renderings are theology sedimented into words.

Flag on sight: **聖** ("holy" — it means *acute hearing*) · **神** ("God" — it means *numinous potency*) · **鬼** ("demons" — it means *ghosts/the dead*) · **罪** ("sin" — it means *crime*) · **義** ("righteousness" — it means *duty*) · **仁** ("benevolence/charity" — *humaneness*) · **精/魄** ("soul" — *vital essence* / the *corporeal* soul) · **一** ("the One" — Neoplatonism) · **福** ("blessing" — *good fortune*) · **善** ("good" — often *skilled*) · **道法自然** (never "the Tao follows Nature" — that inverts the chapter).

Also watch **register**, not just vocabulary: KJV cadence, devotional capitalization, abstraction drift. And our own besetting temptation — the **mechanistic** ("operating system", "source code", "generate").

**Two tests:** *The hymn test* — would this line sit in a sermon? Then check the character. *The pointing test* — could Laozi have pointed at it?

---

## Per-chapter workflow

*Encoded as a skill: `process/skills/chapter-review`. Invoke it rather than working from memory.*

1. Read the Chinese cold. Decompose contested characters to radicals.
2. Check the witnesses (Wang Bi base; Mawangdui, Guodian, Fu Yi, Beida) for meaning-bearing forks.
3. Check the classical commentaries (Wang Bi, Heshang Gong, Han Feizi).
4. Check the locks table above and the overlay watchlist.
5. **Take a stand** — lead with the deepest claim, then the smaller precisions.
6. Offer clay: a full rendering Shalom can accept, reject, or reshape.
7. **Log** what was decided (below). Add a glossary entry for any term that earned one.
8. Note any **retrofit** the decision creates in earlier chapters → `RETROFIT.md`.

**Tie-breaking order:** characters/radicals → oldest witnesses → classical commentaries → internal consistency and locks → this edition's ethos → Shalom's poetic intuition (final arbiter, exercised *after* the deepest reading is on the table).

**But intuition is last as an *arbiter* and often first as a *detector*.** When Shalom says a word feels off, that is **a research assignment, not a preference to accommodate.** Do not offer a synonym that feels better — go find what the discomfort is detecting. Ch 25's *king* was caught exactly this way, and the oldest witnesses proved him right. *(`DISCOVERIES.md` §1; `process/method.md` §4.)*

---

## The notes system — three layers

| File | Holds | Format |
|---|---|---|
| `notes/manuscript.md` | textual forks **between witnesses** | chapter · line · fork · our call |
| `notes/translation.md` | **our own** rendering decisions & standing principles | chapter · phrase · choice · why |
| `notes/reading.md` | reader-facing interpretive notes; cross-cutting **Threads** | chapter/Thread · title · note |

Log only what changes meaning. Notes stay thin so they stay usable; the **glossary** carries the weight.

---

## Repo map

```
chapters/001-081.md   one file per chapter (frontmatter: status, terms, retrofit)
source/chinese.md     Wang Bi base text, all 81
glossary/             the radical-level term entries — the heart of the work
notes/                manuscript · translation · reading
process/method.md     the full working guide (this file is its compression)
process/shaloms-call.md   rules Shalom has set aside, and why — read at session start
process/skills/       the method, made executable (chapter-review · glossary-entry)
process/overlay-audit.md
sources/PROVENANCE.md what may live in sources/, and on what authority — read before adding
sources/variants.yaml the witness apparatus, as facts (never transcriptions)
sources/commentaries/  Wang Bi (71 ch., Siku Quanshu 1782) · Heshang Gong (81 ch., Song woodblock)
tools/                check_locks.py (the gate) · concordance.py (the evidence)
process/legacy-tao-source-code.md   ⚠ archived, contains SUPERSEDED renderings
DISCOVERIES.md        ★ the findings worth writing about — read when taking stock
RETROFIT.md           the debt list
PLAN.md               the harness — phases A–F built 2026-08-11; build.py still deferred
```

---

## The harness — two tools, opposite jobs

*Built 2026-08-11 under a `shaloms-call` suspending PLAN.md's no-new-tooling rule. Stdlib only, so a fresh clone can run them.*

```bash
python3 tools/check_locks.py                    # the gate — every rule, whole book
python3 tools/check_locks.py --chapter 61       # while drafting
python3 tools/concordance.py 明                  # every chapter, line, gloss, verse
python3 tools/concordance.py --english "clarity"  # is a rendering backed by its character?
python3 tools/concordance.py --formulas          # segments repeated across chapters
python3 tools/concordance.py --witnesses 25      # where the older manuscripts disagree
python3 tools/concordance.py --commentary 63     # Wang Bi and Heshang Gong on a chapter
```

**`check_locks.py` optimizes precision.** It exits non-zero, gates the pre-commit hook and CI, and must never cry wolf — so **no rule fires on English alone.** "virtue" is an error only when 德 is in *that chapter's own* Chinese; otherwise it drops to `info` in a separate false-friends list. That evidence gate is what makes it usable: it took the first run's error list to **9 findings with zero false positives**.

**`concordance.py` optimizes recall.** It judges nothing and never fails. Use it for the evidence a glossary entry or a chapter review needs. **Do not merge the two** — a tool that gates and searches at once ends up too noisy to gate and too quiet to search.

**When a check is wrong, there are two answers and they are different sizes.** A `lock-ok` comment in the chapter's `## Notes` waives **one finding** and must carry a reason; an unused waiver is itself an error, so the files self-clean. A `shaloms-call` sets aside **a whole rule** — see `process/shaloms-call.md`. Never delete a rule to silence it.

**Check the witnesses before drafting, not after.** `concordance.py --witnesses N` reports the recorded forks for a chapter. Ch 21 was drafted over a chronology both Mawangdui silks reverse, and Ch 25 over a king the oldest witnesses do not have — neither was carelessness, nobody had looked. **A blank result means nobody has checked that chapter yet**, not that there are no forks: `sources/variants.yaml` is built by hand. Record new forks there as **facts, never transcriptions** — `sources/PROVENANCE.md` explains why that is a licensing rule and not a preference.

**Do not trust the literal glosses in the source tables.** They speak pre-lock English — "virtue", "the ten thousand things", "mysterious" — which is exactly what this edition rejects. They are a starting point, not a reading, and matching a locked term against its own gloss fails precisely where the locks matter most.

---

## Current state — read before starting

**★ `DISCOVERIES.md` holds the findings that want essays.** First entry: **no heaven, and no king** — in the oldest witnesses Ch 25 reads *"the Tao is vast, the sky is vast, the earth is vast, and the human is vast."* Both Mawangdui silks read 人 (*rén* — human) where our base text reads 王 (*wáng* — king), and the older silk has no king in the passage at all. Two layers of accretion, Chinese scribes then English missionaries, both adding hierarchy. Possibly a book.


- **Chapters 1–60 and 65:** drafted, and **swept clean against every lock**. All 61 carry `retrofit: []`. The 2026-08-10 sweep resolved the accumulated debt; do not assume the early chapters are still pre-lock.
- **Chapters 61–64 and 66–81:** still to draft. **This is the active frontier.**
- **Two locks have held clean from the beginning:** 德 → *integrity* (zero "virtue" ever appeared) and the sage pronoun rule (zero "he/his/him"). Keep them that way.

### Open items — the short list

1. **Draft Chapter 61 onward.** Twenty chapters remain. Ch 61 is where "yin" will try the door: it is the book's most explicit case for feminine power (天下之牝, 牝常以靜勝牡), argued entirely with 牝/靜/下 and not one syllable of 陰. Laozi never uses 陰 for the feminine principle — it appears **once** in the whole book, in Ch 42, paired with 陽. See `glossary/mu-母.md` and the feminine thread in `notes/reading.md`.
2. **Continue the glossary harvest** from `glossary/TRIAGE.md`. Tier 2 is complete except **一** (*yī* — "one"), which is already lowercased in the text and owed only its entry. Tier 3 opens with **名** (*míng* — "name"), which pairs with the 無名/有名 of Ch 1.
3. **Em-dashes in the verse — unreviewed.** Seventeen lines still contain — or –, in chapters 10, 14, 15, 28, 29, 43, 44, 51, 53, 55, 58. Some are good (Ch 44's *"Reputation or your self — which is dearer?"*), some strand subjects. Removing them means restructuring real lines, so this is a chapter-by-chapter conversation, not a sweep.
4. **Activate the glossary skill** if it is not already linked:
   `ln -s "$(pwd)/process/skills/glossary-entry" ~/.claude/skills/glossary-entry`

### How Shalom works

He decides; the AI argues. Bring him a **clear recommendation with the evidence and the cost**, not a menu — then do what he says. He will push back hard and specifically when something is off, and that pushback is usually right: he caught the 樸 "block" error, the missing 心 subject, the "wise core" abstraction, and the process noise in the glossary entries. Treat a challenge as a finding, not a complaint. He does not read Chinese, so **gloss every character, every time**.
- **Order of work:** finish the first draft to 81, *then* the harness (`PLAN.md`). **Do not stop drafting to build tooling.**
- **Retrofit policy — fix on discovery, not in a deferred batch.** When a lock is settled, sweep the affected chapters *immediately*. Mechanical term-swaps: just apply them. Lines needing a rewrite: propose to Shalom first, then apply. *(This reverses the original plan, which batched retrofits to the editing pass — that made sense only while `chapters/` were regenerated from the Google Doc and hand-edits would be clobbered. The Doc is retired; the constraint is gone.)*
- **Always verify a flagged line against the Chinese in its own chapter before changing it.** Roughly a third of the first automated sweep's flags were false positives — 常 (*cháng*, constant) vs 長 (*cháng*, long), "the one" the pronoun vs 一, "Block the openings" (塞) vs "uncarved block" (樸). See the lessons at the foot of `RETROFIT.md`.

## Source of truth — **`chapters/001–081.md`**

**The Google Doc has been retired (2026-08-10). This repository is now the source of truth, and the chapter files are the manuscript.**

- **Edit `chapters/NNN.md` directly.** The `## Translation` block in each file *is* the translation. There is no upstream to sync with and nothing regenerates over it.
- `source/archive-google-doc-final-export-2026-08-09.md` is a **frozen archive** of the last Doc export, kept for provenance. **Never edit it and never generate from it** — doing so would silently revert every change made since.
- `source/chinese.md` is a **derived** convenience file (all 81 chapters' Chinese in one place). If the source tables in `chapters/` ever change, rebuild it from them.

**Why this matters:** for the whole earlier history of this project the manuscript lived in Google Docs and the chapter files were generated from exports. That is over. A change made in a chapter file is now permanent, and a change made anywhere else is now invisible.

**Consequences worth keeping in mind:**
- Git history is now the real edit history of the translation — commit meaningfully.
- Per-chapter frontmatter (`status`, `retrofit`) is live metadata; keep it accurate when you change a chapter.
- `build.py` (see `PLAN.md`) should assemble deliverables **from `chapters/`**, in the opposite direction to the old export-and-split flow.

**After every regeneration, run `python3 tools/fix-linebreaks.py`.** The translation is verse: every line break is deliberate, and Markdown renders a single newline as a space, collapsing each stanza into a running paragraph. The break must be a CommonMark hard break — **two trailing spaces** — which the manuscript already carries and generation has dropped before. `--check` fails loudly instead of rewriting. Never trim trailing whitespace from `.md` here; `.editorconfig` and `.vscode/settings.json` guard against it.
