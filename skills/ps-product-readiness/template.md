# Product Readiness Testing

## When to Use This

Use this template when preparing a **pre-launch beta program** to validate the product with real customers before market release. This is a Key Decision Point: the results determine whether to launch (Go) or hold (No Go).

Before running this template, confirm that earlier rounds of user testing have occurred. This is the final validation before launch, not the first time users see the product.

Upstream artifacts that feed this template:
- Solution hypothesis (ps-solution-hypothesis): defines what is being validated
- Product success metrics from ps-outcome-tree: provides measurement anchors for the Goals table
- Risk assessment (ps-risk-assessment): surfaces known risks that may define scope limits
- Persona profiles (ps-proto-persona): helps define who to recruit as beta participants

---

## Template

```markdown
# Product Readiness Test Plan

## Product Context

- Product or initiative:
- Stage: Pre-launch beta program
- Date:
- Test Lead (PM):

---

## Section 1: Product Readiness Test Plan

### Who are we testing with (Customer profiles)?

Describe each type of participant. Go beyond job titles: include role, company type, company size, experience level, and what this profile represents in the target market.

- Profile 1:
- Profile 2:
- Profile 3 (if applicable):

> Quality check: Does each profile describe a real-context participant (role, company type, experience level, and what they represent) rather than just a job title?
> Quality check: Do the profiles represent the actual customer population, not internal team members or users who are already familiar with the product?

---

### How many customers will test?

State the total count, broken down by participant type.

Total: [number]
  - [Type 1]: [count] participants
  - [Type 2]: [count] participants (if applicable, e.g., internal cohort for comparison)

> Quality check: Does the breakdown name the participant types and counts, not just a total number?
> Capacity check: 1-2 lines, approximately 10-15 words total.

---

### How long will the test run?

Define the duration in terms of product usage cycles, minimum usage expectations, or task completion. Calendar days alone are not sufficient.

Duration: [time box or cycle definition]
Usage anchor: [one billing cycle / three sessions per week / first end-to-end workflow completed]

> Quality check: Is the duration anchored to something meaningful about how the product is used, not only a calendar window?
> Capacity check: 10-20 words total.

---

### Test team roles and responsibilities

Name a specific individual for each role. If a role is unfilled, flag it as an open assignment before starting the test.

| Role | Name | Responsibility |
|------|------|----------------|
| Test Lead | | Runs the test, owns the schedule, holds the Go/No Go call |
| Account/Client Contact | | Manages participant expectations, scheduling, and relationships |
| Technical Support | | Triages bugs, handles configuration issues, responds to participant technical questions |
| Quote Collector | | Captures memorable participant statements for use in launch communications |

> Quality check: Is each role filled with a named individual, not a team or function?
> Quality check: Is a Technical Support person named? If not, flag it as a risk before starting.
> Quality check: Is a Quote Collector named? This is a deliverable, not optional.

---

## Section 2: Product Readiness Goals

| Goal/Objective | Measure/Metric | Target |
|----------------|----------------|--------|
| [Specific named goal, not "test the product"] | [Named metric: survey score, task completion rate, time-on-task, error count, uptime] | [Numeric or percentage threshold: e.g., 4.2/5 or 70% or 99.5%] |
| | | |
| | | |
| | | |

Suggested goal areas (4-5 rows covering distinct measurement types):
- Row 1: Workload or efficiency (e.g., reduction in time spent on a named task)
- Row 2: User satisfaction or experience (e.g., post-use survey score)
- Row 3: Self-service adoption rate (e.g., task completion without support assistance)
- Row 4: System reliability (e.g., uptime or error rate)
- Row 5: Optional: coverage, volume, or secondary metric

> Quality check: Does every Target cell contain a number or percentage, not a directional aspiration?
> Quality check: Are goals specific and named (e.g., "Confirm the reconciliation workflow can be completed without support") rather than generic ("test usability")?
> Capacity check: Goal/Objective approximately 4-8 words; Measure/Metric approximately 5-12 words; Target approximately 3-8 words.

---

### Pre-Committed Go/No Go Criteria

Complete this section BEFORE running the test.

Must-pass goals (all must be met for a Go decision):
- [Goal name from table above]
- [Goal name from table above]

Aspirational goals (failure does not block Go, but will be flagged and tracked):
- [Goal name from table above]
- [Goal name from table above]

> Quality check: Have the must-pass goals been agreed in writing before the test begins?
> Quality check: Is this section completed before any test results are visible?

---

## Section 3: Assumptions and Risks

What cannot be tested in this program? What assumptions remain open? Be specific about scope limits and why they exist.

- [Scope limit 1: name the constraint and the reason it is out of scope]
- [Scope limit 2]
- [Scope limit 3]
- [Scope limit 4 if applicable]
- [Scope limit 5 if applicable]

> Quality check: Does each bullet name a specific, real constraint rather than a generic acknowledgment that risks exist?
> Quality check: Are there at least 3 specific scope limits named? If the list is empty, the test scope has not been fully examined.
> Capacity check: Each bullet approximately 15-25 words.

---

## Post-Test Go/No Go Call

Complete after the test concludes.

| Must-Pass Goal | Target | Actual Result | Met? |
|----------------|--------|---------------|------|
| | | | Yes / No |
| | | | Yes / No |

**Decision:**
- [ ] Go: all must-pass goals met
- [ ] No Go: one or more must-pass goals not met
- [ ] Conditional Go: [describe condition]

**Decision owner:**
**Date of call:**
**Memorable quotes captured:**
```

## Usage Guidance

### Filling the Template

1. Complete **Product Context** to anchor the product, stage, and test lead.
2. Answer all four **Test Plan questions** with specific content before planning the test logistics.
3. Write the **Goals table** before recruiting participants. The goals define what the test is designed to measure.
4. Complete **Pre-Committed Go/No Go Criteria** before the test begins. This is the most commonly skipped step.
5. Fill the **Assumptions and Risks section** before finalizing participant communication.
6. Return to complete the **Post-Test Go/No Go Call** after results are in.

### What Goes Where

| Section | Contains | Does NOT Contain |
|---------|----------|------------------|
| Customer Profiles | Role + company type + experience level + what they represent | Job titles alone |
| How Many | Total count broken down by participant type | A single total number |
| Test Duration | Usage cycle or task completion anchor | Calendar days alone |
| Test Team Roles | Named individuals with specific functions | "The PM" or "the engineering team" |
| Goal/Objective | Specific named outcome the test confirms | Generic placeholders like "test usability" |
| Target | Number or percentage | Directional aspirations |
| Assumptions and Risks | Specific named scope limits with reasons | Blank or generic acknowledgment |

### Connecting to Other Skills

- **Upstream:** ps-solution-hypothesis (defines what is being validated), ps-outcome-tree (product success metrics), ps-risk-assessment (known risks), ps-proto-persona (who to recruit)
- **Downstream:** Post-launch retrospective; launch communications (customer quotes)
- **Related:** ps-lofi-experimentation (if earlier rounds of user testing have not occurred, use this skill before planning a readiness test)

### Capacity Reference

| Field | Target Length | Guidance |
|-------|--------------|----------|
| Customer Profile bullet | 15-25 words | Role, company type, experience level, what they represent |
| How Many | 10-15 words total | Count broken down by type |
| Test Duration | 10-20 words | Usage cycle or task completion anchor |
| Team role responsibility | 10-15 words per role | Specific function, not generic ownership |
| Goal/Objective | 4-8 words | Named outcome, not a category |
| Measure/Metric | 5-12 words | Named, countable signal |
| Target | 3-8 words | Numeric or percentage threshold |
| Assumptions/Risks bullet | 15-25 words | Named constraint with reason |
