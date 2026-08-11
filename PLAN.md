# PLAN — the harness

**Status: built 2026-08-11**, except `build.py`, which stays deferred. See `process/shaloms-call.md` → *no-new-tooling* for the call that authorized it, and the reasoning.

*The original plan deferred all of this to Chapter 81, on the grounds that "building it earlier means building checks before the corpus exists to check." That was sound, and it expired: 62 of 81 chapters existed and were swept, so the remaining 19 could be drafted **into** a checked corpus rather than swept afterward. The proof the deferral had outlived its logic was Ch 53, which rendered 大道 (dà dào — "the great Tao") as "the great Way" one line below rendering it correctly, in a chapter carrying `retrofit: []` inside the range the hand sweep had certified clean.*

**The rule this plan originally protected — do not stop drafting to build tooling — resumes when phases A–F are done.** `build.py` remains deferred on its own merits: the text moves in 19 more chapters, and every edition built now would be built twice.

---

## Why this ordering

The failures this harness prevents are already documented and real: 德 slipping back to "virtue" in a Ch 59 draft; 常 vanishing four times in Ch 1; 萬物 becoming "all things"; 明 rendered two ways across a repeated formula; the Sage once called "he." Every one is a **memory** failure, not a filing failure.

`CLAUDE.md` addresses that class of error *now*, by loading the rules into every session. The harness addresses what `CLAUDE.md` cannot: **mechanical verification across 81 chapters at once.** That is an editing-pass activity.

---

## 1. ~~`glossary/terms.yaml` — the locks as data~~ ✅ **DONE (2026-08-10)**

*Built early, deliberately: adding frontmatter to 17 entries was cheap, and retrofitting it to 40 later would not have been. `tools/build_index.py` generates both `terms.yaml` and `INDEX.md` from each entry's frontmatter, recomputing chapter lists from `source/chinese.md` so they cannot drift. `check_locks.py` should read `terms.yaml` rather than a hand-kept list.*

<details><summary>Original spec</summary>

The glossary entries are essays; they carry the reasoning and must stay prose. This file is their machine-readable shadow.

```yaml
- term: 德
  pinyin: dé
  render: integrity
  forbidden: [virtue, Virtue, moral excellence]
  status: locked
  entry: glossary/de-德.md
  chapters: [10, 21, 23, 38, 41, 49, 51, 54, 55, 59, 60, 63, 65, 68, 79]

- term: 明
  pinyin: míng
  render: null              # UNDECIDED — see RETROFIT.md
  candidates: [clear-seeing, illumination]
  status: open
  chapters: [10, 16, 22, 24, 27, 33, 36, 41, 52, 55, 65]
```

Fields: `term · pinyin · render · forbidden · status (locked|open|watchlist) · entry · chapters · notes`.

**Seed it from:** the locks table in `CLAUDE.md`, the watchlist in `process/overlay-audit.md`, and `RETROFIT.md`.

</details>

## 2. `tools/check_locks.py` — principles become tests ✅ **DONE (2026-08-11)**

*Nine rules, 39 tests, 0.16s on the whole book. The design decision that made it usable is the **evidence gate**: no rule fires on English alone, because every chapter file carries its own Chinese. First run found 9 errors with zero false positives — see `RETROFIT.md` → Open. Two rules were not in this spec and earned their place: `mechanistic-register` (which found "source code" live in ch 21) and `stale-shaloms-call`.*

<details><summary>Original spec, and what changed</summary>

The highest-value tool by a wide margin. Reads `terms.yaml`, scans the `## Translation` block of every chapter file, reports violations.

Checks:

- **Forbidden renderings** — "virtue", "heaven", "eternal", "cosmos", "mystery", "sin", "righteousness", "the myriad things", "Holy Man".
- **The Sage pronoun rule** — any `he/his/him` within a sentence of "Sage" or "Master". Zero tolerance; this is a standing rule.
- **Repeated-formula consistency** — lines identical in Chinese across chapters (知常曰明 in 16/55; 生而不有 in 10/51; 不道早已 in 30/55; 玄德 refrains) must be identical in English. Detect by matching source rows, then diff the corresponding English.
- **Devotional capitalization** — flag capitalized Way, Virtue, Heaven, Nature, Being, One outside sentence start.
- **Status coherence** — `status: drafted` with an empty translation block, or a chapter whose `terms:` frontmatter omits a term present in its source rows.

Output: grouped by chapter, with the rule cited and the glossary entry linked. Exit non-zero on violations so it can run in CI.

**What changed in the building:**

- **Repeated-formula consistency is a `warn`, not an `error`, and does not attempt alignment.** The spec assumed you could "detect by matching source rows, then diff the corresponding English." You cannot: verse lines align to source rows in only 27 of 62 drafted chapters, and the literal glosses speak pre-lock English (玄德 is glossed "dark/mysterious virtue/power" where the verse correctly reads "profound integrity"), so gloss-matching fails exactly where the locks matter. Three attempts at inference all failed. The rule now asks an alignment-free question — two chapters sharing a verbatim Chinese segment should have *some* pair of similar lines — which took it from 21 warnings to 11, most of them real, and caught ch 23's 信不足焉.
- **Formulas are indexed as comma-segments, not n-grams.** Sub-segment n-grams produce fragments no translator rendered as a unit (難得之貨 inside 不貴難得之貨), each a warning about nothing.
- **Case policy is derived, not configured.** A forbidden string written with a capital means the capital is the violation. This needed no frontmatter changes and cleared six false positives on "Being".
- **`--staged` mode, error-only, skipping `status: untranslated`** — so a half-drafted chapter never argues with the hook.

</details>

## 3. `tools/concordance.py` — term in, evidence out ✅ **DONE (2026-08-11)**

*The highest-value mode turned out to be the one this spec did not have: `--english`, the reverse direction. A lock is a two-way claim — every 明 renders as clear-seeing **and** every clear-seeing renders 明 — and only that direction catches a rendering applied where its character is absent.*

<details><summary>Original spec</summary>

Replaces the ad-hoc `bash`/`docx` greps used throughout drafting. Given a character or phrase:

- every chapter containing it, with the full Chinese line
- the current English for that line
- whether renderings are consistent, and where they diverge

This is how you catch drift across 81 chapters, and how future glossary entries get their evidence base. (The 天地 entry was built exactly this way — the finding that 陰 appears *once* in the whole book, and 天地 in exactly seven chapters, came from this kind of sweep.)

Add `--pairs` to compare two terms across chapters (the 我/吾, 玄/妙, 正/奇 work).

</details>

## 4. `tools/build.py` — one command to the book ⏸ **still deferred**

*The one item where the original ordering holds. The text moves in 19 more chapters; every edition built now is built twice. Build it when the text stops moving.*

Assembles `chapters/*.md` into deliverables, ending the Google Drive round-trip:

- **Reading edition** (.docx / .pdf / .epub) — verse only, clean typography, the public-domain gift.
- **Study edition** — verse plus source table, pinyin, literal gloss, and the notes for that chapter. *(Named for what it is for, not who it is for: "Scholar's edition" quietly tells an ordinary reader the book is not theirs.)*
- **Companion draft** — glossary entries, threaded reading notes, the method and audit, in reading order.

Three editions, one source of truth. Use `pandoc` where possible; `python-docx` for fine control (the existing v2 table styling is a known-good starting point).

## 5. A chapter-review skill ✅ **DONE (2026-08-11)**

*`process/skills/chapter-review/`. The `glossary-entry` skill was updated in the same pass to use `concordance.py` instead of its inline heredoc.*

The per-chapter workflow (`CLAUDE.md` → *Per-chapter workflow*) is stable enough to encode as a reusable skill: read the Chinese cold → decompose contested characters → check witnesses and commentaries → check locks and the overlay watchlist → **take a stand** → offer clay → log the notes → record retrofit.

Encoding it makes the method **portable and repeatable** — identical whether Claude or Fable is driving — and means the process guide gets *executed*, not merely hoped over. This is also how the method transfers to Fable for the final refinement pass without depending on someone remembering to read `process/method.md`.

## 6. CI ✅ **DONE (2026-08-11)**

`.github/workflows/checks.yml` runs the tests, `check_locks.py`, `fix-linebreaks.py --check`, and a `git diff --exit-code glossary/` proving the generated files are current. `.githooks/pre-commit` gates locally on staged chapters at error severity only — install with `git config core.hooksPath .githooks`.

## 7. `shaloms-call` — the override of record ✅ **DONE (2026-08-11)**

Not in the original plan, and the reason this one could be written at all. `process/shaloms-call.md` records a rule Shalom has set aside, with scope, expiry, and reason. Suspensions are never silent (the checker prints a footer naming them) and an expired call is an error, so each is renewed or retired deliberately. Without it, an override lived only as a sentence in one conversation — invisible in the repo, and leaving the AI to re-argue a settled decision next session.

## 8. `sources/` — the witnesses and commentaries, in the repo 📋 **SPEC'D, not built**

*Proposed 2026-08-11, after Ch 21 required fetching Wang Bi, Heshang Gong, and both Mawangdui silks from the open web to answer one question about one line. **Needs its own `shaloms-call`** — the existing suspension of the no-new-tooling rule covers phases A–F only, and this is new scope.*

### Why

The research process currently depends on a search engine every time a line is contested. Three problems with that, in order of severity:

1. **Search summarizes, and a summary can be wrong.** On Ch 21 the first search correctly reported the 自古及今 / 自今及古 fork — but the three *other* forks in the same two lines (順/閱, 父/甫, 然/狀) only appeared after fetching the actual silk text. A paraphrase of a variant is not evidence of a variant.
2. **It is not reproducible.** No reader can audit the claim "both Mawangdui silks read 自今及古" against anything in this repo. For a CC0 edition whose whole argument is *we show our work*, that is a real gap.
3. **It does not scale to the operation we actually need.** What Ch 21 required — align the witnesses for a line, spot the meaning-bearing forks — is mechanical, and should be one command for any of the 81 chapters, run *before* drafting rather than after.

### What it buys

- `concordance.py --witnesses 21` — the forks for a chapter, aligned, before a word is drafted.
- A new `check_locks.py` rule: **a meaning-bearing variant present in the apparatus but absent from `notes/manuscript.md`** — a fork translated over without a logged decision. This would have caught Ch 21's reversed chronology before the chapter was drafted.
- **It audits backwards.** Sixty-two chapters were drafted with no variant apparatus. This finds the other places a Wang Bi reading quietly decided a line.

### The licensing analysis — read this before copying anything

**The trap:** the obvious sources are not CC0-compatible.

| Source | License | Compatible with CC0? |
|---|---|---|
| **ctext.org** structured data | CC BY-**NC**-SA 3.0 | **No** — ShareAlike cannot be relicensed CC0, and **NonCommercial poisons the companion volume** |
| **zh.wikisource.org** | CC BY-SA 4.0 | **No** — ShareAlike |
| Pre-1929 printed editions | US public domain by date | **Yes** |

**The NonCommercial clause is the sharper problem than the CC0 one.** `../taocompanion` exists so this work can sustain a family. An NC-licensed dependency anywhere in a commercial book's derivation chain is exactly the wrong shape — worse than the CC0 issue, because CC0 is a gift Shalom controls and the companion is income he needs.

**The legal reality is probably fine, and that is not good enough.** Copyright covers original expression; 道可道非常道 is 4th-century BCE and free, and a faithful transcription of a public-domain text attracts no new copyright in the US (*Feist v. Rural Telephone*, 1991, rejecting "sweat of the brow"; *Bridgeman v. Corel*, 1999, for faithful reproductions). What a site **can** own is the compilation, the metadata, and the **added punctuation** — and `notes/translation.md` already establishes that all punctuation in the Chinese is a later editor's addition, not the source's.

But a repository whose first line is *"entirely CC0, with no exceptions"* must not rest its cleanliness on a doctrinal argument about originality. It must be **obviously** clean to a reader who does not want to litigate *Feist*.

### What may and may not be vendored

| Material | Call | Why |
|---|---|---|
| Wang Bi commentary (c. 249 CE) | **vendor** | pre-1929 printings exist in quantity |
| Heshang Gong commentary (Han) | **vendor** | same |
| Han Feizi 解老 / 喻老 (3rd c. BCE) | **vendor** | same |
| Laozi base text | **vendor, re-provenanced** | ancient; re-derive from a named pre-1929 edition, not from ctext |
| **Mawangdui** (excavated 1973) | **do not vendor** | every transcription is modern, and reconstructing the damaged characters is genuine editorial work |
| **Guodian** (excavated 1993) | **do not vendor** | same |
| Modern critical apparatus, annotations, translations | **do not vendor** | in copyright |

**For the excavated witnesses, record the facts rather than the text.** "Mawangdui A and B read 自今及古 where Wang Bi reads 自古及今" is a *fact about a text*, and facts are not copyrightable. This is already what `notes/manuscript.md` does in prose; the change is to make it machine-readable and cite the scholarship instead of reproducing it. Arguably better research practice than copying a transcription, not merely safer.

### Shape

```
sources/
  PROVENANCE.md         per-file: work, author, date, edition, where obtained,
                        rights reasoning, and what in it is editorial
  wangbi/               commentary, by chapter
  heshanggong/          commentary, by chapter
  hanfeizi/             解老 / 喻老
  variants.yaml         the apparatus: chapter · line · witness · reading · our call
                        (facts only — no reconstructed transcriptions)
```

Every vendored file carries frontmatter naming the **specific printed edition** it was transcribed from. A file whose edition cannot be verified does not go in.

### Immediate, separable action ✅ **DONE (2026-08-11)**

**Re-provenance `source/chinese.md`.** Done. The header now rests the CC0 dedication on **the age of the text and nothing else**, cites *Feist* (1991) and *Bridgeman* (1999) for why a faithful transcription of a public-domain work creates no new copyright, and names four **independent pre-1929 printings** where the recension can be verified: the Ming *Zhengtong Daozang* (1445), the *Siku Quanshu* (1782), the Zhejiang *Ershi'er zi* (1875), and the Commercial Press *Sibu congkan* (first series from 1919).

It also states plainly that **the punctuation is editorial and forms no part of the source** — the one element of a modern edition that could carry a thin claim, and the one this project already treats as its own on the record (`notes/translation.md`, *Standing principle · Lineation and punctuation*). ctext keeps a courtesy credit as a transcription check, with its licence named, and nothing depends on it. `process/method.md` §3 and `AGENTS.md` updated to match.

---

## What is left

1. **Resolve the 8 open findings** in `RETROFIT.md` → *Open*. Each needs a rewrite, so each is Shalom's call. The build stays red until they are resolved or waived — which is the ratchet working, not a problem to route around.
2. ~~**Re-provenance `source/chinese.md`** off ctext~~ ✅ **done 2026-08-11** (§8).
3. **Build `sources/`** (§8) — its own PR, its own `shaloms-call`. Licensing verification is the slow part, not the code.
4. **Draft chapters 61–64 and 66–81** with the hook live, through the `chapter-review` skill. This is the active frontier and the reason the harness was built now rather than at 81.
5. **`build.py`**, when the text has stopped moving.

*Steps 1–2 of the original ordering are already done: the Google Docs import is complete and the Doc retired; `terms.yaml` was built 2026-08-10. The open locks 明 and 無為 were settled before this build, so the sweep happened once, as intended.*

---

## What the building taught

Kept here because the next tool in this repo should start from it.

- **The evidence gate is the whole design.** A checker that fires on English alone is a grep with opinions, and at ~33% noise it gets switched off inside a week. This one never fires without the character to prove it, which is possible only because every chapter file carries its own Chinese. It is the difference between 20 flags and 9 findings.
- **Two tools, opposite contracts.** Precision for the gate, recall for the report. Merging them yields something too noisy to gate and too quiet to search.
- **Do not infer what the data cannot support.** Three attempts to align verse lines to source rows all failed, for three independent reasons. The rule that works asks a question needing no alignment at all. When inference keeps failing, change the question rather than tuning the guess.
- **The literal glosses are pre-lock English.** They say "virtue", "ten thousand", "mysterious". Any tool that matches the manuscript against them will fail hardest on exactly the terms the locks exist to protect.
- **Encode invariants, never taste.** Every rule cites a written decision. A rule with no citation is a tool author's opinion wearing a build's authority — which is the "automated quality scoring" refused below.
- **Suppression has to exist, and has to cost something.** Unsuppressable rules get disabled wholesale; free suppression rots. Hence `lock-ok` with a required reason and an unused-waiver error, and `shaloms-call` with a required `until:` and a stale-call error.

---

## Deliberately not building

- **A translation memory / alignment database.** The glossary already does this, in prose, better.
- **Automated quality scoring.** The whole method rests on human judgment sharpened by argument; a metric would be a false authority.
- **Anything that suggests renderings.** The AI's role is to argue for the deepest reading, not to autocomplete the verse. The verse stays Shalom's own.
