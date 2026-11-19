# Set up a Productside Playbook Project in ChatGPT

Give ChatGPT a library of Productside Playbook Plays it can find and apply from uploaded references. No skill installation is needed.

## Set up your Project

1. Create a new Project in ChatGPT named **Productside Playbook**.
2. Add all nine files from [uploads/](uploads/) to the Project's sources. Upload the individual Markdown files. You do not need to upload the repository, script, skill folders, or PDF excerpts.
3. Open [project-instructions.txt](project-instructions.txt). Copy its contents into the Project's instructions field. Uploading this file as a source is not a substitute for setting the instructions.
4. Start a new chat inside the Project and paste:

   > Help me choose a Play. Our warehouse supervisors abandon our scheduling tool after their first week. Guide me one question at a time.

5. Check that ChatGPT names an appropriate Play, finds its uploaded reference, and asks one focused question. Use the [trial checklist](smoke-checks.md) before sharing.

ChatGPT Projects use shared files and project instructions across their chats. See [OpenAI's Projects guide](https://learn.chatgpt.com/docs/projects). Exact upload limits, sharing controls, and available audiences need to be checked in your account. If nine files do not fit, use a Project for one phase with start-here, the navigator, that phase's reference, prompts, and the license. The catalog will still list the whole library; tell ChatGPT which phase you uploaded. It must ask for any missing reference when needed.

## What to upload

| File | What ChatGPT can find in it |
|---|---|
| [00-start-here.md](uploads/00-start-here.md) | Getting started, source status, and snapshot fingerprint |
| [01-playbook-navigator.md](uploads/01-playbook-navigator.md) | Play names, numbers, identifiers, reference locations, and Blueprint guidance |
| [02-context.md](uploads/02-context.md) | Context Plays, including both Outcome Tree sections |
| [03-discover-investigate.md](uploads/03-discover-investigate.md) | Customer discovery, research synthesis, and problem framing |
| [04-discover-define.md](uploads/04-discover-define.md) | Solution definition, experiments, Storyboarding, risks, and Product Outcome Canvas |
| [05-create.md](uploads/05-create.md) | Roadmaps, ongoing discovery, prioritization, launch, and readiness |
| [06-deliver.md](uploads/06-deliver.md) | Measurement and retrospectives |
| [07-prompts.md](uploads/07-prompts.md) | Standalone deck prompts, with their source labels |
| [08-license.md](uploads/08-license.md) | Productside attribution and unchanged license |

## How ChatGPT finds a Play

The navigator's catalog is the lookup table. For example:

> Play 05 / Jobs-to-Be-Done & Outcomes / ps-jobs-to-be-done
>
> Reference: 03-discover-investigate.md
>
> Sections: ps-jobs-to-be-done / Instructions, Template, and Examples

Each Play's single SKILL.md contains its instructions, template, and compact examples. The generator gives those parts named sections in the upload files. Cross-Play links are rewritten to an uploaded filename and section. ChatGPT is instructed to read those sections before applying the Play. This guides reference use; uploading files does not guarantee the model will retrieve or follow every relevant passage. Check actual behavior with the trial requests.

The preserved source sometimes says "skill" or "agent." Project instructions explain that these mean applying the Play from the reference library. A `ps-` identifier is a lookup label, not an installed tool or a command.

Numbering follows the November 2026 B2B work-in-progress Playbook, which is not yet ratified. Plays 03 and 23 share the Outcome Tree reference. Storyboarding and the Blueprint navigator are unnumbered. Play 16 is Product Outcome Canvas.

## Share it

For a product team working together, use the sharing controls available in the Project and verify access with another account. Review the audience and what members can access before inviting people.

For students or unrelated clients, distribute this setup guide, project-instructions.txt, and the nine upload files so each person can create a separate Project. Each Project should hold its own product context. The private GitHub repository requires access; you can distribute the downloaded kit through your normal approved channel instead.

Follow the [Productside license](../LICENSE) when distributing the kit. Do not put private customer material in the reusable library.

## Update the upload kit

For maintainers: Python 3 is required. No additional packages or API keys are needed. These commands write generated files locally; they do not upload to ChatGPT, publish, or spend model usage.

From the repository root, rebuild after changing skills, templates, examples, prompts, the skill catalog, or project instructions:

```bash
python3 chatgpt-project/build.py
```

Check that generated files match their sources:

```bash
python3 chatgpt-project/build.py --check
```

Run the packaging checks:

```bash
python3 -m unittest discover -s chatgpt-project -p 'test_*.py'
```

Edit the source files, then regenerate. Do not edit uploads/ by hand. New Plays require updating the existing skill catalog and the title mapping in build.py. The generator refuses missing or unmapped references and unexpected upload files rather than silently dropping them.

To update ChatGPT, replace the old nine sources with the new set, replace the Project instructions if changed, and start a new chat. Changing GitHub does not update an uploaded snapshot. Repeat the trial checklist after replacing it.

Packaging checks verify content and references. They do not establish live ChatGPT behavior, sharing access, or Productside source approval. Source PDFs and external maintenance documents remain outside the kit; their references are labeled as provenance.
