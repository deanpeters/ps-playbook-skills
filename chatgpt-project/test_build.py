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
        catalog = self.outputs[build.GUIDE]
        self.assertEqual(len(self.plays), 25)
        for play in self.plays:
            self.assertIn(f'[{play["id"]}]', catalog)
            document = self.outputs[play["file"]]
            for part in ["Instructions", "Template", "Examples"]:
                self.assertIn(f'#### {play["id"]} / {part}\n', document)
        self.assertIn("Section Two of the Outcome Tree (Play 23) points to the same full skill as Section One (Play 03)", catalog)
        self.assertIn("Play 16 is Product Outcome Canvas", catalog)

    def test_every_reference_link_has_a_real_file_and_heading(self):
        headings = {}
        for filename, text in self.outputs.items():
            found = set()
            fence = None
            for line in text.split("\n"):
                marker = re.match(r"\s*(`{3,}|~{3,})", line)
                if marker:
                    token = marker.group(1)
                    if fence is None:
                        fence = token
                    elif token[0] == fence[0] and len(token) >= len(fence):
                        fence = None
                    continue
                if fence is None:
                    match = re.match(r"^#{1,6} (.*)", line)
                    if match:
                        found.add(build.section_slug(match.group(1)))
            headings[filename] = found
        count = 0
        for filename, text in self.outputs.items():
            for link in re.findall(r"\]\(([^)]+)\)", text):
                if link.startswith(("https://", "http://", "mailto:")):
                    continue
                target, _, anchor = link.partition("#")
                target = target or filename
                count += 1
                self.assertIn(target, self.outputs)
                if anchor:
                    self.assertIn(anchor, headings[target], link)
        self.assertGreater(count, 100)

    def test_prompt_bodies_are_preserved_with_duplicate_counts(self):
        sources = list((build.ROOT / "prompts").glob("*/*.md"))
        expected = Counter(body for source in sources
                           for body in re.findall(r'```text\n(.*?)```', source.read_text(), re.S))
        actual = Counter(re.findall(r'```text\n(.*?)```', self.outputs[build.PROMPTS], re.S))
        self.assertTrue(expected, "The upload kit must include the library's prompts")
        self.assertEqual(actual, expected)

    def test_guide_routes_every_play_to_both_paths_in_outline_order(self):
        entries = build.play_entries(self.plays)
        self.assertEqual(len(entries), 26)
        for filename in [build.GUIDE, build.PROMPTS]:
            positions = [self.outputs[filename].index(f'### {entry["heading"]}\n') for entry in entries]
            self.assertEqual(positions, sorted(positions))
        for entry in entries:
            self.assertIn(f'#### {entry["id"]} / Instructions\n', self.outputs[build.SKILLS])
            self.assertEqual(self.outputs[build.SKILLS].count(f'#### {entry["id"]} / Instructions\n'), 1)
        guide = self.outputs[build.GUIDE]
        self.assertEqual(guide.count("**Prompt route:**"), 26)
        self.assertEqual(guide.count("**Skill route:**"), 26)
        snapshots = [re.search(r"Source snapshot: `([^`]+)`", text).group(1) for text in self.outputs.values()]
        self.assertEqual(len(set(snapshots)), 1)

    def test_each_play_is_one_self_contained_file(self):
        for play in self.plays:
            self.assertEqual([p.name for p in play["folder"].iterdir()], ["SKILL.md"])
            text = (play["folder"] / "SKILL.md").read_text()
            for heading in ["## Purpose", "## Application", "## Template", "## Examples", "## Common Pitfalls"]:
                self.assertIn(heading, text)
            self.assertNotIn("template.md", text)
            self.assertNotIn("examples/sample.md", text)

    def test_prompts_cover_every_play_and_keep_provenance_distinct(self):
        covered = set()
        numbers = set()
        groups = {"Deck": set(), "Library-authored": set()}
        for path in (build.ROOT / "prompts").glob("*/*.md"):
            text = path.read_text()
            front = text.split("---", 2)[1]
            play_id = re.search(r"^skill: (ps-[\w-]+)$", front, re.M).group(1)
            covered.add(play_id)
            group = build.prompt_group(path)
            groups[group].add(play_id)
            self.assertIn(f"#### {group} / {path.parent.name} / {path.name}\n", self.outputs[build.PROMPTS])
            number = re.search(r"^play_number: (\d+)$", front, re.M)
            if number:
                numbers.add(int(number.group(1)))
            if group == "Library-authored":
                self.assertIn("**Source:** Authored for this library", text)
                self.assertIn("one question at a time", text)
        self.assertEqual(covered, {play["id"] for play in self.plays})
        self.assertEqual(numbers, set(range(1, 25)))
        self.assertFalse(groups["Deck"] & groups["Library-authored"])

    def test_authored_prompt_cannot_be_packaged_as_deck_text(self):
        original_read = Path.read_text
        prompt = next((build.ROOT / "prompts/15-risk-assessment").glob("*.md"))

        def read(path, *args, **kwargs):
            text = original_read(path, *args, **kwargs)
            if path == prompt:
                return text.replace("  kind: authored\n", "  kind: unknown\n")
            return text

        with patch.object(Path, "read_text", read):
            with self.assertRaisesRegex(ValueError, "Unknown prompt source"):
                build.build()

    def test_license_is_unchanged_and_upload_set_is_small(self):
        self.assertEqual(set(self.outputs), {build.GUIDE, build.PROMPTS, build.SKILLS})
        self.assertIn((build.ROOT / "LICENSE").read_text().rstrip(), self.outputs[build.GUIDE])

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
            changed = destination / build.SKILLS
            changed.write_text("outdated upload\n")
            with patch.object(build, "UPLOADS", destination), patch("sys.argv", ["build.py", "--check"]):
                with contextlib.redirect_stderr(io.StringIO()):
                    self.assertEqual(build.main(), 1)
            self.assertEqual(changed.read_text(), "outdated upload\n")


if __name__ == "__main__":
    unittest.main()
