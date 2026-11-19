# Output Prioritization Template

Use this scaffold to produce a paste-ready four-quadrant output prioritization artifact in Productside format.

Complete all four sections in order. Do not skip the center point step - it is required for valid quadrant placements.

---

## Section 1: Identify Outputs

List all candidate outputs (features, capabilities) that could be developed as part of the solution. This is a brainstorm - do not filter or rank yet. Include everything the team has proposed.

**Product or initiative:** [name of the product or feature set being prioritized]
**Customer role:** [who the product is built for - the person who uses or buys it]
**Session participants:** [names and roles of everyone involved in this classification]
**Date:** [date of session]

**Candidate outputs:**

- [Output 1: short name, 3-8 words]
- [Output 2: short name, 3-8 words]
- [Output 3: short name, 3-8 words]
- [Output 4: short name, 3-8 words]
- [Output 5: short name, 3-8 words]
- [Output 6: short name, 3-8 words]
- [Add additional outputs as needed]

> **Quality check:** Does every item name a specific, buildable feature or capability? Remove anything that is an outcome ("faster resolution times"), a goal ("improve user satisfaction"), or a vague category ("better reporting"). Each item should be concrete enough that an engineer could scope it.

---

## Section 2: Center Point Output

The team must agree on one output that is medium cost and medium value - the anchor for all other placements. All other outputs will be classified relative to this center point.

**Center point output:** [name the output]

**Why this is medium/medium:** [1-2 sentences explaining why the team agreed this output represents neither extreme on value or cost - not the most impactful for the customer, not the most expensive to build]

> **Quality check:** Did the whole team agree on this anchor, or did the PM choose it alone? The center point requires team agreement. If only one person chose it, revisit before proceeding.

---

## Section 3: Four Quadrant Classification

Classify each candidate output (except the center point) by Value and Cost relative to the center point. Then assign each to a quadrant.

**Quadrant layout reference:**
- Quadrant I: High Value, Low Cost (upper right) - start here
- Quadrant II: High Value, High Cost (upper left) - plan carefully
- Quadrant III: Low Value, Low Cost (lower right) - deprioritize
- Quadrant IV: Low Value, High Cost (lower left) - avoid or cut

| Output | Value (H/M/L) | Value Rationale | Cost (H/M/L) | Cost Rationale | Quadrant | Priority |
|--------|--------------|-----------------|-------------|----------------|----------|----------|
| [Center point output] | M | Anchor - all other outputs are relative to this | M | Anchor - all other outputs are relative to this | Center | Reference |
| [Output 2] | [H/M/L] | [1-2 sentence customer-outcome rationale] | [H/M/L] | [1-2 sentence technical/engineering rationale] | [I/II/III/IV] | [Start / Plan / Deprioritize / Cut] |
| [Output 3] | [H/M/L] | [1-2 sentence customer-outcome rationale] | [H/M/L] | [1-2 sentence technical/engineering rationale] | [I/II/III/IV] | [Start / Plan / Deprioritize / Cut] |
| [Output 4] | [H/M/L] | [1-2 sentence customer-outcome rationale] | [H/M/L] | [1-2 sentence technical/engineering rationale] | [I/II/III/IV] | [Start / Plan / Deprioritize / Cut] |
| [Output 5] | [H/M/L] | [1-2 sentence customer-outcome rationale] | [H/M/L] | [1-2 sentence technical/engineering rationale] | [I/II/III/IV] | [Start / Plan / Deprioritize / Cut] |
| [Output 6] | [H/M/L] | [1-2 sentence customer-outcome rationale] | [H/M/L] | [1-2 sentence technical/engineering rationale] | [I/II/III/IV] | [Start / Plan / Deprioritize / Cut] |

> **Quality check:** Review the Value column. Does every rationale name a customer benefit or a product outcome - not a business benefit, not an internal metric? If any rationale says "this will drive upsell" or "this will help sales," it is measuring business value, not customer value. Rewrite before finalizing. Review the Cost column. Did engineering or a project manager provide input on cost estimates, or is this PM intuition? Flag any row where cost was estimated without a technical voice.

---

## Section 4: Quadrant Summary and Action Guidance

Organize outputs by quadrant and document the action for each.

**Quadrant I - Start Here (Low Cost, High Value)**

| Output | Product Outcome Supported |
|--------|--------------------------|
| [Output name] | [Name the product outcome this output drives - what does the customer achieve?] |
| [Output name] | [Name the product outcome this output drives] |

Action: Prioritize these outputs for the first development cycle. Carry them into the Outcome-Based Roadmap as "Outputs to Develop."

**Quadrant II - Plan Carefully (High Cost, High Value)**

| Output | Key Assumption to Validate | Recommendation |
|--------|---------------------------|----------------|
| [Output name] | [What assumption about value or cost needs to be validated before committing?] | [Lo-fi experiment / further technical sizing / staged delivery] |

Action: Do not commit these to the build plan until the key assumption is validated. Place them in "Output Concepts to Validate" in the roadmap. Consider ps-lofi-experimentation for the highest-uncertainty items.

**Quadrant III - Deprioritize (Low Cost, Low Value)**

- [Output name] - Deferred. Easy to build but does not drive meaningful customer progress at this stage.
- [Output name] - Deferred. Revisit if a product outcome changes or new discovery reveals higher value.

Action: Remove from the current cycle. Do not build these because they are cheap - build them only if customer evidence improves the value case.

**Quadrant IV - Avoid or Cut (High Cost, Low Value)**

- [Output name] - Cut. Poor return on investment. [Note any stakeholder tradeoff that needs to be surfaced explicitly.]
- [Output name] - Cut. [Note any dependencies or cleanup required.]

Action: Do not schedule. If stakeholders press to keep these, document the specific Quadrant I or II investment that would be displaced and ask for an explicit decision.

> **Quality check:** Is every output placed in exactly one quadrant? Is at least one output in Quadrant IV actually cut, not just deferred? If the entire list landed in Quadrant I and II, the classification has not done its job - revisit the center point and recheck the value rationales.

---

**Next Steps**

1. Feed Quadrant I outputs into the Outcome-Based Roadmap (Template 17) as "Outputs to Develop"
2. Move Quadrant II outputs to "Output Concepts to Validate" and plan validation for the highest-uncertainty items
3. Share the full classification with stakeholders to surface any Quadrant IV political items and document the tradeoff decisions
