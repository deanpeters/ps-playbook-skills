# Outcome & Strategy: Guided Discussion - Examples

---

## Example 1: Strong

**Scenario:** A PM at a logistics software company whose product helps freight carriers manage shipper relationships. The PM's manager has flagged shipper churn as a growing problem and requested a PM-led initiative to address it.

```markdown
# Outcome & Strategy: Guided Discussion

## Scope

- Discussion with: Priya Venkataraman, VP of Product
- Initiative or product: Shipper Retention Initiative
- Date: 14 March 2026
- Time horizon: 12 months (FY26)

---

## Outcome of the Discussion

### Business Outcome (one sentence)

Reduce 90-day shipper churn among mid-market accounts from 22% to under 12% by the end of FY26.

### Why It Matters Now

Mid-market shippers represent 60% of contracted revenue but have shown accelerating churn since Q3 last year, driven in part by two competitors launching improved onboarding experiences. The board has flagged net revenue retention as a primary health metric for FY26 and this segment is pulling it below target.

### Customer

Mid-market shipper operations managers at companies moving 200 to 2,000 shipments per month, responsible for carrier selection, freight cost management, and exception handling. They use our platform daily but currently describe the first 90 days as confusing and unsupported.

### Success Criteria

| Criteria | Metric or Signal | Target |
|---|---|---|
| 90-day churn rate (mid-market) | Percentage of mid-market accounts churning within 90 days of contract start | Under 12% by Q4 FY26 |
| Time to first successful shipment | Days from account activation to first completed shipment | Under 7 days (from current 18) |
| Early-stage support ticket volume | Support tickets per account in first 90 days | Reduce by 40% |

### Constraints

- Engineering capacity: one squad available for this initiative through Q3; a second squad can be added in Q4 if early results warrant it
- Timeline: any changes affecting the shipper onboarding flow must be live before the summer shipping peak (end of May)
- Technology: the current onboarding module is being migrated to the new platform in Q3; solutions must work within the existing module or be designed to port to the new platform
- Out of scope: enterprise accounts and spot-freight shippers are handled by a separate team

### Open Questions and Gaps

- The 12% churn target came from the finance team's NRR model, but no one has validated whether that target is achievable with the resources available. Need to confirm with finance by end of month.
- The root cause of churn is assumed to be onboarding quality, but we have not yet spoken to churned shippers. This assumption drives the entire initiative frame and needs to be tested early in discovery.

---

## Key Decision Point

- [x] Go: alignment is clear across all five areas. Proceed to discovery.

Caveat: the finance target confirmation and root-cause assumption should be first items on the discovery agenda.
```

**Why this works:**

- The business outcome is specific and measurable: a named segment, a named metric (90-day churn), a current baseline (22%), a target (under 12%), and a time horizon (FY26). A third party could assess whether it was achieved.
- The customer is named by role and context. It identifies not just a job title but the operational situation (200 to 2,000 shipments per month, daily users, 90-day struggle) that makes this population meaningful.
- The success criteria table has three rows, each with a named metric and a specific target. None of them say "improve" without quantifying what improvement means.
- The open questions section does not paper over gaps. It explicitly flags two assumptions that could invalidate the entire initiative if unchecked - and the PM takes responsibility for testing them early.
- The KDP is marked Go, but with a documented caveat rather than unqualified sign-off. This is honest alignment.

---

## Example 2: Weak

**Scenario:** The same company, the same manager, the same conversation - but the PM recorded vague answers, accepted weak language as complete, and left critical fields underdefined.

```markdown
# Outcome & Strategy: Guided Discussion

## Scope

- Discussion with: VP of Product
- Initiative or product: Churn project
- Date: March 2026
- Time horizon: this year

---

## Outcome of the Discussion

### Business Outcome (one sentence)

Improve shipper satisfaction and reduce churn.

### Why It Matters Now

Churn has been a problem and the board wants to see it fixed. We are behind competitors.

### Customer

Shippers who use our platform.

### Success Criteria

| Criteria | Metric or Signal | Target |
|---|---|---|
| Satisfaction | NPS or CSAT | Improve |
| Churn | Churn rate | Reduce |

### Constraints

- Limited engineering time
- Need to move fast

### Open Questions and Gaps

None noted.

---

## Key Decision Point

- [x] Go: proceed to discovery.
```

**Why this fails:**

- **Business Outcome:** "Improve shipper satisfaction and reduce churn" bundles two different outcomes with no measurement and no target. A third party cannot assess whether this was achieved. This is the acceptance of vague language that Pitfall 2 describes.
- **Why Now:** "Churn has been a problem" is background noise, not strategic rationale. It does not establish urgency or explain what changed to make this the current priority.
- **Customer:** "Shippers who use our platform" covers potentially thousands of accounts across multiple segments with different needs. It gives discovery no useful frame. Is this small shippers? Enterprise shippers? The entire customer base?
- **Success Criteria:** Both rows say "improve" or "reduce" without a baseline, a target, or a timeframe. These are not success criteria. They are aspirations. A PM cannot tell whether they succeeded if they have no definition of success.
- **Constraints:** "Limited engineering time" and "need to move fast" are not constraints. They are vague acknowledgments that resources are finite. Every project has finite resources. A real constraint names what is fixed: a specific team, a deadline, a technical boundary.
- **Open Questions:** Marking "None noted" when two major assumptions are unvalidated (root cause of churn, achievability of any target) is active gap suppression. The gaps exist. They are just not documented.
- **KDP:** The Go call is marked without any basis for confidence. This PM is proceeding to discovery while carrying a contested outcome, an undefined customer, and unmeasured success criteria.

---

## Example 3: Drift Bug - Outcome Captured as a Project

**Scenario:** Same company, same conversation. But in this version, the PM writes down what the manager said at the end of the meeting - a project scope - instead of the business outcome the project is meant to achieve.

```markdown
### Business Outcome (one sentence)

Launch the new shipper onboarding dashboard by Q3.
```

**Why this fails:**

This is the most common failure mode in this play, and it is easy to miss because it sounds specific and concrete. "Launch the new shipper onboarding dashboard by Q3" has a named deliverable and a date. It feels like a well-defined outcome. It is not.

A project milestone describes what the team will ship. A business outcome describes what changes for the business when the project succeeds.

The dashboard launch is an output. Reducing 90-day churn among mid-market shippers is the outcome. These are categorically different, and the distinction matters for everything that follows:

- **Discovery framed around the project:** the PM will research how to build a better dashboard, not whether a dashboard solves the customer's actual problem. If the real problem is something the dashboard cannot address (pricing, support response time, competitor switching costs), the project will be completed on time and still fail.
- **Success defined by delivery:** the team celebrates shipping the dashboard in Q3, but no one tracks whether churn improved. The business outcome that motivated the project is never measured.
- **No KDP leverage:** if the PM reaches a Go decision with "launch dashboard by Q3" as the outcome, there is no meaningful escalation path if discovery reveals the approach is wrong. You cannot escalate "we should reconsider the dashboard" when the entire frame is "deliver the dashboard."

**The fix:** before recording a business outcome, ask: "Is this what we are delivering, or is this what changes for the business when we deliver it successfully?" If the answer is "what we are delivering," press for the outcome behind it. "What should improve for the business as a result of launching the dashboard?" - that answer is the business outcome.
