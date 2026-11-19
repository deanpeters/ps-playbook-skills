#!/usr/bin/env python3
"""Build or verify skill bundles, Claude plugin ZIPs, and the shared Project kit."""

import argparse
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
VERSION = "0.1.0"
REPOSITORY = "https://github.com/deanpeters/ps-playbook-skills"
COLLECTIONS = {
    "context": "Context",
    "discover-investigate": "Discover + Investigate",
    "discover-define": "Discover + Define",
    "create": "Create",
    "deliver": "Deliver",
    "full-library": "Full library",
}


def project_builder():
    spec = importlib.util.spec_from_file_location("playbook_project_builder", ROOT / "project/build.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read(path):
    return (ROOT / path).read_bytes()


def snapshot(files):
    digest = hashlib.sha256()
    for name, data in sorted(files.items()):
        digest.update(name.encode())
        digest.update(data)
    return digest.hexdigest()[:16]


def package_readme(title, kind, plays, prompts, fingerprint):
    intro = ("Unpack this ZIP to use the skills and prompts as files. A bundle does not install itself."
             if kind == "bundle" else
             "This is a Claude plugin package. Use Claude's custom-plugin installation flow. "
             "A plugin ZIP is not the three-document Project kit.")
    first = plays[0]["id"]
    text = f"""# Productside Playbook: {title}

{intro}

Version: {VERSION}. Source fingerprint: {fingerprint}.

## Try it

"""
    if kind == "bundle":
        text += "Open a prompt under prompts/ and copy its text box into your AI chat. Or attach a chosen skills/psk-.../SKILL.md, which includes its template and examples.\n\n"
    else:
        text += "After installation, find the included skills in your assistant. Ask for a skill by its psk- identifier, or select it from the available skills list.\n\n"
    text += f"> Use {first} for [my product and customer]. Start in Guided mode and ask one question at a time.\n\n"
    text += "Guided teaches while completing the work. Expert uses supplied context and offers coaching on demand. Discovery sketches or simulates with synthesized assumptions labeled. People own research and decisions.\n\n"
    text += f"## Included skills ({len(plays)})\n\n"
    text += "\n".join(f'- [{p["title"]}](skills/{p["id"]}/SKILL.md) (`{p["id"]}`)' for p in plays)
    if kind == "bundle":
        text += f"\n\nIncludes {len(prompts)} matching prompt files. The original Playbook tasks and library-added interaction instructions are labeled separately.\n"
        text += "\nFor a shared prompt library, copy the prompts/ folder to an approved SharePoint library, shared drive, or wiki. Add a simple index and keep one reviewed version for your team. A shared folder does not install skills or automatically connect an AI assistant.\n"
    text += "\nOutcome Tree Sections One and Two share one skill, packaged in Context and the full library. The Blueprint navigator is in the full library only.\n"
    text += "\n## Status and license\n\nContent follows the November 2026 B2B work-in-progress Playbook, not yet ratified. Archive checks and plugin-manifest validation do not establish live installation or behavioral results.\n\n"
    text += f"Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. See [LICENSE](LICENSE). [Setup and current validation status]({REPOSITORY}/tree/main/downloads).\n"
    return text.encode()


def payloads():
    builder = project_builder()
    generated = builder.build()
    for name, content in generated.items():
        path = ROOT / "project/uploads" / name
        if not path.exists() or path.read_text() != content:
            raise ValueError("Project sources are stale. Run python3 project/build.py first.")
    plays = builder.load_plays()
    prompt_files = sorted((ROOT / "prompts").glob("*/*.md"))
    output = {}
    for slug, phase in COLLECTIONS.items():
        selected = plays if slug == "full-library" else [p for p in plays if p["phase"] == phase]
        if not selected:
            raise ValueError(f"No skills in {phase}")
        ids = {p["id"] for p in selected}
        prompts = [p for p in prompt_files if builder.prompt_skill(p) in ids]
        skills = {f'skills/{p["id"]}/SKILL.md': (p["folder"] / "SKILL.md").read_bytes() for p in selected}
        for kind in ("bundle", "plugin"):
            files = {**skills, "LICENSE": read("LICENSE")}
            if kind == "bundle":
                files.update({str(p.relative_to(ROOT)): p.read_bytes() for p in prompts})
            else:
                manifest = {
                    "name": f"psk-playbook-{slug}",
                    "version": VERSION,
                    "description": f"Productside Playbook skills for {phase.lower()} with Guided, Expert, and Discovery modes.",
                    "author": {"name": "Dean Peters"},
                    "repository": REPOSITORY,
                    "license": "SEE LICENSE IN LICENSE",
                }
                files[".claude-plugin/plugin.json"] = (json.dumps(manifest, indent=2) + "\n").encode()
            files["README.md"] = package_readme(phase, kind, selected, prompts, snapshot(files))
            folder = "bundles" if kind == "bundle" else "plugins"
            output[f"{folder}/psk-{kind}-{slug}.zip"] = files
    kit = {"LICENSE": read("LICENSE")}
    for relative in ["project/README.md", "project/project-instructions.md", "project/project-instructions-compact.txt", "project/smoke-checks.md"]:
        content = read(relative)
        if relative == "project/README.md":
            content = content.replace(b"(../skills/README.md)", f"({REPOSITORY}/tree/main/skills)".encode())
        kit[relative] = content
    kit.update({f"project/uploads/{name}": content.encode() for name, content in generated.items()})
    kit["README.md"] = f"""# Productside Playbook: Project kit

Start with [project/README.md](project/README.md). It explains Claude Projects, ChatGPT Projects, Microsoft 365 Copilot Notebooks or Agents, and Gemini Skills (formerly Gems).

Unpack this ZIP. Add the three documents in project/uploads/ as reference content in your tool's supported format. Paste project/project-instructions-compact.txt into its instructions field; project/project-instructions.md is the detailed reference. Follow the platform-specific format notes in the setup guide, including plain-text copies for Microsoft 365 Agent uploads.

Version: {VERSION}. Source fingerprint: {snapshot(kit)}.

Uploaded files do not update automatically from GitHub. Replace all three sources together and test both a prompt and a full Play before sharing. This kit is reference content, not a Claude plugin or Gemini SKILL.md upload package.

Based on materials from Productside. See [LICENSE](LICENSE) for CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. Source content is work-in-progress, not yet ratified. Live platform installation and behavior remain unverified.
""".encode()
    output["bundles/psk-project-kit.zip"] = kit
    return output


def archive_bytes(files):
    output = io.BytesIO()
    with ZipFile(output, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for name, content in sorted(files.items()):
            if name.startswith("/") or ".." in Path(name).parts or "\\" in name:
                raise ValueError(f"Unsafe archive path: {name}")
            entry = ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            entry.compress_type = ZIP_DEFLATED
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, content, compresslevel=9)
    return output.getvalue()


def verify(data, files):
    with ZipFile(io.BytesIO(data)) as archive:
        names = archive.namelist()
        if archive.testzip() or len(names) != len(set(names)) or set(names) != set(files):
            raise ValueError("Archive contents differ from the expected files")
        for name, expected in files.items():
            if archive.read(name) != expected:
                raise ValueError(f"Archive source mismatch: {name}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check ZIPs against current sources without writing")
    args = parser.parse_args()
    try:
        packages = payloads()
        expected = set(packages)
        existing = {str(p.relative_to(HERE)) for directory in (HERE / "bundles", HERE / "plugins") for p in directory.glob("*.zip")}
        unexpected = existing - expected
        if unexpected:
            raise ValueError("Unexpected ZIPs need manual review: " + ", ".join(sorted(unexpected)))
        for relative, files in packages.items():
            target = HERE / relative
            desired = archive_bytes(files)
            verify(desired, files)
            if args.check:
                if not target.exists() or target.read_bytes() != desired:
                    raise ValueError(f"Stale or missing ZIP: {relative}. Run python3 downloads/build.py.")
                verify(target.read_bytes(), files)
            else:
                target.parent.mkdir(exist_ok=True)
                with tempfile.NamedTemporaryFile(dir=target.parent, suffix=".zip.tmp", delete=False) as temporary:
                    temporary.write(desired)
                    temp_path = Path(temporary.name)
                try:
                    temp_path.replace(target)
                finally:
                    temp_path.unlink(missing_ok=True)
            print(f'{"Checked" if args.check else "Built"} {relative}: {len(files)} files')
        print(f"PASS: {len(packages)} packages; sources preserved, license included, deterministic ZIPs.")
        return 0
    except (ValueError, OSError) as error:
        print(f"Cannot package downloads: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
