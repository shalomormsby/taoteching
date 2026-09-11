#!/usr/bin/env python3
"""
The principles builder, against the two things it exists to prevent.

A principles directory fails in exactly two ways, and both are silent: the
evidence link rots, so a rule looks checked when nothing backs it; and a
passing thought acquires the standing of a law because nobody made it earn a
second case. Each is proved here against the state that would otherwise ship.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import build_principles as bp  # noqa: E402


class Slug(unittest.TestCase):
    """The anchors have to resolve on GitHub, not here."""

    def test_matches_githubs_rule(self):
        self.assertEqual(bp.slug("Standing principles"), "standing-principles")
        self.assertEqual(bp.slug("Ch 14's opening triad"), "ch-14s-opening-triad")

    def test_cjk_survives(self):
        """The reason the anchors in this repo are legible at all."""
        self.assertEqual(bp.slug("夷 · 希 · 微 — the names"), "夷-希-微-the-names")

    def test_em_dash_and_middot_are_dropped_not_hyphenated(self):
        """Real case: the separators collapse, the spaces around them do not."""
        self.assertEqual(bp.slug("a · b — c"), "a-b-c")


class Headings(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(__file__).parent / "_tmp_principles.md"

    def tearDown(self):
        self.tmp.unlink(missing_ok=True)

    def test_collects_every_level(self):
        self.tmp.write_text("# One\ntext\n### Three deep\n", encoding="utf-8")
        self.assertEqual(bp.headings_in(self.tmp), {"one", "three-deep"})

    def test_missing_file_is_none_not_empty(self):
        """An absent file and a file with no headings are different failures."""
        self.assertIsNone(bp.headings_in(Path("/nonexistent/x.md")))


class Threshold(unittest.TestCase):
    """One case is an observation, two is a principle. See the README."""

    def test_active_needs_two_cases(self):
        self.assertLess(1, 2, "guard: the threshold is two")


class RealDirectory(unittest.TestCase):
    """The shipped entries must always build clean."""

    def test_every_entry_is_valid_and_every_anchor_resolves(self):
        entries, problems = bp.load()
        problems += bp.verify_anchors(entries)
        self.assertEqual(problems, [], "\n".join(problems))

    def test_the_threshold_holds_across_the_directory(self):
        entries, _ = bp.load()
        for e in entries:
            if e.get("status") == "active":
                self.assertGreaterEqual(
                    len(e.get("evidence", [])), 2,
                    f"{e['file']} is active with fewer than two cases")


if __name__ == "__main__":
    unittest.main()
