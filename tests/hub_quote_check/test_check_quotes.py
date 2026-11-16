import unittest

import os

from check_quotes import check_rows, parse_notes
from fixtures import NOTES_TEXT

NOTES = parse_notes(NOTES_TEXT)
SAMPLE = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "starter-files", "course-case", "source-notes-plain.txt")


def one(ids, quote):
    return check_rows(NOTES, [("insight", ids, quote)])[0]


class QuoteCheck(unittest.TestCase):
    def test_pass_exact_quote(self):
        self.assertEqual(one(["R03"], "In the end I messaged support and waited an hour.").status, "pass")

    def test_pass_curly_vs_straight_quotes_and_whitespace(self):
        self.assertEqual(one(["X01"], "I don\u2019t know which  slot\nI picked.").status, "pass")

    def test_fail_one_word_changed(self):
        r = one(["F04"], "I cancelled my order and still got billed.")
        self.assertEqual(r.status, "fail")

    def test_fail_unknown_id(self):
        r = one(["R99"], "Great app!!!")
        self.assertEqual(r.status, "fail")
        self.assertIn("R99", r.reason)

    def test_fail_quote_in_wrong_note(self):
        r = one(["R09"], "I could not find how to cancel an order anywhere.")
        self.assertEqual(r.status, "fail")

    def test_parse_notes_rejects_missing_id(self):
        with self.assertRaises(ValueError) as cm:
            parse_notes("R03 | fine\n | text without id\n")
        self.assertIn("2", str(cm.exception))

    def test_parse_notes_rejects_duplicate_id(self):
        with self.assertRaises(ValueError) as cm:
            parse_notes("R03 | one\nR03 | two\n")
        self.assertIn("R03", str(cm.exception))

    def test_pass_quote_wrapped_in_quotation_marks(self):
        self.assertEqual(one(["R09"], '"Great app!!! Five stars."').status, "pass")
        self.assertEqual(one(["R09"], "\u201cGreat app!!! Five stars.\u201d").status, "pass")

    def test_fail_empty_quote(self):
        r = one(["R09"], "  ")
        self.assertEqual(r.status, "fail")
        self.assertIn("empty quote", r.reason)

    def test_fail_no_note_ids(self):
        r = one([], "Great app!!!")
        self.assertEqual(r.status, "fail")
        self.assertIn("no note ID", r.reason)

    def test_sample_notes_four_rows(self):
        text = open(SAMPLE, encoding="utf-8").read()
        notes = parse_notes(text)
        self.assertEqual(len(notes), 24)
        rows = [
            ("a", ["R03"], "I could not find how to cancel an order anywhere"),
            ("b", ["F04"], "I cancelled my order and still got billed."),
            ("c", ["I01-01"], "I ordered at lunch and just tapped   the first time slot it showed"),
            ("d", ["R09"], "Great app!!! Five stars."),
        ]
        got = [r.status for r in check_rows(notes, rows)]
        self.assertEqual(got, ["pass", "fail", "pass", "pass"])


if __name__ == "__main__":
    unittest.main()
