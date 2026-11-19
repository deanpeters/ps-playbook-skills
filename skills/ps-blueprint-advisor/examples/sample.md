# Worked Examples: ps-blueprint-advisor

Three examples in one operational domain, following the Productside three-example pattern: a strong Navigate diagnosis, a weak one, and a named drift-bug. Same scenario throughout so the failure modes are isolable.

**Domain and scenario (constant across all three):** A field service software company sells dispatch and work-order software to HVAC service businesses. The customer is the dispatcher who assigns technicians to jobs. The team shipped a route-optimization feature ten weeks ago to 60 accounts. Adoption is flat and two mid-size accounts have hinted they may not renew. Leadership wants a "v2 route-optimization roadmap" next week.

---

## Strong Example

**Advisor:**

First, the customer here is the **dispatcher**, not a software engineer, and the team is a product team serving service businesses, so the diagnosis stays in the dispatcher's workflow.

You are in **Deliver**, straddling back into **Discover + Investigate**. You have a live feature producing signal (Deliver), but flat adoption plus renewal risk means the problem this feature was meant to solve is not settled (Discover).

*What good looks like in Deliver:* evaluate post-launch metrics and make a reinvest-or-retire decision, and keep discovery continuous. You are doing the first half, not the second.

*What bad looks like here:* jumping to a v2 roadmap before you know why dispatchers are not adopting route optimization. That is treating a roadmap as the answer to a question you have not asked.

*Governing principle:* **Feedback Driven** (Learning Never Stops). Flat adoption is the feedback. A v2 built before you understand it is a guess with a timeline.

*Next plays:*
1. `ps-measuring-outcomes` to separate whether this is a discovery problem (dispatchers do not want it), an activation problem (they cannot find or trust it), or a wrong-segment problem.
2. `ps-empathy-interviews` with three low-adoption dispatchers this week, because the usage data will not tell you why they route by hand.
3. Only then `ps-outcome-roadmap` for the v2, anchored to a measured dispatcher outcome, not a feature list.

**Why it works:** it confirms the real customer before diagnosing, names both phases honestly rather than forcing one, cites the canonical principle before the tactic, and routes to real ps- plays each with a reason.

---

## Weak Example

**Advisor:**

You are in **Create**, since you need a v2 roadmap. Run `ps-outcome-roadmap` to lay out the next quarter of route-optimization features, and use a prioritization pass to rank them. That will give leadership what they asked for.

**Why it fails:** plausibly wrong, not obviously bad. It accepts leadership's framing ("we need a roadmap") as the phase call and lands on Create, when the flat adoption and renewal risk put the team in Deliver looping into Discover. It never asks why adoption is flat, so it routes straight to planning on top of an unvalidated feature. The failure mode is **taking the requested deliverable as the diagnosis** instead of diagnosing the situation. Fix direction: diagnose from the situation (adoption, renewal risk), not from the artifact the stakeholder named.

---

## Drift Bug: Phase-Level Principle Asserted as Canonical

**Advisor:**

You are in Deliver moving into Discovery. The principle that applies here is **Health Is Managed Proactively**, so watch your adoption and retention metrics closely, and also **Learning Never Stops** and **Customer Advocacy Is Ongoing**. Keep an eye on all three as you plan v2.

**Why it fails and how it differs from the weak example:** the phase call is actually right, so this is not the weak example's mistake. The failure is different and more specific. It cites three **phase-level** principles (Health Is Managed Proactively, Customer Advocacy Is Ongoing) as if they were the operative principles, and never grounds them in the canonical five. This is the exact drift the skill exists to prevent: principles multiply, the memorable five vanish, and the advice becomes an unmemorable list. Named failure mode: **principle proliferation, five ignored.** Fix direction: lead with the canonical principle, **Feedback Driven**, then, only if useful, note its phase expression (Learning Never Stops). One principle named correctly beats three named loosely.
