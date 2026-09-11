---
id: witnesses-before-drafting
title: "Check the witnesses before drafting, not after"
status: active
since: 2026-08-20
trigger: "you are about to read a chapter's base text closely, or about to change a settled line"
applies: [drafting, notes]
evidence: ["notes/manuscript.md#ch-25-王亦大-人亦大-king-or-human-among-the-four-greats", "notes/manuscript.md#ch-21-道之為物-道之物-the-silks-drop-the-copula"]
check: none
supersedes: []
---

# Check the witnesses before drafting, not after

**The rule.** Run `concordance.py --witnesses N` **before** reading the base text closely. Whether the oldest witnesses carry the chapter at all, and where they disagree with it, changes what you are translating — and it cannot be discovered by reading the received text more carefully.

**When it fires.** At the start of every chapter, and again before changing any line that is already settled.

---

## Why this holds

**A base text is one witness, not the text.** Ours is 王弼 (*Wáng Bì*), third century CE, and the chapters reach us through transmitters who emended. Reading it closely tells you what **that** text says; it cannot tell you the line was added, reversed, or is absent from everything older.

**Two chapters were drafted over exactly that, and neither was carelessness.** Ch 21 was drafted over **a chronology both Mawangdui silks reverse**. Ch 25 was drafted over **a king the oldest witnesses do not have.** Nobody had looked.

**Attestation changes how much weight the base can bear.** Guodian (~300 BCE) carries **31 of 81 chapters**. *Not attested* means the chapter rests on the silks and later — a fact about confidence that should be visible while drafting, not discovered afterwards. It decided ch 4 against ch 56: ch 56 held the ground because it is attested **complete** at Guodian; ch 4 is not attested at all.

**And a blank result is not an answer.** `sources/variants.yaml` is built by hand, chapter by chapter. **A blank means nobody has checked that chapter yet**, not that there are no forks — and the tool says so.

---

## The cases

**Ch 25's 王亦大 / 人亦大** — *king* or *human* among the four greats. The oldest witnesses do not have the king, and the received text installed a throne. → [ch 25](../../notes/manuscript.md#ch-25-王亦大-人亦大-king-or-human-among-the-four-greats)

**Ch 21's 道之為物 / 道之物** — the silks drop the copula, and the chapter was drafted over a chronology they reverse. → [ch 21](../../notes/manuscript.md#ch-21-道之為物-道之物-the-silks-drop-the-copula)

---

## Where it does not fire

**It does not license following a witness by default.** The base text is the base; departing from it is a decision that gets argued and recorded, as at ch 39's 故致數譽無譽 and ch 29's 挫 → 載.

**And a claim about a manuscript is not evidence unless it is in `sources/variants.yaml`.** A popular *"帛書版"* (*bó shū bǎn* — "silk-manuscript edition") text online had been **silently emended**, and we took it for the silks. `DISCOVERIES.md` §1 carries the banner. **Do not trust a manuscript claim that is not in the apparatus.**

---

## What it obliges

1. **Run `--witnesses N` first, before the close reading.** The tool opens with whether Guodian carries the chapter at all.
2. **Read a blank result as "nobody has looked."** Then look, and record what you find.
3. **Record new forks as facts, never transcriptions.** See [[record-the-fact]] — that is a licensing rule, not a preference.
4. **Log meaning-bearing forks in `notes/manuscript.md`** as well as the apparatus.
