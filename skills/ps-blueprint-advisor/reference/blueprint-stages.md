# Blueprint Phases and Principles (Reference)

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
