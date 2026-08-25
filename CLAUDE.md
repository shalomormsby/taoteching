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
| 母 | **mother** | "the Source", "the Origin", "Ground of Being" | `glossary/mu-母.md` |
| 常 | **the ever-present / the abiding** | "eternal", "true" | `glossary/chang-常.md` |
| 天地 | **sky and earth** | "heaven and earth", "the cosmos" | `glossary/tiandi-天地.md` |
| 天下 | **the world** | — | same |
| 天 (alone) | **sky** with 地 near · **nature / the natural** as an agent | "Heaven", "Providence", "the Cosmos" | `glossary/tian-天.md` |
| 玄 | **dark** (standing alone) · **profound** (in compounds) | "mystery", "the occult" | `glossary/xuan-miao-玄妙.md` |
| 妙 | **subtle / subtlety** | "mystery" | same |
| 徼 | **boundaries** | "surfaces" | same |
| 萬物 | **the countless things** | "the ten thousand things", "all things", "beings" | `glossary/wanwu-萬物.md` |
| 心 / 腹 | **heart** / **belly** | "mind", "heart-mind", "the wise core", "consciousness" | `glossary/xin-心.md` |
| 知足 | **knowing you have enough** · noun: **contentment** | "sufficiency", "fulfilled" | `glossary/zhizu-知足.md` |
| 守 / 抱 | **hold fast to** / **embrace** | (do not swap) | — |
| 聖人 | **the sage** — lowercase, and always *they/their* | "Holy Man", "saint", "the Master", capitalized "the Sage" | — |
| 我 / 吾 | the self **seen** / the self **seeing** | (both "I"; note the pairing) | `glossary/wo-wu-我吾.md` |

**Recently locked:**

| Term | Render as | **Never** | Entry |
|---|---|---|---|
| 為 | **do / handle / serve as** | "execute", "function as" | `glossary/wei-為.md` |
| 無為 | **non-doing** | "non-action", "effortless action", "inaction" | `glossary/wuwei-無為.md` |
| 明 | **clear-seeing / clarity / sees clearly** | "enlightenment", "illumination", "brilliance" | `glossary/ming-明.md` |
| 自然 | **of itself / of themselves · so of itself** | capital-N "Nature", "spontaneity", "self-so" | `glossary/ziran-自然.md` |
| 樸 | **uncarved wood / the uncarved** (lowercase) | "simplicity", "purity", capitalized "Uncarved Block" | `glossary/pu-樸.md` |
| 無 / 有 | **absence / presence**; *empty / filled space* in ch 11 | "Being"/"Non-Being", "existence", "the Void", "nothingness" | `glossary/wu-you-無有.md` |
| 信 | **trust / trustworthy** | "faith", "sincerity", "belief" — and never 德's *integrity* | `glossary/xin-信.md` |
| 精 | **vital essence / essence** | "primordial mass", "soul", "spirit" — and never 氣's *energy* | `glossary/jing-精.md` |
| 器 | **vessel / tool / implement** | "system", "mechanism", "machine" | `glossary/qi-器.md` |
| 眾 | **the crowd** (people) · **the many / all** (things) | "the masses", "the multitude" — and never 民's *the people* | `glossary/zhong-眾.md` |
| 公 | **impartiality** (quality) · **lord / minister** (office) | "duke", "equanimity", "justice" | `glossary/gong-公.md` |
| 事 | **affairs / undertakings** · **serve / attend to** | "techniques", "processes" | `glossary/shi-事.md` |
| 善 | **masterful / masterful at** · *good* only where the text names the category | "virtuous", "righteous", "saintly", "benevolent" | `glossary/shan-善.md` |
| 敢 | **push / venture** — the forward press to take | "dare", "daring" | `glossary/gan-敢.md` |
| 爭 | **contend / contention** | "compete", "competition" | `glossary/zheng-爭.md` |
| 王 | **ruler / sovereign** · *to rule* (verb) | "king", "monarch", "emperor" | `glossary/wang-王.md` |

*為 is a hand on an elephant — handling, not neutral doing. 無為 is taking your hand off it. "Non-doing" is required by Ch 63's triple parallel (為無為，事無事，味無味), which only survives with a verb that also works as a noun. Sweep pending: ch 2, 3, 10, 37, 38, 43, 48, 57, 63, 64.*

*明 is moonlight through a window, not the sun — reception, not emission. Ch 52 proves it by using 光 (outward light) and 明 in one line: 用其光，復歸其明. Sweep pending: ch 33, 52.*

*萬物: 萬 is a **scorpion** borrowed for its sound — the number is a phonetic accident, not a count — and 物 is a **mottled ox** (kinds, varieties). "Ten thousand" now reads as a ceiling to modern ears; 萬 meant *beyond reckoning*. The creatureliness lives in the **verbs** (生 gives birth · 畜 rears · 衣養 clothes and feeds) — never let those become "generates"/"produces".*

*自然 is 自 (a nose — the thing you point at to mean "me") + 然 (*rán* — **so, thus**): so because of itself. Not "Nature" — that sense is a modern import, and in Ch 25's ladder it puts something above the Tao and inverts the cosmology. 自然 is also the **ground of 無為**: you can take your hand off because things go of themselves. **Revised 2026-08-24 — "the self-so" is retired and now forbidden.** It was a calque, and a *definite noun* where 王弼 (自然者，無稱之言 — "a term that designates nothing") and 河上公 (道性自然，無所法也 — "there is nothing it models itself on") both refuse to name an entity: the same error as "Nature", smaller in degree. **Ch 25 is the deliberate exception** — the one noun slot is answered with a clause: 道法自然 → "the Tao models itself on being what it is." Swept ch 17, 23, 25, 51, 64.*

*敢 is **a hand with a hunting weapon going after a boar** — *Shuowen*: 進取也, "to advance and take." **Appetite, not bravery**, which is why "not daring" inverts the book: Ch 73's 勇於**不敢**則活 (*yǒng yú bù gǎn zé huó* — "courage in not-敢 lives") makes 不敢 *a form of courage*, and "not daring" cannot be brave. Caught by Shalom, 2026-08-19, after the reading had passed three chapters unexamined. Swept ch 30, 64, 67, 69.*

*王 reads **ruler**, not *king* — and note the forbidden string is `" king"` with a leading space, so "kingdom" stays legal. See `DISCOVERIES.md` §1, whose central claim this entry corrected.*

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

## Consult the sources — they are in the repo, and this is not optional

**The classical commentaries live in `sources/commentaries/`, and every piece of translation or refinement work consults them.** Not from memory, not from a search engine: from the files.

```bash
python3 tools/concordance.py --commentary N    # 王弼 and 河上公 on chapter N
python3 tools/concordance.py --witnesses N     # where the older manuscripts disagree
```

| | Date | Coverage |
|---|---|---|
| **王弼** (*Wáng Bì*) | d. 249 CE | 71 of 81 chapters — Siku Quanshu, 1782 |
| **河上公** (*Héshàng Gōng*) | Han | **all 81** — Song woodblock, and it covers the ten Wang Bi lacks |
| **韓非** (*Hán Fēi*), 解老 / 喻老 | d. 233 BCE | the 17 chapters he discusses — the oldest commentary there is |

**Run them before drafting a chapter and before changing a settled line.** Three of this session's findings came from exactly that and could not have come from anywhere else: Wang Bi's gloss 此上之所云也 settled the referent of 此 in Ch 21; the Siku compilers' note 〔案狀各本俱作然〕 reopened a decision made an hour earlier; Han Feizi's 大必起於小 supplied a reading of Ch 63's hardest line.

**Quote, gloss, and cite them — never copy their English.** There is no English in these files; they are the Chinese. The pre-1931 rule in standing rule 3 governs *translations*, and none are in this repository.

**When they disagree, that is the finding.** Convergence is strong evidence; divergence gets logged in `notes/manuscript.md` and, if it is a textual fork, in `sources/variants.yaml`. Do not average them into a consensus.

**Adding to `sources/` has rules.** Read `sources/PROVENANCE.md` first. The short version: public domain by age, a *nameable* edition, provenance in the frontmatter, and **never a transcription of the Mawangdui or Guodian manuscripts** — reconstructing damaged graphs is living scholarship, so record the *fact* of the variant instead.

---

## Per-chapter workflow

*Encoded as a skill: `process/skills/chapter-review`. Invoke it rather than working from memory.*

1. Read the Chinese cold. Decompose contested characters to radicals. **Then run `--commentary` and `--witnesses` on the chapter.**
2. Check the witnesses (Wang Bi base; Mawangdui, Guodian, Fu Yi, Beida) for meaning-bearing forks.
3. Check the classical commentaries — `concordance.py --commentary N`, not from memory.
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
sources/guodian-inventory.yaml  what the oldest witness (~300 BCE) contains — an inventory, never a text
sources/commentaries/  Wang Bi (71 ch.) · Heshang Gong (all 81) · Han Feizi (17 ch., oldest)
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

**Check the witnesses before drafting, not after.** `concordance.py --witnesses N` opens with whether **Guodian** (~300 BCE, the oldest witness there is) carries the chapter at all — it carries only 31 of 81, and *not attested* means the chapter rests on the silks and later, which changes how much weight they bear. Then it reports the recorded forks. Ch 21 was drafted over a chronology both Mawangdui silks reverse, and Ch 25 over a king the oldest witnesses do not have — neither was carelessness, nobody had looked. **A blank result means nobody has checked that chapter yet**, not that there are no forks: `sources/variants.yaml` is built by hand. Record new forks there as **facts, never transcriptions** — `sources/PROVENANCE.md` explains why that is a licensing rule and not a preference.

**Do not trust the literal glosses in the source tables.** They speak pre-lock English — "virtue", "the ten thousand things", "mysterious" — which is exactly what this edition rejects. They are a starting point, not a reading, and matching a locked term against its own gloss fails precisely where the locks matter most.

---

## Current state — read before starting

**★ `DISCOVERIES.md` holds the findings that want essays — read it when taking stock of what to write.** Two so far, and they are complements. **§2, the question is "is it so?", not "what is it?"** — 自然 (*zìrán* — so of itself) is 自 (*zì* — self) + 然 (*rán* — **so, that it is the case**), and 然 alone closes chapters 21, 54 and 57 on one formula: 吾何以知…然哉？以此, *"how do I know it is so? By this."* Not what a thing **is** but whether it **is so**, answered not by authority but by *this, here, now*. An ontology and an epistemology in twenty characters. **§1, no heaven and no king** — **⚠ superseded in its central claim on 2026-08-20 and awaiting rewrite; read the banner in the file before using any of it.** The *heaven* half stands: 天 (*tiān* — sky) is in every witness, "Heaven" is a missionary import, and the distortion is entirely English. The *king* half was backwards. **Every excavated witness at Ch 25 reads 王** (*wáng* — king), Guodian (~300 BCE) included; 人 (*rén* — human) is a transmitted reading from 傅奕 (Tang) and 范應元 (Song), argued on the internal seam — the next line is 人法地, *humans follow earth*. We still read 人, now as an editorial call, logged as one. The lesson worth keeping: **a popular "帛書版" text online had already been silently emended to 人**, and we took it for the silks. `sources/variants.yaml` is the apparatus; do not trust a manuscript claim that is not in it.


- **Chapters 1–72:** drafted, and swept against every lock. The 2026-08-10 sweep resolved the accumulated debt; do not assume the early chapters are still pre-lock. *(Ch 69 drafted 2026-08-23; Ch 70, 71 and 72, 2026-08-24.)*
- **Chapters 73–81:** still to draft. **This is the active frontier.** None of them is attested at Guodian — 66 is the highest-numbered chapter the oldest witness carries, so from here on the text rests on the Mawangdui silks and later.
- **⚠ `status: drafted` has been proved unreliable once. Do not trust it without looking at the page.** On 2026-08-17 Shalom found Ch 65's `## Translation` block was three ellipses and a fragment, carrying `status: drafted` and `retrofit: []`. An audit of all 81 then found **Ch 20** the same way — 10 verse lines against 25 source rows, missing its entire opening movement (絕學無憂 through 荒兮其未央哉). Both had been counted as finished by the 2026-08-10 hand sweep, by `CLAUDE.md`, and by every session since. Both are now genuinely complete. **No checker rule catches this** — every lock keys off the Chinese to judge the English, and a chapter with no English trivially passes all of them. A proposed `incomplete-draft` rule is in `PLAN.md` → *Proposed rules, unbuilt*, pending a call on `no-new-tooling`. **It was in the original §2 spec as "status coherence" and never built, inside a section stamped ✅ DONE** — which is how the gap stayed invisible.
- **⚠ `check_locks.py` does not scan `glossary/`.** The locks are enforced against the manuscript but never against the files that *define* them, so a glossary entry can contradict its own lock indefinitely. Found 2026-08-23: one line of `glossary/ziran-自然.md` carried **two** violations — a stale "dare" for 敢 and "the ten-thousand things" for 萬物, the latter forbidden outright. A proposed `glossary-self-check` rule is in `PLAN.md`, unbuilt. Until it exists, **sweep `glossary/` by hand whenever a lock is settled** — the entries are prose and the retrofit policy applies to them too.
- **Two locks have held clean from the beginning:** 德 → *integrity* (zero "virtue" ever appeared) and the sage pronoun rule (zero "he/his/him"). Keep them that way.

### Open items — the short list

1. **Draft Chapter 73 onward.** Nine chapters remain, none attested at Guodian. **Ch 71 and 72 are done (2026-08-24).** 71 extends the 20/67/70 thread: 河上公 closes it with 夫聖人**懷**通逹之知，託於不知者 — *"the sage carries penetrating knowledge against the breast and lodges it in not-knowing"* — the same verb 懷 (*huái*) Ch 70 ends on, so **70, 71 and 56 are one gesture**; and he reads 不知知 with an inserted 言 (*yán* — to say), moving the chapter off self-deception and onto **profession**. 72 is where the two commentators split hardest: 其 (*qí*) has no antecedent, 王弼 makes it the people's dwelling and 河上公 makes it your own heart, and the fork is logged rather than averaged. **Watch for the doubled-character device** — 71's 夫唯病病，是以不病 and 72's 夫唯不厭，是以不厭 both needed one English word carrying two senses (*sick of*, *weary of*). **Ch 73 is next**; note `notes/manuscript.md` already flags a whole line missing from the Siku 王弼 there. Wang Bi's commentary is unproofread in the Siku transcription for 8, 14, 15, 19, 30, 54, 62, 70, 71 and 78, so run `--commentary` before assuming both voices are available. Ch 78 brings 王 (*wáng* — ruler) and 天下王, freshly locked.

2. **Continue the glossary harvest** from `glossary/TRIAGE.md`. Tier 2 is complete except **一** (*yī* — "one"), which is already lowercased in the text and owed only its entry. Tier 3 opens with **名** (*míng* — "name"), which pairs with the 無名/有名 of Ch 1. **New candidate, raised by Ch 70: 希** (*xī* — sparse) — 爻 (crossed threads) over 巾 (cloth), *loosely woven fabric you can see through*. Six occurrences, one sense, three different Englishes in the manuscript already (ch 14 *the inaudible*, ch 23 *speak sparingly*, ch 43 *few ever reach this*). Rarity and inaudibility are the same property; see the thread in `notes/reading.md`.
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
