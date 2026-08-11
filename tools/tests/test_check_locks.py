#!/usr/bin/env python3
"""
Tests for check_locks.py, built from the traps the 2026-08-10 sweep actually hit.

    python3 -m unittest discover tools/tests        # or: python3 -m pytest tools/tests

The point of this file is not coverage. It is that roughly a third of that
sweep's 93 flags were false positives, and a checker that cries wolf gets
switched off. So every case below is either a real error that must fire, or a
real false friend that must not — taken from RETROFIT.md's own record.

The false-friend cases are the important half. If one of them starts failing,
the checker has become noise.
"""

import pathlib
import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import check_locks as C                                  # noqa: E402
from lib.corpus import Call, Chapter, SourceRow, Term, Waiver  # noqa: E402


def chapter(number, verse, chinese, status="drafted", notes=""):
    """A chapter with one source row, enough to exercise the evidence gate."""
    lines = verse if isinstance(verse, list) else [verse]
    return Chapter(
        number=number,
        path=Path(f"chapters/{number:03d}.md"),
        status=status,
        retrofit=[],
        verse=[(i + 10, t) for i, t in enumerate(lines)],
        source_rows=[SourceRow(chinese, "pinyin", "literal gloss", 1, 20)],
        notes=notes,
        waivers=[],
    )


def term(t, pinyin, render, forbidden):
    return Term(term=t, pinyin=pinyin, render=render, forbidden=forbidden,
                chapters=[], status="locked", entry=f"glossary/{pinyin}-{t}.md")


CHANG = term("常", "chang", "the ever-present", ["eternal", "everlasting"])
DE = term("德", "de", "integrity", ["virtue", "power"])
DAO = term("道", "dao", "the Tao", ["the Way", "the Path"])
WU_YOU = term("無 & 有", "wu-you", "absence / presence",
              ["Being", "Non-Being", "nothingness"])
PU = term("樸", "pu", "uncarved wood", ["uncarved block", "simplicity"])


def rendering_errors(chapters, terms):
    return [f for f in C.rule_forbidden_rendering(chapters=chapters, terms=terms)
            if f.severity == C.ERROR]


class ForbiddenRenderings(unittest.TestCase):
    """The locks, and the false friends that look like them."""

    def test_stem_match_catches_the_adverb(self):
        # RETROFIT.md lesson 1: \beternal\b misses "eternally", which is exactly
        # how two chapters hid from the sweep.
        found = rendering_errors([chapter(1, "The Tao is eternally so.", "常道")], [CHANG])
        self.assertEqual(len(found), 1)
        self.assertIn("eternal", found[0].message)

    def test_cháng_the_homophone_is_not_blamed(self):
        # 長 (cháng — long) is not 常 (cháng — constant). Ch 22's "therefore
        # endures" and Ch 7's 天長地久 were both wrongly flagged in the sweep.
        self.assertEqual(
            rendering_errors([chapter(22, "Therefore it endures.", "故長久")], [CHANG]), [])

    def test_evidence_gate_demotes_without_the_character(self):
        # "power" is forbidden for 德, but ch 33's "willpower" has no 德 in it.
        ch = chapter(33, "One who perseveres has willpower.", "強行者有志")
        all_found = C.rule_forbidden_rendering(chapters=[ch], terms=[DE])
        self.assertTrue(all_found)
        self.assertTrue(all(f.severity == C.INFO for f in all_found))
        self.assertIn("not in this chapter", all_found[0].message)

    def test_evidence_gate_promotes_with_the_character(self):
        found = rendering_errors([chapter(38, "The highest virtue is still.", "上德不德")], [DE])
        self.assertEqual(len(found), 1)

    def test_capitalized_forbidden_string_is_case_sensitive(self):
        # "the Way" is the violation; "the way of nature" is ordinary English.
        # A case-insensitive scan flagged both in ch 9 and ch 47.
        self.assertEqual(
            rendering_errors([chapter(9, "This is the way of nature.", "天之道")], [DAO]), [])
        self.assertEqual(
            len(rendering_errors([chapter(1, "Walking the Way of nature.", "道可道")], [DAO])), 1)

    def test_sentence_initial_capital_is_allowed(self):
        # "Being embodied and embracing the one" (ch 10) opens a line: the
        # capital is English orthography, not metaphysics.
        self.assertEqual(
            rendering_errors([chapter(10, "Being embodied, can you remain whole?", "有無")],
                             [WU_YOU]), [])

    def test_the_participle_is_not_the_noun(self):
        # "being still", "their being", "insists on being right" — six false
        # positives in the corpus, all cleared by case sensitivity.
        for line in ("Relinquishing desire, being still.",
                     "One who insists on being right is not prominent.",
                     "How could a ruler become ungrounded in their being?"):
            self.assertEqual(rendering_errors([chapter(2, line, "有無")], [WU_YOU]), [],
                             msg=line)

    def test_capital_noun_mid_sentence_still_fires(self):
        found = rendering_errors(
            [chapter(2, "It arises from Being and returns.", "有無相生")], [WU_YOU])
        self.assertEqual(len(found), 1)

    def test_blocking_the_openings_is_not_the_uncarved_block(self):
        # 塞其兌 ("block the openings", ch 52/56) vs 樸 ("uncarved wood").
        self.assertEqual(
            rendering_errors([chapter(52, "Block the openings, close the gate.", "塞其兌")],
                             [PU]), [])

    def test_nothingness_is_caught_where_wu_is_present(self):
        found = rendering_errors([chapter(14, "And returns to nothingness.", "無物")], [WU_YOU])
        self.assertEqual(len(found), 1)


class SagePronoun(unittest.TestCase):
    """Standing rule 1. Zero tolerance, no evidence gate."""

    def test_he_fires(self):
        found = C.rule_sage_pronoun(chapters=[chapter(2, "The sage does his work.", "聖人")])
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0].severity, C.ERROR)

    def test_they_is_clean(self):
        self.assertEqual(
            C.rule_sage_pronoun(chapters=[chapter(2, "The sage does their work.", "聖人")]), [])

    def test_the_word_is_not_a_substring(self):
        # "the" contains "he"; word boundaries matter for this rule even though
        # they must not be used for the forbidden-rendering stems.
        self.assertEqual(
            C.rule_sage_pronoun(chapters=[chapter(2, "The sage shelters them.", "聖人")]), [])


class DevotionalCapitalization(unittest.TestCase):
    """Standing rule 5: capitals confer status, and turn a word into a doctrine."""

    def test_the_great_way_in_chapter_53(self):
        # The live error this harness was built on. Note the phrase rule cannot
        # catch it — "the Way" is broken by the inserted "great" — which is why
        # this rule watches the bare word.
        found = [f for f in C.rule_devotional_capitalization(
            chapters=[chapter(53, "The great Way is very level.", "大道甚夷")])
            if f.severity == C.ERROR]
        self.assertEqual(len(found), 1)
        self.assertIn("Way", found[0].message)

    def test_lowercase_is_clean(self):
        self.assertEqual(C.rule_devotional_capitalization(
            chapters=[chapter(53, "The great way is very level.", "大道甚夷")]), [])

    def test_line_initial_capital_is_allowed(self):
        self.assertEqual(C.rule_devotional_capitalization(
            chapters=[chapter(25, "Nature follows the Tao.", "道法自然")]), [])

    def test_capital_after_a_full_stop_is_allowed(self):
        self.assertEqual(C.rule_devotional_capitalization(
            chapters=[chapter(25, "It is so. Nature follows the Tao.", "道法自然")]), [])


class MechanisticRegister(unittest.TestCase):
    """CLAUDE.md's overlay watchlist: our own besetting temptation."""

    def test_source_code_fires(self):
        found = C.rule_mechanistic_register(
            chapters=[chapter(21, "The unerasable source code of all creation.", "眾甫")])
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0].severity, C.ERROR)


class StatusCoherence(unittest.TestCase):
    def test_drafted_but_empty(self):
        ch = chapter(61, C.UNTRANSLATED_MARKER, "大國者下流", status="drafted")
        found = [f for f in C.rule_status_coherence(chapters=[ch])
                 if "empty" in f.message]
        self.assertEqual(len(found), 1)

    def test_untranslated_but_written(self):
        ch = chapter(61, "The great state flows downward.", "大國者下流",
                     status="untranslated")
        found = [f for f in C.rule_status_coherence(chapters=[ch])
                 if "has verse" in f.message]
        self.assertEqual(len(found), 1)

    def test_drafted_and_written_is_clean(self):
        ch = chapter(61, "The great state flows downward.", "大國者下流")
        self.assertEqual(C.rule_status_coherence(chapters=[ch]), [])


class Waivers(unittest.TestCase):
    """Suppression is allowed, must carry a reason, and must not outlive its finding."""

    def test_waiver_marks_the_finding_waived(self):
        ch = chapter(22, "The sage does his work.", "聖人")
        ch.waivers = [Waiver("sage-pronoun", "quoting a critic · notes/translation.md", 40)]
        findings, _, _ = self._run(ch)
        pronoun = [f for f in findings if f.rule == "sage-pronoun"]
        self.assertEqual(len(pronoun), 1)
        self.assertIsNotNone(pronoun[0].waived_by)

    def test_unused_waiver_is_itself_an_error(self):
        ch = chapter(22, "The sage does their work.", "聖人")
        ch.waivers = [Waiver("sage-pronoun", "no longer needed", 40)]
        findings, _, _ = self._run(ch)
        stale = [f for f in findings if f.rule == "unused-waiver"]
        self.assertEqual(len(stale), 1)
        self.assertEqual(stale[0].severity, C.ERROR)

    def test_a_filtered_run_never_calls_a_waiver_dead(self):
        # A partial run cannot know: --rule leaves the consuming rule unrun, and
        # --chapter drops cross-chapter findings filed under another number.
        # Reporting a live waiver as dead would teach you to delete good waivers.
        ch = chapter(22, "The sage does their work.", "聖人")
        ch.waivers = [Waiver("repeated-formula", "deliberate, see notes", 40)]
        findings, _, _ = self._run(ch, rule_filter={"unused-waiver"})
        self.assertEqual([f for f in findings if f.rule == "unused-waiver"], [])

    def _run(self, ch, calls=(), rule_filter=None):
        """Exercise run()'s waiver and suppression logic against one chapter."""
        original_chapters, original_terms, original_calls = (
            C.load_chapters, C.load_terms, C.load_calls)
        C.load_chapters = lambda only=None: {ch.number: ch}
        C.load_terms = lambda: []
        C.load_calls = lambda: list(calls)
        try:
            return C.run(rule_filter=rule_filter)
        finally:
            C.load_chapters, C.load_terms, C.load_calls = (
                original_chapters, original_terms, original_calls)


class WaiverNames(unittest.TestCase):
    """A waiver may name a term three ways, because bare pinyin collides."""

    def test_three_names_per_term(self):
        self.assertEqual(C._waiver_names("glossary/chang-常.md", "常"),
                         {"chang", "chang-常", "常"})

    def test_the_xin_collision_is_disambiguable(self):
        # 心 (xīn, heart) and 信 (xìn, trust) both slug to "xin". The bare pinyin
        # is therefore ambiguous for this pair; the stem and character are not.
        heart = C._waiver_names("glossary/xin-心.md", "心")
        trust = C._waiver_names("glossary/xin-信.md", "信")
        self.assertEqual(heart & trust, {"xin"})
        self.assertIn("xin-心", heart)
        self.assertIn("xin-信", trust)
        self.assertNotIn("xin-信", heart)


class ShalomsCall(unittest.TestCase):
    """The override of record: suppresses by rule name, and never silently."""

    def test_repo_scope_suppresses(self):
        ch = chapter(22, "The sage does his work.", "聖人")
        call = Call("sage-pronoun", "CLAUDE.md", "repo", "standing", "testing", "2026-08-11")
        findings, suppressed, _ = Waivers._run(self, ch, calls=[call])
        self.assertEqual([f for f in findings if f.rule == "sage-pronoun"], [])
        self.assertIn("sage-pronoun", suppressed)

    def test_chapter_scope_is_narrow(self):
        call = Call("em-dash", "CLAUDE.md", "chapter: 44", "standing", "ch 44's are good",
                    "2026-08-11")
        self.assertTrue(call.covers(44))
        self.assertFalse(call.covers(14))

    def test_repo_scope_covers_everything(self):
        call = Call("em-dash", "CLAUDE.md", "repo", "standing", "why", "2026-08-11")
        self.assertTrue(call.covers(14))

    def test_retired_call_suppresses_nothing(self):
        call = Call("em-dash", "CLAUDE.md", "repo", "standing", "why", "2026-08-11",
                    retired=True)
        self.assertFalse(call.covers(14))

    def test_a_qualified_heading_still_parses(self):
        # "## DATE · rule (label)" and "## DATE · rule — retired" are both
        # legitimate; a regex that required the line to end at the rule id once
        # made a three-call ledger parse as one, silently.
        from lib.corpus import load_calls
        calls = load_calls()
        text = (pathlib.Path(__file__).resolve().parent.parent.parent
                / "process" / "shaloms-call.md").read_text()
        headings = re.findall(r"^## \d{4}-\d{2}-\d{2}\s*·", text, re.M)
        self.assertEqual(len(calls), len(headings),
                         "every dated heading in the ledger must parse to a call")

    def test_unparsed_headings_are_an_error(self):
        # The guard must fire when the counts disagree.
        found = C.rule_shaloms_call_unparsed(calls=[])
        self.assertTrue(found, "guard should fire when no calls parse")
        self.assertEqual(found[0].severity, C.ERROR)

    def test_expired_call_is_an_error(self):
        call = Call("no-new-tooling", "PLAN.md", "repo", "2020-01-01", "why", "2019-12-01")
        found = C.rule_stale_shaloms_call(calls=[call])
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0].severity, C.ERROR)

    def test_standing_call_never_expires(self):
        call = Call("shaloms-call", "here", "repo", "standing", "why", "2026-08-11")
        self.assertEqual(C.rule_stale_shaloms_call(calls=[call]), [])

    def test_future_expiry_is_fine(self):
        call = Call("no-new-tooling", "PLAN.md", "repo", "2099-01-01", "why", "2026-08-11")
        self.assertEqual(C.rule_stale_shaloms_call(calls=[call]), [])


class RepeatedFormula(unittest.TestCase):
    """Verbatim Chinese must produce verbatim English."""

    def _pair(self, en_a, en_b):
        rows = [SourceRow("物壯則老，", "wù zhuàng zé lǎo,",
                          "When things peak in strength, they decay,", 1, 20)]
        chs = []
        for n, en in ((30, en_a), (55, en_b)):
            c = chapter(n, en, "物壯則老，")
            c.source_rows = rows
            chs.append(c)
        return C.rule_repeated_formula(chapters=chs)

    def test_identical_renderings_do_not_warn(self):
        # The state ch 30 and ch 55 were left in after the 2026-08-10 fix.
        found = self._pair("When things reach their peak strength, they decay.",
                           "When things reach their peak strength, they decay.")
        self.assertTrue(all(f.severity == C.INFO for f in found))

    def test_divergent_renderings_warn(self):
        # The state they were in before it.
        found = self._pair("When things reach their peak strength, they decay.",
                           "Whatever grows strong will wither away.")
        self.assertTrue(any(f.severity == C.WARN for f in found))

    def test_grammar_is_not_a_formula(self):
        # 是以聖人 ("therefore the sage") opens 17 chapters. It is syntax, not a
        # formula, and reporting it would bury the four real findings.
        chs = []
        for n in range(1, 6):
            c = chapter(n, "Therefore the sage acts.", "是以聖人")
            c.source_rows = [SourceRow("是以聖人，", "shì yǐ shèng rén,",
                                       "Therefore the sage,", 1, 20)]
            chs.append(c)
        self.assertEqual(C.rule_repeated_formula(chapters=chs), [])


class SourceDrift(unittest.TestCase):
    def test_chapter_matching_base_text_is_clean(self):
        ch = chapter(1, "The Tao that can be spoken is not the Tao.", "道可道，非常道。")
        original = C.load_base_text
        C.load_base_text = lambda: {1: "道可道，非常道。\n"}
        try:
            self.assertEqual(C.rule_source_drift(chapters=[ch]), [])
        finally:
            C.load_base_text = original

    def test_drift_is_an_error(self):
        ch = chapter(1, "The Tao that can be spoken is not the Tao.", "道可道，非常道。")
        original = C.load_base_text
        C.load_base_text = lambda: {1: "道可道，非恆道。\n"}
        try:
            found = C.rule_source_drift(chapters=[ch])
            self.assertEqual(len(found), 1)
            self.assertEqual(found[0].severity, C.ERROR)
        finally:
            C.load_base_text = original


class Variants(unittest.TestCase):
    """The apparatus, and the rule that keeps it honest."""

    def test_the_apparatus_parses(self):
        from lib.corpus import load_variants
        vs = load_variants()
        self.assertTrue(vs, "sources/variants.yaml parsed to nothing")
        for v in vs:
            self.assertTrue(v.chapter, "a variant has no chapter")
            self.assertTrue(v.base, f"ch {v.chapter} variant has no base reading")
            self.assertIn(v.our_call,
                          {"base", "punctuation", "undecided"} | set(v.witnesses),
                          f"ch {v.chapter}: our_call must be 'base', 'punctuation', "
                          f"'undecided', or one of its own witnesses")

    def test_chapter_filter(self):
        from lib.corpus import load_variants
        self.assertTrue(all(v.chapter == 25 for v in load_variants(25)))

    def test_every_meaning_bearing_fork_is_logged(self):
        # The whole point of the apparatus: a fork translated over without a
        # recorded decision is a build failure, not an accident.
        errors = [f for f in C.rule_unlogged_variant() if f.severity == C.ERROR]
        self.assertEqual(errors, [])

    def test_an_unlogged_fork_would_fire(self):
        from lib.corpus import Variant
        original = C.load_variants
        C.load_variants = lambda chapter=None: [Variant(
            chapter=63, line="夫輕諾必寡信", base="諾", witnesses={"mawangdui-a": "許"},
            meaning_bearing=True, our_call="base", note="", logged="")]
        try:
            found = C.rule_unlogged_variant()
            self.assertEqual(len(found), 1)
            self.assertEqual(found[0].severity, C.ERROR)
        finally:
            C.load_variants = original


class TheCorpusItself(unittest.TestCase):
    """Guards on the live manuscript, not on synthetic fixtures."""

    def test_no_male_pronouns_anywhere(self):
        # This lock has held from the first chapter. Keep it that way.
        chapters = [c for c in C.load_chapters().values() if c.drafted]
        self.assertEqual(C.rule_sage_pronoun(chapters=chapters), [])

    def test_no_virtue_anywhere(self):
        # 德 → integrity has also held from the beginning.
        chapters = [c for c in C.load_chapters().values() if c.drafted]
        de = [t for t in C.load_terms() if t.term == "德"]
        self.assertTrue(de, "the 德 lock is missing from terms.yaml")
        self.assertEqual(rendering_errors(chapters, de), [])

    def test_every_chapter_parses(self):
        chapters = C.load_chapters()
        self.assertEqual(len(chapters), 81)
        for n, c in chapters.items():
            self.assertTrue(c.source_rows, f"chapter {n} has no source rows")
            self.assertEqual(c.number, n)

    def test_base_text_has_not_drifted(self):
        chapters = list(C.load_chapters().values())
        self.assertEqual(C.rule_source_drift(chapters=chapters), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
