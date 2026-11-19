# Lo-fi Experimentation

## When to Use This

Use this template during **Discover + Define** when you have a proposed solution direction (ideally from ps-solution-hypothesis) and need to validate the riskiest assumption about it before committing to build.

Upstream work that feeds this template: ps-solution-hypothesis (the If/Then hypothesis to stress-test), ps-framing-the-problem (the validated problem statement), ps-exploring-solution-space (the solution method selected).

This template produces a commitment artifact. By the time you complete it, you have identified what you believe, designed a test, and committed to acting on the results regardless of outcome.

## Template

```markdown
# Lo-fi Experimentation

## Product Context

- Product or service:
- Proposed solution direction:
- Primary customer (the person whose assumption we are testing):

## 1. Key Assumptions

Work with your cross-functional team to list the assumptions that must be true for your solution to create value for the customer and return value to the business. Draft them yourselves first. Keep the two that are make-or-break, about behavior or sentiment, and testable this week.

**Assumption 1:**


> Quality check: If this assumption is false, does the solution approach change significantly? (If not, this is not make-or-break.)
> Quality check: Is this about customer behavior, feeling, or belief - not an internal technical capability?
> Quality check: Can a test produce a clear result within days, not months?
> Capacity check: ~25-40 words.

**Assumption 2:**


> Quality check: Same three tests as Assumption 1.
> Quality check: Is this assumption distinct from Assumption 1, not a restatement?
> Capacity check: ~25-40 words.

## Finish Line (decide before designing)

- Riskiest assumption (Assumption 1 or 2), and why it is riskiest (likelihood of being wrong x cost if wrong):
- Decision this test will inform (what we will do differently based on the result):
- Done: the behavior a pass requires, from how many people:
- What failure looks like:

> Quality check: If you cannot name the decision, the test is not worth running yet.

## 2. Hypothesis Statement

Select one assumption to test first. State which one and why (highest impact on the decision, lowest effort to stage, fastest time to a clear signal).

**Testing Assumption [1 or 2] because:**


**Hypothesis:**

If we [describe the specific stimulus or test we will run],

then [describe the specific, observable, measurable result we expect to see, including a numeric threshold or behavioral indicator].


> Quality check: Does the IF describe a test this week, not a fully built solution?
> Quality check: Does the THEN include a specific number or observable behavior - not "users will prefer it" or "adoption will improve"?
> Quality check: Could this hypothesis be clearly falsified if the threshold is not met?
> Capacity check: ~30-45 words for the full If/Then statement.

## 3. Design Experiment

Describe the smallest thing you will build or stage to test the hypothesis. Include all five elements.

**Method:**
(Specify the lo-fi approach: clickable prototype, Wizard-of-Oz, Concierge, Explainer Video, landing page, paper prototype, price sheet, ad concept, or a named equivalent.)


> Quality check: Is this the smallest method that generates a clear signal? If staging this requires multiple sprints of engineering, choose a lighter approach.

**Audience:**
(Who will participate and how they will be recruited: role title, number of participants, recruitment source.)


> Quality check: Is this the actual target customer, not a convenient internal proxy?
> Quality check: Are these real people? Simulated or synthetic participants produce no customer evidence.

**Metric(s):**
(The specific observable, countable thing to measure.)


> Quality check: Can this metric be observed and counted without subjective interpretation?
> Quality check: Is this tied directly to the hypothesis threshold?

**Time Window:**
(Start date and end date or duration.)


**Decision Rule:**

- [Threshold A] or above: continue as planned
- [Threshold B] to [Threshold A minus 1]: adjust - [specify what changes]
- Below [Threshold B]: pivot - [specify what the pivot means for the solution direction]

> Quality check: Do the three tiers create genuine decision points? A decision rule where all three tiers lead to "continue" is not a decision rule.
> Quality check: Is the pivot tier specific enough that the team knows what to do, not just "reconsider"?

## 4. Experiment Description

Describe what will be shown, said, or demonstrated. Include the stimulus (mockup description, script, ad copy, price sheet text), the core wording the customer will encounter, and any task prompts or scenarios.

Provide enough detail that someone could run this experiment without redesigning it from scratch.


> Quality check: Would someone unfamiliar with the solution be able to run this experiment from this description alone?
> Quality check: Does the description include both the stimulus and the task or question the participant is responding to?
> Capacity check: ~100-150 words.

## Evidence Notes (optional)

- Upstream artifacts used:
- What assumption remains untested after this experiment:
- Recommended next experiment:
- Open risks not addressed by this experiment:
```

## Usage Guidance

### Filling the Template

1. Start with **Product Context** to anchor whose assumption is being tested and which solution direction is under examination.
2. Write **both Key Assumptions** yourselves before selecting one to test. The act of writing both helps identify which is more critical.
3. Fill in the **Finish Line**: choose the riskiest assumption and say why, name the decision the test informs, and define what a pass and a failure look like. Do not imply the selection.
4. Write the **Hypothesis Statement** with a specific threshold before designing the experiment. The threshold drives the metric selection in section 3.
5. Complete all five **Design Experiment** elements. The Decision Rule is required, not optional.
6. Write the **Experiment Description** specific enough to run. This is the field that most often gets left vague.
7. Add **Evidence Notes** only after the artifact is fully complete.

### What Goes Where

| Section | Contains | Does NOT Contain |
|---------|----------|------------------|
| Key Assumptions | Make-or-break customer behavior or sentiment beliefs | Technical feasibility questions, feature specifications, team preferences |
| Hypothesis Statement | Specific test description + measurable threshold | Full solution description, vague improvement language |
| Design Experiment | Method, Audience, Metric, Time Window, Decision Rule (all five) | General approach without specifics, metric without threshold |
| Experiment Description | Runnable stimulus and task prompts | Marketing pitch, comprehensive product spec |

### Connecting to Other Skills

- **Upstream:** ps-solution-hypothesis provides the If/Then chain that surfaces the assumptions most worth testing. ps-framing-the-problem provides the validated problem that grounds the solution direction.
- **Downstream:** Results from the experiment feed ps-risk-assessment (once the critical assumption is validated, risks become clearer). ps-product-outcome-canvas (Template 16) draws from a validated solution direction.

### Capacity Reference

| Field | Guidance |
|-------|----------|
| Each Key Assumption | ~25-40 words |
| Hypothesis Statement | ~30-45 words for the If/Then |
| Method | 1-2 sentences |
| Audience | 1-2 sentences including role, number, source |
| Metric(s) | 1 sentence with the specific measure |
| Time Window | Start and end or duration |
| Decision Rule | Three tiers, each with a threshold and action |
| Experiment Description | ~100-150 words |
