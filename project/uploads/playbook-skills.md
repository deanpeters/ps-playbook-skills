# Productside Playbook: full skill references

Source snapshot: `0a2342fb1e6ce949`. November 2026 B2B work-in-progress Playbook. Not yet ratified.

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. Full license: playbook-plays.md, License appendix.

Start with playbook-plays.md to choose a Play or find its coaching prompts. Each reference below preserves the consolidated SKILL.md instructions, embedded template, and examples. In a Project, Notebook, agent, or Gemini Skill configured with these references, mentions of a skill or agent mean applying the named Play, not calling an unavailable tool.

## Contents

- [Unnumbered: Blueprint navigator](playbook-skills.md#psk-blueprint-advisor--instructions)
- [Play 01: Outcome & Strategy Discussion](playbook-skills.md#psk-outcome-strategy-discussion--instructions)
- [Play 02: Stakeholder Alignment](playbook-skills.md#psk-stakeholder-alignment--instructions)
- [Play 03: Outcome Tree, Section One](playbook-skills.md#psk-outcome-tree--instructions)
- [Play 04: Market Selection & Sizing](playbook-skills.md#psk-market-selection-sizing--instructions)
- [Play 05: Jobs-to-Be-Done & Outcomes](playbook-skills.md#psk-jobs-to-be-done--instructions)
- [Play 06: Personas & Proto-Personas](playbook-skills.md#psk-proto-persona--instructions)
- [Play 07: Empathy Interviews](playbook-skills.md#psk-empathy-interviews--instructions)
- [Play 08: Affinity Mapping](playbook-skills.md#psk-affinity-mapping--instructions)
- [Play 09: Problem Identification](playbook-skills.md#psk-problem-identification--instructions)
- [Play 10: Framing the Problem](playbook-skills.md#psk-framing-the-problem--instructions)
- [Play 11: Exploring the Solution Space](playbook-skills.md#psk-exploring-solution-space--instructions)
- [Play 12: Solution Hypothesis](playbook-skills.md#psk-solution-hypothesis--instructions)
- [Play 13: Positioning Statement](playbook-skills.md#psk-positioning-statement--instructions)
- [Play 14: Lo-fi Experimentation](playbook-skills.md#psk-lofi-experimentation--instructions)
- [Unnumbered: Storyboarding](playbook-skills.md#psk-storyboarding--instructions)
- [Play 15: Risk Assessment](playbook-skills.md#psk-risk-assessment--instructions)
- [Play 16: Product Outcome Canvas](playbook-skills.md#psk-product-outcome-canvas--instructions)
- [Play 17: Outcome-Based Roadmap & Release Plan](playbook-skills.md#psk-outcome-roadmap--instructions)
- [Play 18: Tiny Acts of Discovery](playbook-skills.md#psk-tiny-acts-discovery--instructions)
- [Play 19: Output Prioritization](playbook-skills.md#psk-output-prioritization--instructions)
- [Play 20: Go-to-Market Enablement](playbook-skills.md#psk-go-to-market--instructions)
- [Play 21: Product Readiness Testing](playbook-skills.md#psk-product-readiness--instructions)
- [Play 22: Measuring Outcomes](playbook-skills.md#psk-measuring-outcomes--instructions)
- [Play 23: Outcome Tree, Section Two](playbook-skills.md#psk-outcome-tree--instructions)
- [Play 24: Process Retrospective](playbook-skills.md#psk-process-retrospective--instructions)

## Navigator (cross-phase)


### Unnumbered: Blueprint navigator

Stable identifier: `psk-blueprint-advisor`.

#### psk-blueprint-advisor / Instructions

##### Purpose

Navigate the **Productside Blueprint** and point to the plays that live on it. The play library (psk-outcome-tree, psk-jobs-to-be-done, psk-positioning-statement, and the rest) gives a Product Manager one tool at a time. This skill sits above those plays and answers the questions a single play does not: where are we, what does good look like here, which principle governs this, and what do we do next.

It runs in three modes over one shared knowledge base ([Blueprint reference](playbook-skills.md#psk-blueprint-advisor--instructions)):

- **Navigate.** Place the team on the Blueprint, show what good and bad look like in that phase, name the governing principle, and point to the next play. Run repeatedly to walk a team end to end.
- **Coach a phase.** Go deep on one phase: its objective, tasks, anti-patterns, governing principles, and exit criteria.
- **Audit.** Take a decision, roadmap, or artifact and pressure-test it against the five principles. Return where it holds and where it drifts, with the smallest useful fix.

Use this skill when:

- a team cannot name which Blueprint phase its current work belongs to
- someone reaches for a tool (a prioritization score, a roadmap) before the problem is framed
- a decision needs a principled gut-check before it consumes a quarter
- a new Product Manager needs to learn a phase, not just complete a template

This is not a play itself. It does not produce an outcome tree, a persona, or a positioning statement. It diagnoses, teaches, and points to the play that does. It is also not a governance gate: it advises on sequence and principle, it does not approve or block work.

###### Usage Notes

- This is a **cross-phase navigator**, not a single canonical play. It sits above the play library and routes into it.
- Three modes: Navigate (place the team and point to the next play), Coach (go deep on one phase), Audit (test a decision against the five principles).
- Principle model: the five Optimal Product Process Principles are canonical; phase-level principles inherit and ladder up to them. Three orphan themes (Guardrails, Cross-Functional Ownership, Transparency) are surfaced as open decisions, never asserted as canon.
- Evidence gathering is **user artifacts only** - no web research offered. It works from the user's own account of their situation.
- Loose coupling: play names are pointers, never dependencies. If a play is not installed, the skill gives its gist and offers to do the work inline.

##### Key Concepts

###### Lead With Help, Not Process

The user came for help, not for a process. Answer first. Give something useful in the first breath and weave the diagnosis into the answer, rather than making the user earn it.

Match the response to the size of the ask. A question about ordering three or four features gets a direct suggestion plus, at most, one natural clarifying question. A vague "help me figure out our whole quarter" can justify a fuller diagnosis. Never treat a small question as a strategy offsite.

Hard rules:

- Never tell the user their question is wrong, a "tool question," or out of order. Just help, and fold in what matters.
- Never open with a menu, an entry-mode picker, an estimated question count, or a `Qx/n` label unless the user explicitly asks to be walked through something.
- Ask at most one question before giving value, and make it a real question in plain language, not an intake form.
- Do not lecture about the Blueprint or recite principles at the user. The principle is your reasoning, not your opening line.

###### Route With What They Have, Not What You Wish They Had

Do not assume the play library is installed. Most people running this will have only some of the plays, and some will have none. A play name is a pointer, not a dependency. Whenever you point to a play:

- If it is available, name it and give a one-line reason.
- If it may not be, name it and add the gist of what it does in a sentence, so the user can act without it, and offer to do that thinking with them right here.
- Never end a response with only a list of tools the user may not be able to open. The help has to stand on its own.

###### The Five Canonical Principles Are the Spine

The Blueprint was built on the **Optimal Product Process Principles**: Outcome Obsessed, Feedback Driven, Environment Adaptive, Dynamic Interactivity, Ruthlessly Distilled. These are process principles, not phase-level behaviors. Every phase-level principle in the reference ladders up to one of the five. When the skill cites a principle it names the canonical five first, then the phase-level expression beneath it, never the reverse. This keeps the five front and center instead of letting principles multiply into an unmemorable manual.

###### The Blueprint Has Five Phases, One With Three Facets

The Blueprint phases are Context, Discover + Investigate, Discover + Define, Create, Deliver. Context carries three facets that a team works in parallel: Internal Values and Strategy, Market Environment, and Customers and Users. The reference treats these as facets of the one Context phase, not separate phases, so the phase vocabulary matches the Productside Blueprint.

###### The Blueprint Is a Cycle, Not a Line

Phases run non-linear, concurrent, and constant. That is the Dynamic Interactivity principle. A team can sit in two phases at once or loop back. The skill never forces a clean sequence. When a team genuinely straddles two phases, it names both and prioritizes the one carrying the highest unresolved risk.

###### Diagnose Silently, Then Help

The phase and the governing principle are how you reason, not what you say first. Work out where the user is and which principle is at stake in your own head, then lead with the help that follows from it. Name the phase or the principle only when saying it out loud makes the advice land better. A user should feel understood, not processed. If you catch yourself writing "you are in phase X, the governing principle is Y" before you have given the user anything useful, stop and lead with the useful part.

###### Orphans Are Surfaced, Never Asserted

Three themes in the current materials do not ladder up to the five: Guardrails, Cross-Functional Ownership and Enablement, and Transparency. The skill surfaces these when a phase raises them and labels them open decisions for the Productside team. It never presents them as canonical principles and never quietly folds them in.

###### How AI Supports This Play

The Blueprint pages have no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it). Here AI works as a **navigator**: it reads the team's situation, places the work on the Blueprint, names the principle at stake, and points to the next Play. Where the team really is, and what it runs next, stays the team's call.

- **Use it when:** a team is unsure which phase its work belongs to, or what to do next, or wants a decision audited against the five principles.
- **Avoid it when:** the request is for the skill to set the team's strategy. It knows the Blueprint, not the business.
- **Return:** help first, with the phase read, the principle at stake, and the next Play woven in, each Play with a one-line gist so the advice works even if the Play is not installed.

###### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

###### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

##### Application

Reads from [Blueprint reference](playbook-skills.md#psk-blueprint-advisor--instructions) for all phase content, principle mappings, and play routing. Use [Template](playbook-skills.md#psk-blueprint-advisor--template) for the audit output scaffold. Worked runs are in [Examples](playbook-skills.md#psk-blueprint-advisor--examples).

###### Step 1: Answer the Question in Front of You

Start by helping. Read what the user actually asked and give a useful response to that, sized to the ask. Fold the diagnosis into the answer. For a small, concrete question, that is a direct suggestion plus, at most, one natural clarifying question. Save the fuller diagnosis in Step 3 for requests that are genuinely broad, or where the user is clearly unsure where they are.

Guard your own assumptions silently. Models default to picturing the customer as a developer or engineer and the team as a software squad, and most Productside work is not that. Check your own mental picture of who the product serves before you route. If it changes the answer and you genuinely cannot tell, ask it as a normal question ("who mostly uses this, and what's their day job?"), never as a mandatory opening interrogation and never as a gate on getting help.

###### Step 2: Draw on Evidence Only as the Request Needs It

When a request is broad enough to need grounding, lean on artifacts and the user's own account of their situation. Do not offer web research, and do not front-load a document request. Pull in what already exists as it becomes relevant: strategy or outcome artifacts, discovery evidence, delivery signal. Accept equivalent data from any source, and never gate help on whether a specific upstream play was run.

###### Step 3: Diagnose the Phase When the Ask Is Broad (Navigate)

For a broad or unsure request, place the team. You rarely need to ask all of these out loud. Infer what you can from what they already said, and ask only the one or two that actually change the answer:

1. What is the team trying to decide or move right now?
2. What is already validated with real customers, and what is still assumption?
3. What is the biggest unknown or risk in front of you?
4. What have you already shipped or tested, if anything?

Then help, weaving in rather than reciting: which phase they are in (and a second phase if they straddle two) and why, what good and bad look like there, the governing principle when naming it helps, and the next play or plays. For each play give a one-line reason and a one-line gist, so the advice works even if the user never opens it or does not have it installed. Write it as a person talking, not as labeled fields, and never announce the phase before you have given them something useful.

###### Step 4: Coach a Phase (Coach)

When the user picks a phase, or Navigate hands one over, walk the full phase from the reference: objective, tasks (what good looks like), anti-patterns (what bad looks like), governing principles with their canonical parents, the plays that live there, and explicit exit criteria. Teach the principle, do not just cite it.

###### Step 5: Audit a Decision (Audit)

Take the decision, roadmap, or artifact provided. For each of the five principles return a one-line verdict, holds, at risk, or violated, with the specific evidence from their input. Lead with violations. End with the smallest change that would move each violated principle back to holding. If an orphan theme is clearly relevant, note it separately as an open question, not as a scored principle.

###### Output Convention

Help first, always. Lead with the useful answer and keep the diagnosis woven in and brief. Name a canonical principle only when it sharpens the point, and when you do, use the canonical five, not a phase-level label. Assume the plays may not be installed: every play you point to carries a one-line gist so the advice works even if the user never opens it, and you offer to do that thinking inline. Length follows the ask: short question, short answer.

#### psk-blueprint-advisor / Template

Working scaffold for pressure-testing a decision, roadmap, or artifact against the five Optimal Product Process Principles. Fill the brackets. Lead with violations.

###### Under Review

`[one or two sentences: the decision, roadmap, or artifact being audited]`

> Quality check: state a real decision with a commitment attached, not a vague intention. If there is no commitment at stake, this is Coach or Navigate, not Audit.

###### Verdict by Principle

Each line: principle, verdict (holds / at risk / violated), evidence from the input.

- **Outcome Obsessed** - `[holds | at risk | violated]` - `[evidence]`
- **Feedback Driven** - `[holds | at risk | violated]` - `[evidence]`
- **Environment Adaptive** - `[holds | at risk | violated]` - `[evidence]`
- **Dynamic Interactivity** - `[holds | at risk | violated]` - `[evidence]`
- **Ruthlessly Distilled** - `[holds | at risk | violated]` - `[evidence]`

> Quality check: every verdict cites specific evidence from the input, not a general observation. Name the canonical principle, not a phase-level expression.

###### Smallest Fixes (violations first)

For each violated or at-risk principle, the smallest change that returns it to holding.

1. `[principle]`: `[smallest useful change]`
2. `[principle]`: `[smallest useful change]`

> Quality check: a fix is an action the team can take this week, not a restatement of the problem.

###### Orphan Flags (if relevant)

`[Guardrails / Cross-Functional Ownership / Transparency, only if the decision clearly raises one]`

> Capacity: keep this to open questions for the Productside team. Do not score orphans as if they were canonical principles.

###### Lead Action

`[the single next step, usually the fix for the most damaging violation]`

#### psk-blueprint-advisor / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** Dispatchers have not adopted route optimization. Review Deliver signals and return to discovery before planning version two.
- **Weak:** Accepting the requested version-two roadmap assumes the solution before diagnosing the adoption problem.
- **Drift to avoid:** Principle drift: presenting a phase-specific theme as a sixth canonical principle. Use the five canonical principles and label unresolved themes.


##### Common Pitfalls

- **Process Theater on a Simple Question:** Help first. Answer the question, keep the diagnosis under the surface, and ask at most one natural question if it genuinely changes the answer. Reserve the full guided flow for when the user asks for it or the request is genuinely broad.

- **Answering Blind Instead of Weaving In the One Thing That Matters:** The fix is not to refuse and interrogate, and it is not to answer blind. Give real help and fold in the single check that changes it, in one natural sentence, the way a good colleague would.

- **Routing to Plays the User Does Not Have:** Treat play names as optional pointers. Give the gist of each in a line, make the advice stand on its own, and offer to do the work inline.

- **Citing Phase-Level Principles as if They Were Canonical:** Name the canonical principle first (Ruthlessly Distilled), then its phase expression (Segment Ruthlessly).

- **Assuming a Software Team Serving Software Users:** Run the silent assumption check in Step 1. Name the actual customer role and team composition, and let them shape the phase call and the routing.

- **Forcing a Linear Sequence:** Allow straddling. Name both phases, then prioritize the one carrying the highest unresolved risk.

- **Absorbing Orphan Themes Silently:** Surface orphans as labeled open decisions, never scored as canonical principles.

##### Blueprint Reference

Knowledge base for psk-blueprint-advisor. Single source of truth the skill reads from. The five principles stay canonical; the phases inherit from them.

##### The Five Canonical Principles

The Blueprint was built on the **Optimal Product Process Principles**. These are process principles: they describe how the process behaves, not how a Product Manager behaves inside one phase. Everything downstream inherits from these five.

1. **Outcome Obsessed.** Produces measurable outcomes directly tied to a well-defined product strategy.
2. **Feedback Driven.** Incorporates constant learning from end-users and customers.
3. **Environment Adaptive.** Works regardless of size, type, development methodology, or market conditions.
4. **Dynamic Interactivity.** Operates in the realistic context of non-linear, concurrent, constant activity.
5. **Ruthlessly Distilled.** Provides the simplest path from problem to solution, and intentionally discards dead-ends, projects, and products.

Design rule: every phase-level principle must ladder up to one of the five. If it cannot, it is either noise to cut or a genuinely new theme that has to earn its way into the canonical set by explicit decision. Two themes do not ladder up cleanly and are marked ORPHAN below: Guardrails, and Cross-Functional Ownership and Enablement.

##### The Five Phases

The Blueprint has five phases: Context, Discover + Investigate, Discover + Define, Create, Deliver. Context carries three facets a team works in parallel: Internal Values and Strategy, Market Environment, and Customers and Users. They are facets of one phase, not separate phases.

---

##### Phase 1: Context

Objective: clarify strategy, market reality, and customer value into measurable business objectives that guide product decisions. Worked across three facets.

###### Facet A: Internal Values and Strategy

What good looks like: translate company strategy into product-level business outcomes using outcome trees; define decision guardrails (pricing, regulatory, brand); inventory portfolio dependencies and scope boundaries.

What bad looks like: vision theater (lofty narratives without metrics); conflating OKRs with strategy; a roadmap driven by politics instead of declared outcomes.

Principles (phase to canonical parent): Clarity of Purpose to Outcome Obsessed; Alignment Before Action to Dynamic Interactivity; Outcomes Over Outputs to Outcome Obsessed; Guardrails Matter to ORPHAN; Focus is a Superpower to Ruthlessly Distilled; Strategy is a Living System to Dynamic Interactivity; Humility and Curiosity to Feedback Driven.

###### Facet B: Market Environment

What good looks like: PESTEL tied to hypotheses; competitor and substitute analysis beyond feature lists; validate market size and channel economics; segment and find promising opportunities.

What bad looks like: feature scorecards ignoring buyer economics; annual market reviews that are never updated.

Principles: External Reality Rules to Environment Adaptive; Continuous Vigilance to Environment Adaptive; Competitors Are Teachers to Feedback Driven; Economics Drive Strategy to Outcome Obsessed; Segment Ruthlessly to Ruthlessly Distilled; Evidence Over Ego to Feedback Driven; Adaptation Is Survival to Environment Adaptive.

###### Facet C: Customers and Users

What good looks like: segment by job and context, not just firmographics; empathy interviews synthesized with quantitative data; proto-personas and value paths tied to outcomes, then validated.

What bad looks like: treating customers as a monolith; over-reliance on analytics without direct conversations.

Principles: Empathy First to Feedback Driven; Jobs-to-be-Done Over Demographics to Ruthlessly Distilled; Value Is Defined by the Customer to Outcome Obsessed; Diversity of Perspective to Environment Adaptive; Validation Is Continuous to Feedback Driven; Listen Beyond the Obvious to Feedback Driven; Bias Toward Actionable Insight to Ruthlessly Distilled.

Plays for Context: psk-outcome-strategy-discussion, psk-stakeholder-alignment, psk-outcome-tree, psk-market-selection-sizing (Facet B: name the market, PESTEL, segments with real buyers and users, sourced TAM/SAM/SOM), psk-jobs-to-be-done, psk-proto-persona.

Exit criteria: measurable business objectives named, the primary customer and their job defined, and a defensible read of market and economics.

---

##### Phase 2: Discover + Investigate

Objective: explore the problem space to surface and prioritize opportunities tied to business outcomes and customer value.

What good looks like: assess pains and gains, frequency, willingness-to-pay; triangulate qualitative, quantitative, and market evidence for early fit signals; frame problems clearly; run empathy interviews and synthesize; validate the problem space with experiments.

What bad looks like: premature solutioning; research without decision questions or kill criteria; one-big-bet thinking without a portfolio of options.

Principles: Problem Before Solution to Ruthlessly Distilled; Evidence Over Assumption to Feedback Driven; Portfolio Thinking to Ruthlessly Distilled; Customer Value as North Star to Outcome Obsessed; Iterative Validation to Feedback Driven; Bias Toward Action to Ruthlessly Distilled; Transparency in Decision-Making to ORPHAN.

Plays: psk-empathy-interviews, psk-affinity-mapping, psk-problem-identification, psk-framing-the-problem.

Exit criteria: a framed, evidence-backed problem worth solving, with a kill criterion, not just a list of ideas.

---

##### Phase 3: Discover + Define

Objective: select the best solution approach and de-risk value, feasibility, and viability before scaling.

What good looks like: solution hypotheses and positioning via how-might-we questions; low-fidelity experiments with success metrics set up front; financial and risk analysis; a business model (monetization, channels, go-to-market); a business case tied to outcomes; feasibility checked with stakeholders.

What bad looks like: testing desirability while ignoring viability; treating the MVP as version one instead of a learning vehicle; chasing vanity metrics.

Principles: Solution Fit Is Earned Not Assumed to Feedback Driven; De-Risk Early and Often to Ruthlessly Distilled; Hypotheses Drive Action to Feedback Driven; Success Is Measured Not Declared to Outcome Obsessed; Business Model Awareness to Outcome Obsessed; Stakeholder Engagement Is Continuous to Dynamic Interactivity; Learning Is the Goal to Feedback Driven.

Plays: psk-exploring-solution-space, psk-solution-hypothesis, psk-positioning-statement, psk-lofi-experimentation, psk-storyboarding (a lo-fi way to test the value proposition with real customers), psk-risk-assessment, psk-product-outcome-canvas.

Exit criteria: value, feasibility, and viability each backed by evidence, and a business case tying the chosen solution to a named outcome.

---

##### Phase 4: Create

Objective: prepare product and organization for success through roadmaps, specs, enablement, and launch strategy.

What good looks like: outcome-based roadmaps tied to metrics; backlog shaped by decision rules from Context and Define; readiness planned across support, pricing, and go-to-market; controlled rollouts; support and defect pathways instrumented.

What bad looks like: roadmaps as commitment contracts disconnected from learning; over-specifying early and under-specifying late; treating enablement and pricing as marketing's job.

Principles: Readiness Is Holistic to ORPHAN (Cross-Functional Ownership); Outcome-Based Planning to Outcome Obsessed; Specs Match Uncertainty to Ruthlessly Distilled; Enablement Is a Team Sport to ORPHAN (Cross-Functional Ownership); Iterate Toward Launch to Dynamic Interactivity; Decision Rules Are Explicit to Outcome Obsessed; Risk Management Is Proactive to Ruthlessly Distilled.

Plays: psk-outcome-roadmap, psk-tiny-acts-discovery, psk-output-prioritization, psk-go-to-market, psk-product-readiness.

Exit criteria: the product and the organization are both ready, with a controlled rollout plan and explicit backlog decision rules.

---

##### Phase 5: Deliver

Objective: ship, learn, and sustain growth through measurement and iteration.

What good looks like: manage the lifecycle as the category evolves; measure the buying journey continuously; evaluate post-launch metrics and make reinvest-or-retire decisions; keep discovery continuous.

What bad looks like: declaring victory and shipping without measurement; success theater with vanity adoption metrics; treating roadmap changes as failure instead of learning.

Principles: Learning Never Stops to Feedback Driven; Value Is Proven Not Assumed to Outcome Obsessed; Health Is Managed Proactively to Environment Adaptive; Transparency in Outcomes to ORPHAN; Customer Advocacy Is Ongoing to Feedback Driven; Cross-Functional Ownership to ORPHAN (Cross-Functional Ownership); Adaptation Is Strength to Environment Adaptive.

Plays: psk-measuring-outcomes, psk-process-retrospective.

Exit criteria: value proven with real metrics, and a clear reinvest-or-retire decision rather than a default to continue.

---

##### Orphan Themes (Open Decisions)

These phase-level themes do not ladder up to the five. Do not silently absorb them. Decide.

1. **Guardrails** (ethical, regulatory, brand), appears in Context. Candidate sixth principle, or fold under Outcome Obsessed as a constraint on which outcomes are legitimate.
2. **Cross-Functional Ownership and Enablement**, appears in Create and Deliver. Candidate sixth principle, or treat as an execution norm rather than a process principle.
3. **Transparency in Decision-Making and Outcomes**, appears in Discover + Investigate and Deliver. Arguably a practice serving Feedback Driven and Outcome Obsessed rather than a standalone principle.

The advisor surfaces these when relevant but never asserts them as canonical. That decision belongs to the Productside team.


##### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-blueprint-advisor) for supporting source material and expanded examples.


## Context


### Play 01: Outcome & Strategy Discussion

Stable identifier: `psk-outcome-strategy-discussion`.

#### psk-outcome-strategy-discussion / Instructions

##### Purpose

Run the opening play of the Productside Playbook.

Before discovery begins, a PM needs one thing: a clear, shared understanding of the business outcome they are being asked to achieve. This play produces that understanding through a structured guided discussion with a manager, executive sponsor, or product leadership. The agent helps the PM prepare for that conversation and document what emerges from it. The conversation itself is PM-owned.

Use this skill when you need to:

- prepare a structured discussion guide before meeting with a manager or sponsor
- document the business outcome, context, and success criteria after the conversation
- surface assumptions the PM is already carrying so they can be validated rather than asserted
- make a Key Decision Point call: proceed to discovery, escalate for clarity, or reschedule

This is not a requirements intake. The PM is not receiving a brief. The PM is facilitating a two-way alignment where both parties build shared understanding. If the manager is dictating solutions during a conversation about outcomes, that is a signal to redirect.

##### Key Concepts

###### 1. Guided Discussion vs. Requirements Handoff

A requirements handoff is one-directional: someone tells you what to build. A guided discussion is two-directional: both parties contribute to building shared understanding of what the business needs to achieve and why.

The PM facilitates the discussion by asking open-ended questions, pressing when answers are vague, and recording what emerges. The manager or sponsor provides context, constraints, and strategic rationale. The output is not a spec. It is a shared written record of the alignment reached.

If a PM enters this conversation expecting to receive a feature list, they will miss the purpose of the play. The goal is a business outcome, not a scope document.

###### 2. Business Outcome First

The central task of this play is establishing the business outcome: what the organization is trying to achieve at a strategic or operational level. This is not a feature. It is not a project milestone. It is a measurable change in the state of the business.

Weak: "Launch the new shipper dashboard by Q3"
Stronger: "Reduce 90-day churn among mid-market shippers by 15%"

The launch is an output. The churn reduction is an outcome. This distinction matters because discovery cannot begin without clarity on the outcome. If the PM starts discovery while the business outcome is still defined as a project scope, they will optimize for the project and miss the customer problem.

###### 3. The Key Decision Point (KDP)

At the end of this play, the PM makes an explicit call about whether to proceed.

- Go: alignment is clear, the PM proceeds to discovery
- Partial: some areas are clear, others need follow-up by a specific date
- No-go: alignment is missing or contradictory - escalate or reschedule before continuing

The KDP is not a formality. Skipping it is the failure mode where a PM enters discovery without a stable business outcome and then produces research that no one can act on because the frame is still contested. If the manager cannot agree on the outcome, the PM should not proceed - they should surface the disagreement and request a follow-up.

###### 4. Three Roles of the PM in This Play

The PM wears three hats during this play:

- **Facilitator:** asks open-ended questions, creates space for the manager to think aloud, follows up when answers are vague or contradictory
- **Recorder:** captures what the manager says in structured notes during or immediately after the conversation, writes the agreed business outcome in one clear sentence
- **Sense-maker:** reviews the notes afterward to find gaps, contradictions, and unstated assumptions; flags open questions before starting discovery

The agent supports preparation (before) and documentation (after). The PM owns the middle.

###### 5. Preparing the Guide vs. Running the Discussion vs. Documenting Results

There are three distinct phases of this play:

- **Preparing the guide (agent-supported):** Draft open-ended questions for each discussion area. Surface assumptions the PM already holds. Flag visible gaps or contradictions before the conversation begins.
- **Running the discussion (PM-owned, agent cannot participate):** The PM facilitates the conversation, takes notes, and makes judgment calls in real time. The agent cannot do this.
- **Documenting outcomes (agent-supported):** After the conversation, the PM shares their notes with the agent, who helps structure the summary, identify gaps, and draft the KDP call.

If the user asks the agent to conduct the discussion itself or generate what "the manager probably said," redirect: the discussion must happen with a real person who has context the agent does not have.

###### 6. The Five Discussion Areas

Every guided discussion for this play covers five areas:

1. **Business Outcome** - what the business needs to achieve, written as a measurable change
2. **Why Now** - what changed that makes this the priority, and what happens if it is not addressed
3. **Customer** - who the product serves (role and context), and whether there are secondary stakeholders
4. **Success Criteria** - what measurable change would indicate the outcome was achieved
5. **Constraints and Non-Negotiables** - what is already decided, what is off-limits, and what dependencies exist

These five areas are the structure of both the discussion guide and the documentation template. A conversation that covers all five and produces specific, agreed answers is a successful execution of this play.

###### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **preparation coach for the discussion, never a stand-in for the manager**. It helps the PM gather what they already know, turn it into sharp, unbiased questions for each discussion area, and name the decision the discussion must reach. The answers come from the manager, in the room.

- **Use it when:** the PM has gathered the key documents and wants to prepare questions for the discussion, or has notes from the discussion to turn into the template.
- **Avoid it when:** the request is to guess what the manager will say, or to fill the discussion template without the discussion happening.
- **Return:** the PM's own questions for each discussion area, tested for bias and clarity; the business outcome stated as a measurable change; and, after the discussion, the template filled only from the PM's notes.

###### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

###### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

##### Application

Use [Template](playbook-skills.md#psk-outcome-strategy-discussion--template) for the working scaffold.


###### Required Output Convention

Default to a **clean, paste-ready structured summary** with clearly labeled sections.

That means:

- fill all five discussion areas
- write the business outcome as a single, specific, measurable sentence
- keep the customer statement concrete (a job title and context, not an org chart entry)
- list open questions rather than omitting them
- write the KDP call with a checkbox clearly marked

The summary comes first. Commentary is secondary.

###### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses Discovery mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

###### Step 1: Confirm Scope and Participants

Before preparing the guide, establish:

- Who is the discussion with? (direct manager, exec sponsor, product leadership - name and role if possible)
- What product or initiative is this for?
- What is the time horizon? (quarterly, annual, multi-year)
- Has any prior alignment work been done? (existing OKRs, product brief, strategy deck)

This play does not require a tech-role bias guard. The subject of this conversation is internal strategic alignment, not a customer persona. The customer who the product serves will be identified during the discussion and documented afterward - they are not the subject of this exercise.

Note any prior materials the PM already has, because they will inform which questions can be skipped and which need more depth.

###### Step 2: Prepare the Discussion Guide

Draft open-ended questions for each of the five discussion areas. Questions should:

- invite the manager to think and articulate, not confirm a preformed answer
- be specific enough to prevent vague responses without being leading
- follow a logical progression from big picture to specifics

For each area, also surface the assumptions the PM is already carrying. Write them explicitly so they can be validated (confirmed or corrected) during the conversation rather than treated as facts.

Flag any gaps or contradictions already visible before the conversation. If the PM says "I think we're trying to reduce churn but my manager mentioned a revenue target last quarter," that contradiction should be in the prep guide so the PM knows to resolve it.

**Sample questions for each area:**

Business Outcome:
- What does the business need to achieve in the next [time horizon]?
- How does this connect to our broader strategy or annual goals?
- How will we know, in [X months], that we achieved it?

Why Now:
- What changed that makes this the priority now?
- What happens if we do not address this this quarter or year?

Customer:
- Who is the primary customer this outcome serves?
- Are there secondary customers or stakeholders whose needs we must also respect?

Success Criteria:
- What would measurable success look like at [time horizon]?
- Are there existing metrics or targets we are accountable to?

Constraints and Non-Negotiables:
- What is already decided - budget, timeline, technology choices?
- What is off-limits or outside scope?
- Are there dependencies we must work around?

###### Step 3: Run the Discussion (PM-Owned)

This step is performed by the PM. The agent does not participate.

The PM should:

- facilitate rather than receive (ask questions, follow up, redirect solution-talk back to outcome-talk)
- take notes during or immediately after the conversation
- watch for vague answers and press for specifics ("improve performance" needs a metric; "grow the business" needs a direction and timeframe)
- note when the manager starts proposing solutions - this is a signal that the outcome is not yet clear
- watch for false alignment: both parties nodding without actually agreeing on specifics

**What good alignment feels like:** both parties can state the business outcome in the same specific terms, the customer is named by role and context (not by org chart), and both parties agree on at least one measurable success criterion.

**What false alignment looks like:** the meeting ends with everyone feeling satisfied, but the PM's notes contain phrases like "something around retention," "the usual metrics," or "they mentioned a few things."

###### Step 4: Document the Outcomes

After the conversation, the PM shares their notes and the agent helps structure the summary.

The summary has five sections matching the five discussion areas:

- **Business Outcome:** one clear sentence naming a measurable change
- **Why It Matters Now:** one to two sentences on rationale and urgency
- **Customer:** who the product serves - a job title and context, not a persona name at this stage
- **Success Criteria:** a table with the criteria, the metric or signal, and the target
- **Constraints:** a bullet list of fixed constraints and non-negotiables

In addition, document:

- **Open Questions and Gaps:** anything that was contested, unclear, or left unresolved during the conversation

Be specific about what was agreed and what was not. Papering over gaps at this stage means discovering them later when fixing them is harder.

###### Step 5: Make the KDP Call

After the summary is complete, the PM makes an explicit Key Decision Point decision:

- **Go:** alignment is clear across all five areas. The PM proceeds to discovery.
- **Partial:** most areas are clear, but one or two need follow-up. Document which areas, what is unclear, and a target date for resolution. The PM should not begin full discovery until partial items are resolved.
- **No-go:** the business outcome is still contested, the customer is undefined, or success criteria are absent. The PM escalates the misalignment to the manager or reschedules before continuing.

The agent can help draft the KDP statement, but the call belongs to the PM.

#### psk-outcome-strategy-discussion / Template

###### When to Use This

Use this template before discovery begins to document the alignment conversation between a PM and their manager or executive sponsor. The conversation must happen first. Fill in the outcome section after the discussion, not before.

Completing this template is the exit condition for this play. Do not begin discovery work until the Key Decision Point is marked.

---

###### Template

```markdown
# Outcome & Strategy: Guided Discussion

## Scope

- Discussion with: [name and role]
- Initiative or product: [name]
- Date: [date]
- Time horizon: [quarter / year / multi-year]

---

## Discussion Guide

Use these questions to facilitate the conversation. They are prompts, not a script. Follow the thread wherever it leads, and return to unanswered areas before the meeting ends.

### 1. Business Outcome

- What does the business need to achieve in the next [time horizon]?
- How does this connect to our broader strategy or annual goals?
- How will we know, in [X months], that we achieved it?

### 2. Why Now

- What changed that makes this the priority now?
- What happens if we do not address this this quarter or year?

### 3. Customer

- Who is the primary customer this outcome serves?
- Are there secondary customers or stakeholders whose needs we must also respect?

### 4. Success Criteria

- What would measurable success look like at [time horizon]?
- Are there existing metrics or targets we are accountable to?

### 5. Constraints and Non-Negotiables

- What is already decided - budget, timeline, technology choices?
- What is off-limits or outside scope?
- Are there dependencies we must work around?

---

## Outcome of the Discussion

Complete this section after the conversation.

### Business Outcome (one sentence)

[Write the agreed business outcome here. It must name a measurable change, not a project or a feature.]

### Why It Matters Now

[One to two sentences covering the rationale and urgency.]

### Customer

[Who the product serves - a job title and context, not a persona name at this stage. Example: mid-market shipper operations manager responsible for carrier selection and freight cost management.]

### Success Criteria

| Criteria | Metric or Signal | Target |
|---|---|---|
| | | |
| | | |
| | | |

### Constraints

- [Constraint or non-negotiable]
- [Constraint or non-negotiable]
- [Constraint or non-negotiable]

### Open Questions and Gaps

List anything that was contested, unclear, or left unresolved. Do not omit these to make the summary look complete.

- [Open question or gap]
- [Open question or gap]

---

## Key Decision Point

Mark one.

- [ ] Go: alignment is clear across all five areas. Proceed to discovery.
- [ ] Partial: [specify which areas need follow-up and by what date]
- [ ] No-go: [specify what needs escalation or re-discussion before continuing]

---

> **Quality checks**
> - Is the business outcome written as a measurable change, not a feature or project milestone?
> - Does the customer statement name a real role in a real context, not an org or a function?
> - Are the success criteria specific enough that a third party could assess them?
> - Are open questions documented rather than papered over with placeholder language?
> - Is the KDP explicitly marked?

> **Capacity note**
> The discussion summary should be readable in under five minutes. If it runs longer, consolidate. The purpose of this document is shared alignment, not comprehensive documentation.
```

#### psk-outcome-strategy-discussion / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For shipper retention, align with the manager on the business result, customer, decision boundaries, and evidence needed before discovery.
- **Weak:** "Improve retention somehow" leaves the result and authority unclear.
- **Drift to avoid:** Outcome as project: "Launch a shipper portal" is an output. Establish the business change it is expected to produce.


##### Common Pitfalls

- **Treating the Discussion as a Requirements Intake:** Before the meeting, reframe the purpose: the PM is there to understand what the business needs to achieve, not what to build. If the manager jumps to solutions, the PM redirects: "That sounds like one approach - can we first align on what success looks like for the business overall?"

- **Accepting Vague Outcomes Without Pressing:** Press for specifics. "Improve customer satisfaction" needs a metric and a direction: "Increase NPS from 32 to 50 within 12 months." If the manager cannot provide a specific target, write "TBD" and flag it as a gap that must be resolved before discovery begins.

- **Skipping the KDP:** Treat the KDP as a required output, not an optional reflection. Before starting discovery, the PM should have a written KDP statement on file.

- **Letting the Manager Dictate the Solution:** Solutions that emerge during an outcomes conversation are hypotheses, not decisions. Record them in the open questions section and flag them for validation during discovery.

- **Documenting the Conversation Without Identifying the Gaps:** In the open questions section, be explicit about what was not resolved. A summary with two or three open questions documented is more useful than a summary with five areas filled in with uncertain answers.

- **Confusing Internal Stakeholders with the Customer:** The customer field in this play refers to who the product serves in the field - the person who uses or buys the thing the PM is building. If the product is built for external users, the customer is external. If the product is internal tooling, the customer is the internal user population (not the sponsoring executive).

- **AI Answers for the Manager:** Prepare questions, not answers. Fill the template only from notes of the real discussion, and mark anything still unconfirmed.

##### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-outcome-strategy-discussion) for supporting source material and expanded examples.


### Play 02: Stakeholder Alignment

Stable identifier: `psk-stakeholder-alignment`.

#### psk-stakeholder-alignment / Instructions

##### Purpose

Build a **complete stakeholder map** before discovery begins.

This skill is for the **Context** phase, the second play in the Productside Playbook. It helps a Product Manager identify every person who affects or is affected by their initiative, rate each one by interest and influence, and assign engagement strategies that are specific enough to act on.

A stakeholder map is not a one-time artifact. It is a working tool that should be updated as relationships shift, as skeptics become allies, and as new influencers surface during discovery and delivery.

Use this skill when you need to:

- understand who has power over your initiative before you start
- identify skeptics and blockers before they become problems
- assign engagement strategies that match the actual relationship, not a generic default
- give the team a shared picture of the political landscape

This play comes before empathy interviews and discovery work. The map guides who to recruit, who to brief, and who to watch.

This is not a communications plan, a RACI chart, or a customer list. A communications plan describes when and how to send updates. A RACI describes task ownership. A customer list belongs in the persona play. The stakeholder map does something different: it determines who has input into which decisions and at what depth, before discovery shapes those decisions.

##### Key Concepts

###### Stakeholder vs. Customer

These are distinct categories and must not be conflated.

**Stakeholders** are internal or partner-side people who affect or are affected by the PM's work. They live inside the organization or at the boundary (executives, legal, finance, engineering leads, partner teams). They need to be managed, informed, or satisfied.

**Customers** are the people the product serves in the field. They experience the problem the product is solving. They belong in the persona play (psk-proto-persona), not in the stakeholder map.

Mixing customers into the stakeholder table creates confusion about who needs organizational engagement vs. who needs product discovery. The two groups need fundamentally different treatment.

###### Interest vs. Influence

These two dimensions are independent. Either can be high or low regardless of the other.

**Interest** is how much a stakeholder cares about this specific initiative. A legal counsel may not care about most product initiatives but may be intensely interested in one that touches data privacy.

**Influence** is how much power a stakeholder has over the initiative. Influence is not the same as seniority. A junior engineer who controls the deployment pipeline has high influence. A VP who has no say in technical decisions may have lower influence than their title suggests.

Rating both dimensions separately, and honestly, is the whole point of the matrix.

###### The Four Engagement Modes

The Interest/Influence matrix places stakeholders in one of four quadrants, each with a different engagement strategy:

**Manage closely (High Influence, High Interest):** These are your key partners. They care, and they have power. Involve them early, keep them informed in detail, and make them feel like co-owners where possible. Weekly touchpoints or embedded collaboration. Surprises here are costly.

**Keep satisfied (High Influence, Low Interest):** These are often executive sponsors who are not day-to-day participants. They have the power to greenlight or block, but they do not want to be in every meeting. Keep them briefed at the right altitude - progress, risks, key decisions - without pulling them into operational detail.

**Keep informed (Low Influence, High Interest):** These stakeholders care deeply but cannot directly affect the outcome. They may be strong advocates or enthusiastic users of adjacent systems. Keep them updated through regular communications; they are often your best ambassadors if things go well.

**Monitor (Low Influence, Low Interest):** Minimal engagement needed. Check in periodically so they are not blindsided by major changes, but do not over-invest attention here.

###### Engagement Modes Are About Decision Rights, Not Just Communication

This is the distinction that matters most. Engagement modes are not a comms schedule  -  they determine who has input on which decisions and at what depth.

- **Manage Closely** stakeholders are in the room for trade-off discussions. They have a voice in decisions, not just updates.
- **Keep Satisfied** stakeholders are briefed on outcomes and key decisions, but they are not consulted in the decision process itself. They need altitude-appropriate information, not operational depth.
- **Keep Informed** stakeholders receive regular updates but do not affect decisions. Their value is advocacy and downstream adoption, not direction-setting.
- **Monitor** stakeholders are not in the decision loop at all. Periodic check-ins prevent surprises, but they do not shape the work.

Treating all engagement as a communication cadence question misses this. A PM who sends weekly updates to all stakeholders has not done stakeholder management  -  they have sent emails. The quadrant assignment determines who the PM brings into decisions, not just who receives communications.

###### The Map is a Working Tool

Relationships shift. A skeptic becomes an ally after a successful pilot. An executive who was "keep satisfied" suddenly becomes deeply involved after a business unit change. A new hire in legal introduces a regulatory concern no one anticipated.

Revisit the map at the start of each major phase: after framing, after discovery, before launch. The version you build before discovery is a starting hypothesis, not a final assessment.

###### Completeness Check

The most common failure mode is listing only supporters. A map full of advocates looks optimistic but is nearly useless when a skeptic surfaces during a key decision.

A good stakeholder map includes:

- supporters and champions
- skeptics and cautious observers
- potential blockers
- people who were not consulted on similar initiatives in the past and caused friction as a result

If the map skews entirely positive, something is missing.

###### Stakeholders Are Teammates, Not Opponents

Different functions bring different priorities: legal thinks about risk, finance thinks about returns, engineering thinks about technical feasibility. Those differences create friction  -  but they do not make stakeholders adversaries.

The playbook is explicit: you may have different roles, but you are all working on the same team. A skeptical legal counsel who raises a compliance concern in week two is not an obstacle  -  they are a teammate whose input prevented a problem at launch. A finance stakeholder who pushes back on scope is not blocking the product  -  they are enforcing a constraint that is real for the business.

Approach every stakeholder as someone who shares the organization's goals, even if they express those goals differently than you do. The map is a tool for building a communication strategy across that diversity, not a list of people to manage around.

###### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **critic of the stakeholder map the PM drafted**. It looks for stakeholders the PM missed, asks for the evidence behind each power and interest placement, and checks that each engagement strategy fits the quadrant. The placements and strategies stay the PM's, because only the PM knows these people.

- **Use it when:** the PM has listed stakeholders and wants the map pressure-tested for gaps and placement.
- **Avoid it when:** the request is to characterize real colleagues' motives or influence from a name and a title. The model doesn't know them. When given names and titles, first ask what the PM has observed about each person's decisions and influence, and name any roles that may be missing. Offer placements, each tagged `[AI-SUGGESTED, VALIDATE THIS]`, only if the PM then asks for a provisional Discovery draft.
- **Return:** missing stakeholder roles named for the PM to consider, each placement questioned against what the PM has observed, and engagement strategies checked against decision rights.

###### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

###### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

##### Application

Use [Template](playbook-skills.md#psk-stakeholder-alignment--template) for the full scaffold.


###### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses Discovery mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

###### Step 1: Tech-Role Bias Guard

Before drafting, pause and check who is missing.

In product work, the most visible stakeholders are often engineers, architects, or technical leads - the people the PM works with directly every day. They matter, but they are rarely the only stakeholders and often not the most influential ones.

Before drafting the table, explicitly ask: who else has interest or influence?

Check across these functions:

- Legal and compliance (especially if the initiative touches data, privacy, regulation, or contracts)
- Finance (if the initiative requires budget, headcount, or affects reported metrics)
- Sales and marketing (if the initiative changes the product the sales team sells or the story marketing tells)
- Customer success (if the initiative affects customer onboarding, support, or renewal)
- Operations (if the initiative changes workflows or operational capacity)
- Executive sponsors (who need to greenlight or protect the initiative at senior levels)

Technical roles may still make the list - but they should not be the only roles on it.

###### Step 2: Gather Internal Artifacts

Look at what already exists before writing anything new:

- Org charts or team rosters that show reporting lines and team boundaries
- Prior project retrospectives or postmortems that name who caused friction or was left out
- Prior communications or briefing documents that show who was engaged on similar initiatives
- Existing knowledge about who is skeptical, who is a champion, and who was burned by a previous failure

Ask: who was involved in similar initiatives before? Who was left out and caused problems later?

This is internal artifact work. No web research needed. The evidence lives in documents, relationships, and organizational memory.

###### Step 3: Build the Stakeholder Table

For each stakeholder, capture:

- **Name** - the person's actual name (4 words maximum)
- **Role / Team** - their title and team (6 words maximum)
- **Interest in This Initiative** - one clear sentence describing why they care (12 words maximum)
- **Influence** - High, Medium, or Low
- **Sentiment** - Supportive, Neutral, Skeptical, or Unknown

Aim for 6 to 10 stakeholders. Fewer than six usually means someone important has been missed. More than fifteen usually means the ratings are inflated or the scope of "stakeholder" has been defined too broadly.

Better to include someone and de-prioritize them in the matrix than to miss them entirely.

###### Step 4: Place Stakeholders on the Interest/Influence Matrix

Assign each stakeholder to one of the four quadrants based on their interest and influence ratings.

After placing everyone, check for balance. A map where every stakeholder lands in "manage closely" is a signal that ratings have been inflated. Not every stakeholder is a high-priority engagement. If the ratings feel off, recalibrate.

###### Step 5: Assign Engagement Strategies

For each quadrant, write a brief, specific engagement strategy.

Specific is better than generic:

- "Weekly async update via Slack with decision log" is actionable.
- "Keep informed" is not.

Each strategy should answer: how often, what to share, and what to ask for.

###### Step 6: Identify Risks and Gaps

Three things to capture before closing the map:

**Missing stakeholders:** Anyone who should be here but is not yet identified. A good check is asking: who has blocked similar work in the past? Who has authority that has not been mentioned yet?

**Potential blockers:** Stakeholders who could slow or stop progress if not engaged early. These may not be formal opponents - they may simply be people who will raise concerns at a late stage if they feel uninvolved.

**Political dynamics:** Relationships between stakeholders that create complexity. For example: two stakeholders who have a history of conflict, or a senior stakeholder whose opinion a key influencer defers to entirely.

#### psk-stakeholder-alignment / Template

Use this template to build a **Productside-style stakeholder map** before discovery begins.

If some stakeholders are not yet identified, note that in the Risks and Gaps section rather than leaving the table sparse. A complete map with unknowns flagged is more useful than a partial map that looks tidy.

###### When to Use This

Use this during the Context phase, before empathy interviews or discovery work begins. The stakeholder map tells you who to involve, who to brief, and who to watch.

###### Template

```markdown
# Stakeholder Alignment

## Context

- Initiative / product: [name]
- PM: [name]
- Date: [date]

---

## Stakeholder Table

| Name | Role / Team | Interest in This Initiative | Influence | Sentiment |
|---|---|---|---|---|
| | | | High / Medium / Low | Supportive / Neutral / Skeptical / Unknown |
| | | | High / Medium / Low | Supportive / Neutral / Skeptical / Unknown |
| | | | High / Medium / Low | Supportive / Neutral / Skeptical / Unknown |
| | | | High / Medium / Low | Supportive / Neutral / Skeptical / Unknown |
| | | | High / Medium / Low | Supportive / Neutral / Skeptical / Unknown |
| | | | High / Medium / Low | Supportive / Neutral / Skeptical / Unknown |
| | | | High / Medium / Low | Supportive / Neutral / Skeptical / Unknown |
| | | | High / Medium / Low | Supportive / Neutral / Skeptical / Unknown |

> Aim for at least 6-10 stakeholders. Include skeptics and potential blockers, not just supporters.

---

## Interest / Influence Matrix

### Manage Closely (High Influence, High Interest)
[List names]
- Engagement: [frequency and format - e.g., "weekly 1:1, shared decision log, involved in key trade-off discussions"]

### Keep Satisfied (High Influence, Low Interest)
[List names]
- Engagement: [frequency and format - e.g., "monthly executive brief, flagged when decisions affect scope or budget"]

### Keep Informed (Low Influence, High Interest)
[List names]
- Engagement: [frequency and format - e.g., "biweekly async update via shared doc or Slack, invited to demos"]

### Monitor (Low Influence, Low Interest)
[List names]
- Engagement: [frequency and format - e.g., "quarterly check-in, notified of major milestones only"]

---

## Risks and Gaps

### Missing stakeholders
[Anyone who should be here but is not yet identified]

### Potential blockers
[Stakeholders who could slow or stop progress if not engaged early]

### Political dynamics
[Relationships between stakeholders that could affect how you engage them]

---

> **Quality checks**
> - Does the stakeholder table include skeptics and blockers, not just supporters?
> - Is "influence" based on actual power over this initiative, not just seniority?
> - Are engagement strategies specific enough to act on (cadence, format, content)?
> - Is the map distinguishing stakeholders from customers? Customers belong in the persona play, not here.
> - Have you checked across legal, finance, sales, marketing, operations, and executive functions - not just engineering?

> **Capacity notes**
> - Interest description: aim for one clear sentence per stakeholder (10-15 words)
> - Engagement strategy: one to two sentences per quadrant
> - Name field: 4 words maximum
> - Role / Team field: 6 words maximum
```

###### Usage Guidance

- Build this map before empathy interviews begin.
- Rate influence based on actual power over this initiative, not title alone.
- Keep stakeholders and customers separate. Customers who use the product belong in psk-proto-persona.
- Revisit this map at each major phase boundary (after framing, after discovery, before launch).
- A map with no skeptics or blockers should be treated as incomplete, not as good news.

#### psk-stakeholder-alignment / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For a route-optimization initiative, assess internal stakeholders' interest and influence and choose Manage Closely, Keep Satisfied, Keep Informed, or Monitor accordingly.
- **Weak:** Sending every stakeholder the same weekly update ignores differences in decision involvement.
- **Drift to avoid:** Customers as internal stakeholders: keep discovery subjects distinct from the organizational stakeholder map.


##### Common Pitfalls

- **Listing Only Supporters:** Before closing the map, ask explicitly: who might push back? Who was not consulted on similar initiatives? Add them.

- **Confusing Stakeholders with Customers:** Customers who use the product in the field belong in the persona play (psk-proto-persona), not here. The stakeholder map covers people who affect the initiative organizationally. Keep these lists separate.

- **Equating Influence with Seniority:** Rate influence based on actual power over this specific initiative. Ask: can this person approve, block, accelerate, or veto the work? That is influence. Title alone is not.

- **Treating Interest and Influence as Binary:** Use Medium deliberately. Reserve High for stakeholders with genuine power or deep engagement with this initiative specifically.

- **Building the Map Once and Never Revisiting:** Revisit the map at each major phase boundary. Note what changed and why.

- **Assigning Everyone to "Manage Closely":** Force distribution. Reserve "manage closely" for the two to four stakeholders who genuinely require it. Everyone else gets a lighter strategy.

- **Writing Engagement Strategies as Communication Schedules:** For every "manage closely" and "keep satisfied" stakeholder, specify at least one type of decision they will be consulted on - not just a communication format. Example: "Involve in go/no-go discussion before framing is complete" is an engagement strategy. "Weekly update email" is not.

- **AI Places Stakeholders It Has Never Met:** The PM places each stakeholder from what they have observed. The skill asks for the evidence behind each placement and names roles the PM may have missed.

##### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-stakeholder-alignment) for supporting source material and expanded examples.


### Play 03: Outcome Tree, Section One

Stable identifier: `psk-outcome-tree`.

#### psk-outcome-tree / Instructions

##### Purpose

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

###### Usage Notes

- **Two modalities:** Section One (Template 03, Context phase) establishes the strategic context before discovery. Section Two (Template 23, Define/Deliver phase) updates the tree after discovery with validated outcomes, revised metrics, and actuals vs. planned.
- The template produces a structured artifact with five sections: Business Outcome, Business Success Metrics, Product Outcomes (2-5), Product Success Metrics, and Product Health Metrics.
- Product outcomes use role names, not persona names.
- The play cross-references two other plays: Framing the Problem (Problem Statement box) and Solution Hypothesis Statement (Solution Summary box). Neither is a blocking dependency.
- Upstream: psk-jobs-to-be-done product outcomes feed into this tree. Section Two updates the tree after discovery work.

##### Key Concepts

###### Business Outcomes vs. Product Outcomes

These are two distinct levels. Confusing them is the most common mistake in this play.

**Business Outcome:** What the organization is trying to achieve at a strategic or operational level. It is owned by the business, not by the product team alone.

Example: "Improve new employee onboarding time by 30%"

**Product Outcome:** What the customer or user achieves when the product works well. Product outcomes support the business outcome, but they describe value from the customer's perspective.

Example: "Internal HR managers are focused on strategic initiatives and spend less time doing day-to-day tactical tasks"

The relationship is causal: if the product outcomes are achieved, the business outcome should follow. If that causal link is weak, the tree needs rework.

###### Business Success Metrics

Business success metrics measure progress toward the business outcome. They are often lagging indicators owned by leadership or finance.

These may be defined or TBD at the time of building the tree. It is acceptable to leave them as "TBD" initially, but they should not remain blank permanently.

Examples:
- Time-to-productivity for new hires (days)
- Employee satisfaction score during first 90 days
- HR cost per onboarding cycle

###### Product Success Metrics

Product success metrics measure whether each product outcome is being achieved. They are leading indicators owned by the product team.

Examples:
- Percentage of onboarding tasks completed without HR intervention
- Average HR manager time spent on tactical onboarding tasks per week
- Number of onboarding-related support tickets per month

###### Product Health Metrics

Product health metrics measure the operational health of the product itself, separate from whether it is achieving outcomes.

Examples:
- System uptime percentage
- Average page load time
- Error rate for key workflows
- User adoption rate (active users / total licensed users)

Product health metrics are necessary but not sufficient. A product can be healthy (fast, reliable, available) and still fail to deliver outcomes.

###### The 2-5 Product Outcome Limit

The playbook sets a hard limit: no more than 2-5 product objectives. This is not a suggestion. If you have more than 5, you are either splitting too finely or trying to serve too many business outcomes in one tree.

###### Cross-References to Other Plays

The Outcome Tree references two other playbook artifacts:

- **Problem Statement** (from the Framing the Problem play): feeds into the tree as context for why the business outcome matters
- **Solution Summary** (from the Solution Hypothesis Statement play): feeds into the tree as a summary of the proposed approach

These are cross-references, not blocking dependencies. You can build the Outcome Tree without having completed those plays, but the tree is stronger when they exist.

###### Section One vs. Section Two (Two Modalities, One Skill)

This skill covers both sections of the Outcome Tree as two modalities:

**Section One (Template 03, Context phase):** Build the tree before discovery. Define the business outcome, product outcomes, and metrics framework based on the PM's current understanding of strategy and customer needs.

**Section Two (Deliver phase  -  reuses the Outcome Tree design; the baseline deck labels this occurrence "Template 3 of 24"; the B2B work-in-progress deck numbers it Template 23):** Update the tree after discovery. Revise product outcomes that discovery validated or invalidated. Fill in metrics that were TBD. Add baselines and targets now that real data exists. Record actuals against planned targets. Retire outcomes that turned out to be wrong.

The trigger for Section Two is evidence: completed empathy interviews, validated hypotheses, experiment results, or post-launch measurement data. If the PM has not done discovery work since building Section One, Section Two will just reproduce the same guesses with more confidence. That is not useful.

###### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **critic of the outcome tree the PM drafted**, in both sections. In Section One it checks that the business outcome is measurable, that product outcomes describe what customers achieve, and that metrics are in the right place. In Section Two it asks what discovery evidence supports or contradicts each product outcome. The outcomes, targets, and the verdict on each stay the PM's.

- **Use it when:** the PM has drafted Section One, or has discovery evidence to review in Section Two.
- **Avoid it when:** the request is to invent the business outcome, or to fill in baselines, targets, or actuals without data.
- **Return:** each outcome and metric checked for format and placement, the causal chain from product outcomes to business outcome tested, and in Section Two, each product outcome matched to evidence for the PM to keep, revise, or retire.

###### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

###### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

##### Application

Use [Template](playbook-skills.md#psk-outcome-tree--template) for the full scaffold.


###### Required Output Convention

Default to a **clean, paste-ready structured artifact** with clearly labeled sections.

That means:

- fill all sections (Business Outcome, Business Success Metrics, Product Outcomes, Product Success Metrics, Product Health Metrics)
- produce 2-5 product outcomes that clearly support the business outcome
- keep product outcome statements concise enough for template cells (~15-20 words)
- keep metrics specific and measurable
- explanation belongs below the artifact, not inside the template cells

The artifact comes first. Commentary is secondary.

###### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses Discovery mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

###### Step 1: Confirm the Product and Business Context

Before writing anything, answer:

- what product or service are we talking about?
- what business or organization does this product serve?
- who are the customers/users of this product?

**Guard against tech-role bias.** The product outcomes belong to the customer, the person who uses or buys the product in the field. A clinical data platform's product outcomes belong to clinical operations leads and research scientists, not to data engineers or platform architects. Before writing product outcomes, confirm: does this person write code, design systems, or architect solutions as their primary job? If no, the outcomes should not read like a technologist's goals.

###### Step 2: Gather Evidence Before Writing

Once you know the product and business context, ask the user for relevant materials before drafting:

- **Strategy documents** such as business plans, annual goals, OKR frameworks, or strategic planning decks
- **Existing metrics** such as current KPIs, dashboards, or performance reports
- **Prior discovery work** such as problem statements, persona artifacts, or JTBD artifacts from other skills

This skill uses **artifacts-only** evidence gathering. The business outcomes and product outcomes should come from the PM's own strategic context, not from web research. Do not offer to run web searches for this skill.

###### Step 3: Define the Business Outcome

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

###### Step 4: Define Business Success Metrics

For the business outcome, identify 1-3 metrics that the business would use to measure progress.

These metrics should be:

- measurable (a number, percentage, or rate)
- owned by or visible to business leadership
- connected to the business outcome statement

It is acceptable for these to be "TBD" if the user does not have them yet. Note this in the artifact and flag it as a gap to resolve.

###### Step 5: Define Product Outcomes (2-5)

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

###### Step 6: Define Product Success Metrics

For each product outcome, identify 1-2 metrics that would indicate the outcome is being achieved.

Product success metrics should be:

- leading indicators (they move before the business outcome moves)
- measurable by the product team
- tied to a specific product outcome

If metrics are not yet defined, mark them as "TBD" and note the gap.

###### Step 7: Define Product Health Metrics

Identify 2-4 metrics that measure the operational health of the product itself.

Product health metrics are about the product working correctly, not about outcomes being achieved. They include things like:

- uptime and availability
- performance (load times, response times)
- error rates
- adoption and engagement rates

###### Step 8: Cross-Reference Problem Statement and Solution Summary

If the user has completed the Framing the Problem play (psk-framing-the-problem), pull in the problem statement as context.

If the user has completed the Solution Hypothesis Statement play (psk-solution-hypothesis), pull in the solution summary.

If neither exists yet, note these as optional inputs that strengthen the tree when available.

###### Step 9: Review the Causal Chain

Before finalizing, walk through the logic:

- If Product Outcome 1 is achieved, does it plausibly contribute to the Business Outcome?
- If Product Outcome 2 is achieved, does it plausibly contribute to the Business Outcome?
- Are the product outcomes collectively sufficient to move the business outcome, or are there gaps?
- Are any product outcomes actually business outcomes in disguise?
- Are any product outcomes actually features or solutions?

Flag any weak links for the user to consider.

###### Step 10: Offer Next Steps (Section One)

After the Section One artifact is complete, offer the user up to three next-step options:

1. **Build or refine a problem statement** using psk-framing-the-problem, if no problem statement exists yet
2. **Define a solution hypothesis** using psk-solution-hypothesis, to fill in the Solution Summary box
3. **Run Section Two** of this skill after discovery work to update the tree with evidence

Present these as options, not as mandatory steps. The user decides what comes next.

---

###### Section Two: Updating the Outcome Tree After Discovery

The following steps apply when the PM returns to the Outcome Tree after completing discovery and define work. Section Two is not a new artifact. It is an update pass on the existing Section One artifact.

###### Step 11: Confirm Discovery Evidence Exists

Before running Section Two, verify the PM has new information to work with. Ask:

- What discovery activities have been completed since the tree was built? (empathy interviews, experiments, validation sessions, market research)
- What did discovery reveal that surprised you or contradicted your assumptions?
- Have any product outcomes been validated, invalidated, or changed in priority?

If the PM has no new evidence, Section Two will not add value. Recommend completing discovery work first.

###### Step 12: Review Each Product Outcome Against Evidence

Walk through each product outcome from Section One and ask:

- **Validated:** Did discovery confirm this outcome matters to customers? Keep it, sharpen the language if needed.
- **Invalidated:** Did discovery reveal this outcome is not important to customers, or that the causal link to the business outcome is weaker than assumed? Mark it for retirement or revision.
- **New:** Did discovery reveal a product outcome that was missing from Section One? Add it (staying within the 2-5 limit).
- **Revised:** Does the outcome need reframing based on what customers actually said or did?

Update the Product Outcomes table accordingly. Note what changed and why in the Notes section.

###### Step 13: Update Metrics with Baselines, Targets, and Actuals

For each metric section (business success, product success, product health):

- Replace "TBD" entries with defined metrics where evidence now exists
- Add **baseline** values (what is the current state before the product intervention?)
- Add or refine **target** values (what does success look like, now that you know more?)
- If post-launch: record **actual** values and note variance from target

Use a consistent format: "Metric Name: baseline X, target Y, actual Z (if available)."

###### Step 14: Reassess the Causal Chain

Re-run the causal chain review from Step 9, but with the updated outcomes:

- Do the revised product outcomes still collectively support the business outcome?
- Did discovery reveal gaps in the chain that Section One missed?
- Are the business success metrics still the right ones, or has the business context shifted?

Flag any breaks in the chain for the PM to resolve.

###### Step 15: Offer Next Steps (Section Two)

After the Section Two update is complete, offer the user:

1. **Share the updated tree with stakeholders** to align on revised priorities
2. **Update the roadmap** using psk-outcome-roadmap (if available) to reflect revised outcomes
3. **Schedule the next review cycle** to keep the tree current as the product evolves

#### psk-outcome-tree / Template

###### When to Use This

Use this template during the **Context** phase to connect your product work to a measurable business goal. This is foundational: until you can articulate what the business is trying to achieve and how the product supports that, prioritization and roadmap decisions lack an anchor.

Revisit this artifact regularly. Bring it to team meetings. Use it to share success metrics and check assumptions with the team.

###### Template

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

###### Usage Guidance

###### Filling the Template

1. Start with **Product Context** to anchor who this is for.
2. Add the **Problem Statement** if one exists from previous work.
3. Define the **Business Outcome** first. Everything else flows from it.
4. Add **Business Success Metrics** (even if some are TBD).
5. Define **Product Outcomes** (2-5). These describe what the customer achieves.
6. Add **Product Success Metrics** for each product outcome.
7. Add **Product Health Metrics** for the product itself.
8. Add the **Solution Summary** if one exists.
9. Walk through the **Causal Chain Review** to verify connections.

###### How Many Product Outcomes

The playbook sets a hard limit of 2-5. Default to 2-3 for a focused product. Use 4-5 only when the product serves multiple distinct user roles or the business outcome is broad enough to require multiple paths.

If you find yourself writing more than 5, either:

- consolidate related outcomes into a single, broader outcome
- split into multiple trees, each with a different business outcome

###### What Goes in the Product Outcome Statements

Write each product outcome as a statement about the customer's improved state. Use role names (e.g., "HR managers," "field technicians," "compliance officers"), not individual persona names (e.g., "Maya," "Carlos").

Do not use:

- feature descriptions ("The product provides...")
- implementation details ("Automated workflow for...")
- business metrics ("Revenue increases by...")
- internal team goals ("The engineering team ships...")

###### Connecting to Other Skills

- **Upstream:** psk-framing-the-problem provides the Problem Statement; psk-solution-hypothesis provides the Solution Summary
- **Parallel:** psk-jobs-to-be-done produces product outcomes that may feed into this tree
- **Downstream:** Section Two (this skill, Modality 2) updates the tree after discovery and define work

---

###### Section Two: Updating the Outcome Tree After Discovery

Use this scaffold when returning to the Outcome Tree after completing discovery work. This is not a new artifact. It is an update pass on the Section One artifact above.

###### Prerequisites

Before running Section Two, the PM should have completed at least one of:

- empathy interviews (psk-empathy-interviews)
- solution hypothesis validation (psk-solution-hypothesis)
- lo-fi experimentation (psk-lofi-experimentation)
- market or customer research
- post-launch measurement data

###### Update Scaffold

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

###### When to Run Section Two

Section Two adds value when the PM has new evidence that changes the tree. Common triggers:

- Completed empathy interviews revealed different customer priorities than assumed
- Solution hypothesis testing invalidated an assumed product outcome
- Market research shifted the competitive context
- Post-launch data shows actual vs. planned variance
- Business strategy changed, altering the business outcome or its metrics

Section Two does not add value when:

- The PM has not done discovery work since Section One (the tree will not change)
- The only change is cosmetic rewording (edit the Section One artifact directly)

###### Capacity Reference

See [Template and capacity guidance](playbook-skills.md#psk-outcome-tree--template) for the exact word and character budgets per field.

| Field | Word Budget | Guidance |
|-------|-------------|----------|
| Business Outcome | ~15-25 | Specific, measurable business goal |
| Business Success Metric | ~10-15 | Measurable indicator with units |
| Product Outcome | ~15-20 | Customer-centered value statement |
| Product Success Metric | ~10-15 | Leading indicator tied to an outcome |
| Product Health Metric | ~5-10 | Operational metric with target |

#### psk-outcome-tree / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For irrigation management, connect business results to farm managers reducing avoidable water use, then define success and health measures. Revisit planned outcomes against actual evidence in Section Two.
- **Weak:** A tree with no customer outcomes jumps directly from financial targets to features.
- **Drift to avoid:** Layer confusion: "Ship sensors" is an output; "increase subscription revenue" is a business result. Neither substitutes for customer progress.


##### Common Pitfalls

- **Confusing Product Outcomes with Business Outcomes:** Ask: who experiences this outcome? If the answer is "the business" or "leadership," it is a business outcome. If the answer is "the customer using the product," it is a product outcome. Keep them in their respective boxes.

- **Writing Feature Descriptions as Product Outcomes:** Strip out the product. Ask: what is different for the customer when this feature works? "New employees complete required onboarding steps without waiting for HR availability" is a product outcome. "Self-service onboarding portal" is a feature.

- **Setting More Than 5 Product Objectives:** The playbook limit is 2-5 product outcomes per tree. If you have more, either consolidate related outcomes or split into multiple trees for different business outcomes.

- **Making Business Outcomes Too Vague:** Add a direction, a metric, and a target. "Improve customer satisfaction" becomes "Increase Net Promoter Score from 32 to 50 within 12 months." If the user cannot specify a target, at least specify a direction and a metric.

- **Defaulting to Tech-Role Language in Product Outcomes:** Before writing product outcomes, confirm who the product actually serves. Most products serve people whose primary job is not writing code. An HR platform serves HR managers and employees, not data engineers.

- **Treating This as a One-Time Exercise:** The playbook says to revisit regularly and bring it to team meetings. Schedule periodic reviews and update the tree as strategy evolves.

- **Skipping Product Success Metrics:** Even if exact metrics are not known yet, define the type of measurement. "TBD" is acceptable as a starting point, but flag it as a gap that must be resolved before the next planning cycle.

- **Confusing Product Health Metrics with Product Success Metrics:** Keep them in separate sections. Product health metrics (uptime, latency, error rates) go in the health section. Product success metrics (task completion rates, time savings, adoption of key workflows) go next to their respective outcomes.

- **AI Writes the Tree:** The PM drafts; the skill checks each outcome and metric. Targets and baselines come from the PM's data or are marked to be set.

##### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-outcome-tree) for supporting source material and expanded examples.


### Play 04: Market Selection & Sizing

Stable identifier: `psk-market-selection-sizing`.

#### psk-market-selection-sizing / Instructions

##### Purpose

Create a **Productside-style Market Selection & Sizing artifact** for the market a product serves.

This skill is for the **Context** phase. Before diving into a product opportunity, either an iteration of an existing product or a new one, the team needs to understand what market the product serves, what is happening in that market, and whether it is an interesting one to pursue. The artifact has three parts:

1. **Market Selection** - name the market and run a PESTEL analysis of the forces acting on it
2. **Segment the Market** - cut it into at least two distinct segments, and name the users, buyers, and influencers in each
3. **Size the Market & Segments** - TAM for the market, SAM for each segment, and SOM in annual revenue when there is a product to price

Use this skill when you need to:

- name the market before writing jobs, personas, or problem statements for it
- move segmentation beyond simple industries or demographics
- decide which segments are worth exploring, with a first-pass size behind each
- give later plays (Jobs-to-Be-Done, Personas, Empathy Interviews, Positioning) a defined segment to work from

This is not a financial forecast or a business case. It is a first pass, fast and simple, that the team revisits as it learns more. And it is never a place for numbers without sources.

**Source status:** this Play exists only in the B2B work-in-progress deck (Template 04 of 24), which is not yet ratified. The baseline deck has no equivalent.

###### Usage Notes

- **Type:** component. **Phase:** Context. **Evidence:** web research + user artifacts.
- **Every number needs a source.** Sizing is written as formulas whose inputs carry source IDs or `[TO SOURCE]`, in one counting unit, as ranges, with SOM ≤ SAM ≤ TAM.
- **AI may propose, never invent.** Following the Playbook's own prompts, the skill proposes market definitions, PESTEL entries, and segments with its reasoning visible, and cites what it finds. It never fills a sizing blank with a plausible number.
- **SOM can wait:** it is estimated only when there is a product to price. Otherwise it is deferred until solutions are ideated.
- **Downstream:** psk-jobs-to-be-done, psk-proto-persona, psk-empathy-interviews, and psk-positioning-statement use the segments and the people named in them.
- The source deck is not yet ratified, and its pages are not objectified (no named shapes). The budget entry in `technical/data/canonical_template_budgets.yaml` has guidance only, no shape budgets.

##### Key Concepts

###### Name the Market at the Right Altitude

A market definition centers on **who the product is for and the benefit it provides them**. "Healthcare" is too broad to analyze. One customer's workflow is too narrow to size. Three questions, asked one at a time, get to the right altitude:

1. What problem are people trying to solve, or what are they trying to make better, in this space?
2. Who has this problem (businesses, consumers, channel partners), and when does it become important enough for them to look for help?
3. What do they do today to solve it, and what other options could they choose?

Propose a definition from the answers and have the PM confirm or iterate it. Lock it before running the PESTEL.

###### PESTEL: Evidence, Not a Full Grid

PESTEL names six forces acting on the market: **Political, Economic, Social, Technological, Environmental, Legal.** The goal is evidence, not a filled grid. Each force is committed either as **evidence with a source**, or as an **open question to research**. A PESTEL full of generic forces ("technology is changing fast," "regulation is increasing") fits every market and informs none.

Ask the PM first which forces they know should, or should not, be considered. They know things about this market that no search will find.

###### A Segment Is Defined by Shared Needs, Goals, and Behaviors

A segment is a potential group of customers that is **unique and identifiable through a set of shared traits, goals, preferences, and behaviors.** Industry and company size can bound a segment, but they rarely define one. Two hospitals of the same size can buy for completely different reasons.

Every segment needs:

- a **name** and a brief description of the traits, desires, and preferences that make it unique
- **explicit cut logic**: what makes it distinguishable from the other segments, stated so it can be tested
- the **people operating in it**: users, buyers, and influencers. A segment with no real buyer or user in it is a segment for show.

The template holds two segments, and the Play asks for at least two. A **high-potential segment** has strong underserved needs and problems worth solving to validate.

###### TAM, SAM, SOM: The Productside Way

- **TAM (Total Addressable Market):** think broadly. The whole market the product could serve.
- **SAM (Serviceable Addressable Market):** for **each segment**, the part of the TAM the product can actually serve.
- **SOM (Serviceable Obtainable Market):** for each segment, the share of the SAM the team can realistically win, in **annual revenue**. It must consider **competition**, plus pricing and company constraints.

Name the **counting unit** (sites, firms, accounts, people, checkpoints) and keep it consistent through TAM, SAM, and SOM. Check that SOM ≤ SAM ≤ TAM in the same unit. Revenue is units × an annual price per that same unit.

**SOM can wait.** If there is an existing product, estimate SOM. If not, skip it until solutions have been ideated, or show it as a conditional formula with the price marked as an assumption.

###### Every Number Is a Blank to Source

AI is fast at structure and dangerous at facts. Every figure about size, growth, or competitors that no one can trace to a source is a guess dressed as a finding. So:

- **Write sizing as formulas**, with every input labeled by its source (`[S1]`, `[S2]`) or marked `[TO SOURCE]`.
- **Triangulate.** Use three different approaches (top-down, bottom-up, analogous products, subject-matter experts). Don't rely on a single search or one source.
- **Use ranges.** Ranges reduce overconfidence and turn a debate about one number into a discussion of risk.
- **A market share needs a basis.** "5% in two years" is not a basis. Competitive position, reach, win rate, and capacity are.
- **Never cite competitor revenues** that no filing or report states.

###### "Is It Worth It?" Stays With the PM

The skill can recommend which segments look most promising and say why. The judgment that a market or segment is worth pursuing belongs to the PM and their team.

###### How AI Supports This Play

The Playbook calls AI **fast at structure and dangerous at facts**. It can lay out a PESTEL skeleton, suggest ways to segment a market, and frame a TAM/SAM/SOM calculation. What it cannot do is know the market. Use it to organize the sources the PM has and to expose the gaps still to fill. That turns scattered evidence into a shape the team can reason about.

In this Play, the Playbook's own prompts ask AI to research, propose segments, and recommend two. So this skill does propose, with its reasoning visible and every claim cited. It never supplies a number without a source the PM can check.

- **Use it when:** the market is named (or nearly) and there are real sources, or web research is available, and the PM needs help structuring or sharpening the analysis.
- **Avoid it when:** there are no sources and no way to research, or the request is simply "what's the market size?" Build the structure and mark the numbers `[TO SOURCE]` instead.
- **Return:** a PESTEL with the evidence organized and gaps flagged as questions, segments with explicit cut logic the team can test, and TAM/SAM/SOM as formulas with sourced inputs.

###### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

###### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

##### Application

Use [Template](playbook-skills.md#psk-market-selection-sizing--template) for the scaffold.


###### Required Output Convention

Default to a **one-page market analysis that mirrors the template**:

- **Market Selection:** the market name, and a PESTEL with one short entry per force, each tagged with a source ID or marked as an open question
- **Total Addressable Market:** one or two sized facts, each with a source ID
- **Segments 1 and 2:** name, one- or two-sentence description, and the users, buyers, and influencers operating in it
- **SAM per segment:** the counting logic as a short formula, with units and a range
- **SOM per segment:** the share basis and units × price = annual revenue, as a range, or "deferred until solutions are ideated"
- **Source register** below the artifact: ID, source, date, what it supports
- **Open questions** below the register: the `[TO SOURCE]` blanks and PESTEL questions, ranked by how much they could change the sizing

Use the provenance tags shared across this library wherever content is not the PM's own: `[RESEARCH]` with a source ID for anything found, `[AI-SUGGESTED, VALIDATE THIS]` for forces, segments, or cut logic you proposed. Mark numbers with no source `[TO SOURCE]`, never a guessed value.

Keep entries compact. The template's PESTEL cells, segment descriptions, and sizing boxes are small.

###### If the PM Brings a Draft

When the PM arrives with a market analysis, review it before adding to it:

1. **Altitude.** Is the market named around who the product serves and the benefit, at a level that can be analyzed and sized?
2. **PESTEL.** Flag generic forces and unsourced claims. Ask which are evidence and which are open questions.
3. **Segments.** Is the cut logic explicit and testable? Do the segments differ by needs, goals, and behaviors, or only by industry and size? Does each have real users, buyers, and influencers?
4. **Numbers.** Does every input have a source? Are units consistent, and is SOM ≤ SAM ≤ TAM? Is the market share justified by competition and capacity, or assumed?
5. **Offer fixes last**, as options to accept, adapt, or reject. Return the review as a compact table (element, verdict, why, suggested fix).

###### Step 1: Confirm the Product and Who It Serves

Before anything else, answer:

- What product or product idea is this, existing or new?
- Who is it for, and what benefit does it provide them?
- What decision is this analysis meant to inform?

**Guard against tech-role bias.** Models default to picturing software buyers and developer users. A market is defined by the people with the problem. A pump-station monitoring product's market is water utilities and the operators and directors who run them, not "IoT platforms." The users, buyers, and influencers named in each segment should be the real roles in that market (operators, technicians, directors, council members, regulators), not technologists, unless the product truly serves technologists.

###### Step 2: Gather Evidence Before Drafting

This skill uses **web research and user-supplied artifacts.** Offer both before drafting:

1. **Web research.** Offer to search for the market. Prefer primary sources: government statistics and registries, regulator data, trade-association reports, company filings, and practitioner forums. Cite each source with a link and date. Analyst summaries and vendor marketing are weak sources for sizing.
2. **User-supplied artifacts.** Ask for what the PM already holds: market reports, pricing, competitor information, company constraints, customer lists, or prior strategy work.

If no sources exist yet and web research is unavailable, say so. The Playbook advises against AI sizing without sources. Build the structure, mark every number `[TO SOURCE]`, and give a short research plan. Do not fill the gap with plausible numbers.

###### Step 3: Pressure-Test the Market Definition

Ask the three altitude questions one at a time (see [Name the Market at the Right Altitude](#name-the-market-at-the-right-altitude)). Then propose a market definition and ask the PM to confirm or iterate. Lock it before moving on.

###### Step 4: Build the PESTEL

1. Ask the PM which forces they know should, or should not, be considered.
2. Research each of the six forces.
3. Commit each as evidence with a source ID, or as an open question to research. Label assumptions and uncertainties, and suggest where reliable information could be found.

One short entry per force. If a force has nothing specific to this market, say so rather than filling the cell with a generic trend.

###### Step 5: Segment the Market

1. Propose 4-6 candidate segments defined by needs, goals, and behaviors. For each, state the cut logic and name 2-3 real buyer and user roles who operate in it. Tag them `[AI-SUGGESTED, VALIDATE THIS]` unless they came from the PM or a source.
2. Recommend two high-potential segments (strong underserved needs, problems worth solving to validate) and justify each with evidence.
3. Invite the PM to challenge the cuts and add their own knowledge. The PM chooses the segments that go in the template, at least two.
4. For each chosen segment, list the users, buyers, and influencers. Think broadly.

###### Step 6: Size the Market and Segments

1. **Name the counting unit** for this market and keep it throughout.
2. **TAM.** Size the broad market from the best available sources. Show the arithmetic.
3. **SAM per segment.** Show the counting logic as a formula (for example, number of sites × average units per site), with each input sourced or `[TO SOURCE]`.
4. **Triangulate.** Name three sizing approaches (top-down, bottom-up, analogous products, subject-matter experts) and the research each needs. Note where they agree and disagree.
5. **Express ranges**, not point estimates.
6. **SOM per segment, if there is a product.** State the share basis (competitive alternatives, reach, win rate, capacity, time horizon), then units × annual price = annual revenue, as a range. Mark an assumed price as a pricing assumption, not evidence. If there is no product yet, write "deferred until solutions are ideated."

###### Step 7: Check the Numbers

Before presenting:

- every input has a source ID or is marked `[TO SOURCE]`
- units are consistent across TAM, SAM, and SOM
- SOM ≤ SAM ≤ TAM
- no market share without a stated basis
- no competitor revenue or customer count without a source that states it
- ranges, not single numbers

###### Step 8: Hand the Call to the PM

Present the artifact with the open questions ranked by how much they could change the sizing. Recommend the segment the evidence favors if asked, and say why. Do not declare the market worth pursuing. That call stays with the PM.

###### Step 9: Offer Next Steps

Offer, as options:

1. **Write jobs for the people in the chosen segments** (psk-jobs-to-be-done). The segments and the people named in them are its input.
2. **Build a proto-persona** for the primary user in the most promising segment (psk-proto-persona).
3. **Close the biggest `[TO SOURCE]` gaps** before taking the sizing to leadership.

The user decides what comes next. Revisit this artifact as discovery produces evidence.

#### psk-market-selection-sizing / Template

###### When to Use This

Use this template in the **Context** phase, before Jobs-to-Be-Done and Personas, to name the market a product serves, understand the forces acting on it, cut it into segments, and size the opportunity. It is a first pass you will revisit as you learn more.

Downstream: the segments and the people named in them feed psk-jobs-to-be-done, psk-proto-persona, psk-empathy-interviews, and psk-positioning-statement.

###### Template

```markdown
# Market Selection & Sizing

## Context
- Product or product idea (existing / new):
- Who it is for, and the benefit it provides:
- Decision this analysis informs:
- Counting unit (sites, firms, accounts, people, ...):

## 1. Market Selection
- Market:

### PESTEL
| Force | Entry | Source or status |
|---|---|---|
| Political | | [S#] / OPEN QUESTION |
| Economic | | |
| Social | | |
| Technological | | |
| Environmental | | |
| Legal | | |

> Quality check: Is the market named around who the product is for and the benefit, at a level you can analyze and size?
> Quality check: Is every entry specific to this market? A force that fits any market is generic. Replace it, or mark it OPEN QUESTION.
> Capacity check: One short line per force.

## Total Addressable Market (TAM)
- Sized fact 1: [S#]
- Sized fact 2: [S#]
- TAM (range, in the counting unit):

## 2. Segments

### Segment 1:
- Description (traits, goals, preferences, behaviors that make it unique):
- Cut logic (what distinguishes it from Segment 2, stated so it can be tested):
- Users:
- Buyers:
- Influencers:

### Segment 2:
- Description:
- Cut logic:
- Users:
- Buyers:
- Influencers:

> Quality check: Do the segments differ by needs, goals, and behaviors, not just by industry or size?
> Quality check: Does every segment have a real user and buyer in it?
> Provenance check: Tag suggested segments and cut logic `[AI-SUGGESTED, VALIDATE THIS]` until the team or a source confirms them.

## 3. Size the Market & Segments

### Serviceable Addressable Market (SAM)
| Segment | Counting logic (formula) | Inputs and sources | SAM (range) |
|---|---|---|---|
| 1 | | | |
| 2 | | | |

### Serviceable Obtainable Market (SOM), annual revenue
| Segment | Share basis (competition, reach, win rate, capacity, horizon) | Units x annual price | SOM (range) |
|---|---|---|---|
| 1 | | | |
| 2 | | | |

> Quality check: Does every input have a source ID or `[TO SOURCE]`? No guessed values.
> Quality check: Same counting unit throughout? Is SOM <= SAM <= TAM?
> Quality check: Is every market share justified by competition and capacity, not assumed?
> Quality check: Ranges, not single numbers? Triangulated from more than one approach?
> SOM rule: With no product yet, write "deferred until solutions are ideated," or show a conditional formula with the price marked as an assumption.

## Source Register
| ID | Source (title, publisher, link) | Date | What it supports |
|---|---|---|---|
| S1 | | | |

## Open Questions
Ranked by how much the answer could change the sizing.
1.
2.
3.
```

###### Usage Guidance

- Work the three parts in order: market, then segments, then size.
- Keep entries compact. The canonical template's PESTEL cells, segment boxes, and sizing boxes are small.
- Every number needs a source the PM can check. A number without one is `[TO SOURCE]`.
- The "is it worth it" judgment stays with the PM and their team.
- Revisit this artifact as discovery produces evidence.

#### psk-market-selection-sizing / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For pump-station monitoring, name utilities and their operators, count stations consistently, and source every population and price input. Leave unknown inputs open.
- **Weak:** "Every utility is our market" leaves segment needs and purchasing conditions undefined.
- **Drift to avoid:** The free five percent: SOM is not an arbitrary percentage of a larger market. Show reachable accounts, capacity, adoption assumptions, and evidence.


##### Common Pitfalls

- **AI Invents the Market Size:** Every number carries a source ID or `[TO SOURCE]`. Never fill a blank with a plausible figure.

- **Competitor Numbers No One Can Know:** Use only competitive facts a filing, a report, or a named source states. Otherwise describe the competitor qualitatively and mark the gap.

- **A Generic PESTEL:** One specific entry per force, tied to this market, with a source, or an honest open question.

- **Segments for Show:** Define segments by shared needs, goals, and behaviors, and state the cut logic so it can be tested. Use size or industry only as a boundary.

- **Segments With No People in Them:** Name the users, buyers, and influencers in every segment. Think broadly.

- **The Market at the Wrong Altitude:** Run the three altitude questions. Center the definition on who the product is for and the benefit it provides.

- **The Free Five Percent:** State the share basis: the alternatives customers use, how many the team can reach, a win-rate assumption, and delivery capacity over a named horizon. If there is no basis yet, show SOM as a conditional formula and say what would anchor it.

- **Mixed Counting Units:** Name one counting unit, convert explicitly when needed, and check SOM ≤ SAM ≤ TAM.

- **One Source, One Number:** Triangulate with three approaches and present ranges.

- **Professional-Looking Logic, Never Tested:** Tag AI-suggested cut logic for validation, rank the open questions, and revisit the analysis as discovery produces evidence.

##### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-market-selection-sizing) for supporting source material and expanded examples.


## Discover + Investigate


### Play 05: Jobs-to-Be-Done & Outcomes

Stable identifier: `psk-jobs-to-be-done`.

#### psk-jobs-to-be-done / Instructions

##### Purpose

Create a **Productside-style Jobs-to-Be-Done & Outcomes artifact** for your target market segment.

This skill has **two steps** that can happen together or at different times:

**Step One (Discover + Investigate, pre-discovery):** Enumerate job statements and personas. Capture what the customer is trying to get done across functional, emotional, and social dimensions. Name the personas who have each job. This step produces the Job Statements & Personas table.

**Step Two (often after empathy interviews):** Fill in product outcomes for each job using the Direction + Metric + Context format. This step is stronger when informed by discovery evidence - empathy interviews, field observations, or customer data that validates or corrects the PM's assumptions about what customers actually want to achieve.

The two steps can be run in one session if the PM already has strong evidence. More often, Step One is done first to frame the discovery questions, and Step Two is completed after empathy interviews reveal what outcomes customers actually care about.

The playbook says to consider Jobs-to-Be-Done and Persona at the same time. If you have not built a proto-persona yet, consider doing that first or alongside this skill.

Use this skill when you need to:

- orient the team around customer needs instead of solutions (Step One)
- capture functional, emotional, and social jobs in one place (Step One)
- define product outcomes that are measurable and customer-centered (Step Two)
- build the foundation for problem identification, opportunity framing, and prioritization (both steps)

This is not a solution specification. Until you know what the customer is trying to accomplish, you are not ready to define what to build.

###### Usage Notes

- **Two steps:** Step One (job statements + personas) can be done pre-discovery. Step Two (product outcomes) is strongest after empathy interviews provide evidence. Both steps can be completed in one session if evidence exists.
- **Review path:** if the PM brings a draft, the skill pressure-tests it first (verdict per job and outcome) before offering rewrites. This matches the Playbook's AI prompts.
- The template produces two artifacts: a Job Statement + Persona table and a Product Outcome & Context table.
- Job statements use three Productside formats: Functional, Emotional, Social.
- Product outcomes use the Direction + Metric + Context format. "Optimize," "enhance," and "improve" are never a direction.
- Upstream (B2B work-in-progress deck): Market Selection & Sizing defines the segment these jobs belong to.
- Downstream: psk-problem-identification uses jobs and outcomes from this skill as input. Product outcomes feed into psk-outcome-tree.

##### Key Concepts

###### Three Types of Jobs

Productside distinguishes three types of customer jobs. Most teams only think about functional jobs and miss the emotional and social dimensions that drive adoption, satisfaction, and switching behavior.

**Functional:** What the customer is trying to get done in practical terms.
Format: `[Action verb] + [object of the action]`

Examples:
- "Onboard new employees"
- "Reconcile inventory across three warehouses"
- "Track patient medication adherence"

**Emotional:** How the customer wants to feel while doing the job.
Format: `Feel [Emotion] when [Circumstance]`

Examples:
- "Feel confident when presenting compliance data to auditors"
- "Feel satisfied that my work is helping others"
- "Feel in control when managing multiple site schedules"

**Social:** How the customer wants to be perceived by others.
Format: `Seen as [Social Perception] to [whom]`

Examples:
- "Be seen as responsible and trustworthy by employees and leadership"
- "Be seen as the go-to expert on regional logistics"
- "Be seen as ready for the Director role"

A complete JTBD artifact must include all three types. Functional jobs alone produce a flat, utilitarian view of the customer that misses the human motivations behind adoption and loyalty.

###### Product Outcomes Use a Specific Format

Product outcomes express what the customer wants to achieve. They are not internal business metrics and they are not feature requests.

Format: `Direction + Metric + Context/Circumstance`

The metric names what is being measured. **Default to including a quantified target**  -  a percentage, ratio, range, or exact number. When in doubt, put something in. The PM can refine it; a vague direction cannot be refined.

Preference order for the quantified value: **percentage > ratio > range > exact number**. For time-based outcomes, use a range ("by Q3", "by H2", "by EOY") rather than an exact date  -  specific dates stale out quickly.

Examples:
- "Reduce payroll data entry errors by 30% during quarterly onboarding cycles" (percentage)
- "Reduce HR query response time from 2-day to same-day for tier-1 requests" (ratio)
- "Add 3 new regional customers through HR partner channel by Q4" (exact number + range)
- "Increase HR self-service revenue to $1.2M by H2" (dollar figure + range)

Every outcome must have a direction. Direction + named metric ("Reduce time to complete payroll data entry") is the minimum viable form  -  acceptable when the PM has no basis for a threshold yet, but always the starting point to improve from. Add the quantified threshold ("by 30%", "from 2-day to same-day") when any evidence supports it.

Avoid: "improve efficiency," "faster onboarding," "better HR tools"  -  these are not metrics, just sentiment. **"Optimize," "enhance," and "improve" are never a direction.** They don't say which way the metric moves. Use increase/decrease, faster/slower, expand/contract, reduce, or eliminate.

Metrics can be quantitative (time, cost, quantity) or qualitative (confidence, trust, satisfaction). Qualitative metrics are especially useful for emotional and social jobs: "Increase confidence in incident-handling procedures" is a real outcome. When a qualitative metric can be measured, name how (for example, "trust scores on passenger security surveys").

The context is the result or impact the persona is seeking, expressed through their workflow and constraints. It is tied to whether they are satisfied or dissatisfied with reaching a goal. **The context never references a potential solution.**

Each job can have multiple outcomes. The outcomes should be specific enough to measure and customer-centered enough to guide prioritization.

###### What Makes a Good Product Outcome

The Playbook gives three tests:

- **Stable over time.** It doesn't change when technology changes. "Decrease the time to diagnose engine failure" holds whether the diagnosis is manual or AI-driven.
- **Linked to satisfaction.** It reflects what makes the customer satisfied or dissatisfied when trying to reach a goal.
- **Reveals unmet or overserved needs.** It shows where customers struggle, or where they have more capability than they need.

###### Jobs, Outcomes, and Pains Are Linked

The playbook states this directly: *"Customers experience Pains when they are unable to achieve the desired Outcomes when executing a Job."*

This is load-bearing for the next play. Pains do not float free  -  they arise when a Job is hard to execute and the desired Outcome is out of reach. Writing precise, measurable Outcomes in this play is what makes Problem Identification tractable: the PM already knows what "success" looks like for each Job, so the Pains become specific gaps between where the customer is and where they want to be.

###### Jobs, Outcomes, and Solutions Are Not the Same

- **Job** = what the customer is trying to accomplish
- **Outcome** = the result the customer wants when the job goes well
- **Solution** = what you build to help them (not part of this skill)

If a job statement mentions your product, a feature, or a tool, it is a solution masquerading as a job. Strip it back to the underlying customer progress.

Jobs define the scope of the work. Outcomes define the success criteria within that scope. The most common mistake is writing an outcome and labeling it a job, which mixes up what the customer is trying to accomplish with how they measure success. That undermines opportunity analysis and pulls the team toward feature-driven thinking.

**Jobs are intentionally stable.** Products, tools, and workflows change. Jobs persist. A job anchored to today's implementation ("export the weekly report from the legacy system") will expire with that system. A job anchored to progress ("share weekly checkpoint performance with leadership") will not.

###### Product Outcomes vs. Business Outcomes

This play captures **product outcomes** - things the customer wants to achieve. Business outcomes (revenue, retention, market share) belong in the Outcome Tree (Template 03), not here.

The playbook explicitly says: "Remember product outcomes are the things your customer wants to achieve."

###### Two Steps, One Artifact

The JTBD artifact has two halves: job statements (Table 1) and product outcomes (Table 2). These can be filled at the same time or at different times.

**Why separate them:** Job statements describe what the customer is trying to do. They can be drafted from the PM's current understanding, existing research, or market knowledge. Product outcomes describe the measurable results customers want. These are harder to get right without evidence.

The common pattern is:

1. **Step One:** Draft job statements and personas based on what the PM knows now. Use this to design empathy interview questions.
2. **Run empathy interviews** (psk-empathy-interviews) to validate and enrich understanding.
3. **Step Two:** Return to the JTBD artifact and fill in product outcomes informed by what customers actually said.

If the PM already has strong discovery evidence, both steps can be completed in one session. The skill supports either workflow.

###### Pair with Persona Work

The JTBD template has a Persona column next to every job statement. That column forces you to name *who* has this job - not a generic segment, but a recognizable role.

If you have already built a proto-persona, use that persona name. If not, use a concrete role title that reflects the actual customer (not the PM building the product).

###### How AI Supports This Play

The Playbook casts AI as a **sharp second reader** for jobs and outcomes. It checks each entry against the format, flags a job that is really an outcome or a solution, and pushes for the emotional and social jobs the PM skipped.

What AI cannot do is say what customers are trying to accomplish. Jobs come from real people in a real context. Any job or persona this skill drafts is a hypothesis to validate through Voice-of-the-Customer, never a finding.

- **Use it when:** the target segment is named and the PM has drafted jobs and outcomes, or wants a labeled starting draft to take into discovery.
- **Avoid it when:** the segment is vague or unnamed. Resolve the segment first (Step 1). Without it, any jobs produced are generic and validate nothing.
- **When reviewing a draft, return:** a verdict on each job (clean, or contaminated with an outcome or a solution), the missing emotional and social jobs *named* rather than written, and each outcome checked for direction, metric, and context. See [If the PM Brings a Draft](#if-the-pm-brings-a-draft).

###### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

###### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

##### Application

Use [Template](playbook-skills.md#psk-jobs-to-be-done--template) for the full scaffold.


###### Required Output Convention

Default to a **clean, paste-ready two-table artifact**.

That means:

- fill both tables (Job Statement + Persona on the left, Product Outcome & Context on the right)
- produce exactly 10 job rows covering all three job types unless the user asks for a different count
- produce at least 10 product outcomes (one or more per job)
- keep job statements short enough for the template table cells (~8-10 words)
- keep product outcomes short enough for the template table cells (~12-14 words)
- explanation belongs below the artifact, not inside the table cells

The artifact comes first. Commentary is secondary.

###### If the PM Brings a Draft

When the user arrives with drafted job statements or outcomes, review the draft instead of drafting from scratch. This is the path the Playbook's AI prompts take (the critique guidance in this Play, the critique guidance in this Play).

1. **Confirm the segment.** If it is unnamed or vague, resolve it first (Step 1). Do not review jobs for a segment no one can name.
2. **Review each job.** Give a verdict per row: clean, wrong format, contaminated with an outcome, or contaminated with a solution. Quote the words that cause the problem.
3. **Name the gaps.** Name the missing job types (usually emotional and social) and the personas with no rows. Do not write them unless the user asks.
4. **Review each outcome.** Check direction (never optimize, enhance, or improve), metric (quantitative or qualitative), and context (no solution). Apply the three good-outcome tests.
5. **Offer rewrites last.** Propose fixes as options to accept, adapt, or reject, then fill the template with what the user commits.

Return the review as a compact table (entry, verdict, why, suggested fix) before any rewritten artifact.

###### Step 1: Confirm the Product and Target Market Segment

Before writing anything, answer:

- what product or service are we talking about?
- who is the target market segment?
- who are the personas within that segment? (user, buyer, influencer)

If you cannot answer those clearly, stop and resolve the target first.

**Guard against tech-role bias.** The jobs belong to the customer - the person who uses or buys the product in the field. An IoT platform's customer jobs belong to a fleet manager or logistics director, not a solutions architect. A clinical data platform's customer jobs belong to a clinical operations lead, not a data engineer. Before writing job statements, confirm: does this person write code, design systems, or architect solutions as their primary job? If no, the jobs should not read like a technologist's workday.

###### Step 2: Gather Evidence Before Writing

Once you know the target segment and role, offer the user two things before drafting:

1. **Web research** - offer to run a quick search for the target role in the target industry. Look for how practitioners describe their own work, frustrations, and goals. Job postings, industry forums, trade press, and professional community discussions are good sources. The goal is to capture real customer language, not marketing language about them.

2. **User-supplied artifacts** - ask whether the user has materials to share: interview notes, support tickets, call logs, existing persona or discovery work, competitive intel, or anything else that would ground the jobs and outcomes in evidence.

Either, both, or neither is fine - the user decides. But always offer before drafting.

###### Step 3: Identify the Personas Involved

Before writing job statements, name the personas who will appear in the Persona column.

For most products, there are 2-4 distinct personas involved:

- the primary user (the person who does the job day-to-day)
- the buyer (the person who approves or funds the product)
- influencers or secondary users

Each job row names the persona who has that specific job. Different personas can appear in different rows. Use concrete role titles, not generic labels.

If a proto-persona already exists from the psk-proto-persona skill, reuse that persona name.

**Distribute rows across roles.** Do not repeat the same persona in every row. The point of the Persona column is to show that different people have different jobs. If the product serves a Regional Operations Planner, a Dock Supervisor, and a VP of Distribution, all three should appear in the table - not just the primary user 10 times.

###### Step 4: Write Functional Job Statements

Functional jobs are the practical things the customer is trying to get done.

Format: `[Action verb] + [object of the action]`

Keep them:

- short (8-10 words fits the template cell)
- action-oriented (start with a verb)
- customer-centered (not your product's feature list)
- concrete (not "improve workflow" or "be more efficient")

Weak: "Manage data"
Stronger: "Reconcile shift schedules across three warehouse sites"

Produce at least 5-6 functional jobs.

###### Step 5: Write Emotional Job Statements

Emotional jobs capture how the customer wants to feel.

Format: `Feel [Emotion] when [Circumstance]`

These are not filler. Emotional jobs explain:

- why customers resist or adopt new tools
- what "good enough" means to them
- what turns a satisfied user into an advocate

Weak: "Feel happy using the product"
Stronger: "Feel confident when presenting compliance data to auditors"

Produce at least 2 emotional jobs.

###### Step 6: Write Social Job Statements

Social jobs capture how the customer wants to be perceived.

Format: `Seen as [Social Perception] to [whom]`

Social jobs reveal:

- career motivations that shape product requirements
- organizational pressures that affect adoption
- peer dynamics that drive or block behavior change

Weak: "Be seen as competent"
Stronger: "Be seen as the team's go-to expert on regional logistics by warehouse managers"

Produce at least 2 social jobs.

---

###### Step One / Step Two Boundary

Steps 1-6 above complete **Step One** of this skill: job statements and personas. At this point, the PM has a choice:

1. **Continue to Step Two now** if they already have enough evidence to write product outcomes confidently (prior research, customer data, domain expertise).
2. **Pause and run empathy interviews first** (psk-empathy-interviews) to validate the jobs and gather evidence about what outcomes customers actually care about. Then return to Step Two.

If the PM chooses to pause, offer to help design empathy interview questions based on the job statements just captured. The jobs from Step One make excellent interview prompts.

---

###### Step 7: Identify Product Outcomes for Each Job (Step Two)

For each job, express the product outcomes the customer wants to achieve.

Format: `Direction + Metric + Context/Circumstance`

- **Direction**: Increase, Decrease, Expand, Contract, Reduce, Eliminate  -  always required, never optional
- **Metric**: what is being measured (time, errors, satisfaction, revenue, customer count)  -  default to including a quantified target: percentage, ratio, range, or exact number ($3.5M, 3 new regional customers). Use a time range ("by Q3", "by H2") rather than an exact date. When in doubt, put a number in  -  the PM can refine it.
- **Context**: the specific circumstance that bounds the outcome

Each job can have one or more outcomes. Produce at least 10 outcomes total across all jobs.

If the PM completed empathy interviews between Step One and Step Two, ask what they learned before drafting outcomes. Customer language from interviews should inform the outcome statements directly.

Weak: "Better efficiency"
Stronger: "Reduce time spent reconciling shift schedules across sites" or "Reduce shift reconciliation time by 40% during weekly planning cycles"

Do not write outcomes that are feature requests ("have a dashboard that shows X") or internal business metrics ("increase revenue by 5%"). Product outcomes describe the customer's desired state.

###### Step 8: Separate Outcomes from Solutions

Before finalizing, scan every outcome and ask: is this something the *customer* wants to achieve, or is it something *we* want to build?

Solution indicators to strip out:

- mentions of your product name
- feature descriptions ("a dashboard that...", "an integration with...")
- implementation details ("automated alerts for...", "API-driven...")

Rewrite any solution-contaminated outcomes as customer-centered results.

###### Step 9: Keep the Artifact Compact

The canonical template uses table cells. Job statements should be ~8-10 words. Product outcomes should be ~12-14 words. Persona entries should be 2-3 words (a role title).

If the output requires summarizing before it can be pasted into the playbook, it is too long.

Do not let good prose outrank usable template completion.

###### Step 10: Add Optional Trailing Notes

If helpful, add a brief trailing section such as:

- `Jobs that need more evidence`
- `Outcomes that feel assumed`
- `Gaps in job type coverage`

Keep it separate from the paste-ready artifact.

Do not add a notes section at all unless:

- the user asks for it, or
- the artifact is already fully complete

###### Step 11: Offer Next Steps

After the current step is complete, offer context-appropriate options:

**If Step One is complete but Step Two is not yet done:**

1. **Run empathy interviews** (psk-empathy-interviews) - use the job statements to design interview questions that test whether these are real customer needs. Return to Step Two afterward.
2. **Build or refine a proto-persona** (psk-proto-persona) - if no persona exists yet, or if the JTBD work revealed a persona gap.
3. **Continue to Step Two now** - if the PM already has enough evidence to write product outcomes.

**If both steps are complete:**

1. **Move to Problem Identification** (psk-problem-identification) - synthesize the jobs, pains, and outcomes into candidate problem statements.
2. **Feed product outcomes into the Outcome Tree** (psk-outcome-tree) - the product outcomes from this skill can inform the Outcome Tree's product outcome section.
3. **Build or refine a proto-persona** (psk-proto-persona) - if persona work has not been done yet.

Present these as options, not as mandatory steps. The user decides what comes next.

#### psk-jobs-to-be-done / Template

###### When to Use This

Use this template during **Discover + Investigate** to capture what your target customers are trying to accomplish and what success looks like for them. Pair this with persona work - the playbook says to consider Jobs-to-Be-Done and Persona at the same time.

This template supports **two steps** that can be completed together or at different times:

- **Step One:** Fill the Job Statements & Personas table (Section 1). This can be done pre-discovery.
- **Step Two:** Fill the Product Outcomes table (Section 2). This is often done after empathy interviews provide evidence about what outcomes customers actually care about.

###### Template

```markdown
# Jobs-to-Be-Done & Outcomes

## Product Context

- Product or service:
- Target market segment:
- Primary user persona:
- Buyer persona (if different):

## 1. Job Statements & Personas

Write job statements using the Productside formats:
- **Functional:** [Action verb] + [object of the action]
- **Emotional:** Feel [Emotion] when [Circumstance]
- **Social:** Seen as [Social Perception] to [whom]

| # | Type | Job Statement | Persona |
|---|------|---------------|---------|
| 1 | F | | |
| 2 | F | | |
| 3 | F | | |
| 4 | F | | |
| 5 | F | | |
| 6 | F | | |
| 7 | E | | |
| 8 | E | | |
| 9 | S | | |
| 10 | S | | |

> Quality check: Does every job describe customer progress, not a product feature or internal team task?
> Quality check: Are all three job types represented (Functional, Emotional, Social)?
> Quality check: Would the named persona recognize this as something they are actually trying to do?
> Quality check: Are rows distributed across multiple personas, not one repeated role?
> Capacity check: Job statements should be ~8-10 words. Persona entries should be 2-3 words (a role title).

## 2. Product Outcomes

For each job, express the desired product outcomes using:
**Direction + Metric + Context/Circumstance**

| # | Product Outcome & Context | Related Job(s) |
|---|--------------------------|-----------------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |
| 6 | | |
| 7 | | |
| 8 | | |
| 9 | | |
| 10 | | |

> Quality check: Does every outcome start with a direction word (reduce, increase, minimize, improve, eliminate)?
> Quality check: Is every outcome measurable - could you tell if it happened?
> Quality check: Are these things the *customer* wants to achieve, not internal business metrics?
> Quality check: Have you avoided feature requests disguised as outcomes ("have a dashboard that...")?
> Capacity check: Product outcomes should be ~12-14 words per row.

## Evidence Notes (optional)

- What is well-supported by evidence:
- What is still assumption:
- Recommended next validation steps:
```

###### Usage Guidance

###### Filling the Template

**Step One (can be done pre-discovery):**

1. Start with **Product Context** to anchor who this is for.
2. Fill **Job Statements** starting with functional jobs, then adding emotional and social jobs. Use the Productside sentence formats - do not improvise different structures.

**Step Two (strongest after empathy interviews):**

3. Fill **Product Outcomes** for each job. One job can have multiple outcomes. Use Direction + Metric + Context. If you completed empathy interviews between steps, let customer language inform the outcome statements.
4. The **Evidence Notes** section is optional and trailing. Do not let it displace or delay the main artifact.

###### How Many Rows

The canonical template has 12 rows. Default to 10 filled rows:

- at least 5-6 functional jobs
- at least 2 emotional jobs
- at least 2 social jobs
- at least 10 product outcomes (one or more per job)
- distribute rows across multiple personas, not one repeated role

Add more rows if the evidence supports them. Do not pad with vague jobs to fill the template.

###### What Goes in the Persona Column

Use a concrete role title that reflects the actual customer - the person who has this job in the field. If you built a proto-persona already, reuse that persona name.

Do not use:
- "User" (too vague)
- "Stakeholder" (too abstract)
- The Product Manager's own title (unless the product truly serves PMs)

###### Connecting to Other Skills

- **Upstream:** Proto-persona (the persona names in this template should match)
- **Downstream:** Problem Identification uses the jobs, pains, and outcomes from this artifact
- **Parallel:** The Outcome Tree (Template 03) uses product outcomes from this skill as input

###### Capacity Reference

See [Template and capacity guidance](playbook-skills.md#psk-jobs-to-be-done--template) for the exact word and character budgets per field.

| Field | Word Budget | Guidance |
|-------|-------------|----------|
| Job Statement | ~8-10 | Compact action phrase; use Productside format |
| Persona | ~2-3 | Role title only |
| Product Outcome | ~12-14 | Direction + Metric + Context; one sentence max |

#### psk-jobs-to-be-done / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** Warehouse planner: Functional, "Coordinate daily labor assignments"; Emotional, "Feel confident when reallocating crews"; Social, "Seen as dependable by site supervisors." Outcome: "Reduce reassignment delays during shift changes."
- **Weak:** "Improve efficiency" has no named metric or clear direction.
- **Drift to avoid:** Jobs as solutions: "Use the scheduling dashboard" describes a product interaction. State what the planner is trying to accomplish.


##### Common Pitfalls

- **Writing Only Functional Jobs:** After writing functional jobs, explicitly ask: how does this person want to feel while doing this work? How do they want to be seen by their peers and leadership? Write at least 1-2 emotional and 1-2 social jobs.

- **Confusing Jobs with Solutions:** Strip out any mention of products, features, tools, or implementation. Rewrite as the underlying customer progress: "Track regional performance against quarterly targets."

- **Making Outcomes Vague:** Use the Direction + Metric + Context format, and never use "optimize," "enhance," or "improve" as the direction. "Improve efficiency" becomes "Reduce time spent reconciling data across multiple HR systems." Adding a specific threshold ("by 40% during month-end close") makes it stronger when you have the evidence  -  but even without a number, a named metric beats a vague direction.

- **Defaulting to a Tech Role:** Ask what the customer actually does day-to-day. Most products serve people whose primary job is not writing code. A fleet manager's jobs involve route optimization, driver coordination, and compliance reporting - not API integration or system architecture.

- **Writing Internal Team Tasks as Customer Jobs:** Ask: who experiences the product's value in the field? That person's jobs go in the template. The PM's jobs belong in process docs, not in customer discovery artifacts.

- **Restating Jobs as Outcomes:** Outcomes should describe a measurable result: "Reduce time to complete payroll data entry." "Reduce errors in new employee form submissions." Where the PM has evidence for a specific threshold, adding it strengthens the outcome  -  but a named metric without a number beats a vague direction every time. The outcome is what success looks like *for the customer* when the job goes well.

- **Exceeding Template Capacity:** Job statements: ~8-10 words. Outcomes: ~12-14 words. Persona entries: 2-3 words. Write for the template cell, not for the model's appetite for prose.

- **Underfilling the Template:** Default to 10 job rows covering all three types (Functional, Emotional, Social) with at least 10 outcomes. Distribute rows across multiple personas - do not repeat one role in every row.

- **Presenting AI-Drafted Jobs as Findings:** Label every drafted job and outcome as a hypothesis, and end with Assumptions to Validate. Route the hypotheses into empathy interviews (psk-empathy-interviews) before treating any of them as evidence.

##### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-jobs-to-be-done) for supporting source material and expanded examples.


### Play 06: Personas & Proto-Personas

Stable identifier: `psk-proto-persona`.

#### psk-proto-persona / Instructions

##### Purpose

Create a **Productside-style proto-persona** for the person your product is serving.

This skill is for the **Discover + Investigate** phase, when you need a usable customer profile before you have enough research to call it validated. It helps a Product Manager capture the person behind the segment in a way that is specific enough to guide discovery and prioritization, while staying honest about what is still assumption.

Start with the **primary user persona**. Only after that is coherent should you build the **buyer persona**.

Use this skill when you need to:

- make the target customer feel real to the team
- capture needs, pains, goals, and attitudes in one place
- keep the team from designing for an abstract segment
- identify what still needs customer validation

This is not a validated persona. Until it is grounded in research, it is explicitly a **proto-persona**.

###### Usage Notes

- It starts with the **user persona** first, then optionally the buyer and influencer
- It keeps the profile explicitly **proto** until validated by research
- **Provenance tags:** every line of a working draft is tagged `[FROM YOU]`, `[RESEARCH]`, or `[AI-SUGGESTED, VALIDATE THIS]`. Invented quotes are always AI-suggested. The committed copy moves the tags out of the fields and keeps a ranked Riskiest Assumptions list.
- **Two draft paths:** beliefs or notes get drafted field by field with tags; a finished research-based persona gets reviewed against Clarity, Story, Empathy, Relevance, and Focus, and nothing is added that the research did not produce.
- **Five fields, following the B2B work-in-progress template.** The baseline's separate "What is this persona trying to do?" and "Attitudes & Influences" fields are folded in: what the persona is trying to accomplish goes under Needs | Pains, and attitudes and influences under Desired Outcomes | Goals.

##### Key Concepts

###### Persona vs. Proto-Persona

Productside makes an important distinction:

- **Persona**: a composite profile grounded in real customer research
- **Proto-persona**: a working profile built from limited evidence, team knowledge, and informed assumptions

If you have not validated it with customer research, call it proto.

###### User First, Buyer Second

This play starts with the **user persona**.

That means the person who actually uses, experiences, or lives with the product or service. In many B2B contexts, that is not the same person as the buyer, approver, or executive sponsor.

Only after the user persona is coherent should you repeat the exercise for the buyer.

**Who owns which personas:** Product Managers focus primarily on user personas  -  the people who experience the product day-to-day. Marketing and Sales typically own buyer and influencer personas. Knowing this scopes the PM's work: go deep on the user, treat the buyer as the secondary pass.

The Playbook names three persona types:

- **User:** the person who uses the product day to day
- **Buyer:** the person who controls the budget and makes the buying decision
- **Influencer:** the person who sways the purchase or use but is not the user or buyer

###### Segment vs. Persona: Build for the Center

A segment defines **who** you target, based on data. A persona brings that segment to life as **one relatable character**. Build for the center of the segment (the poster child), not a version stretched to cover everyone.

If a field starts describing everyone ("values efficiency," "wants better tools"), the persona has drifted off-center. Pull it back to the specific person at the heart of the segment.

###### A Persona Is a Communication Tool

A persona's job is to help stakeholders quickly understand and empathize with the people the product serves, so they make better product decisions. Judge a finished persona by five tests:

- **Clarity:** could a busy stakeholder grasp who this person is in under a minute?
- **Story:** do the pieces add up to one believable, coherent person?
- **Empathy:** would stakeholders feel this person's goals and pains?
- **Relevance:** is it clear why this person matters to product decisions?
- **Focus:** is this the specific center of one segment, or a blurry everyone?

The bar is stakeholder empathy, not a perfect document. When a persona is fit for purpose, say so and stop polishing.

###### Customer-Side, Not Product-Team-Side

The persona should usually describe the **customer-side person your product serves**, not the Product Manager building the product.

If your product truly serves Product Managers, then that can be correct. Otherwise, turning "the PM" into the default persona is a drift bug, not a shortcut.

###### The Working Parts of the Productside Persona

The canonical playbook template centers on these fields:

- name and portrait
- bio and demographics
- quotes
- needs and pains (including what the persona is trying to accomplish and the behavior you observe)
- desired outcomes and goals (including their attitudes and influences)

Those fields are the working surface. They are not decoration.

The name is **alliterative**, pairing a first name with the role (Henry HR Specialist, Serena Security Officer), so the team remembers the person and the role together.

This skill follows the B2B work-in-progress template, which has five fields. The baseline template's separate "What is this persona trying to do?" and "Attitudes & Influences" fields are folded in, as the WIP instructions do: what the persona is trying to accomplish and the behavior you observe go under **Needs | Pains**; attitudes and influences go under **Desired Outcomes | Goals**.

###### Proto Means Hypothesis

A proto-persona is **a hypothesis wearing a face**. It should help the team act, but it must not claim certainty it has not earned. It stays provisional until research confirms it. The moment the team treats it as settled, it stops being a proto-persona and becomes a persona profile the team has committed to.

The Playbook's discipline is to **never blur what the PM believes with what was filled in for them**. Every line of a working draft carries one provenance tag:

- `[FROM YOU]` - the PM or their stakeholders supplied it
- `[RESEARCH]` - it came from evidence (interview notes, artifacts, web research), with the source named in the trailing evidence section
- `[AI-SUGGESTED, VALIDATE THIS]` - you filled a gap; this is a guess about the customer and among the first things to test

Quotes you write are always invented. Tag them `[AI-SUGGESTED, VALIDATE THIS]` and treat them as lines to test in interviews, never as evidence. Only words a real customer said get `[RESEARCH]`.

###### How AI Supports This Play

The Playbook casts AI as the **drafter of the proto-persona**. Given what the PM and their stakeholders already believe about this user, it turns those beliefs into a structured persona fast, so research starts with a target instead of a blank page. It fills gaps, but it marks every gap it filled, because those are guesses about the customer and the first things to test. What to believe, and what to test, stays the PM's call.

- **Use it when:** the work is early, before research, and the PM can name what the team already assumes about this user.
- **Avoid it when:** the PM already has real customer research (review the research-based persona instead, see [If the PM Brings a Draft](#if-the-pm-brings-a-draft)), or the proto-persona will never be validated. An untested proto-persona is just a committed stereotype. Say so if the PM has no plan to test it.
- **Return:** every line tagged by provenance, the riskiest assumptions marked to test first, and a plan to validate the profile through research.

###### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

###### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

##### Application

Use [Template](playbook-skills.md#psk-proto-persona--template) for the full scaffold.


###### Required Output Convention

Default to a **clean persona artifact** that a human can use directly.

The artifact comes first. Commentary is secondary.

That means:

- fill every main section of the persona
- keep each section sized to the canonical carrying capacity
- do not add analysis, ranking, or advice before the artifact is complete

The output comes in two stages:

1. **Working draft.** Every line ends with its provenance tag (`[FROM YOU]`, `[RESEARCH]`, `[AI-SUGGESTED, VALIDATE THIS]`). Tags are the only annotation allowed inside the fields. They are short and sit at the end of the line, so the field content still fits the template.
2. **Committed copy.** Once the PM accepts the draft, offer a clean, paste-ready copy with the tags removed, followed by a short **Riskiest Assumptions** list built from the AI-suggested lines, ranked by what to test first. The tags move out of the fields, but they never disappear.

If the PM asks for a clean copy straight away, give it, but still end with the Riskiest Assumptions list.

###### If the PM Brings a Draft

There are two kinds of draft. Treat them differently.

**Beliefs, notes, or a rough proto-persona** (before research). Follow the Playbook's drafting order: alliterative name, Bio & Demographics, Desired Outcomes & Goals, Needs | Pains, then Quotes. For each field, review what the PM gave you first, add only where they are thin, and tag every line. Ask one question at a time when a field is too thin to fill honestly. This mirrors the critique guidance in this Play.

**A finished, research-based persona.** Do not redraft it. This mirrors the critique guidance in this Play:

1. Ask who the stakeholder audience is if you don't know.
2. Give one honest read: is it already good enough to share? If yes, say so plainly and stop.
3. If not, work through the five tests (Clarity, Story, Empathy, Relevance, Focus) one at a time. Say what works, name the one change that would most improve it, and offer a concrete suggestion to accept, adjust, or reject.
4. Prioritize three to five changes. Name the weak spots minor enough to leave alone.
5. Sharpen wording, structure, and emphasis only. **Never add attributes, quotes, or data the research did not produce.** That includes counts and frequencies ("7 of 9 interviewees said...", "most fraud leads") unless the PM supplied them. If a count would strengthen the persona, ask the PM for it instead. When asked to add quotes to a research persona, offer only to pull real lines from the interview notes. Don't offer to write illustrative or composite quotes, even labeled.

###### Canonical Capacity Rules

The canonical example page has real carrying-capacity limits. Respect them.

Use the budgets in [Template and capacity guidance](playbook-skills.md#psk-proto-persona--template).

Default expectations:

- `Name & Portrait`: extremely short
- `Quotes`: a few compact quotes or quote fragments
- `Bio & Demographics`: the largest field, but still compact
- `Needs | Pains`: concise summary, not a paragraph pile, including a tight line on what they are trying to accomplish
- `Desired Outcomes | Goals`: compact future-state statements, plus short attitudes and influences

If the output would need summarizing before it can be pasted into the playbook, it is too long.

###### Step 1: Confirm Who the Product Serves

Before writing anything, answer:

- what product or service are we talking about?
- who experiences the problem most directly?
- who uses the product in the field?
- is that person different from the buyer?

If you cannot answer those clearly, stop and resolve the customer-side target first.

**Guard against tech-role bias.** LLMs default heavily toward software engineers, architects,
and developers when asked about technology products. Most products - even deeply technical
ones - serve people who are not programmers. An IoT platform PM's customer is a fleet
manager, a logistics director, or a smart city program lead - not a solutions architect.
A clinical data platform PM's customer is a clinical operations lead - not a data engineer.

Before writing the persona, confirm the role by asking: does this person write code, design
systems, or architect solutions as their primary job? If the answer is no, the persona
should not read like a technologist. Pains, tools, language, and daily work should reflect
the actual role, not a developer proxy.

###### Step 2: Gather Evidence Before Writing

Once you know the role and industry, offer the user two things before drafting:

1. **Web research** - offer to run a quick search for the target role in the target industry. Good sources include job postings, industry forums, trade press, day-in-the-life profiles, and professional community discussions. The goal is to replace assumptions with real language, real pain points, and real context.

2. **User-supplied artifacts** - ask whether the user has materials they want to share: interview notes, support tickets, call recordings, internal research, job descriptions, competitive intel, or anything else that would ground the persona in evidence.

Either, both, or neither is fine - the user decides. But always offer before drafting.

What to look for in web research:

- how practitioners in this role describe their own work and frustrations
- tools, systems, and workflows they mention
- organizational pressures and incentives specific to the industry
- language and jargon they actually use (not marketing language about them)
- hiring patterns that reveal what the role really does day-to-day

Feed what you find directly into the persona fields. Cite sources lightly in the trailing evidence section, not inline.

###### Step 3: Build the Primary User Persona

Start with the **user persona**.

Fill all of these sections:

- `Name & Portrait`
- `Bio & Demographics`
- `Quotes`
- `Needs | Pains` (with what they are trying to accomplish and the behavior you observe)
- `Desired Outcomes | Goals` (with attitudes and influences)

Do not start with the buyer unless the buyer is also the primary user.

Do not silently skip a section because you think the persona is "already clear enough."

###### Step 4: Use Real Signals Where You Have Them

Pull from any available evidence:

- interview notes
- call notes
- support themes
- field observations
- existing research
- sales or customer success insights

If you do not have direct evidence for something, avoid fake certainty. Acknowledge that in one short trailing note instead of bloating the artifact itself.

###### Step 5: Give the Persona a Real Shape

The persona should feel like a person the team could recognize.

That means:

- specific enough to guide choices
- grounded in behavior, not just demographics
- written in language the customer might actually use

Weak:

- "Works in tech"
- "Needs better tools"
- "Wants productivity"

Stronger:

- "Regional operations planner responsible for keeping warehouse labor, carrier timing, and dock capacity aligned across three sites"
- "Spends two hours every shift reconciling schedule changes across email, spreadsheets, and the warehouse system"

###### Step 6: Separate Pains from Goals

Do not flatten everything into one blob.

- `Needs | Pains` = friction, obstacles, frustrations, unmet needs
- `Desired Outcomes | Goals` = what better looks like for this person

This distinction matters because later Productside plays depend on it.

###### Step 7: Capture Attitudes and Influences Within Goals

The WIP template asks about attitudes and influences under Desired Outcomes | Goals. They are not filler. Capture them there:

- beliefs that shape adoption
- organizational pressures
- tools or people they trust
- incentives, fears, or habits that affect behavior

###### Step 8: Make Provenance and Risk Explicit

Before treating the profile as useful:

- check that every line carries a provenance tag, and that no AI-suggested line is tagged as the PM's or as research
- list the **Riskiest Assumptions**: the AI-suggested lines that would most change the persona if wrong, ranked by what to test first
- name how to validate them (who to interview, what to observe)

If you skip this, the team may treat a hypothesis as truth. Keep the trailing section concise. The tags carry most of the honesty, so the list only needs the top risks.

###### Step 9: Repeat for the Buyer Only If Needed

After the user persona is coherent, you may repeat the same structure for the buyer persona.

Keep them separate if:

- one person uses the product
- another person approves the purchase
- another person influences the decision

###### Step 10: Do Not Add Extra "Helpful" Commentary by Default

Do not add:

- strongest-section commentary
- ranking of pains or goals
- long caveats
- side analysis

unless the user explicitly asks for it.

The default skill output should be a persona the human can use immediately.

###### Step 11: Evolve It

Personas are only helpful if the team uses and updates them.

As research progresses:

- replace assumed quotes with real ones
- refine pains and goals
- split one proto-persona into two if the segment was too broad
- retire fields that turn out to be wrong

#### psk-proto-persona / Template

Use this template to build a **Productside-style proto-persona** for the primary user first, then optionally the buyer.

Tag every line of the working draft with where it came from:

- `[FROM YOU]` - the PM or their stakeholders supplied it
- `[RESEARCH]` - it came from evidence; name the source under Proto-Persona Caveats
- `[AI-SUGGESTED, VALIDATE THIS]` - a filled gap; a guess to test first

Tags go at the end of the line and are the only annotation allowed inside the fields. When the PM commits the persona, the clean copy drops the tags from the fields and keeps the Riskiest Assumptions list.

###### When to Use This

Use this when you need a working customer profile before full validation, and you want the team to have a shared understanding of who the product is serving.

###### Template

```markdown
# Proto-Persona

## Persona Type
- User, Buyer, or Influencer:
- Validation status: Proto-persona / Validated persona
- Confidence level: Low / Medium / High

## Product Context
- Product or service:
- Problem space:
- Why this persona matters:

## Name & Portrait
- Name (alliterative, first name + role, e.g. "Henry HR Specialist"):
- Portrait description:

> Quality check: The persona should feel specific enough to remember and discuss. Avoid placeholders like "User A" unless this is a temporary working draft.

## Bio & Demographics
- Role / title:
- Industry or operating context:
- Organization context:
- Seniority or experience level:
- Relevant demographics:
- Backstory:

> Quality check: Include only demographics and background that actually help the team understand product behavior, needs, or constraints.

## Quotes
- Quote 1:
- Quote 2:
- Quote 3:

> Quality check: Quotes should reveal how this person thinks, speaks, or feels. Avoid generic lines like "I want better tools."
> Provenance check: Invented quotes are always `[AI-SUGGESTED, VALIDATE THIS]`. Only words a real customer said are `[RESEARCH]`.
> Capacity check: Keep quotes compact enough to fit the canonical quotes field.

## Needs | Pains
- Pain or need 1:
- Pain or need 2:
- Pain or need 3:
- What they are trying to accomplish, and the behavior we observe:

> Quality check: These should describe meaningful friction, unmet need, or frustration. Make them specific enough that the team can respond to them.
> Capacity check: Keep this section concise enough to paste into the canonical pain field.

## Desired Outcomes | Goals
- Desired outcome or goal 1:
- Desired outcome or goal 2:
- Desired outcome or goal 3:
- Attitudes and influences (beliefs, people and tools they trust, pressures):

> Quality check: Keep this future-state oriented. These are not tasks or features. They are the improvements this person wants in their work or life.
> Capacity check: Write compact future-state statements, not long rationale.

## Proto-Persona Caveats
- What still feels provisional:
- What should be validated next:
- Highest-priority research gaps:
- Evidence sources (for `[RESEARCH]` lines):

## Riskiest Assumptions
The AI-suggested lines that would most change this persona if wrong, ranked by what to test first.
1.
2.
3.

> Quality check: Does every line above carry a provenance tag? Is any AI-suggested line passed off as the PM's belief or as research?
> Focus check: Does this persona describe the center of one segment, or a blurry everyone?

## Buyer Relationship
- Is this person also the buyer?
- If not, who likely buys or approves?
- What tension might exist between user needs and buyer priorities?

## Research Next Steps
- Who should we interview next?
- What should we validate first?
- Which assumptions are riskiest?
```

###### Usage Guidance

- Build the **user persona first**.
- Only then create a separate buyer persona if the buyer is materially different.
- Keep the proto nature explicit until research confirms the profile.
- Do not use confidential client details in examples or shareable artifacts.
- Keep provenance tags short and at the end of each line. Keep validation notes concise unless the user explicitly asks for heavier evidence annotation.
- Complete every main persona section before adding any commentary.

#### psk-proto-persona / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** Describe the warehouse operations analyst's responsibilities, goals, pains, and workarounds, marking sourced observations separately from assumptions.
- **Weak:** "Busy professional who values efficiency" cannot guide a specific product decision.
- **Drift to avoid:** Invented authenticity: a believable customer quote or research label generated by AI is not evidence. Omit it or label it as fictional.


##### Common Pitfalls

- **Making the Persona Too Generic:** Add behavioral context, concrete pains, and language that reflects how the person actually works.

- **Treating Assumptions as Research:** Tag every line of the working draft with its provenance, and end with a ranked Riskiest Assumptions list. The clean committed copy drops the tags from the fields but keeps that list.

- **Pitfall 2b: Adding Commentary That Displaces the Artifact:** Complete the artifact first. Keep commentary short and trailing.

- **Building the Buyer First:** Build the user first. Add buyer second when relevant.

- **Making the Product Manager the Persona by Default:** Ask explicitly: who experiences the product's value or pain in the field?

- **Defaulting to a Tech Role:** Ask what the customer actually does day-to-day. Most products - even deeply technical ones - serve people whose primary job is not writing code or designing systems. A fleet manager, a logistics director, a clinical operations lead, a utility substation engineer - these are the real customers. If the role does not involve building software as its core function, the persona should not read like a technologist.

- **Confusing Pains with Goals:** Keep friction separate from the future state the persona wants to achieve.

- **Never Updating the Proto-Persona:** Treat the proto-persona as a living document and revise it as discovery produces evidence.

- **Exceeding Template Capacity:** Write to the canonical budget, not to the model's appetite for prose.

- **The Assumptions Are the Model's, Not the Team's:** Review what the PM supplied before adding anything. Add only where they are thin, and tag every addition `[AI-SUGGESTED, VALIDATE THIS]`. If most of the persona is AI-suggested, say so and ask for more of the team's own beliefs before going further.

- **A Name and a Face Imply Proof:** Keep validation status visible ("Proto-persona") on the artifact. Keep invented quotes tagged as invented. Route the Riskiest Assumptions into empathy interviews (psk-empathy-interviews) before the persona is shared as a validated profile.

- **Stretching the Persona to Cover Everyone:** Build for the center of the segment. If the segment really holds two different people, split it into two personas rather than averaging them into one.

##### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-proto-persona) for supporting source material and expanded examples.


### Play 07: Empathy Interviews

Stable identifier: `psk-empathy-interviews`.

#### psk-empathy-interviews / Instructions

##### Purpose

Create a **Productside-style Empathy Interview artifact** for your target customer.

This skill is for the **Discover + Investigate** phase. It closes the evidence loop - moving the team from assumptions about customer needs to validated understanding grounded in real conversation.

This is a **process skill**, not a content-fill skill. It spans three phases:

1. **Prepare** - define learning objectives, choose topic areas, sharpen the PM's interview questions, and optionally rehearse technique against realistic interview moments
2. **Conduct** - provide the PM with a reference card for running the interview (the agent cannot do this step)
3. **Document** - help structure raw interview notes into a findings board the team can act on

The agent helps with phases 1 and 3. Phase 2 happens in the field - the PM conducts the actual interview. The agent cannot substitute for face-to-face (or video) conversation with a real customer. It can play the customer in a rehearsal, but a rehearsal is practice, never research.

Use this skill when you need to:

- validate assumptions from proto-persona or JTBD work with real customers
- understand the customer's actual workflow, frustrations, and motivations
- discover jobs, outcomes, and problems you did not anticipate
- capture the emotional dimension of the customer experience (what they feel, not just what they do)
- build empathy across the product team by documenting first-person customer language

This is not a survey design tool, a usability test script, or a sales call framework. Empathy interviews are discovery conversations - open-ended, story-seeking, and judgment-free.

###### Usage Notes

- This is a **process skill** (`type: process`), not a component skill. It spans preparation, interview conduct, and findings documentation across multiple sessions.
- The agent helps with preparation (Phase 1) and documentation (Phase 3). The PM conducts the actual interview (Phase 2) in the field - the agent cannot substitute for real customer conversation.
- **Preparation follows the Playbook's AI pages:** name the decision, set learning objectives, choose 4-5 topic areas, and review the PM's own questions (leading, closed, solution-fishing, no objective). The agent drafts questions only on request, labeled as a starting draft.
- **Rehearsal (optional):** the agent can play the persona in a technique drill, one tough moment at a time, then review the PM's technique. It is practice, never research. Nothing from a rehearsal goes into findings.
- Evidence gathering: this skill qualifies for **web research + user artifacts**. Web research grounds the PM in the interviewee's domain before the interview. User artifacts (persona work, JTBD output, prior research) inform question preparation.
- The findings board produces structured output that feeds downstream skills: Jobs-to-Be-Done, Desired Outcomes, Problems, and Feels/Appears.
- Upstream: psk-proto-persona (persona grounds the interview target), psk-jobs-to-be-done (provides assumptions to test).
- Downstream: psk-problem-identification (uses problems and jobs from findings), psk-proto-persona (refine with real quotes and observations).

##### Key Concepts

###### The 70/30 Rule

The interviewee is the star. Target 70% listening, 30% talking. If the PM is talking more than the interviewee, they are lecturing, not learning.

###### Open-Ended Questions Over Yes/No

Questions that start with "Can you walk me through..." or "Tell me about the last time..." produce stories. Questions that start with "Do you..." or "Is it..." produce one-word answers that teach nothing.

###### "Tell Me About the Last Time..." Is the Key Probe

The most powerful interview technique is asking about a specific, recent occurrence. "Tell me about the last time you had to reconcile data across systems" produces richer insight than "How do you usually handle data reconciliation?"

###### Look for Say/Feel/Do/Think Inconsistencies

Customers say one thing, feel another, do a third, and think a fourth. The gap between what someone says they do and what they actually do is where the real insight lives. Watch for these disconnects during the interview.

###### Biased Questions Poison the Findings

Leading questions ("Don't you think a dashboard would help?") confirm the PM's hypothesis instead of testing it. The PM must learn to ask neutral questions that let the customer lead.

###### Confirm Understanding by Reflecting Back

After the interviewee shares something significant, repeat back what you heard in your own words: "So if I understand correctly, you're saying..." This does two things: it confirms you captured their meaning accurately, and it often prompts the interviewee to correct, expand, or go deeper  -  surfacing nuance a follow-up probe alone might miss.

###### The Findings Board Maps to Downstream Artifacts

The documentation phase produces four categories that feed directly into other playbook skills:

- **Jobs-to-Be-Done** - what the customer is trying to accomplish (feeds psk-jobs-to-be-done)
- **Desired Outcomes** - what success looks like for the customer (feeds psk-jobs-to-be-done)
- **Problems** - friction, blockers, and pain points observed (feeds psk-problem-identification)
- **Feels/Appears** - emotional and behavioral observations (feeds psk-proto-persona refinement)

###### Team Sport

The playbook says to make it a team sport. Have design and engineering counterparts listen in on interviews. They catch different signals than the PM does, and shared exposure to the customer builds alignment faster than secondhand summaries.

###### Prepared but Not Rigid

Prepare 5-8 questions, but do not follow the list like a script. The best insights come from following the customer's thread, not from checking boxes. If the customer opens an unexpected door, walk through it.

###### The Rescue Probe

If the conversation stalls or the PM gets stuck, the universal fallback is: "Why?" or "Tell me more." These two phrases restart almost any stalled thread.

###### Learning Objectives Serve a Decision

Every interview round should inform a decision the team has to make. Name it before writing a single question ("whether to build for hub airports or small airports first," "whether reconciliation or scheduling is the bigger pain"). Every question the PM keeps should trace to a learning objective, and every learning objective should trace to that decision. A question with no objective behind it is a question to cut.

###### Topic Areas, Not a Script

The Playbook prepares interviews around **4-5 topic areas**, not a fixed list of questions. Topic areas let the PM improvise and dig deeply while the interviewee steers the conversation and tells their stories. Aim them at what the interviews must validate: the persona's jobs and desired outcomes, and the **root-cause problems** that cause pains and block those outcomes.

Questions still matter. The PM writes them, a few per topic area, as starting points. The interview follows the story, not the list.

###### Rehearse Before It Counts

Empathy interviewing is a skill and must be practiced. The Playbook says to role-play with friends and colleagues, and an AI rehearsal partner works too. The drill presents one tough interview moment at a time (a one-word answer, a feature request, a say/do contradiction, silence), and the PM practices the reflex: dig deeper, stay neutral, confirm understanding, resist pitching. Rehearsing out loud, in a chat tool's voice mode, lets the PM hear their own leading phrasing and practice sitting in silence.

A rehearsal is practice, not data. Nothing from it goes into findings.

###### How AI Supports This Play

The Playbook casts AI as **preparation partner and sparring partner**. It focuses the PM on what matters so they can guide the conversation, and it can play tough interview moments so the PM can rehearse before it counts.

What AI cannot do is be the person being interviewed. The whole point of this Play is the real conversation. The moment AI answers as the customer and that answer is treated as input, the team has a script, not research, and the Play is corrupted.

- **Use it when:** real interviews are scheduled and the PM wants to sharpen questions or rehearse technique.
- **Avoid it when:** the PM wants AI to answer as the customer in place of an interview. A simulated interview is practice, not research. If no interviews are scheduled, help schedule them; do not simulate them.
- **Return:** leading or closed questions identified for the PM to rewrite, each kept question tied to a learning objective, and the PM's follow-up reflexes drilled against realistic interview moments. See [If the PM Brings a Draft](#if-the-pm-brings-a-draft) and Step 6.

###### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

###### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

##### Application

Use [Template](playbook-skills.md#psk-empathy-interviews--template) for the full scaffold.


###### Required Output Convention

This skill produces artifacts in **three phases**. Not all phases happen in a single session:

- **Phase 1 output:** The decision and learning objectives, 4-5 topic areas, the PM's interview questions (reviewed) with follow-up probes, and a conduct reference card. Optionally, a rehearsal and its technique review.
- **Phase 3 output:** A structured findings board with Jobs-to-Be-Done, Desired Outcomes, Problems, and Feels/Appears entries sized for the canonical template.

The PM returns to the agent after conducting the interview (Phase 2) to get help with Phase 3.

###### If the PM Brings a Draft

When the PM arrives with draft questions or topic areas, review them before writing anything new. This mirrors the critique guidance in this Play.

1. **Confirm the persona and the decision.** If no learning objectives exist, get them first (Step 3).
2. **Review each question.** Flag leading questions, closed (yes/no) questions, and questions that fish for the PM's solution. Quote the words at fault.
3. **Tie each kept question to a learning objective.** Name any question with no objective behind it, and any objective with no questions.
4. **Name the gaps.** Name missing topic areas (often current workarounds, impact, and the emotional cost) without writing the questions for them.
5. **Offer rewrites last**, as options to accept, adapt, or reject. The PM writes the final wording.

Return the review as a compact table (question, verdict, why, objective) before any rewritten guide.

###### Step 1: Confirm the Product Context and Target Persona

Before writing anything, answer:

- What product or service are we talking about?
- Who is the target customer (the person who will be interviewed)?
- What is their role and what do they do day-to-day?

If you cannot answer these clearly, stop and resolve the target first.

**Guard against tech-role bias.** The interviewee should be the actual customer - the person who uses or buys the product in the field. An IoT platform PM interviews fleet managers, not solutions architects. A clinical data platform PM interviews clinical operations leads, not data engineers. Before drafting questions, confirm: does this person write code, design systems, or architect solutions as their primary job? If no, the questions should not read like a technical interview.

###### Step 2: Gather Evidence Before Writing

Once you know the target persona and role, offer the user two things before drafting questions:

1. **Web research** - offer to run a quick search for the target role in the target industry. Look for how practitioners describe their own work, frustrations, and daily reality. Job postings, industry forums, trade press, and professional community discussions are good sources. The goal is to understand the domain well enough to ask informed questions - not to replace the interview.

2. **User-supplied artifacts** - ask whether the user has materials to share: existing persona work, JTBD output, problem identification artifacts, support tickets, previous interview notes, or any other discovery work that would ground the questions in evidence.

Either, both, or neither is fine - the user decides. But always offer before drafting.

###### Step 3: Define Learning Objectives

Before writing questions, ask the PM: what decision will these interviews inform? What do you need to learn to make it? What assumptions need testing?

Learning objectives are not interview questions - they are the strategic goals behind the questions. Examples:

- "We assume clinical data managers spend 40% of their time on manual reconciliation - is that true?"
- "We do not know how this role currently solves the problem - what workarounds exist?"
- "We need to understand the emotional cost of the current process, not just the operational cost."

3-5 learning objectives are enough. They guide question selection and help the PM stay focused during the interview.

###### Step 4: Choose Topic Areas, Then Sharpen the Questions

**Topic areas first.** Suggest 4-5 topic areas tied to the learning objectives, aimed at the persona's jobs, desired outcomes, and the root-cause problems behind their pains. Give one or two example open-ended questions per area so the PM sees what good looks like.

**The PM writes the questions.** Ask the PM to draft a few questions per topic area, then review them using [If the PM Brings a Draft](#if-the-pm-brings-a-draft). If the PM asks you to draft the questions (or is in Discovery mode), write 5-8 and label them a starting draft for the PM to rewrite in their own voice. Run the same review on your own draft before handing it over.

Whoever writes them, structure the questions to flow naturally:

1. **Opening** - warm-up questions about the person's role and daily work ("Can you walk me through a typical day...")
2. **Core exploration** - questions that dig into the target problem area ("Tell me about the last time...")
3. **Current state** - how they handle the problem today ("What have you tried to make this faster? What has worked best?")
4. **Impact** - what the problem costs them ("How does this affect your work / team / goals...")
5. **Closing** - open-ended wrap-up ("Is there anything else you'd like to share...")

For each question, include 1-2 follow-up probes. Follow-ups should dig deeper:

- "Can you tell me about a specific time that happened?"
- "Why did you choose that approach?"
- "What happened next?"
- "How did that make you feel?"

Do not include yes/no questions. Do not include questions that mention the product or a specific solution. Every kept question names the learning objective it serves.

###### Step 5: Review Conduct Guidance

Before the PM goes into the field, surface the conduct reference card:

- **70/30 rule** - listen 70%, talk 30%
- **Open-ended probes** - "Tell me about the last time...", "Can you walk me through...", "Why?"
- **Story-seeking** - ask about specific recent occurrences, not general habits
- **Bias avoidance** - do not mention the product, do not suggest solutions, do not ask leading questions
- **Inconsistency watch** - note gaps between what they say, feel, do, and think
- **Note-taking** - record exact quotes when possible; note emotions and body language
- **Rescue probe** - if stuck, ask "Why?" or "Tell me more"
- **Closing** - thank them, ask if they are open to further conversations or testing

###### Step 6: Rehearse Technique (Optional)

If the PM wants to practice, run a rehearsal drill. This mirrors the critique guidance in this Play.

1. **Say what this is.** It's practice, not data, and nothing from it goes into findings. Suggest voice mode if the PM's tool has one.
2. **Present one realistic interview moment at a time**, playing the persona: a one-word answer, a jump to a feature request, saying one thing while describing the opposite, going quiet. Respond to the PM's moves as the persona plausibly would, then present the next moment.
3. **When the PM says they are done, give an honest review.** Did they dig deeper, stay neutral and unbiased, confirm understanding, and resist pitching solutions? Say where they slipped and what to do differently next time.
4. **Close by sending them to a real customer.** Remind the PM not to treat anything the simulated persona said as truth.

Never carry rehearsal lines into Step 8 (Document Findings), into quotes, or into any downstream artifact.

###### Step 7: The PM Conducts the Interview

**The agent cannot do this step.** The PM (or a teammate) conducts the actual interview in the field. The agent waits for the PM to return with notes.

When the PM returns, ask for their raw notes, quotes, and observations before structuring findings.

###### Step 8: Document Findings

After the interview, help the PM structure raw notes into the findings board. The board has four quadrants:

**Jobs-to-Be-Done** - what the customer is trying to accomplish, discovered from their stories. Use the Productside job format:
- Functional: [Action verb] + [object of the action]
- Emotional: Feel [Emotion] when [Circumstance]
- Social: Seen as [Social Perception] to [whom]

4-6 entries, ~6-8 words each (sticky-note sized).

**Desired Outcomes** - what success looks like for the customer. Use Direction + Metric + Context format. 3-4 entries, ~8-12 words each.

**Problems** - friction, blockers, and pain points observed during the interview. Write as concrete observations, not abstract categories. 4-6 entries, ~8-12 words each (sticky-note sized).

**Feels/Appears** - emotional and behavioral observations. What the customer appeared to feel, not what they explicitly said. 4 entries, ~6-10 words each (sticky-note sized).

###### Step 9: Capture Raw Quotes

Pull 4-6 direct quotes from the interview notes. These are the customer's actual words - not paraphrased, not cleaned up. Quotes ground the findings in real evidence and are powerful artifacts for building team empathy.

Keep quotes to ~15-20 words each.

###### Step 10: Synthesize Across Interviews

If the PM has conducted multiple interviews, help identify patterns:

- Which jobs and problems appear across multiple interviews?
- Where do interviewees agree? Where do they diverge?
- Are there persona segments emerging from the data?
- What was surprising or unexpected?

Do not force consensus. Divergence is signal, not noise.

###### Step 11: Offer Next Steps

After the findings are documented, offer the user up to three next-step options:

1. **Refine the proto-persona** - update the persona with real quotes, validated pains, and observed attitudes using psk-proto-persona
2. **Move to Problem Identification** - synthesize interview findings into candidate problem statements using psk-problem-identification
3. **Conduct more interviews** - if the sample is small or the findings are inconclusive, prepare questions for another round

Present these as options, not as mandatory steps. The user decides what comes next.

#### psk-empathy-interviews / Template

###### When to Use This

Use this template during **Discover + Investigate** to prepare for empathy interviews, guide conduct, and document findings. This is a process skill that spans three phases - preparation, interview conduct (PM does this in the field), and documentation.

###### Template

###### Phase 1: Interview Preparation

```markdown
# Empathy Interview Preparation

## Product Context

- Product or service:
- Target market segment:
- Target interviewee role:
- Interviewee's primary job:

## Decision These Interviews Inform

- Decision:
- Who makes it, and by when:

## Learning Objectives

What do we need to learn to make that decision? What assumptions need testing?

1.
2.
3.
4.
5.

> Quality check: Are these learning objectives specific enough to guide question selection?
> Quality check: Do they focus on the customer's reality, not on validating a feature idea?
> Quality check: Does every learning objective trace to the decision above?

## Topic Areas

4-5 areas to explore. They let the interviewee steer and tell stories while you dig deeper. Aim them at the persona's jobs, desired outcomes, and the root-cause problems behind their pains.

| # | Topic Area | Learning Objective It Serves | Example Open-Ended Question |
|---|------------|------------------------------|-----------------------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

## Interview Questions

Prepare 5-8 open-ended questions in your own words, a few per topic area. Do not follow this list rigidly - explore deeper when the customer opens a thread.

| # | Question | Follow-Up Probes | Objective |
|---|----------|-----------------|-----------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |

> Quality check: Does every question start with "Can you...", "Tell me about...", "What...", "How...", or "Why..."?
> Quality check: Does any question mention the product name, a feature, or a specific solution? If yes, rewrite it.
> Quality check: Could any question be answered with just "yes" or "no"? If yes, convert to open-ended.
> Quality check: Do the questions cover: daily workflow, pain points, current solutions, impact, and emotional experience?
> Quality check: Does every question name the learning objective it serves? Cut any that don't.
> Capacity check: Questions should be ~15-20 words. Follow-up probes should be ~8-12 words.
```

###### Phase 2: Conduct Guidance (Reference Card)

```markdown
# Interview Conduct Reference Card

## Before the Interview
- [ ] Rehearse your technique (optional): one tough moment at a time, out loud if you can. Practice only; nothing from it goes into findings.
- [ ] Review learning objectives
- [ ] Have questions accessible but not as a rigid script
- [ ] Set up note-taking (or have a teammate take notes)
- [ ] Test recording equipment if applicable (with permission)

## During the Interview

**Opening**
- Introduce yourself and explain why you are talking with them
- Set expectations: "There are no right or wrong answers - I want to learn from your experience"
- Ask permission to take notes or record

**Core Rules**
- 70% listening, 30% talking
- Ask about specific recent occurrences ("Tell me about the last time...")
- Dig deeper on surface answers ("Why?", "Can you say more about that?", "What happened next?")
- Do NOT mention the product, pitch features, or suggest solutions
- Do NOT ask yes/no questions - convert to open-ended
- Do NOT ask "Would you use a tool that...?" or "How would you feel about...?"

**Watch For**
- Inconsistencies between what they say, feel, do, and think
- Emotional reactions - frustration, pride, resignation, anxiety
- Workarounds and hacks they have built
- Language they use to describe their work (capture exact words)

**If You Get Stuck**
- Ask "Why?"
- Ask "Tell me more"
- Ask "Can you give me a specific example?"

**Closing**
- "Is there anything else you'd like to share about your experience?"
- Thank them
- Ask if they are open to further conversations or testing

## After the Interview
- [ ] Document findings within 24 hours (use Phase 3)
- [ ] Share raw notes with teammates who listened in
- [ ] Note what surprised you - surprises are the highest-signal findings
```

###### Phase 3: Document Findings

```markdown
# Empathy Interview Findings

## Interview Context

- Interviewee role:
- Date:
- Interview duration:
- Product context:
- Interviewer(s):

## Raw Quotes

Capture 4-6 direct quotes - the customer's actual words, not paraphrased.

| # | Quote |
|---|-------|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |
| 6 | |

> Quality check: Are these the customer's actual words, or a paraphrase? Use their language.
> Capacity check: Quotes should be ~15-20 words each.

## Findings Board

### Jobs-to-Be-Done

What is the customer trying to accomplish? Discovered from their stories.

| # | Job (Functional / Emotional / Social) |
|---|---------------------------------------|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |
| 6 | |

> Quality check: Do these jobs come from what the customer said, not what you assumed before the interview?
> Quality check: Are all three job types represented if the evidence supports them?
> Capacity check: ~6-8 words per entry (sticky-note sized).

### Desired Outcomes

What does success look like for the customer? Use Direction + Metric + Context.

| # | Desired Outcome |
|---|-----------------|
| 1 | |
| 2 | |
| 3 | |
| 4 | |

> Quality check: Does every outcome use the Direction + Metric + Context format?
> Quality check: Are these the customer's desired outcomes, not your product's value propositions?
> Capacity check: ~8-12 words per entry.

### Problems

Friction, blockers, and pain points observed during the interview.

| # | Problem |
|---|---------|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |
| 6 | |

> Quality check: Are these concrete and specific, not abstract categories like "inefficiency"?
> Quality check: Did the customer describe this problem, or are you inferring it?
> Capacity check: ~8-12 words per entry (sticky-note sized).

### Feels / Appears

Emotional and behavioral observations. What the customer appeared to feel, not just what they said.

| # | Observation |
|---|-------------|
| 1 | |
| 2 | |
| 3 | |
| 4 | |

> Quality check: Do these capture emotions and behaviors, not just opinions?
> Quality check: Did you note any say/feel/do/think inconsistencies?
> Capacity check: ~6-10 words per entry (sticky-note sized).

## Key Insights

- What surprised you:
- What confirmed prior assumptions:
- What contradicted prior assumptions:
- What needs more interviews to validate:

## Evidence Notes

- What is well-supported by this interview:
- What is still a single data point:
- Recommended next steps:
```

###### Usage Guidance

###### The Three Phases

This template covers a multi-session process:

1. **Phase 1 (Preparation)** - the agent helps name the decision, define learning objectives, choose topic areas, review the PM's questions, and optionally rehearse technique. This happens before the interview.
2. **Phase 2 (Conduct)** - the PM takes the reference card into the field and conducts the interview. The agent cannot do this step.
3. **Phase 3 (Documentation)** - the PM returns with raw notes. The agent helps structure findings into the board format.

The PM may complete Phase 1, leave for days or weeks, and return for Phase 3. That is normal.

###### How Many Questions

The canonical template has 6 question slots. Default to 5-8 questions:

- 1-2 opening questions about the person's role and daily work
- 2-3 core questions exploring the target problem area
- 1-2 questions about current solutions and impact
- 1 closing question

Add follow-up probes for each question. Do not over-prepare - 8 questions is a ceiling, not a target.

###### Findings Board Sizing

The findings board maps to the canonical template's sticky-note grid:

| Section | Entries | Words per Entry | Guidance |
|---------|---------|-----------------|----------|
| Jobs-to-Be-Done | 4-6 | ~6-8 | Use Productside JTBD formats |
| Desired Outcomes | 3-4 | ~8-12 | Direction + Metric + Context |
| Problems | 4-6 | ~8-12 | Concrete, specific observations |
| Feels/Appears | 4 | ~6-10 | Emotional and behavioral |
| Raw Quotes | 4-6 | ~15-20 | Customer's actual words |

###### Connecting to Other Skills

- **Upstream:** Proto-persona (grounds the interview target and questions); JTBD (provides assumptions to test)
- **Downstream:** Problem Identification uses the problems and jobs from this artifact; proto-persona refinement uses the quotes and emotional observations
- **Parallel:** JTBD can be updated with newly discovered jobs and outcomes from the interview

###### Capacity Reference

See [Template and capacity guidance](playbook-skills.md#psk-empathy-interviews--template) for the exact word and character budgets per field.

| Field | Word Budget | Guidance |
|-------|-------------|----------|
| Interview Question | ~15-20 | Open-ended, no product mentions |
| Follow-Up Probe | ~8-12 | Dig deeper: "Why?", "Tell me more" |
| Raw Quote | ~15-20 | Customer's actual words |
| Job-to-Be-Done | ~6-8 | Sticky-note sized; Productside format |
| Desired Outcome | ~8-12 | Direction + Metric + Context |
| Problem | ~8-12 | Sticky-note sized; concrete observation |
| Feels/Appears | ~6-10 | Sticky-note sized; emotional/behavioral |

#### psk-empathy-interviews / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** Ask a regional store manager: "Tell me about the last time inventory differed across your stores." Record the real interview separately from preparation.
- **Weak:** "Would a real-time dashboard solve your inventory problem?" leads the witness toward the proposed solution.
- **Drift to avoid:** Rehearsal as research: simulated interview answers must never enter findings as customer evidence.


##### Common Pitfalls

- **Asking Leading Questions:** Strip the question of any solution language or implied answer. "How do you currently monitor [process]?" lets the customer describe their reality. "Don't you think a dashboard would help?" tells them what to say.

- **Asking Yes/No Questions:** Convert to open-ended: "Can you walk me through the last time you had to reconcile data across systems? What happened?"

- **Talking More Than 30%:** Set a physical reminder (a sticky note that says "LISTEN"). After asking a question, wait. Count to five silently before saying anything else. Silence prompts the customer to fill the gap with real insight.

- **Asking About Features Instead of Problems:** Ask about their current reality, not a hypothetical future. "What happens today when X goes wrong?" reveals the problem. "What features would fix it?" reveals the customer's guess about a solution, which is not the same thing.

- **Not Digging Deeper on Surface-Level Answers:** Probe: "Can you tell me more about how you manage it?" or "What does 'fine' look like on a bad day?" The second layer is almost always richer than the first.

- **Skipping Documentation:** Document findings within 24 hours of the interview. Use the findings board structure - it forces categorization and makes the data usable by the rest of the team.

- **Defaulting to a Tech Role:** Before drafting questions, confirm: is this the person who uses or buys the product in the field? If their primary job is not writing code or designing systems, the questions should reflect their actual daily work.

- **Treating This as a Content-Generation Skill:** Phase 3 (Document Findings) requires real interview data as input. If the PM has not talked to a customer, the agent should help with Phase 1 (Prepare Questions) and send the PM into the field. Do not fabricate findings.

- **Treating a Rehearsal as Research:** Label every rehearsal as practice at the start and the end. Refuse to document findings from a simulated interview. If the PM has no real interviews yet, help them recruit and schedule them.

- **Reading the Question List Like a Script:** Prepare around topic areas, not a script. Treat questions as starting points, follow the thread the interviewee opens, and use "Why?" and "Tell me more" to go deeper. Rehearsal (Step 6) builds the reflex.

##### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-empathy-interviews) for supporting source material and expanded examples.


### Play 08: Affinity Mapping

Stable identifier: `psk-affinity-mapping`.

#### psk-affinity-mapping / Instructions

##### Purpose

Create a **Productside-style Affinity Map** from qualitative customer research.

This skill helps a Product Manager synthesize raw observations from empathy interviews, customer feedback, or other research into a working artifact with:

- labeled theme clusters grouping similar observations
- named patterns that reveal what the data is actually saying
- key insights that translate patterns into product-relevant implications

The point is not to produce a summary of what customers said. The point is to surface what the observations collectively reveal.

###### Usage Notes

- **Coach by default.** With real notes, the skill walks the PM through the Playbook's five-step method (orient, split, immerse, group, name) and the PM does the grouping, labeling, and insights.
- **Draft on request.** If the PM asks the skill to group the notes, it produces a map labeled "AI draft grouping: for the team to challenge."
- **No real notes, no map.** The skill will not map invented observations. It routes to psk-empathy-interviews instead.

##### Key Concepts

###### This Skill Bridges Interviews and Problem Identification

Affinity mapping is the synthesis step. Raw observations from empathy interviews are too granular to act on directly. Affinity mapping groups them into patterns. Those patterns become the input to psk-problem-identification.

Without this step, teams often jump from "we talked to customers" to "here is our feature roadmap" without ever making the intermediate inference.

###### Observations and Insights Are Different Things

- **Observations** are what you heard, saw, or documented during research. They are factual and specific.
- **Themes** are labels for clusters of similar observations. They name the pattern.
- **Key insights** are inferences about what those patterns mean for product decisions.

A key insight is not a summary of a theme. It answers: "Given this pattern, what does that mean for what we should build or prioritize?"

###### The Grouping Is Not Permanent

The playbook tip: "Group your data in multiple ways to reveal new insights. There is no wrong way to do it."

Affinity mapping is iterative. If a different grouping reveals something the first pass missed, that is a feature, not a mistake. The artifact should invite re-examination, not lock conclusions.

###### Minimum Three Applies to Both Themes and Insights

Fewer than three themes usually signals that the grouping is too coarse. Fewer than three key insights usually signals that the synthesis stopped at clustering and never made the inferential leap.

###### The Sense-Making Is the Point

The value of affinity mapping lives in the team's debate over where each note belongs. Whoever does the grouping does the thinking. That is why the Playbook keeps the clustering, the theme labels, and the insights with the PM and their team, and casts AI as a guide through the method.

###### The Agent's Role: Coach by Default, Draft on Request

- **Real notes, default:** coach the PM through the method (Step 3). The PM groups, labels, and writes the insights. You teach, question, and illustrate. The line, from the Playbook: you may point at two notes and ask "are these the same behavior?" You may not say "these two go together under this theme."
- **Real notes, and the PM asks you to group them (or chooses Discovery):** produce a draft map, labeled **AI draft grouping: for the team to challenge**. Show why each cluster holds together, and end with the groupings you were least sure of. The team still decides.
- **Fragments only:** coach or draft as above, and label every theme provisional.
- **No real notes:** stop. Affinity mapping on invented data teaches nothing and proves nothing. Offer to help prepare interviews (psk-empathy-interviews), or to set up the template for a workshop once notes exist. Never invent observations or quotes to map. Labeling the work "hypotheses" doesn't change this: produce no themes, clusters, or map layout at all. If the PM needs something for a meeting, offer a short plain list of assumptions to test in interviews, clearly labeled, and point to psk-empathy-interviews.

###### What Binds a Cluster

Test every grouping against the same questions:

- Do these notes share the same **behavior or need**, or just the same **topic**?
- Is this a **real pattern**, or a coincidence of wording?
- What binds them? Usually a **shared pain**, a **shared workaround**, or a **shared goal**.

A theme label captures that shared behavior or need. A label that only names a topic ("Technology," "Communication") has not found the pattern yet.

###### How AI Supports This Play

The Playbook casts AI as a **live guide through the method**. Affinity mapping often starts slow, with a pile of real notes and no clear way in. AI walks the PM through each grouping decision, one note or cluster at a time, and asks the questions that sharpen their reasoning: why does this note belong here, what separates this group from that one, is this a real pattern or a coincidence.

The clustering, the labels, and the insights stay the PM's calls. AI makes the method less intimidating. It does not make the decisions.

- **Use it when:** the PM has real interview or research notes and knows grouping needs to happen but doesn't know how to start.
- **Avoid it when:** there are no real notes yet. Guiding a method on fake data teaches nothing worth learning.
- **Return:** guidance through the method, and a completed set of grouped, labeled themes that the PM can explain and defend.

###### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

###### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

##### Application

Use [Template](playbook-skills.md#psk-affinity-mapping--template) for the scaffold.


###### Required Output Convention

Default to a **clean, paste-ready artifact**.

That means:

- at least three labeled theme clusters, each with grouped observation bullets
- at least three key insights, each with a one-sentence title and a short paragraph
- observation bullets kept short (8-12 words each)
- key insight paragraphs sized for the template (50-80 words)
- explanation and methodology notes below the artifact, not inside the fields
- the map states who grouped it: **the team** (coached) or **AI draft grouping: for the team to challenge**

###### Step 1: Check the Source Data

Before grouping observations, verify the data is customer-side evidence: observations about customer behavior, experience, friction, and goals.

Flag and do not proceed if the observations are primarily:

- internal team opinions or preferences
- product feature requests written in the PM's voice
- engineering architecture notes
- stakeholder directives

Affinity mapping is only as useful as the evidence it synthesizes. If the input data is not customer-side, the output themes will reflect team assumptions, not customer reality.

###### Step 2: Collect Available Artifacts

Ask whether the user has materials to supply:

- empathy interview notes or transcripts
- customer feedback logs or support tickets
- survey open-text responses
- competitive research observations
- outputs from psk-empathy-interviews, psk-jobs-to-be-done, or psk-proto-persona

The more raw material supplied, the stronger the clustering. If only fragments are available, note that the resulting themes are provisional and should be validated before being used in psk-problem-identification.

Do not skip this ask.

###### Step 3: Coach the Method (Default)

Unless the PM asks you to group the notes, walk them through the Playbook's method one step at a time. Do not move on until they finish the current step. This mirrors the critique guidance in this Play.

1. **Orient.** In a few sentences, explain what affinity mapping is and what a good result looks like.
2. **Break notes into observations.** Coach the PM to put each distinct observation on its own note. Show one example of splitting a note that holds two ideas, then have them check theirs.
3. **Immerse.** Have the PM read all the notes first. Ask what stands out, what surprises them, what repeats. Do not summarize the notes for them.
4. **Group.** Have the PM put together notes that seem to share something. Test each grouping with the questions in [What Binds a Cluster](#what-binds-a-cluster). When they are stuck, offer the kinds of things that bind a cluster (shared pain, shared workaround, shared goal) to consider. Do not say which notes go together.
5. **Name the themes.** For each cluster, ask what the notes truly share and have the PM write the label. If the label only names a topic, show a generic example of a stronger label, then have them try again.
6. **Develop the key insights.** Have the PM write at least three. Test each with Step 6's rules.

Mark every example or suggestion as something to consider, accept, adjust, or reject, never as the answer. Keep the PM encouraged; this is a skill they are building. Then format what they commit into the template.

If the PM asks you to group the notes instead, Steps 4-6 below are how you build the draft. They are also the rules you hold the PM's own grouping to when coaching.

###### Step 4: Group the Observations

Cluster the raw observations into groups where similar findings sit together.

Rules for this step:

- Create at least three clusters. More is fine if the data warrants it.
- Do not force observations into neat categories if they genuinely sit between two clusters. A cross-cutting observation is useful data.
- Each cluster should be internally consistent: observations within a cluster should be meaningfully similar, not just topically adjacent.
- Do not discard outlier observations. Findings that do not cluster easily often signal the most overlooked problems.

###### Step 5: Label the Themes

Give each cluster a theme label that names the pattern happening in that cluster, not just the subject area.

Strong theme label: names what is happening for the customer.
- Example: "Scheduling Delays Caused by Disconnected Systems"
- Not: "Scheduling" or "System Problems"

Weak theme label: names a topic that could hold almost any observation.
- Example: "Process Issues" or "Communication Challenges"

Each theme label should be specific enough that a teammate unfamiliar with the research could roughly predict what observations belong inside it.

Default to 4 themes when the data supports it. The blank template has 4 circles. Do not artificially limit to 4 if the data warrants more.

###### Step 6: Develop the Key Insights

Write at least three key insights. One insight per major theme is the baseline. A particularly rich or important theme may warrant a dedicated insight even if it is not the largest cluster.

Each key insight has two required parts:

**Title (one sentence, 5-8 words):** Names the challenge or pattern in plain language.

**Paragraph (50-80 words):** Explains what this pattern means for product decisions. Should answer: What is happening for the customer? Why does it matter? What should the product team understand or do differently because of this?

Key insights are inferences, not summaries. If the insight paragraph could have been written by reading only the theme label, it has not done the synthesis work.

###### Step 7: Review for Completeness

Before finalizing:

- Did the team do the grouping, or is this an AI draft? If it is a draft, is it labeled as one, and has the team challenged it?

- Do the themes cover the breadth of the data, or is there a major cluster of observations that went unlabeled?
- Does any single observation appear in more than one theme cluster? If so, resolve which cluster owns it, or name it as a cross-cutting theme.
- Do the key insights answer "so what?" or do they just restate the theme label?
- Are there at least three themes and at least three insights?
- Are the observation bullets short enough to be paste-ready?

###### Step 8: Offer Next Steps

After delivering the completed affinity map, offer three paths:

1. **Use these key insights in psk-problem-identification** to turn the strongest patterns into candidate problem statements.
2. **Review the insights as a team** to identify which pattern represents the highest-priority problem to pursue.
3. **Re-run affinity mapping with a different grouping lens** to check whether a different clustering reveals patterns the first pass missed.

#### psk-affinity-mapping / Template

###### When to Use This

Use this template during **Discover + Investigate** after you have collected qualitative observations from customer research. You are ready to map when you have raw notes from empathy interviews, customer feedback, survey responses, or other customer-side sources and need to organize them into patterns.

Upstream work that feeds this template: psk-empathy-interviews (primary), psk-jobs-to-be-done, psk-proto-persona.

Downstream: the key insights from this map feed psk-problem-identification.

###### Template

```markdown
# Affinity Map

## Research Context

- Product or service:
- Research conducted:
- Number of observation sources (interviews, surveys, feedback entries, etc.):
- Date mapped:
- Grouped by: The team (coached) / AI draft grouping: for the team to challenge

## Theme Clusters

Group your observations into clusters of similar findings. Label each cluster with a theme
that names the pattern, not just the subject area.

> Quality check: Does each theme label name what is happening for the customer, not just what
> the topic is?
> Quality check: For each cluster, can you say what binds it (a shared pain, workaround, goal,
> or behavior), and is it a real pattern rather than shared wording?
> Quality check: Is each observation a single idea? Split any note that holds two.
> Quality check: Are there at least three distinct clusters?
> Quality check: Do the clusters together cover the breadth of the data, not just the
> loudest findings?
> Capacity check: Theme label should be 6-10 words. Each observation bullet should be 8-12
> words. Aim for 5-8 observations per cluster.

### Theme 1: [Pattern Label]

- [Observation: what a customer said, did, or experienced]
-
-
-
-

### Theme 2: [Pattern Label]

- [Observation]
-
-
-
-

### Theme 3: [Pattern Label]

- [Observation]
-
-
-
-

### Theme 4: [Pattern Label] (add more themes as the data warrants)

- [Observation]
-
-
-
-

## Key Insights

Write at least three key insights. Each insight has a title (one sentence naming the
challenge or pattern) and a paragraph (50-80 words explaining what this pattern means
for product decisions).

Key insights are inferences, not summaries. The paragraph should answer: what is happening
for the customer, why does it matter, and what should the product team understand because
of this pattern?

> Quality check: Does each title name a challenge or pattern in plain language?
> Quality check: Does each paragraph answer "so what?" rather than restating the theme label?
> Quality check: Is each insight grounded in multiple observations, not a single anecdote?
> Capacity check: Title 5-8 words. Paragraph 50-80 words.

### Key Insight 1: [One-Sentence Title]

[Paragraph explaining what this pattern means for product decisions. What is the customer
experiencing? Why does this matter? What should the team understand or do differently
because of this finding?]

### Key Insight 2: [One-Sentence Title]

[Paragraph]

### Key Insight 3: [One-Sentence Title]

[Paragraph]

## Completeness Check

Before treating this map as final, confirm:

- [ ] All major clusters from the raw data are labeled (no significant observations left
      ungrouped)
- [ ] No observation appears in more than one theme cluster without resolution
- [ ] Each key insight answers "so what?" rather than restating its theme label
- [ ] At least three themes and at least three key insights are present
- [ ] Observation bullets are short enough to paste into the template (8-12 words each)

## Notes (optional)

- Observations that did not cluster:
- Themes considered and discarded:
- Suggested re-grouping angles to explore:
- Open questions for follow-up:
```

###### Usage Guidance

###### Filling the Template

1. Start with **Research Context** to anchor what data went into this map.
2. Fill **Theme Clusters** one at a time. Label the theme only after you have seen what observations belong together - resist naming the theme before clustering.
3. Write **Key Insights** after all clusters are labeled. Do not write insights cluster by cluster as you go; seeing all the clusters together often changes what the insights should say.
4. Run the **Completeness Check** before treating the map as done.
5. The **Notes** section is optional. Use it if there are outlier observations or re-grouping ideas worth capturing.

###### If You Have No Observation Data Yet

Affinity mapping requires input data. If no customer-side observations are available:

- Offer to help the user run psk-empathy-interviews first.
- If the user wants a scaffold to use in an upcoming workshop, fill the theme and insight sections with labeled placeholder sections and explain that they should be completed collaboratively with the team after data is collected.
- Do not generate observations from the agent's training data and present them as customer findings.

###### What Goes Where

| Section | Contains | Does NOT Contain |
|---------|----------|------------------|
| Theme Clusters | Direct customer observations grouped by pattern | Opinions, solutions, feature requests, team preferences |
| Theme Labels | A named pattern describing what is happening | A broad topic area that could hold any observation |
| Key Insights | Inferences about what the patterns mean for the product | Restatements of theme labels, feature recommendations |
| Notes | Outliers, open questions, re-grouping ideas | The main deliverable content |

###### Connecting to Other Skills

- **Upstream:** psk-empathy-interviews provides the raw observation notes. psk-jobs-to-be-done and psk-proto-persona provide additional customer context that can inform how observations are grouped.
- **Downstream:** The key insights from this map feed psk-problem-identification. The strongest insight often becomes the focal point for the candidate problem that gets developed in psk-framing-the-problem.

###### Capacity Reference

| Field | Guidance |
|-------|----------|
| Theme label | 6-10 words. Names the pattern, not the topic. |
| Observation bullet | 8-12 words. Direct, factual, customer-side. |
| Key insight title | 5-8 words. Plain language. |
| Key insight paragraph | 50-80 words. Answers "so what?" |

#### psk-affinity-mapping / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** Freight-broker observations about chasing shipment updates form a pattern: visibility gaps create reactive operations. Keep each observation in one cluster and explain the implication.
- **Weak:** A cluster called "Visibility" names a topic without showing a pattern.
- **Drift to avoid:** Observation overlap: putting the same note in several clusters inflates the apparent evidence. Assign its primary meaning or split genuinely separate observations.


##### Common Pitfalls

- **Naming Themes by Topic, Not Pattern:** Name what is happening, not what it is about. "Fragmented Communication Tools Slow Handoffs" has diagnostic value. "Communication" does not.

- **Treating Key Insights as Summaries:** Write insights that answer "so what?" and "what does this mean for what we prioritize or build?" If the insight paragraph could have been inferred from the label alone, it is not yet an insight.

- **Discarding Outlier Observations:** Keep outlier observations visible. If multiple outliers cluster loosely together, name that as an emerging theme. If a single observation stands alone, flag it in the completeness review.

- **Collapsing Distinct Themes to Hit a Target Count:** Keep themes separate if the underlying observations point to different root causes or different customer roles. Six specific themes are more useful than three bloated ones.

- **Mapping Team Opinions Instead of Customer Evidence:** Return to Step 1. Replace internal opinion entries with direct customer observations. If no customer-side data exists yet, run psk-empathy-interviews before mapping.

- **Stopping at the Cluster, Skipping the Insight:** Always complete the key insights section before treating the affinity map as done.

- **Running Affinity Mapping Alone:** Run affinity mapping as a cross-functional team exercise. The process of debating where an observation belongs is part of the value. When the group agrees on a theme label, they have done the sensemaking together.

- **Writing Insights Too Narrowly to Be Actionable:** Key insights should reflect patterns across multiple observations from multiple customers or sources. If only one observation supports a theme, the theme may not yet be valid.

- **AI's Themes Quietly Become the Team's:** Coach by default (Step 3). If the PM asks for a draft grouping, label it as one, show why each cluster holds together, and have the team challenge it before anything moves downstream.

- **Guided Is Mistaken for Validated:** State the evidence base on the map (number and type of sources). Mark themes resting on thin evidence as provisional, and name what more research would confirm them.

##### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-affinity-mapping) for supporting source material and expanded examples.


### Play 09: Problem Identification

Stable identifier: `psk-problem-identification`.

#### psk-problem-identification / Instructions

##### Purpose

Create a **Productside-style Problem Identification artifact** from customer research.

This skill helps a Product Manager turn customer understanding into a compact working surface:

- customer jobs
- pains
- gains
- supporting empathy interview quotes
- candidate problem statements

The point is not to produce a long explanation of the problem space. The point is to help the human complete the play.

This artifact is also a **cross-functional alignment tool.** The output makes customer understanding visible, shareable, and debatable across product, design, engineering, and leadership  -  not just useful to the PM who ran the discovery.

###### Usage Notes

- This exemplar follows the `psk-` naming contract
- It is intentionally budget-aware and template-capacity-aware
- Most default outputs should stay sticky-note-sized or small-cell-sized
- **Coach by default:** the skill asks the PM for the root cause beneath each pain rather than naming it, and catches features posing as problems
- **Evidence honesty:** quotes come only from supplied research (unfilled slots are marked `[needs a real quote]`), and unvalidated causes are marked `[CAUSE TO VALIDATE]`

##### Key Concepts

###### This Play Is an Aggregator

Problem Identification is where earlier discovery work gets pulled together:

- jobs from Jobs-to-Be-Done
- pains and outcomes from Personas & Proto-Personas
- quotes and lived experience from Empathy Interviews
- patterns from Affinity Mapping

The skill should therefore synthesize, not restart discovery from scratch. **Jobs brought in from earlier work should be treated as revisable**  -  as you validate with customers, reframe any job that doesn't hold up. Evidence updates the artifact; don't treat earlier assumptions as fixed truth.

###### The Customer Circle Is the Visual Structure

The canonical template organizes this play as a concentric circle:

- **Center:** the customer persona
- **Inner ring:** Pains and Gains
- **Outer ring:** Customer Jobs
- **Outside the circle:** Problems (root causes of pains, barriers to gains)
- **Sidebar:** Empathy Interview Quotes

This structure is not decoration  -  it shows how problems relate to jobs and how pains and gains are distinct layers between the customer and the things blocking them. A PM filling this template should be thinking in those concentric layers, not just populating a flat list.

###### Problem Statements Use a Specific Productside Format

Candidate problems should use this structure:

`[Problem] gets in the way of achieving [Outcome] for [Persona].`

Do not improvise a different sentence form unless the user explicitly asks for alternatives.

###### Jobs, Pains, Gains, and Problems Are Not the Same

- **Customer jobs** = what the customer is trying to get done
- **Pains** = friction, obstacles, or negative experience
- **Gains** = positive outcomes or benefits they want
- **Problems** = root causes or barriers that block gains or create pains

If these blur together, the play gets muddy fast.

###### A Pain Is a Symptom; a Problem Is the Cause Beneath It

A pain is what the customer **feels**. A problem is the **root cause** that creates the pain or blocks the outcome. "Passengers arrive unprepared" is a pain. "Confusing or late prep instructions" is a cause. Restating a pain in the problem format ("Unprepared passengers get in the way of...") skips the diagnosis while looking finished.

To get from pain to problem, ask what creates the pain. If the answer is the pain reworded, keep digging.

###### A Missing Feature Is Not a Problem

"No real-time dashboard," "lack of integration," and "no automated alerts" name solutions by their absence. When a candidate problem is really a missing feature, ask what problem that feature would solve, and write that instead. Keep the play in the problem space.

###### A Clean Statement Is Not a Proven One

The format makes thinking legible, not correct. A root cause stays a hypothesis until interviews back it. Mark every cause that isn't yet backed by evidence `[CAUSE TO VALIDATE]`, so the team knows what to test before framing the problem in the next play.

###### The Agent's Role: Coach by Default, Draft on Request

- **Default:** for each pain, ask the PM what root cause creates it. Push back when the answer is the pain reworded or a feature in disguise. Once the PM names a real cause, help write it in the Productside format and sharpen the wording. Do not name the cause for them, in any form: no lists, no examples ("it might be..."), and no causes folded into a question ("Is it that she can't see X, or that Y?"). Ask open questions about what the PM heard, saw, or was told ("What happens today when...? What did they say gets in the way?").
- **On request, or in Discovery mode:** propose candidate causes, each marked `[CAUSE TO VALIDATE]`, for the PM to accept, adjust, or reject.
- **Always:** never invent quotes, outcomes, or personas. Quotes come only from supplied research.

###### Quotes Are Supporting Evidence, Not Decoration

The quotes help prove the candidate problems are grounded in real customer experience.

They should sound like lived reality, not sanitized summary copy.

###### Template Capacity Matters

The canonical Productside template for this play has many **sticky-note-sized or small-cell fields**.

That means the default output must be:

- short
- specific
- paste-ready

Do not generate mini-essays for fields that behave like notes.

See [Template and capacity guidance](playbook-skills.md#psk-problem-identification--template) for the real canonical budgets.

###### How AI Supports This Play

The Playbook casts AI as a **coach that separates pains from problems and formats the result**. The PM has done the research. AI helps shape affinity themes, interview insights, jobs, and personas into sharp, well-formed problem statements. The cause has to come from the PM and their evidence.

- **Use it when:** the PM has real insights from affinity mapping and interviews and wants help separating symptoms from causes.
- **Avoid it when:** the PM has not talked to customers yet. AI will format confident root causes and problem statements no one can defend. Say so, and route to psk-empathy-interviews.
- **Return:** pains separated from the root causes beneath them, problem statements in one consistent format, and every guessed root cause marked `[CAUSE TO VALIDATE]`.

###### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

###### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

##### Application

Use [Template](playbook-skills.md#psk-problem-identification--template) for the scaffold.


###### Required Output Convention

Default to a **clean, paste-ready artifact**.

That means:

- fill every expected slot in the template
- jobs, pains, and gains should be short enough for sticky-note or small-cell use
- quotes should be short enough to fit the playbook cells
- problem statements should fit the canonical carrying capacity
- explanation belongs below the artifact, not inside the fields

For the default output, produce exactly:

- 4 customer jobs
- 4 pains
- 4 gains
- up to 6 empathy interview quotes, **real quotes only**
- 6 candidate problem statements

Do not silently reduce those counts because a shorter list feels more elegant. The one exception is quotes: never invent a quote to fill a slot. If the research supplies fewer than six, fill the rest with `[needs a real quote]`.

Append `[CAUSE TO VALIDATE]` to any candidate problem whose root cause is not yet backed by evidence.

If the user wants extended reasoning, add it after a fully completed artifact in a short trailing note.

###### Step 1: Start from Customer Evidence

Before drafting, ask the user whether they have materials to share that would ground the artifact in real evidence:

- customer interview notes or transcripts
- support tickets or call logs
- quotes already collected
- jobs, pains, or gains identified in earlier discovery
- persona or proto-persona output
- any other internal research or field observations

This skill synthesizes earlier discovery work - the more the user can supply, the less the output relies on assumption. Do not skip this ask.

If there is no customer evidence at all, say so plainly. The Playbook advises against this play until the PM has talked to customers. Recommend psk-empathy-interviews first. If the PM still wants a first pass (Discovery), produce it as a labeled hypothesis: no quotes (every slot `[needs a real quote]`), and every candidate problem marked `[CAUSE TO VALIDATE]`.

###### If the PM Brings a Draft

When the PM arrives with pains and a first read on their causes, or with drafted problem statements, work through them rather than redrafting. This mirrors the critique guidance in this Play.

1. **For each pain, ask for the root cause.** If the PM's answer is the pain reworded, say so and ask them to dig.
2. **Watch for solutions in disguise.** If a "problem" is a missing feature, point at it and ask what problem the feature would solve. Don't list candidate causes for the PM to pick from, and don't hint at them as examples or "is it X or Y?" questions; the cause has to come from what they heard. This applies to a cause that looks like a symptom, too: ask why it happens, without guessing the answer.
3. **Format the real causes.** Write each as `[Problem] gets in the way of achieving [Outcome] for [Persona]`, pulling the outcome and persona from what the PM gave you.
4. **Mark the guesses.** Append `[CAUSE TO VALIDATE]` to any cause the PM is still guessing at.

###### Step 2: Write the Customer Jobs

Capture what the customer is trying to get done.

For this play, jobs should be **compact**. Most should fit in a sticky-note-sized field.

Avoid:

- broad mission statements
- generic aspirations
- internal team tasks

Prefer:

- short action-oriented job statements
- concrete customer progress

Output exactly 4 jobs unless the user explicitly asks for a different count.

###### Step 3: Identify Pains

Pains are the friction, obstacles, risks, delays, confusion, or negative experiences surrounding the job.

Keep them short enough to paste directly into the playbook.

Do not turn them into explanation paragraphs.

Output exactly 4 pains unless the user explicitly asks for a different count.

###### Step 4: Identify Gains

Gains are the positive outcomes the customer wants when the job goes well.

Keep gains distinct from pains:

- pains remove friction
- gains create positive progress or benefit

Output exactly 4 gains unless the user explicitly asks for a different count.

###### Step 5: Select Supporting Quotes

Choose quotes that make the problem feel real. **Select them from the research the PM supplied. Never write them.** A quote the agent wrote is not evidence, however real it sounds.

Good quotes:

- show frustration, workaround, or unmet need
- were actually said by a customer
- are short enough to fit the template

Output up to 6 quotes. Mark any unfilled slot `[needs a real quote]`.

###### Step 6: Write Candidate Problems

Use the Productside sentence structure:

`[Problem] gets in the way of achieving [Outcome] for [Persona].`

Each candidate should be:

- concrete
- customer-centered
- a cause, not a pain reworded or a missing feature
- short enough to fit the canonical field

By default, get the cause from the PM (see [If the PM Brings a Draft](#if-the-pm-brings-a-draft)). Mark any cause not yet backed by evidence `[CAUSE TO VALIDATE]`.

Do not pad the sentence with unnecessary context. The field is small.

Output exactly 6 candidate problems unless the user explicitly asks for a different count.

###### Step 7: Keep the Artifact Compact

For this skill, brevity is usability.

If the output is so long that the human Product Manager has to rewrite it before using it, the skill has failed.

Do not let good prose outrank usable template completion.

###### Step 8: Add Optional Short Notes

If helpful, add a brief trailing section such as:

- `What to pressure-test next`
- `Weakest candidate problems`
- `Open evidence gaps`

Keep it separate from the paste-ready artifact.

Do not add a notes section at all unless:

- the user asks for it, or
- the artifact is already fully complete

#### psk-problem-identification / Template

Use this template to build a **Productside-style Problem Identification artifact** from customer research.

Most fields in this play are small. Keep entries compact and paste-ready.

###### Template

```markdown
# Problem Identification

## Product Context
- Product or service:
- Target persona:
- Research source:

## Customer Jobs
- Job 1:
- Job 2:
- Job 3:
- Job 4:

> Quality check: Keep jobs short and concrete. Most should fit in a sticky-note-sized field.
> Completion rule: Fill all 4.

## Pains
- Pain 1:
- Pain 2:
- Pain 3:
- Pain 4:

> Quality check: These are obstacles, risks, frustrations, or negative experiences. Keep them compact.
> Completion rule: Fill all 4.

## Gains
- Gain 1:
- Gain 2:
- Gain 3:
- Gain 4:

> Quality check: Gains are positive outcomes the customer wants, not just the absence of pains.
> Completion rule: Fill all 4.

## Empathy Interview Quotes
- Quote 1:
- Quote 2:
- Quote 3:
- Quote 4:
- Quote 5:
- Quote 6:

> Quality check: Every quote was actually said by a customer and is short enough to fit the template.
> Completion rule: Real quotes only. Mark any unfilled slot `[needs a real quote]`. Never invent one.

## Candidate Problems
- Problem 1: [Problem] gets in the way of achieving [Outcome] for [Persona].
- Problem 2: [Problem] gets in the way of achieving [Outcome] for [Persona].
- Problem 3: [Problem] gets in the way of achieving [Outcome] for [Persona].
- Problem 4: [Problem] gets in the way of achieving [Outcome] for [Persona].
- Problem 5: [Problem] gets in the way of achieving [Outcome] for [Persona].
- Problem 6: [Problem] gets in the way of achieving [Outcome] for [Persona].

> Quality check: Keep each candidate short enough to paste directly into the playbook field. Do not add explanation inside the statement.
> Quality check: Is each [Problem] a root cause, not a pain reworded and not a missing feature?
> Evidence check: Append `[CAUSE TO VALIDATE]` to any candidate whose cause is not yet backed by evidence.
> Completion rule: Fill all 6.

## What To Pressure-Test Next
- Which problem feels strongest?
- Which problem feels weakest?
- What evidence gap still matters?
```

###### Usage Guidance

- Do not turn jobs, pains, gains, or problems into paragraphs.
- If the user wants explanation, add it after the artifact.
- Respect the canonical template capacity in [Template and capacity guidance](playbook-skills.md#psk-problem-identification--template).
- Do not add the `What To Pressure-Test Next` section unless the artifact is already fully complete.

#### psk-problem-identification / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** "Late schedule updates get in the way of keeping dock assignments aligned." Connect this candidate to real observations and retain the customer's language.
- **Weak:** A paragraph combining several problems makes it hard to investigate any one of them.
- **Drift to avoid:** Missing feature as problem: "No dashboard" is a solution-shaped complaint. Identify the customer progress it obstructs.


##### Common Pitfalls

- **Writing Novellas into Sticky-Note Fields:** Respect the template capacity. Small field means short entry.

- **Pitfall 1b: Underfilling the Template:** Match the template slot count by default.

- **Confusing Pains with Problems:** Use pains as evidence, then write a candidate problem in the Productside format.

- **Writing Generic Jobs:** Write short but concrete customer jobs.

- **Making Gains a Mirror Image of Pains:** Ask what better looks like for the customer, not just what less-bad looks like.

- **Losing the Quotes:** Include short quotes that support the candidate problems.

- **Letting Commentary Replace the Artifact:** Complete the artifact first. Commentary is optional and trailing only.

- **Naming a Missing Feature as the Problem:** Ask what problem the missing feature would solve, and write that. "Late notice of policy changes gets in the way of achieving compliance for Henry" leaves the solution open.

- **Format Mistaken for Proof:** Mark every cause not yet backed by evidence `[CAUSE TO VALIDATE]`. Name the evidence base in Product Context. Treat the marked causes as the next round's interview topics.

- **Inventing Quotes to Fill the Slots:** Quotes come only from supplied research. Leave unfilled slots as `[needs a real quote]`.

##### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-problem-identification) for supporting source material and expanded examples.


### Play 10: Framing the Problem

Stable identifier: `psk-framing-the-problem`.

#### psk-framing-the-problem / Instructions

##### Purpose

Create a **Productside-style Framing the Problem artifact** that documents a validated problem and produces a clear problem statement.

This skill is for the **Discover + Investigate** phase and marks a **Key Decision Point** in the Productside Blueprint. It sits at the intersection of Investigate and Define - the PM is deciding that the problem is validated enough to move forward into solution definition.

This is a synthesis skill. It pulls together findings from earlier discovery work:

- persona work (psk-proto-persona)
- jobs-to-be-done (psk-jobs-to-be-done)
- empathy interviews
- problem identification (psk-problem-identification)
- affinity mapping

The output is a structured problem frame using the five-stem sequence, context and constraints, and a final problem statement. This artifact is what the PM reviews with their manager and introduces to product governance.

Use this skill when you need to:

- synthesize prior discovery into a single, reviewable problem definition
- craft a problem statement that leadership can evaluate and act on
- document the customer perspective before moving into solution space
- validate that the team is solving a real, evidence-backed problem

This is not a solution specification. If the output mentions features, tools, or implementation approaches, the framing has drifted into solution space.

###### Usage Notes

- The template produces a single artifact with three sections: Problem Framing (five stems), Context and Constraints, and Final Problem Statement.
- The five-stem sequence is fixed order: I am / Trying to / But / Because / Which makes me feel.
- Evidence gathering is **user artifacts only** - no web research offered. This skill synthesizes the PM's own discovery work.
- Upstream: psk-proto-persona, psk-jobs-to-be-done, psk-problem-identification, empathy interviews.
- Downstream: solution hypothesis, positioning, exploring the solution space (Discover + Define phase).

##### Key Concepts

###### Focus on the Why, and the Outcomes Will Follow

The playbook puts it simply: *"Focus on the 'why,' and the outcomes will follow."*

A problem frame that nails the root cause  -  the **Because** stem  -  gives the team more clarity about what to build than any amount of solution sketching. Don't rush to "what we need to build" before the "why this problem exists" is solid.

This is also a human-centered design exercise. It starts with the person experiencing the problem, not the solution space, and leaves room for creativity and imagination once the why is clear.

###### The Five-Stem Sequence Is a Fixed Structure

The Productside problem frame uses five stems in exact order. Do not reorder, skip, or merge them:

1. **I am:** Describe the user persona's experience with the problem in 3-4 key points
2. **Trying to:** List the outcome they care about
3. **But:** Describe what problem barriers stand in the way
4. **Because:** Enter the root cause of why the problem or barrier exists
5. **Which makes me feel:** Describe the emotions from the customer's point of view

Each stem has a specific job. "I am" establishes who and what they face. "Trying to" names the desired outcome. "But" names the concrete barriers. "Because" explains the root cause. "Which makes me feel" captures the emotional impact. Together they build a complete problem frame from the customer's perspective.

###### Context and Constraints Are Separate from the Problem Frame

Section 2 of the template captures the external conditions surrounding the problem - industry dynamics, regulatory requirements, geographic limitations, technology constraints, budget restrictions, or population characteristics.

These are not barriers (barriers go in "But"). Constraints are the environment the problem exists within. A barrier is what blocks the persona. A constraint is a condition the solution must operate within.

###### The Final Problem Statement Synthesizes the Stems

Section 3 takes the five stems and combines them into one cohesive problem statement. The statement should read as a single flowing narrative that a manager or governance body could understand without seeing the stem breakdown.

The statement must be consistent with the stems above it. If the final statement introduces new information not in the stems, or drops key elements, the frame is broken.

###### This Is a Decision Point

The playbook explicitly marks this template as a Key Decision Point. The output goes to leadership and product governance. The PM is saying: "I have identified and validated this problem. I want to move into defining a solution."

This means the problem frame should be polished enough to present, not a rough working draft. It also means the evidence behind it should be real - from customer research, not from assumptions.

###### Customer Perspective, Not Product Team Perspective

Every stem is written from the customer's point of view. "I am" refers to the customer. "Which makes me feel" captures the customer's emotions. If any stem reads like something the product team would say about their own work, the perspective has drifted.

###### Problem Framing, Not Solution Framing

No solution language is allowed in the problem frame. Do not mention:

- product names or features
- tools or technologies that could solve the problem
- implementation approaches
- "we need to build" or "the product should"

The problem frame describes the world as the customer experiences it today. Solutions come later, in a different play.

###### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **critic of the problem frame the PM drafted**. It checks each stem of the I am / Trying to / But / Because / Which makes me feel sequence for customer voice and evidence, catches a solution hiding in the frame, and tests whether the final statement synthesizes the stems. The frame stays the PM's, built from their discovery evidence.

- **Use it when:** the PM has discovery evidence and a draft frame, and wants it pressure-tested before the decision point.
- **Avoid it when:** there is no discovery evidence yet. A well-formed frame on a guessed problem is still a guess. Route to psk-problem-identification or psk-empathy-interviews.
- **Return:** each stem checked for customer voice, specificity, and evidence; solution language flagged; and the final statement tested against the stems.

###### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

###### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

##### Application

Use [Template](playbook-skills.md#psk-framing-the-problem--template) for the full scaffold.


###### Required Output Convention

Default to a **clean, paste-ready problem frame artifact**.

That means:

- fill all five stems, context and constraints, and the final problem statement
- keep each stem within its word budget (see Capacity Reference below)
- produce a final statement that synthesizes the stems into one cohesive narrative
- explanation belongs below the artifact, not inside the stem fields
- the artifact comes first; commentary is secondary

###### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses Discovery mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

###### Step 1: Confirm the Product and Persona

Before writing anything, answer:

- what product or service is the PM building?
- who is the customer persona whose problem is being framed?
- what prior discovery work exists (persona, JTBD, empathy interviews, problem identification)?

If you cannot identify a specific customer persona, stop and resolve the target first.

**Guard against tech-role bias.** The problem belongs to the customer - the person who uses or buys the product in the field. A clinical data platform's customer problem belongs to a clinical operations lead, not a data engineer. An industrial IoT platform's customer problem belongs to a plant manager, not a solutions architect. Before writing the "I am" stem, confirm: does this person actually experience the problem day-to-day?

###### Step 2: Gather Evidence Before Writing

Once you know the product and persona, offer the user materials to share before drafting:

**User-supplied artifacts** - ask whether the user has materials to ground the frame: interview notes, empathy mapping output, problem identification artifacts, JTBD work, support tickets, or earlier skill outputs.

This skill is **user artifacts only** - it synthesizes the PM's own discovery work. Web research is not offered because the problem frame should come from validated customer evidence, not from external sources the PM has not yet verified.

If the user has no artifacts and no prior discovery work, surface the tension: a problem frame without evidence is an assumption frame. Recommend doing persona, JTBD, or empathy interview work first, but proceed if the user wants to draft an assumption-based frame.

###### Step 3: Fill the "I am" Stem

Describe the persona's experience with the problem in 3-4 key points.

This stem establishes:

- who the persona is (role, not name)
- what their situation looks like
- what they are dealing with day-to-day

Write from the persona's perspective. Use concrete, specific language. "An HR specialist overwhelmed by manual processes" is better than "a professional facing challenges."

Word budget: ~30-40 words.

###### Step 4: Fill the "Trying to" Stem

State the outcome the persona cares about - what they are trying to achieve.

This is not a task list. It is the desired end state. "Automate administrative tasks and free up time for strategic initiatives" describes an outcome. "Complete form A-7 by Friday" describes a task.

Word budget: ~15-20 words.

###### Step 5: Fill the "But" Stem

Name the concrete barriers that stand in the way of the desired outcome.

Barriers are specific and observable:

- "Manual and time-consuming HR processes" - concrete
- "Things are difficult" - vague and useless
- "Outdated systems and fragmented tools slow progress" - concrete

Do not put constraints here. Constraints (regulatory, budget, geographic) go in Context and Constraints. Barriers are what blocks the persona from achieving their outcome.

Word budget: ~20-25 words.

###### Step 6: Fill the "Because" Stem

Explain the root cause - why the barrier exists.

This is the "why behind the why." The barrier is what blocks; the root cause is why that barrier persists. If the barrier is "manual and time-consuming processes," the root cause might be "the lack of an integrated platform and real-time data access."

Push past surface-level causes. "Because things have always been done this way" is not a root cause. "Because the organization's systems were implemented independently over a decade and were never integrated" is closer.

Word budget: ~20-25 words.

###### Step 7: Fill the "Which makes me feel" Stem

Capture the emotional impact from the persona's point of view.

This stem is not optional. It grounds the problem frame in the human experience. Product governance decisions are influenced by understanding the severity of the problem, and emotional impact is part of severity.

Use specific emotional language:

- "Frustrated, stressed, and unable to deliver the value my role demands" - specific
- "Bad" - not specific enough
- "Overwhelmed by the gap between what is expected and what is possible" - specific

Word budget: ~15-20 words.

###### Step 8: Write Context and Constraints

Document the external conditions surrounding the problem:

- **Industry context** - regulatory environment, competitive dynamics, market pressures
- **Geographic constraints** - regional requirements, distributed operations
- **Technology constraints** - legacy systems, integration limitations
- **Budget constraints** - limited resources, competing priorities
- **Population constraints** - characteristics of the target users

Constraints frame the environment the solution must operate within. They are not barriers (those went in "But") and they are not the problem itself.

Word budget: ~30-40 words.

###### Step 9: Synthesize the Final Problem Statement

Combine the five stems into one cohesive statement.

The final statement should:

- read as a single flowing narrative
- use the stem structure: "I am [role] [situation]. Trying to [outcome]. But [barriers]. Because [root cause]. Which makes me feel [emotions]."
- be consistent with the stems above - no new information, no dropped elements
- be presentable to leadership without additional context

Word budget: ~40-50 words.

###### Step 10: Keep the Artifact Compact

The canonical template uses defined fields with limited space. Every stem, the context section, and the final statement should fit within the word budgets specified.

If the output requires summarizing before it can be pasted into the playbook, it is too long.

Do not let good prose outrank usable template completion.

###### Step 11: Offer Next Steps

After the artifact is complete, offer the user up to three next-step options:

1. **Move to solution hypothesis** - the problem is framed and validated; begin exploring what to build (Discover + Define phase)
2. **Refine positioning** - use the problem frame to sharpen how the product is positioned against the problem
3. **Review upstream work** - if the problem frame exposed gaps, go back to proto-persona, JTBD, or empathy interviews to strengthen the evidence

Present these as options, not as mandatory steps. The user decides what comes next.

#### psk-framing-the-problem / Template

###### When to Use This

Use this template during **Discover + Investigate** when you have enough discovery evidence to frame a validated problem and craft a problem statement. This is a **Key Decision Point** - the output goes to leadership and product governance to justify moving into solution definition.

Upstream work that feeds this template: proto-persona, jobs-to-be-done, empathy interviews, problem identification, affinity mapping.

###### Template

```markdown
# Framing the Problem

## Product Context

- Product or service:
- Target market segment:
- Primary persona (the customer with the problem):

## 1. Problem Framing

**I am:**
Describe the user persona's experience with the problem in 3-4 key points


**Trying to:**
List the outcome they care about


**But:**
Describe what problem barriers stand in the way


**Because:**
Enter the root cause of why the problem or barrier exists


**Which makes me feel:**
Describe the emotions from the customer's point of view


> Quality check: Is every stem written from the customer's perspective, not the product team's?
> Quality check: Does the "But" name concrete, observable barriers - not vague "challenges"?
> Quality check: Is the "Because" a root cause, not a restatement of the barrier?
> Quality check: Is the "Which makes me feel" stem present with specific emotions, not just "frustrated"?
> Quality check: Is there any solution language in the stems (product names, features, tools)? Remove it.
> Capacity check: I am ~30-40 words. Trying to ~15-20 words. But ~20-25 words. Because ~20-25 words. Which makes me feel ~15-20 words.

## 2. Context and Constraints

Describe the industry, regulatory, geographic, technology, budget, or population constraints surrounding the problem.


> Quality check: Are these external conditions, not barriers? Barriers go in "But." Constraints describe the environment the solution must operate within.
> Capacity check: ~30-40 words.

## 3. Final Problem Statement

Synthesize the five stems into one cohesive statement.


> Quality check: Does the statement follow the stem structure (I am / Trying to / But / Because / Which makes me feel)?
> Quality check: Is every element in the statement traceable to a stem above? No new information should appear here.
> Quality check: Could a manager read this statement alone and understand the problem without seeing the stems?
> Capacity check: ~40-50 words.

## Evidence Notes (optional)

- Discovery sources used:
- What is well-supported by evidence:
- What is still assumption:
- Recommended next validation steps:
```

###### Usage Guidance

###### Filling the Template

1. Start with **Product Context** to anchor who this is for and whose problem it is.
2. Fill the **five stems in order** - do not skip or reorder. Each stem builds on the previous one.
3. Fill **Context and Constraints** separately - these are external conditions, not part of the problem frame itself.
4. Write the **Final Problem Statement** last, synthesizing all five stems into one cohesive narrative.
5. The **Evidence Notes** section is optional and trailing. Do not let it displace or delay the main artifact.

###### The Stem Sequence Is Fixed

The five stems must appear in this exact order:

1. I am
2. Trying to
3. But
4. Because
5. Which makes me feel

Do not merge stems, skip stems, or reorder them. Each has a distinct function in building the problem frame.

###### What Goes Where

| Section | Contains | Does NOT Contain |
|---------|----------|------------------|
| I am | Persona role, situation, 3-4 key experience points | Product features, team perspective |
| Trying to | The desired outcome | Task lists, feature requests |
| But | Concrete, observable barriers | Constraints (those go in Context) |
| Because | Root cause of the barrier | Surface-level restatements |
| Which makes me feel | Specific customer emotions | "Bad" or "frustrated" alone |
| Context and Constraints | Industry, regulatory, budget, technology, geographic conditions | Barriers (those go in But) |
| Final Problem Statement | Synthesis of all five stems | New information not in the stems |

###### Connecting to Other Skills

- **Upstream:** Proto-persona provides the "I am." JTBD provides the "Trying to." Problem Identification provides barriers, root causes, and candidate problems. Empathy interviews provide emotional evidence.
- **Downstream:** The validated problem statement justifies moving into Discover + Define - solution hypothesis, positioning, exploring the solution space.

###### Capacity Reference

See [Template and capacity guidance](playbook-skills.md#psk-framing-the-problem--template) for the exact word and character budgets per field.

| Field | Word Budget | Guidance |
|-------|-------------|----------|
| I am | ~30-40 | Role + situation + 3-4 key experience points |
| Trying to | ~15-20 | One clear outcome statement |
| But | ~20-25 | Concrete barriers, not vague "challenges" |
| Because | ~20-25 | Root cause, not barrier restatement |
| Which makes me feel | ~15-20 | 2-3 specific emotions with context |
| Context and Constraints | ~30-40 | External conditions bounding the solution space |
| Final Problem Statement | ~40-50 | Cohesive synthesis of all five stems |

#### psk-framing-the-problem / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** A superintendent is trying to coordinate trades, but learns of sequencing changes too late because crews rely on disconnected updates, leaving them anxious about rework. Develop all five stems.
- **Weak:** "We need a scheduling dashboard" names a solution rather than a customer problem.
- **Drift to avoid:** Perspective inversion: "Our team needs to ship faster" frames the product team's work, not the superintendent's experience.


##### Common Pitfalls

- **Jumping to Solutions in the Problem Frame:** Strip out any mention of products, features, tools, or technologies. Rewrite barriers as the customer's experienced friction: "But manual processes across disconnected systems create delays and errors."

- **Writing from the Product Team's Perspective:** Every stem must be written from the customer's point of view. The "I am" is the customer. The emotions in "Which makes me feel" are the customer's emotions. If the frame sounds like a project brief, the perspective has drifted.

- **Making the "But" Too Vague:** Name concrete, observable barriers. What specifically blocks the persona? What do they run into? What fails, breaks, or takes too long? "But manual data reconciliation across three disconnected systems creates weekly reporting delays of 2-3 days."

- **Skipping the Emotional Stem:** Write 2-3 specific emotions with context. "Frustrated" alone is not enough. "Frustrated by the gap between what leadership expects and what current tools allow, and anxious about being seen as ineffective" tells a story.

- **Conflating Constraints with Barriers:** Barriers go in "But" - these are things the persona runs into while trying to achieve their outcome. Constraints go in Context and Constraints - these are conditions the solution must operate within. A barrier is "manual processes create delays." A constraint is "the industry requires SOC 2 compliance."

- **Final Statement Does Not Match the Stems:** The final statement is a synthesis of the stems, not a rewrite. Every element in the statement should trace back to a stem. If the statement needs new information, update the stems first.

- **Defaulting to a Tech Role as the Persona:** Before writing "I am," confirm who actually uses or buys the product in the field. Most products serve people whose primary job is not writing code. A clinical data platform's customer is a clinical operations lead, not a data engineer.

- **Exceeding Template Capacity:** Respect the word budgets. "I am" is ~30-40 words. "Trying to" is ~15-20. "But" is ~20-25. "Because" is ~20-25. "Which makes me feel" is ~15-20. Context is ~30-40. Final statement is ~40-50. Write for the template field, not for the model's appetite for prose.

- **A Frame With No Evidence Under It:** Ask what evidence backs each stem. Mark any stem without evidence as a hypothesis, and route back to discovery before the decision point.

##### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-framing-the-problem) for supporting source material and expanded examples.


## Discover + Define


### Play 11: Exploring the Solution Space

Stable identifier: `psk-exploring-solution-space`.

#### psk-exploring-solution-space / Instructions

##### Purpose

Create a **Productside-style Exploring the Solution Space artifact** for your validated problem.

This skill is for the **Discover + Define** phase. It sits between problem framing and solution hypothesis. The PM has a validated problem statement and needs to come up with a few solution hypotheses to test quickly and cheaply before committing to one direction.

This is a **process skill**, not a content-fill skill. It covers session preparation:

1. **Plan** - define session goals, participants, and resources
2. **Select** - choose ideation methods from the Productside catalog, with at least one from each activity category
3. **Prepare** - produce a session plan the PM can take into the room

The agent helps prepare the session. The actual ideation session happens with the team in real time. The agent cannot substitute for cross-functional collaboration in a design thinking workshop.

Use this skill when you need to:

- explore solution possibilities for a validated problem statement
- plan a design thinking session with the right participants and methods
- select appropriate ideation tools from the Productside catalog
- ensure the session covers divergent thinking, convergent thinking, and testing
- prepare participants and resources for a productive session

This is not a solution-generation tool. The agent does not brainstorm solutions on behalf of the team. It helps the PM plan a structured session where the team generates, prioritizes, and tests ideas together.

###### Usage Notes

- This is a **process skill** (`type: process`). The agent helps prepare a design thinking session; the actual ideation happens with the team in real time.
- Evidence gathering: this skill qualifies for **artifacts only**. The PM brings the validated problem statement, stakeholder alignment, and prior discovery work. No web research needed.
- The method catalog contains 10 tools from the Productside playbook organized across three activity types: Generating Ideas, Prioritizing Ideas, and Testing. A well-planned session includes at least one from each category.
- Upstream: psk-framing-the-problem (validated problem statement is required input), psk-empathy-interviews, psk-proto-persona, psk-jobs-to-be-done.
- Downstream: Solution Hypothesis Statement (the top idea from this session feeds the hypothesis).

##### Key Concepts

###### The Three Activity Types

The Productside catalog organizes ideation methods into three categories. A well-planned session should include at least one method from each:

**Generating Ideas** (divergent thinking) - tools that expand the possibility space. The goal is volume, not quality. Judgment is suspended.

**Prioritizing Ideas** (convergent thinking) - tools that narrow the field. The team evaluates generated ideas against criteria and selects the most promising candidates.

**Testing** (validation) - tools that expose ideas to customer reality before the team commits resources.

Skipping any category creates a gap. Generating without prioritizing produces an unmanageable list. Prioritizing without generating limits the solution space prematurely. Neither without testing means the team commits to untested assumptions.

###### The 10 Methods

These methods come directly from the Productside playbook. Brief descriptions for each:

**Generating Ideas methods:**

1. **How Might We?** - Reframe problem statements as open-ended questions that invite creative solutions. "How might we help fleet managers detect vehicle issues before they cause breakdowns?" Opens the door to multiple solution paths instead of jumping to one.

2. **"Bad Ideas" First Brainstorming** - Start by deliberately generating terrible, impractical, or absurd solutions. This loosens creative inhibition and often reveals interesting inversions. "What if we made drivers diagnose their own engine problems?" might lead to a useful self-diagnostic concept.

3. **Quantity Over Quality** - Set a target number of ideas (e.g., 50 in 15 minutes) and race to hit it. No evaluation, no discussion, just volume. Quality comes later during prioritization.

4. **Mind Mapping** - Start with the core problem at the center and branch outward. Each branch represents a different angle or sub-problem. Connections between branches often reveal non-obvious solution approaches.

**Prioritizing Ideas methods:**

5. **2x2 Matrix** - Plot ideas on two axes (commonly Impact vs. Effort, or Desirability vs. Feasibility). Ideas in the high-impact, low-effort quadrant are strong candidates. Forces evaluation against concrete criteria rather than gut feel.

6. **Dot Voting** - Each participant gets a fixed number of votes (dots) to allocate across ideas. Simple, fast, democratic. Reveals where the team's collective energy concentrates.

7. **Money Voting** - Like dot voting but with fake currency (e.g., $100 per participant). Participants can spread money across ideas or concentrate it. Forces explicit trade-off thinking that dot voting does not.

**Generating + Prioritizing methods:**

8. **6-3-5 Method** - Six people, three ideas each, five rounds. Each person writes three ideas, passes the paper, and the next person builds on them. Combines generation with iterative refinement. Good for teams where vocal members dominate verbal brainstorming.

9. **SCAMPER** - Systematic creativity prompt: Substitute, Combine, Adapt, Modify/Magnify, Put to other uses, Eliminate, Reverse/Rearrange. Apply each lens to an existing solution or concept to generate variations.

**Testing methods:**

10. **Prototyping** - Build a quick, low-fidelity version (paper prototype, clickable wireframe, role-play scenario) to test with real users before committing to development.

11. **Customer Journey Maps** - Map the customer's experience across touchpoints to identify where a solution idea would actually fit into their workflow. Tests whether the solution addresses the right moment in the customer's journey. (Also serves as a generating tool by revealing gaps the team had not considered.)

###### Design Thinking Principles

From the Productside overview, four principles anchor this work:

- **User-Centered Approach** - Solutions must serve the customer, not the technology or the team's assumptions
- **Iterative Process** - The first idea is rarely the best; plan for multiple rounds of generation and refinement
- **Collaboration** - Diverse perspectives produce stronger solutions; include design, engineering, customer-facing roles, and (when possible) customers
- **Creativity** - Structured methods help unlock creative thinking in teams that default to analytical problem-solving

###### Scope the How Might We Questions

The PM drafts **three to five How Might We questions** before the session, each tracing back to the validated problem statement. Then test each one for scope:

- **Too broad** leaves a universe of unrelated solutions.
- **Too narrow** strangles the room, or names a solution inside the question.
- **Just right** leaves room for creativity and imagination without wandering away from the persona's need.

If a solution is hiding in the wording, point at the word and have the PM cut it. A good How Might We opens the space without choosing what goes in it. The questions that pass become the spine of the brainstorm.

###### Protect Divergence

Engineers tend to kill ideas on feasibility before any exist. Set rules that protect the generating phase (quantity over quality, no judgment while generating) and keep the session **safe, engaging, and fun**. The goal is a high quantity of ideas in a safe space, then a prioritized shortlist. Rehearse the hard moments before the session: the room goes quiet, one person dominates, someone shoots down every idea.

###### After the Session: Make the Case

Once the team has prioritized, the PM writes the case for the highest-priority solution **in their own words**:

- **Benefits** for the persona, tied to the specific problem. Generic benefits don't count.
- **Risks**, looked at widely: adoption, dependencies, and the business.
- **Value chain:** how the solution creates value for the customer, and how that customer value returns to the business as progress on a business outcome. Watch for where the chain breaks: customer value that never reaches the business, or a business benefit with no customer value beneath it.

If the PM can't articulate these, that is a signal they don't understand the solution yet. The summary feeds the Solution Hypothesis Statement.

###### This Step vs. Solution Hypothesis

Exploring the Solution Space generates multiple options. The Solution Hypothesis Statement (the next step) commits to one. This step is deliberately divergent, then convergent, then tested. The Solution Hypothesis step takes the winning idea and frames it as a testable hypothesis with clear success criteria.

Do not collapse these two steps into one. The team needs space to explore before committing.

###### How AI Supports This Play

The Playbook casts AI as a **preparation coach before the session and a critic after it**. Before, it sharpens the How Might We questions the PM drafted and helps the PM prepare to run a room of engineers who would rather kill ideas than consider them. After the room produces a prioritized set of hypotheses, AI challenges each one on value, viability, and feasibility, so the shortlist survives scrutiny, not just enthusiasm.

The ideas belong to the team in the session, never to a model beforehand. Which question to ask, who is in the room, and which hypotheses are worth testing all stay with the PM and their stakeholders. AI questions and challenges; the team judges.

- **Use it when:** there is a validated problem statement, and the PM wants to scope How Might We questions, plan the session, or stress-test what the session produced.
- **Avoid it when:** there is no validated problem yet, or the request is to generate the solutions the team should create together. Redirect to planning the session (Pitfall 4). **This holds even when the PM asks directly, and even in Discovery mode:** do not produce a list of solution ideas. The ideas are the one output this Play reserves for the team in the room.
- **Return:** How Might We questions tested for scope, a session plan built for quantity, safety, and engagement, and each prioritized hypothesis challenged on value, viability, and feasibility, with the judgment left to the team.

###### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

###### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

##### Application

Use [Template](playbook-skills.md#psk-exploring-solution-space--template) for the full scaffold.


###### Required Output Convention

This skill produces a **session plan** artifact. The session plan includes:

- Session goals and objectives tied to the validated problem statement
- Participant list with roles and rationale for inclusion
- Resources needed (tools, space, time)
- Selected methods with rationale for each selection
- Usage guidance for each selected method
- Session notes (timing, preparation for participants, follow-up actions)

###### Step 1: Confirm the Product Context and Validate Problem Statement

Before writing anything, answer:

- What product or service are we talking about?
- Who is the target customer?
- What is the validated problem statement?

If the PM does not have a validated problem statement, stop. This skill requires one as input. Direct the PM to psk-framing-the-problem first.

**Guard against tech-role bias.** When the PM identifies session participants, check that the list is cross-functional. If the participant list is only engineers or only technical roles, flag it. Design thinking sessions need diverse perspectives: design, product, engineering, customer success, sales, and (when feasible) actual customers. The PM building a logistics platform should include logistics coordinators in the session, not only backend engineers.

###### Step 2: Gather Evidence (Artifacts Only)

This skill uses **artifacts only** for evidence gathering. No web research is needed.

Ask whether the PM has materials to share:

- Validated problem statement (required)
- Stakeholder alignment document (helps determine participants)
- Prior discovery artifacts (empathy interview findings, JTBD output, persona work, problem identification output)
- Any previous brainstorming or solution exploration work

The validated problem statement is required. All other artifacts are helpful but optional.

###### Step 3: Define Session Goals and Objectives

Help the PM articulate clear goals for the session. Goals should be:

- Specific to the validated problem statement (not generic "brainstorm solutions")
- Measurable enough to know if the session succeeded (e.g., "generate at least 15 solution ideas and narrow to 3 candidates")
- Achievable within the planned session time

Example goal: "Using design thinking methods, ideate solution possibilities for our problem statement: [specific problem statement]. Generate at least 15 candidate ideas, prioritize to 3, and paper-prototype the top candidate."

###### Step 4: Scope the How Might We Questions

Ask the PM to draft three to five How Might We questions from the problem statement before you suggest anything. Then work through them one at a time (mirrors the critique guidance in this Play):

1. Say whether the question is too broad, too narrow, or just right, and why.
2. If a solution hides in the wording, point at the word and ask the PM to cut it.
3. Check it still traces to the problem statement, not a new problem.
4. Ask the PM what kinds of ideas the question would invite, so they can hear its scope.

The PM fixes each question. Offer suggestions as options to review and edit, never as replacements. Commit the questions that pass.

###### Step 5: Determine Participants

Help the PM identify who should attend the session. Key considerations:

- Review the stakeholder alignment document if available
- Include cross-functional representation (product, design, engineering, customer-facing roles)
- Include someone who has direct customer contact or customer evidence
- Keep the group small enough for productive collaboration (5-8 people is the sweet spot)
- Assign a facilitator (the PM or a designee) and a note-taker

For each participant, note their role and what perspective they bring to the session.

###### Step 6: Identify Session Resources

Help the PM plan the practical logistics:

- **Collaboration tools**: Mural, Miro, FigJam, physical whiteboard, sticky notes
- **Meeting setup**: Video conferencing with recording option, or in-person room
- **Time allocation**: Minimum 90 minutes for a single-method session; 2-3 hours for a multi-method session
- **Pre-work**: What participants need to review before the session (problem statement, discovery findings)
- **Documentation**: How outcomes will be captured and shared after the session

###### Step 7: Select Ideation Methods from the Catalog

Recommend methods based on the session goals, team size, and available time. Key rules:

- **Select at least one method from each of the three activity types** (Generating, Prioritizing, Testing)
- **3-4 methods is the sweet spot** for a single session; more than 4 is too many to execute well
- **Sequence matters**: Generate first, then prioritize, then test. Do not reverse the order.

Ask the PM what each method should produce before they commit to it, and make them justify each choice. Build the plan with them rather than setting the agenda for them (mirrors the critique guidance in this Play).

For each selected method, provide:

- Why it fits this session (connection to the problem, team dynamics, time available)
- How to run it (brief facilitation guidance)
- Expected output (what the team produces)
- Time needed (rough estimate)

###### Step 8: Provide Method Usage Guidance

For each selected method, give the PM enough facilitation guidance to run it:

- Setup instructions (what to prepare before starting)
- Step-by-step facilitation flow
- Timing for each phase
- Common facilitation mistakes to avoid
- How the output feeds the next method in the sequence

Then set the **ground rules that protect divergence** (quantity over quality, no judgment while generating), walk the session as a timeline, and ask how the PM will keep it safe, engaging, and fun. **Rehearse the hard moments:** what the PM will do when the room goes quiet, when one person dominates, and when someone shoots down every idea.

###### Step 9: Add Session Notes

Help the PM document practical considerations:

- Total session duration and timing for each method
- Whether multiple sessions are needed (if more than 3-4 methods are selected, split across sessions)
- Pre-session preparation for participants (what to read, what to bring)
- Post-session follow-up (how to document outcomes, who reviews the results)
- How session outcomes feed into the Solution Hypothesis Statement step

###### Step 10: Review the Session Plan for Completeness

Before finalizing, check:

- Does the plan reference the specific validated problem statement?
- Are session goals specific enough to evaluate success?
- Is the participant list cross-functional (not engineering-only)?
- Are at least three activity types covered (Generating, Prioritizing, Testing)?
- Is the time allocation realistic for the number of methods selected?
- Are resources and logistics documented?
- Is there a plan for capturing and sharing outcomes?

###### Step 11: After the Session, Sharpen the Case

When the PM returns with the team's prioritized solutions, help them build the case for the highest-priority one (mirrors the critique guidance in this Play). Do not write the benefits, name the risks, or compose the value story. Make the PM articulate each, then reflect back what is thin, missing, or disconnected:

1. **Benefits:** ask what the solution does for the persona, tied to the specific problem. Point at any benefit that is generic or disconnected.
2. **Risks:** ask what risks the PM sees. After they answer, ask questions that test whether they looked widely enough (adoption, dependencies, the business) without naming a risk yourself.
3. **Value:** have the PM trace customer value to business value, and show where the chain breaks.
4. **Challenge the shortlist** on value, viability, and feasibility if the PM asks. Question it; the team judges it.
5. **Pull it into a solution summary** in the PM's words: the input to psk-solution-hypothesis.

Do not invent customer reactions or business numbers.

###### Step 12: Offer Next Steps

After the session plan is complete, offer the PM up to three next-step options:

1. **Run the session** - take the plan into the room and facilitate the design thinking session with the team
2. **Move to Solution Hypothesis** - after the session and the solution case (Step 11), craft a Solution Hypothesis Statement using psk-solution-hypothesis
3. **Revisit the problem statement** - if the evidence is thin, revisit psk-framing-the-problem before entering the solution space

Present these as options, not mandatory steps. The PM decides what comes next.

#### psk-exploring-solution-space / Template

###### When to Use This

Use this template during **Discover + Define** when you have a validated problem statement and need to plan a design thinking session to explore solution possibilities. This is a process skill for session preparation, not a solution-generation exercise.

Upstream work that feeds this template: validated problem statement (from psk-framing-the-problem), stakeholder alignment, empathy interview findings, proto-persona, jobs-to-be-done.

###### Template

###### Session Plan

```markdown
# Exploring the Solution Space: Session Plan

## Product Context

- Product or service:
- Target market segment:
- Target customer (the person the product serves):

## Validated Problem Statement

Paste the validated problem statement here. If you do not have one, stop and use psk-framing-the-problem first.

> Quality check: Is this a specific, validated problem statement, not a vague "customers struggle with X"?
> Quality check: Is the problem stated from the customer's perspective, not the product team's?

## Session Parameters

### Goals and Objectives

What should this session accomplish? Tie goals to the problem statement.

1.
2.
3.

> Quality check: Are goals specific enough to evaluate whether the session succeeded?
> Quality check: Do goals reference the validated problem statement, not a generic "brainstorm solutions"?
> Quality check: Do goals include a measurable outcome (e.g., "generate at least 15 ideas and narrow to 3")?

### How Might We Questions

Draft three to five yourself. Each must trace back to the validated problem statement.

| # | How Might We... | Scope (too broad / too narrow / just right) | Traces to problem? |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

> Quality check: Is any solution hiding in the wording? Cut it.
> Quality check: Does each question open the space without choosing what goes in it?

### Ground Rules and Hard Moments

- Rules that protect divergence (e.g. quantity over quality, no judgment while generating):
- How we keep it safe, engaging, and fun:
- If the room goes quiet:
- If one person dominates:
- If someone shoots down every idea:

### Participants

Who should attend? Include cross-functional representation.

| Name / Role | Function | Perspective They Bring |
|-------------|----------|----------------------|
| | | |
| | | |
| | | |
| | | |
| | | |

> Quality check: Is the list cross-functional (not only engineers or only technical roles)?
> Quality check: Is someone with direct customer contact or customer evidence included?
> Quality check: Is there a designated facilitator and a note-taker?
> Quality check: Is the group between 5-8 people? Fewer limits diversity; more limits participation.

### Session Resources Needed

- Collaboration tool:
- Meeting setup:
- Time allocated:
- Pre-work for participants:
- Documentation plan:

> Quality check: Is the time allocation realistic for the number of methods selected (minimum 90 min for single-method, 2-3 hours for multi-method)?
> Quality check: Is there a plan for how participants should prepare?

### Notes

- Session timing considerations:
- Multiple sessions needed? (If more than 3-4 methods, split across sessions)
- Post-session follow-up plan:

## Method Selection

Select 3-4 methods from the catalog below. Choose at least one from each activity type.

### Productside Method Catalog

Mark selected methods. For each selected method, add rationale below.

| # | Method | Activity Type | Selected? |
|---|--------|--------------|-----------|
| 1 | How Might We? | Generating Ideas | [ ] |
| 2 | "Bad Ideas" First Brainstorming | Generating Ideas | [ ] |
| 3 | Quantity Over Quality | Generating Ideas | [ ] |
| 4 | Mind Mapping | Generating Ideas | [ ] |
| 5 | 2x2 Matrix | Prioritizing Ideas | [ ] |
| 6 | Dot Voting | Prioritizing Ideas | [ ] |
| 7 | Money Voting | Prioritizing Ideas | [ ] |
| 8 | 6-3-5 Method | Generating + Prioritizing | [ ] |
| 9 | SCAMPER | Generating + Prioritizing | [ ] |
| 10 | Prototyping | Testing | [ ] |
| 11 | Customer Journey Maps | Generating + Testing | [ ] |

> Quality check: Is at least one Generating method selected?
> Quality check: Is at least one Prioritizing method selected?
> Quality check: Is at least one Testing method selected?
> Quality check: Are 3-4 methods selected total? More than 4 in one session is too many.
> Quality check: Are methods sequenced correctly (Generate first, then Prioritize, then Test)?

### Selected Method Details

For each selected method, fill in the details below. Copy this block for each method.

#### Method: [Name]

- **Activity type:** [Generating / Prioritizing / Testing]
- **Why this method fits this session:**
- **Time needed:** [estimate in minutes]
- **Setup instructions:**
- **Facilitation flow:**
  1.
  2.
  3.
- **Expected output:**
- **Common facilitation mistakes to avoid:**
- **How the output feeds the next method:**

> Quality check: Does the facilitation flow include clear time limits for each phase?
> Quality check: Is the expected output concrete enough to feed the next method or the Solution Hypothesis step?
> Capacity check: Setup instructions ~20-30 words. Facilitation flow steps ~10-15 words each.
```

###### Post-Session Documentation

```markdown
# Session Outcomes

## Session Context

- Date:
- Duration:
- Facilitator:
- Participants:
- Problem statement addressed:

## Ideas Generated

List all ideas generated during the session (even the ones that were not prioritized).

| # | Idea | Source Method |
|---|------|-------------|
| 1 | | |
| 2 | | |
| 3 | | |

## Prioritized Ideas

Which ideas rose to the top during prioritization? Include the rationale.

| Rank | Idea | Why It Rose to the Top |
|------|------|----------------------|
| 1 | | |
| 2 | | |
| 3 | | |

> Quality check: Does the rationale connect back to the validated problem statement?
> Quality check: Are the top ideas feasible enough to prototype or test?

## Testing Observations

If prototyping or journey mapping was conducted, document what was learned.

-
-
-

## Solution Case (highest-priority solution, in the PM's own words)

- Solution:
- Benefits for the persona (tied to the problem):
- Risks (adoption, dependencies, business):
- Customer value:
- How customer value returns to the business (which business outcome):

> Quality check: Is any benefit generic, or disconnected from the problem?
> Quality check: Where could the value chain break?

## Next Steps

- [ ] Document and share session outcomes with stakeholders not in the room
- [ ] Select the top candidate for Solution Hypothesis Statement (psk-solution-hypothesis)
- [ ] Plan follow-up session if needed
- [ ] Schedule prototype testing with real customers if applicable
```

###### Usage Guidance

###### Session Flow

A typical session follows this sequence:

1. **Open (10 min)** - Facilitator reviews the problem statement and session goals. Participants align on what they are solving.
2. **Generate (30-45 min)** - Run one or two generating methods. Focus on volume and creativity.
3. **Prioritize (20-30 min)** - Run a prioritization method. Narrow the field to 3-5 candidates.
4. **Test (30-45 min)** - Run a testing method on the top candidates. Expose ideas to customer reality.
5. **Close (15 min)** - Document top ideas, prioritization rationale, and next steps.

###### How Many Methods

Select 3-4 methods for a single session:

- 1-2 Generating methods (if using two, keep total generating time under 45 minutes)
- 1 Prioritizing method
- 1 Testing method

If more methods are needed, plan a second session rather than cramming. Depth produces better ideas than breadth.

###### Time Budgets

| Session Type | Duration | Methods | Guidance |
|-------------|----------|---------|----------|
| Focused | 90 min | 3 methods | One generating, one prioritizing, one testing |
| Standard | 2 hours | 3-4 methods | Two generating, one prioritizing, one testing |
| Extended | 3 hours | 4 methods + breaks | Full cycle with deeper exploration |

###### Connecting to Other Skills

- **Upstream:** psk-framing-the-problem (validated problem statement is required input), psk-empathy-interviews (customer evidence grounds the session), psk-proto-persona (persona context), psk-jobs-to-be-done (jobs and outcomes to solve for)
- **Downstream:** The top idea from this session feeds into the Solution Hypothesis Statement

###### Capacity Reference

| Field | Word Budget | Guidance |
|-------|-------------|----------|
| Session Goal | ~15-25 | Specific, tied to problem statement |
| Method Rationale | ~15-25 | Why this method fits this session |
| Setup Instructions | ~20-30 | What to prepare before starting |
| Facilitation Step | ~10-15 | Clear, actionable instruction |
| Idea Description | ~10-15 | Concrete enough to evaluate |
| Prioritization Rationale | ~15-20 | Why this idea rose to the top |

#### psk-exploring-solution-space / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For a fleet manager facing unexpected breakdowns, frame a How Might We question, choose an ideation method, and plan the team session before comparing ideas.
- **Weak:** A session plan that begins with a chosen predictive-maintenance feature skips exploration.
- **Drift to avoid:** Agent substitutes for the room: an AI-generated solution list is an explicitly requested draft, not evidence of team ideation or agreement.


##### Common Pitfalls

- **Skipping the Problem Statement:** Require the validated problem statement as input. If the PM cannot state the problem clearly, redirect to psk-framing-the-problem before planning a solution space session.

- **Inviting Only Engineers:** Check the participant list for cross-functional diversity. Flag if design, customer-facing roles, or domain experts are missing. A logistics platform PM should have logistics professionals in the session, not only backend developers.

- **Selecting Only Divergent Methods:** Require at least one method from each activity type. If the PM selects only Generating methods, explicitly ask: "How will you prioritize these ideas? How will you test the top candidates before committing?"

- **Treating the Agent as a Substitute for the Team Session:** Redirect the PM to session planning. The agent's job is to help prepare a productive session, not to replace it. The team generates the ideas; the agent helps structure the process.

- **Making Session Goals Too Vague:** Tie goals to the specific problem statement and include measurable outcomes: "Generate at least 15 solution ideas for [problem], prioritize to 3 candidates, and paper-prototype the top candidate."

- **Not Allocating Enough Time:** Budget minimum 90 minutes for a single-method session. Multi-method sessions need 2-3 hours. If the calendar does not allow it, split across multiple sessions rather than cramming everything into one.

- **Selecting Too Many Methods:** Limit to 3-4 methods per session. If more methods are needed, plan a second session. Depth beats breadth in ideation.

- **Forgetting to Document Session Outcomes:** Assign a note-taker during the session. Plan 15 minutes at the end for documenting the top ideas, prioritization rationale, and agreed next steps. The session outcomes should be structured enough to feed the Solution Hypothesis step.

- **AI Ranks the Solutions for You:** Prioritize in the room with the catalog's prioritizing methods (Dot Voting, Money Voting, Value vs. Effort). Afterward, the agent may challenge each shortlisted hypothesis on value, viability, and feasibility. The team decides.

- **A How Might We That Is Too Broad, Too Narrow, or Hiding a Solution:** Draft three to five, test each for scope, cut any solution word, and check each traces to the problem statement.

- **A Shortlist Nobody Can Defend:** Before moving on, the PM writes the case in their own words (Step 11): benefits tied to the problem, risks looked at widely, and the value chain from customer to business.

##### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-exploring-solution-space) for supporting source material and expanded examples.


### Play 12: Solution Hypothesis

Stable identifier: `psk-solution-hypothesis`.

#### psk-solution-hypothesis / Instructions

##### Purpose

Create a **Productside-style Solution Hypothesis Statement artifact** that documents a proposed solution, its benefits and risks, and produces two linked If/Then hypothesis statements.

This skill is for the **Discover + Define** phase. It sits directly downstream of Framing the Problem and Exploring the Solution Space. The PM has validated a problem and explored possible solutions; now they are expressing their chosen solution as a testable hypothesis.

This is a synthesis and articulation skill. It pulls together findings from:

- problem framing (psk-framing-the-problem)
- solution space exploration (psk-exploring-solution-space)
- positioning work (psk-positioning-statement), if available

The output is a five-section artifact: problem statement (imported from upstream), solution summary, solution benefits, risks and assumptions, and a two-column solution hypothesis statement. This artifact is what the PM uses to communicate a testable solution direction to leadership and to justify resource allocation through gate review processes.

Use this skill when you need to:

- express a proposed solution as a testable If/Then hypothesis
- separate customer value from business outcome in a structured format
- document benefits and risks before committing to a solution direction
- create a reviewable artifact for leadership or gate review processes

This is not a PRD or feature specification. If the output reads like a requirements document or a feature list, the hypothesis has drifted into implementation territory.

###### Usage Notes

- The template produces a single artifact with five sections: Problem Statement (imported), Solution Summary, Solution Benefits, Risks and Assumptions, and Solution Hypothesis Statement (two-column If/Then).
- Two hypothesis statements are required, not one: customer-focused (IF solution THEN customer benefit) and business-focused (IF customer benefit THEN business outcome). The THEN of the first becomes the IF of the second.
- Evidence gathering is **artifacts only** - no web research offered. This skill synthesizes the PM's problem framing and solution exploration work.
- Upstream: psk-framing-the-problem, psk-exploring-solution-space, psk-positioning-statement.
- Downstream: lo-fi experimentation, risk assessment, roadmap planning, outcome tree alignment.

##### Key Concepts

###### The If/Then Structure Is the Core Format

A solution hypothesis is not a description of what to build. It is a testable statement: **IF** we do X, **THEN** Y happens. This format forces the PM to connect the solution to an expected outcome, which is the first step toward validation.

A solution summary says "what." A hypothesis says "if we do this, then this result follows." The difference matters because summaries cannot be tested, but hypotheses can.

If you are not sure where to start, write the simplest possible If-then statement and work from there. Precision comes in later iterations.

###### Two Hypotheses, Not One

The Productside format requires two linked hypothesis statements:

1. **Customer-focused:** IF we [provide this solution], THEN [customers experience this benefit]
2. **Business-focused:** IF we [achieve that customer benefit], THEN [we reach this business outcome]

The THEN of the customer-focused hypothesis becomes the IF of the business-focused hypothesis. This chain ensures the PM has thought through both sides: why the customer cares and why the business cares.

If there is only one hypothesis that mixes customer and business language, the chain is broken. Separate them.

###### The Five Sections Have a Specific Flow

The artifact builds in a deliberate sequence:

1. **Problem Statement** carries forward from psk-framing-the-problem. It is imported, not rewritten.
2. **Solution Summary** describes the proposed solution in one paragraph.
3. **Solution Benefits** lists 3-5 specific benefits for the customer and the business.
4. **Risks and Assumptions** lists 3-5 specific risks or assumptions that need validation.
5. **Solution Hypothesis Statement** presents the two-column If/Then output.

Each section feeds the next. The problem grounds the solution. The solution grounds the benefits. The benefits and risks inform the hypothesis. The hypothesis is the synthesis of everything above it.

###### Solution Benefits Are Not Features

A benefit is the outcome the customer or business experiences. A feature is what the product does. "Automated workflow engine" is a feature. "Time saved on manual data entry, freeing specialists to focus on strategic work" is a benefit.

Benefits should answer: so what? If the benefit reads like a capability description, push it one level further to the outcome.

###### Risks and Assumptions Are Specific and Testable

Good risks name concrete failure modes: "Technical integration with legacy HRIS systems may require custom middleware." Bad risks name vague worries: "Things might not work as planned."

Assumptions are things the team believes to be true but has not yet validated. Surfacing them here prepares the PM for the validation work that follows the hypothesis.

###### Connection to the Outcome Tree

The business outcome in the second hypothesis should align with an outcome in the Outcome Tree (if one exists). If the PM has done outcome tree work, the business-focused hypothesis should reference one of the identified business success metrics. This creates traceability from problem to solution to measurable result.

###### Product Outcomes Use Role Names, Not Persona Names

When writing benefits, outcomes, and hypothesis statements, refer to roles ("HR specialists," "clinical operations leads," "field engineers") rather than individual persona names ("Henry," "Maya"). Role names keep the hypothesis generalizable across the target population.

###### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **critic of the solution hypothesis the PM drafted**. It checks the If/Then format, tests whether the customer-focused hypothesis chains into the business-focused one, flags features posing as benefits, and asks whether each risk and assumption is specific enough to test. The solution and the bet stay the PM's.

- **Use it when:** the PM has a validated problem statement and a prioritized solution, and has drafted the hypothesis.
- **Avoid it when:** there is no validated problem statement. A hypothesis about an unframed problem has nothing to test against.
- **Return:** the If/Then chain tested link by link, benefits separated from features, risks and assumptions sharpened into things a test could settle, and proposed rewrites for the PM to accept, adapt, or reject.

###### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

###### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

##### Application

Use [Template](playbook-skills.md#psk-solution-hypothesis--template) for the full scaffold.


###### Required Output Convention

Default to a **clean, paste-ready solution hypothesis artifact**.

That means:

- fill all five sections in order
- keep each section within its word budget (see Capacity Reference below)
- produce two hypothesis statements that chain together correctly
- explanation belongs below the artifact, not inside the template fields
- the artifact comes first; commentary is secondary

###### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses Discovery mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

###### Step 1: Confirm the Product and Customer Context

Before writing anything, answer:

- what product or service is the PM building?
- who is the customer whose problem is being solved?
- what prior work exists (problem statement, solution exploration, positioning)?

If you cannot identify a specific customer, stop and resolve the target first.

**Guard against tech-role bias.** The solution should serve the actual customer, not default to building developer tools. A clinical data platform's solution hypothesis should describe value for clinical operations leads, not data engineers. An agricultural supply chain tool should describe value for farm operations managers, not software developers. Before writing the solution summary, confirm: does this solution serve the person who actually experiences the problem day-to-day?

###### Step 2: Gather Evidence Before Writing

Once you know the product and customer, offer the user materials to share before drafting:

**User-supplied artifacts** - ask whether the user has materials to ground the hypothesis: validated problem statement (from psk-framing-the-problem), solution space exploration output, positioning work, competitive analysis, or earlier skill outputs.

This skill is **artifacts only** - it synthesizes the PM's own problem framing and solution exploration. Web research is not offered because the hypothesis should flow from validated upstream work, not from external sources the PM has not yet verified.

If the user has no validated problem statement, surface the tension: a solution hypothesis without a validated problem is building on assumptions. Recommend completing psk-framing-the-problem first, but proceed if the user wants to draft an assumption-based hypothesis.

###### Step 3: Import or Confirm the Problem Statement

The problem statement comes from psk-framing-the-problem. It should be imported directly, not rewritten.

If the user provides a problem statement, place it in Section 1 as-is. If the user does not have one, help them draft a brief problem statement, but flag it as unvalidated.

The problem statement anchors everything that follows. If the problem is vague, the hypothesis will be vague.

###### Step 4: Write the Solution Summary

Describe the proposed solution in one paragraph. This should come from the user's solution exploration work or their stated direction.

The solution summary should be:

- specific enough to be testable (not "build a better platform")
- written as what the solution does for the customer, not a feature spec
- one paragraph, not a list of capabilities

Word budget: ~30-40 words.

###### Step 5: List Solution Benefits

List 3-5 specific benefits. Each benefit should state the positive outcome for the customer or the business.

Test each benefit: does it describe an outcome, or does it describe a feature? "Automated data entry" is a feature. "Time saved on manual data entry, allowing specialists to focus on strategic initiatives" is a benefit.

Mix customer benefits and business benefits. At least two should be customer-facing, at least one should be business-facing.

Word budget: ~5-10 words per benefit, 3-5 benefits.

###### Step 6: List Risks and Assumptions

List 3-5 specific risks or assumptions that need to be validated.

Each risk or assumption should be:

- specific (not "things might go wrong")
- testable (the team can investigate whether it is true)
- relevant to the proposed solution (not generic business risks)

Common categories: technical integration risk, adoption risk, change management risk, data quality risk, regulatory risk.

Word budget: ~5-10 words per risk, 3-5 risks.

###### Step 7: Write the Customer-Focused Hypothesis

Write the first hypothesis using the If/Then structure:

**IF** we [describe the solution in terms of what it provides to the customer], **THEN** [describe the specific benefit the customer experiences].

The IF should reference the solution summary. The THEN should reference one or more of the benefits listed above.

Use role names, not persona names. "We save HR specialists time" not "we save Henry time."

Word budget: ~30-40 words.

###### Step 8: Write the Business-Focused Hypothesis

Write the second hypothesis. The IF of this statement picks up where the customer-focused hypothesis left off:

**IF** we [achieve the customer benefit from hypothesis 1], **THEN** [describe the measurable business outcome].

The business outcome should be specific and measurable. "We will achieve our goal of improving onboarding time by 30%" is measurable. "We will do better" is not.

Word budget: ~30-40 words.

###### Step 9: Verify the Chain

Check that the two hypotheses link correctly:

- Does the THEN of hypothesis 1 connect logically to the IF of hypothesis 2?
- Does hypothesis 1 focus on customer value?
- Does hypothesis 2 focus on business outcome?
- Are both written as If/Then statements, not as descriptions?

If the chain breaks, revise until the handoff is clean.

###### Step 10: Review for Solution Language vs. Outcome Language

Scan the entire artifact:

- Does the solution summary describe what the solution does, not how it is built?
- Do benefits describe outcomes, not features?
- Do hypotheses connect solutions to outcomes, not solutions to more solutions?
- Are risks specific and testable, not generic worries?

###### Step 11: Offer Next Steps

After the artifact is complete, offer the user up to three next-step options:

1. **Design a lo-fi experiment** - test the hypothesis with a prototype, concierge MVP, or Wizard of Oz approach before committing to full build
2. **Conduct risk assessment** - prioritize and investigate the identified risks and assumptions
3. **Connect to the roadmap** - use the validated hypothesis to inform roadmap planning and resource allocation

Present these as options, not as mandatory steps. The user decides what comes next.

#### psk-solution-hypothesis / Template

###### When to Use This

Use this template during **Discover + Define** when you have a validated problem statement and have explored the solution space. You are ready to express your chosen solution direction as a testable hypothesis with expected customer and business outcomes.

Upstream work that feeds this template: framing the problem (psk-framing-the-problem), exploring the solution space (psk-exploring-solution-space), positioning statement (psk-positioning-statement, if available).

###### Template

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
> Capacity check: ~40-50 words (matching the final problem statement from psk-framing-the-problem).

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

###### Usage Guidance

###### Filling the Template

1. Start with **Product Context** to anchor who this is for and whose problem the solution addresses.
2. **Import the Problem Statement** from psk-framing-the-problem. Do not rewrite it.
3. Write the **Solution Summary** as one paragraph describing what the solution provides.
4. List **Solution Benefits** as outcomes, not features. Push each one past "what it does" to "why it matters."
5. List **Risks and Assumptions** with enough specificity that each one can be investigated.
6. Write the **Customer-Focused Hypothesis** first. Then write the **Business-Focused Hypothesis** using the THEN of the first as the IF of the second.
7. Verify the chain between the two hypotheses.
8. The **Evidence Notes** section is optional and trailing. Do not let it displace or delay the main artifact.

###### The Five Sections Build in Order

Do not skip ahead to writing hypotheses without completing the preceding sections. The problem statement grounds the solution. The solution grounds the benefits. The benefits and risks inform the hypothesis. Writing the hypothesis without the groundwork produces untethered speculation.

###### What Goes Where

| Section | Contains | Does NOT Contain |
|---------|----------|------------------|
| Problem Statement | Validated problem from upstream | New problem framing or solution language |
| Solution Summary | What the solution provides to customers | Implementation details, architecture, feature specs |
| Solution Benefits | Outcomes for customers and the business | Feature names, capability descriptions |
| Risks and Assumptions | Specific, testable failure modes or beliefs | Generic worries, vague concerns |
| Customer Hypothesis | IF solution THEN customer benefit | Business metrics, revenue targets |
| Business Hypothesis | IF customer benefit THEN business outcome | Feature lists, solution descriptions |

###### Connecting to Other Skills

- **Upstream:** psk-framing-the-problem provides the problem statement. psk-exploring-solution-space provides the chosen solution direction. psk-positioning-statement provides framing for how the solution fits the market.
- **Downstream:** The validated hypothesis drives lo-fi experimentation, risk assessment, and roadmap planning. The business outcome in hypothesis 2 should connect to the outcome tree if one exists.

###### Capacity Reference

See [Template and capacity guidance](playbook-skills.md#psk-solution-hypothesis--template) for the exact word and character budgets per field.

| Field | Word Budget | Guidance |
|-------|-------------|----------|
| Problem Statement | ~40-50 | Imported from psk-framing-the-problem |
| Solution Summary | ~30-40 | One paragraph, specific and testable |
| Solution Benefits | ~5-10 each | 3-5 outcome statements, not feature names |
| Risks and Assumptions | ~5-10 each | 3-5 specific, testable risks |
| Customer Hypothesis | ~30-40 | IF solution THEN customer benefit |
| Business Hypothesis | ~30-40 | IF customer benefit THEN business outcome |

#### psk-solution-hypothesis / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** If produce distributors receive earlier shipment-condition signals, then they can intervene before spoilage; if spoilage falls, then the business may improve margin. Define tests for both links.
- **Weak:** "Add tracking, alerts, and dashboards" lists features without predicting a testable change.
- **Drift to avoid:** Feature list as hypothesis: an If clause alone is insufficient. The Then clause must specify a customer or business result.


##### Common Pitfalls

- **Writing a Feature List Instead of an If/Then Hypothesis:** Rewrite as an If/Then statement. The IF describes the solution. The THEN describes the expected outcome for the customer or business. "IF we provide automated workflows that reduce manual data entry, THEN field engineers will complete inspections 40% faster."

- **Merging the Two Hypotheses into One:** Separate into two statements. The customer-focused hypothesis connects solution to customer benefit. The business-focused hypothesis connects customer benefit to business outcome. The THEN of the first becomes the IF of the second.

- **Making the Solution Summary Too Vague to Test:** The solution summary must be specific enough that someone could design a test for it. "Implement an integrated HR management system with automated task workflows, centralized employee records, and a self-service portal for common requests" is testable.

- **Listing Generic Risks:** Each risk should name a specific failure mode. "Resistance to change from employees accustomed to the current manual process" is specific. "Integration with the legacy HRIS may require custom middleware not in the current budget" is specific.

- **Starting Without a Validated Problem Statement:** Complete psk-framing-the-problem first. If that is not possible, at minimum draft a problem statement and flag it as unvalidated. The hypothesis artifact should make visible whether the problem foundation is solid or assumed.

- **Using Persona Names Instead of Role Names in the Hypothesis:** Use role names: "IF we save HR specialists time on manual tasks, THEN they will redirect effort to strategic initiatives like talent development and workforce planning."

- **Writing Benefits That Are Just Restated Features:** Push each benefit one level further. "Automated data entry" becomes "Time recovered from manual data entry, allowing specialists to focus on higher-value work." The feature is the mechanism; the benefit is the outcome the customer cares about.

- **Writing a Business-Focused Hypothesis with No Measurable Outcome:** The business outcome must include a specific metric or target: "THEN we will reduce new employee onboarding time by 30%" or "THEN we will increase field inspection completion rates from 60% to 85% per quarter."

- **AI Writes the Bet:** The PM drafts the chain; the skill tests each link. Rewrites come after the critique, as options.

##### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-solution-hypothesis) for supporting source material and expanded examples.


### Play 13: Positioning Statement

Stable identifier: `psk-positioning-statement`.

#### psk-positioning-statement / Instructions

##### Purpose

Create a **Productside-style Positioning Statement** for your product, service, or brand.

This skill is for the **Discover + Define** phase. It is where the PM crosses from investigation into definition. The positioning statement communicates the product's unique value in a way that aligns stakeholders, guides marketing, and filters product decisions.

With a positioning statement, a team can:

- Proactively choose target markets
- Promote competitive advantage
- Communicate benefits of the product
- Align marketing and product planning

Use this skill when you need to:

- articulate your product's unique value proposition in a structured, repeatable format
- align stakeholders on what the product is, who it serves, and how it differs
- create a filter for product development and marketing prioritization
- document competitive differentiation in outcome terms, not feature lists

Most Product Managers are working on a product that is already out in market. If that is your situation, find your product's existing positioning statement and see if adjustments are needed. If there is no existing positioning, you will craft one here.

###### Usage Notes

- The positioning statement uses the Productside seven-element formula: For / Who / The / Is a / That / Unlike / Our product gives. The order is fixed and all elements are required.
- The formula splits into two halves: Value Proposition (For through That) and Statement of Differentiation (Unlike, Our product gives).
- "That" must be a benefit (customer outcome), not a feature (product capability).
- "Unlike" must name a real competitive alternative, including status quo.
- "Our product gives" must use outcome language, not feature language.
- Upstream: psk-proto-persona (For element), psk-jobs-to-be-done (Who element), psk-problem-identification (need/opportunity).
- Downstream: solution hypothesis, product requirements, marketing messaging.
- This skill qualifies for both web research and user artifacts during evidence gathering.

##### Key Concepts

###### The Seven-Element Formula

The Productside positioning statement uses a fixed structure with seven elements. The order is required and the elements are non-negotiable:

**Value Proposition:**
- **For** [target customer]
- **Who** [statement of the need or opportunity]
- **The** [product name]
- **Is a** [product category]
- **That** [statement of key benefit]

**Statement of Differentiation:**
- **Unlike** [primary competitive alternative]
- **Our product gives** [statement of primary differentiation]

The first five elements establish the value proposition. The last two establish differentiation. Both halves are required.

###### Benefits Over Features

The "That" element is a benefit, not a feature list. A benefit describes the outcome the customer experiences. A feature describes what the product does.

- Feature: "provides real-time dashboards and automated alerts"
- Benefit: "gives more time back to the HR specialist for strategic projects"

If the "That" element reads like a feature spec, rewrite it as the outcome the customer cares about.

###### The "Unlike" Must Name a Real Alternative

The "Unlike" element must name the actual alternative the customer would choose if your product did not exist. This includes:

- a named competitor
- a category of competing products
- the status quo (manual processes, spreadsheets, existing workflows)
- doing nothing

It must not be a strawman - a weak or irrelevant competitor chosen to make differentiation easy. If the PM's strongest competitor is Salesforce, "Unlike" should not name a startup nobody has heard of.

###### Differentiation Must Be Outcome-Based

The "Our product gives" element must state what the customer gains in outcome terms, not what the product has in feature terms.

- Feature-based (wrong): "AI-powered analytics, real-time dashboards, and seamless integration"
- Outcome-based (right): "real-time data access, streamlined workflows and automates repetitive tasks"

The playbook example deliberately uses outcome language: the customer gets time back, gets streamlined workflows, gets automation of repetitive work. These are results, not specs.

###### Credibility Matters

The positioning statement must be believable and compatible with the company brand. Claims that sound like marketing hyperbole ("revolutionary," "world-class," "best-in-class") undermine the statement's utility as an internal alignment tool. If the team cannot defend the claim to a skeptical customer, it does not belong in the statement.

###### The Competitive Matrix Informs Positioning

The playbook pairs the positioning statement with a competitive matrix - a 2x2 grid where:

- The PM selects two of the strongest differentiating factors in their industry
- One factor is assigned to the X-axis, one to the Y-axis
- The PM's product and competitors are mapped on the grid
- The visual identifies positioning opportunity and white space

The competitive matrix is optional input for this skill. The PM may already understand their competitive landscape. But when competitive positioning is unclear, the matrix exercise helps surface the two dimensions that matter most before writing the statement.

###### One Persona, One Statement

Positioning is unique to a **segment and persona**. Write one statement for one persona, then rerun the exercise for each additional persona. A statement stretched to fit every segment speaks to none of them. If the product serves a user and a buyer, each gets their own statement.

###### The Claims Stay Yours

A statement can sound sharper than the evidence supports. Every claim in it (the need, the benefit, the differentiation) must be **relevant** to this persona's need, **credible** for this company, and **differentiated** enough to sway a purchase decision. Only customers and competitive research can confirm any of that. Competitor details that come from general knowledge, the agent's included, are leads to verify, not facts.

###### Positioning for Existing Products

Most PMs inherit a product that already has positioning - explicit or implicit. Before writing a new statement, find the existing one and evaluate whether it needs adjustment rather than replacement. Existing positioning lives in marketing sites, pitch decks, investor materials, and sales enablement docs.

Once the positioning statement is complete - whether newly crafted or refined - add it to the **Product Outcomes Canvas**. The canvas is where it lives as the messaging foundation for all downstream work.

###### How AI Supports This Play

The Playbook casts AI as a **critic of a draft the PM has already written**. It checks the statement against the Productside format, flags features posing as benefits, and challenges whether the differentiation holds up against the alternative the persona would actually choose. It proposes rewrites as options to react to, not replacements for the PM's words.

- **Use it when:** the PM has drafted a positioning statement for a specific segment and persona and wants it critiqued for benefits, relevance, credibility, and differentiation.
- **Avoid it when:** no target segment and persona has been chosen. AI will hand over polished positioning for a customer nobody has defined. Resolve the persona first (Step 1). If there is no draft, coach the PM to write one (see [Draft First, Then Critique](#draft-first-then-critique)).
- **Return:** features flagged where benefits belong, each claim tested for relevance, credibility, and differentiation, the alternative checked, and two or three proposed rewrites for the PM to accept, adapt, or reject.

###### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

###### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

##### Application

Use [Template](playbook-skills.md#psk-positioning-statement--template) for the full scaffold.


###### Required Output Convention

Default to a **clean, paste-ready positioning statement artifact**.

That means:

- fill all seven elements of the formula
- keep each element concise enough to fit the template fields (~10-20 words per element)
- the "That" element states a benefit, not a feature
- the "Unlike" element names a real alternative
- the "Our product gives" element uses outcome language
- explanation belongs below the artifact, not inside the formula fields

The artifact comes first. Commentary is secondary.

###### Draft First, Then Critique

**By default, the PM writes the statement and the skill critiques it.** If the PM has no draft, coach them through Steps 4-10 one element at a time. Explain what each element needs, ask them to write it, and critique what they write. If the PM asks you to draft the statement, or chooses Discovery mode, draft it and tag it `[AI-SUGGESTED, VALIDATE THIS]`, then run the same critique on your own draft.

###### If the PM Brings a Draft

Work through it one point at a time and wait for the PM's answers before rewriting (mirrors the critique guidance in this Play):

1. **Format:** is every element of the formula present?
2. **One persona:** if the statement could fit any customer, point at the words that make it generic.
3. **Features posing as benefits:** for each, ask what it does for the persona, and help restate it as an outcome they care about.
4. **Each claim:** relevant to this persona's need, credible for this company, differentiated enough to sway a purchase?
5. **The alternative:** using general knowledge of competitors and substitutes (including doing nothing or a manual workaround), did the PM name the alternative this persona would really choose, and does the differentiation hold up against it? Label anything you add about competitors as general knowledge to verify.
6. **Then propose two or three rewrites**, each explaining what it changes and why, for the PM to accept, adapt, or reject.

Keep the persona fixed. For another persona, run the critique again.

###### Step 1: Confirm the Product, Target Market, and Persona

Before writing anything, answer:

- what product or service are we positioning?
- who is the target market segment?
- who is the target customer within that segment? (user, buyer, or both)
- is there an existing positioning statement to evaluate first?

If you cannot answer those clearly, stop and resolve the target first.

**Guard against tech-role bias.** The "For" element names the customer - the person who uses or buys the product in the field. An IoT platform's customer is a fleet manager or logistics director, not a solutions architect. A clinical data platform's customer is a clinical operations lead, not a data engineer. Before writing the "For" element, confirm: does this person's primary job involve using the product's value, or are they the person who implements it technically?

###### Step 2: Gather Evidence Before Writing

Once you know the target, offer the user two things before drafting:

1. **Web research** - offer to search for the competitive landscape, how competitors position themselves, market category norms, and how practitioners in the target segment describe their needs. Look for competitor positioning pages, analyst reports, industry press, and practitioner forums. The goal is to understand what alternatives exist and how they are positioned, so the "Unlike" and "Our product gives" elements are grounded in reality.

2. **User-supplied artifacts** - ask whether the user has materials to share: existing positioning statements, competitive analysis, brand guidelines, pitch decks, marketing copy, prior discovery work, or any other material that would ground the statement in evidence.

Either, both, or neither is fine - the user decides. But always offer before drafting.

###### Step 3: Optionally Build a Competitive Matrix

If the PM needs help identifying their competitive landscape or finding the right differentiating dimensions, build a competitive matrix:

1. Identify 3-5 competitors (including status quo if relevant)
2. Brainstorm differentiating factors in the industry
3. Select the two strongest differentiating factors
4. Assign one to X-axis, one to Y-axis (both run Low to High)
5. Map the PM's product and competitors on the grid
6. Identify the positioning opportunity - where is the white space?

The matrix is optional. Skip it if the PM already knows their competitive position clearly.

###### Step 4: Fill "For" - Target Customer

Name the target customer in specific terms. This is the person who uses or buys the product in the field.

- Too broad: "businesses" or "enterprises"
- Too narrow: "Sarah, 34, in Omaha"
- Right level: "HR specialists managing high volumes of employee data and manual processes"

The "For" element should be specific enough that a reader can picture the person, but general enough to represent a segment, not an individual.

###### Step 5: Fill "Who" - Statement of Need or Opportunity

State the need or opportunity that the target customer faces. Use language from prior discovery work - jobs, pains, outcomes - not generic filler.

- Weak: "who want to be more efficient"
- Strong: "who need to reduce inefficiencies and focus on strategic HR initiatives"

If JTBD, proto-persona, or problem identification work exists, pull the need language from those artifacts. The "Who" element should feel like a direct echo of validated customer pain.

###### Step 6: Fill "The" - Product Name

Name the product. Use the actual product name the customer knows, not an internal code name or a generic category.

###### Step 7: Fill "Is a" - Product Category

Claim the product category. The category should be recognizable to the target customer - a label they would use when searching for solutions or describing the product to a colleague.

- Too broad: "a software platform"
- Too narrow: "a Python-based ETL pipeline with REST API support"
- Right level: "HR automation tool"

The category frames the customer's expectations. If they do not recognize the category, they will not understand the positioning.

###### Step 8: Fill "That" - Statement of Key Benefit

State the key benefit the customer receives. This is the single most important outcome - the reason the customer cares.

**This must be a benefit, not a feature.** A benefit describes what the customer gets. A feature describes what the product does.

- Feature (wrong): "provides automated workflows and real-time analytics"
- Benefit (right): "gives more time back to the HR specialist for strategic projects"

If the "That" element contains technical capabilities, architectural details, or feature descriptions, rewrite it as the customer outcome.

###### Step 9: Fill "Unlike" - Primary Competitive Alternative

Name the real competitive alternative. This is what the customer would do if your product did not exist.

**Hard constraint: the "Unlike" must name a real alternative.** This includes:

- a specific competitor by name
- a category of alternatives (e.g., "traditional manual processes and outdated systems")
- the status quo (e.g., "spreadsheet-based tracking and email coordination")

Do not use a strawman competitor. Do not name a competitor the target customer would never actually consider. The "Unlike" should make the reader think "yes, that is exactly what we are competing against."

###### Step 10: Fill "Our product gives" - Statement of Primary Differentiation

State what the customer gets from your product that they do not get from the alternative named in "Unlike."

**Hard constraint: differentiation must be in outcome terms, not feature terms.**

- Feature terms (wrong): "AI-powered analytics, real-time dashboards, and seamless integration"
- Outcome terms (right): "real-time data access, streamlined workflows and automates repetitive tasks"

The differentiation should pass this test: could the customer verify this claim from their own experience? "Real-time data access" is something a customer experiences. "AI-powered analytics" is something a product spec describes.

###### Step 11: Validate the Statement

Before finalizing, run the positioning statement through these checks from the playbook:

1. **Focused on benefits, not features?** - Does the "That" element describe what the customer gets, not what the product does?
2. **Relevant?** - Are the benefits relevant to the target customer's actual needs?
3. **Credible?** - Is the claim believable and compatible with the company brand?
4. **Differentiated and appealing?** - Does the statement offer clear, distinctive benefits that serve as a filter for purchasing decisions?

If any check fails, revise the specific element before finalizing. Propose revisions as options for the PM to accept, adapt, or reject, and say what each one changes.

###### Step 12: Keep the Artifact Compact

The canonical template uses labeled fields. Each element should be concise:

- "For": ~10-15 words
- "Who": ~10-15 words
- "The": ~3-5 words (product name)
- "Is a": ~3-5 words (category)
- "That": ~10-15 words
- "Unlike": ~8-12 words
- "Our product gives": ~15-20 words

If the output requires summarizing before it can be pasted into the playbook, it is too long.

###### Step 13: Offer Next Steps

After the artifact is complete, offer the user up to three next-step options:

1. **Add to the Product Outcomes Canvas** - the positioning statement belongs in the canvas as the messaging foundation for downstream plays; add it there so it is available to Go-to-Market, Key Messages, and any other play that references positioning
2. **Repeat for the next persona** - positioning is unique to a segment and persona; run the exercise again for each additional persona (e.g., the buyer as well as the user)
3. **Move to solution hypothesis** - use the positioning as input to define what the product must do to deliver on the promise

Present these as options, not as mandatory steps. The user decides what comes next.

#### psk-positioning-statement / Template

###### When to Use This

Use this template during **Discover + Define** to articulate your product's unique value proposition and differentiation. This is where you cross from investigation into definition - the positioning statement aligns stakeholders, guides marketing, and filters product decisions.

Most Product Managers are working on a product already in market. If that is your situation, find your product's existing positioning statement first and evaluate whether it needs adjustment.

###### Template

```markdown
# Positioning Statement

## Product Context

- Product or service:
- Target market segment:
- Primary user persona:
- Buyer persona (if different):
- Existing positioning (if any):

## 1. Competitive Matrix (optional)

Select two of the strongest differentiating factors in your industry.
Map your product and competitors on the grid to identify positioning opportunity.

| | Low [X-Axis Factor] | High [X-Axis Factor] |
|---|---|---|
| **High [Y-Axis Factor]** | [Competitor] | [Your Product / Competitor] |
| **Low [Y-Axis Factor]** | [Competitor] | [Competitor] |

- X-Axis differentiating factor:
- Y-Axis differentiating factor:
- Competitors mapped:
- Positioning opportunity identified:

## 2. Positioning Statement

### Value Proposition

**For** _______________________________________________
[target customer]

**Who** _______________________________________________
[statement of the need or opportunity]

**The** _______________________________________________
[product name]

**Is a** _______________________________________________
[product category]

**That** _______________________________________________
[statement of key benefit]

### Statement of Differentiation

**Unlike** _______________________________________________
[primary competitive alternative]

**Our product gives** _______________________________________________
[statement of primary differentiation]

> Quality check: Is the "That" element a benefit (what the customer gets), not a feature (what the product does)?
> Quality check: Does the "Unlike" name a REAL competitive alternative the customer would actually consider?
> Quality check: Is the "Our product gives" element stated in outcome terms, not feature terms?
> Quality check: Are claims credible and compatible with the company brand?
> Quality check: Would a skeptical customer find this believable?
> Quality check: Are there any empty adjectives (innovative, seamless, best-in-class, cutting-edge)?
> Capacity check: For ~10-15 words. Who ~10-15 words. The ~3-5 words. Is a ~3-5 words. That ~10-15 words. Unlike ~8-12 words. Our product gives ~15-20 words.

## Evidence Notes (optional)

- What is well-supported by evidence:
- What is still assumption:
- Recommended next validation steps:
```

###### Usage Guidance

###### Filling the Template

1. Start with **Product Context** to anchor who this is for and whether existing positioning exists.
2. Optionally fill the **Competitive Matrix** to identify differentiating dimensions and positioning opportunity. Skip if you already know your competitive landscape.
3. Fill the **Positioning Statement** elements in order - the seven elements are a fixed sequence. Do not reorder or skip elements.
4. Run the quality checks before finalizing.
5. The **Evidence Notes** section is optional and trailing. Do not let it displace or delay the main artifact.

###### The Seven Elements

The Productside formula has a fixed structure. Fill each element in order:

| Element | What It Is | Word Budget | Guidance |
|---------|-----------|-------------|----------|
| For | Target customer | ~10-15 | Specific enough to picture, general enough to represent a segment |
| Who | Need or opportunity | ~10-15 | Use language from validated discovery, not generic pain |
| The | Product name | ~3-5 | Actual product name the customer knows |
| Is a | Product category | ~3-5 | Category the customer would use when searching or describing |
| That | Key benefit | ~10-15 | Outcome the customer experiences, NOT a feature |
| Unlike | Competitive alternative | ~8-12 | Real alternative the customer would actually choose |
| Our product gives | Primary differentiation | ~15-20 | Outcome-based, NOT feature-based |

###### Hard Constraints

These are not suggestions - they are rules:

- **"That" must be a benefit.** If it describes what the product does instead of what the customer gets, rewrite it.
- **"Unlike" must name a real alternative.** No strawmen. Status quo counts as a real alternative.
- **"Our product gives" must use outcome language.** If it reads like a feature list, rewrite it as customer results.
- **No empty adjectives.** Strip out "innovative," "seamless," "best-in-class," "cutting-edge," and similar filler.

###### Connecting to Other Skills

- **Upstream:** Proto-persona (the "For" element should match), JTBD (the "Who" element should echo validated jobs and outcomes), Problem Identification (validated problems inform the need)
- **Downstream:** Solution hypothesis, product requirements, marketing messaging
- **Parallel:** The competitive matrix can inform or be informed by market sizing work

###### Capacity Reference

See [Template and capacity guidance](playbook-skills.md#psk-positioning-statement--template) for the exact word and character budgets per field.

| Field | Word Budget | Guidance |
|-------|-------------|----------|
| For (target customer) | ~10-15 | Specific role + context |
| Who (need/opportunity) | ~10-15 | Echo validated discovery language |
| The (product name) | ~3-5 | Actual product name |
| Is a (product category) | ~3-5 | Customer-recognizable category |
| That (key benefit) | ~10-15 | Outcome, not feature |
| Unlike (competitor) | ~8-12 | Real alternative |
| Our product gives (differentiation) | ~15-20 | Outcome-based differentiation |
| Competitive matrix X-axis | ~3-5 | Differentiating factor label |
| Competitive matrix Y-axis | ~3-5 | Differentiating factor label |

#### psk-positioning-statement / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For farm operations managers who need timely soil decisions, position the monitoring product around that benefit and a real alternative such as periodic manual sampling. Fill all seven elements.
- **Weak:** "An innovative platform for everyone" provides neither a specific customer nor a credible distinction.
- **Drift to avoid:** Feature-list differentiation: sensors and dashboards are capabilities. Explain the customer outcome that makes the alternative less attractive.


##### Common Pitfalls

- **Features Instead of Benefits in the "That" Element:** Rewrite the "That" element as the outcome the customer experiences: "That gives operations teams immediate visibility into site performance without waiting for weekly reports."

- **Strawman Competitor in the "Unlike" Element:** Name the alternative the target customer would actually choose. If the biggest competitor is Salesforce, name Salesforce. If the real alternative is the status quo (spreadsheets and email), name that. The "Unlike" should make sales reps nod, not roll their eyes.

- **Empty Adjectives in Differentiation:** Replace adjectives with specific outcomes. "Innovative" becomes "reduces onboarding time from weeks to days." "Seamless" becomes "works within the tools the team already uses without requiring migration."

- **Product Category Too Broad or Too Narrow:** Use the category label the target customer would use when searching for solutions or describing the product to a colleague. "HR automation tool" - an HR specialist knows what that means and can compare it to alternatives in the same category.

- **Target Customer Too Generic or Defaulting to a Tech Role:** Name the person who experiences the product's value in the field. If the product is a warehouse labor coordination platform, the target customer is "regional distribution center operations managers," not "businesses" and not "software engineers."

- **The Need/Opportunity Does Not Match Discovery Work:** Pull the "Who" language directly from JTBD artifacts, problem identification work, or empathy interview findings. The need should sound like something a customer actually said, not something a marketer assumed.

- **Differentiation in Feature Terms Instead of Outcome Terms:** Rewrite as outcomes: "Our product gives real-time data access, streamlined workflows and automates repetitive tasks." The customer can verify these claims from their own experience.

- **Forgetting Status Quo as a Valid Competitive Alternative:** Ask: what is the customer doing today without your product? If the answer is "spreadsheets and manual processes," that is a valid and often the most important "Unlike" to address.

- **AI Drafts Before the PM Does:** Coach the PM to draft first, then critique. If the PM asks for a draft, tag it `[AI-SUGGESTED, VALIDATE THIS]` and run the same critique on it.

- **One Statement Stretched Across Segments:** One persona, one statement. Rerun the exercise for each additional persona.

- **Claims Stronger Than the Evidence:** Test every claim for relevance, credibility, and differentiation. Verify competitor details before they shape the "Unlike" element. Soften or drop any claim the evidence can't carry.

##### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-positioning-statement) for supporting source material and expanded examples.


### Play 14: Lo-fi Experimentation

Stable identifier: `psk-lofi-experimentation`.

#### psk-lofi-experimentation / Instructions

##### Purpose

Design a **Productside-style Lo-fi Experimentation artifact** from a proposed solution.

This skill helps a Product Manager turn a solution hypothesis into a complete, runnable experiment plan:

- two critical make-or-break assumptions
- a measurable If/Then hypothesis statement
- a fully specified experiment design (Method, Audience, Metric(s), Time Window, Decision Rule)
- a description of the experiment stimulus

The point is not to validate every assumption. The point is to identify the one assumption whose falseness would change everything, design the smallest possible test, and commit to action rules before results arrive.

This is a **commitment surface**, not an ideation surface.

##### Key Concepts

###### A Test Exists to Settle a Decision

Before designing anything, the PM names **the decision the test will inform**. If they cannot say what they will do differently depending on the result, the test is not worth running yet. Then they define **"done"**: the specific behavior that must be observed from customers or users for a pass, across how many people, and what a failure looks like. These set the finish line. The experiment has one job: produce that signal.

###### The Signal Comes From Real People

A lo-fi test buys evidence from **real customers or users** reacting to a cheap stimulus. The stimulus can be anything from a paper sketch to a vibe-coded prototype. The audience cannot be simulated. Synthetic users, AI-generated personas, or a model's prediction of how customers would react produce no evidence about customers. (The baseline deck's example used 100 simulated users; the B2B work-in-progress deck replaced it with a Wizard-of-Oz test on real passengers.)

###### The Least You Can Build

Every method should be cheaper and faster than building the real thing. Keep asking: what is the least we could build to get a real signal? Steer away from anything that looks like a working version of the product.

###### Lo-fi Means Fast, Not Cheap

The goal of lo-fi experimentation is signal speed, not cost reduction. A $50 user test that answers the question in two days beats a $500 study that takes six weeks. The constraint is time-to-signal, not budget.

###### The Assumption Must Be Make-or-Break

Not every assumption needs an experiment. The right assumption to test is the one that, if false, means the solution approach is wrong. Assumptions about preferences, edge cases, or technical implementation are secondary. The critical assumption is the one that sits under the solution's entire value proposition.

Productside criteria for a valid assumption:
- **Make-or-break**: if this is false, the solution approach changes significantly
- **About behavior or sentiment**: something a customer would do, feel, or believe - not an internal team capability
- **Testable this week**: specific enough that a test can produce a result within days, not months

###### The Lo-fi Hypothesis Differs from the Solution Hypothesis

The Solution Hypothesis (from psk-solution-hypothesis) chains: IF we provide this solution, THEN customers benefit, THEN the business achieves an outcome.

The lo-fi hypothesis is different. It describes a specific test and a specific observable signal:

"If we [expose customers to this stimulus], then [we will observe this specific, measurable result]."

The IF describes the test. The THEN describes an observable, countable result with a threshold.

###### The Decision Rule Prevents Rationalization

Specifying thresholds before results arrive forces the team to act on results rather than explain them away. The three-tier structure (continue / adjust / pivot) creates genuine decision points. Without it, teams find a way to continue regardless of what they learned.

###### Lo-fi Artifacts Are Also Communication Tools

Testing is the primary purpose of lo-fi experimentation. But a lo-fi artifact serves a second, equally valuable function: giving cross-functional stakeholders  -  designers, engineers, executives  -  a concrete, shared picture of the proposed solution before any build investment is made.

A clickable prototype or Wizard-of-Oz simulation makes the product concept tangible enough for meaningful conversation. It surfaces disagreements about user experience early, when the cost of changing direction is low. Product leaders can also use lo-fi artifacts to share the product vision with executives, making the problem and proposed solution vivid in a way that slides and written descriptions cannot.

The artifact you build to test an assumption also becomes the artifact that aligns the team.

###### Experiment Types from the Productside Catalog

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

###### How AI Supports This Play

The Playbook casts AI as a **thought partner in two moments**. First, after the PM lists what must be true for the solution to pay off, AI widens the view toward assumptions the PM cannot see alone and pressure-tests which one is genuinely riskiest. Then it helps design the smallest, fastest test that could prove the PM wrong.

The reasoning stays with the PM. They name the assumptions, rank the risk, decide what a pass looks like, and decide what they will do about it. If AI hands over the riskiest assumption, the PM has skipped the thinking that shows whether they understand their own idea. AI sharpens the probe. The signal comes from real people, never from the model.

- **Use it when:** there is a prioritized solution, and the PM wants to find the riskiest assumption under it and design a cheap, fast experiment that drives a real decision.
- **Avoid it when:** the problem, persona, or solution is still vague. AI will manufacture confident assumptions and a tidy test with nothing real beneath them. Route back to psk-solution-hypothesis or psk-framing-the-problem.
- **Return:** blind-spot assumptions raised as candidates for the PM to weigh, a single riskiest assumption tied to a decision, and the smallest test that produces a real pass-or-fail signal.

###### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

###### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

##### Application

Use [Template](playbook-skills.md#psk-lofi-experimentation--template) for the scaffold.


###### Required Output Convention

Default to a **clean, paste-ready artifact** with all four sections complete:

- exactly 2 key assumptions
- 1 hypothesis statement for the selected assumption
- a fully specified experiment design (all five elements)
- an experiment description specific enough to run

Explanation belongs below the artifact, not inside the fields.

###### Step 1: Apply the Tech-Role Bias Guard

Before identifying assumptions, verify the proposed solution addresses a customer-side problem, not an internal engineering or tooling challenge.

The assumptions to test should be about customer behavior, customer value, or customer adoption. If the assumptions are primarily technical implementation questions ("can we build this?"), redirect to a technical spike rather than a lo-fi experiment.

Ask: Who is experiencing the problem this solution addresses? If the answer is the development team or internal stakeholders rather than end users or buyers, pause and reframe.

###### Step 2: Collect Artifacts

Ask whether the user has materials to supply that would ground the experiment in evidence:

- the solution hypothesis from psk-solution-hypothesis (the If/Then chain)
- the framing-the-problem output (the five-stem problem statement)
- any prior customer feedback on the solution direction
- empathy interview notes that speak to adoption or behavior change
- any earlier lo-fi results that inform what to test next

The experiment should test the riskiest assumption embedded in the solution hypothesis. The more the user can supply, the more the assumption selection is grounded in real discovery rather than team intuition.

If there are no upstream artifacts at all, say so and note that the assumptions and experiment plan will be first-pass hypotheses requiring more grounding.

###### Step 3: Record and Widen the Assumptions

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

###### Step 4: Choose the Riskiest, Name the Decision, Define Done

1. **Pressure-test the PM's risk ranking.** For each assumption, ask how likely it is to be wrong and how much it costs if it is. **The PM chooses the single riskiest.** Do not choose for them. State their choice and reason explicitly.
2. **Name the decision** the test will inform. If the PM cannot say what they will do differently based on the result, tell them the test is not worth running yet.
3. **Define done:** the specific behavior that must be observed from customers or users for a pass, across how many people, and what a failure looks like.

These three (riskiest assumption, decision, win-and-failure condition) are the finish line for the experiment.

###### Step 5: Write the Hypothesis Statement

Turn the riskiest assumption into a testable If/Then statement (mirrors the critique guidance in this Play):

"If we [describe what we will expose the customer to or simulate], then [describe the specific observable result we expect to see]."

The THEN predicts a **behavior the PM can observe**, not a feature they would build. If it predicts a feature, make them fix it. It must include a numeric threshold or a specific observable behavior. "Users will find it easier" is not a hypothesis. "At least 70% of users will complete the task without requesting help" is.

The IF describes the test, not the full solution. "If we build a unified dashboard" is a solution description. "If we give new users a clickable prototype with a unified dashboard" is a test description.

###### Step 6: Design the Experiment

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

###### Step 7: Describe the Experiment

Provide enough detail about what will be shown, said, or demonstrated that someone could run the experiment without redesigning it from scratch.

Include:
- the stimulus (mockup description, script, link, price sheet text, or ad copy)
- the core wording the customer will see or hear
- any task prompts or scenarios presented to participants

This section corresponds to the large right panel on the playbook template ("Visual or detailed text for your experiment").

Keep the description under 150 words. The goal is runnable clarity, not comprehensive specification.

###### Step 8: Add Optional Evidence Notes

If useful, add a brief trailing section with:

- what assumption remains untested after this experiment
- what the recommended next experiment would be
- any open risks not addressed by this experiment

Add this section only after the artifact is fully complete.

###### Step 9: Offer Next Steps

After completing the artifact, offer three options:

1. Run the experiment and return with results for interpretation
2. Design a second experiment for the remaining assumption
3. Proceed to psk-risk-assessment once the critical assumption is validated

#### psk-lofi-experimentation / Template

###### When to Use This

Use this template during **Discover + Define** when you have a proposed solution direction (ideally from psk-solution-hypothesis) and need to validate the riskiest assumption about it before committing to build.

Upstream work that feeds this template: psk-solution-hypothesis (the If/Then hypothesis to stress-test), psk-framing-the-problem (the validated problem statement), psk-exploring-solution-space (the solution method selected).

This template produces a commitment artifact. By the time you complete it, you have identified what you believe, designed a test, and committed to acting on the results regardless of outcome.

###### Template

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

###### Usage Guidance

###### Filling the Template

1. Start with **Product Context** to anchor whose assumption is being tested and which solution direction is under examination.
2. Write **both Key Assumptions** yourselves before selecting one to test. The act of writing both helps identify which is more critical.
3. Fill in the **Finish Line**: choose the riskiest assumption and say why, name the decision the test informs, and define what a pass and a failure look like. Do not imply the selection.
4. Write the **Hypothesis Statement** with a specific threshold before designing the experiment. The threshold drives the metric selection in section 3.
5. Complete all five **Design Experiment** elements. The Decision Rule is required, not optional.
6. Write the **Experiment Description** specific enough to run. This is the field that most often gets left vague.
7. Add **Evidence Notes** only after the artifact is fully complete.

###### What Goes Where

| Section | Contains | Does NOT Contain |
|---------|----------|------------------|
| Key Assumptions | Make-or-break customer behavior or sentiment beliefs | Technical feasibility questions, feature specifications, team preferences |
| Hypothesis Statement | Specific test description + measurable threshold | Full solution description, vague improvement language |
| Design Experiment | Method, Audience, Metric, Time Window, Decision Rule (all five) | General approach without specifics, metric without threshold |
| Experiment Description | Runnable stimulus and task prompts | Marketing pitch, comprehensive product spec |

###### Connecting to Other Skills

- **Upstream:** psk-solution-hypothesis provides the If/Then chain that surfaces the assumptions most worth testing. psk-framing-the-problem provides the validated problem that grounds the solution direction.
- **Downstream:** Results from the experiment feed psk-risk-assessment (once the critical assumption is validated, risks become clearer). psk-product-outcome-canvas (Template 16) draws from a validated solution direction.

###### Capacity Reference

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

#### psk-lofi-experimentation / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For a consultancy onboarding workflow, isolate an uncertain customer behavior, test it with a small prototype, and agree on a decision rule before collecting results.
- **Weak:** "Build the wizard and see whether people like it" leaves both the assumption and decision rule vague.
- **Drift to avoid:** Solution-description bug: an experiment must expose an assumption to failure, not merely describe the planned feature.


##### Common Pitfalls

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

##### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-lofi-experimentation) for supporting source material and expanded examples.


### Unnumbered: Storyboarding

Stable identifier: `psk-storyboarding`.

#### psk-storyboarding / Instructions

##### Purpose

Create a **Productside-style Storyboard** that validates a solution hypothesis through narrative.

This skill helps a Product Manager build a six-panel story centered on their target persona. The story follows a structured arc from the persona's status quo through a high-stakes conflict, into first contact with the solution, and finally to the lasting change that solution enables.

The storyboard belongs in the **Discover + Define phase** of the Productside Playbook. The B2B work-in-progress deck gives it no template number and places its instruction page right after Lo-fi Experimentation; the baseline deck had it as Template 16 of 24 in Create. It is explicitly low-fidelity. The playbook says it plainly: "Don't spend a lot of time building your storyboard; it doesn't need to look pretty!" Speed and clarity of thinking matter here. Aesthetics do not.

The storyboard does two things: it tests whether the PM's story about the customer rings true, and it gives stakeholders and real users something concrete enough to react to.

###### Usage Notes

- This is a component skill that produces a paste-ready six-panel narrative artifact.
- The Solution Hypothesis Statement (from psk-solution-hypothesis) anchors the top of every storyboard.
- Low fidelity is a design principle, not a limitation. Speed and clarity of thinking matter; aesthetics do not.
- The tech-role bias guard in Step 1 of Application is the single most important step in this skill.
- Upstream: psk-solution-hypothesis, psk-proto-persona, psk-framing-the-problem.
- Downstream: leadership alignment, executive communication, Go-to-Market narrative.

##### Key Concepts

###### Three Story Elements

Every storyboard requires three elements working together. If any one is missing, the story breaks down.

**Character** is the persona - the specific customer whose life the PM is trying to improve. The character must match the User Persona from psk-proto-persona. This is not the PM, not the product team, and not a generic user. It is a concrete individual with a job, a world, and things they care about.

**Conflict** is the problem - the specific breakdown that makes the persona's goal unreachable in the current state. The conflict should echo the Problem Statement from psk-framing-the-problem. A storyboard without a real conflict has no stakes and cannot be validated.

**Resolution** is the solution - how the product enters the persona's world and changes what is possible. The resolution must align with the If/Then structure from the Solution Hypothesis in psk-solution-hypothesis.

All three must be present and internally consistent. A strong character paired with a weak conflict produces a story no one can respond to. A strong conflict with a vague resolution does not validate the hypothesis.

###### The Six-Panel Arc

The storyboard uses six prompts in fixed order. Each prompt establishes something specific in the narrative.

**Panel 1 - "Once upon a time..."**
Introduce the persona and their world. Who are they? What does their day look like? What do they care about? This panel grounds the story in a real person with a real context.

**Panel 2 - "Every day..."**
Show the routine that leads toward the problem. What does the broken status quo look like day to day? This is not the crisis yet - it is the pattern that makes the crisis possible.

**Panel 3 - "Until one day..."**
The escalation moment. Something tips from friction into failure. The stakes are high here. A specific event or consequence makes the problem undeniable. This panel must be vivid - vague conflict produces vague feedback.

**Panel 4 - "Because of that..."**
The persona tries something new. They encounter the solution. This is not a feature list. It is an experience - what does it feel like to find and start using the product?

**Panel 5 - "Until finally..."**
The Aha moment. What does success feel like? Name the emotion. This is the moment the persona crosses from struggling to succeeding. Emotion matters here - it is what stakeholders and users respond to.

**Panel 6 - "And every day after that..."**
The lasting change. The persona's world is different now. What is possible that was not possible before? Behavioral change, not just happiness.

###### The Persona Is the Hero

The persona drives the story. The solution is their sidekick - it enables their success, but it does not achieve their goal for them. A storyboard where the solution is the hero has inverted the structure. The PM should be asking "what does the persona do differently?" not "what does the product do?"

###### Low Fidelity Is the Point

Speed matters more than polish in a storyboard. A rough narrative written in twenty minutes and shared with five users produces more insight than a polished visual deck. The six-panel format forces the PM to be specific without burning time on presentation. Images are optional; captions are sufficient.

###### What Validate Means Here

Storyboarding is a validation technique, not just a communication tool. Validation means showing the storyboard to real users or stakeholders and watching how they react. Do they recognize their world in Panel 1? Do they nod at Panel 3? Do they believe Panel 5? If the story does not ring true to people who live it, the hypothesis needs adjustment before anything is built.

###### The Storyboard Is Also a Product Visualization Tool

Validation with real users is the primary purpose of storyboarding. But the same artifact serves a second function: giving cross-functional stakeholders  -  designers, engineers, executives  -  a concrete, shared picture of the proposed solution before any build investment is made.

A well-constructed six-panel story makes the product's user experience visible in a way that wireframes and feature lists cannot. Stakeholders see the flow: the problem the product addresses, the moment of first contact with the solution, the breakthrough, the lasting change. They understand what the product actually does for the customer  -  its key capabilities and overall user value  -  without reading a requirements document.

Product leaders can use the storyboard to share the product vision with executives, making the problem and proposed solution vivid in a way that slides and written descriptions cannot. Build it once; show it to users for validation, show it to the team for alignment, and show it to leadership for direction-setting.

###### Text-First in This Skill

This skill produces text captions, not visual images. Each panel has a caption describing what should be depicted. The PM or a designer can add visuals later. The written captions are sufficient to share, discuss, and validate.

###### The Solution Hypothesis Statement Anchors Every Storyboard

Copy the If/Then statement from psk-solution-hypothesis and place it at the top of every storyboard. This anchors the story to a testable claim. If the story does not follow from the hypothesis, the storyboard is disconnected from the validation the PM needs.

###### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **critic of the storyboard the PM wrote, and a planner for showing it to real customers**. It checks that the persona is the hero and the product the sidekick, that the story follows the beginning, middle, and end arc from the solution hypothesis, and that the PM has a plan to show it to real target customers and record their reactions. The story and the reactions come from people, not the model.

- **Use it when:** the PM has a solution hypothesis and a draft story, and wants it sharpened and readied for testing with customers.
- **Avoid it when:** the request is to predict how customers will react to the storyboard. That is the test, and only real people can run it.
- **Return:** the story checked against the hypothesis and the three-part arc, the product kept in the sidekick role, and a plan to show the storyboard to real target customers and record what they say.

###### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

###### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

##### Application

Use [Template](playbook-skills.md#psk-storyboarding--template) for the scaffold.


###### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses Discovery mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

###### Step 1: Tech-Role Bias Guard

Before writing a single word of the storyboard, confirm who the product serves.

LLMs default to developer, architect, or product manager roles when no persona is specified. Most products serve non-programmers. A storyboard centered on a developer deploying a tool, when the product actually serves field technicians, operations staff, clinical workers, or line managers, will produce a narrative that fails to resonate with the real audience.

Ask the PM: who is the user persona for this product? Read the answer carefully. If the persona is a PM, engineer, developer, or architect - confirm this is actually the customer the product serves, not a proxy for the person running the exercise.

If the persona is the PM themselves, that is a signal the exercise has drifted. Redirect: who is the person your product is built for? That person is the hero.

###### Step 2: Gather Upstream Artifacts

Ask whether the PM has these artifacts to share:

- Solution Hypothesis from psk-solution-hypothesis (the If/Then statement that anchors the storyboard)
- User Persona from psk-proto-persona (the character's name, role, world, pains, and goals)
- Problem Framing from psk-framing-the-problem (the conflict source for Panel 3)

Accept equivalent input from any source. A PM with a product description but no prior plays can still run this skill. Do not block the exercise on missing upstream artifacts.

If artifacts are missing, gather the minimum needed:
- A specific product and what customer it serves
- A concrete description of the problem the customer faces
- A rough If/Then: if we build X, then the customer can do Y

###### Step 3: Write the Solution Hypothesis Statement Header

At the top of the storyboard, place the full If/Then statement from psk-solution-hypothesis (or the PM's equivalent).

Format it as a clearly labeled header:

```
Solution Hypothesis Statement:
IF we [description of solution], THEN [customer benefit].
IF [customer benefit], THEN [business outcome].
```

If only one half of the statement is available, use what is there. Do not fabricate the other half.

###### Step 4: Write Panel 1 - Introduce the Persona and World

Write the "Once upon a time..." caption.

Introduce the persona by name and role. Describe their world: what do they do day to day, what do they care about, what does success look like from their perspective? Ground the reader in a concrete person in a concrete context.

This panel should make the reader feel they know this person. Avoid generic descriptions ("a busy professional").

###### Step 5: Write Panel 2 - The Routine Status Quo

Write the "Every day..." caption.

Show the pattern of friction that precedes the crisis. What does the persona do repeatedly that is inefficient, risky, error-prone, or demoralizing? This is not the disaster yet - it is the condition that makes the disaster inevitable.

The goal of this panel is credibility. The reader (especially users or stakeholders who live this) should recognize the routine as real.

###### Step 6: Write Panel 3 - The Escalation Moment

Write the "Until one day..." caption.

Make this specific and high-stakes. A specific event or consequence tips the frustration into a real failure. Something breaks, something is missed, someone is affected. The stakes should feel real enough that the reader understands why doing nothing is not an option.

Vague conflict ("they faced some challenges") produces no feedback. Specific conflict ("she submitted an incorrect dosing report to the regulator and had to recall 30,000 units for re-audit") gives stakeholders something to react to.

###### Step 7: Write Panel 4 - First Encounter with the Solution

Write the "Because of that..." caption.

Show the persona encountering the product for the first time. This is an experience, not a feature list. What does it feel like to discover the solution exists? What is the first thing they do or notice?

Avoid writing "they used the product and it solved their problem." Describe the moment of first contact - what they saw, what they tried, what surprised them.

###### Step 8: Write Panel 5 - The Aha Moment

Write the "Until finally..." caption.

Name the emotion. This is the moment of breakthrough - the persona realizes the problem is solved or fundamentally changed. What do they feel? Relief, confidence, pride, surprise? Naming the emotion makes the story resonant and makes it easier for real users to confirm or deny when you show them.

###### Step 9: Write Panel 6 - The New Normal

Write the "And every day after that..." caption.

Show the lasting behavioral change. The persona's world is different now. What do they do differently? What is possible that was not possible before? What do they no longer worry about?

Avoid ending on "they were happy." Show what they can do, build, prevent, or decide that was out of reach before.

###### Step 10: Describe the Visual for Each Panel

For each panel, add a one-line visual description: what image or icon would represent this moment if the storyboard were illustrated?

This is optional but useful when sharing with visual thinkers or preparing the storyboard for a design session. Keep visual descriptions compact (5-15 words).

###### Step 11: Offer Next Steps

After completing the storyboard, offer three options:

1. Share with real users: walk three to five users through the storyboard panel by panel and capture where the story rings true and where it breaks down. The conflict moment and the Aha moment are the most important panels to test.
2. Share with leadership: the storyboard is an effective executive alignment tool. It makes the problem and solution concrete without requiring a slide deck.
3. Use in Go-to-Market messaging: the six-panel arc - problem, escalation, discovery, breakthrough, new normal - maps directly to launch narrative and sales enablement content.

#### psk-storyboarding / Template

###### When to Use This

Use this template during the **Create phase** after you have a Solution Hypothesis in hand. The storyboard validates your hypothesis by telling the customer's story - from their everyday world through the problem crisis into the solution and beyond.

Upstream artifacts that feed this template:
- Solution Hypothesis (psk-solution-hypothesis): the If/Then statement that anchors Panel 1 and must survive to Panel 6
- User Persona (psk-proto-persona): the character - name, role, world, pains, goals
- Problem Framing (psk-framing-the-problem): the source of the conflict in Panel 3

You can run this with only a product description if needed. The hypothesis and persona can be sketched on the fly. Do not block the exercise on missing upstream artifacts.

###### Template

```markdown
# Storyboard

## Solution Hypothesis Statement

IF we [describe the solution], THEN [describe the customer benefit].
IF [customer benefit], THEN [describe the business outcome].

---

## Three Story Elements Check

Before writing the panels, confirm these three elements:

- Character (who is the persona?):
- Conflict (what is the problem - must echo the Problem Statement):
- Resolution (what does the solution enable - must align with the Hypothesis):

---

## Panel 1: "Once upon a time..."

Introduce the persona and their world. Who are they, what is their day like, and what do they care about?

[Write your caption here]

Visual description: [optional - what image or icon would represent this moment?]

> Quality check: Does the reader now know who this person is, what they do, and what matters to them? Avoid generic descriptions. Name the role and give one or two concrete details about their world.
> Capacity check: 20-35 words per caption; 5-15 words for visual description.

---

## Panel 2: "Every day..."

Show the routine or status quo that leads toward the problem. What does the broken normal look like?

[Write your caption here]

Visual description: [optional]

> Quality check: Is this a pattern, not an event? Panel 2 shows the friction that precedes the crisis. The crisis belongs in Panel 3.
> Capacity check: 20-35 words.

---

## Panel 3: "Until one day..."

The escalation moment. Something tips from friction into failure. Make it specific and high-stakes.

[Write your caption here]

Visual description: [optional]

> Quality check: Is the consequence specific and concrete? A vague conflict ("some challenges arose") produces no useful feedback. Name what breaks, who is affected, and what the cost is. This panel must earn the stakes of the story.
> Capacity check: 25-40 words.

---

## Panel 4: "Because of that..."

The persona tries something new - first contact with the solution. Write the experience, not the feature list.

[Write your caption here]

Visual description: [optional]

> Quality check: Is this written as an experience the persona has, or as a product capability list? "She discovered the system had already grouped the exceptions by type" is an experience. "The platform provides automated categorization, real-time alerts, and bulk actions" is a feature list. Write the experience.
> Capacity check: 20-35 words.

---

## Panel 5: "Until finally..."

The Aha moment. Success arrives. Name the emotion.

[Write your caption here]

Visual description: [optional]

> Quality check: Does this panel name a specific emotion (relief, confidence, pride, surprise) in addition to describing what the persona achieved? The emotion is what makes the story resonate with real users.
> Capacity check: 20-35 words.

---

## Panel 6: "And every day after that..."

The lasting change. What is now possible that was not possible before? Show the behavioral difference, not just the happiness.

[Write your caption here]

Visual description: [optional]

> Quality check: Does this panel describe a specific behavioral change - something the persona now does, builds, prevents, or decides that was out of reach before? "She feels much better" is not a lasting change. "She now closes the compliance cycle on Tuesday instead of Friday and uses the saved time to coach her junior analysts" is.
> Capacity check: 20-35 words.

---

## Hypothesis Alignment Check

After completing all six panels, re-read the Solution Hypothesis Statement at the top. Then ask:

- Does the conflict in Panel 3 match the problem named in the IF clause?
- Does the solution in Panel 4 match the solution named in the IF clause?
- Does the outcome in Panels 5 and 6 match the THEN clause?

If the story has drifted from the hypothesis, revise before sharing.

---

## Validation Plan

Who will you show this storyboard to?

- User validation (3-5 real users or customers):
- Stakeholder validation (executive or cross-functional review):
- Key question to test: [Which panel are you most uncertain about? What do you most need to hear from users?]
```

###### Usage Guidance

###### Filling the Template

1. Paste or write the Solution Hypothesis Statement at the top before writing any panel.
2. Fill in the Three Story Elements check - character, conflict, resolution - before Panel 1.
3. Write all six panels in order. Resist the urge to skip to Panel 4.
4. After writing all six panels, do the Hypothesis Alignment Check.
5. Add visual descriptions last, if at all.

###### What Goes Where

| Panel | Contains | Does NOT Contain |
|-------|----------|-----------------|
| Panel 1 | Named persona, concrete world details | Generic "busy professional" descriptions |
| Panel 2 | The recurring friction pattern | The crisis event (that belongs in Panel 3) |
| Panel 3 | A specific, consequential failure event | Vague struggle or "some challenges" |
| Panel 4 | The persona's experience of first contact | A feature list or product spec |
| Panel 5 | A named emotion plus the success moment | The product's achievement (not the persona's) |
| Panel 6 | Specific behavioral change going forward | Vague happiness or "life is better now" |

###### Connecting to Other Skills

- **Upstream:** psk-solution-hypothesis provides the If/Then statement; psk-proto-persona provides the character; psk-framing-the-problem provides the conflict source
- **Downstream:** the storyboard feeds leadership alignment, executive communication, and Go-to-Market narrative

###### Capacity Reference

| Field | Target Length | Guidance |
|-------|-------------|---------|
| Solution Hypothesis Statement | 40-70 words | Full If/Then statement from psk-solution-hypothesis |
| Panel 1-2 captions | 20-35 words each | One to three sentences; specific but not overlong |
| Panel 3 caption | 25-40 words | Slightly more room - the conflict needs enough specificity to be testable |
| Panel 4-6 captions | 20-35 words each | One to three sentences |
| Visual descriptions | 5-15 words each | Optional; describe the image, not the story |

#### psk-storyboarding / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** A manufacturing quality inspector encounters a defect, faces its consequences, uses the proposed solution, and reaches a changed outcome across six frames.
- **Weak:** Six screenshots demonstrate an interface without telling a customer story.
- **Drift to avoid:** Tech-role inversion: the inspector is the protagonist; do not replace them with the developer building the tool.


##### Common Pitfalls

- **The Solution Is the Hero:** Rewrite every panel from the persona's perspective. What does the persona do, see, feel, or decide? The product should appear as the enabler of those actions, not the subject of the story.

- **Tech-Role Bias - Developer Persona for a Non-Developer Product:** Before writing Panel 1, confirm who the product is built for. Read the product description. Ask: who uses this in the field? Write for that person.

- **Polished and Long Panels:** Each panel caption should be one to three sentences at most. The prompt phrase does the framing work. The caption adds the specific, concrete detail. Keep it rough.

- **Missing the Conflict - Panel 3 Is Vague:** Name a specific event. Something breaks, fails, or causes visible harm. The more concrete the consequence, the more useful the feedback. "She submitted the wrong version of the report and the audit had to restart" is testable. "She had challenges with the process" is not.

- **Story Disconnected from the Hypothesis:** After completing all six panels, read the If/Then statement and then read Panel 3 and Panel 4. Are they about the same problem and the same solution? If not, the story has drifted. Rewrite to align.

- **Panel 6 Is Too Vague:** Name what the persona can now do, build, prevent, or decide that was impossible before. "She can now submit the monthly compliance report in one day instead of four, and she stops dreading the end of each quarter" is specific. "Things improved" is not.

- **Running This Before the Solution Hypothesis Exists:** Before running this skill, produce at least a rough If/Then statement using psk-solution-hypothesis. Even an informal hypothesis ("IF we automate the reconciliation step, THEN the operations manager can close the books without waiting on the data team") is enough to anchor the story.

- **Jumping to Product Features in Panel 4:** Panel 4 describes the persona's first experience, not the product's capabilities. "She logged in for the first time and saw her three overdue tasks organized by the system - she did not have to create the list herself" is an experience. A feature list is not.

- **Predicted Reactions Instead of a Test:** Show the storyboard to real target customers and record their reactions. Treat any predicted reaction as a guess to test.

##### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-storyboarding) for supporting source material and expanded examples.


### Play 15: Risk Assessment

Stable identifier: `psk-risk-assessment`.

#### psk-risk-assessment / Instructions

##### Purpose

Create a **Productside-style Risk Assessment artifact** from a collaborative team review of a product in development.

This skill helps a Product Manager and their project manager identify potential threats to a product build or launch, classify those threats by severity and likelihood, and build specific mitigation and contingency plans for the highest-priority risks.

The point is not to list everything that could go wrong. The point is to help the team complete the play with a prioritized, actionable risk plan.

##### Key Concepts

###### This Play Is Collaborative, Not Solo

The playbook is explicit: do not run this assessment alone. Partner with your project manager, who can lead the collaborative effort, and involve relevant stakeholders. A solo PM risk list misses organizational, technical, and customer-facing blind spots that surface in a group session.

###### Mitigation and Contingency Are Not the Same

Every risk needs two plans, not one:

- **Mitigation Tactics**: what the team does to reduce the chance the risk occurs. These are proactive actions taken before the risk materializes.
- **Contingency Plans**: what the team does if the risk occurs despite mitigation. These are reactive responses to the risk having already happened.

A plan where both columns contain the same kind of content has not done the work.

###### Risk Breadth Matters More Than Risk Count

Six risks that are all technical is not a complete assessment. A well-formed risk list covers:

- Customer adoption and behavior change
- Technical implementation and integration
- Organizational readiness and change management
- Market or competitive timing
- Data, privacy, or compliance
- Resource or capacity constraints

###### Point of Contact Is the Risk Owner, Not the Task Doer

The Point of Contact is the person accountable for monitoring and managing the risk. This is not necessarily the PM or the person completing the assessment. For adoption risks it may be a change management lead. For technical risks it may be an engineering lead. For compliance risks it may be a legal or security owner.

###### Six Is the Canonical Count

The template has six rows in the identification table. Fill all six. Fewer usually means the team has not looked broadly enough.

###### Risk Assessment Is a Living Document

The assessment is not a one-time checkpoint. Risks change as the product is built, tested, and launched. At minimum, revisit at the first major build decision.

###### Template Capacity Matters

Risk names, mitigation tactics, and contingency plans should be paste-ready for the playbook template. Keep entries specific but compact.

See [Template and capacity guidance](playbook-skills.md#psk-risk-assessment--template) for canonical field budgets.

###### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **a widening and pressure-testing partner for the risks the PM's team brainstormed**. It asks whether the list covers enough ground, offers risk categories (and, after the PM answers, candidate risks marked as candidates), and checks that each mitigation, contingency, and owner is real. Severity, likelihood, and the plan stay with the team.

- **Use it when:** the team has brainstormed risks and wants the list widened and the management plan pressure-tested.
- **Avoid it when:** the request is for a finished risk register for a product the team hasn't discussed. The risks that matter are the ones only the team can see.
- **Return:** gaps in breadth named, candidate risks offered as candidates, each mitigation separated from its contingency, and each risk given a real owner.

###### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

###### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

##### Application

Use [Template](playbook-skills.md#psk-risk-assessment--template) for the scaffold.


###### Required Output Convention

Default to a **clean, paste-ready artifact**.

That means:

- exactly 6 risks in the identification table
- all three sections completed
- Risk Management rows for at least the 2-3 highest-priority risks
- mitigation and contingency clearly distinct in every row
- no generic risk names like "Technical Risk" or "Market Concerns"
- explanation belongs below the artifact, not inside the fields

###### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses Discovery mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

###### Step 1: Apply Tech-Role Bias Guard

Before starting, ask: is the product being evaluated built for a technical or engineering user? If yes, note it and proceed. If not, flag it as you work - risk lists generated for non-technical customer contexts often cluster around implementation concerns (performance, integration, security) because those are the risks the product team lives with, not the risks the customer faces.

This is especially important for risks in the customer adoption and change management categories. The team running this assessment is not the customer. Risks should span customer-facing failure modes, not just build-side concerns.

###### Step 2: Confirm Scope Beyond Technical Risks

Before brainstorming risks, ask the user to consider whether their current thinking is skewed toward engineering concerns. Product teams commonly produce risk lists that are almost entirely technical (performance, integration, security) while missing the risks that most often cause product failures: customer behavior change, organizational resistance, market timing, and adoption barriers.

Prompt the user to think across these categories:

- What adoption or behavior-change risks exist?
- What organizational or change management risks exist?
- What technical or integration risks exist?
- What market or competitive timing risks exist?
- What data, privacy, or compliance risks exist?
- What resource or capacity risks exist?

###### Step 3: Collect Available Artifacts

Before drafting, ask whether the user has materials to share:

- Solution hypothesis from psk-solution-hypothesis (defines what is being de-risked)
- Problem framing from psk-framing-the-problem (gives customer and problem context)
- Any early customer feedback or field observations
- Stakeholder concerns surfaced in prior conversations
- A Stakeholder Alignment artifact (useful for identifying Points of Contact)

The more context about what is being built and for whom, the more targeted the risk identification. Also confirm who will participate in the risk review session.

###### Step 4: Identify Six Risks

Work with the user to identify exactly six risks. For each, capture:

**Risk Name**: a short label that names the type of risk and the specific concern. Follow the pattern: `[Risk Type]: [Specific Concern]`. Example: "Workflow Disruption: surgeons resist new documentation steps."

**Risk Raised By**: the team member or stakeholder who surfaced this risk during the session.

Spread the six risks across at least three distinct categories. Do not let all six cluster in one area.

###### Step 5: Plot Level of Risk

For each of the six risks, classify two dimensions:

**Impact Severity** (if this risk occurs, how severely does it affect the business or product outcome?):
- High: threatens the product goal or business outcome directly
- Medium: causes significant delays, cost increases, or partial goal failure
- Low: creates friction or rework but does not threaten the goal

**Occurrence Probability** (how likely is this to occur given what we know?):
- High: likely without active intervention
- Medium: possible; some conditions that could trigger it exist
- Low: unlikely given current context, but worth tracking

Derive a priority from the combination:

| Impact | Probability | Priority |
|--------|-------------|----------|
| High | High | Critical |
| High | Medium | Critical |
| High | Low | Monitor |
| Medium | High | Critical |
| Medium | Medium | Manage |
| Medium | Low | Accept |
| Low | High | Manage |
| Low | Medium | Accept |
| Low | Low | Accept |

Present the classification as a structured list per risk, not as a visual grid.

###### Step 6: Build the Risk Management Table

For each Critical or Monitor priority risk, and optionally for Manage-priority risks, complete the risk management table:

- **Risk Name**: match exactly the name from Step 3
- **Mitigation Tactics**: specific actions that reduce the chance the risk occurs. Not "test more" or "communicate better." What specifically will the team do, when, and with whom?
- **Contingency Plans**: specific response if the risk occurs despite mitigation. What will the team do? Who decides? What is the timeline?
- **Point of Contact**: the named accountable owner for this risk. If no one can be named, that is a signal the risk is unowned.
- **Notes**: timing dependencies, escalation paths, or open questions

At minimum, complete rows for all Critical-priority risks. Leave Accept-priority risks out if needed to keep the artifact focused.

###### Step 7: Review the Completed Artifact

Before presenting the artifact, check:

- Do higher-priority risks have stronger, more specific plans than lower-priority ones?
- Is every Contingency Plan clearly different from its paired Mitigation Tactic?
- Is every Point of Contact a named individual, not a team or function?
- Are there risks that are actually testable assumptions? If so, flag them as candidates for psk-lofi-experimentation.
- Are priorities meaningfully differentiated? If everything is Critical, the classification has not done its job.

###### Step 8: Flag the Assessment as a Living Document

After delivering the artifact, note that this assessment should be revisited at key decision points. At minimum, flag one specific time to revisit: at the first major build or delivery decision.

###### Step 9: Offer Next Steps

At the end of the artifact, offer three options:

1. Convert the most critical testable assumption into a lo-fi experiment using psk-lofi-experimentation
2. Carry the risk summary forward into psk-product-outcome-canvas when that play is run
3. Share the assessment with stakeholders identified in the Risk Raised By column to validate completeness and confirm Points of Contact

#### psk-risk-assessment / Template

###### When to Use This

Use this template during **Discover + Define** after completing your solution hypothesis and before committing to a build plan. Run it as a collaborative session with your project manager and relevant stakeholders.

Upstream artifacts that feed this template:
- Solution hypothesis (psk-solution-hypothesis): defines what is being built and what must be true for it to succeed
- Problem framing (psk-framing-the-problem): provides customer and context grounding for adoption risks
- Stakeholder Alignment artifact (if available): helps identify Points of Contact for each risk

###### Template

```markdown
# Risk Assessment

## Product Context

- Product or initiative:
- Stage (discovery, build, pre-launch, post-launch):
- Session participants:
- Date of assessment:

---

## Section 1: Identify Risks

Brainstorm the risks that could impact the success of this product or initiative.
Aim for exactly six. Cover adoption, technical, organizational, market, compliance, and resource categories.

| # | Risk Name | Risk Raised By |
|---|-----------|----------------|
| 01 | | |
| 02 | | |
| 03 | | |
| 04 | | |
| 05 | | |
| 06 | | |

> Quality check: Does each Risk Name name a specific concern, not a category? ("Workflow Disruption: clinicians resist new documentation steps" not "User Resistance")
> Quality check: Are risks spread across at least three distinct categories (adoption, technical, organizational, market, compliance, resource)?
> Quality check: Is each Risk Raised By a specific person, not a team or function?
> Capacity check: Risk Name should be ~5-8 words.

---

## Section 2: Plot Level of Risk

For each risk, classify Impact Severity and Occurrence Probability, then derive Priority.

Impact Severity: How severely would this affect the business or product outcome if it occurred? (High / Medium / Low)
Occurrence Probability: How likely is it to occur given what we know? (High / Medium / Low)

Priority guide:
- High Impact + High or Medium Probability = Critical
- High Impact + Low Probability = Monitor
- Medium Impact + High Probability = Critical
- Medium Impact + Medium Probability = Manage
- Medium Impact + Low Probability = Accept
- Low Impact + any Probability = Manage or Accept

---

Risk 01: [Risk Name]
  Impact Severity: [High / Medium / Low]
  Occurrence Probability: [High / Medium / Low]
  Priority: [Critical / Monitor / Manage / Accept]

Risk 02: [Risk Name]
  Impact Severity: [High / Medium / Low]
  Occurrence Probability: [High / Medium / Low]
  Priority: [Critical / Monitor / Manage / Accept]

Risk 03: [Risk Name]
  Impact Severity: [High / Medium / Low]
  Occurrence Probability: [High / Medium / Low]
  Priority: [Critical / Monitor / Manage / Accept]

Risk 04: [Risk Name]
  Impact Severity: [High / Medium / Low]
  Occurrence Probability: [High / Medium / Low]
  Priority: [Critical / Monitor / Manage / Accept]

Risk 05: [Risk Name]
  Impact Severity: [High / Medium / Low]
  Occurrence Probability: [High / Medium / Low]
  Priority: [Critical / Monitor / Manage / Accept]

Risk 06: [Risk Name]
  Impact Severity: [High / Medium / Low]
  Occurrence Probability: [High / Medium / Low]
  Priority: [Critical / Monitor / Manage / Accept]

---

> Quality check: Are priorities meaningfully differentiated? Not every risk should be Critical.
> Quality check: Is Impact Severity rated on business impact, not team inconvenience?
> Quality check: Are Critical risks clearly more urgent than Monitor or Manage risks?

---

## Section 3: Begin Risk Management

Complete this table for all Critical-priority risks. Include Monitor-priority risks if capacity allows.
Accept-priority risks may be listed without management rows.

| Risk Name | Mitigation Tactics | Contingency Plans | Point of Contact | Notes |
|-----------|-------------------|-------------------|------------------|-------|
| | | | | |
| | | | | |
| | | | | |

> Quality check: Is each Mitigation Tactic a specific proactive action that reduces the chance the risk occurs? ("Run pilot with 10 early adopters before full rollout" not "test more thoroughly")
> Quality check: Is each Contingency Plan a specific reactive response for if the risk occurs despite mitigation? ("Halt rollout and reconvene with adoption lead within 5 business days" not "communicate better")
> Quality check: Are Mitigation and Contingency clearly distinct from each other for every row?
> Quality check: Is each Point of Contact a named individual, not a team or role?
> Capacity check: Mitigation Tactics ~15-25 words; Contingency Plans ~15-25 words; Notes ~10-20 words.

---

## Revisit Note

Mark at least one future decision point where this assessment will be reviewed and updated:

- Next scheduled review:
- Trigger for unscheduled review (e.g., "if competitive landscape changes" or "at first major build decision"):
```

###### Usage Guidance

###### Filling the Template

1. Complete **Product Context** to anchor who is in the room and what stage the product is at.
2. Work through **Section 1** as a group. Push for specificity in Risk Names and for breadth across categories.
3. Complete **Section 2** risk by risk. Differentiate priorities. Resist the urge to rate everything Critical.
4. Complete **Section 3** starting with the highest-priority risks. Mitigation before contingency for each row.
5. Add the **Revisit Note** before closing the session.

###### What Goes Where

| Column | Contains | Does NOT Contain |
|--------|----------|------------------|
| Risk Name | Type + specific concern | Generic category labels |
| Risk Raised By | Named individual | "Team" or "Stakeholders" |
| Impact Severity | Business impact rating | Team inconvenience rating |
| Mitigation Tactics | Proactive prevention actions | Responses to the risk occurring |
| Contingency Plans | Reactive response if risk occurs | Duplicate of mitigation |
| Point of Contact | Named accountable individual | Team, function, or role title |

###### Connecting to Other Skills

- **Upstream:** psk-solution-hypothesis provides the solution context that grounds the risk identification. psk-framing-the-problem provides the customer and problem context.
- **Downstream:** psk-product-outcome-canvas (Batch 5) draws the risk summary from this assessment. psk-lofi-experimentation can convert high-priority testable assumptions from this assessment into structured experiments.

###### Capacity Reference

| Field | Target Length | Guidance |
|-------|--------------|----------|
| Risk Name | 5-8 words | Type label plus specific concern |
| Risk Raised By | 2-3 words | First name and last name or role |
| Mitigation Tactics | 15-25 words | Specific proactive action |
| Contingency Plans | 15-25 words | Specific reactive response |
| Notes | 10-20 words | Timing, dependencies, escalation |

#### psk-risk-assessment / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For shipment tracking, name a specific threat, assess severity and likelihood, and distinguish prevention from the contingency if it occurs.
- **Weak:** "Technical risk: high" gives no event, consequence, or response.
- **Drift to avoid:** Response confusion: mitigation reduces likelihood or impact; contingency says what to do if the risk happens.


##### Common Pitfalls

- **All Technical Risks, No Adoption Risks:** Before finalizing the list, explicitly ask: what are the customer behavior change risks? What are the organizational readiness risks? What could cause the product to be technically correct but commercially unsuccessful?

- **Confusing Mitigation with Contingency:** Mitigation happens before the risk occurs and reduces the chance it will. Contingency happens after the risk occurs and limits the damage. Both are required.

- **Point of Contact as a Role, Not a Person:** Name a specific individual. If you cannot name one, that is a signal that the risk is unowned and needs an owner before the assessment is complete.

- **Risk Names That Are Categories, Not Concerns:** Follow the pattern: `[Risk Type]: [Specific Concern]`. "Market Risk" becomes "Competitive Timing: new entrant launches similar feature before our release."

- **Completing Risk Management Only for Easy Risks:** Start the Risk Management table with the Critical-priority risks. If time is limited, leave Accept-priority risks without management rows rather than leaving Critical ones blank.

- **Treating the Assessment as a One-Time Artifact:** Mark at least one specific future date or decision point where the assessment will be reviewed and updated.

- **Inflating Everything to High Severity:** Push the team to differentiate. If more than three risks are truly Critical, the team needs to re-examine whether the ratings reflect business impact or anxiety. Not every risk deserves equal attention.

- **Running the Assessment Alone:** Run this as a collaborative session. The project manager leads the facilitation. Stakeholders surface risks the PM team would not see from inside the product team.

- **A Risk List the Team Never Discussed:** The team brainstorms first. The skill widens the list with categories and candidates, and the team places and owns each risk.

##### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-risk-assessment) for supporting source material and expanded examples.


### Play 16: Product Outcome Canvas

Stable identifier: `psk-product-outcome-canvas`.

#### psk-product-outcome-canvas / Instructions

##### Purpose

Create a **Productside-style Product Outcome Canvas** from the artifacts produced during the Discover + Define phase.

This skill is used at the **Go/No Go decision point** before the team enters the Create phase. Leaders use it to approve investment. PMs use it to practice presenting the business case to their sponsors and stakeholders.

The canvas brings together problem framing, solution positioning, customer stories, outcome targets, metrics, risks, and resource asks into a single, cohesive document. It is the artifact that answers the question leadership always asks: "Why should we build this, what will it do for us, and what do you need from us to make it happen?" It is not a summary slide.

##### Key Concepts

###### Why This Is a Go/No Go Document

The Product Outcome Canvas marks the formal end of the Discover + Define phase. At this point, the team has validated a problem, generated and explored solutions, formed a hypothesis, positioned the product, and assessed risks. The canvas consolidates all of that work into the form that leadership can evaluate and approve.

A canvas completed before this point is speculative. A canvas completed after this point is retrospective. The right moment is when the team has enough evidence to make a credible case but still needs authorization to proceed.

###### The Three-Section Structure

**Section 1: Core Information** anchors the document. Product Name, Date, Product Manager, and Version tell the reader what they are looking at and when.

**Section 2: Summary (left column)** tells the story of the problem and solution. It includes the Problem Statement, Solution Summary, Positioning Statement, two customer stories (one per persona), and the Key Features of the proposed solution.

**Section 3: Project Boundaries (right column)** frames the business case with measurable targets and honest constraints. It includes Business Outcomes, Product Outcomes, Business Success Metrics, Product Success Metrics, top Risks, The Ask, and the Introduction Date.

The two-column design is intentional: the left column persuades through narrative and context; the right column justifies through numbers and commitments.

###### Stories vs. Data

The two customer stories in the Summary section serve a purpose that data cannot: they make the problem real. A well-written story puts leadership in the room with the customer and makes the problem visceral. Data confirms the problem is worth solving; stories make people want to solve it.

Each story should anchor to a concrete moment in the customer's experience: a specific situation where the product either fails or succeeds. The before/after structure is the most reliable format: show the customer without the product, then show the same customer with it.

Stories are about the customer. Not the PM. Not the team. Not the development process. If the story protagonist is writing a PRD, facilitating a sprint, or reviewing a roadmap, the story is about the wrong person.

###### The Ask: Winning Approval

The Ask section is the resource request. Leadership needs to know three things: who you need, how much of their time, and for how long. A vague Ask ("we need engineering and design resources") is not an Ask. It is a wish. A credible Ask names roles, estimates percentage of time, gives a timeline, and flags any change management or infrastructure requirements.

An Ask that is too small under-allocates and sets the project up to slip. An Ask that is too large lacks credibility. Calibrate to the scope of what the canvas describes.

###### Loose Coupling to Upstream Plays

This skill draws from six upstream plays. Every field on the canvas can be populated from an upstream play artifact or from direct input, whichever the PM has available. The skill never blocks a field because an upstream play has not been run. If the PM has a problem statement from a workshop, a spreadsheet, or a prior document, that input is as valid as a psk-framing-the-problem output.

The upstream plays and their contributions:

| Canvas Field | Primary Upstream Source |
|---|---|
| Problem Statement | psk-framing-the-problem |
| Solution Summary | psk-solution-hypothesis |
| Positioning Statement | psk-positioning-statement |
| Business Outcomes, Product Outcomes, Metrics | psk-outcome-tree |
| Risks | psk-risk-assessment |
| Stories | psk-proto-persona (for persona context) |

If an upstream play has not been run, offer to run it before filling the field. If the PM has equivalent input from another source, accept it and proceed.

###### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **reviewer of the canvas before the Go/No Go decision**. It checks that each section is consistent with the upstream work it summarizes, that the user and buyer stories are grounded, that outcomes and metrics are measurable, and that the Ask is specific. Every claim on the canvas must come from the PM's work, because leadership will decide on it.

- **Use it when:** the PM has assembled the canvas from upstream artifacts and wants it reviewed before presenting it.
- **Avoid it when:** the upstream work doesn't exist yet. A canvas assembled from guesses becomes a Go decision on a guess.
- **Return:** inconsistencies between sections flagged, stories checked against evidence, outcomes and metrics checked for measurability, and the Ask sharpened into a specific decision and resource request.

###### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

###### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

##### Application

Use [Template](playbook-skills.md#psk-product-outcome-canvas--template) for the scaffold.


###### Required Output Convention

Default to a **clean, paste-ready artifact**.

That means:

- all three sections completed
- stories written in close-third or first-person with a concrete time anchor
- The Ask specifies roles, percentages, and a timeline
- Risks are named specifically (top 3 from the risk assessment)
- no generic placeholders left in any field
- explanation belongs below the artifact, not inside the fields

###### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses Discovery mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

###### Step 1: Tech-Role Bias Guard

Before writing any content, confirm who the product serves.

Most products serve people who do not write code: clinicians, logistics coordinators, field technicians, operations managers, procurement analysts, regulatory leads. LLMs default to developer/engineer protagonists when context is thin. The stories in this canvas will be wrong if the protagonist is a software engineer when the product serves a supply chain manager.

Ask the PM: "Who is the primary user of this product in the field? What is their job title? What does their day look like before this product exists?"

Use the answer to anchor both stories. If the PM cannot answer this question, offer to run psk-proto-persona before proceeding.

###### Step 2: Gather Upstream Artifacts

Ask the PM which of the following artifacts are available:

- Problem Statement (from psk-framing-the-problem or equivalent)
- Solution Summary or hypothesis (from psk-solution-hypothesis or equivalent)
- Positioning Statement (from psk-positioning-statement or equivalent)
- Business Outcomes, Product Outcomes, and Metrics (from psk-outcome-tree or equivalent)
- Risk Assessment (from psk-risk-assessment or equivalent)
- Persona descriptions (from psk-proto-persona or equivalent, for story context)

For each artifact that is not available, offer to run the corresponding skill or ask the PM to provide the information directly. Do not invent content for any field. If a field must be left incomplete, mark it clearly and note what is needed to complete it.

###### Step 3: Complete Core Information

Capture:

- Product Name (the actual product name, not a placeholder)
- Date (today's date, or the date of the Go/No Go session)
- Product Manager (the PM's name and role)
- Version (start at v1.0 unless the PM specifies otherwise)

###### Step 4: Write the Problem Statement

Use the final Problem Statement from psk-framing-the-problem if available. If not, ask the PM to describe the problem in 2-4 sentences covering: who is affected, what they are trying to do, what is blocking them, and why it matters to the business.

Do not write a problem statement that contains solution language. The problem statement describes the current state, not the desired future state.

Target: 40-60 words.

###### Step 5: Write the Solution Summary

Use the If/Then hypothesis format from psk-solution-hypothesis if available.

If not, ask the PM: "In one or two sentences, what does this product do and what does it enable the customer to do that they cannot do today?"

The Solution Summary describes the proposed solution at a level of specificity that makes the concept clear: specific enough to be meaningful, general enough not to lock in implementation details.

Target: 30-50 words.

###### Step 6: Write the Positioning Statement

Use the seven-element Positioning Statement from psk-positioning-statement if available. The seven elements are: For (target customer), Who (need or opportunity), The (product name), Is a (product category), That (key benefit), Unlike (primary competitive alternative), Our product gives (primary differentiation).

If the upstream artifact is not available, ask the PM to provide the positioning elements directly and assemble them using the formula.

Target: 50-70 words.

###### Step 7: Write Story 1 (User Persona)

Story 1 uses the user persona: the person who uses the product directly in the field.

Write a 2-4 sentence close-third or first-person narrative that anchors to a specific moment. Use a concrete time anchor ("Six weeks after the launch of X, Priya...") to make the story feel real. Show life before and after the product, or show a specific moment where the product makes a critical difference.

The story should make the problem tangible and the solution credible: not by listing features, but by showing the customer's experience.

Do not use the PM or the product team as the protagonist. Do not write a story about building, shipping, or configuring the product.

Target: 50-80 words.

###### Step 8: Write Story 2 (Buyer Persona)

Story 2 uses the buyer persona: the person who approves or funds the product, which may be a manager, director, procurement lead, or executive sponsor.

Use the same format as Story 1 but from the buyer's perspective. The buyer's story often centers on visibility, accountability, risk reduction, or efficiency rather than day-to-day task completion.

If no distinct buyer persona has been defined, ask whether the user and buyer are the same person. If so, note this in the artifact and write a single extended story, or ask the PM whether to differentiate.

Target: 50-80 words.

###### Step 9: Complete Project Boundaries (Outcomes and Metrics)

Use the psk-outcome-tree output if available. Populate:

- Business Outcomes: what the business gains from the product's success (revenue, efficiency, compliance, retention)
- Product Outcomes: what the customer achieves through using the product (role-based, not persona-named)
- Business Success Metrics: 2-3 measurable business-level indicators
- Product Success Metrics: 2-3 measurable product-level indicators

If the outcome tree has not been run, ask the PM to provide the outcomes and metrics directly. Outcomes must use outcome language (not feature language). Metrics must be specific and measurable: not "improve NPS" but "NPS increases from 32 to 45 within 12 months of launch."

Targets: Business Outcomes 15-25 words; Product Outcomes 15-25 words (bulleted); Metrics 2-3 items at 10-15 words each.

###### Step 10: List Key Features

List the top 3-5 features of the proposed solution. These are the capabilities the product will have: what it does, not what the customer achieves. Keep each item short and paste-ready.

Key Features are not outcomes. "Real-time shipment tracking dashboard" is a feature. "Logistics coordinators reduce shipment exception resolution time by 40%" is an outcome.

If the PM has not yet defined features, ask for the top 3-5 things the product will do. Do not infer features from the solution summary or positioning statement without confirmation.

Target: 3-5 bullets at 5-8 words each.

###### Step 11: List Top 3 Risks

Use the psk-risk-assessment output if available. Identify the top 3 risks by priority (Critical first) and list their names only. Do not include the full mitigation and contingency plans.

Risk names in the canvas are labels, not plans. The full risk management detail lives in the Risk Assessment artifact. The canvas shows leadership that the team has a risk picture; it does not replace the risk document.

If the risk assessment has not been run, ask the PM to name the 3 most significant threats to success. Use the format: [Risk Type]: [Specific Concern].

Target: 3 items at 5-8 words each.

###### Step 12: Write The Ask

The Ask is the resource request for the Create phase. It must include:

- Team composition: roles needed (e.g., Senior Engineer, UX Designer, Data Analyst)
- Time allocation: percentage of each role's time committed to this product
- Timeline: duration of the initial build phase (e.g., "8-week build sprint starting Q3 2026")
- Change management or infrastructure requirements: anything outside standard team capacity

If the PM does not have this information, prompt them with: "To give leadership a concrete Ask, I need to know: what roles do you need, how much of their time, and for how long?" Do not leave The Ask as TBD. It is the reason the canvas is presented.

Target: 30-50 words.

###### Step 13: Record the Introduction Date

The Introduction Date is the target launch or release date, meaning when the product reaches customers.

If the PM does not have a specific date, accept a target quarter or milestone ("Q4 2026" or "before annual customer conference in November"). Do not use TBD. If the date is genuinely unknown, flag it and note what decision would unlock it.

Target: 5-10 words.

###### Step 14: Offer Next Steps

After delivering the artifact, offer three options:

1. Share the canvas with the leadership sponsor or investment committee for the Go/No Go decision
2. Enter the Create phase by transitioning to build planning, user story mapping, or roadmap work
3. Schedule a structured review session to pressure-test The Ask and the risk picture before presenting

#### psk-product-outcome-canvas / Template

###### When to Use This

Use this template at the **Go/No Go decision point** at the end of the Discover + Define phase, before the team commits to entering the Create (build) phase. Present the completed canvas to your leadership sponsor or investment committee.

Upstream artifacts that feed this template:
- Problem Statement (psk-framing-the-problem or equivalent)
- Solution Summary (psk-solution-hypothesis or equivalent)
- Positioning Statement (psk-positioning-statement or equivalent)
- Business Outcomes, Product Outcomes, and Metrics (psk-outcome-tree or equivalent)
- Top Risks (psk-risk-assessment or equivalent)
- Persona context (psk-proto-persona or equivalent, for story anchoring)

Loose coupling rule: if an upstream artifact is not available, provide the information directly or ask the agent to run the relevant skill before proceeding. No field should be left as TBD in the final canvas.

###### Template

```markdown
# Product Outcome Canvas

## Section 1: Core Information

- Product Name:
- Date:
- Product Manager:
- Version:

---

## Section 2: Summary

### Problem Statement

[Describe the customer problem in 2-4 sentences. Who is affected, what are they trying to do, what is blocking them, and why does it matter to the business? No solution language.]

> Quality check: Does the problem statement describe a current state without referencing the proposed solution?
> Quality check: Is the problem specific enough that leadership can picture who is affected and why it matters?
> Capacity check: 40-60 words.

---

### Solution Summary

[Describe the proposed solution in 1-2 sentences using If/Then format where possible. What does the product do, and what does it enable the customer to do that they cannot do today?]

> Quality check: Is the solution summary specific enough to be meaningful but general enough not to lock in implementation details?
> Quality check: Does the solution address the problem statement directly?
> Capacity check: 30-50 words.

---

### Positioning Statement

[Seven-element formula: For [target customer], who [need or opportunity], the [product name] is a [product category] that [key benefit]. Unlike [primary competitive alternative], our product gives [primary differentiation].]

> Quality check: Is the "That" element a benefit (what the customer achieves), not a feature (what the product does)?
> Quality check: Does the "Unlike" element name a real competitive alternative the customer would actually choose?
> Quality check: Does "Our product gives" use outcome language, not feature language?
> Capacity check: 50-70 words.

---

### Story 1: User Persona

[Write a 2-4 sentence close-third or first-person narrative anchored to a specific moment. Use a concrete time anchor ("Six weeks after the launch of X, [Name]..."). Show the customer's experience before and after the product, or show a specific moment where the product makes a critical difference. The protagonist is the customer, not the PM, not the product team.]

Narrative format guide:
- Open with a concrete time anchor and a specific name and role
- Show the specific friction or challenge the customer faces without the product, OR show the moment the product resolves it
- Close with the customer's changed experience or outcome
- Example anchor: "Before ClearRoute launched, Marcos Delgado, a procurement coordinator at a regional hospital network, spent three hours each Monday reconciling delivery confirmations across four supplier portals..."

> Quality check: Is the protagonist the customer or buyer? The PM, an engineer, or a product team member should never be the protagonist.
> Quality check: Does the story make a specific moment tangible rather than describing general benefits?
> Quality check: Is the persona name specific and realistic (not a placeholder like "User A")?
> Capacity check: 50-80 words.

---

### Story 2: Buyer Persona

[Write a 2-4 sentence narrative for the buyer persona: the person who approves or funds the product. Use the same format as Story 1. Buyer stories often center on visibility, accountability, risk reduction, or operational efficiency rather than day-to-day task completion. The protagonist is the buyer, not the PM, not the team.]

> Quality check: Is the buyer persona distinct from the user persona? If they are the same person, note this and adjust the story accordingly.
> Quality check: Does the story reflect a buyer's concern (investment, oversight, outcomes) rather than a user's concern (task completion)?
> Capacity check: 50-80 words.

---

### Key Features

[List the top 3-5 capabilities of the proposed solution. These are what the product does, not what the customer achieves. Short bullets, paste-ready.]

- [Feature 1: ~5-8 words]
- [Feature 2: ~5-8 words]
- [Feature 3: ~5-8 words]
- [Feature 4: ~5-8 words (optional)]
- [Feature 5: ~5-8 words (optional)]

> Quality check: Are these features (capabilities) rather than outcomes (results)? "Real-time exception alerts" is a feature. "40% faster resolution" is an outcome.
> Quality check: Are the features specific to this product rather than generic to any product in the category?
> Capacity check: 3-5 bullets at 5-8 words each.

---

## Section 3: Project Boundaries

### Business Outcomes

[What the business gains from this product's success. Use outcome language: revenue, efficiency, retention, compliance, market position. 1-2 sentences or a compact bulleted list.]

> Quality check: Are these business-level outcomes (what the company gains), not product-level outcomes (what the customer achieves)?
> Quality check: Do the outcomes connect to a measurable business goal?
> Capacity check: 15-25 words.

---

### Product Outcomes

[What the customer/user achieves through using the product. Use role names, not persona names. Bulleted list.]

- [Role] [achievement]: [context or measure]
- [Role] [achievement]: [context or measure]

> Quality check: Do these outcomes use role names (e.g., "logistics coordinators") not persona names (e.g., "Priya")?
> Quality check: Are these outcomes (what the customer achieves) distinct from Key Features (what the product does)?
> Capacity check: 15-25 words total.

---

### Business Success Metrics

[2-3 measurable business-level indicators. Each should be specific enough to track. Include direction, metric, and target where possible.]

- [Metric 1: direction + metric + target, ~10-15 words]
- [Metric 2: direction + metric + target, ~10-15 words]
- [Metric 3: optional, ~10-15 words]

> Quality check: Is each metric specific enough to measure ("NPS increases from 32 to 45 within 12 months") rather than directional only ("improve NPS")?
> Capacity check: 2-3 items at 10-15 words each.

---

### Product Success Metrics

[2-3 measurable product-level indicators. These track customer behavior and product performance, not business-level results.]

- [Metric 1: direction + metric + target, ~10-15 words]
- [Metric 2: direction + metric + target, ~10-15 words]
- [Metric 3: optional, ~10-15 words]

> Quality check: Are these product-level indicators (usage, task completion, error rate) distinct from business success metrics (revenue, retention)?
> Capacity check: 2-3 items at 10-15 words each.

---

### Risks

[Top 3 risks from the Risk Assessment, by priority. Names only; do not include the full mitigation and contingency plans. Format: [Risk Type]: [Specific Concern].]

1. [Risk Name: 5-8 words]
2. [Risk Name: 5-8 words]
3. [Risk Name: 5-8 words]

> Quality check: Are these the highest-priority risks (Critical first) rather than an exhaustive list?
> Quality check: Does each risk name a specific concern, not just a category ("Carrier Data Gaps: top 3 carriers lack real-time API" not "Technical Risk")?
> Capacity check: 3 items at 5-8 words each.

---

### What's Next: The Ask

[Name the resources needed to enter the Create phase: team roles, percentage of time, timeline, and any change management or infrastructure requirements. This must be specific enough for leadership to approve or negotiate.]

Format guide:
- Team: [Role] at [%] time, [Role] at [%] time
- Timeline: [duration and start date or quarter]
- Change management or infrastructure: [any requirements outside standard team capacity]

> Quality check: Does The Ask name specific roles and percentages rather than generic functions ("engineering and design resources")?
> Quality check: Is the timeline specific enough to evaluate (not "TBD" or "as soon as possible")?
> Capacity check: 30-50 words.

---

### Introduction Date

[Target launch or release date: when the product reaches customers. Accept a specific date, a target quarter, or a milestone anchor.]

> Quality check: Is the date specific enough to anchor planning? If TBD, note what decision would unlock it.
> Capacity check: 5-10 words.
```

###### Usage Guidance

###### Filling the Template

1. Start with **Section 1: Core Information** to anchor the document.
2. Complete **Section 2: Summary** starting with the Problem Statement, which grounds everything that follows.
3. Write the Positioning Statement before the stories; the positioning clarifies who each story is about.
4. Write the stories last in Section 2, after confirming the persona identities from psk-proto-persona or direct PM input.
5. Complete **Section 3: Project Boundaries** by importing from upstream artifacts wherever possible.
6. Write The Ask after reviewing all other sections; the resource request should reflect the full scope of what the canvas describes.

###### What Goes Where

| Section | Contains | Does NOT Contain |
|---------|----------|-----------------|
| Problem Statement | Customer-facing problem in current state | Solution language, product features |
| Solution Summary | What the product does and enables | Implementation details, technical specs |
| Stories | Customer or buyer experience, specific moments | PM process, team activities, feature lists |
| Key Features | Product capabilities (what it does) | Customer outcomes (what customers achieve) |
| Product Outcomes | What customers achieve (role names) | Persona names, product features |
| The Ask | Roles, percentages, timeline, requirements | Vague functions, TBD timelines |

###### Connecting to Other Skills

- **Upstream:** psk-framing-the-problem (Problem Statement), psk-solution-hypothesis (Solution Summary), psk-positioning-statement (Positioning Statement), psk-outcome-tree (Outcomes and Metrics), psk-risk-assessment (Risks), psk-proto-persona (persona context for stories)
- **Downstream:** Go-to-Market Enablement (Template 20) imports Problem Statement, Positioning Statement, and Key Features

###### Capacity Reference

| Field | Target Length | Guidance |
|-------|--------------|----------|
| Problem Statement | 40-60 words | Describes current state without solution language |
| Solution Summary | 30-50 words | If/Then format where possible |
| Positioning Statement | 50-70 words | Seven-element formula, benefit not feature in "That" |
| Story 1 | 50-80 words | Concrete time anchor, customer protagonist |
| Story 2 | 50-80 words | Buyer protagonist, visibility or accountability focus |
| Key Features | 3-5 bullets, 5-8 words each | Capabilities, not outcomes |
| Business Outcomes | 15-25 words | Business-level, not product-level |
| Product Outcomes | 15-25 words | Role names, not persona names |
| Business Success Metrics | 2-3 items, 10-15 words each | Direction + metric + target |
| Product Success Metrics | 2-3 items, 10-15 words each | Usage and behavior indicators |
| Risks | 3 items, 5-8 words each | Top priority risks, names only |
| The Ask | 30-50 words | Roles + percentages + timeline |
| Introduction Date | 5-10 words | Specific date, quarter, or milestone |

#### psk-product-outcome-canvas / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For a hospital bed-coordination concept, consolidate the charge nurse's problem, tested hypothesis, outcomes, evidence, and risks for leadership's Go/No Go decision.
- **Weak:** A persuasive feature pitch without discovery evidence cannot support an informed investment decision.
- **Drift to avoid:** Decision substitution: a polished canvas does not constitute leadership approval or permission to proceed.


##### Common Pitfalls

- **Stories About the PM's Process Instead of the Customer's Experience:** The protagonist of every story is the customer or buyer. Read the first sentence of each story. If the subject is a PM, a designer, a developer, or a team, rewrite it. The story must anchor to the customer's day and the customer's experience.

- **Listing Every Risk Instead of the Top Three:** The canvas shows the top 3 risks by priority. Accept-priority risks belong in the full Risk Assessment artifact, not on the canvas. The canvas is a summary, not a transcript of the assessment.

- **The Ask Is Too Vague:** The Ask names specific roles ("2 Senior Engineers, 1 UX Designer, 1 Data Analyst at 80% time"), gives a percentage allocation, and names a timeline. If this information is not yet available, the canvas is premature. Run the planning work before presenting.

- **Treating the Canvas as a One-Time Artifact:** Treat the canvas as a living document. Update the Version number and Date when outcomes shift, risks change, or The Ask needs revision. The canvas should reflect the current state of the product investment, not just its initial framing.

- **Using Generic Placeholder Persona Names in Stories:** Use a specific, realistic name that reflects the persona's role and demographic diversity. Pair the name with a concrete job title and situation. "Priya Nair, a logistics coordinator at a mid-market distribution company, spends the first two hours of every morning..." is credible. "The user opens the dashboard..." is not.

- **Filling the Canvas Without Any Upstream Artifacts:** Before drafting any field, ask for the upstream artifacts or equivalent direct input. If no artifacts exist, flag the gap and offer to run the relevant upstream skill. Never invent the content of a field that is supposed to come from customer research or team validation.

- **Tech-Role Bias in the Customer Stories:** Run the tech-role bias guard in Step 1 before writing any content. Confirm the customer's job title and daily workflow. If the product serves non-technical users, the story must reflect non-technical concerns: task completion, time, accuracy, confidence, and visibility rather than system architecture or code quality.

- **Confusing Key Features with Product Outcomes:** Key Features are capabilities (what the product does). Product Outcomes are results (what the customer achieves). Each field serves a different purpose. If the same content appears in both sections, one of them is wrong.

- **A Canvas Built From Nothing:** Assemble the canvas only from upstream artifacts. Mark any section with no source as a gap, and say which play fills it.

##### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-product-outcome-canvas) for supporting source material and expanded examples.


## Create


### Play 17: Outcome-Based Roadmap & Release Plan

Stable identifier: `psk-outcome-roadmap`.

#### psk-outcome-roadmap / Instructions

##### Purpose

Create a **Productside-style Outcome-Based Roadmap and Release Plan** from a product team's validated outcomes and prioritized outputs.

This skill helps a Product Manager combine two connected layers into one artifact: a roadmap organized around product outcomes (what customers achieve) and a release plan organized around outputs (features, capabilities, and experiments). Both layers are sorted by confidence level into Now, Next, and Later columns.

The artifact is a **living document**. Discovery is never complete. As the team runs Tiny Acts of Discovery and resolves assumptions, items graduate from Later to Next to Now. The roadmap should be revisited at every major discovery or delivery milestone.

The critical distinction this skill enforces: the **roadmap row speaks outcome language only**. The **release plan row speaks output language only**. Mixing them creates confusion for every audience.

##### Key Concepts

###### Outcomes vs. Outputs - the Load-Bearing Distinction

This roadmap has two rows for a reason. They speak different languages to different audiences.

**Outcomes** are what customers achieve. They describe a changed state in the customer's world: "field technicians resolve equipment faults without returning to the depot," "quality inspectors catch defects before they leave the line." Outcomes belong in the roadmap row.

**Outputs** are what the team builds. They describe a deliverable: "fault diagnosis mobile app," "in-line defect vision scanner," "parts availability lookup." Outputs belong in the release plan row.

When outputs appear in the roadmap row, executives read a feature list instead of a value plan. When outcomes appear in the release plan row, engineering cannot build a sprint from them. Keep the rows separate.

###### The Now / Next / Later Confidence Framework

The three columns are organized by **confidence level**, not by priority or preference.

**Now - High Confidence:** The team has enough validated evidence to commit. These product outcomes have been tested against real customer behavior and real technical constraints. The team is pursuing them actively. Outputs in this column are in the release plan.

**Next - Medium Confidence:** The team believes in these outcomes and output ideas, but needs to resolve specific assumptions before committing fully. The primary work in Next is validation: running assumptions to ground so confident items can graduate to Now.

**Later - Low Confidence:** These are hypotheses - early-stage outcome ideas and open questions that require research before the team can evaluate them seriously. The primary work in Later is research: converting open questions into resolvable assumptions.

Confidence is not a popularity contest. An outcome moves left because the team has resolved uncertainty, not because leadership prefers it.

###### How Items Graduate

- **Later to Next:** When Assumptions to Research resolve enough uncertainty to form a testable assumption with a clear hypothesis.
- **Next to Now:** When Assumptions to Validate confirm enough confidence that the team can commit to the outcome and begin output development.
- **Now to Done:** When the output is shipped and the outcome can be measured.

Items can also move right. If a Now outcome proves harder to achieve than expected, or if new evidence undermines confidence, it should move back to Next for additional validation.

###### Discovery Is Continuous - Not a Future Phase

The discovery activities in this artifact (Tiny Acts of Discovery, Assumptions to Validate, Assumptions to Research) run **in parallel with the release work**. They are not a future phase that begins after Now outputs ship.

While the team is building Now outputs, it is simultaneously running Tiny Acts to refine those outputs, validating assumptions to graduate Next items, and researching questions to graduate Later items. The three columns are active at the same time.

A roadmap with empty discovery sections is not a living document. It is a delivery schedule.

###### Business Outcomes as the Anchor

Everything on the roadmap traces back to the Business Outcomes header. This is the business-level goal the product serves, drawn from the Outcome Tree. It provides the "why behind the what" and prevents the roadmap from becoming a disconnected list of features.

If a product outcome in the Now column cannot be connected to the Business Outcomes header, it should not be on the roadmap.

###### The Artifact Is a Communication Tool

Different audiences need different layers of the same artifact.

**Executives** read the Business Outcomes header and the roadmap row. They see what business goal is being served and what customer outcomes the team is pursuing at each confidence level.

**Engineering** reads the release plan row. They see what is being built (Now outputs), what needs validation before it can enter the build queue (Next output concepts), and what is still being explored (Later assumptions).

**Both audiences** are looking at the same artifact. No separate decks, no translation layer. The structure does the work.

###### This Builds Directly From the Outcome Tree

The product outcomes in the Now and Next roadmap cells should come directly from the psk-outcome-tree, not be invented fresh here. The PM should not use the roadmap as an opportunity to introduce new outcomes that have not been validated through the Outcome Tree play.

If the Outcome Tree has not been run, offer to run psk-outcome-tree first, or accept the PM's description of outcomes directly. But confirm they are grounded in discovery work.

###### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **critic of the roadmap the PM drafted**. It checks that each horizon holds outcomes, not outputs; that items sit in Now, Next, or Later by confidence; that each output links to an outcome; and that discovery work appears alongside delivery. The placements and the sequence stay with the PM and their team.

- **Use it when:** the PM has an outcome tree and a draft roadmap, and wants it pressure-tested before sharing it.
- **Avoid it when:** the request is to produce a dated feature roadmap, or to place items without the PM's evidence about confidence.
- **Return:** outputs posing as outcomes flagged, each placement questioned against the evidence behind it, and links from outputs to outcomes checked.

###### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

###### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

##### Application

Use [Template](playbook-skills.md#psk-outcome-roadmap--template) for the scaffold.


###### Required Output Convention

Default to a **clean, paste-ready artifact**.

That means:

- Business Outcomes header is specific and measurable (not "grow revenue")
- At least one product outcome in each column (Now, Next, Later)
- At least two outputs in the Now release plan
- Discovery sections (Tiny Acts, Assumptions to Validate, Assumptions to Research) are not left blank
- Every Now output traces to a Now outcome
- No outputs appear in the roadmap row; no outcomes appear in the release plan row
- Explanation belongs below the artifact, not inside the fields

###### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses Discovery mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

When a draft roadmap lists outputs (features, releases, projects), don't guess the outcomes behind them, even labeled as guesses. Name each item as an output and ask the PM what customer outcome it serves and what evidence puts it in Now, Next, or Later. The outcomes come from the PM and their customers.

###### Step 1: Tech-Role Bias Guard

Before drafting any content, confirm that the product outcomes are written from the **customer's perspective**. Outcomes describe what customers achieve - what changes in their world when the product works.

The team role bias is to write outcomes in engineering language: "deploy the alert system," "enable real-time API access," "build the reporting module." These are outputs, not outcomes.

Ask the user: who is the customer for this product, and what does success look like from their point of view? What changes in how they work, what they can accomplish, or how they feel about their work?

Do not proceed until there is a customer-perspective answer to that question.

###### Step 2: Gather Upstream Artifacts

Before drafting, ask whether the user has materials to share:

- Outcome Tree from psk-outcome-tree (Business Outcomes and product outcomes)
- Output prioritization results from psk-output-prioritization (Quadrant I and Quadrant II outputs)
- Tiny Acts findings from psk-tiny-acts-discovery (specific experiments and assumptions)
- Any prior roadmap or release plan the team has already discussed

Check whether each exists; offer to help fill gaps; accept equivalent input from any source. Do not gate the skill on whether the upstream play has been run. Accept the PM's direct description if the artifact is not available.

Make a note of which sections are drawn from upstream artifacts and which are being drafted fresh.

###### Step 3: Write the Business Outcomes Header

Draft the Business Outcomes header from the Outcome Tree's business outcome field. This should be one to two sentences describing the business-level goal this roadmap serves.

The header must be specific and anchored. "Reduce unplanned equipment downtime by 30% across field service regions" is anchored. "Improve operational efficiency" is not.

If the outcome has a measurable target, include it. If it does not, note that a target should be defined.

> Quality check: Can you trace every product outcome below to this business goal? If not, either the business goal is too narrow or one of the product outcomes does not belong on this roadmap.

###### Step 4: Populate the NOW Roadmap - Product Outcomes to Pursue

List the product outcomes the team is confident will create customer value and has committed to pursuing. These should come directly from the Outcome Tree (validated product outcomes) or from the PM's description of validated discovery findings.

Write in customer language: what customers achieve, not what the product does.

Each outcome should be specific enough that the team can measure whether it has been achieved. "Field technicians identify root causes without waiting for depot diagnostics" is specific. "Improve technician experience" is not.

> Quality check: Are these outcomes written from the customer's point of view? Can the team measure achievement? Do they trace to the Business Outcomes header?

###### Step 5: Populate the NEXT Roadmap - Product Outcomes to Validate

List the product outcomes the team believes in but has not yet validated enough to commit to. These outcomes need testing - specific assumptions must resolve before the team can move them to Now.

For each outcome, the key question is: what would have to be true for this to earn high confidence?

> Quality check: Is each outcome distinct from the Now outcomes? Is there a clear validation question that could move this outcome left?

###### Step 6: Populate the LATER Roadmap - Product Outcome Hypotheses

List early-stage outcome ideas that require research before the team can even form a testable hypothesis. These are genuine unknowns - areas where the team has a direction but not enough understanding to design a validation test.

Write these as outcome hypotheses, not as research questions. "Procurement managers could reduce approval cycle time to under 48 hours if sourcing exceptions were flagged earlier" is a hypothesis. "Research whether procurement managers care about approval times" is a research question.

> Quality check: Is each hypothesis plausible based on existing domain knowledge? Is there a clear question that would move this to Next?

###### Step 7: Populate Outputs to Develop (NOW)

List the features and capabilities that will drive the Now outcomes. These come from Quadrant I outputs in psk-output-prioritization (low cost, high value) or from the PM's direct input on what is in active development.

Write as specific output names, not categories. "Real-time fault alert push notification" is specific. "Notification system" is a category.

> Quality check: Does every output trace to a Now outcome? If an output cannot be connected to a Now outcome, it should not be in the Now release plan.

###### Step 8: List Tiny Acts of Discovery (NOW)

List the small, fast experiments the team is running in parallel with Now output development. These come from psk-tiny-acts-discovery or from the PM's direct input.

Each Tiny Act should be specific enough to run: name what is being tested, how, and with whom. "Run a 5-person session with field technicians using a paper mock of the fault alert screen to confirm the alert hierarchy makes sense to them" is a Tiny Act. "Test the UI" is not.

> Quality check: Are these running now, in parallel with the outputs being built? Are they specific enough to execute this week?

###### Step 9: Populate Output Concepts to Validate (NEXT)

List the output ideas that need validation before entering the release plan. These come from Quadrant II outputs in psk-output-prioritization (high cost, high value - needs more evidence before committing) or from the PM's description of candidates under consideration.

> Quality check: Is each concept clearly tied to a Next outcome? Is there a specific assumption that, if validated, would move this into Now outputs?

###### Step 10: List Assumptions to Validate (NEXT)

List the specific hypotheses and assumptions that must be resolved to move Next outcomes and output concepts to Now. Write these as testable hypothesis statements, not as features.

Format: "We believe [customer segment] will [behavior or outcome] when [condition or stimulus], because [reasoning]."

A well-formed assumption can be tested. A feature request ("build the dashboard") cannot.

> Quality check: Is each assumption specific enough to design a test around? Does each assumption trace to a Next outcome or output concept?

###### Step 11: List Assumptions to Research (LATER)

List the open questions and hypotheses that must be explored to move Later outcome hypotheses to Next. These are broader than testable assumptions - they require research to even know what to test.

Write as open questions or early hypotheses. The goal is to move from "we don't know" to "we have a hypothesis we can test."

> Quality check: Is each question specific enough to guide research? Can the PM name a method (interviews, observation, data pull) that would start to answer it?

###### Step 12: Review Alignment

Before presenting the artifact, check:

- Every Now output traces to a Now outcome
- No outputs appear in the roadmap row
- No outcomes appear in the release plan row
- Discovery sections are not blank
- Business Outcomes header is specific and measurable
- Now, Next, and Later columns each have content (the roadmap is not front-loaded into Now)

If an output cannot be traced to an outcome, ask whether the outcome belongs on the roadmap and is missing, or whether the output should be reconsidered.

###### Step 13: Offer Next Steps

At the end of the artifact, offer three options:

1. Share the roadmap with leadership: the Business Outcomes header and roadmap row give executives the outcome-level view they need to evaluate direction without getting into features
2. Share the release plan with engineering: the output-focused bottom row gives the team concrete, prioritized work with clear discovery activities running alongside
3. Schedule a review cadence: propose a specific date or milestone trigger for the next roadmap review, so the artifact stays current as assumptions resolve

#### psk-outcome-roadmap / Template

###### When to Use This

Use this template during the **Create** phase after completing your Outcome Tree and Output Prioritization. It is most powerful when Tiny Acts of Discovery results are available to populate the discovery sections.

Upstream artifacts that feed this template:
- Outcome Tree (psk-outcome-tree): Business Outcomes header and product outcomes for the roadmap row
- Output Prioritization (psk-output-prioritization): Quadrant I outputs for Now release plan; Quadrant II outputs for Next output concepts
- Tiny Acts of Discovery (psk-tiny-acts-discovery): specific experiments and assumptions for the discovery sections

---

###### Template

```markdown
# Outcome-Based Roadmap and Release Plan

**Product or initiative:**
**Date:**
**Team:**

---

## Business Outcomes

[One or two sentences from the Outcome Tree describing the business-level goal this roadmap serves. Include a measurable target if one exists. Example: "Reduce unplanned equipment downtime by 30% across field service regions by end of year, so regional operations teams can meet SLA commitments without emergency dispatch costs."]

---

## Roadmap

The roadmap row communicates in outcome language only - what customers achieve.
Do not list outputs (features, capabilities, or deliverables) in this row.

---

### NOW - High Confidence
**Product Outcomes to Pursue**

[List 1-2 product outcomes the team has validated and is committed to pursuing. Write from the customer's perspective: what they achieve, accomplish, or experience - not what the product does.

Format: one outcome per bullet, 15-25 words each.]

- [Outcome 1: what specific customer role achieves a specific result in a specific situation]
- [Outcome 2: what specific customer role achieves a specific result in a specific situation]

> Quality check: Are these written from the customer's point of view, not the engineering team's? Can each be measured once achieved? Do they trace to the Business Outcomes header above?
> Capacity check: 1-2 outcomes; 15-25 words each.

---

### NEXT - Medium Confidence
**Product Outcomes to Validate**

[List 1-2 product outcomes the team believes in but has not yet validated. These need testing before the team commits to pursuing them. Write in customer language - what customers would achieve if this outcome proved true.]

- [Outcome 1: what specific customer role would achieve if the underlying assumption proves valid]
- [Outcome 2: what specific customer role would achieve if the underlying assumption proves valid]

> Quality check: Is there a clear validation question for each outcome - something that, if answered, would move it to Now? Are these distinct from the Now outcomes?
> Capacity check: 1-2 outcomes; 15-25 words each.

---

### LATER - Low Confidence
**Product Outcome Hypotheses**

[List 1-2 early-stage outcome ideas that require research before the team can evaluate them seriously. These are hypotheses, not validated outcomes. The team has a directional sense but not enough knowledge to design a test yet.]

- [Hypothesis 1: a plausible outcome the team suspects might be valuable but cannot yet validate]
- [Hypothesis 2: a plausible outcome the team suspects might be valuable but cannot yet validate]

> Quality check: Is each written as a hypothesis, not a research question? Is there a clear research path that would move this to Next?
> Capacity check: 1-2 hypotheses; 15-25 words each.

---

## Release Plan

The release plan row communicates in output language only - what gets built.
Do not list customer outcomes in this row.

---

### NOW
**Outputs to Develop**

[List 2-4 specific features or capabilities the team is actively building to drive the Now outcomes. Each output should trace to a Now outcome above. Use Quadrant I outputs from psk-output-prioritization if available.]

- [Output 1: specific feature or capability name - 5-10 words]
- [Output 2: specific feature or capability name - 5-10 words]
- [Output 3: specific feature or capability name - 5-10 words]

> Quality check: Does each output trace to a Now outcome above? Are these specific enough to build a sprint from? No outcomes should appear here.
> Capacity check: 2-4 outputs; 5-10 words each.

**Tiny Acts of Discovery**

[List 1-2 small, fast experiments running now alongside output development. These are not future work - they run in parallel with the outputs above. Use Tiny Acts from psk-tiny-acts-discovery if available.

Format: name the test, the method, and the participants. 10-20 words each.]

- [Tiny Act 1: specific test with named method and participants, running in parallel with Now outputs]
- [Tiny Act 2: specific test with named method and participants]

> Quality check: Are these running now, not after Now outputs ship? Are they specific enough to execute this week? Do they connect to the outputs being built?
> Capacity check: 1-2 Tiny Acts; 10-20 words each.

---

### NEXT
**Output Concepts to Validate**

[List 1-2 output ideas that need validation before entering the release plan. These are candidates, not commitments. Use Quadrant II outputs from psk-output-prioritization if available - high value, high cost items that need more evidence before committing.]

- [Output concept 1: specific feature or capability idea - 5-10 words]
- [Output concept 2: specific feature or capability idea - 5-10 words]

> Quality check: Does each concept trace to a Next outcome above? Is there a specific assumption that, if validated, would move this into Now outputs?
> Capacity check: 1-2 output concepts; 5-10 words each.

**Assumptions to Validate**

[List 2-4 specific hypotheses about customer behavior or adoption that must be resolved before moving Next outcomes and output concepts to Now. Write as testable hypothesis statements, not as feature requests.

Format: "We believe [customer segment] will [behavior] when [condition], because [reasoning]." 10-20 words each.]

- [Assumption 1: testable hypothesis about customer behavior or adoption]
- [Assumption 2: testable hypothesis about customer behavior or adoption]
- [Assumption 3: testable hypothesis about customer behavior or adoption]

> Quality check: Is each assumption specific enough to design a test around? Is it about customer behavior or sentiment - not a technical or feature decision? Does it connect to a Next outcome?
> Capacity check: 2-4 assumptions; 10-20 words each.

---

### LATER
**Assumptions to Research**

[List 2-4 open questions and broad hypotheses that must be explored before Later outcome hypotheses can graduate to Next. These are wider than testable assumptions - they need research to even know what to test.

Format: an open question or early hypothesis. 10-20 words each.]

- [Research question 1: open question or early hypothesis about the Later outcome area]
- [Research question 2: open question or early hypothesis about the Later outcome area]
- [Research question 3: open question or early hypothesis about the Later outcome area]

> Quality check: Is each specific enough to guide a research method (interviews, observation, data pull)? Does it connect to a Later hypothesis above? Would answering this question move an item to Next?
> Capacity check: 2-4 items; 10-20 words each.

---

## Living Document Note

Mark when and how this roadmap will be reviewed:

- Next scheduled review:
- Trigger for unscheduled review (e.g., "when a Tiny Act produces a result" or "when a Next assumption is resolved"):
- Owner of the review cadence:
```

---

###### Usage Guidance

###### Filling the Template

1. Complete **Business Outcomes** first. Everything below it must trace back to this header.
2. Fill the **Roadmap row** (Now, Next, Later) using outcome language. Do not place any feature or output name in this row.
3. Fill the **Release Plan row** (Now, Next, Later) using output language. Do not place any customer outcome statement in this row.
4. Check that every Now output in the release plan traces to a Now outcome in the roadmap.
5. Fill the discovery sections (Tiny Acts, Assumptions to Validate, Assumptions to Research). If any are blank, the artifact is not ready.
6. Add the **Living Document Note** before sharing.

###### What Goes Where

| Section | Language | Contains | Does NOT Contain |
|---------|----------|----------|-----------------|
| Roadmap row | Outcome language | What customers achieve | Features, capabilities, deliverables |
| Release plan row | Output language | What the team builds | Customer outcome statements |
| Business Outcomes header | Business language | Business-level goal with measurable target | Vague directions like "grow revenue" |
| Tiny Acts of Discovery | Action language | Specific tests running now | Future research phases |
| Assumptions to Validate | Hypothesis language | Testable beliefs about customer behavior | Feature requests or build decisions |
| Assumptions to Research | Question language | Open questions needing research | Assumptions already ready to test |

###### The Graduation Path

Items move left as confidence increases:

- Later outcome hypothesis + research resolved = moves to Next as Product Outcome to Validate
- Next outcome + assumptions validated = moves to Now as Product Outcome to Pursue
- Next output concept + assumptions validated = moves to Now as Output to Develop
- Now output shipped + outcome achieved = removed from roadmap; captured in metrics

Items can move right if confidence decreases. A Now outcome with an unexpected discovery finding should move back to Next for additional validation rather than continuing to drive output development on a weakened foundation.

###### Connecting to Other Skills

- **Upstream:** psk-outcome-tree provides the Business Outcomes header and product outcomes for the roadmap row. psk-output-prioritization provides Quadrant I outputs for Now and Quadrant II outputs for Next output concepts. psk-tiny-acts-discovery provides specific experiments and assumptions.
- **Downstream:** This artifact is the primary communication tool for the Create phase. Share the roadmap row (outcome language) with leadership and the release plan row (output language) with engineering.

###### Capacity Reference

| Section | Items | Words per Item | Notes |
|---------|-------|---------------|-------|
| Business Outcomes | 1-2 sentences | 20-35 words total | Specific + measurable target |
| Product Outcomes - Now | 1-2 outcomes | 15-25 words each | Customer language only |
| Product Outcomes - Next | 1-2 outcomes | 15-25 words each | Customer language only |
| Product Outcome Hypotheses - Later | 1-2 hypotheses | 15-25 words each | Customer language only |
| Outputs to Develop | 2-4 outputs | 5-10 words each | Specific feature or capability names |
| Tiny Acts of Discovery | 1-2 acts | 10-20 words each | Running now, in parallel |
| Output Concepts to Validate | 1-2 concepts | 5-10 words each | Candidate outputs, not commitments |
| Assumptions to Validate | 2-4 assumptions | 10-20 words each | Hypothesis format |
| Assumptions to Research | 2-4 questions | 10-20 words each | Open question or early hypothesis |

#### psk-outcome-roadmap / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** Roadmap: technicians diagnose faults sooner. Release plan: deliver the diagnostic checklist that may support that outcome. Distinguish confidence horizons.
- **Weak:** A dated feature list alone hides the customer progress each release is meant to support.
- **Drift to avoid:** Business language in the customer row: revenue growth belongs at the business layer, not as a substitute for the technician's outcome.


##### Common Pitfalls

- **Feature-Based Roadmap - Outputs in the Roadmap Row:** Ask: what does the customer achieve when this output exists and works? That answer is the outcome. Replace the output in the roadmap row with the outcome. Move the output to the release plan row.

- **All Outcomes in NOW - No Differentiation by Confidence:** Push the team to differentiate honestly. If everything is high confidence, either the team is building too narrowly or they have not surfaced what they do not yet know. Most real product situations have at least two or three outcome hypotheses in Next or Later.

- **Roadmap Written in Business/Financial Language:** Reframe every outcome as a customer achievement: "What does the customer experience or accomplish when this metric improves?" "Increase ARR by 15%" becomes "contract renewal managers approve renewals faster because pricing scenarios are visible before the meeting." The business metric can live in the Business Outcomes header, not in the product outcome row.

- **Discovery Sections Left Blank:** Treat empty discovery sections as a red flag, not a formatting gap. At minimum, name one Tiny Act running alongside Now outputs and one assumption in each of Next and Later. If the team genuinely has no open questions, probe: what would have to be true for the Next outcomes to earn high confidence? Those answers are the starting assumptions.

- **Outputs Not Connected to Outcomes:** For each output, ask: which Now outcome does this drive? If no outcome in the Now roadmap row answers that question, either the outcome is missing from the roadmap or the output should not be in the Now release plan.

- **Static Artifact - Built Once and Never Updated:** Establish a specific review cadence tied to discovery milestones, not to the calendar quarter. When a Tiny Act produces a result or an assumption is resolved, the roadmap should update the same week. Build the review trigger into the artifact itself.

- **Business Outcomes Header Missing or Too Vague:** Make the business outcome specific and measurable. Name the direction, the metric, and the target if possible. "Reduce unplanned equipment downtime by 30% in field service regions by end of year" is an anchor. "Improve operations" is not.

- **Assumptions Written as Features Instead of Hypotheses:** Reframe each item as a testable hypothesis about customer behavior: "We believe [customer role] will [specific behavior] when [condition], because [reasoning]." The feature that might follow from a validated assumption is an output - it belongs in the release plan, not in the assumptions section.

- **A Feature List Dressed as an Outcome Roadmap:** Put product outcomes in each horizon, and link each output to the outcome it serves. Place items by confidence, based on evidence.

##### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-outcome-roadmap) for supporting source material and expanded examples.


### Play 18: Tiny Acts of Discovery

Stable identifier: `psk-tiny-acts-discovery`.

#### psk-tiny-acts-discovery / Instructions

##### Purpose

Create a **Productside-style Tiny Acts of Discovery artifact** from a collaborative team session on a product at any stage of development.

This skill helps a Product Manager and their team build an ongoing habit of assumption validation. The playbook states explicitly: "This tool can be used in many phases of a product process or lifecycle." Although it is placed in the Create phase, it applies equally in Discover, Define, and after launch.

This is a **process skill**. The agent helps the PM plan and document the exercise. Steps 1 through 4 (what we know, what we don't, prioritizing assumptions, writing hypotheses) happen in the conversation. Step 5 (running the tiny acts with real users, customers, or data) happens in the field. The agent cannot conduct interviews, run surveys, or generate user research findings on the team's behalf.

The goal is not a single checkpoint. The goal is a culture of continuous learning - what the playbook calls "fail often, fail fast." Failures are data, not setbacks.

###### Usage Notes

This is a **process skill**. The agent helps the PM plan and document the exercise. Steps 5 (running the tiny acts) happen in the field with real users, customers, or data. The agent does not conduct research or generate synthetic findings.

The skill applies at multiple lifecycle phases, not only Create. The playbook states explicitly: "This tool can be used in many phases of a product process or lifecycle."

Downstream connections: Outcome-Based Roadmap (Template 17) - specifically "Outputs to Develop," "Output Concepts to Validate," "Assumptions to Validate," and "Assumptions to Research" sections.

Related skill for single high-stakes assumptions: psk-lofi-experimentation (Template 14).

##### Key Concepts

###### The Five-Step Flow

The exercise follows a fixed sequence:

1. **What do we know?** - Validated facts, observed behaviors, completed research, confirmed assumptions.
2. **What do we not know?** - Gaps, unvalidated assumptions, open questions, missing data.
3. **Prioritize your assumptions** - Classify each "don't know" by impact and uncertainty on a 2x2.
4. **Form your hypotheses** - Write If/Then statements for the top-priority assumptions.
5. **List your Tiny Acts of Discovery** - Design one small, fast test per hypothesis, assign a metric and an owner.

###### A Living Backlog, Not a One-Time List

Tiny acts of discovery is a **habit**: keep a prioritized backlog of assumptions about the product and chip away at it with small, fast acts of learning, over and over. Re-score the backlog whenever new evidence arrives, and keep it where stakeholders can see it. A tiny act can be almost anything: one question to one user, a survey, a fake-door or willingness-to-pay test, a five-person expert chat, a quick prototype. The craft is finding the shortest path to a signal.

A backlog that never gets worked is planning, not discovery. If no act ever runs, the exercise has failed, however tidy the list.

###### The Certainty Score Is the PM's

Only the PM knows how much evidence they actually hold, so **the PM places every assumption** on impact and certainty. The skill pushes on the evidence ("what is it, and how confident are you in it?") and points at placements that look off. It does not move them. A backlog scored by a model is built on the model's guesses, and no one can explain why this, why now.

###### Impact vs. Uncertainty

The 2x2 matrix uses two dimensions:

- **Impact (Y-axis):** If this assumption turns out to be wrong, how much does it damage the product goal? High impact = major rework or goal failure. Low impact = minor friction.
- **Uncertainty (X-axis):** How much evidence do you currently have? High uncertainty = little or no evidence (the opposite of confidence). Low uncertainty = some evidence already exists.

**This is not the same as Output Prioritization**, which uses Value vs. Cost/Effort. Here, the dimensions are the cost of being wrong and the absence of supporting evidence. High impact + high uncertainty = most urgent to test. These go in the upper-right of the matrix.

###### How to Classify an Assumption

Two questions determine placement:

- "If we are wrong about this, does the product goal fail or require major rework?" - this sets Impact.
- "How much evidence do we currently have that supports this being true?" - the less evidence, the higher the Uncertainty rating.

###### Tiny Acts vs. Lo-fi Experimentation

These are related but not interchangeable:

- **Lo-fi Experimentation (Template 14)** is a formal, structured test plan for a single make-or-break assumption. It specifies a full hypothesis with a numeric threshold, a complete method, decision rules with three tiers, a time window, and an audience size. Use Lo-fi when you need a rigorous, documented test before committing to a major build decision.
- **Tiny Acts of Discovery** is for ongoing, lightweight assumption management across many assumptions simultaneously. Tests are smaller. Documentation is lighter. The intent is a culture of continuous learning, not one big formal experiment. Use Tiny Acts when you want to test many assumptions quickly and keep the team calibrated week to week.

A PM who uses Tiny Acts well will identify the single highest-stakes assumption that needs Lo-fi treatment. The two tools work together.

###### Tiny Acts Keep Development Customer-Focused

The purpose of Tiny Acts of Discovery is to anchor product decisions in what real customers actually do, need, and believe  -  not in what the team assumes from the inside. Every assumption worth testing should trace back to a customer behavior, a customer value question, or a customer adoption question.

When the team runs these exercises honestly, they replace internal debate with evidence. A user walkthrough result, a data pull, a survey response  -  these are the inputs that make the development process data-driven rather than opinion-driven. The team learns what customers genuinely need before committing resources to build it.

This is why a "don't know" list composed entirely of technical unknowns misses the point. Technical assumptions matter, but the assumptions that most often determine whether a product succeeds are behavioral and organizational: will customers change their current workflow, does the customer agree the problem is worth solving, will the organization adopt it? Centering Tiny Acts on these questions keeps development focused on meeting actual user needs.

###### The Culture of Continuous Learning

The playbook frames this as "fail often, fail fast." Each tiny act is a deliberate, low-cost way to get signal before investing in something bigger. A test that disproves a hypothesis is not a failure - it is learning that prevents a more expensive mistake downstream. Teams that skip this practice tend to discover wrong assumptions after significant time and money have been spent.

###### Why the Agent Cannot Run the Acts

The tiny acts are field research: user interviews, prototype walkthroughs, data pulls, A/B tests, short surveys administered to real customers. The agent can help design the specific acts, define the metrics, and document results when the PM returns with findings. It cannot conduct research, generate synthetic user responses as if they were real, or simulate field data.

###### How AI Supports This Play

The Playbook casts AI as a **thought partner across the loop**. The PM collects the opportunities and names the assumptions beneath them. AI widens the view and tests how confident the PM really is. The PM picks what to learn next.

- **Use it when:** the PM has a pile of opportunities, ideas, or signals and wants a prioritized backlog of assumptions plus fast, cheap ways to start testing them.
- **Avoid it when:** the backlog is being used to look busy. If no act ever gets run, the skill is helping the team plan instead of discover. Ask which act will run this week.
- **Return:** raw opportunities turned into testable assumptions, the PM's impact and certainty ranking pressure-tested, and a wide range of fast, creative ways to start learning.

###### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

###### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

##### Application

Use [Template](playbook-skills.md#psk-tiny-acts-discovery--template) for the scaffold.


###### Required Output Convention

Default to a **clean, paste-ready artifact**.

That means:

- at least 3 items in the "what we know" list, grounded in evidence
- at least 3 items in the "what we don't know" list, covering a range of assumption categories
- all assumptions classified on both dimensions (impact and uncertainty)
- a clear top-3 emerging from the classification
- one If/Then hypothesis per top-priority assumption
- one tiny act per hypothesis, with a specific metric and a named owner
- explanation belongs below the artifact, not inside the fields

###### Step 1: Confirm Scope and Session Context

Before starting, confirm three things:

1. **What product is this?** Get a one-sentence description of what the product does and who it is for. Vague product descriptions produce vague assumption lists.
2. **What lifecycle phase is the team in?** Tiny Acts applies at any phase, but the categories of unknowns differ. A team in early discovery has mostly behavioral and market unknowns. A team in late Create has mostly technical and adoption unknowns.
3. **Who is in this session?** Tiny Acts is a team exercise. The assumption list should reflect cross-functional perspectives. If the PM is working alone, note this  -  solo lists tend to be narrower and may miss organizational, adoption, and customer-behavior assumptions.

If the PM is working alone without team input, recommend they share the output with one or two stakeholders before designing the tiny acts.

###### Step 2: Tech-Role Bias Guard

Before building the assumption list, confirm what the product does and who actually uses it. Most products do not serve developers or technical architects. A supply chain management platform serves logistics coordinators and warehouse managers. A clinical data platform serves clinical operations leads and data managers. A field service app serves technicians and dispatchers.

Ask the PM directly: "Who is the person who will use this product day-to-day? What is their job title and what does their work look like?" This answer should shape every assumption on the list - the knowns, the unknowns, the hypotheses, and the tiny acts.

Do not allow the assumption list to default to technical unknowns (performance, integration, security) while missing the behavioral and organizational unknowns that most often determine whether a product succeeds.

###### Step 3: Gather Available Artifacts

Before drafting, ask whether the user has relevant materials to share:

- Solution hypothesis from psk-solution-hypothesis (defines what is being tested)
- Problem statement from psk-framing-the-problem (gives the customer and problem context)
- Outcome tree from psk-outcome-tree (clarifies what the team is trying to achieve)
- Any prior research, field observations, or customer feedback already collected
- Existing roadmap items or backlog priorities (these often reveal implicit assumptions)

The more context about what is being built and for whom, the more targeted the assumption list will be. Accept equivalent context from any source - the PM does not need to have run these upstream plays first.

###### Step 4: List What the Team Knows

Help the PM articulate the validated knowns. Push for evidence, not belief. For each item on the "what we know" list, the PM should be able to say where the knowledge came from: an interview, a data pull, a completed test, direct observation, signed research.

Watch for three failure modes:
- Assumptions dressed up as facts ("We know customers want faster reports" with no evidence)
- Old knowledge that has not been revalidated since the product changed
- Team consensus that has never been tested outside the building

Prompt: "How do you know this? What was the source?" If the PM cannot answer, move the item to the "don't know" list.

###### Step 5: List What the Team Does Not Know

Help the PM surface the gaps. Push for breadth across assumption categories, not just technical unknowns:

- **Behavioral:** Will customers change their current workflow? How do they currently do this without the product?
- **Adoption:** Who will champion this internally at the customer organization? Who will resist?
- **Organizational:** Does the customer organization have the capacity and authority to change this process?
- **Market:** Are there alternatives customers will choose instead? How strong is the status quo pull?
- **Value:** Does the customer agree the problem is worth solving? Will they pay or advocate for access?
- **Technical:** Can the product deliver the capability at the required performance and reliability?

A list of unknowns that is all technical has not been done honestly.

###### Step 6: Classify Assumptions by Impact and Uncertainty

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

###### Step 7: Identify the Top 3 Priority Assumptions

From the PM's classification, the PM picks the top 3 (those rated Urgent or High, or the top 3 by priority if fewer than 3 are Urgent/High). These become the inputs to Step 8.

If the PM's top 3 are all in the same category (all technical, all behavioral), flag this. A set of top-priority assumptions that clusters in one area usually means the team has not been honest about breadth.

###### Step 8: Write Hypotheses for the Top 3 Assumptions

For each top-priority assumption, write an If/Then hypothesis:

**Format:** "If [we do or provide X], then [we expect Y outcome] because [reasoning]."

Or for outcome-focused framing: "By achieving [specific outcome or metric], we can [achieve the goal]."

A strong hypothesis names a specific observable result, not a vague positive feeling. "Then customers will complete onboarding in under 10 minutes" is testable. "Then customers will like the experience" is not.

###### Step 9: Design Tiny Acts for Each Hypothesis

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

###### Step 10: Note the Process Boundary

After completing the artifact, be explicit with the PM: the next step is running the tiny acts in the field. This means contacting real users, running the test, collecting the signal, and returning with findings.

Offer to help document results when the PM returns. The typical return conversation looks like: "We ran the walkthrough. Here is what we saw." The agent can then help the PM update the assumption classification, identify which hypotheses were supported or disproved, and decide what the next round of tiny acts should address.

###### Step 11: Offer Next Steps

At the end of the artifact, offer three options:

1. Run the tiny acts and return with findings - the agent will help document results and update the assumption map
2. If one assumption from Step 6 stands out as uniquely high-stakes, convert it into a formal Lo-fi Experimentation plan using psk-lofi-experimentation
3. Feed confirmed results into the Outcome-Based Roadmap (Template 17): the "Outputs to Develop," "Output Concepts to Validate," and "Assumptions to Validate / Research" sections draw directly from Tiny Acts findings

#### psk-tiny-acts-discovery / Template

**Product:** [name the product]
**Customer:** [name the role that uses or buys this product day-to-day - not the PM, not the team]
**Date:** [date of session]
**Participants:** [names and roles]

---

###### Step 1: What Do We Know?

List what the team currently knows about the product and its users. These are validated facts, observed behaviors, completed research, and confirmed assumptions. For each item, note the source.

| What We Know | Source |
|---|---|
| [Specific, verified fact about customer behavior or product] | [interview date, data pull, completed test, field observation] |
| [Specific, verified fact about customer behavior or product] | [interview date, data pull, completed test, field observation] |
| [Specific, verified fact about customer behavior or product] | [interview date, data pull, completed test, field observation] |
| [Add more rows as needed] | |

**Quality check:** Can you name a source for each item? If not, move it to Step 2.

---

###### Step 2: What Do We Not Know?

List the gaps: unknown customer behaviors, unvalidated assumptions, open questions, missing data. Cover a range of categories - behavioral, adoption, organizational, market, value, and technical.

- [Unknown or unvalidated assumption - behavioral]
- [Unknown or unvalidated assumption - adoption or organizational]
- [Unknown or unvalidated assumption - market or value]
- [Unknown or unvalidated assumption - technical]
- [Add more as needed]

**Quality check:** Does this list include unknowns beyond technical ones? Are there behavioral, adoption, and organizational questions here?

---

###### Step 3: Prioritize Your Assumptions

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

###### Step 4: Form Your Hypotheses

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

###### Step 5: List Your Tiny Acts of Discovery

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

###### Next Steps

[ ] Run the tiny acts in the field
[ ] Document results and return to update the assumption classification
[ ] Schedule the next Tiny Acts session: [date]

**When you return with findings:** Share what you observed. The agent will help document results, identify which hypotheses were supported or disproved, and decide what the next round of tiny acts should address.

**If one assumption stands out as uniquely high-stakes:** Consider converting it into a formal Lo-fi Experimentation plan (Template 14) using psk-lofi-experimentation.

**When acts are complete:** Feed confirmed results into the Outcome-Based Roadmap (Template 17) - specifically the "Outputs to Develop," "Output Concepts to Validate," "Assumptions to Validate," and "Assumptions to Research" sections.

#### psk-tiny-acts-discovery / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For an HVAC dispatch assumption, identify what is known, expose the uncertainty, and plan a small field observation whose result could change the next decision.
- **Weak:** A list of research activities without an assumption or decision creates motion without learning.
- **Drift to avoid:** Agent runs the act: AI helps plan and interpret, while people conduct the real observation or experiment.


##### Common Pitfalls

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

##### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-tiny-acts-discovery) for supporting source material and expanded examples.


### Play 19: Output Prioritization

Stable identifier: `psk-output-prioritization`.

#### psk-output-prioritization / Instructions

##### Purpose

Create a **Productside-style Output Prioritization artifact** from a collaborative team review of candidate product outputs.

This skill helps a Product Manager and their cross-functional team evaluate which features and capabilities to build first, based on relative customer value and relative business cost. The result is a four-quadrant placement for every candidate output, a clear ordering for development sequencing, and a transparent record of the tradeoffs the team made.

The point is not to build everything eventually. The point is to help the team make a defensible, customer-grounded decision about what to address first, what to plan carefully, what to deprioritize, and what to cut.

The skill works in two moments. **Before the session**, it prepares the PM to facilitate: the center-point anchor, the moves that keep value and cost honest, and rehearsal for the hard personalities. **After the session**, it records the room's placements in the four-quadrant artifact and checks them. It does not rank the outputs itself.

This is a team exercise. It is not a solo PM exercise. Customer value requires discovery data or validated insight. Business cost requires input from engineering, a project manager, or a technical lead. A solo prioritization session produces outputs ranked by the PM's assumptions, not by evidence.

###### Usage Notes

- This skill is a component (content-fill) skill producing a paste-ready four-quadrant artifact.
- **Two moments:** before the session, it prepares the PM to facilitate (center-point anchor, moves against inflation, rehearsal of hard personalities). After the session, it records the room's placements and checks them. It does not rank the outputs itself.
- Center point anchoring is required before any other classification. Skipping it produces inflation.
- Value is always customer value. Business metrics on the value axis are the primary drift bug.
- Cost classification requires engineering or project manager input. PM-only cost estimates are not sufficient.
- Downstream: Quadrant I outputs feed the Outcome-Based Roadmap (Template 17) as "Outputs to Develop."

##### Key Concepts

###### Outputs Are Not Outcomes

This distinction is load-bearing. An **output** is a feature, capability, or deliverable the team can build: a real-time alert dashboard, an offline sync mode, a bulk import tool. An **outcome** is what a customer achieves when the product works: field technicians catch scheduling conflicts before they become incidents, operations managers spend less time on manual reconciliation.

Confusing outputs for outcomes is the most common failure mode in prioritization. An output that cannot be connected to a customer outcome has no defensible basis for prioritization. If the team cannot name the outcome an output supports, that output should be challenged before it is placed on the grid.

###### The Two Axes

**Value (Y-axis): Customer value.**
How much does this output drive progress toward a product outcome? Does it relieve a significant pain or create a meaningful gain for the customer? Value is defined entirely from the customer's perspective. Business benefits such as upsell opportunity, marketing positioning, or internal cost reduction are not customer value. They may be relevant business considerations, but they cannot substitute for the customer's perspective on the Y-axis.

**Cost (X-axis): Business cost and risk.**
How much does this output cost the business to develop? Cost includes development effort, integration complexity, infrastructure requirements, dependency management, and delivery risk. Engineering and project management input is required for a credible cost estimate. PM intuition is not sufficient.

###### Why Center-Point Anchoring Works

The most common problem in output prioritization is inflation: every feature is called "high value" by someone on the team. The center-point anchor breaks this dynamic.

The team agrees on one output that is genuinely medium cost and medium value - neither the most expensive nor the most impactful candidate on the list. That output anchors the center of the grid. All other outputs are plotted relative to this anchor, not on an absolute scale.

This prevents the "everything is critical" failure mode. It forces relative comparison: is this output more or less valuable than the anchor? More or less costly? Relative comparison is harder to inflate than absolute scoring.

###### Prioritization Is a Conversation About Trade-offs

Prioritization is a conversation about trade-offs, not a calculation. The plotting belongs to the room: real cost comes from the tech team, real value from customer evidence, and the call on what to build first from the PM and their stakeholders together. A ranked list handed down from a tool has no cost data behind it and no buy-in.

The room will want to crowd everything into high-value, low-cost. Moves that break that up:

- **Force comparisons against the anchor.** "More or less valuable than the center point? More or less costly?"
- **Ask for the outcome and the evidence behind every value claim.** Value means customer value tied to a product outcome, not internal excitement.
- **Make tech scope cost out loud.** Cost means the real build cost, not a wave of the hand.

Rehearse the hard moments before the session: the stakeholder who inflates their pet feature, the "everything is a priority" reflex, and cost getting waved away.

###### The Four Quadrants

The canonical labels the quadrants I through IV. The layout differs from standard mathematical quadrant notation:

- **Quadrant I (Low Cost, High Value - upper right):** Start here. Maximum return for minimum investment. These outputs should be at the top of the development sequence.
- **Quadrant II (High Cost, High Value - upper left):** Plan carefully. High return but high investment required. Validate the value assumptions before committing. Uncertainty in cost estimates warrants lo-fi experimentation before full build.
- **Quadrant III (Low Cost, Low Value - lower right):** Deprioritize. These outputs are cheap to build but do not move the needle for customers. "Easy" is not a reason to build.
- **Quadrant IV (High Cost, Low Value - lower left):** Avoid or cut. Poor return on investment. These outputs must be cut or deferred. Stakeholder pressure to keep Quadrant IV items is one of the most common prioritization failures.

###### Cross-Functional Input Is Required

Customer value: requires data from discovery work, empathy interviews, or validated product outcomes. The Outcome Tree (psk-outcome-tree) is the best source for linking outputs to product outcomes.

Business cost: requires input from engineering, a project manager, or a technical lead. Do not estimate cost without a technical voice in the room.

###### How to Connect Outputs to Outcomes

The Outcome Tree shows what customers need to achieve (product outcomes) as a result of the problem the product solves. Each output the team evaluates should be traceable to at least one product outcome. If an output cannot be connected to a product outcome, it is either solving an internal business problem (not a customer problem) or the outcome tree is incomplete.

Quadrant I outputs should be linked to the highest-priority product outcomes before they are committed to the roadmap.

###### Relationship to Tiny Acts of Discovery

Tiny Acts of Discovery is a technique for generating solution ideas before outputs are evaluated. Output Prioritization assumes that the brainstorm phase is complete: the team has already identified all candidate outputs (using Story Mapping, Tiny Acts, or equivalent). The prioritization exercise evaluates that list - it does not generate it.

If the list of candidate outputs is still thin or unclear, run Tiny Acts of Discovery before beginning this exercise.

###### How AI Supports This Play

The Playbook casts AI as a **facilitation coach**. It rehearses the session with the PM: how to set up the room, how to anchor every output against a single center-point output so the ranking stays relative, and how to keep the group honest when every idea drifts into high-value, low-cost territory. What the PM gets is a sharper facilitator, not a ranked list.

- **Use it when:** the PM has a list of outputs and needs to run a session where stakeholders prioritize them by relative value and cost.
- **Avoid it when:** the request is for AI to score and rank the features. It has no real cost data and cannot create team buy-in. Offer to prepare the session instead.
- **Return:** a session plan anchored on a center-point output, moves to keep value and cost honest, and rehearsal for the stakeholder who inflates everything. After the session: the room's placements, recorded and checked.

###### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

###### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

##### Application

Use [Template](playbook-skills.md#psk-output-prioritization--template) for the scaffold.


###### Required Output Convention

Default to a **clean, paste-ready artifact**.

That means:

- a named list of all candidate outputs (brainstorm phase)
- one clearly named center point output with team rationale
- a classification table with Value (H/M/L), Cost (H/M/L), and Quadrant for every output
- a Quadrant Summary listing outputs by quadrant with action guidance
- Quadrant I outputs linked to product outcomes
- explanation belongs below the artifact, not inside the classification fields

###### Step 1: Confirm Who the Customer Is

Before evaluating any output for value, confirm who the customer is - the person who uses or buys the product, not the PM, not the engineering team, and not an internal stakeholder.

This is the tech-role bias guard. LLMs and product teams both default to developer, architect, or internal-operations perspectives when evaluating value. If the product serves field technicians, operations managers, clinical coordinators, or other non-technical roles, the value dimension must be assessed from that person's standpoint.

Ask the user to name the customer role. If a proto-persona exists (from psk-proto-persona), use it. If an Outcome Tree exists (from psk-outcome-tree), confirm the product outcomes before evaluating outputs against value.

###### Step 2: Gather Available Artifacts

Before drafting, ask whether the user has materials to share:

- Solution hypothesis from psk-solution-hypothesis (defines the solution being decomposed into outputs)
- Product outcomes from psk-outcome-tree (used to evaluate value from the customer's perspective)
- Discovery findings from psk-empathy-interviews or psk-problem-identification (used to calibrate which customer pains are most severe)
- Any Story Mapping or Tiny Acts of Discovery results (used to populate the candidate output list)
- Engineering capacity or sprint planning data (used to calibrate cost)

The more context available, the more targeted the classification. If no artifacts are available, note that the output is based on PM assumptions and should be reviewed with the team before committing.

###### Step 3: Identify All Candidate Outputs

Work with the user to list all outputs that could be developed as part of the solution. This is a brainstorm - do not filter or evaluate yet.

For each output, capture:

- A short name (3-8 words) that identifies the feature or capability specifically
- Not a vague category like "reporting" or "integrations" - name the specific thing: "real-time alert dashboard" or "ERP connector for SAP"

Aim for completeness. A prioritization exercise with only three candidates is not a prioritization exercise - it is a list. A good brainstorm produces six to twelve candidates before the evaluation begins.

###### Step 4: Prepare to Facilitate the Session (Default)

Unless the PM is returning with the room's placements, prepare them to lead the session (mirrors the critique guidance in this Play). Do not rank, plot, or score the outputs, and do not pick the top items.

1. **Pressure-test the PM's center-point pick** (Step 5). Is it genuinely middle of the road on both value and cost? If not, help them reason toward a better anchor. They choose it.
2. **Walk the session:** place the anchor first, then have the group plot every other output relative to it.
3. **Coach holding value and cost honest:** value is customer value tied to a product outcome; cost is real build cost scoped with tech.
4. **Give specific moves** for when the room crowds everything into high-value, low-cost (see [Prioritization Is a Conversation About Trade-offs](#prioritization-is-a-conversation-about-trade-offs)).
5. **Rehearse the hard moments.** Ask the PM what they would say to the stakeholder who inflates a pet feature, to "everything is a priority," and when cost gets waved away. Then sharpen it.

Steps 5-12 describe the artifact the room produces. When the PM returns with the room's placements, record them and check them against those steps. When the PM asks you to place outputs before any session, don't place them yet: explain that value and cost come from the room (customer evidence and tech scoping), and offer to prepare the session and pressure-test a center-point anchor. If the PM then still wants a draft, or chooses Discovery mode, label the placements **AI draft placement: for the room to challenge; cost not scoped by tech**, and keep the session as the place the decision is made.

###### Step 5: Find the Center Point Output

The center point output is the anchor for the entire exercise. The team - not the PM alone - must agree on it.

Criteria for the center point:

- Medium cost: not the cheapest thing to build, not the most expensive
- Medium value: not the most impactful thing for the customer, not the least
- Understandable to all participants: the team can reason about other outputs relative to it

Name the center point output explicitly. Write one or two sentences explaining why the team agreed it is medium/medium. This anchors the calibration for every other placement.

###### Step 6: Classify Value for Each Output

Record how the room classified each candidate output except the center point, relative to the center point, as High, Medium, or Low.

Value is customer value. Ask: does this output drive more or less progress toward a product outcome than the center point output? Does it relieve a more or less severe customer pain?

For each classification, write a 1-2 sentence rationale that names the customer benefit or the product outcome it supports. If the rationale cannot name a customer benefit or outcome, the classification is based on assumptions - flag it.

###### Step 7: Classify Cost for Each Output

Record how the room classified cost for each candidate output except the center point, relative to the center point, as High, Medium, or Low.

Cost is business cost and risk. Ask: is this output more or less expensive to build and ship than the center point output? Does it carry more or less integration risk?

For each classification, write a 1-2 sentence rationale based on what engineering or the project manager said. If no technical input is available, note the assumption and recommend a follow-up sizing conversation.

###### Step 8: Place Each Output in Its Quadrant

Combine Value and Cost to assign each output to a quadrant:

- High Value + Low Cost = Quadrant I
- High Value + High Cost = Quadrant II
- Low Value + Low Cost = Quadrant III
- Low Value + High Cost = Quadrant IV
- Medium entries fall on the boundary - use judgment and team discussion to place them

**Check for inflation.** If most outputs landed in Quadrant I, the room rated each output on its own instead of against the anchor. Say so, and suggest the PM revisit the placements against the center point.

Outputs classified Medium/Medium belong near the center point. Treat them as Quadrant II or III candidates depending on which direction the team leans after discussion.

###### Step 9: Identify Quadrant I Outputs

List all Quadrant I outputs. These are the primary candidates for the first development cycle.

For each Quadrant I output, name the product outcome it supports. If it cannot be linked to a product outcome, pause and ask whether the classification is correct.

###### Step 10: Address Quadrant II Outputs

Quadrant II outputs are high value but high cost. Do not treat them as "do next" without additional validation.

For each Quadrant II output:

- Identify what assumptions about value and cost need to be validated before committing to the build
- Consider whether a lo-fi experiment (psk-lofi-experimentation) could reduce uncertainty before committing to full development
- If the team cannot validate the value assumptions, move the output to "Output Concepts to Validate" in the roadmap rather than "Outputs to Develop"

###### Step 11: Deprioritize Quadrant III and Cut Quadrant IV

Quadrant III outputs (Low Cost, Low Value): deprioritize. Do not build them in the current cycle, even if they are cheap. "Easy to build" is not a reason to build. Note them as deferred.

Quadrant IV outputs (High Cost, Low Value): cut or avoid. If stakeholders press to keep Quadrant IV items, document the tradeoff explicitly: what Quadrant I or II investment is deferred to make room for this.

If the team cannot bring themselves to cut any Quadrant IV items, the prioritization exercise has not done its job.

###### Step 12: Link High-Priority Outputs to Product Outcomes

For each Quadrant I output and each Quadrant II output the team decides to pursue, document the product outcome it supports. Use outcome language: what does the customer achieve when this output is available?

If the Outcome Tree has already been completed, reference the specific outcome by name. If not, write the outcome in outcome format: [direction] [metric] [context/circumstance].

###### Step 13: Offer Next Steps

After delivering the artifact, offer three options:

1. Feed Quadrant I outputs into the Outcome-Based Roadmap (Template 17) as "Outputs to Develop"
2. Place Quadrant II outputs in "Output Concepts to Validate" and run psk-lofi-experimentation on the highest-uncertainty ones
3. Share the classification with stakeholders to surface any Quadrant IV items that carry political weight and document the tradeoff decision explicitly

#### psk-output-prioritization / Template

Use this scaffold to produce a paste-ready four-quadrant output prioritization artifact in Productside format.

Complete all four sections in order. Do not skip the center point step - it is required for valid quadrant placements.

---

###### Section 1: Identify Outputs

List all candidate outputs (features, capabilities) that could be developed as part of the solution. This is a brainstorm - do not filter or rank yet. Include everything the team has proposed.

**Product or initiative:** [name of the product or feature set being prioritized]
**Customer role:** [who the product is built for - the person who uses or buys it]
**Session participants:** [names and roles of everyone involved in this classification]
**Date:** [date of session]

**Candidate outputs:**

- [Output 1: short name, 3-8 words]
- [Output 2: short name, 3-8 words]
- [Output 3: short name, 3-8 words]
- [Output 4: short name, 3-8 words]
- [Output 5: short name, 3-8 words]
- [Output 6: short name, 3-8 words]
- [Add additional outputs as needed]

> **Quality check:** Does every item name a specific, buildable feature or capability? Remove anything that is an outcome ("faster resolution times"), a goal ("improve user satisfaction"), or a vague category ("better reporting"). Each item should be concrete enough that an engineer could scope it.

---

###### Section 2: Center Point Output

The team must agree on one output that is medium cost and medium value - the anchor for all other placements. All other outputs will be classified relative to this center point.

**Center point output:** [name the output]

**Why this is medium/medium:** [1-2 sentences explaining why the team agreed this output represents neither extreme on value or cost - not the most impactful for the customer, not the most expensive to build]

> **Quality check:** Did the whole team agree on this anchor, or did the PM choose it alone? The center point requires team agreement. If only one person chose it, revisit before proceeding.

---

###### Section 3: Four Quadrant Classification

Classify each candidate output (except the center point) by Value and Cost relative to the center point. Then assign each to a quadrant.

**Quadrant layout reference:**
- Quadrant I: High Value, Low Cost (upper right) - start here
- Quadrant II: High Value, High Cost (upper left) - plan carefully
- Quadrant III: Low Value, Low Cost (lower right) - deprioritize
- Quadrant IV: Low Value, High Cost (lower left) - avoid or cut

| Output | Value (H/M/L) | Value Rationale | Cost (H/M/L) | Cost Rationale | Quadrant | Priority |
|--------|--------------|-----------------|-------------|----------------|----------|----------|
| [Center point output] | M | Anchor - all other outputs are relative to this | M | Anchor - all other outputs are relative to this | Center | Reference |
| [Output 2] | [H/M/L] | [1-2 sentence customer-outcome rationale] | [H/M/L] | [1-2 sentence technical/engineering rationale] | [I/II/III/IV] | [Start / Plan / Deprioritize / Cut] |
| [Output 3] | [H/M/L] | [1-2 sentence customer-outcome rationale] | [H/M/L] | [1-2 sentence technical/engineering rationale] | [I/II/III/IV] | [Start / Plan / Deprioritize / Cut] |
| [Output 4] | [H/M/L] | [1-2 sentence customer-outcome rationale] | [H/M/L] | [1-2 sentence technical/engineering rationale] | [I/II/III/IV] | [Start / Plan / Deprioritize / Cut] |
| [Output 5] | [H/M/L] | [1-2 sentence customer-outcome rationale] | [H/M/L] | [1-2 sentence technical/engineering rationale] | [I/II/III/IV] | [Start / Plan / Deprioritize / Cut] |
| [Output 6] | [H/M/L] | [1-2 sentence customer-outcome rationale] | [H/M/L] | [1-2 sentence technical/engineering rationale] | [I/II/III/IV] | [Start / Plan / Deprioritize / Cut] |

> **Quality check:** Review the Value column. Does every rationale name a customer benefit or a product outcome - not a business benefit, not an internal metric? If any rationale says "this will drive upsell" or "this will help sales," it is measuring business value, not customer value. Rewrite before finalizing. Review the Cost column. Did engineering or a project manager provide input on cost estimates, or is this PM intuition? Flag any row where cost was estimated without a technical voice.

---

###### Section 4: Quadrant Summary and Action Guidance

Organize outputs by quadrant and document the action for each.

**Quadrant I - Start Here (Low Cost, High Value)**

| Output | Product Outcome Supported |
|--------|--------------------------|
| [Output name] | [Name the product outcome this output drives - what does the customer achieve?] |
| [Output name] | [Name the product outcome this output drives] |

Action: Prioritize these outputs for the first development cycle. Carry them into the Outcome-Based Roadmap as "Outputs to Develop."

**Quadrant II - Plan Carefully (High Cost, High Value)**

| Output | Key Assumption to Validate | Recommendation |
|--------|---------------------------|----------------|
| [Output name] | [What assumption about value or cost needs to be validated before committing?] | [Lo-fi experiment / further technical sizing / staged delivery] |

Action: Do not commit these to the build plan until the key assumption is validated. Place them in "Output Concepts to Validate" in the roadmap. Consider psk-lofi-experimentation for the highest-uncertainty items.

**Quadrant III - Deprioritize (Low Cost, Low Value)**

- [Output name] - Deferred. Easy to build but does not drive meaningful customer progress at this stage.
- [Output name] - Deferred. Revisit if a product outcome changes or new discovery reveals higher value.

Action: Remove from the current cycle. Do not build these because they are cheap - build them only if customer evidence improves the value case.

**Quadrant IV - Avoid or Cut (High Cost, Low Value)**

- [Output name] - Cut. Poor return on investment. [Note any stakeholder tradeoff that needs to be surfaced explicitly.]
- [Output name] - Cut. [Note any dependencies or cleanup required.]

Action: Do not schedule. If stakeholders press to keep these, document the specific Quadrant I or II investment that would be displaced and ask for an explicit decision.

> **Quality check:** Is every output placed in exactly one quadrant? Is at least one output in Quadrant IV actually cut, not just deferred? If the entire list landed in Quadrant I and II, the classification has not done its job - revisit the center point and recheck the value rationales.

---

**Next Steps**

1. Feed Quadrant I outputs into the Outcome-Based Roadmap (Template 17) as "Outputs to Develop"
2. Move Quadrant II outputs to "Output Concepts to Validate" and plan validation for the highest-uncertainty items
3. Share the full classification with stakeholders to surface any Quadrant IV political items and document the tradeoff decisions

#### psk-output-prioritization / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** A care-coordination team compares candidate outputs against an agreed center-point output using relative customer value and business cost; the room records its judgments.
- **Weak:** Unanchored scores appear precise while participants use different scales.
- **Drift to avoid:** Value as revenue: do not replace customer value with business revenue impact or invent the team's placements.


##### Common Pitfalls

- **Defining Value from the Business Perspective:** Before classifying any output, re-read the product outcomes from the Outcome Tree. Each value classification must name what the customer achieves. If the rationale names only what the business gains, rewrite it from the customer's perspective.

- **Skipping the Center Point Anchor:** Name the center point output first. Get team agreement before any other classification begins. All subsequent placements are relative to that anchor.

- **Running This Without Engineering Input on Cost:** Do not finalize cost classifications without a technical voice. At minimum, run a rough sizing conversation with an engineering lead or project manager before locking the grid.

- **Confusing Outputs with Outcomes:** Every item on the candidate list must be a concrete, buildable thing: a specific feature, integration, interface, or capability. If the team is listing outcomes, redirect to the Outcome Tree (psk-outcome-tree) and then ask: what outputs could be built to drive that outcome?

- **Treating Quadrant II as "Do Next" Without Validation:** For every Quadrant II output, name the key assumptions about value that need to be validated before committing to the full build. Consider lo-fi experimentation (psk-lofi-experimentation) for high-uncertainty Quadrant II items before the development commitment is made.

- **Never Cutting Quadrant IV Outputs:** Document the Quadrant IV designation explicitly and surface the tradeoff to the stakeholder. "We can build this, but it will displace [specific Quadrant I output] that [customer outcome]. Is that the right call?" Force the explicit decision rather than letting Quadrant IV items survive by default.

- **Treating Quadrant Positions as Permanent:** Treat the grid as a living artifact. Revisit it when cost estimates change significantly (after technical investigation), when discovery reveals new information about customer value, or when the solution hypothesis changes.

- **Using Internal Metrics as Value:** For each value classification, ask: how does this output change what the customer can achieve? If the answer is only about internal operations, the classification is measuring the wrong thing. A support ticket reduction is only customer value if it means the customer gets unblocked faster - and that customer impact should be the stated rationale.

- **AI Does the Ranking:** Prepare the PM to facilitate (Step 4). The room plots relative to the anchor, tech scopes cost, and the PM and stakeholders decide. The skill records and checks the result.

- **Everything Wins:** Anchor every placement against the center point. Ask for the outcome and evidence behind each value claim, and make tech scope cost out loud.

##### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-output-prioritization) for supporting source material and expanded examples.


### Play 20: Go-to-Market Enablement

Stable identifier: `psk-go-to-market`.

#### psk-go-to-market / Instructions

##### Purpose

Create a **Productside-style Go-to-Market Enablement artifact** that prepares internal teams to execute a product launch.

This skill helps a Product Manager translate months of discovery and definition work into six clear sections that sales, marketing, customer support, and technical teams can act on without additional interpretation. It is the bridge between what the PM knows and what the rest of the organization needs to know before launch day.

This is a **Create phase** skill (Template 20 of 24). It is downstream of almost everything - it synthesizes the work of the full discovery and definition process into a single, jargon-free communication package. It does not produce anything new; it repackages what is already known into the format that non-PM audiences can use.

##### Key Concepts

###### GTM Is a Team Sport

The PM provides information, synthesizes upstream work, and owns the artifact. But they do not build it alone. Sales, marketing, customer support, and technical teams are all stakeholders in the GTM process - they bring the customer-facing context and execution knowledge that the PM does not have from inside the product team. Building this document in isolation produces a document that sounds right but misses what each function actually needs to know.

###### The Persona-Voice Problem Statement

The formal Problem Statement from psk-framing-the-problem uses a structured five-stem format written for product teams. The GTM Problem Statement does something different: it retells the same story in first-person from the customer's perspective, in emotional and accessible language.

The format:
"I am a [role] [doing/struggling with X]. [Pain]. Because [root cause]. Which makes me feel [emotional consequence]."

This reframing is not decoration. Account executives and customer success managers need to feel the customer's pain to communicate it credibly. A business-case summary does not accomplish that. A first-person narrative does.

###### Solution Summary vs. Positioning Statement

These two sections serve different purposes and must not be collapsed into one.

The **Solution Summary** is a plain-language product description. It answers: what is it, what does it do, what does it improve? Drop all PM vocabulary. Write for someone who has never seen the solution hypothesis or the product backlog.

The **Positioning Statement** is the seven-element formula from psk-positioning-statement, written verbatim. This is the structured messaging foundation that all other messaging is derived from. Paraphrasing it loses precision. The seven elements are:
- For: [target customer]
- Who: [need or opportunity]
- The: [product name]
- Is a: [category]
- That: [key benefit - a customer outcome, not a feature]
- Unlike: [primary competitive alternative]
- Our product gives: [primary differentiation - outcome language]

###### Key Messages Are Benefit Statements, Not Feature Lists

The Key Messages table is where each persona learns what is in it for them. This is not a feature brief. Features describe what the product does. Benefits describe what the customer gains. "Automated case routing" is a feature. "Time back to focus on complex cases instead of sorting tickets" is a benefit.

Write 3-5 bullet points per persona. Each bullet answers: what does this change for me, in my role, in my day? If the answer could come from a product spec, it is a feature - rewrite it as an outcome.

###### Every Message Needs Proof

A key message without proof is a claim. Each message gets **proof points the persona would trust**: a testimonial, a pilot result, a case study, a published benchmark. Proof must be real. Proof the team doesn't have yet goes in the Proof Points column with the exact label `To gather:` followed by the kind of proof needed (for example, `To gather: pilot-site quote on status calls`). Never invent it.

Messages are written for **at least one user and one buyer persona**. A buyer usually cares about different outcomes than a user, so if the user and buyer messages overlap heavily, one of them is probably generic. Every message traces back to the positioning statement.

###### Readiness Goals vs. Launch Goals

**Readiness goals** prove the product is ready to ship, measured in a limited pre-release test (Product Readiness Testing). **Launch goals** prove the go-to-market plan worked, measured in the market after release. A goal that belongs to readiness doesn't belong here. A **launch task** ("train the sales team," "publish the web page") isn't a goal either. Ask what result the task should produce.

###### Launch Goals vs. Product Success Metrics

Launch Goals are not the same as the ongoing metrics from psk-outcome-tree or psk-measuring-outcomes. Launch Goals are time-bounded success indicators for the launch window itself: adoption milestones, satisfaction scores, and efficiency gains that confirm the launch executed correctly.

Each row in the Launch Goals table requires a numeric target. "Improve satisfaction" is not a launch goal. "Achieve NPS of 40+ in first 90 days post-launch" is a launch goal. Each target also needs a basis (a baseline, a benchmark, or evidence), a measure the team can actually collect, and a tie to a business or product outcome. **The targets are the PM's to set.** The skill questions whether they are realistic; it does not pick the number.

###### Jargon-Free Writing

This artifact must be readable without a PM dictionary. Every sentence should pass this test: could an account executive read this aloud to a prospect without having to explain a term? Technical vocabulary (API integrations, workflow automation pipelines, orchestration layers) fails that test. Customer-benefit language (faster order processing, fewer manual steps, real-time visibility) passes it.

###### The GTM Timing Arc

Go-to-Market preparation is not a one-week sprint before launch. The typical arc:
- Develop the GTM plan: 1-2 months before launch
- Review and align with stakeholders: 2-6 months before launch
- Drive internal awareness across functions: ongoing during the build phase
- Generate partner awareness: 2-4 months before launch
- Drive market awareness: 1-3 months before launch
- Launch date with press release or announcement: the milestone everything else builds toward

Starting late on GTM preparation is the most common failure mode. This artifact should be in circulation well before the launch date, not assembled in the final week.

###### How AI Supports This Play

The Playbook casts AI as a **critic of the two parts the PM writes fresh here**: key messages with proof points, and launch goals. For messages, AI checks that each is a benefit, free of jargon, and backed by proof the persona would trust. For launch goals, it tests the measure and whether the target is realistic, and keeps launch goals distinct from readiness goals. The messages and targets stay the PM's. AI cannot know what the buyers trust or what the business can hit.

- **Use it when:** positioning and personas are set, and the PM has drafted key messages, proof points, and launch goals to pressure-test.
- **Avoid it when:** positioning or personas are still unsettled (route to psk-positioning-statement or psk-proto-persona), or the request is for AI to set the targets. It has no data on the market or the business.
- **Return:** messages tested for benefit, jargon, and credible proof; launch goals checked for measure, realistic target, and timeframe; and proposed rewrites for the PM to accept, adapt, or reject.

###### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

###### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

##### Application

Use [Template](playbook-skills.md#psk-go-to-market--template) for the scaffold.


###### Required Output Convention

Default to a **clean, paste-ready artifact**.

That means:

- all six sections completed
- Problem Statement in first-person persona voice, not third-person business case
- Positioning Statement in the exact seven-element formula
- Key Messages written as benefit bullets per persona, not feature descriptions
- Launch Goals table with numeric targets in every row
- no PM or technical jargon visible to a non-PM audience
- commentary and explanation belong below the artifact, not inside the fields

###### Step 1: Tech-Role Bias Guard

Before writing any content, confirm who the product serves. LLMs and PMs alike default toward technical vocabulary and engineering-adjacent framing. The Key Messages in particular must be written from the customer's perspective on what changes for them, not from the product team's perspective on what they built.

Ask explicitly: who are the 2-3 personas this product serves? What is their job? What frustrates them? What do they gain? These answers govern the language in every section, especially Key Messages.

If the user's initial framing focuses on capabilities ("what the platform does") rather than customer gains ("what changes for the customer"), surface that and redirect before drafting.

###### Step 2: Gather Upstream Artifacts

Before drafting, ask whether the user has these materials to share:

- Problem framing from psk-framing-the-problem (five-stem format, for translation to persona voice)
- Solution hypothesis from psk-solution-hypothesis (for the Solution Summary)
- Positioning statement from psk-positioning-statement (for verbatim copy into the Positioning Statement section)
- Persona work from psk-proto-persona (identifies the personas for Key Messages and Target Audience)

Use whatever the user can provide. If a section has no upstream source, draft from context and flag it for review. Do not gate the skill on whether all upstream plays have been run.

###### Step 3: Optional Web Research

Web research is appropriate for this skill when it helps with:

- Competitive landscape: understanding what alternatives exist for the "Unlike" element and how to differentiate the Key Messages from competitor positioning
- Market segment context: knowing the size and characteristics of target segments for the Target Audience section
- Industry launch timing norms: understanding whether 1-2 months of GTM prep is typical or compressed for this market

Do not use web research to substitute for customer discovery. If the user lacks a clear problem statement or persona definition, the answer is to run upstream skills, not to fill the gap with market research.

###### Step 4: Write the Problem Statement in Persona Voice

Translate the formal five-stem Problem Statement (from psk-framing-the-problem, or from the user's description if that play has not been run) into a first-person narrative from the customer's perspective.

Use the scaffold:
"I am a [role] [doing/struggling with X]. [Pain]. Because [root cause]. Which makes me feel [emotional consequence]."

The voice should be specific to the persona's role and daily experience. It should be vivid enough that a sales person reading it thinks: "yes, I've heard this from customers."

Check: is this written from the customer's perspective, or from the PM's perspective on the customer? If the PM is the narrator, rewrite it.

Target length: 50-80 words.

###### Step 5: Write the Target Audience Section

Answer three questions in prose:

1. Who is the target customer? (the decision-making unit or the customer type, not a segment label)
2. Who are the product personas? (the named roles from proto-persona work)
3. What are the target market segments? (verticals, company sizes, geographies, or use cases the launch is targeting)

Keep this concise - 30-50 words. This is orientation, not a market sizing exercise.

###### Step 6: Write the Solution Summary

Write a plain-language description of the product: what it is, what it does, what it improves. This is not the hypothesis format (If/Then). It is not the positioning statement. It is a product description in ordinary language.

Test: could a customer support rep read this out loud and explain the product to a customer calling in for the first time? If technical vocabulary appears, rewrite it.

Target length: 40-60 words.

###### Step 7: Write the Positioning Statement

Copy the seven-element Positioning Statement verbatim from the psk-positioning-statement output if available. If not, construct it using the formula:

For: [target customer]
Who: [statement of need or opportunity]
The: [product name]
Is a: [product category]
That: [key benefit - customer outcome, not a feature]
Unlike: [primary competitive alternative]
Our product gives: [primary differentiation - outcome language]

Do not paraphrase. Do not combine elements. Do not drop the "Unlike" element because it feels uncomfortable. The formula's precision is the point.

Target length: 60-90 words for the full statement.

###### Step 8: Write Key Messages for Each Persona

**The PM drafts the messages; the skill critiques them** (mirrors the critique guidance in this Play). Working one persona at a time:

1. Confirm there is at least one user and one buyer persona. If not, ask who uses the product and who decides to buy it.
2. Check each message is a benefit this persona cares about. If it's a feature, ask "so that what?" until the PM reaches the benefit.
3. Check each message traces to the positioning statement, and point at any that drift.
4. Flag jargon that sales, marketing, or support could misread, or that this persona would never say.
5. For each proof point, ask whether this persona would trust it and whether it really backs the message. Point at any message with no proof behind it.
6. Show where user and buyer messages overlap.
7. Then propose rewrites, explaining what each one changes and why. Wait for the PM's answers before rewriting.

Do not invent personas, quotes, testimonials, test results, or data as proof. You may suggest **types** of proof the PM could gather, labeled as proof still needed. If the PM asks you to draft messages, or chooses Discovery mode, draft them tagged `[AI-SUGGESTED, VALIDATE THIS]` with every proof cell marked as proof still to gather.

Build the Key Messages table with one row per persona (2-3 personas typical). For each persona, write 3-5 bullet points that answer: what is in it for this person? Pair the messages with their **proof points**.

Each bullet is a benefit statement:
- It names what changes in the customer's work, not what the product does
- It uses the customer's language, not product vocabulary
- It is specific enough that this persona would recognize their own situation in it

If a bullet could appear in a product spec or a feature announcement ("real-time data sync"), it is a feature - rewrite it as a customer gain ("always current information, no manual refresh").

###### Step 9: Write Launch Goals

**The PM drafts the goals and sets the targets; the skill questions them** (mirrors the critique guidance in this Play). One goal at a time:

1. Does the goal belong to launch, or to readiness? If it proves the product is ready to ship, say so.
2. Is it really a launch task (train sales, publish a page)? If so, ask what result that task should produce.
3. Does it tie to a business or product outcome the PM gave you? Point at any that don't.
4. Can the measure actually be collected? Ask where the data will come from.
5. Test the target: does it have a number and a timeframe, and is it realistic? Ask what baseline, benchmark, or evidence it rests on. If it looks too aggressive or too timid, say why, without picking the number.
6. Then propose tighter wording for each goal, measure, and target.

Do not invent baselines, benchmarks, or market data, and do not choose the targets. In Discovery mode, leave targets as `[PM TO SET]` with a note on what baseline would anchor them.

Build the Launch Goals table with 3-4 rows. Each row covers one success goal for the launch window.

Each row requires:
- Goal/Objective: the named success area (adoption, satisfaction, onboarding efficiency, etc.)
- Measure/Metric: the specific thing being measured (NPS, activation rate, time to first value, etc.)
- Target: a number or percentage (not "improve" or "increase")

These are launch-window metrics, not long-term product success metrics. They confirm the launch executed correctly. The time horizon is typically 30-90 days post-launch.

###### Step 10: Jargon Check

Read back through the completed artifact and flag any vocabulary that a sales director, marketing manager, or customer support lead might not understand without a PM glossary. Common offenders:

- Technical terms: API, orchestration, pipeline, integration layer, real-time sync engine
- PM vocabulary: hypothesis, assumption, outcome tree, solution space, JTBD
- Compound jargon: "automated workflow automation platform" (redundant and opaque)

Rewrite flagged phrases in plain language. The test is: would a new account executive on their second week understand this without asking what it means?

###### Step 11: Offer Next Steps

At the end of the artifact, offer the user three options:

1. Share with sales leadership for review and input on Key Messages - the sales team will flag whether the benefit bullets match what they hear from customers
2. Share with marketing to align on the Positioning Statement as the messaging anchor for launch campaigns
3. Schedule a launch readiness review with all GTM stakeholders to walk through the artifact together and confirm each function knows what they need to execute

#### psk-go-to-market / Template

###### When to Use This

Use this template during the **Create phase** after completing positioning, solution hypothesis, and proto-persona work. Run it collaboratively with sales, marketing, and customer support stakeholders before setting the launch timeline.

Upstream artifacts that feed this template:
- Problem framing (psk-framing-the-problem): provides the five-stem structure to translate into persona voice
- Solution hypothesis (psk-solution-hypothesis): provides the solution framing for plain-language translation
- Positioning statement (psk-positioning-statement): provides the seven-element formula to copy verbatim
- Proto-persona (psk-proto-persona): identifies the personas and their pains for Key Messages and Target Audience

###### Template

```markdown
# Go-to-Market Enablement

## Product Context

- Product or initiative:
- Launch target date:
- GTM participants and functions represented:
- Date prepared:

---

## Section 1: Problem Statement

Write this section in first-person from the customer's perspective.
Use this scaffold: "I am a [role] [doing/struggling with X]. [Pain]. Because [root cause]. Which makes me feel [emotional consequence]."

[Write the persona-voice Problem Statement here]

> Quality check: Is this written in first-person from the customer's perspective, not as a business case summary?
> Quality check: Does it name a specific role, a specific pain, a root cause, and an emotional consequence?
> Quality check: Could a sales representative read this aloud and recognize it as something a customer would actually say?
> Capacity check: 50-80 words. This is a narrative, not a sentence.

---

## Section 2: Target Audience

Answer these three questions in prose:
- Who is the target customer?
- Who are the product personas?
- What are the target market segments?

[Write the Target Audience paragraph here]

> Quality check: Are the personas the people who use or buy the product - not the PM or the product team?
> Quality check: Are market segments specific enough to guide a sales territory or a marketing campaign?
> Capacity check: 30-50 words. This is orientation, not a market analysis.

---

## Section 3: Solution Summary

Write a plain-language description of the product: what it is, what it does, what it improves.
Do not use the If/Then hypothesis format. Do not use product jargon, technical vocabulary, or PM terminology.

[Write the Solution Summary here]

> Quality check: Could a customer support representative read this aloud to a customer who has never heard of the product?
> Quality check: Is every technical or PM term translated into plain language a non-PM would understand?
> Capacity check: 40-60 words.

---

## Section 4: Positioning Statement

Use the seven-element formula verbatim. Do not paraphrase or combine elements. Do not omit the "Unlike" element.

For: [target customer]
Who: [statement of need or opportunity]
The: [product name]
Is a: [product category]
That: [key benefit - a customer outcome, not a feature]
Unlike: [primary competitive alternative - name it, including "spreadsheets and manual processes" if that is the real alternative]
Our product gives: [primary differentiation - outcome language, not feature language]

> Quality check: Does "That" describe what the customer gains, not what the product does?
> Quality check: Does "Unlike" name a real alternative that customers would actually choose instead?
> Quality check: Does "Our product gives" use outcome language, not feature language?
> Quality check: Are all seven elements present and clearly distinct?
> Capacity check: 60-90 words for the full statement.

---

## Section 5: Key Messages

Complete one row per persona (2-3 personas typical), with at least one user and one buyer. Each bullet answers: what is in it for this person?
Write benefit statements - what changes for the customer - not feature descriptions - what the product does. Back each persona's messages with proof points they would trust.

| Persona | Key Messages | Proof Points |
|---------|-------------|--------------|
| [User persona] | - [Benefit bullet: what changes for this person in their work] | - [Proof this persona would trust, or "To gather: ..."] |
| | - [Benefit bullet] | - [Proof] |
| | - [Benefit bullet] | |
| | - [Benefit bullet] | |
| [Buyer persona] | - [Benefit bullet] | - [Proof] |
| | - [Benefit bullet] | - [Proof] |
| | - [Benefit bullet] | |
| | - [Benefit bullet] | |
| [Persona 3 role, if applicable] | - [Benefit bullet] | - [Proof] |
| | - [Benefit bullet] | |
| | - [Benefit bullet] | |

> Quality check: Is every bullet written from the customer's perspective on what they gain, not from the product team's perspective on what they built?
> Quality check: Would these bullets survive the "so what?" test? ("Automated routing" -> so what? -> "no more manual decisions on every order" -> that is a benefit)
> Quality check: Does each persona row address that persona's specific concerns, not a generic product overview?
> Quality check: Is there at least one user and one buyer persona? Do their messages differ?
> Proof check: Is every proof point real (testimonial, pilot result, case study, benchmark)? Mark proof you don't have yet "To gather." Never invent it.
> Capacity check: 3-5 bullets per persona, 10-15 words each.

---

## Section 6: Launch Goals

Complete 3-4 rows. These are launch-window success metrics, not long-term product success metrics.
Every Target cell must contain a number or percentage - not "improve" or "increase."

| Goal/Objective | Measure/Metric | Target |
|----------------|----------------|--------|
| [Named success area for the launch window] | [Specific thing being measured] | [Number or percentage] |
| | | |
| | | |
| | | |

> Quality check: Is every Target cell numeric or percentage-based? If it says "improve" or "increase," it is not a target.
> Quality check: Are these launch-window metrics (30-90 days post-launch), not long-term product metrics?
> Quality check: Is each a launch goal (the market responded), not a readiness goal (ready to ship) or a launch task?
> Quality check: Does every target rest on a baseline, benchmark, or evidence, with a measure someone can actually collect?
> Quality check: Is each Goal/Objective a named success area, not a vague aspiration?
> Capacity check: Goal/Objective ~5-8 words; Measure/Metric ~5-10 words; Target ~3-8 words including the number.

---

## Next Steps

- [ ] Share with sales leadership for Key Messages review
- [ ] Share with marketing as the messaging anchor for launch campaigns
- [ ] Schedule launch readiness review with all GTM stakeholders
```

###### Usage Guidance

###### Filling the Template

1. Complete **Product Context** to anchor who participated and what the launch timeline is.
2. Write the **Problem Statement** last, after reading the framing from psk-framing-the-problem. Translate from analytical to emotional and first-person.
3. Write **Target Audience** from the proto-persona work - personas should match what has already been validated.
4. Write the **Solution Summary** as if explaining the product to a new support hire on day one.
5. Copy the **Positioning Statement** verbatim from psk-positioning-statement output. If that play has not been run, construct it fresh using the formula.
6. Build **Key Messages** persona by persona. Start with the primary user, then the buyer, then any other affected roles.
7. Set **Launch Goals** by working backward from the launch date - what does success look like at 30, 60, and 90 days?

###### What Goes Where

| Section | Contains | Does NOT Contain |
|---------|----------|-----------------|
| Problem Statement | First-person customer narrative with emotion | Third-person business case language |
| Target Audience | Named personas and market segments | The PM or product team as the audience |
| Solution Summary | Plain-language product description | Technical vocabulary, PM jargon, hypothesis format |
| Positioning Statement | Seven-element formula verbatim | Paraphrasing, narrative description, incomplete elements |
| Key Messages | Benefit bullets per persona | Feature descriptions, capability lists |
| Launch Goals | Numeric targets for the launch window | Directional language without numbers, long-term metrics |

###### Connecting to Other Skills

- **Upstream:** psk-framing-the-problem provides the Problem Statement structure for translation. psk-proto-persona provides the personas. psk-solution-hypothesis provides the solution framing. psk-positioning-statement provides the Positioning Statement verbatim.
- **Downstream:** This skill is an endpoint. The artifact feeds into sales enablement, marketing campaigns, and launch readiness reviews - but no other playbook skills consume it.

###### Capacity Reference

| Field | Target Length | Guidance |
|-------|--------------|----------|
| Problem Statement | 50-80 words | First-person narrative, specific and emotional |
| Target Audience | 30-50 words | Prose paragraph, orientation not analysis |
| Solution Summary | 40-60 words | Plain product description, no jargon |
| Positioning Statement | 60-90 words | Seven elements verbatim, all required |
| Key Message bullet | 10-15 words | Benefit, not feature; customer perspective |
| Launch Goal/Objective | 5-8 words | Named success area |
| Measure/Metric | 5-10 words | Specific, countable signal |
| Target | 3-8 words | Number or percentage required |

#### psk-go-to-market / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** Separate messages for field technicians and operations managers; connect each message to that persona's problem and an evidenced benefit.
- **Weak:** One generic feature announcement gives sales no customer-specific reason to care.
- **Drift to avoid:** Invented proof: do not add fabricated testimonials or launch results to make the message persuasive.


##### Common Pitfalls

- **Problem Statement Written in Third-Person Business Case Voice:** Rewrite in first-person from the customer's perspective using the scaffold: "I am a [role]... [pain]. Because [root cause]. Which makes me feel [emotion]." The voice must come from the customer's experience, not the PM's analysis of it.

- **Key Messages That List Features Instead of Benefits:** For each bullet, ask "so what?" until you reach a customer outcome. "Automated order routing" becomes "orders routed to the right warehouse without manual intervention, so coordinators focus on exceptions rather than every transaction."

- **Positioning Statement Paraphrased or Incomplete:** Use the seven-element formula verbatim: For / Who / The / Is a / That / Unlike / Our product gives. Every element must appear. The "Unlike" element must name a real alternative (including "manual processes using spreadsheets" if that is the real competitor).

- **PM Builds the Artifact Alone:** Treat the artifact as a starting draft for collaborative review, not a finished deliverable. Share it with each function and explicitly ask: "Is this how you would describe the customer's problem? Does this messaging match what you hear in the field? What would you add or change?"

- **Launch Goals Are Directional Instead of Numeric:** Every Target cell in the table must contain a number or percentage. "Improve user adoption" becomes "75% of licensed users complete onboarding within 14 days of provisioning."

- **Solution Summary Filled with Product Jargon:** Write a product description that your best customer could read aloud to a colleague. Test it against the question: "could a new account executive on their second week explain this to a prospect?" If not, simplify.

- **Key Messages Written for Only One Persona:** Build Key Messages for each distinct persona: at minimum the primary user and the economic buyer. If the product serves three distinct roles, write three rows.

- **Tech-Role Bias in Key Messages:** Apply the perspective test to every bullet. Ask: who is the subject of this sentence? If it is the product, the platform, or the system, the bullet is a feature. If it is the customer and what they can now do or stop doing, it is a benefit. Rewrite every technical subject into a customer subject.

- **Claims With No Proof Behind Them:** Every message gets proof the persona would trust, or the proof is listed as "still to gather before launch." Never invent testimonials, quotes, or results.

- **Goals That Prove Nothing:** Keep only goals that show the market responded. Move readiness goals to Product Readiness. Turn tasks into the result they should produce. Give every target a baseline or evidence, a measure someone can collect, and a timeframe.

##### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-go-to-market) for supporting source material and expanded examples.


### Play 21: Product Readiness Testing

Stable identifier: `psk-product-readiness`.

#### psk-product-readiness / Instructions

##### Purpose

Create a **Productside-style Product Readiness artifact** from a structured pre-launch test plan.

This skill helps a Product Manager plan and document a beta program that validates the product with real customers before market release. The output is a three-section artifact: a Test Plan (who, how many, how long, and which team roles), a Goals table (objectives, metrics, and numeric targets), and an Assumptions and Risks section (honest documentation of what the test does not cover).

This skill belongs to the **Create phase** and marks a Key Decision Point. The results of the readiness test feed the final Go/No Go decision before launch. The playbook is explicit: **do not be afraid to stop a launch if the product is not ready.** A No Go outcome is a valid and sometimes correct result, not a failure.

Use this skill when you need to:
- design a beta test plan with real customers before committing to market launch
- define Go/No Go criteria that are locked before the test begins
- assign team roles for the test and document what the test does not cover
- gate entry to the Deliver phase with an explicit readiness decision

This is not a first-contact usability test. If users have never touched the product before, this is not the right play - run lo-fi experimentation or a structured pilot first. This is not a readiness check on the product team's internal processes; it is a validation of the product with real customers in real context.

##### Key Concepts

###### This Is Not the First Time Users Test the Product

Product Readiness Testing is the final validation before market release. It presupposes earlier rounds of testing: lo-fi experimentation, clickable prototype feedback, pilot access, and discovery work with real customers. If this is the first time users are touching the product, the team is using Product Readiness Testing to do work that should have been done months earlier.

Before planning the readiness test, confirm that earlier testing has occurred. If it has not, the better next step is lo-fi experimentation or a structured pilot, not a readiness test.

###### Readiness Testing Also Catches Technical Issues Before Launch

Beyond the Go/No Go decision, the readiness test is an opportunity to surface bugs, defects, and configuration failures in a controlled setting before they reach the full market. When participants encounter a broken workflow, a missing integration, or unexpected system behavior, that is signal  -  not noise.

This is one reason a dedicated technical support person on the test team is not optional. Bugs surface during real customer use in ways that internal QA and staging environments cannot predict. A readiness test with real participants using the product in their actual context will expose failure modes that controlled testing misses.

Log every technical issue that surfaces during the program, triage severity, and track resolution before the Go/No Go call. A test that produces a clean set of found-and-fixed issues alongside quantitative goal results is a stronger foundation for a launch decision than metrics alone.

###### Define Success Before Running the Test

Before the test starts, the PM and team must agree in writing which goals are must-pass and which are aspirational. This pre-commitment prevents post-hoc rationalization: the team cannot look at mixed results and convince themselves the test passed because two out of four goals were met.

A Go/No Go decision is only credible if the criteria were locked before anyone saw results.

###### Three Sections, Three Purposes

- **Test Plan (left side):** who participates, how many, how long the test runs, and who on the team is responsible for what. Each question has a specific structural answer, not a generic placeholder.
- **Goals Table (right side):** four to five rows, each naming a specific objective, the metric used to measure it, and a numeric or percentage target. "Improve satisfaction" is not a goal for this table. "User satisfaction score of 4.2 or above on post-use survey" is.
- **Assumptions and Risks (bottom, full width):** an honest, named list of what the test does not cover and why. This section tells stakeholders where the test has known limits. Leaving it blank implies the test covers everything, which it never does.

###### Who to Test With: Profiles, Not Just Job Titles

Customer profiles for the test should describe real-context participation: role, company type, experience level, and what they represent. "HR manager" is a job title. "HR operations manager at a mid-market company (200-500 employees) with no dedicated HR technology team, responsible for manual payroll and benefits administration" is a profile. The difference matters because the profile determines whether the test is exposing the right failure modes.

###### The Goals Table Requires Numeric Targets

Each row in the Goals table must have a number. The target cell is not a description of the direction of improvement. It is the threshold that defines whether the goal was met. Without a number, the team cannot make a clean Go/No Go call.

Canonical goal categories from the playbook: workload reduction, user satisfaction, self-service adoption rate, system uptime.

###### Assumptions and Risks Documents Scope Limits

Every beta program has constraints: limited training, incomplete integrations, specific user populations that are not representative of the full market, features that are intentionally excluded from the test. Document them explicitly. This protects the team from being held accountable for failures that were known to be outside the test scope, and it signals to stakeholders where follow-up validation is still needed.

###### Quotes Are a Deliverable

The playbook says: "Remember to gather quotes from the test program to use during the official launch." The readiness test is an opportunity to collect memorable user statements that can be used in launch communications, internal presentations, and sales conversations. Designate someone on the test team to capture quotes as the test runs. This is not optional.

###### The Test Team Has Distinct Roles

Three functions matter in a readiness test: the PM (leads the test and owns the Go/No Go call), the account or client contact (manages participant expectations and relationship), and a technical support person (handles bugs and configuration issues as they surface). If no one is assigned to technical support, participants hit problems with no one to triage them, and the test collapses into a support event rather than a learning event.

###### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **critic of the readiness test plan the PM drafted**. It checks that participants are defined by profile, that goals have numeric targets resting on a baseline, that Go/No Go criteria are committed before the test, and that quote capture is planned. The targets and the Go/No Go criteria are the PM's to set.

- **Use it when:** the PM has a draft readiness test plan and wants it pressure-tested before the test starts.
- **Avoid it when:** the request is to set the Go/No Go thresholds, or to predict how participants will react. Even when asked to "just pick numbers," leave each threshold `[PM TO SET]`, name the baseline or evidence that would anchor it, and help structure the criteria (measure, threshold, basis). Even once the PM has baselines, don't offer to propose the numbers: show how each baseline narrows the choice, and leave the number to the PM.
- **Return:** participant profiles sharpened, each goal checked for a measure and a baseline, Go/No Go criteria tested for whether they would really stop a launch, and gaps in quote capture and scope flagged.

###### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

###### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

##### Application

Use [Template](playbook-skills.md#psk-product-readiness--template) for the scaffold.


###### Required Output Convention

Default to a **clean, paste-ready artifact**.

That means:

- all four Test Plan questions answered with specific content
- Goals table with 4-5 rows, each including a numeric target
- Go/No Go criteria explicitly named (which goals are must-pass)
- Assumptions and Risks section with 3-5 specific, named scope limits
- Quote capture plan mentioned or integrated into the team roles section
- explanation belongs below the artifact, not inside the fields

###### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses Discovery mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

###### Step 1: Tech-Role Bias Guard

Before drafting, confirm who the product actually serves. Beta testers must represent the actual customer population, not internal technical users unless the product is built for technical users.

Common failure: a product for field service technicians, warehouse supervisors, or HR administrators is tested by the engineering team, the QA team, or internal operations staff who are familiar with the product. These users do not expose the failure modes that matter to the real customer: unfamiliar workflows, different mental models, limited training, and domain-specific constraints.

Ask: "Who is the customer who will use or buy this product in the field?" The answer to that question defines who must be in the test. If the answer is not the same as the people currently on the tester list, name the gap.

###### Step 2: Gather Upstream Artifacts

Before drafting the readiness test plan, ask whether the user has:

- Solution hypothesis from psk-solution-hypothesis (defines what is being validated)
- Product success metrics from psk-outcome-tree (provides the measurable targets the test should confirm)
- Risk assessment from psk-risk-assessment (surfaces known risks that may affect the test or its scope limits)
- Persona profiles from psk-proto-persona (helps define who to recruit for the test)

Accept equivalent information from any source. The PM may already know their beta user pool independently. If upstream artifacts are not available, work with what the PM knows and note where assumptions are being made.

###### Step 3: Define Customer Profiles for the Test

Write a specific description of each type of participant in the test. For each profile:

- Name the role and function (not just the job title)
- Describe the company type and size context
- Note the relevant experience level with the problem or prior tools
- Explain what this participant profile represents in the broader market

If the test includes multiple participant types for comparison (for example, paying customers and internal teams as a control group), describe each type separately and explain what the comparison is designed to reveal.

###### Step 4: Determine Participant Count and Structure

State how many participants will be in the test, broken down by type. The breakdown matters: "8 participants" is less useful than "5 operations managers from mid-market companies and 3 enterprise customers for comparison."

If the product serves multiple segments, the participant structure should reflect which segments are being validated. If the test only covers one segment, name that explicitly as a scope limit in the Assumptions and Risks section.

###### Step 5: Set the Test Duration

Define the test duration in terms that reflect meaningful product use, not just calendar time. Two weeks is meaningful if participants use the product every day. Two weeks is meaningless if participants are expected to use the product once for a monthly process.

Anchor duration to one of three things:
- A product usage cycle (one billing cycle, one reporting period, one scheduling cycle)
- A time box with a minimum usage expectation (three weeks, with at least two full use sessions per week)
- A task completion definition (the test ends when participants have completed the onboarding flow, run their first payroll, or submitted their first order)

Calendar days alone are not sufficient.

###### Step 6: Assign Test Team Roles and Responsibilities

Name specific individuals for each function:

- **Test Lead:** the PM or designated person who runs the test, owns the schedule, and holds the Go/No Go call at the end
- **Account/Client Contact:** the person managing participant expectations, handling scheduling, and maintaining the relationship with beta participants
- **Technical Support:** the person who triages bugs, handles configuration issues, and responds to participant technical questions during the test

Each role should be a named person. If a role is unfilled, name it as an open assignment and flag it as a risk before the test begins.

###### Step 7: Write the Goals Table

For each goal row, provide three things:

- **Goal/Objective:** a specific, named outcome the test is designed to confirm. Not "test the product." Examples: "Confirm the system reduces manual data entry time," "Validate that participants can complete the onboarding flow without support assistance."
- **Measure/Metric:** the specific thing being measured. A survey score, a task completion rate, a time-on-task reading, an error count.
- **Target:** the number or percentage that defines success. "4 out of 5 stars or above," "70% task completion without support," "uptime of 99.5% or higher."

Write 4-5 rows. Cover at least three distinct measurement types: workload or efficiency, user satisfaction or experience, adoption behavior, and system reliability.

###### Step 8: Pre-Commit Go/No Go Criteria

After drafting the Goals table, explicitly name which goals are must-pass and which are aspirational. This step must happen before the test runs.

Format:
- Must-pass goals (all must be met for a Go): [list by row name]
- Aspirational goals (failure does not block Go, but is flagged): [list by row name]

If no pre-commitment is made, the team cannot make a clean Go/No Go call when results are mixed.

###### Step 9: Plan for Quote Capture

Designate one person to collect memorable user statements during the test. Brief them before the test starts on what kinds of quotes are useful: spontaneous reactions to the product, statements about specific pain points resolved, comparisons to prior tools or processes.

Quotes captured during the readiness test can be used in launch communications, internal alignment presentations, and sales conversations.

###### Step 10: Document Assumptions and Risks

Write a bulleted list of what is explicitly not being tested in this program and why. Each bullet should name the specific constraint and the reason it is out of scope.

Examples:
- "Limited employee training on the new platform could slow adoption rates; standardized training materials will not be available until post-launch."
- "Data security testing will be conducted post-readiness due to compliance review timelines."
- "Not all integrations will be tested during this phase; only the primary ERP integration is in scope."
- "The test does not include enterprise customers; segment-specific validation is planned for Q3."

Aim for 3-5 bullets. If the list is empty, that is a signal the test scope has not been fully examined, not that the test covers everything.

###### Step 11: Offer Next Steps

After delivering the artifact, offer three options:

1. Run the test and return with results to complete the Go/No Go decision
2. Carry the readiness test goals and outcomes forward into post-launch retrospective planning
3. Review the Assumptions and Risks section with stakeholders to confirm alignment on scope limits before the test begins

#### psk-product-readiness / Template

###### When to Use This

Use this template when preparing a **pre-launch beta program** to validate the product with real customers before market release. This is a Key Decision Point: the results determine whether to launch (Go) or hold (No Go).

Before running this template, confirm that earlier rounds of user testing have occurred. This is the final validation before launch, not the first time users see the product.

Upstream artifacts that feed this template:
- Solution hypothesis (psk-solution-hypothesis): defines what is being validated
- Product success metrics from psk-outcome-tree: provides measurement anchors for the Goals table
- Risk assessment (psk-risk-assessment): surfaces known risks that may define scope limits
- Persona profiles (psk-proto-persona): helps define who to recruit as beta participants

---

###### Template

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

###### Usage Guidance

###### Filling the Template

1. Complete **Product Context** to anchor the product, stage, and test lead.
2. Answer all four **Test Plan questions** with specific content before planning the test logistics.
3. Write the **Goals table** before recruiting participants. The goals define what the test is designed to measure.
4. Complete **Pre-Committed Go/No Go Criteria** before the test begins. This is the most commonly skipped step.
5. Fill the **Assumptions and Risks section** before finalizing participant communication.
6. Return to complete the **Post-Test Go/No Go Call** after results are in.

###### What Goes Where

| Section | Contains | Does NOT Contain |
|---------|----------|------------------|
| Customer Profiles | Role + company type + experience level + what they represent | Job titles alone |
| How Many | Total count broken down by participant type | A single total number |
| Test Duration | Usage cycle or task completion anchor | Calendar days alone |
| Test Team Roles | Named individuals with specific functions | "The PM" or "the engineering team" |
| Goal/Objective | Specific named outcome the test confirms | Generic placeholders like "test usability" |
| Target | Number or percentage | Directional aspirations |
| Assumptions and Risks | Specific named scope limits with reasons | Blank or generic acknowledgment |

###### Connecting to Other Skills

- **Upstream:** psk-solution-hypothesis (defines what is being validated), psk-outcome-tree (product success metrics), psk-risk-assessment (known risks), psk-proto-persona (who to recruit)
- **Downstream:** Post-launch retrospective; launch communications (customer quotes)
- **Related:** psk-lofi-experimentation (if earlier rounds of user testing have not occurred, use this skill before planning a readiness test)

###### Capacity Reference

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

#### psk-product-readiness / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** A field-service beta plan names real technician participants, workflows, success criteria, health guardrails, and the owner of the Go/No Go call before testing.
- **Weak:** "Try the app and report bugs" does not establish readiness criteria.
- **Drift to avoid:** False readiness: internal checks or plausible simulated results cannot stand in for observed customer testing.


##### Common Pitfalls

- **Testing with Internal Users Only:** The participant list must represent the actual customer population. If internal users are included for comparison, name them as an internal cohort and do not let them substitute for external customer participants. Name this as a risk in the Assumptions and Risks section if external participants cannot be secured.

- **Goals Table Has Directional Aspirations Instead of Numeric Targets:** Every Target cell must contain a number or percentage. "Reduce time spent on monthly reconciliation by 30% or more." "User satisfaction score of 4.0 or above on a 5-point scale." If the team cannot agree on a number before the test, that disagreement is itself a problem to resolve before the test begins.

- **No Pre-Committed Go/No Go Criteria:** After writing the Goals table but before running the test, explicitly name which goals are must-pass. Document it. This pre-commitment is the only thing that makes the Go/No Go call credible.

- **Assumptions and Risks Section Left Blank:** Every readiness test has scope limits. Name them. Incomplete integrations, missing training materials, single-segment coverage, deferred security testing: these are real and nameable. Documenting them is not weakness. It is honesty.

- **This Is the First Time Users Have Tested the Product:** Confirm that earlier testing has occurred before planning a readiness test. If it has not, the better path is lo-fi experimentation (psk-lofi-experimentation) or a structured discovery session, not a formal beta program.

- **Test Duration Defined Only in Calendar Days:** Anchor duration to a product usage cycle ("one full scheduling cycle"), a minimum usage expectation ("three sessions of at least 30 minutes each within the two-week window"), or a task completion definition ("the test ends when participants have completed their first end-to-end workflow"). Calendar time is secondary.

- **No One Assigned to Technical Support:** Name a technical support person before the test begins. This person is on call during the test to triage bugs, resolve configuration issues, and provide participant-facing technical help. If no one can be assigned, name it as a risk in the Assumptions and Risks section and describe the contingency.

- **Forgetting to Collect Quotes:** Designate one person to capture memorable user statements during the test, before it begins. Brief them on what kinds of quotes are useful. Budget time in each participant session to ask open-ended questions that surface quotable responses.

- **Thresholds Nobody Chose:** The PM sets each threshold with its basis. The skill asks what baseline it rests on and whether the team would really stop the launch at that number.

##### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-product-readiness) for supporting source material and expanded examples.


## Deliver


### Play 22: Measuring Outcomes

Stable identifier: `psk-measuring-outcomes`.

#### psk-measuring-outcomes / Instructions

##### Purpose

Create a **Productside-style Measuring Outcomes dashboard** from the Product Manager's Outcome Tree and product analytics baseline.

This is a **Deliver phase** skill. It runs after launch, when real data begins to flow. The dashboard ties each outcome from psk-outcome-tree to specific metrics, named measurement tools, and a baseline - then tracks quarterly and annual updates against that baseline.

The point is not to list every possible metric. The point is to build a focused, regularly updated signal system that tells the PM and senior leadership whether the product is delivering on what it promised. The playbook says this belongs in front of the CEO.

This is a living document, not a one-time artifact. A dashboard that is built at launch and never updated has failed at its job.

###### Usage Notes

- Upstream dependency: psk-outcome-tree (Business Outcome and Product Outcome fields)
- Deliver-phase endpoint: no skills currently feed downstream from this one
- One product outcome per dashboard; multiple dashboards for multiple outcomes
- The two-table structure (Product Success Metrics / Product Health Metrics) is load-bearing - do not conflate the tables
- Baseline data is required before the dashboard is considered active

##### Key Concepts

###### Success Metrics vs. Health Metrics (Load-Bearing Distinction)

These are different things that belong in different tables. Conflating them is the most common failure mode in this play.

**Product Success Metrics** measure progress toward the specific product outcome. They answer: are customers achieving what the product promised them? Examples: reduction in manual data entry, decrease in process cycle time, increase in first-time resolution rates.

**Product Health Metrics** measure the day-to-day operational health of the product itself. They answer: is the product working well and being used sustainably? Examples: system uptime, error rate, feature usage, detection or processing accuracy, support ticket volume, session duration; satisfaction scores such as NPS and CSAT can serve as guardrails here. (The B2B work-in-progress deck's example uses operational health metrics such as uptime, feature usage, and AI detection accuracy.)

A product can show improving success metrics while health metrics deteriorate - and vice versa. This is the key insight the playbook highlights: a PM might see manual tasks drop 40% while CSAT drops sharply, meaning customers are doing less manually but resenting the new system. The dashboard surfaces these contradictions before they become crises.

###### A Success Metric Is a Leading Customer Behavior

A product outcome moves when customers change their behavior. A **product success metric** is a leading indicator: the customer behavior that, when it moves, should pull the business outcome up behind it. Measure the behavior, not just the money that follows.

Three kinds of metric get mistaken for success metrics:

- **Business results** (revenue, churn, margin) are lagging outcomes that point at the business. They belong to the business outcome, not the product success table.
- **Satisfaction or survey scores** are what people *say*. Ask what observable behavior would show the outcome moving. A survey score can back up a behavioral metric, but it shouldn't replace one.
- **Operational plumbing** (uptime, latency, error rate) is a **health** guardrail. Uptime logged as progress is plumbing mistaken for value.

Look for **several** behaviors, not just the obvious one. A metric the skill suggests is a candidate for the PM to judge. And only real data, read by the PM, says whether the outcome was met.

###### Why Both Tables Are Required

The two-table structure is not decorative. It creates deliberate tension:

- Success metrics alone miss adoption and quality signals.
- Health metrics alone miss outcome progress.
- Together, they let the PM spot the pattern where one table improves at the expense of the other.

If a PM only tracks one type, they will be blindsided by the other.

###### The Dashboard Is an Action Trigger, Not Just a Report

Tracking metrics is only the first step. The dashboard's value is realized when the PM and team respond to what the data shows  -  not just observe it.

When success metrics are not moving in the expected direction, that is a signal to investigate: Is the product being used as intended? Is the customer behavior assumption correct? Does the product outcome itself need revision?

When health metrics deteriorate while success metrics improve, that is a signal to diagnose the tradeoff before it compounds. Respond quickly to off-track readings. A dashboard that is reviewed quarterly but prompts no action is a filing exercise. The playbook is explicit: track outcomes and respond quickly when the desired progress is not being made.

###### Baseline Data Is Required, Not Optional

Without a baseline, a metric is an opinion. The PM cannot know whether change is occurring, how much change has occurred, or in which direction - without knowing the starting point.

Baseline data comes from the PM's product analytics, existing reporting tools, or field measurement before or at launch. If baseline data is not yet available at launch, the first priority is collecting it - not filling in the quarterly updates.

###### Measurement Tools Are Named Specifically

"Analytics" is not a measurement tool. Name the actual platform or method: Power BI, Celonis, Qualtrics, Salesforce, Google Analytics, Mixpanel, Amplitude, SQL query from the data warehouse, quarterly user survey. A metric without a named tool is a metric no one will actually collect.

###### One Product Outcome Per Dashboard

The template tracks depth, not breadth. Track one product outcome per dashboard. If a PM has multiple product outcomes, they can run multiple dashboards or track the primary outcome here. Tracking five outcomes on one dashboard produces six rows of numbers that tell no coherent story.

###### The Dashboard Is Updated Quarterly and Annually

The update columns are not aspirational. Set a calendar cadence at the end of this skill session. If no one owns the quarterly update, the dashboard will not be updated, and the investment in building it is wasted.

###### This Builds Directly from the Outcome Tree

The PM should not invent new outcomes for this dashboard. The Business Outcome and Product Outcome fields come verbatim from psk-outcome-tree. If the PM does not have an Outcome Tree, ask for an equivalent statement of what the product is trying to achieve and who benefits.

###### How AI Supports This Play

The Playbook casts AI as a **grader of the metrics the PM drafted**. It sorts them, says which track real customer behavior toward the outcome and which are business results, operational plumbing, or a reflexive satisfaction score, then pushes the PM to imagine behaviors worth watching. What AI cannot do is say the outcome was met. That verdict comes from real data, read by the PM.

- **Use it when:** the PM has product outcomes from the Outcome Tree and wants metrics that prove customers are behaving the way the outcome predicts.
- **Avoid it when:** the product outcome is vague or is really a business outcome. AI will hand over confident metrics aimed at the wrong target. Fix the outcome first (Step 1, or psk-outcome-tree).
- **Return:** each metric sorted into success, health, or business; lagging and lazy metrics sent back for a rethink; and customer behaviors that signal the outcome is moving, as candidates for the PM to judge.

###### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

###### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

##### Application

Use [Template](playbook-skills.md#psk-measuring-outcomes--template) for the scaffold.


###### Required Output Convention

Default to a **clean, paste-ready artifact**.

That means:

- Business Outcome and Product Outcome copied verbatim from the Outcome Tree (or equivalent source)
- 3-4 Product Success Metrics, each specifically named with a directional target
- 3-4 Product Health Metrics, clearly distinct from the success metrics
- Every metric has a named Measurement Tool (no "TBD" or "analytics")
- Every metric has Baseline Data or a concrete plan to collect it
- Quarterly and Annual Update columns left blank (to be filled post-launch)
- A Metric Tension Review note at the end
- Explanation belongs below the artifact, not inside the fields

###### Step 1: Tech-Role Bias Guard

Before drafting, confirm the product outcome describes what the **customer** achieves - not what the engineering team shipped.

Ask: "Does this outcome describe what customers do differently, better, or faster after using the product?"

If the answer is "this describes what we built" or "this describes system capabilities," the outcome needs to be reframed before building the dashboard. A dashboard built on engineering outputs will produce metrics that measure team activity, not customer impact.

###### Step 2: Gather the Outcome Tree

Ask whether the user has a completed psk-outcome-tree artifact. If yes, pull the Business Outcome and Product Outcome verbatim. If not, ask for:

- What business-level outcome is this product trying to drive? (revenue, cost reduction, efficiency, retention - with a specific target if available)
- What does the customer achieve through using the product? (the product outcome - a change in their behavior, capability, or results)

Do not accept generic answers ("improve efficiency"). Push for specific direction, metric, and context.

###### Step 3: Write the Business Outcomes Header

Copy the Business Outcome directly from the Outcome Tree. Do not summarize or reinterpret it. This field shows the causal chain: Business Outcome flows to Product Outcome.

Budget: 15-25 words.

###### Step 4: Write the Product Outcome

Copy the Product Outcome directly from the Outcome Tree. If the PM has multiple product outcomes, ask which one this dashboard will track. Track one.

Budget: 15-25 words.

###### Step 5: Identify 3-4 Product Success Metrics

**The PM drafts the metrics; the skill grades them** (mirrors the critique guidance in this Play). One metric at a time:

1. Ask what customer behavior it captures and how that shows progress toward this specific product outcome.
2. If it's really a business result (revenue, churn), say so. That is a lagging outcome pointing at the business, not a leading product metric.
3. If it's a satisfaction or survey score, push. Ask what observable behavior would show the outcome moving, beyond what people say on a survey.
4. Widen the thinking: what are several different behaviors the PM could measure, not just the obvious one?

Do not choose the metrics or invent numbers. Any metric you suggest is a candidate for the PM to judge. If the PM asks you to propose metrics, or chooses Discovery mode, tag them `[AI-SUGGESTED, VALIDATE THIS]`.

Work with the PM to identify what specific, observable changes would indicate the product outcome is being achieved.

For each metric, ask: "If this product outcome is happening, what would we see in the data?"

Name each metric specifically using this pattern: `[Metric Name]: [specific directional target]`. Example: "Reduce Field Report Errors: decrease submission error rate from 12% to under 3%."

Generic names like "Efficiency" or "User Adoption" are not acceptable. Every metric name should tell someone what is being measured and in which direction.

Cover a range of signals if possible - time savings, error reduction, volume changes, completion and adoption behaviors. Use satisfaction scores only to support a behavioral metric, not in place of one.

###### Step 6: Identify the Measurement Tool for Each Success Metric

For each success metric, name the actual platform or method used to collect the data. Examples: Power BI dashboard, Salesforce report, quarterly CSAT survey, Mixpanel funnel analysis, SQL query from data warehouse.

If no tool is named, no one will collect the data. If the tool is genuinely unknown, flag it as a prerequisite to establish before launch.

###### Step 7: Establish Baseline Data for Each Success Metric

For each success metric, document the current state before or at the point of the product intervention. Examples: "12% error rate as of Q1 2026," "average 4.2 hours per cycle as of March 2026."

If baseline data is not yet available, note what needs to be done to collect it and by when. Do not leave this column blank without a plan. Never fill it with an estimated or invented number; a baseline comes from real data.

Budget: 3-8 words per row (number + unit + timeframe).

###### Step 8: Identify 3-4 Product Health Metrics

Shift to operational health signals. Ask: "If the product is working well and being used sustainably, what would we see in day-to-day data?"

Common health metrics: NPS, CSAT score, churn rate, system uptime percentage, error rate, session duration, DAU/MAU ratio, support ticket volume, time to first meaningful action.

These should be clearly different from the success metrics in Step 5. If a health metric and a success metric are measuring the same thing, one of them is misclassified.

###### Step 9: Identify Measurement Tool and Baseline for Each Health Metric

Same approach as Steps 6 and 7. Name the tool and document the baseline.

If a health metric like NPS is being collected for the first time, the first quarterly update becomes the de facto baseline - note this.

###### Step 10: Review for Metric Tension Patterns

Before presenting the dashboard, review for potential tensions between the two tables:

- Are any success metrics likely to improve in ways that put pressure on health metrics? (e.g., faster throughput could increase error rates)
- Are any health metrics likely to decline if success metrics are pushed aggressively? (e.g., volume increases could strain uptime)

Flag these explicitly. This is the "spot the contradiction" function the playbook calls out. A PM who sees it coming can design for it. A PM who discovers it in Q2 is explaining it to the CEO.

###### Step 11: Offer Next Steps

After delivering the artifact, offer three options:

1. Set a quarterly review cadence - name a specific date for the first update and the person responsible for pulling the data
2. Share the dashboard with senior leadership, including the business outcomes header as context
3. Connect this dashboard back to the Outcome Tree - if metrics are consistently off-target by Q2, consider whether the product outcome itself needs to be revised

#### psk-measuring-outcomes / Template

**Template 22 of 24 | Phase: Deliver | Type: Component**

---

###### Header: Business Outcomes and Product Outcome

**Business Outcomes**

> _Copy the Business Outcome verbatim from your Outcome Tree. This is the business-level goal your product is intended to drive - a specific, measurable direction at the organizational level. Budget: 15-25 words._

[Business Outcome from psk-outcome-tree]

**Quality check:** Does this describe a business-level result (revenue, cost, efficiency, retention) with a measurable direction? If it describes what the product does rather than what the business achieves, revise before proceeding.

---

**Product Outcome**

> _Copy the Product Outcome verbatim from your Outcome Tree. This is what the customer achieves through using the product - the specific change in their behavior, capability, or results. Track one product outcome per dashboard. Budget: 15-25 words._

[Product Outcome from psk-outcome-tree]

**Quality check:** Does this describe what the customer achieves, not what the engineering team shipped? If the subject of this sentence is your product or your team rather than your customer, it needs to be reframed.

---

###### Section 1: Product Success Metrics

Product Success Metrics measure progress toward the specific product outcome above. Each metric answers: are customers achieving what the product promised them?

| Product Success Metric | Measurement Tool | Baseline Data | Quarterly Update 1 | Quarterly Update 2 | Quarterly Update 3 | Annual Update |
|---|---|---|---|---|---|---|
| _[Metric Name: specific directional target. Example: "Reduce Manual Tasks: decrease manual data entry by 40%". Budget: 8-15 words.]_ | _[Name the actual platform or method - Power BI, Celonis, Qualtrics, Salesforce. Not "analytics" or "TBD". Budget: 2-5 words.]_ | _[Current state before or at launch - number, unit, timeframe. Example: "3.2 days average as of Q1 2026". Budget: 3-8 words.]_ | _[Fill post-launch]_ | _[Fill post-launch]_ | _[Fill post-launch]_ | _[Fill post-launch]_ |
| _[Second success metric. Name specifically - what is being measured and in what direction. Budget: 8-15 words.]_ | _[Measurement tool name. Budget: 2-5 words.]_ | _[Baseline number, unit, timeframe. Budget: 3-8 words.]_ | | | | |
| _[Third success metric. Cover a different dimension than rows 1 and 2 - time savings, error reduction, volume changes, or quality. Budget: 8-15 words.]_ | _[Measurement tool name. Budget: 2-5 words.]_ | _[Baseline number, unit, timeframe. Budget: 3-8 words.]_ | | | | |
| _[Optional fourth success metric. Include only if it adds a dimension not covered above. Budget: 8-15 words.]_ | _[Measurement tool name. Budget: 2-5 words.]_ | _[Baseline number, unit, timeframe. Budget: 3-8 words.]_ | | | | |

> **Quality check:** Every metric in this table should change when customers succeed - not when the team ships. If a metric would improve regardless of whether customers are achieving the product outcome, it belongs in the health metrics table or should be removed. Every Measurement Tool cell must name a real tool, not "TBD." Every Baseline Data cell must have a number or a concrete plan to collect one.

---

###### Section 2: Product Health Metrics

Product Health Metrics measure the day-to-day operational health of the product. Each metric answers: is the product working well and being used sustainably?

These are different from Product Success Metrics. Success metrics measure outcome progress. Health metrics measure product performance. If your two tables overlap, one of them is misclassified.

| Product Health Metric | Measurement Tool | Baseline Data | Quarterly Update 1 | Quarterly Update 2 | Quarterly Update 3 | Annual Update |
|---|---|---|---|---|---|---|
| _[Health metric name and directional target. Examples: "NPS: maintain above 40," "System Uptime: 99.5% or higher," "Churn Rate: under 5% monthly." Budget: 3-8 words.]_ | _[Name the actual tool - Qualtrics, Mixpanel, internal monitoring dashboard. Budget: 2-5 words.]_ | _[Baseline at launch or note if first measurement becomes baseline. Budget: 3-8 words.]_ | _[Fill post-launch]_ | _[Fill post-launch]_ | _[Fill post-launch]_ | _[Fill post-launch]_ |
| _[Second health metric. Cover a different dimension - satisfaction, reliability, or usage pattern. Budget: 3-8 words.]_ | _[Measurement tool name. Budget: 2-5 words.]_ | _[Baseline number, unit, timeframe. Budget: 3-8 words.]_ | | | | |
| _[Third health metric. Include at least one early warning indicator - something that would signal deterioration before it becomes a crisis. Budget: 3-8 words.]_ | _[Measurement tool name. Budget: 2-5 words.]_ | _[Baseline number, unit, timeframe. Budget: 3-8 words.]_ | | | | |
| _[Optional fourth health metric. Include only if it signals something the other rows do not. Budget: 3-8 words.]_ | _[Measurement tool name. Budget: 2-5 words.]_ | _[Baseline number, unit, timeframe. Budget: 3-8 words.]_ | | | | |

> **Quality check:** Every metric in this table should measure how the product performs operationally - not what customers achieve through it. If a health metric and a success metric are measuring the same thing, one is misclassified. Include at least one metric that would signal deterioration, not just metrics that track improvement.

---

###### Metric Tension Review

Before sharing this dashboard, check for patterns where improving one metric could put pressure on another:

- Are any success metrics likely to improve in ways that strain health metrics? (Example: pushing volume throughput could increase error rates)
- Are any health metrics likely to decline if success metrics are pushed aggressively? (Example: accelerating onboarding pace could lower CSAT)

_[Note any tensions observed between your two tables. If none are apparent at launch, flag this as something to watch in Q1. A dashboard that never surfaces tension either has no tension to surface, or is not being read carefully enough.]_

---

###### Update Cadence

First quarterly update due: [date]

Owner responsible for pulling data: [name and role]

This dashboard is shared with: [audience - including leadership level]

#### psk-measuring-outcomes / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For utility field maintenance, track customer repair turnaround as a success metric and service reliability as a distinct health metric; identify baselines and measurement tools.
- **Weak:** "Customers are happier" cannot be tracked consistently without a defined measure.
- **Drift to avoid:** Outputs as outcomes: number of features shipped does not show whether technicians resolve faults more effectively.


##### Common Pitfalls

- **Success Metrics and Health Metrics That Are the Same Thing:** Before finalizing, ask: "Do these two tables measure categorically different things?" Success metrics should describe what customers achieve. Health metrics should describe how the product performs operationally. If the two tables could be merged without losing anything, the distinction has not been made.

- **Generic Metric Names:** Use the pattern: `[Metric Name]: [specific directional target]`. "Efficiency" becomes "Reduce Cycle Time: decrease average order processing time from 3.2 days to under 1 day." The metric name should tell someone exactly what to measure and what the target is.

- **No Baseline Data:** Baseline data collection is a prerequisite for the dashboard, not an afterthought. If data is not yet available, identify what needs to be done to collect it before the dashboard is considered active.

- **Measurement Tool Left Blank or Written as "TBD":** Name the actual tool before the dashboard is shared with leadership. If the tool genuinely does not exist yet, establishing it is a prerequisite for the dashboard - not a follow-on task.

- **Metrics That Measure Outputs Instead of Outcomes:** Ask "Does this metric change when customers succeed, or does it change when the team ships?" Output metrics change when the team does something. Outcome metrics change when customers achieve something. Keep outcome metrics in the success table. Move output metrics out entirely or into a separate engineering dashboard.

- **Only Positive Metrics Tracked:** Include at least one metric per table that would signal deterioration: error rate, churn, support ticket volume, CSAT decline. These should be in the health metrics table by design.

- **Dashboard Built Once and Never Updated:** Before the session ends, name a date for the first quarterly update and the person responsible for pulling the data. Add it to a recurring calendar event. The dashboard is not complete until the update cadence is established.

- **Too Many Metrics:** Limit to 3-4 metrics per table, for a total of 6-8 signals. If a metric is not connected to the product outcome or operational health, it does not belong here. Stakeholder-specific metrics belong in stakeholder dashboards, not the outcomes dashboard.

- **Business Outcomes Disguised as Product Success:** Keep business results with the business outcome. For each, ask which customer behavior should move first, and measure that.

- **Health Metrics Posing as Success:** Move operational guardrails to the health table. Success metrics are customer behaviors that lead the outcome.

- **AI Picks the Metrics:** The PM drafts; the skill grades each metric and widens the options. Suggested metrics are candidates the PM accepts or rejects.

##### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-measuring-outcomes) for supporting source material and expanded examples.


### Play 23: Outcome Tree, Section Two

Read Section Two within [the shared Outcome Tree reference](playbook-skills.md#psk-outcome-tree--instructions). The full content is stored once under Context.


### Play 24: Process Retrospective

Stable identifier: `psk-process-retrospective`.

#### psk-process-retrospective / Instructions

##### Purpose

Create a **Productside-style Process Retrospective artifact** from a structured team reflection session.

This is a process skill. The agent helps the PM prepare the session (roster, context, discussion prompts) and document the results after the team meets. The team itself surfaces what went well, what failed, what they are aiming for, and what they are worried about. The agent cannot substitute for that conversation.

This play reviews the **PM process itself** - how the team conducted discovery, framing, validation, and launch - not just what shipped or what engineering delivered. Wind and Anchors items should surface PM-process observations: "Discovery closed before enough customer interviews ran." "Problem statement was not validated with the team before framing began." "The outcome roadmap was never updated after the storyboard changed." These are the items that make a PM-process retrospective distinct from a generic team debrief.

The playbook is direct on two points. First: "Skipping retrospectives reduces the ability for teams to get better together." Second: "Create a safe space for admitting mistakes and learning from failure. Harnessing a growth mindset on the team is the only way to benefit from retros." Both of these are prerequisites, not afterthoughts. A retro run without psychological safety will not surface anything honest. A retro without action items is just a meeting.

Use this skill when you need to:

- close out a phase, launch, or discovery cycle with structured team reflection
- surface what the team learned and what to carry forward
- generate concrete action items with named owners before the next phase starts
- create an honest record of what worked and what failed in the PM process

This is not a software sprint retrospective. The standard agile format (What Went Well / What Didn't / What to Try Next) is a different structure with a different scope. The Productside model uses four named quadrants with a nautical metaphor, reviews the PM process not just delivery outputs, and requires action items with specific owners and dates. If you are running a sprint ceremony, this is the wrong play.

###### Usage Notes

- This is a **process skill** (`type: process`), not a component skill. The agent sets up the session and documents the results. The team runs the actual retrospective.
- Evidence gathering: **neither** - no web research and no upstream artifacts are required. This is an internal team reflection exercise.
- No tech-role bias guard applies here. Step 1 instead confirms the scope and timeframe of the retro.
- Psychological safety is the prerequisite. If the Anchors quadrant is empty or vague, the retro has not worked.
- Action items with owners and dates are the primary deliverable. A retro without them is just a meeting.
- Downstream: psk-risk-assessment - significant Barriers identified in the retro may warrant formal risk planning.

##### Key Concepts

###### The Four-Quadrant Nautical Model

The retrospective is organized around a sailboat illustration that divides the canvas into four quadrants:

**Wind in Our Sails** (upper-left) - past-facing, positive. What has helped the team move forward? What has been successful? What has excited or motivated the team? Items here are honest wins and momentum.

**Beacons on the Horizon** (upper-right) - future-facing, positive. What milestones can the team work toward? What goals are within reach? What can the team get excited about? Items here are forward-looking aspirations and near-term anchors.

**Anchors Holding Us Back** (lower-left) - past-facing, problems. What has dragged the team down? What has prevented progress? When did the team fail or flounder? Items here name specific system and process failures - not individuals.

**Barriers We See Ahead** (lower-right) - future-facing, problems. What will the team need to navigate around? Where might the team get stuck? What problems are likely to get worse? Items here are anticipated obstacles that warrant planning now.

###### The Two Axes

- **Left vs. right**: left quadrants are retrospective (what happened); right quadrants are prospective (what is coming). They require different conversations and different mindsets.
- **Upper vs. lower**: upper quadrants are positive (what is helping and where we are headed); lower quadrants are problems (what is hindering and what lies ahead). Both halves are required.

###### Psychological Safety

Without it, the Anchors quadrant will stay empty or fill with safe abstractions. The team will perform positivity instead of reflection. The PM's job before the session is to create conditions where it is safe to name failures honestly - by name, specifically, without blame attaching to individuals.

The Anchors quadrant is the highest-signal quadrant. If it is empty or vague, the retro has not done its job.

###### The Retrospective Builds Team Communication and Trust

The immediate output of a retro is a set of action items. The downstream output is a team that communicates better and trusts each other more.

When team members share their honest experience  -  what frustrated them, what they got wrong, where the process broke  -  and the team responds with curiosity instead of defensiveness, trust deepens. Engineers who hear the PM name a process failure, designers who hear that a handoff gap hurt the team, cross-functional partners who see that honest reflection is expected here  -  the retro is the practice that makes this kind of candor normal.

Teams that skip retros lose this mechanism. The frustrations remain; the shared understanding that comes from naming them together does not develop. "Skipping retrospectives reduces the ability for teams to get better together"  -  not only because the action items are lost, but because the communication habit that produces them is what builds the team over time.

###### Items Are Sticky-Note Sized

Each quadrant contains short, specific items - 5 to 8 words each. Not paragraphs. Not explanations. "Deployment review had no rollback criteria" is a good item. "Our deployment processes were sometimes inadequate for the complexity of releases" is not. Specificity is the point.

###### Action Items Are the Artifact That Matters

A retro without action items is venting, not improvement. Action items must have:
- An owner (a named person, not "the team" or "engineering")
- A specific action (not "improve communication")
- A date (by when, specifically)

The format is: [Owner] will [action] by [date].

###### Phase Agnosticism

Retrospectives are not only for the end of a project. They can and should run at the end of any phase, sprint, launch, or cycle. The skill works for all of these.

###### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **facilitation coach before the session and recorder after it**. It helps the PM prepare quadrant prompts and protect psychological safety, then turns the team's own items into specific, owned action items. The items come from the team; the agent never writes what the team experienced.

- **Use it when:** the PM is preparing to run a retrospective, or has the team's raw items to organize into action items.
- **Avoid it when:** the request is to write the team's Wind, Anchors, Beacons, or Barriers without a session.
- **Return:** discussion prompts for each quadrant, moves that keep the room safe, and action items with an owner and a date, built only from the team's items.

###### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

###### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

##### Application

Use [Template](playbook-skills.md#psk-process-retrospective--template) for the scaffold.


###### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses Discovery mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

###### Step 1: Confirm Scope and Timeframe

Before any setup, confirm:

- What product, project, feature, or sprint is this retro reviewing?
- What time period does it cover (start date to end date)?
- Is this a phase-end retro, a sprint retro, a post-launch retro, or something else?
- Has the work being reviewed concluded, or is it still in flight?

This grounds every subsequent step. A retro for a two-week sprint looks different from a retro for a six-month launch.

###### Step 2: Set Up the Administrative Section

Fill in the left sidebar:

- **Retrospective for**: the product, project, or feature being reviewed (3-8 words)
- **Date**: the date the session will be or was held
- **Point of Contact roster**: the team roles and their owners. Standard roles include Project Manager, Executive Sponsor, Product Manager, Sales, Marketing, Communications, Operations, Customer Support, Release Engineer, and Legal. Add or remove rows to match the actual team. Each row captures: Role | Name and Title | Other (additional context).

Do not leave the roster blank. Part of the retro's value is that the right people are in the room. An empty roster means no one has decided who those people are.

###### Step 3: Prepare Discussion Prompts for Each Quadrant

Offer the team the three guiding questions for each quadrant. These are not a rigid script - they are entry points.

**Wind in Our Sails:**
- What has helped us move forward?
- What has been successful so far?
- What has excited or motivated us?

**Beacons on the Horizon:**
- What milestones can we work toward?
- What goals do we have?
- What can we get excited about?

**Anchors Holding Us Back:**
- What is dragging us down?
- What has kept us from making progress?
- When did we fail or flounder?

**Barriers We See Ahead:**
- What will we need to navigate around?
- Where might we get stuck?
- What problems might get worse?

Share these prompts with the PM so they can prime the discussion or use them as facilitation aids in the session.

###### Step 4: Provide Note-Taking Guidance

Before the session, brief the PM on item quality:

- Items should be short, honest, and specific - 5 to 8 words each.
- Name the concrete thing, not the abstract category. "Weekly standup ran over 30 minutes and blocked engineering time" is useful. "Communication was poor" is not.
- Items in the Anchors quadrant should name process and system failures, not individuals. "Deployment checklist was not followed for the Oct 3 release" is right. "Alex did not follow the process" is not.
- Both positive and negative quadrants need real content. A full Wind in Our Sails and an empty Anchors is a sign of a safety problem, not a good project.

###### Step 5: Team Runs the Session

This step belongs to the team. The agent pauses here.

The PM facilitates the session, collects items in each quadrant, and captures raw notes. When the session is complete, the PM returns with the raw output and the agent picks up documentation from Step 6.

Offer this handoff explicitly: "Ready to help document the results when the session is done. Share the raw notes from each quadrant when you are back."

###### Step 6: Record Wind in Our Sails Items

From the session output, record 3-5 specific items from the Wind in Our Sails quadrant. Keep each item to 5-8 words. If the raw notes are longer, help the PM compress them without losing the specific observation.

###### Step 7: Record Anchors Holding Us Back Items

From the session output, record 3-5 specific items from the Anchors quadrant. This is the highest-priority documentation step.

If the team's Anchors items are vague ("things were hard sometimes"), flag this before recording. Offer to help the PM work backward to the specific observation: "What specifically was hard? What did 'hard' look like in practice?"

Ensure no item names an individual. If a raw item does, help the PM reframe it toward the system or process: "The approval process requires a 5-day wait with no parallel path" instead of "Jim takes too long to approve things."

###### Step 8: Record Beacons on the Horizon Items

From the session output, record 3-5 items from the Beacons quadrant. If Beacons is empty, prompt the PM: "Did the team surface any goals or milestones they are excited about? Even rough ones count here." A team with no Beacons has no positive forward momentum - that is worth naming.

###### Step 9: Record Barriers We See Ahead Items

From the session output, record 3-5 items from the Barriers quadrant. Note the difference from Anchors: Barriers are anticipated future problems, not past ones. They call for planning, not postmortem.

If items bleed between Anchors (past) and Barriers (future), help the PM sort them. The same root cause can generate both: an Anchor is the past occurrence, a Barrier is the recurrence risk.

###### Step 10: Formulate Action Items

For each Anchor and each Barrier that has a concrete next step, draft an action item. Format: [Owner] will [specific action] by [date].

- Owner must be a named individual, not "the team" or "PM" as a generic.
- Action must be specific enough to verify completion. "Improve the deployment process" is not an action. "Priya will add a rollback checklist to the deployment runbook by Nov 1" is.
- Date must be real. If the PM does not have a date, prompt for one: "What is a realistic deadline for this given the current sprint?"

Produce 1-3 action items minimum. If the team surfaced 5+ Anchors and Barriers but produced 0 action items, something has gone wrong - name that.

###### Step 11: Offer Next Steps

After completing the documented artifact, offer:

1. Share the completed retro with the full team for review - the people in the room should see the documented output before it is filed.
2. Schedule a follow-up check-in at the next logical milestone to review action item progress. A retro with no follow-up is a filing exercise.
3. Note whether any Barriers identified here should feed into a risk assessment (psk-risk-assessment) if they are significant enough to warrant formal mitigation and contingency planning.

#### psk-process-retrospective / Template

###### When to Use This

Use this template to prepare for, run, and document a team retrospective at the end of any phase, sprint, launch, or project. This is a process skill: the PM (or the agent) uses this scaffold to set up and document the session. The team supplies the content in the live discussion.

---

###### Left Sidebar (Administrative)

###### Retrospective For

```
[Product, project, or feature name - 3-8 words]
```

> Quality check: Is this specific enough that a teammate not in the room would know exactly what is being reviewed?

###### Date

```
[Date of the retrospective session]
```

###### Point of Contact

The people in the room for this retro. Add or remove rows to match the actual team.

| Role | Name and Title | Other |
|------|---------------|-------|
| Project Manager | | |
| Executive Sponsor | | |
| Product Manager | | |
| Sales | | |
| Marketing | | |
| Communications | | |
| Operations | | |
| Customer Support | | |
| Release Engineer | | |
| Legal | | |

> Quality check: Is every role either filled or explicitly marked as not applicable? An empty roster means no one has decided who should be in the room.
> Quality check: Are the people listed the ones who actually did the work being reviewed?

###### Action Items

Complete this section after the session. Each item must have an owner, a specific action, and a date.

Format: [Owner] will [specific action] by [date].

```
-
-
-
```

> Quality check: Does every item name a specific person (not "the team")?
> Quality check: Does every item have a concrete completion date?
> Quality check: Is every action specific enough that the owner could verify it is done?
> Capacity check: 15-25 words per action item.

---

###### Main Canvas (Four-Quadrant Discussion Board)

> **Phase gate:** The Left Sidebar (administrative section above) is completed by the PM and agent before the session. The four quadrants below are populated from the team's live discussion  -  not from project documents, history, or agent inference. Do not fill the quadrants before the session. Do not ask the agent to generate quadrant items. These sections belong to the team.

The four quadrants use a nautical metaphor. Upper quadrants are positive (what helps, where we are headed). Lower quadrants are problems (what hindered, what lies ahead). Left quadrants are past-facing (what happened). Right quadrants are future-facing (what is coming).

---

###### Wind in Our Sails (Upper-Left)

*Past-facing, positive. What has helped the team move forward?*

> "What has helped us move forward?"
> "What has been successful so far?"
> "What has excited or motivated us?"

```
-
-
-
-
-
```

> Quality check: Are these specific wins, not generic praise ("good teamwork")?
> Quality check: Does each item name something concrete that actually happened?
> Capacity check: 5-8 words per item (sticky-note sized).

---

###### Beacons on the Horizon (Upper-Right)

*Future-facing, positive. What goals and milestones is the team working toward?*

> "What milestones can we work toward?"
> "What goals do we have?"
> "What can we get excited about?"

```
-
-
-
-
-
```

> Quality check: Are these forward-looking aspirations, not restatements of past wins?
> Quality check: Is at least one item specific enough to know when it is achieved?
> Capacity check: 5-8 words per item (sticky-note sized).

---

###### Anchors Holding Us Back (Lower-Left)

*Past-facing, problems. What has dragged the team down or blocked progress?*

> "What is dragging us down?"
> "What has kept us from making progress?"
> "When did we fail or flounder?"

```
-
-
-
-
-
```

> Quality check: Does each item name a specific event, process failure, or system gap - not an abstraction?
> Quality check: Do any items name individuals? If yes, reframe toward the system or process.
> Quality check: Is this quadrant as substantive as Wind in Our Sails? If it is much shorter, that is a signal of a psychological safety gap.
> Capacity check: 5-8 words per item (sticky-note sized).

---

###### Barriers We See Ahead (Lower-Right)

*Future-facing, problems. What obstacles does the team anticipate in the next cycle?*

> "What will we need to navigate around?"
> "Where might we get stuck?"
> "What problems might get worse?"

```
-
-
-
-
-
```

> Quality check: Are these future-facing? If an item describes something that already happened, it belongs in Anchors.
> Quality check: Are the most significant Barriers candidates for formal risk planning (psk-risk-assessment)?
> Capacity check: 5-8 words per item (sticky-note sized).

#### psk-process-retrospective / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** After a dispatch launch, the team supplies the four nautical quadrants and agrees on actions in the form "[Owner] will [action] by [date]."
- **Weak:** "Communicate better" gives nobody a concrete action or completion point.
- **Drift to avoid:** Boundary violation: the assistant can prepare and document the retrospective but cannot invent the team's reflections before the session.


##### Common Pitfalls

- **Running the Retro Without Psychological Safety:** Before the session, the PM should explicitly frame it as a safe space for naming mistakes. The Anchors quadrant is the measure of whether the safety worked. If it is empty, the session should be reconvened with a different frame - or the underlying safety issues should be addressed before trying again.

- **Items Written as Abstractions Instead of Observations:** Push to the specific observation. "Design review was scheduled with 2 hours notice three times in October" is actionable. "Communication was bad" is not. For every abstract item, ask: what specifically happened? When? What was the concrete effect?

- **Action Items Without Owners or Dates:** Every action item requires a named owner and a specific date. The format is: [Owner] will [specific action] by [date]. If either is missing, the item is not yet an action item.

- **Only the PM Fills In the Template:** The retro must involve the team. The PM can prepare the template and prompts alone (Steps 1-4 above). The content must come from the session. If a live session is not possible, the PM can collect async input from each team member and synthesize it - but solo input is a fallback, not the default.

- **Conflating Anchors and Barriers:** Anchors = what happened in the past that hurt us. Barriers = what we anticipate could hurt us in the future. The same root cause can generate both. Help the team make the cut explicitly: "Was this something that happened, or something you are worried might happen?"

- **Filing the Output Without Following Up on Action Items:** Schedule a check-in at the next milestone to review action item status. Ask whether each item was completed, deferred, or dropped - and why. A retro that generates the same action items twice in a row is a signal that either the action items were not specific enough, or the follow-up structure is broken.

- **Skipping the Beacons Quadrant:** Beacons do not have to be ambitious. Near-term milestones, small wins the team is looking forward to, a specific deliverable they are excited about - all count. Push the PM to ask the team: "What is something in the next cycle we can look forward to?"

- **Making It a Blame Session:** Anchors should name system and process failures, not individuals. "The handoff checklist did not include a sign-off step for the receiving team" names the process gap. "The delivery window was set without engineering input" names the planning failure. Help the PM reframe individual-blame items toward the systemic cause before documenting them.

- **A Retrospective Without the Team:** Prepare the session; record only the team's items. Turn them into action items with an owner and a date.

##### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-process-retrospective) for supporting source material and expanded examples.
