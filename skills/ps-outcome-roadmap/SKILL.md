---
name: ps-outcome-roadmap
description: >-
  Build an outcome-based roadmap and release plan that connects product outcomes
  to outputs, sorted by confidence level. Use when a PM needs to communicate
  what the team is pursuing and why, in language that works for both executives
  and engineering.
intent: >-
  Help a Product Manager and their team create a living roadmap that separates
  what customers will achieve (roadmap layer) from what the team will build
  (release plan layer), organized by confidence level so stakeholders can see
  which work is committed, which is directional, and which is still being
  explored.
type: component
blueprint_stage: Create
best_for:
  - "Building an outcome-based roadmap organized around what customers achieve"
  - "Connecting product outcomes to a concrete release plan with outputs and experiments"
  - "Communicating roadmap decisions to stakeholders in outcome language, not feature lists"
scenarios:
  - "I need to build a roadmap organized around outcomes, not a feature list"
  - "Help me connect our product outcomes to a concrete release plan with dates and owners"
---

## Purpose

Create a **Productside-style Outcome-Based Roadmap and Release Plan** from a product team's validated outcomes and prioritized outputs.

This skill helps a Product Manager combine two connected layers into one artifact: a roadmap organized around product outcomes (what customers achieve) and a release plan organized around outputs (features, capabilities, and experiments). Both layers are sorted by confidence level into Now, Next, and Later columns.

The artifact is a **living document**. Discovery is never complete. As the team runs Tiny Acts of Discovery and resolves assumptions, items graduate from Later to Next to Now. The roadmap should be revisited at every major discovery or delivery milestone.

The critical distinction this skill enforces: the **roadmap row speaks outcome language only**. The **release plan row speaks output language only**. Mixing them creates confusion for every audience.

## Key Concepts

### Outcomes vs. Outputs - the Load-Bearing Distinction

This roadmap has two rows for a reason. They speak different languages to different audiences.

**Outcomes** are what customers achieve. They describe a changed state in the customer's world: "field technicians resolve equipment faults without returning to the depot," "quality inspectors catch defects before they leave the line." Outcomes belong in the roadmap row.

**Outputs** are what the team builds. They describe a deliverable: "fault diagnosis mobile app," "in-line defect vision scanner," "parts availability lookup." Outputs belong in the release plan row.

When outputs appear in the roadmap row, executives read a feature list instead of a value plan. When outcomes appear in the release plan row, engineering cannot build a sprint from them. Keep the rows separate.

### The Now / Next / Later Confidence Framework

The three columns are organized by **confidence level**, not by priority or preference.

**Now - High Confidence:** The team has enough validated evidence to commit. These product outcomes have been tested against real customer behavior and real technical constraints. The team is pursuing them actively. Outputs in this column are in the release plan.

**Next - Medium Confidence:** The team believes in these outcomes and output ideas, but needs to resolve specific assumptions before committing fully. The primary work in Next is validation: running assumptions to ground so confident items can graduate to Now.

**Later - Low Confidence:** These are hypotheses - early-stage outcome ideas and open questions that require research before the team can evaluate them seriously. The primary work in Later is research: converting open questions into resolvable assumptions.

Confidence is not a popularity contest. An outcome moves left because the team has resolved uncertainty, not because leadership prefers it.

### How Items Graduate

- **Later to Next:** When Assumptions to Research resolve enough uncertainty to form a testable assumption with a clear hypothesis.
- **Next to Now:** When Assumptions to Validate confirm enough confidence that the team can commit to the outcome and begin output development.
- **Now to Done:** When the output is shipped and the outcome can be measured.

Items can also move right. If a Now outcome proves harder to achieve than expected, or if new evidence undermines confidence, it should move back to Next for additional validation.

### Discovery Is Continuous - Not a Future Phase

The discovery activities in this artifact (Tiny Acts of Discovery, Assumptions to Validate, Assumptions to Research) run **in parallel with the release work**. They are not a future phase that begins after Now outputs ship.

While the team is building Now outputs, it is simultaneously running Tiny Acts to refine those outputs, validating assumptions to graduate Next items, and researching questions to graduate Later items. The three columns are active at the same time.

A roadmap with empty discovery sections is not a living document. It is a delivery schedule.

### Business Outcomes as the Anchor

Everything on the roadmap traces back to the Business Outcomes header. This is the business-level goal the product serves, drawn from the Outcome Tree. It provides the "why behind the what" and prevents the roadmap from becoming a disconnected list of features.

If a product outcome in the Now column cannot be connected to the Business Outcomes header, it should not be on the roadmap.

### The Artifact Is a Communication Tool

Different audiences need different layers of the same artifact.

**Executives** read the Business Outcomes header and the roadmap row. They see what business goal is being served and what customer outcomes the team is pursuing at each confidence level.

**Engineering** reads the release plan row. They see what is being built (Now outputs), what needs validation before it can enter the build queue (Next output concepts), and what is still being explored (Later assumptions).

**Both audiences** are looking at the same artifact. No separate decks, no translation layer. The structure does the work.

### This Builds Directly From the Outcome Tree

The product outcomes in the Now and Next roadmap cells should come directly from the ps-outcome-tree, not be invented fresh here. The PM should not use the roadmap as an opportunity to introduce new outcomes that have not been validated through the Outcome Tree play.

If the Outcome Tree has not been run, offer to run ps-outcome-tree first, or accept the PM's description of outcomes directly. But confirm they are grounded in discovery work.

### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **critic of the roadmap the PM drafted**. It checks that each horizon holds outcomes, not outputs; that items sit in Now, Next, or Later by confidence; that each output links to an outcome; and that discovery work appears alongside delivery. The placements and the sequence stay with the PM and their team.

- **Use it when:** the PM has an outcome tree and a draft roadmap, and wants it pressure-tested before sharing it.
- **Avoid it when:** the request is to produce a dated feature roadmap, or to place items without the PM's evidence about confidence.
- **Return:** outputs posing as outcomes flagged, each placement questioned against the evidence behind it, and links from outputs to outcomes checked.

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

See the source play pages in [assets/ps_outcome_roadmap_playbook_pages.pdf](assets/ps_outcome_roadmap_playbook_pages.pdf).

### Required Output Convention

Default to a **clean, paste-ready artifact**.

That means:

- Business Outcomes header is specific and measurable (not "grow revenue")
- At least one product outcome in each column (Now, Next, Later)
- At least two outputs in the Now release plan
- Discovery sections (Tiny Acts, Assumptions to Validate, Assumptions to Research) are not left blank
- Every Now output traces to a Now outcome
- No outputs appear in the roadmap row; no outcomes appear in the release plan row
- Explanation belongs below the artifact, not inside the fields

### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in [prompts/01-pressure-test-roadmap.md](prompts/01-pressure-test-roadmap.md) one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

When a draft roadmap lists outputs (features, releases, projects), don't guess the outcomes behind them, even labeled as guesses. Name each item as an output and ask the PM what customer outcome it serves and what evidence puts it in Now, Next, or Later. The outcomes come from the PM and their customers.

### Step 1: Tech-Role Bias Guard

Before drafting any content, confirm that the product outcomes are written from the **customer's perspective**. Outcomes describe what customers achieve - what changes in their world when the product works.

The team role bias is to write outcomes in engineering language: "deploy the alert system," "enable real-time API access," "build the reporting module." These are outputs, not outcomes.

Ask the user: who is the customer for this product, and what does success look like from their point of view? What changes in how they work, what they can accomplish, or how they feel about their work?

Do not proceed until there is a customer-perspective answer to that question.

### Step 2: Gather Upstream Artifacts

Before drafting, ask whether the user has materials to share:

- Outcome Tree from ps-outcome-tree (Business Outcomes and product outcomes)
- Output prioritization results from ps-output-prioritization (Quadrant I and Quadrant II outputs)
- Tiny Acts findings from ps-tiny-acts-discovery (specific experiments and assumptions)
- Any prior roadmap or release plan the team has already discussed

Check whether each exists; offer to help fill gaps; accept equivalent input from any source. Do not gate the skill on whether the upstream play has been run. Accept the PM's direct description if the artifact is not available.

Make a note of which sections are drawn from upstream artifacts and which are being drafted fresh.

### Step 3: Write the Business Outcomes Header

Draft the Business Outcomes header from the Outcome Tree's business outcome field. This should be one to two sentences describing the business-level goal this roadmap serves.

The header must be specific and anchored. "Reduce unplanned equipment downtime by 30% across field service regions" is anchored. "Improve operational efficiency" is not.

If the outcome has a measurable target, include it. If it does not, note that a target should be defined.

> Quality check: Can you trace every product outcome below to this business goal? If not, either the business goal is too narrow or one of the product outcomes does not belong on this roadmap.

### Step 4: Populate the NOW Roadmap - Product Outcomes to Pursue

List the product outcomes the team is confident will create customer value and has committed to pursuing. These should come directly from the Outcome Tree (validated product outcomes) or from the PM's description of validated discovery findings.

Write in customer language: what customers achieve, not what the product does.

Each outcome should be specific enough that the team can measure whether it has been achieved. "Field technicians identify root causes without waiting for depot diagnostics" is specific. "Improve technician experience" is not.

> Quality check: Are these outcomes written from the customer's point of view? Can the team measure achievement? Do they trace to the Business Outcomes header?

### Step 5: Populate the NEXT Roadmap - Product Outcomes to Validate

List the product outcomes the team believes in but has not yet validated enough to commit to. These outcomes need testing - specific assumptions must resolve before the team can move them to Now.

For each outcome, the key question is: what would have to be true for this to earn high confidence?

> Quality check: Is each outcome distinct from the Now outcomes? Is there a clear validation question that could move this outcome left?

### Step 6: Populate the LATER Roadmap - Product Outcome Hypotheses

List early-stage outcome ideas that require research before the team can even form a testable hypothesis. These are genuine unknowns - areas where the team has a direction but not enough understanding to design a validation test.

Write these as outcome hypotheses, not as research questions. "Procurement managers could reduce approval cycle time to under 48 hours if sourcing exceptions were flagged earlier" is a hypothesis. "Research whether procurement managers care about approval times" is a research question.

> Quality check: Is each hypothesis plausible based on existing domain knowledge? Is there a clear question that would move this to Next?

### Step 7: Populate Outputs to Develop (NOW)

List the features and capabilities that will drive the Now outcomes. These come from Quadrant I outputs in ps-output-prioritization (low cost, high value) or from the PM's direct input on what is in active development.

Write as specific output names, not categories. "Real-time fault alert push notification" is specific. "Notification system" is a category.

> Quality check: Does every output trace to a Now outcome? If an output cannot be connected to a Now outcome, it should not be in the Now release plan.

### Step 8: List Tiny Acts of Discovery (NOW)

List the small, fast experiments the team is running in parallel with Now output development. These come from ps-tiny-acts-discovery or from the PM's direct input.

Each Tiny Act should be specific enough to run: name what is being tested, how, and with whom. "Run a 5-person session with field technicians using a paper mock of the fault alert screen to confirm the alert hierarchy makes sense to them" is a Tiny Act. "Test the UI" is not.

> Quality check: Are these running now, in parallel with the outputs being built? Are they specific enough to execute this week?

### Step 9: Populate Output Concepts to Validate (NEXT)

List the output ideas that need validation before entering the release plan. These come from Quadrant II outputs in ps-output-prioritization (high cost, high value - needs more evidence before committing) or from the PM's description of candidates under consideration.

> Quality check: Is each concept clearly tied to a Next outcome? Is there a specific assumption that, if validated, would move this into Now outputs?

### Step 10: List Assumptions to Validate (NEXT)

List the specific hypotheses and assumptions that must be resolved to move Next outcomes and output concepts to Now. Write these as testable hypothesis statements, not as features.

Format: "We believe [customer segment] will [behavior or outcome] when [condition or stimulus], because [reasoning]."

A well-formed assumption can be tested. A feature request ("build the dashboard") cannot.

> Quality check: Is each assumption specific enough to design a test around? Does each assumption trace to a Next outcome or output concept?

### Step 11: List Assumptions to Research (LATER)

List the open questions and hypotheses that must be explored to move Later outcome hypotheses to Next. These are broader than testable assumptions - they require research to even know what to test.

Write as open questions or early hypotheses. The goal is to move from "we don't know" to "we have a hypothesis we can test."

> Quality check: Is each question specific enough to guide research? Can the PM name a method (interviews, observation, data pull) that would start to answer it?

### Step 12: Review Alignment

Before presenting the artifact, check:

- Every Now output traces to a Now outcome
- No outputs appear in the roadmap row
- No outcomes appear in the release plan row
- Discovery sections are not blank
- Business Outcomes header is specific and measurable
- Now, Next, and Later columns each have content (the roadmap is not front-loaded into Now)

If an output cannot be traced to an outcome, ask whether the outcome belongs on the roadmap and is missing, or whether the output should be reconsidered.

### Step 13: Offer Next Steps

At the end of the artifact, offer three options:

1. Share the roadmap with leadership: the Business Outcomes header and roadmap row give executives the outcome-level view they need to evaluate direction without getting into features
2. Share the release plan with engineering: the output-focused bottom row gives the team concrete, prioritized work with clear discovery activities running alongside
3. Schedule a review cadence: propose a specific date or milestone trigger for the next roadmap review, so the artifact stays current as assumptions resolve

## Examples

See [examples/sample.md](examples/sample.md).

The example set includes:

- a strong outcome-based roadmap with clear outcome language in the roadmap row, output language in the release plan row, and active discovery sections in all three columns
- a weak version where outputs appear in the roadmap row, all outcomes are in Now, and discovery sections are empty
- a drift-bug example where outcomes are written in business/financial language instead of customer outcome language, turning the roadmap into an internal financial plan

## Common Pitfalls

### Pitfall 1: Feature-Based Roadmap - Outputs in the Roadmap Row

**Symptom:** The roadmap row contains items like "launch the mobile app," "add dashboard reporting," "migrate to microservices."

**Consequence:** Executives read a feature list. They cannot evaluate whether the team is working on the right customer problems. Engineering has no anchor for what customer value each output is supposed to create.

**Fix:** Ask: what does the customer achieve when this output exists and works? That answer is the outcome. Replace the output in the roadmap row with the outcome. Move the output to the release plan row.

### Pitfall 2: All Outcomes in NOW - No Differentiation by Confidence

**Symptom:** Every product outcome is in the Now column. Next and Later are empty or have token content.

**Consequence:** The roadmap communicates false certainty. There is no signal about what is validated versus what is directional. Leadership cannot assess where the team is taking risk.

**Fix:** Push the team to differentiate honestly. If everything is high confidence, either the team is building too narrowly or they have not surfaced what they do not yet know. Most real product situations have at least two or three outcome hypotheses in Next or Later.

### Pitfall 3: Roadmap Written in Business/Financial Language

**Symptom:** Roadmap outcomes read as: "increase ARR by 15%," "reduce churn 10 basis points," "improve NPS by 5 points."

**Consequence:** The roadmap becomes an internal financial plan, not a customer value plan. Engineering cannot connect their work to these outcomes. Customers would not recognize them as describing their experience. The roadmap has been inverted: it is now communicating what the business gets, not what customers get.

**Fix:** Reframe every outcome as a customer achievement: "What does the customer experience or accomplish when this metric improves?" "Increase ARR by 15%" becomes "contract renewal managers approve renewals faster because pricing scenarios are visible before the meeting." The business metric can live in the Business Outcomes header, not in the product outcome row.

### Pitfall 4: Discovery Sections Left Blank

**Symptom:** Tiny Acts of Discovery, Assumptions to Validate, and Assumptions to Research sections are empty or contain placeholder text.

**Consequence:** The artifact signals that discovery is complete. The team is committing to a build plan without active learning. New risks and changed customer behavior will not surface until after outputs are shipped and measured.

**Fix:** Treat empty discovery sections as a red flag, not a formatting gap. At minimum, name one Tiny Act running alongside Now outputs and one assumption in each of Next and Later. If the team genuinely has no open questions, probe: what would have to be true for the Next outcomes to earn high confidence? Those answers are the starting assumptions.

### Pitfall 5: Outputs Not Connected to Outcomes

**Symptom:** The release plan contains outputs that cannot be traced to any outcome in the roadmap row above.

**Consequence:** The team is building things that do not connect to any validated customer value. When asked why something is being built, the answer is "because stakeholders asked for it" or "it was on last year's roadmap."

**Fix:** For each output, ask: which Now outcome does this drive? If no outcome in the Now roadmap row answers that question, either the outcome is missing from the roadmap or the output should not be in the Now release plan.

### Pitfall 6: Static Artifact - Built Once and Never Updated

**Symptom:** The roadmap is built at the start of a planning cycle and never revisited. Later items never graduate to Next. Next items never graduate to Now.

**Consequence:** The roadmap stops reflecting reality. Assumptions resolve but the roadmap does not update. Engineering builds to a plan that discovery has already invalidated.

**Fix:** Establish a specific review cadence tied to discovery milestones, not to the calendar quarter. When a Tiny Act produces a result or an assumption is resolved, the roadmap should update the same week. Build the review trigger into the artifact itself.

### Pitfall 7: Business Outcomes Header Missing or Too Vague

**Symptom:** The header says "grow revenue," "improve operations," "increase customer satisfaction," or is left blank.

**Consequence:** The roadmap floats without an anchor. Individual outcomes cannot be evaluated for whether they actually serve the business goal. Stakeholders cannot see what the team is ultimately trying to achieve.

**Fix:** Make the business outcome specific and measurable. Name the direction, the metric, and the target if possible. "Reduce unplanned equipment downtime by 30% in field service regions by end of year" is an anchor. "Improve operations" is not.

### Pitfall 8: Assumptions Written as Features Instead of Hypotheses

**Symptom:** The Assumptions to Validate section contains items like "build the inventory lookup," "add notification preferences," "integrate with the ERP."

**Consequence:** The assumptions section becomes a shadow feature backlog. No actual assumption is being tested. The team will build these items without knowing whether the underlying customer behavior or need has been confirmed.

**Fix:** Reframe each item as a testable hypothesis about customer behavior: "We believe [customer role] will [specific behavior] when [condition], because [reasoning]." The feature that might follow from a validated assumption is an output - it belongs in the release plan, not in the assumptions section.

### Pitfall 9: A Feature List Dressed as an Outcome Roadmap

**Symptom:** The roadmap's Now column lists "SSO," "mobile app," and "reporting v2," with an outcome heading added on top.

**Consequence:** The team is back in the build trap, with outcome language as decoration. Executives and engineering read it as a feature commitment.

**Fix:** Put product outcomes in each horizon, and link each output to the outcome it serves. Place items by confidence, based on evidence.

## References

### Skill Files

- [template.md](template.md) - working scaffold
- [prompts/](prompts/README.md) - copy-paste prompt for chat-based AI tools (authored for this library; the deck has no AI page for this Play)
- [examples/sample.md](examples/sample.md) - strong, weak, and drift-bug examples

### Related Skills

- **Upstream:** [ps-outcome-tree](../ps-outcome-tree/SKILL.md) provides Business Outcomes and product outcomes for the roadmap row; [ps-output-prioritization](../ps-output-prioritization/SKILL.md) provides Quadrant I and II outputs for the release plan row; [ps-tiny-acts-discovery](../ps-tiny-acts-discovery/SKILL.md) provides Tiny Acts and assumptions for the discovery sections
- **Downstream:** no direct downstream skill; this artifact is the primary communication tool for the Create phase
- **Related:** ps-lofi-experimentation: assumptions from the Next and Later sections may become structured lo-fi experiments

### Project Docs

- [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)
- [informative-documents/framework-glossary.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/framework-glossary.md)
- [informative-documents/skill-dependency-map.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/skill-dependency-map.md)

### Source Material

- [assets/ps_outcome_roadmap_playbook_pages.pdf](assets/ps_outcome_roadmap_playbook_pages.pdf)
- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 78-80: Template 17 of 24 there. No AI page for this Play; the prompts are authored for this library. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).
- [Baseline Playbook version](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml). Full source PDF supplied separately.
- Productside Playbook companion document (supplied separately)

### Playbook Quote

"The value is in what gets used, not what gets built." (Kris Gale, Yammer)

"Discovery is never complete! Your Roadmap and Release plan is a living document. Conduct continuous discovery to ensure your effort is always positively impacting business outcomes."
