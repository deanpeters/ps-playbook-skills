---
name: ps-lofi-experimentation
description: >-
  Design a lo-fidelity experiment to test a critical solution assumption in
  Productside format. Use when you have a solution hypothesis and need to
  validate it with minimal time and effort before building.
intent: >-
  Help a Product Manager identify the make-or-break assumption in a proposed
  solution, write a measurable If/Then hypothesis, and design the smallest test
  that produces a clear signal, with explicit decision rules that prevent
  post-experiment rationalization.
type: component
blueprint_stage: Discover + Define
best_for:
  - "Designing a cheap, fast experiment to test a critical solution assumption"
  - "Defining pass/fail criteria before running the experiment, not after"
  - "Choosing the right experiment method for the assumption being tested"
scenarios:
  - "I have a solution hypothesis and need to design a cheap experiment to test our riskiest assumption"
  - "Help me pick the right experiment method and define pass/fail criteria before we run it"
---

## Purpose

Design a **Productside-style Lo-fi Experimentation artifact** from a proposed solution.

This skill helps a Product Manager turn a solution hypothesis into a complete, runnable experiment plan:

- two critical make-or-break assumptions
- a measurable If/Then hypothesis statement
- a fully specified experiment design (Method, Audience, Metric(s), Time Window, Decision Rule)
- a description of the experiment stimulus

The point is not to validate every assumption. The point is to identify the one assumption whose falseness would change everything, design the smallest possible test, and commit to action rules before results arrive.

This is a **commitment surface**, not an ideation surface.

## Key Concepts

### A Test Exists to Settle a Decision

Before designing anything, the PM names **the decision the test will inform**. If they cannot say what they will do differently depending on the result, the test is not worth running yet. Then they define **"done"**: the specific behavior that must be observed from customers or users for a pass, across how many people, and what a failure looks like. These set the finish line. The experiment has one job: produce that signal.

### The Signal Comes From Real People

A lo-fi test buys evidence from **real customers or users** reacting to a cheap stimulus. The stimulus can be anything from a paper sketch to a vibe-coded prototype. The audience cannot be simulated. Synthetic users, AI-generated personas, or a model's prediction of how customers would react produce no evidence about customers. (The baseline deck's example used 100 simulated users; the B2B work-in-progress deck replaced it with a Wizard-of-Oz test on real passengers.)

### The Least You Can Build

Every method should be cheaper and faster than building the real thing. Keep asking: what is the least we could build to get a real signal? Steer away from anything that looks like a working version of the product.

### Lo-fi Means Fast, Not Cheap

The goal of lo-fi experimentation is signal speed, not cost reduction. A $50 user test that answers the question in two days beats a $500 study that takes six weeks. The constraint is time-to-signal, not budget.

### The Assumption Must Be Make-or-Break

Not every assumption needs an experiment. The right assumption to test is the one that, if false, means the solution approach is wrong. Assumptions about preferences, edge cases, or technical implementation are secondary. The critical assumption is the one that sits under the solution's entire value proposition.

Productside criteria for a valid assumption:
- **Make-or-break**: if this is false, the solution approach changes significantly
- **About behavior or sentiment**: something a customer would do, feel, or believe - not an internal team capability
- **Testable this week**: specific enough that a test can produce a result within days, not months

### The Lo-fi Hypothesis Differs from the Solution Hypothesis

The Solution Hypothesis (from ps-solution-hypothesis) chains: IF we provide this solution, THEN customers benefit, THEN the business achieves an outcome.

The lo-fi hypothesis is different. It describes a specific test and a specific observable signal:

"If we [expose customers to this stimulus], then [we will observe this specific, measurable result]."

The IF describes the test. The THEN describes an observable, countable result with a threshold.

### The Decision Rule Prevents Rationalization

Specifying thresholds before results arrive forces the team to act on results rather than explain them away. The three-tier structure (continue / adjust / pivot) creates genuine decision points. Without it, teams find a way to continue regardless of what they learned.

### Lo-fi Artifacts Are Also Communication Tools

Testing is the primary purpose of lo-fi experimentation. But a lo-fi artifact serves a second, equally valuable function: giving cross-functional stakeholders — designers, engineers, executives — a concrete, shared picture of the proposed solution before any build investment is made.

A clickable prototype or Wizard-of-Oz simulation makes the product concept tangible enough for meaningful conversation. It surfaces disagreements about user experience early, when the cost of changing direction is low. Product leaders can also use lo-fi artifacts to share the product vision with executives, making the problem and proposed solution vivid in a way that slides and written descriptions cannot.

The artifact you build to test an assumption also becomes the artifact that aligns the team.

### Experiment Types from the Productside Catalog

- **Clickable prototype**: interactive mockup without working code
- **Wizard-of-Oz**: human-powered backend that looks automated to the user
- **Concierge**: PM or team member manually does the job for the customer to simulate the solution
- **Explainer Video**: short video that describes the solution and captures intent or reaction
- **Landing page test**: describes the offer and measures signups, clicks, or stated interest
- **Paper prototype**: hand-drawn or printed screens walked through with customers
- **Price sheet**: tests willingness-to-pay without a working product
- **Ad concept**: tests whether the value proposition generates interest
- **Fake door**: offers a feature or product that does not exist yet and measures who tries to use it
- **Vibe-coded prototype**: a quickly generated, throwaway interactive mockup used as the stimulus; real people still do the reacting

### How AI Supports This Play

The Playbook casts AI as a **thought partner in two moments**. First, after the PM lists what must be true for the solution to pay off, AI widens the view toward assumptions the PM cannot see alone and pressure-tests which one is genuinely riskiest. Then it helps design the smallest, fastest test that could prove the PM wrong.

The reasoning stays with the PM. They name the assumptions, rank the risk, decide what a pass looks like, and decide what they will do about it. If AI hands over the riskiest assumption, the PM has skipped the thinking that shows whether they understand their own idea. AI sharpens the probe. The signal comes from real people, never from the model.

- **Use it when:** there is a prioritized solution, and the PM wants to find the riskiest assumption under it and design a cheap, fast experiment that drives a real decision.
- **Avoid it when:** the problem, persona, or solution is still vague. AI will manufacture confident assumptions and a tidy test with nothing real beneath them. Route back to ps-solution-hypothesis or ps-framing-the-problem.
- **Return:** blind-spot assumptions raised as candidates for the PM to weigh, a single riskiest assumption tied to a decision, and the smallest test that produces a real pass-or-fail signal.

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

See the source play pages in [assets/ps_lofi_experimentation_playbook_pages.pdf](assets/ps_lofi_experimentation_playbook_pages.pdf).

### Required Output Convention

Default to a **clean, paste-ready artifact** with all four sections complete:

- exactly 2 key assumptions
- 1 hypothesis statement for the selected assumption
- a fully specified experiment design (all five elements)
- an experiment description specific enough to run

Explanation belongs below the artifact, not inside the fields.

### Step 1: Apply the Tech-Role Bias Guard

Before identifying assumptions, verify the proposed solution addresses a customer-side problem, not an internal engineering or tooling challenge.

The assumptions to test should be about customer behavior, customer value, or customer adoption. If the assumptions are primarily technical implementation questions ("can we build this?"), redirect to a technical spike rather than a lo-fi experiment.

Ask: Who is experiencing the problem this solution addresses? If the answer is the development team or internal stakeholders rather than end users or buyers, pause and reframe.

### Step 2: Collect Artifacts

Ask whether the user has materials to supply that would ground the experiment in evidence:

- the solution hypothesis from ps-solution-hypothesis (the If/Then chain)
- the framing-the-problem output (the five-stem problem statement)
- any prior customer feedback on the solution direction
- empathy interview notes that speak to adoption or behavior change
- any earlier lo-fi results that inform what to test next

The experiment should test the riskiest assumption embedded in the solution hypothesis. The more the user can supply, the more the assumption selection is grounded in real discovery rather than team intuition.

If there are no upstream artifacts at all, say so and note that the assumptions and experiment plan will be first-pass hypotheses requiring more grounding.

### Step 3: Record and Widen the Assumptions

**The PM lists the assumptions first**, with their team: what must be true for the solution to create value for the customer and return value to the business. Drafting first is what lets you widen their thinking instead of doing it for them. Then (mirrors [prompts/01](prompts/01-find-riskiest-assumption.md)):

1. **Widen the list.** Ask what they may be taking for granted across customer behavior, adoption, and the business. You may name candidate assumptions they missed, marked as candidates for them to judge, not facts.
2. **Test each against the bar:**
   - **Make-or-break**: if this turns out to be false, the solution approach changes significantly
   - **About behavior or sentiment**: something a customer would do, feel, or believe, not an internal team capability or a feature specification
   - **Testable this week**: specific enough that a test produces a clear result within days

   Push the PM to cut the ones that fail.

Each assumption is a factual belief statement, not a question:

Good: "New users expect to complete account setup in a single session without help."
Weak: "Will users be able to complete setup?" (this is a question, not an assumption)
Weak: "The system will support single-session onboarding." (this is a technical capability, not a customer behavior)

The template holds **two key assumptions**: the two that most threaten the solution if false.

If the PM asks you to propose the assumptions, or chooses best guess mode, draft them tagged `[AI-SUGGESTED, VALIDATE THIS]` and run the same tests on them.

### Step 4: Choose the Riskiest, Name the Decision, Define Done

1. **Pressure-test the PM's risk ranking.** For each assumption, ask how likely it is to be wrong and how much it costs if it is. **The PM chooses the single riskiest.** Do not choose for them. State their choice and reason explicitly.
2. **Name the decision** the test will inform. If the PM cannot say what they will do differently based on the result, tell them the test is not worth running yet.
3. **Define done:** the specific behavior that must be observed from customers or users for a pass, across how many people, and what a failure looks like.

These three (riskiest assumption, decision, win-and-failure condition) are the finish line for the experiment.

### Step 5: Write the Hypothesis Statement

Turn the riskiest assumption into a testable If/Then statement (mirrors [prompts/02](prompts/02-design-leanest-test.md)):

"If we [describe what we will expose the customer to or simulate], then [describe the specific observable result we expect to see]."

The THEN predicts a **behavior the PM can observe**, not a feature they would build. If it predicts a feature, make them fix it. It must include a numeric threshold or a specific observable behavior. "Users will find it easier" is not a hypothesis. "At least 70% of users will complete the task without requesting help" is.

The IF describes the test, not the full solution. "If we build a unified dashboard" is a solution description. "If we give new users a clickable prototype with a unified dashboard" is a test description.

### Step 6: Design the Experiment

**Suggest two or three lightweight methods** (Wizard-of-Oz, concierge, fake door, vibe-coded prototype, explainer video, or others from the catalog). For each, ask what the least the team could build to get a real signal is. Steer away from anything that looks like a working version of the product.

Then help the PM complete all five elements. **The PM sets the metric, the time window, and the decision rule.** Question them; do not set them.

- **Method**: the specific lo-fi approach from the Productside catalog (clickable prototype, Wizard-of-Oz, Concierge, Explainer Video, landing page, paper prototype, price sheet, ad concept, fake door, vibe-coded prototype, or a clearly named equivalent)
- **Audience**: **real** target customers or users, and how they will be recruited (role, number, source). Never simulated participants.
- **Metric(s)**: the specific observable, countable thing to measure, mapped to the win condition, not satisfaction scores or vague impressions
- **Time Window**: the start and end date or duration of the experiment, with a real end
- **Decision Rule**: exactly three tiers specifying what the team will do if results exceed, meet, or fall below the threshold

The Decision Rule is required. Write it as:
- [threshold A] or above: continue as planned
- [threshold B] to [threshold A minus 1]: adjust [specify what changes]
- Below [threshold B]: pivot [specify what the pivot means]

**Check the whole design against the finish line:** would this test settle the decision? Does it give customers or users the chance to demonstrate the behavior the PM wants to observe? If not, show where it falls short.

### Step 7: Describe the Experiment

Provide enough detail about what will be shown, said, or demonstrated that someone could run the experiment without redesigning it from scratch.

Include:
- the stimulus (mockup description, script, link, price sheet text, or ad copy)
- the core wording the customer will see or hear
- any task prompts or scenarios presented to participants

This section corresponds to the large right panel on the playbook template ("Visual or detailed text for your experiment").

Keep the description under 150 words. The goal is runnable clarity, not comprehensive specification.

### Step 8: Add Optional Evidence Notes

If useful, add a brief trailing section with:

- what assumption remains untested after this experiment
- what the recommended next experiment would be
- any open risks not addressed by this experiment

Add this section only after the artifact is fully complete.

### Step 9: Offer Next Steps

After completing the artifact, offer three options:

1. Run the experiment and return with results for interpretation
2. Design a second experiment for the remaining assumption
3. Proceed to ps-risk-assessment once the critical assumption is validated

## Examples

See [examples/sample.md](examples/sample.md).

The example set includes:

- a strong Productside-style lo-fi experiment plan
- a weak version with the most common failure modes
- a drift-bug example with a specific named failure and fix guidance

## Common Pitfalls

### Pitfall 1: Treating Assumptions as Requirements

**Symptom:** Every assumption reads as a settled fact or a design decision rather than an uncertain belief.

**Consequence:** There is nothing to test. The "experiment" confirms what was already decided.

**Fix:** An assumption should create doubt. Write each one as something you believe but are not certain of. Ask: "What would we do differently if this turned out to be false?" If the answer is "nothing," it is not a real assumption.

### Pitfall 2: Hypothesis Without a Threshold

**Symptom:** The THEN reads as a vague directional improvement: "customers will find it easier," "users will be more engaged," "adoption will improve."

**Consequence:** Any result can be interpreted as confirmation. The decision rule becomes meaningless.

**Fix:** Add a specific, countable threshold. At least 65% task completion. Average time under 8 minutes. Three out of five participants request a follow-up demo. Without a number or a specific observable behavior, the hypothesis cannot be falsified.

### Pitfall 3: Testing What Is Easy, Not What Is Risky

**Symptom:** The selected assumption is one the team is fairly confident about. The harder, more uncertain assumption is left untested.

**Consequence:** The experiment produces confidence without reducing real risk.

**Fix:** Ask which assumption, if false, would most change the solution direction. That is the one to test first, regardless of how uncomfortable the answer might be.

### Pitfall 4: Missing the Decision Rule

**Symptom:** The experiment has a metric but no specification of what the team will do based on results.

**Consequence:** Post-experiment rationalization. The team finds a way to continue regardless of what the data shows.

**Fix:** Write the decision rule before running the experiment, in the three-tier format: continue / adjust / pivot. The thresholds should create genuine decision points, not foregone conclusions dressed up as rigor.

### Pitfall 5: Designing the Experiment as a Pitch

**Symptom:** The experiment shows only the best-case scenario. Weak spots are omitted. The stimulus is polished marketing material rather than a minimal testable artifact.

**Consequence:** Results reflect how well the team can sell the idea, not whether the assumption holds.

**Fix:** A lo-fi experiment tests whether the assumption is true, not whether the team can present it compellingly. Include the parts of the experience that are most likely to fail.

### Pitfall 6: Describing the Solution Instead of the Test

**Symptom:** The IF clause describes the final solution: "If we build a unified data platform, then..."

**Consequence:** The hypothesis becomes untestable until the solution is built. This is not a lo-fi experiment; it is a roadmap item.

**Fix:** The IF clause should describe the minimum stimulus the team can stage this week. "If we show new users a Wizard-of-Oz version of the unified data view..." is a test. "If we build a unified data platform..." is a project.

### Pitfall 7: Skipping the Cross-Functional Team

**Symptom:** The PM identifies assumptions alone without input from design, engineering, or customer success.

**Consequence:** Assumptions miss risks that other functions see clearly. Engineering knows what is technically fragile. Customer success knows what customers complain about most. Design knows where the UX is most likely to confuse.

**Fix:** The playbook explicitly calls for cross-functional participation in Step 1. Assumption identification is a team exercise, not a solo PM task.

### Pitfall 8: Building Too Much Before Testing

**Symptom:** The experiment design requires multiple sprints of engineering work, a fully functioning API, or a production-ready UI.

**Consequence:** The team has already committed significant resources before testing the assumption. The lo-fi phase has been skipped.

**Fix:** Lo-fi means the smallest artifact that generates a clear signal. If staging the experiment requires building the product, something has gone wrong in the design step. Return to the method selection and find a lighter approach.

### Pitfall 9: AI Names the Assumptions and Picks the Riskiest

**Symptom:** The PM asks "what must be true for this to work?" and "which is riskiest?" and adopts the answers.

**Consequence:** The risk ranking is borrowed, not reasoned. Blind spots stay invisible to the PM, and they skip the thinking that would show whether they understand their own idea.

**Fix:** The PM lists the assumptions and chooses the riskiest. The skill widens the list with candidates marked as candidates, and pressure-tests the ranking by likelihood and cost.

### Pitfall 10: A Test That Decides Nothing

**Symptom:** The experiment is bigger than the question needs, or it gathers "nice-to-know" evidence. No one wrote down what decision the result feeds, or what a pass looks like.

**Consequence:** The results arrive, everyone finds them interesting, and nothing changes. Or the test takes a month to answer a one-week question.

**Fix:** Name the decision and define done (Step 4) before designing anything. Check the finished design against that finish line.

### Pitfall 11: Simulated Participants Treated as Signal

**Symptom:** The "audience" is synthetic users, AI-generated personas, or a model asked how customers would react. "We ran 100 simulated users through the prototype."

**Consequence:** No customer was involved, so no customer evidence was produced. The team acts on the model's predictions as if they were behavior.

**Fix:** The stimulus can be generated (a vibe-coded prototype is fine). The audience must be real target customers or users. If recruiting them is the hard part, choose a lighter method, not a simulated audience.

## References

### Skill Files

- [template.md](template.md) - assumptions, hypothesis, experiment design, and experiment description
- [prompts/](prompts/README.md) - copy-paste prompts for chat-based AI tools (2: find the riskiest assumption and define done, design the leanest test)
- [examples/sample.md](examples/sample.md) - strong, weak, and drift-bug examples

### Related Skills



### Related Project Docs

- [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)
- [framework-glossary.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/framework-glossary.md) (Hypothesis, Experiment, Assumption)
- [skill-authoring-workflow.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/skill-authoring-workflow.md)

### Adjacent Skills

- **Upstream:** [ps-solution-hypothesis](../ps-solution-hypothesis/SKILL.md) (provides the hypothesis to stress-test), [ps-framing-the-problem](../ps-framing-the-problem/SKILL.md), [ps-problem-identification](../ps-problem-identification/SKILL.md)
- **Downstream:** ps-risk-assessment (Template 15), ps-product-outcome-canvas (Template 16)

### Source Material

- [Baseline Playbook version](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml). Full source PDF supplied separately.
- [assets/ps_lofi_experimentation_playbook_pages.pdf](assets/ps_lofi_experimentation_playbook_pages.pdf)
- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 65-70: Template 14 of 24 there, with the AI overview on slide 67 and prompts on slides 68, 69. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).
- Productside Playbook companion document (supplied separately)
