---
name: psk-output-prioritization
description: >-
  Prepare to facilitate, then record, a team ranking of product outputs
  (features, capabilities) by relative customer value and business cost on a
  four-quadrant grid anchored on a center-point output. Use when a team needs to sequence
  what to build first and communicate tradeoffs transparently before committing
  to a roadmap, or when asked to place features in quadrants or name a top N.
intent: >-
  Help a Product Manager and their team evaluate candidate product outputs
  against two dimensions - customer value and business cost - so that the team
  prioritizes what to build first based on evidence, not advocacy. The skill
  produces a paste-ready four-quadrant classification that feeds directly into
  the Outcome-Based Roadmap.
type: component
blueprint_stage: Create
best_for:
  - "Ranking features and capabilities against customer value and business cost"
  - "Placing candidate outputs into a four-quadrant prioritization grid with your team"
  - "Making transparent tradeoff decisions about what to build first"
scenarios:
  - "We have a backlog of feature ideas and need to prioritize based on customer value and cost"
  - "Help me run a prioritization session with the team using a four-quadrant grid"
---


## Purpose

Create a **Productside-style Output Prioritization artifact** from a collaborative team review of candidate product outputs.

This skill helps a Product Manager and their cross-functional team evaluate which features and capabilities to build first, based on relative customer value and relative business cost. The result is a four-quadrant placement for every candidate output, a clear ordering for development sequencing, and a transparent record of the tradeoffs the team made.

The point is not to build everything eventually. The point is to help the team make a defensible, customer-grounded decision about what to address first, what to plan carefully, what to deprioritize, and what to cut.

The skill works in two moments. **Before the session**, it prepares the PM to facilitate: the center-point anchor, the moves that keep value and cost honest, and rehearsal for the hard personalities. **After the session**, it records the room's placements in the four-quadrant artifact and checks them. It does not rank the outputs itself.

This is a team exercise. It is not a solo PM exercise. Customer value requires discovery data or validated insight. Business cost requires input from engineering, a project manager, or a technical lead. A solo prioritization session produces outputs ranked by the PM's assumptions, not by evidence.

### Usage Notes

- This skill is a component (content-fill) skill producing a paste-ready four-quadrant artifact.
- **Two moments:** before the session, it prepares the PM to facilitate (center-point anchor, moves against inflation, rehearsal of hard personalities). After the session, it records the room's placements and checks them. It does not rank the outputs itself.
- Center point anchoring is required before any other classification. Skipping it produces inflation.
- Value is always customer value. Business metrics on the value axis are the primary drift bug.
- Cost classification requires engineering or project manager input. PM-only cost estimates are not sufficient.
- Downstream: Quadrant I outputs feed the Outcome-Based Roadmap (Template 17) as "Outputs to Develop."

## Key Concepts

### Outputs Are Not Outcomes

This distinction is load-bearing. An **output** is a feature, capability, or deliverable the team can build: a real-time alert dashboard, an offline sync mode, a bulk import tool. An **outcome** is what a customer achieves when the product works: field technicians catch scheduling conflicts before they become incidents, operations managers spend less time on manual reconciliation.

Confusing outputs for outcomes is the most common failure mode in prioritization. An output that cannot be connected to a customer outcome has no defensible basis for prioritization. If the team cannot name the outcome an output supports, that output should be challenged before it is placed on the grid.

### The Two Axes

**Value (Y-axis): Customer value.**
How much does this output drive progress toward a product outcome? Does it relieve a significant pain or create a meaningful gain for the customer? Value is defined entirely from the customer's perspective. Business benefits such as upsell opportunity, marketing positioning, or internal cost reduction are not customer value. They may be relevant business considerations, but they cannot substitute for the customer's perspective on the Y-axis.

**Cost (X-axis): Business cost and risk.**
How much does this output cost the business to develop? Cost includes development effort, integration complexity, infrastructure requirements, dependency management, and delivery risk. Engineering and project management input is required for a credible cost estimate. PM intuition is not sufficient.

### Why Center-Point Anchoring Works

The most common problem in output prioritization is inflation: every feature is called "high value" by someone on the team. The center-point anchor breaks this dynamic.

The team agrees on one output that is genuinely medium cost and medium value - neither the most expensive nor the most impactful candidate on the list. That output anchors the center of the grid. All other outputs are plotted relative to this anchor, not on an absolute scale.

This prevents the "everything is critical" failure mode. It forces relative comparison: is this output more or less valuable than the anchor? More or less costly? Relative comparison is harder to inflate than absolute scoring.

### Prioritization Is a Conversation About Trade-offs

Prioritization is a conversation about trade-offs, not a calculation. The plotting belongs to the room: real cost comes from the tech team, real value from customer evidence, and the call on what to build first from the PM and their stakeholders together. A ranked list handed down from a tool has no cost data behind it and no buy-in.

The room will want to crowd everything into high-value, low-cost. Moves that break that up:

- **Force comparisons against the anchor.** "More or less valuable than the center point? More or less costly?"
- **Ask for the outcome and the evidence behind every value claim.** Value means customer value tied to a product outcome, not internal excitement.
- **Make tech scope cost out loud.** Cost means the real build cost, not a wave of the hand.

Rehearse the hard moments before the session: the stakeholder who inflates their pet feature, the "everything is a priority" reflex, and cost getting waved away.

### The Four Quadrants

The canonical labels the quadrants I through IV. The layout differs from standard mathematical quadrant notation:

- **Quadrant I (Low Cost, High Value - upper right):** Start here. Maximum return for minimum investment. These outputs should be at the top of the development sequence.
- **Quadrant II (High Cost, High Value - upper left):** Plan carefully. High return but high investment required. Validate the value assumptions before committing. Uncertainty in cost estimates warrants lo-fi experimentation before full build.
- **Quadrant III (Low Cost, Low Value - lower right):** Deprioritize. These outputs are cheap to build but do not move the needle for customers. "Easy" is not a reason to build.
- **Quadrant IV (High Cost, Low Value - lower left):** Avoid or cut. Poor return on investment. These outputs must be cut or deferred. Stakeholder pressure to keep Quadrant IV items is one of the most common prioritization failures.

### Cross-Functional Input Is Required

Customer value: requires data from discovery work, empathy interviews, or validated product outcomes. The Outcome Tree (psk-outcome-tree) is the best source for linking outputs to product outcomes.

Business cost: requires input from engineering, a project manager, or a technical lead. Do not estimate cost without a technical voice in the room.

### How to Connect Outputs to Outcomes

The Outcome Tree shows what customers need to achieve (product outcomes) as a result of the problem the product solves. Each output the team evaluates should be traceable to at least one product outcome. If an output cannot be connected to a product outcome, it is either solving an internal business problem (not a customer problem) or the outcome tree is incomplete.

Quadrant I outputs should be linked to the highest-priority product outcomes before they are committed to the roadmap.

### Relationship to Tiny Acts of Discovery

Tiny Acts of Discovery is a technique for generating solution ideas before outputs are evaluated. Output Prioritization assumes that the brainstorm phase is complete: the team has already identified all candidate outputs (using Story Mapping, Tiny Acts, or equivalent). The prioritization exercise evaluates that list - it does not generate it.

If the list of candidate outputs is still thin or unclear, run Tiny Acts of Discovery before beginning this exercise.

### How AI Supports This Play

The Playbook casts AI as a **facilitation coach**. It rehearses the session with the PM: how to set up the room, how to anchor every output against a single center-point output so the ranking stays relative, and how to keep the group honest when every idea drifts into high-value, low-cost territory. What the PM gets is a sharper facilitator, not a ranked list.

- **Use it when:** the PM has a list of outputs and needs to run a session where stakeholders prioritize them by relative value and cost.
- **Avoid it when:** the request is for AI to score and rank the features. It has no real cost data and cannot create team buy-in. Offer to prepare the session instead.
- **Return:** a session plan anchored on a center-point output, moves to keep value and cost honest, and rehearsal for the stakeholder who inflates everything. After the session: the room's placements, recorded and checked.

### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

## Application

Use [Template](#template) for the scaffold.


### Required Output Convention

Default to a **clean, paste-ready artifact**.

That means:

- a named list of all candidate outputs (brainstorm phase)
- one clearly named center point output with team rationale
- a classification table with Value (H/M/L), Cost (H/M/L), and Quadrant for every output
- a Quadrant Summary listing outputs by quadrant with action guidance
- Quadrant I outputs linked to product outcomes
- explanation belongs below the artifact, not inside the classification fields

### Step 1: Confirm Who the Customer Is

Before evaluating any output for value, confirm who the customer is - the person who uses or buys the product, not the PM, not the engineering team, and not an internal stakeholder.

This is the tech-role bias guard. LLMs and product teams both default to developer, architect, or internal-operations perspectives when evaluating value. If the product serves field technicians, operations managers, clinical coordinators, or other non-technical roles, the value dimension must be assessed from that person's standpoint.

Ask the user to name the customer role. If a proto-persona exists (from psk-proto-persona), use it. If an Outcome Tree exists (from psk-outcome-tree), confirm the product outcomes before evaluating outputs against value.

### Step 2: Gather Available Artifacts

Before drafting, ask whether the user has materials to share:

- Solution hypothesis from psk-solution-hypothesis (defines the solution being decomposed into outputs)
- Product outcomes from psk-outcome-tree (used to evaluate value from the customer's perspective)
- Discovery findings from psk-empathy-interviews or psk-problem-identification (used to calibrate which customer pains are most severe)
- Any Story Mapping or Tiny Acts of Discovery results (used to populate the candidate output list)
- Engineering capacity or sprint planning data (used to calibrate cost)

The more context available, the more targeted the classification. If no artifacts are available, note that the output is based on PM assumptions and should be reviewed with the team before committing.

### Step 3: Identify All Candidate Outputs

Work with the user to list all outputs that could be developed as part of the solution. This is a brainstorm - do not filter or evaluate yet.

For each output, capture:

- A short name (3-8 words) that identifies the feature or capability specifically
- Not a vague category like "reporting" or "integrations" - name the specific thing: "real-time alert dashboard" or "ERP connector for SAP"

Aim for completeness. A prioritization exercise with only three candidates is not a prioritization exercise - it is a list. A good brainstorm produces six to twelve candidates before the evaluation begins.

### Step 4: Prepare to Facilitate the Session (Default)

Unless the PM is returning with the room's placements, prepare them to lead the session (mirrors the critique guidance in this Play). Do not rank, plot, or score the outputs, and do not pick the top items.

1. **Pressure-test the PM's center-point pick** (Step 5). Is it genuinely middle of the road on both value and cost? If not, help them reason toward a better anchor. They choose it.
2. **Walk the session:** place the anchor first, then have the group plot every other output relative to it.
3. **Coach holding value and cost honest:** value is customer value tied to a product outcome; cost is real build cost scoped with tech.
4. **Give specific moves** for when the room crowds everything into high-value, low-cost (see [Prioritization Is a Conversation About Trade-offs](#prioritization-is-a-conversation-about-trade-offs)).
5. **Rehearse the hard moments.** Ask the PM what they would say to the stakeholder who inflates a pet feature, to "everything is a priority," and when cost gets waved away. Then sharpen it.

Steps 5-12 describe the artifact the room produces. When the PM returns with the room's placements, record them and check them against those steps. When the PM asks you to place outputs before any session, don't place them yet: explain that value and cost come from the room (customer evidence and tech scoping), and offer to prepare the session and pressure-test a center-point anchor. If the PM then still wants a draft, or chooses Discovery mode, label the placements **AI draft placement: for the room to challenge; cost not scoped by tech**, and keep the session as the place the decision is made.

### Step 5: Find the Center Point Output

The center point output is the anchor for the entire exercise. The team - not the PM alone - must agree on it.

Criteria for the center point:

- Medium cost: not the cheapest thing to build, not the most expensive
- Medium value: not the most impactful thing for the customer, not the least
- Understandable to all participants: the team can reason about other outputs relative to it

Name the center point output explicitly. Write one or two sentences explaining why the team agreed it is medium/medium. This anchors the calibration for every other placement.

### Step 6: Classify Value for Each Output

Record how the room classified each candidate output except the center point, relative to the center point, as High, Medium, or Low.

Value is customer value. Ask: does this output drive more or less progress toward a product outcome than the center point output? Does it relieve a more or less severe customer pain?

For each classification, write a 1-2 sentence rationale that names the customer benefit or the product outcome it supports. If the rationale cannot name a customer benefit or outcome, the classification is based on assumptions - flag it.

### Step 7: Classify Cost for Each Output

Record how the room classified cost for each candidate output except the center point, relative to the center point, as High, Medium, or Low.

Cost is business cost and risk. Ask: is this output more or less expensive to build and ship than the center point output? Does it carry more or less integration risk?

For each classification, write a 1-2 sentence rationale based on what engineering or the project manager said. If no technical input is available, note the assumption and recommend a follow-up sizing conversation.

### Step 8: Place Each Output in Its Quadrant

Combine Value and Cost to assign each output to a quadrant:

- High Value + Low Cost = Quadrant I
- High Value + High Cost = Quadrant II
- Low Value + Low Cost = Quadrant III
- Low Value + High Cost = Quadrant IV
- Medium entries fall on the boundary - use judgment and team discussion to place them

**Check for inflation.** If most outputs landed in Quadrant I, the room rated each output on its own instead of against the anchor. Say so, and suggest the PM revisit the placements against the center point.

Outputs classified Medium/Medium belong near the center point. Treat them as Quadrant II or III candidates depending on which direction the team leans after discussion.

### Step 9: Identify Quadrant I Outputs

List all Quadrant I outputs. These are the primary candidates for the first development cycle.

For each Quadrant I output, name the product outcome it supports. If it cannot be linked to a product outcome, pause and ask whether the classification is correct.

### Step 10: Address Quadrant II Outputs

Quadrant II outputs are high value but high cost. Do not treat them as "do next" without additional validation.

For each Quadrant II output:

- Identify what assumptions about value and cost need to be validated before committing to the build
- Consider whether a lo-fi experiment (psk-lofi-experimentation) could reduce uncertainty before committing to full development
- If the team cannot validate the value assumptions, move the output to "Output Concepts to Validate" in the roadmap rather than "Outputs to Develop"

### Step 11: Deprioritize Quadrant III and Cut Quadrant IV

Quadrant III outputs (Low Cost, Low Value): deprioritize. Do not build them in the current cycle, even if they are cheap. "Easy to build" is not a reason to build. Note them as deferred.

Quadrant IV outputs (High Cost, Low Value): cut or avoid. If stakeholders press to keep Quadrant IV items, document the tradeoff explicitly: what Quadrant I or II investment is deferred to make room for this.

If the team cannot bring themselves to cut any Quadrant IV items, the prioritization exercise has not done its job.

### Step 12: Link High-Priority Outputs to Product Outcomes

For each Quadrant I output and each Quadrant II output the team decides to pursue, document the product outcome it supports. Use outcome language: what does the customer achieve when this output is available?

If the Outcome Tree has already been completed, reference the specific outcome by name. If not, write the outcome in outcome format: [direction] [metric] [context/circumstance].

### Step 13: Offer Next Steps

After delivering the artifact, offer three options:

1. Feed Quadrant I outputs into the Outcome-Based Roadmap (Template 17) as "Outputs to Develop"
2. Place Quadrant II outputs in "Output Concepts to Validate" and run psk-lofi-experimentation on the highest-uncertainty ones
3. Share the classification with stakeholders to surface any Quadrant IV items that carry political weight and document the tradeoff decision explicitly

## Template

Use this scaffold to produce a paste-ready four-quadrant output prioritization artifact in Productside format.

Complete all four sections in order. Do not skip the center point step - it is required for valid quadrant placements.

---

### Section 1: Identify Outputs

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

### Section 2: Center Point Output

The team must agree on one output that is medium cost and medium value - the anchor for all other placements. All other outputs will be classified relative to this center point.

**Center point output:** [name the output]

**Why this is medium/medium:** [1-2 sentences explaining why the team agreed this output represents neither extreme on value or cost - not the most impactful for the customer, not the most expensive to build]

> **Quality check:** Did the whole team agree on this anchor, or did the PM choose it alone? The center point requires team agreement. If only one person chose it, revisit before proceeding.

---

### Section 3: Four Quadrant Classification

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

### Section 4: Quadrant Summary and Action Guidance

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

Action: Do not commit these to the build plan until the key assumption is validated. Place them in "Output Concepts to Validate" in the roadmap. Consider psk-lofi-experimentation for the highest-uncertainty items.

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

## Examples

Illustrative and fictional, not customer evidence.

- **Strong:** A care-coordination team compares candidate outputs against an agreed center-point output using relative customer value and business cost; the room records its judgments.
- **Weak:** Unanchored scores appear precise while participants use different scales.
- **Drift to avoid:** Value as revenue: do not replace customer value with business revenue impact or invent the team's placements.


## Common Pitfalls

- **Defining Value from the Business Perspective:** Before classifying any output, re-read the product outcomes from the Outcome Tree. Each value classification must name what the customer achieves. If the rationale names only what the business gains, rewrite it from the customer's perspective.

- **Skipping the Center Point Anchor:** Name the center point output first. Get team agreement before any other classification begins. All subsequent placements are relative to that anchor.

- **Running This Without Engineering Input on Cost:** Do not finalize cost classifications without a technical voice. At minimum, run a rough sizing conversation with an engineering lead or project manager before locking the grid.

- **Confusing Outputs with Outcomes:** Every item on the candidate list must be a concrete, buildable thing: a specific feature, integration, interface, or capability. If the team is listing outcomes, redirect to the Outcome Tree (psk-outcome-tree) and then ask: what outputs could be built to drive that outcome?

- **Treating Quadrant II as "Do Next" Without Validation:** For every Quadrant II output, name the key assumptions about value that need to be validated before committing to the full build. Consider lo-fi experimentation (psk-lofi-experimentation) for high-uncertainty Quadrant II items before the development commitment is made.

- **Never Cutting Quadrant IV Outputs:** Document the Quadrant IV designation explicitly and surface the tradeoff to the stakeholder. "We can build this, but it will displace [specific Quadrant I output] that [customer outcome]. Is that the right call?" Force the explicit decision rather than letting Quadrant IV items survive by default.

- **Treating Quadrant Positions as Permanent:** Treat the grid as a living artifact. Revisit it when cost estimates change significantly (after technical investigation), when discovery reveals new information about customer value, or when the solution hypothesis changes.

- **Using Internal Metrics as Value:** For each value classification, ask: how does this output change what the customer can achieve? If the answer is only about internal operations, the classification is measuring the wrong thing. A support ticket reduction is only customer value if it means the customer gets unblocked faster - and that customer impact should be the stated rationale.

- **AI Does the Ranking:** Prepare the PM to facilitate (Step 4). The room plots relative to the anchor, tech scopes cost, and the PM and stakeholders decide. The skill records and checks the result.

- **Everything Wins:** Anchor every placement against the center point. Ask for the outcome and evidence behind each value claim, and make tech scope cost out loud.

## References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-output-prioritization) for supporting source material and expanded examples.
