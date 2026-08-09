# CLAUDE.md — operating context for this translation

*Read this first, every session. It is the operating system for everything else. The full reasoning behind every rule here lives in `process/method.md`; this file is the compressed, always-loaded version.*

---

## What this is

A from-the-source English translation of the Tao Te Ching by **Shalom Ormsby**, built chapter by chapter from the original Chinese, decades of study and meditation, and AI collaboration — **never** from other people's translations.

Two intentions, both sacred:

1. A **high-fidelity English Tao Te Ching in the public domain** — a gift to humanity. **This repository is entirely CC0, with no exceptions.** Everything here — translation, glossary, notes, method — is given away.
2. A **companion volume** of scholarship and reflection, so the work can sustain its maker and his family. It lives in a **separate private repo (`../taocompanion`)** and is a *rewrite for readers*, drawing on this material without duplicating it. Nothing is withheld from this repo to make room for it.

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

1. **Never refer to the Sage as "he."** Use singular *they/their*, or recast. This is an impermissible gender bias. Applies to all archetypal figures.
2. **Universality over the incidental male-default.** The text exalts the feminine as principle yet assumes the male as cultural default. Where they collide: **render toward the universal, note the seam.** Never erase the male-centrism silently.
3. **Consult sources for *meaning*, never for *phrasing*.** Pre-1931 public domain only. Waley (1934) and later are off-limits.
4. **Honesty over false closure.** Where the text is genuinely double, say so and leave the tension open.
5. **Every decision gets logged** in one of the three notes layers. See below.

---

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
| 萬物 | **the ten-thousand things** | "all things", "the myriad things" | — |
| 知足 | **knowing you have enough** · noun: **contentment** | "sufficiency", "fulfilled" | `glossary/zhizu-知足.md` |
| 守 / 抱 | **hold fast to** / **embrace** | (do not swap) | — |
| 聖人 | **the Sage** — always *they/their* | "Holy Man", "saint", "the Master" | — |
| 我 / 吾 | the self **seen** / the self **seeing** | (both "I"; note the pairing) | `glossary/wo-wu-我吾.md` |
| 自然 | **self-so / of-itself-so** | capital-N "Nature" | — |

**Still open — decide and then lock:**

- **無為** — "non-action" leading; lock where the paradox lives.
- **明** — "clear-seeing" vs "illumination". Ch 16 and Ch 55 currently disagree. **Pick one; 知常曰明 is a repeated formula.**
- **正 / 奇** — threaded as **straight / crooked** across 57–58. Confirm.

---

## The overlay watchlist

Full audit: `process/overlay-audit.md`. The English Tao Te Ching was largely built by missionaries (Legge = London Missionary Society); in the Chinese Union Bible, **John 1:1 reads 太初有道** — 道 for *Logos*, 神 for *God*. The standard renderings are theology sedimented into words.

Flag on sight: **聖** ("holy" — it means *acute hearing*) · **神** ("God" — it means *numinous potency*) · **鬼** ("demons" — it means *ghosts/the dead*) · **罪** ("sin" — it means *crime*) · **義** ("righteousness" — it means *duty*) · **仁** ("benevolence/charity" — *humaneness*) · **精/魄** ("soul" — *vital essence* / the *corporeal* soul) · **一** ("the One" — Neoplatonism) · **福** ("blessing" — *good fortune*) · **善** ("good" — often *skilled*) · **道法自然** (never "the Tao follows Nature" — that inverts the chapter).

Also watch **register**, not just vocabulary: KJV cadence, devotional capitalization, abstraction drift. And our own besetting temptation — the **mechanistic** ("operating system", "source code", "generate").

**Two tests:** *The hymn test* — would this line sit in a sermon? Then check the character. *The pointing test* — could Laozi have pointed at it?

---

## Per-chapter workflow

1. Read the Chinese cold. Decompose contested characters to radicals.
2. Check the witnesses (Wang Bi base; Mawangdui, Guodian, Fu Yi, Beida) for meaning-bearing forks.
3. Check the classical commentaries (Wang Bi, Heshang Gong, Han Feizi).
4. Check the locks table above and the overlay watchlist.
5. **Take a stand** — lead with the deepest claim, then the smaller precisions.
6. Offer clay: a full rendering Shalom can accept, reject, or reshape.
7. **Log** what was decided (below). Add a glossary entry for any term that earned one.
8. Note any **retrofit** the decision creates in earlier chapters → `RETROFIT.md`.

**Tie-breaking order:** characters/radicals → oldest witnesses → classical commentaries → internal consistency and locks → this edition's ethos → Shalom's poetic intuition (final arbiter, exercised *after* the deepest reading is on the table).

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
process/overlay-audit.md
process/legacy-tao-source-code.md   ⚠ archived, contains SUPERSEDED renderings
RETROFIT.md           the debt list
PLAN.md               the harness to build at Ch 81
```

---

## Current state — read before starting

- **Chapters 1–60 and 65:** drafted. The earlier ones are **pre-lock** — they predate several glossary decisions and carry known overlay language ("the cosmos", "mystery", "all things", "eternal"). See `RETROFIT.md` for the scanned, evidence-based list.
- **Chapters 61–64 and 66–81:** still to draft. **This is the active frontier.**
- **Two locks are holding clean across the whole draft:** 德 → *integrity* (zero "virtue") and the Sage pronoun rule (zero "he/his/him"). Keep them that way.
- **Order of work:** finish the first draft to 81, *then* the harness (`PLAN.md`), *then* the retrofit sweep. **Do not stop drafting to build tooling.**

## Source of truth

`source/Tao-Te-Ching-shalom-translation-2026-08-09.md` is Shalom's working manuscript, exported from Google Docs. `chapters/*.md` are **generated from it**. When he supplies a newer export, regenerate the chapter files rather than hand-editing both — otherwise they drift.

**After every regeneration, run `python3 tools/fix-linebreaks.py`.** The translation is verse: every line break is deliberate, and Markdown renders a single newline as a space, collapsing each stanza into a running paragraph. The break must be a CommonMark hard break — **two trailing spaces** — which the manuscript already carries and generation has dropped before. `--check` fails loudly instead of rewriting. Never trim trailing whitespace from `.md` here; `.editorconfig` and `.vscode/settings.json` guard against it.
