# RETROFIT — consistency debt

*Terms settled later in the book oblige changes to chapters drafted earlier. **Policy: fix on discovery, not in a deferred batch.** Mechanical term-swaps are applied immediately; lines needing a rewrite are proposed first, then applied.*

**Status: swept 2026-08-10. Every lock is clear across all 61 drafted chapters. 1 open item, and it is a literary question rather than a lexical one.**

Each chapter file carries its own debt in frontmatter (`retrofit: [...]`), regenerated after every sweep, so this file and the chapters cannot drift apart.

---

## Open — needs your call

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

## Lessons for `tools/check_locks.py`

Three failure modes this sweep exposed. Build the checker against them:

1. **Match stems, not whole words.** `\beternal\b` misses "eternal**ly**" — which hid two chapters. Use `eternal`, `everlast`, `illuminat`, `righteous`.
2. **Case-sensitivity cuts both ways.** A case-insensitive scan flags "the one" (correct) as "the One" (wrong), and a case-sensitive one misses "The cosmos" at the start of a line. The checker needs per-rule case policy, not one global flag.
3. **Homophones and false friends are the real trap.** 常 (*cháng*, constant) vs 長 (*cháng*, long); 自然 (*self-so*) vs the ordinary English word "nature"; 一 (*one*) vs the English pronoun "one"; "Block the openings" (塞) vs "uncarved block" (樸). **Every flagged line must be verified against the Chinese in its own chapter before it is changed** — roughly a third of this sweep's initial 93 flags were false positives.
