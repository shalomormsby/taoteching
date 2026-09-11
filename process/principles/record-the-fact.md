---
id: record-the-fact
title: "For the excavated witnesses, record the fact — never the text"
status: active
since: 2026-08-11
trigger: "you are about to add a reading from Mawangdui or Guodian to the repository"
applies: [notes, tooling]
evidence: ["sources/PROVENANCE.md#the-admission-rules", "sources/PROVENANCE.md#the-guodian-question-asked-properly-and-answered-no-2026-08-17"]
check: none
supersedes: []
---

# For the excavated witnesses, record the fact — never the text

**The rule.** **Never transcribe the Mawangdui or Guodian manuscripts into this repository.** Record the *fact* of a variant instead — that this chapter reads X where our base reads Y — in `sources/variants.yaml`, and cite where the reading comes from.

**When it fires.** Every time an excavated witness has something to say, which is often.

---

## Why this holds

**This is a licensing rule, not a scholarly preference, and it is the sharper of the two constraints.** Reconstructing damaged graphs from lacunose silk and bamboo **is living scholarship**: the editors' judgments about what a broken character was are original work, protected, and recent. A transcription is therefore not a public-domain text in the way a Song woodblock of 王弼 is.

**And there is no public-domain transcription of the Guodian slips, and there cannot be one yet.** The question was asked properly and answered no, in writing, with the reasoning kept.

**A `shaloms-call` cannot fix this one**, and that is worth stating: the override mechanism can set aside this repository's own rules, and it has no authority over somebody else's copyright. Every other rule here is ours to suspend. This one is not.

**The fact is not encumbered, and it is what the work actually needs.** *"Both Mawangdui silks reverse this chronology"* is a statement about the world. It supports every argument a transcription would, and the apparatus is more useful than a text would be — because what a chapter review needs is **where the witnesses disagree**, not another edition to read.

**This is why `guodian-inventory.yaml` exists**: an inventory of what the oldest witness contains, chapter by chapter — never a text.

---

## The cases

**The admission rules** — four conditions, all of which must hold, plus one category excluded outright on grounds unrelated to licence text. → [PROVENANCE](../../sources/PROVENANCE.md#the-admission-rules)

**The Guodian question**, asked properly and answered no, with the reasoning preserved rather than the conclusion alone. → [PROVENANCE](../../sources/PROVENANCE.md#the-guodian-question-asked-properly-and-answered-no-2026-08-17)

---

## Where it does not fire

**Transmitted commentaries are different and are vendored in full.** 王弼, 河上公 and 韓非 are public domain by age, from nameable editions, with per-file provenance. Nothing was reconstructed from damage.

**A commentator's lemma is a witness and may be quoted.** When 河上公 prints 知者 where our base prints 智者, that is a transmitted reading, not an excavated one.

**And no modern translations, of anything, for any reason** — a separate rule with a separate basis. The pre-1931 limit governs *translations*, and none are in this repository.

---

## What it obliges

1. **Read `sources/PROVENANCE.md` before adding anything to `sources/`.**
2. **Record variants as facts in `sources/variants.yaml`**, with the witness named and the difference stated — not the witness's text reproduced.
3. **Cite rather than copy**, and say which edition the claim rests on.
4. **Do not trust a manuscript claim that is not in the apparatus** — a popular online *"帛書版"* had been silently emended, and it cost `DISCOVERIES.md` §1 its central claim.
