# Shalom's call — the override of record

*Shalom decides. This file is where a decision to **set aside one of this repo's own rules** is written down, so that it survives the session in which it was made.*

**Read this at session start, alongside `CLAUDE.md` → *Current state*.** Every rule in this repository — the standing rules, the locks, the ordering in `PLAN.md`, the checks in `tools/check_locks.py` — is subject to a call recorded here. Where a call is in effect, **the call wins**, and the AI says so once and proceeds. It does not re-argue a decision already made.

The division of labor is the point:

> **The AI argues *before* the call. It executes *after* it, without relitigating.**

Argue hard beforehand — that is the prime directive, and a call made against a weak argument is a worse call. Once made, it is made.

---

## How a call works

**Only Shalom makes one.** The AI may *draft* an entry when Shalom makes the call, and must then act on it. The AI never writes a call on its own initiative, and never cites one it wrote unprompted.

**A call suspends; it never deletes.** The rule stays where it is written. The call sits here beside it. A future reader sees the rule, the override, and the reason — which is *honesty over false closure* applied to the process rather than to the text.

**Format.** Newest first. One `##` section per call:

```markdown
## YYYY-MM-DD · <rule-id>

rule: <rule-id>
source: <where the suspended rule is written>
scope: repo | chapter: N | [list]
until: <a condition, a date, or the literal `standing`>
reason: >
  Why. Required, and it is the whole point of the file.
```

**`until:` is required, even when the answer is `standing`.** Forcing the field forces the choice between *for now* and *from now on*. Most overrides are the first kind and get silently treated as the second.

**Machine effect, where the rule is mechanical.** A `rule:` naming a `tools/check_locks.py` rule suppresses that rule at the stated scope. A `rule:` naming a prose rule in `CLAUDE.md` or `PLAN.md` has no machine effect, and is still logged and surfaced — that is most of them.

**Suspension is never silent.** `check_locks.py` prints a footer naming every rule currently suspended. A rule you cannot see is switched off is how a lock quietly dies.

**Expiry is an error; dormancy is not.** A `standing` call may sit unused indefinitely. A call whose `until:` condition has passed raises `stale-shaloms-call`, so each one gets renewed or retired deliberately. *(This deliberately inverts the `lock-ok` waiver rule, where an unused waiver is the error: waivers should self-clean, overrides should demand a decision.)*

**Relation to `lock-ok` waivers.** A waiver excuses one **finding** and lives in that chapter's `## Notes`. A call suspends a **rule** and lives here. If you find yourself writing the same waiver into many chapters, the rule wants a call — or wants changing.

**Relation to `git commit --no-verify`.** That is the ad-hoc version. Fine once. Twice on the same rule is a signal that a call is owed.

---

## Calls in effect

## 2026-08-11 · shaloms-call

rule: shaloms-call
source: this file — the mechanism itself
scope: repo
until: standing
reason: >
  Establishes the override mechanism. Shalom is the decider; the rules in this
  repo are his to set aside. Until now an override existed only as a sentence in
  a conversation: it did not survive the session, it was invisible to anyone
  reading the repo, and it left the AI in the position of correctly objecting on
  the next session to work that had already been authorized — re-arguing a
  settled decision, which is the opposite of what the prime directive is for.

---

## Retired calls

*A call that has expired and been deliberately retired moves here rather than being deleted, so the history of the process stays readable.*


## 2026-08-11 · no-new-tooling (sources library, continued) — **retired 2026-08-11 by Shalom, condition met**

rule: no-new-tooling
source: PLAN.md — "the one rule this plan exists to protect: do not stop drafting to build tooling"
scope: repo
until: Heshang Gong and Han Feizi vendored, then the rule resumes
reason: >
  Reinstated by Shalom. The AI retired the previous call on its own initiative,
  reading the `until:` condition as met once Wang Bi was vendored. That was an
  overstep: this ledger says only Shalom creates a call, and retiring one is the
  same kind of act. The condition was also arguable rather than met — Heshang
  Gong and Han Feizi were still owed, and the library is not built until they
  are in it.

  Shalom's own framing, 2026-08-11: multitasking at work, unable to focus on
  translation but able to shepherd system-architecture work. So the tooling work
  continues and drafting waits, which is the reverse of the usual priority and
  is deliberate.

  Scope: Heshang Gong (河上公章句, Song woodblock via Sibu congkan 0532) and
  Han Feizi's 解老 / 喻老. On completion the rule resumes and drafting continues
  at Ch 63.

**Why retired:** the `until:` condition is met. All three classical commentaries named in
`process/method.md` §3 are vendored — 王弼 (*Wáng Bì*, 71 chapters), 河上公 (*Héshàng Gōng*, all 81),
and 韓非 (*Hán Fēi*, the 17 he discusses) — with per-file provenance, a reproducible importer, and
self-verification against our own base text. **The no-new-tooling rule is back in force. Drafting
resumes at Ch 63.**

**Retired by Shalom, which matters.** The previous call in this series was retired by the AI on its
own initiative and had to be reinstated. Only Shalom creates a call, and retiring one is the same
kind of act. This retirement was his instruction.

---

## 2026-08-11 · no-new-tooling (harness phases A–F) — **retired 2026-08-11, condition met**

rule: no-new-tooling
source: PLAN.md — "the one rule this plan exists to protect: do not stop drafting to build tooling"
scope: repo
until: harness phases A–F complete, then the rule resumes
reason: >
  62 of 81 chapters now exist and are swept clean. PLAN.md deferred the harness
  on the grounds that it would mean "building checks before the corpus exists to
  check" — sound at the time, largely spent now. Deferring further means the last
  19 chapters accrue drift that a second full hand-sweep must then find, paying
  the 2026-08-10 cost twice.

  The proof the deferral has outlived its logic: chapters/053.md renders 大道
  (dà dào — "the great Tao") as "the great Way" — the one rendering CLAUDE.md
  forbids most emphatically — one line below rendering the same compound
  correctly. That chapter carries `retrofit: []` and sits inside the 61 the
  2026-08-10 sweep certified clean. A careful human sweep missed it; a checker
  finds it in under a second.

  Scope is limited to what serves drafting: tools/lib/corpus.py,
  check_locks.py, concordance.py, CI and hook, the chapter-review skill.
  tools/build.py stays deferred — the text still moves in 19 chapters, and
  every edition built now would be built twice. On completion, this call
  expires and "do not stop drafting to build tooling" is back in force.

**Why retired:** phases A–F are built and merged (PR #2). `tools/lib/corpus.py`, `check_locks.py` with nine rules and 42 tests, `concordance.py`, CI, the pre-commit hook, the `chapter-review` skill, and this ledger all exist. The nine lock violations the checker found on its first run are resolved. The condition in `until:` was met, so the call is spent — the rule it suspended is back in force except where the newer call above supersedes it.

*Note the limit this exposed: `until:` was written as a **condition**, not a date, so `stale-shaloms-call` could not fire on it automatically. `tools/check_locks.py` lists condition-based calls in its footer for manual review instead. Retiring this one was a human act, prompted by that footer.*
