---
id: importers-verify-themselves
title: "An importer that does not verify itself is decoration"
status: active
since: 2026-08-11
trigger: "you are vendoring source material a later reader will treat as evidence"
applies: [tooling]
evidence: ["ARCHITECTURE.md#what-is-generated-and-from-what", "PLAN.md#what-the-building-taught"]
check: none
supersedes: []
---

# An importer that does not verify itself is decoration

**The rule.** An importer that vendors evidence must **check what it vendored against something we already hold**, and mark the disagreements. Without that check, the files are not evidence; they are text that looks like evidence.

**When it fires.** When writing or extending any importer, and whenever a vendored file is about to be cited in an argument.

---

## Why this holds

**The check is what converts a copy into a witness.** `import_commentary.py` checks every lemma it vendors against our own base text and marks the divergent ones with `*`. **That mark is the whole value**: a commentator's lemma differing from our base is a manuscript fork, and finding those is most of what the commentaries are for. Without the check, the file is a wall of characters nobody can use.

**And the absence is not visible from the file.** When the check was missing for 韓非 (*Hán Fēi*), **the files asserted an agreement nobody had tested.** Nothing looked wrong — a vendored text with no divergence marks reads exactly like a vendored text that agrees. Silence from an unverified importer is indistinguishable from silence from a verified one, which is why the verification has to be in the importer rather than in a reader's diligence.

**It also pays for itself immediately.** The verification pass on first run caught three corrections plus more in passing, and the 韓非 import surfaced **35 divergent lemmas** — the oldest witness to this text, and a body of evidence that exists only because the importer looked.

**And it is the same argument as the diff gate, one step upstream.** [[deterministic-before-gated]] makes a generated file trustworthy by rebuilding it; this makes a vendored file trustworthy by checking it. Both refuse to let a committed artifact rest on the assumption that whoever made it was careful.

---

## The cases

**The importers verify themselves** — the design statement, alongside the generated-file table. → [ARCHITECTURE](../../ARCHITECTURE.md#what-is-generated-and-from-what)

**What the building taught**, including the corrections the verification pass caught on its first run. → [PLAN](../../PLAN.md#what-the-building-taught)

---

## Where it does not fire

**Where there is nothing to verify against, say so rather than inventing a check.** 說文解字 (*Shuōwén Jiězì*) entries are matched by headword and the match type is recorded — `exact` or otherwise — which is the honest version of the same discipline.

**And verification is not translation.** The importers check *graphs*, not meanings. **There is no English in the vendored files**, deliberately, and none is generated: machine-rendering hundreds of classical definitions would manufacture scholarship nobody did.

---

## What it obliges

1. **Verify against something already in the repository**, and record the method in the file's frontmatter.
2. **Mark divergences rather than resolving them** — a fork is a finding, not a defect.
3. **Make the import reproducible to byte-identical output**, so the vendored file can be gated like any other build product.
4. **Record coverage honestly**, including what is missing — the ten unproofread 王弼 chapters are named, so a blank result is never mistaken for agreement.
