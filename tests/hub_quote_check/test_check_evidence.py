import os
import pathlib
import shutil
import tempfile
import unittest

from check_evidence import check_dir

CASE = pathlib.Path(os.path.dirname(__file__)) / ".." / ".." / "assets" / "starter-files" / "course-case"


class EvidenceCheck(unittest.TestCase):
    def setUp(self):
        self.tmp = pathlib.Path(tempfile.mkdtemp())
        shutil.copytree(CASE / "evidence", self.tmp / "evidence")
        shutil.copytree(CASE / "raw", self.tmp / "raw")

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def run_check(self):
        return {r.name: r for r in check_dir(self.tmp / "evidence", self.tmp / "raw")}

    def edit(self, note_id, old, new, file=None):
        """Replace `old` once, inside the block of `note_id` (or in `file` when given)."""
        if file:
            f, text = self.tmp / "evidence" / file, None
            text = f.read_text(encoding="utf-8")
            self.assertIn(old, text)
            f.write_text(text.replace(old, new, 1), encoding="utf-8")
            return
        for f in (self.tmp / "evidence").glob("I*.md"):
            text = f.read_text(encoding="utf-8")
            start = text.find(f"## {note_id} ")
            if start < 0:
                continue
            end = text.find("\n## ", start + 1)
            end = len(text) if end < 0 else end
            block = text[start:end]
            self.assertIn(old, block)
            f.write_text(text[:start] + block.replace(old, new, 1) + text[end:], encoding="utf-8")
            return
        self.fail(f"note {note_id} not found")

    def test_sample_passes(self):
        results = check_dir(self.tmp / "evidence", self.tmp / "raw")
        self.assertEqual(len(results), 10)
        self.assertTrue(all(r.ok for r in results), [r.problems for r in results if not r.ok])

    def test_fail_one_word_changed(self):
        self.edit("RET-01", "at my desk", "at my table")
        self.assertIn("quote not in I01 turn 04", self.run_check()["RET-01"].problems)

    def test_pass_case_whitespace_and_curly_quotes(self):
        self.edit("RET-08", '> "Honestly, the', '>   “HONESTLY,   the')
        self.edit("RET-08", 'dinner." (I02', 'dinner.” (I02')
        self.assertTrue(self.run_check()["RET-08"].ok)

    def test_fail_wrong_turn(self):
        self.edit("RET-02", "(I01, turn 06)", "(I01, turn 08)")
        problems = self.run_check()["RET-02"].problems
        self.assertIn("quote not in I01 turn 08", problems)
        self.assertIn("source I01 @ turn 08 not in source field", problems)

    def test_fail_turn_does_not_exist(self):
        self.edit("RET-03", "(I01, turn 10)", "(I01, turn 99)")
        self.assertIn("turn 99 not found in I01", self.run_check()["RET-03"].problems)

    def test_fail_raw_file_missing(self):
        self.edit("RET-07", "(I02, turn 08)", "(I09, turn 08)")
        self.assertIn("raw file I09 not found", self.run_check()["RET-07"].problems)

    def test_fail_duplicate_id(self):
        self.edit("RET-04", "## RET-04 ", "## RET-03 ")
        results = check_dir(self.tmp / "evidence", self.tmp / "raw")
        self.assertTrue(any("duplicate id RET-03" in p for r in results for p in r.problems))

    def test_fail_missing_field(self):
        self.edit("RET-05", "- confidence: low\n", "")
        self.assertIn("missing field confidence", self.run_check()["RET-05"].problems)

    def test_fail_outcome_prefix_mismatch(self):
        self.edit("RET-06", "- outcome: RET", "- outcome: ONB")
        self.assertIn("outcome does not match id prefix", self.run_check()["RET-06"].problems)

    def test_fail_tag_not_in_tags_md(self):
        self.edit("RET-09", "price/delivery-fee", "price/fees")
        self.assertIn("tag price/fees not in tags.md", self.run_check()["RET-09"].problems)

    def test_fail_tags_md_missing(self):
        (self.tmp / "evidence" / "tags.md").unlink()
        self.assertIn("tags.md not found", self.run_check()["RET-01"].problems)

    def test_two_files_five_notes_each(self):
        files = sorted(p.name for p in (self.tmp / "evidence").glob("I*.md"))
        self.assertEqual(files, ["I01.md", "I02.md"])


if __name__ == "__main__":
    unittest.main()
