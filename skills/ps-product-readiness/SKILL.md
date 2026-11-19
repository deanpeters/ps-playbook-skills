---
name: ps-product-readiness
description: >-
  Design and document a structured Product Readiness Test plan before launch.
  Use when a PM needs to plan a beta program, define Go/No Go criteria, and
  capture assumptions and risks that are out of scope for the test.
intent: >-
  Help a Product Manager design a structured pre-launch beta program that
  produces a clear Go/No Go decision, so that the team commits to launch only
  when real customers confirm the product is ready, and stops the launch when it
  is not.
type: component
blueprint_stage: Create
best_for:
  - "Designing a structured beta test plan with real customers before market launch"
  - "Defining Go/No Go criteria that are locked before the test begins"
  - "Gating entry to the Deliver phase with an evidence-based readiness check"
scenarios:
  - "We are preparing for launch and need to design a beta test plan with real customers"
  - "Help me define Go/No Go criteria for our pre-launch readiness test"
---


## Purpose

Create a **Productside-style Product Readiness artifact** from a structured pre-launch test plan.

This skill helps a Product Manager plan and document a beta program that validates the product with real customers before market release. The output is a three-section artifact: a Test Plan (who, how many, how long, and which team roles), a Goals table (objectives, metrics, and numeric targets), and an Assumptions and Risks section (honest documentation of what the test does not cover).

This skill belongs to the **Create phase** and marks a Key Decision Point. The results of the readiness test feed the final Go/No Go decision before launch. The playbook is explicit: **do not be afraid to stop a launch if the product is not ready.** A No Go outcome is a valid and sometimes correct result, not a failure.

Use this skill when you need to:
- design a beta test plan with real customers before committing to market launch
- define Go/No Go criteria that are locked before the test begins
- assign team roles for the test and document what the test does not cover
- gate entry to the Deliver phase with an explicit readiness decision

This is not a first-contact usability test. If users have never touched the product before, this is not the right play - run lo-fi experimentation or a structured pilot first. This is not a readiness check on the product team's internal processes; it is a validation of the product with real customers in real context.

## Key Concepts

### This Is Not the First Time Users Test the Product

Product Readiness Testing is the final validation before market release. It presupposes earlier rounds of testing: lo-fi experimentation, clickable prototype feedback, pilot access, and discovery work with real customers. If this is the first time users are touching the product, the team is using Product Readiness Testing to do work that should have been done months earlier.

Before planning the readiness test, confirm that earlier testing has occurred. If it has not, the better next step is lo-fi experimentation or a structured pilot, not a readiness test.

### Readiness Testing Also Catches Technical Issues Before Launch

Beyond the Go/No Go decision, the readiness test is an opportunity to surface bugs, defects, and configuration failures in a controlled setting before they reach the full market. When participants encounter a broken workflow, a missing integration, or unexpected system behavior, that is signal  -  not noise.

This is one reason a dedicated technical support person on the test team is not optional. Bugs surface during real customer use in ways that internal QA and staging environments cannot predict. A readiness test with real participants using the product in their actual context will expose failure modes that controlled testing misses.

Log every technical issue that surfaces during the program, triage severity, and track resolution before the Go/No Go call. A test that produces a clean set of found-and-fixed issues alongside quantitative goal results is a stronger foundation for a launch decision than metrics alone.

### Define Success Before Running the Test

Before the test starts, the PM and team must agree in writing which goals are must-pass and which are aspirational. This pre-commitment prevents post-hoc rationalization: the team cannot look at mixed results and convince themselves the test passed because two out of four goals were met.

A Go/No Go decision is only credible if the criteria were locked before anyone saw results.

### Three Sections, Three Purposes

- **Test Plan (left side):** who participates, how many, how long the test runs, and who on the team is responsible for what. Each question has a specific structural answer, not a generic placeholder.
- **Goals Table (right side):** four to five rows, each naming a specific objective, the metric used to measure it, and a numeric or percentage target. "Improve satisfaction" is not a goal for this table. "User satisfaction score of 4.2 or above on post-use survey" is.
- **Assumptions and Risks (bottom, full width):** an honest, named list of what the test does not cover and why. This section tells stakeholders where the test has known limits. Leaving it blank implies the test covers everything, which it never does.

### Who to Test With: Profiles, Not Just Job Titles

Customer profiles for the test should describe real-context participation: role, company type, experience level, and what they represent. "HR manager" is a job title. "HR operations manager at a mid-market company (200-500 employees) with no dedicated HR technology team, responsible for manual payroll and benefits administration" is a profile. The difference matters because the profile determines whether the test is exposing the right failure modes.

### The Goals Table Requires Numeric Targets

Each row in the Goals table must have a number. The target cell is not a description of the direction of improvement. It is the threshold that defines whether the goal was met. Without a number, the team cannot make a clean Go/No Go call.

Canonical goal categories from the playbook: workload reduction, user satisfaction, self-service adoption rate, system uptime.

### Assumptions and Risks Documents Scope Limits

Every beta program has constraints: limited training, incomplete integrations, specific user populations that are not representative of the full market, features that are intentionally excluded from the test. Document them explicitly. This protects the team from being held accountable for failures that were known to be outside the test scope, and it signals to stakeholders where follow-up validation is still needed.

### Quotes Are a Deliverable

The playbook says: "Remember to gather quotes from the test program to use during the official launch." The readiness test is an opportunity to collect memorable user statements that can be used in launch communications, internal presentations, and sales conversations. Designate someone on the test team to capture quotes as the test runs. This is not optional.

### The Test Team Has Distinct Roles

Three functions matter in a readiness test: the PM (leads the test and owns the Go/No Go call), the account or client contact (manages participant expectations and relationship), and a technical support person (handles bugs and configuration issues as they surface). If no one is assigned to technical support, participants hit problems with no one to triage them, and the test collapses into a support event rather than a learning event.

### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **critic of the readiness test plan the PM drafted**. It checks that participants are defined by profile, that goals have numeric targets resting on a baseline, that Go/No Go criteria are committed before the test, and that quote capture is planned. The targets and the Go/No Go criteria are the PM's to set.

- **Use it when:** the PM has a draft readiness test plan and wants it pressure-tested before the test starts.
- **Avoid it when:** the request is to set the Go/No Go thresholds, or to predict how participants will react. Even when asked to "just pick numbers," leave each threshold `[PM TO SET]`, name the baseline or evidence that would anchor it, and help structure the criteria (measure, threshold, basis). Even once the PM has baselines, don't offer to propose the numbers: show how each baseline narrows the choice, and leave the number to the PM.
- **Return:** participant profiles sharpened, each goal checked for a measure and a baseline, Go/No Go criteria tested for whether they would really stop a launch, and gaps in quote capture and scope flagged.

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

- all four Test Plan questions answered with specific content
- Goals table with 4-5 rows, each including a numeric target
- Go/No Go criteria explicitly named (which goals are must-pass)
- Assumptions and Risks section with 3-5 specific, named scope limits
- Quote capture plan mentioned or integrated into the team roles section
- explanation belongs below the artifact, not inside the fields

### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

### Step 1: Tech-Role Bias Guard

Before drafting, confirm who the product actually serves. Beta testers must represent the actual customer population, not internal technical users unless the product is built for technical users.

Common failure: a product for field service technicians, warehouse supervisors, or HR administrators is tested by the engineering team, the QA team, or internal operations staff who are familiar with the product. These users do not expose the failure modes that matter to the real customer: unfamiliar workflows, different mental models, limited training, and domain-specific constraints.

Ask: "Who is the customer who will use or buy this product in the field?" The answer to that question defines who must be in the test. If the answer is not the same as the people currently on the tester list, name the gap.

### Step 2: Gather Upstream Artifacts

Before drafting the readiness test plan, ask whether the user has:

- Solution hypothesis from ps-solution-hypothesis (defines what is being validated)
- Product success metrics from ps-outcome-tree (provides the measurable targets the test should confirm)
- Risk assessment from ps-risk-assessment (surfaces known risks that may affect the test or its scope limits)
- Persona profiles from ps-proto-persona (helps define who to recruit for the test)

Accept equivalent information from any source. The PM may already know their beta user pool independently. If upstream artifacts are not available, work with what the PM knows and note where assumptions are being made.

### Step 3: Define Customer Profiles for the Test

Write a specific description of each type of participant in the test. For each profile:

- Name the role and function (not just the job title)
- Describe the company type and size context
- Note the relevant experience level with the problem or prior tools
- Explain what this participant profile represents in the broader market

If the test includes multiple participant types for comparison (for example, paying customers and internal teams as a control group), describe each type separately and explain what the comparison is designed to reveal.

### Step 4: Determine Participant Count and Structure

State how many participants will be in the test, broken down by type. The breakdown matters: "8 participants" is less useful than "5 operations managers from mid-market companies and 3 enterprise customers for comparison."

If the product serves multiple segments, the participant structure should reflect which segments are being validated. If the test only covers one segment, name that explicitly as a scope limit in the Assumptions and Risks section.

### Step 5: Set the Test Duration

Define the test duration in terms that reflect meaningful product use, not just calendar time. Two weeks is meaningful if participants use the product every day. Two weeks is meaningless if participants are expected to use the product once for a monthly process.

Anchor duration to one of three things:
- A product usage cycle (one billing cycle, one reporting period, one scheduling cycle)
- A time box with a minimum usage expectation (three weeks, with at least two full use sessions per week)
- A task completion definition (the test ends when participants have completed the onboarding flow, run their first payroll, or submitted their first order)

Calendar days alone are not sufficient.

### Step 6: Assign Test Team Roles and Responsibilities

Name specific individuals for each function:

- **Test Lead:** the PM or designated person who runs the test, owns the schedule, and holds the Go/No Go call at the end
- **Account/Client Contact:** the person managing participant expectations, handling scheduling, and maintaining the relationship with beta participants
- **Technical Support:** the person who triages bugs, handles configuration issues, and responds to participant technical questions during the test

Each role should be a named person. If a role is unfilled, name it as an open assignment and flag it as a risk before the test begins.

### Step 7: Write the Goals Table

For each goal row, provide three things:

- **Goal/Objective:** a specific, named outcome the test is designed to confirm. Not "test the product." Examples: "Confirm the system reduces manual data entry time," "Validate that participants can complete the onboarding flow without support assistance."
- **Measure/Metric:** the specific thing being measured. A survey score, a task completion rate, a time-on-task reading, an error count.
- **Target:** the number or percentage that defines success. "4 out of 5 stars or above," "70% task completion without support," "uptime of 99.5% or higher."

Write 4-5 rows. Cover at least three distinct measurement types: workload or efficiency, user satisfaction or experience, adoption behavior, and system reliability.

### Step 8: Pre-Commit Go/No Go Criteria

After drafting the Goals table, explicitly name which goals are must-pass and which are aspirational. This step must happen before the test runs.

Format:
- Must-pass goals (all must be met for a Go): [list by row name]
- Aspirational goals (failure does not block Go, but is flagged): [list by row name]

If no pre-commitment is made, the team cannot make a clean Go/No Go call when results are mixed.

### Step 9: Plan for Quote Capture

Designate one person to collect memorable user statements during the test. Brief them before the test starts on what kinds of quotes are useful: spontaneous reactions to the product, statements about specific pain points resolved, comparisons to prior tools or processes.

Quotes captured during the readiness test can be used in launch communications, internal alignment presentations, and sales conversations.

### Step 10: Document Assumptions and Risks

Write a bulleted list of what is explicitly not being tested in this program and why. Each bullet should name the specific constraint and the reason it is out of scope.

Examples:
- "Limited employee training on the new platform could slow adoption rates; standardized training materials will not be available until post-launch."
- "Data security testing will be conducted post-readiness due to compliance review timelines."
- "Not all integrations will be tested during this phase; only the primary ERP integration is in scope."
- "The test does not include enterprise customers; segment-specific validation is planned for Q3."

Aim for 3-5 bullets. If the list is empty, that is a signal the test scope has not been fully examined, not that the test covers everything.

### Step 11: Offer Next Steps

After delivering the artifact, offer three options:

1. Run the test and return with results to complete the Go/No Go decision
2. Carry the readiness test goals and outcomes forward into post-launch retrospective planning
3. Review the Assumptions and Risks section with stakeholders to confirm alignment on scope limits before the test begins

## Template

### When to Use This

Use this template when preparing a **pre-launch beta program** to validate the product with real customers before market release. This is a Key Decision Point: the results determine whether to launch (Go) or hold (No Go).

Before running this template, confirm that earlier rounds of user testing have occurred. This is the final validation before launch, not the first time users see the product.

Upstream artifacts that feed this template:
- Solution hypothesis (ps-solution-hypothesis): defines what is being validated
- Product success metrics from ps-outcome-tree: provides measurement anchors for the Goals table
- Risk assessment (ps-risk-assessment): surfaces known risks that may define scope limits
- Persona profiles (ps-proto-persona): helps define who to recruit as beta participants

---

### Template

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

### Usage Guidance

#### Filling the Template

1. Complete **Product Context** to anchor the product, stage, and test lead.
2. Answer all four **Test Plan questions** with specific content before planning the test logistics.
3. Write the **Goals table** before recruiting participants. The goals define what the test is designed to measure.
4. Complete **Pre-Committed Go/No Go Criteria** before the test begins. This is the most commonly skipped step.
5. Fill the **Assumptions and Risks section** before finalizing participant communication.
6. Return to complete the **Post-Test Go/No Go Call** after results are in.

#### What Goes Where

| Section | Contains | Does NOT Contain |
|---------|----------|------------------|
| Customer Profiles | Role + company type + experience level + what they represent | Job titles alone |
| How Many | Total count broken down by participant type | A single total number |
| Test Duration | Usage cycle or task completion anchor | Calendar days alone |
| Test Team Roles | Named individuals with specific functions | "The PM" or "the engineering team" |
| Goal/Objective | Specific named outcome the test confirms | Generic placeholders like "test usability" |
| Target | Number or percentage | Directional aspirations |
| Assumptions and Risks | Specific named scope limits with reasons | Blank or generic acknowledgment |

#### Connecting to Other Skills

- **Upstream:** ps-solution-hypothesis (defines what is being validated), ps-outcome-tree (product success metrics), ps-risk-assessment (known risks), ps-proto-persona (who to recruit)
- **Downstream:** Post-launch retrospective; launch communications (customer quotes)
- **Related:** ps-lofi-experimentation (if earlier rounds of user testing have not occurred, use this skill before planning a readiness test)

#### Capacity Reference

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

## Examples

Illustrative and fictional, not customer evidence.

- **Strong:** A field-service beta plan names real technician participants, workflows, success criteria, health guardrails, and the owner of the Go/No Go call before testing.
- **Weak:** "Try the app and report bugs" does not establish readiness criteria.
- **Drift to avoid:** False readiness: internal checks or plausible simulated results cannot stand in for observed customer testing.


## Common Pitfalls

- **Testing with Internal Users Only:** The participant list must represent the actual customer population. If internal users are included for comparison, name them as an internal cohort and do not let them substitute for external customer participants. Name this as a risk in the Assumptions and Risks section if external participants cannot be secured.

- **Goals Table Has Directional Aspirations Instead of Numeric Targets:** Every Target cell must contain a number or percentage. "Reduce time spent on monthly reconciliation by 30% or more." "User satisfaction score of 4.0 or above on a 5-point scale." If the team cannot agree on a number before the test, that disagreement is itself a problem to resolve before the test begins.

- **No Pre-Committed Go/No Go Criteria:** After writing the Goals table but before running the test, explicitly name which goals are must-pass. Document it. This pre-commitment is the only thing that makes the Go/No Go call credible.

- **Assumptions and Risks Section Left Blank:** Every readiness test has scope limits. Name them. Incomplete integrations, missing training materials, single-segment coverage, deferred security testing: these are real and nameable. Documenting them is not weakness. It is honesty.

- **This Is the First Time Users Have Tested the Product:** Confirm that earlier testing has occurred before planning a readiness test. If it has not, the better path is lo-fi experimentation (ps-lofi-experimentation) or a structured discovery session, not a formal beta program.

- **Test Duration Defined Only in Calendar Days:** Anchor duration to a product usage cycle ("one full scheduling cycle"), a minimum usage expectation ("three sessions of at least 30 minutes each within the two-week window"), or a task completion definition ("the test ends when participants have completed their first end-to-end workflow"). Calendar time is secondary.

- **No One Assigned to Technical Support:** Name a technical support person before the test begins. This person is on call during the test to triage bugs, resolve configuration issues, and provide participant-facing technical help. If no one can be assigned, name it as a risk in the Assumptions and Risks section and describe the contingency.

- **Forgetting to Collect Quotes:** Designate one person to capture memorable user statements during the test, before it begins. Brief them on what kinds of quotes are useful. Budget time in each participant session to ask open-ended questions that surface quotable responses.

- **Thresholds Nobody Chose:** The PM sets each threshold with its basis. The skill asks what baseline it rests on and whether the team would really stop the launch at that number.

## References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-product-readiness) for supporting source material and expanded examples.
