# Create: Play references

November 2026 B2B work-in-progress Playbook. Not yet ratified.

Find Plays by stable identifier in 01-playbook-navigator.md. Each Play below contains its instructions, template, and examples. Mentions of skills or agents in the preserved source mean applying the Play from these uploaded references.

## ps-outcome-roadmap | Outcome-Based Roadmap & Release Plan

Playbook number: 17. Phase: Create.

### ps-outcome-roadmap / Instructions

#### Purpose

Create a **Productside-style Outcome-Based Roadmap and Release Plan** from a product team's validated outcomes and prioritized outputs.

This skill helps a Product Manager combine two connected layers into one artifact: a roadmap organized around product outcomes (what customers achieve) and a release plan organized around outputs (features, capabilities, and experiments). Both layers are sorted by confidence level into Now, Next, and Later columns.

The artifact is a **living document**. Discovery is never complete. As the team runs Tiny Acts of Discovery and resolves assumptions, items graduate from Later to Next to Now. The roadmap should be revisited at every major discovery or delivery milestone.

The critical distinction this skill enforces: the **roadmap row speaks outcome language only**. The **release plan row speaks output language only**. Mixing them creates confusion for every audience.

#### Key Concepts

##### Outcomes vs. Outputs - the Load-Bearing Distinction

This roadmap has two rows for a reason. They speak different languages to different audiences.

**Outcomes** are what customers achieve. They describe a changed state in the customer's world: "field technicians resolve equipment faults without returning to the depot," "quality inspectors catch defects before they leave the line." Outcomes belong in the roadmap row.

**Outputs** are what the team builds. They describe a deliverable: "fault diagnosis mobile app," "in-line defect vision scanner," "parts availability lookup." Outputs belong in the release plan row.

When outputs appear in the roadmap row, executives read a feature list instead of a value plan. When outcomes appear in the release plan row, engineering cannot build a sprint from them. Keep the rows separate.

##### The Now / Next / Later Confidence Framework

The three columns are organized by **confidence level**, not by priority or preference.

**Now - High Confidence:** The team has enough validated evidence to commit. These product outcomes have been tested against real customer behavior and real technical constraints. The team is pursuing them actively. Outputs in this column are in the release plan.

**Next - Medium Confidence:** The team believes in these outcomes and output ideas, but needs to resolve specific assumptions before committing fully. The primary work in Next is validation: running assumptions to ground so confident items can graduate to Now.

**Later - Low Confidence:** These are hypotheses - early-stage outcome ideas and open questions that require research before the team can evaluate them seriously. The primary work in Later is research: converting open questions into resolvable assumptions.

Confidence is not a popularity contest. An outcome moves left because the team has resolved uncertainty, not because leadership prefers it.

##### How Items Graduate

- **Later to Next:** When Assumptions to Research resolve enough uncertainty to form a testable assumption with a clear hypothesis.
- **Next to Now:** When Assumptions to Validate confirm enough confidence that the team can commit to the outcome and begin output development.
- **Now to Done:** When the output is shipped and the outcome can be measured.

Items can also move right. If a Now outcome proves harder to achieve than expected, or if new evidence undermines confidence, it should move back to Next for additional validation.

##### Discovery Is Continuous - Not a Future Phase

The discovery activities in this artifact (Tiny Acts of Discovery, Assumptions to Validate, Assumptions to Research) run **in parallel with the release work**. They are not a future phase that begins after Now outputs ship.

While the team is building Now outputs, it is simultaneously running Tiny Acts to refine those outputs, validating assumptions to graduate Next items, and researching questions to graduate Later items. The three columns are active at the same time.

A roadmap with empty discovery sections is not a living document. It is a delivery schedule.

##### Business Outcomes as the Anchor

Everything on the roadmap traces back to the Business Outcomes header. This is the business-level goal the product serves, drawn from the Outcome Tree. It provides the "why behind the what" and prevents the roadmap from becoming a disconnected list of features.

If a product outcome in the Now column cannot be connected to the Business Outcomes header, it should not be on the roadmap.

##### The Artifact Is a Communication Tool

Different audiences need different layers of the same artifact.

**Executives** read the Business Outcomes header and the roadmap row. They see what business goal is being served and what customer outcomes the team is pursuing at each confidence level.

**Engineering** reads the release plan row. They see what is being built (Now outputs), what needs validation before it can enter the build queue (Next output concepts), and what is still being explored (Later assumptions).

**Both audiences** are looking at the same artifact. No separate decks, no translation layer. The structure does the work.

##### This Builds Directly From the Outcome Tree

The product outcomes in the Now and Next roadmap cells should come directly from the ps-outcome-tree, not be invented fresh here. The PM should not use the roadmap as an opportunity to introduce new outcomes that have not been validated through the Outcome Tree play.

If the Outcome Tree has not been run, offer to run ps-outcome-tree first, or accept the PM's description of outcomes directly. But confirm they are grounded in discovery work.

##### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **critic of the roadmap the PM drafted**. It checks that each horizon holds outcomes, not outputs; that items sit in Now, Next, or Later by confidence; that each output links to an outcome; and that discovery work appears alongside delivery. The placements and the sequence stay with the PM and their team.

- **Use it when:** the PM has an outcome tree and a draft roadmap, and wants it pressure-tested before sharing it.
- **Avoid it when:** the request is to produce a dated feature roadmap, or to place items without the PM's evidence about confidence.
- **Return:** outputs posing as outcomes flagged, each placement questioned against the evidence behind it, and links from outputs to outcomes checked.

##### Working With AI

The Productside Playbook sets one rule for every AI-assisted Play: **the Product Manager does the thinking, and AI pressure-tests it.** In this skill, you are the AI. Hold yourself to these rules:

1. **Pressure-test before you produce.** When the user brings a draft, critique it against the Play's formats and criteria first. Point at the specific words that fail and ask the user to fix them. Offer rewrites only after the critique, as options to accept, adapt, or reject.
2. **Never stand in for the customer.** Do not present jobs, quotes, needs, or pains you generated as research, and do not answer as the persona as if your answers were evidence. Anything you draft about customers is a hypothesis, labeled as one, to validate with real people. Role-play is allowed only as rehearsal where the Play calls for it, labeled as practice, and nothing from it goes into findings.
3. **Never stand in for the team's judgment.** Do not put unsourced figures into the artifact, and do not make calls the team should own. A number without a source is a blank to fill, so mark it that way.
4. **Work the five habits.** *Context:* ask for the persona, market, outcome, and constraints when they are missing. *Guide:* offer competing views and welcome pushback. *Enforce:* work inside the Play's template, not around it. *Outcome:* tie the work to the decision it supports. *Iterate:* go step by step rather than one-shot.
5. **Keep best guess honest.** Best guess mode is allowed. When you use it, label every inferred detail inline and end with **Assumptions to Validate**. A best guess is a starting point to test, never a finding.

For people working in a chat tool without this skill, the Play's copy-paste prompts are in prompts/ (uploaded reference: `07-prompts.md`, section `ps-outcome-roadmap / Companion / README.md`).

##### Guided Mode

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

#### Application

Use template.md (uploaded reference: `05-create.md`, section `ps-outcome-roadmap / Template`) for the scaffold.

See the source play pages in assets/ps_outcome_roadmap_playbook_pages.pdf (source material, not included in this upload kit).

##### Required Output Convention

Default to a **clean, paste-ready artifact**.

That means:

- Business Outcomes header is specific and measurable (not "grow revenue")
- At least one product outcome in each column (Now, Next, Later)
- At least two outputs in the Now release plan
- Discovery sections (Tiny Acts, Assumptions to Validate, Assumptions to Research) are not left blank
- Every Now output traces to a Now outcome
- No outputs appear in the roadmap row; no outcomes appear in the release plan row
- Explanation belongs below the artifact, not inside the fields

##### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in prompts/01-pressure-test-roadmap.md (uploaded reference: `07-prompts.md`, section `ps-outcome-roadmap / Companion / 01-pressure-test-roadmap.md`) one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

When a draft roadmap lists outputs (features, releases, projects), don't guess the outcomes behind them, even labeled as guesses. Name each item as an output and ask the PM what customer outcome it serves and what evidence puts it in Now, Next, or Later. The outcomes come from the PM and their customers.

##### Step 1: Tech-Role Bias Guard

Before drafting any content, confirm that the product outcomes are written from the **customer's perspective**. Outcomes describe what customers achieve - what changes in their world when the product works.

The team role bias is to write outcomes in engineering language: "deploy the alert system," "enable real-time API access," "build the reporting module." These are outputs, not outcomes.

Ask the user: who is the customer for this product, and what does success look like from their point of view? What changes in how they work, what they can accomplish, or how they feel about their work?

Do not proceed until there is a customer-perspective answer to that question.

##### Step 2: Gather Upstream Artifacts

Before drafting, ask whether the user has materials to share:

- Outcome Tree from ps-outcome-tree (Business Outcomes and product outcomes)
- Output prioritization results from ps-output-prioritization (Quadrant I and Quadrant II outputs)
- Tiny Acts findings from ps-tiny-acts-discovery (specific experiments and assumptions)
- Any prior roadmap or release plan the team has already discussed

Check whether each exists; offer to help fill gaps; accept equivalent input from any source. Do not gate the skill on whether the upstream play has been run. Accept the PM's direct description if the artifact is not available.

Make a note of which sections are drawn from upstream artifacts and which are being drafted fresh.

##### Step 3: Write the Business Outcomes Header

Draft the Business Outcomes header from the Outcome Tree's business outcome field. This should be one to two sentences describing the business-level goal this roadmap serves.

The header must be specific and anchored. "Reduce unplanned equipment downtime by 30% across field service regions" is anchored. "Improve operational efficiency" is not.

If the outcome has a measurable target, include it. If it does not, note that a target should be defined.

> Quality check: Can you trace every product outcome below to this business goal? If not, either the business goal is too narrow or one of the product outcomes does not belong on this roadmap.

##### Step 4: Populate the NOW Roadmap - Product Outcomes to Pursue

List the product outcomes the team is confident will create customer value and has committed to pursuing. These should come directly from the Outcome Tree (validated product outcomes) or from the PM's description of validated discovery findings.

Write in customer language: what customers achieve, not what the product does.

Each outcome should be specific enough that the team can measure whether it has been achieved. "Field technicians identify root causes without waiting for depot diagnostics" is specific. "Improve technician experience" is not.

> Quality check: Are these outcomes written from the customer's point of view? Can the team measure achievement? Do they trace to the Business Outcomes header?

##### Step 5: Populate the NEXT Roadmap - Product Outcomes to Validate

List the product outcomes the team believes in but has not yet validated enough to commit to. These outcomes need testing - specific assumptions must resolve before the team can move them to Now.

For each outcome, the key question is: what would have to be true for this to earn high confidence?

> Quality check: Is each outcome distinct from the Now outcomes? Is there a clear validation question that could move this outcome left?

##### Step 6: Populate the LATER Roadmap - Product Outcome Hypotheses

List early-stage outcome ideas that require research before the team can even form a testable hypothesis. These are genuine unknowns - areas where the team has a direction but not enough understanding to design a validation test.

Write these as outcome hypotheses, not as research questions. "Procurement managers could reduce approval cycle time to under 48 hours if sourcing exceptions were flagged earlier" is a hypothesis. "Research whether procurement managers care about approval times" is a research question.

> Quality check: Is each hypothesis plausible based on existing domain knowledge? Is there a clear question that would move this to Next?

##### Step 7: Populate Outputs to Develop (NOW)

List the features and capabilities that will drive the Now outcomes. These come from Quadrant I outputs in ps-output-prioritization (low cost, high value) or from the PM's direct input on what is in active development.

Write as specific output names, not categories. "Real-time fault alert push notification" is specific. "Notification system" is a category.

> Quality check: Does every output trace to a Now outcome? If an output cannot be connected to a Now outcome, it should not be in the Now release plan.

##### Step 8: List Tiny Acts of Discovery (NOW)

List the small, fast experiments the team is running in parallel with Now output development. These come from ps-tiny-acts-discovery or from the PM's direct input.

Each Tiny Act should be specific enough to run: name what is being tested, how, and with whom. "Run a 5-person session with field technicians using a paper mock of the fault alert screen to confirm the alert hierarchy makes sense to them" is a Tiny Act. "Test the UI" is not.

> Quality check: Are these running now, in parallel with the outputs being built? Are they specific enough to execute this week?

##### Step 9: Populate Output Concepts to Validate (NEXT)

List the output ideas that need validation before entering the release plan. These come from Quadrant II outputs in ps-output-prioritization (high cost, high value - needs more evidence before committing) or from the PM's description of candidates under consideration.

> Quality check: Is each concept clearly tied to a Next outcome? Is there a specific assumption that, if validated, would move this into Now outputs?

##### Step 10: List Assumptions to Validate (NEXT)

List the specific hypotheses and assumptions that must be resolved to move Next outcomes and output concepts to Now. Write these as testable hypothesis statements, not as features.

Format: "We believe [customer segment] will [behavior or outcome] when [condition or stimulus], because [reasoning]."

A well-formed assumption can be tested. A feature request ("build the dashboard") cannot.

> Quality check: Is each assumption specific enough to design a test around? Does each assumption trace to a Next outcome or output concept?

##### Step 11: List Assumptions to Research (LATER)

List the open questions and hypotheses that must be explored to move Later outcome hypotheses to Next. These are broader than testable assumptions - they require research to even know what to test.

Write as open questions or early hypotheses. The goal is to move from "we don't know" to "we have a hypothesis we can test."

> Quality check: Is each question specific enough to guide research? Can the PM name a method (interviews, observation, data pull) that would start to answer it?

##### Step 12: Review Alignment

Before presenting the artifact, check:

- Every Now output traces to a Now outcome
- No outputs appear in the roadmap row
- No outcomes appear in the release plan row
- Discovery sections are not blank
- Business Outcomes header is specific and measurable
- Now, Next, and Later columns each have content (the roadmap is not front-loaded into Now)

If an output cannot be traced to an outcome, ask whether the outcome belongs on the roadmap and is missing, or whether the output should be reconsidered.

##### Step 13: Offer Next Steps

At the end of the artifact, offer three options:

1. Share the roadmap with leadership: the Business Outcomes header and roadmap row give executives the outcome-level view they need to evaluate direction without getting into features
2. Share the release plan with engineering: the output-focused bottom row gives the team concrete, prioritized work with clear discovery activities running alongside
3. Schedule a review cadence: propose a specific date or milestone trigger for the next roadmap review, so the artifact stays current as assumptions resolve

#### Examples

See examples/sample.md (uploaded reference: `05-create.md`, section `ps-outcome-roadmap / Examples`).

The example set includes:

- a strong outcome-based roadmap with clear outcome language in the roadmap row, output language in the release plan row, and active discovery sections in all three columns
- a weak version where outputs appear in the roadmap row, all outcomes are in Now, and discovery sections are empty
- a drift-bug example where outcomes are written in business/financial language instead of customer outcome language, turning the roadmap into an internal financial plan

#### Common Pitfalls

##### Pitfall 1: Feature-Based Roadmap - Outputs in the Roadmap Row

**Symptom:** The roadmap row contains items like "launch the mobile app," "add dashboard reporting," "migrate to microservices."

**Consequence:** Executives read a feature list. They cannot evaluate whether the team is working on the right customer problems. Engineering has no anchor for what customer value each output is supposed to create.

**Fix:** Ask: what does the customer achieve when this output exists and works? That answer is the outcome. Replace the output in the roadmap row with the outcome. Move the output to the release plan row.

##### Pitfall 2: All Outcomes in NOW - No Differentiation by Confidence

**Symptom:** Every product outcome is in the Now column. Next and Later are empty or have token content.

**Consequence:** The roadmap communicates false certainty. There is no signal about what is validated versus what is directional. Leadership cannot assess where the team is taking risk.

**Fix:** Push the team to differentiate honestly. If everything is high confidence, either the team is building too narrowly or they have not surfaced what they do not yet know. Most real product situations have at least two or three outcome hypotheses in Next or Later.

##### Pitfall 3: Roadmap Written in Business/Financial Language

**Symptom:** Roadmap outcomes read as: "increase ARR by 15%," "reduce churn 10 basis points," "improve NPS by 5 points."

**Consequence:** The roadmap becomes an internal financial plan, not a customer value plan. Engineering cannot connect their work to these outcomes. Customers would not recognize them as describing their experience. The roadmap has been inverted: it is now communicating what the business gets, not what customers get.

**Fix:** Reframe every outcome as a customer achievement: "What does the customer experience or accomplish when this metric improves?" "Increase ARR by 15%" becomes "contract renewal managers approve renewals faster because pricing scenarios are visible before the meeting." The business metric can live in the Business Outcomes header, not in the product outcome row.

##### Pitfall 4: Discovery Sections Left Blank

**Symptom:** Tiny Acts of Discovery, Assumptions to Validate, and Assumptions to Research sections are empty or contain placeholder text.

**Consequence:** The artifact signals that discovery is complete. The team is committing to a build plan without active learning. New risks and changed customer behavior will not surface until after outputs are shipped and measured.

**Fix:** Treat empty discovery sections as a red flag, not a formatting gap. At minimum, name one Tiny Act running alongside Now outputs and one assumption in each of Next and Later. If the team genuinely has no open questions, probe: what would have to be true for the Next outcomes to earn high confidence? Those answers are the starting assumptions.

##### Pitfall 5: Outputs Not Connected to Outcomes

**Symptom:** The release plan contains outputs that cannot be traced to any outcome in the roadmap row above.

**Consequence:** The team is building things that do not connect to any validated customer value. When asked why something is being built, the answer is "because stakeholders asked for it" or "it was on last year's roadmap."

**Fix:** For each output, ask: which Now outcome does this drive? If no outcome in the Now roadmap row answers that question, either the outcome is missing from the roadmap or the output should not be in the Now release plan.

##### Pitfall 6: Static Artifact - Built Once and Never Updated

**Symptom:** The roadmap is built at the start of a planning cycle and never revisited. Later items never graduate to Next. Next items never graduate to Now.

**Consequence:** The roadmap stops reflecting reality. Assumptions resolve but the roadmap does not update. Engineering builds to a plan that discovery has already invalidated.

**Fix:** Establish a specific review cadence tied to discovery milestones, not to the calendar quarter. When a Tiny Act produces a result or an assumption is resolved, the roadmap should update the same week. Build the review trigger into the artifact itself.

##### Pitfall 7: Business Outcomes Header Missing or Too Vague

**Symptom:** The header says "grow revenue," "improve operations," "increase customer satisfaction," or is left blank.

**Consequence:** The roadmap floats without an anchor. Individual outcomes cannot be evaluated for whether they actually serve the business goal. Stakeholders cannot see what the team is ultimately trying to achieve.

**Fix:** Make the business outcome specific and measurable. Name the direction, the metric, and the target if possible. "Reduce unplanned equipment downtime by 30% in field service regions by end of year" is an anchor. "Improve operations" is not.

##### Pitfall 8: Assumptions Written as Features Instead of Hypotheses

**Symptom:** The Assumptions to Validate section contains items like "build the inventory lookup," "add notification preferences," "integrate with the ERP."

**Consequence:** The assumptions section becomes a shadow feature backlog. No actual assumption is being tested. The team will build these items without knowing whether the underlying customer behavior or need has been confirmed.

**Fix:** Reframe each item as a testable hypothesis about customer behavior: "We believe [customer role] will [specific behavior] when [condition], because [reasoning]." The feature that might follow from a validated assumption is an output - it belongs in the release plan, not in the assumptions section.

##### Pitfall 9: A Feature List Dressed as an Outcome Roadmap

**Symptom:** The roadmap's Now column lists "SSO," "mobile app," and "reporting v2," with an outcome heading added on top.

**Consequence:** The team is back in the build trap, with outcome language as decoration. Executives and engineering read it as a feature commitment.

**Fix:** Put product outcomes in each horizon, and link each output to the outcome it serves. Place items by confidence, based on evidence.

#### References

##### Skill Files

- template.md (uploaded reference: `05-create.md`, section `ps-outcome-roadmap / Template`) - working scaffold
- prompts/ (uploaded reference: `07-prompts.md`, section `ps-outcome-roadmap / Companion / README.md`) - copy-paste prompt for chat-based AI tools (authored for this library; the deck has no AI page for this Play)
- examples/sample.md (uploaded reference: `05-create.md`, section `ps-outcome-roadmap / Examples`) - strong, weak, and drift-bug examples

##### Related Skills

- **Upstream:** ps-outcome-tree (uploaded reference: `02-context.md`, section `ps-outcome-tree / Instructions`) provides Business Outcomes and product outcomes for the roadmap row; ps-output-prioritization (uploaded reference: `05-create.md`, section `ps-output-prioritization / Instructions`) provides Quadrant I and II outputs for the release plan row; ps-tiny-acts-discovery (uploaded reference: `05-create.md`, section `ps-tiny-acts-discovery / Instructions`) provides Tiny Acts and assumptions for the discovery sections
- **Downstream:** no direct downstream skill; this artifact is the primary communication tool for the Create phase
- **Related:** ps-lofi-experimentation: assumptions from the Next and Later sections may become structured lo-fi experiments

##### Project Docs

- [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)
- [informative-documents/framework-glossary.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/framework-glossary.md)
- [informative-documents/skill-dependency-map.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/skill-dependency-map.md)

##### Source Material

- assets/ps_outcome_roadmap_playbook_pages.pdf (source material, not included in this upload kit)
- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 78-80: Template 17 of 24 there. No AI page for this Play; the prompts are authored for this library. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).
- [Baseline Playbook version](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml). Full source PDF supplied separately.
- Productside Playbook companion document (supplied separately)

##### Playbook Quote

"The value is in what gets used, not what gets built." (Kris Gale, Yammer)

"Discovery is never complete! Your Roadmap and Release plan is a living document. Conduct continuous discovery to ensure your effort is always positively impacting business outcomes."

### ps-outcome-roadmap / Template

### Outcome-Based Roadmap and Release Plan

#### When to Use This

Use this template during the **Create** phase after completing your Outcome Tree and Output Prioritization. It is most powerful when Tiny Acts of Discovery results are available to populate the discovery sections.

Upstream artifacts that feed this template:
- Outcome Tree (ps-outcome-tree): Business Outcomes header and product outcomes for the roadmap row
- Output Prioritization (ps-output-prioritization): Quadrant I outputs for Now release plan; Quadrant II outputs for Next output concepts
- Tiny Acts of Discovery (ps-tiny-acts-discovery): specific experiments and assumptions for the discovery sections

---

#### Template

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

[List 2-4 specific features or capabilities the team is actively building to drive the Now outcomes. Each output should trace to a Now outcome above. Use Quadrant I outputs from ps-output-prioritization if available.]

- [Output 1: specific feature or capability name - 5-10 words]
- [Output 2: specific feature or capability name - 5-10 words]
- [Output 3: specific feature or capability name - 5-10 words]

> Quality check: Does each output trace to a Now outcome above? Are these specific enough to build a sprint from? No outcomes should appear here.
> Capacity check: 2-4 outputs; 5-10 words each.

**Tiny Acts of Discovery**

[List 1-2 small, fast experiments running now alongside output development. These are not future work - they run in parallel with the outputs above. Use Tiny Acts from ps-tiny-acts-discovery if available.

Format: name the test, the method, and the participants. 10-20 words each.]

- [Tiny Act 1: specific test with named method and participants, running in parallel with Now outputs]
- [Tiny Act 2: specific test with named method and participants]

> Quality check: Are these running now, not after Now outputs ship? Are they specific enough to execute this week? Do they connect to the outputs being built?
> Capacity check: 1-2 Tiny Acts; 10-20 words each.

---

### NEXT
**Output Concepts to Validate**

[List 1-2 output ideas that need validation before entering the release plan. These are candidates, not commitments. Use Quadrant II outputs from ps-output-prioritization if available - high value, high cost items that need more evidence before committing.]

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

#### Usage Guidance

##### Filling the Template

1. Complete **Business Outcomes** first. Everything below it must trace back to this header.
2. Fill the **Roadmap row** (Now, Next, Later) using outcome language. Do not place any feature or output name in this row.
3. Fill the **Release Plan row** (Now, Next, Later) using output language. Do not place any customer outcome statement in this row.
4. Check that every Now output in the release plan traces to a Now outcome in the roadmap.
5. Fill the discovery sections (Tiny Acts, Assumptions to Validate, Assumptions to Research). If any are blank, the artifact is not ready.
6. Add the **Living Document Note** before sharing.

##### What Goes Where

| Section | Language | Contains | Does NOT Contain |
|---------|----------|----------|-----------------|
| Roadmap row | Outcome language | What customers achieve | Features, capabilities, deliverables |
| Release plan row | Output language | What the team builds | Customer outcome statements |
| Business Outcomes header | Business language | Business-level goal with measurable target | Vague directions like "grow revenue" |
| Tiny Acts of Discovery | Action language | Specific tests running now | Future research phases |
| Assumptions to Validate | Hypothesis language | Testable beliefs about customer behavior | Feature requests or build decisions |
| Assumptions to Research | Question language | Open questions needing research | Assumptions already ready to test |

##### The Graduation Path

Items move left as confidence increases:

- Later outcome hypothesis + research resolved = moves to Next as Product Outcome to Validate
- Next outcome + assumptions validated = moves to Now as Product Outcome to Pursue
- Next output concept + assumptions validated = moves to Now as Output to Develop
- Now output shipped + outcome achieved = removed from roadmap; captured in metrics

Items can move right if confidence decreases. A Now outcome with an unexpected discovery finding should move back to Next for additional validation rather than continuing to drive output development on a weakened foundation.

##### Connecting to Other Skills

- **Upstream:** ps-outcome-tree provides the Business Outcomes header and product outcomes for the roadmap row. ps-output-prioritization provides Quadrant I outputs for Now and Quadrant II outputs for Next output concepts. ps-tiny-acts-discovery provides specific experiments and assumptions.
- **Downstream:** This artifact is the primary communication tool for the Create phase. Share the roadmap row (outcome language) with leadership and the release plan row (output language) with engineering.

##### Capacity Reference

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

### ps-outcome-roadmap / Examples

### Outcome-Based Roadmap and Release Plan Examples

All three examples use a **field service operations** scenario: a SaaS product for utilities and industrial maintenance organizations, helping field technicians diagnose equipment faults and dispatch replacement parts without returning to the depot.

---

#### Example 1 - Strong

**Context:** The PM has completed the Outcome Tree, Output Prioritization, and two rounds of Tiny Acts of Discovery with field technicians and dispatch coordinators. The product is in the Create phase. The team is preparing a roadmap to share with operations leadership and the engineering team.

---

##### Outcome-Based Roadmap and Release Plan

**Product or initiative:** FieldResolve - equipment fault diagnosis and parts dispatch platform
**Date:** June 26, 2026
**Team:** Priya Sharma (PM), Marcus Webb (Engineering Lead), Dana Okonkwo (Dispatch Ops Lead)

---

**Business Outcomes**

Reduce unplanned equipment downtime by 30% across field service regions within 12 months, enabling regional operations teams to meet SLA commitments without emergency dispatch costs.

---

**Roadmap**

##### NOW - High Confidence
**Product Outcomes to Pursue**

- Field technicians identify the root cause of electrical faults on-site without calling the depot, completing diagnosis in under 20 minutes.
- Dispatch coordinators confirm parts availability and initiate orders during the technician's on-site window, avoiding a second site visit.

##### NEXT - Medium Confidence
**Product Outcomes to Validate**

- Regional operations managers see real-time fault resolution status across all active jobs without requiring phone-based status checks from coordinators.
- Field technicians self-assign to nearby jobs without dispatcher involvement when their primary job closes ahead of schedule.

##### LATER - Low Confidence
**Product Outcome Hypotheses**

- Technicians could reduce repeat fault rates by accessing structured repair history for specific equipment models at the point of diagnosis.
- Preventive maintenance schedulers could reduce emergency dispatch volume by acting on predictive signals from resolved fault patterns before equipment failures occur.

---

**Release Plan**

##### NOW
**Outputs to Develop**

- On-site fault diagnosis guided workflow (mobile, offline-capable)
- Parts availability real-time lookup with depot inventory integration
- One-tap parts order initiation from the fault diagnosis screen

**Tiny Acts of Discovery**

- 6-person walkthrough with field technicians using a paper prototype of the fault diagnosis workflow to confirm the decision tree covers their most common fault types (running this week; Priya coordinating with Dana)
- Pull 90 days of dispatch logs to confirm whether parts availability checks happen before or after the technician leaves the site (data pull; Marcus assigned)

---

##### NEXT
**Output Concepts to Validate**

- Regional job status dashboard (live map view for coordinators and ops managers)
- Technician self-scheduling interface for surplus capacity after job close

**Assumptions to Validate**

- We believe dispatch coordinators will use a live job status dashboard to replace their current phone check-in process, because they have described phone interruptions as their primary workload bottleneck.
- We believe field technicians will accept self-assignment to nearby jobs when their primary job closes early, because interviews suggest they prefer staying in the field over returning to the depot when capacity allows.
- We believe ops managers will act on real-time status dashboards to make coverage decisions without waiting for end-of-day coordinator reports.

---

##### LATER
**Assumptions to Research**

- Do technicians retain enough structured fault data after a job closes that a repair history lookup would change their on-site diagnosis behavior, or do they rely on personal memory and informal peer contact?
- Which equipment categories generate the most repeat fault patterns, and do schedulers currently have visibility into those patterns at all?
- Would predictive signals from resolved fault data be specific enough for schedulers to act on, or would the volume of low-confidence signals create alert fatigue?

---

**Living Document Note**

- Next scheduled review: when the Tiny Act results are in (target: 10 days)
- Trigger for unscheduled review: if fault diagnosis completion rate in pilot falls below 70% in first 30 days
- Owner of the review cadence: Priya Sharma

---

##### Why This Works

**Outcome language is preserved in the roadmap row.** Every item in the Now, Next, and Later roadmap sections describes what a field technician, coordinator, or ops manager achieves - not what the product does. "Field technicians identify the root cause of electrical faults on-site" is an outcome. "On-site fault diagnosis guided workflow" is an output - correctly placed in the release plan row.

**Output language is preserved in the release plan row.** The three Now outputs are specific, buildable deliverables. None of them are customer outcome statements. Engineering can write a sprint from these.

**Discovery is active, not future.** The two Tiny Acts are running now - one this week - not scheduled as a phase after Now outputs ship. The Assumptions to Validate connect directly to the Next output concepts. The Assumptions to Research connect to the Later hypotheses.

**Every Now output traces to a Now outcome.** The fault diagnosis workflow drives "field technicians identify root cause without calling the depot." The parts lookup and order initiation drive "dispatch coordinators confirm availability and initiate orders during the site window." No output is floating without an outcome anchor.

**Business Outcomes anchor the whole structure.** The 30% downtime reduction target is specific and measurable. Every product outcome below it can be evaluated for whether it plausibly contributes to that goal.

---

#### Example 2 - Weak

**Context:** Same scenario, same team. The roadmap was built quickly to meet a planning deadline, without reviewing Outcome Tree results or checking whether the discovery sections were complete.

---

##### Outcome-Based Roadmap and Release Plan

**Product or initiative:** FieldResolve
**Date:** June 26, 2026
**Team:** Priya, Marcus, Dana

---

**Business Outcomes**

Improve field service efficiency and reduce costs.

---

**Roadmap**

##### NOW - High Confidence
**Product Outcomes to Pursue**

- Launch mobile fault diagnosis app
- Build parts inventory lookup
- Add one-tap order button
- Create coordinator dashboard
- Enable technician self-scheduling
- Add repair history search

##### NEXT - Medium Confidence
**Product Outcomes to Validate**

- Performance optimization
- Additional integrations

##### LATER - Low Confidence
**Product Outcome Hypotheses**

- Future enhancements based on feedback

---

**Release Plan**

##### NOW
**Outputs to Develop**

- Mobile fault diagnosis app
- Parts inventory lookup
- One-tap order button
- Coordinator dashboard
- Technician self-scheduling
- Repair history search

**Tiny Acts of Discovery**

[None planned - will evaluate after launch]

---

##### NEXT
**Output Concepts to Validate**

- Performance optimization
- Additional integrations

**Assumptions to Validate**

[TBD]

---

##### LATER
**Assumptions to Research**

[TBD]

---

##### Why This Fails

**The roadmap row is full of outputs, not outcomes.** "Launch mobile fault diagnosis app," "build parts inventory lookup," and "add one-tap order button" are all outputs - things the team builds. They describe the product, not what customers achieve. An executive reading this roadmap cannot evaluate whether the team is solving the right customer problem. They see a feature list.

**Everything is in Now with no confidence differentiation.** Six items in the Now roadmap, two vague placeholders in Next, and a single line in Later. This does not reflect genuine confidence assessment - it reflects the team not doing the work of sorting by evidence. There is no signal about what is validated versus what is directional.

**Discovery sections are empty.** "None planned - will evaluate after launch" is the most dangerous phrase in a roadmap. It treats discovery as something that happens after shipping, not alongside it. The team has committed to building six outputs without any active learning about whether customers will use them.

**Business Outcomes is too vague to anchor anything.** "Improve field service efficiency and reduce costs" describes a direction, not a goal. There is no metric, no target, no timeframe. Nothing below it can be evaluated for whether it contributes to this goal, because the goal is too general to fail.

**The roadmap and release plan contain identical content.** When both rows say the same things, the two-layer structure has not been used. The outcome language and output language have not been separated. The artifact communicates nothing to executives that it does not also say to engineering - and it fails both audiences because it mixes the languages.

---

#### Example 3 - Drift Bug: Business/Financial Language in the Roadmap Row

**Context:** Same scenario. The PM has strong financial instincts and is accustomed to communicating with executives in business metric terms. The roadmap outcomes have been written to speak to a CFO review, not to describe what customers achieve.

---

##### Outcome-Based Roadmap and Release Plan

**Product or initiative:** FieldResolve
**Date:** June 26, 2026
**Team:** Priya, Marcus, Dana

---

**Business Outcomes**

Achieve 30% reduction in unplanned downtime costs and a 15% improvement in field workforce utilization by end of fiscal year.

---

**Roadmap**

##### NOW - High Confidence
**Product Outcomes to Pursue**

- Reduce emergency dispatch costs by $2M annually through faster on-site resolution
- Decrease parts logistics spend by 20% through inventory visibility at the point of service

##### NEXT - Medium Confidence
**Product Outcomes to Validate**

- Increase field technician utilization rate from 68% to 78%
- Reduce coordinator overhead by 0.5 FTE through workflow automation

##### LATER - Low Confidence
**Product Outcome Hypotheses**

- Predictive maintenance data could reduce total failure incidents 15% year-over-year

---

*[Release plan below is well-formed - not repeated here for brevity.]*

---

##### Why This Fails - and How to Fix It

**The roadmap row has inverted the language.** Every item in the roadmap now describes a business or financial result, not a customer outcome. "Reduce emergency dispatch costs by $2M," "decrease parts logistics spend by 20%," "increase field technician utilization rate from 68% to 78%" - these are internal business metrics. A field technician, dispatch coordinator, or operations manager would not recognize their daily work in any of these statements.

**This is the Business Outcomes header language, not the Roadmap row language.** The Business Outcomes header is the correct place for financial targets. The roadmap row should answer: "What changes in how customers work when this outcome is achieved?" The financial result follows from the customer outcome - it is not the outcome itself.

**The inversion matters because it breaks the communication function.** Engineering cannot connect their work to "reduce emergency dispatch costs by $2M." They can connect it to "field technicians identify fault root cause without calling the depot." The financial metric is the result of thousands of technicians diagnosing faults faster. The outcome is what the technician experiences.

**The Fix - Reframe Each Item as a Customer Achievement:**

| Financial Language (Wrong) | Customer Outcome Language (Right) |
|---|---|
| Reduce emergency dispatch costs by $2M annually through faster on-site resolution | Field technicians resolve electrical faults on-site without returning to the depot, completing resolution in under 20 minutes |
| Decrease parts logistics spend by 20% through inventory visibility at point of service | Dispatch coordinators confirm parts availability and initiate orders before the technician leaves the site |
| Increase field technician utilization rate from 68% to 78% | Field technicians complete a second job during their shift when their primary job closes ahead of schedule |
| Reduce coordinator overhead by 0.5 FTE through workflow automation | Dispatch coordinators manage daily job assignments without manually calling each technician for status updates |

The business metrics do not disappear - they move to the Business Outcomes header and the success metrics section of the Outcome Tree. The roadmap row communicates what customers experience. The financial outcomes follow from the customer outcomes, but they are not the same thing.

## ps-tiny-acts-discovery | Tiny Acts of Discovery

Playbook number: 18. Phase: Create.

### ps-tiny-acts-discovery / Instructions

#### Purpose

Create a **Productside-style Tiny Acts of Discovery artifact** from a collaborative team session on a product at any stage of development.

This skill helps a Product Manager and their team build an ongoing habit of assumption validation. The playbook states explicitly: "This tool can be used in many phases of a product process or lifecycle." Although it is placed in the Create phase, it applies equally in Discover, Define, and after launch.

This is a **process skill**. The agent helps the PM plan and document the exercise. Steps 1 through 4 (what we know, what we don't, prioritizing assumptions, writing hypotheses) happen in the conversation. Step 5 (running the tiny acts with real users, customers, or data) happens in the field. The agent cannot conduct interviews, run surveys, or generate user research findings on the team's behalf.

The goal is not a single checkpoint. The goal is a culture of continuous learning - what the playbook calls "fail often, fail fast." Failures are data, not setbacks.

#### Key Concepts

##### The Five-Step Flow

The exercise follows a fixed sequence:

1. **What do we know?** - Validated facts, observed behaviors, completed research, confirmed assumptions.
2. **What do we not know?** - Gaps, unvalidated assumptions, open questions, missing data.
3. **Prioritize your assumptions** - Classify each "don't know" by impact and uncertainty on a 2x2.
4. **Form your hypotheses** - Write If/Then statements for the top-priority assumptions.
5. **List your Tiny Acts of Discovery** - Design one small, fast test per hypothesis, assign a metric and an owner.

##### A Living Backlog, Not a One-Time List

Tiny acts of discovery is a **habit**: keep a prioritized backlog of assumptions about the product and chip away at it with small, fast acts of learning, over and over. Re-score the backlog whenever new evidence arrives, and keep it where stakeholders can see it. A tiny act can be almost anything: one question to one user, a survey, a fake-door or willingness-to-pay test, a five-person expert chat, a quick prototype. The craft is finding the shortest path to a signal.

A backlog that never gets worked is planning, not discovery. If no act ever runs, the exercise has failed, however tidy the list.

##### The Certainty Score Is the PM's

Only the PM knows how much evidence they actually hold, so **the PM places every assumption** on impact and certainty. The skill pushes on the evidence ("what is it, and how confident are you in it?") and points at placements that look off. It does not move them. A backlog scored by a model is built on the model's guesses, and no one can explain why this, why now.

##### Impact vs. Uncertainty

The 2x2 matrix uses two dimensions:

- **Impact (Y-axis):** If this assumption turns out to be wrong, how much does it damage the product goal? High impact = major rework or goal failure. Low impact = minor friction.
- **Uncertainty (X-axis):** How much evidence do you currently have? High uncertainty = little or no evidence (the opposite of confidence). Low uncertainty = some evidence already exists.

**This is not the same as Output Prioritization**, which uses Value vs. Cost/Effort. Here, the dimensions are the cost of being wrong and the absence of supporting evidence. High impact + high uncertainty = most urgent to test. These go in the upper-right of the matrix.

##### How to Classify an Assumption

Two questions determine placement:

- "If we are wrong about this, does the product goal fail or require major rework?" - this sets Impact.
- "How much evidence do we currently have that supports this being true?" - the less evidence, the higher the Uncertainty rating.

##### Tiny Acts vs. Lo-fi Experimentation

These are related but not interchangeable:

- **Lo-fi Experimentation (Template 14)** is a formal, structured test plan for a single make-or-break assumption. It specifies a full hypothesis with a numeric threshold, a complete method, decision rules with three tiers, a time window, and an audience size. Use Lo-fi when you need a rigorous, documented test before committing to a major build decision.
- **Tiny Acts of Discovery** is for ongoing, lightweight assumption management across many assumptions simultaneously. Tests are smaller. Documentation is lighter. The intent is a culture of continuous learning, not one big formal experiment. Use Tiny Acts when you want to test many assumptions quickly and keep the team calibrated week to week.

A PM who uses Tiny Acts well will identify the single highest-stakes assumption that needs Lo-fi treatment. The two tools work together.

##### Tiny Acts Keep Development Customer-Focused

The purpose of Tiny Acts of Discovery is to anchor product decisions in what real customers actually do, need, and believe — not in what the team assumes from the inside. Every assumption worth testing should trace back to a customer behavior, a customer value question, or a customer adoption question.

When the team runs these exercises honestly, they replace internal debate with evidence. A user walkthrough result, a data pull, a survey response — these are the inputs that make the development process data-driven rather than opinion-driven. The team learns what customers genuinely need before committing resources to build it.

This is why a "don't know" list composed entirely of technical unknowns misses the point. Technical assumptions matter, but the assumptions that most often determine whether a product succeeds are behavioral and organizational: will customers change their current workflow, does the customer agree the problem is worth solving, will the organization adopt it? Centering Tiny Acts on these questions keeps development focused on meeting actual user needs.

##### The Culture of Continuous Learning

The playbook frames this as "fail often, fail fast." Each tiny act is a deliberate, low-cost way to get signal before investing in something bigger. A test that disproves a hypothesis is not a failure - it is learning that prevents a more expensive mistake downstream. Teams that skip this practice tend to discover wrong assumptions after significant time and money have been spent.

##### Why the Agent Cannot Run the Acts

The tiny acts are field research: user interviews, prototype walkthroughs, data pulls, A/B tests, short surveys administered to real customers. The agent can help design the specific acts, define the metrics, and document results when the PM returns with findings. It cannot conduct research, generate synthetic user responses as if they were real, or simulate field data.

##### How AI Supports This Play

The Playbook casts AI as a **thought partner across the loop**. The PM collects the opportunities and names the assumptions beneath them. AI widens the view and tests how confident the PM really is. The PM picks what to learn next.

- **Use it when:** the PM has a pile of opportunities, ideas, or signals and wants a prioritized backlog of assumptions plus fast, cheap ways to start testing them.
- **Avoid it when:** the backlog is being used to look busy. If no act ever gets run, the skill is helping the team plan instead of discover. Ask which act will run this week.
- **Return:** raw opportunities turned into testable assumptions, the PM's impact and certainty ranking pressure-tested, and a wide range of fast, creative ways to start learning.

##### Working With AI

The Productside Playbook sets one rule for every AI-assisted Play: **the Product Manager does the thinking, and AI pressure-tests it.** In this skill, you are the AI. Hold yourself to these rules:

1. **Pressure-test before you produce.** When the user brings a draft, critique it against the Play's formats and criteria first. Point at the specific words that fail and ask the user to fix them. Offer rewrites only after the critique, as options to accept, adapt, or reject.
2. **Never stand in for the customer.** Do not present jobs, quotes, needs, or pains you generated as research, and do not answer as the persona as if your answers were evidence. Anything you draft about customers is a hypothesis, labeled as one, to validate with real people. Role-play is allowed only as rehearsal where the Play calls for it, labeled as practice, and nothing from it goes into findings.
3. **Never stand in for the team's judgment.** Do not put unsourced figures into the artifact, and do not make calls the team should own. A number without a source is a blank to fill, so mark it that way.
4. **Work the five habits.** *Context:* ask for the persona, market, outcome, and constraints when they are missing. *Guide:* offer competing views and welcome pushback. *Enforce:* work inside the Play's template, not around it. *Outcome:* tie the work to the decision it supports. *Iterate:* go step by step rather than one-shot.
5. **Keep best guess honest.** Best guess mode is allowed. When you use it, label every inferred detail inline and end with **Assumptions to Validate**. A best guess is a starting point to test, never a finding.

For people working in a chat tool without this skill, the Play's copy-paste prompts are in prompts/ (uploaded reference: `07-prompts.md`, section `ps-tiny-acts-discovery / Companion / README.md`).

##### Guided Mode

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

#### Application

Use template.md (uploaded reference: `05-create.md`, section `ps-tiny-acts-discovery / Template`) for the scaffold.

See the source play pages in assets/ps_tiny_acts_discovery_playbook_pages.pdf (source material, not included in this upload kit).

##### Required Output Convention

Default to a **clean, paste-ready artifact**.

That means:

- at least 3 items in the "what we know" list, grounded in evidence
- at least 3 items in the "what we don't know" list, covering a range of assumption categories
- all assumptions classified on both dimensions (impact and uncertainty)
- a clear top-3 emerging from the classification
- one If/Then hypothesis per top-priority assumption
- one tiny act per hypothesis, with a specific metric and a named owner
- explanation belongs below the artifact, not inside the fields

##### Step 1: Confirm Scope and Session Context

Before starting, confirm three things:

1. **What product is this?** Get a one-sentence description of what the product does and who it is for. Vague product descriptions produce vague assumption lists.
2. **What lifecycle phase is the team in?** Tiny Acts applies at any phase, but the categories of unknowns differ. A team in early discovery has mostly behavioral and market unknowns. A team in late Create has mostly technical and adoption unknowns.
3. **Who is in this session?** Tiny Acts is a team exercise. The assumption list should reflect cross-functional perspectives. If the PM is working alone, note this — solo lists tend to be narrower and may miss organizational, adoption, and customer-behavior assumptions.

If the PM is working alone without team input, recommend they share the output with one or two stakeholders before designing the tiny acts.

##### Step 2: Tech-Role Bias Guard

Before building the assumption list, confirm what the product does and who actually uses it. Most products do not serve developers or technical architects. A supply chain management platform serves logistics coordinators and warehouse managers. A clinical data platform serves clinical operations leads and data managers. A field service app serves technicians and dispatchers.

Ask the PM directly: "Who is the person who will use this product day-to-day? What is their job title and what does their work look like?" This answer should shape every assumption on the list - the knowns, the unknowns, the hypotheses, and the tiny acts.

Do not allow the assumption list to default to technical unknowns (performance, integration, security) while missing the behavioral and organizational unknowns that most often determine whether a product succeeds.

##### Step 3: Gather Available Artifacts

Before drafting, ask whether the user has relevant materials to share:

- Solution hypothesis from ps-solution-hypothesis (defines what is being tested)
- Problem statement from ps-framing-the-problem (gives the customer and problem context)
- Outcome tree from ps-outcome-tree (clarifies what the team is trying to achieve)
- Any prior research, field observations, or customer feedback already collected
- Existing roadmap items or backlog priorities (these often reveal implicit assumptions)

The more context about what is being built and for whom, the more targeted the assumption list will be. Accept equivalent context from any source - the PM does not need to have run these upstream plays first.

##### Step 4: List What the Team Knows

Help the PM articulate the validated knowns. Push for evidence, not belief. For each item on the "what we know" list, the PM should be able to say where the knowledge came from: an interview, a data pull, a completed test, direct observation, signed research.

Watch for three failure modes:
- Assumptions dressed up as facts ("We know customers want faster reports" with no evidence)
- Old knowledge that has not been revalidated since the product changed
- Team consensus that has never been tested outside the building

Prompt: "How do you know this? What was the source?" If the PM cannot answer, move the item to the "don't know" list.

##### Step 5: List What the Team Does Not Know

Help the PM surface the gaps. Push for breadth across assumption categories, not just technical unknowns:

- **Behavioral:** Will customers change their current workflow? How do they currently do this without the product?
- **Adoption:** Who will champion this internally at the customer organization? Who will resist?
- **Organizational:** Does the customer organization have the capacity and authority to change this process?
- **Market:** Are there alternatives customers will choose instead? How strong is the status quo pull?
- **Value:** Does the customer agree the problem is worth solving? Will they pay or advocate for access?
- **Technical:** Can the product deliver the capability at the required performance and reliability?

A list of unknowns that is all technical has not been done honestly.

##### Step 6: Classify Assumptions by Impact and Uncertainty

**The PM classifies; the skill challenges** (mirrors prompts/01 (uploaded reference: `07-prompts.md`, section `ps-tiny-acts-discovery / Companion / 01-rank-assumption-backlog.md`)). First help the PM state each item as an assumption: the thing that must be true for it to matter. If their version is vague or hides two assumptions, make them tighten it; react to theirs rather than writing it. Then for each assumption ask two questions: how much would it change product or business decisions if it were true (impact), and how much real evidence they hold (uncertainty). Push hardest on the evidence: what is it, and how confident are they in it? Where a placement looks off given what they just said, point at it and make them reconsider. Do not move it yourself, and do not invent evidence or confidence.

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

##### Step 7: Identify the Top 3 Priority Assumptions

From the PM's classification, the PM picks the top 3 (those rated Urgent or High, or the top 3 by priority if fewer than 3 are Urgent/High). These become the inputs to Step 8.

If the PM's top 3 are all in the same category (all technical, all behavioral), flag this. A set of top-priority assumptions that clusters in one area usually means the team has not been honest about breadth.

##### Step 8: Write Hypotheses for the Top 3 Assumptions

For each top-priority assumption, write an If/Then hypothesis:

**Format:** "If [we do or provide X], then [we expect Y outcome] because [reasoning]."

Or for outcome-focused framing: "By achieving [specific outcome or metric], we can [achieve the goal]."

A strong hypothesis names a specific observable result, not a vague positive feeling. "Then customers will complete onboarding in under 10 minutes" is testable. "Then customers will like the experience" is not.

##### Step 9: Design Tiny Acts for Each Hypothesis

For each hypothesis, find the fastest path to a real signal (mirrors prompts/02 (uploaded reference: `07-prompts.md`, section `ps-tiny-acts-discovery / Companion / 02-design-tiny-act.md`)):

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

##### Step 10: Note the Process Boundary

After completing the artifact, be explicit with the PM: the next step is running the tiny acts in the field. This means contacting real users, running the test, collecting the signal, and returning with findings.

Offer to help document results when the PM returns. The typical return conversation looks like: "We ran the walkthrough. Here is what we saw." The agent can then help the PM update the assumption classification, identify which hypotheses were supported or disproved, and decide what the next round of tiny acts should address.

##### Step 11: Offer Next Steps

At the end of the artifact, offer three options:

1. Run the tiny acts and return with findings - the agent will help document results and update the assumption map
2. If one assumption from Step 6 stands out as uniquely high-stakes, convert it into a formal Lo-fi Experimentation plan using ps-lofi-experimentation
3. Feed confirmed results into the Outcome-Based Roadmap (Template 17): the "Outputs to Develop," "Output Concepts to Validate," and "Assumptions to Validate / Research" sections draw directly from Tiny Acts findings

#### Examples

See examples/sample.md (uploaded reference: `05-create.md`, section `ps-tiny-acts-discovery / Examples`).

The example set includes:

- a strong Tiny Acts exercise with a coherent product scenario, honest knowns, honest unknowns, a clear top-3, measurable hypotheses, and genuinely small acts
- a weak version with the same scenario done poorly: assumptions masquerading as facts, all ratings inflated to high, vague acts with no metrics and no owners
- a drift-bug example where the PM asks the agent to run the tiny acts for them, and the agent correctly explains the process skill boundary

#### Common Pitfalls

##### Pitfall 1: Confusing Assumptions with Facts

**Symptom:** The "what we know" list is full of items the team believes but has not verified: "We know customers want faster reporting." "We know the current tool is insufficient." "We know this will drive adoption."

**Consequence:** The "don't know" list is artificially short. The team skips assumption classification because they think they already know more than they do. The tiny acts target the wrong questions.

**Fix:** For every item on the "what we know" list, ask: "What was the source? When was this verified?" If the PM cannot name a source, the item belongs on the "don't know" list.

##### Pitfall 2: Listing Only Technical Unknowns

**Symptom:** The "what we don't know" list is entirely about system performance, API reliability, data quality, and integration complexity. No behavioral, adoption, organizational, or market unknowns appear.

**Consequence:** The team builds something technically sound that fails in the field because the behavioral and organizational assumptions were never tested.

**Fix:** Before finalizing the list, explicitly prompt: What are the adoption unknowns? What are the organizational unknowns? What are the customer-behavior unknowns? What could cause the product to be technically correct but commercially unsuccessful?

##### Pitfall 3: Treating All Assumptions as Equal Priority

**Symptom:** Every item on the "don't know" list gets rated High Impact and High Uncertainty. Everything is Urgent.

**Consequence:** Prioritization is impossible. The team cannot distinguish which assumption to test first. All energy is diffuse.

**Fix:** Push the team to differentiate. If more than half the list is Urgent, the ratings have not done the work. Ask: "If you could only test one of these this week, which would it be and why?" The answer reveals the true top priority.

##### Pitfall 4: Writing Acts That Are Too Large

**Symptom:** The tiny acts are six-week user studies, full A/B tests with statistical significance requirements, or multi-phase research programs.

**Consequence:** Nothing gets done. The cost of learning is so high that the team skips the acts entirely and proceeds on untested assumptions.

**Fix:** Each act should be completable in days. Five user walkthroughs, not fifty. A targeted data pull, not a full analytics overhaul. A quick survey of 20 current users, not a market research study. If the act takes more than a week to complete, break it into a smaller first step.

##### Pitfall 5: Skipping the Metric Column

**Symptom:** The acts are specific, but the Measure / Metric column is empty or filled with vague language: "see if they like it," "observe the reaction," "check if it works."

**Consequence:** The team runs the act but cannot interpret the results. Was the test a success? A failure? There is no answer.

**Fix:** Every act needs a specific signal: a threshold (70% task completion), a count (more than 15 of 20 users identify this as a top pain), or an observable event (the user completes the checkout flow without asking for help). If the PM cannot define what "pass" looks like, the hypothesis is not ready to test.

##### Pitfall 6: Leaving "Assigned" Blank

**Symptom:** The Assigned column is empty, or it reads "TBD," "the team," or "everyone."

**Consequence:** No one runs the act. Unowned work does not get done.

**Fix:** Every act must have a named individual. If the PM cannot name one, that is a signal the team does not have the capacity to run this act. Either assign it or drop it from the list.

##### Pitfall 7: Conflating Tiny Acts with Lo-fi Experimentation

**Symptom:** The PM uses Tiny Acts to design one formal, rigorous experiment for a single high-stakes assumption, complete with control conditions, statistical significance, and a multi-week time window.

**Consequence:** The tool is being misused. A single formal experiment is not Tiny Acts. The PM is spending Lo-fi Experimentation effort without the rigor that makes Lo-fi defensible.

**Fix:** Tiny Acts is for many small tests running in parallel or in rapid sequence. If the PM needs a single rigorous test for a make-or-break assumption, redirect them to ps-lofi-experimentation (Template 14).

##### Pitfall 8: Running It Once and Filing It Away

**Symptom:** The team completes the exercise at project kickoff and never revisits it. The assumption classification becomes stale. Results from the acts are never documented.

**Consequence:** The practice never becomes continuous. The team loses the habit. Later-phase assumptions go untested because the tool is associated with a one-time activity.

**Fix:** At the end of each Tiny Acts session, schedule the next one explicitly. Tiny Acts is not a milestone - it is a rhythm. The cadence can be biweekly, sprint-based, or triggered by a key decision. What matters is that it recurs.

##### Pitfall 9: AI Scores the Backlog

**Symptom:** The PM pastes the "don't know" list and asks the agent to rate impact and uncertainty. The 2x2 comes back filled in, and the team adopts it.

**Consequence:** Confidence is claimed without the PM's evidence. The ranking is the model's guess, and no one can explain why an assumption sits where it does.

**Fix:** The PM places every assumption. The skill asks what the evidence is, pushes on it, and points at placements that look off.

##### Pitfall 10: The Backlog Replaces the Discovery

**Symptom:** A tidy, well-ranked backlog, acts defined with owners and metrics, and three weeks later none have run. The backlog gets re-groomed instead.

**Consequence:** Planning becomes the activity. It looks strategic and learns nothing.

**Fix:** Commit to one act this week, with a named owner, before polishing the rest. Re-score only when new evidence arrives.

#### References

##### Skill Files

- template.md (uploaded reference: `05-create.md`, section `ps-tiny-acts-discovery / Template`) - working scaffold for the five-step exercise
- prompts/ (uploaded reference: `07-prompts.md`, section `ps-tiny-acts-discovery / Companion / README.md`) - copy-paste prompts for chat-based AI tools (2: build and rank the backlog, design a tiny act)
- examples/sample.md (uploaded reference: `05-create.md`, section `ps-tiny-acts-discovery / Examples`) - strong, weak, and drift-bug examples

##### Related Skills

- **Upstream:** ps-solution-hypothesis (uploaded reference: `04-discover-define.md`, section `ps-solution-hypothesis / Instructions`) defines what is being tested; ps-framing-the-problem (uploaded reference: `03-discover-investigate.md`, section `ps-framing-the-problem / Instructions`) provides customer and problem context; ps-outcome-tree (uploaded reference: `02-context.md`, section `ps-outcome-tree / Instructions`) clarifies success criteria
- **Downstream:** Outcome-Based Roadmap (Template 17): "Outputs to Develop," "Output Concepts to Validate," "Assumptions to Validate," and "Assumptions to Research" draw from Tiny Acts findings
- **Related:** ps-lofi-experimentation (uploaded reference: `04-discover-define.md`, section `ps-lofi-experimentation / Instructions`) (Template 14): for a single high-stakes assumption that requires formal, rigorous testing; ps-risk-assessment (Template 15): high-uncertainty assumptions that cannot be tested quickly may surface as risks

##### Project Docs

- [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)
- [informative-documents/framework-glossary.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/framework-glossary.md)
- [informative-documents/skill-dependency-map.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/skill-dependency-map.md)

##### Source Material

- assets/ps_tiny_acts_discovery_playbook_pages.pdf (source material, not included in this upload kit)
- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 81-86: Template 18 of 24 there, with the AI overview on slide 83 and prompts on slides 84, 85. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).
- [Baseline Playbook version](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml). Full source PDF supplied separately.
- Productside Playbook companion document (supplied separately)

### ps-tiny-acts-discovery / Template

### Tiny Acts of Discovery

**Product:** [name the product]
**Customer:** [name the role that uses or buys this product day-to-day - not the PM, not the team]
**Date:** [date of session]
**Participants:** [names and roles]

---

#### Step 1: What Do We Know?

List what the team currently knows about the product and its users. These are validated facts, observed behaviors, completed research, and confirmed assumptions. For each item, note the source.

| What We Know | Source |
|---|---|
| [Specific, verified fact about customer behavior or product] | [interview date, data pull, completed test, field observation] |
| [Specific, verified fact about customer behavior or product] | [interview date, data pull, completed test, field observation] |
| [Specific, verified fact about customer behavior or product] | [interview date, data pull, completed test, field observation] |
| [Add more rows as needed] | |

**Quality check:** Can you name a source for each item? If not, move it to Step 2.

---

#### Step 2: What Do We Not Know?

List the gaps: unknown customer behaviors, unvalidated assumptions, open questions, missing data. Cover a range of categories - behavioral, adoption, organizational, market, value, and technical.

- [Unknown or unvalidated assumption - behavioral]
- [Unknown or unvalidated assumption - adoption or organizational]
- [Unknown or unvalidated assumption - market or value]
- [Unknown or unvalidated assumption - technical]
- [Add more as needed]

**Quality check:** Does this list include unknowns beyond technical ones? Are there behavioral, adoption, and organizational questions here?

---

#### Step 3: Prioritize Your Assumptions

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

#### Step 4: Form Your Hypotheses

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

#### Step 5: List Your Tiny Acts of Discovery

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

#### Next Steps

[ ] Run the tiny acts in the field
[ ] Document results and return to update the assumption classification
[ ] Schedule the next Tiny Acts session: [date]

**When you return with findings:** Share what you observed. The agent will help document results, identify which hypotheses were supported or disproved, and decide what the next round of tiny acts should address.

**If one assumption stands out as uniquely high-stakes:** Consider converting it into a formal Lo-fi Experimentation plan (Template 14) using ps-lofi-experimentation.

**When acts are complete:** Feed confirmed results into the Outcome-Based Roadmap (Template 17) - specifically the "Outputs to Develop," "Output Concepts to Validate," "Assumptions to Validate," and "Assumptions to Research" sections.

### ps-tiny-acts-discovery / Examples

### Tiny Acts of Discovery - Sample Examples

Three examples using a field services scenario: a mobile dispatch and job management platform for HVAC technicians and their dispatchers at a commercial facilities management company.

---

#### Example 1: Strong

**Product:** ServiceFlow - mobile job management platform for HVAC technicians
**Customer:** HVAC field technicians (primary) and dispatch coordinators (secondary)
**Date:** March 14
**Participants:** Priya Nair (PM), Marco Santos (UX Research), Deb Okonkwo (Engineering Lead)

---

##### Step 1: What Do We Know?

| What We Know | Source |
|---|---|
| Technicians currently receive job assignments via text message and a shared whiteboard at dispatch | Field observation, 3 sites, Feb 12-14 |
| Average time from job assignment to technician departure is 22 minutes under current system | Dispatch log analysis, 90-day pull, Feb 28 |
| 6 of 8 technicians interviewed said they call dispatch at least twice per job for parts availability information | Empathy interviews, Feb 7-9 |
| Dispatchers use two separate tools (CRM and a paper log) to track technician location and job status | Field observation, Feb 13 |
| Management requires job completion sign-off within 2 hours of finish for billing; 34% of jobs currently miss this window | Billing data pull, Q4 review |

---

##### Step 2: What Do We Not Know?

- Will technicians use a mobile app mid-job or will they default to calling dispatch even when the app is available? (behavioral)
- Do technicians have reliable cellular coverage in the mechanical rooms and basements where most HVAC equipment lives? (technical)
- Will dispatchers trust the app's real-time location data enough to stop calling technicians for status updates? (adoption/behavioral)
- Does the facilities management company have a device procurement policy that controls what phones technicians can use? (organizational)
- Will commercial clients accept digital sign-off instead of a paper signature for billing compliance? (market/compliance)
- How do technicians currently handle parts shortages mid-job and would they use an in-app parts request if it existed? (behavioral)

---

##### Step 3: Prioritize Your Assumptions

| Assumption | Impact (H/M/L) | Uncertainty (H/M/L) | Priority |
|---|---|---|---|
| Technicians will use the app mid-job rather than calling dispatch | H | H | Urgent |
| Commercial clients will accept digital sign-off for billing compliance | H | H | Urgent |
| Dispatchers will trust real-time location data and reduce status calls | M | H | High |
| Cellular coverage is adequate in mechanical rooms and basements | H | M | High |
| Company device policy controls which phones technicians can use | M | M | Medium |
| Technicians would use an in-app parts request mid-job | M | M | Medium |

---

##### Step 4: Form Your Hypotheses

**Hypothesis 1** (for: Technicians will use the app mid-job rather than calling dispatch)

> If we give 5 technicians a working prototype of the job detail screen and ask them to complete a simulated mid-job workflow, then at least 4 of 5 will complete the task without asking for help or reverting to their phone call habit, because the key information they currently call for (parts list, customer contact, job notes) will be visible on a single screen.

**Hypothesis 2** (for: Commercial clients will accept digital sign-off for billing compliance)

> If we show the current sign-off workflow and a proposed digital alternative to 3 facilities managers at existing client sites, then at least 2 of 3 will confirm that a digital signature meets their internal audit and billing requirements, because commercial facilities contracts typically specify signature capture but not medium.

**Hypothesis 3** (for: Dispatchers will trust real-time location data and reduce status calls)

> If we shadow a dispatcher for one full shift while they have access to a live map view of technician locations, then the dispatcher will initiate at least 30% fewer inbound status calls compared to their baseline, because the map resolves the most common reason they call (checking whether a technician has left the previous job site).

---

##### Step 5: List Your Tiny Acts of Discovery

| Hypothesis | Tiny Act of Discovery | Measure / Metric to be Collected | Assigned |
|---|---|---|---|
| Hypothesis 1 | Moderated usability walkthrough with 5 technicians using a clickable Figma prototype of the job detail screen. Present 3 mid-job task scenarios. | Task completion rate without researcher assistance. Target: 4 of 5 complete all 3 tasks without asking for help or reaching for their phone. | Marco Santos |
| Hypothesis 2 | 30-minute structured conversation with 3 facilities managers at current client sites. Present current paper process and proposed digital flow side by side. Ask directly about their audit and compliance requirements. | Number of managers who confirm digital capture meets their billing and audit standards. Target: 2 of 3 say yes without requiring additional approval steps. | Priya Nair |
| Hypothesis 3 | Shadow one dispatcher for a single full shift (8 hours) while they access a working location map fed by test devices carried by 3 volunteer technicians. Count inbound status calls during the shift and compare to the dispatcher's own estimate of their normal daily call volume. | Count of dispatcher-initiated status calls during the observed shift vs. self-reported baseline. Target: at least 30% reduction observed. | Deb Okonkwo |

**Next Steps:**
[ ] Run the three acts this sprint (week of March 17)
[ ] Return with findings to update the assumption classification
[ ] Next Tiny Acts session: April 1 (after results are in)

---

**Commentary - why this example works:**

The knowns list has real sources attached: field observations with dates, data pulls with time windows, and interview counts. Nothing on the knowns list is an assumption dressed as a fact.

The unknowns list covers four distinct categories: behavioral (will technicians use the app), compliance/market (will clients accept digital sign-off), adoption (will dispatchers trust the data), and technical (cellular coverage). It is not an all-technical list.

The classification produces a meaningful spread: two Urgent, two High, two Medium. The PM does not need to test all six at once. The top 3 are genuinely more critical than the bottom 3.

The hypotheses are specific and observable. Each THEN clause names a threshold or count. Each hypothesis is falsifiable: the test can produce a clear pass or fail signal.

The tiny acts are genuinely tiny: one 5-person usability walkthrough, three 30-minute client conversations, and one 8-hour shadow session. None of these require weeks or a research budget. All three can be completed this sprint.

---

#### Example 2: Weak

**Product:** ServiceFlow - mobile job management platform for HVAC technicians
**Customer:** HVAC field technicians
**Date:** March 14
**Participants:** Priya Nair (PM)

---

##### Step 1: What Do We Know?

- We know technicians are unhappy with the current process
- We know the product will save time
- We know dispatchers want better visibility
- We know customers will adopt the app because it is simpler than what they use now
- We know the market is ready for a mobile-first solution

---

##### Step 2: What Do We Not Know?

- Will the API integrate with the CRM?
- Will the database scale to support 500 concurrent users?
- Will the mobile app perform acceptably on older Android devices?

---

##### Step 3: Prioritize Your Assumptions

| Assumption | Impact (H/M/L) | Uncertainty (H/M/L) | Priority |
|---|---|---|---|
| API will integrate with CRM | H | H | Urgent |
| Database will scale to 500 users | H | H | Urgent |
| App will perform on older Android | H | H | Urgent |

---

##### Step 4: Form Your Hypotheses

**Hypothesis 1:** If we integrate the API, then the CRM will work with the app.
**Hypothesis 2:** If we test at scale, then performance will be fine.
**Hypothesis 3:** If we optimize for Android, then it will work on all devices.

---

##### Step 5: List Your Tiny Acts of Discovery

| Hypothesis | Tiny Act of Discovery | Measure / Metric to be Collected | Assigned |
|---|---|---|---|
| Hypothesis 1 | Full CRM integration build and QA cycle | TBD | Team |
| Hypothesis 2 | Load testing infrastructure setup | TBD | Team |
| Hypothesis 3 | Multi-device QA across 20 device types | TBD | Team |

---

**Commentary - why this example fails:**

The knowns list is almost entirely composed of beliefs and assumptions, not validated facts. "We know technicians are unhappy" - how do you know? "We know customers will adopt the app" - this is the core assumption the product needs to prove, not something to declare as known. None of the five items has a source. If the source cannot be named, the item belongs in Step 2.

The unknowns list covers only technical questions. There are no behavioral unknowns (will technicians actually use the app in the field), no adoption unknowns (will dispatchers change their habits), no organizational unknowns (device policy, sign-off compliance), and no market unknowns. This team will ship a technically sound product that fails in the field because they never tested the behavioral and organizational assumptions.

The classification inflates every assumption to Urgent. When everything is Urgent, nothing is prioritized. The team cannot decide what to test first.

The hypotheses are not testable. "The CRM will work with the app" is not a THEN clause with an observable threshold. It is a statement of hoped-for outcome.

The acts are not tiny. A "full CRM integration build and QA cycle" is not a tiny act - it is a build milestone. None of these acts can be completed in days. None of them have specific metrics. All three are assigned to "Team," which means no one owns them.

---

#### Example 3: Drift Bug - The PM Asks the Agent to Run the Acts

**Scenario:** A PM has completed Steps 1 through 4 and has identified three tiny acts. They now ask the agent to run the acts on their behalf.

---

**PM:** Okay, I've got my three hypotheses. Can you just generate me 20 survey questions I can send to technicians, run a simulated usability walkthrough using your best guess of how a technician would respond, and pull some industry data showing typical dispatcher call volumes so I can use that as my baseline?

---

**Agent response:**

There are parts of this I can help with and parts that require you and your team to engage with real technicians and dispatchers directly.

**What I can help you do:**

For the survey, I can draft a set of specific, well-formed questions designed to test Hypothesis 2 (technician mid-job behavior). I can make sure the questions are behaviorally grounded, avoid leading language, and are sequenced in a way that surfaces honest responses rather than socially desirable ones. You would then send those to real technicians and share the results with me.

For the usability walkthrough, I can help you write a structured test script - the task prompts, the observation guide, and the note-taking format. Marco Santos would run the actual sessions with the 5 real technicians. I can help interpret what you observed after the sessions.

For the dispatcher baseline, I can help you design a simple self-reported baseline method: a structured question to ask the dispatcher before the shadow session that gives you their own estimate of normal daily call volume. That is more useful than industry benchmarks anyway because it is specific to this dispatcher's workflow.

**What I cannot do:**

I cannot generate synthetic technician responses as a substitute for real ones. If I simulate how a technician "would probably respond" to the usability prototype, I am inventing data. Simulated responses would tell you what I predict, not what your actual customers do - and the gap between those two things is exactly what the tiny act is designed to measure.

I cannot pull proprietary dispatcher call volume data from your organization. I can find published industry benchmarks if they exist, but using industry averages as your baseline would undermine the measurement: your dispatchers may operate very differently from the industry average, and the whole point is to measure change in their specific behavior.

**The process skill boundary:**

Tiny Acts of Discovery is a field research practice. The agent's role is to help you design the acts, sharpen the metrics, write the test scripts, and document what you learn when you return with real findings. The acts themselves require real people, real behavior, and real data.

Let's start with the survey design. What is the most important question you need those 20 technicians to answer honestly?

---

**Commentary - why this example matters:**

The PM's request is understandable. Generating survey questions and synthetic responses feels faster. But synthetic research is not research - it is a hallucination of what the agent thinks users believe. The tiny act exists precisely because the agent's prediction and the user's actual behavior often diverge.

The agent's response does three things correctly:
- It is specific about what it can help with (draft, design, structure)
- It is clear about what it cannot do and why (synthetic data, proprietary org data)
- It redirects immediately to a concrete next step rather than leaving the PM stranded

A process skill boundary is not a refusal. It is a handoff: the agent prepares, the PM runs, the agent helps interpret. Drift occurs when the agent tries to skip the middle phase.

## ps-output-prioritization | Output Prioritization

Playbook number: 19. Phase: Create.

### ps-output-prioritization / Instructions

#### Purpose

Create a **Productside-style Output Prioritization artifact** from a collaborative team review of candidate product outputs.

This skill helps a Product Manager and their cross-functional team evaluate which features and capabilities to build first, based on relative customer value and relative business cost. The result is a four-quadrant placement for every candidate output, a clear ordering for development sequencing, and a transparent record of the tradeoffs the team made.

The point is not to build everything eventually. The point is to help the team make a defensible, customer-grounded decision about what to address first, what to plan carefully, what to deprioritize, and what to cut.

The skill works in two moments. **Before the session**, it prepares the PM to facilitate: the center-point anchor, the moves that keep value and cost honest, and rehearsal for the hard personalities. **After the session**, it records the room's placements in the four-quadrant artifact and checks them. It does not rank the outputs itself.

This is a team exercise. It is not a solo PM exercise. Customer value requires discovery data or validated insight. Business cost requires input from engineering, a project manager, or a technical lead. A solo prioritization session produces outputs ranked by the PM's assumptions, not by evidence.

#### Key Concepts

##### Outputs Are Not Outcomes

This distinction is load-bearing. An **output** is a feature, capability, or deliverable the team can build: a real-time alert dashboard, an offline sync mode, a bulk import tool. An **outcome** is what a customer achieves when the product works: field technicians catch scheduling conflicts before they become incidents, operations managers spend less time on manual reconciliation.

Confusing outputs for outcomes is the most common failure mode in prioritization. An output that cannot be connected to a customer outcome has no defensible basis for prioritization. If the team cannot name the outcome an output supports, that output should be challenged before it is placed on the grid.

##### The Two Axes

**Value (Y-axis): Customer value.**
How much does this output drive progress toward a product outcome? Does it relieve a significant pain or create a meaningful gain for the customer? Value is defined entirely from the customer's perspective. Business benefits such as upsell opportunity, marketing positioning, or internal cost reduction are not customer value. They may be relevant business considerations, but they cannot substitute for the customer's perspective on the Y-axis.

**Cost (X-axis): Business cost and risk.**
How much does this output cost the business to develop? Cost includes development effort, integration complexity, infrastructure requirements, dependency management, and delivery risk. Engineering and project management input is required for a credible cost estimate. PM intuition is not sufficient.

##### Why Center-Point Anchoring Works

The most common problem in output prioritization is inflation: every feature is called "high value" by someone on the team. The center-point anchor breaks this dynamic.

The team agrees on one output that is genuinely medium cost and medium value - neither the most expensive nor the most impactful candidate on the list. That output anchors the center of the grid. All other outputs are plotted relative to this anchor, not on an absolute scale.

This prevents the "everything is critical" failure mode. It forces relative comparison: is this output more or less valuable than the anchor? More or less costly? Relative comparison is harder to inflate than absolute scoring.

##### Prioritization Is a Conversation About Trade-offs

Prioritization is a conversation about trade-offs, not a calculation. The plotting belongs to the room: real cost comes from the tech team, real value from customer evidence, and the call on what to build first from the PM and their stakeholders together. A ranked list handed down from a tool has no cost data behind it and no buy-in.

The room will want to crowd everything into high-value, low-cost. Moves that break that up:

- **Force comparisons against the anchor.** "More or less valuable than the center point? More or less costly?"
- **Ask for the outcome and the evidence behind every value claim.** Value means customer value tied to a product outcome, not internal excitement.
- **Make tech scope cost out loud.** Cost means the real build cost, not a wave of the hand.

Rehearse the hard moments before the session: the stakeholder who inflates their pet feature, the "everything is a priority" reflex, and cost getting waved away.

##### The Four Quadrants

The canonical labels the quadrants I through IV. The layout differs from standard mathematical quadrant notation:

- **Quadrant I (Low Cost, High Value - upper right):** Start here. Maximum return for minimum investment. These outputs should be at the top of the development sequence.
- **Quadrant II (High Cost, High Value - upper left):** Plan carefully. High return but high investment required. Validate the value assumptions before committing. Uncertainty in cost estimates warrants lo-fi experimentation before full build.
- **Quadrant III (Low Cost, Low Value - lower right):** Deprioritize. These outputs are cheap to build but do not move the needle for customers. "Easy" is not a reason to build.
- **Quadrant IV (High Cost, Low Value - lower left):** Avoid or cut. Poor return on investment. These outputs must be cut or deferred. Stakeholder pressure to keep Quadrant IV items is one of the most common prioritization failures.

##### Cross-Functional Input Is Required

Customer value: requires data from discovery work, empathy interviews, or validated product outcomes. The Outcome Tree (ps-outcome-tree) is the best source for linking outputs to product outcomes.

Business cost: requires input from engineering, a project manager, or a technical lead. Do not estimate cost without a technical voice in the room.

##### How to Connect Outputs to Outcomes

The Outcome Tree shows what customers need to achieve (product outcomes) as a result of the problem the product solves. Each output the team evaluates should be traceable to at least one product outcome. If an output cannot be connected to a product outcome, it is either solving an internal business problem (not a customer problem) or the outcome tree is incomplete.

Quadrant I outputs should be linked to the highest-priority product outcomes before they are committed to the roadmap.

##### Relationship to Tiny Acts of Discovery

Tiny Acts of Discovery is a technique for generating solution ideas before outputs are evaluated. Output Prioritization assumes that the brainstorm phase is complete: the team has already identified all candidate outputs (using Story Mapping, Tiny Acts, or equivalent). The prioritization exercise evaluates that list - it does not generate it.

If the list of candidate outputs is still thin or unclear, run Tiny Acts of Discovery before beginning this exercise.

##### How AI Supports This Play

The Playbook casts AI as a **facilitation coach**. It rehearses the session with the PM: how to set up the room, how to anchor every output against a single center-point output so the ranking stays relative, and how to keep the group honest when every idea drifts into high-value, low-cost territory. What the PM gets is a sharper facilitator, not a ranked list.

- **Use it when:** the PM has a list of outputs and needs to run a session where stakeholders prioritize them by relative value and cost.
- **Avoid it when:** the request is for AI to score and rank the features. It has no real cost data and cannot create team buy-in. Offer to prepare the session instead.
- **Return:** a session plan anchored on a center-point output, moves to keep value and cost honest, and rehearsal for the stakeholder who inflates everything. After the session: the room's placements, recorded and checked.

##### Working With AI

The Productside Playbook sets one rule for every AI-assisted Play: **the Product Manager does the thinking, and AI pressure-tests it.** In this skill, you are the AI. Hold yourself to these rules:

1. **Pressure-test before you produce.** When the user brings a draft, critique it against the Play's formats and criteria first. Point at the specific words that fail and ask the user to fix them. Offer rewrites only after the critique, as options to accept, adapt, or reject.
2. **Never stand in for the customer.** Do not present jobs, quotes, needs, or pains you generated as research, and do not answer as the persona as if your answers were evidence. Anything you draft about customers is a hypothesis, labeled as one, to validate with real people. Role-play is allowed only as rehearsal where the Play calls for it, labeled as practice, and nothing from it goes into findings.
3. **Never stand in for the team's judgment.** Do not put unsourced figures into the artifact, and do not make calls the team should own. A number without a source is a blank to fill, so mark it that way.
4. **Work the five habits.** *Context:* ask for the persona, market, outcome, and constraints when they are missing. *Guide:* offer competing views and welcome pushback. *Enforce:* work inside the Play's template, not around it. *Outcome:* tie the work to the decision it supports. *Iterate:* go step by step rather than one-shot.
5. **Keep best guess honest.** Best guess mode is allowed. When you use it, label every inferred detail inline and end with **Assumptions to Validate**. A best guess is a starting point to test, never a finding.

For people working in a chat tool without this skill, the Play's copy-paste prompts are in prompts/ (uploaded reference: `07-prompts.md`, section `ps-output-prioritization / Companion / README.md`).

##### Guided Mode

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

#### Application

Use template.md (uploaded reference: `05-create.md`, section `ps-output-prioritization / Template`) for the scaffold.

See the source play pages in assets/ps_output_prioritization_playbook_pages.pdf (source material, not included in this upload kit).

##### Required Output Convention

Default to a **clean, paste-ready artifact**.

That means:

- a named list of all candidate outputs (brainstorm phase)
- one clearly named center point output with team rationale
- a classification table with Value (H/M/L), Cost (H/M/L), and Quadrant for every output
- a Quadrant Summary listing outputs by quadrant with action guidance
- Quadrant I outputs linked to product outcomes
- explanation belongs below the artifact, not inside the classification fields

##### Step 1: Confirm Who the Customer Is

Before evaluating any output for value, confirm who the customer is - the person who uses or buys the product, not the PM, not the engineering team, and not an internal stakeholder.

This is the tech-role bias guard. LLMs and product teams both default to developer, architect, or internal-operations perspectives when evaluating value. If the product serves field technicians, operations managers, clinical coordinators, or other non-technical roles, the value dimension must be assessed from that person's standpoint.

Ask the user to name the customer role. If a proto-persona exists (from ps-proto-persona), use it. If an Outcome Tree exists (from ps-outcome-tree), confirm the product outcomes before evaluating outputs against value.

##### Step 2: Gather Available Artifacts

Before drafting, ask whether the user has materials to share:

- Solution hypothesis from ps-solution-hypothesis (defines the solution being decomposed into outputs)
- Product outcomes from ps-outcome-tree (used to evaluate value from the customer's perspective)
- Discovery findings from ps-empathy-interviews or ps-problem-identification (used to calibrate which customer pains are most severe)
- Any Story Mapping or Tiny Acts of Discovery results (used to populate the candidate output list)
- Engineering capacity or sprint planning data (used to calibrate cost)

The more context available, the more targeted the classification. If no artifacts are available, note that the output is based on PM assumptions and should be reviewed with the team before committing.

##### Step 3: Identify All Candidate Outputs

Work with the user to list all outputs that could be developed as part of the solution. This is a brainstorm - do not filter or evaluate yet.

For each output, capture:

- A short name (3-8 words) that identifies the feature or capability specifically
- Not a vague category like "reporting" or "integrations" - name the specific thing: "real-time alert dashboard" or "ERP connector for SAP"

Aim for completeness. A prioritization exercise with only three candidates is not a prioritization exercise - it is a list. A good brainstorm produces six to twelve candidates before the evaluation begins.

##### Step 4: Prepare to Facilitate the Session (Default)

Unless the PM is returning with the room's placements, prepare them to lead the session (mirrors prompts/01 (uploaded reference: `07-prompts.md`, section `ps-output-prioritization / Companion / 01-rehearse-prioritization-session.md`)). Do not rank, plot, or score the outputs, and do not pick the top items.

1. **Pressure-test the PM's center-point pick** (Step 5). Is it genuinely middle of the road on both value and cost? If not, help them reason toward a better anchor. They choose it.
2. **Walk the session:** place the anchor first, then have the group plot every other output relative to it.
3. **Coach holding value and cost honest:** value is customer value tied to a product outcome; cost is real build cost scoped with tech.
4. **Give specific moves** for when the room crowds everything into high-value, low-cost (see [Prioritization Is a Conversation About Trade-offs](#prioritization-is-a-conversation-about-trade-offs)).
5. **Rehearse the hard moments.** Ask the PM what they would say to the stakeholder who inflates a pet feature, to "everything is a priority," and when cost gets waved away. Then sharpen it.

Steps 5-12 describe the artifact the room produces. When the PM returns with the room's placements, record them and check them against those steps. When the PM asks you to place outputs before any session, don't place them yet: explain that value and cost come from the room (customer evidence and tech scoping), and offer to prepare the session and pressure-test a center-point anchor. If the PM then still wants a draft, or chooses best guess mode, label the placements **AI draft placement: for the room to challenge; cost not scoped by tech**, and keep the session as the place the decision is made.

##### Step 5: Find the Center Point Output

The center point output is the anchor for the entire exercise. The team - not the PM alone - must agree on it.

Criteria for the center point:

- Medium cost: not the cheapest thing to build, not the most expensive
- Medium value: not the most impactful thing for the customer, not the least
- Understandable to all participants: the team can reason about other outputs relative to it

Name the center point output explicitly. Write one or two sentences explaining why the team agreed it is medium/medium. This anchors the calibration for every other placement.

##### Step 6: Classify Value for Each Output

Record how the room classified each candidate output except the center point, relative to the center point, as High, Medium, or Low.

Value is customer value. Ask: does this output drive more or less progress toward a product outcome than the center point output? Does it relieve a more or less severe customer pain?

For each classification, write a 1-2 sentence rationale that names the customer benefit or the product outcome it supports. If the rationale cannot name a customer benefit or outcome, the classification is based on assumptions - flag it.

##### Step 7: Classify Cost for Each Output

Record how the room classified cost for each candidate output except the center point, relative to the center point, as High, Medium, or Low.

Cost is business cost and risk. Ask: is this output more or less expensive to build and ship than the center point output? Does it carry more or less integration risk?

For each classification, write a 1-2 sentence rationale based on what engineering or the project manager said. If no technical input is available, note the assumption and recommend a follow-up sizing conversation.

##### Step 8: Place Each Output in Its Quadrant

Combine Value and Cost to assign each output to a quadrant:

- High Value + Low Cost = Quadrant I
- High Value + High Cost = Quadrant II
- Low Value + Low Cost = Quadrant III
- Low Value + High Cost = Quadrant IV
- Medium entries fall on the boundary - use judgment and team discussion to place them

**Check for inflation.** If most outputs landed in Quadrant I, the room rated each output on its own instead of against the anchor. Say so, and suggest the PM revisit the placements against the center point.

Outputs classified Medium/Medium belong near the center point. Treat them as Quadrant II or III candidates depending on which direction the team leans after discussion.

##### Step 9: Identify Quadrant I Outputs

List all Quadrant I outputs. These are the primary candidates for the first development cycle.

For each Quadrant I output, name the product outcome it supports. If it cannot be linked to a product outcome, pause and ask whether the classification is correct.

##### Step 10: Address Quadrant II Outputs

Quadrant II outputs are high value but high cost. Do not treat them as "do next" without additional validation.

For each Quadrant II output:

- Identify what assumptions about value and cost need to be validated before committing to the build
- Consider whether a lo-fi experiment (ps-lofi-experimentation) could reduce uncertainty before committing to full development
- If the team cannot validate the value assumptions, move the output to "Output Concepts to Validate" in the roadmap rather than "Outputs to Develop"

##### Step 11: Deprioritize Quadrant III and Cut Quadrant IV

Quadrant III outputs (Low Cost, Low Value): deprioritize. Do not build them in the current cycle, even if they are cheap. "Easy to build" is not a reason to build. Note them as deferred.

Quadrant IV outputs (High Cost, Low Value): cut or avoid. If stakeholders press to keep Quadrant IV items, document the tradeoff explicitly: what Quadrant I or II investment is deferred to make room for this.

If the team cannot bring themselves to cut any Quadrant IV items, the prioritization exercise has not done its job.

##### Step 12: Link High-Priority Outputs to Product Outcomes

For each Quadrant I output and each Quadrant II output the team decides to pursue, document the product outcome it supports. Use outcome language: what does the customer achieve when this output is available?

If the Outcome Tree has already been completed, reference the specific outcome by name. If not, write the outcome in outcome format: [direction] [metric] [context/circumstance].

##### Step 13: Offer Next Steps

After delivering the artifact, offer three options:

1. Feed Quadrant I outputs into the Outcome-Based Roadmap (Template 17) as "Outputs to Develop"
2. Place Quadrant II outputs in "Output Concepts to Validate" and run ps-lofi-experimentation on the highest-uncertainty ones
3. Share the classification with stakeholders to surface any Quadrant IV items that carry political weight and document the tradeoff decision explicitly

#### Examples

See examples/sample.md (uploaded reference: `05-create.md`, section `ps-output-prioritization / Examples`).

The example set includes:

- a strong classification with genuine spread across quadrants, Quadrant I outputs linked to product outcomes, and Quadrant IV outputs actually cut
- a weak version where all outputs are rated high value, no center point is established, and classifications are made without engineering input or customer data
- a drift-bug example where value is defined as business revenue impact rather than customer outcome impact, producing a ranking that serves internal priorities rather than customer needs

#### Common Pitfalls

##### Pitfall 1: Defining Value from the Business Perspective

**Symptom:** Value classifications reference revenue potential, upsell opportunity, investor appeal, or internal cost savings rather than customer outcome impact.

**Consequence:** Outputs that are most beneficial to the business rank higher than outputs that most relieve customer pain or drive customer progress. The product delivers for the business but underserves the customer - and adoption suffers.

**Fix:** Before classifying any output, re-read the product outcomes from the Outcome Tree. Each value classification must name what the customer achieves. If the rationale names only what the business gains, rewrite it from the customer's perspective.

##### Pitfall 2: Skipping the Center Point Anchor

**Symptom:** The team classifies each output as High, Medium, or Low on absolute scales without agreeing on a shared reference point.

**Consequence:** "High value" means different things to different people on the team. Everything trends toward High Value because no one wants to downgrade their preferred feature. The grid fills up in the upper half and prioritization is impossible.

**Fix:** Name the center point output first. Get team agreement before any other classification begins. All subsequent placements are relative to that anchor.

##### Pitfall 3: Running This Without Engineering Input on Cost

**Symptom:** The PM classifies all costs alone, using judgment about what "seems" expensive.

**Consequence:** Cost estimates are wrong. Cheap-looking outputs turn out to be expensive due to integration complexity or technical debt. Expensive-looking outputs may be straightforward. The grid is misleading and the roadmap it generates is unworkable.

**Fix:** Do not finalize cost classifications without a technical voice. At minimum, run a rough sizing conversation with an engineering lead or project manager before locking the grid.

##### Pitfall 4: Confusing Outputs with Outcomes

**Symptom:** The candidate list contains items like "increased retention," "better user experience," or "faster time to value." These are outcomes, not outputs.

**Consequence:** The team is not actually prioritizing what to build - they are prioritizing goals. The grid cannot function because outcomes cannot be placed on a development cost axis.

**Fix:** Every item on the candidate list must be a concrete, buildable thing: a specific feature, integration, interface, or capability. If the team is listing outcomes, redirect to the Outcome Tree (ps-outcome-tree) and then ask: what outputs could be built to drive that outcome?

##### Pitfall 5: Treating Quadrant II as "Do Next" Without Validation

**Symptom:** Quadrant II outputs (High Value, High Cost) are moved directly into the sprint plan alongside Quadrant I outputs, without additional investigation.

**Consequence:** The team commits significant capacity to high-cost builds whose value assumptions have not been validated. When the output ships and adoption is weak, the team discovers the value was overestimated - too late.

**Fix:** For every Quadrant II output, name the key assumptions about value that need to be validated before committing to the full build. Consider lo-fi experimentation (ps-lofi-experimentation) for high-uncertainty Quadrant II items before the development commitment is made.

##### Pitfall 6: Never Cutting Quadrant IV Outputs

**Symptom:** The team acknowledges that certain outputs are High Cost and Low Value but keeps them on the list because a stakeholder "really wants it" or because the feature was promised.

**Consequence:** Capacity is drained by outputs that deliver poor customer value. Quadrant I and II investments are deferred to accommodate Quadrant IV items.

**Fix:** Document the Quadrant IV designation explicitly and surface the tradeoff to the stakeholder. "We can build this, but it will displace [specific Quadrant I output] that [customer outcome]. Is that the right call?" Force the explicit decision rather than letting Quadrant IV items survive by default.

##### Pitfall 7: Treating Quadrant Positions as Permanent

**Symptom:** The team runs this exercise once and treats the quadrant placements as fixed for the life of the product.

**Consequence:** Cost estimates that were based on incomplete technical knowledge remain unchanged even after the team learns the true scope. Value estimates that were based on assumptions remain unchanged even after discovery reveals the customer does not care about that output.

**Fix:** Treat the grid as a living artifact. Revisit it when cost estimates change significantly (after technical investigation), when discovery reveals new information about customer value, or when the solution hypothesis changes.

##### Pitfall 8: Using Internal Metrics as Value

**Symptom:** Value classifications cite internal business metrics: "this output will reduce support tickets by 20%," "this output will accelerate our sales cycle," "this output will improve the demo."

**Consequence:** The product gets built to serve internal teams rather than the customer. Support cost reduction is a valid business goal, but it is not the same as customer value. A feature that reduces support tickets may or may not reduce customer pain.

**Fix:** For each value classification, ask: how does this output change what the customer can achieve? If the answer is only about internal operations, the classification is measuring the wrong thing. A support ticket reduction is only customer value if it means the customer gets unblocked faster - and that customer impact should be the stated rationale.

##### Pitfall 9: AI Does the Ranking

**Symptom:** The PM pastes the feature list and asks which to build first. The agent sorts it into quadrants, and its top three become the plan.

**Consequence:** There's no real cost data and no buy-in behind the ranking. The team never weighs in, and the PM can't defend the ranking when a stakeholder pushes back.

**Fix:** Prepare the PM to facilitate (Step 4). The room plots relative to the anchor, tech scopes cost, and the PM and stakeholders decide. The skill records and checks the result.

##### Pitfall 10: Everything Wins

**Symptom:** Each output is rated on its own merits, and almost all of them land high-value. Cost is waved away rather than scoped. Nothing gets cut.

**Consequence:** The four-quadrant grid becomes one crowded quadrant, and the prioritization decides nothing.

**Fix:** Anchor every placement against the center point. Ask for the outcome and evidence behind each value claim, and make tech scope cost out loud.

#### References

##### Skill Files

- template.md (uploaded reference: `05-create.md`, section `ps-output-prioritization / Template`) - four-quadrant scaffold with quality checks
- prompts/ (uploaded reference: `07-prompts.md`, section `ps-output-prioritization / Companion / README.md`) - copy-paste prompt for chat-based AI tools (1: rehearse your prioritization session)
- examples/sample.md (uploaded reference: `05-create.md`, section `ps-output-prioritization / Examples`) - strong, weak, and drift-bug examples

##### Related Skills

- **Upstream:** ps-outcome-tree (uploaded reference: `02-context.md`, section `ps-outcome-tree / Instructions`) provides product outcomes used to evaluate output value; ps-solution-hypothesis (uploaded reference: `04-discover-define.md`, section `ps-solution-hypothesis / Instructions`) defines the solution being decomposed into candidate outputs
- **Upstream (optional):** ps-tiny-acts-discovery populates the candidate output list; ps-empathy-interviews (uploaded reference: `03-discover-investigate.md`, section `ps-empathy-interviews / Instructions`) and ps-problem-identification (uploaded reference: `03-discover-investigate.md`, section `ps-problem-identification / Instructions`) calibrate which customer pains are most severe
- **Downstream:** Outcome-Based Roadmap (Template 17) - Quadrant I outputs feed "Outputs to Develop"; Quadrant II candidates may feed "Output Concepts to Validate"
- **Related:** ps-lofi-experimentation (uploaded reference: `04-discover-define.md`, section `ps-lofi-experimentation / Instructions`) - high-uncertainty Quadrant II outputs are candidates for lo-fi experiments before full build commitment

##### Project Docs

- [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)
- [informative-documents/framework-glossary.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/framework-glossary.md)
- [informative-documents/skill-dependency-map.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/skill-dependency-map.md)

##### Source Material

- assets/ps_output_prioritization_playbook_pages.pdf (source material, not included in this upload kit)
- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 87-91: Template 19 of 24 there, with the AI overview on slide 89 and prompt on slide 90. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).
- [Baseline Playbook version](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml). Full source PDF supplied separately.
- Productside Playbook companion document (supplied separately)

### ps-output-prioritization / Template

### Output Prioritization Template

Use this scaffold to produce a paste-ready four-quadrant output prioritization artifact in Productside format.

Complete all four sections in order. Do not skip the center point step - it is required for valid quadrant placements.

---

#### Section 1: Identify Outputs

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

#### Section 2: Center Point Output

The team must agree on one output that is medium cost and medium value - the anchor for all other placements. All other outputs will be classified relative to this center point.

**Center point output:** [name the output]

**Why this is medium/medium:** [1-2 sentences explaining why the team agreed this output represents neither extreme on value or cost - not the most impactful for the customer, not the most expensive to build]

> **Quality check:** Did the whole team agree on this anchor, or did the PM choose it alone? The center point requires team agreement. If only one person chose it, revisit before proceeding.

---

#### Section 3: Four Quadrant Classification

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

#### Section 4: Quadrant Summary and Action Guidance

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

Action: Do not commit these to the build plan until the key assumption is validated. Place them in "Output Concepts to Validate" in the roadmap. Consider ps-lofi-experimentation for the highest-uncertainty items.

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

### ps-output-prioritization / Examples

### Output Prioritization Examples

---

#### Example 1: Strong

**Context:** A product team at a healthcare operations company is building a field service coordination tool for home health aides and care coordinators. The solution hypothesis is complete. The PM has validated two product outcomes from the Outcome Tree: (1) care coordinators confirm same-day schedule changes before aides depart, and (2) aides spend less time resolving conflicting visit instructions in the field. The team is running this exercise collaboratively with the engineering lead and a project manager before starting sprint planning.

---

##### Output Prioritization

**Product or initiative:** Home health field service coordination tool
**Customer role:** Care coordinator (primary), home health aide (secondary)
**Session participants:** Yemi Adeyemi (PM), Hana Kozlowski (Engineering Lead), Marcus Webb (Project Manager), Siona Patel (Operations Lead)
**Date:** June 26, 2026

---

**Section 1: Candidate Outputs**

- Real-time schedule change alert (push notification to aide when visit is modified)
- Offline visit record sync (aides can log visit details without cell coverage)
- Conflict detection dashboard (coordinator sees scheduling gaps before dispatch)
- Bulk rescheduling tool (move multiple visits at once during weather events)
- Aide availability calendar (aides submit availability windows; coordinator views them)
- Integration with third-party billing system
- Voice-to-text visit notes (aide dictates instead of typing)

---

**Section 2: Center Point Output**

**Center point output:** Aide availability calendar

**Why this is medium/medium:** The aide availability calendar requires a moderate build (a structured input form, storage, and a read view for coordinators - estimated at two sprints by Hana) and delivers moderate customer value (it reduces coordinator phone tag, which is a real pain, but does not directly address the most acute problem of same-day change notification). The team agreed it sits in the middle of both axes.

---

**Section 3: Four Quadrant Classification**

| Output | Value (H/M/L) | Value Rationale | Cost (H/M/L) | Cost Rationale | Quadrant | Priority |
|--------|--------------|-----------------|-------------|----------------|----------|----------|
| Aide availability calendar | M | Anchor | M | Anchor - two-sprint estimate, standard form + storage build | Center | Reference |
| Real-time schedule change alert | H | Directly supports product outcome 1: care coordinators confirm same-day changes before aides depart. Eliminates the primary source of missed visits. | L | Push notification with existing visit data - one sprint; no new data model required (Hana) | I | Start |
| Conflict detection dashboard | H | Directly supports product outcome 1 from the coordinator side: spots gaps before dispatch rather than after. Prevents the scheduling errors that drive incorrect visit instructions. | M | New view over existing schedule data; two sprints; some aggregation logic (Hana) | I | Start |
| Offline visit record sync | H | Directly supports product outcome 2: aides resolve conflicting instructions faster when they have access to their records in low-coverage areas. Validated in empathy interviews - 7 of 9 aides reported coverage gaps. | H | Requires conflict resolution logic for sync, local storage on device, and server-side reconciliation - four sprints minimum (Hana and Marcus) | II | Plan |
| Voice-to-text visit notes | M | Reduces aide documentation time but does not address the scheduling conflict problem that drives product outcomes 1 or 2. Valued by aides as a convenience feature. | M | Two sprints; relies on device speech API, no custom model needed (Hana) | Center-adjacent | Deprioritize |
| Bulk rescheduling tool | L | Useful during weather events but covers an infrequent scenario. Does not address the daily scheduling conflict problem that drives both product outcomes. | M | Two to three sprints; edge cases in visit dependency logic add complexity (Hana) | III | Deprioritize |
| Integration with third-party billing system | L | Does not impact care coordinators' daily scheduling work or aides' field experience. Serves finance team, not the customer. | H | Four to six sprints; requires custom API work for each billing vendor; high variability (Hana) | IV | Cut |

---

**Section 4: Quadrant Summary and Action Guidance**

**Quadrant I - Start Here**

| Output | Product Outcome Supported |
|--------|--------------------------|
| Real-time schedule change alert | Care coordinators confirm same-day schedule changes before aides depart |
| Conflict detection dashboard | Care coordinators confirm same-day schedule changes before aides depart |

Action: Both outputs enter the next sprint. Schedule change alert first (lower cost, faster signal from real-world use).

**Quadrant II - Plan Carefully**

| Output | Key Assumption to Validate | Recommendation |
|--------|---------------------------|----------------|
| Offline visit record sync | Assumption: aides will proactively sync records when coverage returns rather than relying on coordinator callbacks. This behavior has not been validated in real conditions. | Run a Wizard-of-Oz lo-fi experiment with three aides before committing to the full sync build. |

**Quadrant III - Deprioritize**

- Voice-to-text visit notes - Deferred. Real convenience value for aides but does not drive either product outcome in the current cycle. Revisit after Quadrant I outputs ship and adoption data confirms which pain remains most acute.
- Bulk rescheduling tool - Deferred. Low-frequency use case. Revisit if weather event volume increases or coordinators surface it as a blocking issue.

**Quadrant IV - Avoid or Cut**

- Integration with third-party billing system - Cut. This serves the finance team, not care coordinators or aides. No connection to either product outcome. Building it would consume four to six engineering sprints that would displace the offline sync build. The VP of Finance has requested this feature - Yemi will document the tradeoff in writing and ask for an explicit decision before the next planning cycle.

---

##### Why This Works

The classification shows genuine spread: two outputs in Quadrant I, one in Quadrant II, two deferred, one cut. The center point anchor prevented the team from calling everything high value - voice-to-text notes and the bulk tool ended up where they belong. Value rationales name specific product outcomes or validated interview findings, not business benefits. The Quadrant IV item is actually cut (with an explicit stakeholder tradeoff documented), not quietly deferred. Engineering input was used for every cost classification.

---

#### Example 2: Weak

**Context:** Same product, same scenario. The PM ran this exercise alone between other meetings, without the engineering lead or project manager. No outcome tree had been completed.

---

##### Output Prioritization (Weak Version)

**Product or initiative:** Home health field service coordination tool
**Customer role:** Not specified
**Session participants:** Jamie (PM)
**Date:** June 26, 2026

---

**Section 1: Candidate Outputs**

- Real-time schedule change alert
- Offline visit record sync
- Conflict detection dashboard
- Bulk rescheduling tool
- Aide availability calendar
- Integration with third-party billing system
- Voice-to-text visit notes

---

**Section 2: Center Point Output**

Not established. Jamie proceeded directly to classification.

---

**Section 3: Four Quadrant Classification**

| Output | Value | Cost | Quadrant |
|--------|-------|------|----------|
| Real-time schedule change alert | High | Low | I |
| Offline visit record sync | High | Medium | I |
| Conflict detection dashboard | High | Low | I |
| Bulk rescheduling tool | High | Medium | I |
| Aide availability calendar | High | Low | I |
| Integration with third-party billing system | High | High | II |
| Voice-to-text visit notes | High | Low | I |

---

**Section 4: Quadrant Summary**

Everything is either Quadrant I or Quadrant II. All outputs are labeled high value. No rationale is provided. Nothing is deprioritized. Nothing is cut.

---

##### Why This Fails

Five failures in this classification:

1. **No center point anchor.** Without an anchor, every output defaults to high value. This is the most predictable outcome of skipping Step 4.

2. **No customer role named.** Value cannot be assessed if the team has not agreed on who the customer is. "High value" to whom?

3. **No value rationale.** "High" is not a rationale. The classification table has no evidence - it reflects the PM's advocacy for all outputs, not customer-grounded evidence.

4. **No engineering input on cost.** Offline visit record sync is listed as Medium cost. In the strong example, Hana estimated it at four sprints due to sync conflict resolution complexity. Without a technical voice, cost estimates are guesses.

5. **Nothing is cut.** A prioritization exercise that produces zero cuts has not prioritized anything. It has produced a wish list with a grid label attached.

---

#### Example 3: Drift Bug - Value Defined as Business Revenue Impact

**Context:** Same product. The PM has access to the outcome tree and included the engineering lead. But during the classification session, the PM reframed the value axis as "business revenue impact" rather than customer outcome impact.

---

##### Output Prioritization (Drift-Bug Version)

**Product or initiative:** Home health field service coordination tool
**Customer role:** Care coordinator, home health aide
**Session participants:** Yemi Adeyemi (PM), Hana Kozlowski (Engineering Lead)
**Date:** June 26, 2026

---

**Section 3: Four Quadrant Classification (excerpt)**

| Output | Value (H/M/L) | Value Rationale | Cost (H/M/L) | Quadrant |
|--------|--------------|-----------------|-------------|----------|
| Integration with third-party billing system | H | This will eliminate manual billing reconciliation and reduce finance team overhead by an estimated 12 hours per week. High revenue protection value. | H | II |
| Conflict detection dashboard | M | Good for coordinators but hard to tie to a revenue outcome. No clear upsell path. | M | Center |
| Real-time schedule change alert | L | Coordinators already manage this via phone. Low incremental revenue impact. | L | III |

---

##### The Drift

The PM has substituted business revenue impact for customer outcome impact on the Y-axis. The result:

- Billing system integration (which serves the finance team, not care coordinators) is rated High Value because it protects revenue.
- Conflict detection dashboard (which directly supports care coordinators' ability to prevent missed visits) is rated Medium because it does not generate revenue.
- Real-time schedule change alert (which eliminates the primary cause of missed visits and is the most direct driver of product outcome 1) is rated Low because coordinators "already manage it via phone" - meaning it does not represent incremental revenue.

This ranking inverts the actual prioritization. The output that matters most to the customer lands in Quadrant III (Deprioritize). The output that serves the finance team lands in Quadrant II (Plan Carefully).

##### The Fix

Reframe the value axis before any classification begins: "Value means customer value. What does each output allow the customer to achieve that they cannot achieve today, or cannot achieve as reliably?"

Then return to the Outcome Tree. Product outcome 1 (care coordinators confirm same-day schedule changes before aides depart) is the reference point. For each output, ask: does this output drive progress toward that outcome for care coordinators or home health aides?

- Conflict detection dashboard: yes, directly
- Real-time schedule change alert: yes, directly, and at lower cost
- Billing system integration: no - it serves finance, not care coordinators

The revised quadrant placements match the strong example above. The drift occurred because the PM brought a revenue-attribution lens to a customer-value exercise. Catching this early - before cost estimates are done and stakeholders are aligned - saves a planning cycle.

## ps-go-to-market | Go-to-Market Enablement

Playbook number: 20. Phase: Create.

### ps-go-to-market / Instructions

#### Purpose

Create a **Productside-style Go-to-Market Enablement artifact** that prepares internal teams to execute a product launch.

This skill helps a Product Manager translate months of discovery and definition work into six clear sections that sales, marketing, customer support, and technical teams can act on without additional interpretation. It is the bridge between what the PM knows and what the rest of the organization needs to know before launch day.

This is a **Create phase** skill (Template 20 of 24). It is downstream of almost everything - it synthesizes the work of the full discovery and definition process into a single, jargon-free communication package. It does not produce anything new; it repackages what is already known into the format that non-PM audiences can use.

#### Key Concepts

##### GTM Is a Team Sport

The PM provides information, synthesizes upstream work, and owns the artifact. But they do not build it alone. Sales, marketing, customer support, and technical teams are all stakeholders in the GTM process - they bring the customer-facing context and execution knowledge that the PM does not have from inside the product team. Building this document in isolation produces a document that sounds right but misses what each function actually needs to know.

##### The Persona-Voice Problem Statement

The formal Problem Statement from ps-framing-the-problem uses a structured five-stem format written for product teams. The GTM Problem Statement does something different: it retells the same story in first-person from the customer's perspective, in emotional and accessible language.

The format:
"I am a [role] [doing/struggling with X]. [Pain]. Because [root cause]. Which makes me feel [emotional consequence]."

This reframing is not decoration. Account executives and customer success managers need to feel the customer's pain to communicate it credibly. A business-case summary does not accomplish that. A first-person narrative does.

##### Solution Summary vs. Positioning Statement

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

##### Key Messages Are Benefit Statements, Not Feature Lists

The Key Messages table is where each persona learns what is in it for them. This is not a feature brief. Features describe what the product does. Benefits describe what the customer gains. "Automated case routing" is a feature. "Time back to focus on complex cases instead of sorting tickets" is a benefit.

Write 3-5 bullet points per persona. Each bullet answers: what does this change for me, in my role, in my day? If the answer could come from a product spec, it is a feature - rewrite it as an outcome.

##### Every Message Needs Proof

A key message without proof is a claim. Each message gets **proof points the persona would trust**: a testimonial, a pilot result, a case study, a published benchmark. Proof must be real. Proof the team doesn't have yet goes in the Proof Points column with the exact label `To gather:` followed by the kind of proof needed (for example, `To gather: pilot-site quote on status calls`). Never invent it.

Messages are written for **at least one user and one buyer persona**. A buyer usually cares about different outcomes than a user, so if the user and buyer messages overlap heavily, one of them is probably generic. Every message traces back to the positioning statement.

##### Readiness Goals vs. Launch Goals

**Readiness goals** prove the product is ready to ship, measured in a limited pre-release test (Product Readiness Testing). **Launch goals** prove the go-to-market plan worked, measured in the market after release. A goal that belongs to readiness doesn't belong here. A **launch task** ("train the sales team," "publish the web page") isn't a goal either. Ask what result the task should produce.

##### Launch Goals vs. Product Success Metrics

Launch Goals are not the same as the ongoing metrics from ps-outcome-tree or ps-measuring-outcomes. Launch Goals are time-bounded success indicators for the launch window itself: adoption milestones, satisfaction scores, and efficiency gains that confirm the launch executed correctly.

Each row in the Launch Goals table requires a numeric target. "Improve satisfaction" is not a launch goal. "Achieve NPS of 40+ in first 90 days post-launch" is a launch goal. Each target also needs a basis (a baseline, a benchmark, or evidence), a measure the team can actually collect, and a tie to a business or product outcome. **The targets are the PM's to set.** The skill questions whether they are realistic; it does not pick the number.

##### Jargon-Free Writing

This artifact must be readable without a PM dictionary. Every sentence should pass this test: could an account executive read this aloud to a prospect without having to explain a term? Technical vocabulary (API integrations, workflow automation pipelines, orchestration layers) fails that test. Customer-benefit language (faster order processing, fewer manual steps, real-time visibility) passes it.

##### The GTM Timing Arc

Go-to-Market preparation is not a one-week sprint before launch. The typical arc:
- Develop the GTM plan: 1-2 months before launch
- Review and align with stakeholders: 2-6 months before launch
- Drive internal awareness across functions: ongoing during the build phase
- Generate partner awareness: 2-4 months before launch
- Drive market awareness: 1-3 months before launch
- Launch date with press release or announcement: the milestone everything else builds toward

Starting late on GTM preparation is the most common failure mode. This artifact should be in circulation well before the launch date, not assembled in the final week.

##### How AI Supports This Play

The Playbook casts AI as a **critic of the two parts the PM writes fresh here**: key messages with proof points, and launch goals. For messages, AI checks that each is a benefit, free of jargon, and backed by proof the persona would trust. For launch goals, it tests the measure and whether the target is realistic, and keeps launch goals distinct from readiness goals. The messages and targets stay the PM's. AI cannot know what the buyers trust or what the business can hit.

- **Use it when:** positioning and personas are set, and the PM has drafted key messages, proof points, and launch goals to pressure-test.
- **Avoid it when:** positioning or personas are still unsettled (route to ps-positioning-statement or ps-proto-persona), or the request is for AI to set the targets. It has no data on the market or the business.
- **Return:** messages tested for benefit, jargon, and credible proof; launch goals checked for measure, realistic target, and timeframe; and proposed rewrites for the PM to accept, adapt, or reject.

##### Working With AI

The Productside Playbook sets one rule for every AI-assisted Play: **the Product Manager does the thinking, and AI pressure-tests it.** In this skill, you are the AI. Hold yourself to these rules:

1. **Pressure-test before you produce.** When the user brings a draft, critique it against the Play's formats and criteria first. Point at the specific words that fail and ask the user to fix them. Offer rewrites only after the critique, as options to accept, adapt, or reject.
2. **Never stand in for the customer.** Do not present jobs, quotes, needs, or pains you generated as research, and do not answer as the persona as if your answers were evidence. Anything you draft about customers is a hypothesis, labeled as one, to validate with real people. Role-play is allowed only as rehearsal where the Play calls for it, labeled as practice, and nothing from it goes into findings.
3. **Never stand in for the team's judgment.** Do not put unsourced figures into the artifact, and do not make calls the team should own. A number without a source is a blank to fill, so mark it that way.
4. **Work the five habits.** *Context:* ask for the persona, market, outcome, and constraints when they are missing. *Guide:* offer competing views and welcome pushback. *Enforce:* work inside the Play's template, not around it. *Outcome:* tie the work to the decision it supports. *Iterate:* go step by step rather than one-shot.
5. **Keep best guess honest.** Best guess mode is allowed. When you use it, label every inferred detail inline and end with **Assumptions to Validate**. A best guess is a starting point to test, never a finding.

For people working in a chat tool without this skill, the Play's copy-paste prompts are in prompts/ (uploaded reference: `07-prompts.md`, section `ps-go-to-market / Companion / README.md`).

##### Guided Mode

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

#### Application

Use template.md (uploaded reference: `05-create.md`, section `ps-go-to-market / Template`) for the scaffold.

See the source play pages in assets/ps_go_to_market_playbook_pages.pdf (source material, not included in this upload kit).

##### Required Output Convention

Default to a **clean, paste-ready artifact**.

That means:

- all six sections completed
- Problem Statement in first-person persona voice, not third-person business case
- Positioning Statement in the exact seven-element formula
- Key Messages written as benefit bullets per persona, not feature descriptions
- Launch Goals table with numeric targets in every row
- no PM or technical jargon visible to a non-PM audience
- commentary and explanation belong below the artifact, not inside the fields

##### Step 1: Tech-Role Bias Guard

Before writing any content, confirm who the product serves. LLMs and PMs alike default toward technical vocabulary and engineering-adjacent framing. The Key Messages in particular must be written from the customer's perspective on what changes for them, not from the product team's perspective on what they built.

Ask explicitly: who are the 2-3 personas this product serves? What is their job? What frustrates them? What do they gain? These answers govern the language in every section, especially Key Messages.

If the user's initial framing focuses on capabilities ("what the platform does") rather than customer gains ("what changes for the customer"), surface that and redirect before drafting.

##### Step 2: Gather Upstream Artifacts

Before drafting, ask whether the user has these materials to share:

- Problem framing from ps-framing-the-problem (five-stem format, for translation to persona voice)
- Solution hypothesis from ps-solution-hypothesis (for the Solution Summary)
- Positioning statement from ps-positioning-statement (for verbatim copy into the Positioning Statement section)
- Persona work from ps-proto-persona (identifies the personas for Key Messages and Target Audience)

Use whatever the user can provide. If a section has no upstream source, draft from context and flag it for review. Do not gate the skill on whether all upstream plays have been run.

##### Step 3: Optional Web Research

Web research is appropriate for this skill when it helps with:

- Competitive landscape: understanding what alternatives exist for the "Unlike" element and how to differentiate the Key Messages from competitor positioning
- Market segment context: knowing the size and characteristics of target segments for the Target Audience section
- Industry launch timing norms: understanding whether 1-2 months of GTM prep is typical or compressed for this market

Do not use web research to substitute for customer discovery. If the user lacks a clear problem statement or persona definition, the answer is to run upstream skills, not to fill the gap with market research.

##### Step 4: Write the Problem Statement in Persona Voice

Translate the formal five-stem Problem Statement (from ps-framing-the-problem, or from the user's description if that play has not been run) into a first-person narrative from the customer's perspective.

Use the scaffold:
"I am a [role] [doing/struggling with X]. [Pain]. Because [root cause]. Which makes me feel [emotional consequence]."

The voice should be specific to the persona's role and daily experience. It should be vivid enough that a sales person reading it thinks: "yes, I've heard this from customers."

Check: is this written from the customer's perspective, or from the PM's perspective on the customer? If the PM is the narrator, rewrite it.

Target length: 50-80 words.

##### Step 5: Write the Target Audience Section

Answer three questions in prose:

1. Who is the target customer? (the decision-making unit or the customer type, not a segment label)
2. Who are the product personas? (the named roles from proto-persona work)
3. What are the target market segments? (verticals, company sizes, geographies, or use cases the launch is targeting)

Keep this concise - 30-50 words. This is orientation, not a market sizing exercise.

##### Step 6: Write the Solution Summary

Write a plain-language description of the product: what it is, what it does, what it improves. This is not the hypothesis format (If/Then). It is not the positioning statement. It is a product description in ordinary language.

Test: could a customer support rep read this out loud and explain the product to a customer calling in for the first time? If technical vocabulary appears, rewrite it.

Target length: 40-60 words.

##### Step 7: Write the Positioning Statement

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

##### Step 8: Write Key Messages for Each Persona

**The PM drafts the messages; the skill critiques them** (mirrors prompts/01 (uploaded reference: `07-prompts.md`, section `ps-go-to-market / Companion / 01-pressure-test-messages.md`)). Working one persona at a time:

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

##### Step 9: Write Launch Goals

**The PM drafts the goals and sets the targets; the skill questions them** (mirrors prompts/02 (uploaded reference: `07-prompts.md`, section `ps-go-to-market / Companion / 02-pressure-test-launch-goals.md`)). One goal at a time:

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

##### Step 10: Jargon Check

Read back through the completed artifact and flag any vocabulary that a sales director, marketing manager, or customer support lead might not understand without a PM glossary. Common offenders:

- Technical terms: API, orchestration, pipeline, integration layer, real-time sync engine
- PM vocabulary: hypothesis, assumption, outcome tree, solution space, JTBD
- Compound jargon: "automated workflow automation platform" (redundant and opaque)

Rewrite flagged phrases in plain language. The test is: would a new account executive on their second week understand this without asking what it means?

##### Step 11: Offer Next Steps

At the end of the artifact, offer the user three options:

1. Share with sales leadership for review and input on Key Messages - the sales team will flag whether the benefit bullets match what they hear from customers
2. Share with marketing to align on the Positioning Statement as the messaging anchor for launch campaigns
3. Schedule a launch readiness review with all GTM stakeholders to walk through the artifact together and confirm each function knows what they need to execute

#### Examples

See examples/sample.md (uploaded reference: `05-create.md`, section `ps-go-to-market / Examples`).

The example set includes:

- a strong go-to-market artifact for a supply chain scenario with vivid persona-voice Problem Statement, benefit-focused Key Messages, and numeric Launch Goals
- a weak version with a business-case Problem Statement, feature-list Key Messages, and vague Launch Goals
- a drift-bug example where Key Messages are written from the product team's technical perspective, not from the customer's perspective on their gains

#### Common Pitfalls

##### Pitfall 1: Problem Statement Written in Third-Person Business Case Voice

**Symptom:** The Problem Statement reads like an executive summary: "Our research indicates that supply chain coordinators experience significant inefficiencies in shipment tracking, resulting in productivity losses estimated at..."

**Consequence:** Sales and support teams cannot use this to empathize with customers. It sounds like an analyst report, not a customer's lived experience. The persona voice is what makes this section useful.

**Fix:** Rewrite in first-person from the customer's perspective using the scaffold: "I am a [role]... [pain]. Because [root cause]. Which makes me feel [emotion]." The voice must come from the customer's experience, not the PM's analysis of it.

##### Pitfall 2: Key Messages That List Features Instead of Benefits

**Symptom:** The Key Messages bullets read like release notes: "Automated order routing," "Real-time inventory sync," "Multi-warehouse visibility dashboard."

**Consequence:** Sales and marketing cannot translate these into customer conversations. Features describe what the product does, not what the customer gains. Non-PM audiences cannot bridge that gap on their own.

**Fix:** For each bullet, ask "so what?" until you reach a customer outcome. "Automated order routing" becomes "orders routed to the right warehouse without manual intervention, so coordinators focus on exceptions rather than every transaction."

##### Pitfall 3: Positioning Statement Paraphrased or Incomplete

**Symptom:** The Positioning Statement section contains a narrative description of the product's value rather than the seven-element formula. Or the "Unlike" element is missing because it felt awkward to name a competitor.

**Consequence:** Downstream messaging loses precision. Marketing campaigns, sales pitches, and support scripts all drift because the anchor they share is not structured. The "Unlike" element in particular is what makes positioning distinct - without it, the statement could describe any competitor's product.

**Fix:** Use the seven-element formula verbatim: For / Who / The / Is a / That / Unlike / Our product gives. Every element must appear. The "Unlike" element must name a real alternative (including "manual processes using spreadsheets" if that is the real competitor).

##### Pitfall 4: PM Builds the Artifact Alone

**Symptom:** The GTM document is drafted without input from sales, marketing, or customer support. It is polished and complete but reflects only the PM's perspective.

**Consequence:** The document misses what each function actually needs. Sales will have different questions than marketing. Support will need different language than sales. A solo-authored GTM document rarely survives first contact with the field.

**Fix:** Treat the artifact as a starting draft for collaborative review, not a finished deliverable. Share it with each function and explicitly ask: "Is this how you would describe the customer's problem? Does this messaging match what you hear in the field? What would you add or change?"

##### Pitfall 5: Launch Goals Are Directional Instead of Numeric

**Symptom:** The Launch Goals table contains rows like: "Improve user adoption," "Increase customer satisfaction," "Reduce onboarding friction."

**Consequence:** The team cannot evaluate launch success. Directional goals pass every test and fail every real measurement. Without a number, there is no way to know if the launch succeeded.

**Fix:** Every Target cell in the table must contain a number or percentage. "Improve user adoption" becomes "75% of licensed users complete onboarding within 14 days of provisioning."

##### Pitfall 6: Solution Summary Filled with Product Jargon

**Symptom:** The Solution Summary reads: "A cloud-native SaaS platform with real-time API integrations that orchestrates multi-system workflow automation across ERP and WMS environments."

**Consequence:** Support representatives, account executives, and marketing managers cannot explain the product. This reads as a technical architecture description, not a product description. It communicates nothing useful to a non-PM audience.

**Fix:** Write a product description that your best customer could read aloud to a colleague. Test it against the question: "could a new account executive on their second week explain this to a prospect?" If not, simplify.

##### Pitfall 7: Key Messages Written for Only One Persona

**Symptom:** The Key Messages table has one row for the primary user persona and nothing for the buyer persona or other affected roles.

**Consequence:** Marketing campaigns and sales conversations with buyers (who are different from users) have no messaging anchor. The buyer often controls the purchase decision but has different concerns than the daily user - cost, risk, visibility, and control rather than workflow efficiency.

**Fix:** Build Key Messages for each distinct persona: at minimum the primary user and the economic buyer. If the product serves three distinct roles, write three rows.

##### Pitfall 8: Tech-Role Bias in Key Messages

**Symptom:** Key Messages emphasize technical impressiveness: "The platform's real-time data integration engine delivers sub-200ms sync latency across all connected systems." The bullets celebrate what the engineering team built, not what changes for the customer.

**Consequence:** The GTM document reads as an engineering achievement report. Sales and marketing cannot translate this into customer benefit language because there is no customer benefit language to translate - only technical specifications.

**Fix:** Apply the perspective test to every bullet. Ask: who is the subject of this sentence? If it is the product, the platform, or the system, the bullet is a feature. If it is the customer and what they can now do or stop doing, it is a benefit. Rewrite every technical subject into a customer subject.

##### Pitfall 9: Claims With No Proof Behind Them

**Symptom:** Key messages that promise outcomes ("cut dispatch time in half") with nothing in the proof column, or with proof the model wrote: a testimonial no customer gave, a pilot result no pilot produced.

**Consequence:** Sales repeats a claim it can't back up. The first skeptical buyer asks for evidence, and the message loses credibility for the whole launch.

**Fix:** Every message gets proof the persona would trust, or the proof is listed as "still to gather before launch." Never invent testimonials, quotes, or results.

##### Pitfall 10: Goals That Prove Nothing

**Symptom:** Launch goals like "train the sales team" (a task), "zero critical defects in beta" (a readiness goal), or "40% adoption in 30 days" with no baseline behind the target.

**Consequence:** The team hits every goal and still can't say whether the go-to-market plan worked.

**Fix:** Keep only goals that show the market responded. Move readiness goals to Product Readiness. Turn tasks into the result they should produce. Give every target a baseline or evidence, a measure someone can collect, and a timeframe.

#### References

##### Skill Files

- template.md (uploaded reference: `05-create.md`, section `ps-go-to-market / Template`) - six-section GTM handoff scaffold, with proof points
- prompts/ (uploaded reference: `07-prompts.md`, section `ps-go-to-market / Companion / README.md`) - copy-paste prompts for chat-based AI tools (2: key messages and proof points, launch goals)
- examples/sample.md (uploaded reference: `05-create.md`, section `ps-go-to-market / Examples`) - strong, weak, and drift-bug examples

##### Related Skills

- **Upstream:** ps-framing-the-problem (uploaded reference: `03-discover-investigate.md`, section `ps-framing-the-problem / Instructions`) provides the Problem Statement for translation into persona voice
- **Upstream:** ps-proto-persona (uploaded reference: `03-discover-investigate.md`, section `ps-proto-persona / Instructions`) provides the personas for Key Messages and Target Audience
- **Upstream:** ps-solution-hypothesis (uploaded reference: `04-discover-define.md`, section `ps-solution-hypothesis / Instructions`) provides the solution framing for the Solution Summary
- **Upstream:** ps-positioning-statement (uploaded reference: `04-discover-define.md`, section `ps-positioning-statement / Instructions`) provides the Positioning Statement verbatim
- **Upstream:** ps-product-outcome-canvas (uploaded reference: `04-discover-define.md`, section `ps-product-outcome-canvas / Instructions`) consolidates the Problem Statement, Positioning Statement, and Key Features fields; use the canvas as the source of truth when it is available
- **Downstream:** none (this is a launch enablement output, not a discovery input for any other skill)

##### Project Docs

- [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)
- [informative-documents/framework-glossary.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/framework-glossary.md)
- [informative-documents/skill-dependency-map.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/skill-dependency-map.md)

##### Source Material

- assets/ps_go_to_market_playbook_pages.pdf (source material, not included in this upload kit)
- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 92-97: Template 20 of 24 there, with the AI overview on slide 94 and prompts on slides 95, 96. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).
- [Baseline Playbook version](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml). Full source PDF supplied separately.
- Productside Playbook companion document (supplied separately)

### ps-go-to-market / Template

### Go-to-Market Enablement

#### When to Use This

Use this template during the **Create phase** after completing positioning, solution hypothesis, and proto-persona work. Run it collaboratively with sales, marketing, and customer support stakeholders before setting the launch timeline.

Upstream artifacts that feed this template:
- Problem framing (ps-framing-the-problem): provides the five-stem structure to translate into persona voice
- Solution hypothesis (ps-solution-hypothesis): provides the solution framing for plain-language translation
- Positioning statement (ps-positioning-statement): provides the seven-element formula to copy verbatim
- Proto-persona (ps-proto-persona): identifies the personas and their pains for Key Messages and Target Audience

#### Template

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

#### Usage Guidance

##### Filling the Template

1. Complete **Product Context** to anchor who participated and what the launch timeline is.
2. Write the **Problem Statement** last, after reading the framing from ps-framing-the-problem. Translate from analytical to emotional and first-person.
3. Write **Target Audience** from the proto-persona work - personas should match what has already been validated.
4. Write the **Solution Summary** as if explaining the product to a new support hire on day one.
5. Copy the **Positioning Statement** verbatim from ps-positioning-statement output. If that play has not been run, construct it fresh using the formula.
6. Build **Key Messages** persona by persona. Start with the primary user, then the buyer, then any other affected roles.
7. Set **Launch Goals** by working backward from the launch date - what does success look like at 30, 60, and 90 days?

##### What Goes Where

| Section | Contains | Does NOT Contain |
|---------|----------|-----------------|
| Problem Statement | First-person customer narrative with emotion | Third-person business case language |
| Target Audience | Named personas and market segments | The PM or product team as the audience |
| Solution Summary | Plain-language product description | Technical vocabulary, PM jargon, hypothesis format |
| Positioning Statement | Seven-element formula verbatim | Paraphrasing, narrative description, incomplete elements |
| Key Messages | Benefit bullets per persona | Feature descriptions, capability lists |
| Launch Goals | Numeric targets for the launch window | Directional language without numbers, long-term metrics |

##### Connecting to Other Skills

- **Upstream:** ps-framing-the-problem provides the Problem Statement structure for translation. ps-proto-persona provides the personas. ps-solution-hypothesis provides the solution framing. ps-positioning-statement provides the Positioning Statement verbatim.
- **Downstream:** This skill is an endpoint. The artifact feeds into sales enablement, marketing campaigns, and launch readiness reviews - but no other playbook skills consume it.

##### Capacity Reference

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

### ps-go-to-market / Examples

### Go-to-Market Enablement Examples

All three examples use the same scenario: a field services management platform for a mid-market HVAC and facilities maintenance company, launching a mobile dispatch and job completion product for their service technicians and operations managers.

---

#### Strong Example

**Context:** The product team at a field services software company is preparing to launch a mobile dispatch and job completion platform for HVAC and facilities maintenance companies. They have completed proto-persona work (two personas: field technicians and operations managers), framing-the-problem, solution hypothesis, and a positioning statement. The GTM document was built collaboratively with the sales director, a marketing manager, and the customer success lead.

---

##### Go-to-Market Enablement

**Product or initiative:** FieldSync Mobile - dispatch and job completion for HVAC and facilities maintenance
**Launch target date:** September 15, 2026
**GTM participants:** Camille Osei (PM), Derek Sloane (Sales Director), Marta Jimenez (Marketing Manager), Priya Arun (Customer Success Lead)
**Date prepared:** June 26, 2026

---

**Section 1: Problem Statement**

I am a field technician juggling five to eight jobs a day from a paper dispatch sheet and a phone call system that is already behind by 9 AM. I spend twenty minutes at the start of every job tracking down the right parts information and customer history. Because everything lives in a back-office system I cannot access on my phone. Which makes me feel like I am always one step behind and never quite set up to do a good job for the customer standing in front of me.

---

**Section 2: Target Audience**

Target customer: Operations managers and field technicians at mid-market HVAC and facilities maintenance companies with 20-200 technicians in the field. Personas: Field Technician (daily user, executes jobs) and Operations Manager (buyer, owns dispatch and productivity). Target segments: HVAC service companies, commercial facilities maintenance contractors, and multi-site property management maintenance teams in North America.

---

**Section 3: Solution Summary**

FieldSync Mobile is a dispatch and job management app for field technicians. It delivers each day's job schedule to their phone, with full customer history and parts information attached. Technicians complete and close jobs on-site. Operations managers see real-time job status without calling the field. Paper dispatch sheets and status check calls go away.

---

**Section 4: Positioning Statement**

For: operations managers at mid-market HVAC and facilities maintenance companies
Who: need real-time visibility into field job status without calling technicians for updates
The: FieldSync Mobile
Is a: mobile dispatch and job management platform
That: gives technicians everything they need to complete jobs on-site and closes the status gap between the field and the office
Unlike: paper dispatch sheets and reactive phone-based status updates
Our product gives: operations managers live job progress without manual check-ins, and technicians the right information at the job site without back-office dependency

---

**Section 5: Key Messages**

| Persona | Key Messages | Proof Points |
|---------|-------------|--------------|
| Field Technician | - Start every job with the full customer history and parts information already on your phone, no back-office calls needed | - Pilot technicians made 70% fewer back-office calls in the 6-week pilot |
| | - Close jobs on-site without driving back to drop off paperwork | - Video walkthrough by a pilot-site technician |
| | - Get the next job dispatched to your phone the moment the current one closes | |
| | - Spend job time doing the work, not tracking down what you need to do it | |
| Operations Manager | - Know where every technician is and what job they are on without picking up the phone | - Pilot-site operations manager quote on status calls |
| | - Catch schedule problems before they become missed appointments, not after | - To gather: missed-appointment rate before and after the pilot |
| | - Close out completed jobs in real time, not at the end of the day from handwritten notes | |
| | - Reduce the first-call resolution gap caused by technicians arriving without the right information | |

---

**Section 6: Launch Goals**

| Goal/Objective | Measure/Metric | Target |
|----------------|----------------|--------|
| Field technician adoption | Technicians actively using the app for all assigned jobs | 80% of licensed technicians active within 30 days of provisioning |
| Paperwork elimination | Reduction in paper dispatch sheets printed per week | 90% reduction at pilot sites within 60 days |
| Customer satisfaction | NPS collected from field job completions | NPS of 45 or higher in first 90 days post-launch |
| Operations efficiency | Inbound status calls from operations managers to technicians | 60% reduction within 60 days at pilot sites |

---

**Next Steps**

- [ ] Share with sales leadership for Key Messages review
- [ ] Share with marketing as the messaging anchor for launch campaigns
- [ ] Schedule launch readiness review with all GTM stakeholders

---

##### Why This Works

**Problem Statement:** Written in the technician's first-person voice with a specific pain (twenty minutes tracking down parts), a named root cause (system inaccessible from the field), and an emotional consequence (always one step behind). A sales person reading this will recognize a customer they have talked to.

**Target Audience:** Names both personas clearly, specifies the market segment with enough detail to guide a sales territory decision (20-200 technicians, North America, three named verticals).

**Solution Summary:** No jargon. No technical vocabulary. A new customer support rep could read this to a customer calling in. Every sentence describes what the product does for the person using it.

**Positioning Statement:** All seven elements present. "That" is a customer outcome (closes the status gap), not a feature (has real-time sync). "Unlike" names the real alternative (paper sheets and phone calls). "Our product gives" is outcome language for both buyer and user.

**Key Messages:** Each persona's messages carry proof from the pilot, and the one proof point the team doesn't have yet is marked "To gather" rather than invented. Every bullet is written from the persona's perspective on what changes for them. "Start every job with the full customer history" is not a feature description - it is the technician's experience of the feature. The operations manager row addresses their concerns (visibility, schedule control) separately from the technician row.

**Launch Goals:** Four rows, all numeric targets, all time-bounded. "80% of licensed technicians active within 30 days" is a launch goal. "90% reduction in paper dispatch sheets" is measurable and confirms a behavioral change, not just product availability.

---

#### Weak Example

**Context:** Same scenario, same team, same upstream artifacts. But this version was drafted by the PM alone, without input from sales or marketing, in the afternoon before a leadership presentation.

---

##### Go-to-Market Enablement

**Product or initiative:** FieldSync Mobile
**Launch target date:** September 2026
**GTM participants:** Camille Osei (PM)
**Date prepared:** June 26, 2026

---

**Section 1: Problem Statement**

Our analysis shows that field technicians at HVAC and facilities maintenance companies experience significant inefficiencies in job dispatch and completion workflows. Manual paper-based processes create information gaps between field teams and operations management, resulting in reduced first-call resolution rates and increased inbound status inquiries. There is a clear market opportunity for a mobile-first solution that addresses these coordination challenges.

---

**Section 2: Target Audience**

Mid-market HVAC and facilities maintenance companies. Field technicians and operations managers. Various market segments in the facilities management space.

---

**Section 3: Solution Summary**

FieldSync Mobile is a cloud-native mobile platform that provides real-time job dispatch, status tracking, and completion workflows integrated with back-office systems via API. The platform enables bidirectional data synchronization between field devices and operations management software, eliminating manual data entry and enabling real-time operational visibility.

---

**Section 4: Positioning Statement**

FieldSync Mobile is the leading mobile solution for field services teams. It helps HVAC and facilities companies manage their field workforce more efficiently by connecting technicians with the information they need and giving operations managers the visibility they require to run a productive field operation.

---

**Section 5: Key Messages**

| Persona | Key Messages |
|---------|-------------|
| Field Technician | - Mobile dispatch with real-time updates |
| | - Digital job completion workflows |
| | - Integrated customer and parts data access |
| Operations Manager | - Real-time field visibility dashboard |
| | - Automated status updates |
| | - Paperless operations management |

---

**Section 6: Launch Goals**

| Goal/Objective | Measure/Metric | Target |
|----------------|----------------|--------|
| Improve user adoption | Track active users | Increase over time |
| Increase customer satisfaction | Monitor NPS | Improve from baseline |
| Reduce paper usage | Track paper consumption | Significant reduction |

---

##### Why This Fails

**Problem Statement:** Written as a market analysis report, not from the customer's perspective. "Our analysis shows" is the PM speaking about customers, not a customer speaking for themselves. There is no emotion, no specific role, no named pain. A sales person reading this learns nothing they can use in a customer conversation.

**Target Audience:** Vague. "Various market segments in the facilities management space" gives a sales team nothing to work with. No segment sizing, no specific verticals, no customer profile.

**Solution Summary:** Full of technical jargon: "cloud-native," "bidirectional data synchronization," "API." A customer support rep could not explain this to a customer. A marketing manager would have to completely rewrite it before using it in a campaign.

**Positioning Statement:** Missing four of seven elements. There is no "For / Who / The / Is a / That / Unlike / Our product gives" structure. It reads as a marketing blurb, not a positioning statement. "The leading mobile solution" is a claim, not a differentiator. "Unlike" is absent entirely.

**Key Messages:** Features, not benefits. "Mobile dispatch with real-time updates" is a feature description. It tells the technician what the product has, not what changes for them. A sales person cannot use this to answer "why should I care?" from a prospect.

**Launch Goals:** No numeric targets. "Increase over time" and "Improve from baseline" are not goals - they are directions. The team cannot evaluate launch success against these. They will pass every check and prove nothing.

---

#### Drift-Bug Example

**Title:** Tech-Role Bias - Key Messages Written as an Engineering Achievement Report

**Context:** Same scenario. The PM has done strong upstream work - proto-personas completed, positioning statement drafted, problem framing solid. They reach the Key Messages section and, without realizing it, shift perspective. Instead of writing from the customer's point of view, they write from the product team's point of view about what they built.

---

**Key Messages (drift version):**

| Persona | Key Messages |
|---------|-------------|
| Field Technician | - The platform's offline-capable architecture ensures job data is available even without cell coverage |
| | - A real-time sync engine with sub-500ms latency delivers updated dispatch information the moment jobs are assigned |
| | - The native iOS and Android app uses device GPS to auto-log arrival and departure for compliance audit trails |
| Operations Manager | - A configurable role-based permissions model gives operations managers fine-grained control over technician data visibility |
| | - The dispatch algorithm uses machine learning to optimize technician routing based on historical job completion data |
| | - API-first architecture enables integration with existing ERP and work order management systems |

---

##### What Went Wrong

Every bullet in this table describes what the engineering team built, not what the customer gains. The subjects are the platform, the sync engine, the app, the algorithm, and the API. The customers (the technician, the operations manager) appear only as recipients of technical capabilities, not as people whose work is meaningfully changed.

A sales director reading this cannot use it. An account executive cannot translate "sub-500ms latency" into a customer conversation. A marketing manager cannot turn "API-first architecture" into a campaign benefit. The GTM document has become an engineering spec dressed as a sales enablement tool.

This is tech-role bias: the product team's pride in what they built has displaced the customer's perspective on what they gain.

**The perspective test:** Ask of every bullet: who is the subject? If it is the platform, the engine, the algorithm, or the architecture, it is a feature. Rewrite it so the customer is the subject.

---

**Key Messages (corrected version):**

| Persona | Key Messages |
|---------|-------------|
| Field Technician | - Get to your next job with all customer history and parts information already downloaded, even when cell coverage cuts out |
| | - See new jobs dispatched to your phone the moment they are assigned, no radio check or callback needed |
| | - Arrive and departure logging happens automatically - nothing extra to tap at the start or end of a job |
| Operations Manager | - Control which technicians can see which job types and customer accounts, without IT involvement |
| | - Let the system suggest the most efficient routing for the day's jobs, then adjust with a drag |
| | - Connect FieldSync to your existing work order or ERP system without a custom build |

---

##### The Fix

For each original bullet:
1. Identify the technical subject (the platform, the engine, the algorithm)
2. Ask: what does this mean for the customer, specifically?
3. Rewrite the bullet with the customer as the subject, in the customer's language

"Sub-500ms latency delivers updated dispatch" becomes "See new jobs dispatched the moment they are assigned." The technical fact (latency) disappears. The customer experience (immediate visibility) remains. That is the trade the GTM document requires.

Repeat this for every bullet until no technical vocabulary remains in the Key Messages table.

## ps-product-readiness | Product Readiness Testing

Playbook number: 21. Phase: Create.

### ps-product-readiness / Instructions

#### Purpose

Create a **Productside-style Product Readiness artifact** from a structured pre-launch test plan.

This skill helps a Product Manager plan and document a beta program that validates the product with real customers before market release. The output is a three-section artifact: a Test Plan (who, how many, how long, and which team roles), a Goals table (objectives, metrics, and numeric targets), and an Assumptions and Risks section (honest documentation of what the test does not cover).

This skill belongs to the **Create phase** and marks a Key Decision Point. The results of the readiness test feed the final Go/No Go decision before launch. The playbook is explicit: **do not be afraid to stop a launch if the product is not ready.** A No Go outcome is a valid and sometimes correct result, not a failure.

Use this skill when you need to:
- design a beta test plan with real customers before committing to market launch
- define Go/No Go criteria that are locked before the test begins
- assign team roles for the test and document what the test does not cover
- gate entry to the Deliver phase with an explicit readiness decision

This is not a first-contact usability test. If users have never touched the product before, this is not the right play - run lo-fi experimentation or a structured pilot first. This is not a readiness check on the product team's internal processes; it is a validation of the product with real customers in real context.

#### Key Concepts

##### This Is Not the First Time Users Test the Product

Product Readiness Testing is the final validation before market release. It presupposes earlier rounds of testing: lo-fi experimentation, clickable prototype feedback, pilot access, and discovery work with real customers. If this is the first time users are touching the product, the team is using Product Readiness Testing to do work that should have been done months earlier.

Before planning the readiness test, confirm that earlier testing has occurred. If it has not, the better next step is lo-fi experimentation or a structured pilot, not a readiness test.

##### Readiness Testing Also Catches Technical Issues Before Launch

Beyond the Go/No Go decision, the readiness test is an opportunity to surface bugs, defects, and configuration failures in a controlled setting before they reach the full market. When participants encounter a broken workflow, a missing integration, or unexpected system behavior, that is signal — not noise.

This is one reason a dedicated technical support person on the test team is not optional. Bugs surface during real customer use in ways that internal QA and staging environments cannot predict. A readiness test with real participants using the product in their actual context will expose failure modes that controlled testing misses.

Log every technical issue that surfaces during the program, triage severity, and track resolution before the Go/No Go call. A test that produces a clean set of found-and-fixed issues alongside quantitative goal results is a stronger foundation for a launch decision than metrics alone.

##### Define Success Before Running the Test

Before the test starts, the PM and team must agree in writing which goals are must-pass and which are aspirational. This pre-commitment prevents post-hoc rationalization: the team cannot look at mixed results and convince themselves the test passed because two out of four goals were met.

A Go/No Go decision is only credible if the criteria were locked before anyone saw results.

##### Three Sections, Three Purposes

- **Test Plan (left side):** who participates, how many, how long the test runs, and who on the team is responsible for what. Each question has a specific structural answer, not a generic placeholder.
- **Goals Table (right side):** four to five rows, each naming a specific objective, the metric used to measure it, and a numeric or percentage target. "Improve satisfaction" is not a goal for this table. "User satisfaction score of 4.2 or above on post-use survey" is.
- **Assumptions and Risks (bottom, full width):** an honest, named list of what the test does not cover and why. This section tells stakeholders where the test has known limits. Leaving it blank implies the test covers everything, which it never does.

##### Who to Test With: Profiles, Not Just Job Titles

Customer profiles for the test should describe real-context participation: role, company type, experience level, and what they represent. "HR manager" is a job title. "HR operations manager at a mid-market company (200-500 employees) with no dedicated HR technology team, responsible for manual payroll and benefits administration" is a profile. The difference matters because the profile determines whether the test is exposing the right failure modes.

##### The Goals Table Requires Numeric Targets

Each row in the Goals table must have a number. The target cell is not a description of the direction of improvement. It is the threshold that defines whether the goal was met. Without a number, the team cannot make a clean Go/No Go call.

Canonical goal categories from the playbook: workload reduction, user satisfaction, self-service adoption rate, system uptime.

##### Assumptions and Risks Documents Scope Limits

Every beta program has constraints: limited training, incomplete integrations, specific user populations that are not representative of the full market, features that are intentionally excluded from the test. Document them explicitly. This protects the team from being held accountable for failures that were known to be outside the test scope, and it signals to stakeholders where follow-up validation is still needed.

##### Quotes Are a Deliverable

The playbook says: "Remember to gather quotes from the test program to use during the official launch." The readiness test is an opportunity to collect memorable user statements that can be used in launch communications, internal presentations, and sales conversations. Designate someone on the test team to capture quotes as the test runs. This is not optional.

##### The Test Team Has Distinct Roles

Three functions matter in a readiness test: the PM (leads the test and owns the Go/No Go call), the account or client contact (manages participant expectations and relationship), and a technical support person (handles bugs and configuration issues as they surface). If no one is assigned to technical support, participants hit problems with no one to triage them, and the test collapses into a support event rather than a learning event.

##### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **critic of the readiness test plan the PM drafted**. It checks that participants are defined by profile, that goals have numeric targets resting on a baseline, that Go/No Go criteria are committed before the test, and that quote capture is planned. The targets and the Go/No Go criteria are the PM's to set.

- **Use it when:** the PM has a draft readiness test plan and wants it pressure-tested before the test starts.
- **Avoid it when:** the request is to set the Go/No Go thresholds, or to predict how participants will react. Even when asked to "just pick numbers," leave each threshold `[PM TO SET]`, name the baseline or evidence that would anchor it, and help structure the criteria (measure, threshold, basis). Even once the PM has baselines, don't offer to propose the numbers: show how each baseline narrows the choice, and leave the number to the PM.
- **Return:** participant profiles sharpened, each goal checked for a measure and a baseline, Go/No Go criteria tested for whether they would really stop a launch, and gaps in quote capture and scope flagged.

##### Working With AI

The Productside Playbook sets one rule for every AI-assisted Play: **the Product Manager does the thinking, and AI pressure-tests it.** In this skill, you are the AI. Hold yourself to these rules:

1. **Pressure-test before you produce.** When the user brings a draft, critique it against the Play's formats and criteria first. Point at the specific words that fail and ask the user to fix them. Offer rewrites only after the critique, as options to accept, adapt, or reject.
2. **Never stand in for the customer.** Do not present jobs, quotes, needs, or pains you generated as research, and do not answer as the persona as if your answers were evidence. Anything you draft about customers is a hypothesis, labeled as one, to validate with real people. Role-play is allowed only as rehearsal where the Play calls for it, labeled as practice, and nothing from it goes into findings.
3. **Never stand in for the team's judgment.** Do not put unsourced figures into the artifact, and do not make calls the team should own. A number without a source is a blank to fill, so mark it that way.
4. **Work the five habits.** *Context:* ask for the persona, market, outcome, and constraints when they are missing. *Guide:* offer competing views and welcome pushback. *Enforce:* work inside the Play's template, not around it. *Outcome:* tie the work to the decision it supports. *Iterate:* go step by step rather than one-shot.
5. **Keep best guess honest.** Best guess mode is allowed. When you use it, label every inferred detail inline and end with **Assumptions to Validate**. A best guess is a starting point to test, never a finding.

For people working in a chat tool without this skill, the Play's copy-paste prompts are in prompts/ (uploaded reference: `07-prompts.md`, section `ps-product-readiness / Companion / README.md`).

##### Guided Mode

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

#### Application

Use template.md (uploaded reference: `05-create.md`, section `ps-product-readiness / Template`) for the scaffold.

See the source play pages in assets/ps_product_readiness_playbook_pages.pdf (source material, not included in this upload kit).

##### Required Output Convention

Default to a **clean, paste-ready artifact**.

That means:

- all four Test Plan questions answered with specific content
- Goals table with 4-5 rows, each including a numeric target
- Go/No Go criteria explicitly named (which goals are must-pass)
- Assumptions and Risks section with 3-5 specific, named scope limits
- Quote capture plan mentioned or integrated into the team roles section
- explanation belongs below the artifact, not inside the fields

##### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in prompts/01-pressure-test-readiness-plan.md (uploaded reference: `07-prompts.md`, section `ps-product-readiness / Companion / 01-pressure-test-readiness-plan.md`) one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

##### Step 1: Tech-Role Bias Guard

Before drafting, confirm who the product actually serves. Beta testers must represent the actual customer population, not internal technical users unless the product is built for technical users.

Common failure: a product for field service technicians, warehouse supervisors, or HR administrators is tested by the engineering team, the QA team, or internal operations staff who are familiar with the product. These users do not expose the failure modes that matter to the real customer: unfamiliar workflows, different mental models, limited training, and domain-specific constraints.

Ask: "Who is the customer who will use or buy this product in the field?" The answer to that question defines who must be in the test. If the answer is not the same as the people currently on the tester list, name the gap.

##### Step 2: Gather Upstream Artifacts

Before drafting the readiness test plan, ask whether the user has:

- Solution hypothesis from ps-solution-hypothesis (defines what is being validated)
- Product success metrics from ps-outcome-tree (provides the measurable targets the test should confirm)
- Risk assessment from ps-risk-assessment (surfaces known risks that may affect the test or its scope limits)
- Persona profiles from ps-proto-persona (helps define who to recruit for the test)

Accept equivalent information from any source. The PM may already know their beta user pool independently. If upstream artifacts are not available, work with what the PM knows and note where assumptions are being made.

##### Step 3: Define Customer Profiles for the Test

Write a specific description of each type of participant in the test. For each profile:

- Name the role and function (not just the job title)
- Describe the company type and size context
- Note the relevant experience level with the problem or prior tools
- Explain what this participant profile represents in the broader market

If the test includes multiple participant types for comparison (for example, paying customers and internal teams as a control group), describe each type separately and explain what the comparison is designed to reveal.

##### Step 4: Determine Participant Count and Structure

State how many participants will be in the test, broken down by type. The breakdown matters: "8 participants" is less useful than "5 operations managers from mid-market companies and 3 enterprise customers for comparison."

If the product serves multiple segments, the participant structure should reflect which segments are being validated. If the test only covers one segment, name that explicitly as a scope limit in the Assumptions and Risks section.

##### Step 5: Set the Test Duration

Define the test duration in terms that reflect meaningful product use, not just calendar time. Two weeks is meaningful if participants use the product every day. Two weeks is meaningless if participants are expected to use the product once for a monthly process.

Anchor duration to one of three things:
- A product usage cycle (one billing cycle, one reporting period, one scheduling cycle)
- A time box with a minimum usage expectation (three weeks, with at least two full use sessions per week)
- A task completion definition (the test ends when participants have completed the onboarding flow, run their first payroll, or submitted their first order)

Calendar days alone are not sufficient.

##### Step 6: Assign Test Team Roles and Responsibilities

Name specific individuals for each function:

- **Test Lead:** the PM or designated person who runs the test, owns the schedule, and holds the Go/No Go call at the end
- **Account/Client Contact:** the person managing participant expectations, handling scheduling, and maintaining the relationship with beta participants
- **Technical Support:** the person who triages bugs, handles configuration issues, and responds to participant technical questions during the test

Each role should be a named person. If a role is unfilled, name it as an open assignment and flag it as a risk before the test begins.

##### Step 7: Write the Goals Table

For each goal row, provide three things:

- **Goal/Objective:** a specific, named outcome the test is designed to confirm. Not "test the product." Examples: "Confirm the system reduces manual data entry time," "Validate that participants can complete the onboarding flow without support assistance."
- **Measure/Metric:** the specific thing being measured. A survey score, a task completion rate, a time-on-task reading, an error count.
- **Target:** the number or percentage that defines success. "4 out of 5 stars or above," "70% task completion without support," "uptime of 99.5% or higher."

Write 4-5 rows. Cover at least three distinct measurement types: workload or efficiency, user satisfaction or experience, adoption behavior, and system reliability.

##### Step 8: Pre-Commit Go/No Go Criteria

After drafting the Goals table, explicitly name which goals are must-pass and which are aspirational. This step must happen before the test runs.

Format:
- Must-pass goals (all must be met for a Go): [list by row name]
- Aspirational goals (failure does not block Go, but is flagged): [list by row name]

If no pre-commitment is made, the team cannot make a clean Go/No Go call when results are mixed.

##### Step 9: Plan for Quote Capture

Designate one person to collect memorable user statements during the test. Brief them before the test starts on what kinds of quotes are useful: spontaneous reactions to the product, statements about specific pain points resolved, comparisons to prior tools or processes.

Quotes captured during the readiness test can be used in launch communications, internal alignment presentations, and sales conversations.

##### Step 10: Document Assumptions and Risks

Write a bulleted list of what is explicitly not being tested in this program and why. Each bullet should name the specific constraint and the reason it is out of scope.

Examples:
- "Limited employee training on the new platform could slow adoption rates; standardized training materials will not be available until post-launch."
- "Data security testing will be conducted post-readiness due to compliance review timelines."
- "Not all integrations will be tested during this phase; only the primary ERP integration is in scope."
- "The test does not include enterprise customers; segment-specific validation is planned for Q3."

Aim for 3-5 bullets. If the list is empty, that is a signal the test scope has not been fully examined, not that the test covers everything.

##### Step 11: Offer Next Steps

After delivering the artifact, offer three options:

1. Run the test and return with results to complete the Go/No Go decision
2. Carry the readiness test goals and outcomes forward into post-launch retrospective planning
3. Review the Assumptions and Risks section with stakeholders to confirm alignment on scope limits before the test begins

#### Examples

See examples/sample.md (uploaded reference: `05-create.md`, section `ps-product-readiness / Examples`).

The example set includes:

- a strong readiness test plan with specific customer profiles, numeric targets, pre-committed Go/No Go criteria, and a named scope limits section
- a weak version with vague profiles, directional goals without numbers, and a blank Assumptions and Risks section
- a drift-bug example showing internal-only testing when the product serves field customers, with commentary on what that systematically misses

#### Common Pitfalls

##### Pitfall 1: Testing with Internal Users Only

**Symptom:** The beta participant list consists of engineers, QA staff, internal operations staff, or other employees who are familiar with the product, when the product serves external customers.

**Consequence:** Internal users do not expose the failure modes that matter to real customers: unfamiliar workflows, different mental models, limited training, domain-specific constraints. The test passes cleanly and the launch fails in the field.

**Fix:** The participant list must represent the actual customer population. If internal users are included for comparison, name them as an internal cohort and do not let them substitute for external customer participants. Name this as a risk in the Assumptions and Risks section if external participants cannot be secured.

##### Pitfall 2: Goals Table Has Directional Aspirations Instead of Numeric Targets

**Symptom:** Goal rows read as "improve efficiency," "increase user satisfaction," or "reduce support volume" with no accompanying number in the Target column.

**Consequence:** The team cannot make a clean Go/No Go call because there is no threshold to cross. Post-test rationalization becomes the only path.

**Fix:** Every Target cell must contain a number or percentage. "Reduce time spent on monthly reconciliation by 30% or more." "User satisfaction score of 4.0 or above on a 5-point scale." If the team cannot agree on a number before the test, that disagreement is itself a problem to resolve before the test begins.

##### Pitfall 3: No Pre-Committed Go/No Go Criteria

**Symptom:** The Goals table is complete, but no one has named which goals are must-pass before seeing results.

**Consequence:** When results are mixed (two goals met, two not), the team debates in real time which goals should have been must-pass. The team that is most motivated to launch wins the argument, not the data.

**Fix:** After writing the Goals table but before running the test, explicitly name which goals are must-pass. Document it. This pre-commitment is the only thing that makes the Go/No Go call credible.

##### Pitfall 4: Assumptions and Risks Section Left Blank

**Symptom:** The Assumptions and Risks section is empty or contains only a vague note like "standard product risks apply."

**Consequence:** Stakeholders believe the test covered all dimensions of readiness. When post-launch issues emerge in areas the test did not cover, the team has no documentation that those areas were out of scope.

**Fix:** Every readiness test has scope limits. Name them. Incomplete integrations, missing training materials, single-segment coverage, deferred security testing: these are real and nameable. Documenting them is not weakness. It is honesty.

##### Pitfall 5: This Is the First Time Users Have Tested the Product

**Symptom:** The readiness test is being planned before any earlier rounds of user testing have occurred: no lo-fi experiments, no prototype walkthroughs, no pilot access.

**Consequence:** The readiness test is carrying the burden of all earlier validation that was never done. It will surface basic usability problems and conceptual mismatches that should have been caught months earlier, making it neither a readiness test nor a meaningful learning event.

**Fix:** Confirm that earlier testing has occurred before planning a readiness test. If it has not, the better path is lo-fi experimentation (ps-lofi-experimentation) or a structured discovery session, not a formal beta program.

##### Pitfall 6: Test Duration Defined Only in Calendar Days

**Symptom:** The test duration says "two weeks" or "one month" with no reference to how many times participants are expected to use the product or what usage cycle the product supports.

**Consequence:** For a product that supports a monthly process, a two-week test means participants may use the product only once or not at all. The test produces no meaningful usage data.

**Fix:** Anchor duration to a product usage cycle ("one full scheduling cycle"), a minimum usage expectation ("three sessions of at least 30 minutes each within the two-week window"), or a task completion definition ("the test ends when participants have completed their first end-to-end workflow"). Calendar time is secondary.

##### Pitfall 7: No One Assigned to Technical Support

**Symptom:** The Test Team Roles section names a test lead and an account contact but has no one assigned to handle bugs, configuration issues, or technical questions during the test.

**Consequence:** When participants encounter a bug or a configuration problem, they wait. The test stalls. Participants disengage. The team gets no signal about product behavior because the test became a support event.

**Fix:** Name a technical support person before the test begins. This person is on call during the test to triage bugs, resolve configuration issues, and provide participant-facing technical help. If no one can be assigned, name it as a risk in the Assumptions and Risks section and describe the contingency.

##### Pitfall 8: Forgetting to Collect Quotes

**Symptom:** The test concludes with quantitative data but no direct participant statements. The launch team has metrics but nothing to say in the voice of the customer.

**Consequence:** A missed opportunity for launch marketing, internal alignment, and sales conversations. Quotes captured during a readiness test carry the weight of real pre-launch customer experience, which is harder to generate after launch.

**Fix:** Designate one person to capture memorable user statements during the test, before it begins. Brief them on what kinds of quotes are useful. Budget time in each participant session to ask open-ended questions that surface quotable responses.

##### Pitfall 9: Thresholds Nobody Chose

**Symptom:** The PM asks for Go/No Go criteria and gets "Go if task success is above 85% and CSAT is above 4.2."

**Consequence:** The thresholds have no baseline and no owner. When results land at 83%, nobody knows whether to stop the launch.

**Fix:** The PM sets each threshold with its basis. The skill asks what baseline it rests on and whether the team would really stop the launch at that number.

#### References

##### Skill Files

- template.md (uploaded reference: `05-create.md`, section `ps-product-readiness / Template`) - working scaffold
- prompts/ (uploaded reference: `07-prompts.md`, section `ps-product-readiness / Companion / README.md`) - copy-paste prompt for chat-based AI tools (authored for this library; the deck has no AI page for this Play)
- examples/sample.md (uploaded reference: `05-create.md`, section `ps-product-readiness / Examples`) - strong, weak, and drift-bug examples

##### Related Skills

- **Upstream:** ps-solution-hypothesis (uploaded reference: `04-discover-define.md`, section `ps-solution-hypothesis / Instructions`) defines what is being validated; ps-outcome-tree (uploaded reference: `02-context.md`, section `ps-outcome-tree / Instructions`) provides the product success metrics that Goals table targets should reflect; ps-risk-assessment (uploaded reference: `04-discover-define.md`, section `ps-risk-assessment / Instructions`) surfaces risks that may define scope limits; ps-proto-persona (uploaded reference: `03-discover-investigate.md`, section `ps-proto-persona / Instructions`) helps define who to recruit for the test
- **Downstream:** Post-launch retrospective; launch communications (uses quotes captured during the test)
- **Related:** ps-lofi-experimentation: if earlier rounds of user testing have not occurred, this skill should precede the readiness test

##### Project Docs

- [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)
- [informative-documents/framework-glossary.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/framework-glossary.md)
- [informative-documents/skill-dependency-map.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/skill-dependency-map.md)

##### Source Material

- assets/ps_product_readiness_playbook_pages.pdf (source material, not included in this upload kit)
- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 98-100: Template 21 of 24 there. No AI page for this Play; the prompts are authored for this library. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).
- [Baseline Playbook version](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml). Full source PDF supplied separately.
- Productside Playbook companion document (supplied separately)

### ps-product-readiness / Template

### Product Readiness Testing

#### When to Use This

Use this template when preparing a **pre-launch beta program** to validate the product with real customers before market release. This is a Key Decision Point: the results determine whether to launch (Go) or hold (No Go).

Before running this template, confirm that earlier rounds of user testing have occurred. This is the final validation before launch, not the first time users see the product.

Upstream artifacts that feed this template:
- Solution hypothesis (ps-solution-hypothesis): defines what is being validated
- Product success metrics from ps-outcome-tree: provides measurement anchors for the Goals table
- Risk assessment (ps-risk-assessment): surfaces known risks that may define scope limits
- Persona profiles (ps-proto-persona): helps define who to recruit as beta participants

---

#### Template

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

#### Usage Guidance

##### Filling the Template

1. Complete **Product Context** to anchor the product, stage, and test lead.
2. Answer all four **Test Plan questions** with specific content before planning the test logistics.
3. Write the **Goals table** before recruiting participants. The goals define what the test is designed to measure.
4. Complete **Pre-Committed Go/No Go Criteria** before the test begins. This is the most commonly skipped step.
5. Fill the **Assumptions and Risks section** before finalizing participant communication.
6. Return to complete the **Post-Test Go/No Go Call** after results are in.

##### What Goes Where

| Section | Contains | Does NOT Contain |
|---------|----------|------------------|
| Customer Profiles | Role + company type + experience level + what they represent | Job titles alone |
| How Many | Total count broken down by participant type | A single total number |
| Test Duration | Usage cycle or task completion anchor | Calendar days alone |
| Test Team Roles | Named individuals with specific functions | "The PM" or "the engineering team" |
| Goal/Objective | Specific named outcome the test confirms | Generic placeholders like "test usability" |
| Target | Number or percentage | Directional aspirations |
| Assumptions and Risks | Specific named scope limits with reasons | Blank or generic acknowledgment |

##### Connecting to Other Skills

- **Upstream:** ps-solution-hypothesis (defines what is being validated), ps-outcome-tree (product success metrics), ps-risk-assessment (known risks), ps-proto-persona (who to recruit)
- **Downstream:** Post-launch retrospective; launch communications (customer quotes)
- **Related:** ps-lofi-experimentation (if earlier rounds of user testing have not occurred, use this skill before planning a readiness test)

##### Capacity Reference

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

### ps-product-readiness / Examples

### Product Readiness Testing Examples

**Scenario for all three examples:** A mid-market field service management platform. The product is a mobile work order system that allows field service technicians (HVAC, plumbing, electrical) to receive job assignments, document completed work, and submit service reports from their phones, replacing a paper-based and dispatcher-phone-call process. The PM has completed earlier rounds of discovery interviews and a clickable prototype test. This is the pre-launch readiness test.

---

#### Strong Example

**Context:** The PM has run two earlier rounds of user testing: a clickable prototype walkthrough with eight technicians and a three-week limited-access pilot with one customer site. This readiness test is the final validation before market release to 20+ customers.

---

##### Product Readiness Test Plan

**Product or initiative:** FieldFlow Mobile Work Order System
**Stage:** Pre-launch beta program
**Date:** July 15, 2026
**Test Lead (PM):** Sonia Oduya

---

###### Section 1: Product Readiness Test Plan

**Who are we testing with (Customer profiles)?**

- Profile 1: Independent HVAC service technicians at small field service companies (5-25 employees), with 5+ years of experience in the trade and no prior experience with digital work order software. These participants represent the early-adopter customer segment where manual process friction is highest.
- Profile 2: Dispatchers at mid-market field service companies (25-100 employees) who currently coordinate job assignments by phone and text. These participants represent the decision-making and adoption influence side of the customer relationship. If dispatchers do not adopt the dispatch-side interface, technician adoption will stall.
- Profile 3 (control): Internal operations staff who have been briefed on the product. Included for comparison only; results from this group do not count toward the Go/No Go decision.

**How many customers will test?**

Total: 14 participants
- Independent HVAC technicians: 8 participants
- Dispatchers at mid-market companies: 4 participants
- Internal operations staff (control): 2 participants

**How long will the test run?**

Duration: 3 weeks
Usage anchor: Each participant completes a minimum of 6 full work order cycles (job assignment, on-site work documentation, service report submission) within the 3-week window. For dispatchers, minimum of 10 job dispatches via the platform.

**Test team roles and responsibilities**

| Role | Name | Responsibility |
|------|------|----------------|
| Test Lead | Sonia Oduya | Runs the test, owns the schedule, holds the Go/No Go call |
| Account/Client Contact | Marcus Delgado | Manages participant expectations, scheduling, and relationships with the 4 partner companies |
| Technical Support | Priya Nair | Triages bugs, handles app configuration issues, responds to participant technical questions |
| Quote Collector | Elena Vasquez | Captures memorable participant statements, records spontaneous reactions during check-in calls |

---

###### Section 2: Product Readiness Goals

| Goal/Objective | Measure/Metric | Target |
|----------------|----------------|--------|
| Confirm work order completion time improves | Average time from job dispatch to submitted service report (logged in app) | 25% reduction vs. baseline paper process (measured in pilot) |
| Validate technician satisfaction with mobile interface | Post-use survey score (5-point scale) administered after 2 weeks | 4.0 or above average across technician participants |
| Confirm self-service onboarding without support | Percentage of participants who complete their first work order without contacting technical support | 80% or higher |
| Validate system uptime under real field conditions | Uptime measured across all participant devices and sessions during the 3-week window | 99.0% or higher |
| Check report completeness (data quality) | Percentage of submitted service reports with all required fields completed without PM prompting | 85% or higher |

**Pre-Committed Go/No Go Criteria**

Must-pass goals (all must be met for a Go decision):
- Confirm work order completion time improves (25% reduction)
- Validate technician satisfaction with mobile interface (4.0 or above)
- Confirm self-service onboarding without support (80% or higher)
- Validate system uptime under real field conditions (99.0% or higher)

Aspirational goals (failure does not block Go, but will be flagged):
- Check report completeness (data quality): 85% or higher; will be addressed in post-launch configuration guidance if not met

---

###### Section 3: Assumptions and Risks

- Dispatcher interface is not being tested in this program. Only 4 dispatcher participants are included, and their results are informational rather than part of the Go/No Go criteria. Dispatch-side readiness will be validated in a separate beta before enterprise account rollout.
- The test does not cover all device types. Participants are using iOS devices only. Android support is in the build plan but not yet fully tested; Android-specific issues may surface post-launch.
- Limited integrations are in scope. Only the QuickBooks Online integration is active during this test. Integration with enterprise accounting systems (SAP, Oracle) is planned for Q4 and is not part of this readiness assessment.
- Training materials are in draft form. Participants are working from an unfinished onboarding guide. Final training content will be complete before general availability. Any adoption issues related to unclear onboarding instructions may improve when finalized materials are released.
- The test population is limited to HVAC technicians. Plumbing and electrical trade participants are in the broader customer target but are not represented in this test. Trade-specific workflow variations may surface post-launch for those segments.

---

##### Why This Works

- **Customer profiles are specific.** Each profile names the role, company size, experience level, and what the profile represents in the market. The control group is clearly separated and explicitly excluded from the Go/No Go decision.
- **Participant count is broken down by type.** The breakdown makes the test structure legible: 8 technicians, 4 dispatchers, 2 internal controls.
- **Duration is anchored to usage, not just calendar time.** "Minimum 6 full work order cycles" prevents the risk of a two-week test where participants only touch the product once.
- **All four test team roles are named.** A Quote Collector is named and briefed. Quotes are treated as a deliverable.
- **Goals table has numeric targets.** Every row has a threshold: 25%, 4.0/5, 80%, 99.0%, 85%. No row says "improve" or "increase" without a number.
- **Go/No Go criteria are pre-committed.** Four must-pass goals are named before the test begins. The fifth is explicitly aspirational. The team cannot rationalize a result after seeing the data.
- **Assumptions and Risks section documents five specific scope limits.** Each one names the constraint, why it is out of scope, and what comes next. A stakeholder reading this section knows exactly what the test does not cover.

---

#### Weak Example

**Context:** Same field service management platform. Different planning attempt.

---

##### Product Readiness Test Plan

**Product or initiative:** Field Service App
**Stage:** Beta
**Date:** July 2026
**Test Lead:** Product team

---

###### Section 1: Product Readiness Test Plan

**Who are we testing with (Customer profiles)?**

- Field service technicians
- Some internal users

**How many customers will test?**

Around 10-12 users.

**How long will the test run?**

Two weeks.

**Test team roles and responsibilities**

The product team will manage the test.

---

###### Section 2: Product Readiness Goals

| Goal/Objective | Measure/Metric | Target |
|----------------|----------------|--------|
| Improve efficiency | User feedback | Positive |
| Increase satisfaction | Survey | Good scores |
| Reduce support calls | Support volume | Lower than before |
| Ensure the app works | Uptime | High |

**Pre-Committed Go/No Go Criteria**

The team will review results and decide.

---

###### Section 3: Assumptions and Risks

N/A

---

##### Why This Fails

**Customer profiles are job titles, not profiles.** "Field service technicians" does not describe company type, experience level, or what the participant represents. The inclusion of "some internal users" with no explanation of who they are or why they are included is a red flag: internal users may not represent the customer failure modes the test needs to expose.

**Participant count is vague and has no breakdown.** "Around 10-12 users" gives no structure. There is no way to know how many of each type will be tested.

**Duration is calendar-only.** "Two weeks" with no usage anchor is meaningless for a product used in job cycles. Two weeks could mean two full work order cycles or zero, depending on how often participants are dispatched during that window.

**Test team roles are not assigned.** "The product team will manage the test" means no one is accountable for technical support, participant relationships, or quote capture. When a participant hits a bug, no one is on call to triage it.

**Goals table has directional aspirations with no numbers.** "Positive," "good scores," "lower than before," and "high" are not targets. The team cannot make a Go/No Go call based on these columns. Post-test rationalization is the only option.

**Pre-committed Go/No Go criteria are absent.** "The team will review results and decide" is the absence of criteria. This is how a failed test gets rationalized into a Go.

**Assumptions and Risks is blank.** "N/A" implies the test covers everything. It does not. No test ever does. The absence of named scope limits does not protect the team. It sets them up to be held accountable for failures outside the test scope.

---

#### Drift-Bug Example

**Named failure: Internal-Only Testing Bug**

**What it looks like:**

The product serves field service technicians who work outdoors, in mechanical equipment rooms, and in basements, often with intermittent connectivity, dirty hands, and limited time to interact with a device. The readiness test participant list consists of:

- 6 engineers from the product team
- 4 QA staff members
- 2 customer success managers

All 12 participants are office-based employees who are familiar with the product, have been briefed on its design intent, and are using it on clean WiFi connections during normal business hours.

**Why it fails:**

Internal participants systematically miss the failure modes that matter to field technicians:

- **Connectivity gaps.** Engineers test on reliable WiFi. Technicians work in basements and equipment rooms where cellular signal drops. The app's offline behavior and sync reliability are never tested.
- **Physical context.** Engineers tap the screen with clean fingers in a quiet office. Technicians are wearing work gloves, working in noisy environments, and looking at the screen in direct sunlight. Touch target sizes, screen contrast, and audio notifications behave differently in those conditions.
- **Mental model mismatch.** Engineers know how the data model works. Technicians do not. Confusion about which field maps to which step in their existing paper process will not surface if the test participants already understand the underlying structure.
- **Motivation gap.** Engineers are running the test because it is their job. Technicians adopt new tools when they are demonstrably faster or easier than the current process. Internal testers do not need to cross the adoption motivation threshold because they were never using the prior process in the first place.
- **Workflow variation.** Field service workflows vary by trade, company size, and dispatch model. Internal participants have been briefed on a single idealized workflow. Real technicians will approach the product from a dozen different starting points, only some of which were anticipated in the design.

**The result:**

The test passes cleanly. The team receives positive feedback from internal participants who found the app intuitive and efficient. The launch proceeds. Within three weeks of general availability, the support queue fills with reports from technicians who cannot submit reports when signal drops, who find the text too small to read on job sites, and who are confused about how their existing paper job forms map to the app's field names.

**The fix:**

The participant list must include actual field service technicians, ideally from customer companies that have agreed to participate in a beta program. If recruiting external participants is difficult, the test should be delayed until they can be secured, or the scope should be explicitly limited to internal validation with a named follow-on test using real customers before broader rollout.

If internal participants are included, they should be labeled as an internal cohort and their results should be used only for comparison and instrumentation purposes. They must not substitute for external customer participants in the Go/No Go criteria.

Document this limitation in the Assumptions and Risks section: "The test participant pool does not include external field technicians. Internal cohort results are used for instrumentation only. Field-condition behavior will be validated in a follow-on customer pilot before enterprise rollout."
