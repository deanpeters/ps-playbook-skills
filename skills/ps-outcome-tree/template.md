# Outcome Tree - Section One

## When to Use This

Use this template during the **Context** phase to connect your product work to a measurable business goal. This is foundational: until you can articulate what the business is trying to achieve and how the product supports that, prioritization and roadmap decisions lack an anchor.

Revisit this artifact regularly. Bring it to team meetings. Use it to share success metrics and check assumptions with the team.

## Template

```markdown
# Outcome Tree - Section One

## Product Context

- Product or service:
- Business or organization:
- Primary customer/user role:
- Buyer (if different):

## Problem Statement (from Framing the Problem play, if available)

> [Paste or summarize the problem statement here, or note "Not yet defined"]

## 1. Business Outcome

What is the business trying to achieve? Write a specific, measurable business outcome.

| Business Outcome |
|------------------|
| |

> Quality check: Is this a business-level goal, not a product feature?
> Quality check: Does it include a direction and a metric (even if approximate)?
> Quality check: Could you tell if it happened?

## 2. Business Success Metrics

How does the business measure progress toward the business outcome?

| # | Business Success Metric | Status |
|---|------------------------|--------|
| 1 | | Defined / TBD |
| 2 | | Defined / TBD |
| 3 | | Defined / TBD |

> Quality check: Are these metrics owned by or visible to business leadership?
> Quality check: Are they measurable (a number, percentage, or rate)?

## 3. Product Outcomes (2-5)

What must the customer/user achieve for the business outcome to follow? Use role names, not persona names.

| # | Product Outcome |
|---|----------------|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |

> Quality check: Does each outcome describe value from the customer's perspective?
> Quality check: Is each outcome distinct from the business outcome? (Product outcomes are customer-level, not business-level.)
> Quality check: Have you avoided feature descriptions? ("Self-service portal" is a feature, not an outcome.)
> Quality check: Do you have between 2 and 5 product outcomes? No more than 5.
> Quality check: Do the product outcomes use role names (e.g., "HR managers"), not individual persona names (e.g., "Maya")?
> Capacity check: Product outcome statements should be ~15-20 words.

## 4. Product Success Metrics

How do you measure whether each product outcome is being achieved?

| # | Product Success Metric | Related Outcome | Status |
|---|----------------------|-----------------|--------|
| 1 | | | Defined / TBD |
| 2 | | | Defined / TBD |
| 3 | | | Defined / TBD |
| 4 | | | Defined / TBD |
| 5 | | | Defined / TBD |

> Quality check: Are these leading indicators that the product team can measure?
> Quality check: Is each metric tied to a specific product outcome?
> Quality check: Are these about outcome achievement, not product health? (Uptime is health, not success.)

## 5. Product Health Metrics

How do you measure whether the product itself is working correctly?

| # | Product Health Metric | Target |
|---|---------------------|--------|
| 1 | | |
| 2 | | |
| 3 | | |

> Quality check: Are these operational metrics (uptime, performance, error rates, adoption)?
> Quality check: Are they separate from product success metrics?

## Solution Summary (from Solution Hypothesis Statement play, if available)

> [Paste or summarize the solution hypothesis here, or note "Not yet defined"]

## Causal Chain Review

- Do the product outcomes collectively support the business outcome?
- Are there gaps in the chain?
- Are any product outcomes actually business outcomes in disguise?
- Are any product outcomes actually features?

## Notes (optional)

- Metrics that need further definition:
- Assumptions to validate:
- Cross-references to resolve:
```

## Usage Guidance

### Filling the Template

1. Start with **Product Context** to anchor who this is for.
2. Add the **Problem Statement** if one exists from previous work.
3. Define the **Business Outcome** first. Everything else flows from it.
4. Add **Business Success Metrics** (even if some are TBD).
5. Define **Product Outcomes** (2-5). These describe what the customer achieves.
6. Add **Product Success Metrics** for each product outcome.
7. Add **Product Health Metrics** for the product itself.
8. Add the **Solution Summary** if one exists.
9. Walk through the **Causal Chain Review** to verify connections.

### How Many Product Outcomes

The playbook sets a hard limit of 2-5. Default to 2-3 for a focused product. Use 4-5 only when the product serves multiple distinct user roles or the business outcome is broad enough to require multiple paths.

If you find yourself writing more than 5, either:

- consolidate related outcomes into a single, broader outcome
- split into multiple trees, each with a different business outcome

### What Goes in the Product Outcome Statements

Write each product outcome as a statement about the customer's improved state. Use role names (e.g., "HR managers," "field technicians," "compliance officers"), not individual persona names (e.g., "Maya," "Carlos").

Do not use:

- feature descriptions ("The product provides...")
- implementation details ("Automated workflow for...")
- business metrics ("Revenue increases by...")
- internal team goals ("The engineering team ships...")

### Connecting to Other Skills

- **Upstream:** ps-framing-the-problem provides the Problem Statement; ps-solution-hypothesis provides the Solution Summary
- **Parallel:** ps-jobs-to-be-done produces product outcomes that may feed into this tree
- **Downstream:** Section Two (this skill, Modality 2) updates the tree after discovery and define work

---

## Section Two: Updating the Outcome Tree After Discovery

Use this scaffold when returning to the Outcome Tree after completing discovery work. This is not a new artifact. It is an update pass on the Section One artifact above.

### Prerequisites

Before running Section Two, the PM should have completed at least one of:

- empathy interviews (ps-empathy-interviews)
- solution hypothesis validation (ps-solution-hypothesis)
- lo-fi experimentation (ps-lofi-experimentation)
- market or customer research
- post-launch measurement data

### Update Scaffold

For each section of the Section One artifact, walk through:

```markdown
## Section Two: Outcome Tree Update

Date of update:
Discovery activities completed since Section One:

### Product Outcome Review

| # | Original Product Outcome | Status | Revised Product Outcome (if changed) | Evidence |
|---|-------------------------|--------|--------------------------------------|----------|
| 1 | [from Section One] | Validated / Invalidated / Revised / New | [updated text or "unchanged"] | [what discovery revealed] |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

> Quality check: Is each status decision backed by specific evidence, not intuition?
> Quality check: Are you still within 2-5 product outcomes after revisions?
> Quality check: Did you retire outcomes that discovery invalidated rather than keeping them "just in case"?

### Metrics Update

| Metric Type | Metric | Baseline | Target | Actual (if post-launch) | Status Change |
|-------------|--------|----------|--------|------------------------|---------------|
| Business Success | | | | | Was TBD, now Defined / Unchanged / Revised |
| Product Success | | | | | |
| Product Health | | | | | |

> Quality check: Have all TBD metrics from Section One been resolved or explicitly deferred with a reason?
> Quality check: Are baselines grounded in real data, not estimates?

### Causal Chain Reassessment

- Which links in the chain did discovery strengthen?
- Which links did discovery weaken or break?
- Are there new gaps that Section One missed?

### Changes Summary

- Product outcomes added:
- Product outcomes retired:
- Product outcomes revised:
- Metrics defined (were TBD):
- Metrics revised:
```

### When to Run Section Two

Section Two adds value when the PM has new evidence that changes the tree. Common triggers:

- Completed empathy interviews revealed different customer priorities than assumed
- Solution hypothesis testing invalidated an assumed product outcome
- Market research shifted the competitive context
- Post-launch data shows actual vs. planned variance
- Business strategy changed, altering the business outcome or its metrics

Section Two does not add value when:

- The PM has not done discovery work since Section One (the tree will not change)
- The only change is cosmetic rewording (edit the Section One artifact directly)

### Capacity Reference

See [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml) for the exact word and character budgets per field.

| Field | Word Budget | Guidance |
|-------|-------------|----------|
| Business Outcome | ~15-25 | Specific, measurable business goal |
| Business Success Metric | ~10-15 | Measurable indicator with units |
| Product Outcome | ~15-20 | Customer-centered value statement |
| Product Success Metric | ~10-15 | Leading indicator tied to an outcome |
| Product Health Metric | ~5-10 | Operational metric with target |
