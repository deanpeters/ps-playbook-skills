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

Beyond the Go/No Go decision, the readiness test is an opportunity to surface bugs, defects, and configuration failures in a controlled setting before they reach the full market. When participants encounter a broken workflow, a missing integration, or unexpected system behavior, that is signal — not noise.

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

The Productside Playbook sets one rule for every AI-assisted Play: **the Product Manager does the thinking, and AI pressure-tests it.** In this skill, you are the AI. Hold yourself to these rules:

1. **Pressure-test before you produce.** When the user brings a draft, critique it against the Play's formats and criteria first. Point at the specific words that fail and ask the user to fix them. Offer rewrites only after the critique, as options to accept, adapt, or reject.
2. **Never stand in for the customer.** Do not present jobs, quotes, needs, or pains you generated as research, and do not answer as the persona as if your answers were evidence. Anything you draft about customers is a hypothesis, labeled as one, to validate with real people. Role-play is allowed only as rehearsal where the Play calls for it, labeled as practice, and nothing from it goes into findings.
3. **Never stand in for the team's judgment.** Do not put unsourced figures into the artifact, and do not make calls the team should own. A number without a source is a blank to fill, so mark it that way.
4. **Work the five habits.** *Context:* ask for the persona, market, outcome, and constraints when they are missing. *Guide:* offer competing views and welcome pushback. *Enforce:* work inside the Play's template, not around it. *Outcome:* tie the work to the decision it supports. *Iterate:* go step by step rather than one-shot.
5. **Keep best guess honest.** Best guess mode is allowed. When you use it, label every inferred detail inline and end with **Assumptions to Validate**. A best guess is a starting point to test, never a finding.

For people working in a chat tool without this skill, the Play's copy-paste prompts are in [prompts/](prompts/README.md).

### Guided Mode

When a user asks to be walked through this skill, signals unfamiliarity, or invokes it without enough context, run in guided mode. **Do NOT batch multiple questions into one turn. Do NOT list everything you need up front. One question per turn, every turn.**

1. **Open with a heads-up.** State what the skill produces, the estimated number of questions, and where you will stop for the user's decision. Offer three entry paths:
   - (1) **Guided** - one question at a time with recommendations
   - (2) **Context dump** - paste what you know and I will ask only what is missing
   - (3) **Best guess** - I will infer what I can and label every assumption

   Then ask the first question immediately (do not wait for the user to pick a mode - Guided is the default).

2. **Start from what is already supplied.** Treat text in the request, pasted notes, attached files, upstream Play artifacts, and decisions made earlier in the conversation as answers already given. Do not ask for them again. Begin at the first real gap, and keep the progress label honest about what remains.

3. **One question per turn.** Every turn follows this exact format:

   > `Context Q2/5`
   >
   > **Who are the primary users of this product?**
   >
   > Some options to consider:
   > 1. Clinical data managers who run queries against study databases
   > 2. Research scientists who need self-service access to trial data
   > 3. Biostatisticians who build analysis-ready datasets
   > 4. Other (describe your users)
   >
   > Pick one or more (e.g. `1`, `1,3`, `1 and 3`), or describe in your own words.

   The progress label (e.g. `Context Q2/5`) is mandatory on every turn. Recommendations must always be numbered `1.`, `2.`, `3.`, `4. Other` - never presented as bullet points or unnumbered prose. The three recommendations must be specific to the skill, the industry, and the context gathered so far - never generic placeholders. If you lack domain context for good recommendations, do a web search first to ground your options in real roles, real products, or real workflows. Explain why a question matters when that is not obvious, and ask a follow-up only when the answer could change the artifact or the decision.

   **Exception: evidence only the user has.** When a question asks for something only the user can know (a root cause, what customers said or did, what the user observed, a number they must set), ask it as an open question with no numbered options, and say why there are none. Options there would put guesses in the user's mouth.

4. **Recommendations get smarter each turn.** Each answer becomes context for the next question's recommendations. By the mid-point, options should reflect the specific product, customer, and situation the user has described - not generic suggestions. Early questions can use industry-typical examples; later questions must incorporate what the user has already told you.

5. **In context dump mode, show what you extracted first.** Before asking anything, give a short **Known / Assumed / Missing / Conflicting** summary of what the user supplied. Credit where each item came from, and keep what a source reported separate from what has been verified. Then ask only the questions that would most change the artifact.

6. **Interruption-safe.** Handle any of these mid-session:
   - **Meta questions** ("how many left?", "what does this term mean?"): answer directly, restate progress, restate the pending question, then wait.
   - **Mode switch** ("just take your best guess", "here is everything I know"): switch to the requested mode immediately. For best guess, infer remaining answers from context gathered so far, generate the artifact, and end with an explicit **Assumptions to Validate** list, ranked by how much each could change the decision. For context dump, parse what was provided and ask only about gaps.
   - **Correction** ("actually, go back to Q2"): revisit that question with the original recommendations updated for current context.
   - **Pause or stop**: stop immediately. On resume, summarize what was captured, what is still open, and the next question.

7. **Finish with a summary, then hand back the decision.** After the context is gathered, recap in a few short bullets: what was supplied, what was inferred, what remains unknown or disputed, and whether the work is ready for a decision. Confirm before generating the artifact. If best guess mode was used at any point, end with an explicit **Assumptions to Validate** list. When the user faces a choice (which option, which next Play, whether to proceed), present a numbered ladder: the option the evidence favors first, labeled `(Recommended)`, then two or three genuinely distinct alternatives, each with its tradeoff in one sentence, then `Other`. Allow combining options where it makes sense. The user decides.

## Application

Use [template.md](template.md) for the scaffold.

See the source play pages in [assets/ps_product_readiness_playbook_pages.pdf](assets/ps_product_readiness_playbook_pages.pdf).

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

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in [prompts/01-pressure-test-readiness-plan.md](prompts/01-pressure-test-readiness-plan.md) one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

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

## Examples

See [examples/sample.md](examples/sample.md).

The example set includes:

- a strong readiness test plan with specific customer profiles, numeric targets, pre-committed Go/No Go criteria, and a named scope limits section
- a weak version with vague profiles, directional goals without numbers, and a blank Assumptions and Risks section
- a drift-bug example showing internal-only testing when the product serves field customers, with commentary on what that systematically misses

## Common Pitfalls

### Pitfall 1: Testing with Internal Users Only

**Symptom:** The beta participant list consists of engineers, QA staff, internal operations staff, or other employees who are familiar with the product, when the product serves external customers.

**Consequence:** Internal users do not expose the failure modes that matter to real customers: unfamiliar workflows, different mental models, limited training, domain-specific constraints. The test passes cleanly and the launch fails in the field.

**Fix:** The participant list must represent the actual customer population. If internal users are included for comparison, name them as an internal cohort and do not let them substitute for external customer participants. Name this as a risk in the Assumptions and Risks section if external participants cannot be secured.

### Pitfall 2: Goals Table Has Directional Aspirations Instead of Numeric Targets

**Symptom:** Goal rows read as "improve efficiency," "increase user satisfaction," or "reduce support volume" with no accompanying number in the Target column.

**Consequence:** The team cannot make a clean Go/No Go call because there is no threshold to cross. Post-test rationalization becomes the only path.

**Fix:** Every Target cell must contain a number or percentage. "Reduce time spent on monthly reconciliation by 30% or more." "User satisfaction score of 4.0 or above on a 5-point scale." If the team cannot agree on a number before the test, that disagreement is itself a problem to resolve before the test begins.

### Pitfall 3: No Pre-Committed Go/No Go Criteria

**Symptom:** The Goals table is complete, but no one has named which goals are must-pass before seeing results.

**Consequence:** When results are mixed (two goals met, two not), the team debates in real time which goals should have been must-pass. The team that is most motivated to launch wins the argument, not the data.

**Fix:** After writing the Goals table but before running the test, explicitly name which goals are must-pass. Document it. This pre-commitment is the only thing that makes the Go/No Go call credible.

### Pitfall 4: Assumptions and Risks Section Left Blank

**Symptom:** The Assumptions and Risks section is empty or contains only a vague note like "standard product risks apply."

**Consequence:** Stakeholders believe the test covered all dimensions of readiness. When post-launch issues emerge in areas the test did not cover, the team has no documentation that those areas were out of scope.

**Fix:** Every readiness test has scope limits. Name them. Incomplete integrations, missing training materials, single-segment coverage, deferred security testing: these are real and nameable. Documenting them is not weakness. It is honesty.

### Pitfall 5: This Is the First Time Users Have Tested the Product

**Symptom:** The readiness test is being planned before any earlier rounds of user testing have occurred: no lo-fi experiments, no prototype walkthroughs, no pilot access.

**Consequence:** The readiness test is carrying the burden of all earlier validation that was never done. It will surface basic usability problems and conceptual mismatches that should have been caught months earlier, making it neither a readiness test nor a meaningful learning event.

**Fix:** Confirm that earlier testing has occurred before planning a readiness test. If it has not, the better path is lo-fi experimentation (ps-lofi-experimentation) or a structured discovery session, not a formal beta program.

### Pitfall 6: Test Duration Defined Only in Calendar Days

**Symptom:** The test duration says "two weeks" or "one month" with no reference to how many times participants are expected to use the product or what usage cycle the product supports.

**Consequence:** For a product that supports a monthly process, a two-week test means participants may use the product only once or not at all. The test produces no meaningful usage data.

**Fix:** Anchor duration to a product usage cycle ("one full scheduling cycle"), a minimum usage expectation ("three sessions of at least 30 minutes each within the two-week window"), or a task completion definition ("the test ends when participants have completed their first end-to-end workflow"). Calendar time is secondary.

### Pitfall 7: No One Assigned to Technical Support

**Symptom:** The Test Team Roles section names a test lead and an account contact but has no one assigned to handle bugs, configuration issues, or technical questions during the test.

**Consequence:** When participants encounter a bug or a configuration problem, they wait. The test stalls. Participants disengage. The team gets no signal about product behavior because the test became a support event.

**Fix:** Name a technical support person before the test begins. This person is on call during the test to triage bugs, resolve configuration issues, and provide participant-facing technical help. If no one can be assigned, name it as a risk in the Assumptions and Risks section and describe the contingency.

### Pitfall 8: Forgetting to Collect Quotes

**Symptom:** The test concludes with quantitative data but no direct participant statements. The launch team has metrics but nothing to say in the voice of the customer.

**Consequence:** A missed opportunity for launch marketing, internal alignment, and sales conversations. Quotes captured during a readiness test carry the weight of real pre-launch customer experience, which is harder to generate after launch.

**Fix:** Designate one person to capture memorable user statements during the test, before it begins. Brief them on what kinds of quotes are useful. Budget time in each participant session to ask open-ended questions that surface quotable responses.

### Pitfall 9: Thresholds Nobody Chose

**Symptom:** The PM asks for Go/No Go criteria and gets "Go if task success is above 85% and CSAT is above 4.2."

**Consequence:** The thresholds have no baseline and no owner. When results land at 83%, nobody knows whether to stop the launch.

**Fix:** The PM sets each threshold with its basis. The skill asks what baseline it rests on and whether the team would really stop the launch at that number.

## References

### Skill Files

- [template.md](template.md) - working scaffold
- [prompts/](prompts/README.md) - copy-paste prompt for chat-based AI tools (authored for this library; the deck has no AI page for this Play)
- [examples/sample.md](examples/sample.md) - strong, weak, and drift-bug examples

### Related Skills

- **Upstream:** [ps-solution-hypothesis](../ps-solution-hypothesis/SKILL.md) defines what is being validated; [ps-outcome-tree](../ps-outcome-tree/SKILL.md) provides the product success metrics that Goals table targets should reflect; [ps-risk-assessment](../ps-risk-assessment/SKILL.md) surfaces risks that may define scope limits; [ps-proto-persona](../ps-proto-persona/SKILL.md) helps define who to recruit for the test
- **Downstream:** Post-launch retrospective; launch communications (uses quotes captured during the test)
- **Related:** ps-lofi-experimentation: if earlier rounds of user testing have not occurred, this skill should precede the readiness test

### Project Docs

- [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)
- [informative-documents/framework-glossary.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/framework-glossary.md)
- [informative-documents/skill-dependency-map.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/skill-dependency-map.md)

### Source Material

- [assets/ps_product_readiness_playbook_pages.pdf](assets/ps_product_readiness_playbook_pages.pdf)
- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 98-100: Template 21 of 24 there. No AI page for this Play; the prompts are authored for this library. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).
- [Baseline Playbook version](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml). Full source PDF supplied separately.
- Productside Playbook companion document (supplied separately)
