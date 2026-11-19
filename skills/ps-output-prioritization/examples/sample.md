# Output Prioritization Examples

---

## Example 1: Strong

**Context:** A product team at a healthcare operations company is building a field service coordination tool for home health aides and care coordinators. The solution hypothesis is complete. The PM has validated two product outcomes from the Outcome Tree: (1) care coordinators confirm same-day schedule changes before aides depart, and (2) aides spend less time resolving conflicting visit instructions in the field. The team is running this exercise collaboratively with the engineering lead and a project manager before starting sprint planning.

---

### Output Prioritization

**Product or initiative:** Home health field service coordination tool
**Customer role:** Care coordinator (primary), home health aide (secondary)
**Session participants:** Yemi Adeyemi (PM), Hana Kozlowski (Engineering Lead), Marcus Webb (Project Manager), Siona Patel (Operations Lead)
**Date:** June 26, 2026

---

**Section 1: Candidate Outputs**

- Real-time schedule change alert (push notification to aide when visit is modified)
- Offline visit record sync (aides can log visit details without cell coverage)
- Conflict detection dashboard (coordinator sees scheduling gaps before dispatch)
- Bulk rescheduling tool (move multiple visits at once during weather events)
- Aide availability calendar (aides submit availability windows; coordinator views them)
- Integration with third-party billing system
- Voice-to-text visit notes (aide dictates instead of typing)

---

**Section 2: Center Point Output**

**Center point output:** Aide availability calendar

**Why this is medium/medium:** The aide availability calendar requires a moderate build (a structured input form, storage, and a read view for coordinators - estimated at two sprints by Hana) and delivers moderate customer value (it reduces coordinator phone tag, which is a real pain, but does not directly address the most acute problem of same-day change notification). The team agreed it sits in the middle of both axes.

---

**Section 3: Four Quadrant Classification**

| Output | Value (H/M/L) | Value Rationale | Cost (H/M/L) | Cost Rationale | Quadrant | Priority |
|--------|--------------|-----------------|-------------|----------------|----------|----------|
| Aide availability calendar | M | Anchor | M | Anchor - two-sprint estimate, standard form + storage build | Center | Reference |
| Real-time schedule change alert | H | Directly supports product outcome 1: care coordinators confirm same-day changes before aides depart. Eliminates the primary source of missed visits. | L | Push notification with existing visit data - one sprint; no new data model required (Hana) | I | Start |
| Conflict detection dashboard | H | Directly supports product outcome 1 from the coordinator side: spots gaps before dispatch rather than after. Prevents the scheduling errors that drive incorrect visit instructions. | M | New view over existing schedule data; two sprints; some aggregation logic (Hana) | I | Start |
| Offline visit record sync | H | Directly supports product outcome 2: aides resolve conflicting instructions faster when they have access to their records in low-coverage areas. Validated in empathy interviews - 7 of 9 aides reported coverage gaps. | H | Requires conflict resolution logic for sync, local storage on device, and server-side reconciliation - four sprints minimum (Hana and Marcus) | II | Plan |
| Voice-to-text visit notes | M | Reduces aide documentation time but does not address the scheduling conflict problem that drives product outcomes 1 or 2. Valued by aides as a convenience feature. | M | Two sprints; relies on device speech API, no custom model needed (Hana) | Center-adjacent | Deprioritize |
| Bulk rescheduling tool | L | Useful during weather events but covers an infrequent scenario. Does not address the daily scheduling conflict problem that drives both product outcomes. | M | Two to three sprints; edge cases in visit dependency logic add complexity (Hana) | III | Deprioritize |
| Integration with third-party billing system | L | Does not impact care coordinators' daily scheduling work or aides' field experience. Serves finance team, not the customer. | H | Four to six sprints; requires custom API work for each billing vendor; high variability (Hana) | IV | Cut |

---

**Section 4: Quadrant Summary and Action Guidance**

**Quadrant I - Start Here**

| Output | Product Outcome Supported |
|--------|--------------------------|
| Real-time schedule change alert | Care coordinators confirm same-day schedule changes before aides depart |
| Conflict detection dashboard | Care coordinators confirm same-day schedule changes before aides depart |

Action: Both outputs enter the next sprint. Schedule change alert first (lower cost, faster signal from real-world use).

**Quadrant II - Plan Carefully**

| Output | Key Assumption to Validate | Recommendation |
|--------|---------------------------|----------------|
| Offline visit record sync | Assumption: aides will proactively sync records when coverage returns rather than relying on coordinator callbacks. This behavior has not been validated in real conditions. | Run a Wizard-of-Oz lo-fi experiment with three aides before committing to the full sync build. |

**Quadrant III - Deprioritize**

- Voice-to-text visit notes - Deferred. Real convenience value for aides but does not drive either product outcome in the current cycle. Revisit after Quadrant I outputs ship and adoption data confirms which pain remains most acute.
- Bulk rescheduling tool - Deferred. Low-frequency use case. Revisit if weather event volume increases or coordinators surface it as a blocking issue.

**Quadrant IV - Avoid or Cut**

- Integration with third-party billing system - Cut. This serves the finance team, not care coordinators or aides. No connection to either product outcome. Building it would consume four to six engineering sprints that would displace the offline sync build. The VP of Finance has requested this feature - Yemi will document the tradeoff in writing and ask for an explicit decision before the next planning cycle.

---

### Why This Works

The classification shows genuine spread: two outputs in Quadrant I, one in Quadrant II, two deferred, one cut. The center point anchor prevented the team from calling everything high value - voice-to-text notes and the bulk tool ended up where they belong. Value rationales name specific product outcomes or validated interview findings, not business benefits. The Quadrant IV item is actually cut (with an explicit stakeholder tradeoff documented), not quietly deferred. Engineering input was used for every cost classification.

---

## Example 2: Weak

**Context:** Same product, same scenario. The PM ran this exercise alone between other meetings, without the engineering lead or project manager. No outcome tree had been completed.

---

### Output Prioritization (Weak Version)

**Product or initiative:** Home health field service coordination tool
**Customer role:** Not specified
**Session participants:** Jamie (PM)
**Date:** June 26, 2026

---

**Section 1: Candidate Outputs**

- Real-time schedule change alert
- Offline visit record sync
- Conflict detection dashboard
- Bulk rescheduling tool
- Aide availability calendar
- Integration with third-party billing system
- Voice-to-text visit notes

---

**Section 2: Center Point Output**

Not established. Jamie proceeded directly to classification.

---

**Section 3: Four Quadrant Classification**

| Output | Value | Cost | Quadrant |
|--------|-------|------|----------|
| Real-time schedule change alert | High | Low | I |
| Offline visit record sync | High | Medium | I |
| Conflict detection dashboard | High | Low | I |
| Bulk rescheduling tool | High | Medium | I |
| Aide availability calendar | High | Low | I |
| Integration with third-party billing system | High | High | II |
| Voice-to-text visit notes | High | Low | I |

---

**Section 4: Quadrant Summary**

Everything is either Quadrant I or Quadrant II. All outputs are labeled high value. No rationale is provided. Nothing is deprioritized. Nothing is cut.

---

### Why This Fails

Five failures in this classification:

1. **No center point anchor.** Without an anchor, every output defaults to high value. This is the most predictable outcome of skipping Step 4.

2. **No customer role named.** Value cannot be assessed if the team has not agreed on who the customer is. "High value" to whom?

3. **No value rationale.** "High" is not a rationale. The classification table has no evidence - it reflects the PM's advocacy for all outputs, not customer-grounded evidence.

4. **No engineering input on cost.** Offline visit record sync is listed as Medium cost. In the strong example, Hana estimated it at four sprints due to sync conflict resolution complexity. Without a technical voice, cost estimates are guesses.

5. **Nothing is cut.** A prioritization exercise that produces zero cuts has not prioritized anything. It has produced a wish list with a grid label attached.

---

## Example 3: Drift Bug - Value Defined as Business Revenue Impact

**Context:** Same product. The PM has access to the outcome tree and included the engineering lead. But during the classification session, the PM reframed the value axis as "business revenue impact" rather than customer outcome impact.

---

### Output Prioritization (Drift-Bug Version)

**Product or initiative:** Home health field service coordination tool
**Customer role:** Care coordinator, home health aide
**Session participants:** Yemi Adeyemi (PM), Hana Kozlowski (Engineering Lead)
**Date:** June 26, 2026

---

**Section 3: Four Quadrant Classification (excerpt)**

| Output | Value (H/M/L) | Value Rationale | Cost (H/M/L) | Quadrant |
|--------|--------------|-----------------|-------------|----------|
| Integration with third-party billing system | H | This will eliminate manual billing reconciliation and reduce finance team overhead by an estimated 12 hours per week. High revenue protection value. | H | II |
| Conflict detection dashboard | M | Good for coordinators but hard to tie to a revenue outcome. No clear upsell path. | M | Center |
| Real-time schedule change alert | L | Coordinators already manage this via phone. Low incremental revenue impact. | L | III |

---

### The Drift

The PM has substituted business revenue impact for customer outcome impact on the Y-axis. The result:

- Billing system integration (which serves the finance team, not care coordinators) is rated High Value because it protects revenue.
- Conflict detection dashboard (which directly supports care coordinators' ability to prevent missed visits) is rated Medium because it does not generate revenue.
- Real-time schedule change alert (which eliminates the primary cause of missed visits and is the most direct driver of product outcome 1) is rated Low because coordinators "already manage it via phone" - meaning it does not represent incremental revenue.

This ranking inverts the actual prioritization. The output that matters most to the customer lands in Quadrant III (Deprioritize). The output that serves the finance team lands in Quadrant II (Plan Carefully).

### The Fix

Reframe the value axis before any classification begins: "Value means customer value. What does each output allow the customer to achieve that they cannot achieve today, or cannot achieve as reliably?"

Then return to the Outcome Tree. Product outcome 1 (care coordinators confirm same-day schedule changes before aides depart) is the reference point. For each output, ask: does this output drive progress toward that outcome for care coordinators or home health aides?

- Conflict detection dashboard: yes, directly
- Real-time schedule change alert: yes, directly, and at lower cost
- Billing system integration: no - it serves finance, not care coordinators

The revised quadrant placements match the strong example above. The drift occurred because the PM brought a revenue-attribution lens to a customer-value exercise. Catching this early - before cost estimates are done and stakeholders are aligned - saves a planning cycle.
