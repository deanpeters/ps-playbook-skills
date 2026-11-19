---
name: ps-product-outcome-canvas
description: >-
  Consolidate all discovery and define artifacts into the Product Outcome
  Canvas, the Go/No Go decision document presented to leadership before entering
  the Create phase.
intent: >-
  Help a Product Manager synthesize the outputs of the Discover + Define phase
  into a single executive presentation artifact that makes the business case for
  investment. This is the key decision point document that enables leadership to
  approve entering the Create (build) phase.
type: component
blueprint_stage: Discover + Define
best_for:
  - "Consolidating all Discover + Define artifacts into a single Go/No Go decision surface"
  - "Practicing the business case presentation before pitching to leadership"
  - "Gating entry to the Create phase with a structured investment review"
scenarios:
  - "I need to consolidate all our discovery artifacts into one canvas for the Go/No Go review"
  - "Help me prepare the business case presentation for leadership before we enter the Create phase"
---


## Purpose

Create a **Productside-style Product Outcome Canvas** from the artifacts produced during the Discover + Define phase.

This skill is used at the **Go/No Go decision point** before the team enters the Create phase. Leaders use it to approve investment. PMs use it to practice presenting the business case to their sponsors and stakeholders.

The canvas brings together problem framing, solution positioning, customer stories, outcome targets, metrics, risks, and resource asks into a single, cohesive document. It is the artifact that answers the question leadership always asks: "Why should we build this, what will it do for us, and what do you need from us to make it happen?" It is not a summary slide.

## Key Concepts

### Why This Is a Go/No Go Document

The Product Outcome Canvas marks the formal end of the Discover + Define phase. At this point, the team has validated a problem, generated and explored solutions, formed a hypothesis, positioned the product, and assessed risks. The canvas consolidates all of that work into the form that leadership can evaluate and approve.

A canvas completed before this point is speculative. A canvas completed after this point is retrospective. The right moment is when the team has enough evidence to make a credible case but still needs authorization to proceed.

### The Three-Section Structure

**Section 1: Core Information** anchors the document. Product Name, Date, Product Manager, and Version tell the reader what they are looking at and when.

**Section 2: Summary (left column)** tells the story of the problem and solution. It includes the Problem Statement, Solution Summary, Positioning Statement, two customer stories (one per persona), and the Key Features of the proposed solution.

**Section 3: Project Boundaries (right column)** frames the business case with measurable targets and honest constraints. It includes Business Outcomes, Product Outcomes, Business Success Metrics, Product Success Metrics, top Risks, The Ask, and the Introduction Date.

The two-column design is intentional: the left column persuades through narrative and context; the right column justifies through numbers and commitments.

### Stories vs. Data

The two customer stories in the Summary section serve a purpose that data cannot: they make the problem real. A well-written story puts leadership in the room with the customer and makes the problem visceral. Data confirms the problem is worth solving; stories make people want to solve it.

Each story should anchor to a concrete moment in the customer's experience: a specific situation where the product either fails or succeeds. The before/after structure is the most reliable format: show the customer without the product, then show the same customer with it.

Stories are about the customer. Not the PM. Not the team. Not the development process. If the story protagonist is writing a PRD, facilitating a sprint, or reviewing a roadmap, the story is about the wrong person.

### The Ask: Winning Approval

The Ask section is the resource request. Leadership needs to know three things: who you need, how much of their time, and for how long. A vague Ask ("we need engineering and design resources") is not an Ask. It is a wish. A credible Ask names roles, estimates percentage of time, gives a timeline, and flags any change management or infrastructure requirements.

An Ask that is too small under-allocates and sets the project up to slip. An Ask that is too large lacks credibility. Calibrate to the scope of what the canvas describes.

### Loose Coupling to Upstream Plays

This skill draws from six upstream plays. Every field on the canvas can be populated from an upstream play artifact or from direct input, whichever the PM has available. The skill never blocks a field because an upstream play has not been run. If the PM has a problem statement from a workshop, a spreadsheet, or a prior document, that input is as valid as a ps-framing-the-problem output.

The upstream plays and their contributions:

| Canvas Field | Primary Upstream Source |
|---|---|
| Problem Statement | ps-framing-the-problem |
| Solution Summary | ps-solution-hypothesis |
| Positioning Statement | ps-positioning-statement |
| Business Outcomes, Product Outcomes, Metrics | ps-outcome-tree |
| Risks | ps-risk-assessment |
| Stories | ps-proto-persona (for persona context) |

If an upstream play has not been run, offer to run it before filling the field. If the PM has equivalent input from another source, accept it and proceed.

### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **reviewer of the canvas before the Go/No Go decision**. It checks that each section is consistent with the upstream work it summarizes, that the user and buyer stories are grounded, that outcomes and metrics are measurable, and that the Ask is specific. Every claim on the canvas must come from the PM's work, because leadership will decide on it.

- **Use it when:** the PM has assembled the canvas from upstream artifacts and wants it reviewed before presenting it.
- **Avoid it when:** the upstream work doesn't exist yet. A canvas assembled from guesses becomes a Go decision on a guess.
- **Return:** inconsistencies between sections flagged, stories checked against evidence, outcomes and metrics checked for measurability, and the Ask sharpened into a specific decision and resource request.

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

- all three sections completed
- stories written in close-third or first-person with a concrete time anchor
- The Ask specifies roles, percentages, and a timeline
- Risks are named specifically (top 3 from the risk assessment)
- no generic placeholders left in any field
- explanation belongs below the artifact, not inside the fields

### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

### Step 1: Tech-Role Bias Guard

Before writing any content, confirm who the product serves.

Most products serve people who do not write code: clinicians, logistics coordinators, field technicians, operations managers, procurement analysts, regulatory leads. LLMs default to developer/engineer protagonists when context is thin. The stories in this canvas will be wrong if the protagonist is a software engineer when the product serves a supply chain manager.

Ask the PM: "Who is the primary user of this product in the field? What is their job title? What does their day look like before this product exists?"

Use the answer to anchor both stories. If the PM cannot answer this question, offer to run ps-proto-persona before proceeding.

### Step 2: Gather Upstream Artifacts

Ask the PM which of the following artifacts are available:

- Problem Statement (from ps-framing-the-problem or equivalent)
- Solution Summary or hypothesis (from ps-solution-hypothesis or equivalent)
- Positioning Statement (from ps-positioning-statement or equivalent)
- Business Outcomes, Product Outcomes, and Metrics (from ps-outcome-tree or equivalent)
- Risk Assessment (from ps-risk-assessment or equivalent)
- Persona descriptions (from ps-proto-persona or equivalent, for story context)

For each artifact that is not available, offer to run the corresponding skill or ask the PM to provide the information directly. Do not invent content for any field. If a field must be left incomplete, mark it clearly and note what is needed to complete it.

### Step 3: Complete Core Information

Capture:

- Product Name (the actual product name, not a placeholder)
- Date (today's date, or the date of the Go/No Go session)
- Product Manager (the PM's name and role)
- Version (start at v1.0 unless the PM specifies otherwise)

### Step 4: Write the Problem Statement

Use the final Problem Statement from ps-framing-the-problem if available. If not, ask the PM to describe the problem in 2-4 sentences covering: who is affected, what they are trying to do, what is blocking them, and why it matters to the business.

Do not write a problem statement that contains solution language. The problem statement describes the current state, not the desired future state.

Target: 40-60 words.

### Step 5: Write the Solution Summary

Use the If/Then hypothesis format from ps-solution-hypothesis if available.

If not, ask the PM: "In one or two sentences, what does this product do and what does it enable the customer to do that they cannot do today?"

The Solution Summary describes the proposed solution at a level of specificity that makes the concept clear: specific enough to be meaningful, general enough not to lock in implementation details.

Target: 30-50 words.

### Step 6: Write the Positioning Statement

Use the seven-element Positioning Statement from ps-positioning-statement if available. The seven elements are: For (target customer), Who (need or opportunity), The (product name), Is a (product category), That (key benefit), Unlike (primary competitive alternative), Our product gives (primary differentiation).

If the upstream artifact is not available, ask the PM to provide the positioning elements directly and assemble them using the formula.

Target: 50-70 words.

### Step 7: Write Story 1 (User Persona)

Story 1 uses the user persona: the person who uses the product directly in the field.

Write a 2-4 sentence close-third or first-person narrative that anchors to a specific moment. Use a concrete time anchor ("Six weeks after the launch of X, Priya...") to make the story feel real. Show life before and after the product, or show a specific moment where the product makes a critical difference.

The story should make the problem tangible and the solution credible: not by listing features, but by showing the customer's experience.

Do not use the PM or the product team as the protagonist. Do not write a story about building, shipping, or configuring the product.

Target: 50-80 words.

### Step 8: Write Story 2 (Buyer Persona)

Story 2 uses the buyer persona: the person who approves or funds the product, which may be a manager, director, procurement lead, or executive sponsor.

Use the same format as Story 1 but from the buyer's perspective. The buyer's story often centers on visibility, accountability, risk reduction, or efficiency rather than day-to-day task completion.

If no distinct buyer persona has been defined, ask whether the user and buyer are the same person. If so, note this in the artifact and write a single extended story, or ask the PM whether to differentiate.

Target: 50-80 words.

### Step 9: Complete Project Boundaries (Outcomes and Metrics)

Use the ps-outcome-tree output if available. Populate:

- Business Outcomes: what the business gains from the product's success (revenue, efficiency, compliance, retention)
- Product Outcomes: what the customer achieves through using the product (role-based, not persona-named)
- Business Success Metrics: 2-3 measurable business-level indicators
- Product Success Metrics: 2-3 measurable product-level indicators

If the outcome tree has not been run, ask the PM to provide the outcomes and metrics directly. Outcomes must use outcome language (not feature language). Metrics must be specific and measurable: not "improve NPS" but "NPS increases from 32 to 45 within 12 months of launch."

Targets: Business Outcomes 15-25 words; Product Outcomes 15-25 words (bulleted); Metrics 2-3 items at 10-15 words each.

### Step 10: List Key Features

List the top 3-5 features of the proposed solution. These are the capabilities the product will have: what it does, not what the customer achieves. Keep each item short and paste-ready.

Key Features are not outcomes. "Real-time shipment tracking dashboard" is a feature. "Logistics coordinators reduce shipment exception resolution time by 40%" is an outcome.

If the PM has not yet defined features, ask for the top 3-5 things the product will do. Do not infer features from the solution summary or positioning statement without confirmation.

Target: 3-5 bullets at 5-8 words each.

### Step 11: List Top 3 Risks

Use the ps-risk-assessment output if available. Identify the top 3 risks by priority (Critical first) and list their names only. Do not include the full mitigation and contingency plans.

Risk names in the canvas are labels, not plans. The full risk management detail lives in the Risk Assessment artifact. The canvas shows leadership that the team has a risk picture; it does not replace the risk document.

If the risk assessment has not been run, ask the PM to name the 3 most significant threats to success. Use the format: [Risk Type]: [Specific Concern].

Target: 3 items at 5-8 words each.

### Step 12: Write The Ask

The Ask is the resource request for the Create phase. It must include:

- Team composition: roles needed (e.g., Senior Engineer, UX Designer, Data Analyst)
- Time allocation: percentage of each role's time committed to this product
- Timeline: duration of the initial build phase (e.g., "8-week build sprint starting Q3 2026")
- Change management or infrastructure requirements: anything outside standard team capacity

If the PM does not have this information, prompt them with: "To give leadership a concrete Ask, I need to know: what roles do you need, how much of their time, and for how long?" Do not leave The Ask as TBD. It is the reason the canvas is presented.

Target: 30-50 words.

### Step 13: Record the Introduction Date

The Introduction Date is the target launch or release date, meaning when the product reaches customers.

If the PM does not have a specific date, accept a target quarter or milestone ("Q4 2026" or "before annual customer conference in November"). Do not use TBD. If the date is genuinely unknown, flag it and note what decision would unlock it.

Target: 5-10 words.

### Step 14: Offer Next Steps

After delivering the artifact, offer three options:

1. Share the canvas with the leadership sponsor or investment committee for the Go/No Go decision
2. Enter the Create phase by transitioning to build planning, user story mapping, or roadmap work
3. Schedule a structured review session to pressure-test The Ask and the risk picture before presenting

## Template

### When to Use This

Use this template at the **Go/No Go decision point** at the end of the Discover + Define phase, before the team commits to entering the Create (build) phase. Present the completed canvas to your leadership sponsor or investment committee.

Upstream artifacts that feed this template:
- Problem Statement (ps-framing-the-problem or equivalent)
- Solution Summary (ps-solution-hypothesis or equivalent)
- Positioning Statement (ps-positioning-statement or equivalent)
- Business Outcomes, Product Outcomes, and Metrics (ps-outcome-tree or equivalent)
- Top Risks (ps-risk-assessment or equivalent)
- Persona context (ps-proto-persona or equivalent, for story anchoring)

Loose coupling rule: if an upstream artifact is not available, provide the information directly or ask the agent to run the relevant skill before proceeding. No field should be left as TBD in the final canvas.

### Template

```markdown
# Product Outcome Canvas

## Section 1: Core Information

- Product Name:
- Date:
- Product Manager:
- Version:

---

## Section 2: Summary

### Problem Statement

[Describe the customer problem in 2-4 sentences. Who is affected, what are they trying to do, what is blocking them, and why does it matter to the business? No solution language.]

> Quality check: Does the problem statement describe a current state without referencing the proposed solution?
> Quality check: Is the problem specific enough that leadership can picture who is affected and why it matters?
> Capacity check: 40-60 words.

---

### Solution Summary

[Describe the proposed solution in 1-2 sentences using If/Then format where possible. What does the product do, and what does it enable the customer to do that they cannot do today?]

> Quality check: Is the solution summary specific enough to be meaningful but general enough not to lock in implementation details?
> Quality check: Does the solution address the problem statement directly?
> Capacity check: 30-50 words.

---

### Positioning Statement

[Seven-element formula: For [target customer], who [need or opportunity], the [product name] is a [product category] that [key benefit]. Unlike [primary competitive alternative], our product gives [primary differentiation].]

> Quality check: Is the "That" element a benefit (what the customer achieves), not a feature (what the product does)?
> Quality check: Does the "Unlike" element name a real competitive alternative the customer would actually choose?
> Quality check: Does "Our product gives" use outcome language, not feature language?
> Capacity check: 50-70 words.

---

### Story 1: User Persona

[Write a 2-4 sentence close-third or first-person narrative anchored to a specific moment. Use a concrete time anchor ("Six weeks after the launch of X, [Name]..."). Show the customer's experience before and after the product, or show a specific moment where the product makes a critical difference. The protagonist is the customer, not the PM, not the product team.]

Narrative format guide:
- Open with a concrete time anchor and a specific name and role
- Show the specific friction or challenge the customer faces without the product, OR show the moment the product resolves it
- Close with the customer's changed experience or outcome
- Example anchor: "Before ClearRoute launched, Marcos Delgado, a procurement coordinator at a regional hospital network, spent three hours each Monday reconciling delivery confirmations across four supplier portals..."

> Quality check: Is the protagonist the customer or buyer? The PM, an engineer, or a product team member should never be the protagonist.
> Quality check: Does the story make a specific moment tangible rather than describing general benefits?
> Quality check: Is the persona name specific and realistic (not a placeholder like "User A")?
> Capacity check: 50-80 words.

---

### Story 2: Buyer Persona

[Write a 2-4 sentence narrative for the buyer persona: the person who approves or funds the product. Use the same format as Story 1. Buyer stories often center on visibility, accountability, risk reduction, or operational efficiency rather than day-to-day task completion. The protagonist is the buyer, not the PM, not the team.]

> Quality check: Is the buyer persona distinct from the user persona? If they are the same person, note this and adjust the story accordingly.
> Quality check: Does the story reflect a buyer's concern (investment, oversight, outcomes) rather than a user's concern (task completion)?
> Capacity check: 50-80 words.

---

### Key Features

[List the top 3-5 capabilities of the proposed solution. These are what the product does, not what the customer achieves. Short bullets, paste-ready.]

- [Feature 1: ~5-8 words]
- [Feature 2: ~5-8 words]
- [Feature 3: ~5-8 words]
- [Feature 4: ~5-8 words (optional)]
- [Feature 5: ~5-8 words (optional)]

> Quality check: Are these features (capabilities) rather than outcomes (results)? "Real-time exception alerts" is a feature. "40% faster resolution" is an outcome.
> Quality check: Are the features specific to this product rather than generic to any product in the category?
> Capacity check: 3-5 bullets at 5-8 words each.

---

## Section 3: Project Boundaries

### Business Outcomes

[What the business gains from this product's success. Use outcome language: revenue, efficiency, retention, compliance, market position. 1-2 sentences or a compact bulleted list.]

> Quality check: Are these business-level outcomes (what the company gains), not product-level outcomes (what the customer achieves)?
> Quality check: Do the outcomes connect to a measurable business goal?
> Capacity check: 15-25 words.

---

### Product Outcomes

[What the customer/user achieves through using the product. Use role names, not persona names. Bulleted list.]

- [Role] [achievement]: [context or measure]
- [Role] [achievement]: [context or measure]

> Quality check: Do these outcomes use role names (e.g., "logistics coordinators") not persona names (e.g., "Priya")?
> Quality check: Are these outcomes (what the customer achieves) distinct from Key Features (what the product does)?
> Capacity check: 15-25 words total.

---

### Business Success Metrics

[2-3 measurable business-level indicators. Each should be specific enough to track. Include direction, metric, and target where possible.]

- [Metric 1: direction + metric + target, ~10-15 words]
- [Metric 2: direction + metric + target, ~10-15 words]
- [Metric 3: optional, ~10-15 words]

> Quality check: Is each metric specific enough to measure ("NPS increases from 32 to 45 within 12 months") rather than directional only ("improve NPS")?
> Capacity check: 2-3 items at 10-15 words each.

---

### Product Success Metrics

[2-3 measurable product-level indicators. These track customer behavior and product performance, not business-level results.]

- [Metric 1: direction + metric + target, ~10-15 words]
- [Metric 2: direction + metric + target, ~10-15 words]
- [Metric 3: optional, ~10-15 words]

> Quality check: Are these product-level indicators (usage, task completion, error rate) distinct from business success metrics (revenue, retention)?
> Capacity check: 2-3 items at 10-15 words each.

---

### Risks

[Top 3 risks from the Risk Assessment, by priority. Names only; do not include the full mitigation and contingency plans. Format: [Risk Type]: [Specific Concern].]

1. [Risk Name: 5-8 words]
2. [Risk Name: 5-8 words]
3. [Risk Name: 5-8 words]

> Quality check: Are these the highest-priority risks (Critical first) rather than an exhaustive list?
> Quality check: Does each risk name a specific concern, not just a category ("Carrier Data Gaps: top 3 carriers lack real-time API" not "Technical Risk")?
> Capacity check: 3 items at 5-8 words each.

---

### What's Next: The Ask

[Name the resources needed to enter the Create phase: team roles, percentage of time, timeline, and any change management or infrastructure requirements. This must be specific enough for leadership to approve or negotiate.]

Format guide:
- Team: [Role] at [%] time, [Role] at [%] time
- Timeline: [duration and start date or quarter]
- Change management or infrastructure: [any requirements outside standard team capacity]

> Quality check: Does The Ask name specific roles and percentages rather than generic functions ("engineering and design resources")?
> Quality check: Is the timeline specific enough to evaluate (not "TBD" or "as soon as possible")?
> Capacity check: 30-50 words.

---

### Introduction Date

[Target launch or release date: when the product reaches customers. Accept a specific date, a target quarter, or a milestone anchor.]

> Quality check: Is the date specific enough to anchor planning? If TBD, note what decision would unlock it.
> Capacity check: 5-10 words.
```

### Usage Guidance

#### Filling the Template

1. Start with **Section 1: Core Information** to anchor the document.
2. Complete **Section 2: Summary** starting with the Problem Statement, which grounds everything that follows.
3. Write the Positioning Statement before the stories; the positioning clarifies who each story is about.
4. Write the stories last in Section 2, after confirming the persona identities from ps-proto-persona or direct PM input.
5. Complete **Section 3: Project Boundaries** by importing from upstream artifacts wherever possible.
6. Write The Ask after reviewing all other sections; the resource request should reflect the full scope of what the canvas describes.

#### What Goes Where

| Section | Contains | Does NOT Contain |
|---------|----------|-----------------|
| Problem Statement | Customer-facing problem in current state | Solution language, product features |
| Solution Summary | What the product does and enables | Implementation details, technical specs |
| Stories | Customer or buyer experience, specific moments | PM process, team activities, feature lists |
| Key Features | Product capabilities (what it does) | Customer outcomes (what customers achieve) |
| Product Outcomes | What customers achieve (role names) | Persona names, product features |
| The Ask | Roles, percentages, timeline, requirements | Vague functions, TBD timelines |

#### Connecting to Other Skills

- **Upstream:** ps-framing-the-problem (Problem Statement), ps-solution-hypothesis (Solution Summary), ps-positioning-statement (Positioning Statement), ps-outcome-tree (Outcomes and Metrics), ps-risk-assessment (Risks), ps-proto-persona (persona context for stories)
- **Downstream:** Go-to-Market Enablement (Template 20) imports Problem Statement, Positioning Statement, and Key Features

#### Capacity Reference

| Field | Target Length | Guidance |
|-------|--------------|----------|
| Problem Statement | 40-60 words | Describes current state without solution language |
| Solution Summary | 30-50 words | If/Then format where possible |
| Positioning Statement | 50-70 words | Seven-element formula, benefit not feature in "That" |
| Story 1 | 50-80 words | Concrete time anchor, customer protagonist |
| Story 2 | 50-80 words | Buyer protagonist, visibility or accountability focus |
| Key Features | 3-5 bullets, 5-8 words each | Capabilities, not outcomes |
| Business Outcomes | 15-25 words | Business-level, not product-level |
| Product Outcomes | 15-25 words | Role names, not persona names |
| Business Success Metrics | 2-3 items, 10-15 words each | Direction + metric + target |
| Product Success Metrics | 2-3 items, 10-15 words each | Usage and behavior indicators |
| Risks | 3 items, 5-8 words each | Top priority risks, names only |
| The Ask | 30-50 words | Roles + percentages + timeline |
| Introduction Date | 5-10 words | Specific date, quarter, or milestone |

## Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For a hospital bed-coordination concept, consolidate the charge nurse's problem, tested hypothesis, outcomes, evidence, and risks for leadership's Go/No Go decision.
- **Weak:** A persuasive feature pitch without discovery evidence cannot support an informed investment decision.
- **Drift to avoid:** Decision substitution: a polished canvas does not constitute leadership approval or permission to proceed.


## Common Pitfalls

- **Stories About the PM's Process Instead of the Customer's Experience:** The protagonist of every story is the customer or buyer. Read the first sentence of each story. If the subject is a PM, a designer, a developer, or a team, rewrite it. The story must anchor to the customer's day and the customer's experience.

- **Listing Every Risk Instead of the Top Three:** The canvas shows the top 3 risks by priority. Accept-priority risks belong in the full Risk Assessment artifact, not on the canvas. The canvas is a summary, not a transcript of the assessment.

- **The Ask Is Too Vague:** The Ask names specific roles ("2 Senior Engineers, 1 UX Designer, 1 Data Analyst at 80% time"), gives a percentage allocation, and names a timeline. If this information is not yet available, the canvas is premature. Run the planning work before presenting.

- **Treating the Canvas as a One-Time Artifact:** Treat the canvas as a living document. Update the Version number and Date when outcomes shift, risks change, or The Ask needs revision. The canvas should reflect the current state of the product investment, not just its initial framing.

- **Using Generic Placeholder Persona Names in Stories:** Use a specific, realistic name that reflects the persona's role and demographic diversity. Pair the name with a concrete job title and situation. "Priya Nair, a logistics coordinator at a mid-market distribution company, spends the first two hours of every morning..." is credible. "The user opens the dashboard..." is not.

- **Filling the Canvas Without Any Upstream Artifacts:** Before drafting any field, ask for the upstream artifacts or equivalent direct input. If no artifacts exist, flag the gap and offer to run the relevant upstream skill. Never invent the content of a field that is supposed to come from customer research or team validation.

- **Tech-Role Bias in the Customer Stories:** Run the tech-role bias guard in Step 1 before writing any content. Confirm the customer's job title and daily workflow. If the product serves non-technical users, the story must reflect non-technical concerns: task completion, time, accuracy, confidence, and visibility rather than system architecture or code quality.

- **Confusing Key Features with Product Outcomes:** Key Features are capabilities (what the product does). Product Outcomes are results (what the customer achieves). Each field serves a different purpose. If the same content appears in both sections, one of them is wrong.

- **A Canvas Built From Nothing:** Assemble the canvas only from upstream artifacts. Mark any section with no source as a gap, and say which play fills it.

## References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-product-outcome-canvas) for supporting source material and expanded examples.
