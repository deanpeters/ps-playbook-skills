---
name: ps-process-retrospective
description: >-
  Help a PM prepare for, facilitate documentation of, and close out a team
  retrospective using the Productside nautical four-quadrant model. Use when a
  team needs to reflect on a completed phase, sprint, launch, or project and
  produce concrete action items.
intent: >-
  Help a Product Manager structure and document a team retrospective that
  surfaces honest reflection on what worked, what did not, where the team is
  headed, and what obstacles lie ahead. The agent sets up and documents; the
  team runs the session. Psychological safety is the prerequisite; action items
  with owners and dates are the deliverable.
type: process
blueprint_stage: Deliver
best_for:
  - "Preparing and documenting a structured team reflection session"
  - "Capturing what went well, what failed, and what the team is aiming for next"
  - "Building a continuous improvement habit tied to the Productside lifecycle"
scenarios:
  - "We just finished a product cycle and I need to prepare a team retrospective"
  - "Help me document what went well, what failed, and our action items from the retro session"
---


## Purpose

Create a **Productside-style Process Retrospective artifact** from a structured team reflection session.

This is a process skill. The agent helps the PM prepare the session (roster, context, discussion prompts) and document the results after the team meets. The team itself surfaces what went well, what failed, what they are aiming for, and what they are worried about. The agent cannot substitute for that conversation.

This play reviews the **PM process itself** - how the team conducted discovery, framing, validation, and launch - not just what shipped or what engineering delivered. Wind and Anchors items should surface PM-process observations: "Discovery closed before enough customer interviews ran." "Problem statement was not validated with the team before framing began." "The outcome roadmap was never updated after the storyboard changed." These are the items that make a PM-process retrospective distinct from a generic team debrief.

The playbook is direct on two points. First: "Skipping retrospectives reduces the ability for teams to get better together." Second: "Create a safe space for admitting mistakes and learning from failure. Harnessing a growth mindset on the team is the only way to benefit from retros." Both of these are prerequisites, not afterthoughts. A retro run without psychological safety will not surface anything honest. A retro without action items is just a meeting.

Use this skill when you need to:

- close out a phase, launch, or discovery cycle with structured team reflection
- surface what the team learned and what to carry forward
- generate concrete action items with named owners before the next phase starts
- create an honest record of what worked and what failed in the PM process

This is not a software sprint retrospective. The standard agile format (What Went Well / What Didn't / What to Try Next) is a different structure with a different scope. The Productside model uses four named quadrants with a nautical metaphor, reviews the PM process not just delivery outputs, and requires action items with specific owners and dates. If you are running a sprint ceremony, this is the wrong play.

### Usage Notes

- This is a **process skill** (`type: process`), not a component skill. The agent sets up the session and documents the results. The team runs the actual retrospective.
- Evidence gathering: **neither** - no web research and no upstream artifacts are required. This is an internal team reflection exercise.
- No tech-role bias guard applies here. Step 1 instead confirms the scope and timeframe of the retro.
- Psychological safety is the prerequisite. If the Anchors quadrant is empty or vague, the retro has not worked.
- Action items with owners and dates are the primary deliverable. A retro without them is just a meeting.
- Downstream: ps-risk-assessment - significant Barriers identified in the retro may warrant formal risk planning.

## Key Concepts

### The Four-Quadrant Nautical Model

The retrospective is organized around a sailboat illustration that divides the canvas into four quadrants:

**Wind in Our Sails** (upper-left) - past-facing, positive. What has helped the team move forward? What has been successful? What has excited or motivated the team? Items here are honest wins and momentum.

**Beacons on the Horizon** (upper-right) - future-facing, positive. What milestones can the team work toward? What goals are within reach? What can the team get excited about? Items here are forward-looking aspirations and near-term anchors.

**Anchors Holding Us Back** (lower-left) - past-facing, problems. What has dragged the team down? What has prevented progress? When did the team fail or flounder? Items here name specific system and process failures - not individuals.

**Barriers We See Ahead** (lower-right) - future-facing, problems. What will the team need to navigate around? Where might the team get stuck? What problems are likely to get worse? Items here are anticipated obstacles that warrant planning now.

### The Two Axes

- **Left vs. right**: left quadrants are retrospective (what happened); right quadrants are prospective (what is coming). They require different conversations and different mindsets.
- **Upper vs. lower**: upper quadrants are positive (what is helping and where we are headed); lower quadrants are problems (what is hindering and what lies ahead). Both halves are required.

### Psychological Safety

Without it, the Anchors quadrant will stay empty or fill with safe abstractions. The team will perform positivity instead of reflection. The PM's job before the session is to create conditions where it is safe to name failures honestly - by name, specifically, without blame attaching to individuals.

The Anchors quadrant is the highest-signal quadrant. If it is empty or vague, the retro has not done its job.

### The Retrospective Builds Team Communication and Trust

The immediate output of a retro is a set of action items. The downstream output is a team that communicates better and trusts each other more.

When team members share their honest experience  -  what frustrated them, what they got wrong, where the process broke  -  and the team responds with curiosity instead of defensiveness, trust deepens. Engineers who hear the PM name a process failure, designers who hear that a handoff gap hurt the team, cross-functional partners who see that honest reflection is expected here  -  the retro is the practice that makes this kind of candor normal.

Teams that skip retros lose this mechanism. The frustrations remain; the shared understanding that comes from naming them together does not develop. "Skipping retrospectives reduces the ability for teams to get better together"  -  not only because the action items are lost, but because the communication habit that produces them is what builds the team over time.

### Items Are Sticky-Note Sized

Each quadrant contains short, specific items - 5 to 8 words each. Not paragraphs. Not explanations. "Deployment review had no rollback criteria" is a good item. "Our deployment processes were sometimes inadequate for the complexity of releases" is not. Specificity is the point.

### Action Items Are the Artifact That Matters

A retro without action items is venting, not improvement. Action items must have:
- An owner (a named person, not "the team" or "engineering")
- A specific action (not "improve communication")
- A date (by when, specifically)

The format is: [Owner] will [action] by [date].

### Phase Agnosticism

Retrospectives are not only for the end of a project. They can and should run at the end of any phase, sprint, launch, or cycle. The skill works for all of these.

### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **facilitation coach before the session and recorder after it**. It helps the PM prepare quadrant prompts and protect psychological safety, then turns the team's own items into specific, owned action items. The items come from the team; the agent never writes what the team experienced.

- **Use it when:** the PM is preparing to run a retrospective, or has the team's raw items to organize into action items.
- **Avoid it when:** the request is to write the team's Wind, Anchors, Beacons, or Barriers without a session.
- **Return:** discussion prompts for each quadrant, moves that keep the room safe, and action items with an owner and a date, built only from the team's items.

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

Use [Template](#template) for the scaffold.


### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

### Step 1: Confirm Scope and Timeframe

Before any setup, confirm:

- What product, project, feature, or sprint is this retro reviewing?
- What time period does it cover (start date to end date)?
- Is this a phase-end retro, a sprint retro, a post-launch retro, or something else?
- Has the work being reviewed concluded, or is it still in flight?

This grounds every subsequent step. A retro for a two-week sprint looks different from a retro for a six-month launch.

### Step 2: Set Up the Administrative Section

Fill in the left sidebar:

- **Retrospective for**: the product, project, or feature being reviewed (3-8 words)
- **Date**: the date the session will be or was held
- **Point of Contact roster**: the team roles and their owners. Standard roles include Project Manager, Executive Sponsor, Product Manager, Sales, Marketing, Communications, Operations, Customer Support, Release Engineer, and Legal. Add or remove rows to match the actual team. Each row captures: Role | Name and Title | Other (additional context).

Do not leave the roster blank. Part of the retro's value is that the right people are in the room. An empty roster means no one has decided who those people are.

### Step 3: Prepare Discussion Prompts for Each Quadrant

Offer the team the three guiding questions for each quadrant. These are not a rigid script - they are entry points.

**Wind in Our Sails:**
- What has helped us move forward?
- What has been successful so far?
- What has excited or motivated us?

**Beacons on the Horizon:**
- What milestones can we work toward?
- What goals do we have?
- What can we get excited about?

**Anchors Holding Us Back:**
- What is dragging us down?
- What has kept us from making progress?
- When did we fail or flounder?

**Barriers We See Ahead:**
- What will we need to navigate around?
- Where might we get stuck?
- What problems might get worse?

Share these prompts with the PM so they can prime the discussion or use them as facilitation aids in the session.

### Step 4: Provide Note-Taking Guidance

Before the session, brief the PM on item quality:

- Items should be short, honest, and specific - 5 to 8 words each.
- Name the concrete thing, not the abstract category. "Weekly standup ran over 30 minutes and blocked engineering time" is useful. "Communication was poor" is not.
- Items in the Anchors quadrant should name process and system failures, not individuals. "Deployment checklist was not followed for the Oct 3 release" is right. "Alex did not follow the process" is not.
- Both positive and negative quadrants need real content. A full Wind in Our Sails and an empty Anchors is a sign of a safety problem, not a good project.

### Step 5: Team Runs the Session

This step belongs to the team. The agent pauses here.

The PM facilitates the session, collects items in each quadrant, and captures raw notes. When the session is complete, the PM returns with the raw output and the agent picks up documentation from Step 6.

Offer this handoff explicitly: "Ready to help document the results when the session is done. Share the raw notes from each quadrant when you are back."

### Step 6: Record Wind in Our Sails Items

From the session output, record 3-5 specific items from the Wind in Our Sails quadrant. Keep each item to 5-8 words. If the raw notes are longer, help the PM compress them without losing the specific observation.

### Step 7: Record Anchors Holding Us Back Items

From the session output, record 3-5 specific items from the Anchors quadrant. This is the highest-priority documentation step.

If the team's Anchors items are vague ("things were hard sometimes"), flag this before recording. Offer to help the PM work backward to the specific observation: "What specifically was hard? What did 'hard' look like in practice?"

Ensure no item names an individual. If a raw item does, help the PM reframe it toward the system or process: "The approval process requires a 5-day wait with no parallel path" instead of "Jim takes too long to approve things."

### Step 8: Record Beacons on the Horizon Items

From the session output, record 3-5 items from the Beacons quadrant. If Beacons is empty, prompt the PM: "Did the team surface any goals or milestones they are excited about? Even rough ones count here." A team with no Beacons has no positive forward momentum - that is worth naming.

### Step 9: Record Barriers We See Ahead Items

From the session output, record 3-5 items from the Barriers quadrant. Note the difference from Anchors: Barriers are anticipated future problems, not past ones. They call for planning, not postmortem.

If items bleed between Anchors (past) and Barriers (future), help the PM sort them. The same root cause can generate both: an Anchor is the past occurrence, a Barrier is the recurrence risk.

### Step 10: Formulate Action Items

For each Anchor and each Barrier that has a concrete next step, draft an action item. Format: [Owner] will [specific action] by [date].

- Owner must be a named individual, not "the team" or "PM" as a generic.
- Action must be specific enough to verify completion. "Improve the deployment process" is not an action. "Priya will add a rollback checklist to the deployment runbook by Nov 1" is.
- Date must be real. If the PM does not have a date, prompt for one: "What is a realistic deadline for this given the current sprint?"

Produce 1-3 action items minimum. If the team surfaced 5+ Anchors and Barriers but produced 0 action items, something has gone wrong - name that.

### Step 11: Offer Next Steps

After completing the documented artifact, offer:

1. Share the completed retro with the full team for review - the people in the room should see the documented output before it is filed.
2. Schedule a follow-up check-in at the next logical milestone to review action item progress. A retro with no follow-up is a filing exercise.
3. Note whether any Barriers identified here should feed into a risk assessment (ps-risk-assessment) if they are significant enough to warrant formal mitigation and contingency planning.

## Template

### When to Use This

Use this template to prepare for, run, and document a team retrospective at the end of any phase, sprint, launch, or project. This is a process skill: the PM (or the agent) uses this scaffold to set up and document the session. The team supplies the content in the live discussion.

---

### Left Sidebar (Administrative)

#### Retrospective For

```
[Product, project, or feature name - 3-8 words]
```

> Quality check: Is this specific enough that a teammate not in the room would know exactly what is being reviewed?

#### Date

```
[Date of the retrospective session]
```

#### Point of Contact

The people in the room for this retro. Add or remove rows to match the actual team.

| Role | Name and Title | Other |
|------|---------------|-------|
| Project Manager | | |
| Executive Sponsor | | |
| Product Manager | | |
| Sales | | |
| Marketing | | |
| Communications | | |
| Operations | | |
| Customer Support | | |
| Release Engineer | | |
| Legal | | |

> Quality check: Is every role either filled or explicitly marked as not applicable? An empty roster means no one has decided who should be in the room.
> Quality check: Are the people listed the ones who actually did the work being reviewed?

#### Action Items

Complete this section after the session. Each item must have an owner, a specific action, and a date.

Format: [Owner] will [specific action] by [date].

```
-
-
-
```

> Quality check: Does every item name a specific person (not "the team")?
> Quality check: Does every item have a concrete completion date?
> Quality check: Is every action specific enough that the owner could verify it is done?
> Capacity check: 15-25 words per action item.

---

### Main Canvas (Four-Quadrant Discussion Board)

> **Phase gate:** The Left Sidebar (administrative section above) is completed by the PM and agent before the session. The four quadrants below are populated from the team's live discussion  -  not from project documents, history, or agent inference. Do not fill the quadrants before the session. Do not ask the agent to generate quadrant items. These sections belong to the team.

The four quadrants use a nautical metaphor. Upper quadrants are positive (what helps, where we are headed). Lower quadrants are problems (what hindered, what lies ahead). Left quadrants are past-facing (what happened). Right quadrants are future-facing (what is coming).

---

#### Wind in Our Sails (Upper-Left)

*Past-facing, positive. What has helped the team move forward?*

> "What has helped us move forward?"
> "What has been successful so far?"
> "What has excited or motivated us?"

```
-
-
-
-
-
```

> Quality check: Are these specific wins, not generic praise ("good teamwork")?
> Quality check: Does each item name something concrete that actually happened?
> Capacity check: 5-8 words per item (sticky-note sized).

---

#### Beacons on the Horizon (Upper-Right)

*Future-facing, positive. What goals and milestones is the team working toward?*

> "What milestones can we work toward?"
> "What goals do we have?"
> "What can we get excited about?"

```
-
-
-
-
-
```

> Quality check: Are these forward-looking aspirations, not restatements of past wins?
> Quality check: Is at least one item specific enough to know when it is achieved?
> Capacity check: 5-8 words per item (sticky-note sized).

---

#### Anchors Holding Us Back (Lower-Left)

*Past-facing, problems. What has dragged the team down or blocked progress?*

> "What is dragging us down?"
> "What has kept us from making progress?"
> "When did we fail or flounder?"

```
-
-
-
-
-
```

> Quality check: Does each item name a specific event, process failure, or system gap - not an abstraction?
> Quality check: Do any items name individuals? If yes, reframe toward the system or process.
> Quality check: Is this quadrant as substantive as Wind in Our Sails? If it is much shorter, that is a signal of a psychological safety gap.
> Capacity check: 5-8 words per item (sticky-note sized).

---

#### Barriers We See Ahead (Lower-Right)

*Future-facing, problems. What obstacles does the team anticipate in the next cycle?*

> "What will we need to navigate around?"
> "Where might we get stuck?"
> "What problems might get worse?"

```
-
-
-
-
-
```

> Quality check: Are these future-facing? If an item describes something that already happened, it belongs in Anchors.
> Quality check: Are the most significant Barriers candidates for formal risk planning (ps-risk-assessment)?
> Capacity check: 5-8 words per item (sticky-note sized).

## Examples

Illustrative and fictional, not customer evidence.

- **Strong:** After a dispatch launch, the team supplies the four nautical quadrants and agrees on actions in the form "[Owner] will [action] by [date]."
- **Weak:** "Communicate better" gives nobody a concrete action or completion point.
- **Drift to avoid:** Boundary violation: the assistant can prepare and document the retrospective but cannot invent the team's reflections before the session.


## Common Pitfalls

- **Running the Retro Without Psychological Safety:** Before the session, the PM should explicitly frame it as a safe space for naming mistakes. The Anchors quadrant is the measure of whether the safety worked. If it is empty, the session should be reconvened with a different frame - or the underlying safety issues should be addressed before trying again.

- **Items Written as Abstractions Instead of Observations:** Push to the specific observation. "Design review was scheduled with 2 hours notice three times in October" is actionable. "Communication was bad" is not. For every abstract item, ask: what specifically happened? When? What was the concrete effect?

- **Action Items Without Owners or Dates:** Every action item requires a named owner and a specific date. The format is: [Owner] will [specific action] by [date]. If either is missing, the item is not yet an action item.

- **Only the PM Fills In the Template:** The retro must involve the team. The PM can prepare the template and prompts alone (Steps 1-4 above). The content must come from the session. If a live session is not possible, the PM can collect async input from each team member and synthesize it - but solo input is a fallback, not the default.

- **Conflating Anchors and Barriers:** Anchors = what happened in the past that hurt us. Barriers = what we anticipate could hurt us in the future. The same root cause can generate both. Help the team make the cut explicitly: "Was this something that happened, or something you are worried might happen?"

- **Filing the Output Without Following Up on Action Items:** Schedule a check-in at the next milestone to review action item status. Ask whether each item was completed, deferred, or dropped - and why. A retro that generates the same action items twice in a row is a signal that either the action items were not specific enough, or the follow-up structure is broken.

- **Skipping the Beacons Quadrant:** Beacons do not have to be ambitious. Near-term milestones, small wins the team is looking forward to, a specific deliverable they are excited about - all count. Push the PM to ask the team: "What is something in the next cycle we can look forward to?"

- **Making It a Blame Session:** Anchors should name system and process failures, not individuals. "The handoff checklist did not include a sign-off step for the receiving team" names the process gap. "The delivery window was set without engineering input" names the planning failure. Help the PM reframe individual-blame items toward the systemic cause before documenting them.

- **A Retrospective Without the Team:** Prepare the session; record only the team's items. Turn them into action items with an owner and a date.

## References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-process-retrospective) for supporting source material and expanded examples.
