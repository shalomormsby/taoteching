# RETROFIT — consistency debt

*Terms settled later in the book oblige changes to chapters drafted earlier. **Policy: fix on discovery, not in a deferred batch.** Mechanical term-swaps are applied immediately; lines needing a rewrite are proposed first, then applied.*

**Status: swept 2026-08-10 by hand; re-checked 2026-08-11 by `tools/check_locks.py`, which found nine more.** The hand sweep was very nearly right, and the near-miss is the argument for the tool: Ch 53 rendered 大道 (*dà dào* — "the great Tao") as *"the great Way"* one line below rendering it correctly, in a chapter carrying `retrofit: []`. **1 mechanical fix applied; 8 open items below need your call, plus the 1 literary question.**

Each chapter file carries its own debt in frontmatter (`retrofit: [...]`), regenerated after every sweep, so this file and the chapters cannot drift apart.

---

## Open — needs your call

*The eight below were found by `tools/check_locks.py` on its first run, 2026-08-11, inside the 61 chapters the 2026-08-10 sweep certified clean. Ch 53's "The great Way" → "the great Tao" was mechanical and is already applied. These eight need rewrites, so they are yours to rule on. Each is a live `error` — the build stays red until they are resolved or waived.*

### Ch 23 · "When integrity is weak, the system winds down" — the wrong word and an overlay

This renders **信不足焉，有不信焉** (*xìn bù zú yān, yǒu bù xìn yān* — "trust is insufficient, so there is distrust"). Two problems, and the first is serious:

- **信** (*xìn*) is **trust**, not 德 (*dé* — integrity). The line borrows the lock word for a different character, which makes 德 look inconsistent across the book and loses the chapter's actual subject.
- **"the system winds down"** is invented, and mechanistic. There is no 器 (*qì* — vessel) or any machine here.

**Ch 17 renders the identical Chinese correctly:** *"When leaders don't trust the people, no one trusts the leaders."* **Recommendation: bring 23 to 17's rendering,** or a shortened form of it. *(Found by the `repeated-formula` rule — the two chapters share the segment verbatim.)*

### Ch 21 · "the unerasable source code of all creation" (×2) — the mechanistic overlay, live

Renders **以閱眾甫** (*yǐ yuè zhòng fǔ* — "thereby to observe the origin of the multitudes") and **吾何以知眾甫之狀哉** (*wú hé yǐ zhī zhòng fǔ zhī zhuàng zāi* — "how do I know the condition of the origin of the multitudes?"). 甫 (*fǔ*) is *origin/father*; 眾 (*zhòng*) is *the multitudes*.

"Source code" is `CLAUDE.md`'s named besetting temptation, and it almost certainly leaked from `process/legacy-tao-source-code.md`, which is archived precisely because it holds superseded renderings. **Recommendation: "the origin of the countless things"** or "where everything begins" — and check whether other legacy renderings came across with it.

### Ch 29 · "The world is a sacred system" — 器 is a vessel

**天下神器** (*tiān xià shén qì* — "the world is a sacred vessel"). 器 (*qì*) is already locked to **vessel / tool** inside `glossary/pu-樸.md`. **Recommendation: "the world is a sacred vessel"** — near-mechanical, but it changes an image, so it is yours.

### Ch 29 · 為 rendered "force" three times in four lines — pre-lock, and it now clashes with Ch 64

*Opened 2026-08-14, drafting Ch 64.*

Ch 29 carries **為者敗之，執者失之** verbatim with Ch 64 — `concordance.py --formulas` flags both segments — and renders it *"Those who force it ruin it. Those who grasp it lose it."* The same "force" also stands in for 為 at 將欲取天下而**為**之 (*"those who wish to force their will upon the world"*) and at 不可**為**也 (*"It cannot be forced"*).

為 (*wéi*) is locked to **do / handle / serve as** (`glossary/wei-為.md`) — a hand on an elephant, handling rather than neutral doing. "Force" is not on the forbidden list, but it is a *reading* smuggled in as a translation: it supplies the violence that 為 only implies, and it makes 無為 (non-doing) look like a counsel against aggression rather than against handling as such. Ch 64 now reads **"Those who handle it ruin it. Those who grasp it lose it."** The shared formula must not read two ways.

**Recommendation: sweep all three to 為's own word** — *"those who wish to take the world in hand and handle it"*, *"it cannot be handled, it cannot be grasped"*, *"those who handle it ruin it."* Not mechanical: line 1 needs restructuring and line 1 also carries an em-dash on the watchlist. **Proposing, not applying.**

### Ch 28 · 谷 rendered "reservoir", and 谿 as "deep ravine" — surfaced drafting Ch 66

*Opened 2026-08-17.*

Ch 66 renders 谷 (*gǔ*) as **valley** — 百谷王, "king of the hundred valleys" — which is the character's plain sense and what ch 15 (若谷) and ch 32 (川谷) already carry. **Ch 28 renders the same character as "reservoir"**: 為天下谷 → *"Embody the reservoir of the world."* A reservoir is built, holds by design, and is a *vessel*; a valley is a shape the land takes and holds by being low. This chapter's whole argument is that lowness gathers **without** contrivance, so "reservoir" quietly answers the question the term exists to raise.

Two other renderings in Ch 28 look pre-lock in the same way and should be checked together: **谿** (*xī* — mountain stream, ravine) as *"deep ravine"*, and 官長 as **"master orchestrator"** with 大制不割 as *"the great orchestrator itself does not carve"* — *orchestrator* is close to the mechanistic register `CLAUDE.md` names as our besetting temptation, and 器 is locked to *vessel / tool* one line above it.

**Recommendation: review Ch 28 as a chapter**, not as three term-swaps — the lines are load-bearing and 雄/雌 (rooster/hen, currently *"assertive energy" / "yielding energy"*) needs deciding at the same time. **Proposing, not applying.** 谷 also wants a glossary entry; it appears in 7 chapters.

### 智 is rendered four ways across five drafted chapters, and "cunning" covers four characters

*Opened 2026-08-17, drafting Ch 65.*

**智** (*zhì* — 知 *know* over 日 *sun*) appears in six chapters. The drafted ones do not agree:

| Chapter | Chinese | rendered |
|---|---|---|
| ch 3 | 使夫**智**者不敢為也 | "the **cunning**" |
| ch 18 | **智**慧出，有大偽 | "**cleverness** and erudition" |
| ch 19 | 絕聖棄**智** | "**cleverness**" |
| ch 33 | 知人者**智** | "**intelligent**" |
| ch 65 | 以其**智**多 | "**guile**" *(settled 2026-08-17)* |

And **"cunning" is doing duty for four different characters** — 知 and 智 in adjacent lines of ch 3, 巧 in ch 57 (人多伎巧), and a fourth in ch 58. That is the 眾人/俗人 fault at book scale, and no rule can catch it: each rendering is defensible for its own character.

**Some of this spread is legitimate.** 智 genuinely runs from *wisdom* (ch 33, where it is the lesser term against 明's clear-seeing) through *cleverness* (ch 19, attacking a Confucian virtue) to *artifice* (ch 65, where both commentators gloss it 巧詐/巧偽). A licensed split, like 事. What is **not** legitimate is that it happened by accident, chapter by chapter, with no decision anywhere.

**Recommendation: 智 wants a glossary entry, and it should be taken together with 知 (*zhī* — to know), 明 (*míng*, already locked), and 巧 (*qiǎo*).** Those four form the book's entire epistemology and three of them are currently unlocked. Ch 3 is the urgent repair — one English word for 知 and 智 in consecutive lines makes the distinction invisible exactly where the chapter is drawing it. **Proposing, not applying.**

### Ch 18 · 孝慈 loses 慈 entirely, and Ch 19 renders it "love" — surfaced drafting Ch 67

*Opened 2026-08-19.*

孝慈 (*xiào cí*) is a directional pair: **孝** is the child's devotion **up** to the parent, **慈** is the parent's love **down** to the child. Our two drafted chapters treat it unevenly:

- **Ch 18** — 六親不和，有**孝慈** → *"When families are out of harmony, filial piety appears."* **慈 is dropped.** Half the compound is simply not in the English, and it is the half this edition should least want to lose.
- **Ch 19** — 絕仁棄義，民復**孝慈** → *"the people will return to the natural expressions of filial piety and love."* 慈 becomes *love*, which is not wrong but carries none of the direction.

Ch 67 settles 慈 as **tenderness** (see the Translation Notes), on the strength of 河上公's 愛百姓若赤子, *"loving the people as newborn infants."*

**Recommendation: 孝慈 → "devotion and tenderness" in both**, which keeps the pair legible as a pair — the child's devotion, the parent's tenderness. Ch 18 needs the words restored, not swapped, so it is a rewrite. **Proposing, not applying.** 慈 also wants a glossary entry: three chapters, seven lines, and it is the book's most explicit statement of the feminine at the centre.

### 恃 rendered "presume" in three chapters, and it means "rely on" — surfaced settling 敢

*Opened 2026-08-20.*

恃 (*shì*) is 心 (heart) beside 寺 — **to rely on, to lean on, to depend upon.** Our own source tables gloss it that way in every chapter it appears, and Ch 34 requires it: 萬物**恃**之以生 — *"the countless things **rely** on it to live."*

But the drafted verse renders 為而不恃 as **"does not presume"** — Ch 2's *"The sage acts, but does not presume"*, and Ch 10 and Ch 51's *"acting without presuming."* That is a reading, not a translation: *presume* names an attitude where 恃 names a dependency. The line says the sage acts **and does not lean on what they did** — does not take the deed as a support, a credit, a claim. Ch 51's own neighbours make the shape plain: 生而不有 (bears without possessing), 為而不恃, 長而不宰 (raises without ruling). Three refusals of *holding on*, not three refusals of arrogance.

**And it has a live cost.** *Presume* is the precise English for 不敢 (*bù gǎn*), which `gan-敢.md` has just had to route around — 敢 is the forward press to take, and *"would not presume"* is exactly the register of 不敢高攀 and 愧不敢當. 恃 is holding a word it does not need and 敢 does.

**Recommendation: 恃 → "lean on" or "rely on" across ch 2, 10, 51**, which frees *presume* for 敢 and makes Ch 34 consistent with the other three. Not mechanical — the lines are compact and 為而不恃 sits inside a triple in Ch 51. **Proposing, not applying.** 恃 also wants a glossary entry; it appears in five chapters and pairs naturally with 有 (possess) and 宰 (rule) in Ch 51's triple.

### Ch 15 · 古之善為士者 → "The ancient masters" — the same construction as Ch 68, rendered differently

*Opened 2026-08-20, drafting Ch 68.*

Ch 15 and Ch 68 open on the **identical four characters** — 善為士者, *"one masterful at being a 士"* — and our English shares nothing between them. Ch 68 now reads *"One masterful as a warrior"*; Ch 15 reads **"The ancient masters"**, which drops 善為 (*masterful at being*) altogether and renders 士 as *masters*.

Three problems, in order of size:

1. **士 (*shì*) is not "master."** It named the **warrior-retainer class** of the Zhou, drifting later toward the scholar-official. 王弼 defines it flatly at Ch 68: 士，卒之帥也 — *"士 is the commander of troops."* Ch 41's 上士/中士/下士 are men of rank hearing the Tao. None of them is a master of anything.
2. **"Masters" sits next to a forbidden word.** `CLAUDE.md` bars *"the Master"* as a rendering of 聖人; lowercase *masters* for a different character is not the same breach, but it puts the register the lock exists to keep out back into the book two chapters before 聖人 appears.
3. **善為 vanishes.** The 善 lock is *masterful at*, and the phrase is *masterful at being* — which is what makes Ch 68's paradox work and what Ch 15 spends the rest of its lines describing.

**Ch 15 also carries an em-dash** on the typography watchlist, in the very next line.

**Recommendation: review Ch 15 as a chapter**, not as a term-swap. 士 wants a glossary entry at the same time — three chapters, five lines, and the register runs from soldier to gentleman. **Proposing, not applying.**

### Ch 40 · "Yielding is the Tao's function" — 用 is use

**弱者道之用** (*ruò zhě dào zhī yòng* — "yielding is the use of the Tao"). 用 (*yòng*) is locked to **use** inside `glossary/wu-you-無有.md`, and "function as" is on 為's forbidden list. **Recommendation: "yielding is how the Tao is used"** or "yielding is the Tao at work."

### Ch 25 · "Within this system of four vast things" — 域 is a realm

**域中有四大** (*yù zhōng yǒu sì dà* — "within the realm there are four great things"). 域 (*yù*) is a *domain/territory*, not a system. **Recommendation: "within the realm there are four great things."**

### Ch 14 · "And returns to nothingness" — 無 is absence

**復歸於無物** (*fù guī yú wú wù* — "returns to no-thing"). "Nothingness" is explicitly forbidden for 無: it imports the Void as a metaphysical substance, where 無 is simply *absence*. **Recommendation: "and returns to no-thing"** — which keeps 物 (*wù* — thing) audible and the 無/有 pair intact.

### Ch 14 · "direct your present existence" — 有 is presence

**以御今之有** (*yǐ yù jīn zhī yǒu* — "thereby to steer what is present now"). "Existence" is forbidden for 有. **Recommendation: "to steer what is present now."**

### Ch 2 · "the sage's work endures eternally" — not a violation, but loose

There is **no 常 in this chapter** — the line renders 夫唯弗居，是以不去 (*"precisely because they do not dwell in it, it does not depart"*). So "eternally" breaks no lock. But it asserts permanence where the Chinese says something subtler and more conditional: the work stays *because* the doer does not stay with it. Worth revisiting on literary grounds, not lexical ones.

---

## Swept ✅ — 2026-08-10

| Term | → | Chapters fixed |
|---|---|---|
| **樸** | uncarved wood *(lowercase)* | 15, 19, 28, 32, 37 — plus 2 dependent lines in 32 |
| **萬物** | **the countless things** *(re-locked; see below)* | 1, 2, 4, 8, 10, 16, 32, 34, 37, 39, 40, 41, 42, 51 |
| **天地 / 天下 / 天** | sky and earth · the world · nature | 7, 9, 10, 22, 23, 25, 32, 37, 39, 40, 47, 59 |
| **玄** | dark · profound | 4, 6, 10, 15, 51, 65 |
| **常** | the ever-present | 16, 34, 46 |
| **一** | lowercase *the one* | 10, 22, 39, 42 |
| **明** | clear-seeing · clarity | 33, 36, 52 |
| **無為** | non-doing | 37, 43, 48, 57 |
| **無 / 有** | absence / presence | 2, 40 |
| **自然** | of itself / of themselves · so of itself | 23, 25 |
| **義 / 仁** | duty · humaneness | 18, 19, 38 |
| **知足** | knowing you have enough | 33, 46 |
| **天** (Ch 16 ladder) | the open sky | 16 — see below |

**萬物 re-locked as "the countless things"** *(was briefly "the ten-thousand things")*. 萬 is a **scorpion** borrowed for its sound — the quantity is a phonetic accident, and 萬 meant *beyond reckoning*, which "ten thousand" now inverts for a reader who knows the scale of the universe. Rejected: *"all things"* (a totality where 萬物 is a teeming plurality) and *"beings"* (imports Buddhist 眾生, over-narrows to inner life, and collides with the "Being/Non-Being" rendering already rejected for 有/無). *Ruling: `glossary/wanwu-萬物.md`.*

**Three corrections the verification pass caught:**

> **ch 30 / ch 55** — 物壯則老 is **verbatim in both** and was rendered two different ways. Now identical in both: *"When things reach their peak strength, they decay."*
> **ch 25** — "All matter was formed from the formless" → *"**Something** formed in the undifferentiated."* 有物混成 says *there is a **something***, singular and indefinite — not "all matter," which makes it plural and material and quietly turns the pre-cosmic Tao into stuff.
> **ch 10, 41** — both contained "the ten-thousand things" where the Chinese has **no 物 at all** (生之畜之 in 10; 善貸且成 in 41 — the object is only the pronoun 之, *them*). Swept for consistency, but flagged: the noun is **supplied by the translator**, not present in the source.

**Ch 16's ladder, resolved.** 王乃天，天乃道 now reads *"Sovereignty leads to the open sky. / The open sky leads to the Tao."* Two constraints decided it: Ch 16 and Ch 25 share this exact 天→道 step, so both must say **sky**; and the passage is *anadiplosis* (each line ends on the word the next begins with), so the qualifier had to repeat rather than be introduced once and dropped. **公 was corrected in the same pass** — "equanimity" → **"impartiality"** (公 is the opposite of 私, *private/selfish*), which makes the whole ladder legible as one continuous widening beyond the self. *Logged in `notes/translation.md` and `notes/reading.md`.*

**Also corrected in passing:** Ch 36's "the tools of nature" → *"the sharp instruments of the state"* (國之利器 — 國 is the **state**; "nature" was simply wrong). Ch 22's "therefore is eternal" → *"therefore endures"* (長, not 常). Ch 7's whole opening — 天長地久 is 長/久 (*lasting/enduring*), not 常.

---

## Lessons for `tools/check_locks.py` — now built (2026-08-11)

*All three below are implemented, and each has a test in `tools/tests/test_check_locks.py` named after it. Three further lessons the build itself taught are at the foot of this section.*

Three failure modes this sweep exposed. Build the checker against them:

1. **Match stems, not whole words.** `\beternal\b` misses "eternal**ly**" — which hid two chapters. Use `eternal`, `everlast`, `illuminat`, `righteous`.
2. **Case-sensitivity cuts both ways.** A case-insensitive scan flags "the one" (correct) as "the One" (wrong), and a case-sensitive one misses "The cosmos" at the start of a line. The checker needs per-rule case policy, not one global flag.
3. **Homophones and false friends are the real trap.** 常 (*cháng*, constant) vs 長 (*cháng*, long); 自然 (*of itself*) vs the ordinary English word "nature"; 一 (*one*) vs the English pronoun "one"; "Block the openings" (塞) vs "uncarved block" (樸). **Every flagged line must be verified against the Chinese in its own chapter before it is changed** — roughly a third of this sweep's initial 93 flags were false positives.

## Open debts

**事 (*shì* — affair, matter; to attend to) wants a glossary entry, and 無事 is rendered two ways.**
Ch 48 and Ch 57 render 無事 as **"non-interference"**; Ch 63 renders it inside the triple 為無為，事無事，味無味 as **"tend the not-tending"**. Both are defensible where they stand — 48 and 57 use it as a standalone noun phrase, 63 needs a monosyllabic verb to hold the parallel — but the divergence is unlogged in the glossary because 事 has no entry. Raised drafting Ch 63, 2026-08-11. Not urgent; it becomes urgent the moment 事 is locked. Ch 64 also carries 無事-adjacent material and should be drafted with this open.

**Ch 34 and Ch 63 share 故能成其大 and do not chime.**
Ch 34 renders the formula *"Making no effort to appear great, / The Tao shows true greatness"* — which drops 成 (*chéng* — to complete, accomplish) entirely. Ch 63 renders *"So the sage never does the great, / and so completes their greatness."* The subjects differ (the Tao vs the sage) and the surrounding Chinese differs (以其終不自為大 vs 是以聖人終不為大), so this is not automatically an error — but `repeated-formula` will flag it, and Ch 34's line is the weaker of the two. Worth a look when Ch 34 is next open.

**~~Ch 27 · 無棄人 softened to "no one is lost"~~ — CLOSED 2026-08-12.**
Applied with Shalom's approval, and the fix was larger than the debt: the couplet had also lost 救 (*jiù* — rescue) to *"drawing in"*, 物 to *"entities"* (its only occurrence in the verse), 襲明 to *"innate clarity"* against the 明 glossary's own ruling, and 常 (always) entirely. Now: *"Therefore the sage is always masterful at rescuing people, and so no one is abandoned."* Reasoning in `notes/translation.md` → Ch 27; the cross-chapter argument is a new Thread in `notes/reading.md`.

**~~善 rendered two ways~~ — CLOSED 2026-08-14.** Entry written (`shan-善.md`) and **Ch 49 resolved**: 善 is locked as *masterful* for the skill sense, for 善人/不善人 at 27, 49 and 62, and as the verb *count as masterful* at 49; *good* is kept only where the text names the category (2, 20, 58). Ch 79 (常與善人) and Ch 81 (善者不辯) inherit this when drafted. **Still open: 上善若水** (8) reads *"Supreme goodness is like water"* above eight lines of pure competence, and may want *the highest excellence*.

**`tools/import_commentary.py` mis-splits chapters when a chapter heading sits mid-block.**
Wang Bi's commentary on Ch 62 is in the repo but filed inside `sources/commentaries/wangbi/061.md`, because the Siku printing runs 62 on into 61's block behind the heading 六十二章. `--commentary 62` therefore reports it *not vendored*, and 62 is listed among the ten "unproofread" chapters when in fact its text is present and complete. Worth auditing the other nine (8, 14, 15, 19, 30, 54, 70, 71, 78) the same way before assuming any of them is missing. Raised drafting Ch 62, 2026-08-11.

**公 (*gōng*) is rendered three ways in three chapters and has no glossary entry.**
Ch 16 renders 公 as **impartiality** (容乃公，公乃王), which is what the character says — 八 (to divide) over 厶 (private, self); *Shuowen*: 公，平分也, "fair division." Ch 42's 王公 reads *"kings and lords"*. Ch 62's 三公 reads *"the three ministers"*. All three are defensible in place and none of them know about the others. When 公 is given an entry, Ch 42 and Ch 62 must answer to Ch 16. Raised drafting Ch 62, 2026-08-11. Related: 王 (*wáng*) is itself unsettled — see the "reading past the throne" thread in `notes/reading.md`.

**~~Ch 48's closing stanza~~ — CLOSED 2026-08-12.** Two Chinese lines had been rendered four times; the superseded draft was deleted and the couplet's 取天下 frame and 無事/有事 hinge restored.

**~~無事 rendered two ways~~ — CLOSED 2026-08-12.** Resolved as a **licensed split**, not a single token: **meddle** at 48 and 57, where 無事 names a policy and stands alone; **serve** at 63, where 事 appears twice in one line and the verb must be neutral for the paradox to work. The lock on 事 is on its register, never a single English word. See `glossary/shi-事.md`.

**~~Ch 31 · 吉事/凶事 as "processes"~~ — CLOSED 2026-08-12.** Repaired, along with three further inventions in the same three lines. `"processes"` is now armed in 事's `forbidden:` list.

**無事 is rendered two ways and the entry recommends one.** *"Non-interference"* at Ch 48 and Ch 57; *"tend the not-tending"* at Ch 63. `glossary/shi-事.md` recommends making Ch 63's word the standard, on the strength of Ch 57's quartet, where 無事 is the only member that is not a plain statement. Not applied: the sweep touches drafted verse in two chapters, one of which (48) needs separate repair first.

**~~Ch 7 · 故能成其私 missing~~ — CLOSED 2026-08-12.** The line is restored as *"And so their private self is fulfilled"*, with the question frame put back in the line above it and 身存 corrected from *"their spirits endure"* to *"their selves endure"*.

**私 (*sī*) is rendered two ways and shelters under 公's `covers:`.** *"Private self"* at Ch 7 (settled 2026-08-12) and *"the self"* at Ch 19 (少私寡欲 → "Diminish the self, diminish desire"). Ch 19's is arguably right in place — 私 beside 欲 wants a short word — but 私 is load-bearing enough for the 公 argument that it may want its own entry rather than a `covers:` line.

**Solved by the evidence gate.** Because every chapter file carries its own Chinese, a rule never fires on English alone: "virtue" is an error only when 德 is in *that* chapter's source rows, and otherwise drops to `info` in a separate false-friends list. On the first run this took the error list to **9 findings with zero false positives**, from a naive scan's 20.

Three further lessons, from building it:

4. **A forbidden string already encodes its own case policy.** `"the Way"` written with a capital means the capital *is* the violation — so *"the way of nature"* (ch 9, 47) is fine. `"eternal"` written lowercase means the word in any case, which is what catches "eternally". Deriving the policy from how the decision was written cleared six false positives on "Being" (the participle: *"being still"*, *"their being"*) and needed no new configuration.

5. **Phrase rules and register rules catch different things; keep both.** Ch 53's *"The great Way"* slips past the forbidden phrase `"the Way"` because *great* breaks the string. The `devotional-capitalization` rule watches the bare capitalized word and catches it. Neither rule subsumes the other.

6. **Do not try to align the verse to the source rows.** Only 27 of 62 drafted chapters have verse lines matching source rows one-to-one, and the literal glosses speak **pre-lock** English — 玄德 is glossed "dark/mysterious virtue/power" where the verse correctly reads *"profound integrity"* — so matching a locked term against its own gloss fails exactly where the locks matter most. The `repeated-formula` rule therefore asks an alignment-free question: two chapters sharing a verbatim Chinese segment should have *some* pair of similar lines. If their closest pair still looks nothing alike, it says so. This is how ch 23's 信不足焉 was caught.

### Ch 16 · 復命 → "your original nature" — loose, and it borrows another character's English

`concordance.py --english "nature"` shows nine lines. Seven render 天 (*tiān*) as an agent, which is the settled split. **Two do not:** Ch 16's 是謂復命 and 復命曰常 both read *"returning to your original nature."*

復命 (*fù mìng*) is **returning to the mandate / the allotted course** — 命 (*mìng*) is what is commanded or apportioned, the same character as in *destiny*, not an inner essence. *Original nature* imports a self that was there before and can be recovered, which is closer to 性 (*xìng*) than to 命, and it spends the English word this edition reserves for 天.

Not swept, because it is a rewrite of two lines in a drafted chapter and the surrounding movement (歸根 → 靜 → 復命 → 常 → 明) has to hold together. **Shalom's call.**

### Ch 68 · 配天 — the chapter and its own note disagree

是謂配天，古之極 — *"this is called being 配 (pèi — matched, as one of a pair) with 天, the utmost of the ancients."*

`chapters/068.md` reads **"partnered with the sky."** `notes/translation.md` records the decision as **"matched with nature."** Both cannot stand.

The evidence pulls both ways, which is why it is here rather than swept. 河上公 glosses the line by **expanding 天 to the pair** — 能行此者，德配**天地**, *"one who can do this, their integrity is matched with sky and earth"* — and the split locked in `glossary/tian-天.md` sends 天 to *sky* whenever 地 is in the series. But nothing here is matched **spatially**: what is matched is a person's 德 (*dé* — integrity) against a standard, which is the agent sense, and the agent sense takes *nature*.

**Shalom's call.** It is the single contested line for the 天 split.

### Ch 16 · "Each returns energy to its root" — 氣 is not in this chapter

各復歸其根 is *"each returns to its root."* There is no 氣 (*qì*) in Chapter 16 at all — `concordance.py --english "energy"` shows four lines carrying the word, and only Ch 10 (專**氣**致柔) and Ch 55 (心使**氣**曰強) have the character to license it.

**Also flagged in the same run: Ch 28's *"assertive energy" / "yielding energy"*** for 知其**雄**，守其**雌** — 雄 (*xióng*) and 雌 (*cí*) are a **rooster and a hen**. Rendering the book's central feminine image as an abstract polarity of energies is a live cost, and 雌 is load-bearing for the feminine thread. **Both are Shalom's call**, as they are rewrites rather than swaps.

### 民 and 人 — the whole book at once, deliberately deferred to a holistic pass

**Raised 2026-08-25 at Ch 74, and parked by Shalom for a single decision across all 81 chapters rather than chapter-by-chapter drift.** Ch 74 reads *"the people"* in the meantime; that is a hold, not a settlement.

**Two characters, and English has been treating them as one word.**

- **民** (*mín*) — the **governed**. The graph is an eye pierced by a blade: a subject population, no dignity implied. Always the counterpart of a ruler.
- **人** (*rén*) — a **person, a human being**. The graph is a standing figure in profile. No political relation at all.

**Where it stands today.** 民 appears in 13 chapters, 32 lines, and renders **"the people" in every one of them** — consistent, unlogged, and never argued for. 人 renders inconsistently, and Ch 57 does both **two lines apart**:

- 人多利器，國家滋昏 → *"The more sharp weapons **the people** have, the darker the state becomes."*
- 人多伎巧，奇物滋起 → *"The more cunning **people** become, the more strange contrivances appear."*

Same character, same chapter, two Englishes. That one is ours and it is a genuine drift.

**What is actually at stake, and it is not tidiness.**

1. **Structural rhymes across chapters.** Ch 72 opens 民不畏威 and Ch 74 opens 民不畏死 — the identical three-character frame, two chapters apart. *"When the people no longer fear authority"* and *"When the people do not fear death"* rhyme; drop the article from one and the pair goes silent. `notes/reading.md` builds a chain on that twinning (72 → 74 → 75). Any decision here has to check what else it breaks.
2. **河上公's second register.** He reads every chapter twice — 治國 (governing the state) and 治身 (governing the self) — and on Ch 74's opening line he does both. **"The people" bolts a line to statecraft; "people" lets a reader hear it about themselves.** This is the real argument for the bare noun and it is not a small one.
3. **Whether the distinction is worth an English marker at all.** *The people / people* is one available answer. It is not the only one, and it is doing the work with an article, which is thin.

**Why holistic and not per-chapter.** 民 and 人 run through the most political chapters in the book (3, 10, 17, 19, 32, 57, 58, 65, 66, 72, 74, 75, 80). A rule settled at one chapter propagates to twelve others and to the reading notes that depend on them. This is the shape of decision the glossary exists for.

**Ch 80 adds five more 民 lines to the pile (2026-08-26)**, all rendering *"the people"* on the same hold — and one of them, 使民重死, is load-bearing for the Ch 75 rhyme (民之輕死). Any settlement has to check that pair too.

**Owed:** a `glossary/min-民.md` entry (and very likely a 人 entry or a `covers:` on it), a full sweep, and a `notes/reading.md` pass on any cross-chapter rhyme the call disturbs. **Shalom's call, deferred by Shalom.**

## Ch 52 · 守柔曰強 — the one line the 弱 lock cost

**Raised 2026-08-26, held for Shalom.** Ch 52 currently reads *"To stay with the yielding is strength."* The character is **柔** (*róu* — soft), not 弱. Under the four-word table the 弱 lock forces — 柔 **soft** · 剛 **hard** · 弱 **yielding** · 強 **strong**, required because Ch 78 splits the compound at 弱之勝強，柔之勝剛 — 柔 cannot keep *yielding*.

Not swept, because it is a rewrite rather than a term-swap and the retrofit policy says propose first. *"To stay with the soft is strength"* is the mechanical answer and it is flatter than what is there. Candidates worth weighing against it: *"staying soft is strength"*, or a recast that keeps 守 (*shǒu* — to guard, hold fast to) doing real work, since 守 is itself a locked term (**hold fast to**) and the current line has already softened it to *stay with*. That second point makes this a two-character question, not one.

Also owed: `glossary/rou-柔.md`, which the 弱 entry currently absorbs via `covers:`.

## 恃 — *presuming* → *relying* — ✅ **DONE 2026-08-26**

Raised at Ch 77, settled the same day. 恃 (*shì*) is 忄 (heart) + 寺 — **the heart putting its weight on something**; *Shuowen*: 恃，賴也. *Presume* rendered an imagined attitude rather than the character. Locked as **rely on** in `glossary/shi-恃.md`, which fired as three build errors the moment it was written — the mechanism doing its job.

**Swept: ch 2, 10, 51** (為而不恃 → *acts yet relies on nothing*, one formula in place of three Englishes) **and ch 34** (萬物恃之以生 → *the countless things rely on it to live*, restoring the book's only positive 恃). Ch 77 was drafted correct.

*Not a candidate for `lean on`, though it is the truer picture: 倚 (*yǐ* — to lean against) already holds that word at Ch 58.*

## Ch 22 · the 不自X stanza — ✅ **DONE 2026-08-27**

**Raised at Ch 81, 2026-08-26; resolved the next day, and the chapter turned out to hold two larger errors than the one that opened the debt.** Full argument in `notes/translation.md` · Ch 22.

Ch 22 line: 不自是，故彰 — currently *"Does not debate, therefore is unrivaled."* Both halves are off the Chinese.

- **是 (*shì*) is not 辯.** 是 is *to affirm as right*; 自是 is **to hold oneself right**. *Debate* is the English for 辯 (*biàn* — words between two disputants), which does not occur in ch 22 at all. `concordance.py --english` cannot catch this yet because 辯 has no glossary entry, but it is exactly the class of error the `--english` direction exists to find: a rendering applied in a chapter where the licensing character is **absent**.
- **彰 (*zhāng*) is not "unrivaled."** 彰 is 章 (a pattern) with 彡 (strokes): **to show up plainly, to be distinct.** *Unrivaled* imports a comparison the character does not make.

**Complication that makes it a stanza-level fix, not a line-level one.** The line sits in a four-part parallel — 不自見故明 · 不自是故彰 · 不自伐故有功 · 不自矜故長 — and the first member currently reads *"The sage does not display self, and is therefore luminous."* That 明 (*míng*) is **locked to clear-seeing**, and *luminous* is emission, precisely the reading `glossary/ming-明.md` rejects. So the stanza owes at least two corrections, and they interact: the four 自 (*zì* — self) are one construction and should read as one in English.

**What was actually done.** All four 不自X lines rewritten as one construction, following 王弼's one-to-one mapping of the stanza onto the chapter's four opening paradoxes. *luminous* → **see clearly** (the `ming-明.md` entry had already decided this line; the verse was stale against its own glossary). *does not debate* → **do not insist they are right**. *unrivaled* → **their rightness shows**. *boast* → **claim the work** (河上公: 伐，取也). *takes pride* → **make themselves great** (矜，大也).

**And two larger errors surfaced in the same pass.** 誠全而歸之 had no English at all — the line read *"Try and see for yourself"* — which forced 曲則全 → *"Bend, and stay whole"* so the chapter's closing quote-back would land. And 抱一 was de-mystified to **"embraces one thing"** on 王弼's 一，少之極也, a per-chapter call recorded in the new `glossary/yi-一.md`.

**Two new debts opened by this chapter:**

1. **Ch 28 · 為天下式, twice.** Currently *"Embody the pattern of the world."* 式 (*shì*) is a carpenter's template, not a moral example, and ch 28's own next line proves it — 常德**不忒** (*tè* — to deviate off true) requires a standard to deviate from. Ch 22 now reads *"sets a pattern for the world."* Mechanical enough to sweep, but ch 28's three-fold 谿 / 式 / 谷 series means the parallel has to be checked before touching one member of it.
2. **Ch 24 · 自伐 → "boasts."** 河上公 glosses 伐 flatly as 取也, *"to take"* — so it is claiming credit, not bragging. Ch 22 now reads *claim the work*. Ch 24 is the negative twin of the same stanza (自見者不明，自是者不彰，自伐者無功，自矜者不長) and its other three members are already correct, so this is a one-word question, not a stanza. **Shalom's call.**
