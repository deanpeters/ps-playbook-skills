# Product Outcome Canvas

## When to Use This

Use this template at the **Go/No Go decision point** at the end of the Discover + Define phase, before the team commits to entering the Create (build) phase. Present the completed canvas to your leadership sponsor or investment committee.

Upstream artifacts that feed this template:
- Problem Statement (ps-framing-the-problem or equivalent)
- Solution Summary (ps-solution-hypothesis or equivalent)
- Positioning Statement (ps-positioning-statement or equivalent)
- Business Outcomes, Product Outcomes, and Metrics (ps-outcome-tree or equivalent)
- Top Risks (ps-risk-assessment or equivalent)
- Persona context (ps-proto-persona or equivalent, for story anchoring)

Loose coupling rule: if an upstream artifact is not available, provide the information directly or ask the agent to run the relevant skill before proceeding. No field should be left as TBD in the final canvas.

## Template

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

## Usage Guidance

### Filling the Template

1. Start with **Section 1: Core Information** to anchor the document.
2. Complete **Section 2: Summary** starting with the Problem Statement, which grounds everything that follows.
3. Write the Positioning Statement before the stories; the positioning clarifies who each story is about.
4. Write the stories last in Section 2, after confirming the persona identities from ps-proto-persona or direct PM input.
5. Complete **Section 3: Project Boundaries** by importing from upstream artifacts wherever possible.
6. Write The Ask after reviewing all other sections; the resource request should reflect the full scope of what the canvas describes.

### What Goes Where

| Section | Contains | Does NOT Contain |
|---------|----------|-----------------|
| Problem Statement | Customer-facing problem in current state | Solution language, product features |
| Solution Summary | What the product does and enables | Implementation details, technical specs |
| Stories | Customer or buyer experience, specific moments | PM process, team activities, feature lists |
| Key Features | Product capabilities (what it does) | Customer outcomes (what customers achieve) |
| Product Outcomes | What customers achieve (role names) | Persona names, product features |
| The Ask | Roles, percentages, timeline, requirements | Vague functions, TBD timelines |

### Connecting to Other Skills

- **Upstream:** ps-framing-the-problem (Problem Statement), ps-solution-hypothesis (Solution Summary), ps-positioning-statement (Positioning Statement), ps-outcome-tree (Outcomes and Metrics), ps-risk-assessment (Risks), ps-proto-persona (persona context for stories)
- **Downstream:** Go-to-Market Enablement (Template 20) imports Problem Statement, Positioning Statement, and Key Features

### Capacity Reference

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
