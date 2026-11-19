# Jobs-to-Be-Done & Outcomes - Examples

## Example 1: Strong Productside-Style JTBD Artifact

Scenario: A logistics technology company building a warehouse labor coordination platform for regional distribution center operations managers.

```markdown
# Jobs-to-Be-Done & Outcomes

## Product Context

- Product or service: ShiftSync - warehouse labor coordination platform
- Target market segment: Regional distribution center operations
- Primary user persona: Regional Operations Planner
- Buyer persona (if different): VP of Distribution

## 1. Job Statements & Personas

| # | Type | Job Statement | Persona |
|---|------|---------------|---------|
| 1 | F | Reconcile shift schedules across three warehouse sites | Regional Operations Planner |
| 2 | F | Rebalance labor allocation when demand spikes unexpectedly | Regional Operations Planner |
| 3 | F | Track dock-door utilization against carrier arrival windows | Dock Supervisor |
| 4 | F | Report weekly labor cost variances to regional leadership | Regional Operations Planner |
| 5 | E | Feel in control when managing schedule changes across multiple sites | Regional Operations Planner |
| 6 | E | Feel confident that staffing gaps will not cause missed shipments | Dock Supervisor |
| 7 | S | Be seen as the person who keeps operations running smoothly by site GMs | Regional Operations Planner |

## 2. Product Outcomes

| # | Product Outcome & Context | Related Job(s) |
|---|--------------------------|-----------------|
| 1 | Reduce time spent reconciling schedules across warehouse sites | 1 |
| 2 | Reduce frequency of last-minute overtime approvals during demand spikes | 2 |
| 3 | Increase dock-door utilization rate during peak carrier windows | 3 |
| 4 | Reduce time to produce weekly labor cost variance reports | 4 |
| 5 | Minimize staffing gaps that lead to missed outbound shipments | 2, 6 |
| 6 | Increase confidence in next-day staffing levels before end of shift | 5, 6 |
| 7 | Reduce the number of scheduling conflicts escalated to site GMs | 7 |

## Evidence Notes (optional)

- What is well-supported: Jobs 1-3 came from interviews with two operations planners at Southeast distribution hubs.
- What is still assumption: Social job (7) is inferred from planner language, not directly stated. Dock Supervisor jobs need validation.
- Recommended next: Interview a Dock Supervisor directly. Validate labor cost reporting pain with finance stakeholders.
```

### Why This Works

- **All three job types present.** Four functional jobs ground the artifact in real operational work. Two emotional jobs capture the anxiety behind schedule coordination. One social job reveals the career motivation driving the planner's behavior.
- **Jobs are customer-centered.** Every job describes what the operations planner or dock supervisor does - not what the product does. No feature names, no product references.
- **Outcomes are measurable.** Each outcome uses Direction + Metric + Context. "Reduce time spent reconciling schedules across warehouse sites" - you can measure that. "Improve efficiency" - you cannot.
- **Persona column is concrete.** "Regional Operations Planner" and "Dock Supervisor" are people you could find in an org chart. Not "User" or "Stakeholder."
- **Fits the template.** Job statements are 6-9 words. Outcomes are 8-12 words. Persona entries are 2-3 words. All paste-ready.
- **Evidence notes are honest and trailing.** They identify what needs validation without cluttering the artifact itself.

---

## Example 2: Weak Generic JTBD Artifact

Same scenario, written poorly.

```markdown
# Jobs-to-Be-Done & Outcomes

## Product Context

- Product or service: Warehouse management solution
- Target market segment: Logistics
- Primary user persona: Operations Manager
- Buyer persona (if different): Executive

## 1. Job Statements & Personas

| # | Type | Job Statement | Persona |
|---|------|---------------|---------|
| 1 | F | Manage warehouse operations efficiently | Operations Manager |
| 2 | F | Improve workforce productivity | Operations Manager |
| 3 | F | Optimize scheduling | Operations Manager |
| 4 | F | Reduce costs | Executive |

## 2. Product Outcomes

| # | Product Outcome & Context | Related Job(s) |
|---|--------------------------|-----------------|
| 1 | Better efficiency | 1 |
| 2 | Improved productivity | 2 |
| 3 | More optimized schedules | 3 |
| 4 | Lower operational costs | 4 |
```

### Why This Fails

- **No emotional or social jobs.** Four functional jobs, all generic. The team has no insight into what motivates the customer beyond "do things better."
- **Jobs are too vague.** "Manage warehouse operations efficiently" could mean anything. It does not help the team make tradeoffs or prioritize features.
- **Outcomes restate the jobs.** "Improve workforce productivity" → "Improved productivity." No new information. No measurable metric. No context.
- **Persona is generic.** "Operations Manager" is a job family, not a specific person. "Executive" tells you nothing about who actually approves the purchase.
- **Only 4 rows.** The template expects 7 minimum. The team has blank slots and missing coverage.
- **No evidence notes.** Every claim looks equally confident, but none are grounded.

---

## Example 3: Drift Bug - Jobs Written as Solutions

```markdown
| # | Type | Job Statement | Persona |
|---|------|---------------|---------|
| 1 | F | Use the ShiftSync dashboard to view schedules | Operations Manager |
| 2 | F | Integrate ShiftSync with the existing WMS system | IT Administrator |
| 3 | F | Set up automated alerts for staffing shortages | Operations Manager |
| 4 | F | Configure the reporting module for weekly exports | Operations Manager |
```

### Why This Is Wrong

Every "job" is actually a product feature or implementation task:

- "Use the ShiftSync dashboard" - that is a solution, not a job. The job is "Reconcile shift schedules across sites."
- "Integrate ShiftSync with the existing WMS" - that is an IT task, not a customer job. And the persona has drifted to IT Administrator, which is not the customer the product serves.
- "Set up automated alerts" - that is a configuration step, not something the customer is trying to accomplish in their work life.
- "Configure the reporting module" - same problem. The customer job is "Report weekly labor cost variances to leadership." How the report gets configured is a solution detail.

**Fix:** Strip out every mention of the product. Ask: what was this person trying to do *before* your product existed? That is the job.
