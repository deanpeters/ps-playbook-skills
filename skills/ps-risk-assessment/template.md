# Risk Assessment

## When to Use This

Use this template during **Discover + Define** after completing your solution hypothesis and before committing to a build plan. Run it as a collaborative session with your project manager and relevant stakeholders.

Upstream artifacts that feed this template:
- Solution hypothesis (ps-solution-hypothesis): defines what is being built and what must be true for it to succeed
- Problem framing (ps-framing-the-problem): provides customer and context grounding for adoption risks
- Stakeholder Alignment artifact (if available): helps identify Points of Contact for each risk

## Template

```markdown
# Risk Assessment

## Product Context

- Product or initiative:
- Stage (discovery, build, pre-launch, post-launch):
- Session participants:
- Date of assessment:

---

## Section 1: Identify Risks

Brainstorm the risks that could impact the success of this product or initiative.
Aim for exactly six. Cover adoption, technical, organizational, market, compliance, and resource categories.

| # | Risk Name | Risk Raised By |
|---|-----------|----------------|
| 01 | | |
| 02 | | |
| 03 | | |
| 04 | | |
| 05 | | |
| 06 | | |

> Quality check: Does each Risk Name name a specific concern, not a category? ("Workflow Disruption: clinicians resist new documentation steps" not "User Resistance")
> Quality check: Are risks spread across at least three distinct categories (adoption, technical, organizational, market, compliance, resource)?
> Quality check: Is each Risk Raised By a specific person, not a team or function?
> Capacity check: Risk Name should be ~5-8 words.

---

## Section 2: Plot Level of Risk

For each risk, classify Impact Severity and Occurrence Probability, then derive Priority.

Impact Severity: How severely would this affect the business or product outcome if it occurred? (High / Medium / Low)
Occurrence Probability: How likely is it to occur given what we know? (High / Medium / Low)

Priority guide:
- High Impact + High or Medium Probability = Critical
- High Impact + Low Probability = Monitor
- Medium Impact + High Probability = Critical
- Medium Impact + Medium Probability = Manage
- Medium Impact + Low Probability = Accept
- Low Impact + any Probability = Manage or Accept

---

Risk 01: [Risk Name]
  Impact Severity: [High / Medium / Low]
  Occurrence Probability: [High / Medium / Low]
  Priority: [Critical / Monitor / Manage / Accept]

Risk 02: [Risk Name]
  Impact Severity: [High / Medium / Low]
  Occurrence Probability: [High / Medium / Low]
  Priority: [Critical / Monitor / Manage / Accept]

Risk 03: [Risk Name]
  Impact Severity: [High / Medium / Low]
  Occurrence Probability: [High / Medium / Low]
  Priority: [Critical / Monitor / Manage / Accept]

Risk 04: [Risk Name]
  Impact Severity: [High / Medium / Low]
  Occurrence Probability: [High / Medium / Low]
  Priority: [Critical / Monitor / Manage / Accept]

Risk 05: [Risk Name]
  Impact Severity: [High / Medium / Low]
  Occurrence Probability: [High / Medium / Low]
  Priority: [Critical / Monitor / Manage / Accept]

Risk 06: [Risk Name]
  Impact Severity: [High / Medium / Low]
  Occurrence Probability: [High / Medium / Low]
  Priority: [Critical / Monitor / Manage / Accept]

---

> Quality check: Are priorities meaningfully differentiated? Not every risk should be Critical.
> Quality check: Is Impact Severity rated on business impact, not team inconvenience?
> Quality check: Are Critical risks clearly more urgent than Monitor or Manage risks?

---

## Section 3: Begin Risk Management

Complete this table for all Critical-priority risks. Include Monitor-priority risks if capacity allows.
Accept-priority risks may be listed without management rows.

| Risk Name | Mitigation Tactics | Contingency Plans | Point of Contact | Notes |
|-----------|-------------------|-------------------|------------------|-------|
| | | | | |
| | | | | |
| | | | | |

> Quality check: Is each Mitigation Tactic a specific proactive action that reduces the chance the risk occurs? ("Run pilot with 10 early adopters before full rollout" not "test more thoroughly")
> Quality check: Is each Contingency Plan a specific reactive response for if the risk occurs despite mitigation? ("Halt rollout and reconvene with adoption lead within 5 business days" not "communicate better")
> Quality check: Are Mitigation and Contingency clearly distinct from each other for every row?
> Quality check: Is each Point of Contact a named individual, not a team or role?
> Capacity check: Mitigation Tactics ~15-25 words; Contingency Plans ~15-25 words; Notes ~10-20 words.

---

## Revisit Note

Mark at least one future decision point where this assessment will be reviewed and updated:

- Next scheduled review:
- Trigger for unscheduled review (e.g., "if competitive landscape changes" or "at first major build decision"):
```

## Usage Guidance

### Filling the Template

1. Complete **Product Context** to anchor who is in the room and what stage the product is at.
2. Work through **Section 1** as a group. Push for specificity in Risk Names and for breadth across categories.
3. Complete **Section 2** risk by risk. Differentiate priorities. Resist the urge to rate everything Critical.
4. Complete **Section 3** starting with the highest-priority risks. Mitigation before contingency for each row.
5. Add the **Revisit Note** before closing the session.

### What Goes Where

| Column | Contains | Does NOT Contain |
|--------|----------|------------------|
| Risk Name | Type + specific concern | Generic category labels |
| Risk Raised By | Named individual | "Team" or "Stakeholders" |
| Impact Severity | Business impact rating | Team inconvenience rating |
| Mitigation Tactics | Proactive prevention actions | Responses to the risk occurring |
| Contingency Plans | Reactive response if risk occurs | Duplicate of mitigation |
| Point of Contact | Named accountable individual | Team, function, or role title |

### Connecting to Other Skills

- **Upstream:** ps-solution-hypothesis provides the solution context that grounds the risk identification. ps-framing-the-problem provides the customer and problem context.
- **Downstream:** ps-product-outcome-canvas (Batch 5) draws the risk summary from this assessment. ps-lofi-experimentation can convert high-priority testable assumptions from this assessment into structured experiments.

### Capacity Reference

| Field | Target Length | Guidance |
|-------|--------------|----------|
| Risk Name | 5-8 words | Type label plus specific concern |
| Risk Raised By | 2-3 words | First name and last name or role |
| Mitigation Tactics | 15-25 words | Specific proactive action |
| Contingency Plans | 15-25 words | Specific reactive response |
| Notes | 10-20 words | Timing, dependencies, escalation |
