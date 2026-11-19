# ps-process-retrospective Examples

Three examples using a field service dispatch product launch scenario.

---

## Example 1: Strong

**Commentary on what makes this work:**

- All four quadrants have 3-5 specific, short items. No abstractions.
- Anchors names system and process failures, not individuals.
- Beacons gives the team a concrete positive forward pull.
- Action items follow the [Owner] will [action] by [date] format exactly.
- The roster is complete - everyone who did the work is listed.

---

**Retrospective For:** FieldRoute Dispatch Mobile Launch - Q3

**Date:** October 14, 2025

**Point of Contact:**

| Role | Name and Title | Other |
|------|---------------|-------|
| Project Manager | Marcus Tran, Senior PM | Also coordinating Q4 follow-on |
| Executive Sponsor | Dana Holloway, VP Product | Sign-off authority |
| Product Manager | Priya Saini, PM | Lead for the launch |
| Sales | James Okafor, Regional Sales Lead | |
| Marketing | Yuki Flores, Product Marketing | |
| Communications | n/a | Not applicable for this launch |
| Operations | Remi Osei, Field Ops Manager | |
| Customer Support | Taryn Wu, Support Lead | |
| Release Engineer | Carl Ibarra, Platform Engineer | |
| Legal | n/a | Pre-cleared in May |

**Action Items:**

- Priya will schedule bi-weekly sync with logistics lead by Oct 20 to prevent routing integration delays in Q4.
- Marcus will add a rollback criteria checklist to the deployment runbook before the Nov 1 release window.
- Taryn will document the top 5 dispatcher support questions and circulate to the full team by Oct 28.

---

**Wind in Our Sails:**

- Dispatcher beta group gave strong adoption signal
- Routing accuracy improved from 71% to 88%
- Sales closed two enterprise accounts citing mobile parity
- Cross-functional sync cadence held weekly without gaps
- Support ticket volume was lower than Q2 projections

**Beacons on the Horizon:**

- Q4 push into Midwest market segment
- Real-time traffic routing module scheduled for Jan release
- Net Promoter Score target of 42 by year-end
- Enterprise renewal cycle starts in February

**Anchors Holding Us Back:**

- Logistics API integration was scoped without logistics team input
- Deployment window was set before rollback criteria were defined
- Dispatcher training materials were finalized two days before launch
- Support team received no preview access prior to go-live
- Routing edge cases for rural zones were not in the test plan

**Barriers We See Ahead:**

- Midwest rollout will require dispatcher re-training at 14 sites
- Legacy CAD integration not resolved before Q4 target date
- Platform team is at capacity through December
- Holiday freeze window conflicts with planned Jan release

---

## Example 2: Weak

**Commentary on why this fails:**

- Wind in Our Sails has 5 items; Anchors has 1 vague item ("things were sometimes hard"). That ratio signals a psychological safety problem - the team performed positivity, not reflection.
- Beacons is empty. The team ends with a clear picture of past wins but no forward pull.
- Action items say "improve things going forward" - no owner, no specific action, no date. These are not action items; they are aspirations.
- Items are written as abstractions ("communication could be better") rather than specific observations.

---

**Retrospective For:** FieldRoute Dispatch Mobile Launch

**Date:** October 14, 2025

**Point of Contact:**

| Role | Name and Title | Other |
|------|---------------|-------|
| Project Manager | Marcus Tran | |
| Product Manager | Priya Saini | |
| (others not listed) | | |

**Action Items:**

- Improve things going forward
- Make sure communication is better next time
- Try to avoid the problems we had

---

**Wind in Our Sails:**

- Launch went pretty well overall
- Team worked hard
- Customers seemed happy with the app
- Beta went smoothly
- Good collaboration

**Beacons on the Horizon:**

*(left blank)*

**Anchors Holding Us Back:**

- Things were sometimes hard during the launch

**Barriers We See Ahead:**

- Some things might be challenging in Q4

---

**Why these action items fail:** "Improve things going forward" has no owner. No one is responsible for it, no one can mark it done, and it will appear unchanged at the next retro. "Make sure communication is better" names a category, not a change. A good action item names who does what specific thing by when.

**Why the Anchors quadrant fails:** "Things were sometimes hard during the launch" is not an observation - it is a feeling. It cannot be acted on. The team clearly experienced something concrete (the logistics API scope miss, the late training materials, the support team being caught flat-footed) but did not name it. That means the retro will not produce the fix.

**Why the empty Beacons quadrant is a problem:** The team now has a record of what went well and a vague acknowledgment that something was hard. It has no shared picture of what to work toward. That asymmetry - full rear-view, empty windshield - can leave a team feeling like the retro only surfaced the negative without giving them anything to move toward.

---

## Example 3: Drift Bug - Process Skill Boundary Violation

**The drift:** The PM runs the retrospective alone and then asks the agent to fill in the quadrants based on the project description and timeline documents.

---

**PM prompt:**

"I have attached the project timeline, the launch brief, and the post-launch metrics report. Based on these, can you fill in all four quadrants for me? I can review and approve."

---

**What the agent correctly says:**

"I can help you prepare and document this retrospective, but I cannot fill in the quadrants from the documents you have shared - and doing so would undermine what the retro is for.

The four quadrants need to come from the people who did the work. The Wind in Our Sails items should reflect what the team actually experienced as momentum - not what the metrics report shows as positive. The Anchors items especially need to come from the team, because the most important failures are often the ones that do not appear in the timeline or the metrics - the frustrating process gaps, the near-misses, the things that cost time but did not show up as a missed milestone.

If I fill this in from the documents, you will have a retrospective artifact that reflects the written record of the project - not the lived experience of the team. That is a different thing, and it is less useful.

Here is what I can do right now:

1. Set up the full template with your roster, date, and scope.
2. Write the discussion prompts for each quadrant so you have everything you need to run a 45-minute session with the team.
3. When the session is done, you share the raw notes from each quadrant and I will help you compress them into paste-ready items and format the action items with owners and dates.

Want to start with the session setup?"

---

**Why this is the right response:**

The process skill boundary is not a technicality - it is the point. The value of a retrospective is that the team surfaces what it experienced, not what the documents show. The agent substituting for that conversation produces a document, not a retrospective. The agent's job is to make the real session easier and to document its output faithfully - not to replace it.

This is the same boundary that applies to ps-empathy-interviews: the agent can prepare and document, but it cannot conduct the interview. The same logic holds here: the agent can prepare and document, but it cannot run the team session.
