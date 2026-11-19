"""Packaging checks; these do not run or score ChatGPT behavior."""

from collections import Counter
import contextlib
import io
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import patch

import build


class ProjectKitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.outputs = build.build()
        cls.plays = build.load_plays()

    def test_all_plays_have_real_catalog_destinations(self):
        catalog = self.outputs["01-playbook-navigator.md"]
        self.assertEqual(len(self.plays), 25)
        for play in self.plays:
            self.assertIn(f'`{play["id"]}`', catalog)
            document = self.outputs[play["file"]]
            for part in ["Instructions", "Template", "Examples"]:
                self.assertIn(f'### {play["id"]} / {part}\n', document)
        self.assertIn("Play 03 and Play 23 both resolve to ps-outcome-tree in 02-context.md", catalog)
        self.assertIn("Play 16 means Product Outcome Canvas", catalog)

    def test_every_rewritten_reference_has_a_destination(self):
        count = 0
        for document in self.outputs.values():
            for filename, section in re.findall(r'uploaded reference: `([^`]+)`, section `([^`]+)`', document):
                count += 1
                self.assertIn(filename, self.outputs)
                self.assertIn(f"### {section}\n", self.outputs[filename])
            for link in re.findall(r'\]\(([^)]+)\)', document):
                self.assertTrue(link.startswith(("https://", "http://", "mailto:", "#")), link)
        self.assertGreater(count, 0)

    def test_prompt_bodies_are_preserved_with_duplicate_counts(self):
        sources = list((build.ROOT / "prompts").glob("*/*.md"))
        expected = Counter(body for source in sources
                           for body in re.findall(r'```text\n(.*?)```', source.read_text(), re.S))
        actual = Counter(re.findall(r'```text\n(.*?)```', self.outputs["07-prompts.md"], re.S))
        self.assertTrue(expected, "The upload kit must include the library's prompts")
        self.assertEqual(actual, expected)

    def test_each_play_is_one_self_contained_file(self):
        for play in self.plays:
            self.assertEqual([p.name for p in play["folder"].iterdir()], ["SKILL.md"])
            text = (play["folder"] / "SKILL.md").read_text()
            for heading in ["## Purpose", "## Application", "## Template", "## Examples", "## Common Pitfalls"]:
                self.assertIn(heading, text)
            self.assertNotIn("template.md", text)
            self.assertNotIn("examples/sample.md", text)

    def test_license_is_unchanged_and_upload_set_is_small(self):
        self.assertEqual(len(self.outputs), 9)
        self.assertEqual(self.outputs["08-license.md"], (build.ROOT / "LICENSE").read_text().rstrip() + "\n")

    def test_missing_catalog_entry_fails_instead_of_omitting_a_play(self):
        original_read = Path.read_text
        catalog = build.ROOT / "skills/README.md"

        def read(path, *args, **kwargs):
            text = original_read(path, *args, **kwargs)
            if path == catalog:
                return "\n".join(line for line in text.splitlines() if "[ps-jobs-to-be-done]" not in line)
            return text

        with patch.object(Path, "read_text", read):
            with self.assertRaisesRegex(ValueError, "catalog and skill folders differ"):
                build.build()

    def test_check_detects_stale_output_without_overwriting(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory)
            for name, content in self.outputs.items():
                (destination / name).write_text(content)
            changed = destination / "03-discover-investigate.md"
            changed.write_text("outdated upload\n")
            with patch.object(build, "UPLOADS", destination), patch("sys.argv", ["build.py", "--check"]):
                with contextlib.redirect_stderr(io.StringIO()):
                    self.assertEqual(build.main(), 1)
            self.assertEqual(changed.read_text(), "outdated upload\n")


if __name__ == "__main__":
    unittest.main()
