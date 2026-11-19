# ps-market-selection-sizing

Productside Market Selection & Sizing skill (Template 04 in the B2B work-in-progress deck). New in that deck; the baseline deck has no equivalent Play.

## Files

- `SKILL.md` - skill definition, key concepts, application steps, pitfalls
- `template.md` - market analysis scaffold: market and PESTEL, two segments with their people, TAM / SAM / SOM, source register, open questions
- `prompts/` - copy-paste prompts for chat-based AI tools with web search, run in order in one chat
  - `README.md` - how AI supports this Play, traps, how to run the prompts, source notes
  - `01-pressure-test-market.md` - name the market at the right altitude
  - `02-build-pestel.md` - the six forces as evidence or open questions
  - `03-segment-market.md` - segments by needs, goals, and behaviors, with real buyers and users
  - `04-first-pass-sizing.md` - triangulate a first-pass size; SOM only with a product
- `examples/sample.md` - strong, weak, and drift-bug ("the free five percent") examples; all figures illustrative
- `assets/ps_market_selection_sizing_playbook_pages.pdf` - slides 14-18 of the B2B work-in-progress deck

## Notes

- Skill name uses the `ps-` prefix per project convention.
- **Type:** component. **Phase:** Context. **Evidence:** web research + user artifacts.
- **Every number needs a source.** Sizing is written as formulas whose inputs carry source IDs or `[TO SOURCE]`, in one counting unit, as ranges, with SOM ≤ SAM ≤ TAM.
- **AI may propose, never invent.** Following the Playbook's own prompts, the skill proposes market definitions, PESTEL entries, and segments with its reasoning visible, and cites what it finds. It never fills a sizing blank with a plausible number.
- **SOM can wait:** it is estimated only when there is a product to price. Otherwise it is deferred until solutions are ideated.
- **Downstream:** ps-jobs-to-be-done, ps-proto-persona, ps-empathy-interviews, and ps-positioning-statement use the segments and the people named in them.
- The source deck is not yet ratified, and its pages are not objectified (no named shapes). The budget entry in `technical/data/canonical_template_budgets.yaml` has guidance only, no shape budgets.
