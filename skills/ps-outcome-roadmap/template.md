# Outcome-Based Roadmap and Release Plan

## When to Use This

Use this template during the **Create** phase after completing your Outcome Tree and Output Prioritization. It is most powerful when Tiny Acts of Discovery results are available to populate the discovery sections.

Upstream artifacts that feed this template:
- Outcome Tree (ps-outcome-tree): Business Outcomes header and product outcomes for the roadmap row
- Output Prioritization (ps-output-prioritization): Quadrant I outputs for Now release plan; Quadrant II outputs for Next output concepts
- Tiny Acts of Discovery (ps-tiny-acts-discovery): specific experiments and assumptions for the discovery sections

---

## Template

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

## Usage Guidance

### Filling the Template

1. Complete **Business Outcomes** first. Everything below it must trace back to this header.
2. Fill the **Roadmap row** (Now, Next, Later) using outcome language. Do not place any feature or output name in this row.
3. Fill the **Release Plan row** (Now, Next, Later) using output language. Do not place any customer outcome statement in this row.
4. Check that every Now output in the release plan traces to a Now outcome in the roadmap.
5. Fill the discovery sections (Tiny Acts, Assumptions to Validate, Assumptions to Research). If any are blank, the artifact is not ready.
6. Add the **Living Document Note** before sharing.

### What Goes Where

| Section | Language | Contains | Does NOT Contain |
|---------|----------|----------|-----------------|
| Roadmap row | Outcome language | What customers achieve | Features, capabilities, deliverables |
| Release plan row | Output language | What the team builds | Customer outcome statements |
| Business Outcomes header | Business language | Business-level goal with measurable target | Vague directions like "grow revenue" |
| Tiny Acts of Discovery | Action language | Specific tests running now | Future research phases |
| Assumptions to Validate | Hypothesis language | Testable beliefs about customer behavior | Feature requests or build decisions |
| Assumptions to Research | Question language | Open questions needing research | Assumptions already ready to test |

### The Graduation Path

Items move left as confidence increases:

- Later outcome hypothesis + research resolved = moves to Next as Product Outcome to Validate
- Next outcome + assumptions validated = moves to Now as Product Outcome to Pursue
- Next output concept + assumptions validated = moves to Now as Output to Develop
- Now output shipped + outcome achieved = removed from roadmap; captured in metrics

Items can move right if confidence decreases. A Now outcome with an unexpected discovery finding should move back to Next for additional validation rather than continuing to drive output development on a weakened foundation.

### Connecting to Other Skills

- **Upstream:** ps-outcome-tree provides the Business Outcomes header and product outcomes for the roadmap row. ps-output-prioritization provides Quadrant I outputs for Now and Quadrant II outputs for Next output concepts. ps-tiny-acts-discovery provides specific experiments and assumptions.
- **Downstream:** This artifact is the primary communication tool for the Create phase. Share the roadmap row (outcome language) with leadership and the release plan row (output language) with engineering.

### Capacity Reference

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
