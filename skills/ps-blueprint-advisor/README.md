# ps-blueprint-advisor

Productside Blueprint navigator. Places a team on the Blueprint, coaches a phase, or audits a decision against the five Optimal Product Process Principles, then points to the play to run next.

## Files

- `SKILL.md` - skill definition, key concepts, application steps, pitfalls
- `template.md` - audit output scaffold for pressure-testing a decision against the five principles
- `examples/sample.md` - strong, weak, and drift-bug examples in one operational domain
- `reference/blueprint-stages.md` - the phase and principle knowledge base the skill reads from
- `assets/ps_blueprint_advisor_playbook_pages.pdf` - source pages 1-3 of the canonical playbook (Blueprint overview and phase map)

## Notes

- Skill name uses the `ps-` prefix per project convention.
- This is a **cross-phase navigator**, not a single canonical play. It sits above the play library and routes into it.
- Three modes: Navigate (place the team and point to the next play), Coach (go deep on one phase), Audit (test a decision against the five principles).
- Principle model: the five Optimal Product Process Principles are canonical; phase-level principles inherit and ladder up to them. Three orphan themes (Guardrails, Cross-Functional Ownership, Transparency) are surfaced as open decisions, never asserted as canon.
- Evidence gathering is **user artifacts only** - no web research offered. It works from the user's own account of their situation.
- Loose coupling: play names are pointers, never dependencies. If a play is not installed, the skill gives its gist and offers to do the work inline.

## Known deviations from the standard play anatomy

This skill is a navigator, so it diverges from the norm in two places, on purpose:

1. `blueprint_stage` is `All` rather than one of the five enum values, because it spans every phase.
2. Step 1 leads with help, with the tech-role bias guard kept as a silent self-check rather than an opening interrogation.

Its source pages are the front of the canonical playbook (pages 1-3: Blueprint overview and phase map), distilled into `reference/blueprint-stages.md`.
