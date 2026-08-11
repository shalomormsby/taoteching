# PROVENANCE — what may live in `sources/`, and on what authority

*This directory holds primary material consulted during translation. Every file in it must be **provably free**, because this repository is dedicated CC0 with no exceptions, and because the companion volume in `../taocompanion` is intended to be **sold**.*

**Read the admission rules before adding anything.** They are stricter than copyright law requires, deliberately.

---

## Why stricter than the law requires

The ancient texts are free. The Laozi is roughly 2,400 years old; Wang Bi died in 249 CE; Heshang Gong and Han Feizi are older still. No copyright subsists in any of them, and a faithful transcription of a public-domain text creates no new copyright — in the United States see *Feist v. Rural Telephone* (1991), rejecting "sweat of the brow," and *Bridgeman Art Library v. Corel* (1999) for faithful reproductions.

**So why the caution?** Because "the characters are ancient, therefore the file is free" is an argument, and this repository should not require a reader to accept an argument in order to trust its licence. Two further reasons, both concrete:

1. **The obvious digital sources are not free.** The Chinese Text Project (ctext.org) licenses its structured data **CC BY-NC-SA 3.0**; Chinese Wikisource is **CC BY-SA 4.0**. ShareAlike cannot be relicensed CC0, and **NonCommercial is the sharper problem** — an NC-licensed source anywhere in the derivation chain of a book intended for sale is the wrong shape, regardless of whether the underlying characters are free.
2. **Modern editions really do add protectable material.** Not the characters, but the **punctuation**, the collation apparatus, the emendations, the reconstruction of damaged graphs, the annotations, and the selection and arrangement. Some of that is thin; some of it is genuine scholarship by living people.

---

## The admission rules

**A file may be added only if all four hold.**

1. **The work itself is public domain by age** — pre-modern, and its author long dead.
2. **The specific printing or transcription it came from is either pre-1929, or dedicated CC0 / marked public domain by its holder.** "Found on the open web" is not provenance.
3. **Its frontmatter names that source exactly** — work, author, edition, publisher, year, and where it was obtained. A file whose edition cannot be named does not go in.
4. **Any modern editorial layer is either excluded or marked as such.** Punctuation especially: note whether it is present and that it is editorial.

**And two categories are excluded outright.**

**No transcriptions of the excavated manuscripts.** The **Mawangdui** silks were excavated in 1973 and the **Guodian** bamboo slips in 1993. Every transcription of them is modern, and reconstructing the damaged and missing graphs — the brackets, the □ marks, the conjectural readings — is **genuine editorial work by living scholars**. Reproducing someone's reconstruction is reproducing their scholarship.

**Instead, record the facts.** See `variants.yaml`. "Mawangdui A and B read 自今及古 where Wang Bi reads 自古及今" is a **fact about a text**, and facts are not copyrightable. This is not merely the safe path; it is the better scholarly practice, because a fact can be cited and checked while a bulk transcription only invites trust.

**No modern translations, of anything, for any reason.** Consulting them for *meaning* is governed by `process/method.md` §3 — pre-1931 only. None of them belong in this repository.

---

## What is here

| Path | Contents | Status |
|---|---|---|
| `variants.yaml` | The variant apparatus, as **facts** — chapter, base reading, witness readings, whether meaning-bearing, our call | **populated** |
| `commentaries/` | Wang Bi, Heshang Gong, Han Feizi 解老 / 喻老 | **empty — see below** |

### `commentaries/` is empty, and that is not an oversight

No commentary text has been added, because **no source meeting rule 2 has been obtained yet.** The commentaries were consulted during translation by reading them online, which is entirely proper for research; what is not proper is copying that text into a CC0 repository on the strength of the ancient-characters argument alone.

**To populate it, one of these is needed:**

- A **scan of a pre-1929 printing**, from which the text is transcribed. The recension with Wang Bi's commentary is printed in the *Sibu congkan* (四部叢刊, Commercial Press, first series from 1919) and the *Sibu beiyao* (四部備要, Zhonghua, from the early 1920s, based on a Ming edition), among others. Scans of Republican-era collectanea appear on the Internet Archive and in HathiTrust; the specific volume and its printing date must be verified, not assumed.
- Or a digital edition whose holder has **dedicated it CC0 or marked it public domain** in writing.

When such a source is in hand, the shape is one file per chapter — `commentaries/wangbi/021.md` — each opening with frontmatter naming the edition it was transcribed from, and each noting whether punctuation is present and editorial.

**Until then the honest state of this directory is: empty, with the acquisition path written down.** Better an empty directory with rules than a full one with a licence nobody can defend.

---

## Frontmatter for a commentary file

```yaml
---
work: "老子道德經注"          # the commentary's own title
author: "王弼"                # 226-249 CE
chapter: 21
edition: "四部叢刊 初編"       # the exact printing transcribed from
publisher: "商務印書館"
year: 1919
obtained: "https://archive.org/details/…"   # or: "physical copy, <library>"
punctuation: "editorial, present"           # or "none in source"
rights: "public domain by age; printing predates 1929"
transcribed: 2026-08-11
---
```

---

## On citing rather than copying

Where a commentary's *reading* matters to a decision, the practice already in use is the right one: **quote the phrase that carries the argument, gloss it, and cite it.** Wang Bi's gloss on Chapter 21 — 此上之所云也, *"'this' is what was said above"* — is nine characters, and quoting nine characters of a third-century commentary to make an argument about it is fair by any standard and free by age.

A repository does not need to *contain* a library in order to *use* one.
