# Contributing

*You are welcome here, and you do not need to read Chinese.*

This is a translation of the Tao Te Ching built from the classical Chinese, and
it is dedicated CC0 — public domain, no rights reserved. You owe it nothing. But
if you want to make it better, there is real work to do, and some of it needs
exactly the thing a reader has and a translator loses: **fresh ears.**

---

## First, the honest part

**One person decides.** I translate this book and I make the final call on every
line. That is written into the repository as a mechanism, not a mood — see
[`process/shaloms-call.md`](process/shaloms-call.md). A pull request here is a
**proposal to an editor**, not a change to a commons, and some proposals will be
declined for reasons of consistency you could not have known about.

I would rather tell you that now than have you discover it after an afternoon's
work.

**What that buys you in return:** disagreement is genuinely wanted. The
repository's own operating instructions say the most valuable thing a
collaborator does is *help me see what I cannot see*, and that pushback is worth
more than agreement. Several settled readings in this book exist because someone
said "that word feels wrong" and was right. When you say a line is off, that is
treated as a research assignment, not a complaint.

**Nothing here is urgent.** This is a decades-long reading. Take your time or
never come back; both are fine.

---

## Four ways in, easiest first

### 1. Tell me a line doesn't land — no Chinese needed

**This is the most useful thing most people can do, and the least done.**

I have been inside this text for so long that I can no longer hear it cold. You
can. If a line reads awkwardly, sounds like a fortune cookie, sounds like a
sermon, or simply thuds — say so. You do not need to know why, and you do not
need a fix.

Open an issue with the chapter number and the line. That is a complete
contribution.

*Especially wanted:* anywhere the English sounds like **church**. This edition
strips theistic and moralistic overlays deliberately — "Heaven" for 天 (*tiān* —
sky), "virtue" for 德 (*dé* — integrity) — because the standard English Tao Te
Ching was largely built by missionaries and the register sank into the words. If
a line would sit comfortably in a hymn, I want to know.

### 2. Fill a gloss gap — a little Chinese, or a good dictionary

**389 of the book's 798 characters have no English gloss in this repository.**
87 of them appear three or more times. Every one is a small, self-contained,
genuinely useful contribution.

See [`data/characters.csv`](data/characters.csv) — sort by `occurrences`, filter
`gloss_source` to `none`. Or browse the
[character atlas](https://claude.ai/code/artifact/a2210810-87d7-4144-bdd0-137149c339bd),
which shows what each character is built from.

A further 365 carry `gloss_source: apparatus` — working approximations harvested
from the source tables, not decisions. Several are wrong. 義 (*yì*) is currently
glossed **"and"**, which is simply an error; it means *duty / righteousness*.
Finding those is valuable.

### 3. Check a rendering against the Chinese

If you read classical Chinese, the deepest contribution is the one the tools
cannot make: **is this line right?**

Useful starting points, all of them open questions logged in
[`WORKLIST.md`](WORKLIST.md):

- **民 (*mín* — the governed) versus 人 (*rén* — a person).** One decision, whole
  book, deliberately deferred. Chapter 57 currently renders 人 two different ways
  two lines apart.
- **Em-dashes in the verse.** 32 chapter files still contain them. Some are good;
  some hide a missing subject, which is the specific reason the style forbids
  them. Each is a conversation, not a sweep.
- **正 / 奇** — the *straight / crooked* thread across chapters 57–58, unsettled
  by chapter 78. The character currently carries five different Englishes.

### 4. The tooling

Everything is **Python 3, standard library only** — no install step, no
dependencies, by design. Clone and run:

```bash
python3 tools/check_locks.py          # the gate: every rule, whole book
python3 tools/concordance.py 明        # every occurrence, with its evidence
python3 tools/build_db.py --verify    # rebuild the corpus database
python3 -m unittest discover -s tools/tests
```

Two known gaps if you want something concrete: **87 characters have no 說文解字
entry** matched to them, mostly because the dictionary files them under an older
graph and the mapping is unverified (see `SHUOWEN_VARIANTS` in
`tools/import_shuowen.py` — additions must be *verified against the vendored
text*, never guessed). And a `glossary-self-check` rule is specified but unbuilt
in [`PLAN.md`](PLAN.md): the locks are enforced against the manuscript but never
against the glossary entries that define them.

---

## House rules that will save you a round trip

**Every Chinese character gets an English rendering beside it, every time** — in
issues, in PRs, in commit messages. `為 (wéi — "to do / to handle")`, never a bare
為. This is the loudest rule in the project because I do not read Chinese
fluently, and unglossed Chinese silently converts a question into one I cannot
answer.

**Never call the sage "he."** Use *they/their*, or recast. Applies to every
archetypal figure.

**Lowercase everything but the Tao.** English capitals confer status and turn a
word into a doctrine — *the sage*, *the mother*, *the uncarved*, never *the Sage*.
道 keeps its capital as a proper name; nothing else does.

**Consult sources for meaning, never for phrasing.** Pre-1931 public domain only,
and no modern translation belongs in this repository for any reason. If you are
proposing a rendering, it must come from the Chinese.

**Cite evidence, not intuition — for the argument.** A rendering claim wants the
characters, the older witnesses, or a classical commentary behind it. But *"this
sounds wrong"* needs no evidence at all: that is a finding, and running it down
is my job.

**Trailing whitespace in `.md` is load-bearing.** The translation is verse, and
line breaks are two trailing spaces. Do not let your editor strip them —
`.editorconfig` guards this. Run `python3 tools/fix-linebreaks.py --check`.

---

## Practical

Before opening a PR that touches the manuscript:

```bash
python3 tools/fix-linebreaks.py --check
python3 tools/check_locks.py
python3 -m unittest discover -s tools/tests
```

CI runs the same three. If `check_locks.py` flags something you believe is
correct, do not delete the rule — either waive the single finding with a
`<!-- lock-ok: rule · reason -->` comment in that chapter's `## Notes`, or say so
in the PR and I will make the call.

**Issues are for anything.** Questions, doubts, a line that bothers you, a
character you looked up and found interesting. You do not need a solution to open
one.

**Discussion also happens on Substack** —
[shalomormsby.substack.com](https://shalomormsby.substack.com/) — where the
writing about *why this text still matters* lives. If a conversation there turns
into something the manuscript should answer for, I will bring it here and credit
you by name.

---

## On attribution

CC0 means you owe me nothing, and it means the same in reverse: contributions are
released into the public domain too. If your suggestion changes the text, I will
name you in the notes — not because the license requires it, but because it is
the truth about how the reading was arrived at, and this project logs how it got
where it got.
