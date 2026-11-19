# Risk Assessment Examples

## Strong Example

**Context:** B2B supply chain visibility platform. A product team is preparing to launch a real-time shipment tracking feature for mid-market logistics coordinators. The solution hypothesis is complete. The team is running this assessment collaboratively with the project manager and representatives from sales, engineering, and customer success before committing to the build plan.

---

### Risk Assessment

**Product or initiative:** Real-time shipment tracking for mid-market logistics coordinators
**Stage:** Pre-build, post-hypothesis
**Session participants:** Priya Sharma (PM), Marcus Webb (Project Manager), Dana Okonkwo (Engineering Lead), Lila Chen (Customer Success Lead), Rafael Torres (Sales Lead)
**Date of assessment:** June 26, 2026

---

**Section 1: Identify Risks**

| # | Risk Name | Risk Raised By |
|---|-----------|----------------|
| 01 | Carrier Data Gaps: key carriers lack real-time API coverage | Dana Okonkwo |
| 02 | Coordinator Resistance: dispatchers prefer phone-based status checks | Lila Chen |
| 03 | Integration Complexity: customer ERP systems vary widely in structure | Dana Okonkwo |
| 04 | Regulatory Variance: cross-border shipment data rules differ by region | Rafael Torres |
| 05 | Adoption Plateau: feature is available but not embedded in daily workflow | Priya Sharma |
| 06 | Competitive Timing: incumbent vendor announces similar feature this quarter | Marcus Webb |

---

**Section 2: Plot Level of Risk**

Risk 01: Carrier Data Gaps: key carriers lack real-time API coverage
  Impact Severity: High
  Occurrence Probability: High
  Priority: Critical

Risk 02: Coordinator Resistance: dispatchers prefer phone-based status checks
  Impact Severity: High
  Occurrence Probability: Medium
  Priority: Critical

Risk 03: Integration Complexity: customer ERP systems vary widely in structure
  Impact Severity: Medium
  Occurrence Probability: High
  Priority: Critical

Risk 04: Regulatory Variance: cross-border shipment data rules differ by region
  Impact Severity: High
  Occurrence Probability: Low
  Priority: Monitor

Risk 05: Adoption Plateau: feature is available but not embedded in daily workflow
  Impact Severity: Medium
  Occurrence Probability: Medium
  Priority: Manage

Risk 06: Competitive Timing: incumbent vendor announces similar feature this quarter
  Impact Severity: Medium
  Occurrence Probability: Low
  Priority: Accept

---

**Section 3: Begin Risk Management**

| Risk Name | Mitigation Tactics | Contingency Plans | Point of Contact | Notes |
|-----------|-------------------|-------------------|------------------|-------|
| Carrier Data Gaps: key carriers lack real-time API coverage | Audit the top 20 carriers used by pilot customers before build begins; partner only with carriers that have production-ready APIs | Launch with manual status input for non-covered carriers; communicate coverage scope clearly in onboarding | Dana Okonkwo | Audit needed in first two weeks; gates build kickoff |
| Coordinator Resistance: dispatchers prefer phone-based status checks | Conduct structured workflow observations with 5 coordinators before finalizing feature design; co-design the notification format with dispatcher input | Pause rollout at the first pilot site; schedule 3 facilitated sessions with coordinators to identify adoption blockers and redesign as needed | Lila Chen | Pilot site selection to be confirmed with Rafael Torres |
| Integration Complexity: customer ERP systems vary widely in structure | Build a connector layer with three pre-certified ERP schemas; document integration requirements in sales discovery before contract sign | Offer a manual CSV import path for customers whose ERP is outside the certified set; flag unsupported ERPs during onboarding | Dana Okonkwo | Connector layer adds 3 weeks to build estimate; confirmed with Marcus Webb |
| Regulatory Variance: cross-border shipment data rules differ by region | Identify the three highest-volume cross-border corridors in the customer base; complete regulatory review for those corridors before launch | Geo-restrict the feature for non-reviewed corridors at launch; expand coverage in phased releases after regulatory sign-off | Rafael Torres | Legal review to be initiated by Marcus Webb; 4-week lead time |

**Revisit Note:**
- Next scheduled review: at build kickoff (carrier audit complete)
- Trigger for unscheduled review: if any pilot customer reports integration failure or if carrier API coverage drops below 60% of their shipment volume

---

### Why This Works

- Risk Names follow the `[Type]: [Specific Concern]` pattern. Each one names something specific, not a category.
- Six risks span four distinct categories: technical (01, 03), adoption (02, 05), compliance (04), and competitive (06). No single category dominates.
- Priorities are meaningfully differentiated. Three Critical, one Monitor, one Manage, one Accept. The Accept risk (competitive timing) is acknowledged but not over-invested in given its low probability.
- Mitigation Tactics are proactive and specific: conducting an audit, running workflow observations, building a connector layer. None say "test more thoroughly."
- Contingency Plans are clearly reactive and distinct from mitigation: pausing rollout, geo-restricting, offering a manual path. Each describes what happens after the risk occurs, not before.
- Every Point of Contact is a named individual. Dana Okonkwo owns technical risks. Lila Chen owns the adoption risk. Rafael Torres owns the regulatory and competitive risks.
- The Revisit Note names a specific trigger, not just a vague intention to "check in later."

---

## Weak Example

**Context:** Same supply chain visibility platform. Different attempt at the same assessment.

---

### Risk Assessment

**Product or initiative:** Shipment tracking feature
**Stage:** Development
**Session participants:** Product team

---

**Section 1: Identify Risks**

| # | Risk Name | Risk Raised By |
|---|-----------|----------------|
| 01 | Technical Risk | Team |
| 02 | User Adoption Risk | Team |
| 03 | Integration Risk | Team |
| 04 | Compliance Risk | Team |
| 05 | Resource Risk | Team |
| 06 | Market Risk | Team |

---

**Section 2: Plot Level of Risk**

Risk 01: Technical Risk
  Impact Severity: High
  Occurrence Probability: High
  Priority: Critical

Risk 02: User Adoption Risk
  Impact Severity: High
  Occurrence Probability: High
  Priority: Critical

Risk 03: Integration Risk
  Impact Severity: High
  Occurrence Probability: High
  Priority: Critical

Risk 04: Compliance Risk
  Impact Severity: High
  Occurrence Probability: High
  Priority: Critical

Risk 05: Resource Risk
  Impact Severity: High
  Occurrence Probability: High
  Priority: Critical

Risk 06: Market Risk
  Impact Severity: High
  Occurrence Probability: High
  Priority: Critical

---

**Section 3: Begin Risk Management**

| Risk Name | Mitigation Tactics | Contingency Plans | Point of Contact | Notes |
|-----------|-------------------|-------------------|------------------|-------|
| Technical Risk | Test more thoroughly before launch | Test more thoroughly if issues arise | Product Team | TBD |
| User Adoption Risk | Communicate the feature to users | Communicate more if adoption is low | Product Team | TBD |

---

### Why This Fails

**Risk names are categories, not concerns.** "Technical Risk" does not identify a risk. It names a bucket. The team cannot assess likelihood, plan for it, or communicate it to stakeholders.

**Every risk is rated High/High/Critical.** When everything is Critical, nothing is prioritized. The team has no signal about where to concentrate effort or which risks warrant the most investment.

**Risk Raised By is "Team" for every row.** No individual is accountable. When something goes wrong, accountability evaporates.

**Mitigation and Contingency are identical.** "Test more thoroughly before launch" and "test more thoroughly if issues arise" are not two different plans. They are the same vague instruction applied to two different moments in time, and neither one is actually specific.

**Risk Management rows are incomplete.** Six risks were identified; only two have management rows. The four that were skipped include compliance, resource, and market risks that could be significant.

**The session was run alone.** "Product team" is not a collaborative review. The project manager and relevant stakeholders are not in the room.

---

## Drift-Bug Example

**Named failure: Mitigation-Contingency Swap Bug**

**What it looks like:**

The Mitigation Tactics and Contingency Plans columns contain the same type of content: both describe what the team will do after the risk has already occurred.

Example from a risk of low user adoption after launch:

| Risk Name | Mitigation Tactics | Contingency Plans | Point of Contact | Notes |
|-----------|-------------------|-------------------|------------------|-------|
| Coordinator Resistance: dispatchers avoid the new tracking dashboard | Provide additional training to users if adoption is below 40% at week four | Offer extended support hours if adoption remains slow after training | Lila Chen | Check adoption metrics at week four |

Both entries describe a response to adoption having already failed. Neither one attempts to prevent the adoption failure from occurring in the first place.

**Why it fails:**

Mitigation happens before the risk occurs. The goal is to reduce the probability that adoption fails. The current "Mitigation" is actually a contingency response to adoption already being below target.

**The fix:**

| Risk Name | Mitigation Tactics | Contingency Plans | Point of Contact | Notes |
|-----------|-------------------|-------------------|------------------|-------|
| Coordinator Resistance: dispatchers avoid the new tracking dashboard | Conduct workflow observations with five dispatchers before finalizing the interface; incorporate dispatcher input into the notification format and dashboard layout to match existing habits | If adoption falls below 40% at week four, pause rollout, conduct five structured interviews with non-adopters within two weeks, and redesign the highest-friction touchpoints before resuming | Lila Chen | Observation sessions to be scheduled before build kickoff |

Now Mitigation is proactive: observe real workflows and co-design with users to reduce the chance resistance occurs. Contingency is reactive: pause, learn, redesign. The two are clearly distinct and serve different moments in the risk lifecycle.

**How to spot this bug in your own artifact:**

Ask for each row: "If we execute the Mitigation Tactic perfectly, does it reduce the chance the risk occurs?" If the answer is "only if the risk has already occurred," the content belongs in the Contingency column, not the Mitigation column.
