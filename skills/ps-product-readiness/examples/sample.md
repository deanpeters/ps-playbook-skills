# Product Readiness Testing Examples

**Scenario for all three examples:** A mid-market field service management platform. The product is a mobile work order system that allows field service technicians (HVAC, plumbing, electrical) to receive job assignments, document completed work, and submit service reports from their phones, replacing a paper-based and dispatcher-phone-call process. The PM has completed earlier rounds of discovery interviews and a clickable prototype test. This is the pre-launch readiness test.

---

## Strong Example

**Context:** The PM has run two earlier rounds of user testing: a clickable prototype walkthrough with eight technicians and a three-week limited-access pilot with one customer site. This readiness test is the final validation before market release to 20+ customers.

---

### Product Readiness Test Plan

**Product or initiative:** FieldFlow Mobile Work Order System
**Stage:** Pre-launch beta program
**Date:** July 15, 2026
**Test Lead (PM):** Sonia Oduya

---

#### Section 1: Product Readiness Test Plan

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

#### Section 2: Product Readiness Goals

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

#### Section 3: Assumptions and Risks

- Dispatcher interface is not being tested in this program. Only 4 dispatcher participants are included, and their results are informational rather than part of the Go/No Go criteria. Dispatch-side readiness will be validated in a separate beta before enterprise account rollout.
- The test does not cover all device types. Participants are using iOS devices only. Android support is in the build plan but not yet fully tested; Android-specific issues may surface post-launch.
- Limited integrations are in scope. Only the QuickBooks Online integration is active during this test. Integration with enterprise accounting systems (SAP, Oracle) is planned for Q4 and is not part of this readiness assessment.
- Training materials are in draft form. Participants are working from an unfinished onboarding guide. Final training content will be complete before general availability. Any adoption issues related to unclear onboarding instructions may improve when finalized materials are released.
- The test population is limited to HVAC technicians. Plumbing and electrical trade participants are in the broader customer target but are not represented in this test. Trade-specific workflow variations may surface post-launch for those segments.

---

### Why This Works

- **Customer profiles are specific.** Each profile names the role, company size, experience level, and what the profile represents in the market. The control group is clearly separated and explicitly excluded from the Go/No Go decision.
- **Participant count is broken down by type.** The breakdown makes the test structure legible: 8 technicians, 4 dispatchers, 2 internal controls.
- **Duration is anchored to usage, not just calendar time.** "Minimum 6 full work order cycles" prevents the risk of a two-week test where participants only touch the product once.
- **All four test team roles are named.** A Quote Collector is named and briefed. Quotes are treated as a deliverable.
- **Goals table has numeric targets.** Every row has a threshold: 25%, 4.0/5, 80%, 99.0%, 85%. No row says "improve" or "increase" without a number.
- **Go/No Go criteria are pre-committed.** Four must-pass goals are named before the test begins. The fifth is explicitly aspirational. The team cannot rationalize a result after seeing the data.
- **Assumptions and Risks section documents five specific scope limits.** Each one names the constraint, why it is out of scope, and what comes next. A stakeholder reading this section knows exactly what the test does not cover.

---

## Weak Example

**Context:** Same field service management platform. Different planning attempt.

---

### Product Readiness Test Plan

**Product or initiative:** Field Service App
**Stage:** Beta
**Date:** July 2026
**Test Lead:** Product team

---

#### Section 1: Product Readiness Test Plan

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

#### Section 2: Product Readiness Goals

| Goal/Objective | Measure/Metric | Target |
|----------------|----------------|--------|
| Improve efficiency | User feedback | Positive |
| Increase satisfaction | Survey | Good scores |
| Reduce support calls | Support volume | Lower than before |
| Ensure the app works | Uptime | High |

**Pre-Committed Go/No Go Criteria**

The team will review results and decide.

---

#### Section 3: Assumptions and Risks

N/A

---

### Why This Fails

**Customer profiles are job titles, not profiles.** "Field service technicians" does not describe company type, experience level, or what the participant represents. The inclusion of "some internal users" with no explanation of who they are or why they are included is a red flag: internal users may not represent the customer failure modes the test needs to expose.

**Participant count is vague and has no breakdown.** "Around 10-12 users" gives no structure. There is no way to know how many of each type will be tested.

**Duration is calendar-only.** "Two weeks" with no usage anchor is meaningless for a product used in job cycles. Two weeks could mean two full work order cycles or zero, depending on how often participants are dispatched during that window.

**Test team roles are not assigned.** "The product team will manage the test" means no one is accountable for technical support, participant relationships, or quote capture. When a participant hits a bug, no one is on call to triage it.

**Goals table has directional aspirations with no numbers.** "Positive," "good scores," "lower than before," and "high" are not targets. The team cannot make a Go/No Go call based on these columns. Post-test rationalization is the only option.

**Pre-committed Go/No Go criteria are absent.** "The team will review results and decide" is the absence of criteria. This is how a failed test gets rationalized into a Go.

**Assumptions and Risks is blank.** "N/A" implies the test covers everything. It does not. No test ever does. The absence of named scope limits does not protect the team. It sets them up to be held accountable for failures outside the test scope.

---

## Drift-Bug Example

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
