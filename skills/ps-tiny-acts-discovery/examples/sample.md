# Tiny Acts of Discovery - Sample Examples

Three examples using a field services scenario: a mobile dispatch and job management platform for HVAC technicians and their dispatchers at a commercial facilities management company.

---

## Example 1: Strong

**Product:** ServiceFlow - mobile job management platform for HVAC technicians
**Customer:** HVAC field technicians (primary) and dispatch coordinators (secondary)
**Date:** March 14
**Participants:** Priya Nair (PM), Marco Santos (UX Research), Deb Okonkwo (Engineering Lead)

---

### Step 1: What Do We Know?

| What We Know | Source |
|---|---|
| Technicians currently receive job assignments via text message and a shared whiteboard at dispatch | Field observation, 3 sites, Feb 12-14 |
| Average time from job assignment to technician departure is 22 minutes under current system | Dispatch log analysis, 90-day pull, Feb 28 |
| 6 of 8 technicians interviewed said they call dispatch at least twice per job for parts availability information | Empathy interviews, Feb 7-9 |
| Dispatchers use two separate tools (CRM and a paper log) to track technician location and job status | Field observation, Feb 13 |
| Management requires job completion sign-off within 2 hours of finish for billing; 34% of jobs currently miss this window | Billing data pull, Q4 review |

---

### Step 2: What Do We Not Know?

- Will technicians use a mobile app mid-job or will they default to calling dispatch even when the app is available? (behavioral)
- Do technicians have reliable cellular coverage in the mechanical rooms and basements where most HVAC equipment lives? (technical)
- Will dispatchers trust the app's real-time location data enough to stop calling technicians for status updates? (adoption/behavioral)
- Does the facilities management company have a device procurement policy that controls what phones technicians can use? (organizational)
- Will commercial clients accept digital sign-off instead of a paper signature for billing compliance? (market/compliance)
- How do technicians currently handle parts shortages mid-job and would they use an in-app parts request if it existed? (behavioral)

---

### Step 3: Prioritize Your Assumptions

| Assumption | Impact (H/M/L) | Uncertainty (H/M/L) | Priority |
|---|---|---|---|
| Technicians will use the app mid-job rather than calling dispatch | H | H | Urgent |
| Commercial clients will accept digital sign-off for billing compliance | H | H | Urgent |
| Dispatchers will trust real-time location data and reduce status calls | M | H | High |
| Cellular coverage is adequate in mechanical rooms and basements | H | M | High |
| Company device policy controls which phones technicians can use | M | M | Medium |
| Technicians would use an in-app parts request mid-job | M | M | Medium |

---

### Step 4: Form Your Hypotheses

**Hypothesis 1** (for: Technicians will use the app mid-job rather than calling dispatch)

> If we give 5 technicians a working prototype of the job detail screen and ask them to complete a simulated mid-job workflow, then at least 4 of 5 will complete the task without asking for help or reverting to their phone call habit, because the key information they currently call for (parts list, customer contact, job notes) will be visible on a single screen.

**Hypothesis 2** (for: Commercial clients will accept digital sign-off for billing compliance)

> If we show the current sign-off workflow and a proposed digital alternative to 3 facilities managers at existing client sites, then at least 2 of 3 will confirm that a digital signature meets their internal audit and billing requirements, because commercial facilities contracts typically specify signature capture but not medium.

**Hypothesis 3** (for: Dispatchers will trust real-time location data and reduce status calls)

> If we shadow a dispatcher for one full shift while they have access to a live map view of technician locations, then the dispatcher will initiate at least 30% fewer inbound status calls compared to their baseline, because the map resolves the most common reason they call (checking whether a technician has left the previous job site).

---

### Step 5: List Your Tiny Acts of Discovery

| Hypothesis | Tiny Act of Discovery | Measure / Metric to be Collected | Assigned |
|---|---|---|---|
| Hypothesis 1 | Moderated usability walkthrough with 5 technicians using a clickable Figma prototype of the job detail screen. Present 3 mid-job task scenarios. | Task completion rate without researcher assistance. Target: 4 of 5 complete all 3 tasks without asking for help or reaching for their phone. | Marco Santos |
| Hypothesis 2 | 30-minute structured conversation with 3 facilities managers at current client sites. Present current paper process and proposed digital flow side by side. Ask directly about their audit and compliance requirements. | Number of managers who confirm digital capture meets their billing and audit standards. Target: 2 of 3 say yes without requiring additional approval steps. | Priya Nair |
| Hypothesis 3 | Shadow one dispatcher for a single full shift (8 hours) while they access a working location map fed by test devices carried by 3 volunteer technicians. Count inbound status calls during the shift and compare to the dispatcher's own estimate of their normal daily call volume. | Count of dispatcher-initiated status calls during the observed shift vs. self-reported baseline. Target: at least 30% reduction observed. | Deb Okonkwo |

**Next Steps:**
[ ] Run the three acts this sprint (week of March 17)
[ ] Return with findings to update the assumption classification
[ ] Next Tiny Acts session: April 1 (after results are in)

---

**Commentary - why this example works:**

The knowns list has real sources attached: field observations with dates, data pulls with time windows, and interview counts. Nothing on the knowns list is an assumption dressed as a fact.

The unknowns list covers four distinct categories: behavioral (will technicians use the app), compliance/market (will clients accept digital sign-off), adoption (will dispatchers trust the data), and technical (cellular coverage). It is not an all-technical list.

The classification produces a meaningful spread: two Urgent, two High, two Medium. The PM does not need to test all six at once. The top 3 are genuinely more critical than the bottom 3.

The hypotheses are specific and observable. Each THEN clause names a threshold or count. Each hypothesis is falsifiable: the test can produce a clear pass or fail signal.

The tiny acts are genuinely tiny: one 5-person usability walkthrough, three 30-minute client conversations, and one 8-hour shadow session. None of these require weeks or a research budget. All three can be completed this sprint.

---

## Example 2: Weak

**Product:** ServiceFlow - mobile job management platform for HVAC technicians
**Customer:** HVAC field technicians
**Date:** March 14
**Participants:** Priya Nair (PM)

---

### Step 1: What Do We Know?

- We know technicians are unhappy with the current process
- We know the product will save time
- We know dispatchers want better visibility
- We know customers will adopt the app because it is simpler than what they use now
- We know the market is ready for a mobile-first solution

---

### Step 2: What Do We Not Know?

- Will the API integrate with the CRM?
- Will the database scale to support 500 concurrent users?
- Will the mobile app perform acceptably on older Android devices?

---

### Step 3: Prioritize Your Assumptions

| Assumption | Impact (H/M/L) | Uncertainty (H/M/L) | Priority |
|---|---|---|---|
| API will integrate with CRM | H | H | Urgent |
| Database will scale to 500 users | H | H | Urgent |
| App will perform on older Android | H | H | Urgent |

---

### Step 4: Form Your Hypotheses

**Hypothesis 1:** If we integrate the API, then the CRM will work with the app.
**Hypothesis 2:** If we test at scale, then performance will be fine.
**Hypothesis 3:** If we optimize for Android, then it will work on all devices.

---

### Step 5: List Your Tiny Acts of Discovery

| Hypothesis | Tiny Act of Discovery | Measure / Metric to be Collected | Assigned |
|---|---|---|---|
| Hypothesis 1 | Full CRM integration build and QA cycle | TBD | Team |
| Hypothesis 2 | Load testing infrastructure setup | TBD | Team |
| Hypothesis 3 | Multi-device QA across 20 device types | TBD | Team |

---

**Commentary - why this example fails:**

The knowns list is almost entirely composed of beliefs and assumptions, not validated facts. "We know technicians are unhappy" - how do you know? "We know customers will adopt the app" - this is the core assumption the product needs to prove, not something to declare as known. None of the five items has a source. If the source cannot be named, the item belongs in Step 2.

The unknowns list covers only technical questions. There are no behavioral unknowns (will technicians actually use the app in the field), no adoption unknowns (will dispatchers change their habits), no organizational unknowns (device policy, sign-off compliance), and no market unknowns. This team will ship a technically sound product that fails in the field because they never tested the behavioral and organizational assumptions.

The classification inflates every assumption to Urgent. When everything is Urgent, nothing is prioritized. The team cannot decide what to test first.

The hypotheses are not testable. "The CRM will work with the app" is not a THEN clause with an observable threshold. It is a statement of hoped-for outcome.

The acts are not tiny. A "full CRM integration build and QA cycle" is not a tiny act - it is a build milestone. None of these acts can be completed in days. None of them have specific metrics. All three are assigned to "Team," which means no one owns them.

---

## Example 3: Drift Bug - The PM Asks the Agent to Run the Acts

**Scenario:** A PM has completed Steps 1 through 4 and has identified three tiny acts. They now ask the agent to run the acts on their behalf.

---

**PM:** Okay, I've got my three hypotheses. Can you just generate me 20 survey questions I can send to technicians, run a simulated usability walkthrough using your best guess of how a technician would respond, and pull some industry data showing typical dispatcher call volumes so I can use that as my baseline?

---

**Agent response:**

There are parts of this I can help with and parts that require you and your team to engage with real technicians and dispatchers directly.

**What I can help you do:**

For the survey, I can draft a set of specific, well-formed questions designed to test Hypothesis 2 (technician mid-job behavior). I can make sure the questions are behaviorally grounded, avoid leading language, and are sequenced in a way that surfaces honest responses rather than socially desirable ones. You would then send those to real technicians and share the results with me.

For the usability walkthrough, I can help you write a structured test script - the task prompts, the observation guide, and the note-taking format. Marco Santos would run the actual sessions with the 5 real technicians. I can help interpret what you observed after the sessions.

For the dispatcher baseline, I can help you design a simple self-reported baseline method: a structured question to ask the dispatcher before the shadow session that gives you their own estimate of normal daily call volume. That is more useful than industry benchmarks anyway because it is specific to this dispatcher's workflow.

**What I cannot do:**

I cannot generate synthetic technician responses as a substitute for real ones. If I simulate how a technician "would probably respond" to the usability prototype, I am inventing data. Simulated responses would tell you what I predict, not what your actual customers do - and the gap between those two things is exactly what the tiny act is designed to measure.

I cannot pull proprietary dispatcher call volume data from your organization. I can find published industry benchmarks if they exist, but using industry averages as your baseline would undermine the measurement: your dispatchers may operate very differently from the industry average, and the whole point is to measure change in their specific behavior.

**The process skill boundary:**

Tiny Acts of Discovery is a field research practice. The agent's role is to help you design the acts, sharpen the metrics, write the test scripts, and document what you learn when you return with real findings. The acts themselves require real people, real behavior, and real data.

Let's start with the survey design. What is the most important question you need those 20 technicians to answer honestly?

---

**Commentary - why this example matters:**

The PM's request is understandable. Generating survey questions and synthetic responses feels faster. But synthetic research is not research - it is a hallucination of what the agent thinks users believe. The tiny act exists precisely because the agent's prediction and the user's actual behavior often diverge.

The agent's response does three things correctly:
- It is specific about what it can help with (draft, design, structure)
- It is clear about what it cannot do and why (synthetic data, proprietary org data)
- It redirects immediately to a concrete next step rather than leaving the PM stranded

A process skill boundary is not a refusal. It is a handoff: the agent prepares, the PM runs, the agent helps interpret. Drift occurs when the agent tries to skip the middle phase.
