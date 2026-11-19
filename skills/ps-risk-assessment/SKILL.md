---
name: ps-risk-assessment
description: >-
  Identify, prioritize, and plan for product risks in Productside format. Use
  when you need to surface potential threats to product success, classify them
  by severity and likelihood, and build mitigation and contingency plans before
  committing to a build or launch.
intent: >-
  Help a Product Manager and their team proactively surface and manage the risks
  that threaten a product's development and adoption, so that costly surprises
  are predictable checkpoints rather than emergencies.
type: component
blueprint_stage: Discover + Define
best_for:
  - "Identifying potential threats to a product build or launch with your team"
  - "Classifying risks by severity and likelihood on a heat map"
  - "Building specific mitigation and contingency plans for high-priority risks"
scenarios:
  - "We are about to enter development and I need the team to identify what could go wrong"
  - "Help me run a risk assessment session and build mitigation plans for the top threats"
---

## Purpose

Create a **Productside-style Risk Assessment artifact** from a collaborative team review of a product in development.

This skill helps a Product Manager and their project manager identify potential threats to a product build or launch, classify those threats by severity and likelihood, and build specific mitigation and contingency plans for the highest-priority risks.

The point is not to list everything that could go wrong. The point is to help the team complete the play with a prioritized, actionable risk plan.

## Key Concepts

### This Play Is Collaborative, Not Solo

The playbook is explicit: do not run this assessment alone. Partner with your project manager, who can lead the collaborative effort, and involve relevant stakeholders. A solo PM risk list misses organizational, technical, and customer-facing blind spots that surface in a group session.

### Mitigation and Contingency Are Not the Same

Every risk needs two plans, not one:

- **Mitigation Tactics**: what the team does to reduce the chance the risk occurs. These are proactive actions taken before the risk materializes.
- **Contingency Plans**: what the team does if the risk occurs despite mitigation. These are reactive responses to the risk having already happened.

A plan where both columns contain the same kind of content has not done the work.

### Risk Breadth Matters More Than Risk Count

Six risks that are all technical is not a complete assessment. A well-formed risk list covers:

- Customer adoption and behavior change
- Technical implementation and integration
- Organizational readiness and change management
- Market or competitive timing
- Data, privacy, or compliance
- Resource or capacity constraints

### Point of Contact Is the Risk Owner, Not the Task Doer

The Point of Contact is the person accountable for monitoring and managing the risk. This is not necessarily the PM or the person completing the assessment. For adoption risks it may be a change management lead. For technical risks it may be an engineering lead. For compliance risks it may be a legal or security owner.

### Six Is the Canonical Count

The template has six rows in the identification table. Fill all six. Fewer usually means the team has not looked broadly enough.

### Risk Assessment Is a Living Document

The assessment is not a one-time checkpoint. Risks change as the product is built, tested, and launched. At minimum, revisit at the first major build decision.

### Template Capacity Matters

Risk names, mitigation tactics, and contingency plans should be paste-ready for the playbook template. Keep entries specific but compact.

See [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml) for canonical field budgets.

### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **a widening and pressure-testing partner for the risks the PM's team brainstormed**. It asks whether the list covers enough ground, offers risk categories (and, after the PM answers, candidate risks marked as candidates), and checks that each mitigation, contingency, and owner is real. Severity, likelihood, and the plan stay with the team.

- **Use it when:** the team has brainstormed risks and wants the list widened and the management plan pressure-tested.
- **Avoid it when:** the request is for a finished risk register for a product the team hasn't discussed. The risks that matter are the ones only the team can see.
- **Return:** gaps in breadth named, candidate risks offered as candidates, each mitigation separated from its contingency, and each risk given a real owner.

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

See the source play pages in [assets/ps_risk_assessment_playbook_pages.pdf](assets/ps_risk_assessment_playbook_pages.pdf).

### Required Output Convention

Default to a **clean, paste-ready artifact**.

That means:

- exactly 6 risks in the identification table
- all three sections completed
- Risk Management rows for at least the 2-3 highest-priority risks
- mitigation and contingency clearly distinct in every row
- no generic risk names like "Technical Risk" or "Market Concerns"
- explanation belongs below the artifact, not inside the fields

### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in [prompts/01-widen-and-test-risks.md](prompts/01-widen-and-test-risks.md) one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

### Step 1: Apply Tech-Role Bias Guard

Before starting, ask: is the product being evaluated built for a technical or engineering user? If yes, note it and proceed. If not, flag it as you work - risk lists generated for non-technical customer contexts often cluster around implementation concerns (performance, integration, security) because those are the risks the product team lives with, not the risks the customer faces.

This is especially important for risks in the customer adoption and change management categories. The team running this assessment is not the customer. Risks should span customer-facing failure modes, not just build-side concerns.

### Step 2: Confirm Scope Beyond Technical Risks

Before brainstorming risks, ask the user to consider whether their current thinking is skewed toward engineering concerns. Product teams commonly produce risk lists that are almost entirely technical (performance, integration, security) while missing the risks that most often cause product failures: customer behavior change, organizational resistance, market timing, and adoption barriers.

Prompt the user to think across these categories:

- What adoption or behavior-change risks exist?
- What organizational or change management risks exist?
- What technical or integration risks exist?
- What market or competitive timing risks exist?
- What data, privacy, or compliance risks exist?
- What resource or capacity risks exist?

### Step 3: Collect Available Artifacts

Before drafting, ask whether the user has materials to share:

- Solution hypothesis from ps-solution-hypothesis (defines what is being de-risked)
- Problem framing from ps-framing-the-problem (gives customer and problem context)
- Any early customer feedback or field observations
- Stakeholder concerns surfaced in prior conversations
- A Stakeholder Alignment artifact (useful for identifying Points of Contact)

The more context about what is being built and for whom, the more targeted the risk identification. Also confirm who will participate in the risk review session.

### Step 4: Identify Six Risks

Work with the user to identify exactly six risks. For each, capture:

**Risk Name**: a short label that names the type of risk and the specific concern. Follow the pattern: `[Risk Type]: [Specific Concern]`. Example: "Workflow Disruption: surgeons resist new documentation steps."

**Risk Raised By**: the team member or stakeholder who surfaced this risk during the session.

Spread the six risks across at least three distinct categories. Do not let all six cluster in one area.

### Step 5: Plot Level of Risk

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

### Step 6: Build the Risk Management Table

For each Critical or Monitor priority risk, and optionally for Manage-priority risks, complete the risk management table:

- **Risk Name**: match exactly the name from Step 3
- **Mitigation Tactics**: specific actions that reduce the chance the risk occurs. Not "test more" or "communicate better." What specifically will the team do, when, and with whom?
- **Contingency Plans**: specific response if the risk occurs despite mitigation. What will the team do? Who decides? What is the timeline?
- **Point of Contact**: the named accountable owner for this risk. If no one can be named, that is a signal the risk is unowned.
- **Notes**: timing dependencies, escalation paths, or open questions

At minimum, complete rows for all Critical-priority risks. Leave Accept-priority risks out if needed to keep the artifact focused.

### Step 7: Review the Completed Artifact

Before presenting the artifact, check:

- Do higher-priority risks have stronger, more specific plans than lower-priority ones?
- Is every Contingency Plan clearly different from its paired Mitigation Tactic?
- Is every Point of Contact a named individual, not a team or function?
- Are there risks that are actually testable assumptions? If so, flag them as candidates for ps-lofi-experimentation.
- Are priorities meaningfully differentiated? If everything is Critical, the classification has not done its job.

### Step 8: Flag the Assessment as a Living Document

After delivering the artifact, note that this assessment should be revisited at key decision points. At minimum, flag one specific time to revisit: at the first major build or delivery decision.

### Step 9: Offer Next Steps

At the end of the artifact, offer three options:

1. Convert the most critical testable assumption into a lo-fi experiment using ps-lofi-experimentation
2. Carry the risk summary forward into ps-product-outcome-canvas when that play is run
3. Share the assessment with stakeholders identified in the Risk Raised By column to validate completeness and confirm Points of Contact

## Examples

See [examples/sample.md](examples/sample.md).

The example set includes:

- a strong Productside-style risk assessment with clear prioritization and distinct mitigation and contingency plans
- a weak version with generic risk names, uniform High/High ratings, and no real distinction between mitigation and contingency
- a drift-bug example with commentary on the mitigation-contingency swap failure and how to fix it

## Common Pitfalls

### Pitfall 1: All Technical Risks, No Adoption Risks

**Symptom:** The risk list contains only engineering concerns: performance degradation, API failures, integration complexity.

**Consequence:** The team ships a technically sound product that fails in the market because adoption risks were never surfaced or planned for.

**Fix:** Before finalizing the list, explicitly ask: what are the customer behavior change risks? What are the organizational readiness risks? What could cause the product to be technically correct but commercially unsuccessful?

### Pitfall 2: Confusing Mitigation with Contingency

**Symptom:** The Mitigation Tactics and Contingency Plans columns contain the same type of content, usually responses to the risk having already occurred.

**Consequence:** The team has a reactive plan but no proactive plan. When the risk materializes, the "mitigation" was never executed because it was actually a contingency.

**Fix:** Mitigation happens before the risk occurs and reduces the chance it will. Contingency happens after the risk occurs and limits the damage. Both are required.

### Pitfall 3: Point of Contact as a Role, Not a Person

**Symptom:** The Point of Contact column contains entries like "IT Team," "Product Management," or "Stakeholders."

**Consequence:** No one is actually accountable. When the risk materializes, everyone assumes someone else owns it.

**Fix:** Name a specific individual. If you cannot name one, that is a signal that the risk is unowned and needs an owner before the assessment is complete.

### Pitfall 4: Risk Names That Are Categories, Not Concerns

**Symptom:** Risk names read as: "Technical Risk," "Market Risk," "User Adoption Risk."

**Consequence:** The risk is too abstract to assess, plan for, or communicate to stakeholders.

**Fix:** Follow the pattern: `[Risk Type]: [Specific Concern]`. "Market Risk" becomes "Competitive Timing: new entrant launches similar feature before our release."

### Pitfall 5: Completing Risk Management Only for Easy Risks

**Symptom:** The Risk Management table is fully completed for low-priority risks and left sparse for Critical ones.

**Consequence:** The highest-stakes risks have the weakest plans.

**Fix:** Start the Risk Management table with the Critical-priority risks. If time is limited, leave Accept-priority risks without management rows rather than leaving Critical ones blank.

### Pitfall 6: Treating the Assessment as a One-Time Artifact

**Symptom:** The risk assessment is completed at project kickoff and never revisited.

**Consequence:** Risks that have increased in probability or severity go unmanaged. New risks that emerged during development are invisible.

**Fix:** Mark at least one specific future date or decision point where the assessment will be reviewed and updated.

### Pitfall 7: Inflating Everything to High Severity

**Symptom:** Every risk is rated High Impact and High Probability. Everything is Critical.

**Consequence:** Prioritization is impossible. The team cannot distinguish between risks that demand immediate action and risks worth acknowledging but not investing in heavily.

**Fix:** Push the team to differentiate. If more than three risks are truly Critical, the team needs to re-examine whether the ratings reflect business impact or anxiety. Not every risk deserves equal attention.

### Pitfall 8: Running the Assessment Alone

**Symptom:** The PM completes the risk assessment without the project manager or relevant stakeholders.

**Consequence:** Organizational, operational, and customer-facing blind spots remain invisible. The resulting plan lacks the breadth to be credible or actionable.

**Fix:** Run this as a collaborative session. The project manager leads the facilitation. Stakeholders surface risks the PM team would not see from inside the product team.

### Pitfall 9: A Risk List the Team Never Discussed

**Symptom:** The PM asks the agent for six risks and gets a tidy, plausible list with severity, likelihood, and mitigations filled in.

**Consequence:** The list covers generic risks and misses the ones only the team knows. Nobody owns the mitigations, because nobody chose them.

**Fix:** The team brainstorms first. The skill widens the list with categories and candidates, and the team places and owns each risk.

## References

### Skill Files

- [template.md](template.md) - working scaffold
- [prompts/](prompts/README.md) - copy-paste prompt for chat-based AI tools (authored for this library; the deck has no AI page for this Play)
- [examples/sample.md](examples/sample.md) - strong, weak, and drift-bug examples

### Related Skills

- **Upstream:** [ps-solution-hypothesis](../ps-solution-hypothesis/SKILL.md) defines what is being de-risked; [ps-framing-the-problem](../ps-framing-the-problem/SKILL.md) provides customer and problem context
- **Downstream:** ps-product-outcome-canvas (Batch 5): the Risk field draws from this skill's output
- **Related:** ps-lofi-experimentation: high-priority testable assumptions from this assessment may become lo-fi experiments

### Project Docs

- [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)
- [informative-documents/framework-glossary.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/framework-glossary.md)
- [informative-documents/skill-dependency-map.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/skill-dependency-map.md)

### Source Material

- [assets/ps_risk_assessment_playbook_pages.pdf](assets/ps_risk_assessment_playbook_pages.pdf)
- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 72-74: Template 15 of 24 there. No AI page for this Play; the prompts are authored for this library. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).
- [Baseline Playbook version](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml). Full source PDF supplied separately.
- Productside Playbook companion document (supplied separately)
