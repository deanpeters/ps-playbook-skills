#!/usr/bin/env python3
"""Build the ChatGPT upload kit from this library, using Python's standard library."""

import argparse
import hashlib
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
UPLOADS = HERE / "uploads"
PHASE_FILES = {
    "Context": "02-context.md",
    "Discover + Investigate": "03-discover-investigate.md",
    "Discover + Define": "04-discover-define.md",
    "Create": "05-create.md",
    "Deliver": "06-deliver.md",
}
TITLES = {
    "blueprint-advisor": "Blueprint navigator",
    "outcome-strategy-discussion": "Outcome & Strategy Discussion",
    "stakeholder-alignment": "Stakeholder Alignment",
    "outcome-tree": "Outcome Tree (Sections One and Two)",
    "market-selection-sizing": "Market Selection & Sizing",
    "jobs-to-be-done": "Jobs-to-Be-Done & Outcomes",
    "proto-persona": "Personas & Proto-Personas",
    "empathy-interviews": "Empathy Interviews",
    "affinity-mapping": "Affinity Mapping",
    "problem-identification": "Problem Identification",
    "framing-the-problem": "Framing the Problem",
    "exploring-solution-space": "Exploring the Solution Space",
    "solution-hypothesis": "Solution Hypothesis",
    "positioning-statement": "Positioning Statement",
    "lofi-experimentation": "Lo-fi Experimentation",
    "storyboarding": "Storyboarding",
    "risk-assessment": "Risk Assessment",
    "product-outcome-canvas": "Product Outcome Canvas",
    "outcome-roadmap": "Outcome-Based Roadmap & Release Plan",
    "tiny-acts-discovery": "Tiny Acts of Discovery",
    "output-prioritization": "Output Prioritization",
    "go-to-market": "Go-to-Market Enablement",
    "product-readiness": "Product Readiness Testing",
    "measuring-outcomes": "Measuring Outcomes",
    "process-retrospective": "Process Retrospective",
}
STATUS = "November 2026 B2B work-in-progress Playbook. Not yet ratified."


def without_frontmatter(text):
    if text.startswith("---\n"):
        return text.split("---", 2)[2].lstrip()
    return text


def description(text):
    """Read only the existing description scalar, not arbitrary YAML."""
    front = text.split("---", 2)[1]
    match = re.search(r"^description: ([^\n]*)(?:\n((?:  [^\n]*\n)+))?", front, re.M)
    if not match:
        raise ValueError("Missing skill description")
    first, continuation = match.groups()
    if first.strip() in (">-", ">", "|-", "|"):
        return " ".join((continuation or "").split())
    return first.strip().strip('"')


def load_plays():
    """Use the existing catalog's order, numbering, and phase assignments."""
    plays = []
    phase = None
    for line in (ROOT / "skills/README.md").read_text().splitlines():
        if line.startswith("### "):
            phase = line[4:]
        match = re.match(r"\| \[(ps-[\w-]+)\]\([^)]+\) \| ([^|]+) \|", line)
        if not match:
            continue
        play_id, number = match.groups()
        title = TITLES[play_id[3:]]
        filename = "01-playbook-navigator.md" if phase == "Navigator (cross-phase)" else PHASE_FILES[phase]
        number = number.strip()
        if not re.fullmatch(r"\d+(?: \+ \d+)?", number):
            number = "Unnumbered"
        folder = ROOT / "skills" / play_id
        plays.append({"id": play_id, "title": title, "number": number,
                      "phase": phase, "file": filename, "folder": folder,
                      "description": description((folder / "SKILL.md").read_text())})
    actual = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}
    if {p["id"] for p in plays} != actual or len(plays) != len(actual):
        raise ValueError("Skill catalog and skill folders differ; update skills/README.md first")
    numbers = [int(n) for p in plays for n in re.findall(r"\d+", p["number"])]
    if sorted(numbers) != list(range(1, 25)):
        raise ValueError("Expected exactly one catalog entry for each numbered Play, 01-24")
    return plays


def build():
    plays = load_plays()
    locations = {}
    inputs = {ROOT / "skills/README.md", ROOT / "LICENSE", HERE / "project-instructions.txt", HERE / "build.py"}

    def register(path, filename, section):
        inputs.add(path)
        locations[path.resolve()] = (filename, section)

    for play in plays:
        folder, play_id = play["folder"], play["id"]
        for relative, section in [("SKILL.md", "Instructions"), ("template.md", "Template"),
                                  ("examples/sample.md", "Examples")]:
            register(folder / relative, play["file"], f"{play_id} / {section}")
        for reference in sorted((folder / "reference").glob("*.md")):
            register(reference, play["file"], f"{play_id} / Reference {reference.stem}")
        for prompt in sorted((folder / "prompts").glob("*.md")):
            register(prompt, "07-prompts.md", f"{play_id} / Companion / {prompt.name}")
    deck_prompts = sorted((ROOT / "prompts").glob("*/*.md"))
    for prompt in deck_prompts:
        register(prompt, "07-prompts.md", f"Deck / {prompt.parent.name} / {prompt.name}")

    def render(path):
        """Resolve repository links outside fences; never change prompt bodies."""
        text = without_frontmatter(path.read_text())
        output = []
        fence = None
        # splitlines() would also normalize Unicode separators inside verbatim prompts.
        for line in text.split("\n"):
            marker = re.match(r"\s*(`{3,}|~{3,})", line)
            if marker:
                token = marker.group(1)
                if fence is None:
                    fence = token
                elif token[0] == fence[0] and len(token) >= len(fence):
                    fence = None
                output.append(line)
                continue
            if fence is not None:
                output.append(line)
                continue

            def resolve(match):
                label, target = match.groups()
                if re.match(r"(?:https?://|mailto:|#)", target):
                    return match.group(0)
                local = (path.parent / target.split("#", 1)[0]).resolve()
                if local.is_dir():
                    local = local / ("SKILL.md" if (local / "SKILL.md").exists() else "README.md")
                if local in locations:
                    filename, section = locations[local]
                    return f"{label} (uploaded reference: `{filename}`, section `{section}`)"
                if local.suffix in (".pdf", ".docx", ".pptx"):
                    return f"{label} (source material, not included in this upload kit)"
                raise ValueError(f"Unmapped reference in {path.relative_to(ROOT)}: {target}")

            line = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", resolve, line)
            # Nest source headings below the unique section marker.
            line = re.sub(r"^(#{1,5}) ", r"##\1 ", line)
            output.append(line)
        return "\n".join(output).rstrip() + "\n"

    def section(path):
        filename, heading = locations[path.resolve()]
        metadata = ""
        if path.parent.name == "prompts" or path in deck_prompts:
            raw = path.read_text()
            if raw.startswith("---\n"):
                metadata = "Source metadata (preserved):\n\n```yaml\n" + raw.split("---", 2)[1].strip() + "\n```\n\n"
        return f"\n### {heading}\n\n" + metadata + render(path)

    outputs = {}
    catalog = ["# Playbook navigator and catalog\n", STATUS,
               "\nThese are uploaded Play references, not installed skills. Use the exact filename and section below. A ps- identifier is a stable lookup label, not a tool call.\n",
               "## Find a Play\n",
               "| Play | Name | Stable identifier | Uploaded filename | Section to read |",
               "|---|---|---|---|---|"]
    for play in plays:
        catalog.append(f'| {play["number"]} | {play["title"]} | `{play["id"]}` | `{play["file"]}` | `{play["id"]} / Instructions` |')
    catalog += ["\nPlay 03 and Play 23 both resolve to ps-outcome-tree in 02-context.md. Read its Section One or Section Two as appropriate. Section Two serves the later Deliver work even though both sections are stored together in the Context file.",
                "Storyboarding is unnumbered in this edition and lives in 04-discover-define.md. Play 16 means Product Outcome Canvas. If the user uses older numbering, ask which edition or Play name they mean.",
                "\n## Choose by the work in front of you\n"]
    for play in plays:
        catalog.append(f'### {play["title"]} | {play["id"]}\n\n{play["description"]}\n')
    catalog += ["## Using another Play\n",
                "Read that Play's uploaded Instructions, Template, and Examples sections through this catalog. Offer it as a next step and accept equivalent inputs. Do not ask the user to install a skill or pretend to invoke one. If its reference is unavailable, name the missing filename and section and ask for them. Never fill the gap with invented Productside instructions.\n"]
    outputs["01-playbook-navigator.md"] = "\n".join(catalog) + "\n"
    for phase, filename in PHASE_FILES.items():
        outputs[filename] = f"# {phase}: Play references\n\n{STATUS}\n\nFind Plays by stable identifier in 01-playbook-navigator.md. Each Play below contains its instructions, template, and examples. Mentions of skills or agents in the preserved source mean applying the Play from these uploaded references.\n"
    for play in plays:
        filename, folder = play["file"], play["folder"]
        outputs[filename] += f'\n## {play["id"]} | {play["title"]}\n\nPlaybook number: {play["number"]}. Phase: {play["phase"]}.\n'
        for name in ["SKILL.md", "template.md", "examples/sample.md"]:
            outputs[filename] += section(folder / name)
        for reference in sorted((folder / "reference").glob("*.md")):
            outputs[filename] += section(reference)
    outputs["07-prompts.md"] = f"# Prompts by Play\n\n{STATUS}\n\nPrompt text and source metadata are preserved. Deck prompts come from the standalone prompts/ collection. Play companion prompts come from the individual Play folders and include authored prompts. These collections can reflect different source revisions; do not treat them as identical. For a standalone Playbook prompt request, choose Deck prompts when available. For a Play's supporting prompt, choose its Companion entry. For full Play guidance, read the catalog's Instructions and Template references instead.\n\n## Deck prompts\n"
    for prompt in deck_prompts:
        outputs["07-prompts.md"] += section(prompt)
    outputs["07-prompts.md"] += "\n## Play companion prompts\n"
    for play in plays:
        for prompt in sorted((play["folder"] / "prompts").glob("*.md")):
            outputs["07-prompts.md"] += section(prompt)
    outputs["08-license.md"] = (ROOT / "LICENSE").read_text()
    digest = hashlib.sha256()
    for path in sorted(inputs):
        digest.update(str(path.relative_to(ROOT)).encode())
        digest.update(path.read_bytes())
    revision = digest.hexdigest()[:16]
    outputs["00-start-here.md"] = f"""# Productside Playbook: start here

Use this reference library to work through a Productside Playbook Play, one guided exercise for a piece of product work. You bring your context and judgment. AI pressure-tests your thinking.

## Try it

Start a new chat in this Project and ask:

> Help me choose a Play. Our warehouse supervisors abandon our scheduling tool after their first week. Guide me one question at a time.

Or name a Play:

> Use Play 05, Jobs-to-Be-Done & Outcomes, to review my draft. First find its instructions and template in the uploaded references.

> Use the Outcome Tree, Section Two (Play 23), to revisit our original outcomes against what we learned.

## How to find the Plays

Read `01-playbook-navigator.md`. Its catalog maps each Play's number, name, and stable ps- identifier to an uploaded filename and exact section. There are 25 references covering 24 numbered Plays, an unnumbered Blueprint navigator, and unnumbered Storyboarding. The two Outcome Tree Plays share one reference.

These files are reference documents. No skills are installed. You can ask by name, number, identifier, or describe your task. Before applying a Play, the assistant should read that Play's Instructions, Template, and Examples sections. If it cannot find them, it should ask for the missing reference and say what is unavailable.

## Files in this kit

- `01-playbook-navigator.md`: catalog, routing, and Blueprint guidance.
- `02-context.md`: strategy, stakeholders, outcome trees, and market selection.
- `03-discover-investigate.md`: jobs, personas, interviews, synthesis, and problems.
- `04-discover-define.md`: solution exploration, hypotheses, positioning, experiments, Storyboarding, risks, and Product Outcome Canvas.
- `05-create.md`: roadmaps, tiny discovery acts, prioritization, launch, and readiness.
- `06-deliver.md`: measurement and retrospectives.
- `07-prompts.md`: deck prompts and Play companion prompts, with source labels.
- `08-license.md`: Productside license and attribution.

## Keep the work grounded

The Product Manager does the thinking, and AI pressure-tests it. AI-generated examples and customer details are assumptions to validate. Real interviews, team sessions, experiments, and decisions belong to people. You can bring equivalent prior work without completing every earlier Play.

Keep unrelated products and clients in separate Projects. Before sharing, review the available audience settings and what other members can access. For independent learners, distribute this setup kit so each person can create a separate Project with their own context.

## Source and updates

{STATUS}

Source: deanpeters/ps-playbook-skills. Content fingerprint: `{revision}`. This is an uploaded snapshot; changing GitHub does not update these files. Replace the complete upload set when updating. PDF excerpts, full source decks, and external maintenance documents are not included. References to them in the preserved Play text describe provenance, not material the assistant has read.

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. See 08-license.md.
"""
    return {name: content.rstrip() + "\n" for name, content in outputs.items()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check generated files without changing them")
    args = parser.parse_args()
    try:
        outputs = build()
        existing = {p.name for p in UPLOADS.iterdir() if p.is_file()} if UPLOADS.exists() else set()
        unexpected = existing - outputs.keys()
        if unexpected:
            raise ValueError(f"Unexpected upload files; review manually: {', '.join(sorted(unexpected))}")
        stale = [name for name, content in outputs.items()
                 if not (UPLOADS / name).exists() or (UPLOADS / name).read_text() != content]
        if args.check:
            if stale:
                print("Out of date: " + ", ".join(stale), file=sys.stderr)
                return 1
            print(f"PASS: {len(outputs)} upload files match the source library.")
        else:
            UPLOADS.mkdir(exist_ok=True)
            for name, content in outputs.items():
                (UPLOADS / name).write_text(content)
            print(f"Built {len(outputs)} upload files in {UPLOADS.relative_to(ROOT)}/")
        return 0
    except (ValueError, KeyError, FileNotFoundError) as error:
        print(f"Cannot build Project kit: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
