---
name: ps-outcome-tree
description: >-
  Connect business outcomes to product outcomes using the Productside Outcome
  Tree. Two modalities - Section One (pre-discovery business context) and
  Section Two (post-discovery actuals vs. planned). Use when you need to
  establish or update the strategic link between what the business is trying to
  achieve and what the product must deliver.
intent: >-
  Help a Product Manager define the business outcome their product supports, the
  business success metrics that track it, 2-5 product outcomes that the customer
  needs to achieve, and the product success and health metrics that measure
  delivery, so the team has a shared, testable link between business strategy
  and product work. Then, after discovery, help the PM update the tree with
  validated outcomes, revised metrics, and actual results.
type: component
blueprint_stage: Context
best_for:
  - "Connecting business outcomes to product outcomes before discovery"
  - "Revisiting the tree after discovery with validated evidence"
  - "Defining product and business success metrics that stay aligned"
scenarios:
  - "I need to connect our business goals to product outcomes before starting customer research"
  - "We finished discovery and I need to update our outcome tree with validated evidence"
---


## Purpose

Create and maintain a **Productside-style Outcome Tree artifact** for your product.

This skill has **two modalities** that correspond to two moments in the playbook lifecycle:

**Section One (Modality 1 - Context phase, pre-discovery):** Establish the strategic context. Define the business outcome, business success metrics, 2-5 product outcomes, product success metrics, and product health metrics. This is the foundational frame that connects product work to business goals.

**Section Two (Modality 2 - Define/Deliver phase, post-discovery):** Update the tree with what you have learned. After discovery work (interviews, experiments, validation), revisit the tree to revise product outcomes based on evidence, update metrics with baselines and targets, record actual results against planned targets, and retire or replace outcomes that discovery invalidated.

The two modalities share the same artifact structure. Section Two is not a separate document. It is an update pass on the Section One artifact, informed by what the PM learned during discovery and define work.

Use this skill when you need to:

- connect product work to a measurable business goal (Section One)
- define 2-5 product outcomes that support a specific business outcome (Section One)
- distinguish business-level metrics from product-level metrics (Section One)
- create a shared artifact the team can revisit in planning and review meetings (Section One)
- build the foundation for prioritization and roadmap decisions (Section One)
- update outcomes and metrics after discovery validates or invalidates assumptions (Section Two)
- record actual results against the targets set in Section One (Section Two)
- retire product outcomes that no longer hold after customer research (Section Two)

This is not a one-time exercise. The playbook says to revisit regularly, bring it to team meetings, and use it to check assumptions with the team.

### Usage Notes

- **Two modalities:** Section One (Template 03, Context phase) establishes the strategic context before discovery. Section Two (Template 23, Define/Deliver phase) updates the tree after discovery with validated outcomes, revised metrics, and actuals vs. planned.
- The template produces a structured artifact with five sections: Business Outcome, Business Success Metrics, Product Outcomes (2-5), Product Success Metrics, and Product Health Metrics.
- Product outcomes use role names, not persona names.
- The play cross-references two other plays: Framing the Problem (Problem Statement box) and Solution Hypothesis Statement (Solution Summary box). Neither is a blocking dependency.
- Upstream: ps-jobs-to-be-done product outcomes feed into this tree. Section Two updates the tree after discovery work.

## Key Concepts

### Business Outcomes vs. Product Outcomes

These are two distinct levels. Confusing them is the most common mistake in this play.

**Business Outcome:** What the organization is trying to achieve at a strategic or operational level. It is owned by the business, not by the product team alone.

Example: "Improve new employee onboarding time by 30%"

**Product Outcome:** What the customer or user achieves when the product works well. Product outcomes support the business outcome, but they describe value from the customer's perspective.

Example: "Internal HR managers are focused on strategic initiatives and spend less time doing day-to-day tactical tasks"

The relationship is causal: if the product outcomes are achieved, the business outcome should follow. If that causal link is weak, the tree needs rework.

### Business Success Metrics

Business success metrics measure progress toward the business outcome. They are often lagging indicators owned by leadership or finance.

These may be defined or TBD at the time of building the tree. It is acceptable to leave them as "TBD" initially, but they should not remain blank permanently.

Examples:
- Time-to-productivity for new hires (days)
- Employee satisfaction score during first 90 days
- HR cost per onboarding cycle

### Product Success Metrics

Product success metrics measure whether each product outcome is being achieved. They are leading indicators owned by the product team.

Examples:
- Percentage of onboarding tasks completed without HR intervention
- Average HR manager time spent on tactical onboarding tasks per week
- Number of onboarding-related support tickets per month

### Product Health Metrics

Product health metrics measure the operational health of the product itself, separate from whether it is achieving outcomes.

Examples:
- System uptime percentage
- Average page load time
- Error rate for key workflows
- User adoption rate (active users / total licensed users)

Product health metrics are necessary but not sufficient. A product can be healthy (fast, reliable, available) and still fail to deliver outcomes.

### The 2-5 Product Outcome Limit

The playbook sets a hard limit: no more than 2-5 product objectives. This is not a suggestion. If you have more than 5, you are either splitting too finely or trying to serve too many business outcomes in one tree.

### Cross-References to Other Plays

The Outcome Tree references two other playbook artifacts:

- **Problem Statement** (from the Framing the Problem play): feeds into the tree as context for why the business outcome matters
- **Solution Summary** (from the Solution Hypothesis Statement play): feeds into the tree as a summary of the proposed approach

These are cross-references, not blocking dependencies. You can build the Outcome Tree without having completed those plays, but the tree is stronger when they exist.

### Section One vs. Section Two (Two Modalities, One Skill)

This skill covers both sections of the Outcome Tree as two modalities:

**Section One (Template 03, Context phase):** Build the tree before discovery. Define the business outcome, product outcomes, and metrics framework based on the PM's current understanding of strategy and customer needs.

**Section Two (Deliver phase  -  reuses the Outcome Tree design; the baseline deck labels this occurrence "Template 3 of 24"; the B2B work-in-progress deck numbers it Template 23):** Update the tree after discovery. Revise product outcomes that discovery validated or invalidated. Fill in metrics that were TBD. Add baselines and targets now that real data exists. Record actuals against planned targets. Retire outcomes that turned out to be wrong.

The trigger for Section Two is evidence: completed empathy interviews, validated hypotheses, experiment results, or post-launch measurement data. If the PM has not done discovery work since building Section One, Section Two will just reproduce the same guesses with more confidence. That is not useful.

### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **critic of the outcome tree the PM drafted**, in both sections. In Section One it checks that the business outcome is measurable, that product outcomes describe what customers achieve, and that metrics are in the right place. In Section Two it asks what discovery evidence supports or contradicts each product outcome. The outcomes, targets, and the verdict on each stay the PM's.

- **Use it when:** the PM has drafted Section One, or has discovery evidence to review in Section Two.
- **Avoid it when:** the request is to invent the business outcome, or to fill in baselines, targets, or actuals without data.
- **Return:** each outcome and metric checked for format and placement, the causal chain from product outcomes to business outcome tested, and in Section Two, each product outcome matched to evidence for the PM to keep, revise, or retire.

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

Use [Template](#template) for the full scaffold.


### Required Output Convention

Default to a **clean, paste-ready structured artifact** with clearly labeled sections.

That means:

- fill all sections (Business Outcome, Business Success Metrics, Product Outcomes, Product Success Metrics, Product Health Metrics)
- produce 2-5 product outcomes that clearly support the business outcome
- keep product outcome statements concise enough for template cells (~15-20 words)
- keep metrics specific and measurable
- explanation belongs below the artifact, not inside the template cells

The artifact comes first. Commentary is secondary.

### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

### Step 1: Confirm the Product and Business Context

Before writing anything, answer:

- what product or service are we talking about?
- what business or organization does this product serve?
- who are the customers/users of this product?

**Guard against tech-role bias.** The product outcomes belong to the customer, the person who uses or buys the product in the field. A clinical data platform's product outcomes belong to clinical operations leads and research scientists, not to data engineers or platform architects. Before writing product outcomes, confirm: does this person write code, design systems, or architect solutions as their primary job? If no, the outcomes should not read like a technologist's goals.

### Step 2: Gather Evidence Before Writing

Once you know the product and business context, ask the user for relevant materials before drafting:

- **Strategy documents** such as business plans, annual goals, OKR frameworks, or strategic planning decks
- **Existing metrics** such as current KPIs, dashboards, or performance reports
- **Prior discovery work** such as problem statements, persona artifacts, or JTBD artifacts from other skills

This skill uses **artifacts-only** evidence gathering. The business outcomes and product outcomes should come from the PM's own strategic context, not from web research. Do not offer to run web searches for this skill.

### Step 3: Define the Business Outcome

Write a clear, specific business outcome statement. This is what the organization is trying to achieve.

A strong business outcome:

- names a measurable change (improve, reduce, increase, eliminate)
- includes a target or direction, even if approximate
- is owned by the business, not just the product team
- is specific enough that you could tell if it happened

Weak: "Grow the business"
Stronger: "Improve new employee onboarding time by 30%"

Weak: "Increase efficiency"
Stronger: "Reduce average claim processing time from 14 days to 5 days"

If the user cannot articulate a business outcome, that is a signal that the strategic context is unclear. Help them work through it, but do not invent one.

### Step 4: Define Business Success Metrics

For the business outcome, identify 1-3 metrics that the business would use to measure progress.

These metrics should be:

- measurable (a number, percentage, or rate)
- owned by or visible to business leadership
- connected to the business outcome statement

It is acceptable for these to be "TBD" if the user does not have them yet. Note this in the artifact and flag it as a gap to resolve.

### Step 5: Define Product Outcomes (2-5)

For each product outcome, describe what the customer or user achieves when the product works well.

Product outcomes:

- describe value from the customer's perspective
- use role names, not persona names (e.g., "HR managers" not "Maya")
- support the business outcome through a causal link
- are limited to 2-5 per tree

Format guidance: write each product outcome as a statement about the customer's improved state. Focus on what changes for them, not what the product does.

Weak: "The product has a self-service onboarding module"
Stronger: "Internal HR managers are focused on strategic initiatives and spend less time doing day-to-day tactical tasks"

Weak: "Automated workflow engine"
Stronger: "New employees complete required onboarding steps without waiting for HR availability"

### Step 6: Define Product Success Metrics

For each product outcome, identify 1-2 metrics that would indicate the outcome is being achieved.

Product success metrics should be:

- leading indicators (they move before the business outcome moves)
- measurable by the product team
- tied to a specific product outcome

If metrics are not yet defined, mark them as "TBD" and note the gap.

### Step 7: Define Product Health Metrics

Identify 2-4 metrics that measure the operational health of the product itself.

Product health metrics are about the product working correctly, not about outcomes being achieved. They include things like:

- uptime and availability
- performance (load times, response times)
- error rates
- adoption and engagement rates

### Step 8: Cross-Reference Problem Statement and Solution Summary

If the user has completed the Framing the Problem play (ps-framing-the-problem), pull in the problem statement as context.

If the user has completed the Solution Hypothesis Statement play (ps-solution-hypothesis), pull in the solution summary.

If neither exists yet, note these as optional inputs that strengthen the tree when available.

### Step 9: Review the Causal Chain

Before finalizing, walk through the logic:

- If Product Outcome 1 is achieved, does it plausibly contribute to the Business Outcome?
- If Product Outcome 2 is achieved, does it plausibly contribute to the Business Outcome?
- Are the product outcomes collectively sufficient to move the business outcome, or are there gaps?
- Are any product outcomes actually business outcomes in disguise?
- Are any product outcomes actually features or solutions?

Flag any weak links for the user to consider.

### Step 10: Offer Next Steps (Section One)

After the Section One artifact is complete, offer the user up to three next-step options:

1. **Build or refine a problem statement** using ps-framing-the-problem, if no problem statement exists yet
2. **Define a solution hypothesis** using ps-solution-hypothesis, to fill in the Solution Summary box
3. **Run Section Two** of this skill after discovery work to update the tree with evidence

Present these as options, not as mandatory steps. The user decides what comes next.

---

### Section Two: Updating the Outcome Tree After Discovery

The following steps apply when the PM returns to the Outcome Tree after completing discovery and define work. Section Two is not a new artifact. It is an update pass on the existing Section One artifact.

### Step 11: Confirm Discovery Evidence Exists

Before running Section Two, verify the PM has new information to work with. Ask:

- What discovery activities have been completed since the tree was built? (empathy interviews, experiments, validation sessions, market research)
- What did discovery reveal that surprised you or contradicted your assumptions?
- Have any product outcomes been validated, invalidated, or changed in priority?

If the PM has no new evidence, Section Two will not add value. Recommend completing discovery work first.

### Step 12: Review Each Product Outcome Against Evidence

Walk through each product outcome from Section One and ask:

- **Validated:** Did discovery confirm this outcome matters to customers? Keep it, sharpen the language if needed.
- **Invalidated:** Did discovery reveal this outcome is not important to customers, or that the causal link to the business outcome is weaker than assumed? Mark it for retirement or revision.
- **New:** Did discovery reveal a product outcome that was missing from Section One? Add it (staying within the 2-5 limit).
- **Revised:** Does the outcome need reframing based on what customers actually said or did?

Update the Product Outcomes table accordingly. Note what changed and why in the Notes section.

### Step 13: Update Metrics with Baselines, Targets, and Actuals

For each metric section (business success, product success, product health):

- Replace "TBD" entries with defined metrics where evidence now exists
- Add **baseline** values (what is the current state before the product intervention?)
- Add or refine **target** values (what does success look like, now that you know more?)
- If post-launch: record **actual** values and note variance from target

Use a consistent format: "Metric Name: baseline X, target Y, actual Z (if available)."

### Step 14: Reassess the Causal Chain

Re-run the causal chain review from Step 9, but with the updated outcomes:

- Do the revised product outcomes still collectively support the business outcome?
- Did discovery reveal gaps in the chain that Section One missed?
- Are the business success metrics still the right ones, or has the business context shifted?

Flag any breaks in the chain for the PM to resolve.

### Step 15: Offer Next Steps (Section Two)

After the Section Two update is complete, offer the user:

1. **Share the updated tree with stakeholders** to align on revised priorities
2. **Update the roadmap** using ps-outcome-roadmap (if available) to reflect revised outcomes
3. **Schedule the next review cycle** to keep the tree current as the product evolves

## Template

### When to Use This

Use this template during the **Context** phase to connect your product work to a measurable business goal. This is foundational: until you can articulate what the business is trying to achieve and how the product supports that, prioritization and roadmap decisions lack an anchor.

Revisit this artifact regularly. Bring it to team meetings. Use it to share success metrics and check assumptions with the team.

### Template

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

### Usage Guidance

#### Filling the Template

1. Start with **Product Context** to anchor who this is for.
2. Add the **Problem Statement** if one exists from previous work.
3. Define the **Business Outcome** first. Everything else flows from it.
4. Add **Business Success Metrics** (even if some are TBD).
5. Define **Product Outcomes** (2-5). These describe what the customer achieves.
6. Add **Product Success Metrics** for each product outcome.
7. Add **Product Health Metrics** for the product itself.
8. Add the **Solution Summary** if one exists.
9. Walk through the **Causal Chain Review** to verify connections.

#### How Many Product Outcomes

The playbook sets a hard limit of 2-5. Default to 2-3 for a focused product. Use 4-5 only when the product serves multiple distinct user roles or the business outcome is broad enough to require multiple paths.

If you find yourself writing more than 5, either:

- consolidate related outcomes into a single, broader outcome
- split into multiple trees, each with a different business outcome

#### What Goes in the Product Outcome Statements

Write each product outcome as a statement about the customer's improved state. Use role names (e.g., "HR managers," "field technicians," "compliance officers"), not individual persona names (e.g., "Maya," "Carlos").

Do not use:

- feature descriptions ("The product provides...")
- implementation details ("Automated workflow for...")
- business metrics ("Revenue increases by...")
- internal team goals ("The engineering team ships...")

#### Connecting to Other Skills

- **Upstream:** ps-framing-the-problem provides the Problem Statement; ps-solution-hypothesis provides the Solution Summary
- **Parallel:** ps-jobs-to-be-done produces product outcomes that may feed into this tree
- **Downstream:** Section Two (this skill, Modality 2) updates the tree after discovery and define work

---

### Section Two: Updating the Outcome Tree After Discovery

Use this scaffold when returning to the Outcome Tree after completing discovery work. This is not a new artifact. It is an update pass on the Section One artifact above.

#### Prerequisites

Before running Section Two, the PM should have completed at least one of:

- empathy interviews (ps-empathy-interviews)
- solution hypothesis validation (ps-solution-hypothesis)
- lo-fi experimentation (ps-lofi-experimentation)
- market or customer research
- post-launch measurement data

#### Update Scaffold

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

#### When to Run Section Two

Section Two adds value when the PM has new evidence that changes the tree. Common triggers:

- Completed empathy interviews revealed different customer priorities than assumed
- Solution hypothesis testing invalidated an assumed product outcome
- Market research shifted the competitive context
- Post-launch data shows actual vs. planned variance
- Business strategy changed, altering the business outcome or its metrics

Section Two does not add value when:

- The PM has not done discovery work since Section One (the tree will not change)
- The only change is cosmetic rewording (edit the Section One artifact directly)

#### Capacity Reference

See [Template and capacity guidance](#template) for the exact word and character budgets per field.

| Field | Word Budget | Guidance |
|-------|-------------|----------|
| Business Outcome | ~15-25 | Specific, measurable business goal |
| Business Success Metric | ~10-15 | Measurable indicator with units |
| Product Outcome | ~15-20 | Customer-centered value statement |
| Product Success Metric | ~10-15 | Leading indicator tied to an outcome |
| Product Health Metric | ~5-10 | Operational metric with target |

## Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For irrigation management, connect business results to farm managers reducing avoidable water use, then define success and health measures. Revisit planned outcomes against actual evidence in Section Two.
- **Weak:** A tree with no customer outcomes jumps directly from financial targets to features.
- **Drift to avoid:** Layer confusion: "Ship sensors" is an output; "increase subscription revenue" is a business result. Neither substitutes for customer progress.


## Common Pitfalls

- **Confusing Product Outcomes with Business Outcomes:** Ask: who experiences this outcome? If the answer is "the business" or "leadership," it is a business outcome. If the answer is "the customer using the product," it is a product outcome. Keep them in their respective boxes.

- **Writing Feature Descriptions as Product Outcomes:** Strip out the product. Ask: what is different for the customer when this feature works? "New employees complete required onboarding steps without waiting for HR availability" is a product outcome. "Self-service onboarding portal" is a feature.

- **Setting More Than 5 Product Objectives:** The playbook limit is 2-5 product outcomes per tree. If you have more, either consolidate related outcomes or split into multiple trees for different business outcomes.

- **Making Business Outcomes Too Vague:** Add a direction, a metric, and a target. "Improve customer satisfaction" becomes "Increase Net Promoter Score from 32 to 50 within 12 months." If the user cannot specify a target, at least specify a direction and a metric.

- **Defaulting to Tech-Role Language in Product Outcomes:** Before writing product outcomes, confirm who the product actually serves. Most products serve people whose primary job is not writing code. An HR platform serves HR managers and employees, not data engineers.

- **Treating This as a One-Time Exercise:** The playbook says to revisit regularly and bring it to team meetings. Schedule periodic reviews and update the tree as strategy evolves.

- **Skipping Product Success Metrics:** Even if exact metrics are not known yet, define the type of measurement. "TBD" is acceptable as a starting point, but flag it as a gap that must be resolved before the next planning cycle.

- **Confusing Product Health Metrics with Product Success Metrics:** Keep them in separate sections. Product health metrics (uptime, latency, error rates) go in the health section. Product success metrics (task completion rates, time savings, adoption of key workflows) go next to their respective outcomes.

- **AI Writes the Tree:** The PM drafts; the skill checks each outcome and metric. Targets and baselines come from the PM's data or are marked to be set.

## References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-outcome-tree) for supporting source material and expanded examples.
