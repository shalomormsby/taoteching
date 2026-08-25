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
- **天 as a rung in the four-greats ladder** (25) → **sky**: *humans follow earth, earth follows sky, sky follows the Tao, the Tao models itself on being what it is*

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

### Ch 7

#### 非以其無私邪？故能成其私 → "Is it not because they have no private self? / And so their private self is fulfilled"

*(restored 2026-08-12. The second line had no English at all.)*

Block 2 has four Chinese lines, and the fourth had been replaced rather than translated. 故能**成其私** is *therefore they can **complete their own***; the verse read *"The sage simply does what needs to be done"*, in which no character of the Chinese survives — nothing there means *need*, *do*, or *done*. And the third line had lost its question: 非…邪 is an explicit rhetorical frame, *is it not because…?*, which exists to set up the fourth line as its answer. Flattened to *"Free of selfish desires,"* it became a description, and the answer had nothing to answer.

**私 is the hinge and it appears twice** — 無私 then 成其私, emptied then fulfilled. The graph is 禾 (*hé* — standing grain) beside 厶 (*sī* — a self-enclosing curl): **grain held back for yourself**, the harvest withheld. One English word has to carry both halves or the paradox does not close. We use **private self** in both, which is also the wording of the 公 entry, where 私 is the counter-term (`glossary/gong-公.md`).

**This is the chapter's third self-negation, not its first.** 後其身而**身先** and 外其身而**身存** run the same move on 身 (*shēn* — a picture of a pregnant body, the physical person). So the stanza is three paradoxes in a row, and the last was missing.

**In the same pass: 身存 → "their selves endure"** *(was "their spirits endure")*. 身 is the body, and it is the same character rendered *themselves* one line above; *spirit* is the opposite register and it broke the 身 / 身 / 身 chain the couplet runs on.

### Ch 31

#### 吉事尚左，凶事尚右 → "Auspicious occasions honor the left; inauspicious occasions honor the right"

*(2026-08-12. Was: "Life-generating processes amplify creative energy. Life-negating processes invoke destruction.")*

**Four inventions in three lines.** *Processes* is the mechanistic overlay, and it turns a room of people observing a protocol into physics. 尚 (*shàng*) means only *to esteem, to place above* — nothing in the line says *amplify* or *invoke*. And the next line's *"the place of creation"* / *"the place of destruction"* are supplied outright: 偏將軍居左，上將軍居右 is simply *the secondary general stands left, the highest general stands right*.

Those glosses also buried the point. 吉事 and 凶事 are the Zhou ritual categories — 吉禮 (auspicious rites) and 凶禮 (rites of mourning) — and the chapter's shock is that **the more senior your command, the more you are seated as a mourner.** The text says so itself in the line that follows, 言以喪禮處之, *that is to say, they are placed by the rites of mourning*, which needed no help from us.

*(With this repaired, `"processes"` was added to 事's `forbidden:` list; see `glossary/shi-事.md`.)*

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

**And the word is load-bearing elsewhere.** 然 is the second half of **自然** (*zìrán* — so of itself): 自 (*zì* — self) + 然 (*rán* — so). The character that closes these three questions is the one Laozi builds his term for *being as one is, of oneself* out of. So the question "how do I know it is **so**?" is asked in the vocabulary of self-so-ness, and answered 以此 — *by this, here, now*: by the thing in front of you, being what it is of its own accord. *(See `glossary/ziran-自然.md` for 然's history — it began as a picture of roasting and was borrowed for its sound, so it is grammar rather than image.)*

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

*(revised 2026-08-20 — three decisions in one pass, each of which uncovered the next. The passage remains open pending Guodian; see the note at the foot.)*

#### 天下母 → "the mother of the world"

*(was: "the mother of creation")*

可以為天下母. **天下** (*tiān xià* — under-sky) is locked to **the world**, and the previous rendering deleted the locked term in favour of **creation** — a word `glossary/tiandi-天地.md` sets aside outright: *it implies a creator, and this cosmos was borne, not made.* In a chapter whose opening line is 先天地生 (*born before sky and earth*), installing a creation is the precise overlay the 天-family policy exists to prevent.

Now consistent with Ch 52, which renders 以為天下母 as *"which serves as the mother of the world."*

**Worth recording as a checker gap, not just a fix.** `check_locks.py` keys off the Chinese to judge the English, so it fires when a *wrong* word is present. It cannot fire on a **locked word that is absent** — a rendering that simply deletes 天下 passes every rule silently. Same class of blind spot as the empty `## Translation` blocks found in Ch 20 and Ch 65: the tools cannot see what is not there. A candidate rule for `PLAN.md`.

#### 人 → "humans are also vast" / "one of them is human"

*(was: "the aligned human," in both lines. Supersedes the entry written when the throne was first removed.)*

**⚠ The manuscript grounds collapsed the same day this entry was written, and the reading survives on other grounds.** It is not true that the silks read 人. **Every excavated witness reads 王** (*wáng* — king) — Guodian (~300 BCE), both Mawangdui silks, the Beida Han slips. 人 is a *transmitted* reading: 傅奕 (Tang) for the first line, 范應元 (Song) for the second. We follow it because **the received text contradicts itself** — the next line is 人法地, "humans follow earth" — an internal argument Fan Yingyuan and 奚侗 both made long before the excavations, and one the excavations do not touch. Full apparatus, and the honest account of how the error entered, in the Manuscript Notes.

**This does not disturb the English.** 王 is not gendered in Chinese and `glossary/wang-王.md` renders it *ruler / sovereign* in all eight chapters, never *king*. Even reading 王 here, the line would not have produced a throne.

**What changed: "aligned" is gone.** Nothing in the Chinese licenses it. 人 is simply *human*, and the qualifier was deciding **which** humans are among the four vast things — doing in miniature what the throne did in full. It was ours, not the text's, and it has been deleted.

**Then the real difficulty surfaced, and it is not solvable by word choice.** Three of the four items are **definite singular uniques** — there is one Tao, one sky, one earth. The fourth is a **class term**. English "the human" tries to make it a unique too and lands in taxonomic register (*the human, the domestic cat*): a specimen, not us. "Humans are one of them" fails the other way, on number agreement.

**The asymmetry is in the Chinese and cannot be dissolved, so it should not be disguised.** 人 is deliberately the odd item — the one category in the list that contains the reader.

The solution is to change grammatical strategy between the two lines. The list line takes the natural English **plural** (*humans are also vast*); the count line makes 人 a **predicate** rather than a counted item (*one of them is human*), so nothing has to agree in number. It also puts **human** in final stressed position — the slot the received text gave the king, and the last word before the ladder begins.

This also settles the passage internally: the ladder three lines down already reads *"Humans model themselves on the earth"* (人法地), which is the very line the received text contradicts. Nothing in the passage now argues with it.

**Cost, on the record: 居 flattens to "is."** 居 (*jū*) is properly *to dwell, to occupy a position*. Both commentaries read it here as rank rather than residence — Wang Bi glosses 而王居其一焉 as 處人主之大也 (*"occupies* [處 *chǔ*] *the greatness of the lord of people"*), and Heshang Gong's edition carries the note 居一作處, *"居 is written 處 in one edition."* A verb of position, close to a copula. The loss is small and the gain in the line is large.

**而 is kept as "and."** A draft dropped it for compression; Shalom restored it. It is in the Chinese — 而人居其一焉.

**Correction to the earlier version of this entry**, which offered the three-strokes reading of 王 (sky, human, earth joined by one vertical) as a co-equal etymology. It is not one. That reading is **董仲舒** (*Dǒng Zhòngshū*, c. 179–104 BCE), roughly fourteen centuries younger than the graph, and it entered the dictionaries through the *Shuowen*. The graph is an axe. See `glossary/wang-王.md` and `DISCOVERIES.md` §4.

#### 域中 → "Within all bounds"

*(was: "Within the realm"; before that, "Within this system of four vast things")*

**域** (*yù*) is a **bounded stretch of ground**. The older graph underneath it is 或 (*huò*) — a dagger-axe 戈 (*gē*) standing over a walled enclosure 囗 (*wéi*) on a line — and the *Shuowen Jiezi* reads it 或，邦也。从口从戈以守一。一，地也 (*"或 is a state; 囗 and 戈, guarding 一; 一 is the ground"*). 或 was then borrowed for its sound to mean *or*, and the territorial sense was rebuilt twice: **域** with soil under it, **國** (*guó*) with a wall around it. 域 occurs **exactly once in all 81 chapters**, here.

That fact resolves the witness fork rather than deepening it. **Both silks read 國中有四大** where the base reads 域中. These are not two words but **one root with two classifiers**, which is why `sources/variants.yaml` logs the fork as non-meaning-bearing. Whichever is written, the word means *bounded territory*.

**Why "realm" had to go, and it is our own besetting error.** A realm is **what a king rules**. Having taken 王 out of the line, the container word put the throne back one word to the left — in the English only, with nothing in the Chinese asking for it. That is `DISCOVERIES.md` §4's third installation, committed by us, in the same sentence from which we had just removed the fourth.

**Why Laozi could not have used 天下 here, and why the choice looks deliberate.** 天下 means *under-sky*: it is defined by lying beneath 天. This sentence **counts 天 as one of the four vast things**, and it must also hold the Tao, which the same chapter calls 先天地生 (*born before sky and earth*). A container named *the part underneath the sky* excludes two of the four items by construction. And the proof it is deliberate stands three lines earlier in this very chapter — 可以為天下母. He has 天下 in hand, uses it for what the Tao mothers, then **switches** the moment he needs a container wide enough to hold the sky. Two container words, one chapter, doing two jobs. That is about as strong an argument for intent as this text ever offers.

**The commentaries split here, and we follow Heshang Gong.** He reads 域 concretely — 八極之内有四大, *"within the eight extremities there are four vast things"*: a place, out to the horizon. **Wang Bi reads it as the un-nameable** — 無稱不可得而名曰域也…道天地王皆在乎無稱之内, *"what has no designation cannot be named; we call it 域. The Tao, sky, earth and the ruler are all inside the un-designated."*

**We reject Wang Bi's reading, on this chapter's own last line.** His gloss puts a container **around** the Tao — something the Tao is merely one item within. That is the identical inversion this edition refuses in 道法自然 (*dào fǎ zìrán*), where "the Tao follows Nature" installs a higher thing. He is solving a puzzle the chapter does not pose, and paying for it with the cosmology. He is also visibly uncomfortable, which is itself the tell: 國 is a *state* word, and the oldest witnesses put the four vast things inside a walled political territory. The territorial frame is older than the throne — a separate finding, and a live one.

**"Within the bounds of this world" — drafted and rejected the same day.** The demonstrative was reaching for something right: pointing is this book's own epistemic move, 以此 (*yǐ cǐ* — *by this*), the answer Chapters 21, 54 and 57 all give. But **"this world" in English carries a built-in opposite — the next one** (*not of this world*, John 18:36). 域 has an **edge, not an elsewhere**. And it collided: with 天下母 now correctly rendered *the world*, the word *world* would have done two different jobs eight words apart, erasing on the page the very distinction that justified the word choice. An earlier pass on this line had already recorded that 域中 carries **no demonstrative**.

**Cost, on the record:** *all bounds* is slightly strange English, and it drops the **ground** that 土 puts under 域. Accepted for now, and the frame may reopen.

#### Open — this passage is not settled

`sources/variants.yaml` records **Mawangdui only** for Chapter 25, and `concordance.py --witnesses 25` flags it: Guodian (~300 BCE, bundle A) **carries this chapter and has never been checked at the four greats.** `DISCOVERIES.md` §1 rests on the claim that the oldest witnesses read 人. Until Guodian is recorded, that claim is supported by the silks alone, and 域/國, 王/人, and the whole container frame stay open.


### Ch 27

#### 救 → "rescue", never "drawing in" — and the couplet's lost axis

*(2026-08-12, prompted by the Ch 62 retrofit. The line had read "masterful at drawing in people, ensures that no one is lost.")*

**The couplet had no axis.** 常善**救**人，故無**棄**人 turns on a pair of opposites: 救 (*jiù* — **rescue**) and 棄 (*qì* — **abandon**). The 故 (*gù* — "therefore") only does work because they pull against each other — *always masterful at rescuing, therefore no one is abandoned.* The English had paired *"drawing in"* with *"lost"*, which are not opposites and not even on one axis, so the "therefore" joined two unrelated observations.

**救 is not "drawing in."** The graph is 求 (*qiú* — to seek, to beg) beside 攴 (*pū* — a hand holding a stick, the action radical): intervening to pull someone out of trouble. Both commentators are explicit — Heshang Gong on 常善救物: 聖人所以教民順四時，以**救**萬物之殘傷, *"the sage teaches the people to follow the four seasons, in order to **rescue** the countless things from injury and mutilation"*; and on 常善救人: 欲以**救**人在命, *"wishing thereby to save people's lives."*

**"Rescue" and not "save," deliberately.** *Save* is the obvious English and it fails the hymn test outright — *"the sage is always good at saving people"* belongs in a sermon, and 救 has no soteriology in it. *Rescue* keeps the physical act. **This is also simply the house word already:** Ch 52 renders 終身不救 as *"your life is beyond saving"* — Ch 27 was the outlier, not the precedent. 救 also stands at Ch 67 (天將救之), still undrafted, which should follow.

#### 物 → "things", never "entities"

*"Entities"* occurred **exactly once in all 81 chapters of verse** — this line — and was tied to no locked term. 物 (*wù*) is a mottled ox: things, kinds, stuff. Heshang Gong's gloss settles the register: 聖人不賤石而貴玉，視之如一, *"the sage does not despise stone and prize jade; he sees them as one."* Stones and jade, not entities. The 萬物 lock forbids *"beings"* for the same reason — see `glossary/wanwu-萬物.md` — and *entities* is that abstraction in a lab coat.

#### 襲明 → "inherited clarity", not "innate clarity"

`glossary/ming-明.md` had already ruled this: 襲明 → **"inherited clarity."** The verse said *innate*, which claims the opposite about where it comes from — 襲 (*xí*) is to inherit, to receive in succession, to put on in layers. *Innate* says it was born in you; *inherited* says it was handed to you. The glossary decided; the verse had not been told.

#### 常 restored

常 (*cháng* — always) had been dropped from both halves. It is the word that makes this a standing disposition rather than an occasion, and it is why the sage's rescuing is the *reason* nobody ends up discarded.

**Retrofit closed.** This was the debt opened when Ch 62 settled 棄 → *abandon*; `RETROFIT.md` can drop it. The wider point is logged as a Thread in `notes/reading.md`: Wang Bi glosses this very line with 不造進向以殊**棄不肖** — *"does not create tracks of advancement that single out and discard **the unfit**"* — and 不肖 is Ch 62's 不善人.

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

### Ch 48

#### The closing stanza was drafted twice, and the superseded draft was kept

*(repaired 2026-08-12)*

Block 2 carries **two** lines of Chinese — 取天下常以無事 and 及其有事，不足以取天下 — and the English rendered them **four** times: the logged reading, then a second, more literal pass that had lost its subject (*"always won by non-interference."*) and used *"win the world,"* the exact word the 取天下 entry above argues against. The second stanza was dead draft. It is deleted, not repaired.

#### 取天下常以無事 → "The world always comes to you by not meddling with it"

The couplet is **framed and pivoted**, and the English had kept neither. 取天下 opens it and closes it; between those, one character flips — **無事 → 有事**, absence of undertaking to presence of it, built on the 無/有 pair this edition locks as *absence / presence*.

The old second line rendered 有事 as *"you grab at it."* Grabbing is 執 (*zhí*), a hand seizing — Chapter 29's word, and not in this chapter. **有事 is milder and more insidious: having a project.** Wang Bi glosses it 自已造也, *"manufactured by oneself"*; Heshang Gong, 好有事，則政教煩, *"fond of having undertakings, and governance turns troublesome."* Officiousness, not violence.

Now: *"The world always comes to you by not meddling with it. / The moment you meddle, it stops coming."* 常 (*cháng* — always) returns; 取天下 frames it twice as *comes to you* / *stops coming*, keeping the logged decision that 取 is reception and not conquest; and 無事/有事 becomes one English word negated and then affirmed, so the line turns on a hinge instead of drifting.

**Still open here:** 取天下 reads *"comes to you"* in this chapter and *"win the world"* in Ch 57, which the Ch 29 note already flagged as wanting one treatment across 29 / 48 / 57. Not addressed.

### Ch 57

#### 無事 → "I do not meddle"

*(was: "I practice non-interference")*

The line sits third in a quartet, and it was the only member that was not a plain saying:

> 我**無為**，而民自化 — *I do not do, and the people transform themselves*
> 我好靜，而民自正 — *I love stillness, and the people right themselves*
> 我**無事**，而民自富 — *I do not meddle, and the people enrich themselves*
> 我無欲，而民自樸 — *I am desireless, and the people become plain of themselves*

In the Chinese, 無為 and 無事 are visibly the same construction — the same negation over two different hands (`glossary/shi-事.md`). Four plain statements now, and the pairing is audible. The chapter's other 無事, 以無事取天下, follows: *"win the world by not meddling."*

### Ch 49

#### 善者，吾善之 → "The masterful, I count as masterful"

*(2026-08-14. Was: "The good, I am good to.")*

善 stands four times in two lines — twice for the kind of person, twice as a **verb**, *to reckon as 善*. Rendering it *good* made this a chapter about kindness to the wicked. It is not; it is a chapter about **refusing to grade people**, which is a stranger and better claim, and the same one Ch 27 (無棄人) and Ch 62 (何棄之有) make.

**Wang Bi decided it, by reading Ch 49 in Ch 27's own vocabulary.** On the couplet: 各**因**其**用**，則善不失也, *"go along with each according to their **use**, and then 善 is not lost."* On the tag 德善, three characters: **無棄人也**, *"there are no discarded people"* — Ch 27's own line. And at the chapter's close: 能者與之，**資**者取之, *"those with ability, go along with; those who are **raw material**, take them up"* — 資 being the exact character Ch 27 gives the unmasterful. Heshang Gong reads it morally instead (百姓雖有不善者，聖人化之使善也) and that stays on the record. Full argument in `glossary/shan-善.md`.

#### 德善 / 德信 → "Integrity is mastery" / "Integrity is trust"

*(was: "for integrity is good" / "for integrity is trustworthy")*

Two characters, no verb, and **no causal word** — no 故, no 因. The English had supplied a *because*, turning a bare tag into a moral premise. Removing it makes the stronger claim: **integrity is not the reason for the refusal to grade; integrity *is* the refusal to grade.**

*Rejected: reading 德 as its homophone 得 (dé — to obtain), giving "and so mastery is gained."* It is a common reading and Wang Bi's 無棄人也 fits it, but this edition locks 德 → integrity everywhere and a search-level consensus is not sufficient warrant to break a lock. **Shalom's call.**

#### 歙歙焉 → "breathes gently" · 渾其心 → "let their heart go muddy"

歙 (*xī*) is to draw in, to inhale. Wang Bi glosses 歙歙焉 as 心無所主也, *"the heart presides over nothing."* **"Breathes gently"** keeps the breath; what it lets go is the self-effacement Wang Bi hears. *(An edition fork, undecided: Heshang Gong's text reads 怵怵 — chù chù, wary — and the 釋文 records 惵惵.)*

渾 (*hún*) is to blend, to make turbid. The earlier *"merges their heart with the world"* had the sense and lost the water. **Muddy** chimes with Ch 15's 混兮其若濁, *"Mixed, like muddy water"* — where muddiness is the good state you sit still inside until it clears. Wang Bi: 意無所適莫也, *"the intention has no for and no against."*

#### 百姓皆注其耳目，聖人皆孩之 → "The people pour out their attention, all eyes and ears; / the sage sees them pure as infants"

**注** (*zhù*) is water pouring — the same character the Mawangdui silks put at the head of Ch 62. Both commentators gloss it as 用 (*yòng* — to use). English supplies the gift here: ***all eyes and ears*** is a live idiom for rapt attention **and is literally 耳目**, so the idiom carries the sense while the organs survive.

**孩** (*hái*) is not primarily *child*. The *Shuowen* defines its older form 咳 as 小兒笑也, **"a small child's laughing"** — the sense *child* came from the smile. And Ch 20 uses it that way: 如嬰兒之未**孩**, *"like an infant that has not yet smiled."* Those two are the only occurrences in the book, so Ch 20 is our dictionary for Ch 49. *(The Siku editors note the 釋文's claim that Wang Bi's text read 咳 here — the same word, the older graph.)*

**Why "sees them" and not "makes them."** 孩之 is grammatically causative, and Wang Bi reads it so (皆使和而無欲，如嬰兒也). But **the chapter's machinery is three acts of regard, not three interventions** — 吾善之 (*I count them masterful*), 吾信之 (*I trust them*), 孩之 (*the sage sees them as infants*). Rendering the last as something done *to* the people breaks that, in a chapter whose whole subject is not managing them. It leans to Heshang Gong's 愛念 (*cherishes, holds in mind*) over Wang Bi's causative, and *pure* is supplied — it does the work of telling a modern reader which property of infancy is meant, since English *infantile* runs the wrong way. **Both costs are Shalom's call, taken deliberately.**

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

We render it **positively and plainly**, because the line that follows depends on it: fine words and fine conduct work even on the inept, therefore no one is beyond reach, therefore 何棄之有 — why abandon them? Under Heshang Gong's dismissal that sentence does not follow from anything. But the tension with Ch 81 is genuine and stays open; it is not to be smoothed when Ch 81 is drafted.

*(The line also carries a textual fork — the silks and both commentaries divide it differently — resolved 2026-08-12 in favour of our base text. See the Manuscript Notes. The verse now reads "Fine words can buy honor. / Fine conduct can raise a person above others.")*

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
> *the human follows earth, earth follows the sky, **the sky follows the Tao**, the Tao models itself on being what it is.*

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

#### 事無事 → "serve the not-serving"

*(2026-08-12. Was "tend the not-tending," briefly; the glossary entry had illustrated it as "attend the not-attending.")*

The triple 為無為，事無事，味無味 is the line that forced the 無為 → *non-doing* lock (`glossary/wuwei-無為.md`). **Each beat is one character twice with 無 (*wú* — there is no) between them**, so the verb has to hold in two positions at once — as a verb, and as the thing that verb is done to. That constrains the middle beat in a way the other 無事 lines are not constrained, because at Ch 48 and Ch 57 無事 stands alone with nothing to rhyme against.

**The verb must also be neutral.** *Do* is neutral, *taste* is neutral, and the paradox lives in the negation. *Meddle* — the word chosen for 48 and 57 — fails twice here: you meddle *in* something, so the bare transitive is not English, and a verb that is already a rebuke flattens the line into a plain prohibition, which is the one thing it must not become.

**Serve** is 事's oldest verb sense and the one the graph draws — a hand holding the badge of office is a hand *in service*. It is also already this edition's word for 事 at Ch 59 (治人**事**天 → *governing people and serving nature*) and Ch 61 (入**事**人 → *enter and serve people*), so the middle beat now ties to the two chapters where 事 is unambiguously *serve*. And it is one syllable, which keeps the three beats even against *do* and *taste*.

*A loss the triple already accepts:* 味無味 reads **"taste the flavorless"** — two English words for one character — because *flavorless* buys the chime with Ch 35's 淡乎其無味, where the Tao itself is bland and flavorless. The internal echo is worth having and is not sacred.

*Why "tend" was retired within the day:* tending is what you do to a garden to make it grow, so *not tending* implies neglect that kills — the reverse of what these chapters claim, which is that things flourish once the hand comes off (民自富, *the people grow rich of themselves*). Caught by Shalom.

#### 味無味 → "taste the flavorless"

*(not "taste the tasteless")*

Ch 35 already renders 淡乎其無味 as *"It is bland and flavorless"* — and the thing being described there is the **Tao**. Matching the word makes 味無味 legible as what it is: not a general counsel of blandness but an instruction to **taste the Tao**. Wang Bi reads it the same way — 以恬淡為味, *"takes the calm and bland as its flavor."*

#### 大小多少 → "Great or small, many or few" — a quantifier, not a maxim

Four bare characters — 大 (*dà* — great), 小 (*xiǎo* — small), 多 (*duō* — many), 少 (*shǎo* — few) — with no grammar between them. Three readings are genuinely available, and each classical commentator takes a different one:

- **王弼 (Wang Bi):** binds them to the clause that follows. His comment on the joint lemma 大小多少報怨以徳 is entirely about resentment — 小怨則不足以報，大怨則天下之所欲誅，順天下之所同者，德也, *"a small resentment is not worth repaying; a great resentment is what the whole world wishes to punish; to go along with what the world holds in common — that is integrity."* So: **great or small, many or few [resentments]**, repay resentment with integrity.
- **河上公 (Heshang Gong):** 欲大反小，欲多反少，自然之道也 — *"want the great, revert to the small; want the many, revert to the few — this is the way of what is so of itself."* So: shrink the large.
- **The common modern reading**, supported obliquely by Han Feizi's 敬細以遠大 (*"respect the minute in order to keep the great at a distance"*): magnify the small — *treat the small as great, the few as many*.

**We follow Wang Bi**, on three grounds. He is the commentator on our own base text. His is the only reading under which the eight characters of the line form one thought rather than two unrelated ones — which matters now that Mawangdui A confirms 報怨以德 belongs here (see the Manuscript Notes). And the scale-doctrine the other two readings extract is already stated outright two lines down, in 圖難於其易，為大於其細 — the chapter does not need 大小多少 to say it a second time.

**The cost, stated plainly:** a famous aphorism becomes a grammatical particle. We accept it. Where the chapter argues scale it argues it in full sentences; this line is about grievance.

#### 細 → "slight", never "small"

細 (*xì*) is 糸 (*mì* — silk thread) over 田 — **thread-fineness**, not size, and the distinction is the chapter's. Han Feizi's illustrations of 細 are all hairline things: a thousand-yard dike bursting through **an ant's hole** (螻蟻之穴), a hundred-foot house burning from **smoke in a crack** (突隙之煙), a disease caught at the 腠理 (*còu lǐ* — the pores of the skin). Those are not small. They are *thin*. 小 (*xiǎo*) keeps *small*; 細 takes **slight**. The two must not collapse into one English word, here or at Ch 67's 其細也夫.

### Ch 64 · 始於足下 → "begins beneath your feet", never "with a single step"

There is no step in the line. 足下 (*zú xià*) is 足 (*zú* — foot) under 下 (*xià* — below): **under the foot**, the ground you are standing on. The received English — *"a journey of a thousand miles begins with a single step"* — inserts a step, and with it a whole doctrine of effortful beginnings that the chapter does not hold.

The commentaries settle it. 河上公 glosses the three proverbs in three matched phrases: 從小成大 (*"from small it becomes great"*), 從卑至高 (*"from low it reaches high"*), 從近至遠 (*"**from near** it reaches far"*). **Near**, not *few*. The axis is distance from where you stand, not a count of steps.

**What "a single step" drops:** the chapter's argument. Every other image here is of a thing that is small and close and *not yet anything* — 未兆 (not yet cracked into a sign), 微 (faint), 毫末 (a hair's tip), 累土 (a heap of dirt). "A single step" converts that into motivation. "Beneath your feet" keeps it as location — *this, here, now*, which is the same epistemology as the 以此 formula in `DISCOVERIES.md` §2.

### Ch 64 · 毫末 → "a hair's tip", never "a tiny sprout"

毫 (*háo*) is the fine hair of an animal's winter coat; 末 (*mò*) is 木 (tree) with a stroke marking the **tip** of the branch. **The tip of a hair.** Our source-table gloss reads "a tiny sprout," which domesticates the image into botany to match the tree — and loses the scale, which is the point. Laozi is not saying a big tree starts as a small tree. He is saying it starts as something as fine as a hair.

### Ch 64 · 未兆 → "gives no sign" — and a note on keeping research out of the verse

兆 (*zhào*) is the **fissure in a heated oracle bone or turtle plastron** — the crack the diviner reads. That is a real finding and it settles the reading: 未兆 is not "before it shows signs" in some loose metaphorical sense but *before anything readable has appeared*, which is why the paired verb is 謀 (*móu* — to plan, to lay a scheme). Wang Bi ties the whole opening to it — 謀之無功之勢, *"you plan it while the situation has not yet yielded any result"* — and Heshang Gong glosses the state as 未有形兆, *"has not yet taken shape or sign."*

**But the etymology stays in this file.** The line was first drafted as *"What has not yet cracked into a sign is easy to plan for"* and Shalom caught it as awkward, which it was, in two ways worth naming because the failure will recur:

1. **The research was in the poem.** The oracle-bone crack explains why the reading is right; it is not what a listener heard. Laozi's audience heard *before there is any sign of it*. Run the pointing test on the English, not only on the Chinese.
2. **The proportion was wrong.** The Chinese quatrain runs 4–5–4–4 characters — 其安易持 · 其未兆易謀 · 其脆易泮 · 其微易散. The draft ran 7–13–7–7 words. The Chinese lengthens that line by one character; the English nearly doubled it, and a stanza built on parallel shows the bulge immediately. **Count the characters before deciding an English line is finished.**

**Settled: "What shows no sign is easy to plan for."** Eight words against the neighbours' seven, matching the slight stretch the Chinese itself allows. It keeps 兆's own noun.

*The accepted loss:* 未 (*wèi*) is "not **yet**," and *shows no sign* drops the *yet*. The stanza recovers it two lines down, where 為之於未有 reads *"handle it while it is not yet there"* — so the temporal frame is stated once rather than twice. Alternates considered and set aside: *"What shows no sign yet"* (keeps 未 exactly, costs a beat on the trailing word) and *"What has not yet shown itself"* (closest to Heshang Gong's 未有形兆, but ten words, and the bulge returns).

### Ch 64 · 復眾人之所過 → "brings the crowd back from where they have gone too far"

過 (*guò*) carries both *pass by* and *go too far*, and English can hold both — going past **is** overshooting. The commentaries take the second, and they agree:

- **王弼:** 不學而能者自然也，喻於不學者過也，故學不學以復衆人之過 — *"what one is capable of **without** learning is what is so of itself; being instructed away from the unlearned is the **overshooting**; so one learns the not-learning in order to bring back the crowd's overshooting."*
- **河上公:** 衆人學問反過本為末，過實為華 — *"the crowd's learning turns the wrong way: they **overshoot** the root for the branch, overshoot the substance for the flower"* — and 復之者使反本也, *"to 復 them is to make them return to the root."*

So 復 (*fù*) is **bring back**, not *recover*, and what is brought back is people, not lost knowledge. The common English *"restores what the multitude has passed over"* reads 過 as *passed by* and turns the sage into an archivist of neglected things.

**Wang Bi's gloss is the chapter's hinge**, and worth stating plainly: he equates 不學 (*bù xué* — the unlearned) with 自然 (*zìrán* — so of itself). That makes the last line, 以輔萬物之自然，the thesis rather than the coda, and makes 學不學 the same move as 為無為 — get your hand off the thing that already works.

### Ch 64 · 欲不欲 / 學不學 keep Ch 63's shape

欲不欲 (*yù bù yù*) and 學不學 (*xué bù xué*) are grammatically identical to Ch 63's triple 為無為，事無事，味無味, rendered there *"Do the not-doing, serve the not-serving, taste the flavorless."* So here: **"wants the not-wanting"** — and, by an accepted departure, **"learns to unlearn."**

*Why the second one breaks the pattern.* The parallel wants "learns the not-learning," and 不學 is strictly the capacity that **precedes** learning — Wang Bi's 不學而能者自然也, *"what one is capable of without learning is what is so of itself"* — where *unlearn* implies erasing something already acquired. Related, not identical. Shalom kept "learns to unlearn" for its compression, with the cost named: the four-line series loses one of its two matched hinges. Logged so the departure is visible rather than looking like drift.

Heshang Gong reads both lines differently — 聖人欲人所不欲, *"the sage desires what people do not desire"* — a comparative rather than a reflexive. We keep the reflexive, on internal consistency: this construction is a signature of the book and it must not shift shape between adjacent chapters.

### Ch 64 · 自然 → "being so of themselves", and 不敢為 → "never pushes them"

Two closing decisions, both about resisting a smoother English.

**以輔萬物之自然** was drafted as *"supports the countless things in being what they truly are."* That is lovely and it imports a metaphysics the Chinese does not have: *truly* implies a false self to be told apart from a real one. 自然 (*zìrán*) is **so-of-itself** — process, not essence, and nothing underneath it to be true to. Settled as **"in being so of themselves."**

**而不敢為** was drafted as *"without forcing anything."* Two losses. First, 為 (*wéi*) is already rendered **handle** twelve lines above, in 為者敗之 — the same character cannot be two English words inside one chapter. Second, 敢 (*gǎn*) disappears altogether: the sage *could* and refuses to, which is restraint before what is so of itself rather than a description of manner. It also matters for this chapter specifically, whose logic is also the logic of preemption (see the Reading Notes on the shadow). 不敢為 is the constraint that keeps the chapter honest, and a prohibition must not soften into a style.

**First settled as "and does not dare to do," then superseded on 2026-08-20 by the 敢 lock** — see `glossary/gan-敢.md` and the sweep note below. *Dare* reads as fear in modern English and Ch 73 makes 不敢 a form of courage. **Now "and never pushes them,"** which carries 敢為 as one verb rather than splitting it; the argument above stands unchanged, only the English moved.

*A limit of the harness, recorded because it will recur:* **"force" cannot be forbidden for 為 mechanically.** Six chapters carry both 為 and 強 (*qiáng* — strong, to force), and Ch 25's *"Forcing a label upon it"* renders 強 legitimately. The checker's evidence gate cannot say *right for that character, wrong for this one, same chapter*. So this stays a judgment call, and the Ch 29 debt in `RETROFIT.md` has to be argued rather than swept.

### Ch 66 · 處前而民不害 → "the people are not hindered" — and the reading we did not take

害 (*hài*) is *harm*, and the line is genuinely double.

**河上公 reads it as the people's intent:** 民親之若父母，無有欲害之心也 — *"the people are close to them as to father and mother, and have no heart wishing to harm them."* On that reading, 不害 describes what the people do **not want to do to the leader**.

**We read it as the people's experience**, on the parallel. The couplet is built as 處**上**而民不**重** / 處**前**而民不**害** — position, then consequence, twice. Above produces weight; in front produces obstruction. Reading the second half as a shift from the people's burden to the people's intent breaks a parallel the Chinese builds carefully.

And Heshang Gong supplies the obstruction reading himself, in the same breath: 不以光明蔽後 — *"does not use their brilliance to **eclipse** those behind."* 蔽 (*bì*) is to screen or cover over. That is the harm of standing in front, and 害 carries *hinder* within its range (cf. 妨害). **Settled as "the people are not hindered."** The alternative is real and is recorded here rather than dissolved.

### Ch 66 · 爭 → "compete", carried forward — but the term is owed an entry now

爭 (*zhēng*) is two hands, 爪 above and 又 below, pulling at one object between them: a tug of war. Rendered **"compete"** here to match the three drafted chapters that already use it — ch 3 (使民不爭), ch 8 (twice), and ch 22, which shares this chapter's closing formula 故天下莫能與之爭 verbatim and reads *"no one in the world can compete with them."*

**But "compete" is not obviously right, and the decision is about to get expensive.** 爭 is elemental grabbing, not rule-governed rivalry; modern English "compete" carries sport and markets. *Contend* is closer to the two hands. Three undrafted chapters are queued on this word — **68** (不爭之德, "the integrity of not-爭"), **73** (不爭而善勝), and **81** (為而不爭) — and 68's line in particular reads very differently as *the integrity of not contending*.

**Recommendation: settle 爭 with a glossary entry before drafting 68.** Deciding it now costs one entry; deciding it after 68, 73 and 81 costs a four-chapter retrofit on a term that appears in seven.

### Ch 65 · 明 → "clever" — a licensed departure from the lock, on Wang Bi's authority

明 (*míng*) is locked to **clear-seeing / clarity**, never "enlightenment" or "brilliance." **Ch 65 departs from it**, rendering 非以明民 as *"did not use it to make the people clever."* The departure is deliberate and is the only one in the book.

**Wang Bi defines the word himself, in this chapter, and defines it against the lock:**

> 明謂多見巧詐，蔽其樸也 — *"明 here means seeing much and artful deceit, screening over their uncarved."*
> 愚謂無知守真，順自然也 — *"愚 here means without cunning, holding fast to the true, following what is so of itself."*

That is not the 明 of Ch 33 (自知者明 — *"to know oneself is clear-seeing"*) or Ch 52. Here 明 is transitive and causative — 明民, *to make the people 明* — and what it produces, on Wang Bi's reading, is **巧詐** (*qiǎo zhà* — artifice and deceit). Heshang Gong reads it identically: 不以道教民明知巧詐也, *"does not use the Tao to teach the people bright-knowing and artful deceit."*

**So the lock is not broken; the character is being used in a second sense, and both classical commentators say so in as many words.** Rendering "clear-seeing" here would produce the opposite of the chapter: it would have the ancients withholding clarity from the people, which is precisely the authoritarian misreading this chapter has suffered for a century.

*This is the case `CLAUDE.md` anticipates — "departures require a logged reason." The reason is above.*

### Ch 65 · 愚 → "guileless", not "ignorant"

愚 (*yú*) is the word that makes this chapter look like a programme for keeping subjects stupid. It is not, and the evidence is internal.

**The sage claims 愚 for themselves.** Ch 20, already drafted, renders 我愚人之心也哉 as *"I have the heart of a fool!"* — a boast, in a passage where the speaker is proud to be the dull one among the bright. The ruler in Ch 65 is not lowering the people beneath themselves. They are bringing everyone to where the sage already stands. That is levelling, not subjugation, and it collapses the standard reading.

**And both commentators gloss 愚 with this edition's own locked terms.** Wang Bi: 無知守真，**順自然**也 — following what is **so of itself**. Heshang Gong: 使**朴質**不詐偽 — making them **plain and uncarved**, not deceitful. 愚 is the uncarved state, not a deprivation.

**"Guileless" over "simple" or "ignorant".** *Simple* is ambiguous in English and slides toward *simple-minded*; *ignorant* imports exactly the deprivation the Chinese does not have. *Guileless* says what both commentaries say — **without 巧詐, artifice** — and is unambiguously a virtue. The cost: it loses the verbal link to Ch 20's *fool*, which the Reading Notes carry instead.

### Ch 65 · 福 → "good fortune", never "blessing"

福 (*fú*) sits on the overlay watchlist, and the literal gloss in this chapter's own Source table says **"a blessing to the state."** *Blessing* imports a blesser — an agent who confers favor — and there is none here. 國之福 is the state's **good fortune**, the plain counterpart of 國之賊, *the state's thief*. Rendered as the pair the Chinese builds: *robs the state* / *is the state's good fortune*.

### Ch 65 · 與物反矣 → "turns back together with things" — 反 holds both senses, and the book already chose

反 (*fǎn*) is 厂 (a slope) with 又 (a hand) — a hand turning something over, or a climb back across a ridge. From that one gesture come **reverse**, **oppose**, and **return**. The two commentators take different halves:

- **王弼:** 反其真也 — *"it returns to **their** true."* 反 as *return*.
- **河上公:** 玄德之人與萬物反異，萬物欲益己，玄德施與人也 — *"runs **counter** to the countless things: they wish to benefit themselves; profound integrity gives to others."* 反 as *contrary*.

**The line was first drafted on Heshang Gong's reading** — *"It runs contrary to things"* — argued from the 反/順 hinge, since 順 (going with the current) is 反's natural opposite and the paradox needs the opposition. **That was wrong, and for a reason worth recording: the argument never checked what 反 already means elsewhere in our own translation.**

- **Ch 25:** 遠曰**反** → *"going far means **returning**."*
- **Ch 40:** **反**者道之動 → *"**Returning** is the Tao's movement."*

**And Ch 65 puts 反 immediately after 遠, which is Ch 25's exact sequence.** 深矣，遠矣，與物反矣 traces the same arc as 大曰逝，逝曰遠，遠曰反 — deep, far, and then the turn. The chapter is not making a new claim about opposition; it is saying that profound integrity moves the way the Tao moves.

**The grammar settles it too.** 與 (*yǔ*) marks accompaniment — *together with*. Laozi did not write 逆物 (*against things*) or 反於物 (*opposed to things*), but 與物反: *with things, turned back*. Under the contrary reading, 與 is left doing nothing.

**Settled as "and turns back together with things."** *Turns back* carries both senses in ordinary English — you turn back toward home, and you turn back an advance — so the paradox survives intact without the book contradicting itself. **The paradox is inside the character**, and it is a physical fact rather than a mystical one: turning around and going against are the same act, seen from two positions. To anyone still walking forward, the one who has turned for home is coming straight at them.

### Ch 65 · 大順 → "runs with the great current", never "the great accord"

順 (*shùn*) is 川 (*chuān* — a river, three strokes of running water) over 頁 (*yè* — a head, the radical in 頭, 顏, 頸). **A head facing downstream.** Not agreement — *orientation*. Its opposite is 逆 (*nì*), an inverted person plus the movement radical: going upstream.

Drafted first as **"the great accord"** and caught by Shalom as vague. It was, in three ways: Latinate and abstract where 順 is a picture; *bilateral* (accord is mutual agreement) where 順 is unilateral and directional; and it flattened the chapter's close into conflict resolution — *runs contrary… then reaches agreement* — when the claim is that you turn from what things grab for and the current takes you.

**How the error happened, since the mechanism will recur:** *harmony* was unavailable — it belongs to 和 (*hé*) at ch 18, 42 and 55 — so the draft reached for the nearest synonym instead of going back to the character. A thesaurus standing in for a radical.

**Two facts raise the stakes.** 順 appears **exactly once in the whole book**, this line; 逆 never appears at all. It is a hapax at a chapter's final word, so it gets one shot and no consistency constraint. Rendered **"and only then runs with the great current"** — one verb, two prepositions, so the English performs the reversal the Chinese performs. *Current* keeps the water without taking 流's *flow* at Ch 61's 下流.

### Ch 65 · 智 → "guile", and why not "clever" or "cunning"

**The draft collapsed two characters into one word.** 明民 read *"make the people clever"* and 以其智多 read *"they are too clever"* — 明 (*míng*) and 智 (*zhì*), four lines apart, both *clever*. The same fault as 眾人/俗人 in Ch 20, and the checker cannot see it for the same reason.

**"Cunning" was the obvious repair and is already spoken for three times over:** ch 3 uses it for **知** (無知無欲) *and* for **智** (使夫智者) in adjacent lines, ch 57 for **巧** (人多伎巧), and ch 58 once more. A fourth character would make it useless.

**愚 and 智 are this chapter's own antonym pair** — 將以**愚**之 against 以其**智**多 — and 愚 is already rendered *guileless*. So 智 takes **guile**, and the English pair mirrors the Chinese pair exactly, in the same proportion: 愚 once and 智 three times, *guileless* once and *guile* three times.

**It is also what the commentators say.** 王弼: 多**智巧詐** — *"much 智, artful deceit."* 河上公: 以其**智**多，故為**巧偽** — *"because their 智 is much, they practise artifice and falsity."* Neither reads 智 here as innocent intelligence.

*The cost, stated:* 智 is a Confucian **virtue** — one of 仁義禮智 (humaneness, duty, ritual, wisdom) — so a neutral English word keeps Laozi's polemic sharp, attacking a thing everyone admires. *Guile* pre-loads the verdict. **We accept that here and not elsewhere:** the polemic lives in Ch 19's 絕聖棄智, which keeps *cleverness*. In Ch 65 both commentators say 智 has already curdled into artifice. A licensed split by chapter, like 無事.

### 王 → "ruler / sovereign / to rule", never "king" — swept 2026-08-19

The full argument is in `glossary/wang-王.md` and `DISCOVERIES.md` §4. The rendering decisions, chapter by chapter:

| Chapter | Chinese | was | now |
|---|---|---|---|
| 16 | 公乃王，王乃天 | sovereignty | **unchanged** — already ungendered |
| 25 | 王亦大 *(silks: 人)* | the aligned human | **unchanged** — already follows the witnesses |
| 32, 37 | 侯王 | rulers | **unchanged** |
| 39 | 侯王 ×3 | **wise** rulers | **rulers** |
| 42 | 王公 | **kings** and lords | **rulers and lords** |
| 66 | 百谷王 ×2 | **king** of the hundred valleys | **rule** the hundred valleys |

**The principle: 王 carries no gender and English *king* cannot shed one.** Chinese nouns have no grammatical gender and the graph is an axe-head, not a person. So *king* does not translate a gender; it adds one — and seats it on a throne in eight chapters that define authority by lowness.

**Ch 66 takes the verb.** 王 works verbally in classical Chinese (*wàng* — to reign over), and 能為百谷王 accepts it: *rivers and seas can **rule** the hundred valleys.* The verb keeps the power and seats nobody. Shalom's line.

**Ch 39's "wise" was ours.** 侯王 is a flat class term for the ruling stratum. Rendering it *wise rulers* three times handed the office a compliment the Chinese withholds — in the chapter whose own line is 是以侯王自謂孤、寡、不穀, *"this is why rulers call themselves orphaned, meagre, unworthy."* Deleted. Recorded rather than quietly fixed, because it is the clearest instance in this repository of the translator's politics leaking into the verse, and it was found only because three older overlays were being chased.

**Ch 42 keeps 公's word.** 王公 is 王 + 公, and 公 is locked to *lord / minister*, so the compound reads *rulers and lords*.

**Left open, and proposed rather than applied: Ch 25's "the aligned human."** Both silks read 人 (*rén* — human) where the received text reads 王, and our verse follows them — correctly. But it renders bare 人 as *the aligned human*, and nothing in the Chinese licenses *aligned*. The qualifier does in miniature what the throne did in full: it decides which humans are among the four great things. `DISCOVERIES.md` §1 rests on the line reading simply **the human**. Recommended deletion; a different character from 王 and Shalom's own word, so it waits on him.

### Ch 66 · 百谷王 → "rule the hundred valleys"

Two further reasons beyond the gender, both about this chapter specifically.

**The referent is water.** 百谷王 is said of rivers and seas. There is no monarch in the sentence to be male or female, so standing rule 2's *note the seam* does not apply — there is no seam in the Chinese to note, only one we would be making.

**And the chapter is arguing against the throne's own metaphor.** 以其善下之 — the sea rules the valleys *because it is masterful at staying below them*. Every English monarch-word encodes elevation, which is precisely the spatial claim being inverted. 河上公 keeps the water in view: 江海以卑故眾流歸之 — *"rivers and seas, being low, so the many streams come home to them."*

### Ch 67 · 慈 → "tenderness", never "compassion" or "mercy"

**慈 (*cí*) is a parent's love for a child, and the direction is the whole word.** It lives in the pair 孝慈 (*xiào cí*), which this book uses twice — Ch 18's 六親不和，有孝慈 and Ch 19's 絕仁棄義，民復孝慈. The two halves run opposite ways: 孝 is the child's devotion **upward** to the parent, 慈 is the parent's love **downward** to the child. 慈母 (*cí mǔ*) is the ordinary Chinese phrase for a loving mother.

河上公 glosses the first treasure with no abstraction at all: 一曰慈 → **愛百姓若赤子**, *"loving the hundred surnames as if they were **newborn infants**."* 赤子 is a just-born child.

**Why "compassion" fails.** *Com-passion* is suffering-with: a response to another's pain, horizontal, offered to anyone. 慈 is not a response to anything. It is the standing disposition of a parent toward a child, present whether or not the child suffers, and pointed at one's own. The received word also fails the hymn test on contact — *"the sage is full of compassion"* is a sermon — and it carries Buddhist freight (慈悲, *cíbēi*, is the standard Buddhist compound) that postdates this text.

**Why "mercy" is worse.** Mercy is punishment withheld. It requires a judge, a sentence, and a power to inflict it. Nothing in 慈 has any of that.

**Why not simply "love".** English *love* covers eros, liking, charity and God, and carries none of 慈's direction. It is not wrong, and it is the alternate if *tenderness* proves too soft.

**Why "tenderness", including the objection to it.** It is bodily rather than moral — you can point at someone handling an infant tenderly, and you cannot point at compassion. It is not a virtue-word in English, so the naturalistic razor leaves it intact.

The objection is that it sounds passive, in a chapter that claims this treasure **wins wars**. That softness is the point and should not be engineered away. **The chapter's rhetorical structure is: here is the softest thing there is, and it is the most powerful** — so an English word that already sounds strong pre-resolves the paradox the Chinese builds. Ch 78's 柔弱勝剛強 is the same move.

**And the mechanism is not sentimental.** Both commentators explain how tenderness wins, and neither appeals to providence. 王弼: 相慜而不避於難，故勝也 — *"they feel for one another and do not shirk danger, therefore they win."* 河上公: 百姓親附，并心一意 — *"the people draw close and attach, joining hearts into one intent."* Unit cohesion. People who love each other do not run.

*Consequence, and it is owed:* Ch 18 currently renders 孝慈 as **"filial piety"** alone — 慈 is dropped outright — and Ch 19 renders it *"filial piety and love."* Logged in `RETROFIT.md`.

### Ch 67 · 儉 → "frugality", and 且 → "grab at"

**儉 (*jiǎn*)** appears only in this chapter, and it is economic rather than ascetic. 王弼: 節儉愛費，天下不匱 — *"sparing, and careful of expenditure, so the world does not run short."* 河上公 makes it fiscal: 賦儉若取之於己也 — *"taxing sparingly, as if taking from one's own."* Hence **frugality**, and the paradox stands as the Chinese has it: 儉故能廣, *spend little and your reach is wide.*

**且 (*qiě*)** in 今捨慈且勇 is usually read as a bland conjunction, *and*. 王弼 says otherwise, in three characters: 且猶取也 — ***"且 is like 取 (to grab, to take)."*** So the line is not "abandon tenderness and be brave" but **"abandon tenderness and grab at courage."** The grabbing is what makes the triple an indictment rather than a description, and it is why the verdict is 死矣, *that is death*.

### Ch 67 · 成器長 → "chief of the vessels"

器 is locked to **vessel / tool / implement**, and Ch 28 supplies the reading: 樸散則為器 — *"when the uncarved is scattered it becomes vessels."* Vessels are the specialised things, each carved into one use. So 成器長 says the one who refuses to go first becomes what all the specialised things answer to, **because they were never carved into a use of their own.** 王弼: 唯後外其身，為物所歸 — *"only by putting themselves behind and outside do they become what things return to."*

Left visible rather than smoothed: 河上公 reads 成器長 as 得道人 — the chief of those who have attained the Tao, so a leader of people rather than of implements. And **Han Feizi's text reads 事 (affairs) for 器**, which is the older witness. See the Manuscript Notes.

### Ch 67 · 守 → "defend" — a licensed flexion

守 (*shǒu*) is locked to **hold fast to**, paired against 抱 (embrace). In 以守則固 it is plainly military — to hold a position under siege, against 戰 (*zhàn* — to give battle) in the same line. 河上公 writes it out: 以守衛則堅固, *"used in defending the walls, it is solid."* Rendered **"defend with it and you hold firm"**, which keeps *hold* audible without pretending the lock's sense is the one operating.

### Ch 67 · 天將救之 — the strain case, kept open

Already flagged in this file as one of the readings that will not settle: **天將救之，以慈衛之 reads agentive.** 天 is locked to *nature / the natural* and never *Heaven*, but this line has nature **doing** something — rescuing, and then guarding.

河上公 does not soften it either: 天將救助善人，必與慈仁之性 — *"when nature is about to help a good person, it necessarily **gives** them a nature of loving-kindness."* On his reading nature hands over the tenderness, which then does the guarding.

**Rendered "When nature would rescue someone, it guards them with tenderness."** *Would rescue* keeps the conditional 將 and stops short of a promise; *rescue* rather than *save* follows the decision already logged at Ch 27 and Ch 52 — 救 has no soteriology in it. The agency stays where the Chinese puts it, and the strain stays named.

### Ch 67 · 似不肖 → "look like nothing", and 細 → "petty"

**The chapter opens on Laozi, not on the Tao** — see the Manuscript Notes, where the base text's 道 is set aside on six converging arguments.

**似不肖 carries a pun and English can hold it.** 肖 (*xiào*) is *to resemble*; 不肖 (*bù xiào*) is both **not resembling anything** and, as a fixed humility term, **a nobody**. 王弼 takes the first — 肖則失其所以為大矣, *"if it resembled, it would lose what makes it great"* — and 河上公 takes the second, glossing the whole line as 佯愚, *feigning foolishness*. Rendered **"look like nothing"**, which in English means both *resembles nothing* and *appears to be no one*, and which lets the next two lines run as a chain: *look like nothing · look like nothing · looked like something*.

**細 → "petty" here, "slight" at Ch 63 — a licensed flexion.** The Ch 63 decision established that 細 (*xì*) is thread-fineness and must never collapse into 小 (*xiǎo* — small). *Petty* keeps that distinction and fits the subject, which on the settled reading is a **person**: 河上公 glosses 其細 as 唯如小人也，非長者 — *"just like a petty man, not an elder."* *Slight* is right for a task at Ch 63 and wrong for a man here.

**The line, settled:**

> Everyone says I am vast, and look like nothing.
> Only because I am vast do I look like nothing.
> If I looked like something, I would long ago have become petty.

### 敢 → "push / venture", never "dare" — swept 2026-08-20

Full argument in `glossary/gan-敢.md`. The short of it: **"not daring" reads as fear in modern English, and the book says the reverse.** Chapter 73 — 勇於敢則殺，勇於**不敢**則活, *"courage in 敢 kills; courage in **not**-敢 lives"* — makes 不敢 a form of courage, which *not daring* cannot carry.

敢 is a hand with a hunting weapon going after a boar; the *Shuowen* has 進取也, *"to advance and take."* **Appetite, not bravery.** And 不敢 is a politeness formula in classical Chinese — 不敢高攀, *"I could not presume upon your attention"* — the language of declining to help yourself, not of being afraid.

| Chapter | Chinese | was | now |
|---|---|---|---|
| 30 | 不敢以取強 | doesn't **dare** to seize dominance | never **pushes on** to seize dominance |
| 64 | 而不敢為 | and never **dares** to handle them | and never **pushes** them |
| 67 | 不敢為天下先 ×2 | not **daring** to be first in the world | never **pushing** to be first in the world |

**Ch 64 renders 不敢為 as a unit.** *"And never pushes them"* carries 敢為 in one English verb, because *push to handle* will not stand. The chapter's contrast is sharper for it: 輔 (*fǔ*) is the spare timber lashed alongside a cart-wheel to brace it, and a brace holds from the side where a push moves from behind. **Support them; do not push them.**

**On sharing "push" with 推.** Ch 66's 天下樂推 reads *"the world gladly pushes them forward"*, so one English word now covers 推 (*tuī*) and 敢 in adjacent chapters. Accepted deliberately, and it is not the 眾人/俗人 fault: those two collapsed **inside one chapter** and hid a distinction that chapter was drawing. These two sit in neighbouring chapters doing **complementary** work — the same physical act with opposite agents. *They never push themselves forward; the world pushes them forward.* That is what Chapters 66 and 67 jointly argue, and the shared verb states it.

### Ch 73 · 敢 stays "pushing" even where the grammar would allow "pursuit"

`glossary/gan-敢.md` left one question open: Ch 73 holds the book's **only affirmative 敢**, nominalised after 於 in 勇於敢則殺, so the slot wants a noun and *pursuit* — the word closest to the character's boar-hunting picture — becomes grammatically available for the first time.

**Settled as "pushing", on 河上公's gloss.** He reads 敢 here as 有為 (*yǒu wéi* — having-doing, acting): 勇敢**有為**即殺身也, *"brave-daring and **acting** is killing yourself,"* and 勇於不敢**有為**則活其身, *"brave in not-daring-to-act keeps the body alive."* And on 天之所惡 he is blunter still — 惡**有為**也, *"what it hates is **acting**."*

So 敢 in this chapter is not chasing a quarry. It is **pressing forward to act at all**, which is the same forward press rendered *push* at Chapters 30, 64 and 67. *Pursuit* would import a target the chapter does not have, and would split the term across the one chapter that defines it.

**The line reads:** *"Brave in pushing, and you are killed. Brave in not pushing, and you live."* 勇 (*yǒng* — courage) sits on both sides, which is the point: this is not courage against cowardice but two directions of courage.

### Ch 73 · 繟然 → "unhurried", and the net that is not a watcher

**繟然 (*chǎn rán*)** is glossed by 河上公 in two characters — 繟，寬也, *"繟 means wide, loose."* Wang Bi fills in the behaviour: 安而不忘危，未召而謀之 — *"at ease and not forgetting danger; plans before being summoned."* Rendered **"unhurried"**: it keeps the ease and avoids *slack*, which is a fault in English. The looseness echoes 疏 (*shū* — wide-meshed) two lines later, and a reader who hears that is hearing the chapter's shape.

**天網恢恢，疏而不失 must not become surveillance.** 河上公 reads it morally — 司察人善惡，無有所失, *"it watches over human good and evil, and nothing is lost"* — and that reading is the seed of every later use of 天網恢恢 as a slogan about divine justice catching criminals.

**We decline it.** There is no watcher in the Chinese, only a net; 失 (*shī*) is *to lose*, not *to convict*. Rendered **"Nature's net is vast. Its mesh is wide, and nothing slips through."** That is a statement about how consequence works — loosely, at a distance, without haste, and completely — not about anyone keeping a ledger. The naturalistic razor applies here as much as to 天 itself, and the moral reading is exactly the overlay this edition strips.

**天之所惡 stays agentive, and is flagged.** *What nature hates* has nature doing something, as 天將救之 does at Ch 67. Both commentators read it that way and neither softens it. Kept, and named here rather than dissolved — the same strain case, now in a second chapter.

### Ch 73 · 天之道 → "the way of nature"

Established at Ch 9 (*"This is the way of nature"*) and Ch 47, and not a breach of the 道 lock: the lock forbids **the Way** as a rendering of 道 standing alone, where it carries *Logos*. 天之道 is a possessive — nature's way of going about things — and lowercase *way* inside it is ordinary English. Chapters 77, 79 and 81 all carry 天之道 or 天道 and should follow.

### Ch 73 · 惡 → "turns against", and 難 → "finds this hard"

**惡 (*wù*) is to loathe, not to dislike.** The first draft read *"what nature hates"*; the revision tried *dislikes*, which weakens a word this chapter makes lethal — a nature that merely dislikes pressing forward does not get people killed for it. But *hates* gives nature a feeling, which is the agentive strain already flagged at Ch 67's 天將救之.

**Settled as "what nature turns against."** It keeps 惡's full aversive force and makes it an orientation rather than an emotion, which is the naturalistic razor applied to a verb rather than a noun.

**難 (*nán*) is difficult, not unknown.** 是以聖人猶難之 was drafted as *"Even the sage doesn't know"* — a natural reading of the English sequence, since the line follows 孰知其故？ (*"who knows the reason?"*). Both commentators refuse it, and Wang Bi refuses it in four characters:

> 言誰能知天下之所惡意故耶？**其唯聖人。**夫聖人之明，猶難**於勇敢**，況無聖人之明而欲行之也
> *"Who can know the reason for what is hated? **Only the sage.** And the sage's own clarity still finds it difficult **with respect to daring** — how much more someone lacking that clarity who means to act anyway."*

其唯聖人 says the sage **does** know. And both gloss 難 as 難**於勇敢** — difficult *with respect to pressing forward*. The sage's difficulty is about **acting**, not about **knowing**.

**Settled as "Even the sage finds this hard."** The true reading is the harder one: not that everyone is equally in the dark, which would be a comfort, but that the person best equipped to judge when to press forward is the one most reluctant to.

### Ch 68 · 不與 → "does not engage them" — Wang Bi glosses it with 爭

不與 (*bù yǔ*) is two characters and no verb: *does not [go] with.* 與 (*yǔ*) is the accompaniment marker already met at Ch 65's 與物反 (*turns back together with things*) and at Ch 22 and 66's 莫能與之爭 (*no one can contend **with** them*).

**王弼 supplies the missing verb in three characters:** 不與**爭**也 — *"does not contend with them."* So 不與 is the same refusal as 不爭, stated by dropping the verb rather than negating it. Rendered **"does not engage them"** — a military idiom in English, which is the register the whole chapter is in, and which keeps *contend* free for the 不爭之德 three lines later where 爭 actually appears.

河上公 reads the mechanism rather than the word: 不與敵爭而敵**自**服也 — *"does not contend with the enemy, and the enemy submits **of itself**."* 自 (*zì* — self) again, doing the work 自然 does everywhere else in this book.

### Ch 68 · 士 → "warrior", and the term is rendered three ways across the book

**王弼 defines it in this chapter:** 士，卒之帥也 — *"士 is the commander of troops."* So in Ch 68 the word is unambiguously military, and the paradox is built on it: *one masterful as a **warrior** is not **martial**.*

**But 士 is doing different work elsewhere and our English shows it:**

| Chapter | Chinese | rendered |
|---|---|---|
| 15 | 古之善為**士**者 | "The ancient **masters**" |
| 41 | 上**士** · 中**士** · 下**士** | *(undrafted)* |
| 68 | 善為**士**者 | "One masterful as a **warrior**" |

Ch 15 and Ch 68 open on the **identical construction** — 善為士者, *"one masterful at being a 士"* — and take different English. Some spread is legitimate: 士 named the warrior-retainer class of the Zhou and drifted toward the scholar-official, and Ch 41's 上士/中士/下士 hearing the Tao are men of rank rather than soldiers. But Ch 15 also collapses 善為 entirely, and *masters* sits close to a word `CLAUDE.md` forbids for 聖人. Logged in `RETROFIT.md`.

### Ch 68 · 配天 → "matched with nature", and 極 is a ridgepole

**配 (*pèi*)** is the character of pairing — it is the word in 配偶 (*pèi ǒu* — a spouse). Not *accords with*, not *corresponds to*: **matched with**, as one of a pair. 河上公: 能行此者，德**配**天地 — *"one who can do this, their integrity is matched with sky and earth."*

**極 (*jí*)** is the **ridgepole** — the highest beam of a house — and from there the utmost, the pole, the limit. 古之極 is not "the ancient principle" but *the furthest the ancients got*. 河上公: 是乃古之極要道也.

Rendered **"being matched with nature, the utmost the ancients reached."**

### Ch 68 · the fourth clause breaks the pattern, and should

Three clauses negate — 不武, 不怒, 不與 — and the fourth does not: 善用人者，**為之下**, *"one masterful at using people **puts themselves below** them."* Three refusals, then one positive act, and the positive one is the one the chapter names twice more in its closing triple.

王弼 says why it has to be an act rather than an abstention: 用人而不為之下，則力不為用也 — *"use people and fail to put yourself below them, and their strength will not be usable."* The lowness is not modesty. It is the mechanism.

### Ch 69 · 吾寶 is Ch 67's 三寶, and Wang Bi says so

The line is 輕敵幾**喪吾寶** (*qīng dí jī sàng wú bǎo* — "making light of the enemy comes close to losing my treasures"). **王弼 glosses it in four characters: 寳，三寳也** — *"寶 means the three treasures"* — and closes 故曰幾亡吾寶.

Two chapters back, Ch 67: 我有**三寶**，持而保之 — *"I have three treasures. I hold them and keep them safe."* 慈 (*cí* — tenderness), 儉 (*jiǎn* — frugality), 不敢為天下先 (*bù gǎn wéi tiān xià xiān* — never pushing to be first in the world).

**So Ch 69 is Ch 67's treasures worked out on a battlefield, and the chapter's two ends are its first and third treasures.** The opening 吾不敢**為主** (*"I do not push to move first"*) is 不敢**為天下先** in military dress — the third treasure, the refusal to go first. The closing 哀者勝矣 (*"the one who grieves wins"*) is the first, 慈, in its hardest case. 河上公 makes the same connection from the other end: 哀者，**慈**仁 — *"the one who grieves is tender and humane."*

**河上公 reads 寶 as 身 instead** — 寶身也，欺輕敵者近喪身也, *"寶 means the body; one who makes light of the enemy comes near to losing his life."* That is the prudential reading and it is flatter. We follow Wang Bi, on the strength of the verbal echo: 吾寶 two chapters after 我有三寶 is not an accident.

**Rendered "my treasures", plural and undefined**, so a reader who has come through Ch 67 hears it and a reader who has not is not told something Laozi does not say here.

**喪 is *lose*, not *destroy*** — the mourning word, and 王弼 glosses the line with 亡 (*wáng* — to lose, to perish). *Destroy* would make it something an enemy does to you from outside; the chapter says the opposite, that contempt is how you let go of your own tenderness. Rendered **"nearly costs me my treasures"**, which keeps 輕敵 as the agent, as the Chinese grammar has it, without the wrecking.

### Ch 69 · 主 / 客 — the image is jargon, and jargon has to be translated

不敢**為主**，而**為客**. The characters are lovely: 主 (*zhǔ*) is a **lamp with its flame standing on it** — whoever keeps the fire, so whoever's house it is. 客 (*kè*) is 宀 (a roof) over 各 (a foot arriving at a threshold) — whoever comes under someone else's roof.

**Drafted first as "I do not push to be the host. I come as the guest," and changed on Shalom's objection: he could not tell what the saying meant, and neither could any reader who had not been told.** The objection is correct, and the reason is that **主/客 was a term of art**, not an image. Warring States military writing used the pair the way English uses *offense* and *defense*. A reader in 400 BCE heard technical vocabulary; a modern English reader hears a dinner party. **Jargon rendered as image is a mistranslation, not fidelity** — the same argument that sends 天 to *nature* rather than *Heaven*.

The reason first given for keeping the image also fails. It was said to preserve the link to Ch 34's 衣養萬物**而不為主**, the identical construction — but Ch 34's English already reads *master* and *owner*, not *host*. The link was broken at the far end before this chapter was drafted.

**河上公 supplies the sense outright:** 主先也，不敢先舉兵 — *"主 means **first**; he does not push to be the first to raise troops"* — and 客者和而不倡 — *"the 客 harmonises and does not **initiate**."*

Drafted next as *"I do not push to move first. I answer the one who does,"* **and objected to again on the same ground**: the reader has to carry *moves first* across the sentence boundary and supply it, and *answer* is a literary word doing the work of *respond*. Two demands on one short line.

Rendered **"I do not push to move first. I move second."** 河上公's sense, with nothing left to infer — 客 is the second party by definition. *First* is deliberate: it puts the line in the same words as Ch 67's third treasure, 不敢為天下先, *"never pushing to be first in the world."* The lamp and the threshold live in this note.

### Ch 69 · 進寸 / 退尺 — an inch of whose ground?

不敢**進寸**，而**退尺**. Read bare, this is *"advance not an inch, retreat a foot"* — and it sounds like flinching, which is precisely the charge `glossary/gan-敢.md` exists to prevent.

**河上公 says what the two verbs denote, and it is not tactical at all:** 侵**人**境界，利人財寶為**進**；閉門守城為**退** — *"to cross into **another's** borders and take profit from their goods is what **進** means; to shut your gate and hold your own city is what **退** means."*

So 進 is **trespass**, and 退 is **staying home**. Which makes the inch and the foot an argument rather than a ratio of nerve: **an inch of someone else's ground is not worth a foot of your own.** 寸 (*cùn*) is the inch measured at the wrist-pulse and 尺 (*chǐ*) is ten of them; English inch-to-foot is twelve, close enough, and both are body-measures, so the pointing test holds.

Drafted as **"I do not push an inch into another's ground. I give up a foot of my own"** — the English naming what the Chinese leaves implicit, on 河上公's authority, and closing off the purely tactical reading (*give ground to draw the enemy in*, ordinary Sunzi, which the bare characters permit).

**Shortened on 2026-08-24 to "I do not push forward an inch. I give up a foot."** The gain is the line: the long version was the only place in the chapter where the English ran past its Chinese, and it sat badly against the plain second half of the couplet.

**The cost, stated plainly, because it is real.** The bare English loses the *asymmetry* that was the note's whole finding — an inch of **someone else's** ground is not worth a foot of **your own** — and it reopens the tactical reading. Two things hold the line up anyway, neither of them as strong as naming it. *Push forward* carries 敢 (*gǎn* — the forward press to take), so the refusal is of appetite and not of nerve; and *give up* implies what is given up is one's own. The 河上公 gloss now lives in the reader-facing note at `notes/reading.md`, which is where a claim the verse does not make belongs.

### Ch 69 · 行無行 — the one line where the character repeats, and the English can too

The four negations are not all the same shape. Three are verb-無-noun: 攘無臂, 扔無敵, 執無兵. **The first repeats the graph**: 行無行 — but 行 is two words in one character, *xíng* (to go, to march) and *háng* (a row, a rank), and the line uses both. 王弼 settles which is which: 行謂行陳也, *"行 here means 行陣, the battle formation."* If both instances were ranks the line would have no verb at all.

**So all four are verb-無-noun after all**, and the English should say so. Drafted as *"forming ranks where there are no ranks,"* which preserved the repetition at the price of making the first member the odd one out. **Changed 2026-08-24 to "marching where there are no ranks"** — the plainer verb sense, and the four-line parallel becomes true rather than merely claimed. Then *baring / hauling / gripping where there is no X*. Descending length, 4-3-3-3, as in the Chinese.

What is lost is the graph's own echo, which no English can carry without inventing a pun the Chinese is not making.

**攘 and 扔 are Ch 38's pair, negated.** Ch 38: 則**攘臂**而**扔**之 — ritual, when no one answers it, *"bares its arms and hauls them in."* Ch 69 takes the identical gesture and empties it. The aggression makes every motion it knows and each one closes on nothing. 王弼: 言無有與之抗也 — *"there is nothing there to push back against."*

### Ch 69 · 哀 is grief, not compassion — and Ch 31 is the proof

哀 (*āi*) is 口 (a mouth) enclosed in 衣 (a garment): a cry inside mourning clothes. It occurs **twice in the book**, and the other is Ch 31: 殺人之眾，以悲**哀**泣之 … 戰勝以**喪**禮處之 — *"when many have been killed, weep for them with sorrow and grief … a victory in battle is handled by the rites of mourning."* Same subject, same battlefield, same word.

Both commentators pull it toward 慈 (*cí* — tenderness), and they are right about where it leads, but the character is **mourning**, and the claim is stronger for staying there. 王弼 gives the mechanism exactly: 哀者必相惜而不趣利避害，故必勝 — *"those who grieve necessarily cherish one another, and do not chase advantage or dodge harm, and so they must win."* **The grieving army does not calculate.** That is why it wins — not because grief is admirable but because a soldier already in mourning has nothing left to protect.

Rendered **"the one who grieves wins."** Not "the sorrowful", not "the compassionate", not "the one who mourns the war" — the text does not say what the grief is for, and naming it would decide something the Chinese leaves open.

### Ch 69 · 禍莫大於 matches Ch 46, and 兵 puns across the chapter

**禍莫大於輕敵** takes Ch 46's English for the identical formula 禍莫大於不知足: *"there is no greater disaster than …"* Kept parallel deliberately.

**兵 (*bīng*) — two hands holding an axe — opens and closes the chapter.** 用**兵**有言 and 執無**兵**. The graph means both *the weapon* and *the people carrying it*, and the chapter uses one sense at each end: the saying belongs to the people who hold the thing that turns out not to be there.

**Drafted as *"among those who wield weapons there is a saying"* so that the English repeated *weapons* at both ends and the pun survived. Changed 2026-08-24 to "Soldiers have a saying," and the pun is the price.** The objection was register: the long form is stiff and archaic. *Warriors* was proposed and rejected — the word is ennobling in modern English (warrior spirit, the inner warrior) and this chapter deflates the whole enterprise; Ch 31 calls 兵 不祥之器, *instruments of ill omen*. **The honest cost of *soldiers* is twofold**: the English echo at the two ends is gone, and 用兵 is strictly what a *commander* does — 河上公 glosses the line 不敢先舉兵, *does not push to be first to raise troops*, which is a command decision, not a private's. Plainness was judged worth both. Ch 31 renders 兵 as *weapons*; Ch 30 renders 不以兵強天下 as *military force*, which is the looser use and stands.

**執 → "gripping", not "grasping."** 執 is a kneeling figure with the hands manacled — a physical seizing. Ch 29's 執者失之 (*"those who grasp it lose it"*) is the abstract sense and keeps *grasp*; here the hand is on a hilt.

### Ch 69 · whose "I" this is

河上公 flags the voice before anything else: 老子疾時用兵，故託巳設其義也 — *"Laozi loathed the militarism of his age, so he borrowed the first person to set out its meaning."* The 吾 of 吾不敢為主 is a **quoted** I, and 用兵有言 is rendered as an explicit attribution — *"soldiers have a saying"* — so the borrowing is visible on the page. By 吾寶 in the last movement the voice has come back to Laozi's own, which is what makes 吾寶 reach for Ch 67's 我有三寶.

### Ch 69 · 不敢 twice, and the lock makes the Ch 67 link audible

The chapter opens with 敢 (*gǎn*) twice — 吾**不敢**為主 … **不敢**進寸 — and `glossary/gan-敢.md` forbids *dare* outright: in modern English *he did not dare* means *he was afraid*, and Ch 73's 勇於不敢 (*"courage in not-敢"*) requires a word that can be brave. 敢 is a hand with a hunting weapon going after a boar; the *Shuowen* glosses it 進取 — **to advance and take**.

Rendered **"I do not push to move first … I do not push forward an inch."** The repetition is the Chinese's own. And *push* is the verb Ch 67 already uses for the third treasure — *"never pushing to be first in the world"* — so the reader hears the treasure being spent without being told about it, which is the whole argument of the note above.

### 自然 · "the self-so" retired — the lock committed the error it was written to prevent

**Reopened by Shalom, 2026-08-24, on the grounds that the word felt wrong.** It was, and the fault was structural rather than stylistic. Full argument in `glossary/ziran-自然.md` → *Why "the self-so" was retired*. The three findings:

**1 · It was a noun, and both commentators refuse to name a thing.** 王弼 on 道法自然: 自然者，**無稱之言**，窮極之辭也 — *"自然 is a term that **designates nothing**, an expression of the ultimate."* 河上公 on the same line: 道性自然，**無所法也** — *"the Tao's nature is 自然; **there is nothing it takes as a model**."* English *"the self-so"* is a definite noun phrase, and *the* instructs a reader to go looking for a thing. Once they look, 自然 becomes a fifth rung on a ladder whose whole point is that it has four. **That is the same structural error as "Nature," smaller in degree and identical in kind** — and this entry's own case against "Nature" is what convicts it.

**2 · It failed the pointing test.** 河上公 shows what passing looks like, glossing Ch 23: 雲從龍，風從虎，水流濕，火就燥 — *"clouds follow the dragon, wind follows the tiger, water flows toward the damp, fire goes toward the dry."* He points at **water finding the low ground**. Nobody can point at *the self-so*. It is a calque that lives only inside sinology and survived in the verse only because a note explained it.

**3 · The lock had already lost.** Its stated fear was that local renderings would make the term invisible. Three of five lines paraphrased anyway — 17, 51, 64 — and those three read *well*. What the lock preserved was the calque in the two lines it damaged.

**Now locked: 自然 → "of itself / of themselves · so of itself."** *"Self-so" is forbidden.* Only two verse lines moved.

### Ch 25 · 道法自然 → "the Tao models itself on being what it is"

**Shalom's rendering, and the reason it is right is that it declines to be a noun.** 法 (*fǎ* — to take as one's model) stays *models itself on* through all four rungs, so the pattern holds; what changes is that the object stops being a **name** (earth, sky, the Tao) and becomes a **clause**. The dissolution of the regress is made grammatically visible. A ladder that ends in *A is A* has ended, and Wang Bi's 窮極之辭 — *an expression of the ultimate*, what you say when there is nothing further to say — is exactly that shape.

**Both commentators gloss this line with 性** (*xìng* — inherent nature): 王弼's 道不違自然乃得其**性** and 河上公's 道**性**自然. *"Being what it is"* is 性 in plain English, so the essence-flavoured reading is not an import here — it is what the commentary tradition already does with this line.

**The precedent that does not bind it.** `notes/translation.md` (Ch 64, above) rejected *"in being what they truly are"* for 萬物之自然, because *truly* implies a false self to be told apart from a real one. That rejection stands and does not transfer: at Ch 64 the subject is **creatures**, where a true-self/false-self split is a live theological import; at Ch 25 the subject is **the Tao**, of which both commentators already predicate 性.

**The cost, named rather than hidden.** *"Being what it is"* spends the **自**. It names the state but not its provenance, and the whole force of the nose-character is that the being-so comes **from the thing itself and nowhere else**. That loss is accepted at Ch 25 and paid back at the other four, which all carry *itself / themselves*. **The one place 自然 sits in a noun slot is the one place we decline to translate it as a noun** — which is probably the truest thing available to say about the word.

### Ch 23 · 希言自然 → "Speak sparingly, for things go of themselves" — a strain case

A-自然 compressed to four characters, and **English has no predicate slot that fits it.** Recorded as a strain case rather than smoothed.

**"For," not "and."** Shalom's call, and it is the right dependency: *for* makes sparing speech follow **from** things going of themselves, which is 自然 as the **ground**. *And* would make it a consequence, reversing the direction. 河上公 supports the ground reading — 希言者是愛言也，愛言者**自然之道** — *"sparing speech is being sparing with speech; being sparing with speech is the **Tao of 自然**"* — and it is the mechanism of Ch 17, where the ruler says little and the people say *we did this ourselves*.

**What it adds.** The English supplies the consequence clause the Chinese only implies. 王弼 licenses it: 無味不足聽之言，乃是**自然之至言**也 — *"speech that is flavourless and not worth listening to: this is 自然's utmost speech."*

### Ch 25 · two changes made in the working tree, logged after the fact

Found unlogged during the 自然 sweep and recorded now rather than left silent.

- **萬物之母 area — "mother of creation" → "mother of the world."** Correct: the line is 可以為**天下**母, and 天下 (*tiān xià*) is locked to **the world**. *Creation* also imports a created order with a creator behind it, which is the theistic overlay this edition strips.
- **"the aligned human" → "humans."** 域中有四大，而**人**居其一焉 says *humans* with no qualifier. *The aligned human* smuggled in a spiritual grade the Chinese does not have, and made the fourth of the four greats a subset of people rather than people. *(Note that 人 here is itself the editorial reading — every excavated witness reads 王, "king." See `DISCOVERIES.md` §1 and the Ch 25 entry in `notes/manuscript.md`.)*

**The closest rival at Ch 25 — *"the Tao models itself on its own nature"* — was tested and refused, 2026-08-24.** It is the strongest alternative available: 性 (*xìng* — inherent nature) is the word both commentators use of this line, and *its own* carries the 自 lexically. Three things defeat it, and the argument is recorded in full in `glossary/ziran-自然.md` → *The closest rival, and why it was refused*: **nature is 天's word in this edition** (nine occurrences, none from 自然) and 天 is the rung two lines above; **河上公 reaches for 性 to cancel the modelling relation** (無所法也 — *"there is nothing it models itself on"*), not to fill it; and a possessed noun **re-posits a thing**, which is the axis the line was rewritten to clear.

### Ch 16 · 復命 → "returning to what was given" — and the pronoun that changed the subject

Was *"returning to your original nature."* Three faults, in rising order.

**命 (*mìng*) is a command issued to you, not an essence inside you.** The graph is 口 (a mouth) and 卩 (a kneeling figure) under a roof: **a mouth giving an order to someone kneeling.** From there, what is ordered *for* you — an allotment, a span. *Original nature* points inward at what you already are; 命 points outward at what you were handed. The book uses it that way two chapters later: Ch 51's 莫之**命** is rendered *"no one **commands** it."*

**It also spent 天's English.** *Nature* is this edition's word for 天 acting as an agent (9, 47, 59, 67, 73). Ch 16 has no 天 in the line, so the rendering was borrowing from a character that was not there — found while auditing the 自然 revision, `concordance.py --english "nature"`.

**And "your" is not in the Chinese.** The passage is about 萬物: 夫物芸芸，各復歸其根 — *"the things flourish; each returns to its root."* 是謂復命 refers to **that**. The pronoun swung the camera onto the reader and turned a cosmological observation into a personal instruction. This was the worst of the three, because it is invisible — nothing in the English looks wrong.

**Why "given" and not "nature," when both commentators gloss 復命 with 性命.** They do — 王弼: 復命則得**性命**之常; 河上公: 是為**復還性命**. But watch what 河上公 attaches: **使不死也**, *"so that they do not die,"* and on the line above 各復反其根而**更生**也, *"each returns to its root and is **born again**."* The weight is on the **allotted life**, not on a spiritual essence to be recovered. *What was given* keeps the issuing, keeps the life, and takes no pronoun.

**The more literal alternative is "what was allotted,"** which is nearer to 命 and stiffer; *given* was chosen for the verse and the argument recorded here.

### 天 · the split between "sky" and "nature", written down at last

Entry: `glossary/tian-天.md`, 2026-08-24. **The rule was already the practice; it had never been recorded**, and the lock table pointed at `glossary/tiandi-天地.md` — an entry for the *compound* 天地, not for the solo character.

**92 occurrences, the book's most frequent content character** — more than 道. 61 are 天下 (*tiān xià* — the world), 9 are 天地 (*tiān dì* — sky and earth), and **19 stand alone**. Those nineteen split cleanly:

- **8 are a tier in a cosmological series, with 地 (*dì* — earth) beside them → *sky*.** Ch 7 天長地久, Ch 16 王乃天，天乃道, Ch 25 the four greats and the ladder, Ch 39 天得一以清 against 地得一以寧. **地 is physical, so 天 is physical**; a thing and a principle cannot stand in one series.
- **11 take verbs — giving, hating, rescuing, having a way → *nature*.** 天之道 six times (9, 47, 73, 77 ×2, 81), plus 事天 (59), 天將救之 (67), 天之所惡 and 天網 (73), 天道無親 (79). **地 is absent from every one.**

**The split is forced, not chosen.** English has no word with 天's range: *sky* cannot say 天之道, *nature* cannot say 天地. A language that lacks a term's range either splits the word or flattens the text, and flattening is what produced *Heaven*.

**The mechanical form of the rule, for drafting: if 地 is in the line or the series, it is *sky*.** That decides every clear case. The one contested line is 配天 (Ch 68) — see `RETROFIT.md`.

**Chapters 77, 79 and 81 are undrafted and all three carry 天之道 / 天道.** They take **"the way of nature,"** matching Ch 9, 47 and 73. The book writes the formula with and without the particle 之; nothing turns on it and both take one English.

### Ch 70 · 行 — not "execute", and not "do" either

The Source table glosses 行 (*xíng*) as **"execute"** — twice — which is pre-lock English and mechanistic on its face. But the trap underneath is subtler. The obvious repair is *"easy to do"*, and **為 (*wéi* — do / handle) does not occur anywhere in Chapter 70.** Handing 為's locked word to a chapter that has no 為 is precisely what the `--english` direction of the checker exists to catch: a lock is a two-way claim.

**Shalom's choice: "follow."** The AI argued for **"walk"** — 行 is a picture of **a crossroads**, four ways meeting, going on foot, and in a book whose title character 道 (*dào*) is a road (辵 walking + 首 head) the foot metaphor is native rather than imposed. *"Practise"* was rejected by both as abstraction drift.

**The cost of "follow", recorded so it is not rediscovered later.** The word already carries **four other characters** in this manuscript — 從 (*cóng*, ch 21, *"simply follows the Tao"*), 隨 (*suí*, ch 2 and 29), 徒 (*tú*, ch 50), and a bare 之 (ch 14). 行 makes five. It also lands two lines above 則我者 (*"those who pattern themselves on me"*), where *follow* and *pattern oneself on* read as a strong and a weak form of one idea rather than as two different things. Accepted anyway: the line is plainer, and plainness is what 河上公 says the words have (省…約, *pared down… bound tight*).

### Ch 70 · 君 takes "ruler", and the overlap with 王 is deliberate

言有宗，事有君 — *words have an ancestor, affairs have a* 君 (*jūn*). 君 is 尹 (a hand gripping the staff of office) over 口 (mouth): the hand that governs and the mouth that commands.

**Rendered "ruler", which is also 王's (*wáng*) locked word.** Two reasons this is safe and one reason it is right. Safe: 王 does not appear in Chapter 70, so nothing collides on the page, and "ruler" is not on 王's forbidden list — that list forbids *" king"*, not the word we chose. Right: **internal consistency already decided it.** Ch 26's 靜為躁君 stands as *"silence is the ruler of the agitated."* One character, one English.

**"Lord" and "master" were both rejected.** *Lord* fails the hymn test in a chapter already speaking in the first person about being unknown. *Master* is forbidden outright for 聖人 (*shèng rén* — the sage), and 聖人 is in this chapter's last line; the collision would be two lines apart.

### Ch 70 · 宗 and 君 are people, and stay people

The besetting error in this couplet is not a wrong word, it is **abstraction**: 宗 becomes "a principle" and 君 becomes "a governing authority", and the line turns into epistemology. Both characters are persons. 宗 (*zōng*) is 宀 (a roof) over 示 (an altar tablet) — **the ancestral shrine inside the house**, hence lineage, hence ancestor. 河上公 keeps them concrete too: 有宗祖根本 (*"an ancestral root"*) and 事有君臣 (*"affairs have lord and vassal"*).

Held as **"Words have an ancestor. Affairs have a ruler."** Two short sentences, two people, no dash — the couplet's whole force is that the thing behind speech is *someone you could stand in front of*. The pointing test passes; "a principle behind words" does not.

### Ch 70 · 夫唯無知 — left double on purpose

夫唯無知，是以不我知 (*fú wéi wú zhī, shì yǐ bù wǒ zhī*) forks, and the fork changes the chapter's temperature:

- **A — the majority reading.** *Because they have no understanding, they do not understand me.* The crowd is at fault. This is the reading that makes Ch 70 a complaint.
- **B — 河上公's reading.** 是我德之暗，不見於外，窮極微妙，故无知也 — *"this is my 德 (integrity) being unlit, not seen on the outside, reaching the limit of the subtle — therefore there is no knowing."* He attaches 無知 to **the speaker's own hiddenness**. Nothing is on show, so nothing is known. Nobody is at fault.

Reading B is what the chapter's closing image says out loud — the sage **put the sacking on** — and it is what 河上公 says one line earlier as well: 人惡柔弱好剛強也, *"people hate the soft and weak and love the hard and strong."* Not stupidity. **Preference.**

**Rendered so that English holds both:** *"Only because there is no knowing it / do they not know me."* "No knowing it" reads either as *it cannot be known* (B) or as *they do not know* (A). This is honesty over false closure, executed in the verse rather than only in the note. The 夫唯 → **"only because"** construction matches Ch 67's 夫唯大，故似不肖.

### Ch 70 · 被褐而懷玉 — coarse cloth, and the echo with Ch 20

被 (*pī*) is to drape over; 褐 (*hè*) is 衤 (cloth) with a coarse hair-fibre, **a labourer's sacking**; 懷 (*huái*) is 忄 (heart) inside 褱, a garment-graph — something carried **inside the robe, against the chest**.

Note the shape: **a clothing word outside, a clothing word inside, and jade between them.** The line is built out of layers, and that is the argument.

**"Coarse cloth" was chosen over "sacking" for a cross-chapter reason.** Ch 20 renders 而我獨頑似鄙 as *"I alone am stubborn, and look coarse."* 鄙 (*bǐ* — the outskirts, rustic) and 褐 are different characters, but they are the same claim — *this one looks low-born* — and letting the English rhyme makes the 20 ↔ 70 thread audible to a reader who has no Chinese. Logged rather than left to chance.

**"Against the chest", not "at the heart",** even though 懷 carries the 忄 radical. 心 (*xīn* — heart) is locked, and the character is absent from this chapter; a radical is not a licence.


### Ch 70 · 知 stays one word in English, because it is one act in the Chinese

**知 (*zhī*) occurs five times in twelve lines** — 易知, 莫能知, 無知, 不我知, 知我者 — and it is the most concentrated run of the book's central verb anywhere in the text (47 chapters carry it). A first pass rendered the first two as *"understand"* and the last three as *"know"*, which is the natural English reflex: you understand a sentence, you know a person.

**Reverted to "know" throughout, and the reason is structural rather than cosmetic.** The couplet in the middle — 言有宗，事有君, *words have ancestors, affairs have rulers* — exists to say that the words come from someone. So comprehending the sentences and knowing the speaker are **not two acts**. That is why one character does both jobs, and why 不我知 (*"they do not know me"*) is offered as the *explanation* for 莫能行 (*"none can follow"*). Split the English and the chapter appears to describe two separate failures — they missed the argument, and separately they missed the man. The Chinese names one failure five times.

**Two supports.** *"Easy to know"* is idiomatic English about **people** ("she's easy to know"); applied to words it is faintly odd, and the oddness quietly makes the words person-like — which is what 言有宗 then says outright. And **Chapter 71 is built entirely out of 知** (知不知，上；不知知，病 — *"knowing not-knowing is highest; not knowing yet knowing is sickness"*). 70 and 71 are adjacent on purpose; an *understand* in 70 breaks the hinge before 71 is drafted.

### Ch 70 · 被 and 懷 are two different verbs, and the line is made of the difference

A pass through the last line rendered both as *wear*: *"wears coarse cloth, but wears jade against their chest."* The repetition flattens the only architecture the line has.

被 (*pī*) is **draped over the outside**. 懷 (*huái*) is 忄 (heart) inside 褱, a garment-graph — **held within the robe, at the breast**. A cloth word outside, a cloth word inside, and the jade between them. 河上公 reads it exactly so: 被褐者薄外，懷玉者厚内 — *"wearing coarse cloth is thin outside; holding jade is thick within."* **懷 takes a verb of carrying**, not of wearing.

*(A smaller open question in the same line: 而 is held as **"but."** 河上公's 薄外／厚内 treats the two halves as a **matched pair** describing one person rather than as a contradiction, which argues faintly for "and". "But" was kept for the reader's ear.)*

### Ch 71 · 不知知 renders toward the mouth, not the mind

**Every standard English reads the second half as self-deception** — *"not to know, yet think you know."* We read it as **profession**: *"not to know and to claim you know."* Three supports, in the tie-breaking order.

**The graph.** 知 (*zhī*) is 矢 (*shǐ* — an arrow) over 口 (*kǒu* — a mouth): speech that flies straight to the target. The word has a mouth in it before it has a mind in it.

**The commentary.** 河上公 inserts 言 (*yán* — to say) into *both* halves, which he did not have to do: 知道**言**不知，是乃德之上 — *"to know the Tao and **say** you do not know: this is the height of integrity"* — and 不知道**言**知，是乃德之病, *"not to know the Tao and **say** you know: this is integrity's disease."* On his reading the chapter is not about the limits of knowledge at all. It is about the gap between what you hold and what you profess.

**Internal consistency.** Ch 56 opens 知者不言，言者不知 — *those who know do not speak; those who speak do not know* — which is this chapter's first line with the 言 already in it. And Ch 70 ends with the sage carrying jade **against the chest** under coarse cloth. 河上公 closes his note on 71 with the same gesture and nearly the same verb: 夫聖人**懷**通逹之知，託於不知者 — *"the sage **carries** penetrating knowledge against the breast, and lodges it in not-knowing."* 懷 is the character Ch 70 ends on. **70 and 71 are one gesture, and the commentator says so.**

*The interior reading is not wrong and is not erased — it is named in the chapter's `## Notes`. English forces a choice here that the Chinese does not force; we chose the reading the evidence favors and the one a reader is least likely to already have.*

### Ch 71 · "sick of the sickness" — one English word for one Chinese word

**病病 is the chapter's whole engine**: the first 病 verbal, the second nominal. The literal gloss in the source table says *"recognizing the disease as a disease"* — cool, diagnostic, and wrong about the verb. 河上公 supplies the sense: 夫唯能**病苦**衆人有強知之病 — *"only because they are **pained and distressed by** the crowd having the disease of forced knowing."* 病苦 is to suffer over, not to classify.

**English "sick of" is the only construction that keeps one word doing both jobs**, and it happens to carry exactly 病苦's sense of being wearied and pained by a thing. **Cost, logged:** *"sick of"* can read as impatient — sick of your nagging. The context defuses most of it, and the alternative (*troubled by the trouble*, *pained by the sickness*) either breaks the doubling or loses the body. 病 is 疒 (*nè* — a person lying against a bed-plank) over a phonetic; *Shuowen* has it as 疾加也, illness intensified. There is a body in this word and the English must keep it.

**Do not vary the repetition — but distinguish two kinds of it.** 病 falls seven times in four lines. Every instinct of English prose style wants to alternate *sickness / ailment / affliction*; the Chinese hammers one syllable, and the hammering is the argument. **That lexical repetition is kept entire.**

**The structural repetition is not.** The last line is 聖人不病，以其病病，是以不病 — literally **A, because B, therefore A.** Classical Chinese closes a period by restating its opening; English carries the conclusion inside the causal clause already, so *"the sage is not sick because they are sick of the sickness"* says the whole line. **Shalom cut the trailing 是以不病 (2026-08-24)** as an editorial redundancy, and it is one: nothing in the sense is lost, and the cut leaves the last two lines in exact chiasmus — *sick of the sickness → not sick*, then *not sick → sick of the sickness* — which is the shape the Chinese has underneath the padding.

*Recorded because it is a **cut**, not a rendering. 河上公 lemmatizes both halves, so the doubled text was in place by the Han and this is our edition's decision, not a witness's.*

**And 不病 stays flat.** A pass rendered 是以不病 as *"do you become no longer sick"* — six English words for two characters, carrying a **recovery arc** the Chinese does not have. 河上公 reads the line the other way: 是以**不自病**也, *"therefore they do not sicken themselves."* He adds 自 (*zì* — self). The cure is **not contracting it**, not getting over it, and "no longer" points backward at an illness the commentary says was never caught. Held at *"are you not sick"*, which also keeps the last two lines in exact chiasmus.

### Ch 72 · 大威 is not a bigger stick

**The standard English makes this line a threat**, and our own source table's literal gloss invites it: 民不畏威，則大威至 → *"when the people do not fear authority, then great authority arrives."* Read that way the chapter opens by telling a ruler that a larger power is waiting to enforce what theirs cannot — which is precisely the theology-of-office this edition exists to strip out.

**Both commentators read it as collapse.** 王弼: 民不能堪其威，則上下大潰矣，天誅將至 — *"the people cannot bear that dread; then high and low collapse utterly, and the reckoning of nature is coming."* 河上公, flatly: 威害也…大害至，謂死亡也 — *"威 means harm… the great harm arrives, meaning death."* Neither has anything arriving to enforce the ruler's will. **What arrives when your dread stops working is the end of the arrangement.**

**The English gives the first 威 an owner and leaves the second unowned** — *"when the people no longer fear **your** dread, **the** great dread arrives"* — because that asymmetry is the sentence. One dread belongs to somebody. The other does not belong to anyone, which is why it cannot be used.

**One character, two referents — so the English splits the word.** 威 (*wēi*) is 戌 (a great axe) over 女: the fear a figure commands and the figure commanding it, in one word. 王弼 glosses the ruler's 威 as **威權** (*wēiquán* — awe-power, **authority**) and the second as **天誅** (nature's reckoning). The Chinese runs one word through both slots and the shock is that the two are *not the same thing*; English cannot hold that in one word without asserting something false, so it renders *authority* / *the great collapse* and lets the difference be audible. The noun comes from 王弼's own gloss: 上下**大潰**矣, where 潰 (*kuì*) is a **dyke bursting**. A collapse answers to nobody, which is exactly the property the second 威 has and the first does not.

*A draft that kept the repetition — "when the people no longer fear **your dread**, the great dread arrives" — was killed by Shalom. You fear a thing; dread is the feeling. 畏威 works in Chinese and "fear dread" does not work in English, and the repetition was not worth the sentence. Also rejected, from the other direction: **"true authority arises"**, which makes 大威 a legitimate power replacing an illegitimate one. That is a larger inversion than the threat-reading it was meant to fix, and it is what the hymn test is for — the line would sit very comfortably in a sermon.* **Overlay watch:** 王弼's 天誅 is 天 (*tiān* — sky, nature) plus 誅 (*zhū* — to condemn, to execute) — **nature's reckoning**, not divine punishment. The pull toward "Heaven's judgment" is strong here and it is strongest in the commentary, where no checker is looking.

### Ch 72 · 厭 is a pun, and English happens to have the same one

厭 (*yàn* / *yā*) is 甘 (sweet) over 肉 (meat) under 厂 (a cliff): **sated with rich food**, hence *fed up with, sick of*; and by way of the cliff-graph it is the ancestor of 壓 (*yā* — to press down, to crush). One character, both senses live.

夫唯不厭，是以不厭 uses both in six characters: *do not press them down, and they will not be fed up with you.* 王弼 spells the second one out — 不自厭，是以天下莫之厭, *"does not make themselves loathsome, therefore no one in the world loathes them."*

**"Oppress" carries the pressing half exactly** — *ob-premere*, to press against — and it is the plainer, more pointable word. But the second 厭 is **not pressure, it is loathing**, and 王弼 spells it out: 不自厭，是以天下**莫之厭**, *"therefore no one in the world loathes them."* So the two halves take two Englishes: *when you do not oppress them, they will not tire of you.*

**Ch 66 fixes the second half** and the two chapters are twins: 是以天下樂推而不厭 → *"the world gladly pushes them forward and never tires of them"*, sitting directly under 聖人處上而民不重 — *the sage stands above and the people are not weighed down.* Ch 53's 厭飲食 → *"gorged on food and drink"* holds the root sense of the graph.

**"When", not "because" — and the cost is 唯.** Chs 2, 8 and 22 all render 夫唯…是以 as *"Because…"*, and a fourth is a tic; Shalom moved this one to *"when"*. What that drops is 唯 (*wéi*), 隹 (a short-tailed bird) beside 口 (mouth) — **solely, and nothing else**. 河上公 will not even leave it at one exclusive: he writes 夫唯**獨**不厭精神之人, stacking 獨 (*dú* — alone) on top of 唯. Without *only*, the line can be heard as a prediction rather than a mechanism. Logged as a known loss rather than repaired, because *"only when you do not oppress them do they not tire of you"* buys 唯 back at the price of a clanking double-negative inversion, and this chapter's other lines are plain.

*A draft rendered both with "weary" — "only when you do not weary them do they not weary of you" — on the grounds that one English word should do the work of one Chinese character. It bought the doubling at the price of "weary what gives them life", which is not a thing English does to a livelihood. **Two accurate words beat one clever one.***

**Second chapter running on the same device.** Ch 71: 夫唯病病，是以不病. Ch 72: 夫唯不厭，是以不厭. In both, a doubled character does two jobs and the English survives only by finding one word with two senses — *sick of the sickness*, *weary of you*. Worth watching for in 73–81 rather than being surprised by it again.

### Ch 72 · "loves themselves and does not hold themselves precious"

自愛，不自貴 turns on a distinction English usually blurs. 貴 (*guì*) sits on 貝, a **cowrie shell** — it means *costly* before it means *honoured*, and ch 70 already renders it *precious*. **You can love a thing without pricing it.** That is the line, and it is the answer to the chapter's first half: a ruler who has set their own price high has to keep collecting on it, which is what the crowding is.

*Not "exalt" — ch 3 already spends that word on 尚 (尚賢, "exalting the exceptional"). 河上公 splits the pair cleanly: 自愛其身以保精氣也 (bodily — preserving vital essence and energy) against 不自貴高榮名於世 (social — glory and fame).*

**故去彼取此 names its axis.** Ch 12 (*"rejects the hungry gaze, chooses gut wisdom"*) and ch 38 (*"rejects surfaces and embraces life's thickness"*) both fill in the referents. A draft here left *that* and *this* bare instead, on the grounds that the referents sit in the line immediately above and 河上公 spells them out: 去彼**自見自貴**，取此**自知自愛**. Shalom killed it for a structural reason: the preceding line carries **four** items, and English *that/this* cannot sort four things into two pairs.

**The characters supply the sorting principle, and it is spatial.** 彼 (*bǐ*) is 彳 (a step) beside 皮 — *yonder, over there*. 此 (*cǐ*) is *this, here*. And the axis is exactly the right one: 自見 (display) and 自貴 (self-pricing) **require an audience** — they are out there. 自知 (knowing) and 自愛 (loving) require nobody — they are here. Hence *"they let go of what is out there and take what is here."*

Keeping **here** also holds the chapter inside the 以此 thread that closes chapters 21, 54 and 57 — *how do I know it is so? By this* — which a bare "this" was carrying but not communicating. See `DISCOVERIES.md` §2.
