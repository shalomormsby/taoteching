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
| **自然** | the self-so · of itself | 23, 25 |
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
3. **Homophones and false friends are the real trap.** 常 (*cháng*, constant) vs 長 (*cháng*, long); 自然 (*self-so*) vs the ordinary English word "nature"; 一 (*one*) vs the English pronoun "one"; "Block the openings" (塞) vs "uncarved block" (樸). **Every flagged line must be verified against the Chinese in its own chapter before it is changed** — roughly a third of this sweep's initial 93 flags were false positives.

## Open debts

**事 (*shì* — affair, matter; to attend to) wants a glossary entry, and 無事 is rendered two ways.**
Ch 48 and Ch 57 render 無事 as **"non-interference"**; Ch 63 renders it inside the triple 為無為，事無事，味無味 as **"tend the not-tending"**. Both are defensible where they stand — 48 and 57 use it as a standalone noun phrase, 63 needs a monosyllabic verb to hold the parallel — but the divergence is unlogged in the glossary because 事 has no entry. Raised drafting Ch 63, 2026-08-11. Not urgent; it becomes urgent the moment 事 is locked. Ch 64 also carries 無事-adjacent material and should be drafted with this open.

**Ch 34 and Ch 63 share 故能成其大 and do not chime.**
Ch 34 renders the formula *"Making no effort to appear great, / The Tao shows true greatness"* — which drops 成 (*chéng* — to complete, accomplish) entirely. Ch 63 renders *"So the sage never does the great, / and so completes their greatness."* The subjects differ (the Tao vs the sage) and the surrounding Chinese differs (以其終不自為大 vs 是以聖人終不為大), so this is not automatically an error — but `repeated-formula` will flag it, and Ch 34's line is the weaker of the two. Worth a look when Ch 34 is next open.

**Ch 27 · 無棄人 is softened to "no one is lost"; Ch 62 renders 棄 as "throw away".**
棄 (*qì*) is a graph of an infant in a basket being cast out — child-abandonment, literally. Ch 27's 故無棄人 currently reads *"ensures that no one is lost"*, which is gentler than the character and gentler than Ch 62's 何棄之有 (*"why would you throw them away?"*). The two lines are making one argument and should sound like it. Raised drafting Ch 62, 2026-08-11. Needs a rewrite of Ch 27's line, not a term-swap, so it goes to Shalom rather than being applied.

**`tools/import_commentary.py` mis-splits chapters when a chapter heading sits mid-block.**
Wang Bi's commentary on Ch 62 is in the repo but filed inside `sources/commentaries/wangbi/061.md`, because the Siku printing runs 62 on into 61's block behind the heading 六十二章. `--commentary 62` therefore reports it *not vendored*, and 62 is listed among the ten "unproofread" chapters when in fact its text is present and complete. Worth auditing the other nine (8, 14, 15, 19, 30, 54, 70, 71, 78) the same way before assuming any of them is missing. Raised drafting Ch 62, 2026-08-11.

**公 (*gōng*) is rendered three ways in three chapters and has no glossary entry.**
Ch 16 renders 公 as **impartiality** (容乃公，公乃王), which is what the character says — 八 (to divide) over 厶 (private, self); *Shuowen*: 公，平分也, "fair division." Ch 42's 王公 reads *"kings and lords"*. Ch 62's 三公 reads *"the three ministers"*. All three are defensible in place and none of them know about the others. When 公 is given an entry, Ch 42 and Ch 62 must answer to Ch 16. Raised drafting Ch 62, 2026-08-11. Related: 王 (*wáng*) is itself unsettled — see the "reading past the throne" thread in `notes/reading.md`.

**Solved by the evidence gate.** Because every chapter file carries its own Chinese, a rule never fires on English alone: "virtue" is an error only when 德 is in *that* chapter's source rows, and otherwise drops to `info` in a separate false-friends list. On the first run this took the error list to **9 findings with zero false positives**, from a naive scan's 20.

Three further lessons, from building it:

4. **A forbidden string already encodes its own case policy.** `"the Way"` written with a capital means the capital *is* the violation — so *"the way of nature"* (ch 9, 47) is fine. `"eternal"` written lowercase means the word in any case, which is what catches "eternally". Deriving the policy from how the decision was written cleared six false positives on "Being" (the participle: *"being still"*, *"their being"*) and needed no new configuration.

5. **Phrase rules and register rules catch different things; keep both.** Ch 53's *"The great Way"* slips past the forbidden phrase `"the Way"` because *great* breaks the string. The `devotional-capitalization` rule watches the bare capitalized word and catches it. Neither rule subsumes the other.

6. **Do not try to align the verse to the source rows.** Only 27 of 62 drafted chapters have verse lines matching source rows one-to-one, and the literal glosses speak **pre-lock** English — 玄德 is glossed "dark/mysterious virtue/power" where the verse correctly reads *"profound integrity"* — so matching a locked term against its own gloss fails exactly where the locks matter most. The `repeated-formula` rule therefore asks an alignment-free question: two chapters sharing a verbatim Chinese segment should have *some* pair of similar lines. If their closest pair still looks nothing alike, it says so. This is how ch 23's 信不足焉 was caught.
