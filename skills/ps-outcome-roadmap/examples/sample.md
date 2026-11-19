# Outcome-Based Roadmap and Release Plan Examples

All three examples use a **field service operations** scenario: a SaaS product for utilities and industrial maintenance organizations, helping field technicians diagnose equipment faults and dispatch replacement parts without returning to the depot.

---

## Example 1 - Strong

**Context:** The PM has completed the Outcome Tree, Output Prioritization, and two rounds of Tiny Acts of Discovery with field technicians and dispatch coordinators. The product is in the Create phase. The team is preparing a roadmap to share with operations leadership and the engineering team.

---

### Outcome-Based Roadmap and Release Plan

**Product or initiative:** FieldResolve - equipment fault diagnosis and parts dispatch platform
**Date:** June 26, 2026
**Team:** Priya Sharma (PM), Marcus Webb (Engineering Lead), Dana Okonkwo (Dispatch Ops Lead)

---

**Business Outcomes**

Reduce unplanned equipment downtime by 30% across field service regions within 12 months, enabling regional operations teams to meet SLA commitments without emergency dispatch costs.

---

**Roadmap**

### NOW - High Confidence
**Product Outcomes to Pursue**

- Field technicians identify the root cause of electrical faults on-site without calling the depot, completing diagnosis in under 20 minutes.
- Dispatch coordinators confirm parts availability and initiate orders during the technician's on-site window, avoiding a second site visit.

### NEXT - Medium Confidence
**Product Outcomes to Validate**

- Regional operations managers see real-time fault resolution status across all active jobs without requiring phone-based status checks from coordinators.
- Field technicians self-assign to nearby jobs without dispatcher involvement when their primary job closes ahead of schedule.

### LATER - Low Confidence
**Product Outcome Hypotheses**

- Technicians could reduce repeat fault rates by accessing structured repair history for specific equipment models at the point of diagnosis.
- Preventive maintenance schedulers could reduce emergency dispatch volume by acting on predictive signals from resolved fault patterns before equipment failures occur.

---

**Release Plan**

### NOW
**Outputs to Develop**

- On-site fault diagnosis guided workflow (mobile, offline-capable)
- Parts availability real-time lookup with depot inventory integration
- One-tap parts order initiation from the fault diagnosis screen

**Tiny Acts of Discovery**

- 6-person walkthrough with field technicians using a paper prototype of the fault diagnosis workflow to confirm the decision tree covers their most common fault types (running this week; Priya coordinating with Dana)
- Pull 90 days of dispatch logs to confirm whether parts availability checks happen before or after the technician leaves the site (data pull; Marcus assigned)

---

### NEXT
**Output Concepts to Validate**

- Regional job status dashboard (live map view for coordinators and ops managers)
- Technician self-scheduling interface for surplus capacity after job close

**Assumptions to Validate**

- We believe dispatch coordinators will use a live job status dashboard to replace their current phone check-in process, because they have described phone interruptions as their primary workload bottleneck.
- We believe field technicians will accept self-assignment to nearby jobs when their primary job closes early, because interviews suggest they prefer staying in the field over returning to the depot when capacity allows.
- We believe ops managers will act on real-time status dashboards to make coverage decisions without waiting for end-of-day coordinator reports.

---

### LATER
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

### Why This Works

**Outcome language is preserved in the roadmap row.** Every item in the Now, Next, and Later roadmap sections describes what a field technician, coordinator, or ops manager achieves - not what the product does. "Field technicians identify the root cause of electrical faults on-site" is an outcome. "On-site fault diagnosis guided workflow" is an output - correctly placed in the release plan row.

**Output language is preserved in the release plan row.** The three Now outputs are specific, buildable deliverables. None of them are customer outcome statements. Engineering can write a sprint from these.

**Discovery is active, not future.** The two Tiny Acts are running now - one this week - not scheduled as a phase after Now outputs ship. The Assumptions to Validate connect directly to the Next output concepts. The Assumptions to Research connect to the Later hypotheses.

**Every Now output traces to a Now outcome.** The fault diagnosis workflow drives "field technicians identify root cause without calling the depot." The parts lookup and order initiation drive "dispatch coordinators confirm availability and initiate orders during the site window." No output is floating without an outcome anchor.

**Business Outcomes anchor the whole structure.** The 30% downtime reduction target is specific and measurable. Every product outcome below it can be evaluated for whether it plausibly contributes to that goal.

---

## Example 2 - Weak

**Context:** Same scenario, same team. The roadmap was built quickly to meet a planning deadline, without reviewing Outcome Tree results or checking whether the discovery sections were complete.

---

### Outcome-Based Roadmap and Release Plan

**Product or initiative:** FieldResolve
**Date:** June 26, 2026
**Team:** Priya, Marcus, Dana

---

**Business Outcomes**

Improve field service efficiency and reduce costs.

---

**Roadmap**

### NOW - High Confidence
**Product Outcomes to Pursue**

- Launch mobile fault diagnosis app
- Build parts inventory lookup
- Add one-tap order button
- Create coordinator dashboard
- Enable technician self-scheduling
- Add repair history search

### NEXT - Medium Confidence
**Product Outcomes to Validate**

- Performance optimization
- Additional integrations

### LATER - Low Confidence
**Product Outcome Hypotheses**

- Future enhancements based on feedback

---

**Release Plan**

### NOW
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

### NEXT
**Output Concepts to Validate**

- Performance optimization
- Additional integrations

**Assumptions to Validate**

[TBD]

---

### LATER
**Assumptions to Research**

[TBD]

---

### Why This Fails

**The roadmap row is full of outputs, not outcomes.** "Launch mobile fault diagnosis app," "build parts inventory lookup," and "add one-tap order button" are all outputs - things the team builds. They describe the product, not what customers achieve. An executive reading this roadmap cannot evaluate whether the team is solving the right customer problem. They see a feature list.

**Everything is in Now with no confidence differentiation.** Six items in the Now roadmap, two vague placeholders in Next, and a single line in Later. This does not reflect genuine confidence assessment - it reflects the team not doing the work of sorting by evidence. There is no signal about what is validated versus what is directional.

**Discovery sections are empty.** "None planned - will evaluate after launch" is the most dangerous phrase in a roadmap. It treats discovery as something that happens after shipping, not alongside it. The team has committed to building six outputs without any active learning about whether customers will use them.

**Business Outcomes is too vague to anchor anything.** "Improve field service efficiency and reduce costs" describes a direction, not a goal. There is no metric, no target, no timeframe. Nothing below it can be evaluated for whether it contributes to this goal, because the goal is too general to fail.

**The roadmap and release plan contain identical content.** When both rows say the same things, the two-layer structure has not been used. The outcome language and output language have not been separated. The artifact communicates nothing to executives that it does not also say to engineering - and it fails both audiences because it mixes the languages.

---

## Example 3 - Drift Bug: Business/Financial Language in the Roadmap Row

**Context:** Same scenario. The PM has strong financial instincts and is accustomed to communicating with executives in business metric terms. The roadmap outcomes have been written to speak to a CFO review, not to describe what customers achieve.

---

### Outcome-Based Roadmap and Release Plan

**Product or initiative:** FieldResolve
**Date:** June 26, 2026
**Team:** Priya, Marcus, Dana

---

**Business Outcomes**

Achieve 30% reduction in unplanned downtime costs and a 15% improvement in field workforce utilization by end of fiscal year.

---

**Roadmap**

### NOW - High Confidence
**Product Outcomes to Pursue**

- Reduce emergency dispatch costs by $2M annually through faster on-site resolution
- Decrease parts logistics spend by 20% through inventory visibility at the point of service

### NEXT - Medium Confidence
**Product Outcomes to Validate**

- Increase field technician utilization rate from 68% to 78%
- Reduce coordinator overhead by 0.5 FTE through workflow automation

### LATER - Low Confidence
**Product Outcome Hypotheses**

- Predictive maintenance data could reduce total failure incidents 15% year-over-year

---

*[Release plan below is well-formed - not repeated here for brevity.]*

---

### Why This Fails - and How to Fix It

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
