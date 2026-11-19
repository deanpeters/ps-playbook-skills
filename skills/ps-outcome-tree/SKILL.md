---
name: ps-outcome-tree
description: >-
  Connect business outcomes to product outcomes using the Productside Outcome
  Tree. Two modalities - Section One (pre-discovery business context) and
  Section Two (post-discovery actuals vs. planned). Use when you need to
  establish or update the strategic link between what the business is trying to
  achieve and what the product must deliver.
intent: >-
  Help a Product Manager define the business outcome their product supports, the
  business success metrics that track it, 2-5 product outcomes that the customer
  needs to achieve, and the product success and health metrics that measure
  delivery, so the team has a shared, testable link between business strategy
  and product work. Then, after discovery, help the PM update the tree with
  validated outcomes, revised metrics, and actual results.
type: component
blueprint_stage: Context
best_for:
  - "Connecting business outcomes to product outcomes before discovery"
  - "Revisiting the tree after discovery with validated evidence"
  - "Defining product and business success metrics that stay aligned"
scenarios:
  - "I need to connect our business goals to product outcomes before starting customer research"
  - "We finished discovery and I need to update our outcome tree with validated evidence"
---

## Purpose

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

## Key Concepts

### Business Outcomes vs. Product Outcomes

These are two distinct levels. Confusing them is the most common mistake in this play.

**Business Outcome:** What the organization is trying to achieve at a strategic or operational level. It is owned by the business, not by the product team alone.

Example: "Improve new employee onboarding time by 30%"

**Product Outcome:** What the customer or user achieves when the product works well. Product outcomes support the business outcome, but they describe value from the customer's perspective.

Example: "Internal HR managers are focused on strategic initiatives and spend less time doing day-to-day tactical tasks"

The relationship is causal: if the product outcomes are achieved, the business outcome should follow. If that causal link is weak, the tree needs rework.

### Business Success Metrics

Business success metrics measure progress toward the business outcome. They are often lagging indicators owned by leadership or finance.

These may be defined or TBD at the time of building the tree. It is acceptable to leave them as "TBD" initially, but they should not remain blank permanently.

Examples:
- Time-to-productivity for new hires (days)
- Employee satisfaction score during first 90 days
- HR cost per onboarding cycle

### Product Success Metrics

Product success metrics measure whether each product outcome is being achieved. They are leading indicators owned by the product team.

Examples:
- Percentage of onboarding tasks completed without HR intervention
- Average HR manager time spent on tactical onboarding tasks per week
- Number of onboarding-related support tickets per month

### Product Health Metrics

Product health metrics measure the operational health of the product itself, separate from whether it is achieving outcomes.

Examples:
- System uptime percentage
- Average page load time
- Error rate for key workflows
- User adoption rate (active users / total licensed users)

Product health metrics are necessary but not sufficient. A product can be healthy (fast, reliable, available) and still fail to deliver outcomes.

### The 2-5 Product Outcome Limit

The playbook sets a hard limit: no more than 2-5 product objectives. This is not a suggestion. If you have more than 5, you are either splitting too finely or trying to serve too many business outcomes in one tree.

### Cross-References to Other Plays

The Outcome Tree references two other playbook artifacts:

- **Problem Statement** (from the Framing the Problem play): feeds into the tree as context for why the business outcome matters
- **Solution Summary** (from the Solution Hypothesis Statement play): feeds into the tree as a summary of the proposed approach

These are cross-references, not blocking dependencies. You can build the Outcome Tree without having completed those plays, but the tree is stronger when they exist.

### Section One vs. Section Two (Two Modalities, One Skill)

This skill covers both sections of the Outcome Tree as two modalities:

**Section One (Template 03, Context phase):** Build the tree before discovery. Define the business outcome, product outcomes, and metrics framework based on the PM's current understanding of strategy and customer needs.

**Section Two (Deliver phase — reuses the Outcome Tree design; the baseline deck labels this occurrence "Template 3 of 24"; the B2B work-in-progress deck numbers it Template 23):** Update the tree after discovery. Revise product outcomes that discovery validated or invalidated. Fill in metrics that were TBD. Add baselines and targets now that real data exists. Record actuals against planned targets. Retire outcomes that turned out to be wrong.

The trigger for Section Two is evidence: completed empathy interviews, validated hypotheses, experiment results, or post-launch measurement data. If the PM has not done discovery work since building Section One, Section Two will just reproduce the same guesses with more confidence. That is not useful.

### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **critic of the outcome tree the PM drafted**, in both sections. In Section One it checks that the business outcome is measurable, that product outcomes describe what customers achieve, and that metrics are in the right place. In Section Two it asks what discovery evidence supports or contradicts each product outcome. The outcomes, targets, and the verdict on each stay the PM's.

- **Use it when:** the PM has drafted Section One, or has discovery evidence to review in Section Two.
- **Avoid it when:** the request is to invent the business outcome, or to fill in baselines, targets, or actuals without data.
- **Return:** each outcome and metric checked for format and placement, the causal chain from product outcomes to business outcome tested, and in Section Two, each product outcome matched to evidence for the PM to keep, revise, or retire.

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

Use [template.md](template.md) for the full scaffold.

See the original three-page playbook source in [assets/ps_outcome_tree_playbook_pages.pdf](assets/ps_outcome_tree_playbook_pages.pdf).

### Required Output Convention

Default to a **clean, paste-ready structured artifact** with clearly labeled sections.

That means:

- fill all sections (Business Outcome, Business Success Metrics, Product Outcomes, Product Success Metrics, Product Health Metrics)
- produce 2-5 product outcomes that clearly support the business outcome
- keep product outcome statements concise enough for template cells (~15-20 words)
- keep metrics specific and measurable
- explanation belongs below the artifact, not inside the template cells

The artifact comes first. Commentary is secondary.

### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in [prompts/01-check-section-one.md](prompts/01-check-section-one.md) one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

### Step 1: Confirm the Product and Business Context

Before writing anything, answer:

- what product or service are we talking about?
- what business or organization does this product serve?
- who are the customers/users of this product?

**Guard against tech-role bias.** The product outcomes belong to the customer, the person who uses or buys the product in the field. A clinical data platform's product outcomes belong to clinical operations leads and research scientists, not to data engineers or platform architects. Before writing product outcomes, confirm: does this person write code, design systems, or architect solutions as their primary job? If no, the outcomes should not read like a technologist's goals.

### Step 2: Gather Evidence Before Writing

Once you know the product and business context, ask the user for relevant materials before drafting:

- **Strategy documents** such as business plans, annual goals, OKR frameworks, or strategic planning decks
- **Existing metrics** such as current KPIs, dashboards, or performance reports
- **Prior discovery work** such as problem statements, persona artifacts, or JTBD artifacts from other skills

This skill uses **artifacts-only** evidence gathering. The business outcomes and product outcomes should come from the PM's own strategic context, not from web research. Do not offer to run web searches for this skill.

### Step 3: Define the Business Outcome

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

### Step 4: Define Business Success Metrics

For the business outcome, identify 1-3 metrics that the business would use to measure progress.

These metrics should be:

- measurable (a number, percentage, or rate)
- owned by or visible to business leadership
- connected to the business outcome statement

It is acceptable for these to be "TBD" if the user does not have them yet. Note this in the artifact and flag it as a gap to resolve.

### Step 5: Define Product Outcomes (2-5)

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

### Step 6: Define Product Success Metrics

For each product outcome, identify 1-2 metrics that would indicate the outcome is being achieved.

Product success metrics should be:

- leading indicators (they move before the business outcome moves)
- measurable by the product team
- tied to a specific product outcome

If metrics are not yet defined, mark them as "TBD" and note the gap.

### Step 7: Define Product Health Metrics

Identify 2-4 metrics that measure the operational health of the product itself.

Product health metrics are about the product working correctly, not about outcomes being achieved. They include things like:

- uptime and availability
- performance (load times, response times)
- error rates
- adoption and engagement rates

### Step 8: Cross-Reference Problem Statement and Solution Summary

If the user has completed the Framing the Problem play (ps-framing-the-problem), pull in the problem statement as context.

If the user has completed the Solution Hypothesis Statement play (ps-solution-hypothesis), pull in the solution summary.

If neither exists yet, note these as optional inputs that strengthen the tree when available.

### Step 9: Review the Causal Chain

Before finalizing, walk through the logic:

- If Product Outcome 1 is achieved, does it plausibly contribute to the Business Outcome?
- If Product Outcome 2 is achieved, does it plausibly contribute to the Business Outcome?
- Are the product outcomes collectively sufficient to move the business outcome, or are there gaps?
- Are any product outcomes actually business outcomes in disguise?
- Are any product outcomes actually features or solutions?

Flag any weak links for the user to consider.

### Step 10: Offer Next Steps (Section One)

After the Section One artifact is complete, offer the user up to three next-step options:

1. **Build or refine a problem statement** using ps-framing-the-problem, if no problem statement exists yet
2. **Define a solution hypothesis** using ps-solution-hypothesis, to fill in the Solution Summary box
3. **Run Section Two** of this skill after discovery work to update the tree with evidence

Present these as options, not as mandatory steps. The user decides what comes next.

---

### Section Two: Updating the Outcome Tree After Discovery

The following steps apply when the PM returns to the Outcome Tree after completing discovery and define work. Section Two is not a new artifact. It is an update pass on the existing Section One artifact.

### Step 11: Confirm Discovery Evidence Exists

Before running Section Two, verify the PM has new information to work with. Ask:

- What discovery activities have been completed since the tree was built? (empathy interviews, experiments, validation sessions, market research)
- What did discovery reveal that surprised you or contradicted your assumptions?
- Have any product outcomes been validated, invalidated, or changed in priority?

If the PM has no new evidence, Section Two will not add value. Recommend completing discovery work first.

### Step 12: Review Each Product Outcome Against Evidence

Walk through each product outcome from Section One and ask:

- **Validated:** Did discovery confirm this outcome matters to customers? Keep it, sharpen the language if needed.
- **Invalidated:** Did discovery reveal this outcome is not important to customers, or that the causal link to the business outcome is weaker than assumed? Mark it for retirement or revision.
- **New:** Did discovery reveal a product outcome that was missing from Section One? Add it (staying within the 2-5 limit).
- **Revised:** Does the outcome need reframing based on what customers actually said or did?

Update the Product Outcomes table accordingly. Note what changed and why in the Notes section.

### Step 13: Update Metrics with Baselines, Targets, and Actuals

For each metric section (business success, product success, product health):

- Replace "TBD" entries with defined metrics where evidence now exists
- Add **baseline** values (what is the current state before the product intervention?)
- Add or refine **target** values (what does success look like, now that you know more?)
- If post-launch: record **actual** values and note variance from target

Use a consistent format: "Metric Name: baseline X, target Y, actual Z (if available)."

### Step 14: Reassess the Causal Chain

Re-run the causal chain review from Step 9, but with the updated outcomes:

- Do the revised product outcomes still collectively support the business outcome?
- Did discovery reveal gaps in the chain that Section One missed?
- Are the business success metrics still the right ones, or has the business context shifted?

Flag any breaks in the chain for the PM to resolve.

### Step 15: Offer Next Steps (Section Two)

After the Section Two update is complete, offer the user:

1. **Share the updated tree with stakeholders** to align on revised priorities
2. **Update the roadmap** using ps-outcome-roadmap (if available) to reflect revised outcomes
3. **Schedule the next review cycle** to keep the tree current as the product evolves

## Examples

See [examples/sample.md](examples/sample.md).

The example set includes:

- a strong Outcome Tree artifact for a sustainable agriculture platform
- a weak, vague version of the same scenario
- a drift-bug example showing product outcomes confused with business outcomes and internal tasks
- commentary on why the weak versions fail

## Common Pitfalls

### Pitfall 1: Confusing Product Outcomes with Business Outcomes

**Symptom:** Product outcomes read like organizational goals: "Increase market share by 15%" or "Reduce operational costs by $2M."

**Consequence:** The tree conflates two levels. The product team cannot act on business outcomes directly, and the causal link between product work and business results disappears.

**Fix:** Ask: who experiences this outcome? If the answer is "the business" or "leadership," it is a business outcome. If the answer is "the customer using the product," it is a product outcome. Keep them in their respective boxes.

### Pitfall 2: Writing Feature Descriptions as Product Outcomes

**Symptom:** "The product provides a self-service portal" or "Automated notifications for pending tasks."

**Consequence:** The tree describes what the product does instead of what the customer achieves. The team optimizes for shipping features rather than delivering outcomes.

**Fix:** Strip out the product. Ask: what is different for the customer when this feature works? "New employees complete required onboarding steps without waiting for HR availability" is a product outcome. "Self-service onboarding portal" is a feature.

### Pitfall 3: Setting More Than 5 Product Objectives

**Symptom:** The tree lists 7, 8, or 10 product outcomes.

**Consequence:** The team cannot focus. Every sprint touches a different outcome. Progress is diffuse and unmeasurable.

**Fix:** The playbook limit is 2-5 product outcomes per tree. If you have more, either consolidate related outcomes or split into multiple trees for different business outcomes.

### Pitfall 4: Making Business Outcomes Too Vague

**Symptom:** "Grow the business," "Improve customer satisfaction," "Be more innovative."

**Consequence:** The business outcome cannot be measured, so the entire tree has no anchor. The team cannot tell if the product is contributing to business success.

**Fix:** Add a direction, a metric, and a target. "Improve customer satisfaction" becomes "Increase Net Promoter Score from 32 to 50 within 12 months." If the user cannot specify a target, at least specify a direction and a metric.

### Pitfall 5: Defaulting to Tech-Role Language in Product Outcomes

**Symptom:** "Data engineers can build pipelines 40% faster" or "Platform architects can deploy microservices with fewer configuration errors."

**Consequence:** The product outcomes reflect LLM training bias toward technical roles, not the actual customer population.

**Fix:** Before writing product outcomes, confirm who the product actually serves. Most products serve people whose primary job is not writing code. An HR platform serves HR managers and employees, not data engineers.

### Pitfall 6: Treating This as a One-Time Exercise

**Symptom:** The team builds the Outcome Tree once, files it away, and never revisits it.

**Consequence:** The tree becomes stale. Business outcomes shift, product outcomes are achieved or abandoned, and metrics change. The artifact stops reflecting reality.

**Fix:** The playbook says to revisit regularly and bring it to team meetings. Schedule periodic reviews and update the tree as strategy evolves.

### Pitfall 7: Skipping Product Success Metrics

**Symptom:** Product outcomes are defined but their success metrics are left permanently blank.

**Consequence:** The team cannot tell if an outcome is being achieved. Product outcomes without metrics are aspirational statements, not actionable targets.

**Fix:** Even if exact metrics are not known yet, define the type of measurement. "TBD" is acceptable as a starting point, but flag it as a gap that must be resolved before the next planning cycle.

### Pitfall 8: Confusing Product Health Metrics with Product Success Metrics

**Symptom:** "99.9% uptime" listed as a product success metric for an outcome like "HR managers spend less time on tactical tasks."

**Consequence:** The team conflates operational health (is the product working?) with outcome achievement (is the product delivering value?). A product can have perfect uptime and still fail to move outcomes.

**Fix:** Keep them in separate sections. Product health metrics (uptime, latency, error rates) go in the health section. Product success metrics (task completion rates, time savings, adoption of key workflows) go next to their respective outcomes.

### Pitfall 9: AI Writes the Tree

**Symptom:** The PM asks for an outcome tree for their product and gets a complete one: business outcome, five product outcomes, metrics, targets.

**Consequence:** The targets have no baseline, and the outcomes are the model's view of the business. The tree looks like strategy and is a guess.

**Fix:** The PM drafts; the skill checks each outcome and metric. Targets and baselines come from the PM's data or are marked to be set.

## References

### Skill Files

- [template.md](template.md) - working scaffold
- [prompts/](prompts/README.md) - copy-paste prompts for chat-based AI tools (authored for this library; the deck has no AI page for this Play)
- [examples/sample.md](examples/sample.md) - strong, weak, and drift-bug examples

### Related Project Docs

- [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)
- [framework-glossary.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/framework-glossary.md)
- [skill-authoring-workflow.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/skill-authoring-workflow.md)
- [template_conversion_rules.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/template_conversion_rules.md)
- [template_conversion_usage.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/template_conversion_usage.md)

### Related Skills

- [ps-jobs-to-be-done](../ps-jobs-to-be-done/SKILL.md) - product outcomes from JTBD feed into this tree
- [ps-framing-the-problem](../ps-framing-the-problem/SKILL.md) - problem statement feeds the Problem Statement box
- [ps-solution-hypothesis](../ps-solution-hypothesis/SKILL.md) - solution summary feeds the Solution Summary box
- [ps-proto-persona](../ps-proto-persona/SKILL.md) - persona work informs who the product outcomes serve

### Source Material

- [Baseline Playbook version](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml). Full source PDF supplied separately.
- [assets/ps_outcome_tree_playbook_pages.pdf](assets/ps_outcome_tree_playbook_pages.pdf)
- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 11-13 and 106-108: Template 03 and 23 of 24 there. No AI page for this Play; the prompts are authored for this library. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).
- Productside Playbook companion document (supplied separately)
