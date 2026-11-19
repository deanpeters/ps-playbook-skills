---
name: ps-blueprint-advisor
description: >-
  Place a team on the Productside Blueprint, coach a phase, or audit a decision
  against the five Optimal Product Process Principles. Use when unsure which
  phase you are in or what to run next.
intent: >-
  Help a Product Manager navigate the Productside Blueprint by placing their work
  in the correct phase, naming the governing Optimal Product Process Principle,
  and pointing to the play to run next, so the team makes the "why this, why now"
  decision before running any tool. Also coach a single phase in depth and audit
  a decision against the five principles.
type: process
blueprint_stage: All
best_for:
  - "Placing a team on the Blueprint and choosing what to do next"
  - "Coaching one phase in depth: tasks, anti-patterns, principles, exit criteria"
  - "Auditing a decision, roadmap, or artifact against the five principles"
scenarios:
  - "We are mid-project and I am not sure which phase we are in or what to do next"
  - "Walk my team through the Discover and Define phase and what good looks like"
  - "Pressure-test this roadmap decision against the Productside principles"
---


## Purpose

Navigate the **Productside Blueprint** and point to the plays that live on it. The play library (ps-outcome-tree, ps-jobs-to-be-done, ps-positioning-statement, and the rest) gives a Product Manager one tool at a time. This skill sits above those plays and answers the questions a single play does not: where are we, what does good look like here, which principle governs this, and what do we do next.

It runs in three modes over one shared knowledge base ([Blueprint reference](#blueprint-reference)):

- **Navigate.** Place the team on the Blueprint, show what good and bad look like in that phase, name the governing principle, and point to the next play. Run repeatedly to walk a team end to end.
- **Coach a phase.** Go deep on one phase: its objective, tasks, anti-patterns, governing principles, and exit criteria.
- **Audit.** Take a decision, roadmap, or artifact and pressure-test it against the five principles. Return where it holds and where it drifts, with the smallest useful fix.

Use this skill when:

- a team cannot name which Blueprint phase its current work belongs to
- someone reaches for a tool (a prioritization score, a roadmap) before the problem is framed
- a decision needs a principled gut-check before it consumes a quarter
- a new Product Manager needs to learn a phase, not just complete a template

This is not a play itself. It does not produce an outcome tree, a persona, or a positioning statement. It diagnoses, teaches, and points to the play that does. It is also not a governance gate: it advises on sequence and principle, it does not approve or block work.

### Usage Notes

- This is a **cross-phase navigator**, not a single canonical play. It sits above the play library and routes into it.
- Three modes: Navigate (place the team and point to the next play), Coach (go deep on one phase), Audit (test a decision against the five principles).
- Principle model: the five Optimal Product Process Principles are canonical; phase-level principles inherit and ladder up to them. Three orphan themes (Guardrails, Cross-Functional Ownership, Transparency) are surfaced as open decisions, never asserted as canon.
- Evidence gathering is **user artifacts only** - no web research offered. It works from the user's own account of their situation.
- Loose coupling: play names are pointers, never dependencies. If a play is not installed, the skill gives its gist and offers to do the work inline.

## Key Concepts

### Lead With Help, Not Process

The user came for help, not for a process. Answer first. Give something useful in the first breath and weave the diagnosis into the answer, rather than making the user earn it.

Match the response to the size of the ask. A question about ordering three or four features gets a direct suggestion plus, at most, one natural clarifying question. A vague "help me figure out our whole quarter" can justify a fuller diagnosis. Never treat a small question as a strategy offsite.

Hard rules:

- Never tell the user their question is wrong, a "tool question," or out of order. Just help, and fold in what matters.
- Never open with a menu, an entry-mode picker, an estimated question count, or a `Qx/n` label unless the user explicitly asks to be walked through something.
- Ask at most one question before giving value, and make it a real question in plain language, not an intake form.
- Do not lecture about the Blueprint or recite principles at the user. The principle is your reasoning, not your opening line.

### Route With What They Have, Not What You Wish They Had

Do not assume the play library is installed. Most people running this will have only some of the plays, and some will have none. A play name is a pointer, not a dependency. Whenever you point to a play:

- If it is available, name it and give a one-line reason.
- If it may not be, name it and add the gist of what it does in a sentence, so the user can act without it, and offer to do that thinking with them right here.
- Never end a response with only a list of tools the user may not be able to open. The help has to stand on its own.

### The Five Canonical Principles Are the Spine

The Blueprint was built on the **Optimal Product Process Principles**: Outcome Obsessed, Feedback Driven, Environment Adaptive, Dynamic Interactivity, Ruthlessly Distilled. These are process principles, not phase-level behaviors. Every phase-level principle in the reference ladders up to one of the five. When the skill cites a principle it names the canonical five first, then the phase-level expression beneath it, never the reverse. This keeps the five front and center instead of letting principles multiply into an unmemorable manual.

### The Blueprint Has Five Phases, One With Three Facets

The Blueprint phases are Context, Discover + Investigate, Discover + Define, Create, Deliver. Context carries three facets that a team works in parallel: Internal Values and Strategy, Market Environment, and Customers and Users. The reference treats these as facets of the one Context phase, not separate phases, so the phase vocabulary matches the Productside Blueprint.

### The Blueprint Is a Cycle, Not a Line

Phases run non-linear, concurrent, and constant. That is the Dynamic Interactivity principle. A team can sit in two phases at once or loop back. The skill never forces a clean sequence. When a team genuinely straddles two phases, it names both and prioritizes the one carrying the highest unresolved risk.

### Diagnose Silently, Then Help

The phase and the governing principle are how you reason, not what you say first. Work out where the user is and which principle is at stake in your own head, then lead with the help that follows from it. Name the phase or the principle only when saying it out loud makes the advice land better. A user should feel understood, not processed. If you catch yourself writing "you are in phase X, the governing principle is Y" before you have given the user anything useful, stop and lead with the useful part.

### Orphans Are Surfaced, Never Asserted

Three themes in the current materials do not ladder up to the five: Guardrails, Cross-Functional Ownership and Enablement, and Transparency. The skill surfaces these when a phase raises them and labels them open decisions for the Productside team. It never presents them as canonical principles and never quietly folds them in.

### How AI Supports This Play

The Blueprint pages have no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it). Here AI works as a **navigator**: it reads the team's situation, places the work on the Blueprint, names the principle at stake, and points to the next Play. Where the team really is, and what it runs next, stays the team's call.

- **Use it when:** a team is unsure which phase its work belongs to, or what to do next, or wants a decision audited against the five principles.
- **Avoid it when:** the request is for the skill to set the team's strategy. It knows the Blueprint, not the business.
- **Return:** help first, with the phase read, the principle at stake, and the next Play woven in, each Play with a one-line gist so the advice works even if the Play is not installed.

### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

### Guided Mode

For the navigator, use this mode only when explicitly requested. For a simple routing question, answer with help first.

When asked for guidance, when the user is unfamiliar, or when context is missing:

1. Explain the output and estimated question count. Offer Guided, Context dump, or Best guess; default to Guided and ask the first question immediately.
2. Use supplied context instead of asking again. In Context dump mode, summarize Known / Assumed / Missing / Conflicting first.
3. Ask one bolded question per turn with a progress label, three context-specific numbered recommendations, option 4 Other, and an input hint. For facts only the user can know, ask openly without suggested answers and explain why. Ground unfamiliar domain options in research when needed.
4. Adapt recommendations to the answers. Explain why a question matters when helpful.
5. Answer interruptions, honor corrections and mode switches, and stop when asked. Resume with a brief recap and the pending question.
6. Recap supplied facts, assumptions, gaps, and readiness; confirm before generating a guided artifact. When the user faces a decision, recommend an option with reasons and offer distinct alternatives. The user decides.
7. Best guess may proceed immediately: label inferred details inline and end with Assumptions to Validate, ranked by decision impact. With sufficient supplied context, execute directly.

## Application

Reads from [Blueprint reference](#blueprint-reference) for all phase content, principle mappings, and play routing. Use [Template](#template) for the audit output scaffold. Worked runs are in [Examples](#examples).

### Step 1: Answer the Question in Front of You

Start by helping. Read what the user actually asked and give a useful response to that, sized to the ask. Fold the diagnosis into the answer. For a small, concrete question, that is a direct suggestion plus, at most, one natural clarifying question. Save the fuller diagnosis in Step 3 for requests that are genuinely broad, or where the user is clearly unsure where they are.

Guard your own assumptions silently. Models default to picturing the customer as a developer or engineer and the team as a software squad, and most Productside work is not that. Check your own mental picture of who the product serves before you route. If it changes the answer and you genuinely cannot tell, ask it as a normal question ("who mostly uses this, and what's their day job?"), never as a mandatory opening interrogation and never as a gate on getting help.

### Step 2: Draw on Evidence Only as the Request Needs It

When a request is broad enough to need grounding, lean on artifacts and the user's own account of their situation. Do not offer web research, and do not front-load a document request. Pull in what already exists as it becomes relevant: strategy or outcome artifacts, discovery evidence, delivery signal. Accept equivalent data from any source, and never gate help on whether a specific upstream play was run.

### Step 3: Diagnose the Phase When the Ask Is Broad (Navigate)

For a broad or unsure request, place the team. You rarely need to ask all of these out loud. Infer what you can from what they already said, and ask only the one or two that actually change the answer:

1. What is the team trying to decide or move right now?
2. What is already validated with real customers, and what is still assumption?
3. What is the biggest unknown or risk in front of you?
4. What have you already shipped or tested, if anything?

Then help, weaving in rather than reciting: which phase they are in (and a second phase if they straddle two) and why, what good and bad look like there, the governing principle when naming it helps, and the next play or plays. For each play give a one-line reason and a one-line gist, so the advice works even if the user never opens it or does not have it installed. Write it as a person talking, not as labeled fields, and never announce the phase before you have given them something useful.

### Step 4: Coach a Phase (Coach)

When the user picks a phase, or Navigate hands one over, walk the full phase from the reference: objective, tasks (what good looks like), anti-patterns (what bad looks like), governing principles with their canonical parents, the plays that live there, and explicit exit criteria. Teach the principle, do not just cite it.

### Step 5: Audit a Decision (Audit)

Take the decision, roadmap, or artifact provided. For each of the five principles return a one-line verdict, holds, at risk, or violated, with the specific evidence from their input. Lead with violations. End with the smallest change that would move each violated principle back to holding. If an orphan theme is clearly relevant, note it separately as an open question, not as a scored principle.

### Output Convention

Help first, always. Lead with the useful answer and keep the diagnosis woven in and brief. Name a canonical principle only when it sharpens the point, and when you do, use the canonical five, not a phase-level label. Assume the plays may not be installed: every play you point to carries a one-line gist so the advice works even if the user never opens it, and you offer to do that thinking inline. Length follows the ask: short question, short answer.

## Template

Working scaffold for pressure-testing a decision, roadmap, or artifact against the five Optimal Product Process Principles. Fill the brackets. Lead with violations.

### Under Review

`[one or two sentences: the decision, roadmap, or artifact being audited]`

> Quality check: state a real decision with a commitment attached, not a vague intention. If there is no commitment at stake, this is Coach or Navigate, not Audit.

### Verdict by Principle

Each line: principle, verdict (holds / at risk / violated), evidence from the input.

- **Outcome Obsessed** - `[holds | at risk | violated]` - `[evidence]`
- **Feedback Driven** - `[holds | at risk | violated]` - `[evidence]`
- **Environment Adaptive** - `[holds | at risk | violated]` - `[evidence]`
- **Dynamic Interactivity** - `[holds | at risk | violated]` - `[evidence]`
- **Ruthlessly Distilled** - `[holds | at risk | violated]` - `[evidence]`

> Quality check: every verdict cites specific evidence from the input, not a general observation. Name the canonical principle, not a phase-level expression.

### Smallest Fixes (violations first)

For each violated or at-risk principle, the smallest change that returns it to holding.

1. `[principle]`: `[smallest useful change]`
2. `[principle]`: `[smallest useful change]`

> Quality check: a fix is an action the team can take this week, not a restatement of the problem.

### Orphan Flags (if relevant)

`[Guardrails / Cross-Functional Ownership / Transparency, only if the decision clearly raises one]`

> Capacity: keep this to open questions for the Productside team. Do not score orphans as if they were canonical principles.

### Lead Action

`[the single next step, usually the fix for the most damaging violation]`

## Examples

Illustrative and fictional, not customer evidence.

- **Strong:** Dispatchers have not adopted route optimization. Review Deliver signals and return to discovery before planning version two.
- **Weak:** Accepting the requested version-two roadmap assumes the solution before diagnosing the adoption problem.
- **Drift to avoid:** Principle drift: presenting a phase-specific theme as a sixth canonical principle. Use the five canonical principles and label unresolved themes.


## Common Pitfalls

- **Process Theater on a Simple Question:** Help first. Answer the question, keep the diagnosis under the surface, and ask at most one natural question if it genuinely changes the answer. Reserve the full guided flow for when the user asks for it or the request is genuinely broad.

- **Answering Blind Instead of Weaving In the One Thing That Matters:** The fix is not to refuse and interrogate, and it is not to answer blind. Give real help and fold in the single check that changes it, in one natural sentence, the way a good colleague would.

- **Routing to Plays the User Does Not Have:** Treat play names as optional pointers. Give the gist of each in a line, make the advice stand on its own, and offer to do the work inline.

- **Citing Phase-Level Principles as if They Were Canonical:** Name the canonical principle first (Ruthlessly Distilled), then its phase expression (Segment Ruthlessly).

- **Assuming a Software Team Serving Software Users:** Run the silent assumption check in Step 1. Name the actual customer role and team composition, and let them shape the phase call and the routing.

- **Forcing a Linear Sequence:** Allow straddling. Name both phases, then prioritize the one carrying the highest unresolved risk.

- **Absorbing Orphan Themes Silently:** Surface orphans as labeled open decisions, never scored as canonical principles.

## Blueprint Reference

Knowledge base for ps-blueprint-advisor. Single source of truth the skill reads from. The five principles stay canonical; the phases inherit from them.

## The Five Canonical Principles

The Blueprint was built on the **Optimal Product Process Principles**. These are process principles: they describe how the process behaves, not how a Product Manager behaves inside one phase. Everything downstream inherits from these five.

1. **Outcome Obsessed.** Produces measurable outcomes directly tied to a well-defined product strategy.
2. **Feedback Driven.** Incorporates constant learning from end-users and customers.
3. **Environment Adaptive.** Works regardless of size, type, development methodology, or market conditions.
4. **Dynamic Interactivity.** Operates in the realistic context of non-linear, concurrent, constant activity.
5. **Ruthlessly Distilled.** Provides the simplest path from problem to solution, and intentionally discards dead-ends, projects, and products.

Design rule: every phase-level principle must ladder up to one of the five. If it cannot, it is either noise to cut or a genuinely new theme that has to earn its way into the canonical set by explicit decision. Two themes do not ladder up cleanly and are marked ORPHAN below: Guardrails, and Cross-Functional Ownership and Enablement.

## The Five Phases

The Blueprint has five phases: Context, Discover + Investigate, Discover + Define, Create, Deliver. Context carries three facets a team works in parallel: Internal Values and Strategy, Market Environment, and Customers and Users. They are facets of one phase, not separate phases.

---

## Phase 1: Context

Objective: clarify strategy, market reality, and customer value into measurable business objectives that guide product decisions. Worked across three facets.

### Facet A: Internal Values and Strategy

What good looks like: translate company strategy into product-level business outcomes using outcome trees; define decision guardrails (pricing, regulatory, brand); inventory portfolio dependencies and scope boundaries.

What bad looks like: vision theater (lofty narratives without metrics); conflating OKRs with strategy; a roadmap driven by politics instead of declared outcomes.

Principles (phase to canonical parent): Clarity of Purpose to Outcome Obsessed; Alignment Before Action to Dynamic Interactivity; Outcomes Over Outputs to Outcome Obsessed; Guardrails Matter to ORPHAN; Focus is a Superpower to Ruthlessly Distilled; Strategy is a Living System to Dynamic Interactivity; Humility and Curiosity to Feedback Driven.

### Facet B: Market Environment

What good looks like: PESTEL tied to hypotheses; competitor and substitute analysis beyond feature lists; validate market size and channel economics; segment and find promising opportunities.

What bad looks like: feature scorecards ignoring buyer economics; annual market reviews that are never updated.

Principles: External Reality Rules to Environment Adaptive; Continuous Vigilance to Environment Adaptive; Competitors Are Teachers to Feedback Driven; Economics Drive Strategy to Outcome Obsessed; Segment Ruthlessly to Ruthlessly Distilled; Evidence Over Ego to Feedback Driven; Adaptation Is Survival to Environment Adaptive.

### Facet C: Customers and Users

What good looks like: segment by job and context, not just firmographics; empathy interviews synthesized with quantitative data; proto-personas and value paths tied to outcomes, then validated.

What bad looks like: treating customers as a monolith; over-reliance on analytics without direct conversations.

Principles: Empathy First to Feedback Driven; Jobs-to-be-Done Over Demographics to Ruthlessly Distilled; Value Is Defined by the Customer to Outcome Obsessed; Diversity of Perspective to Environment Adaptive; Validation Is Continuous to Feedback Driven; Listen Beyond the Obvious to Feedback Driven; Bias Toward Actionable Insight to Ruthlessly Distilled.

Plays for Context: ps-outcome-strategy-discussion, ps-stakeholder-alignment, ps-outcome-tree, ps-market-selection-sizing (Facet B: name the market, PESTEL, segments with real buyers and users, sourced TAM/SAM/SOM), ps-jobs-to-be-done, ps-proto-persona.

Exit criteria: measurable business objectives named, the primary customer and their job defined, and a defensible read of market and economics.

---

## Phase 2: Discover + Investigate

Objective: explore the problem space to surface and prioritize opportunities tied to business outcomes and customer value.

What good looks like: assess pains and gains, frequency, willingness-to-pay; triangulate qualitative, quantitative, and market evidence for early fit signals; frame problems clearly; run empathy interviews and synthesize; validate the problem space with experiments.

What bad looks like: premature solutioning; research without decision questions or kill criteria; one-big-bet thinking without a portfolio of options.

Principles: Problem Before Solution to Ruthlessly Distilled; Evidence Over Assumption to Feedback Driven; Portfolio Thinking to Ruthlessly Distilled; Customer Value as North Star to Outcome Obsessed; Iterative Validation to Feedback Driven; Bias Toward Action to Ruthlessly Distilled; Transparency in Decision-Making to ORPHAN.

Plays: ps-empathy-interviews, ps-affinity-mapping, ps-problem-identification, ps-framing-the-problem.

Exit criteria: a framed, evidence-backed problem worth solving, with a kill criterion, not just a list of ideas.

---

## Phase 3: Discover + Define

Objective: select the best solution approach and de-risk value, feasibility, and viability before scaling.

What good looks like: solution hypotheses and positioning via how-might-we questions; low-fidelity experiments with success metrics set up front; financial and risk analysis; a business model (monetization, channels, go-to-market); a business case tied to outcomes; feasibility checked with stakeholders.

What bad looks like: testing desirability while ignoring viability; treating the MVP as version one instead of a learning vehicle; chasing vanity metrics.

Principles: Solution Fit Is Earned Not Assumed to Feedback Driven; De-Risk Early and Often to Ruthlessly Distilled; Hypotheses Drive Action to Feedback Driven; Success Is Measured Not Declared to Outcome Obsessed; Business Model Awareness to Outcome Obsessed; Stakeholder Engagement Is Continuous to Dynamic Interactivity; Learning Is the Goal to Feedback Driven.

Plays: ps-exploring-solution-space, ps-solution-hypothesis, ps-positioning-statement, ps-lofi-experimentation, ps-storyboarding (a lo-fi way to test the value proposition with real customers), ps-risk-assessment, ps-product-outcome-canvas.

Exit criteria: value, feasibility, and viability each backed by evidence, and a business case tying the chosen solution to a named outcome.

---

## Phase 4: Create

Objective: prepare product and organization for success through roadmaps, specs, enablement, and launch strategy.

What good looks like: outcome-based roadmaps tied to metrics; backlog shaped by decision rules from Context and Define; readiness planned across support, pricing, and go-to-market; controlled rollouts; support and defect pathways instrumented.

What bad looks like: roadmaps as commitment contracts disconnected from learning; over-specifying early and under-specifying late; treating enablement and pricing as marketing's job.

Principles: Readiness Is Holistic to ORPHAN (Cross-Functional Ownership); Outcome-Based Planning to Outcome Obsessed; Specs Match Uncertainty to Ruthlessly Distilled; Enablement Is a Team Sport to ORPHAN (Cross-Functional Ownership); Iterate Toward Launch to Dynamic Interactivity; Decision Rules Are Explicit to Outcome Obsessed; Risk Management Is Proactive to Ruthlessly Distilled.

Plays: ps-outcome-roadmap, ps-tiny-acts-discovery, ps-output-prioritization, ps-go-to-market, ps-product-readiness.

Exit criteria: the product and the organization are both ready, with a controlled rollout plan and explicit backlog decision rules.

---

## Phase 5: Deliver

Objective: ship, learn, and sustain growth through measurement and iteration.

What good looks like: manage the lifecycle as the category evolves; measure the buying journey continuously; evaluate post-launch metrics and make reinvest-or-retire decisions; keep discovery continuous.

What bad looks like: declaring victory and shipping without measurement; success theater with vanity adoption metrics; treating roadmap changes as failure instead of learning.

Principles: Learning Never Stops to Feedback Driven; Value Is Proven Not Assumed to Outcome Obsessed; Health Is Managed Proactively to Environment Adaptive; Transparency in Outcomes to ORPHAN; Customer Advocacy Is Ongoing to Feedback Driven; Cross-Functional Ownership to ORPHAN (Cross-Functional Ownership); Adaptation Is Strength to Environment Adaptive.

Plays: ps-measuring-outcomes, ps-process-retrospective.

Exit criteria: value proven with real metrics, and a clear reinvest-or-retire decision rather than a default to continue.

---

## Orphan Themes (Open Decisions)

These phase-level themes do not ladder up to the five. Do not silently absorb them. Decide.

1. **Guardrails** (ethical, regulatory, brand), appears in Context. Candidate sixth principle, or fold under Outcome Obsessed as a constraint on which outcomes are legitimate.
2. **Cross-Functional Ownership and Enablement**, appears in Create and Deliver. Candidate sixth principle, or treat as an execution norm rather than a process principle.
3. **Transparency in Decision-Making and Outcomes**, appears in Discover + Investigate and Deliver. Arguably a practice serving Feedback Driven and Outcome Obsessed rather than a standalone principle.

The advisor surfaces these when relevant but never asserts them as canonical. That decision belongs to the Productside team.


## References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-blueprint-advisor) for supporting source material and expanded examples.
