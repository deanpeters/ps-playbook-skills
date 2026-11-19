# ps-stakeholder-alignment Examples

All examples use a fictionalized scenario: a PM at a mid-size food distribution company building a **route optimization platform** for their logistics operations team.

---

## Example 1: Strong Stakeholder Map

This example shows a complete, balanced map with actionable engagement strategies and a meaningful risks section.

```markdown
# Stakeholder Alignment

## Context

- Initiative / product: Route Optimization Platform
- PM: Jordan Rivera
- Date: March 2026

---

## Stakeholder Table

| Name | Role / Team | Interest in This Initiative | Influence | Sentiment |
|---|---|---|---|---|
| Marcus Chen | VP Operations | Owns the cost and service KPIs this platform affects | High | Supportive |
| Linda Osei | Director of Logistics | Day-to-day owner of route planning and dispatcher teams | High | Supportive |
| Priya Mehta | IT Infrastructure Lead | Responsible for systems the platform must integrate with | High | Skeptical |
| David Russo | Finance Director | Controls capital budget and must approve tool spend over $50K | High | Neutral |
| Sandra Kowalski | Legal / Compliance | Reviewing data sharing terms with the carrier API provider | Medium | Unknown |
| Tomas Vega | Regional Warehouse Manager | Manages the sites piloting the first rollout | Medium | Supportive |
| Aisha Nkrumah | Customer Success Lead | Escalates customer complaints when delivery windows are missed | Medium | Neutral |
| Ray Park | Head of Sales | Sells delivery reliability as a competitive differentiator | Low | Supportive |
| Felix Olawale | Carrier Relations Manager | Manages contracts with the carriers whose data feeds the platform | High | Skeptical |

---

## Interest / Influence Matrix

### Manage Closely (High Influence, High Interest)
Marcus Chen, Linda Osei, Priya Mehta, Felix Olawale
- Engagement: Weekly sync with Linda and Priya for operational and technical alignment; biweekly executive brief with Marcus; dedicated working session with Felix to address carrier data concerns before pilot begins

### Keep Satisfied (High Influence, Low Interest)
David Russo
- Engagement: Monthly one-page financial summary covering projected savings, spend to date, and risk to budget; flagged immediately when scope or timeline changes affect approved spend

### Keep Informed (Low Influence, High Interest)
Sandra Kowalski, Tomas Vega, Aisha Nkrumah
- Engagement: Biweekly written update shared via email covering progress, open decisions, and pilot schedule; Sandra gets a separate heads-up on any change to carrier data handling; Tomas and Aisha invited to pilot demos

### Monitor (Low Influence, Low Interest)
Ray Park
- Engagement: Quarterly update on release milestones; notified when the platform reaches GA so Sales can update messaging

---

## Risks and Gaps

### Missing stakeholders
IT Security has not been identified yet. Any platform ingesting real-time carrier GPS and routing data will require a security review. Need to identify the right contact before vendor contracts are signed.

### Potential blockers
Felix Olawale (Carrier Relations) is skeptical because a previous integration project damaged a key carrier relationship. If he is not involved early in the API design decisions, he may raise concerns at the contract stage that delay the pilot by a quarter.

Priya Mehta (IT Infrastructure) has flagged concerns about the platform's dependency on a cloud infrastructure configuration her team does not currently support. If that is not resolved before development begins, the pilot environment may not be ready in time.

### Political dynamics
Marcus Chen and David Russo have a documented history of disagreement over technology investment. Marcus has pushed for faster modernization; David has blocked two prior initiatives on ROI grounds. Any proposal to Marcus should be framed with David's financial framing in mind, not just operational benefit.
```

**Why this works**

- the table includes skeptics (Priya Mehta, Felix Olawale) alongside supporters, which makes the map useful when friction surfaces
- influence ratings reflect actual power over this initiative, not just title (Felix, a manager-level role, is correctly rated High because of carrier relationship control)
- Finance is represented even though this is primarily an operations initiative
- engagement strategies are specific: cadence, format, and content are named for each quadrant
- the risks section names a concrete blocker with a mechanism (Felix's concern about a prior integration) and a specific consequence (a quarter delay to pilot)
- IT Security is flagged as a gap before it becomes a problem

---

## Example 2: Weak Stakeholder Map

Same initiative, same company - but the map is incomplete and the engagement strategies are too vague to act on.

```markdown
# Stakeholder Alignment

## Context

- Initiative / product: Route Optimization Platform
- PM: Jordan Rivera
- Date: March 2026

---

## Stakeholder Table

| Name | Role / Team | Interest in This Initiative | Influence | Sentiment |
|---|---|---|---|---|
| Marcus Chen | VP Operations | Interested in the project | High | Supportive |
| Linda Osei | Director of Logistics | Key stakeholder | High | Supportive |
| Tomas Vega | Regional Manager | Involved in pilot | High | Supportive |

---

## Interest / Influence Matrix

### Manage Closely (High Influence, High Interest)
Marcus Chen, Linda Osei, Tomas Vega
- Engagement: Keep them updated

### Keep Satisfied (High Influence, Low Interest)
[None identified]

### Keep Informed (Low Influence, High Interest)
[None identified]

### Monitor (Low Influence, Low Interest)
[None identified]

---

## Risks and Gaps

[None identified]
```

**Why this fails**

- only three stakeholders, all listed as Supportive - no skeptics, no blockers, no Finance or Legal
- Tomas Vega is rated High Influence, which inflates the "manage closely" quadrant without justification; his actual influence is Medium
- interest descriptions are placeholders ("interested in the project," "key stakeholder") with no content
- "Keep them updated" is not an engagement strategy - it has no cadence, format, or content
- the risks section is empty, which means the PM will be surprised by Felix Olawale and IT Security when they surface later
- three quadrants are completely empty, which signals the ratings have not been calibrated against the full stakeholder landscape

---

## Example 3: Drift Bug - Customers Listed as Stakeholders

This is a common misuse. The PM has included the end users of the route optimization platform - the people who will actually use the product in the field - inside the stakeholder table.

```markdown
## Stakeholder Table

| Name | Role / Team | Interest in This Initiative | Influence | Sentiment |
|---|---|---|---|---|
| Marcus Chen | VP Operations | Owns the KPIs this platform affects | High | Supportive |
| Linda Osei | Director of Logistics | Day-to-day owner of route planning | High | Supportive |
| Route dispatchers | Operations / Dispatch | Will use the platform daily | Medium | Unknown |
| Truck drivers | Field / Delivery | Will receive optimized routes from the system | Low | Unknown |
```

**Why this is a drift bug**

Route dispatchers and truck drivers are the customers the product serves in the field. They experience the problem the platform is solving. They need product discovery and empathy work - interviews, observations, prototype feedback.

They are not stakeholders in the organizational sense. They cannot greenlight or block the initiative. They do not need to be briefed on budget decisions or release timelines. Including them in the stakeholder table creates confusion about who needs organizational engagement vs. who needs discovery work.

The correct destination for route dispatchers and truck drivers is the persona play (ps-proto-persona), where their jobs-to-be-done, pains, and goals can be captured properly.

The stakeholder map covers the people inside the organization who affect whether the initiative succeeds. The persona play covers the people in the field who the product serves. Keep these lists separate.
