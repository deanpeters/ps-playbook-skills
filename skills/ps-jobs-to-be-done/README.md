# ps-jobs-to-be-done

Productside Jobs-to-Be-Done & Outcomes skill (Template 04 in the baseline deck, Template 05 in the B2B work-in-progress deck). Two steps in one skill.

## Files

- `SKILL.md` - skill definition, key concepts, application steps for both steps, pitfalls
- `template.md` - working scaffold with two-table structure and quality checks
- `prompts/` - copy-paste prompts for chat-based AI tools, used in order
  - `README.md` - how AI supports this Play, traps, how to run the prompts, source notes
  - `01-check-job-statements.md` - pressure-test drafted job statements
  - `02-check-product-outcomes.md` - pressure-test drafted product outcomes
- `examples/sample.md` - strong, weak, and drift-bug examples with commentary
- `assets/ps_jobs_to_be_done_playbook_pages.pdf` - source pages from the canonical playbook

## Notes

- Skill name uses the `ps-` prefix per project convention.
- **Two steps:** Step One (job statements + personas) can be done pre-discovery. Step Two (product outcomes) is strongest after empathy interviews provide evidence. Both steps can be completed in one session if evidence exists.
- **Review path:** if the PM brings a draft, the skill pressure-tests it first (verdict per job and outcome) before offering rewrites. This matches the Playbook's AI prompts.
- This skill belongs to the **Discover + Investigate** phase and pairs directly with ps-proto-persona. The playbook says to consider JTBD and Persona at the same time.
- The template produces two artifacts: a Job Statement + Persona table and a Product Outcome & Context table.
- Job statements use three Productside formats: Functional, Emotional, Social.
- Product outcomes use the Direction + Metric + Context format. "Optimize," "enhance," and "improve" are never a direction.
- Upstream (B2B work-in-progress deck): Market Selection & Sizing defines the segment these jobs belong to.
- Downstream: ps-problem-identification uses jobs and outcomes from this skill as input. Product outcomes feed into ps-outcome-tree.
