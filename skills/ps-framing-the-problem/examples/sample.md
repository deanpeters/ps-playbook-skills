# Framing the Problem - Examples

## Example 1: Strong Productside-Style Problem Frame

Scenario: A construction technology company building a project scheduling platform for commercial general contractors managing multi-trade coordination on large jobsites.

```markdown
# Framing the Problem

## Product Context

- Product or service: BuildSync - commercial construction project scheduling platform
- Target market segment: Commercial general contractors (projects $10M-$100M)
- Primary persona (the customer with the problem): Senior Project Superintendent

## 1. Problem Framing

**I am:**
A Senior Project Superintendent managing 4-6 active trades on a commercial jobsite. Coordinating daily work sequences across concrete, mechanical, electrical, and finishing crews. Relying on paper-based logs, phone calls, and weekly coordination meetings that are outdated before they end.

**Trying to:**
Keep all trades progressing on schedule without conflicts, so the project delivers on time and within the liquidated damages window.

**But:**
Trade schedule conflicts are discovered on-site rather than in advance, causing crews to stand idle or rework completed sections. Change orders cascade unpredictably across the critical path.

**Because:**
Each trade subcontractor maintains their own schedule independently, and there is no shared view of interdependencies until crews physically arrive and find conflicts on the ground.

**Which makes me feel:**
Constantly behind, unable to stay ahead of problems despite 14-hour days on-site, and worried that schedule slips will damage my reputation with the owner and my firm's leadership.

## 2. Context and Constraints

Commercial construction operates under contractual milestone deadlines with liquidated damages for delays. Trade subcontractors are independent companies with limited technology adoption. Jobsite connectivity is unreliable. The superintendent's authority is coordination-based, not contractual - they cannot direct subcontractor labor.

## 3. Final Problem Statement

I am a Senior Project Superintendent coordinating multiple trades on a commercial jobsite using disconnected, manual scheduling methods. Trying to keep all trades progressing without conflicts and deliver on time. But schedule conflicts are discovered on-site, causing idle crews and rework. Because each subcontractor maintains their own schedule with no shared view of interdependencies. Which makes me feel constantly behind and anxious about my professional reputation.

## Evidence Notes (optional)

- Discovery sources: Interviews with three superintendents at Southeast commercial GCs, jobsite shadowing (2 days).
- Well-supported: Trade coordination friction, on-site conflict discovery, paper-based scheduling.
- Still assumption: Liquidated damages anxiety is inferred from contract language, not directly stated by interviewees.
- Next steps: Interview a subcontractor project manager to validate their side of the coordination gap.
```

### Why This Works

- **All five stems present and in order.** The sequence builds logically: who they are, what they want, what blocks them, why, and how it feels.
- **Customer perspective throughout.** Every stem is written from the superintendent's point of view. The product team is never mentioned.
- **Barriers are concrete.** "Trade schedule conflicts are discovered on-site" is specific and observable. Not "things are challenging" or "there are issues."
- **Root cause goes deeper than the barrier.** The barrier is on-site conflict discovery. The root cause is independent scheduling with no shared view. These are different things.
- **Emotional stem is specific.** "Constantly behind" and "worried about reputation" are concrete emotions with context. Not just "frustrated."
- **Constraints are separate from barriers.** Liquidated damages, subcontractor independence, and jobsite connectivity are external conditions, not things blocking the superintendent's day-to-day work.
- **Final statement synthesizes cleanly.** Every element traces back to a stem. No new information. A manager could read it alone and understand the problem.
- **No solution language.** The frame does not mention the product, features, dashboards, or tools. It describes the problem as it exists today.
- **Fits the template.** Each stem is within its word budget. The artifact is paste-ready.

---

## Example 2: Weak Generic Problem Frame

Same scenario, written poorly.

```markdown
# Framing the Problem

## Product Context

- Product or service: Construction scheduling solution
- Target market segment: Construction
- Primary persona (the customer with the problem): Construction Manager

## 1. Problem Framing

**I am:**
A construction professional dealing with scheduling challenges in a complex environment.

**Trying to:**
Improve project outcomes and efficiency across all workstreams.

**But:**
Current processes are inefficient and outdated, creating various challenges for the team.

**Because:**
The industry has been slow to adopt modern technology solutions.

**Which makes me feel:**
(not included)

## 2. Context and Constraints

Construction is a large and complex industry with many stakeholders and regulatory requirements.

## 3. Final Problem Statement

Construction managers face scheduling challenges due to outdated processes and slow technology adoption. A modern platform could streamline coordination and improve project outcomes, helping teams work more efficiently and meet deadlines.
```

### Why This Fails

- **"I am" is generic.** "A construction professional dealing with scheduling challenges" could describe anyone. No role specificity, no concrete experience points, no evidence of real customer understanding.
- **"Trying to" is vague.** "Improve project outcomes and efficiency" is a corporate platitude, not a customer's desired outcome. What outcomes? What efficiency? What does success look like to this person?
- **"But" is empty.** "Current processes are inefficient and outdated" says nothing specific. What processes? Inefficient how? What actually breaks or fails?
- **"Because" blames the industry.** "Slow to adopt technology" is an external observation, not a root cause. Why are schedules disconnected? Why do conflicts happen on-site? The root cause should explain the mechanism.
- **"Which makes me feel" is missing entirely.** The emotional stem was skipped, removing the human dimension. Leadership sees a process problem but has no sense of severity.
- **Constraints are one vague sentence.** No specific regulatory, contractual, or technology constraints are named.
- **Final statement contains solution language.** "A modern platform could streamline coordination" is a solution pitch, not a problem statement. The problem frame has become a product justification.
- **Nothing is paste-ready.** The content is too vague to act on and too generic to present to governance.

---

## Example 3: Drift Bug - Frame Written from the Product Team's Perspective

```markdown
## 1. Problem Framing

**I am:**
A product team building a scheduling platform for the construction industry. We have been investigating the market for six months and have identified significant opportunities in the commercial GC segment.

**Trying to:**
Build a differentiated scheduling product that captures market share from legacy tools and positions us as the innovation leader in construction technology.

**But:**
Our competitors have a head start in the market and existing customer relationships are difficult to break. Our engineering team is small and we cannot build all features at once.

**Because:**
The construction technology market is fragmented and buyers are risk-averse, making it hard to gain traction with a new entrant.

**Which makes me feel:**
Under pressure to show traction before the next board meeting and concerned about runway if we do not close enterprise deals soon.
```

### Why This Is Wrong

Every stem is written from the product team's perspective instead of the customer's:

- **"I am" describes the team, not the customer.** The persona is "a product team," not the superintendent or project manager who experiences the problem. The problem frame should document the customer's world, not the team's go-to-market challenges.
- **"Trying to" is a business objective.** "Capture market share" and "position as innovation leader" are company goals, not customer outcomes. The customer is trying to keep trades on schedule and avoid liquidated damages - they do not care about the product team's competitive positioning.
- **"But" lists the team's competitive barriers.** "Competitors have a head start" and "engineering team is small" are the team's problems, not the customer's. The customer's barriers are about schedule conflicts and manual coordination.
- **"Because" explains market dynamics.** Market fragmentation and buyer risk-aversion are business analysis, not root causes for the customer's problem.
- **"Which makes me feel" captures team anxiety.** "Board meeting pressure" and "runway concerns" are the founders' emotions, not the customer's. The customer feels behind, overwhelmed, and worried about their professional reputation.

**Fix:** Rewrite every stem from the customer's point of view. Ask: who uses this product in the field? What is their day like? What frustrates them? The problem frame documents their experience, not the team's business case. If the team needs to document their own competitive challenges, that belongs in a strategy doc, not in a problem frame.
