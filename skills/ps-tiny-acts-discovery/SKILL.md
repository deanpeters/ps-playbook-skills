---
name: ps-tiny-acts-discovery
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

The purpose of Tiny Acts of Discovery is to anchor product decisions in what real customers actually do, need, and believe — not in what the team assumes from the inside. Every assumption worth testing should trace back to a customer behavior, a customer value question, or a customer adoption question.

When the team runs these exercises honestly, they replace internal debate with evidence. A user walkthrough result, a data pull, a survey response — these are the inputs that make the development process data-driven rather than opinion-driven. The team learns what customers genuinely need before committing resources to build it.

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

See the source play pages in [assets/ps_tiny_acts_discovery_playbook_pages.pdf](assets/ps_tiny_acts_discovery_playbook_pages.pdf).

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
3. **Who is in this session?** Tiny Acts is a team exercise. The assumption list should reflect cross-functional perspectives. If the PM is working alone, note this — solo lists tend to be narrower and may miss organizational, adoption, and customer-behavior assumptions.

If the PM is working alone without team input, recommend they share the output with one or two stakeholders before designing the tiny acts.

### Step 2: Tech-Role Bias Guard

Before building the assumption list, confirm what the product does and who actually uses it. Most products do not serve developers or technical architects. A supply chain management platform serves logistics coordinators and warehouse managers. A clinical data platform serves clinical operations leads and data managers. A field service app serves technicians and dispatchers.

Ask the PM directly: "Who is the person who will use this product day-to-day? What is their job title and what does their work look like?" This answer should shape every assumption on the list - the knowns, the unknowns, the hypotheses, and the tiny acts.

Do not allow the assumption list to default to technical unknowns (performance, integration, security) while missing the behavioral and organizational unknowns that most often determine whether a product succeeds.

### Step 3: Gather Available Artifacts

Before drafting, ask whether the user has relevant materials to share:

- Solution hypothesis from ps-solution-hypothesis (defines what is being tested)
- Problem statement from ps-framing-the-problem (gives the customer and problem context)
- Outcome tree from ps-outcome-tree (clarifies what the team is trying to achieve)
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

**The PM classifies; the skill challenges** (mirrors [prompts/01](prompts/01-rank-assumption-backlog.md)). First help the PM state each item as an assumption: the thing that must be true for it to matter. If their version is vague or hides two assumptions, make them tighten it; react to theirs rather than writing it. Then for each assumption ask two questions: how much would it change product or business decisions if it were true (impact), and how much real evidence they hold (uncertainty). Push hardest on the evidence: what is it, and how confident are they in it? Where a placement looks off given what they just said, point at it and make them reconsider. Do not move it yourself, and do not invent evidence or confidence.

If the PM asks you to classify, or chooses best guess mode, draft the classification tagged `[AI-SUGGESTED, VALIDATE THIS]` and say plainly that uncertainty depends on evidence only the PM can see.

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

For each hypothesis, find the fastest path to a real signal (mirrors [prompts/02](prompts/02-design-tiny-act.md)):

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
2. If one assumption from Step 6 stands out as uniquely high-stakes, convert it into a formal Lo-fi Experimentation plan using ps-lofi-experimentation
3. Feed confirmed results into the Outcome-Based Roadmap (Template 17): the "Outputs to Develop," "Output Concepts to Validate," and "Assumptions to Validate / Research" sections draw directly from Tiny Acts findings

## Examples

See [examples/sample.md](examples/sample.md).

The example set includes:

- a strong Tiny Acts exercise with a coherent product scenario, honest knowns, honest unknowns, a clear top-3, measurable hypotheses, and genuinely small acts
- a weak version with the same scenario done poorly: assumptions masquerading as facts, all ratings inflated to high, vague acts with no metrics and no owners
- a drift-bug example where the PM asks the agent to run the tiny acts for them, and the agent correctly explains the process skill boundary

## Common Pitfalls

### Pitfall 1: Confusing Assumptions with Facts

**Symptom:** The "what we know" list is full of items the team believes but has not verified: "We know customers want faster reporting." "We know the current tool is insufficient." "We know this will drive adoption."

**Consequence:** The "don't know" list is artificially short. The team skips assumption classification because they think they already know more than they do. The tiny acts target the wrong questions.

**Fix:** For every item on the "what we know" list, ask: "What was the source? When was this verified?" If the PM cannot name a source, the item belongs on the "don't know" list.

### Pitfall 2: Listing Only Technical Unknowns

**Symptom:** The "what we don't know" list is entirely about system performance, API reliability, data quality, and integration complexity. No behavioral, adoption, organizational, or market unknowns appear.

**Consequence:** The team builds something technically sound that fails in the field because the behavioral and organizational assumptions were never tested.

**Fix:** Before finalizing the list, explicitly prompt: What are the adoption unknowns? What are the organizational unknowns? What are the customer-behavior unknowns? What could cause the product to be technically correct but commercially unsuccessful?

### Pitfall 3: Treating All Assumptions as Equal Priority

**Symptom:** Every item on the "don't know" list gets rated High Impact and High Uncertainty. Everything is Urgent.

**Consequence:** Prioritization is impossible. The team cannot distinguish which assumption to test first. All energy is diffuse.

**Fix:** Push the team to differentiate. If more than half the list is Urgent, the ratings have not done the work. Ask: "If you could only test one of these this week, which would it be and why?" The answer reveals the true top priority.

### Pitfall 4: Writing Acts That Are Too Large

**Symptom:** The tiny acts are six-week user studies, full A/B tests with statistical significance requirements, or multi-phase research programs.

**Consequence:** Nothing gets done. The cost of learning is so high that the team skips the acts entirely and proceeds on untested assumptions.

**Fix:** Each act should be completable in days. Five user walkthroughs, not fifty. A targeted data pull, not a full analytics overhaul. A quick survey of 20 current users, not a market research study. If the act takes more than a week to complete, break it into a smaller first step.

### Pitfall 5: Skipping the Metric Column

**Symptom:** The acts are specific, but the Measure / Metric column is empty or filled with vague language: "see if they like it," "observe the reaction," "check if it works."

**Consequence:** The team runs the act but cannot interpret the results. Was the test a success? A failure? There is no answer.

**Fix:** Every act needs a specific signal: a threshold (70% task completion), a count (more than 15 of 20 users identify this as a top pain), or an observable event (the user completes the checkout flow without asking for help). If the PM cannot define what "pass" looks like, the hypothesis is not ready to test.

### Pitfall 6: Leaving "Assigned" Blank

**Symptom:** The Assigned column is empty, or it reads "TBD," "the team," or "everyone."

**Consequence:** No one runs the act. Unowned work does not get done.

**Fix:** Every act must have a named individual. If the PM cannot name one, that is a signal the team does not have the capacity to run this act. Either assign it or drop it from the list.

### Pitfall 7: Conflating Tiny Acts with Lo-fi Experimentation

**Symptom:** The PM uses Tiny Acts to design one formal, rigorous experiment for a single high-stakes assumption, complete with control conditions, statistical significance, and a multi-week time window.

**Consequence:** The tool is being misused. A single formal experiment is not Tiny Acts. The PM is spending Lo-fi Experimentation effort without the rigor that makes Lo-fi defensible.

**Fix:** Tiny Acts is for many small tests running in parallel or in rapid sequence. If the PM needs a single rigorous test for a make-or-break assumption, redirect them to ps-lofi-experimentation (Template 14).

### Pitfall 8: Running It Once and Filing It Away

**Symptom:** The team completes the exercise at project kickoff and never revisits it. The assumption classification becomes stale. Results from the acts are never documented.

**Consequence:** The practice never becomes continuous. The team loses the habit. Later-phase assumptions go untested because the tool is associated with a one-time activity.

**Fix:** At the end of each Tiny Acts session, schedule the next one explicitly. Tiny Acts is not a milestone - it is a rhythm. The cadence can be biweekly, sprint-based, or triggered by a key decision. What matters is that it recurs.

### Pitfall 9: AI Scores the Backlog

**Symptom:** The PM pastes the "don't know" list and asks the agent to rate impact and uncertainty. The 2x2 comes back filled in, and the team adopts it.

**Consequence:** Confidence is claimed without the PM's evidence. The ranking is the model's guess, and no one can explain why an assumption sits where it does.

**Fix:** The PM places every assumption. The skill asks what the evidence is, pushes on it, and points at placements that look off.

### Pitfall 10: The Backlog Replaces the Discovery

**Symptom:** A tidy, well-ranked backlog, acts defined with owners and metrics, and three weeks later none have run. The backlog gets re-groomed instead.

**Consequence:** Planning becomes the activity. It looks strategic and learns nothing.

**Fix:** Commit to one act this week, with a named owner, before polishing the rest. Re-score only when new evidence arrives.

## References

### Skill Files

- [template.md](template.md) - working scaffold for the five-step exercise
- [prompts/](prompts/README.md) - copy-paste prompts for chat-based AI tools (2: build and rank the backlog, design a tiny act)
- [examples/sample.md](examples/sample.md) - strong, weak, and drift-bug examples

### Related Skills

- **Upstream:** [ps-solution-hypothesis](../ps-solution-hypothesis/SKILL.md) defines what is being tested; [ps-framing-the-problem](../ps-framing-the-problem/SKILL.md) provides customer and problem context; [ps-outcome-tree](../ps-outcome-tree/SKILL.md) clarifies success criteria
- **Downstream:** Outcome-Based Roadmap (Template 17): "Outputs to Develop," "Output Concepts to Validate," "Assumptions to Validate," and "Assumptions to Research" draw from Tiny Acts findings
- **Related:** [ps-lofi-experimentation](../ps-lofi-experimentation/SKILL.md) (Template 14): for a single high-stakes assumption that requires formal, rigorous testing; ps-risk-assessment (Template 15): high-uncertainty assumptions that cannot be tested quickly may surface as risks

### Project Docs

- [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)
- [informative-documents/framework-glossary.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/framework-glossary.md)
- [informative-documents/skill-dependency-map.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/skill-dependency-map.md)

### Source Material

- [assets/ps_tiny_acts_discovery_playbook_pages.pdf](assets/ps_tiny_acts_discovery_playbook_pages.pdf)
- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 81-86: Template 18 of 24 there, with the AI overview on slide 83 and prompts on slides 84, 85. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).
- [Baseline Playbook version](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml). Full source PDF supplied separately.
- Productside Playbook companion document (supplied separately)
