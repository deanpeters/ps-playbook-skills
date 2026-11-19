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

### Usage Notes

- Upstream dependency: ps-outcome-tree (Business Outcome and Product Outcome fields)
- Deliver-phase endpoint: no skills currently feed downstream from this one
- One product outcome per dashboard; multiple dashboards for multiple outcomes
- The two-table structure (Product Success Metrics / Product Health Metrics) is load-bearing - do not conflate the tables
- Baseline data is required before the dashboard is considered active

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

Tracking metrics is only the first step. The dashboard's value is realized when the PM and team respond to what the data shows  -  not just observe it.

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

## Template

**Template 22 of 24 | Phase: Deliver | Type: Component**

---

### Header: Business Outcomes and Product Outcome

**Business Outcomes**

> _Copy the Business Outcome verbatim from your Outcome Tree. This is the business-level goal your product is intended to drive - a specific, measurable direction at the organizational level. Budget: 15-25 words._

[Business Outcome from ps-outcome-tree]

**Quality check:** Does this describe a business-level result (revenue, cost, efficiency, retention) with a measurable direction? If it describes what the product does rather than what the business achieves, revise before proceeding.

---

**Product Outcome**

> _Copy the Product Outcome verbatim from your Outcome Tree. This is what the customer achieves through using the product - the specific change in their behavior, capability, or results. Track one product outcome per dashboard. Budget: 15-25 words._

[Product Outcome from ps-outcome-tree]

**Quality check:** Does this describe what the customer achieves, not what the engineering team shipped? If the subject of this sentence is your product or your team rather than your customer, it needs to be reframed.

---

### Section 1: Product Success Metrics

Product Success Metrics measure progress toward the specific product outcome above. Each metric answers: are customers achieving what the product promised them?

| Product Success Metric | Measurement Tool | Baseline Data | Quarterly Update 1 | Quarterly Update 2 | Quarterly Update 3 | Annual Update |
|---|---|---|---|---|---|---|
| _[Metric Name: specific directional target. Example: "Reduce Manual Tasks: decrease manual data entry by 40%". Budget: 8-15 words.]_ | _[Name the actual platform or method - Power BI, Celonis, Qualtrics, Salesforce. Not "analytics" or "TBD". Budget: 2-5 words.]_ | _[Current state before or at launch - number, unit, timeframe. Example: "3.2 days average as of Q1 2026". Budget: 3-8 words.]_ | _[Fill post-launch]_ | _[Fill post-launch]_ | _[Fill post-launch]_ | _[Fill post-launch]_ |
| _[Second success metric. Name specifically - what is being measured and in what direction. Budget: 8-15 words.]_ | _[Measurement tool name. Budget: 2-5 words.]_ | _[Baseline number, unit, timeframe. Budget: 3-8 words.]_ | | | | |
| _[Third success metric. Cover a different dimension than rows 1 and 2 - time savings, error reduction, volume changes, or quality. Budget: 8-15 words.]_ | _[Measurement tool name. Budget: 2-5 words.]_ | _[Baseline number, unit, timeframe. Budget: 3-8 words.]_ | | | | |
| _[Optional fourth success metric. Include only if it adds a dimension not covered above. Budget: 8-15 words.]_ | _[Measurement tool name. Budget: 2-5 words.]_ | _[Baseline number, unit, timeframe. Budget: 3-8 words.]_ | | | | |

> **Quality check:** Every metric in this table should change when customers succeed - not when the team ships. If a metric would improve regardless of whether customers are achieving the product outcome, it belongs in the health metrics table or should be removed. Every Measurement Tool cell must name a real tool, not "TBD." Every Baseline Data cell must have a number or a concrete plan to collect one.

---

### Section 2: Product Health Metrics

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

### Metric Tension Review

Before sharing this dashboard, check for patterns where improving one metric could put pressure on another:

- Are any success metrics likely to improve in ways that strain health metrics? (Example: pushing volume throughput could increase error rates)
- Are any health metrics likely to decline if success metrics are pushed aggressively? (Example: accelerating onboarding pace could lower CSAT)

_[Note any tensions observed between your two tables. If none are apparent at launch, flag this as something to watch in Q1. A dashboard that never surfaces tension either has no tension to surface, or is not being read carefully enough.]_

---

### Update Cadence

First quarterly update due: [date]

Owner responsible for pulling data: [name and role]

This dashboard is shared with: [audience - including leadership level]

## Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For utility field maintenance, track customer repair turnaround as a success metric and service reliability as a distinct health metric; identify baselines and measurement tools.
- **Weak:** "Customers are happier" cannot be tracked consistently without a defined measure.
- **Drift to avoid:** Outputs as outcomes: number of features shipped does not show whether technicians resolve faults more effectively.


## Common Pitfalls

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

## References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-measuring-outcomes) for supporting source material and expanded examples.
