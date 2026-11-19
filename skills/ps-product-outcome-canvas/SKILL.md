---
name: ps-product-outcome-canvas
description: >-
  Consolidate all discovery and define artifacts into the Product Outcome
  Canvas, the Go/No Go decision document presented to leadership before entering
  the Create phase.
intent: >-
  Help a Product Manager synthesize the outputs of the Discover + Define phase
  into a single executive presentation artifact that makes the business case for
  investment. This is the key decision point document that enables leadership to
  approve entering the Create (build) phase.
type: component
blueprint_stage: Discover + Define
best_for:
  - "Consolidating all Discover + Define artifacts into a single Go/No Go decision surface"
  - "Practicing the business case presentation before pitching to leadership"
  - "Gating entry to the Create phase with a structured investment review"
scenarios:
  - "I need to consolidate all our discovery artifacts into one canvas for the Go/No Go review"
  - "Help me prepare the business case presentation for leadership before we enter the Create phase"
---

## Purpose

Create a **Productside-style Product Outcome Canvas** from the artifacts produced during the Discover + Define phase.

This skill is used at the **Go/No Go decision point** before the team enters the Create phase. Leaders use it to approve investment. PMs use it to practice presenting the business case to their sponsors and stakeholders.

The canvas brings together problem framing, solution positioning, customer stories, outcome targets, metrics, risks, and resource asks into a single, cohesive document. It is the artifact that answers the question leadership always asks: "Why should we build this, what will it do for us, and what do you need from us to make it happen?" It is not a summary slide.

## Key Concepts

### Why This Is a Go/No Go Document

The Product Outcome Canvas marks the formal end of the Discover + Define phase. At this point, the team has validated a problem, generated and explored solutions, formed a hypothesis, positioned the product, and assessed risks. The canvas consolidates all of that work into the form that leadership can evaluate and approve.

A canvas completed before this point is speculative. A canvas completed after this point is retrospective. The right moment is when the team has enough evidence to make a credible case but still needs authorization to proceed.

### The Three-Section Structure

**Section 1: Core Information** anchors the document. Product Name, Date, Product Manager, and Version tell the reader what they are looking at and when.

**Section 2: Summary (left column)** tells the story of the problem and solution. It includes the Problem Statement, Solution Summary, Positioning Statement, two customer stories (one per persona), and the Key Features of the proposed solution.

**Section 3: Project Boundaries (right column)** frames the business case with measurable targets and honest constraints. It includes Business Outcomes, Product Outcomes, Business Success Metrics, Product Success Metrics, top Risks, The Ask, and the Introduction Date.

The two-column design is intentional: the left column persuades through narrative and context; the right column justifies through numbers and commitments.

### Stories vs. Data

The two customer stories in the Summary section serve a purpose that data cannot: they make the problem real. A well-written story puts leadership in the room with the customer and makes the problem visceral. Data confirms the problem is worth solving; stories make people want to solve it.

Each story should anchor to a concrete moment in the customer's experience: a specific situation where the product either fails or succeeds. The before/after structure is the most reliable format: show the customer without the product, then show the same customer with it.

Stories are about the customer. Not the PM. Not the team. Not the development process. If the story protagonist is writing a PRD, facilitating a sprint, or reviewing a roadmap, the story is about the wrong person.

### The Ask: Winning Approval

The Ask section is the resource request. Leadership needs to know three things: who you need, how much of their time, and for how long. A vague Ask ("we need engineering and design resources") is not an Ask. It is a wish. A credible Ask names roles, estimates percentage of time, gives a timeline, and flags any change management or infrastructure requirements.

An Ask that is too small under-allocates and sets the project up to slip. An Ask that is too large lacks credibility. Calibrate to the scope of what the canvas describes.

### Loose Coupling to Upstream Plays

This skill draws from six upstream plays. Every field on the canvas can be populated from an upstream play artifact or from direct input, whichever the PM has available. The skill never blocks a field because an upstream play has not been run. If the PM has a problem statement from a workshop, a spreadsheet, or a prior document, that input is as valid as a ps-framing-the-problem output.

The upstream plays and their contributions:

| Canvas Field | Primary Upstream Source |
|---|---|
| Problem Statement | ps-framing-the-problem |
| Solution Summary | ps-solution-hypothesis |
| Positioning Statement | ps-positioning-statement |
| Business Outcomes, Product Outcomes, Metrics | ps-outcome-tree |
| Risks | ps-risk-assessment |
| Stories | ps-proto-persona (for persona context) |

If an upstream play has not been run, offer to run it before filling the field. If the PM has equivalent input from another source, accept it and proceed.

### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **reviewer of the canvas before the Go/No Go decision**. It checks that each section is consistent with the upstream work it summarizes, that the user and buyer stories are grounded, that outcomes and metrics are measurable, and that the Ask is specific. Every claim on the canvas must come from the PM's work, because leadership will decide on it.

- **Use it when:** the PM has assembled the canvas from upstream artifacts and wants it reviewed before presenting it.
- **Avoid it when:** the upstream work doesn't exist yet. A canvas assembled from guesses becomes a Go decision on a guess.
- **Return:** inconsistencies between sections flagged, stories checked against evidence, outcomes and metrics checked for measurability, and the Ask sharpened into a specific decision and resource request.

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

See the source play pages in [assets/ps_product_outcome_canvas_playbook_pages.pdf](assets/ps_product_outcome_canvas_playbook_pages.pdf).

### Required Output Convention

Default to a **clean, paste-ready artifact**.

That means:

- all three sections completed
- stories written in close-third or first-person with a concrete time anchor
- The Ask specifies roles, percentages, and a timeline
- Risks are named specifically (top 3 from the risk assessment)
- no generic placeholders left in any field
- explanation belongs below the artifact, not inside the fields

### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in [prompts/01-review-canvas.md](prompts/01-review-canvas.md) one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

### Step 1: Tech-Role Bias Guard

Before writing any content, confirm who the product serves.

Most products serve people who do not write code: clinicians, logistics coordinators, field technicians, operations managers, procurement analysts, regulatory leads. LLMs default to developer/engineer protagonists when context is thin. The stories in this canvas will be wrong if the protagonist is a software engineer when the product serves a supply chain manager.

Ask the PM: "Who is the primary user of this product in the field? What is their job title? What does their day look like before this product exists?"

Use the answer to anchor both stories. If the PM cannot answer this question, offer to run ps-proto-persona before proceeding.

### Step 2: Gather Upstream Artifacts

Ask the PM which of the following artifacts are available:

- Problem Statement (from ps-framing-the-problem or equivalent)
- Solution Summary or hypothesis (from ps-solution-hypothesis or equivalent)
- Positioning Statement (from ps-positioning-statement or equivalent)
- Business Outcomes, Product Outcomes, and Metrics (from ps-outcome-tree or equivalent)
- Risk Assessment (from ps-risk-assessment or equivalent)
- Persona descriptions (from ps-proto-persona or equivalent, for story context)

For each artifact that is not available, offer to run the corresponding skill or ask the PM to provide the information directly. Do not invent content for any field. If a field must be left incomplete, mark it clearly and note what is needed to complete it.

### Step 3: Complete Core Information

Capture:

- Product Name (the actual product name, not a placeholder)
- Date (today's date, or the date of the Go/No Go session)
- Product Manager (the PM's name and role)
- Version (start at v1.0 unless the PM specifies otherwise)

### Step 4: Write the Problem Statement

Use the final Problem Statement from ps-framing-the-problem if available. If not, ask the PM to describe the problem in 2-4 sentences covering: who is affected, what they are trying to do, what is blocking them, and why it matters to the business.

Do not write a problem statement that contains solution language. The problem statement describes the current state, not the desired future state.

Target: 40-60 words.

### Step 5: Write the Solution Summary

Use the If/Then hypothesis format from ps-solution-hypothesis if available.

If not, ask the PM: "In one or two sentences, what does this product do and what does it enable the customer to do that they cannot do today?"

The Solution Summary describes the proposed solution at a level of specificity that makes the concept clear: specific enough to be meaningful, general enough not to lock in implementation details.

Target: 30-50 words.

### Step 6: Write the Positioning Statement

Use the seven-element Positioning Statement from ps-positioning-statement if available. The seven elements are: For (target customer), Who (need or opportunity), The (product name), Is a (product category), That (key benefit), Unlike (primary competitive alternative), Our product gives (primary differentiation).

If the upstream artifact is not available, ask the PM to provide the positioning elements directly and assemble them using the formula.

Target: 50-70 words.

### Step 7: Write Story 1 (User Persona)

Story 1 uses the user persona: the person who uses the product directly in the field.

Write a 2-4 sentence close-third or first-person narrative that anchors to a specific moment. Use a concrete time anchor ("Six weeks after the launch of X, Priya...") to make the story feel real. Show life before and after the product, or show a specific moment where the product makes a critical difference.

The story should make the problem tangible and the solution credible: not by listing features, but by showing the customer's experience.

Do not use the PM or the product team as the protagonist. Do not write a story about building, shipping, or configuring the product.

Target: 50-80 words.

### Step 8: Write Story 2 (Buyer Persona)

Story 2 uses the buyer persona: the person who approves or funds the product, which may be a manager, director, procurement lead, or executive sponsor.

Use the same format as Story 1 but from the buyer's perspective. The buyer's story often centers on visibility, accountability, risk reduction, or efficiency rather than day-to-day task completion.

If no distinct buyer persona has been defined, ask whether the user and buyer are the same person. If so, note this in the artifact and write a single extended story, or ask the PM whether to differentiate.

Target: 50-80 words.

### Step 9: Complete Project Boundaries (Outcomes and Metrics)

Use the ps-outcome-tree output if available. Populate:

- Business Outcomes: what the business gains from the product's success (revenue, efficiency, compliance, retention)
- Product Outcomes: what the customer achieves through using the product (role-based, not persona-named)
- Business Success Metrics: 2-3 measurable business-level indicators
- Product Success Metrics: 2-3 measurable product-level indicators

If the outcome tree has not been run, ask the PM to provide the outcomes and metrics directly. Outcomes must use outcome language (not feature language). Metrics must be specific and measurable: not "improve NPS" but "NPS increases from 32 to 45 within 12 months of launch."

Targets: Business Outcomes 15-25 words; Product Outcomes 15-25 words (bulleted); Metrics 2-3 items at 10-15 words each.

### Step 10: List Key Features

List the top 3-5 features of the proposed solution. These are the capabilities the product will have: what it does, not what the customer achieves. Keep each item short and paste-ready.

Key Features are not outcomes. "Real-time shipment tracking dashboard" is a feature. "Logistics coordinators reduce shipment exception resolution time by 40%" is an outcome.

If the PM has not yet defined features, ask for the top 3-5 things the product will do. Do not infer features from the solution summary or positioning statement without confirmation.

Target: 3-5 bullets at 5-8 words each.

### Step 11: List Top 3 Risks

Use the ps-risk-assessment output if available. Identify the top 3 risks by priority (Critical first) and list their names only. Do not include the full mitigation and contingency plans.

Risk names in the canvas are labels, not plans. The full risk management detail lives in the Risk Assessment artifact. The canvas shows leadership that the team has a risk picture; it does not replace the risk document.

If the risk assessment has not been run, ask the PM to name the 3 most significant threats to success. Use the format: [Risk Type]: [Specific Concern].

Target: 3 items at 5-8 words each.

### Step 12: Write The Ask

The Ask is the resource request for the Create phase. It must include:

- Team composition: roles needed (e.g., Senior Engineer, UX Designer, Data Analyst)
- Time allocation: percentage of each role's time committed to this product
- Timeline: duration of the initial build phase (e.g., "8-week build sprint starting Q3 2026")
- Change management or infrastructure requirements: anything outside standard team capacity

If the PM does not have this information, prompt them with: "To give leadership a concrete Ask, I need to know: what roles do you need, how much of their time, and for how long?" Do not leave The Ask as TBD. It is the reason the canvas is presented.

Target: 30-50 words.

### Step 13: Record the Introduction Date

The Introduction Date is the target launch or release date, meaning when the product reaches customers.

If the PM does not have a specific date, accept a target quarter or milestone ("Q4 2026" or "before annual customer conference in November"). Do not use TBD. If the date is genuinely unknown, flag it and note what decision would unlock it.

Target: 5-10 words.

### Step 14: Offer Next Steps

After delivering the artifact, offer three options:

1. Share the canvas with the leadership sponsor or investment committee for the Go/No Go decision
2. Enter the Create phase by transitioning to build planning, user story mapping, or roadmap work
3. Schedule a structured review session to pressure-test The Ask and the risk picture before presenting

## Examples

See [examples/sample.md](examples/sample.md).

The example set includes:

- a strong canvas with vivid customer stories, specific metrics, and a concrete Ask
- a weak canvas with PM-centric stories, vague metrics, and a TBD Ask
- a drift-bug example with tech-role bias and invented upstream data

## Common Pitfalls

### Pitfall 1: Stories About the PM's Process Instead of the Customer's Experience

**Symptom:** Story 1 or Story 2 describes the PM running discovery, writing requirements, facilitating sprint planning, or presenting to stakeholders.

**Consequence:** Leadership hears a story about the product team's work, not about the customer's problem. The stories fail to make the case for the product.

**Fix:** The protagonist of every story is the customer or buyer. Read the first sentence of each story. If the subject is a PM, a designer, a developer, or a team, rewrite it. The story must anchor to the customer's day and the customer's experience.

### Pitfall 2: Listing Every Risk Instead of the Top Three

**Symptom:** The Risks section on the canvas contains all six risks from the risk assessment, including Accept-priority risks.

**Consequence:** Leadership cannot distinguish which risks the team considers serious from which risks are background noise.

**Fix:** The canvas shows the top 3 risks by priority. Accept-priority risks belong in the full Risk Assessment artifact, not on the canvas. The canvas is a summary, not a transcript of the assessment.

### Pitfall 3: The Ask Is Too Vague

**Symptom:** The Ask section reads "We will need engineering, design, and data resources" or "Timeline TBD."

**Consequence:** Leadership cannot approve what they cannot evaluate. A vague Ask signals that the team is not ready to enter the Create phase.

**Fix:** The Ask names specific roles ("2 Senior Engineers, 1 UX Designer, 1 Data Analyst at 80% time"), gives a percentage allocation, and names a timeline. If this information is not yet available, the canvas is premature. Run the planning work before presenting.

### Pitfall 4: Treating the Canvas as a One-Time Artifact

**Symptom:** The canvas is completed for the initial Go/No Go decision and never revisited.

**Consequence:** As the product evolves through the Create phase, the canvas becomes disconnected from current reality. When leadership asks for a status update, the team has to rebuild from scratch.

**Fix:** Treat the canvas as a living document. Update the Version number and Date when outcomes shift, risks change, or The Ask needs revision. The canvas should reflect the current state of the product investment, not just its initial framing.

### Pitfall 5: Using Generic Placeholder Persona Names in Stories

**Symptom:** Stories use placeholder names like "User A," "The Buyer," or "Jane Doe" without specific role context.

**Consequence:** The stories feel generic and fail to make the problem tangible. Leadership cannot picture a real person in a real situation.

**Fix:** Use a specific, realistic name that reflects the persona's role and demographic diversity. Pair the name with a concrete job title and situation. "Priya Nair, a logistics coordinator at a mid-market distribution company, spends the first two hours of every morning..." is credible. "The user opens the dashboard..." is not.

### Pitfall 6: Filling the Canvas Without Any Upstream Artifacts

**Symptom:** The canvas is populated entirely from the agent's inference, without asking the PM for problem statements, hypothesis outputs, or outcome tree data.

**Consequence:** The canvas reflects what the agent imagined the product to be, not what the PM's discovery work established. The content may sound coherent but will not match the team's actual findings.

**Fix:** Before drafting any field, ask for the upstream artifacts or equivalent direct input. If no artifacts exist, flag the gap and offer to run the relevant upstream skill. Never invent the content of a field that is supposed to come from customer research or team validation.

### Pitfall 7: Tech-Role Bias in the Customer Stories

**Symptom:** The story protagonist is a software developer, data engineer, or architect when the product serves operations staff, field workers, clinicians, or other non-technical roles.

**Consequence:** Leadership hears a story about engineering concerns rather than customer problems. The canvas misrepresents who the product is for.

**Fix:** Run the tech-role bias guard in Step 1 before writing any content. Confirm the customer's job title and daily workflow. If the product serves non-technical users, the story must reflect non-technical concerns: task completion, time, accuracy, confidence, and visibility rather than system architecture or code quality.

### Pitfall 8: Confusing Key Features with Product Outcomes

**Symptom:** The Key Features section lists outcomes ("Logistics coordinators resolve shipment exceptions 40% faster") instead of capabilities ("Real-time shipment exception alerts").

**Consequence:** The canvas double-counts outcomes in both the Project Boundaries and Key Features sections, obscuring the distinction between what the product does and what the customer achieves.

**Fix:** Key Features are capabilities (what the product does). Product Outcomes are results (what the customer achieves). Each field serves a different purpose. If the same content appears in both sections, one of them is wrong.

### Pitfall 9: A Canvas Built From Nothing

**Symptom:** The PM asks for a Product Outcome Canvas for a new idea and gets every section filled: stories, metrics, features, risks, and an Ask.

**Consequence:** Leadership makes a Go/No Go decision on a document that summarizes work nobody did.

**Fix:** Assemble the canvas only from upstream artifacts. Mark any section with no source as a gap, and say which play fills it.

## References

### Skill Files

- [template.md](template.md) - working scaffold
- [prompts/](prompts/README.md) - copy-paste prompt for chat-based AI tools (authored for this library; the deck has no AI page for this Play)
- [examples/sample.md](examples/sample.md) - strong, weak, and drift-bug examples

### Related Skills

- **Upstream:** [ps-framing-the-problem](../ps-framing-the-problem/SKILL.md) provides the Problem Statement; [ps-solution-hypothesis](../ps-solution-hypothesis/SKILL.md) provides the Solution Summary; [ps-positioning-statement](../ps-positioning-statement/SKILL.md) provides the seven-element Positioning Statement; [ps-outcome-tree](../ps-outcome-tree/SKILL.md) provides Outcomes and Metrics; [ps-risk-assessment](../ps-risk-assessment/SKILL.md) provides the top Risks; [ps-proto-persona](../ps-proto-persona/SKILL.md) provides persona context for the stories
- **Downstream:** [ps-product-readiness](../ps-product-readiness/SKILL.md) is the next Key Decision Point — the beta test plan gates Deliver phase entry; run ps-product-readiness after completing Create phase work
- **Downstream:** [ps-go-to-market](../ps-go-to-market/SKILL.md) imports the Problem Statement, Positioning Statement, and Key Features fields from this canvas at launch time

### Dependency Map

See [informative-documents/skill-dependency-map.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/skill-dependency-map.md) for the full upstream/downstream table.

### Project Docs

- [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)
- [informative-documents/framework-glossary.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/framework-glossary.md)
- [informative-documents/skill-dependency-map.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/skill-dependency-map.md)

### Source Material

- [assets/ps_product_outcome_canvas_playbook_pages.pdf](assets/ps_product_outcome_canvas_playbook_pages.pdf)
- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 75-77: Template 16 of 24 there. No AI page for this Play; the prompts are authored for this library. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).
- [Baseline Playbook version](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml). Full source PDF supplied separately.
- Productside Playbook companion document (supplied separately)
