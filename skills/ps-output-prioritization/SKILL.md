---
name: ps-output-prioritization
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

Customer value: requires data from discovery work, empathy interviews, or validated product outcomes. The Outcome Tree (ps-outcome-tree) is the best source for linking outputs to product outcomes.

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

The Productside Playbook sets one rule for every AI-assisted Play: **the Product Manager does the thinking, and AI pressure-tests it.** In this skill, you are the AI. Hold yourself to these rules:

1. **Pressure-test before you produce.** When the user brings a draft, critique it against the Play's formats and criteria first. Point at the specific words that fail and ask the user to fix them. Offer rewrites only after the critique, as options to accept, adapt, or reject.
2. **Never stand in for the customer.** Do not present jobs, quotes, needs, or pains you generated as research, and do not answer as the persona as if your answers were evidence. Anything you draft about customers is a hypothesis, labeled as one, to validate with real people. Role-play is allowed only as rehearsal where the Play calls for it, labeled as practice, and nothing from it goes into findings.
3. **Never stand in for the team's judgment.** Do not put unsourced figures into the artifact, and do not make calls the team should own. A number without a source is a blank to fill, so mark it that way.
4. **Work the five habits.** *Context:* ask for the persona, market, outcome, and constraints when they are missing. *Guide:* offer competing views and welcome pushback. *Enforce:* work inside the Play's template, not around it. *Outcome:* tie the work to the decision it supports. *Iterate:* go step by step rather than one-shot.
5. **Keep best guess honest.** Best guess mode is allowed. When you use it, label every inferred detail inline and end with **Assumptions to Validate**. A best guess is a starting point to test, never a finding.

For people working in a chat tool without this skill, the Play's copy-paste prompts are in [prompts/](prompts/README.md).

### Guided Mode

When a user asks to be walked through this skill, signals unfamiliarity, or invokes it without enough context, run in guided mode. **Do NOT batch multiple questions into one turn. Do NOT list everything you need up front. One question per turn, every turn.**

1. **Open with a heads-up.** State what the skill produces, the estimated number of questions, and where you will stop for the user's decision. Offer three entry paths:
   - (1) **Guided** - one question at a time with recommendations
   - (2) **Context dump** - paste what you know and I will ask only what is missing
   - (3) **Best guess** - I will infer what I can and label every assumption

   Then ask the first question immediately (do not wait for the user to pick a mode - Guided is the default).

2. **Start from what is already supplied.** Treat text in the request, pasted notes, attached files, upstream Play artifacts, and decisions made earlier in the conversation as answers already given. Do not ask for them again. Begin at the first real gap, and keep the progress label honest about what remains.

3. **One question per turn.** Every turn follows this exact format:

   > `Context Q2/5`
   >
   > **Who are the primary users of this product?**
   >
   > Some options to consider:
   > 1. Clinical data managers who run queries against study databases
   > 2. Research scientists who need self-service access to trial data
   > 3. Biostatisticians who build analysis-ready datasets
   > 4. Other (describe your users)
   >
   > Pick one or more (e.g. `1`, `1,3`, `1 and 3`), or describe in your own words.

   The progress label (e.g. `Context Q2/5`) is mandatory on every turn. Recommendations must always be numbered `1.`, `2.`, `3.`, `4. Other` - never presented as bullet points or unnumbered prose. The three recommendations must be specific to the skill, the industry, and the context gathered so far - never generic placeholders. If you lack domain context for good recommendations, do a web search first to ground your options in real roles, real products, or real workflows. Explain why a question matters when that is not obvious, and ask a follow-up only when the answer could change the artifact or the decision.

   **Exception: evidence only the user has.** When a question asks for something only the user can know (a root cause, what customers said or did, what the user observed, a number they must set), ask it as an open question with no numbered options, and say why there are none. Options there would put guesses in the user's mouth.

4. **Recommendations get smarter each turn.** Each answer becomes context for the next question's recommendations. By the mid-point, options should reflect the specific product, customer, and situation the user has described - not generic suggestions. Early questions can use industry-typical examples; later questions must incorporate what the user has already told you.

5. **In context dump mode, show what you extracted first.** Before asking anything, give a short **Known / Assumed / Missing / Conflicting** summary of what the user supplied. Credit where each item came from, and keep what a source reported separate from what has been verified. Then ask only the questions that would most change the artifact.

6. **Interruption-safe.** Handle any of these mid-session:
   - **Meta questions** ("how many left?", "what does this term mean?"): answer directly, restate progress, restate the pending question, then wait.
   - **Mode switch** ("just take your best guess", "here is everything I know"): switch to the requested mode immediately. For best guess, infer remaining answers from context gathered so far, generate the artifact, and end with an explicit **Assumptions to Validate** list, ranked by how much each could change the decision. For context dump, parse what was provided and ask only about gaps.
   - **Correction** ("actually, go back to Q2"): revisit that question with the original recommendations updated for current context.
   - **Pause or stop**: stop immediately. On resume, summarize what was captured, what is still open, and the next question.

7. **Finish with a summary, then hand back the decision.** After the context is gathered, recap in a few short bullets: what was supplied, what was inferred, what remains unknown or disputed, and whether the work is ready for a decision. Confirm before generating the artifact. If best guess mode was used at any point, end with an explicit **Assumptions to Validate** list. When the user faces a choice (which option, which next Play, whether to proceed), present a numbered ladder: the option the evidence favors first, labeled `(Recommended)`, then two or three genuinely distinct alternatives, each with its tradeoff in one sentence, then `Other`. Allow combining options where it makes sense. The user decides.

## Application

Use [template.md](template.md) for the scaffold.

See the source play pages in [assets/ps_output_prioritization_playbook_pages.pdf](assets/ps_output_prioritization_playbook_pages.pdf).

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

Ask the user to name the customer role. If a proto-persona exists (from ps-proto-persona), use it. If an Outcome Tree exists (from ps-outcome-tree), confirm the product outcomes before evaluating outputs against value.

### Step 2: Gather Available Artifacts

Before drafting, ask whether the user has materials to share:

- Solution hypothesis from ps-solution-hypothesis (defines the solution being decomposed into outputs)
- Product outcomes from ps-outcome-tree (used to evaluate value from the customer's perspective)
- Discovery findings from ps-empathy-interviews or ps-problem-identification (used to calibrate which customer pains are most severe)
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

Unless the PM is returning with the room's placements, prepare them to lead the session (mirrors [prompts/01](prompts/01-rehearse-prioritization-session.md)). Do not rank, plot, or score the outputs, and do not pick the top items.

1. **Pressure-test the PM's center-point pick** (Step 5). Is it genuinely middle of the road on both value and cost? If not, help them reason toward a better anchor. They choose it.
2. **Walk the session:** place the anchor first, then have the group plot every other output relative to it.
3. **Coach holding value and cost honest:** value is customer value tied to a product outcome; cost is real build cost scoped with tech.
4. **Give specific moves** for when the room crowds everything into high-value, low-cost (see [Prioritization Is a Conversation About Trade-offs](#prioritization-is-a-conversation-about-trade-offs)).
5. **Rehearse the hard moments.** Ask the PM what they would say to the stakeholder who inflates a pet feature, to "everything is a priority," and when cost gets waved away. Then sharpen it.

Steps 5-12 describe the artifact the room produces. When the PM returns with the room's placements, record them and check them against those steps. When the PM asks you to place outputs before any session, don't place them yet: explain that value and cost come from the room (customer evidence and tech scoping), and offer to prepare the session and pressure-test a center-point anchor. If the PM then still wants a draft, or chooses best guess mode, label the placements **AI draft placement: for the room to challenge; cost not scoped by tech**, and keep the session as the place the decision is made.

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
- Consider whether a lo-fi experiment (ps-lofi-experimentation) could reduce uncertainty before committing to full development
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
2. Place Quadrant II outputs in "Output Concepts to Validate" and run ps-lofi-experimentation on the highest-uncertainty ones
3. Share the classification with stakeholders to surface any Quadrant IV items that carry political weight and document the tradeoff decision explicitly

## Examples

See [examples/sample.md](examples/sample.md).

The example set includes:

- a strong classification with genuine spread across quadrants, Quadrant I outputs linked to product outcomes, and Quadrant IV outputs actually cut
- a weak version where all outputs are rated high value, no center point is established, and classifications are made without engineering input or customer data
- a drift-bug example where value is defined as business revenue impact rather than customer outcome impact, producing a ranking that serves internal priorities rather than customer needs

## Common Pitfalls

### Pitfall 1: Defining Value from the Business Perspective

**Symptom:** Value classifications reference revenue potential, upsell opportunity, investor appeal, or internal cost savings rather than customer outcome impact.

**Consequence:** Outputs that are most beneficial to the business rank higher than outputs that most relieve customer pain or drive customer progress. The product delivers for the business but underserves the customer - and adoption suffers.

**Fix:** Before classifying any output, re-read the product outcomes from the Outcome Tree. Each value classification must name what the customer achieves. If the rationale names only what the business gains, rewrite it from the customer's perspective.

### Pitfall 2: Skipping the Center Point Anchor

**Symptom:** The team classifies each output as High, Medium, or Low on absolute scales without agreeing on a shared reference point.

**Consequence:** "High value" means different things to different people on the team. Everything trends toward High Value because no one wants to downgrade their preferred feature. The grid fills up in the upper half and prioritization is impossible.

**Fix:** Name the center point output first. Get team agreement before any other classification begins. All subsequent placements are relative to that anchor.

### Pitfall 3: Running This Without Engineering Input on Cost

**Symptom:** The PM classifies all costs alone, using judgment about what "seems" expensive.

**Consequence:** Cost estimates are wrong. Cheap-looking outputs turn out to be expensive due to integration complexity or technical debt. Expensive-looking outputs may be straightforward. The grid is misleading and the roadmap it generates is unworkable.

**Fix:** Do not finalize cost classifications without a technical voice. At minimum, run a rough sizing conversation with an engineering lead or project manager before locking the grid.

### Pitfall 4: Confusing Outputs with Outcomes

**Symptom:** The candidate list contains items like "increased retention," "better user experience," or "faster time to value." These are outcomes, not outputs.

**Consequence:** The team is not actually prioritizing what to build - they are prioritizing goals. The grid cannot function because outcomes cannot be placed on a development cost axis.

**Fix:** Every item on the candidate list must be a concrete, buildable thing: a specific feature, integration, interface, or capability. If the team is listing outcomes, redirect to the Outcome Tree (ps-outcome-tree) and then ask: what outputs could be built to drive that outcome?

### Pitfall 5: Treating Quadrant II as "Do Next" Without Validation

**Symptom:** Quadrant II outputs (High Value, High Cost) are moved directly into the sprint plan alongside Quadrant I outputs, without additional investigation.

**Consequence:** The team commits significant capacity to high-cost builds whose value assumptions have not been validated. When the output ships and adoption is weak, the team discovers the value was overestimated - too late.

**Fix:** For every Quadrant II output, name the key assumptions about value that need to be validated before committing to the full build. Consider lo-fi experimentation (ps-lofi-experimentation) for high-uncertainty Quadrant II items before the development commitment is made.

### Pitfall 6: Never Cutting Quadrant IV Outputs

**Symptom:** The team acknowledges that certain outputs are High Cost and Low Value but keeps them on the list because a stakeholder "really wants it" or because the feature was promised.

**Consequence:** Capacity is drained by outputs that deliver poor customer value. Quadrant I and II investments are deferred to accommodate Quadrant IV items.

**Fix:** Document the Quadrant IV designation explicitly and surface the tradeoff to the stakeholder. "We can build this, but it will displace [specific Quadrant I output] that [customer outcome]. Is that the right call?" Force the explicit decision rather than letting Quadrant IV items survive by default.

### Pitfall 7: Treating Quadrant Positions as Permanent

**Symptom:** The team runs this exercise once and treats the quadrant placements as fixed for the life of the product.

**Consequence:** Cost estimates that were based on incomplete technical knowledge remain unchanged even after the team learns the true scope. Value estimates that were based on assumptions remain unchanged even after discovery reveals the customer does not care about that output.

**Fix:** Treat the grid as a living artifact. Revisit it when cost estimates change significantly (after technical investigation), when discovery reveals new information about customer value, or when the solution hypothesis changes.

### Pitfall 8: Using Internal Metrics as Value

**Symptom:** Value classifications cite internal business metrics: "this output will reduce support tickets by 20%," "this output will accelerate our sales cycle," "this output will improve the demo."

**Consequence:** The product gets built to serve internal teams rather than the customer. Support cost reduction is a valid business goal, but it is not the same as customer value. A feature that reduces support tickets may or may not reduce customer pain.

**Fix:** For each value classification, ask: how does this output change what the customer can achieve? If the answer is only about internal operations, the classification is measuring the wrong thing. A support ticket reduction is only customer value if it means the customer gets unblocked faster - and that customer impact should be the stated rationale.

### Pitfall 9: AI Does the Ranking

**Symptom:** The PM pastes the feature list and asks which to build first. The agent sorts it into quadrants, and its top three become the plan.

**Consequence:** There's no real cost data and no buy-in behind the ranking. The team never weighs in, and the PM can't defend the ranking when a stakeholder pushes back.

**Fix:** Prepare the PM to facilitate (Step 4). The room plots relative to the anchor, tech scopes cost, and the PM and stakeholders decide. The skill records and checks the result.

### Pitfall 10: Everything Wins

**Symptom:** Each output is rated on its own merits, and almost all of them land high-value. Cost is waved away rather than scoped. Nothing gets cut.

**Consequence:** The four-quadrant grid becomes one crowded quadrant, and the prioritization decides nothing.

**Fix:** Anchor every placement against the center point. Ask for the outcome and evidence behind each value claim, and make tech scope cost out loud.

## References

### Skill Files

- [template.md](template.md) - four-quadrant scaffold with quality checks
- [prompts/](prompts/README.md) - copy-paste prompt for chat-based AI tools (1: rehearse your prioritization session)
- [examples/sample.md](examples/sample.md) - strong, weak, and drift-bug examples

### Related Skills

- **Upstream:** [ps-outcome-tree](../ps-outcome-tree/SKILL.md) provides product outcomes used to evaluate output value; [ps-solution-hypothesis](../ps-solution-hypothesis/SKILL.md) defines the solution being decomposed into candidate outputs
- **Upstream (optional):** ps-tiny-acts-discovery populates the candidate output list; [ps-empathy-interviews](../ps-empathy-interviews/SKILL.md) and [ps-problem-identification](../ps-problem-identification/SKILL.md) calibrate which customer pains are most severe
- **Downstream:** Outcome-Based Roadmap (Template 17) - Quadrant I outputs feed "Outputs to Develop"; Quadrant II candidates may feed "Output Concepts to Validate"
- **Related:** [ps-lofi-experimentation](../ps-lofi-experimentation/SKILL.md) - high-uncertainty Quadrant II outputs are candidates for lo-fi experiments before full build commitment

### Project Docs

- [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)
- [informative-documents/framework-glossary.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/framework-glossary.md)
- [informative-documents/skill-dependency-map.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/skill-dependency-map.md)

### Source Material

- [assets/ps_output_prioritization_playbook_pages.pdf](assets/ps_output_prioritization_playbook_pages.pdf)
- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 87-91: Template 19 of 24 there, with the AI overview on slide 89 and prompt on slide 90. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).
- [Baseline Playbook version](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml). Full source PDF supplied separately.
- Productside Playbook companion document (supplied separately)
