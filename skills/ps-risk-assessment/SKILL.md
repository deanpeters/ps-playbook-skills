---
name: ps-risk-assessment
description: >-
  Identify, prioritize, and plan for product risks in Productside format. Use
  when you need to surface potential threats to product success, classify them
  by severity and likelihood, and build mitigation and contingency plans before
  committing to a build or launch.
intent: >-
  Help a Product Manager and their team proactively surface and manage the risks
  that threaten a product's development and adoption, so that costly surprises
  are predictable checkpoints rather than emergencies.
type: component
blueprint_stage: Discover + Define
best_for:
  - "Identifying potential threats to a product build or launch with your team"
  - "Classifying risks by severity and likelihood on a heat map"
  - "Building specific mitigation and contingency plans for high-priority risks"
scenarios:
  - "We are about to enter development and I need the team to identify what could go wrong"
  - "Help me run a risk assessment session and build mitigation plans for the top threats"
---


## Purpose

Create a **Productside-style Risk Assessment artifact** from a collaborative team review of a product in development.

This skill helps a Product Manager and their project manager identify potential threats to a product build or launch, classify those threats by severity and likelihood, and build specific mitigation and contingency plans for the highest-priority risks.

The point is not to list everything that could go wrong. The point is to help the team complete the play with a prioritized, actionable risk plan.

## Key Concepts

### This Play Is Collaborative, Not Solo

The playbook is explicit: do not run this assessment alone. Partner with your project manager, who can lead the collaborative effort, and involve relevant stakeholders. A solo PM risk list misses organizational, technical, and customer-facing blind spots that surface in a group session.

### Mitigation and Contingency Are Not the Same

Every risk needs two plans, not one:

- **Mitigation Tactics**: what the team does to reduce the chance the risk occurs. These are proactive actions taken before the risk materializes.
- **Contingency Plans**: what the team does if the risk occurs despite mitigation. These are reactive responses to the risk having already happened.

A plan where both columns contain the same kind of content has not done the work.

### Risk Breadth Matters More Than Risk Count

Six risks that are all technical is not a complete assessment. A well-formed risk list covers:

- Customer adoption and behavior change
- Technical implementation and integration
- Organizational readiness and change management
- Market or competitive timing
- Data, privacy, or compliance
- Resource or capacity constraints

### Point of Contact Is the Risk Owner, Not the Task Doer

The Point of Contact is the person accountable for monitoring and managing the risk. This is not necessarily the PM or the person completing the assessment. For adoption risks it may be a change management lead. For technical risks it may be an engineering lead. For compliance risks it may be a legal or security owner.

### Six Is the Canonical Count

The template has six rows in the identification table. Fill all six. Fewer usually means the team has not looked broadly enough.

### Risk Assessment Is a Living Document

The assessment is not a one-time checkpoint. Risks change as the product is built, tested, and launched. At minimum, revisit at the first major build decision.

### Template Capacity Matters

Risk names, mitigation tactics, and contingency plans should be paste-ready for the playbook template. Keep entries specific but compact.

See [Template and capacity guidance](#template) for canonical field budgets.

### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **a widening and pressure-testing partner for the risks the PM's team brainstormed**. It asks whether the list covers enough ground, offers risk categories (and, after the PM answers, candidate risks marked as candidates), and checks that each mitigation, contingency, and owner is real. Severity, likelihood, and the plan stay with the team.

- **Use it when:** the team has brainstormed risks and wants the list widened and the management plan pressure-tested.
- **Avoid it when:** the request is for a finished risk register for a product the team hasn't discussed. The risks that matter are the ones only the team can see.
- **Return:** gaps in breadth named, candidate risks offered as candidates, each mitigation separated from its contingency, and each risk given a real owner.

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

- exactly 6 risks in the identification table
- all three sections completed
- Risk Management rows for at least the 2-3 highest-priority risks
- mitigation and contingency clearly distinct in every row
- no generic risk names like "Technical Risk" or "Market Concerns"
- explanation belongs below the artifact, not inside the fields

### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

### Step 1: Apply Tech-Role Bias Guard

Before starting, ask: is the product being evaluated built for a technical or engineering user? If yes, note it and proceed. If not, flag it as you work - risk lists generated for non-technical customer contexts often cluster around implementation concerns (performance, integration, security) because those are the risks the product team lives with, not the risks the customer faces.

This is especially important for risks in the customer adoption and change management categories. The team running this assessment is not the customer. Risks should span customer-facing failure modes, not just build-side concerns.

### Step 2: Confirm Scope Beyond Technical Risks

Before brainstorming risks, ask the user to consider whether their current thinking is skewed toward engineering concerns. Product teams commonly produce risk lists that are almost entirely technical (performance, integration, security) while missing the risks that most often cause product failures: customer behavior change, organizational resistance, market timing, and adoption barriers.

Prompt the user to think across these categories:

- What adoption or behavior-change risks exist?
- What organizational or change management risks exist?
- What technical or integration risks exist?
- What market or competitive timing risks exist?
- What data, privacy, or compliance risks exist?
- What resource or capacity risks exist?

### Step 3: Collect Available Artifacts

Before drafting, ask whether the user has materials to share:

- Solution hypothesis from ps-solution-hypothesis (defines what is being de-risked)
- Problem framing from ps-framing-the-problem (gives customer and problem context)
- Any early customer feedback or field observations
- Stakeholder concerns surfaced in prior conversations
- A Stakeholder Alignment artifact (useful for identifying Points of Contact)

The more context about what is being built and for whom, the more targeted the risk identification. Also confirm who will participate in the risk review session.

### Step 4: Identify Six Risks

Work with the user to identify exactly six risks. For each, capture:

**Risk Name**: a short label that names the type of risk and the specific concern. Follow the pattern: `[Risk Type]: [Specific Concern]`. Example: "Workflow Disruption: surgeons resist new documentation steps."

**Risk Raised By**: the team member or stakeholder who surfaced this risk during the session.

Spread the six risks across at least three distinct categories. Do not let all six cluster in one area.

### Step 5: Plot Level of Risk

For each of the six risks, classify two dimensions:

**Impact Severity** (if this risk occurs, how severely does it affect the business or product outcome?):
- High: threatens the product goal or business outcome directly
- Medium: causes significant delays, cost increases, or partial goal failure
- Low: creates friction or rework but does not threaten the goal

**Occurrence Probability** (how likely is this to occur given what we know?):
- High: likely without active intervention
- Medium: possible; some conditions that could trigger it exist
- Low: unlikely given current context, but worth tracking

Derive a priority from the combination:

| Impact | Probability | Priority |
|--------|-------------|----------|
| High | High | Critical |
| High | Medium | Critical |
| High | Low | Monitor |
| Medium | High | Critical |
| Medium | Medium | Manage |
| Medium | Low | Accept |
| Low | High | Manage |
| Low | Medium | Accept |
| Low | Low | Accept |

Present the classification as a structured list per risk, not as a visual grid.

### Step 6: Build the Risk Management Table

For each Critical or Monitor priority risk, and optionally for Manage-priority risks, complete the risk management table:

- **Risk Name**: match exactly the name from Step 3
- **Mitigation Tactics**: specific actions that reduce the chance the risk occurs. Not "test more" or "communicate better." What specifically will the team do, when, and with whom?
- **Contingency Plans**: specific response if the risk occurs despite mitigation. What will the team do? Who decides? What is the timeline?
- **Point of Contact**: the named accountable owner for this risk. If no one can be named, that is a signal the risk is unowned.
- **Notes**: timing dependencies, escalation paths, or open questions

At minimum, complete rows for all Critical-priority risks. Leave Accept-priority risks out if needed to keep the artifact focused.

### Step 7: Review the Completed Artifact

Before presenting the artifact, check:

- Do higher-priority risks have stronger, more specific plans than lower-priority ones?
- Is every Contingency Plan clearly different from its paired Mitigation Tactic?
- Is every Point of Contact a named individual, not a team or function?
- Are there risks that are actually testable assumptions? If so, flag them as candidates for ps-lofi-experimentation.
- Are priorities meaningfully differentiated? If everything is Critical, the classification has not done its job.

### Step 8: Flag the Assessment as a Living Document

After delivering the artifact, note that this assessment should be revisited at key decision points. At minimum, flag one specific time to revisit: at the first major build or delivery decision.

### Step 9: Offer Next Steps

At the end of the artifact, offer three options:

1. Convert the most critical testable assumption into a lo-fi experiment using ps-lofi-experimentation
2. Carry the risk summary forward into ps-product-outcome-canvas when that play is run
3. Share the assessment with stakeholders identified in the Risk Raised By column to validate completeness and confirm Points of Contact

## Template

### When to Use This

Use this template during **Discover + Define** after completing your solution hypothesis and before committing to a build plan. Run it as a collaborative session with your project manager and relevant stakeholders.

Upstream artifacts that feed this template:
- Solution hypothesis (ps-solution-hypothesis): defines what is being built and what must be true for it to succeed
- Problem framing (ps-framing-the-problem): provides customer and context grounding for adoption risks
- Stakeholder Alignment artifact (if available): helps identify Points of Contact for each risk

### Template

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

### Usage Guidance

#### Filling the Template

1. Complete **Product Context** to anchor who is in the room and what stage the product is at.
2. Work through **Section 1** as a group. Push for specificity in Risk Names and for breadth across categories.
3. Complete **Section 2** risk by risk. Differentiate priorities. Resist the urge to rate everything Critical.
4. Complete **Section 3** starting with the highest-priority risks. Mitigation before contingency for each row.
5. Add the **Revisit Note** before closing the session.

#### What Goes Where

| Column | Contains | Does NOT Contain |
|--------|----------|------------------|
| Risk Name | Type + specific concern | Generic category labels |
| Risk Raised By | Named individual | "Team" or "Stakeholders" |
| Impact Severity | Business impact rating | Team inconvenience rating |
| Mitigation Tactics | Proactive prevention actions | Responses to the risk occurring |
| Contingency Plans | Reactive response if risk occurs | Duplicate of mitigation |
| Point of Contact | Named accountable individual | Team, function, or role title |

#### Connecting to Other Skills

- **Upstream:** ps-solution-hypothesis provides the solution context that grounds the risk identification. ps-framing-the-problem provides the customer and problem context.
- **Downstream:** ps-product-outcome-canvas (Batch 5) draws the risk summary from this assessment. ps-lofi-experimentation can convert high-priority testable assumptions from this assessment into structured experiments.

#### Capacity Reference

| Field | Target Length | Guidance |
|-------|--------------|----------|
| Risk Name | 5-8 words | Type label plus specific concern |
| Risk Raised By | 2-3 words | First name and last name or role |
| Mitigation Tactics | 15-25 words | Specific proactive action |
| Contingency Plans | 15-25 words | Specific reactive response |
| Notes | 10-20 words | Timing, dependencies, escalation |

## Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For shipment tracking, name a specific threat, assess severity and likelihood, and distinguish prevention from the contingency if it occurs.
- **Weak:** "Technical risk: high" gives no event, consequence, or response.
- **Drift to avoid:** Response confusion: mitigation reduces likelihood or impact; contingency says what to do if the risk happens.


## Common Pitfalls

- **All Technical Risks, No Adoption Risks:** Before finalizing the list, explicitly ask: what are the customer behavior change risks? What are the organizational readiness risks? What could cause the product to be technically correct but commercially unsuccessful?

- **Confusing Mitigation with Contingency:** Mitigation happens before the risk occurs and reduces the chance it will. Contingency happens after the risk occurs and limits the damage. Both are required.

- **Point of Contact as a Role, Not a Person:** Name a specific individual. If you cannot name one, that is a signal that the risk is unowned and needs an owner before the assessment is complete.

- **Risk Names That Are Categories, Not Concerns:** Follow the pattern: `[Risk Type]: [Specific Concern]`. "Market Risk" becomes "Competitive Timing: new entrant launches similar feature before our release."

- **Completing Risk Management Only for Easy Risks:** Start the Risk Management table with the Critical-priority risks. If time is limited, leave Accept-priority risks without management rows rather than leaving Critical ones blank.

- **Treating the Assessment as a One-Time Artifact:** Mark at least one specific future date or decision point where the assessment will be reviewed and updated.

- **Inflating Everything to High Severity:** Push the team to differentiate. If more than three risks are truly Critical, the team needs to re-examine whether the ratings reflect business impact or anxiety. Not every risk deserves equal attention.

- **Running the Assessment Alone:** Run this as a collaborative session. The project manager leads the facilitation. Stakeholders surface risks the PM team would not see from inside the product team.

- **A Risk List the Team Never Discussed:** The team brainstorms first. The skill widens the list with categories and candidates, and the team places and owns each risk.

## References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-risk-assessment) for supporting source material and expanded examples.
