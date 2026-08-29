<!--
Thank you. Before anything else: this repository is CC0, and contributions are
released into the public domain too. If your change alters the text, you'll be
named in the notes — because that's the truth about how the reading was arrived
at, not because the license asks for it.
-->

**What changes, and why**

**If this touches the translation**

- [ ] Every Chinese character in this PR carries pinyin and an English rendering
- [ ] Checked against the Chinese in its own chapter, not from memory
- [ ] Checked whether the change propagates — `python3 tools/concordance.py <character>`
- [ ] The sage is never "he"
- [ ] Lowercase throughout, except the Tao
- [ ] Trailing double-spaces preserved (verse line breaks are load-bearing)

**Checks**

```bash
python3 tools/fix-linebreaks.py --check
python3 tools/check_locks.py
python3 -m unittest discover -s tools/tests
```

- [ ] All three pass

<!--
If check_locks.py flags something you believe is right, don't delete the rule.
Either waive the single finding with a `<!-- lock-ok: rule · reason -->` comment
in that chapter's `## Notes`, or say so here and I'll make the call.
-->

**Anything you're unsure about**

<!-- Genuinely welcome. An unfinished PR with a good question beats a polished one. -->
