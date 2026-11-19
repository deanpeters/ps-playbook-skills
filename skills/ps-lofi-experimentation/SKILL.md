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

Testing is the primary purpose of lo-fi experimentation. But a lo-fi artifact serves a second, equally valuable function: giving cross-functional stakeholders  -  designers, engineers, executives  -  a concrete, shared picture of the proposed solution before any build investment is made.

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

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

## Application

Use [Template](#template) for the scaffold.


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

**The PM lists the assumptions first**, with their team: what must be true for the solution to create value for the customer and return value to the business. Drafting first is what lets you widen their thinking instead of doing it for them. Then (mirrors the critique guidance in this Play):

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

If the PM asks you to propose the assumptions, or chooses Discovery mode, draft them tagged `[AI-SUGGESTED, VALIDATE THIS]` and run the same tests on them.

### Step 4: Choose the Riskiest, Name the Decision, Define Done

1. **Pressure-test the PM's risk ranking.** For each assumption, ask how likely it is to be wrong and how much it costs if it is. **The PM chooses the single riskiest.** Do not choose for them. State their choice and reason explicitly.
2. **Name the decision** the test will inform. If the PM cannot say what they will do differently based on the result, tell them the test is not worth running yet.
3. **Define done:** the specific behavior that must be observed from customers or users for a pass, across how many people, and what a failure looks like.

These three (riskiest assumption, decision, win-and-failure condition) are the finish line for the experiment.

### Step 5: Write the Hypothesis Statement

Turn the riskiest assumption into a testable If/Then statement (mirrors the critique guidance in this Play):

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

## Template

### When to Use This

Use this template during **Discover + Define** when you have a proposed solution direction (ideally from ps-solution-hypothesis) and need to validate the riskiest assumption about it before committing to build.

Upstream work that feeds this template: ps-solution-hypothesis (the If/Then hypothesis to stress-test), ps-framing-the-problem (the validated problem statement), ps-exploring-solution-space (the solution method selected).

This template produces a commitment artifact. By the time you complete it, you have identified what you believe, designed a test, and committed to acting on the results regardless of outcome.

### Template

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

### Usage Guidance

#### Filling the Template

1. Start with **Product Context** to anchor whose assumption is being tested and which solution direction is under examination.
2. Write **both Key Assumptions** yourselves before selecting one to test. The act of writing both helps identify which is more critical.
3. Fill in the **Finish Line**: choose the riskiest assumption and say why, name the decision the test informs, and define what a pass and a failure look like. Do not imply the selection.
4. Write the **Hypothesis Statement** with a specific threshold before designing the experiment. The threshold drives the metric selection in section 3.
5. Complete all five **Design Experiment** elements. The Decision Rule is required, not optional.
6. Write the **Experiment Description** specific enough to run. This is the field that most often gets left vague.
7. Add **Evidence Notes** only after the artifact is fully complete.

#### What Goes Where

| Section | Contains | Does NOT Contain |
|---------|----------|------------------|
| Key Assumptions | Make-or-break customer behavior or sentiment beliefs | Technical feasibility questions, feature specifications, team preferences |
| Hypothesis Statement | Specific test description + measurable threshold | Full solution description, vague improvement language |
| Design Experiment | Method, Audience, Metric, Time Window, Decision Rule (all five) | General approach without specifics, metric without threshold |
| Experiment Description | Runnable stimulus and task prompts | Marketing pitch, comprehensive product spec |

#### Connecting to Other Skills

- **Upstream:** ps-solution-hypothesis provides the If/Then chain that surfaces the assumptions most worth testing. ps-framing-the-problem provides the validated problem that grounds the solution direction.
- **Downstream:** Results from the experiment feed ps-risk-assessment (once the critical assumption is validated, risks become clearer). ps-product-outcome-canvas (Template 16) draws from a validated solution direction.

#### Capacity Reference

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

## Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For a consultancy onboarding workflow, isolate an uncertain customer behavior, test it with a small prototype, and agree on a decision rule before collecting results.
- **Weak:** "Build the wizard and see whether people like it" leaves both the assumption and decision rule vague.
- **Drift to avoid:** Solution-description bug: an experiment must expose an assumption to failure, not merely describe the planned feature.


## Common Pitfalls

- **Treating Assumptions as Requirements:** An assumption should create doubt. Write each one as something you believe but are not certain of. Ask: "What would we do differently if this turned out to be false?" If the answer is "nothing," it is not a real assumption.

- **Hypothesis Without a Threshold:** Add a specific, countable threshold. At least 65% task completion. Average time under 8 minutes. Three out of five participants request a follow-up demo. Without a number or a specific observable behavior, the hypothesis cannot be falsified.

- **Testing What Is Easy, Not What Is Risky:** Ask which assumption, if false, would most change the solution direction. That is the one to test first, regardless of how uncomfortable the answer might be.

- **Missing the Decision Rule:** Write the decision rule before running the experiment, in the three-tier format: continue / adjust / pivot. The thresholds should create genuine decision points, not foregone conclusions dressed up as rigor.

- **Designing the Experiment as a Pitch:** A lo-fi experiment tests whether the assumption is true, not whether the team can present it compellingly. Include the parts of the experience that are most likely to fail.

- **Describing the Solution Instead of the Test:** The IF clause should describe the minimum stimulus the team can stage this week. "If we show new users a Wizard-of-Oz version of the unified data view..." is a test. "If we build a unified data platform..." is a project.

- **Skipping the Cross-Functional Team:** The playbook explicitly calls for cross-functional participation in Step 1. Assumption identification is a team exercise, not a solo PM task.

- **Building Too Much Before Testing:** Lo-fi means the smallest artifact that generates a clear signal. If staging the experiment requires building the product, something has gone wrong in the design step. Return to the method selection and find a lighter approach.

- **AI Names the Assumptions and Picks the Riskiest:** The PM lists the assumptions and chooses the riskiest. The skill widens the list with candidates marked as candidates, and pressure-tests the ranking by likelihood and cost.

- **A Test That Decides Nothing:** Name the decision and define done (Step 4) before designing anything. Check the finished design against that finish line.

- **Simulated Participants Treated as Signal:** The stimulus can be generated (a vibe-coded prototype is fine). The audience must be real target customers or users. If recruiting them is the hard part, choose a lighter method, not a simulated audience.

## References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-lofi-experimentation) for supporting source material and expanded examples.
