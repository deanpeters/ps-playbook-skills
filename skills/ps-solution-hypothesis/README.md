# ps-solution-hypothesis

Productside Solution Hypothesis Statement skill (Template 12).

## Files

- `SKILL.md` - skill definition, key concepts, application steps, pitfalls
- `template.md` - working scaffold with five sections, two-column If/Then hypothesis, and quality checks
- `prompts/` - copy-paste prompt for chat-based AI tools (authored for this library; the deck has no AI page for this Play)
  - `README.md` - how AI supports this Play, the common trap, how to run the prompt
  - `01-pressure-test-solution-hypothesis.md` - pressure-test your solution hypothesis
- `examples/sample.md` - strong, weak, and drift-bug examples with commentary
- `assets/ps_solution_hypothesis_playbook_pages.pdf` - source pages from the canonical playbook

## Notes

- Skill name uses the `ps-` prefix per project convention.
- This skill belongs to the **Discover + Define** phase.
- The template produces a single artifact with five sections: Problem Statement (imported), Solution Summary, Solution Benefits, Risks and Assumptions, and Solution Hypothesis Statement (two-column If/Then).
- Two hypothesis statements are required, not one: customer-focused (IF solution THEN customer benefit) and business-focused (IF customer benefit THEN business outcome). The THEN of the first becomes the IF of the second.
- Evidence gathering is **artifacts only** - no web research offered. This skill synthesizes the PM's problem framing and solution exploration work.
- Upstream: ps-framing-the-problem, ps-exploring-solution-space, ps-positioning-statement.
- Downstream: lo-fi experimentation, risk assessment, roadmap planning, outcome tree alignment.
