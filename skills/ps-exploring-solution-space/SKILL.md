---
name: ps-exploring-solution-space
description: >-
  Prepare a design thinking session to brainstorm and evaluate solution
  hypotheses using the Productside method catalog. Use when you have a validated
  problem statement and need to explore the solution space before committing to
  a direction, or when asked to generate solution ideas for a problem.
intent: >-
  Help a Product Manager plan and prepare a structured design thinking session
  that generates, prioritizes, and tests solution ideas for a validated problem
  statement, using the Productside method catalog of 10 ideation tools organized
  across three activity types (Generating Ideas, Prioritizing Ideas, Testing).
type: process
blueprint_stage: Discover + Define
best_for:
  - "Planning a design thinking session to brainstorm solutions for a validated problem"
  - "Evaluating multiple solution directions before committing to one hypothesis"
  - "Preparing facilitation materials for a collaborative solution exploration session"
scenarios:
  - "We have a validated problem and need to brainstorm solution directions with the team"
  - "Help me prepare a design thinking session to explore solutions for our framed problem"
---


## Purpose

Create a **Productside-style Exploring the Solution Space artifact** for your validated problem.

This skill is for the **Discover + Define** phase. It sits between problem framing and solution hypothesis. The PM has a validated problem statement and needs to come up with a few solution hypotheses to test quickly and cheaply before committing to one direction.

This is a **process skill**, not a content-fill skill. It covers session preparation:

1. **Plan** - define session goals, participants, and resources
2. **Select** - choose ideation methods from the Productside catalog, with at least one from each activity category
3. **Prepare** - produce a session plan the PM can take into the room

The agent helps prepare the session. The actual ideation session happens with the team in real time. The agent cannot substitute for cross-functional collaboration in a design thinking workshop.

Use this skill when you need to:

- explore solution possibilities for a validated problem statement
- plan a design thinking session with the right participants and methods
- select appropriate ideation tools from the Productside catalog
- ensure the session covers divergent thinking, convergent thinking, and testing
- prepare participants and resources for a productive session

This is not a solution-generation tool. The agent does not brainstorm solutions on behalf of the team. It helps the PM plan a structured session where the team generates, prioritizes, and tests ideas together.

### Usage Notes

- This is a **process skill** (`type: process`). The agent helps prepare a design thinking session; the actual ideation happens with the team in real time.
- Evidence gathering: this skill qualifies for **artifacts only**. The PM brings the validated problem statement, stakeholder alignment, and prior discovery work. No web research needed.
- The method catalog contains 10 tools from the Productside playbook organized across three activity types: Generating Ideas, Prioritizing Ideas, and Testing. A well-planned session includes at least one from each category.
- Upstream: ps-framing-the-problem (validated problem statement is required input), ps-empathy-interviews, ps-proto-persona, ps-jobs-to-be-done.
- Downstream: Solution Hypothesis Statement (the top idea from this session feeds the hypothesis).

## Key Concepts

### The Three Activity Types

The Productside catalog organizes ideation methods into three categories. A well-planned session should include at least one method from each:

**Generating Ideas** (divergent thinking) - tools that expand the possibility space. The goal is volume, not quality. Judgment is suspended.

**Prioritizing Ideas** (convergent thinking) - tools that narrow the field. The team evaluates generated ideas against criteria and selects the most promising candidates.

**Testing** (validation) - tools that expose ideas to customer reality before the team commits resources.

Skipping any category creates a gap. Generating without prioritizing produces an unmanageable list. Prioritizing without generating limits the solution space prematurely. Neither without testing means the team commits to untested assumptions.

### The 10 Methods

These methods come directly from the Productside playbook. Brief descriptions for each:

**Generating Ideas methods:**

1. **How Might We?** - Reframe problem statements as open-ended questions that invite creative solutions. "How might we help fleet managers detect vehicle issues before they cause breakdowns?" Opens the door to multiple solution paths instead of jumping to one.

2. **"Bad Ideas" First Brainstorming** - Start by deliberately generating terrible, impractical, or absurd solutions. This loosens creative inhibition and often reveals interesting inversions. "What if we made drivers diagnose their own engine problems?" might lead to a useful self-diagnostic concept.

3. **Quantity Over Quality** - Set a target number of ideas (e.g., 50 in 15 minutes) and race to hit it. No evaluation, no discussion, just volume. Quality comes later during prioritization.

4. **Mind Mapping** - Start with the core problem at the center and branch outward. Each branch represents a different angle or sub-problem. Connections between branches often reveal non-obvious solution approaches.

**Prioritizing Ideas methods:**

5. **2x2 Matrix** - Plot ideas on two axes (commonly Impact vs. Effort, or Desirability vs. Feasibility). Ideas in the high-impact, low-effort quadrant are strong candidates. Forces evaluation against concrete criteria rather than gut feel.

6. **Dot Voting** - Each participant gets a fixed number of votes (dots) to allocate across ideas. Simple, fast, democratic. Reveals where the team's collective energy concentrates.

7. **Money Voting** - Like dot voting but with fake currency (e.g., $100 per participant). Participants can spread money across ideas or concentrate it. Forces explicit trade-off thinking that dot voting does not.

**Generating + Prioritizing methods:**

8. **6-3-5 Method** - Six people, three ideas each, five rounds. Each person writes three ideas, passes the paper, and the next person builds on them. Combines generation with iterative refinement. Good for teams where vocal members dominate verbal brainstorming.

9. **SCAMPER** - Systematic creativity prompt: Substitute, Combine, Adapt, Modify/Magnify, Put to other uses, Eliminate, Reverse/Rearrange. Apply each lens to an existing solution or concept to generate variations.

**Testing methods:**

10. **Prototyping** - Build a quick, low-fidelity version (paper prototype, clickable wireframe, role-play scenario) to test with real users before committing to development.

11. **Customer Journey Maps** - Map the customer's experience across touchpoints to identify where a solution idea would actually fit into their workflow. Tests whether the solution addresses the right moment in the customer's journey. (Also serves as a generating tool by revealing gaps the team had not considered.)

### Design Thinking Principles

From the Productside overview, four principles anchor this work:

- **User-Centered Approach** - Solutions must serve the customer, not the technology or the team's assumptions
- **Iterative Process** - The first idea is rarely the best; plan for multiple rounds of generation and refinement
- **Collaboration** - Diverse perspectives produce stronger solutions; include design, engineering, customer-facing roles, and (when possible) customers
- **Creativity** - Structured methods help unlock creative thinking in teams that default to analytical problem-solving

### Scope the How Might We Questions

The PM drafts **three to five How Might We questions** before the session, each tracing back to the validated problem statement. Then test each one for scope:

- **Too broad** leaves a universe of unrelated solutions.
- **Too narrow** strangles the room, or names a solution inside the question.
- **Just right** leaves room for creativity and imagination without wandering away from the persona's need.

If a solution is hiding in the wording, point at the word and have the PM cut it. A good How Might We opens the space without choosing what goes in it. The questions that pass become the spine of the brainstorm.

### Protect Divergence

Engineers tend to kill ideas on feasibility before any exist. Set rules that protect the generating phase (quantity over quality, no judgment while generating) and keep the session **safe, engaging, and fun**. The goal is a high quantity of ideas in a safe space, then a prioritized shortlist. Rehearse the hard moments before the session: the room goes quiet, one person dominates, someone shoots down every idea.

### After the Session: Make the Case

Once the team has prioritized, the PM writes the case for the highest-priority solution **in their own words**:

- **Benefits** for the persona, tied to the specific problem. Generic benefits don't count.
- **Risks**, looked at widely: adoption, dependencies, and the business.
- **Value chain:** how the solution creates value for the customer, and how that customer value returns to the business as progress on a business outcome. Watch for where the chain breaks: customer value that never reaches the business, or a business benefit with no customer value beneath it.

If the PM can't articulate these, that is a signal they don't understand the solution yet. The summary feeds the Solution Hypothesis Statement.

### This Step vs. Solution Hypothesis

Exploring the Solution Space generates multiple options. The Solution Hypothesis Statement (the next step) commits to one. This step is deliberately divergent, then convergent, then tested. The Solution Hypothesis step takes the winning idea and frames it as a testable hypothesis with clear success criteria.

Do not collapse these two steps into one. The team needs space to explore before committing.

### How AI Supports This Play

The Playbook casts AI as a **preparation coach before the session and a critic after it**. Before, it sharpens the How Might We questions the PM drafted and helps the PM prepare to run a room of engineers who would rather kill ideas than consider them. After the room produces a prioritized set of hypotheses, AI challenges each one on value, viability, and feasibility, so the shortlist survives scrutiny, not just enthusiasm.

The ideas belong to the team in the session, never to a model beforehand. Which question to ask, who is in the room, and which hypotheses are worth testing all stay with the PM and their stakeholders. AI questions and challenges; the team judges.

- **Use it when:** there is a validated problem statement, and the PM wants to scope How Might We questions, plan the session, or stress-test what the session produced.
- **Avoid it when:** there is no validated problem yet, or the request is to generate the solutions the team should create together. Redirect to planning the session (Pitfall 4). **This holds even when the PM asks directly, and even in best guess mode:** do not produce a list of solution ideas. The ideas are the one output this Play reserves for the team in the room.
- **Return:** How Might We questions tested for scope, a session plan built for quantity, safety, and engagement, and each prioritized hypothesis challenged on value, viability, and feasibility, with the judgment left to the team.

### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

### Guided Mode

When asked for guidance, when the user is unfamiliar, or when context is missing:

1. Explain the output and estimated question count. Offer Guided, Context dump, or Best guess; default to Guided and ask the first question immediately.
2. Use supplied context instead of asking again. In Context dump mode, summarize Known / Assumed / Missing / Conflicting first.
3. Ask one bolded question per turn with a progress label, three context-specific numbered recommendations, option 4 Other, and an input hint. For facts only the user can know, ask openly without suggested answers and explain why. Ground unfamiliar domain options in research when needed.
4. Adapt recommendations to the answers. Explain why a question matters when helpful.
5. Answer interruptions, honor corrections and mode switches, and stop when asked. Resume with a brief recap and the pending question.
6. Recap supplied facts, assumptions, gaps, and readiness; confirm before generating a guided artifact. When the user faces a decision, recommend an option with reasons and offer distinct alternatives. The user decides.
7. Best guess may proceed immediately: label inferred details inline and end with Assumptions to Validate, ranked by decision impact. With sufficient supplied context, execute directly.

## Application

Use [Template](#template) for the full scaffold.


### Required Output Convention

This skill produces a **session plan** artifact. The session plan includes:

- Session goals and objectives tied to the validated problem statement
- Participant list with roles and rationale for inclusion
- Resources needed (tools, space, time)
- Selected methods with rationale for each selection
- Usage guidance for each selected method
- Session notes (timing, preparation for participants, follow-up actions)

### Step 1: Confirm the Product Context and Validate Problem Statement

Before writing anything, answer:

- What product or service are we talking about?
- Who is the target customer?
- What is the validated problem statement?

If the PM does not have a validated problem statement, stop. This skill requires one as input. Direct the PM to ps-framing-the-problem first.

**Guard against tech-role bias.** When the PM identifies session participants, check that the list is cross-functional. If the participant list is only engineers or only technical roles, flag it. Design thinking sessions need diverse perspectives: design, product, engineering, customer success, sales, and (when feasible) actual customers. The PM building a logistics platform should include logistics coordinators in the session, not only backend engineers.

### Step 2: Gather Evidence (Artifacts Only)

This skill uses **artifacts only** for evidence gathering. No web research is needed.

Ask whether the PM has materials to share:

- Validated problem statement (required)
- Stakeholder alignment document (helps determine participants)
- Prior discovery artifacts (empathy interview findings, JTBD output, persona work, problem identification output)
- Any previous brainstorming or solution exploration work

The validated problem statement is required. All other artifacts are helpful but optional.

### Step 3: Define Session Goals and Objectives

Help the PM articulate clear goals for the session. Goals should be:

- Specific to the validated problem statement (not generic "brainstorm solutions")
- Measurable enough to know if the session succeeded (e.g., "generate at least 15 solution ideas and narrow to 3 candidates")
- Achievable within the planned session time

Example goal: "Using design thinking methods, ideate solution possibilities for our problem statement: [specific problem statement]. Generate at least 15 candidate ideas, prioritize to 3, and paper-prototype the top candidate."

### Step 4: Scope the How Might We Questions

Ask the PM to draft three to five How Might We questions from the problem statement before you suggest anything. Then work through them one at a time (mirrors the critique guidance in this Play):

1. Say whether the question is too broad, too narrow, or just right, and why.
2. If a solution hides in the wording, point at the word and ask the PM to cut it.
3. Check it still traces to the problem statement, not a new problem.
4. Ask the PM what kinds of ideas the question would invite, so they can hear its scope.

The PM fixes each question. Offer suggestions as options to review and edit, never as replacements. Commit the questions that pass.

### Step 5: Determine Participants

Help the PM identify who should attend the session. Key considerations:

- Review the stakeholder alignment document if available
- Include cross-functional representation (product, design, engineering, customer-facing roles)
- Include someone who has direct customer contact or customer evidence
- Keep the group small enough for productive collaboration (5-8 people is the sweet spot)
- Assign a facilitator (the PM or a designee) and a note-taker

For each participant, note their role and what perspective they bring to the session.

### Step 6: Identify Session Resources

Help the PM plan the practical logistics:

- **Collaboration tools**: Mural, Miro, FigJam, physical whiteboard, sticky notes
- **Meeting setup**: Video conferencing with recording option, or in-person room
- **Time allocation**: Minimum 90 minutes for a single-method session; 2-3 hours for a multi-method session
- **Pre-work**: What participants need to review before the session (problem statement, discovery findings)
- **Documentation**: How outcomes will be captured and shared after the session

### Step 7: Select Ideation Methods from the Catalog

Recommend methods based on the session goals, team size, and available time. Key rules:

- **Select at least one method from each of the three activity types** (Generating, Prioritizing, Testing)
- **3-4 methods is the sweet spot** for a single session; more than 4 is too many to execute well
- **Sequence matters**: Generate first, then prioritize, then test. Do not reverse the order.

Ask the PM what each method should produce before they commit to it, and make them justify each choice. Build the plan with them rather than setting the agenda for them (mirrors the critique guidance in this Play).

For each selected method, provide:

- Why it fits this session (connection to the problem, team dynamics, time available)
- How to run it (brief facilitation guidance)
- Expected output (what the team produces)
- Time needed (rough estimate)

### Step 8: Provide Method Usage Guidance

For each selected method, give the PM enough facilitation guidance to run it:

- Setup instructions (what to prepare before starting)
- Step-by-step facilitation flow
- Timing for each phase
- Common facilitation mistakes to avoid
- How the output feeds the next method in the sequence

Then set the **ground rules that protect divergence** (quantity over quality, no judgment while generating), walk the session as a timeline, and ask how the PM will keep it safe, engaging, and fun. **Rehearse the hard moments:** what the PM will do when the room goes quiet, when one person dominates, and when someone shoots down every idea.

### Step 9: Add Session Notes

Help the PM document practical considerations:

- Total session duration and timing for each method
- Whether multiple sessions are needed (if more than 3-4 methods are selected, split across sessions)
- Pre-session preparation for participants (what to read, what to bring)
- Post-session follow-up (how to document outcomes, who reviews the results)
- How session outcomes feed into the Solution Hypothesis Statement step

### Step 10: Review the Session Plan for Completeness

Before finalizing, check:

- Does the plan reference the specific validated problem statement?
- Are session goals specific enough to evaluate success?
- Is the participant list cross-functional (not engineering-only)?
- Are at least three activity types covered (Generating, Prioritizing, Testing)?
- Is the time allocation realistic for the number of methods selected?
- Are resources and logistics documented?
- Is there a plan for capturing and sharing outcomes?

### Step 11: After the Session, Sharpen the Case

When the PM returns with the team's prioritized solutions, help them build the case for the highest-priority one (mirrors the critique guidance in this Play). Do not write the benefits, name the risks, or compose the value story. Make the PM articulate each, then reflect back what is thin, missing, or disconnected:

1. **Benefits:** ask what the solution does for the persona, tied to the specific problem. Point at any benefit that is generic or disconnected.
2. **Risks:** ask what risks the PM sees. After they answer, ask questions that test whether they looked widely enough (adoption, dependencies, the business) without naming a risk yourself.
3. **Value:** have the PM trace customer value to business value, and show where the chain breaks.
4. **Challenge the shortlist** on value, viability, and feasibility if the PM asks. Question it; the team judges it.
5. **Pull it into a solution summary** in the PM's words: the input to ps-solution-hypothesis.

Do not invent customer reactions or business numbers.

### Step 12: Offer Next Steps

After the session plan is complete, offer the PM up to three next-step options:

1. **Run the session** - take the plan into the room and facilitate the design thinking session with the team
2. **Move to Solution Hypothesis** - after the session and the solution case (Step 11), craft a Solution Hypothesis Statement using ps-solution-hypothesis
3. **Revisit the problem statement** - if the evidence is thin, revisit ps-framing-the-problem before entering the solution space

Present these as options, not mandatory steps. The PM decides what comes next.

## Template

### When to Use This

Use this template during **Discover + Define** when you have a validated problem statement and need to plan a design thinking session to explore solution possibilities. This is a process skill for session preparation, not a solution-generation exercise.

Upstream work that feeds this template: validated problem statement (from ps-framing-the-problem), stakeholder alignment, empathy interview findings, proto-persona, jobs-to-be-done.

### Template

#### Session Plan

```markdown
# Exploring the Solution Space: Session Plan

## Product Context

- Product or service:
- Target market segment:
- Target customer (the person the product serves):

## Validated Problem Statement

Paste the validated problem statement here. If you do not have one, stop and use ps-framing-the-problem first.

> Quality check: Is this a specific, validated problem statement, not a vague "customers struggle with X"?
> Quality check: Is the problem stated from the customer's perspective, not the product team's?

## Session Parameters

### Goals and Objectives

What should this session accomplish? Tie goals to the problem statement.

1.
2.
3.

> Quality check: Are goals specific enough to evaluate whether the session succeeded?
> Quality check: Do goals reference the validated problem statement, not a generic "brainstorm solutions"?
> Quality check: Do goals include a measurable outcome (e.g., "generate at least 15 ideas and narrow to 3")?

### How Might We Questions

Draft three to five yourself. Each must trace back to the validated problem statement.

| # | How Might We... | Scope (too broad / too narrow / just right) | Traces to problem? |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

> Quality check: Is any solution hiding in the wording? Cut it.
> Quality check: Does each question open the space without choosing what goes in it?

### Ground Rules and Hard Moments

- Rules that protect divergence (e.g. quantity over quality, no judgment while generating):
- How we keep it safe, engaging, and fun:
- If the room goes quiet:
- If one person dominates:
- If someone shoots down every idea:

### Participants

Who should attend? Include cross-functional representation.

| Name / Role | Function | Perspective They Bring |
|-------------|----------|----------------------|
| | | |
| | | |
| | | |
| | | |
| | | |

> Quality check: Is the list cross-functional (not only engineers or only technical roles)?
> Quality check: Is someone with direct customer contact or customer evidence included?
> Quality check: Is there a designated facilitator and a note-taker?
> Quality check: Is the group between 5-8 people? Fewer limits diversity; more limits participation.

### Session Resources Needed

- Collaboration tool:
- Meeting setup:
- Time allocated:
- Pre-work for participants:
- Documentation plan:

> Quality check: Is the time allocation realistic for the number of methods selected (minimum 90 min for single-method, 2-3 hours for multi-method)?
> Quality check: Is there a plan for how participants should prepare?

### Notes

- Session timing considerations:
- Multiple sessions needed? (If more than 3-4 methods, split across sessions)
- Post-session follow-up plan:

## Method Selection

Select 3-4 methods from the catalog below. Choose at least one from each activity type.

### Productside Method Catalog

Mark selected methods. For each selected method, add rationale below.

| # | Method | Activity Type | Selected? |
|---|--------|--------------|-----------|
| 1 | How Might We? | Generating Ideas | [ ] |
| 2 | "Bad Ideas" First Brainstorming | Generating Ideas | [ ] |
| 3 | Quantity Over Quality | Generating Ideas | [ ] |
| 4 | Mind Mapping | Generating Ideas | [ ] |
| 5 | 2x2 Matrix | Prioritizing Ideas | [ ] |
| 6 | Dot Voting | Prioritizing Ideas | [ ] |
| 7 | Money Voting | Prioritizing Ideas | [ ] |
| 8 | 6-3-5 Method | Generating + Prioritizing | [ ] |
| 9 | SCAMPER | Generating + Prioritizing | [ ] |
| 10 | Prototyping | Testing | [ ] |
| 11 | Customer Journey Maps | Generating + Testing | [ ] |

> Quality check: Is at least one Generating method selected?
> Quality check: Is at least one Prioritizing method selected?
> Quality check: Is at least one Testing method selected?
> Quality check: Are 3-4 methods selected total? More than 4 in one session is too many.
> Quality check: Are methods sequenced correctly (Generate first, then Prioritize, then Test)?

### Selected Method Details

For each selected method, fill in the details below. Copy this block for each method.

#### Method: [Name]

- **Activity type:** [Generating / Prioritizing / Testing]
- **Why this method fits this session:**
- **Time needed:** [estimate in minutes]
- **Setup instructions:**
- **Facilitation flow:**
  1.
  2.
  3.
- **Expected output:**
- **Common facilitation mistakes to avoid:**
- **How the output feeds the next method:**

> Quality check: Does the facilitation flow include clear time limits for each phase?
> Quality check: Is the expected output concrete enough to feed the next method or the Solution Hypothesis step?
> Capacity check: Setup instructions ~20-30 words. Facilitation flow steps ~10-15 words each.
```

#### Post-Session Documentation

```markdown
# Session Outcomes

## Session Context

- Date:
- Duration:
- Facilitator:
- Participants:
- Problem statement addressed:

## Ideas Generated

List all ideas generated during the session (even the ones that were not prioritized).

| # | Idea | Source Method |
|---|------|-------------|
| 1 | | |
| 2 | | |
| 3 | | |

## Prioritized Ideas

Which ideas rose to the top during prioritization? Include the rationale.

| Rank | Idea | Why It Rose to the Top |
|------|------|----------------------|
| 1 | | |
| 2 | | |
| 3 | | |

> Quality check: Does the rationale connect back to the validated problem statement?
> Quality check: Are the top ideas feasible enough to prototype or test?

## Testing Observations

If prototyping or journey mapping was conducted, document what was learned.

-
-
-

## Solution Case (highest-priority solution, in the PM's own words)

- Solution:
- Benefits for the persona (tied to the problem):
- Risks (adoption, dependencies, business):
- Customer value:
- How customer value returns to the business (which business outcome):

> Quality check: Is any benefit generic, or disconnected from the problem?
> Quality check: Where could the value chain break?

## Next Steps

- [ ] Document and share session outcomes with stakeholders not in the room
- [ ] Select the top candidate for Solution Hypothesis Statement (ps-solution-hypothesis)
- [ ] Plan follow-up session if needed
- [ ] Schedule prototype testing with real customers if applicable
```

### Usage Guidance

#### Session Flow

A typical session follows this sequence:

1. **Open (10 min)** - Facilitator reviews the problem statement and session goals. Participants align on what they are solving.
2. **Generate (30-45 min)** - Run one or two generating methods. Focus on volume and creativity.
3. **Prioritize (20-30 min)** - Run a prioritization method. Narrow the field to 3-5 candidates.
4. **Test (30-45 min)** - Run a testing method on the top candidates. Expose ideas to customer reality.
5. **Close (15 min)** - Document top ideas, prioritization rationale, and next steps.

#### How Many Methods

Select 3-4 methods for a single session:

- 1-2 Generating methods (if using two, keep total generating time under 45 minutes)
- 1 Prioritizing method
- 1 Testing method

If more methods are needed, plan a second session rather than cramming. Depth produces better ideas than breadth.

#### Time Budgets

| Session Type | Duration | Methods | Guidance |
|-------------|----------|---------|----------|
| Focused | 90 min | 3 methods | One generating, one prioritizing, one testing |
| Standard | 2 hours | 3-4 methods | Two generating, one prioritizing, one testing |
| Extended | 3 hours | 4 methods + breaks | Full cycle with deeper exploration |

#### Connecting to Other Skills

- **Upstream:** ps-framing-the-problem (validated problem statement is required input), ps-empathy-interviews (customer evidence grounds the session), ps-proto-persona (persona context), ps-jobs-to-be-done (jobs and outcomes to solve for)
- **Downstream:** The top idea from this session feeds into the Solution Hypothesis Statement

#### Capacity Reference

| Field | Word Budget | Guidance |
|-------|-------------|----------|
| Session Goal | ~15-25 | Specific, tied to problem statement |
| Method Rationale | ~15-25 | Why this method fits this session |
| Setup Instructions | ~20-30 | What to prepare before starting |
| Facilitation Step | ~10-15 | Clear, actionable instruction |
| Idea Description | ~10-15 | Concrete enough to evaluate |
| Prioritization Rationale | ~15-20 | Why this idea rose to the top |

## Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For a fleet manager facing unexpected breakdowns, frame a How Might We question, choose an ideation method, and plan the team session before comparing ideas.
- **Weak:** A session plan that begins with a chosen predictive-maintenance feature skips exploration.
- **Drift to avoid:** Agent substitutes for the room: an AI-generated solution list is an explicitly requested draft, not evidence of team ideation or agreement.


## Common Pitfalls

- **Skipping the Problem Statement:** Require the validated problem statement as input. If the PM cannot state the problem clearly, redirect to ps-framing-the-problem before planning a solution space session.

- **Inviting Only Engineers:** Check the participant list for cross-functional diversity. Flag if design, customer-facing roles, or domain experts are missing. A logistics platform PM should have logistics professionals in the session, not only backend developers.

- **Selecting Only Divergent Methods:** Require at least one method from each activity type. If the PM selects only Generating methods, explicitly ask: "How will you prioritize these ideas? How will you test the top candidates before committing?"

- **Treating the Agent as a Substitute for the Team Session:** Redirect the PM to session planning. The agent's job is to help prepare a productive session, not to replace it. The team generates the ideas; the agent helps structure the process.

- **Making Session Goals Too Vague:** Tie goals to the specific problem statement and include measurable outcomes: "Generate at least 15 solution ideas for [problem], prioritize to 3 candidates, and paper-prototype the top candidate."

- **Not Allocating Enough Time:** Budget minimum 90 minutes for a single-method session. Multi-method sessions need 2-3 hours. If the calendar does not allow it, split across multiple sessions rather than cramming everything into one.

- **Selecting Too Many Methods:** Limit to 3-4 methods per session. If more methods are needed, plan a second session. Depth beats breadth in ideation.

- **Forgetting to Document Session Outcomes:** Assign a note-taker during the session. Plan 15 minutes at the end for documenting the top ideas, prioritization rationale, and agreed next steps. The session outcomes should be structured enough to feed the Solution Hypothesis step.

- **AI Ranks the Solutions for You:** Prioritize in the room with the catalog's prioritizing methods (Dot Voting, Money Voting, Value vs. Effort). Afterward, the agent may challenge each shortlisted hypothesis on value, viability, and feasibility. The team decides.

- **A How Might We That Is Too Broad, Too Narrow, or Hiding a Solution:** Draft three to five, test each for scope, cut any solution word, and check each traces to the problem statement.

- **A Shortlist Nobody Can Defend:** Before moving on, the PM writes the case in their own words (Step 11): benefits tied to the problem, risks looked at widely, and the value chain from customer to business.

## References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-exploring-solution-space) for supporting source material and expanded examples.
