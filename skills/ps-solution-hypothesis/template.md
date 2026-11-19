# Solution Hypothesis Statement

## When to Use This

Use this template during **Discover + Define** when you have a validated problem statement and have explored the solution space. You are ready to express your chosen solution direction as a testable hypothesis with expected customer and business outcomes.

Upstream work that feeds this template: framing the problem (ps-framing-the-problem), exploring the solution space (ps-exploring-solution-space), positioning statement (ps-positioning-statement, if available).

## Template

```markdown
# Solution Hypothesis Statement

## Product Context

- Product or service:
- Target market segment:
- Primary customer (the person who uses or buys the product):

## 1. Problem Statement

Import from your Framing the Problem output. Do not rewrite.


> Quality check: Is this a validated problem statement, or an assumption? If it is an assumption, flag it.
> Quality check: Is the problem written from the customer's perspective, not the product team's?
> Capacity check: ~40-50 words (matching the final problem statement from ps-framing-the-problem).

## 2. Solution Summary

Describe the proposed solution in one paragraph. What does the solution provide to the customer?


> Quality check: Is this specific enough to be testable? "Build a better platform" is not testable.
> Quality check: Does the summary describe what the solution does for the customer, not how it is built?
> Quality check: Is there a clear connection between this solution and the problem statement above?
> Capacity check: ~30-40 words.

## 3. Solution Benefits

List 3-5 specific benefits. Each benefit should describe an outcome, not a feature.

-
-
-
-

> Quality check: Does each benefit answer "so what?" or does it just describe a capability?
> Quality check: Are there both customer-facing and business-facing benefits in the list?
> Quality check: Do benefits use role names ("HR specialists"), not persona names ("Henry")?
> Capacity check: ~5-10 words per benefit, 3-5 benefits.

## 4. Risks and Assumptions

List 3-5 specific risks or assumptions that need to be validated.

-
-
-
-

> Quality check: Is each risk specific enough to investigate? "Things might go wrong" is not specific.
> Quality check: Are these risks relevant to this solution, not generic business risks?
> Quality check: Could the team design a test or investigation for each risk?
> Capacity check: ~5-10 words per risk, 3-5 risks.

## 5. Solution Hypothesis Statement

### Customer-Focused Hypothesis

IF we [describe what the solution provides to customers],
THEN [describe the specific benefit customers experience].


### Business-Focused Hypothesis

IF we [restate the customer benefit from above],
THEN [describe the measurable business outcome].


> Quality check: Does the THEN of the customer-focused hypothesis match the IF of the business-focused hypothesis? This chain must connect.
> Quality check: Is the customer-focused hypothesis about customer value, not business metrics?
> Quality check: Is the business-focused hypothesis about a measurable business outcome, not a vague improvement?
> Quality check: Are both written as If/Then statements, not as feature descriptions?
> Quality check: Do hypotheses use role names, not persona names?
> Capacity check: ~30-40 words per hypothesis.

## Evidence Notes (optional)

- Upstream artifacts used:
- What is well-supported by evidence:
- What is still assumption:
- Recommended next validation steps:
```

## Usage Guidance

### Filling the Template

1. Start with **Product Context** to anchor who this is for and whose problem the solution addresses.
2. **Import the Problem Statement** from ps-framing-the-problem. Do not rewrite it.
3. Write the **Solution Summary** as one paragraph describing what the solution provides.
4. List **Solution Benefits** as outcomes, not features. Push each one past "what it does" to "why it matters."
5. List **Risks and Assumptions** with enough specificity that each one can be investigated.
6. Write the **Customer-Focused Hypothesis** first. Then write the **Business-Focused Hypothesis** using the THEN of the first as the IF of the second.
7. Verify the chain between the two hypotheses.
8. The **Evidence Notes** section is optional and trailing. Do not let it displace or delay the main artifact.

### The Five Sections Build in Order

Do not skip ahead to writing hypotheses without completing the preceding sections. The problem statement grounds the solution. The solution grounds the benefits. The benefits and risks inform the hypothesis. Writing the hypothesis without the groundwork produces untethered speculation.

### What Goes Where

| Section | Contains | Does NOT Contain |
|---------|----------|------------------|
| Problem Statement | Validated problem from upstream | New problem framing or solution language |
| Solution Summary | What the solution provides to customers | Implementation details, architecture, feature specs |
| Solution Benefits | Outcomes for customers and the business | Feature names, capability descriptions |
| Risks and Assumptions | Specific, testable failure modes or beliefs | Generic worries, vague concerns |
| Customer Hypothesis | IF solution THEN customer benefit | Business metrics, revenue targets |
| Business Hypothesis | IF customer benefit THEN business outcome | Feature lists, solution descriptions |

### Connecting to Other Skills

- **Upstream:** ps-framing-the-problem provides the problem statement. ps-exploring-solution-space provides the chosen solution direction. ps-positioning-statement provides framing for how the solution fits the market.
- **Downstream:** The validated hypothesis drives lo-fi experimentation, risk assessment, and roadmap planning. The business outcome in hypothesis 2 should connect to the outcome tree if one exists.

### Capacity Reference

See [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml) for the exact word and character budgets per field.

| Field | Word Budget | Guidance |
|-------|-------------|----------|
| Problem Statement | ~40-50 | Imported from ps-framing-the-problem |
| Solution Summary | ~30-40 | One paragraph, specific and testable |
| Solution Benefits | ~5-10 each | 3-5 outcome statements, not feature names |
| Risks and Assumptions | ~5-10 each | 3-5 specific, testable risks |
| Customer Hypothesis | ~30-40 | IF solution THEN customer benefit |
| Business Hypothesis | ~30-40 | IF customer benefit THEN business outcome |
