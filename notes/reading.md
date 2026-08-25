# Reading Notes

*One of three notes layers. This one is **reader-facing**: interpretive notes that illuminate the meaning or structure of a passage for someone reading the finished text.*

---

## Using this file

**What goes here — and what does not.**

| Layer | Holds |
|---|---|
| `notes/manuscript.md` | textual forks between witnesses |
| `notes/translation.md` | our own rendering decisions and standing principles |
| **`notes/reading.md`** ← this file | **reader-facing interpretation; cross-cutting Threads** |

Reserve this layer for what illuminates **meaning** for the reader. A textual variant belongs in the Manuscript Notes; a word-choice belongs in the Translation Notes. A note here may *cite* either, but its subject is what the passage says.

**How it is ordered.**

| Level | What it is |
|---|---|
| `##` | one of the two sections below |
| `###` | a **Thread** (a motif running across chapters), or a chapter, written `Ch N · <title>` |

1. **Threads** — motifs that run across the book, and belong to no single chapter.
2. **Chapter notes** — **ascending by chapter number**.

**Three rules that keep it that way.**

1. **New chapters are inserted in number order, never appended.** Chronology is git's job.
2. **The locks apply here too.** These notes are prose *about* the translation and they quote it constantly, so a stale rendering here contradicts the verse. `check_locks.py` scans only `chapters/` and cannot see this file — four violations survived here undetected until the 2026-08-11 restructure (*ten thousand things*, *mysterious female*, *heaven and earth*, *uncarved block*). **When a lock changes, sweep this file by hand.**
3. **Mark research leads with ⟡** so the ones worth an essay can be found. The strongest graduate to `DISCOVERIES.md`.

---

## Threads

### Thread · The mother and her kin (the feminine)

Read the book once for its feminine imagery alone, and a single figure rises through it chapter after chapter — the generative power of the low, the empty, the yielding, the receptive, which Laozi calls, without embarrassment, *female*. Four names carry the thread:

- **母, the mother** (1, 20, 25, 52, 59) — the source that bears the countless things, that the sage nurses from (食母, 20), and that one returns to and holds fast (復守其母, 52). *See her own entry.*
- **玄牝, the dark female** (6) — the cosmic womb: "the valley spirit never dies; this is the dark female. Her gate is the root of sky and earth." Chapter 6 is the thread's densest knot, binding *valley* + *spirit* + *female* + *gate* + *root* in six lines.
- **雌, the female** (10, 28) — the receptive role the sage is told to *keep to*: "know the male, but hold to the female, and be the valley of the world" (28) — which then flows straight on to the *infant* (嬰兒) and the *uncarved* (樸).
- **谷, the valley** (6, 15, 28, 32, 39, 66) — the feminine topography: the low, hollow, empty place that, precisely by being lowest and emptiest, receives everything and gives without end. The valley holds more than the peak.

And these four gather a wider family: the **infant** (嬰兒 / 赤子 — 10, 20, 28, 55), the mother's fruit; **water** (水 — 8, 78), soft and low and life-giving; the **soft and yielding** (柔弱 — 36, 76, 78), which outlasts the hard; and **stillness** (靜 — 61, where "the female overcomes the male through stillness").

Here is why the thread matters, and why it is easy to miss. Laozi wrote in a world that prized the masculine — the assertive, the hard, the high, the full, the striving. He inverts the whole ladder. The female outlasts the male; the valley holds more than the summit; the soft defeats the hard; the low is where power pools; the one who *bears and releases* is stronger than the one who *grasps and rules*. This is not a scattering of pretty images. It is the load-bearing structure of the book's entire idea of power — and for centuries it was quieted by translators who preferred a sterner Way. To follow the mother and her kin from chapter to chapter is to watch Laozi build his most radical claim in plain sight: that the source of all strength is not the fist but the womb.

*(On what this is and isn't: the exaltation of 雌, 牝, 母, 柔 is a valorizing of the receptive-generative* mode *— an ethical and cosmological stance — not a social program about women. But the stance is real, unusual for its era, and central; we let it stand where the text places it: at the center.)*

### Thread · Reading past the throne — and past the male default

⟡ *research lead; may be worth a chapter of its own*

The Tao Te Ching exalts the feminine as a **principle** — 母 (*mǔ* — mother), 牝 (*pìn* — the female animal), 雌 (*cí* — the female bird), 谷 (*gǔ* — valley), 柔 (*róu* — the yielding) — while assuming, as a text of its age, two cultural defaults it never argues for: that the exemplary person is **male**, and that the exemplary agent is a **ruler**. This edition reads past both, and notes the seam each time. Gathered here because the seam has a pattern, and the pattern may be the more interesting subject.

**Where the manuscripts side with us.** Ch 25's four greats: our base text reads 王 (*wáng* — king), but **both Mawangdui silks read 人** (*rén* — human), and the older silk has no king anywhere in the passage. The received text then contradicts itself one line later with 人法地 ("humans follow earth"). So on the book's most famous cosmological ladder, the throne appears to be a **later overlay**, and the older reading is the universal one. *("Overlay," not "interpolation": 王 standing where 人 stood is a substitution, not inserted material — and it names the same phenomenon this project already names in the translation layer. See `DISCOVERIES.md` §1.)* *(Apparatus in the Manuscript Notes; rendering in the Translation Notes.)*

**Where we universalize on our own authority, and say so.** Ch 16's 公乃王 becomes *"impartiality leads to sovereignty"* — a quality, not a monarch. Ch 55's 朘 (*zuī*), specifically the infant boy's member in the older witnesses, is read through our base text's 全 (*quán* — whole) as *"their whole being quickens with life,"* keeping the emblem available to infants of every gender. Ch 62's 天子 becomes *"a child of the sky"* — the title kept, the *Son* dropped, since the graph is a swaddled infant with no sex in it. Every 聖人 (*shèng rén* — the sage) takes singular *they*.

**Where the text needs no help.** Ch 61 makes the most explicit case for feminine power in the book — 天下之牝 ("the female of the world"), 牝常以靜勝牡 ("the female always overcomes the male through stillness") — and argues it entirely with 牝 / 靜 (*jìng* — stillness) / 下 (*xià* — below), without one syllable of 陰 (*yīn*). 陰 appears **once in all 81 chapters**, in Ch 42, paired with 陽 (*yáng*), and never as the feminine principle. The popular yin-yang framing of Laozi is imported.

**The questions worth a chapter.** Is 王 even a person? The graph is read as an axe-head, the emblem of authority — or as three horizontals (sky, human, earth) crossed by one vertical: **the one who joins the three realms**, a *function* rather than a sex or a station. The *Shuowen Jiezi* (~100 CE) glosses 王 as 天下所歸往, "that to which the world turns," which is a description of gravitational pull, not of a man on a seat. And if the throne is an overlay in Ch 25, where else? The book is addressed to rulers throughout — 侯王 (*hóu wáng* — lords and kings) in 32 and 37, 治國 (*zhì guó* — governing the state), 聖人之治 (the sage's governing). How much of that is Laozi, and how much is the text's transmission through court libraries by scribes for whom the reader was self-evidently a prince?

### Thread · Nobody is written off — and it is not forgiveness

⟡ *research lead; three chapters already, and it may be four or five*

**Three chapters make one claim in three different vocabularies, and none of them is about mercy.**

> **Ch 27** · 常善救人，故無**棄**人 — *always masterful at rescuing people, and so no one is **abandoned**.*
> **Ch 49** · 善者，吾善之；**不善**者，吾亦善之 — *the good, I am good to; the **not good**, I am also good to.*
> **Ch 62** · 人之**不善**，何**棄**之有？ — *when a person is **unmasterful**, why **abandon** them?*

They interlock on their own vocabulary. 棄 (*qì* — abandon) binds 27 to 62; 不善 (*bù shàn* — not-good, unmasterful) binds 49 to 62. **And Wang Bi ties 27 to the others himself**, glossing its line: 聖人…不造進向以殊**棄不肖** — *"the sage does not create tracks of advancement that single out and discard **the unfit**."* 不肖 (*bù xiào* — the unworthy, those who don't measure up) is Ch 62's 不善人 in another word.

**What makes the thread worth an essay is what it refuses.** The obvious Western frames are *forgiveness* and *mercy*, and neither fits — both presuppose a ledger. Forgiveness cancels a debt; mercy waives a penalty; each requires you first to have written the entry. **These chapters decline to open the account.** Ch 49's sage has 無常心, *no fixed heart*, and so has nothing to sort people into. Ch 27's sage does not build the ranking apparatus (Wang Bi's 進向, tracks of advancement) that would produce a discard pile. Ch 62 does not pardon the unmasterful; it asks what abandoning would even consist of. And **Ch 63**'s 報怨以德, *repay resentment with integrity*, is the same refusal one step further out — it declines to price a grievance that has already landed, which is exactly the accounting Confucius defends in *Analects* 14.34 when he insists on 以直報怨, proportion.

**Why the 善 = "masterful" reading matters here.** Held as *good/bad*, this is a doctrine of grace toward sinners and the whole thread collapses into Christian charity. Held as *masterful/unmasterful*, it is a claim about **competence and use**: Ch 27 goes straight on to say the masterful are the teachers of the unmasterful and the unmasterful are their 資 (*zī* — raw material, stock-in-trade), and that failing to value either is 大迷, great confusion. **Nobody is discarded because nobody is waste.** That is an argument from resourcefulness, not from pity — and it is why Ch 27 puts it beside a locksmith and a knot-tier.

**The seam is now closed.** 善 reads **masterful** in all three chapters as of 2026-08-14, so the thread rests on one word. Ch 49's 吾善之 is 善 used as a **verb** — *to reckon as 善* — and renders *"I count as masterful,"* which is appraisal rather than kindness: the sage is not being nice to the incompetent, they are refusing to run the grading. **Wang Bi tied the chapters together himself**, glossing Ch 49's 德善 with 無棄人也 — Ch 27's own line — and closing that chapter with 資 (*zī* — raw material), the character Ch 27 gives the unmasterful. See `glossary/shan-善.md`.

**Where it may still reach.** Ch 79 (和大怨, *reconciling a great resentment*) is undrafted and belongs here. So, possibly, does Ch 41's 不笑不足以為道 — the laughter of the lowest sort of student, which the text takes as confirmation rather than as grounds for dismissal.

---

## Chapter notes

### Ch 16 · The ladder out of the self

The chapter closes on a chain in which each rung is the first word of the next — 知常**容**，**容**乃**公**，**公**乃**王**，**王**乃**天**，**天**乃**道**，**道**乃久. The links are the form, and the climb has one direction: **each rung widens the circle beyond the self.**

*Capaciousness* (容) is the ability to hold what comes without shutting it out — still a quality of a person. *Impartiality* (公) turns that outward; the character is the direct opposite of 私 (*sī* — private, selfish), and it means the public, the common, what belongs to no one in particular. *Sovereignty* (王) is impartiality with reach: no longer just fair, but responsible for everyone. Then the ladder leaves the human world entirely: **the open sky** (天) is impartiality made total — 天無私覆, *the sky covers without partiality*, over the just and the unjust alike, owned by nobody. And past even that, *the Tao* — and only then 久, **the enduring**, arriving last, as a result rather than a goal.

What makes the chain worth following is where it starts: 知常, *knowing the ever-present*. Not with an ethical resolution to be fair, but with seeing how things actually move — out and back, root and return. Fairness is not the first step here; it is what happens to someone who has watched the cycle long enough to stop taking their own position as the center. And endurance is not sought at all. It is what is left over at the top of a ladder built entirely out of letting go of preference.

*(The same 天 → 道 step reappears in Ch 25's ladder — 地法天，天法道 — which is why both must read "sky.")*

### Ch 28 · The road that only runs forward — 復歸於樸

Chapter 28 tells you three times to go back: 復歸於嬰兒, *return again to the infant*; 復歸於無極, *return again to the limitless*; 復歸於樸, *return again to the uncarved.* Each is impossible in the plain sense. No one becomes an infant again. And wood does not un-carve — once the log is bowls and wheels, no craft on earth makes it a log.

Laozi never explains, and the honest reading has to sit with that. But the chapter's own closing line suggests where the answer lies: 大制不割 — *the greatest shaping does no severing.* If the great cut leaves nothing cut, then what is being asked is not the restoration of a former shape. It is the loosening of your identification with the shape you were cut into — the bowl remembering it was never only a bowl. The wood is still wood. The carving went only as deep as the form.

Read that way, the three returns are not nostalgia for a lost condition but a change in where you stand: still holding a function, no longer *being* it. Which is also why Chapter 57's people can "become plain of themselves" (民自樸) without anyone unmaking them. Nothing was undone. They simply stopped being handled.

### Ch 29 · 神器 — the sacred vessel is a bronze, and it was already lost

⟡ *research lead, to develop*

天下神器 (*tiān xià shén qì*) is usually read as an abstraction — the world is sacred, do not meddle. But 器 (*qì*) is a concrete object, and in the late Zhou a **神器** was concrete indeed: the **ritual bronzes**, above all the 九鼎 (*jiǔ dǐng* — the **nine cauldrons**), legendarily cast by Yu the Great and passed from dynasty to dynasty as the visible warrant of the mandate to rule. To hold the cauldrons was to hold the world. 神器 later comes to mean the throne itself.

So Ch 29 opens on 將欲**取**天下 — *wishing to **seize** the world* — and answers: the world is a sacred vessel, 不可執, **it cannot be grasped**. To a contemporary ear that is not a metaphor. It is a sentence about reaching for the cauldrons.

**Two things make this sharper than a passing allusion.**

**A near-contemporary text asks exactly this question and gives Laozi's answer in Laozi's vocabulary.** In the *Zuo Zhuan* (*Xuangong* 3, **606 BCE**), King Zhuang of Chu masses troops on the Zhou border and asks after "the size and weight of the cauldrons" — 問鼎, which becomes the idiom for coveting a throne. The Zhou envoy Wangsun Man answers: **在德不在鼎** — *"it lies in 德, not in the cauldrons."* **德** — the word this edition locks as **integrity**. Two texts of the same era, one in court and one in verse, both saying the vessel is not the thing.

**And the nine cauldrons were themselves lost in the late Zhou** — vanished, their whereabouts unknown by the time Qin unified in 221 BCE. The supreme sacred vessel disappeared precisely amid the grasping for it. 執者失之: *those who grasp it lose it.* The chapter's warning had already come true, in the most literal way available, within living memory of its composition.

**To develop.** Shalom has stood in front of Zhou bronzes at the Smithsonian and was moved by them — the patterns, and the meanings worked into them. That is the right way into this note: the 饕餮 (*tāotiè*) mask, the 雷紋 (*léi wén* — thunder pattern), the inscriptions cast *inside* the vessel where only the ancestor and the spirits would read them. A vessel whose most important writing faces inward is a good emblem for a chapter about not grasping. Worth expanding for the companion volume, and worth checking against the *Zuo Zhuan* passage in full.

### Ch 50 · The empty tenth

Laozi counts three groups, each "three in ten" (十有三): those who live out their natural span; those who die young; and those who — though alive — drive themselves onto deadly ground by clinging too hard to life. That is nine-tenths. The tenth is never named — yet it is exactly where the master of life stands: the one with *no death-ground* (無死地), who has slipped the ledger of living-and-dying altogether. The form enacts the sense. A figure defined by *absence* — no foothold for death — is fittingly left in the tally's empty place: uncounted because uncatchable.

This rests on hearing 十有三 as "three in ten," which reads naturally in the parallel. But it is worth knowing that the oldest surviving commentary on the *Laozi* — Han Feizi's *Jie Lao* (韓非子·解老, 3rd c. BCE) — heard the number as **thirteen**: the body's four limbs and nine orifices (四肢九竅), the thirteen gates through which life is spent and death enters. On that reading there is no missing tenth at all; the passage is anatomy, not arithmetic. We keep the "three in ten" sense for its plainness and for the beautiful vacancy it leaves — but the empty tenth is our inference, not Laozi's statement, and an ancient ear heard other music in the number.

### Ch 55 · The newborn who takes no harm — an emblem, not a promise

蜂蠆虺蛇不螫，猛獸不據，攫鳥不搏 — venomous creatures do not sting the newborn, fierce beasts do not seize it, birds of prey do not strike. Read as a literal claim, this is simply false: a wasp stings a peaceful baby; a leopard does not pause to check its 德. Laozi is not writing zoology — he is painting the same emblem as **Chapter 50**, the master of life whom rhino, tiger, and blade cannot harm 以其無死地, *because there is no death-ground in him.* The newborn *is* that figure: a being of such total harmlessness and non-contention that it offers **no target**, and so is simply not in harm's way — a truth about the *state of perfect harmony* (和), not a survival guarantee for babies. There is a naturalistic seed (calm, unafraid, non-aggressive harmlessness provokes less attack; fear and threat are what trigger the strike), but the figure far exceeds the seed. So read it as *emblem*, not fact: the infant is the image of the harmonious, targetless state — the same 無死地 as the master of 50.

### Ch 57 · The two lives of 正 — order imposed, and order arisen

The chapter opens and closes on the same character, 正, and the distance between its two appearances is the whole teaching. It begins as a *method of rule* — 以正治國, "govern the state with uprightness," the straight and correct applied from above — and it ends with no ruler applying anything: 我好靜而民自正, "I love stillness, and the people right themselves." Same word, opposite motion. First, 正 is imposed; last, 正 arises.

Everything between the two argues the point. The first half is a catalogue of imposition backfiring — the more taboos, the poorer the people; the more laws proclaimed, the more thieves — every attempt to carve order into the world breeding its own opposite. The second half is the reversal: when the ruler will not act, will not meddle, wants nothing, and above all grows *still*, the people transform, right, enrich, and grow plain — 自, of their own accord. Order was never something to install; it was something to stop preventing. That is the bookend's quiet claim: you do not make people upright by being upright *at* them. You grow still, and the uprightness that was in them all along comes up by itself — the way plainness (自樸) does in the very next breath.

### Ch 58 · Fortune and disaster, folded together — and why nothing stays "right"

The chapter's heart is one of the most quoted lines in the book: 禍兮福之所倚，福兮禍之所伏 — "disaster is what fortune leans on; fortune is where disaster hides." It is built as a mirror on purpose. Disaster is fortune's *support*, the ground it rests against (倚, to lean); fortune is disaster's *hiding place*, the covert it crouches inside (伏, to lie in wait). Neither is a place you can arrive at and hold. Each already carries the other — the good luck resting on the very thing that will undo it, the ruin already nested inside the thing you are celebrating.

Then Laozi presses past luck into judgment itself: 孰知其極？其無正 — "who knows where it ends? It has no fixed norm." Nothing in the reversal stays put — not even the categories we most trust: 正復為奇，善復為妖, the straight turns crooked, the good turns monstrous. And here 58 quietly dismantles 57. There you governed the state *with* the straight and waged war *with* the crooked (以正治國，以奇用兵), sure of the difference; now the straight turns crooked of its own accord — the very norm you ruled by becomes the deviance you opposed. The line you built policy on will not hold still. This is why the people have been 迷 (lost) so long: they keep clutching a fixed "good" and a settled "right" in a world where these keep changing into their opposites.

The sage's answer is the four closing lines — square but not cutting, edged but not wounding, straight but not overreaching, bright but not dazzling. Not weakness: the only sane response to a world of reversals. If sharp virtue flips into its opposite (as 察察, the sharp-eyed ruler, bred crafty people), then keep the edge without the cut — hold the straight without honing it into a blade that gouges, the light without the glare that blinds. The sage does not press their correctness on the world, precisely because pressed correctness is what curdles into its opposite. Integrity held softly is the one thing the reversal cannot turn.

### Ch 62 · A sanctuary the size of a corner

The chapter opens by saying where the Tao is, and the answer is domestic. The word is 奧 (*ào*), and it names **the southwest corner of a house** — the innermost corner, furthest from the door. In a Zhou-era home that corner was the household's altar space: where the presiding spirit of the house was honoured and where the head of the family sat. Confucius refers to it in exactly that way, in a proverb about whether it is smarter to court the spirit of the honoured corner or the spirit of the kitchen stove.

So it is a sanctuary — but a sanctuary you could reach in three steps, in the one room you live in. Not a temple. **The Tao is not above the house. It is in it, in the part of the room you do not use for traffic.** That single image does more against the theistic overlay than any argument: the standard English renderings reach for *mystery* and put the Tao in a fog, or reach for *sanctuary* and build it a cathedral, when the Chinese has it where the winter grain and the family tablets are. This edition keeps the word *sanctuary* and gives the corner back here, because the two together are the thought.

The commentators split on which property of that corner matters, and the split is worth keeping. Heshang Gong hears a **storehouse** — *"there is nothing it does not hold."* Wang Bi hears **shade** — *"a word for what one can get shelter under."* Hold, or shelter. Both are things a corner does and a temple does not.

**And the whole chapter is built on that domestic scale.** Its centre of gravity is the moment where the state assembles its highest ceremony — raising up a child of the sky, installing the three ministers, jade discs too wide for one pair of arms carried in procession ahead of a team of four horses — and the text answers: **better to sit where you are and offer this Tao.** They stand a ruler up; the reply is to sit down. The corner of the room against the throne room.

Then it closes by naming what the ancients valued in it, and the answer is startlingly unspiritual: *seek and you find; have a crime against you and you are spared.* Heshang Gong reads that entirely literally — a chaotic age, a benighted ruler, punishments and executions inflicted at random. Not sin, not absolution. **A person with the law after them, and a way of not being killed.** Which is the older English sense of *sanctuary* too: not a holy building but the right of the pursued not to be seized. The chapter is about who gets abandoned, and its answer is nobody.

### Ch 62 · What "a child of the sky" was claiming

The phrase now reads as an image, and it is worth knowing that to Laozi it did not. 天子 (*tiān zǐ* — "child of the sky") was the standard official title of the Zhou ruler for some five hundred years before this book. In his mouth it was ordinary — as ordinary as *Prime Minister*, which is made of "first" and "servant" and which nobody hears. **The strangeness readers feel in "a child of the sky" is a recovered literalism, not a riddle.** Worth naming as a translation cost as well as a gain: we have flipped the ratio between office and picture. This is the one chapter where that trade is clearly worth making, because the chapter exists to shrink the office.

**What the title claimed.** The Zhou had overthrown the Shang, whose kings claimed descent from their own high god 帝 (*dì*). Their answer to the obvious objection changed Chinese thought permanently: legitimacy is **not inherited from an ancestor-god**; it is granted from overhead, and it can be **withdrawn**. Hence *child* — subordinate, provisional, answerable, disownable. The grandest available claim and a leash in one phrase, and every dynasty that later fell, fell officially because the sky took it back. **"Son of Heaven" communicates none of this**; it sounds permanent and inherited, which is exactly what the Chinese was minted to deny.

**And "sky" is truer to the theology than "Heaven", not merely more literal.** The Shang's 帝 was a **person** — an ancestor one petitioned and satisfied with sacrifice. What the Zhou put in his place was not: 天 is the overhead, impersonal and silent, responding to conduct rather than to offerings. Rendering it *Heaven* re-personalizes precisely what a revolution had de-personalized, and puts the ancestor-god back on his seat.

**What Laozi does with it is almost nothing, and that is the point.** He does not attack the title, deny the mandate, or call the ruler illegitimate. He lists the most impressive things a society can stage — the enthronement, the three ministers, the treasure borne in procession — and observes that sitting still beats them. No polemic, only a change of scale. Which is why the grandeur has to be genuinely grand on the page.

**The real turn, and the chapter's joke.** Follow the genealogy honestly. Ch 25: the human follows earth, earth follows the sky, **and the sky follows the Tao** — the sky is a rung, not a summit — and the Tao is 先天地生, *born before sky and earth*, so the sky is itself a child. Trace the ruler's line one step past the sky and you arrive at the **mother**, which by this book's flat insistence rules nothing: 生而不有 (*"gives birth without possessing"*, 10 and 51), 萬物歸焉而不為主 (*"the countless things return to it, yet it does not act as their master"*, 34). **The title claims descent from authority; the book's own cosmology, followed to the end, delivers descent from something that refuses authority.**

**And the manuscripts push it further.** At that same ladder in Ch 25, both Mawangdui silks read 人 (*rén* — human) where our base text reads 王 (*wáng* — king). If the four great things include the **human** and not the monarch, then being a child of the sky was never a royal privilege. Everyone is. The exclusivity was the accretion. *(See `DISCOVERIES.md` §1 and §3, which this note sits between.)*

*(A small thing, and real: 子 is the character that ends Laozi's own name — 老子, "the old child," universally read "the Old Master." The word that makes a ruler the sky's dependent is the word that makes a philosopher a teacher.)*

### Ch 63 · The line Confucius refused

⟡ *research lead; likely a `DISCOVERIES.md` candidate*

報怨以德 (*bào yuàn yǐ dé* — "repay resentment with integrity") is not a general sentiment. It is one side of a named argument, and the other side is in the *Analects*.

**Analects 14.34:**

> 或曰：「以德報怨，何如？」
> 子曰：「何以報德？以直報怨，以德報德。」
>
> Someone said: *"Repay resentment with 德 (dé — integrity) — how about that?"*
> The Master said: *"Then with what would you repay 德? Repay resentment with 直 (zhí — uprightness, the straight), and repay 德 with 德."*

Confucius is not proposing 以德報怨. **He is quoting it in order to reject it** — the 或曰, "someone said," marks it as a saying already in circulation, put to him by another. And his objection is not softness; it is **accounting**. If integrity is what you spend on your enemies, you have nothing left that means anything when you meet a friend. He substitutes 直 (*zhí*) — the straight, the level, the proportionate response. Answer a wrong with what the wrong actually merits.

**Chapter 63 takes the position he refused, and states it as bare instruction.** No question, no interlocutor, no defence. Four characters.

Two things make this more than a coincidence of phrasing. **The saying predates both texts** — 或曰 tells us Confucius was answering something already abroad, which means Ch 63 is not answering Confucius so much as both are answering the same older line, from opposite ends. And **Mawangdui A puts 報怨以德 in this chapter**, so it cannot be dismissed as a late intrusion by an editor who had read the *Analects* and wanted to score a point (see the Manuscript Notes).

**Why Laozi's answer is not simply the softer one.** Confucius's objection assumes 德 is a **finite currency** — spend it wrongly and you are short. Everything this edition has found in 德 says otherwise: it is not a stock of merit but a *condition* — what a thing is when nothing is bent in it (see `glossary/de-德.md`). You cannot run out of being uncrooked. Under that reading, 以直報怨 and 以德報怨 are not two settings on a dial of leniency. They are two different theories of what integrity **is**. Confucius's answer is the correct one if 德 is earned and allocated; Laozi's is the only possible one if 德 is simply how you stand.

**And the chapter's placement argues for it.** 報怨以德 arrives one line after 為無為 (*wéi wú wéi* — do the not-doing). Proportionate retribution is a *hand on the elephant*: it requires you to weigh the offence, price the response, and administer it. Answering from 德 requires none of that machinery, which is precisely why it belongs in this chapter and not in a chapter about kindness.

**And it pairs with Ch 62.** Both chapters ask what is owed to someone who has done wrong, and both answer by refusing to run the ledger — 62 by declining to abandon the unmasterful, 63 by declining to price the grievance. *(Worth developing for the companion volume. The 直 / 德 contrast in particular is a clean way into what this edition means by* integrity*, stated by an opponent who understood it well enough to object.)*

### Ch 64 · the journey begins where you are standing

The best-known sentence in the book outside Chapter 1 is, in English, an inspirational one: *a journey of a thousand miles begins with a single step.* The Chinese does not say that. 足下 is **under the foot** — not a step taken but the ground already beneath you.

Read the three proverbs together and the correction is obvious. A tree wide enough to need both arms around it is born from **a hair's tip**. A nine-tiered terrace rises from **a heap of dirt**. A thousand-mile journey begins **beneath your feet**. Small, low, near. Heshang Gong glosses them in exactly those three words: 從小成大, 從卑至高, 從近至遠. Nothing in the set is about resolve. Everything in it is about the thing being still tiny, still close, still catchable — which is the argument of the chapter's opening, that what has not yet cracked into a sign is easy to plan for.

The step-version quietly moves the emphasis from *where you are* to *what you do*. That is the reverse of the chapter, which ends by telling the sage not to push at all.

### Thread · take your hand off it — Ch 63 and Ch 64 are one argument in two halves

These two chapters share a grammar and split a claim. Ch 63 opens 為無為，事無事，味無味 (*do the not-doing, serve the not-serving, taste the flavorless*); Ch 64 answers with 欲不欲 (*want the not-wanting*) and 學不學 (*learn the not-learning*). Five instances of the same move: take the verb, negate its object, and hand the result back as a practice.

Wang Bi supplies what the move is **for**. Glossing 學不學 he writes 不學而能者自然也 — *"what one is capable of without learning is what is so of itself."* The not-learned is not ignorance; it is the part of you that already works. So the whole construction points at 自然 (*zìrán* — so of itself), and the chapter's last line says so outright: 以輔萬物之自然，而不敢為 — support the countless things in being so of themselves, and never push them.

That is the ground of non-doing stated as plainly as the book states it. You can take your hand off the thing because the thing goes of itself.

### Ch 64 · the seam at "those who handle it ruin it"

The chapter turns without warning. Six lines of practical counsel about catching things early, three proverbs about small beginnings — and then 為者敗之，執者失之, *those who handle it ruin it, those who grasp it lose it*, which appears verbatim in Chapter 29 and argues something close to the opposite: don't handle it at all.

The join may be physical. Chapter 64 is the one chapter the Guodian bamboo slips carry **twice**, its opening span and its closing span in different bundles. Whether or not the received chapter is two sayings sewn together, the tension is real and worth leaving open: *act early* and *do not act* are not the same instruction, and the chapter offers no bridge between them. What it offers instead is a scale. Early enough, and handling is barely handling — it is a hand on a hair's tip.

### Ch 66 · the sage never climbs — they sink, and are carried

The chapter inverts the direction of elevation, and the hinge is one verb: 推 (*tuī* — to push). **The world pushes them forward.** They do not rise; they are raised, and only because they went down first.

The image is hydraulic and it needs no metaphysics. Rivers and seas are king of the hundred valleys for one reason — they lie lower, and water goes where water goes. Nothing is commanded. 善下之 (*shàn xià zhī*) makes lowness an *act* and not a condition: 下 is a verb here, and 善 is the lock's *masterful at*. The sea is not passively low. It is skilled at being low.

Then the political translation, in a pair worth noticing: to be above the people you go below **in speech** (以言下之), and to be ahead of them you put **your self** behind (以身後之). 言 (*yán* — word) and 身 (*shēn* — body, person). Humility in what you say; deference in where you stand. Two different organs of the same movement.

河上公 gives the consequence an image the English should not lose sight of: 民戴而不為重 — *"the people **carry them on their heads**, and it is not a weight."* 戴 (*dài*) is specifically to bear on the head, the way a load is carried in a village. The leader is not on a throne above the people; they are on the people's heads, and light enough that nobody minds.

### Thread · going low — Ch 8, Ch 61, Ch 66

One argument, made three times, in three registers, and the book never names it as a doctrine.

- **Ch 8, in water.** 上善若水 — water benefits the countless things without competing, and *dwells where the crowd will not go*. The ethical register.
- **Ch 61, in the feminine.** 大國者下流 — the large state is the downstream flow, and 牝常以靜勝牡, the female overcomes the male by stillness. The erotic and diplomatic register. Argued entirely with 牝 (*pìn* — female animal) and 下 (*xià* — below), with no 陰 anywhere.
- **Ch 66, in hydraulics.** Rivers and seas rule the valleys by lying beneath them. The political register, and the plainest of the three: no gender, no ethics, just the fact that water goes down.

The through-line is 下 — *below* as an action you take. Read together they say the same thing about power that Ch 64 says about timing: the effective move is the one that costs nothing because it goes with what already happens. And all three end in the same place, which is Ch 66's last line and Ch 22's: **because they do not compete, no one can compete with them.**

### Ch 65 · the chapter that gets Laozi called an authoritarian

This is the chapter people quote to show that the Tao Te Ching is a manual for keeping subjects docile — *"the ancients did not enlighten the people but kept them ignorant."* Four things are wrong with that sentence, and three of them are in the Chinese.

**1. 明 here is not clarity, it is cunning.** Wang Bi glosses it in the chapter itself: 明謂多見巧詐，蔽其樸也 — *"明 means seeing much and artful deceit, screening over their uncarved."* Not the 明 of Ch 33's *"to know oneself is clear-seeing."* Nobody is withholding insight.

**2. 愚 is what the sage claims for themselves.** Ch 20: 我愚人之心也哉 — *"I have the heart of a fool!"* — said as a boast. The ruler here is not pushing the people below themselves; they are bringing everyone to where the sage already stands.

**3. The chapter's target is the ruler's cleverness, not the people's.** This is the part that gets missed, and Wang Bi spells out the mechanism as an escalation spiral: 以智術動民，邪心既動，復以巧術防民之偽，民知其術防，隨而避之 — *"use clever technique on the people and their crooked hearts stir; once stirred, you use more artifice to guard against their deceit; the people learn the technique and evade it in turn."* Each round of official cleverness manufactures the popular cleverness it was meant to contain. 以智治國，國之賊 — **the thief of the state is the clever ruler.** The people are hard to govern because they have been taught to be.

**4. And the honest caveat.** Strip all three and something still stands: 非以明民 does say *do not make the people knowing*, and the chapter nowhere distinguishes manipulation from learning in general. Laozi is genuinely suspicious of sophistication as such — Ch 19's 絕聖棄智 and Ch 48's *"in pursuit of learning you increase daily"* say the same thing without the political framing. **This edition does not rescue that.** What it declines to do is translate a suspicion of cleverness as a policy of enforced ignorance, when both classical commentators read it the other way and the sage applies the word to themselves.

### Ch 20 · the loneliest chapter, and it opens with a joke

Chapter 20 is the one place the book sounds like a person rather than a position — 我 (*wǒ*, the self seen) appears seven times, and every appearance is a complaint. But it opens in comedy, and the comedy is the argument.

**唯 and 阿 are both ways of saying yes.** One is the assent you give a superior; the other is the grunt you give a friend. 河上公: 同為應對 — *"both are ways of answering."* And the question is: 相去幾何, how far apart are they? Then immediately: and good and bad, how far apart are *those*? The joke sets the trap. If you concede that the gap between *yes sir* and *yeah* is trivially small, you have already conceded something about the gap between good and bad — which is the distinction the entire apparatus of learning exists to police. That is why 絕學無憂 stands at the head: **abandon learning and there is no worry**, because the worry was manufactured by the distinctions.

王弼 gives the mechanism, and it is one of the best lines in his commentary: 自然已足，益之則憂 — ***"what is so of itself is already enough; add to it and you get worry."*** He illustrates it with 續鳧之足，何異截鶴之脛 — *"lengthening a duck's legs: how does that differ from cutting short a crane's shins?"* Both are improvements. Both are injuries.

**Then the chapter refuses its own consolation.** 人之所畏，不可不畏 — *what people fear must be feared*. Wang Bi does not soften it: 故人之所畏，吾亦畏焉 — *"what people fear, I fear too."* The speaker has seen through the distinctions and is **still afraid**, and says so before saying anything else about their own state. No enlightenment is claimed. That single line is what keeps the rest of the chapter from being a boast.

**And then the long descent**, in which every term of praise is inverted. The crowd is at the feast; the speaker is an infant who cannot yet smile. The crowd has more than enough; the speaker has missed out. The worldly are bright and sharp; the speaker is dark and dull. Muddled. Stubborn. Coarse.

The last word is where it resolves, and it resolves without arguing: 而貴食母 — *I prize feeding from the mother.* Everyone else is at the great feast, 太牢, the ox-sacrifice. The speaker is at the breast. Not a lesser meal — the **first** one, the one that comes before food is something you choose. 王弼: 食母，生之本也, *"the feeding mother is the root of what lives."*

*(See the feminine thread: this is 母 as sustenance rather than origin, and it is the same mother as Ch 1's 萬物之母 and Ch 52's 天下母, met at the point of contact rather than described.)*

### Ch 67 · the first treasure is a mother's love, and it wins wars

Laozi names three treasures and puts **慈 (*cí*)** first — then returns to it twice more, which he does for neither of the others. It is the most emphatic thing in the chapter and the English tradition has quietly neutered it.

慈 is not compassion. It is what a parent feels for a child, and Chinese marks the direction: in the pair 孝慈, 孝 runs **up** from child to parent and 慈 runs **down** from parent to child. 慈母 is how you say *loving mother*. Heshang Gong will not let it float free either — his gloss on the first treasure is 愛百姓若赤子, *"loving the people as newborn infants."*

So the book's first treasure is **maternal love**, named as such, in a chapter about war.

**And the chapter claims it is the strongest thing there is.** 慈故能勇 — from tenderness, courage. 夫慈，以戰則勝，以守則固 — fight with it and you win, defend with it and you hold. That is not a metaphor and the commentators do not treat it as one. 王弼: 相慜而不避於難，故勝也 — *"they feel for one another and do not shirk danger, therefore they win."* 河上公: 百姓親附，并心一意 — *"the people draw close, joining hearts into one intent."* Both are describing unit cohesion. **An army whose people love each other does not break**, and armies are lost when they break.

The chapter then names the failure mode with unusual violence. 王弼 glosses the particle 且 as 取, *to grab*: 今捨慈且勇 is **abandon tenderness and grab at courage** — courage taken directly, without the love it was supposed to come from. Same for reach without frugality, and the front without the rear. The verdict is two characters: 死矣. *That is death.*

Read with the feminine thread, this is the sharpest instance in the book. Chapter 61 argues that the female overcomes the male through stillness. Chapter 6 makes the valley spirit 玄牝, the dark female, the root of sky and earth. **Chapter 67 puts a mother's love at the head of a list of what makes a state survive a war** — and then says that a state which trades it for courage is already dead.

*(See also the reading note on Ch 66: rivers and seas rule by lying beneath. The three treasures are the same argument in another register — tenderness, frugality, and refusing to go first are all ways of being underneath.)*

### Ch 73 · two directions of courage, and a chapter that admits it does not know

The chapter opens on a distinction English keeps losing: **courage stands on both sides of it.**

> 勇於敢則殺，勇於不敢則活
> *"Brave in pushing, and you are killed. Brave in not pushing, and you live."*

勇 (*yǒng* — courage) is not what separates the two. What separates them is 敢 (*gǎn*) — the forward press to take, the hand going after the boar. Both people are brave. One of them presses forward and dies of it.

That is why *"daring"* cannot carry 敢 here: it makes the second line read as cowardice rewarded, when the Chinese says there is a **bravery in not pressing** which is harder than the other kind. 河上公 puts the target plainly — the thing being refused is 有為 (*yǒu wéi* — having-doing, acting) — which makes this chapter 無為's clearest statement in the language of the battlefield.

**Then the chapter does something rare: it stops and admits ignorance.** 天之所惡，孰知其故？ — *what nature hates, who knows why?* No answer follows in our base text. Both classical commentaries had one more line here — 是以聖人猶難之, *"therefore even the sage finds it difficult"* — and Wang Bi's comment on it is the most humane sentence in his commentary: 夫聖人之明，猶難於勇敢，況無聖人之明而欲行之也 — *"the sage's own clarity still finds this hard; how much more someone without it who means to act anyway."* (See the Manuscript Notes; the line's absence from our base is unresolved.)

**And then the four negations, which are the answer the question did not get.**

> It does not contend, yet is masterful at overcoming.
> It does not speak, yet is masterful at answering.
> It does not summon, yet things come of themselves.
> It is unhurried, yet masterful at planning.

Four refusals, four competences. Nothing here is *doing* anything, and everything gets done — 不召而自來 is 自然 (*zìrán* — so of itself) stated as a fact about arrival rather than a principle.

**The last image is the one to be careful with.** 天網恢恢，疏而不失 — *nature's net is vast; its mesh is wide, and nothing slips through* — became, in later Chinese, a slogan about divine justice catching criminals, and Heshang Gong already reads it that way: 司察人善惡, *"it watches over human good and evil."*

There is no watcher in the Chinese. There is a net with wide holes and nothing getting out. **That is a statement about how consequence works** — loosely, slowly, at a distance, and completely — and it is far more unnerving than surveillance, because nobody has to be paying attention for it to hold.

### Ch 68 · a chapter about war in which nobody fights

Four clauses, each opening on 善 (*shàn* — masterful at), and each one takes the obvious competence and removes what everyone thinks it is made of.

> One masterful as a warrior is not martial.
> One masterful at fighting does not rage.
> One masterful at overcoming enemies does not engage them.
> One masterful at using people puts themselves below them.

王弼 explains the first by pointing at Chapter 67: 武尚**先**陵人也 — *"martiality prizes going **first** and trampling people."* 先 (*xiān* — first, ahead) is the very thing Chapter 67 makes the third treasure of refusing. And he explains the second the same way: 後而不**先**，應而不**唱** — *"behind and not first, responding and not leading off."* 唱 (*chàng*) is to lead off in song, the same word Heshang Gong used for the third treasure at Ch 67, 不為**倡**始.

So Chapter 68 is Chapter 67 put into uniform. Tenderness, frugality and not pushing to the front become: not martial, not enraged, not engaging, underneath.

**And the third clause is the one that startles.** 善勝敵者，不與 — *one masterful at overcoming enemies does not engage them.* Not *defeats them easily*: **does not meet them at all.** 河上公 spells out what replaces the battle — 附近以仁，來遠以德 — *"draws the near with humaneness, brings the distant with integrity"* — and then the outcome, 敵**自**服也, *the enemy submits **of itself**.* The 自 is the same of-itself that runs the rest of the book. Nobody was defeated. The opposition simply stopped being opposition.

**Then the closing triple names it, and the name is a lock we already hold.** 是謂**不爭**之德 — *this is called the integrity of not contending.* 爭 (*zhēng*) is two hands pulling at one object, and this chapter has just spent four lines describing a soldier who never takes hold of the rope.

The last claim is the largest in the book's political vocabulary: 是謂配天 — *this is called being **matched with** nature.* 配 is the word for a spouse. Not obeying nature, not imitating it. Paired with it, as an equal — which is the only place in the Tao Te Ching where a human practice is said to stand alongside 天 rather than beneath it.

### Ch 69 · the war chapter that never lets you win one

Ch 69 completes a run: **30, 31, 68, 69** are the book's military chapters, and not one of them describes a victory worth having. This one is the strangest, because it is built entirely out of a soldier's saying and then takes the saying somewhere no soldier would.

The saying looks prudent: don't start it, give ground. But 河上公 (*Héshàng Gōng*) tells us what its two verbs actually mean, and it is not doctrine at all. 進 (*jìn* — advance) is **crossing another's border to take their things**; 退 (*tuì* — retreat) is **shutting your own gate**. So the inch and the foot are not a measure of nerve, they are an argument: an inch of someone else's ground is not worth a foot of your own. Then Laozi comments, and the comment is not prudent at all. Four gestures of aggression, and each one closes on nothing: the army marches and there are no ranks, the arm bares and there is no arm, the hand hauls and there is no enemy, the fist grips and there is no weapon. This is 無為 (*wúwéi* — non-doing) put in armour. The enemy has not been defeated. The enemy has been **declined**.

And then the last line, which is the one to sit with. When two armies are evenly matched, the thing that decides it is not doctrine, or numbers, or terrain. **It is which side is already grieving.** Not the angrier side, not the more righteous. The side that has understood in advance what is about to happen to everyone.

That is the same claim as Ch 31's *a victory in battle should be treated like a funeral rite*, made earlier — before the battle rather than after it — and turned from an ethic into a mechanism.

**Thread · the treasures.** Ch 67 names three (tenderness, frugality, never first). Ch 69 spends two of them without renaming them: *I do not push to move first* is *never pushing to be first*, and *the one who grieves wins* is *tenderness*. The middle treasure, frugality, is what the retreat is — an inch of ground is not worth what it costs.

### Ch 70 · the chapter that is not complaining

Read cold, Chapter 70 sounds like a grievance: *my words are easy, and nobody follows them.* Almost every English rendering leans that way, and some of them let contempt in. **河上公 (*Héshàng Gōng*) closes that reading off at both hinges, and the last line proves him right.**

On 天下莫能知 (*"none in the world can know"*) he does not say the world is stupid. He says: **人惡柔弱好剛強也** — *"people hate the soft and weak and love the hard and strong."* The obstacle is not comprehension, it is **appetite**. They understood it perfectly well and wanted the other thing. That is a diagnosis the book makes again at Ch 76, where 柔弱 (*róu ruò* — soft and weak) is what living things are and 剛強 (*gāng qiáng* — hard and strong) is what corpses are.

On 夫唯無知 he turns the sentence the other way round entirely: **是我德之暗，不見於外** — *"this is my integrity being unlit, not seen on the outside."* There is nothing on display. Not being known is not a failure that happened to the sage; **it is the sage's own arrangement.**

And then the image, which is the whole chapter compressed: 被褐而懷玉 — **the sage wears coarse cloth and carries jade against the chest.** 褐 (*hè*) is a labourer's sacking; 玉 (*yù*) is jade, held inside the robe. Note that the line is made of layers — a garment word outside, a garment word inside (懷, *huái*, is 心 wrapped in cloth), and the treasure between them. **Nobody dressed the sage in sacking. The sage put it on.**

Which makes Chapter 70 a portrait of the book itself. Plain surface, easy sentences, nothing that glitters — and the reason it is not understood is the same reason it is worth understanding.

**Thread · the three lonely chapters.** `notes/manuscript.md` §6 argues that **20, 67 and 70 are one chapter in three voices**, all first-person, all about being misread by 天下 (*tiān xià* — the world). Chapter 70 is the one that explains the other two. Ch 20: *I alone am stubborn, and look coarse* (似鄙). Ch 67: *everyone says I am vast, and look like nothing* (似不肖). Ch 70 supplies the mechanism both were describing — **looking like nothing is the practice, not the accident.** The English keeps the seam visible: Ch 20's *look coarse* and Ch 70's *coarse cloth*.

### Thread · 希 — the loosely woven cloth

**希 (*xī*) is one character doing one thing in six places, and this edition has been rendering it three different ways without noticing.**

The graph is 爻 (crossed threads) over 巾 (a cloth): **fabric woven so loosely you can see through it.** *Sparse.* Every use in the book is that, applied to a different medium:

| | | |
|---|---|---|
| ch 14 | 名曰希 | sparse **to the ear** → *the inaudible* |
| ch 23 | 希言自然 | sparse **speech** → *speak sparingly* |
| ch 41 | 大音希聲 | the great sound is **sparse of tone** |
| ch 43 | 天下希及之 | sparse **in number** → *few ever reach this* |
| ch 70 | 知我者希 | *those who know me are **few*** |
| ch 74 | 希有不傷其手 | **rarely** without cutting the hand |

Rarity and inaudibility are not two meanings. They are the same property — *thinly distributed* — read once across a crowd and once across a sound. The book's ideal of speech (ch 23) and the book's account of its own reception (ch 70) turn out to be **the same word**: Laozi speaks sparsely, and is sparsely heard.

**And then the couplet does something with it.** 知我者希，則我者貴 — *those who know me are few; those who pattern themselves on me are precious.* 希 (few) is followed immediately by 貴 (*guì* — precious), and the pairing is not accidental: scarcity is where value comes from, an association old enough in Chinese to be proverbial. **河上公 makes the link explicit — 希少也…故為貴也**, *"希 means few… therefore they are precious."* It is the only warmth in the chapter, and it is addressed to whoever is still reading.

**則 is worth a second look, too.** 則 (*zé*) is 鼎 (a bronze cauldron) beside 刀 (a knife): **a law cut into bronze.** Hence "rule, pattern", and as a verb, *to take as one's pattern*. 則我者 is not merely someone who agrees — it is someone who has **cut this into their own metal**. Rendered *"those who pattern themselves on me"* rather than "those who follow me": following is a direction, patterning is a shape.

### Ch 71 · the sickness is not ignorance

Read quickly, this is the Socratic chapter — *I know that I know nothing* — and it gets quoted that way. It is not quite that.

**Nothing here says ignorance is the problem.** The problem is 不知知: the ignorance *plus the claim*. 河上公 names the disease precisely — 強知 (*qiáng zhī*), **forced knowing** — and he names its motive: 妄行強知之爭，以自顯著, *"recklessly practicing the contention of forced knowing, in order to make oneself conspicuous."* 爭 (*zhēng* — contend) is the book's word for the whole grasping posture; **knowledge here is just another arena for it.** The person who claims to know is doing the same thing as the person who climbs, hoards, or fights. That is the finding: this chapter is not about epistemology. It is chapter 8 and chapter 22 applied to the mind.

**And the cure is not humility, exactly.** 夫唯病病 — the sage does not become modest, they become **sick of the sickness**. 河上公 makes the sage's condition sympathetic rather than superior: they are 病苦 (*pained and distressed*) by watching everyone else force it. What keeps them clear is that the spectacle hurts them.

**What the diseased actually lose, on 河上公's reading, is their lives.** His last clause: 内傷精神，減壽消年 — *"inwardly it wounds the vital essence and the spirit; it shortens the span and eats the years."* Claiming to know is not a mere error of manners. It burns something up.

**Thread · 70 → 71, one gesture.** Chapter 70 ends with the sage in coarse cloth, jade **held against the chest** (懷). 河上公 closes chapter 71 with the same verb: 夫聖人懷通逹之知，託於不知者 — *"the sage carries penetrating knowledge against the breast, and lodges it in not-knowing."* The sage **has** the knowledge. Putting it away is the practice. So the first line of 71 is not a confession of emptiness; it is a description of the same concealment 70 just explained — 是我德之暗，不見於外, *"this is my integrity being unlit, not seen on the outside."* Chapter 56 supplies the third side: 知者不言，言者不知. Three chapters, one move.

### Ch 72 · the chapter says why rulers crowd people

Two halves that look unrelated — *do not crowd the people* and *the sage does not display themselves* — and 王弼 joins them in five characters. On 不自貴 he writes **自貴則物狎厭居生**: *"exalt yourself, and things crowd and weary dwelling and living."*

**Self-display is the motive for the crowding.** The ruler presses on the people's houses and livelihoods because they need to be seen doing it. Dread has to be demonstrated or it is not dread; a ruler who has priced themselves high has to keep collecting on the price. Remove 自見 (self-display) and 自貴 (self-pricing) and the pressing loses its engine — there is nothing left it was for.

That is why the chapter's cure is not *govern gently*. It is **自知，自愛** — know yourself, love yourself. A ruler who already knows what they are does not need the people to keep confirming it.

**And the opening line is not a threat, though nearly every English makes it one.** 民不畏威，則大威至 is usually read as *fear my authority, or a greater authority will come.* Both commentators read the opposite: 王弼 has 上下大潰矣 (*high and low collapse utterly*) and 天誅將至 (*the reckoning of nature is coming*); 河上公 has 大害至，謂死亡也 (*the great harm arrives, meaning death*). **When authority stops working, nothing arrives to enforce it for you.** What arrives is the end of the arrangement.

**Nor is it a consolation.** The opposite error is just as available and slightly more seductive: *when people stop fearing authority, true authority arises* — the illegitimate giving way to the legitimate. There is no such thing in the chapter. 至 (*zhì*) is an arrow striking ground, not a dawn. **Coercion has a floor, and the floor is not held up by anything.**

**Thread · the two chapters inside Ch 72.** 其 (*qí* — their/its) has no antecedent, and the commentators supply opposite ones. For 王弼 it is the people's dwelling and livelihood, and the chapter is political. For 河上公 it is **your own** — 其所居 is the heart, where the spirit dwells; 其所生 is the vital essence that keeps you alive; and the offence is not taxation but appetite (飲食不節…邪僻滿腹，爲伐本厭神 — *"eating without restraint… depravity filling the belly: this cuts down the root and crushes the spirit"*). His title for the chapter is 〈愛己〉, **loving oneself**.

We render 王弼, because 民 is the topic of the previous line and 河上公 has to import two characters the chapter does not contain. But he is reading something real: **the second half is four 自 in two lines** — 自知, 不自見, 自愛, 不自貴 — the densest run of *self* anywhere in the book. The chapter opens on the people and closes on the person. His reading is what you get if you take the ending as the key to the beginning, and the ending does invite it. `notes/manuscript.md` has the apparatus.
