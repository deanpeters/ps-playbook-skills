# Outcome Tree - Section One: Examples

## Example 1: Strong Productside-Style Outcome Tree

Scenario: A sustainable agriculture technology company building a precision irrigation platform for regional farm operations managers and agronomists.

```markdown
# Outcome Tree - Section One

## Product Context

- Product or service: AquaPrecision - precision irrigation management platform
- Business or organization: AgriTech Solutions (mid-market agricultural technology provider)
- Primary customer/user role: Regional Farm Operations Manager
- Buyer (if different): VP of Agricultural Operations

## Problem Statement (from Framing the Problem play, if available)

> Regional farm operations managers currently rely on manual field inspections and weather forecasts to schedule irrigation, resulting in 25-35% water waste and inconsistent crop yields across managed acreage. They need a way to make irrigation decisions based on real-time soil and weather data so they can reduce water usage while maintaining or improving yield consistency.

## 1. Business Outcome

| Business Outcome |
|------------------|
| Reduce water consumption across managed farm operations by 20% within 18 months while maintaining crop yield targets |

## 2. Business Success Metrics

| # | Business Success Metric | Status |
|---|------------------------|--------|
| 1 | Total water usage per acre across all managed properties (gallons/acre/season) | Defined |
| 2 | Crop yield variance from target across managed properties (percentage) | Defined |
| 3 | Irrigation-related operational cost per acre (dollars/acre/season) | TBD |

## 3. Product Outcomes (2-5)

| # | Product Outcome |
|---|----------------|
| 1 | Regional farm operations managers make irrigation scheduling decisions based on current field conditions rather than manual inspections |
| 2 | Agronomists identify water stress across multiple fields before visible crop damage occurs |
| 3 | Field technicians complete irrigation system adjustments in a single site visit instead of multiple trips |

## 4. Product Success Metrics

| # | Product Success Metric | Related Outcome | Status |
|---|----------------------|-----------------|--------|
| 1 | Percentage of irrigation decisions made using platform data vs. manual inspection | 1 | TBD |
| 2 | Average time from water stress onset to agronomist awareness (hours) | 2 | TBD |
| 3 | Average number of site visits per irrigation adjustment cycle | 3 | Defined |
| 4 | Percentage of managed acres with active sensor coverage | 1, 2 | Defined |

## 5. Product Health Metrics

| # | Product Health Metric | Target |
|---|---------------------|--------|
| 1 | Sensor data ingestion uptime | 99.5% |
| 2 | Average time from sensor reading to dashboard update | < 15 minutes |
| 3 | Weekly active users as percentage of licensed accounts | > 70% |

## Solution Summary (from Solution Hypothesis Statement play, if available)

> Not yet defined

## Causal Chain Review

- Product Outcome 1 (data-driven irrigation decisions) directly reduces water waste by replacing imprecise manual scheduling.
- Product Outcome 2 (early stress detection) prevents yield loss that would otherwise offset water savings.
- Product Outcome 3 (single-visit adjustments) reduces operational cost per acre, supporting the cost metric.
- Gap: No product outcome addresses seasonal planning or long-term water budgeting. This may be needed if the 20% reduction target requires structural changes, not just better daily decisions.
```

### Why This Works

- **Clear causal chain.** Each product outcome connects logically to the business outcome. Reducing water consumption requires better irrigation decisions (Outcome 1), preventing crop damage that undermines savings (Outcome 2), and reducing operational cost of the changes (Outcome 3).
- **Business outcome is specific and measurable.** "Reduce water consumption by 20% within 18 months while maintaining yield targets" has a direction, a metric, a target, and a timeframe.
- **Product outcomes are customer-centered.** Each describes what a specific role achieves, not what the product does. "Regional farm operations managers make irrigation scheduling decisions based on current field conditions" is about the manager's changed behavior, not a product feature.
- **Role names, not persona names.** "Regional farm operations managers," "agronomists," and "field technicians" are roles. No individual names like "Carlos" or "Priya."
- **Metrics are distinguished by type.** Business success metrics (water per acre, yield variance) are separate from product success metrics (decisions using platform data, time to awareness) and product health metrics (uptime, latency, adoption). No confusion between levels.
- **Honest about gaps.** The causal chain review flags a gap in seasonal planning. TBD metrics are marked as such rather than invented.

---

## Example 2: Weak Generic Outcome Tree

Same scenario, written poorly.

```markdown
# Outcome Tree - Section One

## Product Context

- Product or service: Smart irrigation system
- Business or organization: AgriTech company
- Primary customer/user role: Farmer
- Buyer (if different): Same

## 1. Business Outcome

| Business Outcome |
|------------------|
| Grow the business and improve sustainability |

## 2. Business Success Metrics

| # | Business Success Metric | Status |
|---|------------------------|--------|
| 1 | Revenue growth | TBD |
| 2 | Customer satisfaction | TBD |

## 3. Product Outcomes (2-5)

| # | Product Outcome |
|---|----------------|
| 1 | Better water management |
| 2 | Improved crop yields |
| 3 | Reduced costs |
| 4 | Increased efficiency |
| 5 | Better data visibility |
| 6 | Faster decision making |
| 7 | Improved sustainability metrics |

## 4. Product Success Metrics

| # | Product Success Metric | Related Outcome | Status |
|---|----------------------|-----------------|--------|
| 1 | User satisfaction | All | TBD |

## 5. Product Health Metrics

| # | Product Health Metric | Target |
|---|---------------------|--------|
| 1 | System uptime | High |
```

### Why This Fails

- **Business outcome is unmeasurable.** "Grow the business and improve sustainability" has no direction, no metric, and no target. Nobody can tell if it happened.
- **Product outcomes are vague abstractions.** "Better water management" and "increased efficiency" could mean anything. They do not describe a customer's changed state.
- **Too many product outcomes.** Seven outcomes exceeds the 2-5 limit. The team cannot focus.
- **No customer roles.** "Farmer" is too generic. Which farmer? The operations manager, the agronomist, the field technician? Different roles have different outcomes.
- **Metrics are absent or generic.** "User satisfaction" as a single metric for all outcomes provides no signal. "High" is not a target.
- **No causal chain.** There is no visible logic connecting product outcomes to the business outcome. The tree is a wish list, not a strategy artifact.

---

## Example 3: Drift Bug - Product Outcomes Confused with Business Outcomes and Internal Tasks

```markdown
## 3. Product Outcomes (2-5)

| # | Product Outcome |
|---|----------------|
| 1 | Increase market share in the precision agriculture segment by 15% |
| 2 | Achieve $5M in annual recurring revenue from irrigation management subscriptions |
| 3 | Ship the Q3 release with sensor integration on time |
| 4 | Reduce customer churn rate to below 8% annually |
| 5 | Complete SOC 2 compliance certification before fiscal year end |
```

### Why This Is Wrong

Every entry confuses the level of the tree it belongs in:

- **"Increase market share by 15%"** is a business outcome, not a product outcome. Market share is a business-level metric. The product team cannot directly control market share. This belongs in the Business Outcome box, not in the Product Outcomes section.
- **"Achieve $5M in ARR"** is a business financial target. It tells you nothing about what the customer achieves. Revenue is a consequence of delivering product outcomes, not a product outcome itself.
- **"Ship the Q3 release on time"** is an internal team task. It describes what the engineering team does, not what the customer gets. Shipping on time may be necessary, but it is not a product outcome.
- **"Reduce customer churn to below 8%"** is a business retention metric. Churn rate is a lagging business indicator. The product outcome would describe what changed for the customer that made them stay.
- **"Complete SOC 2 compliance certification"** is an internal operational task. It may be a prerequisite for selling to certain customers, but it is not something the customer achieves.

**Fix:** For each entry, ask: "Who experiences this? Is it the customer using the product, or is it the business/team?" Then rewrite:

- "Increase market share by 15%" becomes the Business Outcome (or a business metric)
- "$5M ARR" becomes a Business Success Metric
- "Ship Q3 release" gets removed entirely (this is a project milestone, not an outcome at any level)
- "Reduce churn to below 8%" becomes a Business Success Metric
- "SOC 2 certification" gets removed or noted as a prerequisite, not an outcome

The actual product outcomes would describe what farm operations managers, agronomists, or field technicians achieve differently because the product exists.
