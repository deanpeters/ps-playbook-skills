---
name: ps-measuring-outcomes
description: >-
  Build a post-launch outcomes dashboard that ties product and business outcomes
  to specific metrics, measurement tools, and baseline data. Use after launch to
  track whether the product is delivering on its promises.
intent: >-
  Help a Product Manager create a living measurement dashboard that tracks both
  Product Success Metrics and Product Health Metrics against the outcomes
  defined in the Outcome Tree. This skill completes the Outcome Tree cycle by
  making outcomes measurable over time, not just aspirationally defined.
type: component
blueprint_stage: Deliver
best_for:
  - "Building a post-launch dashboard that ties outcomes to specific metrics and baselines"
  - "Tracking quarterly and annual progress against the Outcome Tree"
  - "Connecting product analytics to business outcomes for leadership reporting"
scenarios:
  - "We launched last month and I need to build a dashboard that tracks our outcome metrics"
  - "Help me connect our product analytics to the business outcomes in our Outcome Tree"
---

## Purpose

Create a **Productside-style Measuring Outcomes dashboard** from the Product Manager's Outcome Tree and product analytics baseline.

This is a **Deliver phase** skill. It runs after launch, when real data begins to flow. The dashboard ties each outcome from ps-outcome-tree to specific metrics, named measurement tools, and a baseline - then tracks quarterly and annual updates against that baseline.

The point is not to list every possible metric. The point is to build a focused, regularly updated signal system that tells the PM and senior leadership whether the product is delivering on what it promised. The playbook says this belongs in front of the CEO.

This is a living document, not a one-time artifact. A dashboard that is built at launch and never updated has failed at its job.

## Key Concepts

### Success Metrics vs. Health Metrics (Load-Bearing Distinction)

These are different things that belong in different tables. Conflating them is the most common failure mode in this play.

**Product Success Metrics** measure progress toward the specific product outcome. They answer: are customers achieving what the product promised them? Examples: reduction in manual data entry, decrease in process cycle time, increase in first-time resolution rates.

**Product Health Metrics** measure the day-to-day operational health of the product itself. They answer: is the product working well and being used sustainably? Examples: system uptime, error rate, feature usage, detection or processing accuracy, support ticket volume, session duration; satisfaction scores such as NPS and CSAT can serve as guardrails here. (The B2B work-in-progress deck's example uses operational health metrics such as uptime, feature usage, and AI detection accuracy.)

A product can show improving success metrics while health metrics deteriorate - and vice versa. This is the key insight the playbook highlights: a PM might see manual tasks drop 40% while CSAT drops sharply, meaning customers are doing less manually but resenting the new system. The dashboard surfaces these contradictions before they become crises.

### A Success Metric Is a Leading Customer Behavior

A product outcome moves when customers change their behavior. A **product success metric** is a leading indicator: the customer behavior that, when it moves, should pull the business outcome up behind it. Measure the behavior, not just the money that follows.

Three kinds of metric get mistaken for success metrics:

- **Business results** (revenue, churn, margin) are lagging outcomes that point at the business. They belong to the business outcome, not the product success table.
- **Satisfaction or survey scores** are what people *say*. Ask what observable behavior would show the outcome moving. A survey score can back up a behavioral metric, but it shouldn't replace one.
- **Operational plumbing** (uptime, latency, error rate) is a **health** guardrail. Uptime logged as progress is plumbing mistaken for value.

Look for **several** behaviors, not just the obvious one. A metric the skill suggests is a candidate for the PM to judge. And only real data, read by the PM, says whether the outcome was met.

### Why Both Tables Are Required

The two-table structure is not decorative. It creates deliberate tension:

- Success metrics alone miss adoption and quality signals.
- Health metrics alone miss outcome progress.
- Together, they let the PM spot the pattern where one table improves at the expense of the other.

If a PM only tracks one type, they will be blindsided by the other.

### The Dashboard Is an Action Trigger, Not Just a Report

Tracking metrics is only the first step. The dashboard's value is realized when the PM and team respond to what the data shows — not just observe it.

When success metrics are not moving in the expected direction, that is a signal to investigate: Is the product being used as intended? Is the customer behavior assumption correct? Does the product outcome itself need revision?

When health metrics deteriorate while success metrics improve, that is a signal to diagnose the tradeoff before it compounds. Respond quickly to off-track readings. A dashboard that is reviewed quarterly but prompts no action is a filing exercise. The playbook is explicit: track outcomes and respond quickly when the desired progress is not being made.

### Baseline Data Is Required, Not Optional

Without a baseline, a metric is an opinion. The PM cannot know whether change is occurring, how much change has occurred, or in which direction - without knowing the starting point.

Baseline data comes from the PM's product analytics, existing reporting tools, or field measurement before or at launch. If baseline data is not yet available at launch, the first priority is collecting it - not filling in the quarterly updates.

### Measurement Tools Are Named Specifically

"Analytics" is not a measurement tool. Name the actual platform or method: Power BI, Celonis, Qualtrics, Salesforce, Google Analytics, Mixpanel, Amplitude, SQL query from the data warehouse, quarterly user survey. A metric without a named tool is a metric no one will actually collect.

### One Product Outcome Per Dashboard

The template tracks depth, not breadth. Track one product outcome per dashboard. If a PM has multiple product outcomes, they can run multiple dashboards or track the primary outcome here. Tracking five outcomes on one dashboard produces six rows of numbers that tell no coherent story.

### The Dashboard Is Updated Quarterly and Annually

The update columns are not aspirational. Set a calendar cadence at the end of this skill session. If no one owns the quarterly update, the dashboard will not be updated, and the investment in building it is wasted.

### This Builds Directly from the Outcome Tree

The PM should not invent new outcomes for this dashboard. The Business Outcome and Product Outcome fields come verbatim from ps-outcome-tree. If the PM does not have an Outcome Tree, ask for an equivalent statement of what the product is trying to achieve and who benefits.

### How AI Supports This Play

The Playbook casts AI as a **grader of the metrics the PM drafted**. It sorts them, says which track real customer behavior toward the outcome and which are business results, operational plumbing, or a reflexive satisfaction score, then pushes the PM to imagine behaviors worth watching. What AI cannot do is say the outcome was met. That verdict comes from real data, read by the PM.

- **Use it when:** the PM has product outcomes from the Outcome Tree and wants metrics that prove customers are behaving the way the outcome predicts.
- **Avoid it when:** the product outcome is vague or is really a business outcome. AI will hand over confident metrics aimed at the wrong target. Fix the outcome first (Step 1, or ps-outcome-tree).
- **Return:** each metric sorted into success, health, or business; lagging and lazy metrics sent back for a rethink; and customer behaviors that signal the outcome is moving, as candidates for the PM to judge.

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

See the source play pages in [assets/ps_measuring_outcomes_playbook_pages.pdf](assets/ps_measuring_outcomes_playbook_pages.pdf).

### Required Output Convention

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

### Step 1: Tech-Role Bias Guard

Before drafting, confirm the product outcome describes what the **customer** achieves - not what the engineering team shipped.

Ask: "Does this outcome describe what customers do differently, better, or faster after using the product?"

If the answer is "this describes what we built" or "this describes system capabilities," the outcome needs to be reframed before building the dashboard. A dashboard built on engineering outputs will produce metrics that measure team activity, not customer impact.

### Step 2: Gather the Outcome Tree

Ask whether the user has a completed ps-outcome-tree artifact. If yes, pull the Business Outcome and Product Outcome verbatim. If not, ask for:

- What business-level outcome is this product trying to drive? (revenue, cost reduction, efficiency, retention - with a specific target if available)
- What does the customer achieve through using the product? (the product outcome - a change in their behavior, capability, or results)

Do not accept generic answers ("improve efficiency"). Push for specific direction, metric, and context.

### Step 3: Write the Business Outcomes Header

Copy the Business Outcome directly from the Outcome Tree. Do not summarize or reinterpret it. This field shows the causal chain: Business Outcome flows to Product Outcome.

Budget: 15-25 words.

### Step 4: Write the Product Outcome

Copy the Product Outcome directly from the Outcome Tree. If the PM has multiple product outcomes, ask which one this dashboard will track. Track one.

Budget: 15-25 words.

### Step 5: Identify 3-4 Product Success Metrics

**The PM drafts the metrics; the skill grades them** (mirrors [prompts/01](prompts/01-grade-success-metrics.md)). One metric at a time:

1. Ask what customer behavior it captures and how that shows progress toward this specific product outcome.
2. If it's really a business result (revenue, churn), say so. That is a lagging outcome pointing at the business, not a leading product metric.
3. If it's a satisfaction or survey score, push. Ask what observable behavior would show the outcome moving, beyond what people say on a survey.
4. Widen the thinking: what are several different behaviors the PM could measure, not just the obvious one?

Do not choose the metrics or invent numbers. Any metric you suggest is a candidate for the PM to judge. If the PM asks you to propose metrics, or chooses best guess mode, tag them `[AI-SUGGESTED, VALIDATE THIS]`.

Work with the PM to identify what specific, observable changes would indicate the product outcome is being achieved.

For each metric, ask: "If this product outcome is happening, what would we see in the data?"

Name each metric specifically using this pattern: `[Metric Name]: [specific directional target]`. Example: "Reduce Field Report Errors: decrease submission error rate from 12% to under 3%."

Generic names like "Efficiency" or "User Adoption" are not acceptable. Every metric name should tell someone what is being measured and in which direction.

Cover a range of signals if possible - time savings, error reduction, volume changes, completion and adoption behaviors. Use satisfaction scores only to support a behavioral metric, not in place of one.

### Step 6: Identify the Measurement Tool for Each Success Metric

For each success metric, name the actual platform or method used to collect the data. Examples: Power BI dashboard, Salesforce report, quarterly CSAT survey, Mixpanel funnel analysis, SQL query from data warehouse.

If no tool is named, no one will collect the data. If the tool is genuinely unknown, flag it as a prerequisite to establish before launch.

### Step 7: Establish Baseline Data for Each Success Metric

For each success metric, document the current state before or at the point of the product intervention. Examples: "12% error rate as of Q1 2026," "average 4.2 hours per cycle as of March 2026."

If baseline data is not yet available, note what needs to be done to collect it and by when. Do not leave this column blank without a plan. Never fill it with an estimated or invented number; a baseline comes from real data.

Budget: 3-8 words per row (number + unit + timeframe).

### Step 8: Identify 3-4 Product Health Metrics

Shift to operational health signals. Ask: "If the product is working well and being used sustainably, what would we see in day-to-day data?"

Common health metrics: NPS, CSAT score, churn rate, system uptime percentage, error rate, session duration, DAU/MAU ratio, support ticket volume, time to first meaningful action.

These should be clearly different from the success metrics in Step 5. If a health metric and a success metric are measuring the same thing, one of them is misclassified.

### Step 9: Identify Measurement Tool and Baseline for Each Health Metric

Same approach as Steps 6 and 7. Name the tool and document the baseline.

If a health metric like NPS is being collected for the first time, the first quarterly update becomes the de facto baseline - note this.

### Step 10: Review for Metric Tension Patterns

Before presenting the dashboard, review for potential tensions between the two tables:

- Are any success metrics likely to improve in ways that put pressure on health metrics? (e.g., faster throughput could increase error rates)
- Are any health metrics likely to decline if success metrics are pushed aggressively? (e.g., volume increases could strain uptime)

Flag these explicitly. This is the "spot the contradiction" function the playbook calls out. A PM who sees it coming can design for it. A PM who discovers it in Q2 is explaining it to the CEO.

### Step 11: Offer Next Steps

After delivering the artifact, offer three options:

1. Set a quarterly review cadence - name a specific date for the first update and the person responsible for pulling the data
2. Share the dashboard with senior leadership, including the business outcomes header as context
3. Connect this dashboard back to the Outcome Tree - if metrics are consistently off-target by Q2, consider whether the product outcome itself needs to be revised

## Examples

See [examples/sample.md](examples/sample.md).

The example set includes:

- a strong dashboard with clearly distinct success and health metrics, named tools, established baselines, and a metric tension note
- a weak version with generic metric names, no measurement tools, no baseline data, and indistinguishable tables
- a drift-bug example where success metrics have drifted to tracking engineering outputs instead of customer outcomes, with commentary on how to fix it

## Common Pitfalls

### Pitfall 1: Success Metrics and Health Metrics That Are the Same Thing

**Symptom:** Both tables contain similar metrics - user satisfaction appears in both, or process time appears in both under different names.

**Consequence:** The two-table structure provides no useful signal. When one table trends up and the other trends down, the PM cannot tell which is the real story because the metrics are not measuring different dimensions.

**Fix:** Before finalizing, ask: "Do these two tables measure categorically different things?" Success metrics should describe what customers achieve. Health metrics should describe how the product performs operationally. If the two tables could be merged without losing anything, the distinction has not been made.

### Pitfall 2: Generic Metric Names

**Symptom:** Metrics are named "Efficiency," "User Satisfaction," "Adoption," or "Performance."

**Consequence:** These names cannot be tracked, compared quarter to quarter, or presented to leadership with credibility. They measure nothing because they name nothing.

**Fix:** Use the pattern: `[Metric Name]: [specific directional target]`. "Efficiency" becomes "Reduce Cycle Time: decrease average order processing time from 3.2 days to under 1 day." The metric name should tell someone exactly what to measure and what the target is.

### Pitfall 3: No Baseline Data

**Symptom:** The Baseline Data column is blank, marked "TBD," or contains a vague description ("currently high error rates").

**Consequence:** All future quarterly updates are uninterpretable. There is no starting point against which to measure change. After two quarters, the PM cannot tell whether the metric moved, or moved enough, or in the right direction.

**Fix:** Baseline data collection is a prerequisite for the dashboard, not an afterthought. If data is not yet available, identify what needs to be done to collect it before the dashboard is considered active.

### Pitfall 4: Measurement Tool Left Blank or Written as "TBD"

**Symptom:** The Measurement Tool column contains "TBD," "analytics," "to be determined," or is left empty.

**Consequence:** No one will collect the data. A metric with no named tool is aspirational, not operational. At Q1 review, the column will still be blank.

**Fix:** Name the actual tool before the dashboard is shared with leadership. If the tool genuinely does not exist yet, establishing it is a prerequisite for the dashboard - not a follow-on task.

### Pitfall 5: Metrics That Measure Outputs Instead of Outcomes

**Symptom:** Success metrics include things like "Features shipped: 12 per quarter," "API response time: under 200ms," or "Deployments: weekly cadence."

**Consequence:** The dashboard tells the engineering team they are busy, but tells no one - including the PM - whether customers are achieving anything. These are output metrics, not outcome metrics.

**Fix:** Ask "Does this metric change when customers succeed, or does it change when the team ships?" Output metrics change when the team does something. Outcome metrics change when customers achieve something. Keep outcome metrics in the success table. Move output metrics out entirely or into a separate engineering dashboard.

### Pitfall 6: Only Positive Metrics Tracked

**Symptom:** Every metric in both tables is a positive trend signal. There are no early warning indicators for when things go wrong.

**Consequence:** The dashboard cannot distinguish between "everything is fine" and "we have not yet caught the problem." By the time a negative trend is visible in positive-only dashboards, it is usually too late to intervene before a leadership conversation.

**Fix:** Include at least one metric per table that would signal deterioration: error rate, churn, support ticket volume, CSAT decline. These should be in the health metrics table by design.

### Pitfall 7: Dashboard Built Once and Never Updated

**Symptom:** The dashboard is completed at launch, shared with leadership, and then not revisited. The quarterly columns remain blank indefinitely.

**Consequence:** The entire investment in building the dashboard is wasted. A static artifact cannot surface metric tensions, track outcome progress, or inform product decisions.

**Fix:** Before the session ends, name a date for the first quarterly update and the person responsible for pulling the data. Add it to a recurring calendar event. The dashboard is not complete until the update cadence is established.

### Pitfall 8: Too Many Metrics

**Symptom:** The dashboard tracks 10-15 metrics across both tables. Every stakeholder's preferred signal has been included.

**Consequence:** No single metric carries enough weight to drive a decision. The quarterly review becomes a data dump. Leadership cannot identify which signals matter most.

**Fix:** Limit to 3-4 metrics per table, for a total of 6-8 signals. If a metric is not connected to the product outcome or operational health, it does not belong here. Stakeholder-specific metrics belong in stakeholder dashboards, not the outcomes dashboard.

### Pitfall 9: Business Outcomes Disguised as Product Success

**Symptom:** The success table lists "Increase revenue 15%," "Reduce churn to 5%," "Grow ARR."

**Consequence:** These lag. By the time they move, the quarter is over, and they can't tell the team whether customers are behaving the way the product outcome predicts. Customer behavior is never measured.

**Fix:** Keep business results with the business outcome. For each, ask which customer behavior should move first, and measure that.

### Pitfall 10: Health Metrics Posing as Success

**Symptom:** "99.9% uptime" or "API latency under 200ms" sits in the success table.

**Consequence:** Plumbing is mistaken for value. The product can run perfectly while customers' behavior never changes.

**Fix:** Move operational guardrails to the health table. Success metrics are customer behaviors that lead the outcome.

### Pitfall 11: AI Picks the Metrics

**Symptom:** The PM asks "what should we measure?" and adopts the list. The metrics sound right, but no one on the team chose them or knows how they'd be collected.

**Consequence:** Nobody owns the metrics, and the dashboard tracks the model's idea of the outcome rather than the team's.

**Fix:** The PM drafts; the skill grades each metric and widens the options. Suggested metrics are candidates the PM accepts or rejects.

## References

### Skill Files

- [template.md](template.md) - outcomes dashboard scaffold
- [prompts/](prompts/README.md) - copy-paste prompt for chat-based AI tools (1: grade your success metrics)
- [examples/sample.md](examples/sample.md) - strong, weak, and drift-bug examples

### Related Skills

- **Upstream:** [ps-outcome-tree](../ps-outcome-tree/SKILL.md) - Business Outcomes and Product Outcome fields come from here; do not invent new outcomes for this dashboard
- **Downstream:** this is a Deliver-phase endpoint; no skills currently feed from it

### Project Docs

- [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)
- [informative-documents/framework-glossary.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/framework-glossary.md)
- [informative-documents/skill-dependency-map.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/skill-dependency-map.md)

### Source Material

- [assets/ps_measuring_outcomes_playbook_pages.pdf](assets/ps_measuring_outcomes_playbook_pages.pdf)
- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 101-105: Template 22 of 24 there, with the AI overview on slide 103 and prompt on slide 104. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).
- [Baseline Playbook version](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml). Full source PDF supplied separately.
- Productside Playbook companion document (supplied separately)
