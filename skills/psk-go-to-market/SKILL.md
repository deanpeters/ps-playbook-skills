---
name: psk-go-to-market
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

The formal Problem Statement from psk-framing-the-problem uses a structured five-stem format written for product teams. The GTM Problem Statement does something different: it retells the same story in first-person from the customer's perspective, in emotional and accessible language.

The format:
"I am a [role] [doing/struggling with X]. [Pain]. Because [root cause]. Which makes me feel [emotional consequence]."

This reframing is not decoration. Account executives and customer success managers need to feel the customer's pain to communicate it credibly. A business-case summary does not accomplish that. A first-person narrative does.

### Solution Summary vs. Positioning Statement

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

### Key Messages Are Benefit Statements, Not Feature Lists

The Key Messages table is where each persona learns what is in it for them. This is not a feature brief. Features describe what the product does. Benefits describe what the customer gains. "Automated case routing" is a feature. "Time back to focus on complex cases instead of sorting tickets" is a benefit.

Write 3-5 bullet points per persona. Each bullet answers: what does this change for me, in my role, in my day? If the answer could come from a product spec, it is a feature - rewrite it as an outcome.

### Every Message Needs Proof

A key message without proof is a claim. Each message gets **proof points the persona would trust**: a testimonial, a pilot result, a case study, a published benchmark. Proof must be real. Proof the team doesn't have yet goes in the Proof Points column with the exact label `To gather:` followed by the kind of proof needed (for example, `To gather: pilot-site quote on status calls`). Never invent it.

Messages are written for **at least one user and one buyer persona**. A buyer usually cares about different outcomes than a user, so if the user and buyer messages overlap heavily, one of them is probably generic. Every message traces back to the positioning statement.

### Readiness Goals vs. Launch Goals

**Readiness goals** prove the product is ready to ship, measured in a limited pre-release test (Product Readiness Testing). **Launch goals** prove the go-to-market plan worked, measured in the market after release. A goal that belongs to readiness doesn't belong here. A **launch task** ("train the sales team," "publish the web page") isn't a goal either. Ask what result the task should produce.

### Launch Goals vs. Product Success Metrics

Launch Goals are not the same as the ongoing metrics from psk-outcome-tree or psk-measuring-outcomes. Launch Goals are time-bounded success indicators for the launch window itself: adoption milestones, satisfaction scores, and efficiency gains that confirm the launch executed correctly.

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
- **Avoid it when:** positioning or personas are still unsettled (route to psk-positioning-statement or psk-proto-persona), or the request is for AI to set the targets. It has no data on the market or the business.
- **Return:** messages tested for benefit, jargon, and credible proof; launch goals checked for measure, realistic target, and timeframe; and proposed rewrites for the PM to accept, adapt, or reject.

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

- Problem framing from psk-framing-the-problem (five-stem format, for translation to persona voice)
- Solution hypothesis from psk-solution-hypothesis (for the Solution Summary)
- Positioning statement from psk-positioning-statement (for verbatim copy into the Positioning Statement section)
- Persona work from psk-proto-persona (identifies the personas for Key Messages and Target Audience)

Use whatever the user can provide. If a section has no upstream source, draft from context and flag it for review. Do not gate the skill on whether all upstream plays have been run.

### Step 3: Optional Web Research

Web research is appropriate for this skill when it helps with:

- Competitive landscape: understanding what alternatives exist for the "Unlike" element and how to differentiate the Key Messages from competitor positioning
- Market segment context: knowing the size and characteristics of target segments for the Target Audience section
- Industry launch timing norms: understanding whether 1-2 months of GTM prep is typical or compressed for this market

Do not use web research to substitute for customer discovery. If the user lacks a clear problem statement or persona definition, the answer is to run upstream skills, not to fill the gap with market research.

### Step 4: Write the Problem Statement in Persona Voice

Translate the formal five-stem Problem Statement (from psk-framing-the-problem, or from the user's description if that play has not been run) into a first-person narrative from the customer's perspective.

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

### Step 8: Write Key Messages for Each Persona

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

### Step 9: Write Launch Goals

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

## Template

### When to Use This

Use this template during the **Create phase** after completing positioning, solution hypothesis, and proto-persona work. Run it collaboratively with sales, marketing, and customer support stakeholders before setting the launch timeline.

Upstream artifacts that feed this template:
- Problem framing (psk-framing-the-problem): provides the five-stem structure to translate into persona voice
- Solution hypothesis (psk-solution-hypothesis): provides the solution framing for plain-language translation
- Positioning statement (psk-positioning-statement): provides the seven-element formula to copy verbatim
- Proto-persona (psk-proto-persona): identifies the personas and their pains for Key Messages and Target Audience

### Template

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

### Usage Guidance

#### Filling the Template

1. Complete **Product Context** to anchor who participated and what the launch timeline is.
2. Write the **Problem Statement** last, after reading the framing from psk-framing-the-problem. Translate from analytical to emotional and first-person.
3. Write **Target Audience** from the proto-persona work - personas should match what has already been validated.
4. Write the **Solution Summary** as if explaining the product to a new support hire on day one.
5. Copy the **Positioning Statement** verbatim from psk-positioning-statement output. If that play has not been run, construct it fresh using the formula.
6. Build **Key Messages** persona by persona. Start with the primary user, then the buyer, then any other affected roles.
7. Set **Launch Goals** by working backward from the launch date - what does success look like at 30, 60, and 90 days?

#### What Goes Where

| Section | Contains | Does NOT Contain |
|---------|----------|-----------------|
| Problem Statement | First-person customer narrative with emotion | Third-person business case language |
| Target Audience | Named personas and market segments | The PM or product team as the audience |
| Solution Summary | Plain-language product description | Technical vocabulary, PM jargon, hypothesis format |
| Positioning Statement | Seven-element formula verbatim | Paraphrasing, narrative description, incomplete elements |
| Key Messages | Benefit bullets per persona | Feature descriptions, capability lists |
| Launch Goals | Numeric targets for the launch window | Directional language without numbers, long-term metrics |

#### Connecting to Other Skills

- **Upstream:** psk-framing-the-problem provides the Problem Statement structure for translation. psk-proto-persona provides the personas. psk-solution-hypothesis provides the solution framing. psk-positioning-statement provides the Positioning Statement verbatim.
- **Downstream:** This skill is an endpoint. The artifact feeds into sales enablement, marketing campaigns, and launch readiness reviews - but no other playbook skills consume it.

#### Capacity Reference

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

## Examples

Illustrative and fictional, not customer evidence.

- **Strong:** Separate messages for field technicians and operations managers; connect each message to that persona's problem and an evidenced benefit.
- **Weak:** One generic feature announcement gives sales no customer-specific reason to care.
- **Drift to avoid:** Invented proof: do not add fabricated testimonials or launch results to make the message persuasive.


## Common Pitfalls

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

## References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-go-to-market) for supporting source material and expanded examples.
