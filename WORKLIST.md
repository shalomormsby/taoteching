# WORKLIST — what the manuscript still owes

*The single forward-looking file. Everything here is **open**. When something closes it leaves this file and becomes a one-line pointer in the ledger at the foot — because the reasoning already lives somewhere permanent, and repeating it here is how the old debt list grew to 343 lines and went stale.*

**Where things live.** The **ruling and its full argument** go in `glossary/`. The **decision, thin**, goes in `notes/` — manuscript forks in `notes/manuscript.md`, our own rendering calls in `notes/translation.md`, reader-facing threads in `notes/reading.md`. **What is still owed** goes here. Nothing belongs in two of those.

**Policy: fix on discovery, not in a deferred batch.** Mechanical term-swaps are applied immediately. Lines needing a rewrite are proposed to Shalom first, then applied. Each chapter carries its own debt in frontmatter (`retrofit: [...]`).

**The first draft is complete — 81 of 81, since 2026-08-26. The editing pass is the work now.**

**Progress: Pass 0 ✅ · Pass A ✅ · Pass B ✅ · Pass C ✅ (2026-08-31) — D–G open.** Pass D, the chapter-level rewrites, is the work now. Gate green: 0 errors, 95 tests, hard breaks intact, worklist consistent with itself.

*Supersedes `RETROFIT.md` and `EDITING-PASS.md`, merged into this file on 2026-08-28 and both now deleted. This file is `RETROFIT.md` renamed, so `git log --follow WORKLIST.md` still reaches the project's start; the 2026-08-10 sweep record and the lessons it taught the checker moved to `PLAN.md`. Every item below was re-verified against the manuscript at the merge; the old file listed six repairs that had already been made.*

---

## The list

**⬜ open · 🔶 part done · ✅ done · ⏸ deferred by Shalom.** Detail for every row is below, under the matching heading. **69 item rows: 47 open · 17 done · 2 part done · 3 deferred.** *(Counted from the table itself — a hand-kept tally drifts. It read "43 open · 18 done" and matched nothing.)*

| # | | Item | Ch | Pass |
|---|---|---|---|---|
| | | **Passes** | | |
| P0 | ✅ | Text bugs — a stray word, a missing *of*, a junk row, a corrupted table, a double space | 5 8 39 42 59 | 0 |
| PA | ✅ | **強 → strong**, completing the four-word table; 力 covered as *force* | 15 30 33 42 52 55 68 | A |
| PB | ✅ | **仁 → humaneness · 慈 → tenderness · 孝 → devotion**; Guodian G1 closed | 5 18 19 20 38 | B |
| PC | ✅ | ~~**The mirrors**~~ — every C-tagged row closed (T3-1, T2-9→14); T2-15's remainder moved to D with ch 28 and T1-8 | T3-1 · T2-9→15 | C |
| PD | ⬜ | **Chapter-level rewrites** — the real work, 18 chapters (22 and 64 only as the settled side of T2-15's pairs). *Ch is the union of the D-tagged rows below — recompute, do not hand-edit* | 3 4 8 10 11 13 16 22 28 29 31 32 35 36 38 39 41 64 | D |
| PE | ⬜ | Entries and sweeps — **守 執 保** (T2-19 ★) · 身 氣 靜 君 士 智 事 志 谷 恃 | book-wide | E |
| PF | ⬜ | The deferred calls | 民/人 · 正/奇 · em-dashes | F |
| PG | ⬜ | `build.py` | — | G |
| | | **Tier 1 · Wrong, not merely inconsistent** | | |
| T1-1 | ⬜ | 無知 and 無為 are on the wrong lines; 疵 dropped | 10 | D |
| T1-2 | ✅ | ~~道沖 inverted…帝 erased~~ — ch 4 rebuilt; **帝 locked to *god*, new entry**; closes T2-14c | 4 | D |
| T1-3 | ✅ | ~~為無為 → *"Without effort"*; 敢 dropped~~ — ch 3's closing movement rebuilt; 治 restored at both ends; **`"effortless" / "without effort"` added to 無為's forbidden list** | 3 | D |
| T1-4 | ✅ | ~~無為 → *"takes no action"*; 上 rendered two ways; invented *pure*~~ — ch 38 rebuilt; **失 restored as the chapter's spine**; 大丈夫 → *the great person* (Shalom's call); opens T4-7 | 38 | D |
| T1-5 | ✅ | ~~Bare 德 → *"profound integrity"* ×3~~ — 玄德's word, on a chapter with no 玄; triad restored | 23 | C |
| T1-6 | ⬜ | 守 → *"Embrace"* — 守/抱 swapped | 16 | D |
| T1-7 | ✅ | ~~守 → *"attune to"* ×3; 常 dropped from all three 常德~~ — 守 → *hold to*; 常 restored ×3; the template runs unbroken | 28 | D |
| T1-8 | ⬜ | 為 → *"force"* ×3; clashes with ch 64's *handle* | 29 | D |
| T1-9 | ⬜ | 左/右 as *"creation"/"destruction"*, then literal four lines later | 31 | D |
| T1-10 | ⬜ | 無身 → *"the separate self dissolves"* — an Advaita import | 13 | D |
| T1-11 | ⬜ | 古始 → *"the primordial source"* — forbidden register | 14 | E |
| T1-12 | ⬜ | 往 → *"the world routes to you"* ×2 — mechanistic | 35 | D |
| T1-13 | ⬜ | *"returns energy to its root"* — 氣 is not in this chapter | 16 | D |
| T1-14 | ⬜ | The closing 譬…猶 simile is garbled | 32 | D |
| T1-15 | ✅ | ~~谷 → *"reservoir"*, 谿, 官長, 大制 → *"orchestrator"*~~ — 谷 → *valley* (its word in 6 chapters); 制 → *cutting* (as ch 32); 割 → *severs* | 28 | D |
| T1-16 | ✅ | ~~雄/雌 → *"assertive/yielding energy"*~~ — **rooster and hen**, forced by 牝/牡 already holding *male* / *female* | 28 | D |
| T1-17 | ⬜ | 明 → *"clever"* — the one licensed lock exception, unrecorded | 65 | E |
| T1-18 | ⬜ | 佐 → *"One who rules"* — follows 河上公 against the grammar, unlogged | 30 | E |
| T1-19 | ⬜ | 大器晚成 → *"never completed"* — English follows a witness our table doesn't carry | 41 | D |
| T1-20 | ⬜ | Four `unlogged-variant` warnings | 2 9 26 51 | E |
| T1-21 | ⬜ | 配天 — the chapter and its own note disagree; the contested 天 line | 68 | F |
| | | **Tier 2 · One character, many Englishes** | | |
| T2-19 | ⬜ | ★ **The holding family — 守 執 保 有 collapsed into "hold."** 執 carries opposite valences and the English hides it | 5 9 14 15 16 28 29 32 35 37 52 62 64 67 69 74 79 | E |
| T2-1 | ⬜ | **身** — *body* / *self* / *themselves*, and two of them inside ch 54 | 7 9 13 44 54 | E |
| T2-2 | 🔶 | **智** four ways; **ch 3 settled as *the knowers*, fork logged**; *"cunning"* still wears 巧 at 19 and 57 | 3 18 19 33 65 | E |
| T2-3 | ⬜ | **士** three ways, two on the identical phrase 善為士者. *Rank question → T4-7* | 15 41 68 | E |
| T2-4 | ⬜ | **氣** — *life energy* / *vital breath* / *vital energy* | 10 42 55 | E |
| T2-21 | ⬜ | **厚** four ways — *thick* (38) · *heavy* (44) · *abundant* (55) · *rich* (75) | 38 44 50 55 75 | E |
| T2-22 | ⬜ | **嬰兒 / 赤子** both read *newborn*; 嬰兒 also reads *infant*. Word gets chosen at ch 10 (T1-1) | 10 20 28 55 | E |
| T2-5 | ⬜ | **靜** reads *"Silence"* here alone | 26 | E |
| T2-6 | ⬜ | **君** two ways three lines apart; 君子 → *"the sage"* — the opposition's honorific on our figure. *Rank question → T4-7* | 26 31 | E |
| T2-7 | ⬜ | **志** — *ambition* (3) / *will* (33) | 3 33 | E |
| T2-8 | ⬜ | Eight 善 rendered eight ways; 上善若水 a separate question | 8 | D |
| T2-9 | ✅ | ~~**辯** → *"eloquence"*~~ — **argue** in both; the 大X若Y frame does not endorse its X | 45 81 | C |
| T2-10 | ✅ | ~~**襲** — *inherited clarity* vs *the practice of*~~ — **two characters, not two readings**; 襲/習 fork recorded | 27 52 | C |
| T2-11 | ✅ | ~~**殆** → *"depletion"*; 没身不殆 two ways~~ — **danger** ×5, one-to-one; ch 15's invented danger and ch 25's dropped 周行 fixed too | 15 16 25 32 44 52 | C |
| T2-12 | ✅ | ~~**以此** three ways~~ — all three now *"By this."*; two stale notes corrected | 21 54 57 | C |
| T2-13 | ✅ | ~~**故去彼取此** three ways~~ — all three now ch 72's line; *gut* locked; *embrace* freed | 12 38 72 | C |
| T2-14 | ✅ | ~~難得之貨 ×3 · 信不足焉 ×2 · 挫其銳…同其塵 ×2~~ — subject settled with T1-2: the Tao at ch 4, imperative at ch 56 | 3 4 12 17 23 56 64 | C |
| T2-15 | 🔶 | Formula pairs — **5 closed**; 為天下式 unified at ch 22/28 (*serve as the world's pattern*). Only 為者敗之 left, with T1-8 | 22 28 29 64 | D |
| T2-16 | ⬜ | **事** wants an entry; 無事's licensed split needs confirming | 48 57 63 | E |
| T2-17 | ⬜ | **私** two ways, sheltering under 公's `covers:` | 7 19 | E |
| T2-20 | ⬜ | **巧** — *skill* (45) vs *cunning* (19, 57); the same fault as 辯, one line above it | 19 45 57 | E |
| T2-18 | ⬜ | 復命 → *"returning to what was given"* — still interpretive for 命 | 16 | D |
| | | **Tier 3 · Missed parallelisms** | | |
| T3-1 | ✅ | ~~★ **The 不自X / 自X者 mirror**~~ — ch 24 rewritten as ch 22's negative; ch 31 swept | 22↔24↔31 | C |
| T3-2 | ⬜ | Seven 善X couplets, seven unlike shapes | 8 | D |
| T3-3 | ⬜ | Three identical 當其無 frames rendered three ways; 利 and 用 lost | 11 | D |
| T3-4 | ⬜ | Four 將欲X之，必固Y之 nominalized into abstract laws | 36 | D |
| T3-5 | ✅ | ~~Three four-beat stanzas rendered as prose~~ — the 知其X/守其Y · 為天下Z · 常德不W · 復歸於V template restored | 28 | D |
| T3-6 | ⬜ | The 得一 / 無以 mirror breaks at its sixth pair | 39 | D |
| T3-7 | ⬜ | 寄/託 are a pair, rendered *entrusted with* / *truly care for* | 13 | D |
| R1 | ⬜ | ★ **Harvest 韓非's 35 divergent lemmas into `variants.yaml`** — the oldest witness to this text, currently marked but unexploited | 1 27 36 38 46 47 50 54 58 59 60 63 64 67 | E |
| R2 | ⬜ | **義 (yì) wants a glossary entry** — reads *duty* in all 5 lines, unlocked, and the atlas therefore publishes *righteousness* | 18 19 38 | E |
| | | **Tier 4 · Deferred by Shalom** | | |
| T4-1 | ⏸ | **民 / 人** — one decision, whole book. Consider taking 身 (T2-1) with it. *Kin to T4-7* | 13 chapters | F |
| T4-2 | ⏸ | **正 / 奇** — five Englishes | 37 45 57 58 78 | F |
| T4-3 | ⏸ | **Em-dashes in the verse** — 15 lines *(ch 28's two went with its rewrite, not by decision)* | 10 14 15 29 43 44 51 53 55 58 | F |
| T4-7 | ⬜ | ★ **Rank and gender — 大丈夫 · 君子 · 士.** Male rank-words dissolved in two opposite directions. Kin to T4-1 | 15 26 31 38 41 68 | F |
| T4-4 | ⬜ | 剛 owed its own mention | — | E |
| T4-5 | ⬜ | Glossary harvest — 一 名 希, plus ten new candidates | — | E |
| T4-6 | ⬜ | Guodian **G2–G6** | 5 16 17 18 25 + 26 more | E |
| T4-8 | ⬜ | 說文 (c. 100 CE) quotes the four-greats line as 人亦大 — six centuries before our oldest 人 witness | 25 | E |
| | | **Tier 5 · The harness** | | |
| T5-1 | ⬜ | Build **thin-translation** — the only rule that finds *absence* | — | G |
| T5-2 | ⬜ | `repeated-formula` should name the segment's own English | — | G |
| T5-3 | ⬜ | Forbidden lists thin on near-synonyms — *clever*, *depletion*, *energy*. *(無為 gained *effortless* / *without effort* / *takes no action* with T1-3 and T1-4; these three stand)* | — | E |
| T5-4 | ⬜ | Run `--english` on every lock; it is the only reverse-direction check | — | ongoing |
| T5-5 | ⬜ | The 70-item false-friend `info` list is not being read | — | G |
| T5-6 | ⬜ | `import_commentary.py` mis-splits when a heading sits mid-block | — | G |
| T5-7 | ⬜ | `build.py` — deferred until the text stops moving | — | G |
| T5-8 | ✅ | ~~`WORKLIST.md` keeps lists that restate its own table, ungated~~ — `check_worklist.py`, 16 tests, in CI | — | G |
| T5-9 | ✅ | ~~`data/` is generated but nothing gates it~~ — atlas rebuilt-and-diffed in CI; `build_graph.py` made deterministic | — | G |

**Why passes and not chapters.** Each pass closes **one decision and every chapter it touches**, in one sitting with the commentaries open, rather than walking 1→81 and re-opening the same argument twenty times.

**Pass D is the real work and must not be rushed into a sweep.** Sixteen chapters needing rewrites, each a full `chapter-review` with the witnesses and the commentaries — plus ch 22 and ch 64, which are already sound and are visited only as the settled half of T2-15's two remaining formula pairs.

*A second copy of this table, headed "The order of work," sat lower in this file and was deleted on 2026-08-31. It had drifted: it listed Pass D as seventeen chapters including 15, 26 and 30 — none of which has a D-tagged row — while omitting 38, which does, and it still showed Pass C unstarted. **The pass rows above are the only copy.** The `Ch` column for `PD` is the union of the `Ch` values on the D-tagged rows; when a row's pass changes, recompute it rather than editing it by hand.*

### The harness — closed 2026-08-31

**T5-8 · `tools/check_worklist.py`.** Four hand-kept lists went stale in three days and a person found every one by reading; `tools/` had no rule that read `WORKLIST.md` at all. Six rules, all enforcing something the file already says about itself: **pass-chapters** (a pass row's `Ch` is the union of its rows' `Ch`, and a cell that *points at rows* is never checked — declining to keep a list is the goal), **closed-pass** (no pass marked done over an open or part-done row; ⏸ does not block), **tally**, **pass-exists**, **duplicate-id**. 16 tests, each fixture a real failure this repo shipped. Wired into CI.

**T5-9 · the atlas is gated, and `build_graph.py` is deterministic.** `data/constellation-chars.json` had **never agreed with `data/characters.csv`** — both entered in `2466b4d`, but the JSON was built from an older database than the CSV it shipped beside, so it published glosses the CSV had withdrawn (95 characters) and older wordings for 93 more (*"the sea"* against the CSV's *"sea"*). Nothing rebuilt it, and nothing compared them. CI now rebuilds `build_db → export → build_graph` and fails on `git diff --exit-code data/`, the same shape as the glossary gate. **That gate was only safe after fixing the generator:** `export.py` orders all 11 of its queries, `build_graph.py` ordered 1 of 8, so its row order came from SQLite's planner — stable on one machine, and exactly the kind of stability that breaks when the gate moves to another. Every query is now ordered and the co-occurrence map is emitted sorted, so the output is a function of the data alone. Verified: node and link **sets** are unchanged by the ordering fix; only order moved.

---

## The finding

**This is two books.**

Chapters **56–81** were drafted *through* the locks, with `check_locks.py` live, the commentaries in `sources/`, and `chapter-review` running. Chapters **1–41** were drafted in the Google Doc era and have only ever been **swept** — term-swapped against locks settled after the fact.

| | chapters | clean | swap | chapter-level rewrite |
|---|---|---|---|---|
| **1–41** | 41 | **3** (7%) | 16 | **22** (54%) |
| 42–55 | 14 | 2 | 11 | 1 |
| **56–81** | 26 | **20** (77%) | 6 | 0 |

**And a sweep is structurally blind to what is wrong with the early half.** Every lock keys off a Chinese character in order to judge the English, so a chapter that simply **does not render** the character passes every check. Ch 4 drops 吾不知誰之子 (*wú bù zhī shuí zhī zǐ* — "I do not know whose child it is") and erases 帝 (*dì* — the high god of the Shang); ch 25 drops 周行 (*zhōu xíng* — "moves in a circle"); ch 28 drops 常 (*cháng*) from all three 常德 lines; ch 3 dropped 敢 (*gǎn*) and 治 (*zhì*). **All four carried `retrofit: []` and passed every check.** *(Ch 4 repaired 2026-08-31 with T1-2; ch 3 with T1-3. Ch 25 and 28 stand.)* This is the Ch 20 / Ch 65 failure one level down — not an empty translation block, but a *thin* one.

**So the work is a second draft of chapters 1–41, not another sweep.**

---

## Tier 1 · Wrong, not merely inconsistent

Meaning changed. Each needs a decision; most need one line rewritten.

### Errors of fact

1. **Ch 10 — 無知 and 無為 are on the wrong lines.** Our base reads 愛民治國，能**無知**乎 and 明白四達，能**無為**乎. The verse answers them backwards: *"can you lead **without doing**?"* / *"can you be **unknowing**?"* Some editions swap the pair; ours does not, and either way it is unlogged. Also in this chapter: 滌除玄覽，能無疵乎 loses 疵 (*cī* — flaw) entirely, and 明白四達 renders 明 as *"understanding"*.

2. ✅ **Closed 2026-08-31 — the first Pass D chapter.** Four faults and a missing line. **道沖 inverted and given 器's *vessel*** (沖 is *empty*, 不盈 is *never fills*; both halves were flipped). **淵 dropped**, taking one of two matched 兮 frames with it. **吾不知誰之子 not translated at all.** And **帝 erased into "ancestor"** — the inverse overlay: the Chinese names a god and the English deleted him, deleting Laozi's own demotion of him. **帝 is now locked** (`glossary/di-帝.md`) to *god*, rendered *"older than any god"* — not *the high god*, because the definite article asserts a singular supreme deity the scholarship has not settled, **and *the* confers status as effectively as a capital.** Along the way: **兮 never hedges** (twelve occurrences, [asserted]兮，[hedged]), **存 is being-still-there against 亡** — *remain* imports a depletion the first line denies, *exist* belongs to 有 — and **象 is the comparison, not the noun**, because wherever 象 is a noun it is marked by 之/有/大 and here it stands bare. **Closes T2-14c**: the quatrain keeps the Tao as subject at ch 4, the imperative at ch 56. 或/若 fork recorded.

### Lock violations live in the verse

3. ✅ **Closed 2026-08-31 — Pass D's second chapter.** The whole closing movement had **the opposite grammar from the Chinese**: 常使民無知無欲 / 使夫智者不敢為也 / 為無為，則無不治 are built on 使 (*shǐ* — to cause), 使 and 為, and the English on three *"Without"*s, so the sage who acts became a sage who abstains. **為無為 → *"Without effort"* breached the 無為 lock on the one line `glossary/wuwei-無為.md` cites as its own proof** (*"something you actively do … continuous, **effortful**, and difficult"*); it now carries ch 63's English exactly, *"Do the not-doing."* **治 (*zhì* — to govern) had been dropped from the hinge** 是以聖人之治 while still closing the chapter at 無不治 — both ends restored, and *"nothing is left ungoverned"* recovers the echo with 無不為 at ch 37 and 48. **敢 applied** (*never push to act*), **常 restored** (*ever*), and 志 → *ambition*. **The English had also read as manipulation, and the Chinese does not** — 無知, 無欲 and 不敢為 are each the sage's **own** state elsewhere (10 · 1, 34 · 64, 67, 69), and three English collocations invented the asymmetry. The general finding is now a standing principle, ***collocation carries a verdict*** (`notes/translation.md`), beside ch 4's *the definite article*. **Harness hole closed:** the forbidden list held `"effortless action"` and not `"without effort"`; both `"effortless"` and `"without effort"` are now on 無為's list and verified firing. **Still owed at ch 3:** the 知/智 pair (T2-2), and 心 dropped from 使民心不亂.
4. ✅ **Closed 2026-08-31 — Pass D's third chapter.** **失 (*shī* — to lose) is the chapter's spine and had been deleted from its hinge.** Five occurrences, more than in any chapter in the book — 下德不**失**德, then 失道 · 失德 · 失仁 · 失義 — and line 2 read *"clutches at integrity."* The argument that vanished with it: **the refusal to lose is what produces the losing** (王弼: 求而得之，必有失焉). **And *clutches* renders 執, which is not in the chapter** — it came from 王弼's gloss on the line *above*, describing what 上德 lacks; 河上公 reads the contrast as **visibility**, not grasping. **無為 → *"takes no action"*** was invisible to `check_locks` (`"non-action"` was on the list, `"takes no action"` was not — now added and verified firing). **上** read *highest* ×2 and ***Ultimate*** ×3 with a capital, on a ladder's rung-marker, against ch 41 and against `glossary/wei-為.md`'s own table. **首 / 始** shared one English in adjacent lines; **華 / 實** had three across two stanzas. **以為 → *"has something it acts for,"*** restoring the 2×2 grid 王弼 states outright (無以為者，無所偏為也). The invented *pure*, *imitation*, *life's* and *of being* are all gone, and the 禮 rung now takes the two lines the Chinese gives it. **大丈夫 → *the great person*, gendered reference removed deliberately (Shalom's call)** — standing rule 2's default, so no `shaloms-call`; the violation was the silence. **Opens T4-7** (rank and gender) and **T2-21** (厚). Two collation notes recorded: 扔/仍 in `sources/variants.yaml`, 焦竑's four 處 in `notes/manuscript.md` only.
5. ✅ **Closed 2026-08-31.** Bare 德 had been given **玄德**'s English on three lines, in a chapter containing no 玄. 德 is locked to *integrity*, and `--english "profound integrity"` now returns only 玄德's four lines (10, 51, 65 ×2). **The cost was structural:** the stanza is a three-term parallel — 道者同於道；德者同於德；失者同於失 — and an adjective on the middle term alone broke it. Second time this chapter has handed 德's slot to the wrong word; the first was 信 (*xìn* — trust) taking 德's.
6. **Ch 16 — 守 → *"Embrace."*** 守 is *hold fast to*, 抱 is *embrace*; the lock says do not swap. **Ch 52 does it right.**
7. **Ch 28 — 守 → *"attune to"*** on all three 知其X守其Y lines, and 常 dropped from all three 常德.
8. **Ch 29 — 為 rendered *"force"* three times in four lines.** 為 is locked to *do / handle / serve as*. *Force* is a reading smuggled in as a translation: it supplies violence 為 only implies, and makes 無為 look like counsel against aggression rather than against handling as such. **Ch 64 carries 為者敗之，執者失之 verbatim and now reads *"Those who handle it ruin it."*** The shared formula must not read two ways. Line 1 also carries an em-dash.

### Inventions and overlays

9. **Ch 31 — 左/右 rendered *"creation"/"destruction"*, then rendered literally four lines later.** The chapter cannot be read against itself, and the reader cannot see that 吉事尚左，凶事尚右 is explaining 君子居則貴左.
10. **Ch 13 — 無身 → *"the separate self dissolves."*** 及吾無身 is *"when I have no body."* An Advaita frame on the one line where 身 works hardest.
11. **Ch 14 — 古始 → *"the primordial source."*** *The Source* is forbidden for 母 and is the register the naturalistic razor exists to strip. 古始 is *"the ancient beginning."*
12. **Ch 35 — 往 → *"the world routes to you,"* twice.** Network vocabulary; our named besetting temptation.
13. **Ch 16 — *"Each returns energy to its root."*** 氣 is not in this chapter.
14. **Ch 32 — the closing simile is garbled.** 譬道之在天下，猶川谷之於江海 is *"the Tao in the world is like streams and valleys to rivers and the sea."* The 譬…猶 frame is gone and the comparison's direction is muddled.
15. **Ch 28 — 谷 → *"reservoir"*, 谿 → *"deep ravine"*, 官長 → *"master orchestrator"*, 大制 → *"the great orchestrator."*** Ch 66, 15 and 32 all render 谷 as **valley**, which is the plain sense; a reservoir is *built* and holds by design, and the chapter's argument is that lowness gathers **without** contrivance. *Orchestrator* is the mechanistic register, one line below 器. 谷 also wants an entry — seven chapters.
16. **Ch 28 — 雄/雌 as *"assertive energy" / "yielding energy."*** 雄 and 雌 are a **rooster and a hen**. Rendering the book's central feminine image as an abstract polarity of energies is a live cost, and 雌 is load-bearing for the feminine thread. **Take ch 28 as one review, not five swaps.**

### Unlogged departures — defensible, but nothing records them

17. **Ch 65 — 明 → *"clever."*** Breaks the 明 lock, and **both commentators support the break**: 王弼 明謂多見巧詐蔽其樸也. Almost certainly right; **the one licensed exception to a settled lock in the book, and nothing records it.** Owed: a line in `notes/translation.md`, a paragraph in `glossary/ming-明.md`, a `lock-ok` waiver, and *clever* added to 明's forbidden list so the exception is visible rather than invisible.
18. **Ch 30 — 佐 → *"One who rules."*** 佐 is *to assist*; the chapter addresses a ruler's **adviser**. 河上公 rescues it reflexively — 謂人主能以道自輔佐也 — but we follow a commentary against the plain grammar without saying so.
19. **Ch 41 — 大器晚成 → *"never completed."*** Our table reads 晚成 (**late**-completed); *never completed* is the Mawangdui 免成 reading. Bring the English to our Chinese, or take the silks deliberately and record it.
20. **Four `unlogged-variant` warnings**: ch 2 (相形…相盈), ch 9 (銳), ch 26 (君子), ch 51 (亭之毒之). Each claims a `notes/manuscript.md` entry that does not exist.
21. **Ch 68 — 配天 — the chapter and its own note disagree.** Reads *"partnered with the sky"*; 天 stands alone with no 地 near, which the lock sends to *nature / the natural*. **The single contested line for the 天 split.**

---

## Tier 2 · One character, many Englishes

19. **★ The holding family — four characters collapsed into one English word.** *Raised 2026-08-28 by Shalom at ch 24, after 有道者 (*yǒu dào zhě*) turned out to read *"those who hold the Tao"* for a different character than ch 15's 保此道者.*

   | | | current Englishes |
   |---|---|---|
   | 守 (*shǒu*) | guard, hold fast to — **locked** | *hold* (5, 32) · *guarded* (9) · **embrace** (16) · **attune to** (28 ×3) · *hold to* (37) · *hold fast to* (52) · *stay with* (52) · *defend* (67) — **eight** |
   | 執 (*zhí*) | to grasp, to seize | *Hold* (14) · *grasped* (29, 64) · **Embody** (35) · *gripping* (69) · *seize* (74) · *holds* (79) — **six** |
   | 保 (*bǎo*) | to keep, to preserve | *cannot last* (9) · **holds** (15) · *safekeeping* (62) · *keep safe* (67) — **four** |
   | 有 (*yǒu*) | to have — *presence* is locked in `wu-you-無有.md` | 有道者 → **are with the Tao** (24, 31, 77) ✅ *settled 2026-08-28* |

   **The sharpest problem is 執, and it is the 強 problem again.** 執 is the book's word for **the wrong kind of taking-hold**: 不可執也 (*bù kě zhí yě* — "it cannot be grasped," ch 29) and 執者失之 (*zhí zhě shī zhī* — "those who grasp it lose it," ch 29 and 64). But ch 14 gives 執古之道 (*zhí gǔ zhī dào*) as *"**Hold** the ancient Tao"* — an instruction, positive. **Same character, opposite valence, and our English resolves a tension the Chinese leaves standing.** Ch 79's 執左契 (*zhí zuǒ qì* — "holds the left tally") is a third, neutral use. Whatever 執 takes has to be sayable in all three.

   **And 執 is dropped outright at ch 35** — 執大象 (*zhí dà xiàng* — "grasp the great image") reads *"Embody the great form,"* in the same line as the *routes to you* mechanism already flagged at T1-12.

   **What Shalom named as the priority: the verbs for relating to the Tao.** The book has at least five and English is collapsing them.

   | ch | Chinese | now |
   |---|---|---|
   | 14 | 執古之道 | *Hold the ancient Tao* |
   | 15 | 保此道者 | *One who holds the Tao* |
   | 23 | 從事於道者 | *the one who aligns their actions with the Tao* |
   | 24, 31, 77 | 有道者 | *those who are with the Tao* ✅ |
   | 52 | 復守其母 | *return and hold fast to our mother* |

   **Order of work.** 守's eight Englishes are partly already tracked — ch 16 is T1-6 and ch 28 is T1-7, both Pass D — so the sweep should follow those rewrites rather than precede them. 執 needs an entry of its own and should be taken with 為 (*wéi* — to handle), since 為者敗之，執者失之 pairs them and T1-8 is unresolved at ch 29. 保 is small (four lines) and can ride along.

1. **身 (*shēn* — body) drifts, and ch 54 uses two Englishes inside one stanza.** 修之於身 → *"in your **body**"*; five lines later 以身觀身 → *"the **self** through your own **self**."* Across the book: *body* (13, 54), *self* (7, 44, 54), *themselves* (7), dissolved entirely at ch 9 (身退 → *"cease striving"*). **Same shape as 民/人 — decide them together.**
2. **智 rendered four ways, and *"cunning"* covers four characters.** *cunning* (3), *cleverness* (18, 19), *intelligent* (33), *guile* (65). Some spread is legitimate — 智 runs from *wisdom* at 33 through *cleverness* at 19 to *artifice* at 65, a licensed split like 事. What is not legitimate is that it happened by accident. **And *cunning* also did duty for 知 (ch 3, adjacent line), 巧 (ch 57), and a fourth at ch 58.** **Ch 3 is closed (2026-08-31, with T1-3):** 無知 → *unknowing*, 智者 → **the knowers**, and *cunning* is off the chapter. The word was chosen because **the commentators diverge on who the 智者 are** — 王弼 prints 智者 and glosses 智者謂知為也 (*"those who know how to handle"*), 河上公 prints 知者 with the phonetic note 知音智 and glosses 思慮深不輕言, almost verbatim what he says of the *approving* 知者 at ch 56 — so any English specific enough to settle it picks a side. Fork now in `sources/variants.yaml` and `notes/manuscript.md`. **The book-wide split stands** at 18, 19, 33, 65. **Take 智 with 知, 巧, and the locked 明** — those four are the book's whole epistemology and three are unlocked.
3. **士 (*shì*) has three Englishes, two on the identical phrase.** 善為士者 is *"The ancient masters"* (15) and *"The master warrior"* (68); 上士/中士/下士 are *students* (41). 王弼 defines it flatly: 士，卒之帥也, *"the commander of troops."* None of them is a master of anything, and *masters* puts back the register the 聖人 lock exists to keep out.
4. **氣 has three Englishes:** *life energy* (10), *vital breath* (42), *vital energy* (55).
5. **靜 reads *"Silence"* at ch 26** alone, against *stillness* at 15, 16, 37, 45, 57, 61.
6. **君 reads *ruler* then *mastery* three lines apart at ch 26 — and 君子 is rendered *"the sage"* at ch 26 and twice at ch 31.** Conflating 君子 with 聖人 erases a distinction the book draws deliberately.
7. **志 (*zhì*) reads *striving* (3) and *will* (33).** Small, real, no entry.
8. **Ch 8's eight 善 are rendered eight ways** — *goodness · a solid foundation · limitless depth · pure kindness · trustworthy · good order · skillful · good timing.* The 善 lock is not applied to its own showcase chapter. **上善若水 is the separate question**: *"Supreme goodness"* stands above eight lines of pure competence and may want *the highest excellence*.
9. ✅ **Closed 2026-08-31.** **argue** in both; ch 45 reads *"Great argument seems halting."* Ch 81's Notes had licensed the split on the premise that **辯 is praised at ch 45** — wrong. **The 大X若Y frame does not endorse its X**, and the proof is one line above: 大巧若拙 puts 巧 (*qiǎo*) in the frame, and 巧 is condemned at ch 19 (絕巧棄利) and ch 57 (人多伎巧). The commentators put the two chapters together, not apart — 王弼 on ch 45: 大辯因物而言，己**無所造** (*"great 辯 speaks according to things; the self invents nothing"*), against 河上公 on ch 81: **不綵文**也 (*"does not ornament their words"*). Not the 強 both-valences case: *eloquence* manufactured the appearance of a double. 說文 on 辯: 治也。从言在辡之閒 — words between **two tattooing knives**, a courtroom. 訥 → *halting* (說文 言難也, of speech specifically) rather than *awkward*, which overlapped 拙. **Spun off as T2-20:** 巧 has the identical fault, *skill* (45) against *cunning* (19, 57).
10. ✅ **Closed 2026-08-31, and the cause was a manuscript fork nobody had logged.** The two Englishes were **not two readings of one character**: ch 27 rendered 襲 (*xí* — to layer a garment over another), ch 52 rendered **習** (*xí* — to practise), which our base text does not print. Both commentaries print 習 at ch 52 — 河上公 glosses it 習修常道 — and the Siku 王弼 carries 〔案習各本作襲〕. **We keep 襲 in both**, on the pair: 是謂襲明 / 是謂襲常 is one frame, and 明 / 常 are bonded by 知常曰明 (16, 55). **襲 is 說文's 左衽袍 — a robe closed to the left, i.e. grave-clothes**, one garment over another; *inherit* is a derived sense and lost the layering. Now *"clarity worn covered"* (27) and *"holding the ever-present covered"* (52). Fork recorded in `sources/variants.yaml` and `notes/manuscript.md`. **The `unlogged-variant` rule could never have caught this** — it fires only on variants a chapter *claims*, and an English quietly following an unrecorded reading is invisible to it.
11. ✅ **Closed 2026-08-31.** 殆 (*dài*) had **five occurrences and four Englishes, none of them 殆**: *"Not even death threatens this"* (16), *"Inexhaustible"* (25), *"depletion"* (32, 44), *"no harm"* (52). All five now read **danger**, and *danger* renders nothing else — one-to-one in both directions. 說文 危也; the graph is 歺 (*è*), the **bare-bone radical** of 死 and 殃. **Both commentators converge in all five places** (河上公 不危殆 ×3; 王弼 免殆 at ch 25) — no divergence to preserve. Two of the four Englishes were other characters' words: *harm* is 害's (35, 56, 66, 73, 81), *inexhaustible* is 窮's (6, 35). **Ch 16 was a mistranslation, not a mismatch** — 没身 is "to the end of one's life," as ch 52 already had it, not *death*; and the sentence belonged to the person, not the Tao. **Two extras fixed on the way:** ch 25's 周行 (*zhōu xíng* — "moves in a circle") had been dropped entirely and is restored, and **ch 15's *"aware of danger from all sides"* was invented** — no 殆 in that chapter, no threat in the Chinese, and 河上公 has 畏四鄰**知之**, *the fear of being found out*; now *"Hesitant, as if wary of neighbors on four sides."* **殆 and 畏 both still owe glossary entries**, so *danger* is correct book-wide but unenforced.
12. ✅ **Closed 2026-08-30.** All three read **"By this."** — ch 57 keeps its colon, which is punctuation and marks the only forward-pointing one of the three. *"Precisely"* had no warrant; *"here, now"* was 河上公 (*Héshàng Gōng*)'s gloss 此，今也 (*cǐ, jīn yě* — "'this' means now") lifted into the verse, and it picked his reading over 王弼 (*Wáng Bì*)'s anaphoric 此上之所云也 (*"'this' is what was said above"*), which the old note claimed it "held." **Two stale claims corrected** — `notes/manuscript.md` §*What the commentators say 此 means* and `DISCOVERIES.md` §2's table and evidence list. **Rider:** ch 57's 其 (*qí* — it) had been rendered *"this"*, colliding with 此 one clause apart; now *"it."* **Two standing principles added** to `notes/translation.md`: *the commentaries are evidence, never candidate renderings*, and *register — no modern spiritual idiom* (the "here, now" / *Be Here Now* family).
13. ✅ **Closed 2026-08-30.** All three read **"They let go of what is out there and take what is here."** 彼 (*bǐ* — that, yonder) occurs **exactly three times in the book and all three are this tag**, so there was no competing context. Ch 12 and 38 had been rendering the *referents* and deleting the *deixis*; ch 72's axis-not-referent solution was right in all three. **Two side gains:** *embrace* freed from 取 (*qǔ* — to take) at ch 38 — it had been wearing four characters, and the other two are T2-19; and ch 12's *"gut wisdom"* turned out to be a **lock breach against its own entry**, which has a paragraph headed *"Why 'belly' and not 'gut'"* citing ch 12. **Harness hole found and closed:** `covers:` records a `render:` but no `forbidden:` list, so *gut* was unforbidden book-wide; `"gut"` is now on 心's `forbidden:` and verified firing. **Still owed on ch 38's stanza** (Pass D, T1-4): *"thickness **of being**"* and *"**life's** fruit"* invent words.
14. 🔶 **難得之貨 — closed 2026-08-30.** All three read **"rare goods"**, and **貨 (*huò*) is now locked to *goods* with its own entry** (`glossary/huo-貨.md`, `status: locked`, forbidding *treasure · precious · scarce · riches*). The error was not inconsistency: all three Englishes put the value **in the object** — *the precious* (貴's word, and 貴 is the verb in the same line), *rare treasures* (寶's), *precious goods* — which made 不貴難得之貨 circular and dropped the ruler out of a sentence about what a ruler does. 貨 was also wearing 富's *wealth* at **ch 44**, now swept. *Rare* renders no character and that cost is recorded: **"hard" is 堅's**, and 難's own *difficult* will not go attributive. **Two general rules came out of it** — *one Chinese modifier, one English modifier* (no near-synonym doublets; they are a KJV tell), and the note that English has **no one-word adjective for "difficult to obtain" that is not also a value word**, which is why three chapters drifted the same way independently. **Ch 3 riders applied:** 民 restored to the middle clause of the triad, and 不貴 → *prizing* in both ch 3 and ch 64. **Still owed at ch 12:** 妨 (*fáng* — to hinder) reads *corrupt*, a moral word for an obstruction word. **信不足焉，有不信焉 — closed 2026-08-30**, the oldest open item in the debt list. Both chapters now read **"Where trust runs short, there is no trust,"** and **ch 23's `lock-ok` waiver is gone with it** — it said *"revisit in the editing pass,"* and this was that pass. The split had been argued on context (ch 17 political, ch 23 about 同 *tóng* — merging), and **the commentators cross it in both directions**: 王弼 reads the line at **ch 17** as impersonal natural law (此自然之道也), 河上公 supplies a ruler at **ch 23** (君信不足於下). **Ch 17 was also wrong, not just mismatched** — *"leaders don't trust the people"* made 信 an inner attitude, which `glossary/xin-信.md` forbids (信 is a 符契, a split tally — a correspondence that can be checked), and ran the failure backwards: 河上公 has the people **deceive** a ruler who could not be relied on. Both old versions asserted **reciprocity**, which is 河上公's reading; 王弼's is **emergence**, with no second party. The English is now agent-free and holds both. `glossary/xin-信.md` updated to match. **挫其銳…同其塵 — closed 2026-08-31, and the only Pass C item that does not fully unify.** Ch 4's four lines now carry ch 56's nouns and its couplet lineation: **"It blunts the sharpness, untangles the knots. / Dims its own light, merges with the dust."** The live error was a **lock breach** — *brilliance* is on 明's `forbidden:` list, 光 (*guāng*) is 明's counter-term, and `glossary/ming-明.md` had **already glossed both chapters together** as *dim your light*. `check_locks.py` could not see it (no 明 in ch 4, so the evidence gate drops it to `info`); only `--english` finds this class. **The subject is deliberately left split** and travels with ch 4's rewrite (T1-2): 王弼 reads ch 4's lines with **the Tao** as subject and ch 56's as **a person's practice**, and unlike ch 17/23 the frames do not appear in the wrong chapters. Ch 4's subject is downstream of 道沖 inverted, 吾不知誰之子 dropped, and 帝 erased — deciding it now means deciding it twice. **Ch 56 held the ground** because it is attested **complete at Guodian**; ch 4 is not attested at all.
15. **Formula pairs the checker names:** 是謂玄德 (10 vs 51/65) · 故能成其大 (34 vs 63) · 可以長久 (44 vs 59) · 是以聖人猶難之 (63 vs 73) · 為者敗之，執者失之 (29 vs 64) · 為天下式 (22 vs 28) · 物或惡之 and 故有道者不處 (24 vs 31) · 不貴難得之貨 (3 vs 64).
16. **事 wants an entry, and 無事's licensed split needs confirming.** *meddle* at 48 and 57, *serve the not-serving* at 63. `glossary/shi-事.md` recommends making ch 63's word the standard on the strength of ch 57's quartet. Not applied.
17. **私 reads two ways** — *private self* (7) and *the self* (19) — sheltering under 公's `covers:`. Ch 19's is arguably right in place, but 私 may want its own entry rather than a `covers:` line.
18. **Ch 16 — 復命 → *"returning to what was given."*** No longer borrowing another character's English, but still interpretive for 命. Worth a look when ch 16 is reviewed.

---

## Tier 3 · Missed parallelisms

Structure the Chinese has and the English does not. These are rewrites, and they are where the poetry is.

1. **★ Ch 22 ↔ Ch 24 — the 不自X / 自X者 mirror, the biggest in the book.** Ch 22's stanza was rebuilt 2026-08-27 following 王弼's one-to-one mapping; ch 24 is its exact negative and still reads in unrelated words. Ch 24 also flattens 餘食贅行 (王弼: 盛饌之餘, *"the leftovers of a rich feast"*, and 肬贅, a wart) to *"wasteful and superfluous"*, and renders 物 as *"the material world."* **Its last two lines are shared verbatim with ch 31 and must move together.**
2. **Ch 8 — seven 善X couplets, seven unlike shapes.**
3. **Ch 11 — three identical 當其無，有…之用 frames rendered three ways**, and 有之以為利，無之以為用 loses both 利 and 用 into *"creates potential."*
4. **Ch 36 — four 將欲X之，必固Y之 conditionals nominalized into abstract laws.** *"Contraction requires firm expansion"* has no agent and no *first*. Ch 36 is the least dense chapter in the book (0.88).
5. **Ch 28 — three four-beat stanzas rendered as prose**, with 守 wrong and 常 missing in all three.
6. **Ch 39 — the 得一 and 無以 lists are a mirror, and the sixth pair breaks.** The first ends 侯王得一以為天下**貞**, the second 侯王無以**貴高**; our English answers *"true anchors"* with *"their anchoring."*
7. **Ch 13 — 寄/託 are a pair**, rendered *"entrusted with"* and *"truly care for."*
8. **Ch 33 — 力/強** — closed by Pass A, but the chapter's remaining couplets are worth a look when 智 is settled.

---

## Research · R1 — 韓非's divergent lemmas

*Opened 2026-08-29, after the `unmarked-lemma` defect was fixed. The marks now exist; nothing has been done with what they reveal.*

**Why this is worth a pass of its own.** 韓非 (*Hán Fēi*) died in **233 BCE**. His quotations in 解老 (*Jiě Lǎo* — "Explaining Laozi") and 喻老 (*Yù Lǎo* — "Illustrating Laozi") are **the oldest witness to the Laozi text in existence** — older than the Mawangdui silks (c. 200 BCE) and roughly contemporary with the tail of the Guodian tradition. And unlike Guodian and Mawangdui, **his text is vendored in this repository and quotable**: it is public domain by age, so `PROVENANCE.md`'s "record the fact, never the transcription" rule does not bind here. We can cite the reading directly.

**35 of his 53 lemmas differ from our base text**, every one now carrying `*`. Four more differ only in printed glyph and are correctly unmarked. The divergences are **not yet in `sources/variants.yaml`, so `--witnesses N` shows nothing for any of these chapters.**

**Five of them bear directly on decisions already open on this list**, which is the real argument for doing it:

| ch | 韓非 reads | our base | bears on |
|---|---|---|---|
| 60 | 聖人亦不傷**民** | 聖人亦不傷**人** | **T4-1**, the deferred 民/人 decision — the oldest witness has 民 where we have 人 |
| 27 | 雖**知**大迷 | 雖**智**大迷 | **T2-2**, 智 rendered four ways; 韓非 reads the other character |
| 64 | **恃**萬物之自然 | **以輔**萬物之自然 | 恃 (*shì* — rely on) against 輔 (*fǔ* — assist), on a line swept for 敢; 恃 was itself settled 2026-08-26 |
| 67 | **吾**有三寶，持而**寶**之 | **我**有三寶，持而**保**之 | the locked 我/吾 pair (`glossary/wo-wu-我吾.md`), and 保/寶 feeds **T2-19**'s holding family |
| 36 | **邦**之利器 | **國**之利器 | the 邦/國 Han name-taboo already logged at ch 61 in `notes/manuscript.md` |

**Substantive forks worth their own entries**, beyond those five:

| ch | 韓非 | our base | what turns on it |
|---|---|---|---|
| 38 | 失道而後**失**德，失德而後**失**仁… | 失道而後德，失德而後仁… | he repeats 失 (*shī* — to lose) in all four clauses: *"lose the Tao, then lose integrity"* rather than *"lose the Tao, and then integrity."* **A different chapter**, and we edited it in Pass B without knowing |
| 58 | 廉而不**穢** | 廉而不**劌** | 劌 (*guì* — to wound) against 穢 (*huì* — foul, weed-choked); our verse reads *"sharp but does not wound"* |
| 50 | 虎無所**錯**其爪 | 虎無所**用**其爪 | 錯 (*cuò* — to set down) against 用 (*yòng* — to use) |
| 36 | 將欲**取**之 | 將欲**奪**之 | 奪 (*duó* — to seize by force) against 取 (*qǔ* — to take); **T3-4** is rewriting these four conditionals |
| 36 | 魚不可脫於**深**淵 | 魚不可脫於淵 | 韓非 adds 深 (*shēn* — deep) |
| 67 | 故能為成**事**長 | 故能成**器**長 | 器 (*qì* — vessel) is locked; 韓非 reads 事 (*shì* — affairs), also locked |
| 54 | **脩**之身 | 修之**於**身 | 脩/修 is a lexical choice, deliberately **not** folded as a printing variant; he also drops 於 |
| 59 | 治人事天莫**如**嗇 | 莫**若**嗇 | same sense, real variant |
| 47 | 不出**於**戶，**可以**知天下 | 不出戶知天下 | he adds 於 and 可以 throughout |

**Noise to record but not to log.** Roughly a third of the 35 are 也 / 矣 / 乎 / 之 particles added or dropped — 韓非 is quoting inside prose essays, often from memory, and pads for rhythm. Ch 1's 道**之**可道，非常道**也** is the clearest case. **Mark them, do not give them `variants.yaml` entries**, or the apparatus fills with noise and the real forks stop standing out.

**How to do it accurately.**

1. **Read the lemma in its essay, not alone.** 韓非 sometimes quotes a line to argue against a reading, and the surrounding 〔解老〕 or 〔喻老〕 prose says which. The vendored file has both.
2. **Use the existing schema** — `chapter · line · base · witnesses · meaning_bearing · our_call · note · logged`, with `hanfeizi` as the witness id, which `sources/variants.yaml` already declares in its header.
3. **`our_call: base` unless there is a reason** — this is an edition of the received recension, as settled at ch 25 and ch 19.
4. **Set `meaning_bearing` honestly.** Particle padding is `false`; a different content word is `true`. Every `true` needs a `notes/manuscript.md` entry or `check_locks.py` will fail the build — which is the ratchet working.
5. **Regenerate**: `python3 tools/build_db.py && python3 tools/export.py`, then `--witnesses N` on the affected chapters.

**The command that produces the evidence table:** fold each `*`-marked lemma with `lib.corpus.fold`, align it against `load_base_text()` with `difflib.SequenceMatcher`, and print the non-equal opcodes. That is how the tables above were generated; it takes about fifteen lines.

**Do not start this before Pass D.** Ch 36, 38, 54, 64 and 67 are all being rewritten, and a variant entry written against a line that is about to change will have to be written twice.

---

## Tier 4 · Open calls, deferred by Shalom

- **★ Rank and gender — 大丈夫 · 君子 · 士. T4-7, opened 2026-08-31 with ch 38.** This book has a family of **male rank-words**, and the manuscript has been dissolving them silently **in two opposite directions**. 大丈夫 (*dà zhàng fū*, ch 38, a hapax) was turned into a **modern psychological type** — *"the mature person"*, now *the great person*. 君子 (*jūn zǐ* — literally *a ruler's son*, the Confucian gentleman, ch 26 and 31) is rendered **"the sage"**, which hands the opposition's honorific to Laozi's own figure, whose name is a different word entirely (聖人). 士 (*shì* — a male service rank: knight, officer, retainer, ch 15, 41, 68) reads three ways, twice on the identical phrase 善為士者. **The shared question is what to do with *rank*, and it is not the one-character-many-Englishes question that T2-3 and T2-6 currently file it under** — a rank word universalised loses the rank, which is often what the line is about. 說文 makes the stakes concrete for 夫: 一以象簪也…人長八尺，故曰丈夫 — *"the single stroke depicts a hairpin… a person stands eight 尺 tall, therefore we say 丈夫"* — a measurement and a capping ceremony, not an inner state. Standing rule 2's carve-out is for the **incidental** male-default; these are not incidental. **Owed:** one decision across all three, the seam noted wherever it is universalised, and a check on whether 君子 can keep *"the sage"* at all. **Kin to T4-1 (民/人) and to T2-1 (身) — the same question about social categories.** Cross-refs: T2-3, T2-6.

- **民 / 人 — one decision, whole book, deferred 2026-08-25.** 民 (the governed, an eye pierced by a blade) reads *"the people"* in all 32 of its lines — consistent, unlogged, never argued for. 人 drifts, and **ch 57 renders it both ways two lines apart.** A rule settled at one chapter propagates to twelve others and to the cross-chapter rhymes in `notes/reading.md` (72 → 74 → 75 turns on 民不畏X; ch 80's 使民重死 is load-bearing for ch 75's 民之輕死). Ch 74 reads *"the people"* as a **hold, not a precedent**. Owed: `glossary/min-民.md`, very likely a 人 entry or `covers:`, a sweep, and a `notes/reading.md` pass. **This sweep adds 身 to the same shape of problem — consider deciding the three together.**
- **正 / 奇** — five Englishes across ch 37, 45, 57, 58, 78. Owed: `glossary/zheng-正.md`.
- **Em-dashes in the verse** — 17 lines across ch 10, 14, 15, 28, 29, 43, 44, 51, 53, 55, 58. Ch 44's three are good. Ch 10 and ch 51 share the same en-dash on the same line (長而不宰) and move together.
- **柔 → soft, 剛 → hard** — 剛 still owed its own mention; 柔 is `covers:`-ed by `ruo-弱.md`.
- **Glossary harvest** from `TRIAGE.md`: 一 is owed only its entry, then 名, then 希. **This sweep adds 身, 氣, 靜, 君, 士, 智, 事, 志, 谷, 恃.**
- **Guodian G2–G6** (`PLAN.md`). G1 closed 2026-08-28.

---

## Tier 5 · The harness

1. **Two proposed rules remain unbuilt** — `incomplete-draft` and `glossary-self-check` (`PLAN.md`). **Neither would have caught most of what the 2026-08-28 sweep found.** What would:
   - a **thin-translation** heuristic — English words per Chinese character against the book's own median. It ranks ch 36 (0.88), ch 11 (0.98), ch 3 (1.03), ch 7 (1.04) at the bottom, and all four turn out to have dropped material. **The only rule here that finds *absence*.**
   - **`repeated-formula` should name the segment's own English**, not the closest line by token overlap. Its 67% "mismatches" at 22/66 are line-break artifacts, while the real four-line divergence at 4/56 never surfaces.
   - **forbidden lists are thin on near-synonyms** — *clever* is not on 明's, *depletion* is not on 殆's, *energy* is not on 氣's.

   **And a measurement for `glossary-self-check`, taken 2026-08-30.** Running every lock's `forbidden:` list over the prose docs — `method.md`, `overlay-audit.md`, `AGENTS.md`, `README.md`, `CLAUDE.md`, `ARCHITECTURE.md`, `CONTRIBUTING.md` — returns **66 hits, of which 65 are the document quoting a forbidden word in order to forbid it.** `overlay-audit.md`'s whole table is a list of words not to use; `AGENTS.md` has a Never column. **A naive scan of these files would be 98% noise**, which is exactly the design note already in `PLAN.md`: the rule must scan only an entry's *own* English — the `> *…*` gloss lines, `render:`, and the "Where it stands" table — and leave the argument around it alone. The one true finding was in `process/method.md`, which rendered 玄牝 (*xuán pìn*) as *"the mysterious female"* where 玄 is locked to **dark**; fixed the same day.
2. **`concordance.py --english` is the only instrument that looks in the reverse direction, and it should be run on every lock.** Pass A found two two-way violations no rule can reach: 固 at ch 55 and 壯 at ch 30 and 55 had borrowed 強's English **inside chapters that contain 強**, so the evidence gate that makes the checker trustworthy is exactly what blinds it.
3. **The false-friend `info` list is 70 items and is not being read.** Almost all are ordinary English. Consider suppressing the ones that recur book-wide so the list stays scannable.
4. **`tools/import_commentary.py` mis-splits chapters when a chapter heading sits mid-block.** Wang Bi's ch 18 currently carries ch 19's lemmas.
5. **`build.py` stays deferred** until the text stops moving.

---

## Chapter status, all 81

**Clean** *(no finding beyond the Tier 4 open calls)* — 5, 15, 18, 19, 20, 22, 30, 33, 38, 40, 42, 46, 52, 53, 55, 56, 59, 60, 61, 62, 64, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81

**Needs a swap** — 1, 2, 6, 7, 9, 12, 14, 17, 21, 23, 25, 27, 34, 37, 43, 44, 45, 47, 48, 49, 50, 51, 54, 57, 58, 63, 65

**Needs a chapter-level rewrite** — 3, 4, 8, 10, 11, 13, 16, 24, 26, 28, 29, 31, 32, 35, 36, 39, 41

*Chapters 5, 15, 18, 19, 20, 30, 33, 38, 42, 52, 55, 59, 68 moved up during Passes 0–B. Ch 38 retains two debts (Tier 1 §4); ch 15 retains 士 (Tier 2 §3); ch 30 retains 佐 (Tier 1 §18); ch 68 retains 配天 (Tier 1 §21) — they are listed clean only where this file says otherwise above.*

---

## Closed — the ledger

*One line each. The reasoning lives where the pointer says; it is deliberately not repeated here.*

| Closed | What | Where the reasoning lives |
|---|---|---|
| 2026-08-10 | The first hand sweep, ~40 chapters, every lock then settled | `PLAN.md` → *What the building taught* |
| 2026-08-12 | Ch 27 無棄人 · Ch 48 closing stanza · Ch 31 吉事/凶事 · Ch 7 故能成其私 | `notes/translation.md` |
| 2026-08-12 | 無事 as a licensed split — *meddle* / *serve* | `glossary/shi-事.md` |
| 2026-08-14 | 善 → **masterful**, *good* only where the text names the category | `glossary/shan-善.md` |
| 2026-08-11 | Ch 21 *source code* · Ch 29 *sacred system* · Ch 40 用 · Ch 25 域 · Ch 14 無物 and 有 · Ch 2 *eternally* · Ch 23 *winds down* | `notes/translation.md` |
| 2026-08-26 | 恃 → *rely on*, freeing *presume* for 敢 — ch 2, 10, 51, 34 | `glossary/gan-敢.md` |
| 2026-08-26 | Ch 52 守柔曰強 → *the soft* | `glossary/ruo-弱.md` |
| 2026-08-27 | Ch 22's 不自X stanza rebuilt; 抱一 → *one thing* | `notes/translation.md` · Ch 22 · `glossary/yi-一.md` |
| 2026-08-28 | **Pass 0** — five text bugs (ch 5, 8, 39, 42, 59) | this file's git history |
| 2026-08-28 | **Pass A** — 強 → **strong**, completing the four-word table; 力 covered as *force* | `glossary/qiang-強.md` · `notes/translation.md` |
| 2026-08-28 | **Pass B** — 仁 → **humaneness**, 慈 → **tenderness**, 孝 → **devotion** | `glossary/ren-仁.md` · `glossary/ci-慈.md` |
| 2026-08-28 | **G1** — the ch 19 Guodian fork recorded as facts | `sources/variants.yaml` · `notes/manuscript.md` · Ch 19 |
| 2026-08-28 | **T3-1** — ch 24 rewritten as ch 22's mirror; 物 → *living things*; ch 31 swept | `chapters/024.md` · Notes · `notes/translation.md` |
| 2026-08-28 | **T2-15, four of six** — 是謂玄德 (10) · 故能成其大 (34) · 可以長久 (44, 59) · 猶難之 (63, 73) | `notes/translation.md` |
| 2026-08-30 | **T2-12** — 以此 → *"By this."* in all three; 2 stale notes corrected; 2 standing principles added | `notes/translation.md` · `notes/manuscript.md` · `DISCOVERIES.md` · Ch 21/54/57 |
| 2026-08-30 | **T2-13** — 故去彼取此 → ch 72's line in all three; `"gut"` locked onto 心; *embrace* freed from 取 | `notes/translation.md` · `glossary/xin-心.md` · Ch 12/38/72 |
| 2026-08-30 | **T2-14a** — 難得之貨 → *rare goods*; **貨 locked to *goods***, new entry; ch 44 swept off 富's *wealth* | `glossary/huo-貨.md` · `notes/translation.md` · Ch 3/12/44/64 |
| 2026-08-30 | **T2-14b** — 信不足焉 → *"Where trust runs short, there is no trust"* in both; ch 23's waiver removed | `notes/translation.md` · `glossary/xin-信.md` · Ch 17/23 |
| 2026-08-31 | **T2-14c** — 挫其銳…同其塵: ch 4 takes ch 56's nouns and couplets; *brilliance* breach closed; subject deferred to T1-2. **Closes the eleven named mirrors; PC stays 🔶 for T2-9/10/11** | `notes/translation.md` · Ch 4/56 |
| 2026-08-31 | **T5-8 · T5-9** — `check_worklist.py` (16 tests); atlas gated in CI; `build_graph.py` made deterministic | `tools/check_worklist.py` · `tools/build_graph.py` · `.github/workflows/checks.yml` |
| 2026-08-31 | **T2-11** — 殆 → **danger** ×5, one-to-one; ch 16's 没身 mistranslation; ch 25's 周行 restored; ch 15's invented danger removed | `notes/translation.md` · Ch 15/16/25/32/44/52 |
| 2026-08-31 | **T2-10** — 襲 → *covered* (27, 52); the 襲/習 fork found and recorded | `sources/variants.yaml` · `notes/manuscript.md` · `notes/translation.md` · Ch 27/52 |
| 2026-08-31 | **T2-9 → Pass C ✅** — 辯 → *argue* (45, 81), 訥 → *halting*; 巧 spun off as T2-20 | `notes/translation.md` · Ch 45/81 |
| 2026-08-31 | **T1-5** — ch 23's bare 德 off 玄德's word; the 道/德/失 triad restored | `chapters/023.md` |
| 2026-08-31 | **T1-2 → Pass D begins** — ch 4 rebuilt; **帝 locked**, new entry; 或/若 fork logged; T2-14c closed | `glossary/di-帝.md` · `notes/translation.md` · `notes/manuscript.md` · `sources/variants.yaml` · Ch 4 |
| 2026-08-31 | **T1-3** — ch 3's closing movement rebuilt: 使 causatives restored, 治 at both ends, 為無為 unified with ch 63, 敢 and 常 applied. New standing principle: ***collocation carries a verdict***. 無為's forbidden list widened | `notes/translation.md` · `glossary/wuwei-無為.md` · Ch 3 |
| 2026-08-31 | **T2-2 (ch 3)** — 智者 → **the knowers**; *cunning* off the chapter; the 智者/知者 fork and the 民 restoration in the third clause both recorded | `sources/variants.yaml` · `notes/manuscript.md` · `notes/translation.md` · Ch 3 |
| 2026-08-31 | **T1-4** — ch 38 rebuilt: 失 restored as the chapter's spine, *clutches* (=執, absent) out, one English for 上 · 首/始 · 華/實, 以為 as the 2×2 grid, 大丈夫 → *the great person*. Opens **T4-7** (rank and gender) and T2-21 (厚) | `notes/translation.md` · `notes/manuscript.md` · `sources/variants.yaml` · `glossary/wuwei-無為.md` · Ch 38 |
| 2026-09-01 | **T1-7 · T1-15 · T1-16 · T3-5 · T2-15** — ch 28 de-abstracted: **rooster/hen** (forced by 牝/牡), 谷 → *valley*, 制 → *cutting* · 割 → *severs*, 守 → *hold to*, 常 restored ×3, the template unbroken; ch 22 unified on 為天下式 | `notes/translation.md` · `notes/manuscript.md` · Ch 22/28 |
