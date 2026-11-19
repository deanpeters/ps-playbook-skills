# ps-outcome-tree

Productside Outcome Tree skill (Templates 03 and 23). Two modalities in one skill.

## Files

- `SKILL.md` - skill definition, key concepts, application steps for both modalities, pitfalls
- `template.md` - working scaffolds for Section One (pre-discovery) and Section Two (post-discovery update)
- `prompts/` - copy-paste prompts for chat-based AI tools (authored for this library; the deck has no AI page for this Play)
  - `README.md` - how AI supports this Play, the common trap, how to run the prompts
  - `01-check-section-one.md` - check your outcome tree, section one
  - `02-review-section-two.md` - review your outcome tree against evidence, section two
- `examples/sample.md` - strong, weak, and drift-bug examples with commentary
- `assets/ps_outcome_tree_playbook_pages.pdf` - source pages from the canonical playbook

## Notes

- Skill name uses the `ps-` prefix per project convention.
- **Two modalities:** Section One (Template 03, Context phase) establishes the strategic context before discovery. Section Two (Template 23, Define/Deliver phase) updates the tree after discovery with validated outcomes, revised metrics, and actuals vs. planned.
- The template produces a structured artifact with five sections: Business Outcome, Business Success Metrics, Product Outcomes (2-5), Product Success Metrics, and Product Health Metrics.
- Product outcomes use role names, not persona names.
- The play cross-references two other plays: Framing the Problem (Problem Statement box) and Solution Hypothesis Statement (Solution Summary box). Neither is a blocking dependency.
- Upstream: ps-jobs-to-be-done product outcomes feed into this tree. Section Two updates the tree after discovery work.
