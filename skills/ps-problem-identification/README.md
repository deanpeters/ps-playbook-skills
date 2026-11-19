# ps-problem-identification

Exemplar Productside Playbook skill based on the **Problem Identification** play (Template 08 in the baseline deck, Template 09 in the B2B work-in-progress deck).

## Files

- `SKILL.md` - the skill instructions
- `template.md` - compact, paste-ready scaffold
- `prompts/` - copy-paste prompt for chat-based AI tools
  - `README.md` - how AI supports this Play, traps, how to run the prompt, source notes
  - `01-shape-problem-statements.md` - separate pains from root causes and format problem statements
- `examples/sample.md` - stronger and weaker examples, including the missing-feature drift bug
- `assets/ps_problem_identification_playbook_pages.pdf` - the three source pages from the canonical playbook PDF

## Notes

- This exemplar follows the `ps-` naming contract
- It is intentionally budget-aware and template-capacity-aware
- Most default outputs should stay sticky-note-sized or small-cell-sized
- **Coach by default:** the skill asks the PM for the root cause beneath each pain rather than naming it, and catches features posing as problems
- **Evidence honesty:** quotes come only from supplied research (unfilled slots are marked `[needs a real quote]`), and unvalidated causes are marked `[CAUSE TO VALIDATE]`
