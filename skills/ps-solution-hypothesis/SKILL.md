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

Use [template.md](template.md) for the full scaffold.

See the original three-page playbook source in [assets/ps_solution_hypothesis_playbook_pages.pdf](assets/ps_solution_hypothesis_playbook_pages.pdf).

### Required Output Convention

Default to a **clean, paste-ready solution hypothesis artifact**.

That means:

- fill all five sections in order
- keep each section within its word budget (see Capacity Reference below)
- produce two hypothesis statements that chain together correctly
- explanation belongs below the artifact, not inside the template fields
- the artifact comes first; commentary is secondary

### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in [prompts/01-pressure-test-solution-hypothesis.md](prompts/01-pressure-test-solution-hypothesis.md) one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

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

## Examples

See [examples/sample.md](examples/sample.md).

The example set includes:

- a strong Productside-style solution hypothesis with all five sections, two chained If/Then statements, and specific benefits and risks
- a weak, generic version with vague solution summary, feature-as-benefit language, and a single merged hypothesis
- a drift-bug example showing the hypothesis written as a feature list instead of an If/Then chain
- commentary on why the weak versions fail

## Common Pitfalls

### Pitfall 1: Writing a Feature List Instead of an If/Then Hypothesis

**Symptom:** The "Solution Hypothesis Statement" section lists features: "We will build automated workflows, a self-service portal, and a reporting dashboard."

**Consequence:** The team has a build plan but no expected outcome to validate against. There is no testable prediction, just a list of things to construct.

**Fix:** Rewrite as an If/Then statement. The IF describes the solution. The THEN describes the expected outcome for the customer or business. "IF we provide automated workflows that reduce manual data entry, THEN field engineers will complete inspections 40% faster."

### Pitfall 2: Merging the Two Hypotheses into One

**Symptom:** A single statement tries to cover both customer value and business outcome: "If we build this platform, then customers will be happier and we will grow revenue."

**Consequence:** The chain from customer value to business outcome is lost. The team cannot tell whether they are testing for customer adoption or business impact, and they cannot diagnose which link broke if results disappoint.

**Fix:** Separate into two statements. The customer-focused hypothesis connects solution to customer benefit. The business-focused hypothesis connects customer benefit to business outcome. The THEN of the first becomes the IF of the second.

### Pitfall 3: Making the Solution Summary Too Vague to Test

**Symptom:** "Build a better platform for our customers" or "Create an integrated solution."

**Consequence:** The hypothesis is untestable because the solution is undefined. What platform? Better how? Integrated with what?

**Fix:** The solution summary must be specific enough that someone could design a test for it. "Implement an integrated HR management system with automated task workflows, centralized employee records, and a self-service portal for common requests" is testable.

### Pitfall 4: Listing Generic Risks

**Symptom:** "Things might not work." "There could be challenges." "Users might not adopt it."

**Consequence:** The team has no actionable risk mitigation plan. Generic risks cannot be investigated or resolved.

**Fix:** Each risk should name a specific failure mode. "Resistance to change from employees accustomed to the current manual process" is specific. "Integration with the legacy HRIS may require custom middleware not in the current budget" is specific.

### Pitfall 5: Starting Without a Validated Problem Statement

**Symptom:** The problem statement section is blank or contains a one-line assumption. The hypothesis jumps straight to "here is what we should build."

**Consequence:** The hypothesis solves a problem that may not exist. Without a validated problem, the team cannot tell if the solution is addressing real customer friction or imagined friction.

**Fix:** Complete ps-framing-the-problem first. If that is not possible, at minimum draft a problem statement and flag it as unvalidated. The hypothesis artifact should make visible whether the problem foundation is solid or assumed.

### Pitfall 6: Using Persona Names Instead of Role Names in the Hypothesis

**Symptom:** "IF we save Henry time on manual tasks, THEN Henry will focus on strategic initiatives."

**Consequence:** The hypothesis sounds like it serves one person rather than a customer population. Leadership cannot tell whether this is a scalable solution or a custom accommodation.

**Fix:** Use role names: "IF we save HR specialists time on manual tasks, THEN they will redirect effort to strategic initiatives like talent development and workforce planning."

### Pitfall 7: Writing Benefits That Are Just Restated Features

**Symptom:** The benefits list reads like a feature spec: "Automated data entry. Dashboard reporting. Self-service portal."

**Consequence:** The team confuses what the product does with why it matters. Benefits should answer "so what?" Features answer "what does it do?"

**Fix:** Push each benefit one level further. "Automated data entry" becomes "Time recovered from manual data entry, allowing specialists to focus on higher-value work." The feature is the mechanism; the benefit is the outcome the customer cares about.

### Pitfall 8: Writing a Business-Focused Hypothesis with No Measurable Outcome

**Symptom:** "IF customers are happier, THEN the business will do better."

**Consequence:** There is no way to tell whether the hypothesis was confirmed or refuted. "Do better" is not measurable.

**Fix:** The business outcome must include a specific metric or target: "THEN we will reduce new employee onboarding time by 30%" or "THEN we will increase field inspection completion rates from 60% to 85% per quarter."

### Pitfall 9: AI Writes the Bet

**Symptom:** The PM asks for a solution hypothesis and gets a complete, confident If/Then chain with benefits, risks, and a business outcome.

**Consequence:** No one on the team chose the bet. When the test results come in, nobody knows which link was the real assumption.

**Fix:** The PM drafts the chain; the skill tests each link. Rewrites come after the critique, as options.

## References

### Skill Files

- [template.md](template.md) - working scaffold
- [prompts/](prompts/README.md) - copy-paste prompt for chat-based AI tools (authored for this library; the deck has no AI page for this Play)
- [examples/sample.md](examples/sample.md) - strong, weak, and drift-bug examples

### Related Project Docs

- [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)
- [framework-glossary.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/framework-glossary.md)
- [skill-authoring-workflow.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/skill-authoring-workflow.md)
- [template_conversion_rules.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/template_conversion_rules.md)
- [template_conversion_usage.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/template_conversion_usage.md)

### Related Skills

#### Upstream (input to this skill)

- [ps-framing-the-problem](../ps-framing-the-problem/SKILL.md) - validated problem statement that anchors the hypothesis
- [ps-exploring-solution-space](../ps-exploring-solution-space/) - solution exploration that identifies the proposed solution direction
- [ps-positioning-statement](../ps-positioning-statement/SKILL.md) - positioning work that informs how the solution is framed

#### Downstream (uses output from this skill)

- Outcome tree - the business outcome in hypothesis 2 should align with outcome tree metrics
- Lo-fi experimentation - the testable hypothesis drives experiment design
- Roadmap planning - the validated hypothesis informs what goes on the roadmap

### Source Material

- [Baseline Playbook version](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml). Full source PDF supplied separately.
- [assets/ps_solution_hypothesis_playbook_pages.pdf](assets/ps_solution_hypothesis_playbook_pages.pdf)
- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 57-59: Template 12 of 24 there. No AI page for this Play; the prompts are authored for this library. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).
- Productside Playbook companion document (supplied separately)
