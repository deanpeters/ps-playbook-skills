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
PHASES = ("Navigator (cross-phase)", "Context", "Discover + Investigate",
          "Discover + Define", "Create", "Deliver")
GUIDE = "playbook-plays.md"
SKILLS = "playbook-skills.md"
PROMPTS = "playbook-prompts.md"
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


def prompt_group(path):
    """Read the source discriminator without adding a YAML dependency."""
    text = path.read_text()
    if not text.startswith("---\n"):
        raise ValueError(f"Prompt is missing source metadata: {path.name}")
    front = text.split("---", 2)[1]
    source = re.search(r"^source:\n((?:  [^\n]*\n)+)", front, re.M)
    if not source:
        raise ValueError(f"Prompt is missing source metadata: {path.name}")
    fields = source.group(1)
    if re.search(r"^  kind: authored$", fields, re.M):
        match = re.search(r"^  based_on: (skills/ps-[\w-]+/SKILL\.md)$", fields, re.M)
        skill = re.search(r"^skill: (ps-[\w-]+)$", front, re.M)
        if not match or not skill or match.group(1) != f"skills/{skill.group(1)}/SKILL.md":
            raise ValueError(f"Authored prompt must identify its matching Play source: {path.name}")
        if not (ROOT / match.group(1)).is_file():
            raise ValueError(f"Authored prompt refers to a missing Play: {path.name}")
        if re.search(r"^  (?:slide|template_slide|file):", fields, re.M):
            raise ValueError(f"Authored prompt must not claim deck provenance: {path.name}")
        return "Library-authored"
    if not re.search(r"^  kind:", fields, re.M) and re.search(r"^  file: .*\.pptx$", fields, re.M):
        return "Deck"
    raise ValueError(f"Unknown prompt source: {path.name}")


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
        if phase not in PHASES:
            raise ValueError(f"Unknown Blueprint phase: {phase}")
        filename = SKILLS
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


def section_slug(heading):
    """GitHub-style anchors for the generated, punctuation-light lookup headings."""
    return re.sub(r"\s", "-", re.sub(r"[^\w\s-]", "", heading.lower()))


def play_entries(plays):
    """Numbered Plays 03 and 23 share one skill but need separate reader routes."""
    entries = []
    for play in plays:
        entry = dict(play)
        if play["id"] == "ps-outcome-tree":
            entry.update(number="03", title="Outcome Tree, Section One")
        if play["id"] == "ps-process-retrospective":
            tree = next(p for p in plays if p["id"] == "ps-outcome-tree")
            entries.append(dict(tree, number="23", title="Outcome Tree, Section Two", phase="Deliver"))
        entries.append(entry)
    for entry in entries:
        prefix = f'Play {entry["number"]}' if entry["number"] != "Unnumbered" else "Unnumbered"
        entry["heading"] = f'{prefix}: {entry["title"]}'
    return entries


def prompt_skill(path):
    front = path.read_text().split("---", 2)[1]
    match = re.search(r"^skill: (ps-[\w-]+)$", front, re.M)
    if not match:
        raise ValueError(f"Prompt is missing its Play identifier: {path.name}")
    return match.group(1)


def capture_contract():
    """Keep the shared interaction text in the existing Project instructions."""
    text = (HERE / "project-instructions.txt").read_text()
    match = re.search(r"^GUIDED CONTEXT CAPTURE\n(.*?)\n\nPLAY BOUNDARIES$", text, re.S | re.M)
    if not match:
        raise ValueError("Project instructions are missing the guided capture contract")
    return match.group(1).strip()


def build():
    plays = load_plays()
    capture = capture_contract()
    entries = play_entries(plays)
    locations = {}
    inputs = {ROOT / "skills/README.md", ROOT / "LICENSE", HERE / "project-instructions.txt", HERE / "build.py"}
    prompt_files = sorted((ROOT / "prompts").glob("*/*.md"))
    groups = {prompt: prompt_group(prompt) for prompt in prompt_files}
    assigned = set()

    def register(path, filename, section):
        inputs.add(path)
        locations[path.resolve()] = (filename, section)

    for play in plays:
        folder, play_id = play["folder"], play["id"]
        contents = sorted(p.name for p in folder.iterdir())
        if contents != ["SKILL.md"]:
            raise ValueError(f"{play_id} must contain only SKILL.md; found {contents}")
        text = (folder / "SKILL.md").read_text()
        guided = re.search(r"### Guided Mode\n(.*?)\n## Application", text, re.S)
        if not guided or guided.group(1).strip() != capture:
            raise ValueError(f"{play_id} does not match the shared guided capture contract")
        for heading in ["## Template\n", "## Examples\n"]:
            if heading not in text:
                raise ValueError(f"{play_id} is missing its embedded {heading.strip('# ').strip()}")
        register(folder / "SKILL.md", SKILLS, f"{play_id} / Instructions")
    for prompt in prompt_files:
        text = prompt.read_text()
        front = text.split("---", 2)[1]
        body = re.search(r"```text\n(.*?)```", text, re.S)
        original_label = "Original Playbook prompt (unchanged):" if groups[prompt] == "Deck" else "Play coaching prompt:"
        prefix = "Guided context capture (library-added interaction instructions):\n\n" + capture + "\n\n" + original_label + "\n\n"
        if "\ninteraction: guided-context-capture\n" not in front or not body or not body.group(1).startswith(prefix):
            raise ValueError(f"Prompt does not match the shared guided capture contract: {prompt.name}")
        if not body.group(1)[len(prefix):].strip():
            raise ValueError(f"Prompt is missing its underlying Play task: {prompt.name}")
    for entry in entries:
        matches = []
        for prompt in prompt_files:
            front = prompt.read_text().split("---", 2)[1]
            number = re.search(r"^play_number: (\d+)$", front, re.M)
            number = f"{int(number.group(1)):02d}" if number else "Unnumbered"
            if prompt_skill(prompt) == entry["id"] and number == entry["number"]:
                matches.append(prompt)
        if not matches:
            raise ValueError(f'No coaching prompt for {entry["heading"]}')
        entry["prompts"] = sorted(matches)
        for prompt in matches:
            if prompt in assigned:
                raise ValueError(f"Prompt assigned more than once: {prompt.name}")
            assigned.add(prompt)
            register(prompt, PROMPTS, f"{groups[prompt]} / {prompt.parent.name} / {prompt.name}")
    if assigned != set(prompt_files):
        raise ValueError("Some prompts do not match the Play catalog")

    digest = hashlib.sha256()
    for path in sorted(inputs):
        digest.update(str(path.relative_to(ROOT)).encode())
        digest.update(path.read_bytes())
    revision = digest.hexdigest()[:16]
    attribution = f"Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. Full license: {GUIDE}, License appendix."
    snapshot = f"Source snapshot: `{revision}`. {STATUS}"

    def link(filename, heading, label):
        return f"[{label}]({filename}#{section_slug(heading)})"

    def render(path):
        """Adapt navigation and heading depth outside fences; preserve prompt text."""
        output = []
        fence = None
        for line in without_frontmatter(path.read_text()).split("\n"):
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
                if target in ("#template", "#examples", "#application", "#blueprint-reference"):
                    part = {"#template": "Template", "#examples": "Examples"}.get(target, "Instructions")
                    return link(SKILLS, f"{path.parent.name} / {part}", label)
                if target.startswith(("https://", "http://", "mailto:", "#")):
                    return match.group(0)
                local = (path.parent / target.split("#", 1)[0]).resolve()
                if local.is_dir():
                    local = local / ("SKILL.md" if (local / "SKILL.md").exists() else "README.md")
                if local in locations:
                    filename, heading = locations[local]
                    return link(filename, heading, label)
                if local.suffix in (".pdf", ".docx", ".pptx"):
                    return f"{label} (source material, not included in this upload kit)"
                raise ValueError(f"Unmapped reference in {path.relative_to(ROOT)}: {target}")

            line = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", resolve, line)
            if path.name == "SKILL.md" and line in ("## Template", "## Examples"):
                output.append(f"#### {path.parent.name} / {line[3:]}")
                continue
            heading = re.match(r"^(#{1,6}) (.*)", line)
            if heading:
                line = "#" * min(len(heading.group(1)) + 3, 6) + " " + heading.group(2)
            output.append(line)
        return "\n".join(output).rstrip() + "\n"

    guide = ["# Productside Playbook: choose a Play\n",
             "A Play is a guided exercise for a piece of product work. Start with the question or decision in front of you, then choose how you want help. You do the thinking, and AI pressure-tests it.\n",
             "## Two ways to use a Play\n",
             f"| I want to... | Start here | What to do |\n|---|---|---|\n| Get coaching, critique, or rehearsal for a task | {PROMPTS} | Find the Play below, copy its prompt into a chat, and replace the bracketed context. Nothing to install. |\n| Work through the full method and produce its artifact | {SKILLS} | Find the same Play's instructions, embedded template, examples, and quality checks. In a Project, ask the assistant to use that reference. |\n",
             "A prompt is a bounded conversation. A skill is the fuller guide to the Play. You can use either route, switch between them, and bring equivalent prior work without completing earlier Plays.\n",
             "## Choose how to work\n",
             "| Mode | What it means |\n|---|---|\n| Guided | Complete the work and learn the method one step at a time. Get coaching and context-relevant best-guess recommendations when training was missed, forgotten, or interrupted. |\n| Expert | Bring your context, draft, or artifacts and ask for the result. Ask for guidance on any step when needed, then continue without restarting intake. |\n| Discovery | Let the assistant synthesize missing context and quickly sketch the outcomes you seek. Get just enough guidance for a simulated walkthrough, with assumptions visible and listed for validation. |\n",
             "You can switch modes during a conversation. Supplied context is reused. Every mode closes with a summary of what was supplied, synthesized, and still unresolved, then hands the decision back to you. Guided recommendations are options to consider, not answers assumed on your behalf. Discovery does not require a complete brief; simulated outcomes remain distinct from interviews, team agreement, or actual results. The Blueprint navigator helps first rather than forcing an intake form.\n",
             "## Try it\n",
             '> "Help me choose a Play. Our warehouse supervisors stop using our scheduling tool after their first week. Guide me one question at a time."\n',
             '> "Use Play 05 to critique my draft job statements. Find its coaching prompt first; use the skill reference if we need the template or format rules."\n',
             f"## Using the three files\n\nIn a ChatGPT Project, add this guide, {PROMPTS}, and {SKILLS} as sources and use the supplied Project instructions. They are reference documents; no agent skills are installed by uploading them. Start a new chat for each distinct outcome.\n\nOutside a Project, copy a prompt into your AI chat, or attach the individual Play's SKILL.md from the repository. In an agent tool that supports installed skills, use the corresponding skills/ps-.../ folder and that tool's installation instructions. Each folder contains only SKILL.md.\n",
             "## Find a Play\n",
             "Use the number, name, or ps- identifier. Both companion files follow this guide's phase and Play order. Section Two of the Outcome Tree (Play 23) points to the same full skill as Section One (Play 03); its prompt has a separate Deliver entry. Storyboarding and the Blueprint navigator are unnumbered. Play 16 is Product Outcome Canvas. Clarify older numbering by Play name.\n",
             "| Play | Name | Prompts | Full skill |\n|---|---|---|---|"]
    for entry in entries:
        guide.append(f'| {entry["number"]} | {entry["title"]} | {link(PROMPTS, entry["heading"], "Open prompts")} | {link(SKILLS, entry["id"] + " / Instructions", entry["id"])} |')
    skills = ["# Productside Playbook: full skill references\n", snapshot + "\n", attribution + "\n",
              f"Start with {GUIDE} to choose a Play or find its coaching prompts. Each reference below preserves the consolidated SKILL.md instructions, embedded template, and examples. In a ChatGPT Project, mentions of a skill or agent mean applying this uploaded reference, not calling an installed tool.\n",
              "## Contents\n"]
    prompts = ["# Productside Playbook: coaching prompts\n", snapshot + "\n", attribution + "\n",
               f"Start with {GUIDE} to choose a Play. For the full method and working template, use {SKILLS}. Copy the text inside the selected prompt box, add your context, and keep the judgments with you or your team.\n",
               "Playbook-supplied prompts are labeled Deck. Added prompts are labeled Library-authored. Every copyable prompt now includes a library-added Guided / Expert / Discovery capture layer; the original Play task remains unchanged in its labeled section. Deck identifies the underlying prompt's source, not the added interaction instructions. These additions do not change which Plays the source Playbook calls AI-Enabled. Follow each Play's prompt sequence; later steps may require real research or a team session.\n",
               "## Contents\n"]
    for entry in entries:
        prompts.append(f'- {link(PROMPTS, entry["heading"], entry["heading"])}')
        skills.append(f'- {link(SKILLS, entry["id"] + " / Instructions", entry["heading"])}')
    emitted = set()
    for phase in PHASES:
        guide.append(f"\n## {phase}\n")
        skills.append(f"\n## {phase}\n")
        prompts.append(f"\n## {phase}\n")
        for entry in (e for e in entries if e["phase"] == phase):
            reader_description = re.sub(r"\bPM\b", "Product Manager", entry["description"])
            guide.extend([f'### {entry["heading"]}\n', reader_description + "\n"])
            if entry["number"] == "23":
                guide.append("Use this when new discovery or post-launch evidence calls for revisiting the original tree. Read Section Two of the shared skill.\n")
            guide.append("**Prompt route:**\n")
            for prompt in entry["prompts"]:
                filename, heading = locations[prompt.resolve()]
                guide.append(f'- {link(filename, heading, prompt.stem[3:].replace("-", " ").capitalize())} ({groups[prompt]}).')
            guide.append(f'\n**Skill route:** {link(SKILLS, entry["id"] + " / Instructions", entry["id"])}. Read Instructions, Template, and Examples in that reference.\n')
            prompts.append(f'\n### {entry["heading"]}\n\nStable identifier: `{entry["id"]}`.\n')
            for prompt in entry["prompts"]:
                _, heading = locations[prompt.resolve()]
                raw = prompt.read_text()
                metadata = raw.split("---", 2)[1].strip()
                prompts.append(f"\n#### {heading}\n\n**Underlying prompt source: {groups[prompt]}. Interaction layer: library-added guided capture.**\n\nSource metadata:\n\n```yaml\n{metadata}\n```\n\n" + render(prompt))
            if entry["id"] in emitted:
                skills.append(f'\n### {entry["heading"]}\n\nRead Section Two within {link(SKILLS, entry["id"] + " / Instructions", "the shared Outcome Tree reference")}. The full content is stored once under Context.\n')
                continue
            emitted.add(entry["id"])
            path = entry["folder"] / "SKILL.md"
            skills.append(f'\n### {entry["heading"]}\n\nStable identifier: `{entry["id"]}`.\n\n#### {entry["id"]} / Instructions\n\n' + render(path))
    guide.extend(["## Evidence, ownership, and missing references\n",
                  "AI-generated customer details are hypotheses, not research. People conduct real interviews, experiments, and team sessions, and own decisions. Record only evidence you have and distinguish it from assumptions. If the assistant cannot locate a needed source or section, it should name what is missing and ask for it, not invent Productside instructions. Keep unrelated clients or products in separate Projects.\n",
                  "## Source and updates\n", snapshot + "\n",
                  "This kit is generated from deanpeters/ps-playbook-skills. Changes on GitHub do not update uploaded sources. Replace all three together and update Project instructions when changed. Full decks, PDF excerpts, and external maintenance documents are outside this kit; their mentions in skill text are provenance. Test actual reference use and sharing access before wider distribution.\n",
                  attribution + "\n", "## License\n",
                  "The complete license text follows unchanged.\n\n````markdown\n" + (ROOT / "LICENSE").read_text().rstrip() + "\n````\n"])
    return {GUIDE: "\n".join(guide).rstrip() + "\n",
            SKILLS: "\n".join(skills).rstrip() + "\n",
            PROMPTS: "\n".join(prompts).rstrip() + "\n"}


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
