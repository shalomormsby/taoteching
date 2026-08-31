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

## The locks — how they behave

**The locks themselves live in [`glossary/INDEX.md`](glossary/INDEX.md)** — every term, its rendering, what is forbidden, how much of the book it touches, and whether it is locked or still a recommendation. **It is generated from the entries' own frontmatter, so it is never stale. Read it; do not keep a second copy anywhere.**

*A table used to sit here and was maintained by hand. It went stale twice in one week — 仁 and 慈 were locked and never reached it — while the generated index had them right the whole time. `check_locks.py` enforces the locks from `terms.yaml` regardless, so the copy was a reminder of a rule a tool already keeps.*

What does not fit in a generated table, and does not go stale:

- **A lock is on register, not on one English word.** Several terms carry licensed flexions — 事 (*shì* — affairs / to attend to), 弱 (*ruò* — yielding / *weaken*), 強 (*qiáng* — strong / *strengthen* / *forcing*). The entry states which, and why.
- **Grammar overrides a lock.** 弱其志 (*ruò qí zhì* — "weaken their ambition") takes an object, and a stance word cannot. The split is marked in the Chinese, so it can be checked rather than argued.
- **Some characters carry both valences, and the English must not resolve them.** 強 is the disease at ch 76 and the cure at ch 52 — 王弼: 守強不強，守柔乃強也, *"holding to 強 is not 強; holding to the soft is truly 強."* 執 (*zhí* — to grasp) is the wrong kind of taking-hold at ch 29 and an instruction at ch 14. An English carrying a verdict cannot do both jobs.
- **A `forbidden:` entry cannot express *right for that character, wrong for this one, same chapter*.** So *integrity* cannot be forbidden for 信 (*xìn* — trust): chapters 21, 23, 38 and 49 hold both 信 and 德. Those distinctions live in the entry's prose and in the reader.
- **A lock is a claim in both directions.** The checker can only test one — see the harness section on `--english`.

**Open questions, and terms still owed an entry, are in `WORKLIST.md`.** Do not list them here.

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

Three commentaries are vendored — 王弼 (*Wáng Bì*, d. 249 CE), 河上公 (*Héshàng Gōng*, Han) and 韓非 (*Hán Fēi*, d. 233 BCE, the oldest there is). **Which of them covers a given chapter is a question for the tool, not for a table:** `--commentary N` prints what exists and says *not vendored* for what does not. Coverage and per-file provenance live in `sources/PROVENANCE.md`.

**Run them before drafting a chapter and before changing a settled line.** Three of this session's findings came from exactly that and could not have come from anywhere else: Wang Bi's gloss 此上之所云也 settled the referent of 此 in Ch 21; the Siku compilers' note 〔案狀各本俱作然〕 reopened a decision made an hour earlier; Han Feizi's 大必起於小 supplied a reading of Ch 63's hardest line.

**Quote, gloss, and cite them — never copy their English.** There is no English in these files; they are the Chinese. The pre-1931 rule in standing rule 3 governs *translations*, and none are in this repository.

**When they disagree, that is the finding.** Convergence is strong evidence; divergence gets logged in `notes/manuscript.md` and, if it is a textual fork, in `sources/variants.yaml`. Do not average them into a consensus.

**Adding to `sources/` has rules.** Read `sources/PROVENANCE.md` first. The short version: public domain by age, a *nameable* edition, provenance in the frontmatter, and **never a transcription of the Mawangdui or Guodian manuscripts** — reconstructing damaged graphs is living scholarship, so record the *fact* of the variant instead.

---

## Per-chapter workflow

**Encoded as a skill: `process/skills/chapter-review`. Invoke it — do not work from memory, and do not keep a second copy of its steps here.** It carries the sequence, the watchlist pass, the typography rules, and the logging.

**Tie-breaking order:** characters and radicals → oldest witnesses → classical commentaries → internal consistency and the locks → this edition's ethos → Shalom's poetic intuition, exercised *after* the deepest reading is on the table.

**Adding or revising a glossary entry has its own skill:** `process/skills/glossary-entry`.

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

- **★ Intuition is last as an *arbiter* and often first as a *detector*.** When Shalom says a word feels off, that is **a research assignment, not a preference to accommodate.** Do not offer a synonym that feels better — go find what the discomfort is detecting. Ch 25's *king* was caught exactly this way, and the oldest witnesses proved him right (`DISCOVERIES.md` §1).
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
