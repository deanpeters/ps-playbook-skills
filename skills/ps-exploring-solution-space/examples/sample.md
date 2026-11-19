# Exploring the Solution Space - Examples

## Example 1: Strong Session Plan

Scenario: A fleet management company building a predictive maintenance platform for regional fleet managers at a mid-size trucking company.

### Session Plan

```markdown
# Exploring the Solution Space: Session Plan

## Product Context

- Product or service: FleetSense - predictive maintenance platform for commercial trucking
- Target market segment: Mid-size regional trucking fleets (200-500 vehicles)
- Target customer (the person the product serves): Regional Fleet Manager

## Validated Problem Statement

"I am a regional fleet manager overseeing 300+ vehicles across 8 depots. I am trying to minimize unplanned breakdowns that strand drivers and delay deliveries. But I rely on scheduled maintenance intervals and driver-reported issues, which miss emerging mechanical failures. Because there is no way to detect early warning signs across the fleet without physically inspecting each vehicle. Which makes me feel anxious every morning that today will be the day a truck breaks down on a highway with a full load."

## Session Parameters

### Goals and Objectives

1. Using design thinking methods, ideate at least 15 solution possibilities that address early detection of mechanical failures across a distributed fleet
2. Prioritize ideas against two criteria: impact on reducing unplanned breakdowns and feasibility with current fleet hardware
3. Paper-prototype the top candidate to test whether a depot manager can understand the alert workflow in under 2 minutes

### Participants

| Name / Role | Function | Perspective They Bring |
|-------------|----------|----------------------|
| Maria Chen (PM) | Product | Facilitator; owns the problem definition and roadmap context |
| Derek Williams | UX Design | User workflow and interface feasibility; depot manager mental models |
| Priya Nair | Engineering | Sensor data and telemetry constraints; what is technically feasible today |
| Tom Ramirez | Customer Success | Direct depot manager relationships; hears their complaints weekly |
| Sandra Lee | Fleet Operations SME | 12 years as a fleet manager; understands the daily reality of maintenance scheduling |
| James Park | Data Science | Predictive model capabilities; what patterns telemetry data can reveal |

### Session Resources Needed

- Collaboration tool: Mural board (template pre-built with problem statement and method sections)
- Meeting setup: Conference room with large screen for Mural; video bridge for Sandra (remote)
- Time allocated: 2.5 hours (including 15-minute break)
- Pre-work for participants: Read the validated problem statement and empathy interview summary (shared via email 3 days before session)
- Documentation plan: James takes notes in Mural during session; Maria writes up outcomes within 24 hours

### Notes

- Sandra (Fleet Operations SME) is remote from the Dallas depot; ensure she has Mural access and a working camera
- May need a follow-up session for deeper prototyping if the first prototype raises new questions
- Session outcomes feed directly into the Solution Hypothesis Statement, scheduled for next sprint planning

## Method Selection

| # | Method | Activity Type | Selected? |
|---|--------|--------------|-----------|
| 1 | How Might We? | Generating Ideas | [x] |
| 2 | "Bad Ideas" First Brainstorming | Generating Ideas | [ ] |
| 3 | Quantity Over Quality | Generating Ideas | [x] |
| 4 | Mind Mapping | Generating Ideas | [ ] |
| 5 | 2x2 Matrix | Prioritizing Ideas | [x] |
| 6 | Dot Voting | Prioritizing Ideas | [ ] |
| 7 | Money Voting | Prioritizing Ideas | [ ] |
| 8 | 6-3-5 Method | Generating + Prioritizing | [ ] |
| 9 | SCAMPER | Generating + Prioritizing | [ ] |
| 10 | Prototyping | Testing | [x] |
| 11 | Customer Journey Maps | Generating + Testing | [ ] |

### Selected Method Details

#### Method: How Might We?

- **Activity type:** Generating Ideas
- **Why this method fits this session:** Reframes the validated problem statement into multiple solution angles. The problem has several dimensions (detection, communication, workflow) and HMW questions will help the team see each one as a separate opportunity.
- **Time needed:** 20 minutes
- **Setup instructions:** Pre-write the core problem statement on the Mural board. Prepare 3-4 starter HMW reframes as examples.
- **Facilitation flow:**
  1. Read the problem statement aloud (2 min)
  2. Each participant writes HMW questions individually on sticky notes (8 min)
  3. Share and cluster similar HMW questions on the board (10 min)
- **Expected output:** 12-20 HMW questions clustered into 3-5 themes
- **Common facilitation mistakes to avoid:** Do not let HMW questions become solution statements ("HMW build a dashboard" is a solution, not a question). Keep them open-ended.
- **How the output feeds the next method:** HMW clusters become the prompt categories for Quantity Over Quality ideation.

#### Method: Quantity Over Quality

- **Activity type:** Generating Ideas
- **Why this method fits this session:** The team has strong analytical tendencies (data science, engineering). This method deliberately suppresses evaluation and pushes for volume, which counteracts the team's instinct to filter too early.
- **Time needed:** 25 minutes
- **Setup instructions:** Set a target of 50 ideas total across the team. Put a visible timer on screen. Each HMW cluster gets its own column on the Mural board.
- **Facilitation flow:**
  1. Assign each HMW cluster to the board (2 min)
  2. Set timer for 15 minutes; everyone writes ideas silently on sticky notes (15 min)
  3. Quick read-through of all ideas, no discussion or evaluation (8 min)
- **Expected output:** 40-60 raw solution ideas across all HMW clusters
- **Common facilitation mistakes to avoid:** Do not allow discussion or critique during the generation phase. If someone says "that won't work," redirect: "Write it down anyway."
- **How the output feeds the next method:** The raw list of 40-60 ideas becomes the input for 2x2 Matrix prioritization.

#### Method: 2x2 Matrix

- **Activity type:** Prioritizing Ideas
- **Why this method fits this session:** The team needs to evaluate ideas against two dimensions that matter for this problem: (1) impact on reducing unplanned breakdowns, and (2) feasibility given current fleet hardware and sensor capabilities.
- **Time needed:** 30 minutes
- **Setup instructions:** Draw the 2x2 grid on the Mural board. Label axes: X = Feasibility with current fleet hardware, Y = Impact on reducing unplanned breakdowns. Pre-define what "high" and "low" mean for each axis.
- **Facilitation flow:**
  1. Review the two axes and definitions (5 min)
  2. As a group, place each idea on the matrix; brief discussion per idea (20 min)
  3. Identify the top 3-5 ideas from the high-impact, high-feasibility quadrant (5 min)
- **Expected output:** 3-5 prioritized solution ideas with the team aligned on why they rank highest
- **Common facilitation mistakes to avoid:** Do not spend more than 1-2 minutes debating placement of any single idea. If there is disagreement, place it at the boundary and move on.
- **How the output feeds the next method:** The top-ranked idea becomes the subject for paper prototyping.

#### Method: Prototyping

- **Activity type:** Testing
- **Why this method fits this session:** The top idea needs a quick reality check before the team commits. A paper prototype of the alert workflow will reveal whether a depot manager can understand it without training.
- **Time needed:** 35 minutes
- **Setup instructions:** Prepare blank paper, markers, and sticky notes (physical or Mural equivalents). Sandra (the fleet operations SME) will role-play the depot manager receiving the alert.
- **Facilitation flow:**
  1. Derek sketches 3-4 screens or steps of the alert workflow (10 min)
  2. Sandra walks through the prototype as if she received the alert at her desk (10 min)
  3. Team observes and notes where Sandra hesitates, asks questions, or gets confused (during walkthrough)
  4. Debrief: what worked, what confused, what is missing (15 min)
- **Expected output:** A validated or revised alert workflow concept with specific feedback from a domain expert
- **Common facilitation mistakes to avoid:** Do not explain the prototype to Sandra before she tries it. Let her figure it out. The confusion is the data.
- **How the output feeds the next method:** Prototype feedback informs the Solution Hypothesis Statement.
```

### Why This Works

- **The problem statement is present and specific.** Every session goal connects back to "reducing unplanned breakdowns across a distributed fleet." The team knows exactly what problem they are solving.
- **Participants are cross-functional.** Engineering and data science are present, but so are UX design, customer success, and an actual fleet operations expert. The fleet SME brings the customer perspective into the room.
- **Methods cover all three activity types.** Generating (How Might We + Quantity Over Quality), Prioritizing (2x2 Matrix), and Testing (Prototyping). The team will not leave with just a list of ideas; they will leave with a tested concept.
- **Methods are sequenced correctly.** Diverge first (HMW, then Quantity Over Quality), converge (2x2 Matrix), then test (Prototyping). Each method's output feeds the next.
- **Time is realistic.** 2.5 hours for four methods, including a break. Each method has a specific time allocation that adds up correctly.
- **Pre-work is defined.** Participants will arrive having read the problem statement and interview summary, so the session does not waste 30 minutes on context-setting.
- **Facilitation guidance is concrete.** Each method includes step-by-step instructions, time budgets, and common mistakes. The PM can run this session even if they have never facilitated a design thinking workshop before.

---

## Example 2: Weak Session Plan

Same scenario, written poorly.

### Session Plan (Weak)

```markdown
# Exploring the Solution Space: Session Plan

## Product Context

- Product or service: Fleet maintenance tool
- Target market segment: Trucking
- Target customer: Fleet manager

## Validated Problem Statement

Trucks break down and it's a problem.

## Session Parameters

### Goals and Objectives

1. Brainstorm solutions

### Participants

| Name / Role | Function | Perspective They Bring |
|-------------|----------|----------------------|
| Priya Nair | Engineering | Backend architecture |
| James Park | Data Science | ML models |
| Alex Kim | Engineering | Frontend development |
| Wei Zhang | Engineering | DevOps and infrastructure |

### Session Resources Needed

- Collaboration tool: Zoom call
- Meeting setup: Regular standup time slot
- Time allocated: 30 minutes
- Pre-work for participants: None
- Documentation plan: Someone will take notes

### Notes

(none)

## Method Selection

| # | Method | Activity Type | Selected? |
|---|--------|--------------|-----------|
| 1 | How Might We? | Generating Ideas | [ ] |
| 2 | "Bad Ideas" First Brainstorming | Generating Ideas | [ ] |
| 3 | Quantity Over Quality | Generating Ideas | [x] |
| 4 | Mind Mapping | Generating Ideas | [ ] |
| 5 | 2x2 Matrix | Prioritizing Ideas | [ ] |
| 6 | Dot Voting | Prioritizing Ideas | [ ] |
| 7 | Money Voting | Prioritizing Ideas | [ ] |
| 8 | 6-3-5 Method | Generating + Prioritizing | [ ] |
| 9 | SCAMPER | Generating + Prioritizing | [ ] |
| 10 | Prototyping | Testing | [ ] |
| 11 | Customer Journey Maps | Generating + Testing | [ ] |

### Selected Method Details

#### Method: Quantity Over Quality

- **Activity type:** Generating Ideas
- **Why this method fits this session:** Good for brainstorming.
- **Time needed:** 30 minutes
- **Setup instructions:** Open a shared doc.
- **Facilitation flow:**
  1. Everyone writes ideas
- **Expected output:** A list of ideas
- **Common facilitation mistakes to avoid:** None noted
- **How the output feeds the next method:** N/A (only one method)
```

### Why This Fails

- **No real problem statement.** "Trucks break down and it's a problem" is not a validated problem statement. It gives the team no direction for ideation. Solutions generated from this are solving a generic complaint, not a specific customer pain.
- **Session goal is too vague.** "Brainstorm solutions" has no measurable outcome, no connection to the problem, and no way to tell if the session succeeded.
- **Participants are all engineers.** No design, no customer success, no fleet operations expertise. The session will produce technically interesting ideas that may have no connection to what fleet managers actually need.
- **30 minutes is not enough.** Barely enough time for introductions and one round of ideation. No time to prioritize, no time to test, no time to discuss.
- **Only one method from one category.** Generating ideas with no plan to prioritize or test them. The team will leave with a list of ideas and no criteria to evaluate which ones are worth pursuing.
- **No pre-work.** Participants arrive cold, so the first 10 minutes are spent explaining the context, leaving 20 minutes for actual work.
- **No documentation plan.** "Someone will take notes" means nobody will. Session outcomes will be lost.
- **No facilitation flow.** "Everyone writes ideas" is not facilitation guidance. There are no time limits, no rules about suspending judgment, no structure for sharing or discussing.

---

## Example 3: Drift Bug - Asking the Agent to Generate Solutions

This example shows a common misuse pattern where the PM skips session preparation entirely.

### The Interaction

```
PM: "I have a validated problem statement about fleet managers not being able to
detect mechanical failures early. Can you brainstorm 10 solution ideas for me?"

Agent: [Should NOT generate solutions. Should redirect to session planning.]
```

### What the PM Expects

The PM expects the agent to act as a brainstorming partner, generating a list of solution concepts (e.g., "IoT sensor dashboard," "predictive maintenance alerts," "driver mobile app") that the PM can evaluate and select from.

### Why This Is Wrong

This skips the entire purpose of Exploring the Solution Space. The skill exists to help the PM plan a **team session** where diverse perspectives generate, evaluate, and test ideas together.

When the agent generates solutions:

- **The ideas come from training data, not from the team.** The agent has no access to the engineering team's knowledge of sensor capabilities, the customer success team's understanding of depot workflows, or the fleet SME's practical experience with maintenance scheduling.
- **The team has no ownership.** Ideas generated by an AI tool feel like assignments, not like creative contributions. The team builds on and champions ideas they generated themselves.
- **Divergent thinking is short-circuited.** A single AI response cannot replicate the generative energy of six people building on each other's ideas in real time. The 6-3-5 method works because Person B reads Person A's idea and sees something Person A did not. That iterative building cannot happen with agent-generated lists.
- **Prioritization is hollow.** If the PM asks the agent to also rank the ideas, the ranking reflects training data patterns, not the team's specific context, constraints, and strategic priorities.

### The Correct Response

```
Agent: "I can help you plan a design thinking session to explore solutions with
your team, but I should not generate the solutions for you. The value of this
step comes from your cross-functional team generating, prioritizing, and testing
ideas together.

Let me help you prepare:
- What is your validated problem statement? (You mentioned fleet managers and
  mechanical failure detection.)
- Who should be in the room for this session?
- What collaboration tools does your team use?

We will select methods from the Productside catalog that fit your team size and
available time, and I will provide facilitation guidance for each method."
```

### The Deeper Pattern

This drift bug is not unique to this skill. It appears whenever a process skill is involved:

- In ps-empathy-interviews, the PM asks the agent to "generate interview findings" without conducting an interview
- In ps-exploring-solution-space, the PM asks the agent to "brainstorm solutions" without running a session
- In both cases, the agent produces plausible-sounding output that has no grounding in reality

The guard is the same: the agent helps **prepare** and **document**, but the actual human activity (interviewing, brainstorming, facilitating) cannot be replaced.
