---
name: ps-go-to-market
description: >-
  Build a Go-to-Market Enablement artifact that aligns sales, marketing,
  support, and technical teams before launch. Use when the PM needs to
  communicate what is launching, who it is for, why it matters, and what each
  team should say about it, or when asked to write launch messages, add
  testimonials, or set launch goals.
intent: >-
  Help a Product Manager synthesize the outputs of discovery, problem framing,
  solution definition, and positioning into a single launch-ready communication
  package for non-PM audiences. The artifact speaks to account executives,
  marketing directors, and customer support leads - not to engineers or PMs.
type: component
blueprint_stage: Create
best_for:
  - "Translating discovery work into launch materials sales and marketing can act on"
  - "Aligning cross-functional teams on messaging, objection handling, and support readiness"
  - "Preparing internal teams to execute a product launch without additional PM interpretation"
scenarios:
  - "We are launching next quarter and I need to prepare sales and marketing enablement materials"
  - "Help me translate our discovery findings into materials the go-to-market team can use"
---

## Purpose

Create a **Productside-style Go-to-Market Enablement artifact** that prepares internal teams to execute a product launch.

This skill helps a Product Manager translate months of discovery and definition work into six clear sections that sales, marketing, customer support, and technical teams can act on without additional interpretation. It is the bridge between what the PM knows and what the rest of the organization needs to know before launch day.

This is a **Create phase** skill (Template 20 of 24). It is downstream of almost everything - it synthesizes the work of the full discovery and definition process into a single, jargon-free communication package. It does not produce anything new; it repackages what is already known into the format that non-PM audiences can use.

## Key Concepts

### GTM Is a Team Sport

The PM provides information, synthesizes upstream work, and owns the artifact. But they do not build it alone. Sales, marketing, customer support, and technical teams are all stakeholders in the GTM process - they bring the customer-facing context and execution knowledge that the PM does not have from inside the product team. Building this document in isolation produces a document that sounds right but misses what each function actually needs to know.

### The Persona-Voice Problem Statement

The formal Problem Statement from ps-framing-the-problem uses a structured five-stem format written for product teams. The GTM Problem Statement does something different: it retells the same story in first-person from the customer's perspective, in emotional and accessible language.

The format:
"I am a [role] [doing/struggling with X]. [Pain]. Because [root cause]. Which makes me feel [emotional consequence]."

This reframing is not decoration. Account executives and customer success managers need to feel the customer's pain to communicate it credibly. A business-case summary does not accomplish that. A first-person narrative does.

### Solution Summary vs. Positioning Statement

These two sections serve different purposes and must not be collapsed into one.

The **Solution Summary** is a plain-language product description. It answers: what is it, what does it do, what does it improve? Drop all PM vocabulary. Write for someone who has never seen the solution hypothesis or the product backlog.

The **Positioning Statement** is the seven-element formula from ps-positioning-statement, written verbatim. This is the structured messaging foundation that all other messaging is derived from. Paraphrasing it loses precision. The seven elements are:
- For: [target customer]
- Who: [need or opportunity]
- The: [product name]
- Is a: [category]
- That: [key benefit - a customer outcome, not a feature]
- Unlike: [primary competitive alternative]
- Our product gives: [primary differentiation - outcome language]

### Key Messages Are Benefit Statements, Not Feature Lists

The Key Messages table is where each persona learns what is in it for them. This is not a feature brief. Features describe what the product does. Benefits describe what the customer gains. "Automated case routing" is a feature. "Time back to focus on complex cases instead of sorting tickets" is a benefit.

Write 3-5 bullet points per persona. Each bullet answers: what does this change for me, in my role, in my day? If the answer could come from a product spec, it is a feature - rewrite it as an outcome.

### Every Message Needs Proof

A key message without proof is a claim. Each message gets **proof points the persona would trust**: a testimonial, a pilot result, a case study, a published benchmark. Proof must be real. Proof the team doesn't have yet goes in the Proof Points column with the exact label `To gather:` followed by the kind of proof needed (for example, `To gather: pilot-site quote on status calls`). Never invent it.

Messages are written for **at least one user and one buyer persona**. A buyer usually cares about different outcomes than a user, so if the user and buyer messages overlap heavily, one of them is probably generic. Every message traces back to the positioning statement.

### Readiness Goals vs. Launch Goals

**Readiness goals** prove the product is ready to ship, measured in a limited pre-release test (Product Readiness Testing). **Launch goals** prove the go-to-market plan worked, measured in the market after release. A goal that belongs to readiness doesn't belong here. A **launch task** ("train the sales team," "publish the web page") isn't a goal either. Ask what result the task should produce.

### Launch Goals vs. Product Success Metrics

Launch Goals are not the same as the ongoing metrics from ps-outcome-tree or ps-measuring-outcomes. Launch Goals are time-bounded success indicators for the launch window itself: adoption milestones, satisfaction scores, and efficiency gains that confirm the launch executed correctly.

Each row in the Launch Goals table requires a numeric target. "Improve satisfaction" is not a launch goal. "Achieve NPS of 40+ in first 90 days post-launch" is a launch goal. Each target also needs a basis (a baseline, a benchmark, or evidence), a measure the team can actually collect, and a tie to a business or product outcome. **The targets are the PM's to set.** The skill questions whether they are realistic; it does not pick the number.

### Jargon-Free Writing

This artifact must be readable without a PM dictionary. Every sentence should pass this test: could an account executive read this aloud to a prospect without having to explain a term? Technical vocabulary (API integrations, workflow automation pipelines, orchestration layers) fails that test. Customer-benefit language (faster order processing, fewer manual steps, real-time visibility) passes it.

### The GTM Timing Arc

Go-to-Market preparation is not a one-week sprint before launch. The typical arc:
- Develop the GTM plan: 1-2 months before launch
- Review and align with stakeholders: 2-6 months before launch
- Drive internal awareness across functions: ongoing during the build phase
- Generate partner awareness: 2-4 months before launch
- Drive market awareness: 1-3 months before launch
- Launch date with press release or announcement: the milestone everything else builds toward

Starting late on GTM preparation is the most common failure mode. This artifact should be in circulation well before the launch date, not assembled in the final week.

### How AI Supports This Play

The Playbook casts AI as a **critic of the two parts the PM writes fresh here**: key messages with proof points, and launch goals. For messages, AI checks that each is a benefit, free of jargon, and backed by proof the persona would trust. For launch goals, it tests the measure and whether the target is realistic, and keeps launch goals distinct from readiness goals. The messages and targets stay the PM's. AI cannot know what the buyers trust or what the business can hit.

- **Use it when:** positioning and personas are set, and the PM has drafted key messages, proof points, and launch goals to pressure-test.
- **Avoid it when:** positioning or personas are still unsettled (route to ps-positioning-statement or ps-proto-persona), or the request is for AI to set the targets. It has no data on the market or the business.
- **Return:** messages tested for benefit, jargon, and credible proof; launch goals checked for measure, realistic target, and timeframe; and proposed rewrites for the PM to accept, adapt, or reject.

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

See the source play pages in [assets/ps_go_to_market_playbook_pages.pdf](assets/ps_go_to_market_playbook_pages.pdf).

### Required Output Convention

Default to a **clean, paste-ready artifact**.

That means:

- all six sections completed
- Problem Statement in first-person persona voice, not third-person business case
- Positioning Statement in the exact seven-element formula
- Key Messages written as benefit bullets per persona, not feature descriptions
- Launch Goals table with numeric targets in every row
- no PM or technical jargon visible to a non-PM audience
- commentary and explanation belong below the artifact, not inside the fields

### Step 1: Tech-Role Bias Guard

Before writing any content, confirm who the product serves. LLMs and PMs alike default toward technical vocabulary and engineering-adjacent framing. The Key Messages in particular must be written from the customer's perspective on what changes for them, not from the product team's perspective on what they built.

Ask explicitly: who are the 2-3 personas this product serves? What is their job? What frustrates them? What do they gain? These answers govern the language in every section, especially Key Messages.

If the user's initial framing focuses on capabilities ("what the platform does") rather than customer gains ("what changes for the customer"), surface that and redirect before drafting.

### Step 2: Gather Upstream Artifacts

Before drafting, ask whether the user has these materials to share:

- Problem framing from ps-framing-the-problem (five-stem format, for translation to persona voice)
- Solution hypothesis from ps-solution-hypothesis (for the Solution Summary)
- Positioning statement from ps-positioning-statement (for verbatim copy into the Positioning Statement section)
- Persona work from ps-proto-persona (identifies the personas for Key Messages and Target Audience)

Use whatever the user can provide. If a section has no upstream source, draft from context and flag it for review. Do not gate the skill on whether all upstream plays have been run.

### Step 3: Optional Web Research

Web research is appropriate for this skill when it helps with:

- Competitive landscape: understanding what alternatives exist for the "Unlike" element and how to differentiate the Key Messages from competitor positioning
- Market segment context: knowing the size and characteristics of target segments for the Target Audience section
- Industry launch timing norms: understanding whether 1-2 months of GTM prep is typical or compressed for this market

Do not use web research to substitute for customer discovery. If the user lacks a clear problem statement or persona definition, the answer is to run upstream skills, not to fill the gap with market research.

### Step 4: Write the Problem Statement in Persona Voice

Translate the formal five-stem Problem Statement (from ps-framing-the-problem, or from the user's description if that play has not been run) into a first-person narrative from the customer's perspective.

Use the scaffold:
"I am a [role] [doing/struggling with X]. [Pain]. Because [root cause]. Which makes me feel [emotional consequence]."

The voice should be specific to the persona's role and daily experience. It should be vivid enough that a sales person reading it thinks: "yes, I've heard this from customers."

Check: is this written from the customer's perspective, or from the PM's perspective on the customer? If the PM is the narrator, rewrite it.

Target length: 50-80 words.

### Step 5: Write the Target Audience Section

Answer three questions in prose:

1. Who is the target customer? (the decision-making unit or the customer type, not a segment label)
2. Who are the product personas? (the named roles from proto-persona work)
3. What are the target market segments? (verticals, company sizes, geographies, or use cases the launch is targeting)

Keep this concise - 30-50 words. This is orientation, not a market sizing exercise.

### Step 6: Write the Solution Summary

Write a plain-language description of the product: what it is, what it does, what it improves. This is not the hypothesis format (If/Then). It is not the positioning statement. It is a product description in ordinary language.

Test: could a customer support rep read this out loud and explain the product to a customer calling in for the first time? If technical vocabulary appears, rewrite it.

Target length: 40-60 words.

### Step 7: Write the Positioning Statement

Copy the seven-element Positioning Statement verbatim from the ps-positioning-statement output if available. If not, construct it using the formula:

For: [target customer]
Who: [statement of need or opportunity]
The: [product name]
Is a: [product category]
That: [key benefit - customer outcome, not a feature]
Unlike: [primary competitive alternative]
Our product gives: [primary differentiation - outcome language]

Do not paraphrase. Do not combine elements. Do not drop the "Unlike" element because it feels uncomfortable. The formula's precision is the point.

Target length: 60-90 words for the full statement.

### Step 8: Write Key Messages for Each Persona

**The PM drafts the messages; the skill critiques them** (mirrors [prompts/01](prompts/01-pressure-test-messages.md)). Working one persona at a time:

1. Confirm there is at least one user and one buyer persona. If not, ask who uses the product and who decides to buy it.
2. Check each message is a benefit this persona cares about. If it's a feature, ask "so that what?" until the PM reaches the benefit.
3. Check each message traces to the positioning statement, and point at any that drift.
4. Flag jargon that sales, marketing, or support could misread, or that this persona would never say.
5. For each proof point, ask whether this persona would trust it and whether it really backs the message. Point at any message with no proof behind it.
6. Show where user and buyer messages overlap.
7. Then propose rewrites, explaining what each one changes and why. Wait for the PM's answers before rewriting.

Do not invent personas, quotes, testimonials, test results, or data as proof. You may suggest **types** of proof the PM could gather, labeled as proof still needed. If the PM asks you to draft messages, or chooses best guess mode, draft them tagged `[AI-SUGGESTED, VALIDATE THIS]` with every proof cell marked as proof still to gather.

Build the Key Messages table with one row per persona (2-3 personas typical). For each persona, write 3-5 bullet points that answer: what is in it for this person? Pair the messages with their **proof points**.

Each bullet is a benefit statement:
- It names what changes in the customer's work, not what the product does
- It uses the customer's language, not product vocabulary
- It is specific enough that this persona would recognize their own situation in it

If a bullet could appear in a product spec or a feature announcement ("real-time data sync"), it is a feature - rewrite it as a customer gain ("always current information, no manual refresh").

### Step 9: Write Launch Goals

**The PM drafts the goals and sets the targets; the skill questions them** (mirrors [prompts/02](prompts/02-pressure-test-launch-goals.md)). One goal at a time:

1. Does the goal belong to launch, or to readiness? If it proves the product is ready to ship, say so.
2. Is it really a launch task (train sales, publish a page)? If so, ask what result that task should produce.
3. Does it tie to a business or product outcome the PM gave you? Point at any that don't.
4. Can the measure actually be collected? Ask where the data will come from.
5. Test the target: does it have a number and a timeframe, and is it realistic? Ask what baseline, benchmark, or evidence it rests on. If it looks too aggressive or too timid, say why, without picking the number.
6. Then propose tighter wording for each goal, measure, and target.

Do not invent baselines, benchmarks, or market data, and do not choose the targets. In best guess mode, leave targets as `[PM TO SET]` with a note on what baseline would anchor them.

Build the Launch Goals table with 3-4 rows. Each row covers one success goal for the launch window.

Each row requires:
- Goal/Objective: the named success area (adoption, satisfaction, onboarding efficiency, etc.)
- Measure/Metric: the specific thing being measured (NPS, activation rate, time to first value, etc.)
- Target: a number or percentage (not "improve" or "increase")

These are launch-window metrics, not long-term product success metrics. They confirm the launch executed correctly. The time horizon is typically 30-90 days post-launch.

### Step 10: Jargon Check

Read back through the completed artifact and flag any vocabulary that a sales director, marketing manager, or customer support lead might not understand without a PM glossary. Common offenders:

- Technical terms: API, orchestration, pipeline, integration layer, real-time sync engine
- PM vocabulary: hypothesis, assumption, outcome tree, solution space, JTBD
- Compound jargon: "automated workflow automation platform" (redundant and opaque)

Rewrite flagged phrases in plain language. The test is: would a new account executive on their second week understand this without asking what it means?

### Step 11: Offer Next Steps

At the end of the artifact, offer the user three options:

1. Share with sales leadership for review and input on Key Messages - the sales team will flag whether the benefit bullets match what they hear from customers
2. Share with marketing to align on the Positioning Statement as the messaging anchor for launch campaigns
3. Schedule a launch readiness review with all GTM stakeholders to walk through the artifact together and confirm each function knows what they need to execute

## Examples

See [examples/sample.md](examples/sample.md).

The example set includes:

- a strong go-to-market artifact for a supply chain scenario with vivid persona-voice Problem Statement, benefit-focused Key Messages, and numeric Launch Goals
- a weak version with a business-case Problem Statement, feature-list Key Messages, and vague Launch Goals
- a drift-bug example where Key Messages are written from the product team's technical perspective, not from the customer's perspective on their gains

## Common Pitfalls

### Pitfall 1: Problem Statement Written in Third-Person Business Case Voice

**Symptom:** The Problem Statement reads like an executive summary: "Our research indicates that supply chain coordinators experience significant inefficiencies in shipment tracking, resulting in productivity losses estimated at..."

**Consequence:** Sales and support teams cannot use this to empathize with customers. It sounds like an analyst report, not a customer's lived experience. The persona voice is what makes this section useful.

**Fix:** Rewrite in first-person from the customer's perspective using the scaffold: "I am a [role]... [pain]. Because [root cause]. Which makes me feel [emotion]." The voice must come from the customer's experience, not the PM's analysis of it.

### Pitfall 2: Key Messages That List Features Instead of Benefits

**Symptom:** The Key Messages bullets read like release notes: "Automated order routing," "Real-time inventory sync," "Multi-warehouse visibility dashboard."

**Consequence:** Sales and marketing cannot translate these into customer conversations. Features describe what the product does, not what the customer gains. Non-PM audiences cannot bridge that gap on their own.

**Fix:** For each bullet, ask "so what?" until you reach a customer outcome. "Automated order routing" becomes "orders routed to the right warehouse without manual intervention, so coordinators focus on exceptions rather than every transaction."

### Pitfall 3: Positioning Statement Paraphrased or Incomplete

**Symptom:** The Positioning Statement section contains a narrative description of the product's value rather than the seven-element formula. Or the "Unlike" element is missing because it felt awkward to name a competitor.

**Consequence:** Downstream messaging loses precision. Marketing campaigns, sales pitches, and support scripts all drift because the anchor they share is not structured. The "Unlike" element in particular is what makes positioning distinct - without it, the statement could describe any competitor's product.

**Fix:** Use the seven-element formula verbatim: For / Who / The / Is a / That / Unlike / Our product gives. Every element must appear. The "Unlike" element must name a real alternative (including "manual processes using spreadsheets" if that is the real competitor).

### Pitfall 4: PM Builds the Artifact Alone

**Symptom:** The GTM document is drafted without input from sales, marketing, or customer support. It is polished and complete but reflects only the PM's perspective.

**Consequence:** The document misses what each function actually needs. Sales will have different questions than marketing. Support will need different language than sales. A solo-authored GTM document rarely survives first contact with the field.

**Fix:** Treat the artifact as a starting draft for collaborative review, not a finished deliverable. Share it with each function and explicitly ask: "Is this how you would describe the customer's problem? Does this messaging match what you hear in the field? What would you add or change?"

### Pitfall 5: Launch Goals Are Directional Instead of Numeric

**Symptom:** The Launch Goals table contains rows like: "Improve user adoption," "Increase customer satisfaction," "Reduce onboarding friction."

**Consequence:** The team cannot evaluate launch success. Directional goals pass every test and fail every real measurement. Without a number, there is no way to know if the launch succeeded.

**Fix:** Every Target cell in the table must contain a number or percentage. "Improve user adoption" becomes "75% of licensed users complete onboarding within 14 days of provisioning."

### Pitfall 6: Solution Summary Filled with Product Jargon

**Symptom:** The Solution Summary reads: "A cloud-native SaaS platform with real-time API integrations that orchestrates multi-system workflow automation across ERP and WMS environments."

**Consequence:** Support representatives, account executives, and marketing managers cannot explain the product. This reads as a technical architecture description, not a product description. It communicates nothing useful to a non-PM audience.

**Fix:** Write a product description that your best customer could read aloud to a colleague. Test it against the question: "could a new account executive on their second week explain this to a prospect?" If not, simplify.

### Pitfall 7: Key Messages Written for Only One Persona

**Symptom:** The Key Messages table has one row for the primary user persona and nothing for the buyer persona or other affected roles.

**Consequence:** Marketing campaigns and sales conversations with buyers (who are different from users) have no messaging anchor. The buyer often controls the purchase decision but has different concerns than the daily user - cost, risk, visibility, and control rather than workflow efficiency.

**Fix:** Build Key Messages for each distinct persona: at minimum the primary user and the economic buyer. If the product serves three distinct roles, write three rows.

### Pitfall 8: Tech-Role Bias in Key Messages

**Symptom:** Key Messages emphasize technical impressiveness: "The platform's real-time data integration engine delivers sub-200ms sync latency across all connected systems." The bullets celebrate what the engineering team built, not what changes for the customer.

**Consequence:** The GTM document reads as an engineering achievement report. Sales and marketing cannot translate this into customer benefit language because there is no customer benefit language to translate - only technical specifications.

**Fix:** Apply the perspective test to every bullet. Ask: who is the subject of this sentence? If it is the product, the platform, or the system, the bullet is a feature. If it is the customer and what they can now do or stop doing, it is a benefit. Rewrite every technical subject into a customer subject.

### Pitfall 9: Claims With No Proof Behind Them

**Symptom:** Key messages that promise outcomes ("cut dispatch time in half") with nothing in the proof column, or with proof the model wrote: a testimonial no customer gave, a pilot result no pilot produced.

**Consequence:** Sales repeats a claim it can't back up. The first skeptical buyer asks for evidence, and the message loses credibility for the whole launch.

**Fix:** Every message gets proof the persona would trust, or the proof is listed as "still to gather before launch." Never invent testimonials, quotes, or results.

### Pitfall 10: Goals That Prove Nothing

**Symptom:** Launch goals like "train the sales team" (a task), "zero critical defects in beta" (a readiness goal), or "40% adoption in 30 days" with no baseline behind the target.

**Consequence:** The team hits every goal and still can't say whether the go-to-market plan worked.

**Fix:** Keep only goals that show the market responded. Move readiness goals to Product Readiness. Turn tasks into the result they should produce. Give every target a baseline or evidence, a measure someone can collect, and a timeframe.

## References

### Skill Files

- [template.md](template.md) - six-section GTM handoff scaffold, with proof points
- [prompts/](prompts/README.md) - copy-paste prompts for chat-based AI tools (2: key messages and proof points, launch goals)
- [examples/sample.md](examples/sample.md) - strong, weak, and drift-bug examples

### Related Skills

- **Upstream:** [ps-framing-the-problem](../ps-framing-the-problem/SKILL.md) provides the Problem Statement for translation into persona voice
- **Upstream:** [ps-proto-persona](../ps-proto-persona/SKILL.md) provides the personas for Key Messages and Target Audience
- **Upstream:** [ps-solution-hypothesis](../ps-solution-hypothesis/SKILL.md) provides the solution framing for the Solution Summary
- **Upstream:** [ps-positioning-statement](../ps-positioning-statement/SKILL.md) provides the Positioning Statement verbatim
- **Upstream:** [ps-product-outcome-canvas](../ps-product-outcome-canvas/SKILL.md) consolidates the Problem Statement, Positioning Statement, and Key Features fields; use the canvas as the source of truth when it is available
- **Downstream:** none (this is a launch enablement output, not a discovery input for any other skill)

### Project Docs

- [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)
- [informative-documents/framework-glossary.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/framework-glossary.md)
- [informative-documents/skill-dependency-map.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/skill-dependency-map.md)

### Source Material

- [assets/ps_go_to_market_playbook_pages.pdf](assets/ps_go_to_market_playbook_pages.pdf)
- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 92-97: Template 20 of 24 there, with the AI overview on slide 94 and prompts on slides 95, 96. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).
- [Baseline Playbook version](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml). Full source PDF supplied separately.
- Productside Playbook companion document (supplied separately)
