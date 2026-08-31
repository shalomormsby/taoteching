# CLAUDE.md — operating context for this translation

*Read this first, every session. It is the operating system for everything else. The full reasoning behind every rule here lives in `process/method.md`; this file is the compressed, always-loaded version.*

---

# ⛔ BEFORE YOU WRITE ANYTHING: gloss every Chinese character, every time

**Shalom does not read Chinese.** Never write a Chinese character, word, phrase, line, or chapter title — in conversation, in a document, in a commit message, in a table, anywhere — without an English rendering immediately beside it.

**The format, always:** 為 (*wéi* — "to do / to handle"). Character, pinyin with tone marks, English. Never a bare 為.

**This applies even when:**
- the term was glossed earlier in the same session, or in the same message
- it is a chapter title, a compound, a commentator's name, or a quoted line
- it is "obviously" familiar — 道, 德, 天, 無為 all still get glossed
- you are quoting 王弼 (*Wáng Bì*) or 河上公 (*Héshàng Gōng*); **quoted commentary gets a full English rendering, not a paraphrase**
- you are asking a question and think the answer is obvious

A working approximation is fine and expected; the *deep* meaning is what the glossary entry is for. **Unglossed Chinese makes the work unreadable to the person whose work it is** — it silently converts a question into a thing he cannot answer.

*This is standing rule 0 below. It is repeated here because it is the rule most often broken, and it was broken repeatedly on 2026-08-28 despite being written down.*

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

0. **Shalom does not read Chinese. Gloss every character, every time — see the banner at the top of this file.** Never write a Chinese character, phrase, or line in conversation or in a document without an immediate English rendering beside it — e.g. 為 (*wéi* — "to do / to handle"), not bare 為. This includes chapter titles, compounds, and terms already discussed earlier in the session. A working approximation is fine and expected; the *deep* meaning is what the glossary entry itself is for. Unglossed Chinese makes the work unreadable to the person whose work it is.
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
| 弱 | **yielding** · *weaken* only where it takes an object | "frail", "feeble", "powerless" — and never 柔's *soft* | `glossary/ruo-弱.md` |
| 一 | **the one** (lowercase) · *one thing* at ch 22 only | "the One", "Oneness", "the Absolute" | `glossary/yi-一.md` |
| 全 | **whole** · *stay whole* · *keep whole* (transitive) | "complete", "perfect", "flawless", and every verb of repair | `glossary/quan-全.md` |
| 強 | **strong** · *strengthen* (with an object) · *forcing* (straining a nature) | "mighty", "forceful", "brute strength", "perseverance" — and never 力's *force* | `glossary/qiang-強.md` |
| 仁 | **humaneness** | "benevolence", "charity", "goodwill" | `glossary/ren-仁.md` |
| 慈 / 孝 | **tenderness** / **devotion** | "compassion", "mercy", "maternal love", "filial piety" | `glossary/ci-慈.md` |

*為 is a hand on an elephant — handling, not neutral doing. 無為 is taking your hand off it. "Non-doing" is required by Ch 63's triple parallel (為無為，事無事，味無味), which only survives with a verb that also works as a noun.*

*明 is moonlight through a window, not the sun — reception, not emission. Ch 52 proves it by using 光 (outward light) and 明 in one line: 用其光，復歸其明.* *(swept)*

*萬物: 萬 is a **scorpion** borrowed for its sound — the number is a phonetic accident, not a count — and 物 is a **mottled ox** (kinds, varieties). "Ten thousand" now reads as a ceiling to modern ears; 萬 meant *beyond reckoning*. The creatureliness lives in the **verbs** (生 gives birth · 畜 rears · 衣養 clothes and feeds) — never let those become "generates"/"produces".*

*自然 is 自 (a nose — the thing you point at to mean "me") + 然 (*rán* — **so, thus**): so because of itself. Not "Nature" — that sense is a modern import, and in Ch 25's ladder it puts something above the Tao and inverts the cosmology. 自然 is also the **ground of 無為**: you can take your hand off because things go of themselves. **Revised 2026-08-24 — "the self-so" is retired and now forbidden.** It was a calque, and a *definite noun* where 王弼 (自然者，無稱之言 — "a term that designates nothing") and 河上公 (道性自然，無所法也 — "there is nothing it models itself on") both refuse to name an entity: the same error as "Nature", smaller in degree. **Ch 25 is the deliberate exception** — the one noun slot is answered with a clause: 道法自然 → "the Tao models itself on being what it is." Swept ch 17, 23, 25, 51, 64.*

*敢 is **a hand with a hunting weapon going after a boar** — *Shuowen*: 進取也, "to advance and take." **Appetite, not bravery**, which is why "not daring" inverts the book: Ch 73's 勇於**不敢**則活 (*yǒng yú bù gǎn zé huó* — "courage in not-敢 lives") makes 不敢 *a form of courage*, and "not daring" cannot be brave. Caught by Shalom, 2026-08-19, after the reading had passed three chapters unexamined. Swept ch 30, 64, 67, 69.*

*弱 is **two 弓** (*gōng* — a bow) with 彡 (fine strokes): a bow is useful *because* it bends. Not one classical gloss in this repository reads deficiency — 王弼 on ch 40 says 柔弱同通不可窮極, *"soft and 弱 alike **pass through**; they cannot be exhausted"*; 河上公 on ch 78 answers 弱之勝強 with 水能滅火, *"water can put out fire."* **Ch 78 splits the compound** (弱之勝強，柔之勝剛) and so forces four distinct words: 柔 **soft** · 剛 **hard** · 弱 **yielding** · 強 **strong**. Swept ch 36, 55, 76; **ch 40 needed no change**, which is how the error was caught. Two lines keep *weaken* on grammar — ch 3 弱其志 and ch 36 將欲弱之 take an object, and a stance word cannot.*

*強 completes the four-word table 弱 already forced (柔 **soft** · 剛 **hard** · 弱 **yielding** · 強 **strong**). The graph is a **grain weevil** (說文: 蚚也，从虫弘聲) borrowed for its sound from the Qin onward, displacing 彊 — 弓有力也, **"a bow having force."** So 強 and 弱 are one instrument in two states, and ch 76's 木強則折 ("a tree that is 強 snaps") is a bow drawn past its give. **The book uses 強 for both the disease and the cure and never resolves it** — 王弼 on ch 52: 守強不強，守柔乃強也, *"holding to 強 is not 強; holding to the soft is truly 強."* An English carrying a verdict cannot do both, which is why *forcing* and *true strength* both fail. 河上公 names the whole quartet at ch 42: 去弱為強，去柔為剛 is what the crowd teaches; 去強為弱，去剛為柔 is what Laozi teaches. **力 is `covers:`-ed as *force*** — ch 33 sets 有力 against 強 and our text had the pair inverted. Swept ch 30, 55; ch 15, 33, 42, 52, 55 owed a rewrite.*

*王 reads **ruler**, not *king* — and note the forbidden string is `" king"` with a leading space, so "kingdom" stays legal. See `DISCOVERIES.md` §1, whose central claim this entry corrected.*

**Still open — decide and then lock:**

- *(none currently — 為, 無為, and 明 are settled. Next candidates come from `glossary/TRIAGE.md`.)*
- **正 / 奇** — the *straight / crooked* thread across 57–58 is now **unsettled by ch 78**, which locks 正言 as **words on the mark** on the graph (止 a foot on a target; 征 is the same word). 正 currently carries four Englishes — *uprightness* (57), *the straight* (58), *order* (45), *rights itself* (37) — and ch 78 makes a fifth. Owed: a decision across all five, then `glossary/zheng-正.md`. See `notes/translation.md` · Ch 78 for the argument and for the three rejected candidates.
- **柔 → soft, 剛 → hard** — implied by the 弱 lock's four-word table, applied at ch 76 and now at ch 78, which is the line that forces it (弱之勝強，柔之勝剛). **Ch 52's 守柔曰強 now reads *"To stay with the soft is called strong"*** — revised again 2026-08-28 so that it and ch 55's 心使氣曰強 end on the same word; the two use one frame with opposite verdicts, and 王弼 refuses to resolve it (守強不強，守柔乃強也). 柔 is `covers:`-ed by `glossary/ruo-弱.md`; 剛 is still owed its own mention.

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
8. Note any **retrofit** the decision creates in earlier chapters → `WORKLIST.md`.

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
                      ⚠ generated by import_commentary.py — never hand-edit
sources/shuowen/      說文解字 (Shuōwén Jiězì, c. 100 CE) on all 711 characters — generated
data/                 the character atlas — sqlite, CSVs, explorer.html, graph JSON
                      ⚠ all generated; see data/README.md for the gloss trust tiers
tools/                check_locks.py (the gate) · concordance.py (the evidence)
                      build_db.py → export.py → build_explorer.py / build_graph.py
                      build_index.py (glossary → locks) · fix-linebreaks.py · importers
README.md             the front door — what this is, and how it works
CONTRIBUTING.md       four ways in for outside contributors
AGENTS.md             the same operating context, for non-Claude tools
process/legacy-tao-source-code.md   ⚠ archived, contains SUPERSEDED renderings
DISCOVERIES.md        ★ the findings worth writing about — read when taking stock
WORKLIST.md           ★ the one forward-looking file — what the manuscript still owes
                      (was RETROFIT.md + EDITING-PASS.md, merged 2026-08-28)
PLAN.md               the harness — phases A–F built 2026-08-11; build.py still deferred
ARCHITECTURE.md       ★ how the system fits together — read before changing tooling
                      (authorities · what is generated · the gates · the 12 rules)
```

---

## The harness — two tools, opposite jobs

*Stdlib only, so a fresh clone can run everything with no install step. `PLAN.md`'s no-new-tooling rule was set aside permanently on 2026-08-28 — tooling now needs a reason, like any other work, not a call.*

**Read `ARCHITECTURE.md` before changing any of it.** It maps what holds authority, what is generated, how a decision becomes an enforced rule, and what each gate covers.

```bash
python3 tools/check_locks.py                    # the gate — every rule, whole book
python3 tools/check_locks.py --chapter 61       # while drafting
python3 tools/concordance.py 明                  # every chapter, line, gloss, verse
python3 tools/concordance.py --english "clarity"  # is a rendering backed by its character?
python3 tools/concordance.py --formulas          # segments repeated across chapters
python3 tools/concordance.py --witnesses 25      # where the older manuscripts disagree
python3 tools/concordance.py --commentary 63     # Wang Bi and Heshang Gong on a chapter

python3 tools/build_index.py                     # REQUIRED after any glossary edit
python3 tools/fix-linebreaks.py                  # REQUIRED after editing any verse
python3 tools/build_db.py && python3 tools/export.py    # rebuild the atlas
python3 -m unittest discover -s tools/tests      # the checker's own tests
```

**`check_locks.py` optimizes precision.** It exits non-zero, gates the pre-commit hook and CI, and must never cry wolf — so **no rule fires on English alone.** "virtue" is an error only when 德 is in *that chapter's own* Chinese; otherwise it drops to `info` in a separate false-friends list. That evidence gate is what makes it usable: it took the first run's error list to **9 findings with zero false positives**.

**`concordance.py` optimizes recall.** It judges nothing and never fails. Use it for the evidence a glossary entry or a chapter review needs.

**Run `--english` on every lock you settle.** A lock is a claim in *both* directions — every 強 renders *strong*, **and** every *strong* renders 強 — and the checker can only ever test the first, because its evidence gate keys off the character being present. The second direction caught 固 (*gù* — firm) and 壯 (*zhuàng* — in its prime) both wearing 強's English **inside chapters that contain 強**, where no rule can see them. This is a reader's job and nothing will do it for you. **Do not merge the two** — a tool that gates and searches at once ends up too noisy to gate and too quiet to search.

**When a check is wrong, there are two answers and they are different sizes.** A `lock-ok` comment in the chapter's `## Notes` waives **one finding** and must carry a reason; an unused waiver is itself an error, so the files self-clean. A `shaloms-call` sets aside **a whole rule** — see `process/shaloms-call.md`. Never delete a rule to silence it.

**Check the witnesses before drafting, not after.** `concordance.py --witnesses N` opens with whether **Guodian** (~300 BCE, the oldest witness there is) carries the chapter at all — it carries only 31 of 81, and *not attested* means the chapter rests on the silks and later, which changes how much weight they bear. Then it reports the recorded forks. Ch 21 was drafted over a chronology both Mawangdui silks reverse, and Ch 25 over a king the oldest witnesses do not have — neither was carelessness, nobody had looked. **A blank result means nobody has checked that chapter yet**, not that there are no forks: `sources/variants.yaml` is built by hand. Record new forks there as **facts, never transcriptions** — `sources/PROVENANCE.md` explains why that is a licensing rule and not a preference.

**Do not trust the literal glosses in the source tables.** They speak pre-lock English — "virtue", "the ten thousand things", "mysterious" — which is exactly what this edition rejects. They are a starting point, not a reading, and matching a locked term against its own gloss fails precisely where the locks matter most.

---

## Current state — read before starting

**★ `DISCOVERIES.md` holds the findings that want essays — read it when taking stock of what to write.** Five so far:

| | | |
|---|---|---|
| **§5** | Home was in the word, and we left it out | 歸 (*guī* — to return) |
| **§4** | The throne was installed four times, and one of them was ours | 王 (*wáng* — king) |
| **§3** | The overlay that was never in the Chinese | the missionary lexicon |
| **§2** | The question is not "what is it?" — it is "is it so?" | 自然 (*zìrán* — so of itself) |
| **§1** | No heaven, and no king | 天 (*tiān* — sky) · 王 |

**⚠ §1's central claim was superseded on 2026-08-20 and the file carries a banner saying so — read it before using any of §1.** The *heaven* half stands: 天 is in every witness, "Heaven" is a missionary import, and the distortion is entirely English. The *king* half was backwards. **Every excavated witness at ch 25 reads 王**, Guodian (~300 BCE) included; 人 (*rén* — human) is a transmitted reading from 傅奕 (*Fù Yì*, Tang) and 范應元 (*Fàn Yìngyuán*, Song). We still read 人, now as an editorial call, logged as one. **The lesson worth keeping: a popular "帛書版" (*bó shū bǎn* — "silk-manuscript edition") text online had already been silently emended, and we took it for the silks.** `sources/variants.yaml` is the apparatus; do not trust a manuscript claim that is not in it.

**★ `WORKLIST.md` is the one forward-looking file. Read it before starting work — it holds every open item, prioritized, and the pass order.** What follows here is operating context that does not change week to week; anything that *does* lives there.

- **The first draft is complete — 81 of 81, since 2026-08-26. The editing pass is now the work.**
- **⚠ This is two books, and the seam is around chapter 42.** Chapters **56–81** were drafted *through* the locks, with the checker live and the commentaries in the repo: 77% are clean. Chapters **1–41** were drafted in the Google Doc era and have only ever been *swept* — term-swapped against locks settled afterwards. **Only 7% are clean, and 54% need a chapter-level rewrite.** **Do not assume an early chapter is sound because it carries `status: drafted` and `retrofit: []`** — ch 4 drops a whole line, ch 25 drops 周行 (*zhōu xíng* — "moves in a circle"), ch 28 drops 常 (*cháng* — the ever-present) three times, and every one of them passes every check. A sweep is structurally blind to this: every lock keys off a character to judge the English, so a chapter that simply **does not render** the character passes trivially. Full statement and the chapter-by-chapter status in `WORKLIST.md`.
- **Work in passes, grouped by term, not chapter by chapter.** A decision settled at one chapter propagates to a dozen others; walking 1→81 re-opens the same argument twenty times. Passes 0, A and B are done (text bugs · 強 · 仁/慈/孝) and C is in progress. The order and what each closes is in `WORKLIST.md`.
- **Tooling no longer needs a call.** `PLAN.md`'s no-new-tooling rule was set aside permanently on 2026-08-28 (`process/shaloms-call.md`, `until: standing`). Built since: the corpus database (`build_db.py`, `export.py`), the character atlas in `data/`, and the `unmarked-lemma` rule. **Still unbuilt:** `glossary-self-check` and the **thin-translation** heuristic — the latter is the only proposed rule that would find *absence*, which is the failure mode the early chapters actually have. Both are `WORKLIST` T5. `build.py` stays deferred: the text is still moving.

- **⚠ `status: drafted` has been proved unreliable once. Do not trust it without looking at the page.** On 2026-08-17 Shalom found Ch 65's `## Translation` block was three ellipses and a fragment, carrying `status: drafted` and `retrofit: []`. An audit of all 81 then found **Ch 20** the same way — 10 verse lines against 25 source rows, missing its entire opening movement (絕學無憂 through 荒兮其未央哉). Both had been counted as finished by the 2026-08-10 hand sweep, by `CLAUDE.md`, and by every session since. Both are now genuinely complete. **No checker rule catches this** — every lock keys off the Chinese to judge the English, and a chapter with no English trivially passes all of them. A proposed `incomplete-draft` rule is in `PLAN.md` → *Proposed rules, unbuilt*, still unbuilt; the **thin-translation** heuristic in `WORKLIST` T5-1 measures the same thing as a ratio over the corpus and would catch the thin chapters as well as the empty ones. **It was in the original §2 spec as "status coherence" and never built, inside a section stamped ✅ DONE** — which is how the gap stayed invisible.
- **⚠ `check_locks.py` does not scan `glossary/`.** The locks are enforced against the manuscript but never against the files that *define* them, so a glossary entry can contradict its own lock indefinitely. Found 2026-08-23: one line of `glossary/ziran-自然.md` carried **two** violations — a stale "dare" for 敢 and "the ten-thousand things" for 萬物, the latter forbidden outright. A proposed `glossary-self-check` rule is in `PLAN.md`, unbuilt. Until it exists, **sweep `glossary/` by hand whenever a lock is settled** — the entries are prose and the retrofit policy applies to them too.
- **Two locks have held clean from the beginning:** 德 → *integrity* (zero "virtue" ever appeared) and the sage pronoun rule (zero "he/his/him"). Keep them that way.

### Deferred by Shalom — do not reopen without asking

*These are parked deliberately. Argue them if you have new evidence; do not quietly settle one inside a chapter review.*

1. **民 / 人 — one decision, whole book (2026-08-25).** 民 (*mín* — the governed, an eye pierced by a blade) reads *"the people"* in all 32 of its lines; 人 (*rén* — a person) drifts, and **ch 57 renders it both ways two lines apart**. A rule settled at one chapter propagates to twelve others and to the cross-chapter rhymes in `notes/reading.md`. Ch 74 reads *"the people"* as a **hold, not a precedent**. `WORKLIST` T4-1 — which also notes that 身 (*shēn* — body) is the same shape of problem and may want deciding with it.
2. **正 / 奇** — five Englishes across ch 37, 45, 57, 58, 78. `WORKLIST` T4-2.
3. **Em-dashes in the verse** — 17 lines. Some are good (ch 44's *"Reputation or your self — which is dearer?"*), some strand subjects. Removing them means restructuring real lines, so it is a conversation, not a sweep. `WORKLIST` T4-3.

**Everything else that is owed — 48 open items, tiered and with a pass order — is in `WORKLIST.md`.** Do not maintain a second list here.

*One setup step, if the skills are not linked:*
`ln -s "$(pwd)/process/skills/glossary-entry" ~/.claude/skills/glossary-entry`

### How Shalom works

He decides; the AI argues. Bring him a **clear recommendation with the evidence and the cost**, not a menu — then do what he says. He will push back hard and specifically when something is off, and that pushback is usually right: he caught the 樸 "block" error, the missing 心 subject, the "wise core" abstraction, the process noise in the glossary entries, and — 2026-08-28 — that *"go unseen"* was handing a grasping figure the book's own compliment. Treat a challenge as a finding, not a complaint. He does not read Chinese, so **gloss every character, every time**.

- **★ One question at a time.** Do not stack four decisions into one message. Bring the deepest one, with a recommendation; take his answer; then bring the next. *(Said plainly on 2026-08-28: "You're asking too many questions at once.")*
- **A commentator's gloss is not the text, and he will catch it.** 王弼 explaining 贅 (*zhuì* — superfluous) as 肬贅 (*yóu zhuì* — a wart) does not make *wart* a candidate rendering. Offer what the line says; keep the commentary as evidence for it.
- **Order of work:** the first draft is done, so the passes in `WORKLIST.md` are the order. **Work by term, not chapter by chapter** — one decision touches a dozen chapters, and walking 1→81 re-opens the same argument twenty times.
- **Retrofit policy — fix on discovery, not in a deferred batch.** When a lock is settled, sweep the affected chapters *immediately*. Mechanical term-swaps: just apply them. Lines needing a rewrite: propose to Shalom first, then apply. *(This reverses the original plan, which batched retrofits to the editing pass — that made sense only while `chapters/` were regenerated from the Google Doc and hand-edits would be clobbered. The Doc is retired; the constraint is gone.)*
- **Always verify a flagged line against the Chinese in its own chapter before changing it.** Roughly a third of the first automated sweep's flags were false positives — 常 (*cháng*, constant) vs 長 (*cháng*, long), "the one" the pronoun vs 一, "Block the openings" (塞) vs "uncarved block" (樸). See `PLAN.md` → *What the 2026-08-10 sweep taught the checker*.

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
