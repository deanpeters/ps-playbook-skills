# ps-empathy-interviews

Productside Empathy Interviews skill (Template 06 in the baseline deck, Template 07 in the B2B work-in-progress deck).

## Files

- `SKILL.md` - skill definition, key concepts, application steps, pitfalls
- `template.md` - three-phase scaffold: preparation, conduct guidance, findings documentation
- `prompts/` - copy-paste prompts for chat-based AI tools, used in order
  - `README.md` - how AI supports this Play, traps, how to run the prompts, source notes
  - `01-prepare-interview-guide.md` - topic areas and example questions; the PM writes their own
  - `02-rehearse-technique.md` - practice drill against tough interview moments (voice mode recommended)
- `examples/sample.md` - strong, weak, and bias-bug examples with commentary
- `assets/ps_empathy_interviews_playbook_pages.pdf` - source pages from the canonical playbook

## Notes

- Skill name uses the `ps-` prefix per project convention.
- This skill belongs to the **Discover + Investigate** phase.
- This is a **process skill** (`type: process`), not a component skill. It spans preparation, interview conduct, and findings documentation across multiple sessions.
- The agent helps with preparation (Phase 1) and documentation (Phase 3). The PM conducts the actual interview (Phase 2) in the field - the agent cannot substitute for real customer conversation.
- **Preparation follows the Playbook's AI pages:** name the decision, set learning objectives, choose 4-5 topic areas, and review the PM's own questions (leading, closed, solution-fishing, no objective). The agent drafts questions only on request, labeled as a starting draft.
- **Rehearsal (optional):** the agent can play the persona in a technique drill, one tough moment at a time, then review the PM's technique. It is practice, never research. Nothing from a rehearsal goes into findings.
- Evidence gathering: this skill qualifies for **web research + user artifacts**. Web research grounds the PM in the interviewee's domain before the interview. User artifacts (persona work, JTBD output, prior research) inform question preparation.
- The findings board produces structured output that feeds downstream skills: Jobs-to-Be-Done, Desired Outcomes, Problems, and Feels/Appears.
- Upstream: ps-proto-persona (persona grounds the interview target), ps-jobs-to-be-done (provides assumptions to test).
- Downstream: ps-problem-identification (uses problems and jobs from findings), ps-proto-persona (refine with real quotes and observations).
