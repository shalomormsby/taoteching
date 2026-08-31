#!/usr/bin/env python3
"""
The worklist checker, against the drift it was written for.

Every fixture below is a real failure this repository shipped. A checker that
only ever passes is worth nothing, so each rule is proved against the state
that got past a human reader, and then against the corrected state.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import check_worklist as cw  # noqa: E402


HEAD = "| # | | Item | Ch | Pass |\n|---|---|---|---|---|\n"


def table(*rows):
    return HEAD + "".join(rows)


def row(rid, status, ch, pass_, item="x"):
    return f"| {rid} | {status} | {item} | {ch} | {pass_} |\n"


def rules(text):
    findings, _ = cw.check(text)
    return sorted(f.rule for f in findings)


class PassChapters(unittest.TestCase):
    """The failure of 2026-08-31: two hand-kept Pass D lists, both wrong."""

    def test_the_real_drift_is_caught(self):
        # PD listed 15, 26 and 30 — no D-tagged row named any of them — and
        # omitted 38, which T1-4 does name.
        t = table(
            row("PD", "⬜", "3 4 15 26 30", "D"),
            row("T1-2", "⬜", "4", "D"),
            row("T1-3", "⬜", "3", "D"),
            row("T1-4", "⬜", "38", "D"),
        )
        findings, _ = cw.check(t)
        self.assertEqual([f.rule for f in findings], ["pass-chapters"])
        detail = findings[0].detail
        self.assertIn("missing 38", detail)
        self.assertIn("15 26 30", detail)
        self.assertIn("3 4 38", findings[0].fix)

    def test_the_corrected_list_passes(self):
        t = table(
            row("PD", "⬜", "3 4 38", "D"),
            row("T1-3", "⬜", "3", "D"),
            row("T1-2", "⬜", "4", "D"),
            row("T1-4", "⬜", "38", "D"),
        )
        self.assertEqual(rules(t), [])

    def test_a_pointer_cell_is_not_a_list_and_is_never_checked(self):
        """PC says 'T3-1 · T2-9→15'. Declining to keep a list is the goal."""
        t = table(
            row("PC", "🔶", "T3-1 · T2-9→15", "C"),
            row("T2-9", "⬜", "45", "C"),
        )
        self.assertEqual(rules(t), [])

    def test_book_wide_and_dashes_are_not_lists(self):
        t = table(
            row("PE", "⬜", "book-wide", "E"),
            row("PG", "⬜", "—", "G"),
            row("T2-1", "⬜", "7 9 13", "E"),
            row("T5-7", "⬜", "—", "G"),
        )
        self.assertEqual(rules(t), [])

    def test_plus_n_more_does_not_leak_a_chapter_number(self):
        """'5 16 17 18 25 + 26 more' must not read 26 as a chapter."""
        self.assertEqual(cw._chapters("5 16 17 18 25 + 26 more"),
                         frozenset({5, 16, 17, 18, 25}))


class ClosedPass(unittest.TestCase):
    """The failure of 2026-08-31: PC marked done over three open C rows."""

    def test_a_pass_cannot_be_done_over_open_rows(self):
        t = table(
            row("PC", "✅", "T3-1", "C"),
            row("T2-9", "⬜", "45", "C"),
            row("T2-10", "⬜", "27 52", "C"),
            row("T2-11", "⬜", "16 32 44 52", "C"),
        )
        findings, _ = cw.check(t)
        self.assertEqual([f.rule for f in findings], ["closed-pass"])
        self.assertIn("3 row(s)", findings[0].detail)
        self.assertIn("T2-9", findings[0].detail)

    def test_part_done_rows_also_block_a_closed_pass(self):
        t = table(row("PC", "✅", "T3-1", "C"), row("T2-15", "🔶", "10 22", "C"))
        self.assertEqual(rules(t), ["closed-pass"])

    def test_deferred_rows_do_not_block(self):
        """⏸ is Shalom's call, not outstanding work."""
        t = table(row("PF", "✅", "—", "F"), row("T4-1", "⏸", "13", "F"))
        self.assertEqual(rules(t), [])

    def test_a_genuinely_finished_pass_passes(self):
        t = table(
            row("PB", "✅", "5 18", "B"),
            row("T1-9", "✅", "5", "B"),
            row("T2-2", "✅", "18", "B"),
        )
        self.assertEqual(rules(t), [])


class Tally(unittest.TestCase):
    def test_a_wrong_header_count_is_caught_and_the_fix_is_printed(self):
        t = ("**2 item rows: 2 open · 0 done · 0 part done · 0 deferred.**\n\n"
             + table(row("PD", "⬜", "—", "D"),
                     row("T1-1", "⬜", "10", "D"), row("T1-2", "✅", "4", "D")))
        findings, _ = cw.check(t)
        self.assertEqual([f.rule for f in findings], ["tally"])
        self.assertIn("1 open · 1 done", findings[0].fix)

    def test_a_right_header_count_passes(self):
        t = ("**2 item rows: 1 open · 1 done · 0 part done · 0 deferred.**\n\n"
             + table(row("PD", "⬜", "—", "D"),
                     row("T1-1", "⬜", "10", "D"), row("T1-2", "✅", "4", "D")))
        self.assertEqual(rules(t), [])


class Structure(unittest.TestCase):
    def test_duplicate_ids(self):
        t = table(row("PD", "⬜", "—", "D"),
                  row("T1-1", "⬜", "10", "D"), row("T1-1", "⬜", "11", "D"))
        self.assertEqual(rules(t), ["duplicate-id"])

    def test_a_pass_letter_with_no_pass_row(self):
        t = table(row("T9-1", "⬜", "10", "Z"))
        self.assertEqual(rules(t), ["pass-exists"])

    def test_ongoing_is_a_licensed_non_pass(self):
        """T5-4 is tagged 'ongoing' deliberately — it never closes."""
        t = table(row("T5-4", "⬜", "—", "ongoing"))
        self.assertEqual(rules(t), [])

    def test_ledger_and_prose_tables_are_ignored(self):
        """Only rows whose first cell is a row id and second a status count."""
        t = table(row("PD", "⬜", "—", "D"), row("T1-1", "⬜", "10", "D")) + (
            "| 2026-08-30 | **T2-12** — 以此 | `notes/translation.md` |\n"
            "| **56–81** | 26 | **20** (77%) | 6 | 0 |\n")
        _, rows = cw.check(t)
        self.assertEqual([r.id for r in rows], ["PD", "T1-1"])


class LiveFile(unittest.TestCase):
    def test_the_real_worklist_is_consistent(self):
        findings, rows = cw.check(cw.WORKLIST.read_text(encoding="utf-8"))
        self.assertEqual(
            findings, [],
            "WORKLIST.md drifted: " + "; ".join(f.detail for f in findings))
        self.assertGreater(len(rows), 40, "the table failed to parse")


if __name__ == "__main__":
    unittest.main()
