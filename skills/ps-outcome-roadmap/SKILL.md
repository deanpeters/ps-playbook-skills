---
name: ps-outcome-roadmap
description: >-
  Build an outcome-based roadmap and release plan that connects product outcomes
  to outputs, sorted by confidence level. Use when a PM needs to communicate
  what the team is pursuing and why, in language that works for both executives
  and engineering.
intent: >-
  Help a Product Manager and their team create a living roadmap that separates
  what customers will achieve (roadmap layer) from what the team will build
  (release plan layer), organized by confidence level so stakeholders can see
  which work is committed, which is directional, and which is still being
  explored.
type: component
blueprint_stage: Create
best_for:
  - "Building an outcome-based roadmap organized around what customers achieve"
  - "Connecting product outcomes to a concrete release plan with outputs and experiments"
  - "Communicating roadmap decisions to stakeholders in outcome language, not feature lists"
scenarios:
  - "I need to build a roadmap organized around outcomes, not a feature list"
  - "Help me connect our product outcomes to a concrete release plan with dates and owners"
---


## Purpose

Create a **Productside-style Outcome-Based Roadmap and Release Plan** from a product team's validated outcomes and prioritized outputs.

This skill helps a Product Manager combine two connected layers into one artifact: a roadmap organized around product outcomes (what customers achieve) and a release plan organized around outputs (features, capabilities, and experiments). Both layers are sorted by confidence level into Now, Next, and Later columns.

The artifact is a **living document**. Discovery is never complete. As the team runs Tiny Acts of Discovery and resolves assumptions, items graduate from Later to Next to Now. The roadmap should be revisited at every major discovery or delivery milestone.

The critical distinction this skill enforces: the **roadmap row speaks outcome language only**. The **release plan row speaks output language only**. Mixing them creates confusion for every audience.

## Key Concepts

### Outcomes vs. Outputs - the Load-Bearing Distinction

This roadmap has two rows for a reason. They speak different languages to different audiences.

**Outcomes** are what customers achieve. They describe a changed state in the customer's world: "field technicians resolve equipment faults without returning to the depot," "quality inspectors catch defects before they leave the line." Outcomes belong in the roadmap row.

**Outputs** are what the team builds. They describe a deliverable: "fault diagnosis mobile app," "in-line defect vision scanner," "parts availability lookup." Outputs belong in the release plan row.

When outputs appear in the roadmap row, executives read a feature list instead of a value plan. When outcomes appear in the release plan row, engineering cannot build a sprint from them. Keep the rows separate.

### The Now / Next / Later Confidence Framework

The three columns are organized by **confidence level**, not by priority or preference.

**Now - High Confidence:** The team has enough validated evidence to commit. These product outcomes have been tested against real customer behavior and real technical constraints. The team is pursuing them actively. Outputs in this column are in the release plan.

**Next - Medium Confidence:** The team believes in these outcomes and output ideas, but needs to resolve specific assumptions before committing fully. The primary work in Next is validation: running assumptions to ground so confident items can graduate to Now.

**Later - Low Confidence:** These are hypotheses - early-stage outcome ideas and open questions that require research before the team can evaluate them seriously. The primary work in Later is research: converting open questions into resolvable assumptions.

Confidence is not a popularity contest. An outcome moves left because the team has resolved uncertainty, not because leadership prefers it.

### How Items Graduate

- **Later to Next:** When Assumptions to Research resolve enough uncertainty to form a testable assumption with a clear hypothesis.
- **Next to Now:** When Assumptions to Validate confirm enough confidence that the team can commit to the outcome and begin output development.
- **Now to Done:** When the output is shipped and the outcome can be measured.

Items can also move right. If a Now outcome proves harder to achieve than expected, or if new evidence undermines confidence, it should move back to Next for additional validation.

### Discovery Is Continuous - Not a Future Phase

The discovery activities in this artifact (Tiny Acts of Discovery, Assumptions to Validate, Assumptions to Research) run **in parallel with the release work**. They are not a future phase that begins after Now outputs ship.

While the team is building Now outputs, it is simultaneously running Tiny Acts to refine those outputs, validating assumptions to graduate Next items, and researching questions to graduate Later items. The three columns are active at the same time.

A roadmap with empty discovery sections is not a living document. It is a delivery schedule.

### Business Outcomes as the Anchor

Everything on the roadmap traces back to the Business Outcomes header. This is the business-level goal the product serves, drawn from the Outcome Tree. It provides the "why behind the what" and prevents the roadmap from becoming a disconnected list of features.

If a product outcome in the Now column cannot be connected to the Business Outcomes header, it should not be on the roadmap.

### The Artifact Is a Communication Tool

Different audiences need different layers of the same artifact.

**Executives** read the Business Outcomes header and the roadmap row. They see what business goal is being served and what customer outcomes the team is pursuing at each confidence level.

**Engineering** reads the release plan row. They see what is being built (Now outputs), what needs validation before it can enter the build queue (Next output concepts), and what is still being explored (Later assumptions).

**Both audiences** are looking at the same artifact. No separate decks, no translation layer. The structure does the work.

### This Builds Directly From the Outcome Tree

The product outcomes in the Now and Next roadmap cells should come directly from the ps-outcome-tree, not be invented fresh here. The PM should not use the roadmap as an opportunity to introduce new outcomes that have not been validated through the Outcome Tree play.

If the Outcome Tree has not been run, offer to run ps-outcome-tree first, or accept the PM's description of outcomes directly. But confirm they are grounded in discovery work.

### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **critic of the roadmap the PM drafted**. It checks that each horizon holds outcomes, not outputs; that items sit in Now, Next, or Later by confidence; that each output links to an outcome; and that discovery work appears alongside delivery. The placements and the sequence stay with the PM and their team.

- **Use it when:** the PM has an outcome tree and a draft roadmap, and wants it pressure-tested before sharing it.
- **Avoid it when:** the request is to produce a dated feature roadmap, or to place items without the PM's evidence about confidence.
- **Return:** outputs posing as outcomes flagged, each placement questioned against the evidence behind it, and links from outputs to outcomes checked.

### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

### Guided Mode

When asked for guidance, when the user is unfamiliar, or when context is missing:

1. Explain the output and estimated question count. Offer Guided, Context dump, or Best guess; default to Guided and ask the first question immediately.
2. Use supplied context instead of asking again. In Context dump mode, summarize Known / Assumed / Missing / Conflicting first.
3. Ask one bolded question per turn with a progress label, three context-specific numbered recommendations, option 4 Other, and an input hint. For facts only the user can know, ask openly without suggested answers and explain why. Ground unfamiliar domain options in research when needed.
4. Adapt recommendations to the answers. Explain why a question matters when helpful.
5. Answer interruptions, honor corrections and mode switches, and stop when asked. Resume with a brief recap and the pending question.
6. Recap supplied facts, assumptions, gaps, and readiness; confirm before generating a guided artifact. When the user faces a decision, recommend an option with reasons and offer distinct alternatives. The user decides.
7. Best guess may proceed immediately: label inferred details inline and end with Assumptions to Validate, ranked by decision impact. With sufficient supplied context, execute directly.

## Application

Use [Template](#template) for the scaffold.


### Required Output Convention

Default to a **clean, paste-ready artifact**.

That means:

- Business Outcomes header is specific and measurable (not "grow revenue")
- At least one product outcome in each column (Now, Next, Later)
- At least two outputs in the Now release plan
- Discovery sections (Tiny Acts, Assumptions to Validate, Assumptions to Research) are not left blank
- Every Now output traces to a Now outcome
- No outputs appear in the roadmap row; no outcomes appear in the release plan row
- Explanation belongs below the artifact, not inside the fields

### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

When a draft roadmap lists outputs (features, releases, projects), don't guess the outcomes behind them, even labeled as guesses. Name each item as an output and ask the PM what customer outcome it serves and what evidence puts it in Now, Next, or Later. The outcomes come from the PM and their customers.

### Step 1: Tech-Role Bias Guard

Before drafting any content, confirm that the product outcomes are written from the **customer's perspective**. Outcomes describe what customers achieve - what changes in their world when the product works.

The team role bias is to write outcomes in engineering language: "deploy the alert system," "enable real-time API access," "build the reporting module." These are outputs, not outcomes.

Ask the user: who is the customer for this product, and what does success look like from their point of view? What changes in how they work, what they can accomplish, or how they feel about their work?

Do not proceed until there is a customer-perspective answer to that question.

### Step 2: Gather Upstream Artifacts

Before drafting, ask whether the user has materials to share:

- Outcome Tree from ps-outcome-tree (Business Outcomes and product outcomes)
- Output prioritization results from ps-output-prioritization (Quadrant I and Quadrant II outputs)
- Tiny Acts findings from ps-tiny-acts-discovery (specific experiments and assumptions)
- Any prior roadmap or release plan the team has already discussed

Check whether each exists; offer to help fill gaps; accept equivalent input from any source. Do not gate the skill on whether the upstream play has been run. Accept the PM's direct description if the artifact is not available.

Make a note of which sections are drawn from upstream artifacts and which are being drafted fresh.

### Step 3: Write the Business Outcomes Header

Draft the Business Outcomes header from the Outcome Tree's business outcome field. This should be one to two sentences describing the business-level goal this roadmap serves.

The header must be specific and anchored. "Reduce unplanned equipment downtime by 30% across field service regions" is anchored. "Improve operational efficiency" is not.

If the outcome has a measurable target, include it. If it does not, note that a target should be defined.

> Quality check: Can you trace every product outcome below to this business goal? If not, either the business goal is too narrow or one of the product outcomes does not belong on this roadmap.

### Step 4: Populate the NOW Roadmap - Product Outcomes to Pursue

List the product outcomes the team is confident will create customer value and has committed to pursuing. These should come directly from the Outcome Tree (validated product outcomes) or from the PM's description of validated discovery findings.

Write in customer language: what customers achieve, not what the product does.

Each outcome should be specific enough that the team can measure whether it has been achieved. "Field technicians identify root causes without waiting for depot diagnostics" is specific. "Improve technician experience" is not.

> Quality check: Are these outcomes written from the customer's point of view? Can the team measure achievement? Do they trace to the Business Outcomes header?

### Step 5: Populate the NEXT Roadmap - Product Outcomes to Validate

List the product outcomes the team believes in but has not yet validated enough to commit to. These outcomes need testing - specific assumptions must resolve before the team can move them to Now.

For each outcome, the key question is: what would have to be true for this to earn high confidence?

> Quality check: Is each outcome distinct from the Now outcomes? Is there a clear validation question that could move this outcome left?

### Step 6: Populate the LATER Roadmap - Product Outcome Hypotheses

List early-stage outcome ideas that require research before the team can even form a testable hypothesis. These are genuine unknowns - areas where the team has a direction but not enough understanding to design a validation test.

Write these as outcome hypotheses, not as research questions. "Procurement managers could reduce approval cycle time to under 48 hours if sourcing exceptions were flagged earlier" is a hypothesis. "Research whether procurement managers care about approval times" is a research question.

> Quality check: Is each hypothesis plausible based on existing domain knowledge? Is there a clear question that would move this to Next?

### Step 7: Populate Outputs to Develop (NOW)

List the features and capabilities that will drive the Now outcomes. These come from Quadrant I outputs in ps-output-prioritization (low cost, high value) or from the PM's direct input on what is in active development.

Write as specific output names, not categories. "Real-time fault alert push notification" is specific. "Notification system" is a category.

> Quality check: Does every output trace to a Now outcome? If an output cannot be connected to a Now outcome, it should not be in the Now release plan.

### Step 8: List Tiny Acts of Discovery (NOW)

List the small, fast experiments the team is running in parallel with Now output development. These come from ps-tiny-acts-discovery or from the PM's direct input.

Each Tiny Act should be specific enough to run: name what is being tested, how, and with whom. "Run a 5-person session with field technicians using a paper mock of the fault alert screen to confirm the alert hierarchy makes sense to them" is a Tiny Act. "Test the UI" is not.

> Quality check: Are these running now, in parallel with the outputs being built? Are they specific enough to execute this week?

### Step 9: Populate Output Concepts to Validate (NEXT)

List the output ideas that need validation before entering the release plan. These come from Quadrant II outputs in ps-output-prioritization (high cost, high value - needs more evidence before committing) or from the PM's description of candidates under consideration.

> Quality check: Is each concept clearly tied to a Next outcome? Is there a specific assumption that, if validated, would move this into Now outputs?

### Step 10: List Assumptions to Validate (NEXT)

List the specific hypotheses and assumptions that must be resolved to move Next outcomes and output concepts to Now. Write these as testable hypothesis statements, not as features.

Format: "We believe [customer segment] will [behavior or outcome] when [condition or stimulus], because [reasoning]."

A well-formed assumption can be tested. A feature request ("build the dashboard") cannot.

> Quality check: Is each assumption specific enough to design a test around? Does each assumption trace to a Next outcome or output concept?

### Step 11: List Assumptions to Research (LATER)

List the open questions and hypotheses that must be explored to move Later outcome hypotheses to Next. These are broader than testable assumptions - they require research to even know what to test.

Write as open questions or early hypotheses. The goal is to move from "we don't know" to "we have a hypothesis we can test."

> Quality check: Is each question specific enough to guide research? Can the PM name a method (interviews, observation, data pull) that would start to answer it?

### Step 12: Review Alignment

Before presenting the artifact, check:

- Every Now output traces to a Now outcome
- No outputs appear in the roadmap row
- No outcomes appear in the release plan row
- Discovery sections are not blank
- Business Outcomes header is specific and measurable
- Now, Next, and Later columns each have content (the roadmap is not front-loaded into Now)

If an output cannot be traced to an outcome, ask whether the outcome belongs on the roadmap and is missing, or whether the output should be reconsidered.

### Step 13: Offer Next Steps

At the end of the artifact, offer three options:

1. Share the roadmap with leadership: the Business Outcomes header and roadmap row give executives the outcome-level view they need to evaluate direction without getting into features
2. Share the release plan with engineering: the output-focused bottom row gives the team concrete, prioritized work with clear discovery activities running alongside
3. Schedule a review cadence: propose a specific date or milestone trigger for the next roadmap review, so the artifact stays current as assumptions resolve

## Template

### When to Use This

Use this template during the **Create** phase after completing your Outcome Tree and Output Prioritization. It is most powerful when Tiny Acts of Discovery results are available to populate the discovery sections.

Upstream artifacts that feed this template:
- Outcome Tree (ps-outcome-tree): Business Outcomes header and product outcomes for the roadmap row
- Output Prioritization (ps-output-prioritization): Quadrant I outputs for Now release plan; Quadrant II outputs for Next output concepts
- Tiny Acts of Discovery (ps-tiny-acts-discovery): specific experiments and assumptions for the discovery sections

---

### Template

```markdown
# Outcome-Based Roadmap and Release Plan

**Product or initiative:**
**Date:**
**Team:**

---

## Business Outcomes

[One or two sentences from the Outcome Tree describing the business-level goal this roadmap serves. Include a measurable target if one exists. Example: "Reduce unplanned equipment downtime by 30% across field service regions by end of year, so regional operations teams can meet SLA commitments without emergency dispatch costs."]

---

## Roadmap

The roadmap row communicates in outcome language only - what customers achieve.
Do not list outputs (features, capabilities, or deliverables) in this row.

---

### NOW - High Confidence
**Product Outcomes to Pursue**

[List 1-2 product outcomes the team has validated and is committed to pursuing. Write from the customer's perspective: what they achieve, accomplish, or experience - not what the product does.

Format: one outcome per bullet, 15-25 words each.]

- [Outcome 1: what specific customer role achieves a specific result in a specific situation]
- [Outcome 2: what specific customer role achieves a specific result in a specific situation]

> Quality check: Are these written from the customer's point of view, not the engineering team's? Can each be measured once achieved? Do they trace to the Business Outcomes header above?
> Capacity check: 1-2 outcomes; 15-25 words each.

---

### NEXT - Medium Confidence
**Product Outcomes to Validate**

[List 1-2 product outcomes the team believes in but has not yet validated. These need testing before the team commits to pursuing them. Write in customer language - what customers would achieve if this outcome proved true.]

- [Outcome 1: what specific customer role would achieve if the underlying assumption proves valid]
- [Outcome 2: what specific customer role would achieve if the underlying assumption proves valid]

> Quality check: Is there a clear validation question for each outcome - something that, if answered, would move it to Now? Are these distinct from the Now outcomes?
> Capacity check: 1-2 outcomes; 15-25 words each.

---

### LATER - Low Confidence
**Product Outcome Hypotheses**

[List 1-2 early-stage outcome ideas that require research before the team can evaluate them seriously. These are hypotheses, not validated outcomes. The team has a directional sense but not enough knowledge to design a test yet.]

- [Hypothesis 1: a plausible outcome the team suspects might be valuable but cannot yet validate]
- [Hypothesis 2: a plausible outcome the team suspects might be valuable but cannot yet validate]

> Quality check: Is each written as a hypothesis, not a research question? Is there a clear research path that would move this to Next?
> Capacity check: 1-2 hypotheses; 15-25 words each.

---

## Release Plan

The release plan row communicates in output language only - what gets built.
Do not list customer outcomes in this row.

---

### NOW
**Outputs to Develop**

[List 2-4 specific features or capabilities the team is actively building to drive the Now outcomes. Each output should trace to a Now outcome above. Use Quadrant I outputs from ps-output-prioritization if available.]

- [Output 1: specific feature or capability name - 5-10 words]
- [Output 2: specific feature or capability name - 5-10 words]
- [Output 3: specific feature or capability name - 5-10 words]

> Quality check: Does each output trace to a Now outcome above? Are these specific enough to build a sprint from? No outcomes should appear here.
> Capacity check: 2-4 outputs; 5-10 words each.

**Tiny Acts of Discovery**

[List 1-2 small, fast experiments running now alongside output development. These are not future work - they run in parallel with the outputs above. Use Tiny Acts from ps-tiny-acts-discovery if available.

Format: name the test, the method, and the participants. 10-20 words each.]

- [Tiny Act 1: specific test with named method and participants, running in parallel with Now outputs]
- [Tiny Act 2: specific test with named method and participants]

> Quality check: Are these running now, not after Now outputs ship? Are they specific enough to execute this week? Do they connect to the outputs being built?
> Capacity check: 1-2 Tiny Acts; 10-20 words each.

---

### NEXT
**Output Concepts to Validate**

[List 1-2 output ideas that need validation before entering the release plan. These are candidates, not commitments. Use Quadrant II outputs from ps-output-prioritization if available - high value, high cost items that need more evidence before committing.]

- [Output concept 1: specific feature or capability idea - 5-10 words]
- [Output concept 2: specific feature or capability idea - 5-10 words]

> Quality check: Does each concept trace to a Next outcome above? Is there a specific assumption that, if validated, would move this into Now outputs?
> Capacity check: 1-2 output concepts; 5-10 words each.

**Assumptions to Validate**

[List 2-4 specific hypotheses about customer behavior or adoption that must be resolved before moving Next outcomes and output concepts to Now. Write as testable hypothesis statements, not as feature requests.

Format: "We believe [customer segment] will [behavior] when [condition], because [reasoning]." 10-20 words each.]

- [Assumption 1: testable hypothesis about customer behavior or adoption]
- [Assumption 2: testable hypothesis about customer behavior or adoption]
- [Assumption 3: testable hypothesis about customer behavior or adoption]

> Quality check: Is each assumption specific enough to design a test around? Is it about customer behavior or sentiment - not a technical or feature decision? Does it connect to a Next outcome?
> Capacity check: 2-4 assumptions; 10-20 words each.

---

### LATER
**Assumptions to Research**

[List 2-4 open questions and broad hypotheses that must be explored before Later outcome hypotheses can graduate to Next. These are wider than testable assumptions - they need research to even know what to test.

Format: an open question or early hypothesis. 10-20 words each.]

- [Research question 1: open question or early hypothesis about the Later outcome area]
- [Research question 2: open question or early hypothesis about the Later outcome area]
- [Research question 3: open question or early hypothesis about the Later outcome area]

> Quality check: Is each specific enough to guide a research method (interviews, observation, data pull)? Does it connect to a Later hypothesis above? Would answering this question move an item to Next?
> Capacity check: 2-4 items; 10-20 words each.

---

## Living Document Note

Mark when and how this roadmap will be reviewed:

- Next scheduled review:
- Trigger for unscheduled review (e.g., "when a Tiny Act produces a result" or "when a Next assumption is resolved"):
- Owner of the review cadence:
```

---

### Usage Guidance

#### Filling the Template

1. Complete **Business Outcomes** first. Everything below it must trace back to this header.
2. Fill the **Roadmap row** (Now, Next, Later) using outcome language. Do not place any feature or output name in this row.
3. Fill the **Release Plan row** (Now, Next, Later) using output language. Do not place any customer outcome statement in this row.
4. Check that every Now output in the release plan traces to a Now outcome in the roadmap.
5. Fill the discovery sections (Tiny Acts, Assumptions to Validate, Assumptions to Research). If any are blank, the artifact is not ready.
6. Add the **Living Document Note** before sharing.

#### What Goes Where

| Section | Language | Contains | Does NOT Contain |
|---------|----------|----------|-----------------|
| Roadmap row | Outcome language | What customers achieve | Features, capabilities, deliverables |
| Release plan row | Output language | What the team builds | Customer outcome statements |
| Business Outcomes header | Business language | Business-level goal with measurable target | Vague directions like "grow revenue" |
| Tiny Acts of Discovery | Action language | Specific tests running now | Future research phases |
| Assumptions to Validate | Hypothesis language | Testable beliefs about customer behavior | Feature requests or build decisions |
| Assumptions to Research | Question language | Open questions needing research | Assumptions already ready to test |

#### The Graduation Path

Items move left as confidence increases:

- Later outcome hypothesis + research resolved = moves to Next as Product Outcome to Validate
- Next outcome + assumptions validated = moves to Now as Product Outcome to Pursue
- Next output concept + assumptions validated = moves to Now as Output to Develop
- Now output shipped + outcome achieved = removed from roadmap; captured in metrics

Items can move right if confidence decreases. A Now outcome with an unexpected discovery finding should move back to Next for additional validation rather than continuing to drive output development on a weakened foundation.

#### Connecting to Other Skills

- **Upstream:** ps-outcome-tree provides the Business Outcomes header and product outcomes for the roadmap row. ps-output-prioritization provides Quadrant I outputs for Now and Quadrant II outputs for Next output concepts. ps-tiny-acts-discovery provides specific experiments and assumptions.
- **Downstream:** This artifact is the primary communication tool for the Create phase. Share the roadmap row (outcome language) with leadership and the release plan row (output language) with engineering.

#### Capacity Reference

| Section | Items | Words per Item | Notes |
|---------|-------|---------------|-------|
| Business Outcomes | 1-2 sentences | 20-35 words total | Specific + measurable target |
| Product Outcomes - Now | 1-2 outcomes | 15-25 words each | Customer language only |
| Product Outcomes - Next | 1-2 outcomes | 15-25 words each | Customer language only |
| Product Outcome Hypotheses - Later | 1-2 hypotheses | 15-25 words each | Customer language only |
| Outputs to Develop | 2-4 outputs | 5-10 words each | Specific feature or capability names |
| Tiny Acts of Discovery | 1-2 acts | 10-20 words each | Running now, in parallel |
| Output Concepts to Validate | 1-2 concepts | 5-10 words each | Candidate outputs, not commitments |
| Assumptions to Validate | 2-4 assumptions | 10-20 words each | Hypothesis format |
| Assumptions to Research | 2-4 questions | 10-20 words each | Open question or early hypothesis |

## Examples

Illustrative and fictional, not customer evidence.

- **Strong:** Roadmap: technicians diagnose faults sooner. Release plan: deliver the diagnostic checklist that may support that outcome. Distinguish confidence horizons.
- **Weak:** A dated feature list alone hides the customer progress each release is meant to support.
- **Drift to avoid:** Business language in the customer row: revenue growth belongs at the business layer, not as a substitute for the technician's outcome.


## Common Pitfalls

- **Feature-Based Roadmap - Outputs in the Roadmap Row:** Ask: what does the customer achieve when this output exists and works? That answer is the outcome. Replace the output in the roadmap row with the outcome. Move the output to the release plan row.

- **All Outcomes in NOW - No Differentiation by Confidence:** Push the team to differentiate honestly. If everything is high confidence, either the team is building too narrowly or they have not surfaced what they do not yet know. Most real product situations have at least two or three outcome hypotheses in Next or Later.

- **Roadmap Written in Business/Financial Language:** Reframe every outcome as a customer achievement: "What does the customer experience or accomplish when this metric improves?" "Increase ARR by 15%" becomes "contract renewal managers approve renewals faster because pricing scenarios are visible before the meeting." The business metric can live in the Business Outcomes header, not in the product outcome row.

- **Discovery Sections Left Blank:** Treat empty discovery sections as a red flag, not a formatting gap. At minimum, name one Tiny Act running alongside Now outputs and one assumption in each of Next and Later. If the team genuinely has no open questions, probe: what would have to be true for the Next outcomes to earn high confidence? Those answers are the starting assumptions.

- **Outputs Not Connected to Outcomes:** For each output, ask: which Now outcome does this drive? If no outcome in the Now roadmap row answers that question, either the outcome is missing from the roadmap or the output should not be in the Now release plan.

- **Static Artifact - Built Once and Never Updated:** Establish a specific review cadence tied to discovery milestones, not to the calendar quarter. When a Tiny Act produces a result or an assumption is resolved, the roadmap should update the same week. Build the review trigger into the artifact itself.

- **Business Outcomes Header Missing or Too Vague:** Make the business outcome specific and measurable. Name the direction, the metric, and the target if possible. "Reduce unplanned equipment downtime by 30% in field service regions by end of year" is an anchor. "Improve operations" is not.

- **Assumptions Written as Features Instead of Hypotheses:** Reframe each item as a testable hypothesis about customer behavior: "We believe [customer role] will [specific behavior] when [condition], because [reasoning]." The feature that might follow from a validated assumption is an output - it belongs in the release plan, not in the assumptions section.

- **A Feature List Dressed as an Outcome Roadmap:** Put product outcomes in each horizon, and link each output to the outcome it serves. Place items by confidence, based on evidence.

## References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-outcome-roadmap) for supporting source material and expanded examples.
