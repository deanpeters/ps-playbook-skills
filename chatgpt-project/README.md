# Set up a Productside Playbook Project in ChatGPT

Choose a Play, then get coaching from a prompt or work through its full skill reference. The kit has three sources with a shared phase-and-Play outline.

| Upload this file | Use it for |
|---|---|
| [playbook-plays.md](uploads/playbook-plays.md) | Start here. Choose a Play and follow its prompt route or skill route. Includes the catalog, source status, and full license. |
| [playbook-prompts.md](uploads/playbook-prompts.md) | Copy a coaching prompt for critique, learning, or rehearsal. Prompts appear by phase, Play, and sequence, with source labels. |
| [playbook-skills.md](uploads/playbook-skills.md) | Read the full Play instructions, embedded template, examples, and quality checks. |

## Set up your Project

1. Create a new Project in ChatGPT named **Productside Playbook**.
2. Add the three Markdown files linked above to its sources.
3. Open [project-instructions.txt](project-instructions.txt) and paste its contents into the Project's instructions field. Uploading it as another source is not a substitute for setting the instructions.
4. Start a new chat in the Project and paste:

   > Help me choose a Play. Our warehouse supervisors stop using our scheduling tool after their first week. Guide me one question at a time.

5. Try both routes for a Play:

   > Find the Play 05 coaching prompt and help me review my draft job statements.

   > Now use the full Play 05 skill reference to explain its template and quality checks.

6. Check the results with the [trial checklist](smoke-checks.md) before sharing.

ChatGPT Projects use uploaded sources and common project instructions across their chats. See [OpenAI's Projects guide](https://learn.chatgpt.com/docs/projects). Check upload limits and sharing controls in your account. Headings and catalog links help locate content; test actual retrieval rather than assuming the assistant has read the whole library.

## How the three files work together

The Play guide serves both audiences. A prompt user can choose a task and open a bounded coaching conversation. A skill user can find the full method and the artifact to produce. Both use the same Play names and stable identifiers.

For example, **Play 05: Jobs-to-Be-Done & Outcomes** links to:

- Its prompts in playbook-prompts.md, in sequence.
- `ps-jobs-to-be-done / Instructions` in playbook-skills.md, with embedded Template and Examples sections.

The guide and prompt collection have separate entries for all 24 numbered Plays, plus the unnumbered Blueprint navigator and Storyboarding. The skill collection stores the full Outcome Tree reference once, under Context; Play 23 under Deliver points back to its Section Two. Play 16 is Product Outcome Canvas in this edition.

In a ChatGPT Project these are uploaded references. No skills are installed by uploading them. Outside a Project, copy a prompt into a chat or attach an individual Play's SKILL.md. For an agent tool that supports skill installation, use its instructions and the corresponding repository skill folder.

Prompt labels distinguish **Deck**, supplied by the Playbook, from **Library-authored**, added for this library. The additions do not change the Playbook's AI-Enabled designations. Source material follows the November 2026 B2B work-in-progress Playbook, which is not yet ratified.

## Share or update

For a team working on one product, use the Project's available sharing controls and verify access with another account. For independent learners or unrelated clients, distribute this setup guide, project-instructions.txt, and the three source files so each person can create a separate Project. Review the audience and accessible content before sharing. Follow the license included in playbook-plays.md.

If you used the earlier nine-file kit, remove those nine sources from ChatGPT before adding this set. Replace the Project instructions as well, then start a new chat. For future updates, replace all three files together; their source fingerprints should match. Changes on GitHub do not update uploaded snapshots.

## Rebuild the files

For maintainers: Python 3 is required, with no additional packages or API keys. These commands write or check local files; they do not upload, publish, or run model sessions.

From the repository root:

```bash
python3 chatgpt-project/build.py
```

Check that the files match their sources:

```bash
python3 chatgpt-project/build.py --check
```

Run the packaging checks:

```bash
python3 -m unittest discover -s chatgpt-project -p 'test_*.py'
```

Edit skills, prompts, or project instructions, then rebuild. Do not edit uploads/ by hand. New Plays require updating skills/README.md and the title mapping in build.py. The generator rejects missing or unmapped references, prompts without catalog entries, and unexpected upload files.

Packaging checks verify content, ordering, and references. They do not establish live ChatGPT behavior, sharing access, or Productside approval.
