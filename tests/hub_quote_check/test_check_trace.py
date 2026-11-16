import os
import unittest

from check_trace import check_trace, parse_rows
from check_quotes import parse_notes

SAMPLE = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "starter-files", "course-case", "insights-plain.txt")
VALID = set(parse_notes(open(SAMPLE, encoding="utf-8").read()))


def one(line):
    return check_trace(VALID, parse_rows(line))[0]


class TraceCheck(unittest.TestCase):
    def test_pass_existing_ids(self):
        self.assertEqual(one("L5 | IN-02, IN-09").status, "pass")

    def test_pass_labelled_assumption(self):
        self.assertEqual(one("L2 | assumption").status, "pass")

    def test_fail_unknown_id(self):
        r = one("L3 | IN-01, IN-42")
        self.assertEqual(r.status, "fail")
        self.assertIn("IN-42", r.reason)

    def test_fail_no_id(self):
        self.assertEqual(one("L1 |").status, "fail")

    def test_fail_assumption_mixed_with_id(self):
        self.assertEqual(one("L6 | IN-05, assumption").status, "fail")

    def test_ids_are_case_and_space_tolerant(self):
        self.assertEqual(one("L1 |  in-01 ,IN-02 ").status, "pass")

    def test_parse_rows_rejects_line_without_separator(self):
        with self.assertRaises(ValueError) as cm:
            parse_rows("L1 IN-01")
        self.assertIn("line 1", str(cm.exception))


if __name__ == "__main__":
    unittest.main()
