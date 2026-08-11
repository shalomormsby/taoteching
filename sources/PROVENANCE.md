# PROVENANCE — what may live in `sources/`, and on what authority

*This directory holds primary material consulted during translation. Every file in it must be **provably free**, because this repository is dedicated CC0 with no exceptions, and because the companion volume in `../taocompanion` is intended to be **sold**.*

**Read the admission rules before adding anything.** They are stricter than copyright law requires, deliberately.

---

## A correction, 2026-08-11

**This file previously said Chinese Wikisource could not be used, because its content is CC BY-SA 4.0. That was wrong**, and the error was over-caution: it read the site-wide licence banner instead of the copyright policy.

Wikisource's policy says the opposite, in terms:

> *"the transcription of a work on Wikisource does not create a new copyright, so if the original work has entered the public domain the transcription here is also public domain"* … *"anything that could attract copyright would no longer be faithful to the original, and because of that, the CC BY-SA default license for contributions never comes into play for mainspace content."*

That is Wikisource's own account of its own licence, and it matches the law it is reasoning from (*Feist* 1991; *Bridgeman v. Corel* 1999). **The blocker described here for three weeks did not exist.** The caution was cheap and the correction is cheaper; recorded rather than quietly edited away, because a provenance file that hides its own mistakes is worth nothing.

**What does not change:** ctext.org's structured data really is **CC BY-NC-SA 3.0**, and NonCommercial really is incompatible with the companion volume. And the exclusion of the excavated manuscripts stands on entirely different grounds — see below.

---

## Why stricter than the law requires

The ancient texts are free. The Laozi is roughly 2,400 years old; Wang Bi died in 249 CE; Heshang Gong and Han Feizi are older still. No copyright subsists in any of them, and a faithful transcription of a public-domain text creates no new copyright — in the United States see *Feist v. Rural Telephone* (1991), rejecting "sweat of the brow," and *Bridgeman Art Library v. Corel* (1999) for faithful reproductions.

**So why keep rules at all?** Because "the characters are ancient, therefore the file is free" needs to be *true of the specific file in front of you*. Two things can make it untrue:

1. **A source can have its own licence over its own additions.** ctext.org licenses its structured data **CC BY-NC-SA 3.0**. The characters are not theirs, but the database is.
2. **Modern editions really do add protectable material.** Not the characters, but the **punctuation**, the collation apparatus, the emendations, the reconstruction of damaged graphs, the annotations, and the selection and arrangement. Some of that is thin; some is genuine scholarship by living people.

---

## The admission rules

**A file may be added only if all four hold.**

1. **The work itself is public domain by age** — pre-modern, and its author long dead.
2. **The specific printing or transcription is either pre-1929, or dedicated CC0 / marked public domain, or a faithful transcription of such a printing.** "Found on the open web" is not provenance; the *edition* must be nameable.
3. **Its frontmatter names that source exactly** — work, author, edition, dates, host, and URL.
4. **Any modern editorial layer is either absent, excluded, or marked.** Punctuation especially.

**And one category is excluded outright, on grounds unrelated to licence text.**

**No transcriptions of the excavated manuscripts.** The **Mawangdui** silks were excavated in 1973 and the **Guodian** slips in 1993. Reconstructing their damaged and missing graphs — the brackets, the □ marks, the conjectural readings — is **genuine editorial work by living scholars**, not faithful transcription of anything. Reproducing a reconstruction reproduces the scholarship.

**Instead, record the facts.** See `variants.yaml`. "Mawangdui A and B read 自今及古 where Wang Bi reads 自古及今" is a **fact about a text**, and facts are not copyrightable. This is not merely the safe path; it is better practice, because a fact can be cited and checked while a bulk transcription only invites trust.

**No modern translations, of anything, for any reason.** Consulting them for *meaning* is governed by `process/method.md` §3 — pre-1931 only. None belong in this repository.

---

## What is here

| Path | Contents | Coverage |
|---|---|---|
| `variants.yaml` | The variant apparatus, as **facts** | 22 forks across 11 chapters |
| `commentaries/wangbi/` | 王弼 (d. 249 CE) on the Laozi, lemma by lemma | **71 of 81 chapters** |
| `.cache/` | The fetched wikitext the import ran from | gitignored |

### `commentaries/wangbi/` — 老子道徳經注

**Source:** 欽定四庫全書 (Siku Quanshu), 子部十四 · 道家類 — imperially commissioned 1773, completed 1782. Transcribed on Chinese Wikisource in mainspace, tagged `{{PD-old}}`, at [老子道徳經 (四庫全書本)](https://zh.wikisource.org/zh-hant/老子道徳經_(四庫全書本)). A scan of the same edition, digitised by Zhejiang University Library, is at [archive.org/details/06049303.cn](https://archive.org/details/06049303.cn).

**Punctuation: none.** The transcription's own editorial policy excludes it — the wikitext opens *請根據四庫全書掃描版校對本頁 … 加標點請另外建立頁面* ("proofread against the Siku Quanshu scan … to add punctuation, create a separate page"). So the vendored text is the authorial layer only, which is both the cleanest rights position and the more faithful one.

**Imported by `tools/import_commentary.py`**, which is the point: the vendoring is **reproducible**, and it **verifies itself**. The source interleaves Laozi lemmas with Wang Bi's comment on each, so every lemma is matched against our own `source/chinese.md`:

```
71/81 chapters · 328 lemma lines matched exactly, 26 with variants (93%) · 470 commentary lines
```

A lemma that matches is direct evidence the transcription was carried across intact at that point. Lemmas that differ are **reported, never normalized away** — Siku glyph forms go in the importer's `ORTHOGRAPHIC` map, and genuine forks go in `variants.yaml`.

**The 10 missing chapters — 8, 14, 15, 19, 30, 54, 62, 70, 71, 78** — are simply not yet transcribed on Wikisource. To add them: transcribe from the archive.org scan above, or wait for the proofreading, then re-run the importer. `concordance.py --commentary N` says so plainly rather than failing silently.

**Preserved from the edition:** the Siku compilers' own collation notes, marked 〔…〕. They are 18th-century editorial matter, public domain by age, and immediately useful — the note at Ch 21, 〔案狀各本俱作然〕 ("for 狀, all editions read 然"), reopened a decision we had already made. **□** marks a glyph the transcribers could not encode; a gap is never passed off as text.

### Still owed: 河上公 (Heshang Gong) and 韓非子 (Han Feizi)

**Heshang Gong is available and its path is known.** Chinese Wikisource has 老子道德經 (四部叢刊本), whose provenance is *景常熟瞿氏鐵琴銅劍樓藏宋刊本* — a photo-reproduction of the **Song** printed edition held in the Qu family's Iron-Qin-Copper-Sword Tower, Changshu, in *Sibu congkan* volume 0532. Clean by age and by edition.

The obstacle is mechanical, not legal: that text is **transcluded from the `Page:` namespace**, one wikipage per scan image (`<pages from="16" to="51" index="Sibu Congkan0532-河上公-老子道德經-1-1.djvu" />`), so it must be assembled from ~36 pages per volume, and its chapter boundaries are not marked in the wikitext. Roughly a day's work to do properly, and worth doing — Heshang Gong's reading of Ch 21's 閱 as 稟 ("to bestow") is the sort of dissent that should be one command away.

Han Feizi's 解老 / 喻老 is the oldest commentary on the Laozi and covers only part of the text; it should be added chapter-selectively.

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
