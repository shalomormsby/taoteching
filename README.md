# 道德經 · Tao Te Ching

**A new English translation from the classical Chinese, by Shalom Ormsby.**

**Everything here is public domain (CC0). It is a gift — take it, use it, build on it. No permission needed, no attribution required.**

---

## What this is

A from-the-source translation of the Tao Te Ching, built chapter by chapter from the original Chinese, decades of study and meditation, and AI collaboration — **never from other people's translations.** No copyrighted version was consulted at any stage. Where older public-domain translations were read at all, it was to understand the *range of meanings* a line has carried, never to borrow words.

The work rests on three commitments:

- **Fidelity and poetry, together.** The literal meaning is honored; the English is living verse, not a gloss.
- **The feminine at the center.** The Mother (母), the dark female (玄牝), the valley (谷), the yielding (柔) — Laozi's generative imagery kept warm and bodily, never abstracted into a sexless "Source."
- **The naturalistic razor.** The overlays come off — theistic ("Heaven"), moralistic ("virtue"), and mechanistic alike — and the text's own images are restored: water, root, valley, uncarved wood, the newborn, the Mother.

Every consequential decision is documented. Nothing is asserted without evidence, and genuine ambiguities are left open rather than resolved by fiat.

## Read it

Start at [`chapters/001.md`](chapters/001.md). Each chapter carries the English verse, the Chinese with pinyin and a literal gloss, and any notes particular to it.

## Repository map

| Path | Contents |
|---|---|
| `chapters/001–081.md` | One file per chapter — translation, source text, notes |
| `source/chinese.md` | The base Chinese text (Wang Bi received recension) |
| [`glossary/INDEX.md`](glossary/INDEX.md) | **Start here for terms** — every locked rendering, generated from the entries |
| `glossary/` | Radical-level entries on the key terms — the heart of the work |
| `notes/manuscript.md` | Textual forks between the ancient witnesses, and which reading we follow |
| `notes/translation.md` | Our own rendering decisions, and the standing principles |
| `notes/reading.md` | Interpretive notes for readers; cross-cutting threads |
| `process/method.md` | The full working method |
| `process/overlay-audit.md` | Reading Laozi without the missionary lens |
| `process/skills/` | The method made executable, for AI collaborators |
| [`sources/`](sources/PROVENANCE.md) | Primary material and the variant apparatus, with per-file provenance rules |
| `tools/` | The harness — see below |
| `CLAUDE.md` · `AGENTS.md` | Operating context for AI collaborators and tools |
| [`DISCOVERIES.md`](DISCOVERIES.md) | **The findings worth writing about** — start here for what this research turned up |
| `RETROFIT.md` | Known consistency debt across chapters |
| `PLAN.md` | The harness: what is built, what is deliberately not |

## The tools

Stdlib Python only — no dependencies, so a fresh clone can run them.

```bash
python3 tools/check_locks.py               # do the 81 chapters still obey the locks?
python3 tools/concordance.py 明             # every chapter, line, gloss and rendering
python3 tools/concordance.py --english "clarity"   # is a rendering backed by its character?
python3 tools/concordance.py --formulas    # Chinese segments repeated across chapters
python3 tools/concordance.py --witnesses 25 # where the older manuscripts disagree
python3 tools/build_index.py               # regenerate glossary/INDEX.md and terms.yaml
python3 tools/fix-linebreaks.py            # restore the verse's hard line breaks
python3 -m unittest discover -s tools/tests
```

`check_locks.py` is a gate: it reads the locked renderings out of the glossary entries' own frontmatter and reports where the manuscript contradicts a decision already made. It never rewrites the verse, and it never fires on the English alone — a forbidden rendering is only an error when the character licensing it is present in that same chapter's Chinese. `concordance.py` is the opposite kind of tool: it judges nothing and never fails.

To have the locks checked before every commit:

```bash
git config core.hooksPath .githooks
```

The hook checks only the chapters you are committing, only at error severity, and skips chapters still marked `status: untranslated`. `git commit --no-verify` bypasses it once; `process/shaloms-call.md` is where a rule gets set aside for good.

## Method, briefly

The base text is the **Wang Bi** received recension. Where the older witnesses — **Guodian** (~300 BCE), **Mawangdui** (before 168 BCE), **Beida**, **Fu Yi** — differ in a way that changes meaning, the fork is logged and the choice explained.

Contested lines are read four ways before rendering: the **characters themselves** (Shuowen Jiezi, oracle-bone and bronze forms, radical decomposition), the **manuscript witnesses**, the **classical commentaries** (Wang Bi, Heshang Gong, Han Feizi's 解老 / 喻老), and the **internal evidence** of how a term behaves across all 81 chapters.

Terms are **locked**: once a rendering is settled it applies everywhere, and departures are logged. Where this translation departs from the English convention — *integrity* not "virtue," *sky and earth* not "heaven and earth," *the Tao* left untranslated — the reasoning is in [`glossary/`](glossary/) and [`process/overlay-audit.md`](process/overlay-audit.md).

## Status

| Chapters | State |
|---|---|
| 1–60, 65 | First draft complete |
| 61–64, 66–81 | In progress |

A full editing pass follows the completed first draft. Early chapters predate several later decisions; see [`RETROFIT.md`](RETROFIT.md).

## License

[**CC0 1.0 Universal**](https://creativecommons.org/publicdomain/zero/1.0/) — public domain, no exceptions anywhere in this repository.

Reproduce it, adapt it, print it, perform it, translate it onward, train on it, or sell it. No permission needed, no attribution required, no strings. The Tao Te Ching belongs to everyone; a new English rendering of it should too.

*A companion volume — the story of how these decisions were made — is in preparation separately.*

---

*為而不爭* — act, and do not contend.
