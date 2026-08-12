# Translation Notes

*One of three notes layers. This one logs **our own rendering decisions** — the places where we deliberately depart from the most literal English for reasons of meaning, ethos, or clarity, and want the reasoning on record so a future reader (or a future us) can see it was a choice, not an accident.*

---

## Using this file

**What goes here — and what does not.**

| Layer | Holds |
|---|---|
| `notes/manuscript.md` | textual forks **between witnesses** |
| **`notes/translation.md`** ← this file | **our own rendering decisions and standing principles** |
| `notes/reading.md` | reader-facing interpretation; cross-cutting **Threads** |

Log only **deliberate departures** from the literal, never routine word-choices. Entry format: *chapter · the phrase · the choice · why* — and where a rendering was retired, say what it was and when.

**How it is ordered.**

| Level | What it is |
|---|---|
| `##` | one of the four sections below, in this fixed order |
| `###` | a chapter (`Ch 62`), or — in sections 1–3 — a single principle, lock, or thread |
| `####` | one decision, titled `character → "rendering"` |

1. **Standing principles** — rules that govern every chapter.
2. **Locks — the rationale** — why a locked rendering is the one it is. The lock itself lives in `CLAUDE.md` and the glossary; the argument lives here.
3. **Cross-chapter decisions** — threads and sweeps belonging to no single chapter.
4. **Chapter notes** — **ascending by chapter number**. Within a chapter, entries follow the order the lines appear in the verse.

**Four rules that keep it that way.**

1. **Every decision gets an `####` heading**, even when a chapter has only one. Uniform outline, and every decision gets an anchor that can be linked to from a chapter file or from `CLAUDE.md`.
2. **The heading carries only the stable claim** — `#### 奧 → "the sanctuary"`. Supersessions, dates, and *(was: …)* go on the line beneath it. A heading that records history rots every link pointing at it.
3. **New chapters are inserted in number order, never appended.** Chronology is git's job, and git does it better.
4. **No `---` between entries.** Headings do that work. Rules separate the four `##` sections only.

**Before adding an entry, check whether the chapter already has one.** Appending blind has produced a real duplicate here once already (三公, merged 2026-08-11).

**No machine reads this file.** `check_locks.py` parses only `notes/manuscript.md`, and only by substring-matching `Ch N `. So this file can be reorganized freely; `manuscript.md` cannot lose that literal string per chapter without blinding the `unlogged-variant` rule.

---

## Standing principles

### Lineation and punctuation — "the marks are yours; the music isn't"

The ancient text carries **no punctuation and no line breaks** — it is unbroken columns of characters. Every comma, period, and line-break in the Chinese Text Project (and in every modern edition) is a *later editor's* addition. So on the page, punctuation and lineation are **ours** — expressive tools, to be used freely and deliberately.

But the source is not formless. Classical Chinese — and the Daodejing above all — moves in **regular character-beats** and **parallel pairs and triads**, and that pulse is real and audible even without a single mark. (Chapter 56: 塞其兌，閉其門，挫其銳，解其紛，和其光，同其塵 is *six even three-character phrases*, grouped as three couplets — close the senses · blunt-and-untangle · dim-and-merge.)

Hence the rule: **the marks are ours; the music is the source's.** Lay the English out freely, but let the layout *track* the original's rhythm and parallelism rather than cut across it — and **stay consistent within any parallel series.** The original weighs those six phrases equally; giving four of them their own lines while fusing the last two quietly overrides a symmetry the text is holding. When an instinct says *join these* (as 和光同塵 — "dim the light, merge with the dust" — is one bound gesture), trust it, then *extend* it, so the whole series is treated alike. Freedom in the marks; discipline in the music.

### Typography — lowercase, and no em-dashes in the verse

**Lowercase everything but the Tao.** The Chinese has no capitals; every one in the English is ours, and in English **capitals confer status** — they turn a word into a doctrine and a figure into a deity. So: *the sage*, *the mother*, *the uncarved*, *stillness*, *the limitless*, *profound integrity*, *the great Tao* — all lowercase. **道 keeps its capital** because "Tao" functions as a proper name, and proper nouns in editorial notes (Mawangdui, Guodian) keep theirs. Nothing else does. *(This is the Tier-3 "devotional capitalization" problem named in `process/overlay-audit.md` — the overlay that enters below the level of vocabulary.)*

**母 stays lowercase — the case that tested the rule.** *(decided 2026-08-11 by Shalom, after argument.)* 母 (*mǔ* — mother) is the strongest candidate in the book for a second capital, and it was capitalized in four documents for months without anyone having decided it. **She stays lowercase**, on five grounds:

1. **Ch 25 draws the line itself, in the chapter that licenses the Tao's capital.** 可以為天下**母** (*"it can serve as the mother of the world"*) → 吾不知其名 (*"I do not know its name"*) → 強字之曰**道** (*"forced, I style it the Tao"*). The text offers *mother* as a role, then says it has no name, then coins one under protest. Wang Bi glosses the middle line 名以定形 — *"a name fixes a form"* — and this has none. A capital would confer the name the chapter withholds.
2. **The grammar never names her.** All seven occurrences are genitive (萬物之母, 有國之母), possessive (其母 ×2), the object of a verb (食母), or governed by 為 — *serve as* (可以為天下母, 以為天下母). She is never a bare subject and is never addressed. English proper nouns do not take genitives that way: we say *Athena*, not *the Athena of the city*.
3. **Both classical commentators call it a comparison, explicitly.** Heshang Gong on 25: 道育養萬物精氣，**如**母之養子 — *"the Tao rears the countless things' vital breath, **like** a mother nourishing her child"* — where 如 means *like*. Wang Bi on 52: 母本也，子末也 — *"the mother is the root, the child the branch-tip,"* a structural pair.
4. **The overlay risk is the modern kind.** Capital-M *Mother* in English is occupied by the Great Mother of Jung and Neumann, Mother Nature, Holy Mother. Importing a twentieth-century archetype is the same move as importing *Logos*, from a different century — and this edition already rejected 自然 → "Nature" on that ground. Note also what 母's own lock forbids: *"the Source," "the Origin," "the Ground of Being"* — three capitalized abstractions. The capital is the gesture they have in common.
5. **The capital works against the feminine rather than for it.** In English capitals confer *institutional* status, not intimacy — compare *my mother* with *my Mother*. 母 is 女 (a kneeling woman) with **two dots added at the breasts**; the nursing body is the only thing distinguishing it from "woman," and Ch 20's 食母 is nursing at that breast. Ch 52 reads *"Find our mother, and you know her children"* — near and familial. *"Find our Mother"* is liturgy. **The capital promotes her out of the body and into a pantheon, which is how she was lost the first time**, when translators reached for "the Source."

**And the rule is not a hierarchy.** 道 keeps its capital because *"Tao"* is **transliterated**, not translated — grouped, above, with proper nouns in editorial notes (Mawangdui, Guodian). Every *English* word in this edition is lowercase. So *mother* is not ranked below the Tao; they are on opposite sides of a line about language, not status.

*The one exception in the repository: glossary entry `##` headings are Title Case by house convention — "The Countless Things," "Sky and Earth," "The Mother." That is a title format, not a rendering claim.*

**Sweep, 2026-08-11:** 45 instances lowercased across `CLAUDE.md`, `README.md`, `DISCOVERIES.md`, `process/method.md`, `process/overlay-audit.md`, both notes files, and six glossary entries. `chapters/` was already clean — all 14 occurrences in the verse were lowercase, and `check_locks.py` carries `"Mother": "母"` in `_DEVOTIONAL`, so a capital in the verse has always been a hard error. The drift was entirely in the prose *about* the verse. *(Not swept: `process/legacy-tao-source-code.md`, archived and superseded, and `source/archive-*`, frozen.)*

**Avoid the em-dash in the verse.** Two reasons. It has become a conspicuous marker of machine-written prose, which is corrosive to a translation made this way and offered in good faith. And more importantly, it **strands grammatical subjects**: a dash lets a clause trail into a participle whose actor is unnamed, which is exactly how Chapter 2's *"the sage does not begin them — giving birth without possessing…"* left a reader unable to tell whether the sage or the countless things were doing the giving. Classical Chinese omits subjects freely; English cannot, and a dash disguises the omission instead of resolving it. **Name the subject and end the sentence.**

### The 天 family — "no heaven, and no cosmos either"

**The rule: point, don't categorize.** 天 is neither a realm nor an abstraction. Render it as what a person standing on the ground can actually see.

- **天地** → **sky and earth** — always both nouns, never fused into one
- **天下** → **the world** (locked at 48, 56, 57; literally *under-sky*, idiomatically the human realm)
- **天 alone, as the impersonal ordering principle** — 天之道, 天道, 事天 → **nature / the natural**: "the way of nature," "serving nature"
- **天 as a rung in the four-greats ladder** (25) → **sky**: *humans follow earth, earth follows sky, sky follows the Tao, the Tao follows its own self-so*

**Why not "heaven."** The cadence "the beginning… heaven and earth" is Genesis 1:1 nearly verbatim — it installs a creator in the very chapter denying that the source can be named. And the word is not a neutral convention but a **missionary inheritance** (see Process guide §3, and the overlay audit).

**Why not "cosmos."** A Greek term of art (κόσμος, *ordered arrangement*), abstract, singular, and modern-scientific in register — and it collapses a pair the text keeps splitting: 天地之**間**, the space *between* them (5); 天大，地大, counted separately among the four greats (25); 地法天, distinct rungs (25); 天長地久, split predicates (7); 天地相**合**, they *join* and dew falls (32). You cannot have a between, a ladder, or a coupling with one thing.

**Strain cases, left unsettled rather than forced:** 天門 (10) — may be the gates of the senses, not the sky; 天將救之 (67) — reads agentive. *(天子 (62) was a third, and was settled 2026-08-11 → "a child of the sky." See Ch 62 below.)*

**Retrofit sweep — this rule is almost entirely retroactive.** 天地 occurs in **Chapters 1, 5, 6, 7, 23, 25, 32** — every one inside the completed 1–38 range, and *nowhere* after 38. Also **59**, where 事天 currently reads "serving the cosmos" → *serving nature*. Forward-facing only: 天之道 in **73, 77, 81** and 天道 in **79**.

*Full argument and evidence: "Glossary — 天地 (Tiān Dì), Sky and Earth."*

---

## Locks — the rationale

### 無為 → "non-doing"

*(not "non-action")*

The conventional English is "non-action"; we depart from it deliberately, on three grounds. **(1) The chime.** 無為而無不為 (ch 37, 48) repeats the same character, 為 then 不為, so the English should repeat the same word: *"does not do, yet nothing is left undone"* — *do* and *undone* share a root and close the line on itself, which "non-action … left undone" cannot. **(2) The register.** 為 is a hand laid on an elephant — concrete, manual, Anglo-Saxon territory; "action" is abstract, Latinate, and a term of art in Western philosophy. It also slides morphologically into "**inaction**," which is the two-thousand-year quietist misreading. **(3) Chapter 63 decides it.** 為無為，事無事，味無味 is a triple parallel of ordinary verbs, each negated and taken as an object. The structure survives only with a word that is both verb and noun. *Doing* is; *action* is not ("act the non-action, affair the non-affair" collapses). One chapter with three parallel members, and only one candidate holds all three.

Also rejected: **"effortless action"** — an interpretation smuggled into a rendering, which resolves the paradox in advance and deletes the negation that gives 無為而無不為 its whole force. And **leaving it untranslated** — we keep 道 untranslated because every rendering is wrong; 無為 is renderable, and rendering it keeps the reader inside the argument instead of handing them a mantra.

*The middle member of that triple is rendered **"tend the not-tending"** — see Ch 63 below, which supersedes the illustrative "attend the not-attending" used in `glossary/wuwei-無為.md`.*

*Full reasoning: `glossary/wuwei-無為.md`. Sweep: ch 2, 3, 10, 37, 38, 43, 48, 57, 63, 64.*

---

## Cross-chapter decisions

### Ch 57–58 · 正 / 奇 — one thread, and 其無正 ≠ "no limit"

Two linked calls. First, 其無正 (孰知其極？其無正) is "it has no fixed norm," *not* "no limit" — 極 (limit) is the prior clause; 正 here is the *normative / correct*, and it has to survive into the next line, whose subject is that same 正: 正復為奇 ("the straight turns crooked"). Render 正 as "limit" and the keyword vanishes. Second — the reason this is logged — 正 and 奇 must read the **same** in 57 and 58, because 58 is deliberately unmaking 57: there the ruler governs *with* 正 and wages war *with* 奇 (以正治國，以奇用兵), certain of the boundary; here 正復為奇 erases it. We thread them **straight / crooked** — 57's "govern with the straight" and "the people straighten themselves" (民自正), 58's "the straight turns crooked" — so the reader feels 58 pull 57 apart. (奇 keeps a little play — "surprise / the oblique" where 57 means battlefield tactics — but 正 holds as *straight / upright* throughout both.)

### Sweep · Ch 8, 20, 21, 31, 38 — the four locks 信, 精, 器, 眾

Four entries were written together (`xin-信.md`, `jing-精.md`, `qi-器.md`, `zhong-眾.md`) and each obliged changes in the verse. Logged together because the pattern matters more than the individual lines.

**眾 → the crowd.** The word had drifted into four Englishes: *all* (1), **dropped entirely** (8), *the masses* six times (20), *the many* (21). "The masses" is out — it imports a nineteenth-century class politics Laozi has no word for, and Ch 20's crowd is *merry at a spring festival*, not a proletariat. Ch 20's six lines now read *the crowd*, with agreement adjusted. Ch 31's 殺人之眾 becomes *"when many have been killed."*

**Ch 8 · 處眾人之所惡 was not translated at all.** The line had become *"It seeks the lowest places"* — which keeps the water and deletes the people the water is being measured against. 惡 (*è*) is *to find distasteful*, and the claim is comparative: water goes where **the crowd will not**. Now *"It dwells where the crowd will not go."* This is the most substantive change in the sweep, and it was invisible to the checker, which can only see renderings that are wrong, never ones that are missing.

**Ch 8 · 言善信 → "In speech, it is trustworthy"** *(was "In spoken words, it is sincerity")*. 信 is a **split tally** — a correspondence that can be checked — not an inner state. Sincerity is unfalsifiable; you can be sincerely unreliable.

**Ch 38 · 忠信之薄 → "the thinning of loyalty and trust"** *(was "the waning of integrity")*. Two characters had collapsed into one, and that one belonged to 德: 忠 (*zhōng* — loyalty) vanished, and 信 took 德's locked word for the second time in the book (Ch 23 was the first). 薄 (*bó*) is literally **thin**, which matters because the chapter closes on the same axis — 處其厚，不居其薄, *dwell in the thickness, not the thinness*. "Waning" broke a thread the chapter returns to.

**Ch 21 · 精 → "vital essence"** *(was "the primordial mass of creation")*. 精 is 米 (*mǐ* — rice) with *Shuowen*'s gloss **擇也**, to sift: **hulled grain**, what is left when the bulk is taken away. "Primordial mass" was the precise inversion — mass is the husk 精 is winnowed *from* — and it dated the text to the twentieth century. The following line's 其中有信 also surfaced properly: *"This essence is utterly real, and it can be trusted."*

**器 → vessel / tool / implement**, promoted out of 樸's `covers:` into its own entry. Nine chapters is too much reach for a footnote, and Ch 41's 大器 and Ch 67's 器長 use a **capacity** sense — what a person can hold — that 樸's entry had no room for. No verse changed: Ch 29 was fixed earlier in the session and the rest were already inside the lock.

**One thing this sweep taught, now recorded in `CLAUDE.md`.** A `forbidden:` rendering must be a word **no other character in those same chapters can legitimately claim.** "Integrity" cannot be forbidden for 信, because chapters 21, 23, 38 and 49 hold both 信 and 德. "Energy" cannot be forbidden for 精, because Ch 55 holds both 精 and 氣 and 氣 rightly takes *vital energy* there. The checker gates on presence of a character and cannot say *right for that one, wrong for this one, same chapter*. Those two distinctions are held by the entries and by the reader, not by the tool.

---

## Chapter notes

### Ch 14

#### 無物 → "no-thing," both times

*(was: "nothingness" and "no-image")*

**無物** (*wú wù* — "no-thing") occurs **twice in the whole book, both in this chapter**, and was rendered two different ways, neither of them right.

| Chinese | Was | Problem |
|---|---|---|
| 復歸於**無物** | "returns to nothingness" | "nothingness" is forbidden for 無 — it imports the Void as a substance where 無 is simply *absence* |
| **無物**之象 | "the image of no-image" | 物 is a **thing**, not an image — and 象 (*xiàng* — image) is already the other half of the phrase |

That second line rendered the couplet 無狀之狀，**無物**之象 as *"the shape of no-shape, the image of no-image."* The symmetry is seductive and it was built on a mistranslation: **the line got its parallelism by duplicating 象 and deleting 物.** Now *"the shape of no-shape, the image of no-thing"* — genuinely parallel in the way the Chinese is, 無X之X twice with **different** X's.

"No-thing" keeps 物 audible and keeps 無 as absence. *(Hyphenated deliberately: "no thing" open reads as an emphatic "not anything," where 無物 is a **state** the thing returns to.)*

#### 執古之道，以御今之有 → "Hold the ancient Tao, and steer what is present now"

*(was: "to direct your present existence")*

Three repairs. **"Existence" is forbidden for 有** — 今之有 is *the presence of now*, what there currently is, not a person's lifetime. **"Your" was supplied**, and it shrank the line: the Chinese steers *what is*, not one's own affairs. And **御** (*yù*) is *to drive a chariot* — "steer" keeps the reins where "direct" is bloodless.

**A resonance now audible across chapters.** 執 (*zhí* — to grasp) is the same character as Ch 29's 不可**執**也, *"it cannot be grasped."* Ch 29 forbids grasping **the world**; Ch 14 commands grasping **the ancient Tao**. That looks deliberate: you cannot hold the world, so hold the thread instead. We keep "Hold" here rather than "Grasp" — *grasp the Tao* risks reading as *comprehend the Tao*, which is precisely what this chapter spends fourteen lines denying is possible.

### Ch 16

#### 王乃天，天乃道 → "the open sky"

*(not "nature," not bare "sky")*

Two decisions in one line. **First, it stays "sky."** Ch 16 and Ch 25 share this exact step — 王乃**天**，**天**乃道 (16) and 地法**天**，**天**法道 (25) — so rendering one "nature" and the other "sky" would hide from the reader that they are the same climb. The 天-family policy allows *nature* for 天 as an impersonal principle, but internal consistency outranks local fit; "reads better" is not a reason to break a lock.

**Second, the qualifier had to survive repetition.** The passage is *anadiplosis* — each line ends on the word the next begins with (容乃公，公乃王，王乃天，天乃道) — and the chain is the form. So a qualifier introduced once and dropped ("the all-covering sky… / The sky…") would break the link exactly where the poem holds itself together. **"The open sky"** repeats without thudding, stays an image rather than an abstraction, and carries both the vastness and the ownerlessness that make 天 the rung above 王: a king rules a domain, but the sky is over everything without preference (天無私覆).

#### 公 → "impartiality," not "equanimity"

公 is the direct opposite of 私 (*sī* — private, selfish): the public, the common, what belongs to no one. Equanimity is inner calm and sends rung two back inside the person, stalling an ascent whose whole motion is *outward*. With "impartiality," the ladder reads as one continuous widening of the circle beyond the self. *(See the Ch 16 Reading Note. This is the rendering Ch 42 and Ch 62 will have to answer to when 公 is given a glossary entry — see `RETROFIT.md`.)*

### Ch 21

#### 道之為物 → "Whatever the Tao is, it is only vague, only elusive"

*(was "In the manifest realm, the Tao appears intangible and dark", then briefly "As a thing, the Tao is…")*

Two things were wrong with the original. **"The manifest realm" imports a two-realm metaphysics** — a manifest world set against an unmanifest one — that the line does not contain and the book does not hold. And **"dark"** was doing duty for 惚, where the lock reserves *dark* for 玄.

The first repair rendered it *"As a thing, the Tao is…"*, which was accurate and badly built. 道之為物，惟恍惟惚 is **topic–comment**: the topic is *what the Tao amounts to as an entity*, the comment is *only indistinct*. "As a thing," as a sentence opener, is neither an English topic construction nor a plain subject, so it dangles — and modern colloquial English has given *"a thing"* a sense (*is that a thing?*) that actively interferes. **"Whatever the Tao is"** renders the topic directly and idiomatically.

**The witnesses confirm the topic and settle nothing else.** Both Mawangdui silks read 道之物 without 為, making 之 a plain possessive — *the Tao's thingness*. Same sense, no copula. Logged in the Manuscript Notes and in `sources/variants.yaml`.

*Cost, on the record:* **物 is lost here.** It returns four lines later in 其中有物 (*"within it there is a thing"*), so the Chinese has an echo the English no longer carries — the Tao is a 物 with a 物 inside it. Traded deliberately: the echo is a scholar's pleasure and the clarity is the reader's, and the chapter's force is in the reversal, which lands harder from a plain opening.

*And 惟…惟… → "only… only…" is a choice, not a translation.* 惟 can be restrictive (*only*) or a mere emphatic particle, in which case the line is simply *"indistinct and vague."* We keep "only" because the chapter needs **nothing but vagueness** for the "and yet" of the descent to pay off — but the restrictive force is ours.

#### The four-fold descent — restoring 其中有X, the chiasmus, and the anadiplosis

The middle of Chapter 21 is one continuous structure and the English had dissolved it into five unrelated observations. The Chinese:

> 道之為物，惟恍惟惚。
> 惚兮恍兮，其中有象；
> 恍兮惚兮，其中有物。
> 窈兮冥兮，其中有精；
> 其精甚真，其中有信。

**Three devices, all of them load-bearing.**

**The refrain.** 其中有X occurs **four times** — 象 (*xiàng* — image), 物 (*wù* — thing), 精 (*jīng* — vital essence), 信 (*xìn* — trust). One phrase, four objects, each more real than the last: a semblance, then something actual, then its concentrate, then the fact that it holds. The English had rendered the four as *"appear forms," "appear entities," "lies vital essence," "it can be trusted"* — four different constructions, so the descent read as a list of findings rather than one repeated act of looking deeper into the same place.

**The chiasmus.** 惚兮恍兮 and then 恍兮惚兮: the same two words, reversed. The preamble introduces them as 恍-惚, line three reverses that, line four reverses again. Rendering both as some version of "intangible and dark" flattened a deliberate turn. Now **"Elusive and vague"** then **"Vague and elusive."**

**The anadiplosis.** Line four ends on 精 and line five opens 其精 — the same hinge Ch 16's ladder runs on (公乃王，王乃天…), where each line begins on the word the last one ended with. Now *"…within it there is vital essence. / Its essence utterly real…"*

**And the nesting was wrong.** 其中 is "within **it**" — the Tao — in all four lines. The English read *"within these intangible, dark **forms** appear entities,"* making the forms a container for the entities and inventing a hierarchy the Chinese does not have. Everything is found in the same place, at four depths of attention.

**"Dark" is gone from this stanza.** It had been doing duty for 惚 (*hū*), where the lock reserves *dark* for 玄 (*xuán*). 恍 and 惚 are near-synonyms for *blurred, indistinct, hard to fix* — the pairing is the point — so they take **vague** and **elusive**, which can also reverse in English. *(This also keeps faith with Ch 14, where the same compound 惚恍 already reads "the elusive.")*

*Not carried over: 兮 (xī), the sighing exclamatory particle, four times. English has no unembarrassing equivalent, and the doubled adjectives carry the incantatory quality instead.*

*Worth noticing, and left in the reading notes rather than the verse: the darkest word in the stanza, 冥 (míng — dim, obscure), is a homophone of 明 (míng — clear-seeing), the book's word for sight that is unobstructed. The chapter finds the real thing at the bottom of the dim.*

#### 以閱眾甫 → "In this name, I observe the origin of the many"

*(was: "the unerasable source code of all creation")*

The old rendering carried our own besetting temptation, the **mechanistic** — and almost certainly inherited it from `process/legacy-tao-source-code.md`, whose framework is superseded. Three things were wrong with it.

**"Source code" adds what the Chinese refuses.** 眾甫 (*zhòng fǔ*) is *the origin of the many*: 甫 is a **seedling in a field**, borrowed early as a respectful word for a man and so *father / beginning / that from which things come*. Code is **written, by someone**, which reinstalls the author the chapter is at pains to leave out, and it **executes deterministically**, where a seedling unfolds. Both imports are exactly backwards.

**閱 (*yuè*) is *to observe*, not *to be*.** The old line said the Tao **is** the origin; the Chinese says the persisting name is what lets you **see** the origin. A different and much smaller claim, and the honest one. *(Heshang Gong dissents, glossing 閱 as 稟 — to bestow — so that the Tao confers on the many and the question becomes how one knows they receive 氣 from it. We decline: that reads a Han cosmology of qi-transmission back into the line, and the closing question is explicitly epistemic — 何以**知**.)*

**"It" and "this" had no antecedents.** 其名不去，以閱眾甫: the instrument of 以 (*yǐ* — thereby) is 其名, **the name** — Wang Bi confirms it (以無名說萬物始也, "it is by the nameless that the beginning of the countless things is explained"). Naming it in the English fixes the first pronoun. The second is fixed by repetition: **"In *this* name … By *this*, here, now"** gives 此 a visible antecedent for the first time. *Cost, on the record:* pointing 此 at the name narrows it — Wang Bi glosses 此 as 上之所云, "what was said above," meaning the whole descent through 象 / 物 / 精 / 信. "Here, now" widens the referent back out past the name to the present encounter, so the line carries both readings at once. A controlled double rather than a vague one.

**And "the many," not "the countless things."** 眾 (*zhòng*) is not 萬物, and 萬物 does not occur in this chapter. Borrowing the 萬物 lock here would repeat the error just corrected in Ch 23, where 信 had been given 德's locked word. Elsewhere 眾 is rendered *all* (Ch 1's "the gate of all subtleties") and *the crowd* (Ch 20), so "the many" is in register. **"I," not "we,"** because the chapter's voice is 吾 (*wú* — the self *seeing*), which the next line makes explicit.

#### 吾何以知眾甫之狀哉 → "How do I know the origin of the many is so?"

*(was: "…the origin of the many?", with the contested word untranslated)*

The line's last content word is contested. Our base text reads **狀** (*zhuàng* — shape, form, condition); four older sources read **然** (*rán* — so, thus, that it is so). The English had rendered **neither**, asking simply "How do I know the origin of the many?" — which is why nothing had broken: the line was true under either reading, and silently so.

**We follow 然, and the decisive argument is not a manuscript one.** 狀 occurs **twice** in the whole book (here, and Ch 14's 無狀之狀, "the shape of no-shape"). 然 occurs **twelve** times. And 吾何以知…然哉？以此 is a **fixed closing formula**:

> Ch 54 · 吾何以知天下**然**哉？以此 — *"How do I know the world is so? By precisely this."*
> Ch 57 · 吾何以知其**然**哉？以此 — *"How do I know this is so? By this:"*
> Ch 21 · 吾何以知眾甫之**然**哉？以此 — *"How do I know the origin of the many is so? By this, here, now."*

**然 completes the formula; 狀 breaks it.** Three chapters ask one question and answer it one way, and the English now lets a reader hear that.

**Then the witnesses, all agreeing:** both Mawangdui silks read 然; the Song Heshang Gong edition reads 然; and the Siku Quanshu compilers wrote a collation note on this very line — 〔案狀各本俱作然〕, *"as for 狀, all editions read 然."* Our 狀 may be close to unique.

**And the word is load-bearing elsewhere.** 然 is the second half of **自然** (*zìrán* — the self-so): 自 (*zì* — self) + 然 (*rán* — so). The character that closes these three questions is the one Laozi builds his term for *being as one is, of oneself* out of. So the question "how do I know it is **so**?" is asked in the vocabulary of self-so-ness, and answered 以此 — *by this, here, now*: by the thing in front of you, being what it is of its own accord. *(See `glossary/ziran-自然.md` for 然's history — it began as a picture of roasting and was borrowed for its sound, so it is grammar rather than image.)*

**The base text is unchanged.** The Source table keeps 狀, and only the translation follows the older reading — the practice already established at Ch 41 (免成), Ch 42 (學父), Ch 47 (明) and Ch 53 (竽). `source/chinese.md` stays a faithful transcription of one recension rather than becoming a composite.

*Found because Shalom asked whether 然 was related to 自然. It is, and the relation is the argument.*

### Ch 23

#### 信不足焉，有不信焉 → "Where trust is withheld, trust is withheld in return"

*(and Ch 17 keeps its own rendering — a deliberate divergence)*

**⟡ Flagged for the editing pass.** This is the first place we knowingly render the same Chinese two different ways. It is a considered choice, not an oversight, and it should be revisited once all 81 chapters exist as first drafts.

The seven characters 信不足焉，有不信焉 (*xìn bù zú yān, yǒu bù xìn yān* — "trust is not sufficient; there is distrust") close both **Ch 17** and **Ch 23**, verbatim. Our standing practice is that verbatim Chinese produces verbatim English — 物壯則老 in Ch 30 and 55 was resolved exactly that way. Here we depart, because **the two chapters put the line in different mouths.**

**Ch 17 is a chapter about rulers** — 太上 (*tài shàng* — the highest), 其次 (*qí cì* — the next), the descending grades of governance, and 功成事遂，百姓皆謂我自然 ("the work done, the people all say they did it themselves"). Supplying *leaders* and *the people* as the missing subjects is not an import there; it is the chapter's own subject, restored. It stays: *"When leaders don't trust the people, no one trusts the leaders."*

**Ch 23 is not about rulers at all.** It is about 同 (*tóng* — merging): aligning with the Tao, with integrity, or with loss, and receiving in kind. Naming leaders and subjects there would install a political frame the chapter never sets up, and would narrow a line the chapter uses generally. So Ch 23 keeps the subject unsupplied and the reciprocity bare: **"Where trust is withheld, trust is withheld in return."** The repetition in the English carries what 不足/不信 does in the Chinese — the same thing returning, unchanged, to whoever sent it.

**What the correction was.** The line previously read *"When integrity is weak, the system winds down,"* which was wrong twice. **信 is not 德.** 信 is 人 (*rén* — a person) beside 言 (*yán* — speech): a person standing by their word, *trust*. Rendering it "integrity" borrows 德's locked word for a different character — and does so three lines after the chapter has used 德 explicitly (德者同於德), collapsing a deliberate change of subject. And **"the system winds down" is not in the text**: 有不信焉 is "there is distrust," a closed loop, where "winds down" is entropy — something losing energy on its own rather than receiving what it gave.

**Cost, on the record:** a reader comparing the two chapters will find one Chinese line and two English ones. We are betting that the gain in each chapter's own voice outweighs the loss of the echo between them. The editing pass should test that bet with all 81 chapters in view.

### Ch 25

#### 域中有四大 → "Within the realm there are four vast things"

*(was: "Within this system of four vast things")*

**域** (*yù*) is a **bounded stretch of ground** — 土 (*tǔ* — earth) beside 或, an enclosed area held under guard; it is the root of 區域 (*qūyù* — region) and 領域 (*lǐngyù* — domain). It occurs **exactly once in all 81 chapters**, here, so there is no consistency question — only what the word does in this line.

"System" was wrong in a specific way, not merely in register: **a system is a set of relations, where 域 is an extent of ground.** The line is spatial, and that spatiality is the point of what follows — 人法地，地法天，天法道 (humans follow earth, earth follows sky, sky follows the Tao). **A ladder needs somewhere to stand.** "System" turned a stack of places into a diagram.

Two smaller repairs in the same line. The Chinese has **no demonstrative** — 域中 is simply *within the bounds*, and "this system of four vast things" implied the four *constitute* the realm, where 域 is the container they sit inside. And 居其一 is given as "is one of them"; 居 (*jū*) is properly *to dwell, to occupy a position*, so "occupies one place among them" is closer, but it reads worse and loses little.

#### 王 → "the aligned human"

*(the deliberate removal of the throne, and of the gender)* ⟡ *research lead, to develop*

Where the received text has 王 (*wáng* — king), we render **the aligned human**. This was chosen on the edition's own grounds — standing rule 2, *universality over the incidental male-default* — and it deserves stating plainly rather than passing unremarked, because a reader will want to see it was chosen.

**The manuscript evidence independently supports it, and this was found only afterward.** Both Mawangdui silks read **人** (*rén* — human) in the list of four greats, and the older silk reads 人 in both places, with no king anywhere in the passage. So the rendering does not remove a king Laozi installed; it restores the reading the oldest witnesses carry. Full apparatus in the Manuscript Notes.

**Three further supports, for the fuller treatment this deserves:**

- **The received text argues against itself.** Wang Bi's very next line is 人法地 — *humans* follow earth. A text that makes the king one of the four greats and humans the bottom rung in consecutive lines has a seam in it.
- **王 is not grammatically gendered, and may not even be personal.** Classical Chinese marks no gender on the word; the maleness is cultural default, not lexical — exactly the collision standing rule 2 exists for. And the graph is read two ways: as an axe-head (the emblem of authority), or as three horizontal strokes — sky, human, earth — joined by one vertical: **the one who connects the three realms.** Under the second reading 王 names a *function*, not a person or a sex. The *Shuowen Jiezi* (~100 CE) glosses it 天下所歸往, "that to which the world turns."
- **This edition already de-thrones 王 elsewhere.** Ch 16's ladder renders 公乃王 as *"Impartiality leads to sovereignty"* — an abstraction, not a monarch. Ch 25 is now consistent with that.

*Cost, on the record:* **"aligned" is supplied.** 人 is simply *human*; nothing in the line says *aligned*. It is doing the work of explaining why this human is 大 (*dà* — vast) — namely that they model earth, sky, and the Tao in the lines that follow. Defensible as a gloss made visible, but it is ours, not the text's.

**To develop.** Shalom flags this as possibly worth a chapter of its own. The thread runs wider than Ch 25 — see the Reading Notes thread on reading past the throne, and `DISCOVERIES.md` §1 and §3.

### Ch 29

#### 天下神器 → "the world is a sacred vessel"

*(was: "a sacred system")*

**器** (*qì*) is a **vessel**, and it is already locked that way inside `glossary/pu-樸.md` (`covers: 器 → vessel / tool`). It holds everywhere else in the book: Ch 11's clay worked into 器, Ch 28's 樸散則為器 ("when the uncarved wood is carved, it is made into tools"), Ch 31's 不祥之器 (weapons, "instruments of ill omen"), Ch 36's 國之利器 ("the sharp instruments of the state"). Ch 29 was the sole outlier, and "system" was the mechanistic overlay this edition exists to strip.

**The vessel is also what makes the rest of the chapter work.** The next clause is 不可**執**也 — "it cannot be **grasped**" — and then 執者失之, "those who grasp it lose it." You grasp at a vessel and break it. You do not grasp a system. The image and the warning are one gesture, and "system" severed them. *(This was already right in the notes: the Ch 48 entry cites Ch 29's 神器 as "a sacred vessel" — the reasoning was settled and only the verse had drifted. Found by `tools/check_locks.py`.)*

**執 was also rendered two ways, two lines apart** — "controlled," then "grasp." The Chinese is a tight chiasmus, 不可為也，不可執也 · 為者敗之，執者失之, and it only lands if 為 and 執 each keep one English word. Now: *"It cannot be forced. It cannot be grasped. / Those who force it ruin it. Those who grasp it lose it."* Four beats for four. "Controlled" also lost the hand — 執 is a graph of a hand seizing.

**And "try to" is gone from 為者/執者.** The Chinese says *those who do it*, not *those who attempt it*. The attempt is not the failure; the doing is.

*Left alone: the em-dash in this chapter's first line is one of the defensible ones — both clauses carry named subjects ("Those who wish…" / "I see…"), so it strands nothing. Noted so a later em-dash sweep does not remove it reflexively.*

*Still open here, not fixed: 取 (qǔ — seize) has vanished from 將欲取天下而為之, where "force their will upon the world" merges 取 and 為 into a single gesture. The Ch 48 entry makes much of 取's severed-ear violence, so 取天下 across Ch 29 / 48 / 57 may want one consistent treatment.*

### Ch 40

#### 弱者道之用 → "Yielding is the Tao's use"

*(was: "the Tao's function")*

"Function" was the mechanistic overlay twice over: **用** (*yòng*) is locked to **use** inside `glossary/wu-you-無有.md` (`covers: 用 → use`), and "function as" is on 為's forbidden list. **"Use" is simply the lock applied.**

It also repairs the couplet. Ch 40 is the shortest chapter in the book and is built entirely of parallels: 反者道之**動** / 弱者道之**用** — returning is the Tao's **動** (*dòng* — movement), yielding is its **用**. 動 and 用 are a matched pair, *how it moves* and *how it works*. "Movement" is concrete and observable where "function" is abstract and mechanical, and the mismatch broke the one structure the chapter has.

**And it restores a link to Ch 11**, which renders 有器之用 and 有室之用 as *"A clay vessel becomes useful"* and *"A room becomes useful."* Both chapters make one argument: **usefulness comes from what is hollow or yields.** Rendering 用 as "function" here and "useful" there hid it.

*A note on the genitive, which is deliberately left double.* "The Tao's use" can be read as *how the Tao operates* or as *how the Tao is put to use*. 道之用 carries both and classical Chinese does not disambiguate, so the English should not either. (Rejected: "working" — accurate to 用's sense of efficacy, but in modern ears it reads as employment, a job of work.)

### Ch 48

#### 取天下 → "the world comes to you"

*(not "win" or "take the world")*

The literal 取 is *seize / take* — its graph is a hand (又) gripping an ear (耳), the severed left ear of a slain enemy, counted on the battlefield for reward. It is the most grasping word in the language. But Laozi *subverts* it: the world is a 神器, a sacred vessel that 不可執 — "cannot be grasped" — and 執者失之, "whoever grasps it loses it" (Ch 29). The conqueror's verb names precisely the thing that fails.

- We rejected **"win"** because it imports *competition and victory*, the very thing Laozi renounces (不爭, non-contention). "Win the world" sounds hard-fought; the teaching is that you come to it by *not* fighting for it.
- We chose the receptive reframe — **"the world comes to you"** — because it says aloud what 取天下 only implies: the non-grasping ruler is one the world *gravitates toward* (cf. 天下往, "the world goes to him," Ch 35; 天下樂推, "the world delights to carry him forward," Ch 66), not one who seizes it.
- The failure-clause 及其有事 (literally "once there are affairs / once one meddles") we render **"the moment you grab at it, it slips away,"** letting "grab" carry the 取/執 grasping-image and echo 執者失之.

Net: fidelity to the *word* traded for fidelity to the *teaching*. A conscious choice, logged here.

### Ch 52

#### 其母 / 天下母 → "our mother"

*(not "the mother")*

The Chinese is 其母, "its mother," and 天下母, "the mother of the world" — *the*, not *our*. We add the possessive on purpose, and its warrant is already in the text: the mother of *all-under-heaven* is the mother of *us*, and of everything — so "our" invents no relationship, it only draws out the one Laozi states. It also turns her children (其子) into our *siblings*: we and the rivers and the stars, all born of one mother — as Taoist a thought as the book holds.

But the possessive is held under one strict condition, the same the 母 entry draws: **"our" means *belonging*, never *possession*.** The cosmic mother is fierce, not fond (天地不仁, 5); she bears all and clings to none, and favors no one. She is "ours" only the way the sky is ours — everyone's, possessed by none. Read as *the mother of us all*, "our mother" may be the truest word in the chapter; let it drift toward *our own dear mom* and it betrays her. The warmth is earned only while it stays inclusive.

A note on placement: in Chapter 52 we keep line 1's cosmic naming — "the mother of the world" (天下母) — and turn to "our mother" only from line 2 (其母), as the movement goes inward, toward return and homecoming. Awe first, then intimacy: she is named as the mother of *everything* before she is held as the mother of *us*.

### Ch 53

#### 是謂 → "This exposes…"

*(not "This is called…")*

The formula 是謂 X means "this is called X" — a *naming*. In this one line (是謂盜竽) we render it "**exposes**": *"This exposes the ringleader of thieves."* The departure is deliberate, and it buys two things.

*Grammar.* The literal "This is the ringleader of thieves" welds a *scene* (the immaculate court, the silk, the gorging) to a *person* (the ringleader) with a bare "is," and the seam shows — a tableau is not a man. "Exposes" is a verb a scene can rightly do to a person: it reveals, unmasks, lays him bare.

*Force.* It draws out what the naming *does* here. All the ruler's splendor poses as legitimate majesty; to *name* it "the ringleader of thieves" is to strip that majesty off and show the criminal beneath. "Exposes" turns the whole description into an unmasking — the robes torn away to reveal the thief.

It is not literal (是謂 is "is called," not "exposes") — but to name a robed ruler the chief of thieves *is* to expose him; we let the English verb do what the Chinese naming does in force. A small liberty that repairs a real referential seam, and turns splendor into disguise.

### Ch 55

#### 全作 → "its whole being quickens with life"

*(setting aside the traditional male-erection gloss)*

The line proves the newborn's intact vitality: 未知牝牡之合而全作，精之至也 — *not yet knowing the union of female and male, yet [it] stirs — vital essence at its utmost.* The traditional reading is the male infant's reflex erection (explicit in the older 朘 variant; see Manuscript Notes). We read our base text's 全 ("whole") in its plain sense — *the whole being quickens with life* — a defensible **minority** reading, chosen deliberately so the emblem holds for infants of every gender. Nothing essential is lost: the desirelessness (*not yet knowing… yet*), the spontaneity (*with life, of itself*), and 精之至 (vital essence at its fullest) all remain — arguably *deepened*, since it is now the whole infant alive with undesiring vitality, not one organ. Faithful to the point; universal in the image. *(Governing principle: Process guide §0, "universality over the incidental male-default.")*

### Ch 57

#### 取天下 → "win the world through non-interference"

*(the Ch 48 rule, second instance)*

The phrase returns from 48. There, 取天下常以無事 taught that the world is won only through non-doing, and we rendered 取天下 not as "take" or "seize" but as the world *coming to you* — 取 as reception, not conquest. Here the same lesson is compressed into a single clause: 以無事取天下. The draft reached for "master the world," but 無事 and "master" cancel each other — the line's whole claim is that you gain the world by *not* mastering it. So we hold the 48 reading: "win the world through non-interference," the world gained by the open hand. 取 is what falls to you when you stop grabbing for it — in 57 as in 48. (One consistency note travels with it: 無事 stays **non-interference** in both of its appearances here — 以無事取天下 and 我無事而民自富 — and stays distinct from 無為, *non-doing*, which the same stanza uses separately. See the open seam under Ch 63 · 事無事.)

### Ch 61

#### 為下 → "is underneath" / "ought to be underneath"

*(not "takes the lower position")*

為下 (*wéi xià* — "be the low one") occurs exactly twice in the chapter: once of the female animal (以靜**為下**) and once in the closing line (大者宜**為下**). Nothing else in the chapter uses that construction; the middle lines use 以下 and bare 下. So the two are a clasp, binding the barnyard to the statecraft, and **they must read identically in English** or the chapter stops being one thought.

We render both **"underneath."** The safe alternative, "takes the lower position," is bureaucratic and holds only one of the three things 下 is doing here. 下 runs nine times through nine lines — in 下流 (*xià liú* — downstream), twice inside 天下 (*tiān xià* — "under-sky," the world), in 以下 / 下以 / 下而, and in the two 為下 — and it means, simultaneously, *downstream*, *humbled*, and *underneath in mating*. The chapter's argument runs on that convergence. "Underneath" is the only plain English that holds all three, and it lets the final line land as hard as the Chinese does: the great power's proper posture is the cow's posture. That discomfort is the chapter.

#### 或下以取，或下而取 → "the large state takes by going low, the small state by staying low"

A recap line (故 — *gù*, "so"), seven characters against the fourteen-character couplet it summarizes. The only difference between its halves is a particle: 下**以**取 (以 marks purpose — lowers *in order to* take) against 下**而**取 (而 marks mere sequence — lowers, *and* takes). We do not build on that contrast. Heshang Gong reads the line as a plain restatement of the two cases and does not treat 以/而 as semantic, so the distinction may be rhythmic; and an English recap that reproduces the couplet with a hairline change reads as repetition, not summary.

What we render instead is the asymmetry that is certainly present and that the final line acts on: **who has to move.** Both parties go low, but only the large one has anywhere to come down from. "Going / staying" carries that in one aspectual pair while keeping the single lexical item "low" in both halves, mirroring the single 下 the Chinese repeats. An earlier draft used "stooping" for the large state; it was dropped because English *stoop* carries condescension (*stoop to conquer*) that 下 does not, and disdain for lowness is precisely the hierarchy this chapter inverts. **Cost, on the record:** the Chinese puts the difference in grammar and we have put it in vocabulary, and the non-purposive force of 而 is not carried.

#### 牝 stays an animal

牝 (*pìn*) is 牛 (*niú* — cattle) plus a phonetic: the female of a domestic animal, with a secondary sense of the genitals. Its partner 牡 (*mǔ* — the male animal) is 牛 with a component that in the oracle bones draws a penis, later regularized to 土 (*tǔ* — earth). The book's only other use of the pair, Ch 55's 未知牝牡之合 ("not yet knowing the joining of female and male"), is unambiguously about mating. So we render "the female" and "the male," and we keep *she*. **Not "the receptive female"** — 受 or any word for receptivity is simply not in the line, and the adjective tells the reader how to feel about the animal so that they never have to meet her. What "the female" still drops is that this is a stockbreeder's word; the glossary carries that, on the same principle as 心 (*xīn* — heart) and 物 (*wù* — things).

#### 取 stays "take," distinct from 勝

The chapter switches verbs deliberately: 勝 (*shèng* — overcome) appears once, and only of the animal; 取 (*qǔ* — take) appears four times, and only of the states. Rendering both "overcome" collapses the analogy into an identity. 取 is also the richer word — the graph is 又 (*yòu* — a hand) seizing 耳 (*ěr* — an ear), the tally taken from the fallen, and it is the original form of 娶 (*qǔ* — to take a wife). A war-trophy word and a marriage word, in a chapter arguing that you acquire by lying down. We let the double stand.

### Ch 62

#### 奧 → "the sanctuary"

*(never "mystery." Revised 2026-08-11; "the sheltered corner" was the first rendering and is retired.)*

道者萬物之奧. The source gloss offered *"the profound mystery/sanctuary of the ten thousand things"*, and *mystery* is the overlay. 奧 (*ào*) is a **place in a house**: the southwest corner of a dwelling, away from the door, dark — where the household shrine stood and the honored guest was seated. Concrete enough to point at, which is the test.

Both commentators gloss it as a place, and they diverge on which property matters:

- **河上公:** 奧，藏也。道為萬物之藏，無所不容也 — *"奧 is a storehouse. The Tao is the storehouse of the countless things; there is nothing it does not hold."* → **containment**.
- **王弼:** 奧猶曖也，可得庇䕃之辭 — *"奧 is like 曖 (ài — dim, shaded); it is a word for what one can get shelter under."* → **shade**.

We follow Wang Bi, because the two clauses that immediately follow are both about people taking refuge (寶 / 保). **The first rendering was "the sheltered corner."** It was accurate and it was opaque: a modern reader has no way to know why a corner of a house should matter, and the line's whole job is to say what the Tao *is* to everything.

**Why "sanctuary" — a word this note originally forbade.** Shalom challenged the rejection, and the challenge was right. "Sanctuary" was ruled out by reflex as an imported church, but the 奧 corner **was** the household's altar space: the seat of the presiding domestic spirit and the place of honour for the head of the family. *Analects* 3.13 turns on exactly that — 與其媚於**奧**，寧媚於灶, *"rather than court the 奧 [the spirit of the house's honoured corner], court the 灶 (zào — the stove god)."* Rendering a cult site as a cult site is translation, not overlay.

**And the decisive argument is one neither of us had going in.** English *sanctuary* carries two live senses: a holy place, **and the right of a fugitive to take refuge and not be seized.** The chapter's closing line is 求以得，有罪以免 — *"seek, and you find; have a crime against you, and you are spared"* — and Heshang Gong glosses it with no piety whatever: 遭亂世闇君，妄行刑誅，修道則可以解死, *"to meet a chaotic age and a benighted ruler, where punishments and executions fall at random; cultivating the Tao, one can be released from death."* **The chapter ends on the legal sense of the word.** *Sanctuary* does not import a church here; it anticipates the ending, and it primes 寶 / 保 (treasure / safekeeping) two lines earlier.

**The cost, named.** In English a sanctuary is somewhere you *go* — a building, a destination. The 奧 is where you already are: the part of the single room you live in that is furthest from the door. That domesticity matters in a book whose Ch 47 reads *"Without leaving home, you know the whole world."* The corner is therefore moved into the reader-facing note rather than dropped. And nothing is borrowed from the locks: 玄 (*xuán*) keeps *dark*, 妙 (*miào*) keeps *subtle* — 奧 takes neither.

#### 奧 — answering the 注 / 主 variant

*(added 2026-08-11)*

Both Mawangdui silks read **注** (*zhù*) where our base reads 奧. The standard modern critical edition, Gao Ming's *帛書老子校注*, takes 注 as a loan for **主** (*zhǔ* — master), yielding *"the Tao is the master of the countless things"* — and supports it from Zheng Xuan on the *Liji · Liyun* (奧猶主也, *"奧 is like 主"*) and from the *Zuozhuan*'s 國有奧主. That is a serious reading and it deserves to be answered rather than ignored.

**We answer it from Chapter 34, which denies it twice in the same two words:**

> 衣養**萬物**而不為**主** — *"it clothes and feeds the countless things, yet does not act as their master."*
> **萬物**歸焉而不為**主** — *"the countless things return to it, yet it does not act as their master."*

A Ch 62 reading 道者萬物之主 would set the book against itself on 萬物 and 主 — the identical pair, one chapter apart, asserted here and denied there. And nothing forces us to pay that: **注 at face value is 氵 (water) beside 主 — to pour into.** Read plainly, the silks say *what the countless things pour into*, which is a **confluence**, arriving one chapter after Ch 61's 大國者下流 (*the downstream flow*) and 天下之交 (*the confluence of the world*), and answering Ch 32's 猶川谷之於江海.

**And Gao Ming's own chain runs through a room.** 奧 can mean *master* only because the 奧 corner is where the household head presides — the *Shuowen* defines it flatly as 宛也，室之西南隅, *"the winding place; the southwest corner of a room."* The corner is prior; the mastery is derived from it. **So every witness here keeps the place, and only the dominion is optional — and Ch 34 forbids the dominion.** "The sanctuary" holds exactly what 奧 and 注 share and declines exactly what the book denies elsewhere.

#### 善 / 不善 → "masterful" / "unmasterful"

*(not "good" / "bad")*

The single decision that keeps this chapter out of the sermon. 善人 and 不善人 slide easily into *good person* and *bad person*; three lines later stands 有罪以免, and 罪 (*zuì*) is **crime**, not sin. Put those two renderings together and Ch 62 reads as a doctrine of grace, with 奧 supplying the sanctuary to receive it — a gospel assembled out of three separate slips, none of which the Chinese makes.

Held as **masterful / unmasterful** (following Ch 27, which renders 善 the same way), the chapter argues about **competence** instead: the Tao is the treasure of those who are adept and the safekeeping of those who are not, so why abandon anyone? Ch 62's 何棄之有 and Ch 27's 無棄人 are the same claim, and they should sound like it.

Heshang Gong confirms the register from the other end. His gloss on 有罪 is not moral at all — 遭亂世闇君，妄行刑誅，修道則可以解死 — *"to meet a chaotic age and a benighted ruler, where punishments and executions are inflicted at random; cultivating the Tao, one can be released from death."* Literal criminal jeopardy under an arbitrary state. Nobody is being absolved of anything.

#### 寶 / 保 — a sound-pair, and possibly a later one

*(corrected 2026-08-11)*

善人之**寶**，不善人之所**保** — both are *bǎo*. 寶 is treasure; 保 is 人 (person) beside 子 (child) — to keep safe, to hold. Wang Bi separates them exactly: 寶以為用也 (*"treasure, because they put it to use"*) / 保以全也 (*"safekeeping, because it keeps them whole"*). We render **treasure** / **safekeeping**, which keeps the two senses and loses the chime.

**This note first called the pair an original feature of the line. The witnesses do not support that.** Both Mawangdui silks use **one graph in both positions**, and published transcriptions disagree about which — so the received text's two graphs may be a **later differentiation of a single word**, and what we are rendering as a pun may be a Han editor's clarification of something the older text left as plain repetition. We keep the base text and the two senses, which Wang Bi's gloss independently supports. But the claim that Laozi wrote a pun here is withdrawn. *(Apparatus in the Manuscript Notes.)*

#### 美言 — a tension with Ch 81 that we are not resolving

Ch 62 grants 美言 (*měi yán* — fine words) real purchase: they can be traded, and honored conduct can set a person apart. **Ch 81 flatly distrusts them:** 信言不美，美言不信 — *"trustworthy words are not beautiful; beautiful words are not trustworthy."* The commentators split on the tone here too: Heshang Gong reads the line as a put-down (美言者獨可於市耳 — *"fine words are good for the marketplace, and that is all"*; 未足以尊道 — *"not enough to honor the Tao"*), while Wang Bi reads it as praise of the Tao, whose good report 奪衆貨之賈, *"outbids the price of every other good."*

We render it **positively and plainly**, because the line that follows depends on it: fine words and honored conduct work even on the inept, therefore no one is beyond reach, therefore 何棄之有 — why abandon them? Under Heshang Gong's dismissal that sentence does not follow from anything. But the tension with Ch 81 is genuine and stays open; it is not to be smoothed when Ch 81 is drafted.

*(The punctuation fork in this line — both commentators and both silks split after 市 and read 尊行 — is in the Manuscript Notes.)*

#### 何棄之有 → "why abandon them?"

*(was: "why would you throw them away?" — retired 2026-08-11, flagged by Shalom)*

Two faults in one clause, and the grammar is the first.

**何 … 之有 is a fixed classical idiom, and it is impersonal.** Literally *"what ___ is there?"* — the same construction as the *Analects*' 何陋之有 (*hé lòu zhī yǒu* — *"what meanness is there in it?"*), where 之 (*zhī*) fronts the object before the verb. Its force is an **emphatic denial in the shape of a question**: *there is no such thing.* The earlier rendering supplied a **"you"** the Chinese does not have, converting a statement about how things stand into a reproach aimed at the reader.

**And 棄 is graver than "throw away".** The graph is three elements: an **infant drawn upside-down** (head-first, as at birth), a pair of **hands**, and a **winnowing basket** — two hands lifting a basket with a newborn in it. The word is *infant exposure*. It was not a dead metaphor: the Zhou agricultural ancestor Hou Ji was **named** 棄, *Abandoned*, from the story that his mother left him at birth and he survived. Heshang Gong uses it as a social category — 無有**棄民**, *"there were no abandoned people"* — and Wang Bi glosses the line with 放 (*fàng* — **banishment**), the formal penalty of expulsion.

So the register is exposure, banishment, a person put outside where they cannot live. **"Throw away" is the wrong size**: in modern English it means trash, which sounds harsher and lands lighter. **"Abandon"** is the ordinary English word for what the character depicts — *an abandoned child* is this picture exactly.

**Rejected as a trap:** *"what is there to abandon?"* is the most literal rendering of the idiom and the most misleading, because English hears it as *there is nothing in them worth keeping* — the reverse of the chapter's claim. *"How could they be abandoned?"* is closer to the idiom's flatness and was the runner-up; *"why abandon them?"* keeps the force and the mouth-feel.

**Retrofit owed:** Ch 27's 故無棄人 currently reads *"ensures that no one is lost."* Same character, same argument, and Ch 27 is now the softer of the two. See `RETROFIT.md`.

#### 立 → "raise up", to keep the 立 / 坐 axis

立 (*lì*) is a person standing on a ground-line — to stand a thing upright, and the ordinary verb for establishing a ruler. 坐 (*zuò*) is to sit. The chapter's two halves are 故**立**天子 and 不如**坐**進此道: they *stand a ruler up*, and the answer is to *sit down*. We render "raise up" rather than "enthrone" — which was the first draft, and which both flattens the verb and adds a throne the Chinese does not have, in a chapter about not adding thrones. **Stated honestly: 立 is idiomatic for enthroning and the contrast may not be deliberate.** But 坐進此道 *is* marked — "sitting and offering" is odd enough that Wang Bi glosses it out (不如坐而進此道) — so the axis is available in the Chinese, and keeping it costs the English nothing.

#### 天子 → "a child of the sky"

*(was: "Son of Heaven" — retired 2026-08-11, and with it the strain case that protected it)*

**The rendering "Son of Heaven" was the only "Heaven" in all 81 chapters.** Every other 天 (*tiān*) in this edition is *sky* or *nature*. One phrase in one chapter was carrying the entire theistic vocabulary of the English Tao Te Ching by itself, protected by a strain-case note arguing that the title should be kept "the way one keeps *Pope*." The analogy runs backwards: *Pope* is what Catholics actually call him, whereas **no Chinese speaker has ever said "Son of Heaven."** It is an English phrase about a Chinese title.

**The characters.** 天 is a picture of a standing person with the head marked — 大 (a human, arms out) under a stroke. *Shuowen Jiezi* (~100 CE): 天，顛也，至高無上，从一大 — *"天 is 顛 (diān — the crown of the head); the highest, with nothing above it; composed of 一 over 大."* The word is the top of a person, hence what is overhead, hence sky. No realm, no occupant. 子 is a **swaddled infant** — big head, arms, wrapped legs — and this book uses it that way in both places it matters: Ch 4's 吾不知誰之**子** (*"I do not know whose child it is"*) and Ch 52's 既得其母，以知其**子**, where 子 is fixed by direct opposition to 母 (mother), a lock. So 天子 is **the sky's child**.

**Where "Son of Heaven" comes from — two layers, both already named by this project.** The *Chinese* layer: 天子 is not an old neutral word for a ruler. Shang kings called themselves 王 and appealed to 帝 (*dì* — the high ancestral god); the Zhou, having conquered them, produced 天命 (*tiān mìng* — the sky's mandate) to explain why the Shang's own god had abandoned them, and 天子 is the title that doctrine minted. A legitimation device, made by the winners — the same move `DISCOVERIES.md` §1 catches in Ch 25, where our base text reads 王 (king) and both Mawangdui silks read 人 (human). The *English* layer: Legge and his contemporaries rendered 天 as "Heaven" throughout and 天子 as "Son of Heaven," in an English where *Son of ___* had one resonance. These are the translators who put 太初有道 at John 1:1. The phrase was built to sound like scripture.

**Checked, 2026-08-11 — and the silks have it.** When this decision was first made, `--witnesses 62` was blank and we declined to claim 天子 was an interpolation on the strength of not knowing. **The Mawangdui text carries 立天子.** So the title is Laozi's own and *not* an accretion of the Ch 25 kind. **The overlay was never in the Chinese. It was entirely in the English.** Nor should we have wanted it otherwise: Ch 62 names the apex of state ceremony — the enthronement, the three highest offices, jade borne ahead of four-horse teams — in order to knock it over with 不如坐進此道, *better to sit where you are*. Remove the grandeur and the argument goes with it. **We keep the title and change the English.**

**Why "child of the sky" is right, and the argument is internal.** In this book the sky is not the top of anything:

> 人法地，地法天，**天法道**，道法自然 (25)
> *the human follows earth, earth follows the sky, **the sky follows the Tao**, the Tao follows the self-so.*

And the Tao is 先天地生, *born before sky and earth*. **The sky is itself a child.** Ch 4 leaves the Tao's own parentage unknown and puts it before 帝; Ch 52 gives the world a mother. So within Laozi's own cosmology, 天子 is not a claim of divine descent — it is kinship with a junior member of the family, whose actual parent is the 母. **The title deflates on contact with Ch 25.** "Son of Heaven" prevents that; "a child of the sky" performs it. In a chapter whose whole argument is that this apparatus is worth less than sitting down, the smaller-sounding phrase is the more accurate one.

**Three locks recovered at once:** 天 keeps *sky*; the capital goes, per standing rule 5; and *Son* goes, which the graph never supported. **The seam, noted and not erased:** every historical 天子 was a man, and the title was male in every practical sense. 子 is not — it is an infant in swaddling. We render toward the universal, as at Ch 16's 公乃王 and Ch 55's 朘, and say so here.

**Cost, on the record:** we have traded office for image. 天子 was a piece of ordinary state vocabulary — as ordinary as *Prime Minister*, which is made of "first" and "servant" and which nobody hears — and the English now foregrounds a picture the Chinese kept in the background. Worth it in this chapter, whose business is shrinking the office. It would not be worth it in a chapter that needed the institution to sit there inertly. 天子 occurs nowhere else, so the trade is never retested. *(Fuller treatment in the Reading Notes; `DISCOVERIES.md` §3.)*

#### 三公 → "the three ministers"

*(not "the Three Dukes." Two entries on this were merged 2026-08-11.)*

公 (*gōng*) is 八 (*bā* — to divide; two strokes parting) over 厶 (*sī* — private, the self, the old form of 私). The word is **the dividing-up of what is private** — hence *public, common, impartial*; *Shuowen*: 公，平分也, *"公 is fair division."* This edition already renders it that way at Ch 16 (容乃**公**，**公**乃王 → *"Embracing all leads to impartiality. Impartiality leads to sovereignty."*).

As an office title 公 is conventionally *duke*, a borrowed European feudal rank we reject; *minister* says the same thing about an office of state without importing a peerage. Lowercase, per standing rule 5.

**The silks settle it in our favour:** where our base reads 三公 they write 三鄉, which editors read as a loan for 三**卿** (*sān qīng*) — the word that simply means *high minister*. Our "three ministers" turns out to be the oldest witness's own word.

It still drops the 公 etymology, and Ch 42's 王公 currently reads *"kings and lords."* Three chapters, three treatments. **公 wants a glossary entry**, and when it gets one, Ch 42 and Ch 62 will have to answer to Ch 16. Logged in `RETROFIT.md`.

#### 拱璧以先駟馬 → "jade discs too wide for one pair of arms, borne ahead of a team of four horses"

拱 (*gǒng*) is the gesture of both arms encircling — Wang Bi writes 拱抱寶璧, *"jade discs one embraces."* 璧 (*bì*) is the ring-shaped ceremonial jade. The jade travelling **in front of** the horses is the protocol of the highest state gift. The whole image exists to be set against 坐進此道 — 坐 (*zuò* — to sit). A procession, against sitting still. We keep both verbs concrete: *"better to sit where you are and offer this Tao."*

### Ch 63

#### 事無事 → "tend the not-tending"

The triple 為無為，事無事，味無味 is the line that forced the 無為 → *non-doing* lock (see `glossary/wuwei-無為.md`), because only a verb that also works as a noun survives all three members. The glossary entry illustrates 事 with *"attend the not-attending"*; we render **tend**. Same act, but *tend* keeps a hand in it and *attend* is a Latinate abstraction, and three plain monosyllables are what make the parallel audible.

*Open seam:* 無事 is rendered **"non-interference"** at Ch 48 and Ch 57, where it stands alone as a noun phrase. That does not chime with *tend* here. Both are defensible in place, but 事 has not been given a glossary entry and probably wants one; see `RETROFIT.md`.

#### 味無味 → "taste the flavorless"

*(not "taste the tasteless")*

Ch 35 already renders 淡乎其無味 as *"It is bland and flavorless"* — and the thing being described there is the **Tao**. Matching the word makes 味無味 legible as what it is: not a general counsel of blandness but an instruction to **taste the Tao**. Wang Bi reads it the same way — 以恬淡為味, *"takes the calm and bland as its flavor."*

#### 大小多少 → "Great or small, many or few" — a quantifier, not a maxim

Four bare characters — 大 (*dà* — great), 小 (*xiǎo* — small), 多 (*duō* — many), 少 (*shǎo* — few) — with no grammar between them. Three readings are genuinely available, and each classical commentator takes a different one:

- **王弼 (Wang Bi):** binds them to the clause that follows. His comment on the joint lemma 大小多少報怨以徳 is entirely about resentment — 小怨則不足以報，大怨則天下之所欲誅，順天下之所同者，德也, *"a small resentment is not worth repaying; a great resentment is what the whole world wishes to punish; to go along with what the world holds in common — that is integrity."* So: **great or small, many or few [resentments]**, repay resentment with integrity.
- **河上公 (Heshang Gong):** 欲大反小，欲多反少，自然之道也 — *"want the great, revert to the small; want the many, revert to the few — this is the way of the self-so."* So: shrink the large.
- **The common modern reading**, supported obliquely by Han Feizi's 敬細以遠大 (*"respect the minute in order to keep the great at a distance"*): magnify the small — *treat the small as great, the few as many*.

**We follow Wang Bi**, on three grounds. He is the commentator on our own base text. His is the only reading under which the eight characters of the line form one thought rather than two unrelated ones — which matters now that Mawangdui A confirms 報怨以德 belongs here (see the Manuscript Notes). And the scale-doctrine the other two readings extract is already stated outright two lines down, in 圖難於其易，為大於其細 — the chapter does not need 大小多少 to say it a second time.

**The cost, stated plainly:** a famous aphorism becomes a grammatical particle. We accept it. Where the chapter argues scale it argues it in full sentences; this line is about grievance.

#### 細 → "slight", never "small"

細 (*xì*) is 糸 (*mì* — silk thread) over 田 — **thread-fineness**, not size, and the distinction is the chapter's. Han Feizi's illustrations of 細 are all hairline things: a thousand-yard dike bursting through **an ant's hole** (螻蟻之穴), a hundred-foot house burning from **smoke in a crack** (突隙之煙), a disease caught at the 腠理 (*còu lǐ* — the pores of the skin). Those are not small. They are *thin*. 小 (*xiǎo*) keeps *small*; 細 takes **slight**. The two must not collapse into one English word, here or at Ch 67's 其細也夫.
