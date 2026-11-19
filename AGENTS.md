# Working on this library

Read README.md and LICENSE first. Keep this project focused on skills and prompts.

- Preserve Productside frameworks, distinctions, templates, examples, guided mode, and human decision ownership.
- Keep the `ps-` skill names. One folder serves one coherent job.
- Each `skills/ps-.../` folder contains only `SKILL.md`. Keep the working template, essential usage notes, compact examples, and quality checks inside that file. Standalone prompts belong in the top-level `prompts/` collection; supporting source material stays in the original project.
- Keep Playbook prompt text verbatim. Label authored prompts and inferred details honestly.
- Use Guided, Expert (context dump), and Discovery (spitball) as the three interaction modes. Keep the compact capture contract in `chatgpt-project/project-instructions.txt` aligned with all skill Guided Mode blocks and prompt wrappers. A wrapper is library-authored; preserve the underlying Playbook prompt verbatim in its labeled section. Discovery never supplies invented evidence or team decisions.
- Guided teaches while completing the work with context-relevant best-guess recommendations. Expert acts on supplied context and offers guidance on any step without restarting intake. Discovery synthesizes missing context and quickly sketches or simulates a walkthrough with just enough guidance; keep synthesized assumptions and simulated outcomes distinct from real evidence.
- Do not invent customer evidence, quotes, or numbers.
- Keep reader instructions short, concrete, and accessible to Product Managers who do not code.
- Do not include secrets, local configuration, private client material, or full source decks.
- Do not use em dashes or double hyphens as dashes.
- Preserve the Productside license and attribution.
- Before committing, check local Markdown links, frontmatter, and prompt sequence links. Changes to skill behavior also need relevant behavioral validation in the source project.
- After changing library content, run `python3 chatgpt-project/build.py` and `python3 chatgpt-project/build.py --check`. The ChatGPT kit uses uploaded Play references, not installed skills. Preserve its catalog destinations and prompt text. See [setup and packaging checks](chatgpt-project/README.md).
- The Project upload set has three files: `playbook-plays.md` is the guide for both prompt and skill users; `playbook-prompts.md` contains the coaching prompts; `playbook-skills.md` contains full Play references. Keep their phase and Play ordering aligned.
- Do not commit or publish unless the user asks.

Maintenance standards and source tracking live in the [original project](https://github.com/Productside/Productside-Playbook-Skills). This copy intentionally omits its build system, eval suite, bundles, and planning documents.
