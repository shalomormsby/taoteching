# Manuscript Notes

*One of three notes layers. This one logs **textual forks between the witnesses** — where the older manuscripts disagree with our base text in a way that changes what a line says.*

---

## Using this file

**What goes here — and what does not.**

| Layer | Holds |
|---|---|
| **`notes/manuscript.md`** ← this file | **textual forks between witnesses** |
| `notes/translation.md` | our own rendering decisions and standing principles |
| `notes/reading.md` | reader-facing interpretation; cross-cutting **Threads** |

Our base text is the received **Wang Bi** recension (via the Chinese Text Project). Log only the **meaning-bearing** places where the older witnesses — **Guodian** (~300 BCE), **Mawangdui** (before 168 BCE), **Beida** (early Han), and the Tang-era **Fu Yi** text — diverge in a way that changes what a line says or how we have chosen to render it. Purely graphic or particle-only variants are not logged. Entry format: *chapter · the line · the fork · our call.*

**Never transcribe the Mawangdui or Guodian manuscripts.** Record the **fact** of a variant, never a modern editor's reconstruction of a damaged graph. `sources/PROVENANCE.md` explains why this is a licensing rule and not a preference.

**How it is ordered.**

| Level | What it is |
|---|---|
| `##` | one of the two sections below |
| `###` | a chapter, always written `Ch N · <the line or the fork>` |
| `####` | one fork, where a chapter has more than one |

1. **Punctuation and parsing forks** — where no character differs and only the editorial marks do.
2. **Witness forks** — **ascending by chapter number**. Within a chapter, in verse order.

**Three rules that keep it that way.**

1. **⚠ Every chapter heading must contain the literal string `Ch N ` — with a trailing space.** `check_locks.py`'s `unlogged-variant` rule substring-matches exactly that against this file, and fails the build when `sources/variants.yaml` records a fork this file has not logged. A heading reading `### Ch 21` alone, with no space after the number, **silently blinds the check.** Always write `### Ch 21 · …`.
2. **Every entry here should have a matching row in `sources/variants.yaml`**, and its `logged:` field should point back here. The two must not drift; the checker exists to stop them.
3. **New chapters are inserted in number order, never appended.** Chronology is git's job.

---

## Punctuation and parsing forks

*No character differs; only the editorial marks do. The Chinese carries no punctuation, so every mark in every edition is a later editor's.*

### Ch 32 · 道常無名。樸雖小 — where the break falls changes the subject

- **Received:** 道常無名**。**樸雖小，天下莫能臣也。 — *"The Tao is ever nameless. Though uncarved wood is small, nothing can subordinate it."* (樸 is the subject; the wood is what is small.)
- **Ours:** 道常無名**樸。**雖小，天下莫能臣也。 — *"The Tao is ever nameless, uncarved. Though small, nothing in the world can make it a subject."* (無名樸 is a compound attribute of the Tao; **the Tao** is what is small.)

We follow the second, on three grounds. **(1) The parallel with Chapter 37** is near-decisive — both chapters run *道常 + [attribute]*, then the identical sentence about rulers: 道常**無為**。侯王若能守之，萬物將自化 (37) / 道常**無名樸**。侯王若能守之，萬物將自賓 (32). Same frame, same rulers, same self-so outcome. **(2) The pronoun.** 侯王若能守**之** — *if lords and kings can hold **it*** — takes the Tao as its antecedent naturally; under the received parse the nearest antecedent is a piece of timber. **(3) Chapter 34 already says the Tao is small**: 常無欲，可名於**小** — *"ever without desire, it may be named small"* — and, in the next breath, 可名為**大**, *"it may be named great."* Chapter 32 is that claim made a second time; 天下莫能臣也 is a real assertion about the Tao and a puzzle about wood.

*(A side benefit: with 樸 read attributively, the English needs no article, so nothing reifies the uncarved into an object — the same correction made when "block" was retired. See `glossary/pu-樸.md`.)*

### Ch 62 · 美言可以市尊，美行可以加人 — **resolved 2026-08-12: we keep the base text**

**Shalom's call, made against the recommendation.** Both readings are set out here in full, because the evidence is genuinely split and the argument on the losing side is worth preserving.

**The fork.** Our received base divides the line after 尊 and reads 美行 (*měi xíng* — fine conduct), giving a 美 / 美 parallel: *"fine words can buy honor; fine conduct can raise a person above others."* **Both Mawangdui silks**, the **Fu Yi** and **Fan Yingyuan** editions, and **both classical commentaries** instead divide after 市 and read 尊行 (*zūn xíng* — honored conduct). Heshang Gong's lemmas are printed as two separate units — 美言可以市 and 尊行可以加人 — and Wang Bi's comment splits identically, closing each half with its own 故曰 (故曰美言可以市也 … 故曰可以加於人也).

**For the base, which is where we land.** The ***Huainanzi*** (c. 139 BCE) quotes the line **twice**, in 人間訓 and 道應訓, with the 美 / 美 parallel — the oldest *quotation* of the line, against the oldest *manuscripts*. **Yu Yue** and **Zhu Qianzhi** both followed it. And the split camp is not unanimous: **Fu Yi reads 尊言, not 尊行**, so the witnesses that agree against our base do not agree with each other.

**The case against this call, recorded so it stays available.**

**1. Lectio difficilior.** Our base is the **smooth** reading — fully parallel, 美 answering 美. The split is **rough**: an asymmetric pair with 市 (*shì* — market) left standing alone as a bare verb. In a text this full of parallel couplets, a copyist meeting the rough reading has an obvious motive to regularize it and none to break a clean parallel, so the drift would run from the split toward our base rather than the reverse.

**2. Wang Bi's text contradicts Wang Bi's commentary**, and that is a documented systematic feature of this recension — some seventy-nine places where the Laozi transmitted *over* the commentary differs from readings quoted *inside* it, the received text having been supplanted by Heshang Gong-line readings. On that reasoning the text Wang Bi actually had read the split, and our base is later here than the commentary printed above it.

**What the call changed.** The verse, which had been drafted on the split. Chapter 62 now reads *"Fine words can buy honor. / Fine conduct can raise a person above others."* The line's function is unaffected either way — fine words and fine bearing have purchase, therefore no one is beyond reach, therefore 何棄之有.

**Still open, and a different question:** the line's **tone**. Heshang Gong reads it as a put-down (美言者獨可於市耳 — *"fine words are good for the marketplace, and that is all"*), Wang Bi as praise of the Tao, and Ch 81 will say 信言不美，美言不信. That is a reading question, not a textual one, and it lives in the Translation Notes.

---

## Witness forks

### Ch 21 · 道之為物 / 道之物 — the silks drop the copula

Our base reads 道之**為**物，惟恍惟惚. Both Mawangdui silks read **道之物** with no 為, leaving 之 as a plain possessive: *the Tao's thingness*, rather than *the Tao's being a thing*. **Both point at the same sense**, so the reading is not in doubt — but the fork is worth logging because it settles what the line's **topic** is: not the Tao itself but *what the Tao amounts to as an entity*, which is a topic-comment construction and wants topic-comment English. Hence *"Whatever the Tao is, it is only vague, only elusive."* We keep the base text; nothing turns on 為. (The silks also read 唯 for 惟 and 望/朢 for 恍 — graphic and phonetic variants, not meaning-bearing.)

#### 自古及今 / 自今及古 — the direction of the inquiry

Our base reads 自**古**及**今** ("from ancient times until today"). **Both Mawangdui silks** read 自**今**及**古** ("from **now back to** antiquity"). **We keep the base text**, and log the fork because it is genuinely meaning-bearing: it reverses the direction of the inquiry. Mawangdui makes the chapter *start* from the present and trace backward; Wang Bi makes it *arrive* at the present. We render the arrival — the line ends on "today," and the closing "By this, here, now" completes the movement toward the reader, which is the movement of the whole chapter.

The same two lines carry two more forks. 以**閱**眾**甫** against the silks' 以**順**眾**父** (順 = *follow along with*, not *observe*) — we keep 閱; and 甫/父 needs no decision, since Ch 42 already settled that 父 here means *origin / root*, not "godfather," and both give "origin" in English.

#### 眾甫之狀 / 眾甫之然 — **resolved 2026-08-11: we follow 然**

Our base reads 眾甫之**狀** ("the *shape* of that origin"); four independent witnesses read **然** ("that it *is so*") — both Mawangdui silks, the Song Heshang Gong edition, and the Siku Quanshu compilers' own collation note on this very line, 〔案狀各本俱作然〕, *"for 狀, all editions read 然."*

**We follow 然**, and the decisive argument is not a manuscript one: 吾何以知…然哉？以此 is a **fixed closing formula** that Ch 54 and Ch 57 both use, so 然 completes it and 狀 breaks it. Full reasoning in the Translation Notes; `our_call: mawangdui-a` in `sources/variants.yaml`. The base text and Source table keep 狀; only the translation follows the witnesses, as at Ch 41, 42, 47 and 53.

*(An earlier version of this note ended "marked `undecided` pending Shalom's call." That was stale — the call was made and the apparatus records it. Corrected 2026-08-11.)*

The same Siku file carries a second collation note, 〔案此二句一本在下二句之下〕, recording a **line-order** variant: in one edition the 象 couplet follows the 物 couplet rather than preceding it. Logged, not acted on.

#### What the commentators say 此 means — and our line holds both

The two oldest commentaries gloss 以此 differently, and the English *"By this, here, now"* happens to carry both. **Wang Bi:** 此上之所云也 — *"'this' is what was said above,"* the whole descent through 象 / 物 / 精 / 信. **Heshang Gong:** 此今也 — *"'this' means **now**,"* glossing on to 以今萬物皆得道精氣而生 (*"because now the countless things all obtain the Tao's essence-qi and live"*). Heshang Gong's reading also independently supports the Mawangdui 自今及古 direction, from the opposite end of the tradition. *(Both quoted from `sources/commentaries/`.)*

### Ch 25 · 王亦大 / 人亦大 — king or human among the four greats

Our base reads 故道大，天大，地大，**王**亦大 ("the **king** is also great") and 域中有四大，而**王**居其一焉. **Both Mawangdui silks read 人 (*rén* — human) in the list of four**, and the older silk (甲本, c. 200 BCE) reads 人 in *both* places — 天大地大**人**亦大 … 而**人**居一焉. Silk B (乙本, c. 175 BCE) is caught mid-drift: 人 in the list, 王 in the line after. **We follow 人**, rendering *the aligned human*.

Two further points. **The received text contradicts itself:** Wang Bi's own next line is 人法地 ("humans follow earth"), so the received recension makes the *king* one of the four greats and then instantly makes *humans* the bottom rung of the ladder. The silks are internally consistent; the received text is not. And **域 / 國** is a second fork in the same line — our base reads 域中 (*yù zhōng* — within the domain), both silks read 國中 (*guó zhōng* — within the state). Both are spatial and "within the realm" serves either, so it is logged rather than decided. *(Note also 有物**混**成 / 有物**昆**成 — a graphic variant only, both "merged, undifferentiated"; not meaning-bearing.)*

*This is `DISCOVERIES.md` §1.*

### Ch 41 · 大器晚成 / 免成 — late, or never

Received: 晚成, "completed **late**." Mawangdui reads 免成, Guodian reads 曼成 — both "**never** completed / free of completion." We follow the manuscript reading — *"the great vessel is never completed"* — because it completes the parallel with its neighbors (無隅 / 希聲 / 無形, each "the great X *lacks* its defining mark"). Flagged here rather than decided in silence.

### Ch 42 · 教父 / 學父 — father of teaching, or of learning

Received: 教父, "father of **teaching**." Mawangdui reads 學父, "father of **learning**." We follow 學父 — *"this I take as the root of learning"* — the bolder reading, and the older one in the silk. (Two further points on this line: 父 here means *origin / root*, not "godfather"; and there is no possessive in the Chinese — it is "the root of learning," not "of *my* learning." The 吾 is only the one who adopts it.)

### Ch 46 · 禍莫大於不知足 — the manuscripts remember a third clause

The received text gives **two** calamity-clauses: 禍莫大於不知足 (no *disaster* greater than discontent) / 咎莫大於欲得 (no *fault* greater than the desire to acquire). Mawangdui and the Fu Yi text open the run with a **third, prior** line: **罪莫大於可欲** — "there is no greater **crime** than desire" (可欲, "the desirable," the same phrase as Ch 3's 不見可欲). So the older witnesses remember a rising three-beat — **crime**/desire → **disaster**/discontent → **fault**/greed — that the received text trimmed to two. We keep the received pair, noting the manuscripts' fuller crescendo.

### Ch 47 · 不見而名 / 不見而明 — the homophone fork

Received: 不見而**名** (名, *to name / discern*) — "without seeing, discerns." Mawangdui reads 不見而**明** (明, *clarity / be clear*) — "without seeing, understands clearly." We follow **明**: it completes the parallel (*know / see-clearly / accomplish*, each without its usual means) and reads cleaner than 名 here. Worth noting the fork falls between two of our own glossary entries — 名 (the name / ledger) and 明 (clear-seeing) — the homophone pair, both *míng*.

### Ch 53 · 是謂盜夸 / 盜竽 — the boast, or the lead-pipe

Received: 盜**夸** (dào kuā) — "the *swagger* / boast / extravagance of thieves." The Mawangdui silks read 盜**竽** (dào yú), and the oldest commentary on the *Laozi*, Han Feizi's *Jie Lao*, reads it so too. 竽 is the great reed mouth-organ that *led* the ancient ensemble; in Han Feizi's own words, "when the *yu* leads, the bells and zithers all follow; when the *yu* sounds, every instrument falls into harmony with it." So 盜竽 is not the *boast* of thieves but their **lead-pipe** — the tone-setter, the ringleader whose tune the whole band of lesser thieves plays along to. We follow **竽**: the gleaming ruler is not merely a loud thief but the chief one, the head the country's thievery falls in behind. (The variant sharpens the charge, too — 夸 accuses him of showing off; 竽 accuses him of *leading the theft*.)

### Ch 55 · 全作 / 朘作 — the newborn's quickening

**Correction, 2026-08-11:** this note previously said our base text reads 而**全**作. It does not — **our source table reads 而朘作**, the Mawangdui and Fu Yi reading, while the verse renders 全 (*"their whole being quickens with life"*). The received Wang Bi reading is indeed 全, as the Siku Quanshu printing confirms (`sources/commentaries/wangbi/055.md`). So the verse follows 全, the source table shows 朘, and the note had misdescribed both. Found by the commentary import. The rendering stands; only the account of where it came from was wrong.

Received Wang Bi: 而**全**作 — 全 = *whole, complete* — "yet it quickens wholly." The older **Mawangdui** and **Fu Yi** texts read 而**朘**作, where 朘 (zuī) is specifically *the infant boy's member* — an explicit male erection. The traditional gloss takes both as the reflex erection (全 as a decorous stand-in for 朘). We keep our base text's **全** and read it in its plain sense — *the whole being quickens with life* — which preserves the point (精之至: desireless potency arising from fullness) while keeping the emblem universal, for infants of every gender. (See the paired Translation Note, and Process guide §0 on the incidental male-default.)

### Ch 61 · 邦 / 國 — the Han name-taboo

Where our received base reads 國 (*guó* — state) seven times in this chapter, the Mawangdui silks read 邦 (*bāng* — state). This is the systematic Han substitution avoiding the personal name of the founding emperor Liu Bang (劉邦), and it runs through the received text wherever 邦 stood. Meaning-neutral, logged once here rather than at every occurrence.

#### 則取大國 — active, not passive

Received: 小國以下大國，則**取**大國 — *"a small state, by going below a large state, then **takes** the large state."* The Chinese carries no passive marker, yet most translations render the second half passively ("is taken by the large state"), and some editions supply 於 (取**於**大國) to license it. We keep the **active** reading in both halves. The chiastic repetition is the argument: the same move, made by either party, acquires the other. Heshang Gong reads it so as well, glossing the pair as the large state gaining the small state's goodwill and the small state gaining the large state's favour. Making the second half passive restores exactly the ordinary power relation this chapter exists to invert.

### Ch 62 · 奧 / 注 — the chapter's first word is not in the oldest witnesses

Both Mawangdui silks read **注** (*zhù*) where our base text reads **奧** (*ào*). Gao Ming's *帛書老子校注* takes 注 as a loan for **主** (*zhǔ* — master, lord), giving *"the Tao is the master of the countless things"*, and supports it from outside the *Laozi*: Zheng Xuan glosses 奧 as 主 in his commentary on the *Liji · Liyun* (奧猶主也), and the *Zuozhuan* (Zhao 13) has 國有奧主, *"the state has its 奧主."* So 奧 and 主 are not far apart in Han usage, and the emendation is the mainstream scholarly reading.

**We keep 奧, and the reason is internal.** Chapter 34 denies the mastery reading twice, in the identical two words: 衣養**萬物**而不為**主** and **萬物**歸焉而不為**主** — *"it clothes and feeds the countless things yet does not act as their master"; "the countless things return to it yet it does not act as their master."* A Ch 62 that reads 道者萬物之主 puts the book in flat contradiction with itself on 萬物 and 主, the same pair of words in both places. That is a heavy price, and the variant does not require us to pay it: 注 at face value is 氵 (water) beside 主 and means **to pour into**, which gives *"what the countless things pour into"* — a confluence image, sitting one chapter after Ch 61's 大國者下流 (*"the large state is the downstream flow"*) and 天下之交 (*"the confluence of the world"*), and answering Ch 32's 猶川谷之於江海. And Gao Ming's own chain runs through a room: 奧 can mean *master* only because the 奧 corner is where the household head presides. **The place is the older layer of the word, and both witnesses keep the place. Only the dominion is optional, and Ch 34 forbids it.**

#### 善人之寶，不善人之所保 — two forks, and one of them undoes a note

(1) Our base uses **two different graphs** — 寶 (*bǎo* — treasure), then 保 (*bǎo* — to keep safe). **The silks use the same graph twice**, and published transcriptions disagree about which one, a disagreement that is itself modern editorial work rather than a fact about the silk. So the received text's elegant pair may be a **later differentiation of a single word**, and the Translation Note that treated it as an original piece of wordplay has been corrected accordingly. (2) Separately, Dunhuang manuscripts, Yan Zun and Zhao Zhijian read 不善人之所**不**保 — *with a negation* — while Yan Kejun reports all editions reading 所保. We keep the base text: the negation would make the Tao what the unmasterful **fail** to keep, which contradicts the 何棄之有 three lines later.

#### 天子 stands in the silks

立天子 is present in the Mawangdui text, so the title is **not** a later accretion of the kind found at Ch 25, where our base reads 王 (king) and both silks read 人 (human). The grandeur is Laozi's own, put there to be knocked down. This settles the question left open when the chapter was drafted; see the Translation Notes on 天子 → *"a child of the sky,"* and `DISCOVERIES.md` §3.

#### 三公 / 三鄉 — the silks name the office with the word that means minister

Where our base reads 三**公** (*sān gōng*), the silks write 三**鄉**, which editors read as a loan for 三**卿** (*sān qīng* — the three high ministers). Not meaning-bearing, and logged only because it settles an English question: 公 is conventionally rendered *duke*, a borrowed European rank, and the oldest witness calls the office by the word that simply means **minister**. Our rendering turns out to be the older reading's own word.

#### Apparatus note · Wang Bi's commentary on this chapter is filed under Chapter 61

`tools/concordance.py --commentary 62` reports Wang Bi as *not vendored*, and the importer lists 62 among ten chapters whose Siku transcription is unproofread. But the text is present: the Siku printing runs Chapter 62 on into Chapter 61's block, opening with the chapter heading and the compilers' own collation note 〔案河上公注本此為為道章〕 (*"in the Heshang Gong recension this is the chapter titled 為道"*), and the whole of Wang Bi's Ch 62 commentary follows inside `sources/commentaries/wangbi/061.md`. Ch 62 was drafted with it. **The importer's chapter-splitting needs a look** — wherever else a chapter heading sits mid-block, the same thing will have happened. Logged in `RETROFIT.md`.

### Ch 63 · 報怨以德 is native to this chapter, not a stray from Ch 79

The line 報怨以德 (*bào yuàn yǐ dé* — "repay resentment with integrity") has long been suspected of being a fragment displaced from Ch 79, which is the book's other chapter on grievance (和大怨 — "reconciling a great resentment"). **Mawangdui A has it here**, in this chapter, immediately following 大小多少. So its placement is as old as our oldest witness to it, and the argument it picks with the *Analects* (see the Reading Notes) is the chapter's own and not an accident of transmission.

#### 夫輕諾必寡信 — damaged in both silks

The 輕諾 / 寡信 line is broken in both Mawangdui manuscripts; B preserves only fragments of the span between 輕 (*qīng* — light) and 信 (*xìn* — trust), with graphs missing. Our reading of it therefore rests on the **received text alone**, and so does the *trust* rendering of 信 at this line. Worth stating rather than rendering as though the witnesses concurred. (We record the fact of the damage and not any modern reconstruction of the lost graphs — see `sources/PROVENANCE.md`.)
