import os
import pathlib
import shutil
import tempfile
import unicodedata
import unittest

from check_clean import check_clean

CASE = pathlib.Path(os.path.dirname(__file__)) / ".." / ".." / "assets" / "starter-files" / "course-case"
FILLERS = ["um", "uh"]


class CleanCheck(unittest.TestCase):
    def setUp(self):
        self.tmp = pathlib.Path(tempfile.mkdtemp())
        self.draft = self.tmp / "draft.txt"
        self.clean = self.tmp / "clean.txt"
        shutil.copy(CASE / "transcript-before-clean" / "I01-before-clean.txt", self.draft)
        shutil.copy(CASE / "raw" / "I01.txt", self.clean)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def run_check(self, **kw):
        return {r.name: r for r in check_clean(self.draft, self.clean, FILLERS, **kw)}

    def edit_clean(self, old, new):
        text = self.clean.read_text(encoding="utf-8")
        self.assertIn(old, text)
        self.clean.write_text(text.replace(old, new, 1), encoding="utf-8")

    def test_sample_passes(self):
        results = check_clean(self.draft, self.clean, FILLERS)
        self.assertEqual(len(results), 16)
        self.assertTrue(all(r.ok for r in results), [(r.name, r.problems) for r in results if not r.ok])

    def test_fail_one_word_changed(self):
        self.edit_clean("tapped the first time slot", "tapped the first delivery slot")
        self.assertTrue(any("words differ" in p for p in self.run_check()["turn 04"].problems))

    def test_fail_word_dropped(self):
        self.edit_clean("I did not think about", "I did not think")
        self.assertTrue(any("words differ" in p for p in self.run_check()["turn 04"].problems))

    def test_pass_case_punctuation_and_spacing(self):
        self.edit_clean("Sure. It was", "SURE,   it was")
        self.assertTrue(self.run_check()["turn 02"].ok)

    def test_fail_undeclared_filler_kept_out(self):
        self.draft.write_text(self.draft.read_text(encoding="utf-8").replace("Um, sure.", "Well, sure.", 1), encoding="utf-8")
        self.assertTrue(any("words differ" in p for p in self.run_check()["turn 02"].problems))

    def test_fail_speaker_changed(self):
        self.edit_clean("02 P1:", "02 Interviewer:")
        self.assertIn("speaker differs: draft P1, clean Interviewer", self.run_check()["turn 02"].problems)

    def test_fail_turn_removed(self):
        lines = [l for l in self.clean.read_text(encoding="utf-8").splitlines() if not l.startswith("08 ")]
        self.clean.write_text("\n".join(lines) + "\n", encoding="utf-8")
        self.assertIn("draft has 16 lines, clean has 15 turns", self.run_check()["file"].problems)

    def test_fail_unresolved_question_mark(self):
        self.edit_clean("Support was polite.", "Support was [?] polite.")
        self.assertIn("marked [?]: listen to the recording and fix", self.run_check()["turn 08"].problems)

    def test_fail_name_still_present(self):
        self.edit_clean("Thanks for making time.", "Thanks for making time, Lan.")
        problems = self.run_check(names=["Lan", "Tech Mart"])["turn 01"].problems
        self.assertIn("name Lan still present", problems)

    def test_name_match_is_whole_word(self):
        self.edit_clean("Can you tell", "Can you tell me about Landing. Can you tell")
        self.assertTrue(all("name" not in p for p in self.run_check(names=["Lan"])["turn 01"].problems))

    def write_pair(self, draft, clean, form="NFC"):
        for path, text in ((self.draft, draft), (self.clean, clean)):
            path.write_text(unicodedata.normalize(form, text), encoding="utf-8")

    def test_fail_no_turns_read(self):
        self.write_pair("note\n[00:00:01] Speaker 1: yes\n", "note\n01 Speaker 1: no\n")
        self.assertIn("no turns found", self.run_check()["file"].problems)

    def test_fail_wrapped_line(self):
        self.write_pair("note\n[00:00:01] P1: yes\nand more\n", "note\n01 P1: yes\nsomething else\n")
        self.assertIn("clean line 3 is not a turn", self.run_check()["file"].problems)

    def test_fail_tone_changed_in_decomposed_files(self):
        self.write_pair("note\n[00:00:01] P1: má\n", "note\n01 P1: mà\n", form="NFD")
        self.assertFalse(self.run_check()["turn 01"].ok)

    def test_pass_same_words_in_different_unicode_forms(self):
        self.write_pair("note\n[00:00:01] P1: má\n", "note\n01 P1: má\n")
        self.draft.write_text(unicodedata.normalize("NFD", self.draft.read_text(encoding="utf-8")), encoding="utf-8")
        self.assertTrue(self.run_check()["turn 01"].ok)

    def test_fail_name_in_speaker_label_with_padded_list_entry(self):
        self.write_pair("note\n[00:00:01] Lan: yes\n", "note\n01 Lan: yes\n")
        self.assertIn("name Lan still present", self.run_check(names=["Lan "])["turn 01"].problems)

    def test_fail_name_in_note_line(self):
        self.edit_clean("Participant: P1.", "Participant: Lan.")
        self.assertIn("name Lan still present", self.run_check(names=["Lan"])["file"].problems)

    def test_filler_with_space_after_comma(self):
        results = check_clean(self.draft, self.clean, ["um", " uh"])
        self.assertTrue(all(r.ok for r in results))


if __name__ == "__main__":
    unittest.main()
