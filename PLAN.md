# PLAN — the harness, to build at Chapter 81

*Deliberately deferred. The tooling below earns its keep during the **editing pass**, because the editing pass is the retrofit pass. Building it earlier means building checks before the corpus exists to check.*

**The one rule this plan exists to protect: do not stop drafting to build tooling.** Finish the first draft to 81 first.

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

## 2. `tools/check_locks.py` — principles become tests

The highest-value tool by a wide margin. Reads `terms.yaml`, scans the `## Translation` block of every chapter file, reports violations.

Checks:

- **Forbidden renderings** — "virtue", "heaven", "eternal", "cosmos", "mystery", "sin", "righteousness", "the myriad things", "Holy Man".
- **The Sage pronoun rule** — any `he/his/him` within a sentence of "Sage" or "Master". Zero tolerance; this is a standing rule.
- **Repeated-formula consistency** — lines identical in Chinese across chapters (知常曰明 in 16/55; 生而不有 in 10/51; 不道早已 in 30/55; 玄德 refrains) must be identical in English. Detect by matching source rows, then diff the corresponding English.
- **Devotional capitalization** — flag capitalized Way, Virtue, Heaven, Nature, Being, One outside sentence start.
- **Status coherence** — `status: drafted` with an empty translation block, or a chapter whose `terms:` frontmatter omits a term present in its source rows.

Output: grouped by chapter, with the rule cited and the glossary entry linked. Exit non-zero on violations so it can run in CI.

## 3. `tools/concordance.py` — term in, evidence out

Replaces the ad-hoc `bash`/`docx` greps used throughout drafting. Given a character or phrase:

- every chapter containing it, with the full Chinese line
- the current English for that line
- whether renderings are consistent, and where they diverge

This is how you catch drift across 81 chapters, and how future glossary entries get their evidence base. (The 天地 entry was built exactly this way — the finding that 陰 appears *once* in the whole book, and 天地 in exactly seven chapters, came from this kind of sweep.)

Add `--pairs` to compare two terms across chapters (the 我/吾, 玄/妙, 正/奇 work).

## 4. `tools/build.py` — one command to the book

Assembles `chapters/*.md` into deliverables, ending the Google Drive round-trip:

- **Reading edition** (.docx / .pdf / .epub) — verse only, clean typography, the public-domain gift.
- **Scholar's edition** — verse plus source table, pinyin, literal gloss, and the notes for that chapter.
- **Companion draft** — glossary entries, threaded reading notes, the method and audit, in reading order.

Three editions, one source of truth. Use `pandoc` where possible; `python-docx` for fine control (the existing v2 table styling is a known-good starting point).

## 5. A chapter-review skill

The per-chapter workflow (`CLAUDE.md` → *Per-chapter workflow*) is stable enough to encode as a reusable skill: read the Chinese cold → decompose contested characters → check witnesses and commentaries → check locks and the overlay watchlist → **take a stand** → offer clay → log the notes → record retrofit.

Encoding it makes the method **portable and repeatable** — identical whether Claude or Fable is driving — and means the process guide gets *executed*, not merely hoped over. This is also how the method transfers to Fable for the final refinement pass without depending on someone remembering to read `process/method.md`.

## 6. CI (optional, cheap)

A GitHub Action running `check_locks.py` on push. Turns the standing principles into a gate: a chapter cannot regress to "virtue" without the build going red.

---

## Suggested order at Ch 81

1. **Import** the Google Docs drafts for 39–60 (`RETROFIT.md` → *Import debt*). Nothing else is trustworthy until the repo holds the whole book.
2. Build `terms.yaml` — mostly transcription from existing decisions.
3. Build `check_locks.py`; run it; **expect a large, useful failure list.** That list *is* the retrofit plan, mechanically derived.
4. Resolve the open locks — 明, 無為 — before sweeping, so the sweep only happens once.
5. Run the retrofit sweep chapter by chapter, re-running the checker.
6. Build `concordance.py` as needed during the sweep; it will pay for itself in the first hour.
7. `build.py` last, when the text has stopped moving.

---

## Deliberately not building

- **A translation memory / alignment database.** The glossary already does this, in prose, better.
- **Automated quality scoring.** The whole method rests on human judgment sharpened by argument; a metric would be a false authority.
- **Anything that suggests renderings.** The AI's role is to argue for the deepest reading, not to autocomplete the verse. The verse stays Shalom's own.
