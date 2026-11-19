---
name: ps-solution-hypothesis
description: >-
  Craft a testable solution hypothesis using the If/Then structure, producing
  both a customer-focused and a business-focused hypothesis that chain together,
  grounded in a validated problem statement.
intent: >-
  Help a Product Manager translate a validated problem statement and solution
  exploration into a structured, testable solution hypothesis that separates
  customer value from business outcome, using the Productside two-column If/Then
  format that chains customer benefit into measurable business results.
type: component
blueprint_stage: Discover + Define
best_for:
  - "Crafting a testable If/Then hypothesis from a validated problem and solution direction"
  - "Documenting the proposed solution's benefits, risks, and assumptions"
  - "Creating paired hypothesis statements that connect solution to product and business outcomes"
scenarios:
  - "I need to turn our best solution direction into a testable hypothesis with If/Then statements"
  - "Help me document the solution we chose, its risks, and the assumptions we need to validate"
---


## Purpose

Create a **Productside-style Solution Hypothesis Statement artifact** that documents a proposed solution, its benefits and risks, and produces two linked If/Then hypothesis statements.

This skill is for the **Discover + Define** phase. It sits directly downstream of Framing the Problem and Exploring the Solution Space. The PM has validated a problem and explored possible solutions; now they are expressing their chosen solution as a testable hypothesis.

This is a synthesis and articulation skill. It pulls together findings from:

- problem framing (ps-framing-the-problem)
- solution space exploration (ps-exploring-solution-space)
- positioning work (ps-positioning-statement), if available

The output is a five-section artifact: problem statement (imported from upstream), solution summary, solution benefits, risks and assumptions, and a two-column solution hypothesis statement. This artifact is what the PM uses to communicate a testable solution direction to leadership and to justify resource allocation through gate review processes.

Use this skill when you need to:

- express a proposed solution as a testable If/Then hypothesis
- separate customer value from business outcome in a structured format
- document benefits and risks before committing to a solution direction
- create a reviewable artifact for leadership or gate review processes

This is not a PRD or feature specification. If the output reads like a requirements document or a feature list, the hypothesis has drifted into implementation territory.

### Usage Notes

- The template produces a single artifact with five sections: Problem Statement (imported), Solution Summary, Solution Benefits, Risks and Assumptions, and Solution Hypothesis Statement (two-column If/Then).
- Two hypothesis statements are required, not one: customer-focused (IF solution THEN customer benefit) and business-focused (IF customer benefit THEN business outcome). The THEN of the first becomes the IF of the second.
- Evidence gathering is **artifacts only** - no web research offered. This skill synthesizes the PM's problem framing and solution exploration work.
- Upstream: ps-framing-the-problem, ps-exploring-solution-space, ps-positioning-statement.
- Downstream: lo-fi experimentation, risk assessment, roadmap planning, outcome tree alignment.

## Key Concepts

### The If/Then Structure Is the Core Format

A solution hypothesis is not a description of what to build. It is a testable statement: **IF** we do X, **THEN** Y happens. This format forces the PM to connect the solution to an expected outcome, which is the first step toward validation.

A solution summary says "what." A hypothesis says "if we do this, then this result follows." The difference matters because summaries cannot be tested, but hypotheses can.

If you are not sure where to start, write the simplest possible If-then statement and work from there. Precision comes in later iterations.

### Two Hypotheses, Not One

The Productside format requires two linked hypothesis statements:

1. **Customer-focused:** IF we [provide this solution], THEN [customers experience this benefit]
2. **Business-focused:** IF we [achieve that customer benefit], THEN [we reach this business outcome]

The THEN of the customer-focused hypothesis becomes the IF of the business-focused hypothesis. This chain ensures the PM has thought through both sides: why the customer cares and why the business cares.

If there is only one hypothesis that mixes customer and business language, the chain is broken. Separate them.

### The Five Sections Have a Specific Flow

The artifact builds in a deliberate sequence:

1. **Problem Statement** carries forward from ps-framing-the-problem. It is imported, not rewritten.
2. **Solution Summary** describes the proposed solution in one paragraph.
3. **Solution Benefits** lists 3-5 specific benefits for the customer and the business.
4. **Risks and Assumptions** lists 3-5 specific risks or assumptions that need validation.
5. **Solution Hypothesis Statement** presents the two-column If/Then output.

Each section feeds the next. The problem grounds the solution. The solution grounds the benefits. The benefits and risks inform the hypothesis. The hypothesis is the synthesis of everything above it.

### Solution Benefits Are Not Features

A benefit is the outcome the customer or business experiences. A feature is what the product does. "Automated workflow engine" is a feature. "Time saved on manual data entry, freeing specialists to focus on strategic work" is a benefit.

Benefits should answer: so what? If the benefit reads like a capability description, push it one level further to the outcome.

### Risks and Assumptions Are Specific and Testable

Good risks name concrete failure modes: "Technical integration with legacy HRIS systems may require custom middleware." Bad risks name vague worries: "Things might not work as planned."

Assumptions are things the team believes to be true but has not yet validated. Surfacing them here prepares the PM for the validation work that follows the hypothesis.

### Connection to the Outcome Tree

The business outcome in the second hypothesis should align with an outcome in the Outcome Tree (if one exists). If the PM has done outcome tree work, the business-focused hypothesis should reference one of the identified business success metrics. This creates traceability from problem to solution to measurable result.

### Product Outcomes Use Role Names, Not Persona Names

When writing benefits, outcomes, and hypothesis statements, refer to roles ("HR specialists," "clinical operations leads," "field engineers") rather than individual persona names ("Henry," "Maya"). Role names keep the hypothesis generalizable across the target population.

### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **critic of the solution hypothesis the PM drafted**. It checks the If/Then format, tests whether the customer-focused hypothesis chains into the business-focused one, flags features posing as benefits, and asks whether each risk and assumption is specific enough to test. The solution and the bet stay the PM's.

- **Use it when:** the PM has a validated problem statement and a prioritized solution, and has drafted the hypothesis.
- **Avoid it when:** there is no validated problem statement. A hypothesis about an unframed problem has nothing to test against.
- **Return:** the If/Then chain tested link by link, benefits separated from features, risks and assumptions sharpened into things a test could settle, and proposed rewrites for the PM to accept, adapt, or reject.

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

Default to a **clean, paste-ready solution hypothesis artifact**.

That means:

- fill all five sections in order
- keep each section within its word budget (see Capacity Reference below)
- produce two hypothesis statements that chain together correctly
- explanation belongs below the artifact, not inside the template fields
- the artifact comes first; commentary is secondary

### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

### Step 1: Confirm the Product and Customer Context

Before writing anything, answer:

- what product or service is the PM building?
- who is the customer whose problem is being solved?
- what prior work exists (problem statement, solution exploration, positioning)?

If you cannot identify a specific customer, stop and resolve the target first.

**Guard against tech-role bias.** The solution should serve the actual customer, not default to building developer tools. A clinical data platform's solution hypothesis should describe value for clinical operations leads, not data engineers. An agricultural supply chain tool should describe value for farm operations managers, not software developers. Before writing the solution summary, confirm: does this solution serve the person who actually experiences the problem day-to-day?

### Step 2: Gather Evidence Before Writing

Once you know the product and customer, offer the user materials to share before drafting:

**User-supplied artifacts** - ask whether the user has materials to ground the hypothesis: validated problem statement (from ps-framing-the-problem), solution space exploration output, positioning work, competitive analysis, or earlier skill outputs.

This skill is **artifacts only** - it synthesizes the PM's own problem framing and solution exploration. Web research is not offered because the hypothesis should flow from validated upstream work, not from external sources the PM has not yet verified.

If the user has no validated problem statement, surface the tension: a solution hypothesis without a validated problem is building on assumptions. Recommend completing ps-framing-the-problem first, but proceed if the user wants to draft an assumption-based hypothesis.

### Step 3: Import or Confirm the Problem Statement

The problem statement comes from ps-framing-the-problem. It should be imported directly, not rewritten.

If the user provides a problem statement, place it in Section 1 as-is. If the user does not have one, help them draft a brief problem statement, but flag it as unvalidated.

The problem statement anchors everything that follows. If the problem is vague, the hypothesis will be vague.

### Step 4: Write the Solution Summary

Describe the proposed solution in one paragraph. This should come from the user's solution exploration work or their stated direction.

The solution summary should be:

- specific enough to be testable (not "build a better platform")
- written as what the solution does for the customer, not a feature spec
- one paragraph, not a list of capabilities

Word budget: ~30-40 words.

### Step 5: List Solution Benefits

List 3-5 specific benefits. Each benefit should state the positive outcome for the customer or the business.

Test each benefit: does it describe an outcome, or does it describe a feature? "Automated data entry" is a feature. "Time saved on manual data entry, allowing specialists to focus on strategic initiatives" is a benefit.

Mix customer benefits and business benefits. At least two should be customer-facing, at least one should be business-facing.

Word budget: ~5-10 words per benefit, 3-5 benefits.

### Step 6: List Risks and Assumptions

List 3-5 specific risks or assumptions that need to be validated.

Each risk or assumption should be:

- specific (not "things might go wrong")
- testable (the team can investigate whether it is true)
- relevant to the proposed solution (not generic business risks)

Common categories: technical integration risk, adoption risk, change management risk, data quality risk, regulatory risk.

Word budget: ~5-10 words per risk, 3-5 risks.

### Step 7: Write the Customer-Focused Hypothesis

Write the first hypothesis using the If/Then structure:

**IF** we [describe the solution in terms of what it provides to the customer], **THEN** [describe the specific benefit the customer experiences].

The IF should reference the solution summary. The THEN should reference one or more of the benefits listed above.

Use role names, not persona names. "We save HR specialists time" not "we save Henry time."

Word budget: ~30-40 words.

### Step 8: Write the Business-Focused Hypothesis

Write the second hypothesis. The IF of this statement picks up where the customer-focused hypothesis left off:

**IF** we [achieve the customer benefit from hypothesis 1], **THEN** [describe the measurable business outcome].

The business outcome should be specific and measurable. "We will achieve our goal of improving onboarding time by 30%" is measurable. "We will do better" is not.

Word budget: ~30-40 words.

### Step 9: Verify the Chain

Check that the two hypotheses link correctly:

- Does the THEN of hypothesis 1 connect logically to the IF of hypothesis 2?
- Does hypothesis 1 focus on customer value?
- Does hypothesis 2 focus on business outcome?
- Are both written as If/Then statements, not as descriptions?

If the chain breaks, revise until the handoff is clean.

### Step 10: Review for Solution Language vs. Outcome Language

Scan the entire artifact:

- Does the solution summary describe what the solution does, not how it is built?
- Do benefits describe outcomes, not features?
- Do hypotheses connect solutions to outcomes, not solutions to more solutions?
- Are risks specific and testable, not generic worries?

### Step 11: Offer Next Steps

After the artifact is complete, offer the user up to three next-step options:

1. **Design a lo-fi experiment** - test the hypothesis with a prototype, concierge MVP, or Wizard of Oz approach before committing to full build
2. **Conduct risk assessment** - prioritize and investigate the identified risks and assumptions
3. **Connect to the roadmap** - use the validated hypothesis to inform roadmap planning and resource allocation

Present these as options, not as mandatory steps. The user decides what comes next.

## Template

### When to Use This

Use this template during **Discover + Define** when you have a validated problem statement and have explored the solution space. You are ready to express your chosen solution direction as a testable hypothesis with expected customer and business outcomes.

Upstream work that feeds this template: framing the problem (ps-framing-the-problem), exploring the solution space (ps-exploring-solution-space), positioning statement (ps-positioning-statement, if available).

### Template

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

### Usage Guidance

#### Filling the Template

1. Start with **Product Context** to anchor who this is for and whose problem the solution addresses.
2. **Import the Problem Statement** from ps-framing-the-problem. Do not rewrite it.
3. Write the **Solution Summary** as one paragraph describing what the solution provides.
4. List **Solution Benefits** as outcomes, not features. Push each one past "what it does" to "why it matters."
5. List **Risks and Assumptions** with enough specificity that each one can be investigated.
6. Write the **Customer-Focused Hypothesis** first. Then write the **Business-Focused Hypothesis** using the THEN of the first as the IF of the second.
7. Verify the chain between the two hypotheses.
8. The **Evidence Notes** section is optional and trailing. Do not let it displace or delay the main artifact.

#### The Five Sections Build in Order

Do not skip ahead to writing hypotheses without completing the preceding sections. The problem statement grounds the solution. The solution grounds the benefits. The benefits and risks inform the hypothesis. Writing the hypothesis without the groundwork produces untethered speculation.

#### What Goes Where

| Section | Contains | Does NOT Contain |
|---------|----------|------------------|
| Problem Statement | Validated problem from upstream | New problem framing or solution language |
| Solution Summary | What the solution provides to customers | Implementation details, architecture, feature specs |
| Solution Benefits | Outcomes for customers and the business | Feature names, capability descriptions |
| Risks and Assumptions | Specific, testable failure modes or beliefs | Generic worries, vague concerns |
| Customer Hypothesis | IF solution THEN customer benefit | Business metrics, revenue targets |
| Business Hypothesis | IF customer benefit THEN business outcome | Feature lists, solution descriptions |

#### Connecting to Other Skills

- **Upstream:** ps-framing-the-problem provides the problem statement. ps-exploring-solution-space provides the chosen solution direction. ps-positioning-statement provides framing for how the solution fits the market.
- **Downstream:** The validated hypothesis drives lo-fi experimentation, risk assessment, and roadmap planning. The business outcome in hypothesis 2 should connect to the outcome tree if one exists.

#### Capacity Reference

See [Template and capacity guidance](#template) for the exact word and character budgets per field.

| Field | Word Budget | Guidance |
|-------|-------------|----------|
| Problem Statement | ~40-50 | Imported from ps-framing-the-problem |
| Solution Summary | ~30-40 | One paragraph, specific and testable |
| Solution Benefits | ~5-10 each | 3-5 outcome statements, not feature names |
| Risks and Assumptions | ~5-10 each | 3-5 specific, testable risks |
| Customer Hypothesis | ~30-40 | IF solution THEN customer benefit |
| Business Hypothesis | ~30-40 | IF customer benefit THEN business outcome |

## Examples

Illustrative and fictional, not customer evidence.

- **Strong:** If produce distributors receive earlier shipment-condition signals, then they can intervene before spoilage; if spoilage falls, then the business may improve margin. Define tests for both links.
- **Weak:** "Add tracking, alerts, and dashboards" lists features without predicting a testable change.
- **Drift to avoid:** Feature list as hypothesis: an If clause alone is insufficient. The Then clause must specify a customer or business result.


## Common Pitfalls

- **Writing a Feature List Instead of an If/Then Hypothesis:** Rewrite as an If/Then statement. The IF describes the solution. The THEN describes the expected outcome for the customer or business. "IF we provide automated workflows that reduce manual data entry, THEN field engineers will complete inspections 40% faster."

- **Merging the Two Hypotheses into One:** Separate into two statements. The customer-focused hypothesis connects solution to customer benefit. The business-focused hypothesis connects customer benefit to business outcome. The THEN of the first becomes the IF of the second.

- **Making the Solution Summary Too Vague to Test:** The solution summary must be specific enough that someone could design a test for it. "Implement an integrated HR management system with automated task workflows, centralized employee records, and a self-service portal for common requests" is testable.

- **Listing Generic Risks:** Each risk should name a specific failure mode. "Resistance to change from employees accustomed to the current manual process" is specific. "Integration with the legacy HRIS may require custom middleware not in the current budget" is specific.

- **Starting Without a Validated Problem Statement:** Complete ps-framing-the-problem first. If that is not possible, at minimum draft a problem statement and flag it as unvalidated. The hypothesis artifact should make visible whether the problem foundation is solid or assumed.

- **Using Persona Names Instead of Role Names in the Hypothesis:** Use role names: "IF we save HR specialists time on manual tasks, THEN they will redirect effort to strategic initiatives like talent development and workforce planning."

- **Writing Benefits That Are Just Restated Features:** Push each benefit one level further. "Automated data entry" becomes "Time recovered from manual data entry, allowing specialists to focus on higher-value work." The feature is the mechanism; the benefit is the outcome the customer cares about.

- **Writing a Business-Focused Hypothesis with No Measurable Outcome:** The business outcome must include a specific metric or target: "THEN we will reduce new employee onboarding time by 30%" or "THEN we will increase field inspection completion rates from 60% to 85% per quarter."

- **AI Writes the Bet:** The PM drafts the chain; the skill tests each link. Rewrites come after the critique, as options.

## References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-solution-hypothesis) for supporting source material and expanded examples.
