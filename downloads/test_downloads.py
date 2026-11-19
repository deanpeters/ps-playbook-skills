"""Archive checks. These do not install plugins or run model sessions."""

import importlib.util
import io
import json
from pathlib import Path
import unittest
from zipfile import ZipFile

spec = importlib.util.spec_from_file_location("download_builder", Path(__file__).with_name("build.py"))
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


class DownloadTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.packages = build.payloads()

    def test_release_contains_both_formats_and_project_kit(self):
        expected = {f"{folder}/psk-{kind}-{slug}.zip"
                    for folder, kind in [("bundles", "bundle"), ("plugins", "plugin")]
                    for slug in build.COLLECTIONS}
        expected.add("bundles/psk-project-kit.zip")
        self.assertEqual(set(self.packages), expected)
        self.assertEqual(len(expected), 13)

    def test_membership_namespaces_and_source_content(self):
        expected_counts = {"context": (4, 8), "discover-investigate": (6, 9),
                           "discover-define": (7, 11), "create": (5, 7),
                           "deliver": (2, 2), "full-library": (25, 38)}
        for slug, (skills, prompts) in expected_counts.items():
            for folder, kind in [("bundles", "bundle"), ("plugins", "plugin")]:
                files = self.packages[f"{folder}/psk-{kind}-{slug}.zip"]
                skill_files = [name for name in files if name.startswith("skills/")]
                self.assertEqual(len(skill_files), skills)
                for name in skill_files:
                    self.assertRegex(name, r"^skills/psk-[a-z0-9-]+/SKILL\.md$")
                    self.assertEqual(files[name], (build.ROOT / name).read_bytes())
                self.assertEqual(files["LICENSE"], (build.ROOT / "LICENSE").read_bytes())
                if kind == "bundle":
                    prompt_files = [name for name in files if name.startswith("prompts/")]
                    self.assertEqual(len(prompt_files), prompts)
                    for name in prompt_files:
                        self.assertEqual(files[name], (build.ROOT / name).read_bytes())
                else:
                    manifest = json.loads(files[".claude-plugin/plugin.json"])
                    self.assertEqual(manifest["name"], f"psk-playbook-{slug}")
                    self.assertEqual(manifest["version"], build.VERSION)
                    self.assertFalse(any(name.startswith("prompts/") for name in files))

    def test_project_kit_has_current_sources_and_instructions(self):
        files = self.packages["bundles/psk-project-kit.zip"]
        self.assertEqual(len(files), 9)
        for path in (build.ROOT / "project/uploads").glob("*.md"):
            self.assertEqual(files[str(path.relative_to(build.ROOT))], path.read_bytes())
        compact = files["project/project-instructions-compact.txt"].decode()
        self.assertLessEqual(len(compact), 7700)
        self.assertIn("project/README.md", files)
        self.assertNotIn(b"(../skills/README.md)", files["project/README.md"])

    def test_current_archives_are_deterministic_and_match_payloads(self):
        for relative, files in self.packages.items():
            expected = build.archive_bytes(files)
            self.assertEqual(expected, build.archive_bytes(files))
            self.assertEqual((build.HERE / relative).read_bytes(), expected)
            build.verify(expected, files)
            with ZipFile(io.BytesIO(expected)) as archive:
                self.assertFalse(any(".DS_Store" in name or "__pycache__" in name for name in archive.namelist()))

    def test_mismatched_archive_content_is_rejected(self):
        files = {"LICENSE": b"license", "skills/psk-test/SKILL.md": b"original"}
        wrong = dict(files, **{"skills/psk-test/SKILL.md": b"changed"})
        with self.assertRaisesRegex(ValueError, "source mismatch"):
            build.verify(build.archive_bytes(wrong), files)

    def test_unsafe_archive_paths_are_rejected(self):
        for path in ["../outside", "/absolute", "folder/../../outside", "folder\\outside"]:
            with self.subTest(path=path), self.assertRaisesRegex(ValueError, "Unsafe archive path"):
                build.archive_bytes({path: b"content"})


if __name__ == "__main__":
    unittest.main()
