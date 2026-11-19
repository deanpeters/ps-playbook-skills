# Measuring Outcomes - Examples

Three examples using a field services management scenario. A software company has built a mobile field dispatch platform for utility maintenance crews. Field technicians use it to receive work orders, log completion, and report equipment conditions. The scenario is deliberately non-HR to avoid the canonical template example.

---

## Example 1: Strong

**Why this works:** Business and Product Outcomes are clearly distinct and traceable. Success metrics are named specifically with directional targets and real tools. Health metrics measure a categorically different dimension. Baselines are established. The tension review catches a real risk before launch.

---

### Header

**Business Outcomes**

Reduce unplanned utility outage costs by 25% over 18 months by improving the speed and accuracy of field maintenance responses across 14 regional service districts.

**Product Outcome**

Field maintenance technicians complete work orders with verified equipment condition data on the first visit, eliminating return trips caused by incomplete field reports.

---

### Product Success Metrics

| Product Success Metric | Measurement Tool | Baseline Data | Quarterly Update 1 | Quarterly Update 2 | Quarterly Update 3 | Annual Update |
|---|---|---|---|---|---|---|
| Reduce Return Trips: decrease same-job return visits from 18% to under 6% | Salesforce Field Service dispatch reports | 18% return visit rate, Q4 2025 rolling 90-day average | | | | |
| Cut Report Completion Time: decrease time from work order close to verified report submission from 47 min to under 15 min | Mixpanel event tracking (work order close to report submit timestamp) | 47 minutes median, Q4 2025 | | | | |
| Increase First-Visit Resolution: raise jobs resolved without supervisor escalation from 71% to 88% | Power BI operations dashboard, supervisor escalation flag | 71% first-visit resolution rate, Q4 2025 | | | | |
| Improve Equipment Condition Capture Rate: increase work orders with photo + structured condition data from 34% to 90% | SQL query, field_reports table, condition_data_complete flag | 34% full capture rate, December 2025 audit | | | | |

---

### Product Health Metrics

| Product Health Metric | Measurement Tool | Baseline Data | Quarterly Update 1 | Quarterly Update 2 | Quarterly Update 3 | Annual Update |
|---|---|---|---|---|---|---|
| NPS: maintain technician NPS above 42 | Qualtrics quarterly pulse, field technician cohort | 31 NPS at pilot cohort (Oct 2025, n=44) | | | | |
| App Uptime: 99.4% or higher during field hours (6am-8pm local) | Internal monitoring (PagerDuty SLA dashboard) | 98.1% uptime, 6-month pre-launch average | | | | |
| Report Error Rate: maintain submission error rate below 2% | Salesforce validation failure log, auto-flagged submissions | 6.2% error rate (pre-platform, manual process baseline) | | | | |
| DAU/MAU Ratio: active usage ratio above 0.80 (technicians who use app at least 20 of 25 working days) | Mixpanel user cohort report | First measurement becomes baseline at Q1 | | | | |

---

### Metric Tension Review

Two tensions to watch:

1. **Return trip reduction vs. NPS.** If technicians feel pressure to close work orders without escalating when they are unsure, return trips may drop while technician NPS also drops - because technicians feel set up to fail. Watch both signals together at Q1. If return trips improve but NPS declines, investigate whether technicians are skipping escalations they should be making.

2. **Equipment condition capture rate vs. submission error rate.** Pushing technicians to submit more structured data faster may initially increase submission errors as they learn the new format. Expect error rates to temporarily increase in Q1 before improving. Flag this to leadership before Q1 data is reviewed.

---

**Commentary:** This dashboard works because the two tables are genuinely measuring different things. Success metrics tell you whether customers (technicians) are achieving the product outcome - fewer return trips, faster verified reporting, better first-visit resolution. Health metrics tell you whether the product is operationally sound - reliability, user experience, adoption depth. The metric tension review catches a real dynamic before it becomes a surprise in leadership reporting.

---

## Example 2: Weak

**Why this fails:** Metrics are generic and unverifiable. No measurement tools are named. No baseline data is established. The two tables are indistinguishable from each other - success and health metrics are measuring the same things in vague ways.

---

### Header

**Business Outcomes**

Improve our operational performance and reduce costs.

**Product Outcome**

Make field technicians more efficient.

---

### Product Success Metrics

| Product Success Metric | Measurement Tool | Baseline Data | Quarterly Update 1 | Quarterly Update 2 | Quarterly Update 3 | Annual Update |
|---|---|---|---|---|---|---|
| Efficiency | Analytics | TBD | | | | |
| User Adoption | TBD | TBD | | | | |
| Quality | Reports | Currently not great | | | | |

---

### Product Health Metrics

| Product Health Metric | Measurement Tool | Baseline Data | Quarterly Update 1 | Quarterly Update 2 | Quarterly Update 3 | Annual Update |
|---|---|---|---|---|---|---|
| User Satisfaction | Survey | TBD | | | | |
| System Performance | IT monitoring | TBD | | | | |
| Adoption Rate | Analytics | TBD | | | | |

---

### Metric Tension Review

Things will improve after launch. Will monitor quarterly.

---

**Commentary:** This dashboard fails on every load-bearing criterion. "Improve operational performance" is not a Business Outcome - it has no direction, no metric, and no target. "Make field technicians more efficient" is not a Product Outcome - it tells you nothing about what customers would achieve differently. "Efficiency," "Quality," and "User Adoption" are not metrics - they are category labels with no measurable signal attached. "Analytics" and "TBD" are not measurement tools. "Currently not great" is not baseline data. The two tables are indistinguishable - "User Satisfaction" in the health table and "Efficiency" in the success table are measuring the same vague thing. At Q1 review, every column will still be blank because no one was told what to collect or where to find it.

---

## Example 3: Drift Bug - Output Metrics Instead of Outcome Metrics

**Why this fails:** The success metrics have drifted from tracking customer outcomes to tracking engineering outputs. Every metric improves when the team ships more, not when customers achieve something. This is the output-vs-outcome inversion.

---

### Header

**Business Outcomes**

Reduce unplanned utility outage costs by 25% over 18 months by improving the speed and accuracy of field maintenance responses.

**Product Outcome**

Field maintenance technicians complete work orders with verified equipment condition data on the first visit, eliminating return trips caused by incomplete field reports.

---

### Product Success Metrics (Drift Bug)

| Product Success Metric | Measurement Tool | Baseline Data | Quarterly Update 1 | Quarterly Update 2 | Quarterly Update 3 | Annual Update |
|---|---|---|---|---|---|---|
| Features Shipped: 12 new platform features per quarter | JIRA release board | 4 features per quarter, Q4 2025 | | | | |
| API Response Time: average under 200ms | New Relic APM | 320ms average, November 2025 | | | | |
| Weekly Deployments: maintain weekly release cadence | CI/CD pipeline logs | Bi-weekly deployments, Q4 2025 | | | | |
| Bug Resolution: resolve P1 bugs within 48 hours | JIRA bug tracking, P1 label | 72-hour average resolution, Q4 2025 | | | | |

---

**Commentary:** This drift is extremely common on engineering-led teams. Notice that the Business Outcome and Product Outcome are correctly written - they describe what the business and customers should achieve. But the success metrics measure what the engineering team does, not what customers experience. Features shipped, API response time, deployment cadence, and bug resolution speed all tell the engineering team they are productive. None of them tell anyone whether technician return trips decreased, whether report completion time improved, or whether first-visit resolution rates went up. A PM could hit all four of these success metrics while customer outcomes move in the wrong direction - and would have no signal until a leadership review.

**Fix:** Return to the product outcome: "field maintenance technicians complete work orders with verified equipment condition data on the first visit, eliminating return trips." Ask: "If this is happening, what would we see in the data?" That question points directly to return visit rates, report completion times, and equipment condition capture rates - the outcome metrics from Example 1. API response time and deployment cadence belong in an engineering operations dashboard, not here.
