# Discover + Define: Play references

November 2026 B2B work-in-progress Playbook. Not yet ratified.

Find Plays by stable identifier in 01-playbook-navigator.md. Each Play below contains its instructions, template, and examples. Mentions of skills or agents in the preserved source mean applying the Play from these uploaded references.

## ps-exploring-solution-space | Exploring the Solution Space

Playbook number: 11. Phase: Discover + Define.

### ps-exploring-solution-space / Instructions

#### Purpose

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

##### Usage Notes

- This is a **process skill** (`type: process`). The agent helps prepare a design thinking session; the actual ideation happens with the team in real time.
- Evidence gathering: this skill qualifies for **artifacts only**. The PM brings the validated problem statement, stakeholder alignment, and prior discovery work. No web research needed.
- The method catalog contains 10 tools from the Productside playbook organized across three activity types: Generating Ideas, Prioritizing Ideas, and Testing. A well-planned session includes at least one from each category.
- Upstream: ps-framing-the-problem (validated problem statement is required input), ps-empathy-interviews, ps-proto-persona, ps-jobs-to-be-done.
- Downstream: Solution Hypothesis Statement (the top idea from this session feeds the hypothesis).

#### Key Concepts

##### The Three Activity Types

The Productside catalog organizes ideation methods into three categories. A well-planned session should include at least one method from each:

**Generating Ideas** (divergent thinking) - tools that expand the possibility space. The goal is volume, not quality. Judgment is suspended.

**Prioritizing Ideas** (convergent thinking) - tools that narrow the field. The team evaluates generated ideas against criteria and selects the most promising candidates.

**Testing** (validation) - tools that expose ideas to customer reality before the team commits resources.

Skipping any category creates a gap. Generating without prioritizing produces an unmanageable list. Prioritizing without generating limits the solution space prematurely. Neither without testing means the team commits to untested assumptions.

##### The 10 Methods

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

##### Design Thinking Principles

From the Productside overview, four principles anchor this work:

- **User-Centered Approach** - Solutions must serve the customer, not the technology or the team's assumptions
- **Iterative Process** - The first idea is rarely the best; plan for multiple rounds of generation and refinement
- **Collaboration** - Diverse perspectives produce stronger solutions; include design, engineering, customer-facing roles, and (when possible) customers
- **Creativity** - Structured methods help unlock creative thinking in teams that default to analytical problem-solving

##### Scope the How Might We Questions

The PM drafts **three to five How Might We questions** before the session, each tracing back to the validated problem statement. Then test each one for scope:

- **Too broad** leaves a universe of unrelated solutions.
- **Too narrow** strangles the room, or names a solution inside the question.
- **Just right** leaves room for creativity and imagination without wandering away from the persona's need.

If a solution is hiding in the wording, point at the word and have the PM cut it. A good How Might We opens the space without choosing what goes in it. The questions that pass become the spine of the brainstorm.

##### Protect Divergence

Engineers tend to kill ideas on feasibility before any exist. Set rules that protect the generating phase (quantity over quality, no judgment while generating) and keep the session **safe, engaging, and fun**. The goal is a high quantity of ideas in a safe space, then a prioritized shortlist. Rehearse the hard moments before the session: the room goes quiet, one person dominates, someone shoots down every idea.

##### After the Session: Make the Case

Once the team has prioritized, the PM writes the case for the highest-priority solution **in their own words**:

- **Benefits** for the persona, tied to the specific problem. Generic benefits don't count.
- **Risks**, looked at widely: adoption, dependencies, and the business.
- **Value chain:** how the solution creates value for the customer, and how that customer value returns to the business as progress on a business outcome. Watch for where the chain breaks: customer value that never reaches the business, or a business benefit with no customer value beneath it.

If the PM can't articulate these, that is a signal they don't understand the solution yet. The summary feeds the Solution Hypothesis Statement.

##### This Step vs. Solution Hypothesis

Exploring the Solution Space generates multiple options. The Solution Hypothesis Statement (the next step) commits to one. This step is deliberately divergent, then convergent, then tested. The Solution Hypothesis step takes the winning idea and frames it as a testable hypothesis with clear success criteria.

Do not collapse these two steps into one. The team needs space to explore before committing.

##### How AI Supports This Play

The Playbook casts AI as a **preparation coach before the session and a critic after it**. Before, it sharpens the How Might We questions the PM drafted and helps the PM prepare to run a room of engineers who would rather kill ideas than consider them. After the room produces a prioritized set of hypotheses, AI challenges each one on value, viability, and feasibility, so the shortlist survives scrutiny, not just enthusiasm.

The ideas belong to the team in the session, never to a model beforehand. Which question to ask, who is in the room, and which hypotheses are worth testing all stay with the PM and their stakeholders. AI questions and challenges; the team judges.

- **Use it when:** there is a validated problem statement, and the PM wants to scope How Might We questions, plan the session, or stress-test what the session produced.
- **Avoid it when:** there is no validated problem yet, or the request is to generate the solutions the team should create together. Redirect to planning the session (Pitfall 4). **This holds even when the PM asks directly, and even in best guess mode:** do not produce a list of solution ideas. The ideas are the one output this Play reserves for the team in the room.
- **Return:** How Might We questions tested for scope, a session plan built for quantity, safety, and engagement, and each prioritized hypothesis challenged on value, viability, and feasibility, with the judgment left to the team.

##### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

##### Guided Mode

When asked for guidance, when the user is unfamiliar, or when context is missing:

1. Explain the output and estimated question count. Offer Guided, Context dump, or Best guess; default to Guided and ask the first question immediately.
2. Use supplied context instead of asking again. In Context dump mode, summarize Known / Assumed / Missing / Conflicting first.
3. Ask one bolded question per turn with a progress label, three context-specific numbered recommendations, option 4 Other, and an input hint. For facts only the user can know, ask openly without suggested answers and explain why. Ground unfamiliar domain options in research when needed.
4. Adapt recommendations to the answers. Explain why a question matters when helpful.
5. Answer interruptions, honor corrections and mode switches, and stop when asked. Resume with a brief recap and the pending question.
6. Recap supplied facts, assumptions, gaps, and readiness; confirm before generating a guided artifact. When the user faces a decision, recommend an option with reasons and offer distinct alternatives. The user decides.
7. Best guess may proceed immediately: label inferred details inline and end with Assumptions to Validate, ranked by decision impact. With sufficient supplied context, execute directly.

#### Application

Use Template (uploaded reference: `04-discover-define.md`, section `ps-exploring-solution-space / Template`) for the full scaffold.


##### Required Output Convention

This skill produces a **session plan** artifact. The session plan includes:

- Session goals and objectives tied to the validated problem statement
- Participant list with roles and rationale for inclusion
- Resources needed (tools, space, time)
- Selected methods with rationale for each selection
- Usage guidance for each selected method
- Session notes (timing, preparation for participants, follow-up actions)

##### Step 1: Confirm the Product Context and Validate Problem Statement

Before writing anything, answer:

- What product or service are we talking about?
- Who is the target customer?
- What is the validated problem statement?

If the PM does not have a validated problem statement, stop. This skill requires one as input. Direct the PM to ps-framing-the-problem first.

**Guard against tech-role bias.** When the PM identifies session participants, check that the list is cross-functional. If the participant list is only engineers or only technical roles, flag it. Design thinking sessions need diverse perspectives: design, product, engineering, customer success, sales, and (when feasible) actual customers. The PM building a logistics platform should include logistics coordinators in the session, not only backend engineers.

##### Step 2: Gather Evidence (Artifacts Only)

This skill uses **artifacts only** for evidence gathering. No web research is needed.

Ask whether the PM has materials to share:

- Validated problem statement (required)
- Stakeholder alignment document (helps determine participants)
- Prior discovery artifacts (empathy interview findings, JTBD output, persona work, problem identification output)
- Any previous brainstorming or solution exploration work

The validated problem statement is required. All other artifacts are helpful but optional.

##### Step 3: Define Session Goals and Objectives

Help the PM articulate clear goals for the session. Goals should be:

- Specific to the validated problem statement (not generic "brainstorm solutions")
- Measurable enough to know if the session succeeded (e.g., "generate at least 15 solution ideas and narrow to 3 candidates")
- Achievable within the planned session time

Example goal: "Using design thinking methods, ideate solution possibilities for our problem statement: [specific problem statement]. Generate at least 15 candidate ideas, prioritize to 3, and paper-prototype the top candidate."

##### Step 4: Scope the How Might We Questions

Ask the PM to draft three to five How Might We questions from the problem statement before you suggest anything. Then work through them one at a time (mirrors the critique guidance in this Play):

1. Say whether the question is too broad, too narrow, or just right, and why.
2. If a solution hides in the wording, point at the word and ask the PM to cut it.
3. Check it still traces to the problem statement, not a new problem.
4. Ask the PM what kinds of ideas the question would invite, so they can hear its scope.

The PM fixes each question. Offer suggestions as options to review and edit, never as replacements. Commit the questions that pass.

##### Step 5: Determine Participants

Help the PM identify who should attend the session. Key considerations:

- Review the stakeholder alignment document if available
- Include cross-functional representation (product, design, engineering, customer-facing roles)
- Include someone who has direct customer contact or customer evidence
- Keep the group small enough for productive collaboration (5-8 people is the sweet spot)
- Assign a facilitator (the PM or a designee) and a note-taker

For each participant, note their role and what perspective they bring to the session.

##### Step 6: Identify Session Resources

Help the PM plan the practical logistics:

- **Collaboration tools**: Mural, Miro, FigJam, physical whiteboard, sticky notes
- **Meeting setup**: Video conferencing with recording option, or in-person room
- **Time allocation**: Minimum 90 minutes for a single-method session; 2-3 hours for a multi-method session
- **Pre-work**: What participants need to review before the session (problem statement, discovery findings)
- **Documentation**: How outcomes will be captured and shared after the session

##### Step 7: Select Ideation Methods from the Catalog

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

##### Step 8: Provide Method Usage Guidance

For each selected method, give the PM enough facilitation guidance to run it:

- Setup instructions (what to prepare before starting)
- Step-by-step facilitation flow
- Timing for each phase
- Common facilitation mistakes to avoid
- How the output feeds the next method in the sequence

Then set the **ground rules that protect divergence** (quantity over quality, no judgment while generating), walk the session as a timeline, and ask how the PM will keep it safe, engaging, and fun. **Rehearse the hard moments:** what the PM will do when the room goes quiet, when one person dominates, and when someone shoots down every idea.

##### Step 9: Add Session Notes

Help the PM document practical considerations:

- Total session duration and timing for each method
- Whether multiple sessions are needed (if more than 3-4 methods are selected, split across sessions)
- Pre-session preparation for participants (what to read, what to bring)
- Post-session follow-up (how to document outcomes, who reviews the results)
- How session outcomes feed into the Solution Hypothesis Statement step

##### Step 10: Review the Session Plan for Completeness

Before finalizing, check:

- Does the plan reference the specific validated problem statement?
- Are session goals specific enough to evaluate success?
- Is the participant list cross-functional (not engineering-only)?
- Are at least three activity types covered (Generating, Prioritizing, Testing)?
- Is the time allocation realistic for the number of methods selected?
- Are resources and logistics documented?
- Is there a plan for capturing and sharing outcomes?

##### Step 11: After the Session, Sharpen the Case

When the PM returns with the team's prioritized solutions, help them build the case for the highest-priority one (mirrors the critique guidance in this Play). Do not write the benefits, name the risks, or compose the value story. Make the PM articulate each, then reflect back what is thin, missing, or disconnected:

1. **Benefits:** ask what the solution does for the persona, tied to the specific problem. Point at any benefit that is generic or disconnected.
2. **Risks:** ask what risks the PM sees. After they answer, ask questions that test whether they looked widely enough (adoption, dependencies, the business) without naming a risk yourself.
3. **Value:** have the PM trace customer value to business value, and show where the chain breaks.
4. **Challenge the shortlist** on value, viability, and feasibility if the PM asks. Question it; the team judges it.
5. **Pull it into a solution summary** in the PM's words: the input to ps-solution-hypothesis.

Do not invent customer reactions or business numbers.

##### Step 12: Offer Next Steps

After the session plan is complete, offer the PM up to three next-step options:

1. **Run the session** - take the plan into the room and facilitate the design thinking session with the team
2. **Move to Solution Hypothesis** - after the session and the solution case (Step 11), craft a Solution Hypothesis Statement using ps-solution-hypothesis
3. **Revisit the problem statement** - if the evidence is thin, revisit ps-framing-the-problem before entering the solution space

Present these as options, not mandatory steps. The PM decides what comes next.

### ps-exploring-solution-space / Template

##### When to Use This

Use this template during **Discover + Define** when you have a validated problem statement and need to plan a design thinking session to explore solution possibilities. This is a process skill for session preparation, not a solution-generation exercise.

Upstream work that feeds this template: validated problem statement (from ps-framing-the-problem), stakeholder alignment, empathy interview findings, proto-persona, jobs-to-be-done.

##### Template

###### Session Plan

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

###### Post-Session Documentation

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

##### Usage Guidance

###### Session Flow

A typical session follows this sequence:

1. **Open (10 min)** - Facilitator reviews the problem statement and session goals. Participants align on what they are solving.
2. **Generate (30-45 min)** - Run one or two generating methods. Focus on volume and creativity.
3. **Prioritize (20-30 min)** - Run a prioritization method. Narrow the field to 3-5 candidates.
4. **Test (30-45 min)** - Run a testing method on the top candidates. Expose ideas to customer reality.
5. **Close (15 min)** - Document top ideas, prioritization rationale, and next steps.

###### How Many Methods

Select 3-4 methods for a single session:

- 1-2 Generating methods (if using two, keep total generating time under 45 minutes)
- 1 Prioritizing method
- 1 Testing method

If more methods are needed, plan a second session rather than cramming. Depth produces better ideas than breadth.

###### Time Budgets

| Session Type | Duration | Methods | Guidance |
|-------------|----------|---------|----------|
| Focused | 90 min | 3 methods | One generating, one prioritizing, one testing |
| Standard | 2 hours | 3-4 methods | Two generating, one prioritizing, one testing |
| Extended | 3 hours | 4 methods + breaks | Full cycle with deeper exploration |

###### Connecting to Other Skills

- **Upstream:** ps-framing-the-problem (validated problem statement is required input), ps-empathy-interviews (customer evidence grounds the session), ps-proto-persona (persona context), ps-jobs-to-be-done (jobs and outcomes to solve for)
- **Downstream:** The top idea from this session feeds into the Solution Hypothesis Statement

###### Capacity Reference

| Field | Word Budget | Guidance |
|-------|-------------|----------|
| Session Goal | ~15-25 | Specific, tied to problem statement |
| Method Rationale | ~15-25 | Why this method fits this session |
| Setup Instructions | ~20-30 | What to prepare before starting |
| Facilitation Step | ~10-15 | Clear, actionable instruction |
| Idea Description | ~10-15 | Concrete enough to evaluate |
| Prioritization Rationale | ~15-20 | Why this idea rose to the top |

### ps-exploring-solution-space / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For a fleet manager facing unexpected breakdowns, frame a How Might We question, choose an ideation method, and plan the team session before comparing ideas.
- **Weak:** A session plan that begins with a chosen predictive-maintenance feature skips exploration.
- **Drift to avoid:** Agent substitutes for the room: an AI-generated solution list is an explicitly requested draft, not evidence of team ideation or agreement.


#### Common Pitfalls

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

#### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-exploring-solution-space) for supporting source material and expanded examples.

## ps-solution-hypothesis | Solution Hypothesis

Playbook number: 12. Phase: Discover + Define.

### ps-solution-hypothesis / Instructions

#### Purpose

Create a **Productside-style Solution Hypothesis Statement artifact** that documents a proposed solution, its benefits and risks, and produces two linked If/Then hypothesis statements.

This skill is for the **Discover + Define** phase. It sits directly downstream of Framing the Problem and Exploring the Solution Space. The PM has validated a problem and explored possible solutions; now they are expressing their chosen solution as a testable hypothesis.

This is a synthesis and articulation skill. It pulls together findings from:

- problem framing (ps-framing-the-problem)
- solution space exploration (ps-exploring-solution-space)
- positioning work (ps-positioning-statement), if available

The output is a five-section artifact: problem statement (imported from upstream), solution summary, solution benefits, risks and assumptions, and a two-column solution hypothesis statement. This artifact is what the PM uses to communicate a testable solution direction to leadership and to justify resource allocation through gate review processes.

Use this skill when you need to:

- express a proposed solution as a testable If/Then hypothesis
- separate customer value from business outcome in a structured format
- document benefits and risks before committing to a solution direction
- create a reviewable artifact for leadership or gate review processes

This is not a PRD or feature specification. If the output reads like a requirements document or a feature list, the hypothesis has drifted into implementation territory.

##### Usage Notes

- The template produces a single artifact with five sections: Problem Statement (imported), Solution Summary, Solution Benefits, Risks and Assumptions, and Solution Hypothesis Statement (two-column If/Then).
- Two hypothesis statements are required, not one: customer-focused (IF solution THEN customer benefit) and business-focused (IF customer benefit THEN business outcome). The THEN of the first becomes the IF of the second.
- Evidence gathering is **artifacts only** - no web research offered. This skill synthesizes the PM's problem framing and solution exploration work.
- Upstream: ps-framing-the-problem, ps-exploring-solution-space, ps-positioning-statement.
- Downstream: lo-fi experimentation, risk assessment, roadmap planning, outcome tree alignment.

#### Key Concepts

##### The If/Then Structure Is the Core Format

A solution hypothesis is not a description of what to build. It is a testable statement: **IF** we do X, **THEN** Y happens. This format forces the PM to connect the solution to an expected outcome, which is the first step toward validation.

A solution summary says "what." A hypothesis says "if we do this, then this result follows." The difference matters because summaries cannot be tested, but hypotheses can.

If you are not sure where to start, write the simplest possible If-then statement and work from there. Precision comes in later iterations.

##### Two Hypotheses, Not One

The Productside format requires two linked hypothesis statements:

1. **Customer-focused:** IF we [provide this solution], THEN [customers experience this benefit]
2. **Business-focused:** IF we [achieve that customer benefit], THEN [we reach this business outcome]

The THEN of the customer-focused hypothesis becomes the IF of the business-focused hypothesis. This chain ensures the PM has thought through both sides: why the customer cares and why the business cares.

If there is only one hypothesis that mixes customer and business language, the chain is broken. Separate them.

##### The Five Sections Have a Specific Flow

The artifact builds in a deliberate sequence:

1. **Problem Statement** carries forward from ps-framing-the-problem. It is imported, not rewritten.
2. **Solution Summary** describes the proposed solution in one paragraph.
3. **Solution Benefits** lists 3-5 specific benefits for the customer and the business.
4. **Risks and Assumptions** lists 3-5 specific risks or assumptions that need validation.
5. **Solution Hypothesis Statement** presents the two-column If/Then output.

Each section feeds the next. The problem grounds the solution. The solution grounds the benefits. The benefits and risks inform the hypothesis. The hypothesis is the synthesis of everything above it.

##### Solution Benefits Are Not Features

A benefit is the outcome the customer or business experiences. A feature is what the product does. "Automated workflow engine" is a feature. "Time saved on manual data entry, freeing specialists to focus on strategic work" is a benefit.

Benefits should answer: so what? If the benefit reads like a capability description, push it one level further to the outcome.

##### Risks and Assumptions Are Specific and Testable

Good risks name concrete failure modes: "Technical integration with legacy HRIS systems may require custom middleware." Bad risks name vague worries: "Things might not work as planned."

Assumptions are things the team believes to be true but has not yet validated. Surfacing them here prepares the PM for the validation work that follows the hypothesis.

##### Connection to the Outcome Tree

The business outcome in the second hypothesis should align with an outcome in the Outcome Tree (if one exists). If the PM has done outcome tree work, the business-focused hypothesis should reference one of the identified business success metrics. This creates traceability from problem to solution to measurable result.

##### Product Outcomes Use Role Names, Not Persona Names

When writing benefits, outcomes, and hypothesis statements, refer to roles ("HR specialists," "clinical operations leads," "field engineers") rather than individual persona names ("Henry," "Maya"). Role names keep the hypothesis generalizable across the target population.

##### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **critic of the solution hypothesis the PM drafted**. It checks the If/Then format, tests whether the customer-focused hypothesis chains into the business-focused one, flags features posing as benefits, and asks whether each risk and assumption is specific enough to test. The solution and the bet stay the PM's.

- **Use it when:** the PM has a validated problem statement and a prioritized solution, and has drafted the hypothesis.
- **Avoid it when:** there is no validated problem statement. A hypothesis about an unframed problem has nothing to test against.
- **Return:** the If/Then chain tested link by link, benefits separated from features, risks and assumptions sharpened into things a test could settle, and proposed rewrites for the PM to accept, adapt, or reject.

##### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

##### Guided Mode

When asked for guidance, when the user is unfamiliar, or when context is missing:

1. Explain the output and estimated question count. Offer Guided, Context dump, or Best guess; default to Guided and ask the first question immediately.
2. Use supplied context instead of asking again. In Context dump mode, summarize Known / Assumed / Missing / Conflicting first.
3. Ask one bolded question per turn with a progress label, three context-specific numbered recommendations, option 4 Other, and an input hint. For facts only the user can know, ask openly without suggested answers and explain why. Ground unfamiliar domain options in research when needed.
4. Adapt recommendations to the answers. Explain why a question matters when helpful.
5. Answer interruptions, honor corrections and mode switches, and stop when asked. Resume with a brief recap and the pending question.
6. Recap supplied facts, assumptions, gaps, and readiness; confirm before generating a guided artifact. When the user faces a decision, recommend an option with reasons and offer distinct alternatives. The user decides.
7. Best guess may proceed immediately: label inferred details inline and end with Assumptions to Validate, ranked by decision impact. With sufficient supplied context, execute directly.

#### Application

Use Template (uploaded reference: `04-discover-define.md`, section `ps-solution-hypothesis / Template`) for the full scaffold.


##### Required Output Convention

Default to a **clean, paste-ready solution hypothesis artifact**.

That means:

- fill all five sections in order
- keep each section within its word budget (see Capacity Reference below)
- produce two hypothesis statements that chain together correctly
- explanation belongs below the artifact, not inside the template fields
- the artifact comes first; commentary is secondary

##### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

##### Step 1: Confirm the Product and Customer Context

Before writing anything, answer:

- what product or service is the PM building?
- who is the customer whose problem is being solved?
- what prior work exists (problem statement, solution exploration, positioning)?

If you cannot identify a specific customer, stop and resolve the target first.

**Guard against tech-role bias.** The solution should serve the actual customer, not default to building developer tools. A clinical data platform's solution hypothesis should describe value for clinical operations leads, not data engineers. An agricultural supply chain tool should describe value for farm operations managers, not software developers. Before writing the solution summary, confirm: does this solution serve the person who actually experiences the problem day-to-day?

##### Step 2: Gather Evidence Before Writing

Once you know the product and customer, offer the user materials to share before drafting:

**User-supplied artifacts** - ask whether the user has materials to ground the hypothesis: validated problem statement (from ps-framing-the-problem), solution space exploration output, positioning work, competitive analysis, or earlier skill outputs.

This skill is **artifacts only** - it synthesizes the PM's own problem framing and solution exploration. Web research is not offered because the hypothesis should flow from validated upstream work, not from external sources the PM has not yet verified.

If the user has no validated problem statement, surface the tension: a solution hypothesis without a validated problem is building on assumptions. Recommend completing ps-framing-the-problem first, but proceed if the user wants to draft an assumption-based hypothesis.

##### Step 3: Import or Confirm the Problem Statement

The problem statement comes from ps-framing-the-problem. It should be imported directly, not rewritten.

If the user provides a problem statement, place it in Section 1 as-is. If the user does not have one, help them draft a brief problem statement, but flag it as unvalidated.

The problem statement anchors everything that follows. If the problem is vague, the hypothesis will be vague.

##### Step 4: Write the Solution Summary

Describe the proposed solution in one paragraph. This should come from the user's solution exploration work or their stated direction.

The solution summary should be:

- specific enough to be testable (not "build a better platform")
- written as what the solution does for the customer, not a feature spec
- one paragraph, not a list of capabilities

Word budget: ~30-40 words.

##### Step 5: List Solution Benefits

List 3-5 specific benefits. Each benefit should state the positive outcome for the customer or the business.

Test each benefit: does it describe an outcome, or does it describe a feature? "Automated data entry" is a feature. "Time saved on manual data entry, allowing specialists to focus on strategic initiatives" is a benefit.

Mix customer benefits and business benefits. At least two should be customer-facing, at least one should be business-facing.

Word budget: ~5-10 words per benefit, 3-5 benefits.

##### Step 6: List Risks and Assumptions

List 3-5 specific risks or assumptions that need to be validated.

Each risk or assumption should be:

- specific (not "things might go wrong")
- testable (the team can investigate whether it is true)
- relevant to the proposed solution (not generic business risks)

Common categories: technical integration risk, adoption risk, change management risk, data quality risk, regulatory risk.

Word budget: ~5-10 words per risk, 3-5 risks.

##### Step 7: Write the Customer-Focused Hypothesis

Write the first hypothesis using the If/Then structure:

**IF** we [describe the solution in terms of what it provides to the customer], **THEN** [describe the specific benefit the customer experiences].

The IF should reference the solution summary. The THEN should reference one or more of the benefits listed above.

Use role names, not persona names. "We save HR specialists time" not "we save Henry time."

Word budget: ~30-40 words.

##### Step 8: Write the Business-Focused Hypothesis

Write the second hypothesis. The IF of this statement picks up where the customer-focused hypothesis left off:

**IF** we [achieve the customer benefit from hypothesis 1], **THEN** [describe the measurable business outcome].

The business outcome should be specific and measurable. "We will achieve our goal of improving onboarding time by 30%" is measurable. "We will do better" is not.

Word budget: ~30-40 words.

##### Step 9: Verify the Chain

Check that the two hypotheses link correctly:

- Does the THEN of hypothesis 1 connect logically to the IF of hypothesis 2?
- Does hypothesis 1 focus on customer value?
- Does hypothesis 2 focus on business outcome?
- Are both written as If/Then statements, not as descriptions?

If the chain breaks, revise until the handoff is clean.

##### Step 10: Review for Solution Language vs. Outcome Language

Scan the entire artifact:

- Does the solution summary describe what the solution does, not how it is built?
- Do benefits describe outcomes, not features?
- Do hypotheses connect solutions to outcomes, not solutions to more solutions?
- Are risks specific and testable, not generic worries?

##### Step 11: Offer Next Steps

After the artifact is complete, offer the user up to three next-step options:

1. **Design a lo-fi experiment** - test the hypothesis with a prototype, concierge MVP, or Wizard of Oz approach before committing to full build
2. **Conduct risk assessment** - prioritize and investigate the identified risks and assumptions
3. **Connect to the roadmap** - use the validated hypothesis to inform roadmap planning and resource allocation

Present these as options, not as mandatory steps. The user decides what comes next.

### ps-solution-hypothesis / Template

##### When to Use This

Use this template during **Discover + Define** when you have a validated problem statement and have explored the solution space. You are ready to express your chosen solution direction as a testable hypothesis with expected customer and business outcomes.

Upstream work that feeds this template: framing the problem (ps-framing-the-problem), exploring the solution space (ps-exploring-solution-space), positioning statement (ps-positioning-statement, if available).

##### Template

```markdown
# Solution Hypothesis Statement

## Product Context

- Product or service:
- Target market segment:
- Primary customer (the person who uses or buys the product):

## 1. Problem Statement

Import from your Framing the Problem output. Do not rewrite.


> Quality check: Is this a validated problem statement, or an assumption? If it is an assumption, flag it.
> Quality check: Is the problem written from the customer's perspective, not the product team's?
> Capacity check: ~40-50 words (matching the final problem statement from ps-framing-the-problem).

## 2. Solution Summary

Describe the proposed solution in one paragraph. What does the solution provide to the customer?


> Quality check: Is this specific enough to be testable? "Build a better platform" is not testable.
> Quality check: Does the summary describe what the solution does for the customer, not how it is built?
> Quality check: Is there a clear connection between this solution and the problem statement above?
> Capacity check: ~30-40 words.

## 3. Solution Benefits

List 3-5 specific benefits. Each benefit should describe an outcome, not a feature.

-
-
-
-

> Quality check: Does each benefit answer "so what?" or does it just describe a capability?
> Quality check: Are there both customer-facing and business-facing benefits in the list?
> Quality check: Do benefits use role names ("HR specialists"), not persona names ("Henry")?
> Capacity check: ~5-10 words per benefit, 3-5 benefits.

## 4. Risks and Assumptions

List 3-5 specific risks or assumptions that need to be validated.

-
-
-
-

> Quality check: Is each risk specific enough to investigate? "Things might go wrong" is not specific.
> Quality check: Are these risks relevant to this solution, not generic business risks?
> Quality check: Could the team design a test or investigation for each risk?
> Capacity check: ~5-10 words per risk, 3-5 risks.

## 5. Solution Hypothesis Statement

### Customer-Focused Hypothesis

IF we [describe what the solution provides to customers],
THEN [describe the specific benefit customers experience].


### Business-Focused Hypothesis

IF we [restate the customer benefit from above],
THEN [describe the measurable business outcome].


> Quality check: Does the THEN of the customer-focused hypothesis match the IF of the business-focused hypothesis? This chain must connect.
> Quality check: Is the customer-focused hypothesis about customer value, not business metrics?
> Quality check: Is the business-focused hypothesis about a measurable business outcome, not a vague improvement?
> Quality check: Are both written as If/Then statements, not as feature descriptions?
> Quality check: Do hypotheses use role names, not persona names?
> Capacity check: ~30-40 words per hypothesis.

## Evidence Notes (optional)

- Upstream artifacts used:
- What is well-supported by evidence:
- What is still assumption:
- Recommended next validation steps:
```

##### Usage Guidance

###### Filling the Template

1. Start with **Product Context** to anchor who this is for and whose problem the solution addresses.
2. **Import the Problem Statement** from ps-framing-the-problem. Do not rewrite it.
3. Write the **Solution Summary** as one paragraph describing what the solution provides.
4. List **Solution Benefits** as outcomes, not features. Push each one past "what it does" to "why it matters."
5. List **Risks and Assumptions** with enough specificity that each one can be investigated.
6. Write the **Customer-Focused Hypothesis** first. Then write the **Business-Focused Hypothesis** using the THEN of the first as the IF of the second.
7. Verify the chain between the two hypotheses.
8. The **Evidence Notes** section is optional and trailing. Do not let it displace or delay the main artifact.

###### The Five Sections Build in Order

Do not skip ahead to writing hypotheses without completing the preceding sections. The problem statement grounds the solution. The solution grounds the benefits. The benefits and risks inform the hypothesis. Writing the hypothesis without the groundwork produces untethered speculation.

###### What Goes Where

| Section | Contains | Does NOT Contain |
|---------|----------|------------------|
| Problem Statement | Validated problem from upstream | New problem framing or solution language |
| Solution Summary | What the solution provides to customers | Implementation details, architecture, feature specs |
| Solution Benefits | Outcomes for customers and the business | Feature names, capability descriptions |
| Risks and Assumptions | Specific, testable failure modes or beliefs | Generic worries, vague concerns |
| Customer Hypothesis | IF solution THEN customer benefit | Business metrics, revenue targets |
| Business Hypothesis | IF customer benefit THEN business outcome | Feature lists, solution descriptions |

###### Connecting to Other Skills

- **Upstream:** ps-framing-the-problem provides the problem statement. ps-exploring-solution-space provides the chosen solution direction. ps-positioning-statement provides framing for how the solution fits the market.
- **Downstream:** The validated hypothesis drives lo-fi experimentation, risk assessment, and roadmap planning. The business outcome in hypothesis 2 should connect to the outcome tree if one exists.

###### Capacity Reference

See Template and capacity guidance (uploaded reference: `04-discover-define.md`, section `ps-solution-hypothesis / Template`) for the exact word and character budgets per field.

| Field | Word Budget | Guidance |
|-------|-------------|----------|
| Problem Statement | ~40-50 | Imported from ps-framing-the-problem |
| Solution Summary | ~30-40 | One paragraph, specific and testable |
| Solution Benefits | ~5-10 each | 3-5 outcome statements, not feature names |
| Risks and Assumptions | ~5-10 each | 3-5 specific, testable risks |
| Customer Hypothesis | ~30-40 | IF solution THEN customer benefit |
| Business Hypothesis | ~30-40 | IF customer benefit THEN business outcome |

### ps-solution-hypothesis / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** If produce distributors receive earlier shipment-condition signals, then they can intervene before spoilage; if spoilage falls, then the business may improve margin. Define tests for both links.
- **Weak:** "Add tracking, alerts, and dashboards" lists features without predicting a testable change.
- **Drift to avoid:** Feature list as hypothesis: an If clause alone is insufficient. The Then clause must specify a customer or business result.


#### Common Pitfalls

- **Writing a Feature List Instead of an If/Then Hypothesis:** Rewrite as an If/Then statement. The IF describes the solution. The THEN describes the expected outcome for the customer or business. "IF we provide automated workflows that reduce manual data entry, THEN field engineers will complete inspections 40% faster."

- **Merging the Two Hypotheses into One:** Separate into two statements. The customer-focused hypothesis connects solution to customer benefit. The business-focused hypothesis connects customer benefit to business outcome. The THEN of the first becomes the IF of the second.

- **Making the Solution Summary Too Vague to Test:** The solution summary must be specific enough that someone could design a test for it. "Implement an integrated HR management system with automated task workflows, centralized employee records, and a self-service portal for common requests" is testable.

- **Listing Generic Risks:** Each risk should name a specific failure mode. "Resistance to change from employees accustomed to the current manual process" is specific. "Integration with the legacy HRIS may require custom middleware not in the current budget" is specific.

- **Starting Without a Validated Problem Statement:** Complete ps-framing-the-problem first. If that is not possible, at minimum draft a problem statement and flag it as unvalidated. The hypothesis artifact should make visible whether the problem foundation is solid or assumed.

- **Using Persona Names Instead of Role Names in the Hypothesis:** Use role names: "IF we save HR specialists time on manual tasks, THEN they will redirect effort to strategic initiatives like talent development and workforce planning."

- **Writing Benefits That Are Just Restated Features:** Push each benefit one level further. "Automated data entry" becomes "Time recovered from manual data entry, allowing specialists to focus on higher-value work." The feature is the mechanism; the benefit is the outcome the customer cares about.

- **Writing a Business-Focused Hypothesis with No Measurable Outcome:** The business outcome must include a specific metric or target: "THEN we will reduce new employee onboarding time by 30%" or "THEN we will increase field inspection completion rates from 60% to 85% per quarter."

- **AI Writes the Bet:** The PM drafts the chain; the skill tests each link. Rewrites come after the critique, as options.

#### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-solution-hypothesis) for supporting source material and expanded examples.

## ps-positioning-statement | Positioning Statement

Playbook number: 13. Phase: Discover + Define.

### ps-positioning-statement / Instructions

#### Purpose

Create a **Productside-style Positioning Statement** for your product, service, or brand.

This skill is for the **Discover + Define** phase. It is where the PM crosses from investigation into definition. The positioning statement communicates the product's unique value in a way that aligns stakeholders, guides marketing, and filters product decisions.

With a positioning statement, a team can:

- Proactively choose target markets
- Promote competitive advantage
- Communicate benefits of the product
- Align marketing and product planning

Use this skill when you need to:

- articulate your product's unique value proposition in a structured, repeatable format
- align stakeholders on what the product is, who it serves, and how it differs
- create a filter for product development and marketing prioritization
- document competitive differentiation in outcome terms, not feature lists

Most Product Managers are working on a product that is already out in market. If that is your situation, find your product's existing positioning statement and see if adjustments are needed. If there is no existing positioning, you will craft one here.

##### Usage Notes

- The positioning statement uses the Productside seven-element formula: For / Who / The / Is a / That / Unlike / Our product gives. The order is fixed and all elements are required.
- The formula splits into two halves: Value Proposition (For through That) and Statement of Differentiation (Unlike, Our product gives).
- "That" must be a benefit (customer outcome), not a feature (product capability).
- "Unlike" must name a real competitive alternative, including status quo.
- "Our product gives" must use outcome language, not feature language.
- Upstream: ps-proto-persona (For element), ps-jobs-to-be-done (Who element), ps-problem-identification (need/opportunity).
- Downstream: solution hypothesis, product requirements, marketing messaging.
- This skill qualifies for both web research and user artifacts during evidence gathering.

#### Key Concepts

##### The Seven-Element Formula

The Productside positioning statement uses a fixed structure with seven elements. The order is required and the elements are non-negotiable:

**Value Proposition:**
- **For** [target customer]
- **Who** [statement of the need or opportunity]
- **The** [product name]
- **Is a** [product category]
- **That** [statement of key benefit]

**Statement of Differentiation:**
- **Unlike** [primary competitive alternative]
- **Our product gives** [statement of primary differentiation]

The first five elements establish the value proposition. The last two establish differentiation. Both halves are required.

##### Benefits Over Features

The "That" element is a benefit, not a feature list. A benefit describes the outcome the customer experiences. A feature describes what the product does.

- Feature: "provides real-time dashboards and automated alerts"
- Benefit: "gives more time back to the HR specialist for strategic projects"

If the "That" element reads like a feature spec, rewrite it as the outcome the customer cares about.

##### The "Unlike" Must Name a Real Alternative

The "Unlike" element must name the actual alternative the customer would choose if your product did not exist. This includes:

- a named competitor
- a category of competing products
- the status quo (manual processes, spreadsheets, existing workflows)
- doing nothing

It must not be a strawman - a weak or irrelevant competitor chosen to make differentiation easy. If the PM's strongest competitor is Salesforce, "Unlike" should not name a startup nobody has heard of.

##### Differentiation Must Be Outcome-Based

The "Our product gives" element must state what the customer gains in outcome terms, not what the product has in feature terms.

- Feature-based (wrong): "AI-powered analytics, real-time dashboards, and seamless integration"
- Outcome-based (right): "real-time data access, streamlined workflows and automates repetitive tasks"

The playbook example deliberately uses outcome language: the customer gets time back, gets streamlined workflows, gets automation of repetitive work. These are results, not specs.

##### Credibility Matters

The positioning statement must be believable and compatible with the company brand. Claims that sound like marketing hyperbole ("revolutionary," "world-class," "best-in-class") undermine the statement's utility as an internal alignment tool. If the team cannot defend the claim to a skeptical customer, it does not belong in the statement.

##### The Competitive Matrix Informs Positioning

The playbook pairs the positioning statement with a competitive matrix - a 2x2 grid where:

- The PM selects two of the strongest differentiating factors in their industry
- One factor is assigned to the X-axis, one to the Y-axis
- The PM's product and competitors are mapped on the grid
- The visual identifies positioning opportunity and white space

The competitive matrix is optional input for this skill. The PM may already understand their competitive landscape. But when competitive positioning is unclear, the matrix exercise helps surface the two dimensions that matter most before writing the statement.

##### One Persona, One Statement

Positioning is unique to a **segment and persona**. Write one statement for one persona, then rerun the exercise for each additional persona. A statement stretched to fit every segment speaks to none of them. If the product serves a user and a buyer, each gets their own statement.

##### The Claims Stay Yours

A statement can sound sharper than the evidence supports. Every claim in it (the need, the benefit, the differentiation) must be **relevant** to this persona's need, **credible** for this company, and **differentiated** enough to sway a purchase decision. Only customers and competitive research can confirm any of that. Competitor details that come from general knowledge, the agent's included, are leads to verify, not facts.

##### Positioning for Existing Products

Most PMs inherit a product that already has positioning - explicit or implicit. Before writing a new statement, find the existing one and evaluate whether it needs adjustment rather than replacement. Existing positioning lives in marketing sites, pitch decks, investor materials, and sales enablement docs.

Once the positioning statement is complete - whether newly crafted or refined - add it to the **Product Outcomes Canvas**. The canvas is where it lives as the messaging foundation for all downstream work.

##### How AI Supports This Play

The Playbook casts AI as a **critic of a draft the PM has already written**. It checks the statement against the Productside format, flags features posing as benefits, and challenges whether the differentiation holds up against the alternative the persona would actually choose. It proposes rewrites as options to react to, not replacements for the PM's words.

- **Use it when:** the PM has drafted a positioning statement for a specific segment and persona and wants it critiqued for benefits, relevance, credibility, and differentiation.
- **Avoid it when:** no target segment and persona has been chosen. AI will hand over polished positioning for a customer nobody has defined. Resolve the persona first (Step 1). If there is no draft, coach the PM to write one (see [Draft First, Then Critique](#draft-first-then-critique)).
- **Return:** features flagged where benefits belong, each claim tested for relevance, credibility, and differentiation, the alternative checked, and two or three proposed rewrites for the PM to accept, adapt, or reject.

##### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

##### Guided Mode

When asked for guidance, when the user is unfamiliar, or when context is missing:

1. Explain the output and estimated question count. Offer Guided, Context dump, or Best guess; default to Guided and ask the first question immediately.
2. Use supplied context instead of asking again. In Context dump mode, summarize Known / Assumed / Missing / Conflicting first.
3. Ask one bolded question per turn with a progress label, three context-specific numbered recommendations, option 4 Other, and an input hint. For facts only the user can know, ask openly without suggested answers and explain why. Ground unfamiliar domain options in research when needed.
4. Adapt recommendations to the answers. Explain why a question matters when helpful.
5. Answer interruptions, honor corrections and mode switches, and stop when asked. Resume with a brief recap and the pending question.
6. Recap supplied facts, assumptions, gaps, and readiness; confirm before generating a guided artifact. When the user faces a decision, recommend an option with reasons and offer distinct alternatives. The user decides.
7. Best guess may proceed immediately: label inferred details inline and end with Assumptions to Validate, ranked by decision impact. With sufficient supplied context, execute directly.

#### Application

Use Template (uploaded reference: `04-discover-define.md`, section `ps-positioning-statement / Template`) for the full scaffold.


##### Required Output Convention

Default to a **clean, paste-ready positioning statement artifact**.

That means:

- fill all seven elements of the formula
- keep each element concise enough to fit the template fields (~10-20 words per element)
- the "That" element states a benefit, not a feature
- the "Unlike" element names a real alternative
- the "Our product gives" element uses outcome language
- explanation belongs below the artifact, not inside the formula fields

The artifact comes first. Commentary is secondary.

##### Draft First, Then Critique

**By default, the PM writes the statement and the skill critiques it.** If the PM has no draft, coach them through Steps 4-10 one element at a time. Explain what each element needs, ask them to write it, and critique what they write. If the PM asks you to draft the statement, or chooses best guess mode, draft it and tag it `[AI-SUGGESTED, VALIDATE THIS]`, then run the same critique on your own draft.

##### If the PM Brings a Draft

Work through it one point at a time and wait for the PM's answers before rewriting (mirrors the critique guidance in this Play):

1. **Format:** is every element of the formula present?
2. **One persona:** if the statement could fit any customer, point at the words that make it generic.
3. **Features posing as benefits:** for each, ask what it does for the persona, and help restate it as an outcome they care about.
4. **Each claim:** relevant to this persona's need, credible for this company, differentiated enough to sway a purchase?
5. **The alternative:** using general knowledge of competitors and substitutes (including doing nothing or a manual workaround), did the PM name the alternative this persona would really choose, and does the differentiation hold up against it? Label anything you add about competitors as general knowledge to verify.
6. **Then propose two or three rewrites**, each explaining what it changes and why, for the PM to accept, adapt, or reject.

Keep the persona fixed. For another persona, run the critique again.

##### Step 1: Confirm the Product, Target Market, and Persona

Before writing anything, answer:

- what product or service are we positioning?
- who is the target market segment?
- who is the target customer within that segment? (user, buyer, or both)
- is there an existing positioning statement to evaluate first?

If you cannot answer those clearly, stop and resolve the target first.

**Guard against tech-role bias.** The "For" element names the customer - the person who uses or buys the product in the field. An IoT platform's customer is a fleet manager or logistics director, not a solutions architect. A clinical data platform's customer is a clinical operations lead, not a data engineer. Before writing the "For" element, confirm: does this person's primary job involve using the product's value, or are they the person who implements it technically?

##### Step 2: Gather Evidence Before Writing

Once you know the target, offer the user two things before drafting:

1. **Web research** - offer to search for the competitive landscape, how competitors position themselves, market category norms, and how practitioners in the target segment describe their needs. Look for competitor positioning pages, analyst reports, industry press, and practitioner forums. The goal is to understand what alternatives exist and how they are positioned, so the "Unlike" and "Our product gives" elements are grounded in reality.

2. **User-supplied artifacts** - ask whether the user has materials to share: existing positioning statements, competitive analysis, brand guidelines, pitch decks, marketing copy, prior discovery work, or any other material that would ground the statement in evidence.

Either, both, or neither is fine - the user decides. But always offer before drafting.

##### Step 3: Optionally Build a Competitive Matrix

If the PM needs help identifying their competitive landscape or finding the right differentiating dimensions, build a competitive matrix:

1. Identify 3-5 competitors (including status quo if relevant)
2. Brainstorm differentiating factors in the industry
3. Select the two strongest differentiating factors
4. Assign one to X-axis, one to Y-axis (both run Low to High)
5. Map the PM's product and competitors on the grid
6. Identify the positioning opportunity - where is the white space?

The matrix is optional. Skip it if the PM already knows their competitive position clearly.

##### Step 4: Fill "For" - Target Customer

Name the target customer in specific terms. This is the person who uses or buys the product in the field.

- Too broad: "businesses" or "enterprises"
- Too narrow: "Sarah, 34, in Omaha"
- Right level: "HR specialists managing high volumes of employee data and manual processes"

The "For" element should be specific enough that a reader can picture the person, but general enough to represent a segment, not an individual.

##### Step 5: Fill "Who" - Statement of Need or Opportunity

State the need or opportunity that the target customer faces. Use language from prior discovery work - jobs, pains, outcomes - not generic filler.

- Weak: "who want to be more efficient"
- Strong: "who need to reduce inefficiencies and focus on strategic HR initiatives"

If JTBD, proto-persona, or problem identification work exists, pull the need language from those artifacts. The "Who" element should feel like a direct echo of validated customer pain.

##### Step 6: Fill "The" - Product Name

Name the product. Use the actual product name the customer knows, not an internal code name or a generic category.

##### Step 7: Fill "Is a" - Product Category

Claim the product category. The category should be recognizable to the target customer - a label they would use when searching for solutions or describing the product to a colleague.

- Too broad: "a software platform"
- Too narrow: "a Python-based ETL pipeline with REST API support"
- Right level: "HR automation tool"

The category frames the customer's expectations. If they do not recognize the category, they will not understand the positioning.

##### Step 8: Fill "That" - Statement of Key Benefit

State the key benefit the customer receives. This is the single most important outcome - the reason the customer cares.

**This must be a benefit, not a feature.** A benefit describes what the customer gets. A feature describes what the product does.

- Feature (wrong): "provides automated workflows and real-time analytics"
- Benefit (right): "gives more time back to the HR specialist for strategic projects"

If the "That" element contains technical capabilities, architectural details, or feature descriptions, rewrite it as the customer outcome.

##### Step 9: Fill "Unlike" - Primary Competitive Alternative

Name the real competitive alternative. This is what the customer would do if your product did not exist.

**Hard constraint: the "Unlike" must name a real alternative.** This includes:

- a specific competitor by name
- a category of alternatives (e.g., "traditional manual processes and outdated systems")
- the status quo (e.g., "spreadsheet-based tracking and email coordination")

Do not use a strawman competitor. Do not name a competitor the target customer would never actually consider. The "Unlike" should make the reader think "yes, that is exactly what we are competing against."

##### Step 10: Fill "Our product gives" - Statement of Primary Differentiation

State what the customer gets from your product that they do not get from the alternative named in "Unlike."

**Hard constraint: differentiation must be in outcome terms, not feature terms.**

- Feature terms (wrong): "AI-powered analytics, real-time dashboards, and seamless integration"
- Outcome terms (right): "real-time data access, streamlined workflows and automates repetitive tasks"

The differentiation should pass this test: could the customer verify this claim from their own experience? "Real-time data access" is something a customer experiences. "AI-powered analytics" is something a product spec describes.

##### Step 11: Validate the Statement

Before finalizing, run the positioning statement through these checks from the playbook:

1. **Focused on benefits, not features?** - Does the "That" element describe what the customer gets, not what the product does?
2. **Relevant?** - Are the benefits relevant to the target customer's actual needs?
3. **Credible?** - Is the claim believable and compatible with the company brand?
4. **Differentiated and appealing?** - Does the statement offer clear, distinctive benefits that serve as a filter for purchasing decisions?

If any check fails, revise the specific element before finalizing. Propose revisions as options for the PM to accept, adapt, or reject, and say what each one changes.

##### Step 12: Keep the Artifact Compact

The canonical template uses labeled fields. Each element should be concise:

- "For": ~10-15 words
- "Who": ~10-15 words
- "The": ~3-5 words (product name)
- "Is a": ~3-5 words (category)
- "That": ~10-15 words
- "Unlike": ~8-12 words
- "Our product gives": ~15-20 words

If the output requires summarizing before it can be pasted into the playbook, it is too long.

##### Step 13: Offer Next Steps

After the artifact is complete, offer the user up to three next-step options:

1. **Add to the Product Outcomes Canvas** - the positioning statement belongs in the canvas as the messaging foundation for downstream plays; add it there so it is available to Go-to-Market, Key Messages, and any other play that references positioning
2. **Repeat for the next persona** - positioning is unique to a segment and persona; run the exercise again for each additional persona (e.g., the buyer as well as the user)
3. **Move to solution hypothesis** - use the positioning as input to define what the product must do to deliver on the promise

Present these as options, not as mandatory steps. The user decides what comes next.

### ps-positioning-statement / Template

##### When to Use This

Use this template during **Discover + Define** to articulate your product's unique value proposition and differentiation. This is where you cross from investigation into definition - the positioning statement aligns stakeholders, guides marketing, and filters product decisions.

Most Product Managers are working on a product already in market. If that is your situation, find your product's existing positioning statement first and evaluate whether it needs adjustment.

##### Template

```markdown
# Positioning Statement

## Product Context

- Product or service:
- Target market segment:
- Primary user persona:
- Buyer persona (if different):
- Existing positioning (if any):

## 1. Competitive Matrix (optional)

Select two of the strongest differentiating factors in your industry.
Map your product and competitors on the grid to identify positioning opportunity.

| | Low [X-Axis Factor] | High [X-Axis Factor] |
|---|---|---|
| **High [Y-Axis Factor]** | [Competitor] | [Your Product / Competitor] |
| **Low [Y-Axis Factor]** | [Competitor] | [Competitor] |

- X-Axis differentiating factor:
- Y-Axis differentiating factor:
- Competitors mapped:
- Positioning opportunity identified:

## 2. Positioning Statement

### Value Proposition

**For** _______________________________________________
[target customer]

**Who** _______________________________________________
[statement of the need or opportunity]

**The** _______________________________________________
[product name]

**Is a** _______________________________________________
[product category]

**That** _______________________________________________
[statement of key benefit]

### Statement of Differentiation

**Unlike** _______________________________________________
[primary competitive alternative]

**Our product gives** _______________________________________________
[statement of primary differentiation]

> Quality check: Is the "That" element a benefit (what the customer gets), not a feature (what the product does)?
> Quality check: Does the "Unlike" name a REAL competitive alternative the customer would actually consider?
> Quality check: Is the "Our product gives" element stated in outcome terms, not feature terms?
> Quality check: Are claims credible and compatible with the company brand?
> Quality check: Would a skeptical customer find this believable?
> Quality check: Are there any empty adjectives (innovative, seamless, best-in-class, cutting-edge)?
> Capacity check: For ~10-15 words. Who ~10-15 words. The ~3-5 words. Is a ~3-5 words. That ~10-15 words. Unlike ~8-12 words. Our product gives ~15-20 words.

## Evidence Notes (optional)

- What is well-supported by evidence:
- What is still assumption:
- Recommended next validation steps:
```

##### Usage Guidance

###### Filling the Template

1. Start with **Product Context** to anchor who this is for and whether existing positioning exists.
2. Optionally fill the **Competitive Matrix** to identify differentiating dimensions and positioning opportunity. Skip if you already know your competitive landscape.
3. Fill the **Positioning Statement** elements in order - the seven elements are a fixed sequence. Do not reorder or skip elements.
4. Run the quality checks before finalizing.
5. The **Evidence Notes** section is optional and trailing. Do not let it displace or delay the main artifact.

###### The Seven Elements

The Productside formula has a fixed structure. Fill each element in order:

| Element | What It Is | Word Budget | Guidance |
|---------|-----------|-------------|----------|
| For | Target customer | ~10-15 | Specific enough to picture, general enough to represent a segment |
| Who | Need or opportunity | ~10-15 | Use language from validated discovery, not generic pain |
| The | Product name | ~3-5 | Actual product name the customer knows |
| Is a | Product category | ~3-5 | Category the customer would use when searching or describing |
| That | Key benefit | ~10-15 | Outcome the customer experiences, NOT a feature |
| Unlike | Competitive alternative | ~8-12 | Real alternative the customer would actually choose |
| Our product gives | Primary differentiation | ~15-20 | Outcome-based, NOT feature-based |

###### Hard Constraints

These are not suggestions - they are rules:

- **"That" must be a benefit.** If it describes what the product does instead of what the customer gets, rewrite it.
- **"Unlike" must name a real alternative.** No strawmen. Status quo counts as a real alternative.
- **"Our product gives" must use outcome language.** If it reads like a feature list, rewrite it as customer results.
- **No empty adjectives.** Strip out "innovative," "seamless," "best-in-class," "cutting-edge," and similar filler.

###### Connecting to Other Skills

- **Upstream:** Proto-persona (the "For" element should match), JTBD (the "Who" element should echo validated jobs and outcomes), Problem Identification (validated problems inform the need)
- **Downstream:** Solution hypothesis, product requirements, marketing messaging
- **Parallel:** The competitive matrix can inform or be informed by market sizing work

###### Capacity Reference

See Template and capacity guidance (uploaded reference: `04-discover-define.md`, section `ps-positioning-statement / Template`) for the exact word and character budgets per field.

| Field | Word Budget | Guidance |
|-------|-------------|----------|
| For (target customer) | ~10-15 | Specific role + context |
| Who (need/opportunity) | ~10-15 | Echo validated discovery language |
| The (product name) | ~3-5 | Actual product name |
| Is a (product category) | ~3-5 | Customer-recognizable category |
| That (key benefit) | ~10-15 | Outcome, not feature |
| Unlike (competitor) | ~8-12 | Real alternative |
| Our product gives (differentiation) | ~15-20 | Outcome-based differentiation |
| Competitive matrix X-axis | ~3-5 | Differentiating factor label |
| Competitive matrix Y-axis | ~3-5 | Differentiating factor label |

### ps-positioning-statement / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For farm operations managers who need timely soil decisions, position the monitoring product around that benefit and a real alternative such as periodic manual sampling. Fill all seven elements.
- **Weak:** "An innovative platform for everyone" provides neither a specific customer nor a credible distinction.
- **Drift to avoid:** Feature-list differentiation: sensors and dashboards are capabilities. Explain the customer outcome that makes the alternative less attractive.


#### Common Pitfalls

- **Features Instead of Benefits in the "That" Element:** Rewrite the "That" element as the outcome the customer experiences: "That gives operations teams immediate visibility into site performance without waiting for weekly reports."

- **Strawman Competitor in the "Unlike" Element:** Name the alternative the target customer would actually choose. If the biggest competitor is Salesforce, name Salesforce. If the real alternative is the status quo (spreadsheets and email), name that. The "Unlike" should make sales reps nod, not roll their eyes.

- **Empty Adjectives in Differentiation:** Replace adjectives with specific outcomes. "Innovative" becomes "reduces onboarding time from weeks to days." "Seamless" becomes "works within the tools the team already uses without requiring migration."

- **Product Category Too Broad or Too Narrow:** Use the category label the target customer would use when searching for solutions or describing the product to a colleague. "HR automation tool" - an HR specialist knows what that means and can compare it to alternatives in the same category.

- **Target Customer Too Generic or Defaulting to a Tech Role:** Name the person who experiences the product's value in the field. If the product is a warehouse labor coordination platform, the target customer is "regional distribution center operations managers," not "businesses" and not "software engineers."

- **The Need/Opportunity Does Not Match Discovery Work:** Pull the "Who" language directly from JTBD artifacts, problem identification work, or empathy interview findings. The need should sound like something a customer actually said, not something a marketer assumed.

- **Differentiation in Feature Terms Instead of Outcome Terms:** Rewrite as outcomes: "Our product gives real-time data access, streamlined workflows and automates repetitive tasks." The customer can verify these claims from their own experience.

- **Forgetting Status Quo as a Valid Competitive Alternative:** Ask: what is the customer doing today without your product? If the answer is "spreadsheets and manual processes," that is a valid and often the most important "Unlike" to address.

- **AI Drafts Before the PM Does:** Coach the PM to draft first, then critique. If the PM asks for a draft, tag it `[AI-SUGGESTED, VALIDATE THIS]` and run the same critique on it.

- **One Statement Stretched Across Segments:** One persona, one statement. Rerun the exercise for each additional persona.

- **Claims Stronger Than the Evidence:** Test every claim for relevance, credibility, and differentiation. Verify competitor details before they shape the "Unlike" element. Soften or drop any claim the evidence can't carry.

#### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-positioning-statement) for supporting source material and expanded examples.

## ps-lofi-experimentation | Lo-fi Experimentation

Playbook number: 14. Phase: Discover + Define.

### ps-lofi-experimentation / Instructions

#### Purpose

Design a **Productside-style Lo-fi Experimentation artifact** from a proposed solution.

This skill helps a Product Manager turn a solution hypothesis into a complete, runnable experiment plan:

- two critical make-or-break assumptions
- a measurable If/Then hypothesis statement
- a fully specified experiment design (Method, Audience, Metric(s), Time Window, Decision Rule)
- a description of the experiment stimulus

The point is not to validate every assumption. The point is to identify the one assumption whose falseness would change everything, design the smallest possible test, and commit to action rules before results arrive.

This is a **commitment surface**, not an ideation surface.

#### Key Concepts

##### A Test Exists to Settle a Decision

Before designing anything, the PM names **the decision the test will inform**. If they cannot say what they will do differently depending on the result, the test is not worth running yet. Then they define **"done"**: the specific behavior that must be observed from customers or users for a pass, across how many people, and what a failure looks like. These set the finish line. The experiment has one job: produce that signal.

##### The Signal Comes From Real People

A lo-fi test buys evidence from **real customers or users** reacting to a cheap stimulus. The stimulus can be anything from a paper sketch to a vibe-coded prototype. The audience cannot be simulated. Synthetic users, AI-generated personas, or a model's prediction of how customers would react produce no evidence about customers. (The baseline deck's example used 100 simulated users; the B2B work-in-progress deck replaced it with a Wizard-of-Oz test on real passengers.)

##### The Least You Can Build

Every method should be cheaper and faster than building the real thing. Keep asking: what is the least we could build to get a real signal? Steer away from anything that looks like a working version of the product.

##### Lo-fi Means Fast, Not Cheap

The goal of lo-fi experimentation is signal speed, not cost reduction. A $50 user test that answers the question in two days beats a $500 study that takes six weeks. The constraint is time-to-signal, not budget.

##### The Assumption Must Be Make-or-Break

Not every assumption needs an experiment. The right assumption to test is the one that, if false, means the solution approach is wrong. Assumptions about preferences, edge cases, or technical implementation are secondary. The critical assumption is the one that sits under the solution's entire value proposition.

Productside criteria for a valid assumption:
- **Make-or-break**: if this is false, the solution approach changes significantly
- **About behavior or sentiment**: something a customer would do, feel, or believe - not an internal team capability
- **Testable this week**: specific enough that a test can produce a result within days, not months

##### The Lo-fi Hypothesis Differs from the Solution Hypothesis

The Solution Hypothesis (from ps-solution-hypothesis) chains: IF we provide this solution, THEN customers benefit, THEN the business achieves an outcome.

The lo-fi hypothesis is different. It describes a specific test and a specific observable signal:

"If we [expose customers to this stimulus], then [we will observe this specific, measurable result]."

The IF describes the test. The THEN describes an observable, countable result with a threshold.

##### The Decision Rule Prevents Rationalization

Specifying thresholds before results arrive forces the team to act on results rather than explain them away. The three-tier structure (continue / adjust / pivot) creates genuine decision points. Without it, teams find a way to continue regardless of what they learned.

##### Lo-fi Artifacts Are Also Communication Tools

Testing is the primary purpose of lo-fi experimentation. But a lo-fi artifact serves a second, equally valuable function: giving cross-functional stakeholders  -  designers, engineers, executives  -  a concrete, shared picture of the proposed solution before any build investment is made.

A clickable prototype or Wizard-of-Oz simulation makes the product concept tangible enough for meaningful conversation. It surfaces disagreements about user experience early, when the cost of changing direction is low. Product leaders can also use lo-fi artifacts to share the product vision with executives, making the problem and proposed solution vivid in a way that slides and written descriptions cannot.

The artifact you build to test an assumption also becomes the artifact that aligns the team.

##### Experiment Types from the Productside Catalog

- **Clickable prototype**: interactive mockup without working code
- **Wizard-of-Oz**: human-powered backend that looks automated to the user
- **Concierge**: PM or team member manually does the job for the customer to simulate the solution
- **Explainer Video**: short video that describes the solution and captures intent or reaction
- **Landing page test**: describes the offer and measures signups, clicks, or stated interest
- **Paper prototype**: hand-drawn or printed screens walked through with customers
- **Price sheet**: tests willingness-to-pay without a working product
- **Ad concept**: tests whether the value proposition generates interest
- **Fake door**: offers a feature or product that does not exist yet and measures who tries to use it
- **Vibe-coded prototype**: a quickly generated, throwaway interactive mockup used as the stimulus; real people still do the reacting

##### How AI Supports This Play

The Playbook casts AI as a **thought partner in two moments**. First, after the PM lists what must be true for the solution to pay off, AI widens the view toward assumptions the PM cannot see alone and pressure-tests which one is genuinely riskiest. Then it helps design the smallest, fastest test that could prove the PM wrong.

The reasoning stays with the PM. They name the assumptions, rank the risk, decide what a pass looks like, and decide what they will do about it. If AI hands over the riskiest assumption, the PM has skipped the thinking that shows whether they understand their own idea. AI sharpens the probe. The signal comes from real people, never from the model.

- **Use it when:** there is a prioritized solution, and the PM wants to find the riskiest assumption under it and design a cheap, fast experiment that drives a real decision.
- **Avoid it when:** the problem, persona, or solution is still vague. AI will manufacture confident assumptions and a tidy test with nothing real beneath them. Route back to ps-solution-hypothesis or ps-framing-the-problem.
- **Return:** blind-spot assumptions raised as candidates for the PM to weigh, a single riskiest assumption tied to a decision, and the smallest test that produces a real pass-or-fail signal.

##### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

##### Guided Mode

When asked for guidance, when the user is unfamiliar, or when context is missing:

1. Explain the output and estimated question count. Offer Guided, Context dump, or Best guess; default to Guided and ask the first question immediately.
2. Use supplied context instead of asking again. In Context dump mode, summarize Known / Assumed / Missing / Conflicting first.
3. Ask one bolded question per turn with a progress label, three context-specific numbered recommendations, option 4 Other, and an input hint. For facts only the user can know, ask openly without suggested answers and explain why. Ground unfamiliar domain options in research when needed.
4. Adapt recommendations to the answers. Explain why a question matters when helpful.
5. Answer interruptions, honor corrections and mode switches, and stop when asked. Resume with a brief recap and the pending question.
6. Recap supplied facts, assumptions, gaps, and readiness; confirm before generating a guided artifact. When the user faces a decision, recommend an option with reasons and offer distinct alternatives. The user decides.
7. Best guess may proceed immediately: label inferred details inline and end with Assumptions to Validate, ranked by decision impact. With sufficient supplied context, execute directly.

#### Application

Use Template (uploaded reference: `04-discover-define.md`, section `ps-lofi-experimentation / Template`) for the scaffold.


##### Required Output Convention

Default to a **clean, paste-ready artifact** with all four sections complete:

- exactly 2 key assumptions
- 1 hypothesis statement for the selected assumption
- a fully specified experiment design (all five elements)
- an experiment description specific enough to run

Explanation belongs below the artifact, not inside the fields.

##### Step 1: Apply the Tech-Role Bias Guard

Before identifying assumptions, verify the proposed solution addresses a customer-side problem, not an internal engineering or tooling challenge.

The assumptions to test should be about customer behavior, customer value, or customer adoption. If the assumptions are primarily technical implementation questions ("can we build this?"), redirect to a technical spike rather than a lo-fi experiment.

Ask: Who is experiencing the problem this solution addresses? If the answer is the development team or internal stakeholders rather than end users or buyers, pause and reframe.

##### Step 2: Collect Artifacts

Ask whether the user has materials to supply that would ground the experiment in evidence:

- the solution hypothesis from ps-solution-hypothesis (the If/Then chain)
- the framing-the-problem output (the five-stem problem statement)
- any prior customer feedback on the solution direction
- empathy interview notes that speak to adoption or behavior change
- any earlier lo-fi results that inform what to test next

The experiment should test the riskiest assumption embedded in the solution hypothesis. The more the user can supply, the more the assumption selection is grounded in real discovery rather than team intuition.

If there are no upstream artifacts at all, say so and note that the assumptions and experiment plan will be first-pass hypotheses requiring more grounding.

##### Step 3: Record and Widen the Assumptions

**The PM lists the assumptions first**, with their team: what must be true for the solution to create value for the customer and return value to the business. Drafting first is what lets you widen their thinking instead of doing it for them. Then (mirrors the critique guidance in this Play):

1. **Widen the list.** Ask what they may be taking for granted across customer behavior, adoption, and the business. You may name candidate assumptions they missed, marked as candidates for them to judge, not facts.
2. **Test each against the bar:**
   - **Make-or-break**: if this turns out to be false, the solution approach changes significantly
   - **About behavior or sentiment**: something a customer would do, feel, or believe, not an internal team capability or a feature specification
   - **Testable this week**: specific enough that a test produces a clear result within days

   Push the PM to cut the ones that fail.

Each assumption is a factual belief statement, not a question:

Good: "New users expect to complete account setup in a single session without help."
Weak: "Will users be able to complete setup?" (this is a question, not an assumption)
Weak: "The system will support single-session onboarding." (this is a technical capability, not a customer behavior)

The template holds **two key assumptions**: the two that most threaten the solution if false.

If the PM asks you to propose the assumptions, or chooses best guess mode, draft them tagged `[AI-SUGGESTED, VALIDATE THIS]` and run the same tests on them.

##### Step 4: Choose the Riskiest, Name the Decision, Define Done

1. **Pressure-test the PM's risk ranking.** For each assumption, ask how likely it is to be wrong and how much it costs if it is. **The PM chooses the single riskiest.** Do not choose for them. State their choice and reason explicitly.
2. **Name the decision** the test will inform. If the PM cannot say what they will do differently based on the result, tell them the test is not worth running yet.
3. **Define done:** the specific behavior that must be observed from customers or users for a pass, across how many people, and what a failure looks like.

These three (riskiest assumption, decision, win-and-failure condition) are the finish line for the experiment.

##### Step 5: Write the Hypothesis Statement

Turn the riskiest assumption into a testable If/Then statement (mirrors the critique guidance in this Play):

"If we [describe what we will expose the customer to or simulate], then [describe the specific observable result we expect to see]."

The THEN predicts a **behavior the PM can observe**, not a feature they would build. If it predicts a feature, make them fix it. It must include a numeric threshold or a specific observable behavior. "Users will find it easier" is not a hypothesis. "At least 70% of users will complete the task without requesting help" is.

The IF describes the test, not the full solution. "If we build a unified dashboard" is a solution description. "If we give new users a clickable prototype with a unified dashboard" is a test description.

##### Step 6: Design the Experiment

**Suggest two or three lightweight methods** (Wizard-of-Oz, concierge, fake door, vibe-coded prototype, explainer video, or others from the catalog). For each, ask what the least the team could build to get a real signal is. Steer away from anything that looks like a working version of the product.

Then help the PM complete all five elements. **The PM sets the metric, the time window, and the decision rule.** Question them; do not set them.

- **Method**: the specific lo-fi approach from the Productside catalog (clickable prototype, Wizard-of-Oz, Concierge, Explainer Video, landing page, paper prototype, price sheet, ad concept, fake door, vibe-coded prototype, or a clearly named equivalent)
- **Audience**: **real** target customers or users, and how they will be recruited (role, number, source). Never simulated participants.
- **Metric(s)**: the specific observable, countable thing to measure, mapped to the win condition, not satisfaction scores or vague impressions
- **Time Window**: the start and end date or duration of the experiment, with a real end
- **Decision Rule**: exactly three tiers specifying what the team will do if results exceed, meet, or fall below the threshold

The Decision Rule is required. Write it as:
- [threshold A] or above: continue as planned
- [threshold B] to [threshold A minus 1]: adjust [specify what changes]
- Below [threshold B]: pivot [specify what the pivot means]

**Check the whole design against the finish line:** would this test settle the decision? Does it give customers or users the chance to demonstrate the behavior the PM wants to observe? If not, show where it falls short.

##### Step 7: Describe the Experiment

Provide enough detail about what will be shown, said, or demonstrated that someone could run the experiment without redesigning it from scratch.

Include:
- the stimulus (mockup description, script, link, price sheet text, or ad copy)
- the core wording the customer will see or hear
- any task prompts or scenarios presented to participants

This section corresponds to the large right panel on the playbook template ("Visual or detailed text for your experiment").

Keep the description under 150 words. The goal is runnable clarity, not comprehensive specification.

##### Step 8: Add Optional Evidence Notes

If useful, add a brief trailing section with:

- what assumption remains untested after this experiment
- what the recommended next experiment would be
- any open risks not addressed by this experiment

Add this section only after the artifact is fully complete.

##### Step 9: Offer Next Steps

After completing the artifact, offer three options:

1. Run the experiment and return with results for interpretation
2. Design a second experiment for the remaining assumption
3. Proceed to ps-risk-assessment once the critical assumption is validated

### ps-lofi-experimentation / Template

##### When to Use This

Use this template during **Discover + Define** when you have a proposed solution direction (ideally from ps-solution-hypothesis) and need to validate the riskiest assumption about it before committing to build.

Upstream work that feeds this template: ps-solution-hypothesis (the If/Then hypothesis to stress-test), ps-framing-the-problem (the validated problem statement), ps-exploring-solution-space (the solution method selected).

This template produces a commitment artifact. By the time you complete it, you have identified what you believe, designed a test, and committed to acting on the results regardless of outcome.

##### Template

```markdown
# Lo-fi Experimentation

## Product Context

- Product or service:
- Proposed solution direction:
- Primary customer (the person whose assumption we are testing):

## 1. Key Assumptions

Work with your cross-functional team to list the assumptions that must be true for your solution to create value for the customer and return value to the business. Draft them yourselves first. Keep the two that are make-or-break, about behavior or sentiment, and testable this week.

**Assumption 1:**


> Quality check: If this assumption is false, does the solution approach change significantly? (If not, this is not make-or-break.)
> Quality check: Is this about customer behavior, feeling, or belief - not an internal technical capability?
> Quality check: Can a test produce a clear result within days, not months?
> Capacity check: ~25-40 words.

**Assumption 2:**


> Quality check: Same three tests as Assumption 1.
> Quality check: Is this assumption distinct from Assumption 1, not a restatement?
> Capacity check: ~25-40 words.

## Finish Line (decide before designing)

- Riskiest assumption (Assumption 1 or 2), and why it is riskiest (likelihood of being wrong x cost if wrong):
- Decision this test will inform (what we will do differently based on the result):
- Done: the behavior a pass requires, from how many people:
- What failure looks like:

> Quality check: If you cannot name the decision, the test is not worth running yet.

## 2. Hypothesis Statement

Select one assumption to test first. State which one and why (highest impact on the decision, lowest effort to stage, fastest time to a clear signal).

**Testing Assumption [1 or 2] because:**


**Hypothesis:**

If we [describe the specific stimulus or test we will run],

then [describe the specific, observable, measurable result we expect to see, including a numeric threshold or behavioral indicator].


> Quality check: Does the IF describe a test this week, not a fully built solution?
> Quality check: Does the THEN include a specific number or observable behavior - not "users will prefer it" or "adoption will improve"?
> Quality check: Could this hypothesis be clearly falsified if the threshold is not met?
> Capacity check: ~30-45 words for the full If/Then statement.

## 3. Design Experiment

Describe the smallest thing you will build or stage to test the hypothesis. Include all five elements.

**Method:**
(Specify the lo-fi approach: clickable prototype, Wizard-of-Oz, Concierge, Explainer Video, landing page, paper prototype, price sheet, ad concept, or a named equivalent.)


> Quality check: Is this the smallest method that generates a clear signal? If staging this requires multiple sprints of engineering, choose a lighter approach.

**Audience:**
(Who will participate and how they will be recruited: role title, number of participants, recruitment source.)


> Quality check: Is this the actual target customer, not a convenient internal proxy?
> Quality check: Are these real people? Simulated or synthetic participants produce no customer evidence.

**Metric(s):**
(The specific observable, countable thing to measure.)


> Quality check: Can this metric be observed and counted without subjective interpretation?
> Quality check: Is this tied directly to the hypothesis threshold?

**Time Window:**
(Start date and end date or duration.)


**Decision Rule:**

- [Threshold A] or above: continue as planned
- [Threshold B] to [Threshold A minus 1]: adjust - [specify what changes]
- Below [Threshold B]: pivot - [specify what the pivot means for the solution direction]

> Quality check: Do the three tiers create genuine decision points? A decision rule where all three tiers lead to "continue" is not a decision rule.
> Quality check: Is the pivot tier specific enough that the team knows what to do, not just "reconsider"?

## 4. Experiment Description

Describe what will be shown, said, or demonstrated. Include the stimulus (mockup description, script, ad copy, price sheet text), the core wording the customer will encounter, and any task prompts or scenarios.

Provide enough detail that someone could run this experiment without redesigning it from scratch.


> Quality check: Would someone unfamiliar with the solution be able to run this experiment from this description alone?
> Quality check: Does the description include both the stimulus and the task or question the participant is responding to?
> Capacity check: ~100-150 words.

## Evidence Notes (optional)

- Upstream artifacts used:
- What assumption remains untested after this experiment:
- Recommended next experiment:
- Open risks not addressed by this experiment:
```

##### Usage Guidance

###### Filling the Template

1. Start with **Product Context** to anchor whose assumption is being tested and which solution direction is under examination.
2. Write **both Key Assumptions** yourselves before selecting one to test. The act of writing both helps identify which is more critical.
3. Fill in the **Finish Line**: choose the riskiest assumption and say why, name the decision the test informs, and define what a pass and a failure look like. Do not imply the selection.
4. Write the **Hypothesis Statement** with a specific threshold before designing the experiment. The threshold drives the metric selection in section 3.
5. Complete all five **Design Experiment** elements. The Decision Rule is required, not optional.
6. Write the **Experiment Description** specific enough to run. This is the field that most often gets left vague.
7. Add **Evidence Notes** only after the artifact is fully complete.

###### What Goes Where

| Section | Contains | Does NOT Contain |
|---------|----------|------------------|
| Key Assumptions | Make-or-break customer behavior or sentiment beliefs | Technical feasibility questions, feature specifications, team preferences |
| Hypothesis Statement | Specific test description + measurable threshold | Full solution description, vague improvement language |
| Design Experiment | Method, Audience, Metric, Time Window, Decision Rule (all five) | General approach without specifics, metric without threshold |
| Experiment Description | Runnable stimulus and task prompts | Marketing pitch, comprehensive product spec |

###### Connecting to Other Skills

- **Upstream:** ps-solution-hypothesis provides the If/Then chain that surfaces the assumptions most worth testing. ps-framing-the-problem provides the validated problem that grounds the solution direction.
- **Downstream:** Results from the experiment feed ps-risk-assessment (once the critical assumption is validated, risks become clearer). ps-product-outcome-canvas (Template 16) draws from a validated solution direction.

###### Capacity Reference

| Field | Guidance |
|-------|----------|
| Each Key Assumption | ~25-40 words |
| Hypothesis Statement | ~30-45 words for the If/Then |
| Method | 1-2 sentences |
| Audience | 1-2 sentences including role, number, source |
| Metric(s) | 1 sentence with the specific measure |
| Time Window | Start and end or duration |
| Decision Rule | Three tiers, each with a threshold and action |
| Experiment Description | ~100-150 words |

### ps-lofi-experimentation / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For a consultancy onboarding workflow, isolate an uncertain customer behavior, test it with a small prototype, and agree on a decision rule before collecting results.
- **Weak:** "Build the wizard and see whether people like it" leaves both the assumption and decision rule vague.
- **Drift to avoid:** Solution-description bug: an experiment must expose an assumption to failure, not merely describe the planned feature.


#### Common Pitfalls

- **Treating Assumptions as Requirements:** An assumption should create doubt. Write each one as something you believe but are not certain of. Ask: "What would we do differently if this turned out to be false?" If the answer is "nothing," it is not a real assumption.

- **Hypothesis Without a Threshold:** Add a specific, countable threshold. At least 65% task completion. Average time under 8 minutes. Three out of five participants request a follow-up demo. Without a number or a specific observable behavior, the hypothesis cannot be falsified.

- **Testing What Is Easy, Not What Is Risky:** Ask which assumption, if false, would most change the solution direction. That is the one to test first, regardless of how uncomfortable the answer might be.

- **Missing the Decision Rule:** Write the decision rule before running the experiment, in the three-tier format: continue / adjust / pivot. The thresholds should create genuine decision points, not foregone conclusions dressed up as rigor.

- **Designing the Experiment as a Pitch:** A lo-fi experiment tests whether the assumption is true, not whether the team can present it compellingly. Include the parts of the experience that are most likely to fail.

- **Describing the Solution Instead of the Test:** The IF clause should describe the minimum stimulus the team can stage this week. "If we show new users a Wizard-of-Oz version of the unified data view..." is a test. "If we build a unified data platform..." is a project.

- **Skipping the Cross-Functional Team:** The playbook explicitly calls for cross-functional participation in Step 1. Assumption identification is a team exercise, not a solo PM task.

- **Building Too Much Before Testing:** Lo-fi means the smallest artifact that generates a clear signal. If staging the experiment requires building the product, something has gone wrong in the design step. Return to the method selection and find a lighter approach.

- **AI Names the Assumptions and Picks the Riskiest:** The PM lists the assumptions and chooses the riskiest. The skill widens the list with candidates marked as candidates, and pressure-tests the ranking by likelihood and cost.

- **A Test That Decides Nothing:** Name the decision and define done (Step 4) before designing anything. Check the finished design against that finish line.

- **Simulated Participants Treated as Signal:** The stimulus can be generated (a vibe-coded prototype is fine). The audience must be real target customers or users. If recruiting them is the hard part, choose a lighter method, not a simulated audience.

#### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-lofi-experimentation) for supporting source material and expanded examples.

## ps-storyboarding | Storyboarding

Playbook number: Unnumbered. Phase: Discover + Define.

### ps-storyboarding / Instructions

#### Purpose

Create a **Productside-style Storyboard** that validates a solution hypothesis through narrative.

This skill helps a Product Manager build a six-panel story centered on their target persona. The story follows a structured arc from the persona's status quo through a high-stakes conflict, into first contact with the solution, and finally to the lasting change that solution enables.

The storyboard belongs in the **Discover + Define phase** of the Productside Playbook. The B2B work-in-progress deck gives it no template number and places its instruction page right after Lo-fi Experimentation; the baseline deck had it as Template 16 of 24 in Create. It is explicitly low-fidelity. The playbook says it plainly: "Don't spend a lot of time building your storyboard; it doesn't need to look pretty!" Speed and clarity of thinking matter here. Aesthetics do not.

The storyboard does two things: it tests whether the PM's story about the customer rings true, and it gives stakeholders and real users something concrete enough to react to.

##### Usage Notes

- This is a component skill that produces a paste-ready six-panel narrative artifact.
- The Solution Hypothesis Statement (from ps-solution-hypothesis) anchors the top of every storyboard.
- Low fidelity is a design principle, not a limitation. Speed and clarity of thinking matter; aesthetics do not.
- The tech-role bias guard in Step 1 of Application is the single most important step in this skill.
- Upstream: ps-solution-hypothesis, ps-proto-persona, ps-framing-the-problem.
- Downstream: leadership alignment, executive communication, Go-to-Market narrative.

#### Key Concepts

##### Three Story Elements

Every storyboard requires three elements working together. If any one is missing, the story breaks down.

**Character** is the persona - the specific customer whose life the PM is trying to improve. The character must match the User Persona from ps-proto-persona. This is not the PM, not the product team, and not a generic user. It is a concrete individual with a job, a world, and things they care about.

**Conflict** is the problem - the specific breakdown that makes the persona's goal unreachable in the current state. The conflict should echo the Problem Statement from ps-framing-the-problem. A storyboard without a real conflict has no stakes and cannot be validated.

**Resolution** is the solution - how the product enters the persona's world and changes what is possible. The resolution must align with the If/Then structure from the Solution Hypothesis in ps-solution-hypothesis.

All three must be present and internally consistent. A strong character paired with a weak conflict produces a story no one can respond to. A strong conflict with a vague resolution does not validate the hypothesis.

##### The Six-Panel Arc

The storyboard uses six prompts in fixed order. Each prompt establishes something specific in the narrative.

**Panel 1 - "Once upon a time..."**
Introduce the persona and their world. Who are they? What does their day look like? What do they care about? This panel grounds the story in a real person with a real context.

**Panel 2 - "Every day..."**
Show the routine that leads toward the problem. What does the broken status quo look like day to day? This is not the crisis yet - it is the pattern that makes the crisis possible.

**Panel 3 - "Until one day..."**
The escalation moment. Something tips from friction into failure. The stakes are high here. A specific event or consequence makes the problem undeniable. This panel must be vivid - vague conflict produces vague feedback.

**Panel 4 - "Because of that..."**
The persona tries something new. They encounter the solution. This is not a feature list. It is an experience - what does it feel like to find and start using the product?

**Panel 5 - "Until finally..."**
The Aha moment. What does success feel like? Name the emotion. This is the moment the persona crosses from struggling to succeeding. Emotion matters here - it is what stakeholders and users respond to.

**Panel 6 - "And every day after that..."**
The lasting change. The persona's world is different now. What is possible that was not possible before? Behavioral change, not just happiness.

##### The Persona Is the Hero

The persona drives the story. The solution is their sidekick - it enables their success, but it does not achieve their goal for them. A storyboard where the solution is the hero has inverted the structure. The PM should be asking "what does the persona do differently?" not "what does the product do?"

##### Low Fidelity Is the Point

Speed matters more than polish in a storyboard. A rough narrative written in twenty minutes and shared with five users produces more insight than a polished visual deck. The six-panel format forces the PM to be specific without burning time on presentation. Images are optional; captions are sufficient.

##### What Validate Means Here

Storyboarding is a validation technique, not just a communication tool. Validation means showing the storyboard to real users or stakeholders and watching how they react. Do they recognize their world in Panel 1? Do they nod at Panel 3? Do they believe Panel 5? If the story does not ring true to people who live it, the hypothesis needs adjustment before anything is built.

##### The Storyboard Is Also a Product Visualization Tool

Validation with real users is the primary purpose of storyboarding. But the same artifact serves a second function: giving cross-functional stakeholders  -  designers, engineers, executives  -  a concrete, shared picture of the proposed solution before any build investment is made.

A well-constructed six-panel story makes the product's user experience visible in a way that wireframes and feature lists cannot. Stakeholders see the flow: the problem the product addresses, the moment of first contact with the solution, the breakthrough, the lasting change. They understand what the product actually does for the customer  -  its key capabilities and overall user value  -  without reading a requirements document.

Product leaders can use the storyboard to share the product vision with executives, making the problem and proposed solution vivid in a way that slides and written descriptions cannot. Build it once; show it to users for validation, show it to the team for alignment, and show it to leadership for direction-setting.

##### Text-First in This Skill

This skill produces text captions, not visual images. Each panel has a caption describing what should be depicted. The PM or a designer can add visuals later. The written captions are sufficient to share, discuss, and validate.

##### The Solution Hypothesis Statement Anchors Every Storyboard

Copy the If/Then statement from ps-solution-hypothesis and place it at the top of every storyboard. This anchors the story to a testable claim. If the story does not follow from the hypothesis, the storyboard is disconnected from the validation the PM needs.

##### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **critic of the storyboard the PM wrote, and a planner for showing it to real customers**. It checks that the persona is the hero and the product the sidekick, that the story follows the beginning, middle, and end arc from the solution hypothesis, and that the PM has a plan to show it to real target customers and record their reactions. The story and the reactions come from people, not the model.

- **Use it when:** the PM has a solution hypothesis and a draft story, and wants it sharpened and readied for testing with customers.
- **Avoid it when:** the request is to predict how customers will react to the storyboard. That is the test, and only real people can run it.
- **Return:** the story checked against the hypothesis and the three-part arc, the product kept in the sidekick role, and a plan to show the storyboard to real target customers and record what they say.

##### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

##### Guided Mode

When asked for guidance, when the user is unfamiliar, or when context is missing:

1. Explain the output and estimated question count. Offer Guided, Context dump, or Best guess; default to Guided and ask the first question immediately.
2. Use supplied context instead of asking again. In Context dump mode, summarize Known / Assumed / Missing / Conflicting first.
3. Ask one bolded question per turn with a progress label, three context-specific numbered recommendations, option 4 Other, and an input hint. For facts only the user can know, ask openly without suggested answers and explain why. Ground unfamiliar domain options in research when needed.
4. Adapt recommendations to the answers. Explain why a question matters when helpful.
5. Answer interruptions, honor corrections and mode switches, and stop when asked. Resume with a brief recap and the pending question.
6. Recap supplied facts, assumptions, gaps, and readiness; confirm before generating a guided artifact. When the user faces a decision, recommend an option with reasons and offer distinct alternatives. The user decides.
7. Best guess may proceed immediately: label inferred details inline and end with Assumptions to Validate, ranked by decision impact. With sufficient supplied context, execute directly.

#### Application

Use Template (uploaded reference: `04-discover-define.md`, section `ps-storyboarding / Template`) for the scaffold.


##### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

##### Step 1: Tech-Role Bias Guard

Before writing a single word of the storyboard, confirm who the product serves.

LLMs default to developer, architect, or product manager roles when no persona is specified. Most products serve non-programmers. A storyboard centered on a developer deploying a tool, when the product actually serves field technicians, operations staff, clinical workers, or line managers, will produce a narrative that fails to resonate with the real audience.

Ask the PM: who is the user persona for this product? Read the answer carefully. If the persona is a PM, engineer, developer, or architect - confirm this is actually the customer the product serves, not a proxy for the person running the exercise.

If the persona is the PM themselves, that is a signal the exercise has drifted. Redirect: who is the person your product is built for? That person is the hero.

##### Step 2: Gather Upstream Artifacts

Ask whether the PM has these artifacts to share:

- Solution Hypothesis from ps-solution-hypothesis (the If/Then statement that anchors the storyboard)
- User Persona from ps-proto-persona (the character's name, role, world, pains, and goals)
- Problem Framing from ps-framing-the-problem (the conflict source for Panel 3)

Accept equivalent input from any source. A PM with a product description but no prior plays can still run this skill. Do not block the exercise on missing upstream artifacts.

If artifacts are missing, gather the minimum needed:
- A specific product and what customer it serves
- A concrete description of the problem the customer faces
- A rough If/Then: if we build X, then the customer can do Y

##### Step 3: Write the Solution Hypothesis Statement Header

At the top of the storyboard, place the full If/Then statement from ps-solution-hypothesis (or the PM's equivalent).

Format it as a clearly labeled header:

```
Solution Hypothesis Statement:
IF we [description of solution], THEN [customer benefit].
IF [customer benefit], THEN [business outcome].
```

If only one half of the statement is available, use what is there. Do not fabricate the other half.

##### Step 4: Write Panel 1 - Introduce the Persona and World

Write the "Once upon a time..." caption.

Introduce the persona by name and role. Describe their world: what do they do day to day, what do they care about, what does success look like from their perspective? Ground the reader in a concrete person in a concrete context.

This panel should make the reader feel they know this person. Avoid generic descriptions ("a busy professional").

##### Step 5: Write Panel 2 - The Routine Status Quo

Write the "Every day..." caption.

Show the pattern of friction that precedes the crisis. What does the persona do repeatedly that is inefficient, risky, error-prone, or demoralizing? This is not the disaster yet - it is the condition that makes the disaster inevitable.

The goal of this panel is credibility. The reader (especially users or stakeholders who live this) should recognize the routine as real.

##### Step 6: Write Panel 3 - The Escalation Moment

Write the "Until one day..." caption.

Make this specific and high-stakes. A specific event or consequence tips the frustration into a real failure. Something breaks, something is missed, someone is affected. The stakes should feel real enough that the reader understands why doing nothing is not an option.

Vague conflict ("they faced some challenges") produces no feedback. Specific conflict ("she submitted an incorrect dosing report to the regulator and had to recall 30,000 units for re-audit") gives stakeholders something to react to.

##### Step 7: Write Panel 4 - First Encounter with the Solution

Write the "Because of that..." caption.

Show the persona encountering the product for the first time. This is an experience, not a feature list. What does it feel like to discover the solution exists? What is the first thing they do or notice?

Avoid writing "they used the product and it solved their problem." Describe the moment of first contact - what they saw, what they tried, what surprised them.

##### Step 8: Write Panel 5 - The Aha Moment

Write the "Until finally..." caption.

Name the emotion. This is the moment of breakthrough - the persona realizes the problem is solved or fundamentally changed. What do they feel? Relief, confidence, pride, surprise? Naming the emotion makes the story resonant and makes it easier for real users to confirm or deny when you show them.

##### Step 9: Write Panel 6 - The New Normal

Write the "And every day after that..." caption.

Show the lasting behavioral change. The persona's world is different now. What do they do differently? What is possible that was not possible before? What do they no longer worry about?

Avoid ending on "they were happy." Show what they can do, build, prevent, or decide that was out of reach before.

##### Step 10: Describe the Visual for Each Panel

For each panel, add a one-line visual description: what image or icon would represent this moment if the storyboard were illustrated?

This is optional but useful when sharing with visual thinkers or preparing the storyboard for a design session. Keep visual descriptions compact (5-15 words).

##### Step 11: Offer Next Steps

After completing the storyboard, offer three options:

1. Share with real users: walk three to five users through the storyboard panel by panel and capture where the story rings true and where it breaks down. The conflict moment and the Aha moment are the most important panels to test.
2. Share with leadership: the storyboard is an effective executive alignment tool. It makes the problem and solution concrete without requiring a slide deck.
3. Use in Go-to-Market messaging: the six-panel arc - problem, escalation, discovery, breakthrough, new normal - maps directly to launch narrative and sales enablement content.

### ps-storyboarding / Template

##### When to Use This

Use this template during the **Create phase** after you have a Solution Hypothesis in hand. The storyboard validates your hypothesis by telling the customer's story - from their everyday world through the problem crisis into the solution and beyond.

Upstream artifacts that feed this template:
- Solution Hypothesis (ps-solution-hypothesis): the If/Then statement that anchors Panel 1 and must survive to Panel 6
- User Persona (ps-proto-persona): the character - name, role, world, pains, goals
- Problem Framing (ps-framing-the-problem): the source of the conflict in Panel 3

You can run this with only a product description if needed. The hypothesis and persona can be sketched on the fly. Do not block the exercise on missing upstream artifacts.

##### Template

```markdown
# Storyboard

## Solution Hypothesis Statement

IF we [describe the solution], THEN [describe the customer benefit].
IF [customer benefit], THEN [describe the business outcome].

---

## Three Story Elements Check

Before writing the panels, confirm these three elements:

- Character (who is the persona?):
- Conflict (what is the problem - must echo the Problem Statement):
- Resolution (what does the solution enable - must align with the Hypothesis):

---

## Panel 1: "Once upon a time..."

Introduce the persona and their world. Who are they, what is their day like, and what do they care about?

[Write your caption here]

Visual description: [optional - what image or icon would represent this moment?]

> Quality check: Does the reader now know who this person is, what they do, and what matters to them? Avoid generic descriptions. Name the role and give one or two concrete details about their world.
> Capacity check: 20-35 words per caption; 5-15 words for visual description.

---

## Panel 2: "Every day..."

Show the routine or status quo that leads toward the problem. What does the broken normal look like?

[Write your caption here]

Visual description: [optional]

> Quality check: Is this a pattern, not an event? Panel 2 shows the friction that precedes the crisis. The crisis belongs in Panel 3.
> Capacity check: 20-35 words.

---

## Panel 3: "Until one day..."

The escalation moment. Something tips from friction into failure. Make it specific and high-stakes.

[Write your caption here]

Visual description: [optional]

> Quality check: Is the consequence specific and concrete? A vague conflict ("some challenges arose") produces no useful feedback. Name what breaks, who is affected, and what the cost is. This panel must earn the stakes of the story.
> Capacity check: 25-40 words.

---

## Panel 4: "Because of that..."

The persona tries something new - first contact with the solution. Write the experience, not the feature list.

[Write your caption here]

Visual description: [optional]

> Quality check: Is this written as an experience the persona has, or as a product capability list? "She discovered the system had already grouped the exceptions by type" is an experience. "The platform provides automated categorization, real-time alerts, and bulk actions" is a feature list. Write the experience.
> Capacity check: 20-35 words.

---

## Panel 5: "Until finally..."

The Aha moment. Success arrives. Name the emotion.

[Write your caption here]

Visual description: [optional]

> Quality check: Does this panel name a specific emotion (relief, confidence, pride, surprise) in addition to describing what the persona achieved? The emotion is what makes the story resonate with real users.
> Capacity check: 20-35 words.

---

## Panel 6: "And every day after that..."

The lasting change. What is now possible that was not possible before? Show the behavioral difference, not just the happiness.

[Write your caption here]

Visual description: [optional]

> Quality check: Does this panel describe a specific behavioral change - something the persona now does, builds, prevents, or decides that was out of reach before? "She feels much better" is not a lasting change. "She now closes the compliance cycle on Tuesday instead of Friday and uses the saved time to coach her junior analysts" is.
> Capacity check: 20-35 words.

---

## Hypothesis Alignment Check

After completing all six panels, re-read the Solution Hypothesis Statement at the top. Then ask:

- Does the conflict in Panel 3 match the problem named in the IF clause?
- Does the solution in Panel 4 match the solution named in the IF clause?
- Does the outcome in Panels 5 and 6 match the THEN clause?

If the story has drifted from the hypothesis, revise before sharing.

---

## Validation Plan

Who will you show this storyboard to?

- User validation (3-5 real users or customers):
- Stakeholder validation (executive or cross-functional review):
- Key question to test: [Which panel are you most uncertain about? What do you most need to hear from users?]
```

##### Usage Guidance

###### Filling the Template

1. Paste or write the Solution Hypothesis Statement at the top before writing any panel.
2. Fill in the Three Story Elements check - character, conflict, resolution - before Panel 1.
3. Write all six panels in order. Resist the urge to skip to Panel 4.
4. After writing all six panels, do the Hypothesis Alignment Check.
5. Add visual descriptions last, if at all.

###### What Goes Where

| Panel | Contains | Does NOT Contain |
|-------|----------|-----------------|
| Panel 1 | Named persona, concrete world details | Generic "busy professional" descriptions |
| Panel 2 | The recurring friction pattern | The crisis event (that belongs in Panel 3) |
| Panel 3 | A specific, consequential failure event | Vague struggle or "some challenges" |
| Panel 4 | The persona's experience of first contact | A feature list or product spec |
| Panel 5 | A named emotion plus the success moment | The product's achievement (not the persona's) |
| Panel 6 | Specific behavioral change going forward | Vague happiness or "life is better now" |

###### Connecting to Other Skills

- **Upstream:** ps-solution-hypothesis provides the If/Then statement; ps-proto-persona provides the character; ps-framing-the-problem provides the conflict source
- **Downstream:** the storyboard feeds leadership alignment, executive communication, and Go-to-Market narrative

###### Capacity Reference

| Field | Target Length | Guidance |
|-------|-------------|---------|
| Solution Hypothesis Statement | 40-70 words | Full If/Then statement from ps-solution-hypothesis |
| Panel 1-2 captions | 20-35 words each | One to three sentences; specific but not overlong |
| Panel 3 caption | 25-40 words | Slightly more room - the conflict needs enough specificity to be testable |
| Panel 4-6 captions | 20-35 words each | One to three sentences |
| Visual descriptions | 5-15 words each | Optional; describe the image, not the story |

### ps-storyboarding / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** A manufacturing quality inspector encounters a defect, faces its consequences, uses the proposed solution, and reaches a changed outcome across six frames.
- **Weak:** Six screenshots demonstrate an interface without telling a customer story.
- **Drift to avoid:** Tech-role inversion: the inspector is the protagonist; do not replace them with the developer building the tool.


#### Common Pitfalls

- **The Solution Is the Hero:** Rewrite every panel from the persona's perspective. What does the persona do, see, feel, or decide? The product should appear as the enabler of those actions, not the subject of the story.

- **Tech-Role Bias - Developer Persona for a Non-Developer Product:** Before writing Panel 1, confirm who the product is built for. Read the product description. Ask: who uses this in the field? Write for that person.

- **Polished and Long Panels:** Each panel caption should be one to three sentences at most. The prompt phrase does the framing work. The caption adds the specific, concrete detail. Keep it rough.

- **Missing the Conflict - Panel 3 Is Vague:** Name a specific event. Something breaks, fails, or causes visible harm. The more concrete the consequence, the more useful the feedback. "She submitted the wrong version of the report and the audit had to restart" is testable. "She had challenges with the process" is not.

- **Story Disconnected from the Hypothesis:** After completing all six panels, read the If/Then statement and then read Panel 3 and Panel 4. Are they about the same problem and the same solution? If not, the story has drifted. Rewrite to align.

- **Panel 6 Is Too Vague:** Name what the persona can now do, build, prevent, or decide that was impossible before. "She can now submit the monthly compliance report in one day instead of four, and she stops dreading the end of each quarter" is specific. "Things improved" is not.

- **Running This Before the Solution Hypothesis Exists:** Before running this skill, produce at least a rough If/Then statement using ps-solution-hypothesis. Even an informal hypothesis ("IF we automate the reconciliation step, THEN the operations manager can close the books without waiting on the data team") is enough to anchor the story.

- **Jumping to Product Features in Panel 4:** Panel 4 describes the persona's first experience, not the product's capabilities. "She logged in for the first time and saw her three overdue tasks organized by the system - she did not have to create the list herself" is an experience. A feature list is not.

- **Predicted Reactions Instead of a Test:** Show the storyboard to real target customers and record their reactions. Treat any predicted reaction as a guess to test.

#### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-storyboarding) for supporting source material and expanded examples.

## ps-risk-assessment | Risk Assessment

Playbook number: 15. Phase: Discover + Define.

### ps-risk-assessment / Instructions

#### Purpose

Create a **Productside-style Risk Assessment artifact** from a collaborative team review of a product in development.

This skill helps a Product Manager and their project manager identify potential threats to a product build or launch, classify those threats by severity and likelihood, and build specific mitigation and contingency plans for the highest-priority risks.

The point is not to list everything that could go wrong. The point is to help the team complete the play with a prioritized, actionable risk plan.

#### Key Concepts

##### This Play Is Collaborative, Not Solo

The playbook is explicit: do not run this assessment alone. Partner with your project manager, who can lead the collaborative effort, and involve relevant stakeholders. A solo PM risk list misses organizational, technical, and customer-facing blind spots that surface in a group session.

##### Mitigation and Contingency Are Not the Same

Every risk needs two plans, not one:

- **Mitigation Tactics**: what the team does to reduce the chance the risk occurs. These are proactive actions taken before the risk materializes.
- **Contingency Plans**: what the team does if the risk occurs despite mitigation. These are reactive responses to the risk having already happened.

A plan where both columns contain the same kind of content has not done the work.

##### Risk Breadth Matters More Than Risk Count

Six risks that are all technical is not a complete assessment. A well-formed risk list covers:

- Customer adoption and behavior change
- Technical implementation and integration
- Organizational readiness and change management
- Market or competitive timing
- Data, privacy, or compliance
- Resource or capacity constraints

##### Point of Contact Is the Risk Owner, Not the Task Doer

The Point of Contact is the person accountable for monitoring and managing the risk. This is not necessarily the PM or the person completing the assessment. For adoption risks it may be a change management lead. For technical risks it may be an engineering lead. For compliance risks it may be a legal or security owner.

##### Six Is the Canonical Count

The template has six rows in the identification table. Fill all six. Fewer usually means the team has not looked broadly enough.

##### Risk Assessment Is a Living Document

The assessment is not a one-time checkpoint. Risks change as the product is built, tested, and launched. At minimum, revisit at the first major build decision.

##### Template Capacity Matters

Risk names, mitigation tactics, and contingency plans should be paste-ready for the playbook template. Keep entries specific but compact.

See Template and capacity guidance (uploaded reference: `04-discover-define.md`, section `ps-risk-assessment / Template`) for canonical field budgets.

##### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **a widening and pressure-testing partner for the risks the PM's team brainstormed**. It asks whether the list covers enough ground, offers risk categories (and, after the PM answers, candidate risks marked as candidates), and checks that each mitigation, contingency, and owner is real. Severity, likelihood, and the plan stay with the team.

- **Use it when:** the team has brainstormed risks and wants the list widened and the management plan pressure-tested.
- **Avoid it when:** the request is for a finished risk register for a product the team hasn't discussed. The risks that matter are the ones only the team can see.
- **Return:** gaps in breadth named, candidate risks offered as candidates, each mitigation separated from its contingency, and each risk given a real owner.

##### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

##### Guided Mode

When asked for guidance, when the user is unfamiliar, or when context is missing:

1. Explain the output and estimated question count. Offer Guided, Context dump, or Best guess; default to Guided and ask the first question immediately.
2. Use supplied context instead of asking again. In Context dump mode, summarize Known / Assumed / Missing / Conflicting first.
3. Ask one bolded question per turn with a progress label, three context-specific numbered recommendations, option 4 Other, and an input hint. For facts only the user can know, ask openly without suggested answers and explain why. Ground unfamiliar domain options in research when needed.
4. Adapt recommendations to the answers. Explain why a question matters when helpful.
5. Answer interruptions, honor corrections and mode switches, and stop when asked. Resume with a brief recap and the pending question.
6. Recap supplied facts, assumptions, gaps, and readiness; confirm before generating a guided artifact. When the user faces a decision, recommend an option with reasons and offer distinct alternatives. The user decides.
7. Best guess may proceed immediately: label inferred details inline and end with Assumptions to Validate, ranked by decision impact. With sufficient supplied context, execute directly.

#### Application

Use Template (uploaded reference: `04-discover-define.md`, section `ps-risk-assessment / Template`) for the scaffold.


##### Required Output Convention

Default to a **clean, paste-ready artifact**.

That means:

- exactly 6 risks in the identification table
- all three sections completed
- Risk Management rows for at least the 2-3 highest-priority risks
- mitigation and contingency clearly distinct in every row
- no generic risk names like "Technical Risk" or "Market Concerns"
- explanation belongs below the artifact, not inside the fields

##### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

##### Step 1: Apply Tech-Role Bias Guard

Before starting, ask: is the product being evaluated built for a technical or engineering user? If yes, note it and proceed. If not, flag it as you work - risk lists generated for non-technical customer contexts often cluster around implementation concerns (performance, integration, security) because those are the risks the product team lives with, not the risks the customer faces.

This is especially important for risks in the customer adoption and change management categories. The team running this assessment is not the customer. Risks should span customer-facing failure modes, not just build-side concerns.

##### Step 2: Confirm Scope Beyond Technical Risks

Before brainstorming risks, ask the user to consider whether their current thinking is skewed toward engineering concerns. Product teams commonly produce risk lists that are almost entirely technical (performance, integration, security) while missing the risks that most often cause product failures: customer behavior change, organizational resistance, market timing, and adoption barriers.

Prompt the user to think across these categories:

- What adoption or behavior-change risks exist?
- What organizational or change management risks exist?
- What technical or integration risks exist?
- What market or competitive timing risks exist?
- What data, privacy, or compliance risks exist?
- What resource or capacity risks exist?

##### Step 3: Collect Available Artifacts

Before drafting, ask whether the user has materials to share:

- Solution hypothesis from ps-solution-hypothesis (defines what is being de-risked)
- Problem framing from ps-framing-the-problem (gives customer and problem context)
- Any early customer feedback or field observations
- Stakeholder concerns surfaced in prior conversations
- A Stakeholder Alignment artifact (useful for identifying Points of Contact)

The more context about what is being built and for whom, the more targeted the risk identification. Also confirm who will participate in the risk review session.

##### Step 4: Identify Six Risks

Work with the user to identify exactly six risks. For each, capture:

**Risk Name**: a short label that names the type of risk and the specific concern. Follow the pattern: `[Risk Type]: [Specific Concern]`. Example: "Workflow Disruption: surgeons resist new documentation steps."

**Risk Raised By**: the team member or stakeholder who surfaced this risk during the session.

Spread the six risks across at least three distinct categories. Do not let all six cluster in one area.

##### Step 5: Plot Level of Risk

For each of the six risks, classify two dimensions:

**Impact Severity** (if this risk occurs, how severely does it affect the business or product outcome?):
- High: threatens the product goal or business outcome directly
- Medium: causes significant delays, cost increases, or partial goal failure
- Low: creates friction or rework but does not threaten the goal

**Occurrence Probability** (how likely is this to occur given what we know?):
- High: likely without active intervention
- Medium: possible; some conditions that could trigger it exist
- Low: unlikely given current context, but worth tracking

Derive a priority from the combination:

| Impact | Probability | Priority |
|--------|-------------|----------|
| High | High | Critical |
| High | Medium | Critical |
| High | Low | Monitor |
| Medium | High | Critical |
| Medium | Medium | Manage |
| Medium | Low | Accept |
| Low | High | Manage |
| Low | Medium | Accept |
| Low | Low | Accept |

Present the classification as a structured list per risk, not as a visual grid.

##### Step 6: Build the Risk Management Table

For each Critical or Monitor priority risk, and optionally for Manage-priority risks, complete the risk management table:

- **Risk Name**: match exactly the name from Step 3
- **Mitigation Tactics**: specific actions that reduce the chance the risk occurs. Not "test more" or "communicate better." What specifically will the team do, when, and with whom?
- **Contingency Plans**: specific response if the risk occurs despite mitigation. What will the team do? Who decides? What is the timeline?
- **Point of Contact**: the named accountable owner for this risk. If no one can be named, that is a signal the risk is unowned.
- **Notes**: timing dependencies, escalation paths, or open questions

At minimum, complete rows for all Critical-priority risks. Leave Accept-priority risks out if needed to keep the artifact focused.

##### Step 7: Review the Completed Artifact

Before presenting the artifact, check:

- Do higher-priority risks have stronger, more specific plans than lower-priority ones?
- Is every Contingency Plan clearly different from its paired Mitigation Tactic?
- Is every Point of Contact a named individual, not a team or function?
- Are there risks that are actually testable assumptions? If so, flag them as candidates for ps-lofi-experimentation.
- Are priorities meaningfully differentiated? If everything is Critical, the classification has not done its job.

##### Step 8: Flag the Assessment as a Living Document

After delivering the artifact, note that this assessment should be revisited at key decision points. At minimum, flag one specific time to revisit: at the first major build or delivery decision.

##### Step 9: Offer Next Steps

At the end of the artifact, offer three options:

1. Convert the most critical testable assumption into a lo-fi experiment using ps-lofi-experimentation
2. Carry the risk summary forward into ps-product-outcome-canvas when that play is run
3. Share the assessment with stakeholders identified in the Risk Raised By column to validate completeness and confirm Points of Contact

### ps-risk-assessment / Template

##### When to Use This

Use this template during **Discover + Define** after completing your solution hypothesis and before committing to a build plan. Run it as a collaborative session with your project manager and relevant stakeholders.

Upstream artifacts that feed this template:
- Solution hypothesis (ps-solution-hypothesis): defines what is being built and what must be true for it to succeed
- Problem framing (ps-framing-the-problem): provides customer and context grounding for adoption risks
- Stakeholder Alignment artifact (if available): helps identify Points of Contact for each risk

##### Template

```markdown
# Risk Assessment

## Product Context

- Product or initiative:
- Stage (discovery, build, pre-launch, post-launch):
- Session participants:
- Date of assessment:

---

## Section 1: Identify Risks

Brainstorm the risks that could impact the success of this product or initiative.
Aim for exactly six. Cover adoption, technical, organizational, market, compliance, and resource categories.

| # | Risk Name | Risk Raised By |
|---|-----------|----------------|
| 01 | | |
| 02 | | |
| 03 | | |
| 04 | | |
| 05 | | |
| 06 | | |

> Quality check: Does each Risk Name name a specific concern, not a category? ("Workflow Disruption: clinicians resist new documentation steps" not "User Resistance")
> Quality check: Are risks spread across at least three distinct categories (adoption, technical, organizational, market, compliance, resource)?
> Quality check: Is each Risk Raised By a specific person, not a team or function?
> Capacity check: Risk Name should be ~5-8 words.

---

## Section 2: Plot Level of Risk

For each risk, classify Impact Severity and Occurrence Probability, then derive Priority.

Impact Severity: How severely would this affect the business or product outcome if it occurred? (High / Medium / Low)
Occurrence Probability: How likely is it to occur given what we know? (High / Medium / Low)

Priority guide:
- High Impact + High or Medium Probability = Critical
- High Impact + Low Probability = Monitor
- Medium Impact + High Probability = Critical
- Medium Impact + Medium Probability = Manage
- Medium Impact + Low Probability = Accept
- Low Impact + any Probability = Manage or Accept

---

Risk 01: [Risk Name]
  Impact Severity: [High / Medium / Low]
  Occurrence Probability: [High / Medium / Low]
  Priority: [Critical / Monitor / Manage / Accept]

Risk 02: [Risk Name]
  Impact Severity: [High / Medium / Low]
  Occurrence Probability: [High / Medium / Low]
  Priority: [Critical / Monitor / Manage / Accept]

Risk 03: [Risk Name]
  Impact Severity: [High / Medium / Low]
  Occurrence Probability: [High / Medium / Low]
  Priority: [Critical / Monitor / Manage / Accept]

Risk 04: [Risk Name]
  Impact Severity: [High / Medium / Low]
  Occurrence Probability: [High / Medium / Low]
  Priority: [Critical / Monitor / Manage / Accept]

Risk 05: [Risk Name]
  Impact Severity: [High / Medium / Low]
  Occurrence Probability: [High / Medium / Low]
  Priority: [Critical / Monitor / Manage / Accept]

Risk 06: [Risk Name]
  Impact Severity: [High / Medium / Low]
  Occurrence Probability: [High / Medium / Low]
  Priority: [Critical / Monitor / Manage / Accept]

---

> Quality check: Are priorities meaningfully differentiated? Not every risk should be Critical.
> Quality check: Is Impact Severity rated on business impact, not team inconvenience?
> Quality check: Are Critical risks clearly more urgent than Monitor or Manage risks?

---

## Section 3: Begin Risk Management

Complete this table for all Critical-priority risks. Include Monitor-priority risks if capacity allows.
Accept-priority risks may be listed without management rows.

| Risk Name | Mitigation Tactics | Contingency Plans | Point of Contact | Notes |
|-----------|-------------------|-------------------|------------------|-------|
| | | | | |
| | | | | |
| | | | | |

> Quality check: Is each Mitigation Tactic a specific proactive action that reduces the chance the risk occurs? ("Run pilot with 10 early adopters before full rollout" not "test more thoroughly")
> Quality check: Is each Contingency Plan a specific reactive response for if the risk occurs despite mitigation? ("Halt rollout and reconvene with adoption lead within 5 business days" not "communicate better")
> Quality check: Are Mitigation and Contingency clearly distinct from each other for every row?
> Quality check: Is each Point of Contact a named individual, not a team or role?
> Capacity check: Mitigation Tactics ~15-25 words; Contingency Plans ~15-25 words; Notes ~10-20 words.

---

## Revisit Note

Mark at least one future decision point where this assessment will be reviewed and updated:

- Next scheduled review:
- Trigger for unscheduled review (e.g., "if competitive landscape changes" or "at first major build decision"):
```

##### Usage Guidance

###### Filling the Template

1. Complete **Product Context** to anchor who is in the room and what stage the product is at.
2. Work through **Section 1** as a group. Push for specificity in Risk Names and for breadth across categories.
3. Complete **Section 2** risk by risk. Differentiate priorities. Resist the urge to rate everything Critical.
4. Complete **Section 3** starting with the highest-priority risks. Mitigation before contingency for each row.
5. Add the **Revisit Note** before closing the session.

###### What Goes Where

| Column | Contains | Does NOT Contain |
|--------|----------|------------------|
| Risk Name | Type + specific concern | Generic category labels |
| Risk Raised By | Named individual | "Team" or "Stakeholders" |
| Impact Severity | Business impact rating | Team inconvenience rating |
| Mitigation Tactics | Proactive prevention actions | Responses to the risk occurring |
| Contingency Plans | Reactive response if risk occurs | Duplicate of mitigation |
| Point of Contact | Named accountable individual | Team, function, or role title |

###### Connecting to Other Skills

- **Upstream:** ps-solution-hypothesis provides the solution context that grounds the risk identification. ps-framing-the-problem provides the customer and problem context.
- **Downstream:** ps-product-outcome-canvas (Batch 5) draws the risk summary from this assessment. ps-lofi-experimentation can convert high-priority testable assumptions from this assessment into structured experiments.

###### Capacity Reference

| Field | Target Length | Guidance |
|-------|--------------|----------|
| Risk Name | 5-8 words | Type label plus specific concern |
| Risk Raised By | 2-3 words | First name and last name or role |
| Mitigation Tactics | 15-25 words | Specific proactive action |
| Contingency Plans | 15-25 words | Specific reactive response |
| Notes | 10-20 words | Timing, dependencies, escalation |

### ps-risk-assessment / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For shipment tracking, name a specific threat, assess severity and likelihood, and distinguish prevention from the contingency if it occurs.
- **Weak:** "Technical risk: high" gives no event, consequence, or response.
- **Drift to avoid:** Response confusion: mitigation reduces likelihood or impact; contingency says what to do if the risk happens.


#### Common Pitfalls

- **All Technical Risks, No Adoption Risks:** Before finalizing the list, explicitly ask: what are the customer behavior change risks? What are the organizational readiness risks? What could cause the product to be technically correct but commercially unsuccessful?

- **Confusing Mitigation with Contingency:** Mitigation happens before the risk occurs and reduces the chance it will. Contingency happens after the risk occurs and limits the damage. Both are required.

- **Point of Contact as a Role, Not a Person:** Name a specific individual. If you cannot name one, that is a signal that the risk is unowned and needs an owner before the assessment is complete.

- **Risk Names That Are Categories, Not Concerns:** Follow the pattern: `[Risk Type]: [Specific Concern]`. "Market Risk" becomes "Competitive Timing: new entrant launches similar feature before our release."

- **Completing Risk Management Only for Easy Risks:** Start the Risk Management table with the Critical-priority risks. If time is limited, leave Accept-priority risks without management rows rather than leaving Critical ones blank.

- **Treating the Assessment as a One-Time Artifact:** Mark at least one specific future date or decision point where the assessment will be reviewed and updated.

- **Inflating Everything to High Severity:** Push the team to differentiate. If more than three risks are truly Critical, the team needs to re-examine whether the ratings reflect business impact or anxiety. Not every risk deserves equal attention.

- **Running the Assessment Alone:** Run this as a collaborative session. The project manager leads the facilitation. Stakeholders surface risks the PM team would not see from inside the product team.

- **A Risk List the Team Never Discussed:** The team brainstorms first. The skill widens the list with categories and candidates, and the team places and owns each risk.

#### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-risk-assessment) for supporting source material and expanded examples.

## ps-product-outcome-canvas | Product Outcome Canvas

Playbook number: 16. Phase: Discover + Define.

### ps-product-outcome-canvas / Instructions

#### Purpose

Create a **Productside-style Product Outcome Canvas** from the artifacts produced during the Discover + Define phase.

This skill is used at the **Go/No Go decision point** before the team enters the Create phase. Leaders use it to approve investment. PMs use it to practice presenting the business case to their sponsors and stakeholders.

The canvas brings together problem framing, solution positioning, customer stories, outcome targets, metrics, risks, and resource asks into a single, cohesive document. It is the artifact that answers the question leadership always asks: "Why should we build this, what will it do for us, and what do you need from us to make it happen?" It is not a summary slide.

#### Key Concepts

##### Why This Is a Go/No Go Document

The Product Outcome Canvas marks the formal end of the Discover + Define phase. At this point, the team has validated a problem, generated and explored solutions, formed a hypothesis, positioned the product, and assessed risks. The canvas consolidates all of that work into the form that leadership can evaluate and approve.

A canvas completed before this point is speculative. A canvas completed after this point is retrospective. The right moment is when the team has enough evidence to make a credible case but still needs authorization to proceed.

##### The Three-Section Structure

**Section 1: Core Information** anchors the document. Product Name, Date, Product Manager, and Version tell the reader what they are looking at and when.

**Section 2: Summary (left column)** tells the story of the problem and solution. It includes the Problem Statement, Solution Summary, Positioning Statement, two customer stories (one per persona), and the Key Features of the proposed solution.

**Section 3: Project Boundaries (right column)** frames the business case with measurable targets and honest constraints. It includes Business Outcomes, Product Outcomes, Business Success Metrics, Product Success Metrics, top Risks, The Ask, and the Introduction Date.

The two-column design is intentional: the left column persuades through narrative and context; the right column justifies through numbers and commitments.

##### Stories vs. Data

The two customer stories in the Summary section serve a purpose that data cannot: they make the problem real. A well-written story puts leadership in the room with the customer and makes the problem visceral. Data confirms the problem is worth solving; stories make people want to solve it.

Each story should anchor to a concrete moment in the customer's experience: a specific situation where the product either fails or succeeds. The before/after structure is the most reliable format: show the customer without the product, then show the same customer with it.

Stories are about the customer. Not the PM. Not the team. Not the development process. If the story protagonist is writing a PRD, facilitating a sprint, or reviewing a roadmap, the story is about the wrong person.

##### The Ask: Winning Approval

The Ask section is the resource request. Leadership needs to know three things: who you need, how much of their time, and for how long. A vague Ask ("we need engineering and design resources") is not an Ask. It is a wish. A credible Ask names roles, estimates percentage of time, gives a timeline, and flags any change management or infrastructure requirements.

An Ask that is too small under-allocates and sets the project up to slip. An Ask that is too large lacks credibility. Calibrate to the scope of what the canvas describes.

##### Loose Coupling to Upstream Plays

This skill draws from six upstream plays. Every field on the canvas can be populated from an upstream play artifact or from direct input, whichever the PM has available. The skill never blocks a field because an upstream play has not been run. If the PM has a problem statement from a workshop, a spreadsheet, or a prior document, that input is as valid as a ps-framing-the-problem output.

The upstream plays and their contributions:

| Canvas Field | Primary Upstream Source |
|---|---|
| Problem Statement | ps-framing-the-problem |
| Solution Summary | ps-solution-hypothesis |
| Positioning Statement | ps-positioning-statement |
| Business Outcomes, Product Outcomes, Metrics | ps-outcome-tree |
| Risks | ps-risk-assessment |
| Stories | ps-proto-persona (for persona context) |

If an upstream play has not been run, offer to run it before filling the field. If the PM has equivalent input from another source, accept it and proceed.

##### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **reviewer of the canvas before the Go/No Go decision**. It checks that each section is consistent with the upstream work it summarizes, that the user and buyer stories are grounded, that outcomes and metrics are measurable, and that the Ask is specific. Every claim on the canvas must come from the PM's work, because leadership will decide on it.

- **Use it when:** the PM has assembled the canvas from upstream artifacts and wants it reviewed before presenting it.
- **Avoid it when:** the upstream work doesn't exist yet. A canvas assembled from guesses becomes a Go decision on a guess.
- **Return:** inconsistencies between sections flagged, stories checked against evidence, outcomes and metrics checked for measurability, and the Ask sharpened into a specific decision and resource request.

##### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

##### Guided Mode

When asked for guidance, when the user is unfamiliar, or when context is missing:

1. Explain the output and estimated question count. Offer Guided, Context dump, or Best guess; default to Guided and ask the first question immediately.
2. Use supplied context instead of asking again. In Context dump mode, summarize Known / Assumed / Missing / Conflicting first.
3. Ask one bolded question per turn with a progress label, three context-specific numbered recommendations, option 4 Other, and an input hint. For facts only the user can know, ask openly without suggested answers and explain why. Ground unfamiliar domain options in research when needed.
4. Adapt recommendations to the answers. Explain why a question matters when helpful.
5. Answer interruptions, honor corrections and mode switches, and stop when asked. Resume with a brief recap and the pending question.
6. Recap supplied facts, assumptions, gaps, and readiness; confirm before generating a guided artifact. When the user faces a decision, recommend an option with reasons and offer distinct alternatives. The user decides.
7. Best guess may proceed immediately: label inferred details inline and end with Assumptions to Validate, ranked by decision impact. With sufficient supplied context, execute directly.

#### Application

Use Template (uploaded reference: `04-discover-define.md`, section `ps-product-outcome-canvas / Template`) for the scaffold.


##### Required Output Convention

Default to a **clean, paste-ready artifact**.

That means:

- all three sections completed
- stories written in close-third or first-person with a concrete time anchor
- The Ask specifies roles, percentages, and a timeline
- Risks are named specifically (top 3 from the risk assessment)
- no generic placeholders left in any field
- explanation belongs below the artifact, not inside the fields

##### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

##### Step 1: Tech-Role Bias Guard

Before writing any content, confirm who the product serves.

Most products serve people who do not write code: clinicians, logistics coordinators, field technicians, operations managers, procurement analysts, regulatory leads. LLMs default to developer/engineer protagonists when context is thin. The stories in this canvas will be wrong if the protagonist is a software engineer when the product serves a supply chain manager.

Ask the PM: "Who is the primary user of this product in the field? What is their job title? What does their day look like before this product exists?"

Use the answer to anchor both stories. If the PM cannot answer this question, offer to run ps-proto-persona before proceeding.

##### Step 2: Gather Upstream Artifacts

Ask the PM which of the following artifacts are available:

- Problem Statement (from ps-framing-the-problem or equivalent)
- Solution Summary or hypothesis (from ps-solution-hypothesis or equivalent)
- Positioning Statement (from ps-positioning-statement or equivalent)
- Business Outcomes, Product Outcomes, and Metrics (from ps-outcome-tree or equivalent)
- Risk Assessment (from ps-risk-assessment or equivalent)
- Persona descriptions (from ps-proto-persona or equivalent, for story context)

For each artifact that is not available, offer to run the corresponding skill or ask the PM to provide the information directly. Do not invent content for any field. If a field must be left incomplete, mark it clearly and note what is needed to complete it.

##### Step 3: Complete Core Information

Capture:

- Product Name (the actual product name, not a placeholder)
- Date (today's date, or the date of the Go/No Go session)
- Product Manager (the PM's name and role)
- Version (start at v1.0 unless the PM specifies otherwise)

##### Step 4: Write the Problem Statement

Use the final Problem Statement from ps-framing-the-problem if available. If not, ask the PM to describe the problem in 2-4 sentences covering: who is affected, what they are trying to do, what is blocking them, and why it matters to the business.

Do not write a problem statement that contains solution language. The problem statement describes the current state, not the desired future state.

Target: 40-60 words.

##### Step 5: Write the Solution Summary

Use the If/Then hypothesis format from ps-solution-hypothesis if available.

If not, ask the PM: "In one or two sentences, what does this product do and what does it enable the customer to do that they cannot do today?"

The Solution Summary describes the proposed solution at a level of specificity that makes the concept clear: specific enough to be meaningful, general enough not to lock in implementation details.

Target: 30-50 words.

##### Step 6: Write the Positioning Statement

Use the seven-element Positioning Statement from ps-positioning-statement if available. The seven elements are: For (target customer), Who (need or opportunity), The (product name), Is a (product category), That (key benefit), Unlike (primary competitive alternative), Our product gives (primary differentiation).

If the upstream artifact is not available, ask the PM to provide the positioning elements directly and assemble them using the formula.

Target: 50-70 words.

##### Step 7: Write Story 1 (User Persona)

Story 1 uses the user persona: the person who uses the product directly in the field.

Write a 2-4 sentence close-third or first-person narrative that anchors to a specific moment. Use a concrete time anchor ("Six weeks after the launch of X, Priya...") to make the story feel real. Show life before and after the product, or show a specific moment where the product makes a critical difference.

The story should make the problem tangible and the solution credible: not by listing features, but by showing the customer's experience.

Do not use the PM or the product team as the protagonist. Do not write a story about building, shipping, or configuring the product.

Target: 50-80 words.

##### Step 8: Write Story 2 (Buyer Persona)

Story 2 uses the buyer persona: the person who approves or funds the product, which may be a manager, director, procurement lead, or executive sponsor.

Use the same format as Story 1 but from the buyer's perspective. The buyer's story often centers on visibility, accountability, risk reduction, or efficiency rather than day-to-day task completion.

If no distinct buyer persona has been defined, ask whether the user and buyer are the same person. If so, note this in the artifact and write a single extended story, or ask the PM whether to differentiate.

Target: 50-80 words.

##### Step 9: Complete Project Boundaries (Outcomes and Metrics)

Use the ps-outcome-tree output if available. Populate:

- Business Outcomes: what the business gains from the product's success (revenue, efficiency, compliance, retention)
- Product Outcomes: what the customer achieves through using the product (role-based, not persona-named)
- Business Success Metrics: 2-3 measurable business-level indicators
- Product Success Metrics: 2-3 measurable product-level indicators

If the outcome tree has not been run, ask the PM to provide the outcomes and metrics directly. Outcomes must use outcome language (not feature language). Metrics must be specific and measurable: not "improve NPS" but "NPS increases from 32 to 45 within 12 months of launch."

Targets: Business Outcomes 15-25 words; Product Outcomes 15-25 words (bulleted); Metrics 2-3 items at 10-15 words each.

##### Step 10: List Key Features

List the top 3-5 features of the proposed solution. These are the capabilities the product will have: what it does, not what the customer achieves. Keep each item short and paste-ready.

Key Features are not outcomes. "Real-time shipment tracking dashboard" is a feature. "Logistics coordinators reduce shipment exception resolution time by 40%" is an outcome.

If the PM has not yet defined features, ask for the top 3-5 things the product will do. Do not infer features from the solution summary or positioning statement without confirmation.

Target: 3-5 bullets at 5-8 words each.

##### Step 11: List Top 3 Risks

Use the ps-risk-assessment output if available. Identify the top 3 risks by priority (Critical first) and list their names only. Do not include the full mitigation and contingency plans.

Risk names in the canvas are labels, not plans. The full risk management detail lives in the Risk Assessment artifact. The canvas shows leadership that the team has a risk picture; it does not replace the risk document.

If the risk assessment has not been run, ask the PM to name the 3 most significant threats to success. Use the format: [Risk Type]: [Specific Concern].

Target: 3 items at 5-8 words each.

##### Step 12: Write The Ask

The Ask is the resource request for the Create phase. It must include:

- Team composition: roles needed (e.g., Senior Engineer, UX Designer, Data Analyst)
- Time allocation: percentage of each role's time committed to this product
- Timeline: duration of the initial build phase (e.g., "8-week build sprint starting Q3 2026")
- Change management or infrastructure requirements: anything outside standard team capacity

If the PM does not have this information, prompt them with: "To give leadership a concrete Ask, I need to know: what roles do you need, how much of their time, and for how long?" Do not leave The Ask as TBD. It is the reason the canvas is presented.

Target: 30-50 words.

##### Step 13: Record the Introduction Date

The Introduction Date is the target launch or release date, meaning when the product reaches customers.

If the PM does not have a specific date, accept a target quarter or milestone ("Q4 2026" or "before annual customer conference in November"). Do not use TBD. If the date is genuinely unknown, flag it and note what decision would unlock it.

Target: 5-10 words.

##### Step 14: Offer Next Steps

After delivering the artifact, offer three options:

1. Share the canvas with the leadership sponsor or investment committee for the Go/No Go decision
2. Enter the Create phase by transitioning to build planning, user story mapping, or roadmap work
3. Schedule a structured review session to pressure-test The Ask and the risk picture before presenting

### ps-product-outcome-canvas / Template

##### When to Use This

Use this template at the **Go/No Go decision point** at the end of the Discover + Define phase, before the team commits to entering the Create (build) phase. Present the completed canvas to your leadership sponsor or investment committee.

Upstream artifacts that feed this template:
- Problem Statement (ps-framing-the-problem or equivalent)
- Solution Summary (ps-solution-hypothesis or equivalent)
- Positioning Statement (ps-positioning-statement or equivalent)
- Business Outcomes, Product Outcomes, and Metrics (ps-outcome-tree or equivalent)
- Top Risks (ps-risk-assessment or equivalent)
- Persona context (ps-proto-persona or equivalent, for story anchoring)

Loose coupling rule: if an upstream artifact is not available, provide the information directly or ask the agent to run the relevant skill before proceeding. No field should be left as TBD in the final canvas.

##### Template

```markdown
# Product Outcome Canvas

## Section 1: Core Information

- Product Name:
- Date:
- Product Manager:
- Version:

---

## Section 2: Summary

### Problem Statement

[Describe the customer problem in 2-4 sentences. Who is affected, what are they trying to do, what is blocking them, and why does it matter to the business? No solution language.]

> Quality check: Does the problem statement describe a current state without referencing the proposed solution?
> Quality check: Is the problem specific enough that leadership can picture who is affected and why it matters?
> Capacity check: 40-60 words.

---

### Solution Summary

[Describe the proposed solution in 1-2 sentences using If/Then format where possible. What does the product do, and what does it enable the customer to do that they cannot do today?]

> Quality check: Is the solution summary specific enough to be meaningful but general enough not to lock in implementation details?
> Quality check: Does the solution address the problem statement directly?
> Capacity check: 30-50 words.

---

### Positioning Statement

[Seven-element formula: For [target customer], who [need or opportunity], the [product name] is a [product category] that [key benefit]. Unlike [primary competitive alternative], our product gives [primary differentiation].]

> Quality check: Is the "That" element a benefit (what the customer achieves), not a feature (what the product does)?
> Quality check: Does the "Unlike" element name a real competitive alternative the customer would actually choose?
> Quality check: Does "Our product gives" use outcome language, not feature language?
> Capacity check: 50-70 words.

---

### Story 1: User Persona

[Write a 2-4 sentence close-third or first-person narrative anchored to a specific moment. Use a concrete time anchor ("Six weeks after the launch of X, [Name]..."). Show the customer's experience before and after the product, or show a specific moment where the product makes a critical difference. The protagonist is the customer, not the PM, not the product team.]

Narrative format guide:
- Open with a concrete time anchor and a specific name and role
- Show the specific friction or challenge the customer faces without the product, OR show the moment the product resolves it
- Close with the customer's changed experience or outcome
- Example anchor: "Before ClearRoute launched, Marcos Delgado, a procurement coordinator at a regional hospital network, spent three hours each Monday reconciling delivery confirmations across four supplier portals..."

> Quality check: Is the protagonist the customer or buyer? The PM, an engineer, or a product team member should never be the protagonist.
> Quality check: Does the story make a specific moment tangible rather than describing general benefits?
> Quality check: Is the persona name specific and realistic (not a placeholder like "User A")?
> Capacity check: 50-80 words.

---

### Story 2: Buyer Persona

[Write a 2-4 sentence narrative for the buyer persona: the person who approves or funds the product. Use the same format as Story 1. Buyer stories often center on visibility, accountability, risk reduction, or operational efficiency rather than day-to-day task completion. The protagonist is the buyer, not the PM, not the team.]

> Quality check: Is the buyer persona distinct from the user persona? If they are the same person, note this and adjust the story accordingly.
> Quality check: Does the story reflect a buyer's concern (investment, oversight, outcomes) rather than a user's concern (task completion)?
> Capacity check: 50-80 words.

---

### Key Features

[List the top 3-5 capabilities of the proposed solution. These are what the product does, not what the customer achieves. Short bullets, paste-ready.]

- [Feature 1: ~5-8 words]
- [Feature 2: ~5-8 words]
- [Feature 3: ~5-8 words]
- [Feature 4: ~5-8 words (optional)]
- [Feature 5: ~5-8 words (optional)]

> Quality check: Are these features (capabilities) rather than outcomes (results)? "Real-time exception alerts" is a feature. "40% faster resolution" is an outcome.
> Quality check: Are the features specific to this product rather than generic to any product in the category?
> Capacity check: 3-5 bullets at 5-8 words each.

---

## Section 3: Project Boundaries

### Business Outcomes

[What the business gains from this product's success. Use outcome language: revenue, efficiency, retention, compliance, market position. 1-2 sentences or a compact bulleted list.]

> Quality check: Are these business-level outcomes (what the company gains), not product-level outcomes (what the customer achieves)?
> Quality check: Do the outcomes connect to a measurable business goal?
> Capacity check: 15-25 words.

---

### Product Outcomes

[What the customer/user achieves through using the product. Use role names, not persona names. Bulleted list.]

- [Role] [achievement]: [context or measure]
- [Role] [achievement]: [context or measure]

> Quality check: Do these outcomes use role names (e.g., "logistics coordinators") not persona names (e.g., "Priya")?
> Quality check: Are these outcomes (what the customer achieves) distinct from Key Features (what the product does)?
> Capacity check: 15-25 words total.

---

### Business Success Metrics

[2-3 measurable business-level indicators. Each should be specific enough to track. Include direction, metric, and target where possible.]

- [Metric 1: direction + metric + target, ~10-15 words]
- [Metric 2: direction + metric + target, ~10-15 words]
- [Metric 3: optional, ~10-15 words]

> Quality check: Is each metric specific enough to measure ("NPS increases from 32 to 45 within 12 months") rather than directional only ("improve NPS")?
> Capacity check: 2-3 items at 10-15 words each.

---

### Product Success Metrics

[2-3 measurable product-level indicators. These track customer behavior and product performance, not business-level results.]

- [Metric 1: direction + metric + target, ~10-15 words]
- [Metric 2: direction + metric + target, ~10-15 words]
- [Metric 3: optional, ~10-15 words]

> Quality check: Are these product-level indicators (usage, task completion, error rate) distinct from business success metrics (revenue, retention)?
> Capacity check: 2-3 items at 10-15 words each.

---

### Risks

[Top 3 risks from the Risk Assessment, by priority. Names only; do not include the full mitigation and contingency plans. Format: [Risk Type]: [Specific Concern].]

1. [Risk Name: 5-8 words]
2. [Risk Name: 5-8 words]
3. [Risk Name: 5-8 words]

> Quality check: Are these the highest-priority risks (Critical first) rather than an exhaustive list?
> Quality check: Does each risk name a specific concern, not just a category ("Carrier Data Gaps: top 3 carriers lack real-time API" not "Technical Risk")?
> Capacity check: 3 items at 5-8 words each.

---

### What's Next: The Ask

[Name the resources needed to enter the Create phase: team roles, percentage of time, timeline, and any change management or infrastructure requirements. This must be specific enough for leadership to approve or negotiate.]

Format guide:
- Team: [Role] at [%] time, [Role] at [%] time
- Timeline: [duration and start date or quarter]
- Change management or infrastructure: [any requirements outside standard team capacity]

> Quality check: Does The Ask name specific roles and percentages rather than generic functions ("engineering and design resources")?
> Quality check: Is the timeline specific enough to evaluate (not "TBD" or "as soon as possible")?
> Capacity check: 30-50 words.

---

### Introduction Date

[Target launch or release date: when the product reaches customers. Accept a specific date, a target quarter, or a milestone anchor.]

> Quality check: Is the date specific enough to anchor planning? If TBD, note what decision would unlock it.
> Capacity check: 5-10 words.
```

##### Usage Guidance

###### Filling the Template

1. Start with **Section 1: Core Information** to anchor the document.
2. Complete **Section 2: Summary** starting with the Problem Statement, which grounds everything that follows.
3. Write the Positioning Statement before the stories; the positioning clarifies who each story is about.
4. Write the stories last in Section 2, after confirming the persona identities from ps-proto-persona or direct PM input.
5. Complete **Section 3: Project Boundaries** by importing from upstream artifacts wherever possible.
6. Write The Ask after reviewing all other sections; the resource request should reflect the full scope of what the canvas describes.

###### What Goes Where

| Section | Contains | Does NOT Contain |
|---------|----------|-----------------|
| Problem Statement | Customer-facing problem in current state | Solution language, product features |
| Solution Summary | What the product does and enables | Implementation details, technical specs |
| Stories | Customer or buyer experience, specific moments | PM process, team activities, feature lists |
| Key Features | Product capabilities (what it does) | Customer outcomes (what customers achieve) |
| Product Outcomes | What customers achieve (role names) | Persona names, product features |
| The Ask | Roles, percentages, timeline, requirements | Vague functions, TBD timelines |

###### Connecting to Other Skills

- **Upstream:** ps-framing-the-problem (Problem Statement), ps-solution-hypothesis (Solution Summary), ps-positioning-statement (Positioning Statement), ps-outcome-tree (Outcomes and Metrics), ps-risk-assessment (Risks), ps-proto-persona (persona context for stories)
- **Downstream:** Go-to-Market Enablement (Template 20) imports Problem Statement, Positioning Statement, and Key Features

###### Capacity Reference

| Field | Target Length | Guidance |
|-------|--------------|----------|
| Problem Statement | 40-60 words | Describes current state without solution language |
| Solution Summary | 30-50 words | If/Then format where possible |
| Positioning Statement | 50-70 words | Seven-element formula, benefit not feature in "That" |
| Story 1 | 50-80 words | Concrete time anchor, customer protagonist |
| Story 2 | 50-80 words | Buyer protagonist, visibility or accountability focus |
| Key Features | 3-5 bullets, 5-8 words each | Capabilities, not outcomes |
| Business Outcomes | 15-25 words | Business-level, not product-level |
| Product Outcomes | 15-25 words | Role names, not persona names |
| Business Success Metrics | 2-3 items, 10-15 words each | Direction + metric + target |
| Product Success Metrics | 2-3 items, 10-15 words each | Usage and behavior indicators |
| Risks | 3 items, 5-8 words each | Top priority risks, names only |
| The Ask | 30-50 words | Roles + percentages + timeline |
| Introduction Date | 5-10 words | Specific date, quarter, or milestone |

### ps-product-outcome-canvas / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For a hospital bed-coordination concept, consolidate the charge nurse's problem, tested hypothesis, outcomes, evidence, and risks for leadership's Go/No Go decision.
- **Weak:** A persuasive feature pitch without discovery evidence cannot support an informed investment decision.
- **Drift to avoid:** Decision substitution: a polished canvas does not constitute leadership approval or permission to proceed.


#### Common Pitfalls

- **Stories About the PM's Process Instead of the Customer's Experience:** The protagonist of every story is the customer or buyer. Read the first sentence of each story. If the subject is a PM, a designer, a developer, or a team, rewrite it. The story must anchor to the customer's day and the customer's experience.

- **Listing Every Risk Instead of the Top Three:** The canvas shows the top 3 risks by priority. Accept-priority risks belong in the full Risk Assessment artifact, not on the canvas. The canvas is a summary, not a transcript of the assessment.

- **The Ask Is Too Vague:** The Ask names specific roles ("2 Senior Engineers, 1 UX Designer, 1 Data Analyst at 80% time"), gives a percentage allocation, and names a timeline. If this information is not yet available, the canvas is premature. Run the planning work before presenting.

- **Treating the Canvas as a One-Time Artifact:** Treat the canvas as a living document. Update the Version number and Date when outcomes shift, risks change, or The Ask needs revision. The canvas should reflect the current state of the product investment, not just its initial framing.

- **Using Generic Placeholder Persona Names in Stories:** Use a specific, realistic name that reflects the persona's role and demographic diversity. Pair the name with a concrete job title and situation. "Priya Nair, a logistics coordinator at a mid-market distribution company, spends the first two hours of every morning..." is credible. "The user opens the dashboard..." is not.

- **Filling the Canvas Without Any Upstream Artifacts:** Before drafting any field, ask for the upstream artifacts or equivalent direct input. If no artifacts exist, flag the gap and offer to run the relevant upstream skill. Never invent the content of a field that is supposed to come from customer research or team validation.

- **Tech-Role Bias in the Customer Stories:** Run the tech-role bias guard in Step 1 before writing any content. Confirm the customer's job title and daily workflow. If the product serves non-technical users, the story must reflect non-technical concerns: task completion, time, accuracy, confidence, and visibility rather than system architecture or code quality.

- **Confusing Key Features with Product Outcomes:** Key Features are capabilities (what the product does). Product Outcomes are results (what the customer achieves). Each field serves a different purpose. If the same content appears in both sections, one of them is wrong.

- **A Canvas Built From Nothing:** Assemble the canvas only from upstream artifacts. Mark any section with no source as a gap, and say which play fills it.

#### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-product-outcome-canvas) for supporting source material and expanded examples.
