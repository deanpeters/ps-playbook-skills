---
name: psk-tiny-acts-discovery
description: >-
  Run continuous assumption validation through small, fast tests. Use at any
  phase of the product lifecycle to keep the team calibrated on what they know,
  what they don't, and what to test next.
intent: >-
  Help a Product Manager maintain a continuous practice of assumption validation
  using the Productside Tiny Acts of Discovery framework - a five-step flow from
  validated knowns to classified unknowns to field-ready tests - so the team
  always knows what is proven, what is open, and what small, fast test to run
  next before committing further resources.
type: process
blueprint_stage: Create
best_for:
  - "Running continuous assumption validation through small, fast tests"
  - "Building a team habit of testing assumptions rather than debating them"
  - "Maintaining discovery momentum at any phase of the product lifecycle"
scenarios:
  - "I want to run quick assumption tests with my team without waiting for a formal experiment"
  - "Help me set up a tiny acts session to validate three assumptions we have been debating"
---


## Purpose

Create a **Productside-style Tiny Acts of Discovery artifact** from a collaborative team session on a product at any stage of development.

This skill helps a Product Manager and their team build an ongoing habit of assumption validation. The playbook states explicitly: "This tool can be used in many phases of a product process or lifecycle." Although it is placed in the Create phase, it applies equally in Discover, Define, and after launch.

This is a **process skill**. The agent helps the PM plan and document the exercise. Steps 1 through 4 (what we know, what we don't, prioritizing assumptions, writing hypotheses) happen in the conversation. Step 5 (running the tiny acts with real users, customers, or data) happens in the field. The agent cannot conduct interviews, run surveys, or generate user research findings on the team's behalf.

The goal is not a single checkpoint. The goal is a culture of continuous learning - what the playbook calls "fail often, fail fast." Failures are data, not setbacks.

### Usage Notes

This is a **process skill**. The agent helps the PM plan and document the exercise. Steps 5 (running the tiny acts) happen in the field with real users, customers, or data. The agent does not conduct research or generate synthetic findings.

The skill applies at multiple lifecycle phases, not only Create. The playbook states explicitly: "This tool can be used in many phases of a product process or lifecycle."

Downstream connections: Outcome-Based Roadmap (Template 17) - specifically "Outputs to Develop," "Output Concepts to Validate," "Assumptions to Validate," and "Assumptions to Research" sections.

Related skill for single high-stakes assumptions: psk-lofi-experimentation (Template 14).

## Key Concepts

### The Five-Step Flow

The exercise follows a fixed sequence:

1. **What do we know?** - Validated facts, observed behaviors, completed research, confirmed assumptions.
2. **What do we not know?** - Gaps, unvalidated assumptions, open questions, missing data.
3. **Prioritize your assumptions** - Classify each "don't know" by impact and uncertainty on a 2x2.
4. **Form your hypotheses** - Write If/Then statements for the top-priority assumptions.
5. **List your Tiny Acts of Discovery** - Design one small, fast test per hypothesis, assign a metric and an owner.

### A Living Backlog, Not a One-Time List

Tiny acts of discovery is a **habit**: keep a prioritized backlog of assumptions about the product and chip away at it with small, fast acts of learning, over and over. Re-score the backlog whenever new evidence arrives, and keep it where stakeholders can see it. A tiny act can be almost anything: one question to one user, a survey, a fake-door or willingness-to-pay test, a five-person expert chat, a quick prototype. The craft is finding the shortest path to a signal.

A backlog that never gets worked is planning, not discovery. If no act ever runs, the exercise has failed, however tidy the list.

### The Certainty Score Is the PM's

Only the PM knows how much evidence they actually hold, so **the PM places every assumption** on impact and certainty. The skill pushes on the evidence ("what is it, and how confident are you in it?") and points at placements that look off. It does not move them. A backlog scored by a model is built on the model's guesses, and no one can explain why this, why now.

### Impact vs. Uncertainty

The 2x2 matrix uses two dimensions:

- **Impact (Y-axis):** If this assumption turns out to be wrong, how much does it damage the product goal? High impact = major rework or goal failure. Low impact = minor friction.
- **Uncertainty (X-axis):** How much evidence do you currently have? High uncertainty = little or no evidence (the opposite of confidence). Low uncertainty = some evidence already exists.

**This is not the same as Output Prioritization**, which uses Value vs. Cost/Effort. Here, the dimensions are the cost of being wrong and the absence of supporting evidence. High impact + high uncertainty = most urgent to test. These go in the upper-right of the matrix.

### How to Classify an Assumption

Two questions determine placement:

- "If we are wrong about this, does the product goal fail or require major rework?" - this sets Impact.
- "How much evidence do we currently have that supports this being true?" - the less evidence, the higher the Uncertainty rating.

### Tiny Acts vs. Lo-fi Experimentation

These are related but not interchangeable:

- **Lo-fi Experimentation (Template 14)** is a formal, structured test plan for a single make-or-break assumption. It specifies a full hypothesis with a numeric threshold, a complete method, decision rules with three tiers, a time window, and an audience size. Use Lo-fi when you need a rigorous, documented test before committing to a major build decision.
- **Tiny Acts of Discovery** is for ongoing, lightweight assumption management across many assumptions simultaneously. Tests are smaller. Documentation is lighter. The intent is a culture of continuous learning, not one big formal experiment. Use Tiny Acts when you want to test many assumptions quickly and keep the team calibrated week to week.

A PM who uses Tiny Acts well will identify the single highest-stakes assumption that needs Lo-fi treatment. The two tools work together.

### Tiny Acts Keep Development Customer-Focused

The purpose of Tiny Acts of Discovery is to anchor product decisions in what real customers actually do, need, and believe  -  not in what the team assumes from the inside. Every assumption worth testing should trace back to a customer behavior, a customer value question, or a customer adoption question.

When the team runs these exercises honestly, they replace internal debate with evidence. A user walkthrough result, a data pull, a survey response  -  these are the inputs that make the development process data-driven rather than opinion-driven. The team learns what customers genuinely need before committing resources to build it.

This is why a "don't know" list composed entirely of technical unknowns misses the point. Technical assumptions matter, but the assumptions that most often determine whether a product succeeds are behavioral and organizational: will customers change their current workflow, does the customer agree the problem is worth solving, will the organization adopt it? Centering Tiny Acts on these questions keeps development focused on meeting actual user needs.

### The Culture of Continuous Learning

The playbook frames this as "fail often, fail fast." Each tiny act is a deliberate, low-cost way to get signal before investing in something bigger. A test that disproves a hypothesis is not a failure - it is learning that prevents a more expensive mistake downstream. Teams that skip this practice tend to discover wrong assumptions after significant time and money have been spent.

### Why the Agent Cannot Run the Acts

The tiny acts are field research: user interviews, prototype walkthroughs, data pulls, A/B tests, short surveys administered to real customers. The agent can help design the specific acts, define the metrics, and document results when the PM returns with findings. It cannot conduct research, generate synthetic user responses as if they were real, or simulate field data.

### How AI Supports This Play

The Playbook casts AI as a **thought partner across the loop**. The PM collects the opportunities and names the assumptions beneath them. AI widens the view and tests how confident the PM really is. The PM picks what to learn next.

- **Use it when:** the PM has a pile of opportunities, ideas, or signals and wants a prioritized backlog of assumptions plus fast, cheap ways to start testing them.
- **Avoid it when:** the backlog is being used to look busy. If no act ever gets run, the skill is helping the team plan instead of discover. Ask which act will run this week.
- **Return:** raw opportunities turned into testable assumptions, the PM's impact and certainty ranking pressure-tested, and a wide range of fast, creative ways to start learning.

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

Default to a **clean, paste-ready artifact**.

That means:

- at least 3 items in the "what we know" list, grounded in evidence
- at least 3 items in the "what we don't know" list, covering a range of assumption categories
- all assumptions classified on both dimensions (impact and uncertainty)
- a clear top-3 emerging from the classification
- one If/Then hypothesis per top-priority assumption
- one tiny act per hypothesis, with a specific metric and a named owner
- explanation belongs below the artifact, not inside the fields

### Step 1: Confirm Scope and Session Context

Before starting, confirm three things:

1. **What product is this?** Get a one-sentence description of what the product does and who it is for. Vague product descriptions produce vague assumption lists.
2. **What lifecycle phase is the team in?** Tiny Acts applies at any phase, but the categories of unknowns differ. A team in early discovery has mostly behavioral and market unknowns. A team in late Create has mostly technical and adoption unknowns.
3. **Who is in this session?** Tiny Acts is a team exercise. The assumption list should reflect cross-functional perspectives. If the PM is working alone, note this  -  solo lists tend to be narrower and may miss organizational, adoption, and customer-behavior assumptions.

If the PM is working alone without team input, recommend they share the output with one or two stakeholders before designing the tiny acts.

### Step 2: Tech-Role Bias Guard

Before building the assumption list, confirm what the product does and who actually uses it. Most products do not serve developers or technical architects. A supply chain management platform serves logistics coordinators and warehouse managers. A clinical data platform serves clinical operations leads and data managers. A field service app serves technicians and dispatchers.

Ask the PM directly: "Who is the person who will use this product day-to-day? What is their job title and what does their work look like?" This answer should shape every assumption on the list - the knowns, the unknowns, the hypotheses, and the tiny acts.

Do not allow the assumption list to default to technical unknowns (performance, integration, security) while missing the behavioral and organizational unknowns that most often determine whether a product succeeds.

### Step 3: Gather Available Artifacts

Before drafting, ask whether the user has relevant materials to share:

- Solution hypothesis from psk-solution-hypothesis (defines what is being tested)
- Problem statement from psk-framing-the-problem (gives the customer and problem context)
- Outcome tree from psk-outcome-tree (clarifies what the team is trying to achieve)
- Any prior research, field observations, or customer feedback already collected
- Existing roadmap items or backlog priorities (these often reveal implicit assumptions)

The more context about what is being built and for whom, the more targeted the assumption list will be. Accept equivalent context from any source - the PM does not need to have run these upstream plays first.

### Step 4: List What the Team Knows

Help the PM articulate the validated knowns. Push for evidence, not belief. For each item on the "what we know" list, the PM should be able to say where the knowledge came from: an interview, a data pull, a completed test, direct observation, signed research.

Watch for three failure modes:
- Assumptions dressed up as facts ("We know customers want faster reports" with no evidence)
- Old knowledge that has not been revalidated since the product changed
- Team consensus that has never been tested outside the building

Prompt: "How do you know this? What was the source?" If the PM cannot answer, move the item to the "don't know" list.

### Step 5: List What the Team Does Not Know

Help the PM surface the gaps. Push for breadth across assumption categories, not just technical unknowns:

- **Behavioral:** Will customers change their current workflow? How do they currently do this without the product?
- **Adoption:** Who will champion this internally at the customer organization? Who will resist?
- **Organizational:** Does the customer organization have the capacity and authority to change this process?
- **Market:** Are there alternatives customers will choose instead? How strong is the status quo pull?
- **Value:** Does the customer agree the problem is worth solving? Will they pay or advocate for access?
- **Technical:** Can the product deliver the capability at the required performance and reliability?

A list of unknowns that is all technical has not been done honestly.

### Step 6: Classify Assumptions by Impact and Uncertainty

**The PM classifies; the skill challenges** (mirrors the critique guidance in this Play). First help the PM state each item as an assumption: the thing that must be true for it to matter. If their version is vague or hides two assumptions, make them tighten it; react to theirs rather than writing it. Then for each assumption ask two questions: how much would it change product or business decisions if it were true (impact), and how much real evidence they hold (uncertainty). Push hardest on the evidence: what is it, and how confident are they in it? Where a placement looks off given what they just said, point at it and make them reconsider. Do not move it yourself, and do not invent evidence or confidence.

If the PM asks you to classify, or chooses Discovery mode, draft the classification tagged `[AI-SUGGESTED, VALIDATE THIS]` and say plainly that uncertainty depends on evidence only the PM can see.

The two dimensions:

**Impact (H/M/L):**
- H: If this assumption is wrong, the product goal fails or major rework is required
- M: If wrong, significant delay or partial goal failure
- L: If wrong, minor friction or minor rework

**Uncertainty (H/M/L):**
- H: Little or no evidence currently exists to support this assumption
- M: Some evidence exists but it is incomplete or indirect
- L: Reasonable evidence exists; this is more a confirmation question

Present the classification as a table. Do not try to render the visual quadrant - a structured classification table with columns for Assumption, Impact, Uncertainty, and Priority communicates the same information in a paste-ready format.

Derive Priority from the combination:

| Impact | Uncertainty | Priority |
|--------|-------------|----------|
| H | H | Urgent |
| H | M | High |
| H | L | Monitor |
| M | H | High |
| M | M | Medium |
| M | L | Low |
| L | H | Medium |
| L | M | Low |
| L | L | Deprioritize |

### Step 7: Identify the Top 3 Priority Assumptions

From the PM's classification, the PM picks the top 3 (those rated Urgent or High, or the top 3 by priority if fewer than 3 are Urgent/High). These become the inputs to Step 8.

If the PM's top 3 are all in the same category (all technical, all behavioral), flag this. A set of top-priority assumptions that clusters in one area usually means the team has not been honest about breadth.

### Step 8: Write Hypotheses for the Top 3 Assumptions

For each top-priority assumption, write an If/Then hypothesis:

**Format:** "If [we do or provide X], then [we expect Y outcome] because [reasoning]."

Or for outcome-focused framing: "By achieving [specific outcome or metric], we can [achieve the goal]."

A strong hypothesis names a specific observable result, not a vague positive feeling. "Then customers will complete onboarding in under 10 minutes" is testable. "Then customers will like the experience" is not.

### Step 9: Design Tiny Acts for Each Hypothesis

For each hypothesis, find the fastest path to a real signal (mirrors the critique guidance in this Play):

1. Ask what the PM would do differently based on the answer. If nothing, pick a different assumption.
2. Brainstorm a **wide, creative range** of tiny acts in different shapes: a conversation, an observation, a survey, a small build, a pricing or behavior test, a fake door, a five-person expert chat. Don't default to the same few method names.
3. For each, ask the PM what signal it would produce, and how fast and cheap it is.
4. Push toward the single fastest act that still gives a real signal: "What is the least we could do this week to learn this?" **The PM picks the act.**
5. Help them name the measure and the owner. Do not invent results.

Each act is a small, fast, cheap test. A tiny act should be completable in days, not weeks. It should involve real people or real data, not synthetic substitutes.

The table has three columns:

- **Tiny Act of Discovery:** the specific test (e.g., "5-person usability walkthrough of prototype checkout flow," "pull 30 days of support ticket data and tag by root cause," "survey 20 current users on their existing workaround")
- **Measure / Metric to be Collected:** the specific signal that will indicate whether the hypothesis holds (e.g., "task completion rate above 80%," "percentage of tickets attributed to missing export function," "percentage who rate current workaround as 'inadequate'")
- **Assigned:** the named team member responsible for running this act

Watch for two failure modes:
- Acts that are too large (a six-week A/B test is not tiny)
- Acts with no metric assigned (untestable hypotheses produce no signal)
- Acts with no owner assigned (unowned tests do not get run)

### Step 10: Note the Process Boundary

After completing the artifact, be explicit with the PM: the next step is running the tiny acts in the field. This means contacting real users, running the test, collecting the signal, and returning with findings.

Offer to help document results when the PM returns. The typical return conversation looks like: "We ran the walkthrough. Here is what we saw." The agent can then help the PM update the assumption classification, identify which hypotheses were supported or disproved, and decide what the next round of tiny acts should address.

### Step 11: Offer Next Steps

At the end of the artifact, offer three options:

1. Run the tiny acts and return with findings - the agent will help document results and update the assumption map
2. If one assumption from Step 6 stands out as uniquely high-stakes, convert it into a formal Lo-fi Experimentation plan using psk-lofi-experimentation
3. Feed confirmed results into the Outcome-Based Roadmap (Template 17): the "Outputs to Develop," "Output Concepts to Validate," and "Assumptions to Validate / Research" sections draw directly from Tiny Acts findings

## Template

**Product:** [name the product]
**Customer:** [name the role that uses or buys this product day-to-day - not the PM, not the team]
**Date:** [date of session]
**Participants:** [names and roles]

---

### Step 1: What Do We Know?

List what the team currently knows about the product and its users. These are validated facts, observed behaviors, completed research, and confirmed assumptions. For each item, note the source.

| What We Know | Source |
|---|---|
| [Specific, verified fact about customer behavior or product] | [interview date, data pull, completed test, field observation] |
| [Specific, verified fact about customer behavior or product] | [interview date, data pull, completed test, field observation] |
| [Specific, verified fact about customer behavior or product] | [interview date, data pull, completed test, field observation] |
| [Add more rows as needed] | |

**Quality check:** Can you name a source for each item? If not, move it to Step 2.

---

### Step 2: What Do We Not Know?

List the gaps: unknown customer behaviors, unvalidated assumptions, open questions, missing data. Cover a range of categories - behavioral, adoption, organizational, market, value, and technical.

- [Unknown or unvalidated assumption - behavioral]
- [Unknown or unvalidated assumption - adoption or organizational]
- [Unknown or unvalidated assumption - market or value]
- [Unknown or unvalidated assumption - technical]
- [Add more as needed]

**Quality check:** Does this list include unknowns beyond technical ones? Are there behavioral, adoption, and organizational questions here?

---

### Step 3: Prioritize Your Assumptions

Classify each item from Step 2 by Impact and Uncertainty.

- **Impact:** H = product goal fails or major rework required if wrong; M = significant delay or partial goal failure; L = minor friction or rework
- **Uncertainty:** H = little or no supporting evidence; M = some evidence, incomplete or indirect; L = reasonable evidence exists

| Assumption | Impact (H/M/L) | Uncertainty (H/M/L) | Priority |
|---|---|---|---|
| [Assumption from Step 2] | H/M/L | H/M/L | Urgent / High / Medium / Low / Deprioritize |
| [Assumption from Step 2] | H/M/L | H/M/L | Urgent / High / Medium / Low / Deprioritize |
| [Assumption from Step 2] | H/M/L | H/M/L | Urgent / High / Medium / Low / Deprioritize |
| [Add more rows as needed] | | | |

**Priority reference:**

| Impact | Uncertainty | Priority |
|---|---|---|
| H | H | Urgent |
| H | M | High |
| H | L | Monitor |
| M | H | High |
| M | M | Medium |
| M | L | Low |
| L | H | Medium |
| L | M | Low |
| L | L | Deprioritize |

**Quality check:** Is everything Urgent? If so, push the team to differentiate. Are the top priorities spread across at least two different assumption categories?

---

### Step 4: Form Your Hypotheses

Take the top 3 assumptions from Step 3 (Urgent or High priority). Write an If/Then hypothesis for each.

**Format:** "If [we do or provide X], then [we expect a specific, observable Y] because [reasoning]."

**Hypothesis 1** (for: [name the assumption])

> If [action or stimulus], then [specific observable result], because [reasoning].

**Hypothesis 2** (for: [name the assumption])

> If [action or stimulus], then [specific observable result], because [reasoning].

**Hypothesis 3** (for: [name the assumption])

> If [action or stimulus], then [specific observable result], because [reasoning].

**Quality check:** Does each THEN clause name a specific observable result? "Customers will complete the task in under 5 minutes" is testable. "Customers will be satisfied" is not.

---

### Step 5: List Your Tiny Acts of Discovery

For each hypothesis, design one small, fast, cheap test. Each act should be completable in days, not weeks.

| Hypothesis | Tiny Act of Discovery | Measure / Metric to be Collected | Assigned |
|---|---|---|---|
| Hypothesis 1 | [Specific test: 5-person walkthrough, data pull, short survey, etc.] | [Specific signal: threshold, count, or observable event] | [Named person] |
| Hypothesis 2 | [Specific test: 5-person walkthrough, data pull, short survey, etc.] | [Specific signal: threshold, count, or observable event] | [Named person] |
| Hypothesis 3 | [Specific test: 5-person walkthrough, data pull, short survey, etc.] | [Specific signal: threshold, count, or observable event] | [Named person] |

**Quality check:**
- Is each act completable in days, not weeks?
- Does each act have a named metric? ("See if they like it" is not a metric.)
- Does each act have a named owner? (Unowned acts do not get run.)

---

### Next Steps

[ ] Run the tiny acts in the field
[ ] Document results and return to update the assumption classification
[ ] Schedule the next Tiny Acts session: [date]

**When you return with findings:** Share what you observed. The agent will help document results, identify which hypotheses were supported or disproved, and decide what the next round of tiny acts should address.

**If one assumption stands out as uniquely high-stakes:** Consider converting it into a formal Lo-fi Experimentation plan (Template 14) using psk-lofi-experimentation.

**When acts are complete:** Feed confirmed results into the Outcome-Based Roadmap (Template 17) - specifically the "Outputs to Develop," "Output Concepts to Validate," "Assumptions to Validate," and "Assumptions to Research" sections.

## Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For an HVAC dispatch assumption, identify what is known, expose the uncertainty, and plan a small field observation whose result could change the next decision.
- **Weak:** A list of research activities without an assumption or decision creates motion without learning.
- **Drift to avoid:** Agent runs the act: AI helps plan and interpret, while people conduct the real observation or experiment.


## Common Pitfalls

- **Confusing Assumptions with Facts:** For every item on the "what we know" list, ask: "What was the source? When was this verified?" If the PM cannot name a source, the item belongs on the "don't know" list.

- **Listing Only Technical Unknowns:** Before finalizing the list, explicitly prompt: What are the adoption unknowns? What are the organizational unknowns? What are the customer-behavior unknowns? What could cause the product to be technically correct but commercially unsuccessful?

- **Treating All Assumptions as Equal Priority:** Push the team to differentiate. If more than half the list is Urgent, the ratings have not done the work. Ask: "If you could only test one of these this week, which would it be and why?" The answer reveals the true top priority.

- **Writing Acts That Are Too Large:** Each act should be completable in days. Five user walkthroughs, not fifty. A targeted data pull, not a full analytics overhaul. A quick survey of 20 current users, not a market research study. If the act takes more than a week to complete, break it into a smaller first step.

- **Skipping the Metric Column:** Every act needs a specific signal: a threshold (70% task completion), a count (more than 15 of 20 users identify this as a top pain), or an observable event (the user completes the checkout flow without asking for help). If the PM cannot define what "pass" looks like, the hypothesis is not ready to test.

- **Leaving "Assigned" Blank:** Every act must have a named individual. If the PM cannot name one, that is a signal the team does not have the capacity to run this act. Either assign it or drop it from the list.

- **Conflating Tiny Acts with Lo-fi Experimentation:** Tiny Acts is for many small tests running in parallel or in rapid sequence. If the PM needs a single rigorous test for a make-or-break assumption, redirect them to psk-lofi-experimentation (Template 14).

- **Running It Once and Filing It Away:** At the end of each Tiny Acts session, schedule the next one explicitly. Tiny Acts is not a milestone - it is a rhythm. The cadence can be biweekly, sprint-based, or triggered by a key decision. What matters is that it recurs.

- **AI Scores the Backlog:** The PM places every assumption. The skill asks what the evidence is, pushes on it, and points at placements that look off.

- **The Backlog Replaces the Discovery:** Commit to one act this week, with a named owner, before polishing the rest. Re-score only when new evidence arrives.

## References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-tiny-acts-discovery) for supporting source material and expanded examples.
