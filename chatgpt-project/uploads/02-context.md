# Context: Play references

November 2026 B2B work-in-progress Playbook. Not yet ratified.

Find Plays by stable identifier in 01-playbook-navigator.md. Each Play below contains its instructions, template, and examples. Mentions of skills or agents in the preserved source mean applying the Play from these uploaded references.

## ps-outcome-strategy-discussion | Outcome & Strategy Discussion

Playbook number: 01. Phase: Context.

### ps-outcome-strategy-discussion / Instructions

#### Purpose

Run the opening play of the Productside Playbook.

Before discovery begins, a PM needs one thing: a clear, shared understanding of the business outcome they are being asked to achieve. This play produces that understanding through a structured guided discussion with a manager, executive sponsor, or product leadership. The agent helps the PM prepare for that conversation and document what emerges from it. The conversation itself is PM-owned.

Use this skill when you need to:

- prepare a structured discussion guide before meeting with a manager or sponsor
- document the business outcome, context, and success criteria after the conversation
- surface assumptions the PM is already carrying so they can be validated rather than asserted
- make a Key Decision Point call: proceed to discovery, escalate for clarity, or reschedule

This is not a requirements intake. The PM is not receiving a brief. The PM is facilitating a two-way alignment where both parties build shared understanding. If the manager is dictating solutions during a conversation about outcomes, that is a signal to redirect.

#### Key Concepts

##### 1. Guided Discussion vs. Requirements Handoff

A requirements handoff is one-directional: someone tells you what to build. A guided discussion is two-directional: both parties contribute to building shared understanding of what the business needs to achieve and why.

The PM facilitates the discussion by asking open-ended questions, pressing when answers are vague, and recording what emerges. The manager or sponsor provides context, constraints, and strategic rationale. The output is not a spec. It is a shared written record of the alignment reached.

If a PM enters this conversation expecting to receive a feature list, they will miss the purpose of the play. The goal is a business outcome, not a scope document.

##### 2. Business Outcome First

The central task of this play is establishing the business outcome: what the organization is trying to achieve at a strategic or operational level. This is not a feature. It is not a project milestone. It is a measurable change in the state of the business.

Weak: "Launch the new shipper dashboard by Q3"
Stronger: "Reduce 90-day churn among mid-market shippers by 15%"

The launch is an output. The churn reduction is an outcome. This distinction matters because discovery cannot begin without clarity on the outcome. If the PM starts discovery while the business outcome is still defined as a project scope, they will optimize for the project and miss the customer problem.

##### 3. The Key Decision Point (KDP)

At the end of this play, the PM makes an explicit call about whether to proceed.

- Go: alignment is clear, the PM proceeds to discovery
- Partial: some areas are clear, others need follow-up by a specific date
- No-go: alignment is missing or contradictory - escalate or reschedule before continuing

The KDP is not a formality. Skipping it is the failure mode where a PM enters discovery without a stable business outcome and then produces research that no one can act on because the frame is still contested. If the manager cannot agree on the outcome, the PM should not proceed - they should surface the disagreement and request a follow-up.

##### 4. Three Roles of the PM in This Play

The PM wears three hats during this play:

- **Facilitator:** asks open-ended questions, creates space for the manager to think aloud, follows up when answers are vague or contradictory
- **Recorder:** captures what the manager says in structured notes during or immediately after the conversation, writes the agreed business outcome in one clear sentence
- **Sense-maker:** reviews the notes afterward to find gaps, contradictions, and unstated assumptions; flags open questions before starting discovery

The agent supports preparation (before) and documentation (after). The PM owns the middle.

##### 5. Preparing the Guide vs. Running the Discussion vs. Documenting Results

There are three distinct phases of this play:

- **Preparing the guide (agent-supported):** Draft open-ended questions for each discussion area. Surface assumptions the PM already holds. Flag visible gaps or contradictions before the conversation begins.
- **Running the discussion (PM-owned, agent cannot participate):** The PM facilitates the conversation, takes notes, and makes judgment calls in real time. The agent cannot do this.
- **Documenting outcomes (agent-supported):** After the conversation, the PM shares their notes with the agent, who helps structure the summary, identify gaps, and draft the KDP call.

If the user asks the agent to conduct the discussion itself or generate what "the manager probably said," redirect: the discussion must happen with a real person who has context the agent does not have.

##### 6. The Five Discussion Areas

Every guided discussion for this play covers five areas:

1. **Business Outcome** - what the business needs to achieve, written as a measurable change
2. **Why Now** - what changed that makes this the priority, and what happens if it is not addressed
3. **Customer** - who the product serves (role and context), and whether there are secondary stakeholders
4. **Success Criteria** - what measurable change would indicate the outcome was achieved
5. **Constraints and Non-Negotiables** - what is already decided, what is off-limits, and what dependencies exist

These five areas are the structure of both the discussion guide and the documentation template. A conversation that covers all five and produces specific, agreed answers is a successful execution of this play.

##### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **preparation coach for the discussion, never a stand-in for the manager**. It helps the PM gather what they already know, turn it into sharp, unbiased questions for each discussion area, and name the decision the discussion must reach. The answers come from the manager, in the room.

- **Use it when:** the PM has gathered the key documents and wants to prepare questions for the discussion, or has notes from the discussion to turn into the template.
- **Avoid it when:** the request is to guess what the manager will say, or to fill the discussion template without the discussion happening.
- **Return:** the PM's own questions for each discussion area, tested for bias and clarity; the business outcome stated as a measurable change; and, after the discussion, the template filled only from the PM's notes.

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

Use Template (uploaded reference: `02-context.md`, section `ps-outcome-strategy-discussion / Template`) for the working scaffold.


##### Required Output Convention

Default to a **clean, paste-ready structured summary** with clearly labeled sections.

That means:

- fill all five discussion areas
- write the business outcome as a single, specific, measurable sentence
- keep the customer statement concrete (a job title and context, not an org chart entry)
- list open questions rather than omitting them
- write the KDP call with a checkbox clearly marked

The summary comes first. Commentary is secondary.

##### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

##### Step 1: Confirm Scope and Participants

Before preparing the guide, establish:

- Who is the discussion with? (direct manager, exec sponsor, product leadership - name and role if possible)
- What product or initiative is this for?
- What is the time horizon? (quarterly, annual, multi-year)
- Has any prior alignment work been done? (existing OKRs, product brief, strategy deck)

This play does not require a tech-role bias guard. The subject of this conversation is internal strategic alignment, not a customer persona. The customer who the product serves will be identified during the discussion and documented afterward - they are not the subject of this exercise.

Note any prior materials the PM already has, because they will inform which questions can be skipped and which need more depth.

##### Step 2: Prepare the Discussion Guide

Draft open-ended questions for each of the five discussion areas. Questions should:

- invite the manager to think and articulate, not confirm a preformed answer
- be specific enough to prevent vague responses without being leading
- follow a logical progression from big picture to specifics

For each area, also surface the assumptions the PM is already carrying. Write them explicitly so they can be validated (confirmed or corrected) during the conversation rather than treated as facts.

Flag any gaps or contradictions already visible before the conversation. If the PM says "I think we're trying to reduce churn but my manager mentioned a revenue target last quarter," that contradiction should be in the prep guide so the PM knows to resolve it.

**Sample questions for each area:**

Business Outcome:
- What does the business need to achieve in the next [time horizon]?
- How does this connect to our broader strategy or annual goals?
- How will we know, in [X months], that we achieved it?

Why Now:
- What changed that makes this the priority now?
- What happens if we do not address this this quarter or year?

Customer:
- Who is the primary customer this outcome serves?
- Are there secondary customers or stakeholders whose needs we must also respect?

Success Criteria:
- What would measurable success look like at [time horizon]?
- Are there existing metrics or targets we are accountable to?

Constraints and Non-Negotiables:
- What is already decided - budget, timeline, technology choices?
- What is off-limits or outside scope?
- Are there dependencies we must work around?

##### Step 3: Run the Discussion (PM-Owned)

This step is performed by the PM. The agent does not participate.

The PM should:

- facilitate rather than receive (ask questions, follow up, redirect solution-talk back to outcome-talk)
- take notes during or immediately after the conversation
- watch for vague answers and press for specifics ("improve performance" needs a metric; "grow the business" needs a direction and timeframe)
- note when the manager starts proposing solutions - this is a signal that the outcome is not yet clear
- watch for false alignment: both parties nodding without actually agreeing on specifics

**What good alignment feels like:** both parties can state the business outcome in the same specific terms, the customer is named by role and context (not by org chart), and both parties agree on at least one measurable success criterion.

**What false alignment looks like:** the meeting ends with everyone feeling satisfied, but the PM's notes contain phrases like "something around retention," "the usual metrics," or "they mentioned a few things."

##### Step 4: Document the Outcomes

After the conversation, the PM shares their notes and the agent helps structure the summary.

The summary has five sections matching the five discussion areas:

- **Business Outcome:** one clear sentence naming a measurable change
- **Why It Matters Now:** one to two sentences on rationale and urgency
- **Customer:** who the product serves - a job title and context, not a persona name at this stage
- **Success Criteria:** a table with the criteria, the metric or signal, and the target
- **Constraints:** a bullet list of fixed constraints and non-negotiables

In addition, document:

- **Open Questions and Gaps:** anything that was contested, unclear, or left unresolved during the conversation

Be specific about what was agreed and what was not. Papering over gaps at this stage means discovering them later when fixing them is harder.

##### Step 5: Make the KDP Call

After the summary is complete, the PM makes an explicit Key Decision Point decision:

- **Go:** alignment is clear across all five areas. The PM proceeds to discovery.
- **Partial:** most areas are clear, but one or two need follow-up. Document which areas, what is unclear, and a target date for resolution. The PM should not begin full discovery until partial items are resolved.
- **No-go:** the business outcome is still contested, the customer is undefined, or success criteria are absent. The PM escalates the misalignment to the manager or reschedules before continuing.

The agent can help draft the KDP statement, but the call belongs to the PM.

### ps-outcome-strategy-discussion / Template

##### When to Use This

Use this template before discovery begins to document the alignment conversation between a PM and their manager or executive sponsor. The conversation must happen first. Fill in the outcome section after the discussion, not before.

Completing this template is the exit condition for this play. Do not begin discovery work until the Key Decision Point is marked.

---

##### Template

```markdown
# Outcome & Strategy: Guided Discussion

## Scope

- Discussion with: [name and role]
- Initiative or product: [name]
- Date: [date]
- Time horizon: [quarter / year / multi-year]

---

## Discussion Guide

Use these questions to facilitate the conversation. They are prompts, not a script. Follow the thread wherever it leads, and return to unanswered areas before the meeting ends.

### 1. Business Outcome

- What does the business need to achieve in the next [time horizon]?
- How does this connect to our broader strategy or annual goals?
- How will we know, in [X months], that we achieved it?

### 2. Why Now

- What changed that makes this the priority now?
- What happens if we do not address this this quarter or year?

### 3. Customer

- Who is the primary customer this outcome serves?
- Are there secondary customers or stakeholders whose needs we must also respect?

### 4. Success Criteria

- What would measurable success look like at [time horizon]?
- Are there existing metrics or targets we are accountable to?

### 5. Constraints and Non-Negotiables

- What is already decided - budget, timeline, technology choices?
- What is off-limits or outside scope?
- Are there dependencies we must work around?

---

## Outcome of the Discussion

Complete this section after the conversation.

### Business Outcome (one sentence)

[Write the agreed business outcome here. It must name a measurable change, not a project or a feature.]

### Why It Matters Now

[One to two sentences covering the rationale and urgency.]

### Customer

[Who the product serves - a job title and context, not a persona name at this stage. Example: mid-market shipper operations manager responsible for carrier selection and freight cost management.]

### Success Criteria

| Criteria | Metric or Signal | Target |
|---|---|---|
| | | |
| | | |
| | | |

### Constraints

- [Constraint or non-negotiable]
- [Constraint or non-negotiable]
- [Constraint or non-negotiable]

### Open Questions and Gaps

List anything that was contested, unclear, or left unresolved. Do not omit these to make the summary look complete.

- [Open question or gap]
- [Open question or gap]

---

## Key Decision Point

Mark one.

- [ ] Go: alignment is clear across all five areas. Proceed to discovery.
- [ ] Partial: [specify which areas need follow-up and by what date]
- [ ] No-go: [specify what needs escalation or re-discussion before continuing]

---

> **Quality checks**
> - Is the business outcome written as a measurable change, not a feature or project milestone?
> - Does the customer statement name a real role in a real context, not an org or a function?
> - Are the success criteria specific enough that a third party could assess them?
> - Are open questions documented rather than papered over with placeholder language?
> - Is the KDP explicitly marked?

> **Capacity note**
> The discussion summary should be readable in under five minutes. If it runs longer, consolidate. The purpose of this document is shared alignment, not comprehensive documentation.
```

### ps-outcome-strategy-discussion / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For shipper retention, align with the manager on the business result, customer, decision boundaries, and evidence needed before discovery.
- **Weak:** "Improve retention somehow" leaves the result and authority unclear.
- **Drift to avoid:** Outcome as project: "Launch a shipper portal" is an output. Establish the business change it is expected to produce.


#### Common Pitfalls

- **Treating the Discussion as a Requirements Intake:** Before the meeting, reframe the purpose: the PM is there to understand what the business needs to achieve, not what to build. If the manager jumps to solutions, the PM redirects: "That sounds like one approach - can we first align on what success looks like for the business overall?"

- **Accepting Vague Outcomes Without Pressing:** Press for specifics. "Improve customer satisfaction" needs a metric and a direction: "Increase NPS from 32 to 50 within 12 months." If the manager cannot provide a specific target, write "TBD" and flag it as a gap that must be resolved before discovery begins.

- **Skipping the KDP:** Treat the KDP as a required output, not an optional reflection. Before starting discovery, the PM should have a written KDP statement on file.

- **Letting the Manager Dictate the Solution:** Solutions that emerge during an outcomes conversation are hypotheses, not decisions. Record them in the open questions section and flag them for validation during discovery.

- **Documenting the Conversation Without Identifying the Gaps:** In the open questions section, be explicit about what was not resolved. A summary with two or three open questions documented is more useful than a summary with five areas filled in with uncertain answers.

- **Confusing Internal Stakeholders with the Customer:** The customer field in this play refers to who the product serves in the field - the person who uses or buys the thing the PM is building. If the product is built for external users, the customer is external. If the product is internal tooling, the customer is the internal user population (not the sponsoring executive).

- **AI Answers for the Manager:** Prepare questions, not answers. Fill the template only from notes of the real discussion, and mark anything still unconfirmed.

#### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-outcome-strategy-discussion) for supporting source material and expanded examples.

## ps-stakeholder-alignment | Stakeholder Alignment

Playbook number: 02. Phase: Context.

### ps-stakeholder-alignment / Instructions

#### Purpose

Build a **complete stakeholder map** before discovery begins.

This skill is for the **Context** phase, the second play in the Productside Playbook. It helps a Product Manager identify every person who affects or is affected by their initiative, rate each one by interest and influence, and assign engagement strategies that are specific enough to act on.

A stakeholder map is not a one-time artifact. It is a working tool that should be updated as relationships shift, as skeptics become allies, and as new influencers surface during discovery and delivery.

Use this skill when you need to:

- understand who has power over your initiative before you start
- identify skeptics and blockers before they become problems
- assign engagement strategies that match the actual relationship, not a generic default
- give the team a shared picture of the political landscape

This play comes before empathy interviews and discovery work. The map guides who to recruit, who to brief, and who to watch.

This is not a communications plan, a RACI chart, or a customer list. A communications plan describes when and how to send updates. A RACI describes task ownership. A customer list belongs in the persona play. The stakeholder map does something different: it determines who has input into which decisions and at what depth, before discovery shapes those decisions.

#### Key Concepts

##### Stakeholder vs. Customer

These are distinct categories and must not be conflated.

**Stakeholders** are internal or partner-side people who affect or are affected by the PM's work. They live inside the organization or at the boundary (executives, legal, finance, engineering leads, partner teams). They need to be managed, informed, or satisfied.

**Customers** are the people the product serves in the field. They experience the problem the product is solving. They belong in the persona play (ps-proto-persona), not in the stakeholder map.

Mixing customers into the stakeholder table creates confusion about who needs organizational engagement vs. who needs product discovery. The two groups need fundamentally different treatment.

##### Interest vs. Influence

These two dimensions are independent. Either can be high or low regardless of the other.

**Interest** is how much a stakeholder cares about this specific initiative. A legal counsel may not care about most product initiatives but may be intensely interested in one that touches data privacy.

**Influence** is how much power a stakeholder has over the initiative. Influence is not the same as seniority. A junior engineer who controls the deployment pipeline has high influence. A VP who has no say in technical decisions may have lower influence than their title suggests.

Rating both dimensions separately, and honestly, is the whole point of the matrix.

##### The Four Engagement Modes

The Interest/Influence matrix places stakeholders in one of four quadrants, each with a different engagement strategy:

**Manage closely (High Influence, High Interest):** These are your key partners. They care, and they have power. Involve them early, keep them informed in detail, and make them feel like co-owners where possible. Weekly touchpoints or embedded collaboration. Surprises here are costly.

**Keep satisfied (High Influence, Low Interest):** These are often executive sponsors who are not day-to-day participants. They have the power to greenlight or block, but they do not want to be in every meeting. Keep them briefed at the right altitude - progress, risks, key decisions - without pulling them into operational detail.

**Keep informed (Low Influence, High Interest):** These stakeholders care deeply but cannot directly affect the outcome. They may be strong advocates or enthusiastic users of adjacent systems. Keep them updated through regular communications; they are often your best ambassadors if things go well.

**Monitor (Low Influence, Low Interest):** Minimal engagement needed. Check in periodically so they are not blindsided by major changes, but do not over-invest attention here.

##### Engagement Modes Are About Decision Rights, Not Just Communication

This is the distinction that matters most. Engagement modes are not a comms schedule  -  they determine who has input on which decisions and at what depth.

- **Manage Closely** stakeholders are in the room for trade-off discussions. They have a voice in decisions, not just updates.
- **Keep Satisfied** stakeholders are briefed on outcomes and key decisions, but they are not consulted in the decision process itself. They need altitude-appropriate information, not operational depth.
- **Keep Informed** stakeholders receive regular updates but do not affect decisions. Their value is advocacy and downstream adoption, not direction-setting.
- **Monitor** stakeholders are not in the decision loop at all. Periodic check-ins prevent surprises, but they do not shape the work.

Treating all engagement as a communication cadence question misses this. A PM who sends weekly updates to all stakeholders has not done stakeholder management  -  they have sent emails. The quadrant assignment determines who the PM brings into decisions, not just who receives communications.

##### The Map is a Working Tool

Relationships shift. A skeptic becomes an ally after a successful pilot. An executive who was "keep satisfied" suddenly becomes deeply involved after a business unit change. A new hire in legal introduces a regulatory concern no one anticipated.

Revisit the map at the start of each major phase: after framing, after discovery, before launch. The version you build before discovery is a starting hypothesis, not a final assessment.

##### Completeness Check

The most common failure mode is listing only supporters. A map full of advocates looks optimistic but is nearly useless when a skeptic surfaces during a key decision.

A good stakeholder map includes:

- supporters and champions
- skeptics and cautious observers
- potential blockers
- people who were not consulted on similar initiatives in the past and caused friction as a result

If the map skews entirely positive, something is missing.

##### Stakeholders Are Teammates, Not Opponents

Different functions bring different priorities: legal thinks about risk, finance thinks about returns, engineering thinks about technical feasibility. Those differences create friction  -  but they do not make stakeholders adversaries.

The playbook is explicit: you may have different roles, but you are all working on the same team. A skeptical legal counsel who raises a compliance concern in week two is not an obstacle  -  they are a teammate whose input prevented a problem at launch. A finance stakeholder who pushes back on scope is not blocking the product  -  they are enforcing a constraint that is real for the business.

Approach every stakeholder as someone who shares the organization's goals, even if they express those goals differently than you do. The map is a tool for building a communication strategy across that diversity, not a list of people to manage around.

##### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **critic of the stakeholder map the PM drafted**. It looks for stakeholders the PM missed, asks for the evidence behind each power and interest placement, and checks that each engagement strategy fits the quadrant. The placements and strategies stay the PM's, because only the PM knows these people.

- **Use it when:** the PM has listed stakeholders and wants the map pressure-tested for gaps and placement.
- **Avoid it when:** the request is to characterize real colleagues' motives or influence from a name and a title. The model doesn't know them. When given names and titles, first ask what the PM has observed about each person's decisions and influence, and name any roles that may be missing. Offer placements, each tagged `[AI-SUGGESTED, VALIDATE THIS]`, only if the PM then asks for a best guess.
- **Return:** missing stakeholder roles named for the PM to consider, each placement questioned against what the PM has observed, and engagement strategies checked against decision rights.

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

Use Template (uploaded reference: `02-context.md`, section `ps-stakeholder-alignment / Template`) for the full scaffold.


##### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

##### Step 1: Tech-Role Bias Guard

Before drafting, pause and check who is missing.

In product work, the most visible stakeholders are often engineers, architects, or technical leads - the people the PM works with directly every day. They matter, but they are rarely the only stakeholders and often not the most influential ones.

Before drafting the table, explicitly ask: who else has interest or influence?

Check across these functions:

- Legal and compliance (especially if the initiative touches data, privacy, regulation, or contracts)
- Finance (if the initiative requires budget, headcount, or affects reported metrics)
- Sales and marketing (if the initiative changes the product the sales team sells or the story marketing tells)
- Customer success (if the initiative affects customer onboarding, support, or renewal)
- Operations (if the initiative changes workflows or operational capacity)
- Executive sponsors (who need to greenlight or protect the initiative at senior levels)

Technical roles may still make the list - but they should not be the only roles on it.

##### Step 2: Gather Internal Artifacts

Look at what already exists before writing anything new:

- Org charts or team rosters that show reporting lines and team boundaries
- Prior project retrospectives or postmortems that name who caused friction or was left out
- Prior communications or briefing documents that show who was engaged on similar initiatives
- Existing knowledge about who is skeptical, who is a champion, and who was burned by a previous failure

Ask: who was involved in similar initiatives before? Who was left out and caused problems later?

This is internal artifact work. No web research needed. The evidence lives in documents, relationships, and organizational memory.

##### Step 3: Build the Stakeholder Table

For each stakeholder, capture:

- **Name** - the person's actual name (4 words maximum)
- **Role / Team** - their title and team (6 words maximum)
- **Interest in This Initiative** - one clear sentence describing why they care (12 words maximum)
- **Influence** - High, Medium, or Low
- **Sentiment** - Supportive, Neutral, Skeptical, or Unknown

Aim for 6 to 10 stakeholders. Fewer than six usually means someone important has been missed. More than fifteen usually means the ratings are inflated or the scope of "stakeholder" has been defined too broadly.

Better to include someone and de-prioritize them in the matrix than to miss them entirely.

##### Step 4: Place Stakeholders on the Interest/Influence Matrix

Assign each stakeholder to one of the four quadrants based on their interest and influence ratings.

After placing everyone, check for balance. A map where every stakeholder lands in "manage closely" is a signal that ratings have been inflated. Not every stakeholder is a high-priority engagement. If the ratings feel off, recalibrate.

##### Step 5: Assign Engagement Strategies

For each quadrant, write a brief, specific engagement strategy.

Specific is better than generic:

- "Weekly async update via Slack with decision log" is actionable.
- "Keep informed" is not.

Each strategy should answer: how often, what to share, and what to ask for.

##### Step 6: Identify Risks and Gaps

Three things to capture before closing the map:

**Missing stakeholders:** Anyone who should be here but is not yet identified. A good check is asking: who has blocked similar work in the past? Who has authority that has not been mentioned yet?

**Potential blockers:** Stakeholders who could slow or stop progress if not engaged early. These may not be formal opponents - they may simply be people who will raise concerns at a late stage if they feel uninvolved.

**Political dynamics:** Relationships between stakeholders that create complexity. For example: two stakeholders who have a history of conflict, or a senior stakeholder whose opinion a key influencer defers to entirely.

### ps-stakeholder-alignment / Template

Use this template to build a **Productside-style stakeholder map** before discovery begins.

If some stakeholders are not yet identified, note that in the Risks and Gaps section rather than leaving the table sparse. A complete map with unknowns flagged is more useful than a partial map that looks tidy.

##### When to Use This

Use this during the Context phase, before empathy interviews or discovery work begins. The stakeholder map tells you who to involve, who to brief, and who to watch.

##### Template

```markdown
# Stakeholder Alignment

## Context

- Initiative / product: [name]
- PM: [name]
- Date: [date]

---

## Stakeholder Table

| Name | Role / Team | Interest in This Initiative | Influence | Sentiment |
|---|---|---|---|---|
| | | | High / Medium / Low | Supportive / Neutral / Skeptical / Unknown |
| | | | High / Medium / Low | Supportive / Neutral / Skeptical / Unknown |
| | | | High / Medium / Low | Supportive / Neutral / Skeptical / Unknown |
| | | | High / Medium / Low | Supportive / Neutral / Skeptical / Unknown |
| | | | High / Medium / Low | Supportive / Neutral / Skeptical / Unknown |
| | | | High / Medium / Low | Supportive / Neutral / Skeptical / Unknown |
| | | | High / Medium / Low | Supportive / Neutral / Skeptical / Unknown |
| | | | High / Medium / Low | Supportive / Neutral / Skeptical / Unknown |

> Aim for at least 6-10 stakeholders. Include skeptics and potential blockers, not just supporters.

---

## Interest / Influence Matrix

### Manage Closely (High Influence, High Interest)
[List names]
- Engagement: [frequency and format - e.g., "weekly 1:1, shared decision log, involved in key trade-off discussions"]

### Keep Satisfied (High Influence, Low Interest)
[List names]
- Engagement: [frequency and format - e.g., "monthly executive brief, flagged when decisions affect scope or budget"]

### Keep Informed (Low Influence, High Interest)
[List names]
- Engagement: [frequency and format - e.g., "biweekly async update via shared doc or Slack, invited to demos"]

### Monitor (Low Influence, Low Interest)
[List names]
- Engagement: [frequency and format - e.g., "quarterly check-in, notified of major milestones only"]

---

## Risks and Gaps

### Missing stakeholders
[Anyone who should be here but is not yet identified]

### Potential blockers
[Stakeholders who could slow or stop progress if not engaged early]

### Political dynamics
[Relationships between stakeholders that could affect how you engage them]

---

> **Quality checks**
> - Does the stakeholder table include skeptics and blockers, not just supporters?
> - Is "influence" based on actual power over this initiative, not just seniority?
> - Are engagement strategies specific enough to act on (cadence, format, content)?
> - Is the map distinguishing stakeholders from customers? Customers belong in the persona play, not here.
> - Have you checked across legal, finance, sales, marketing, operations, and executive functions - not just engineering?

> **Capacity notes**
> - Interest description: aim for one clear sentence per stakeholder (10-15 words)
> - Engagement strategy: one to two sentences per quadrant
> - Name field: 4 words maximum
> - Role / Team field: 6 words maximum
```

##### Usage Guidance

- Build this map before empathy interviews begin.
- Rate influence based on actual power over this initiative, not title alone.
- Keep stakeholders and customers separate. Customers who use the product belong in ps-proto-persona.
- Revisit this map at each major phase boundary (after framing, after discovery, before launch).
- A map with no skeptics or blockers should be treated as incomplete, not as good news.

### ps-stakeholder-alignment / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For a route-optimization initiative, assess internal stakeholders' interest and influence and choose Manage Closely, Keep Satisfied, Keep Informed, or Monitor accordingly.
- **Weak:** Sending every stakeholder the same weekly update ignores differences in decision involvement.
- **Drift to avoid:** Customers as internal stakeholders: keep discovery subjects distinct from the organizational stakeholder map.


#### Common Pitfalls

- **Listing Only Supporters:** Before closing the map, ask explicitly: who might push back? Who was not consulted on similar initiatives? Add them.

- **Confusing Stakeholders with Customers:** Customers who use the product in the field belong in the persona play (ps-proto-persona), not here. The stakeholder map covers people who affect the initiative organizationally. Keep these lists separate.

- **Equating Influence with Seniority:** Rate influence based on actual power over this specific initiative. Ask: can this person approve, block, accelerate, or veto the work? That is influence. Title alone is not.

- **Treating Interest and Influence as Binary:** Use Medium deliberately. Reserve High for stakeholders with genuine power or deep engagement with this initiative specifically.

- **Building the Map Once and Never Revisiting:** Revisit the map at each major phase boundary. Note what changed and why.

- **Assigning Everyone to "Manage Closely":** Force distribution. Reserve "manage closely" for the two to four stakeholders who genuinely require it. Everyone else gets a lighter strategy.

- **Writing Engagement Strategies as Communication Schedules:** For every "manage closely" and "keep satisfied" stakeholder, specify at least one type of decision they will be consulted on - not just a communication format. Example: "Involve in go/no-go discussion before framing is complete" is an engagement strategy. "Weekly update email" is not.

- **AI Places Stakeholders It Has Never Met:** The PM places each stakeholder from what they have observed. The skill asks for the evidence behind each placement and names roles the PM may have missed.

#### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-stakeholder-alignment) for supporting source material and expanded examples.

## ps-outcome-tree | Outcome Tree (Sections One and Two)

Playbook number: 03 + 23. Phase: Context.

### ps-outcome-tree / Instructions

#### Purpose

Create and maintain a **Productside-style Outcome Tree artifact** for your product.

This skill has **two modalities** that correspond to two moments in the playbook lifecycle:

**Section One (Modality 1 - Context phase, pre-discovery):** Establish the strategic context. Define the business outcome, business success metrics, 2-5 product outcomes, product success metrics, and product health metrics. This is the foundational frame that connects product work to business goals.

**Section Two (Modality 2 - Define/Deliver phase, post-discovery):** Update the tree with what you have learned. After discovery work (interviews, experiments, validation), revisit the tree to revise product outcomes based on evidence, update metrics with baselines and targets, record actual results against planned targets, and retire or replace outcomes that discovery invalidated.

The two modalities share the same artifact structure. Section Two is not a separate document. It is an update pass on the Section One artifact, informed by what the PM learned during discovery and define work.

Use this skill when you need to:

- connect product work to a measurable business goal (Section One)
- define 2-5 product outcomes that support a specific business outcome (Section One)
- distinguish business-level metrics from product-level metrics (Section One)
- create a shared artifact the team can revisit in planning and review meetings (Section One)
- build the foundation for prioritization and roadmap decisions (Section One)
- update outcomes and metrics after discovery validates or invalidates assumptions (Section Two)
- record actual results against the targets set in Section One (Section Two)
- retire product outcomes that no longer hold after customer research (Section Two)

This is not a one-time exercise. The playbook says to revisit regularly, bring it to team meetings, and use it to check assumptions with the team.

##### Usage Notes

- **Two modalities:** Section One (Template 03, Context phase) establishes the strategic context before discovery. Section Two (Template 23, Define/Deliver phase) updates the tree after discovery with validated outcomes, revised metrics, and actuals vs. planned.
- The template produces a structured artifact with five sections: Business Outcome, Business Success Metrics, Product Outcomes (2-5), Product Success Metrics, and Product Health Metrics.
- Product outcomes use role names, not persona names.
- The play cross-references two other plays: Framing the Problem (Problem Statement box) and Solution Hypothesis Statement (Solution Summary box). Neither is a blocking dependency.
- Upstream: ps-jobs-to-be-done product outcomes feed into this tree. Section Two updates the tree after discovery work.

#### Key Concepts

##### Business Outcomes vs. Product Outcomes

These are two distinct levels. Confusing them is the most common mistake in this play.

**Business Outcome:** What the organization is trying to achieve at a strategic or operational level. It is owned by the business, not by the product team alone.

Example: "Improve new employee onboarding time by 30%"

**Product Outcome:** What the customer or user achieves when the product works well. Product outcomes support the business outcome, but they describe value from the customer's perspective.

Example: "Internal HR managers are focused on strategic initiatives and spend less time doing day-to-day tactical tasks"

The relationship is causal: if the product outcomes are achieved, the business outcome should follow. If that causal link is weak, the tree needs rework.

##### Business Success Metrics

Business success metrics measure progress toward the business outcome. They are often lagging indicators owned by leadership or finance.

These may be defined or TBD at the time of building the tree. It is acceptable to leave them as "TBD" initially, but they should not remain blank permanently.

Examples:
- Time-to-productivity for new hires (days)
- Employee satisfaction score during first 90 days
- HR cost per onboarding cycle

##### Product Success Metrics

Product success metrics measure whether each product outcome is being achieved. They are leading indicators owned by the product team.

Examples:
- Percentage of onboarding tasks completed without HR intervention
- Average HR manager time spent on tactical onboarding tasks per week
- Number of onboarding-related support tickets per month

##### Product Health Metrics

Product health metrics measure the operational health of the product itself, separate from whether it is achieving outcomes.

Examples:
- System uptime percentage
- Average page load time
- Error rate for key workflows
- User adoption rate (active users / total licensed users)

Product health metrics are necessary but not sufficient. A product can be healthy (fast, reliable, available) and still fail to deliver outcomes.

##### The 2-5 Product Outcome Limit

The playbook sets a hard limit: no more than 2-5 product objectives. This is not a suggestion. If you have more than 5, you are either splitting too finely or trying to serve too many business outcomes in one tree.

##### Cross-References to Other Plays

The Outcome Tree references two other playbook artifacts:

- **Problem Statement** (from the Framing the Problem play): feeds into the tree as context for why the business outcome matters
- **Solution Summary** (from the Solution Hypothesis Statement play): feeds into the tree as a summary of the proposed approach

These are cross-references, not blocking dependencies. You can build the Outcome Tree without having completed those plays, but the tree is stronger when they exist.

##### Section One vs. Section Two (Two Modalities, One Skill)

This skill covers both sections of the Outcome Tree as two modalities:

**Section One (Template 03, Context phase):** Build the tree before discovery. Define the business outcome, product outcomes, and metrics framework based on the PM's current understanding of strategy and customer needs.

**Section Two (Deliver phase  -  reuses the Outcome Tree design; the baseline deck labels this occurrence "Template 3 of 24"; the B2B work-in-progress deck numbers it Template 23):** Update the tree after discovery. Revise product outcomes that discovery validated or invalidated. Fill in metrics that were TBD. Add baselines and targets now that real data exists. Record actuals against planned targets. Retire outcomes that turned out to be wrong.

The trigger for Section Two is evidence: completed empathy interviews, validated hypotheses, experiment results, or post-launch measurement data. If the PM has not done discovery work since building Section One, Section Two will just reproduce the same guesses with more confidence. That is not useful.

##### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **critic of the outcome tree the PM drafted**, in both sections. In Section One it checks that the business outcome is measurable, that product outcomes describe what customers achieve, and that metrics are in the right place. In Section Two it asks what discovery evidence supports or contradicts each product outcome. The outcomes, targets, and the verdict on each stay the PM's.

- **Use it when:** the PM has drafted Section One, or has discovery evidence to review in Section Two.
- **Avoid it when:** the request is to invent the business outcome, or to fill in baselines, targets, or actuals without data.
- **Return:** each outcome and metric checked for format and placement, the causal chain from product outcomes to business outcome tested, and in Section Two, each product outcome matched to evidence for the PM to keep, revise, or retire.

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

Use Template (uploaded reference: `02-context.md`, section `ps-outcome-tree / Template`) for the full scaffold.


##### Required Output Convention

Default to a **clean, paste-ready structured artifact** with clearly labeled sections.

That means:

- fill all sections (Business Outcome, Business Success Metrics, Product Outcomes, Product Success Metrics, Product Health Metrics)
- produce 2-5 product outcomes that clearly support the business outcome
- keep product outcome statements concise enough for template cells (~15-20 words)
- keep metrics specific and measurable
- explanation belongs below the artifact, not inside the template cells

The artifact comes first. Commentary is secondary.

##### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

##### Step 1: Confirm the Product and Business Context

Before writing anything, answer:

- what product or service are we talking about?
- what business or organization does this product serve?
- who are the customers/users of this product?

**Guard against tech-role bias.** The product outcomes belong to the customer, the person who uses or buys the product in the field. A clinical data platform's product outcomes belong to clinical operations leads and research scientists, not to data engineers or platform architects. Before writing product outcomes, confirm: does this person write code, design systems, or architect solutions as their primary job? If no, the outcomes should not read like a technologist's goals.

##### Step 2: Gather Evidence Before Writing

Once you know the product and business context, ask the user for relevant materials before drafting:

- **Strategy documents** such as business plans, annual goals, OKR frameworks, or strategic planning decks
- **Existing metrics** such as current KPIs, dashboards, or performance reports
- **Prior discovery work** such as problem statements, persona artifacts, or JTBD artifacts from other skills

This skill uses **artifacts-only** evidence gathering. The business outcomes and product outcomes should come from the PM's own strategic context, not from web research. Do not offer to run web searches for this skill.

##### Step 3: Define the Business Outcome

Write a clear, specific business outcome statement. This is what the organization is trying to achieve.

A strong business outcome:

- names a measurable change (improve, reduce, increase, eliminate)
- includes a target or direction, even if approximate
- is owned by the business, not just the product team
- is specific enough that you could tell if it happened

Weak: "Grow the business"
Stronger: "Improve new employee onboarding time by 30%"

Weak: "Increase efficiency"
Stronger: "Reduce average claim processing time from 14 days to 5 days"

If the user cannot articulate a business outcome, that is a signal that the strategic context is unclear. Help them work through it, but do not invent one.

##### Step 4: Define Business Success Metrics

For the business outcome, identify 1-3 metrics that the business would use to measure progress.

These metrics should be:

- measurable (a number, percentage, or rate)
- owned by or visible to business leadership
- connected to the business outcome statement

It is acceptable for these to be "TBD" if the user does not have them yet. Note this in the artifact and flag it as a gap to resolve.

##### Step 5: Define Product Outcomes (2-5)

For each product outcome, describe what the customer or user achieves when the product works well.

Product outcomes:

- describe value from the customer's perspective
- use role names, not persona names (e.g., "HR managers" not "Maya")
- support the business outcome through a causal link
- are limited to 2-5 per tree

Format guidance: write each product outcome as a statement about the customer's improved state. Focus on what changes for them, not what the product does.

Weak: "The product has a self-service onboarding module"
Stronger: "Internal HR managers are focused on strategic initiatives and spend less time doing day-to-day tactical tasks"

Weak: "Automated workflow engine"
Stronger: "New employees complete required onboarding steps without waiting for HR availability"

##### Step 6: Define Product Success Metrics

For each product outcome, identify 1-2 metrics that would indicate the outcome is being achieved.

Product success metrics should be:

- leading indicators (they move before the business outcome moves)
- measurable by the product team
- tied to a specific product outcome

If metrics are not yet defined, mark them as "TBD" and note the gap.

##### Step 7: Define Product Health Metrics

Identify 2-4 metrics that measure the operational health of the product itself.

Product health metrics are about the product working correctly, not about outcomes being achieved. They include things like:

- uptime and availability
- performance (load times, response times)
- error rates
- adoption and engagement rates

##### Step 8: Cross-Reference Problem Statement and Solution Summary

If the user has completed the Framing the Problem play (ps-framing-the-problem), pull in the problem statement as context.

If the user has completed the Solution Hypothesis Statement play (ps-solution-hypothesis), pull in the solution summary.

If neither exists yet, note these as optional inputs that strengthen the tree when available.

##### Step 9: Review the Causal Chain

Before finalizing, walk through the logic:

- If Product Outcome 1 is achieved, does it plausibly contribute to the Business Outcome?
- If Product Outcome 2 is achieved, does it plausibly contribute to the Business Outcome?
- Are the product outcomes collectively sufficient to move the business outcome, or are there gaps?
- Are any product outcomes actually business outcomes in disguise?
- Are any product outcomes actually features or solutions?

Flag any weak links for the user to consider.

##### Step 10: Offer Next Steps (Section One)

After the Section One artifact is complete, offer the user up to three next-step options:

1. **Build or refine a problem statement** using ps-framing-the-problem, if no problem statement exists yet
2. **Define a solution hypothesis** using ps-solution-hypothesis, to fill in the Solution Summary box
3. **Run Section Two** of this skill after discovery work to update the tree with evidence

Present these as options, not as mandatory steps. The user decides what comes next.

---

##### Section Two: Updating the Outcome Tree After Discovery

The following steps apply when the PM returns to the Outcome Tree after completing discovery and define work. Section Two is not a new artifact. It is an update pass on the existing Section One artifact.

##### Step 11: Confirm Discovery Evidence Exists

Before running Section Two, verify the PM has new information to work with. Ask:

- What discovery activities have been completed since the tree was built? (empathy interviews, experiments, validation sessions, market research)
- What did discovery reveal that surprised you or contradicted your assumptions?
- Have any product outcomes been validated, invalidated, or changed in priority?

If the PM has no new evidence, Section Two will not add value. Recommend completing discovery work first.

##### Step 12: Review Each Product Outcome Against Evidence

Walk through each product outcome from Section One and ask:

- **Validated:** Did discovery confirm this outcome matters to customers? Keep it, sharpen the language if needed.
- **Invalidated:** Did discovery reveal this outcome is not important to customers, or that the causal link to the business outcome is weaker than assumed? Mark it for retirement or revision.
- **New:** Did discovery reveal a product outcome that was missing from Section One? Add it (staying within the 2-5 limit).
- **Revised:** Does the outcome need reframing based on what customers actually said or did?

Update the Product Outcomes table accordingly. Note what changed and why in the Notes section.

##### Step 13: Update Metrics with Baselines, Targets, and Actuals

For each metric section (business success, product success, product health):

- Replace "TBD" entries with defined metrics where evidence now exists
- Add **baseline** values (what is the current state before the product intervention?)
- Add or refine **target** values (what does success look like, now that you know more?)
- If post-launch: record **actual** values and note variance from target

Use a consistent format: "Metric Name: baseline X, target Y, actual Z (if available)."

##### Step 14: Reassess the Causal Chain

Re-run the causal chain review from Step 9, but with the updated outcomes:

- Do the revised product outcomes still collectively support the business outcome?
- Did discovery reveal gaps in the chain that Section One missed?
- Are the business success metrics still the right ones, or has the business context shifted?

Flag any breaks in the chain for the PM to resolve.

##### Step 15: Offer Next Steps (Section Two)

After the Section Two update is complete, offer the user:

1. **Share the updated tree with stakeholders** to align on revised priorities
2. **Update the roadmap** using ps-outcome-roadmap (if available) to reflect revised outcomes
3. **Schedule the next review cycle** to keep the tree current as the product evolves

### ps-outcome-tree / Template

##### When to Use This

Use this template during the **Context** phase to connect your product work to a measurable business goal. This is foundational: until you can articulate what the business is trying to achieve and how the product supports that, prioritization and roadmap decisions lack an anchor.

Revisit this artifact regularly. Bring it to team meetings. Use it to share success metrics and check assumptions with the team.

##### Template

```markdown
# Outcome Tree - Section One

## Product Context

- Product or service:
- Business or organization:
- Primary customer/user role:
- Buyer (if different):

## Problem Statement (from Framing the Problem play, if available)

> [Paste or summarize the problem statement here, or note "Not yet defined"]

## 1. Business Outcome

What is the business trying to achieve? Write a specific, measurable business outcome.

| Business Outcome |
|------------------|
| |

> Quality check: Is this a business-level goal, not a product feature?
> Quality check: Does it include a direction and a metric (even if approximate)?
> Quality check: Could you tell if it happened?

## 2. Business Success Metrics

How does the business measure progress toward the business outcome?

| # | Business Success Metric | Status |
|---|------------------------|--------|
| 1 | | Defined / TBD |
| 2 | | Defined / TBD |
| 3 | | Defined / TBD |

> Quality check: Are these metrics owned by or visible to business leadership?
> Quality check: Are they measurable (a number, percentage, or rate)?

## 3. Product Outcomes (2-5)

What must the customer/user achieve for the business outcome to follow? Use role names, not persona names.

| # | Product Outcome |
|---|----------------|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |

> Quality check: Does each outcome describe value from the customer's perspective?
> Quality check: Is each outcome distinct from the business outcome? (Product outcomes are customer-level, not business-level.)
> Quality check: Have you avoided feature descriptions? ("Self-service portal" is a feature, not an outcome.)
> Quality check: Do you have between 2 and 5 product outcomes? No more than 5.
> Quality check: Do the product outcomes use role names (e.g., "HR managers"), not individual persona names (e.g., "Maya")?
> Capacity check: Product outcome statements should be ~15-20 words.

## 4. Product Success Metrics

How do you measure whether each product outcome is being achieved?

| # | Product Success Metric | Related Outcome | Status |
|---|----------------------|-----------------|--------|
| 1 | | | Defined / TBD |
| 2 | | | Defined / TBD |
| 3 | | | Defined / TBD |
| 4 | | | Defined / TBD |
| 5 | | | Defined / TBD |

> Quality check: Are these leading indicators that the product team can measure?
> Quality check: Is each metric tied to a specific product outcome?
> Quality check: Are these about outcome achievement, not product health? (Uptime is health, not success.)

## 5. Product Health Metrics

How do you measure whether the product itself is working correctly?

| # | Product Health Metric | Target |
|---|---------------------|--------|
| 1 | | |
| 2 | | |
| 3 | | |

> Quality check: Are these operational metrics (uptime, performance, error rates, adoption)?
> Quality check: Are they separate from product success metrics?

## Solution Summary (from Solution Hypothesis Statement play, if available)

> [Paste or summarize the solution hypothesis here, or note "Not yet defined"]

## Causal Chain Review

- Do the product outcomes collectively support the business outcome?
- Are there gaps in the chain?
- Are any product outcomes actually business outcomes in disguise?
- Are any product outcomes actually features?

## Notes (optional)

- Metrics that need further definition:
- Assumptions to validate:
- Cross-references to resolve:
```

##### Usage Guidance

###### Filling the Template

1. Start with **Product Context** to anchor who this is for.
2. Add the **Problem Statement** if one exists from previous work.
3. Define the **Business Outcome** first. Everything else flows from it.
4. Add **Business Success Metrics** (even if some are TBD).
5. Define **Product Outcomes** (2-5). These describe what the customer achieves.
6. Add **Product Success Metrics** for each product outcome.
7. Add **Product Health Metrics** for the product itself.
8. Add the **Solution Summary** if one exists.
9. Walk through the **Causal Chain Review** to verify connections.

###### How Many Product Outcomes

The playbook sets a hard limit of 2-5. Default to 2-3 for a focused product. Use 4-5 only when the product serves multiple distinct user roles or the business outcome is broad enough to require multiple paths.

If you find yourself writing more than 5, either:

- consolidate related outcomes into a single, broader outcome
- split into multiple trees, each with a different business outcome

###### What Goes in the Product Outcome Statements

Write each product outcome as a statement about the customer's improved state. Use role names (e.g., "HR managers," "field technicians," "compliance officers"), not individual persona names (e.g., "Maya," "Carlos").

Do not use:

- feature descriptions ("The product provides...")
- implementation details ("Automated workflow for...")
- business metrics ("Revenue increases by...")
- internal team goals ("The engineering team ships...")

###### Connecting to Other Skills

- **Upstream:** ps-framing-the-problem provides the Problem Statement; ps-solution-hypothesis provides the Solution Summary
- **Parallel:** ps-jobs-to-be-done produces product outcomes that may feed into this tree
- **Downstream:** Section Two (this skill, Modality 2) updates the tree after discovery and define work

---

##### Section Two: Updating the Outcome Tree After Discovery

Use this scaffold when returning to the Outcome Tree after completing discovery work. This is not a new artifact. It is an update pass on the Section One artifact above.

###### Prerequisites

Before running Section Two, the PM should have completed at least one of:

- empathy interviews (ps-empathy-interviews)
- solution hypothesis validation (ps-solution-hypothesis)
- lo-fi experimentation (ps-lofi-experimentation)
- market or customer research
- post-launch measurement data

###### Update Scaffold

For each section of the Section One artifact, walk through:

```markdown
## Section Two: Outcome Tree Update

Date of update:
Discovery activities completed since Section One:

### Product Outcome Review

| # | Original Product Outcome | Status | Revised Product Outcome (if changed) | Evidence |
|---|-------------------------|--------|--------------------------------------|----------|
| 1 | [from Section One] | Validated / Invalidated / Revised / New | [updated text or "unchanged"] | [what discovery revealed] |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

> Quality check: Is each status decision backed by specific evidence, not intuition?
> Quality check: Are you still within 2-5 product outcomes after revisions?
> Quality check: Did you retire outcomes that discovery invalidated rather than keeping them "just in case"?

### Metrics Update

| Metric Type | Metric | Baseline | Target | Actual (if post-launch) | Status Change |
|-------------|--------|----------|--------|------------------------|---------------|
| Business Success | | | | | Was TBD, now Defined / Unchanged / Revised |
| Product Success | | | | | |
| Product Health | | | | | |

> Quality check: Have all TBD metrics from Section One been resolved or explicitly deferred with a reason?
> Quality check: Are baselines grounded in real data, not estimates?

### Causal Chain Reassessment

- Which links in the chain did discovery strengthen?
- Which links did discovery weaken or break?
- Are there new gaps that Section One missed?

### Changes Summary

- Product outcomes added:
- Product outcomes retired:
- Product outcomes revised:
- Metrics defined (were TBD):
- Metrics revised:
```

###### When to Run Section Two

Section Two adds value when the PM has new evidence that changes the tree. Common triggers:

- Completed empathy interviews revealed different customer priorities than assumed
- Solution hypothesis testing invalidated an assumed product outcome
- Market research shifted the competitive context
- Post-launch data shows actual vs. planned variance
- Business strategy changed, altering the business outcome or its metrics

Section Two does not add value when:

- The PM has not done discovery work since Section One (the tree will not change)
- The only change is cosmetic rewording (edit the Section One artifact directly)

###### Capacity Reference

See Template and capacity guidance (uploaded reference: `02-context.md`, section `ps-outcome-tree / Template`) for the exact word and character budgets per field.

| Field | Word Budget | Guidance |
|-------|-------------|----------|
| Business Outcome | ~15-25 | Specific, measurable business goal |
| Business Success Metric | ~10-15 | Measurable indicator with units |
| Product Outcome | ~15-20 | Customer-centered value statement |
| Product Success Metric | ~10-15 | Leading indicator tied to an outcome |
| Product Health Metric | ~5-10 | Operational metric with target |

### ps-outcome-tree / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For irrigation management, connect business results to farm managers reducing avoidable water use, then define success and health measures. Revisit planned outcomes against actual evidence in Section Two.
- **Weak:** A tree with no customer outcomes jumps directly from financial targets to features.
- **Drift to avoid:** Layer confusion: "Ship sensors" is an output; "increase subscription revenue" is a business result. Neither substitutes for customer progress.


#### Common Pitfalls

- **Confusing Product Outcomes with Business Outcomes:** Ask: who experiences this outcome? If the answer is "the business" or "leadership," it is a business outcome. If the answer is "the customer using the product," it is a product outcome. Keep them in their respective boxes.

- **Writing Feature Descriptions as Product Outcomes:** Strip out the product. Ask: what is different for the customer when this feature works? "New employees complete required onboarding steps without waiting for HR availability" is a product outcome. "Self-service onboarding portal" is a feature.

- **Setting More Than 5 Product Objectives:** The playbook limit is 2-5 product outcomes per tree. If you have more, either consolidate related outcomes or split into multiple trees for different business outcomes.

- **Making Business Outcomes Too Vague:** Add a direction, a metric, and a target. "Improve customer satisfaction" becomes "Increase Net Promoter Score from 32 to 50 within 12 months." If the user cannot specify a target, at least specify a direction and a metric.

- **Defaulting to Tech-Role Language in Product Outcomes:** Before writing product outcomes, confirm who the product actually serves. Most products serve people whose primary job is not writing code. An HR platform serves HR managers and employees, not data engineers.

- **Treating This as a One-Time Exercise:** The playbook says to revisit regularly and bring it to team meetings. Schedule periodic reviews and update the tree as strategy evolves.

- **Skipping Product Success Metrics:** Even if exact metrics are not known yet, define the type of measurement. "TBD" is acceptable as a starting point, but flag it as a gap that must be resolved before the next planning cycle.

- **Confusing Product Health Metrics with Product Success Metrics:** Keep them in separate sections. Product health metrics (uptime, latency, error rates) go in the health section. Product success metrics (task completion rates, time savings, adoption of key workflows) go next to their respective outcomes.

- **AI Writes the Tree:** The PM drafts; the skill checks each outcome and metric. Targets and baselines come from the PM's data or are marked to be set.

#### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-outcome-tree) for supporting source material and expanded examples.

## ps-market-selection-sizing | Market Selection & Sizing

Playbook number: 04. Phase: Context.

### ps-market-selection-sizing / Instructions

#### Purpose

Create a **Productside-style Market Selection & Sizing artifact** for the market a product serves.

This skill is for the **Context** phase. Before diving into a product opportunity, either an iteration of an existing product or a new one, the team needs to understand what market the product serves, what is happening in that market, and whether it is an interesting one to pursue. The artifact has three parts:

1. **Market Selection** - name the market and run a PESTEL analysis of the forces acting on it
2. **Segment the Market** - cut it into at least two distinct segments, and name the users, buyers, and influencers in each
3. **Size the Market & Segments** - TAM for the market, SAM for each segment, and SOM in annual revenue when there is a product to price

Use this skill when you need to:

- name the market before writing jobs, personas, or problem statements for it
- move segmentation beyond simple industries or demographics
- decide which segments are worth exploring, with a first-pass size behind each
- give later plays (Jobs-to-Be-Done, Personas, Empathy Interviews, Positioning) a defined segment to work from

This is not a financial forecast or a business case. It is a first pass, fast and simple, that the team revisits as it learns more. And it is never a place for numbers without sources.

**Source status:** this Play exists only in the B2B work-in-progress deck (Template 04 of 24), which is not yet ratified. The baseline deck has no equivalent.

##### Usage Notes

- **Type:** component. **Phase:** Context. **Evidence:** web research + user artifacts.
- **Every number needs a source.** Sizing is written as formulas whose inputs carry source IDs or `[TO SOURCE]`, in one counting unit, as ranges, with SOM ≤ SAM ≤ TAM.
- **AI may propose, never invent.** Following the Playbook's own prompts, the skill proposes market definitions, PESTEL entries, and segments with its reasoning visible, and cites what it finds. It never fills a sizing blank with a plausible number.
- **SOM can wait:** it is estimated only when there is a product to price. Otherwise it is deferred until solutions are ideated.
- **Downstream:** ps-jobs-to-be-done, ps-proto-persona, ps-empathy-interviews, and ps-positioning-statement use the segments and the people named in them.
- The source deck is not yet ratified, and its pages are not objectified (no named shapes). The budget entry in `technical/data/canonical_template_budgets.yaml` has guidance only, no shape budgets.

#### Key Concepts

##### Name the Market at the Right Altitude

A market definition centers on **who the product is for and the benefit it provides them**. "Healthcare" is too broad to analyze. One customer's workflow is too narrow to size. Three questions, asked one at a time, get to the right altitude:

1. What problem are people trying to solve, or what are they trying to make better, in this space?
2. Who has this problem (businesses, consumers, channel partners), and when does it become important enough for them to look for help?
3. What do they do today to solve it, and what other options could they choose?

Propose a definition from the answers and have the PM confirm or iterate it. Lock it before running the PESTEL.

##### PESTEL: Evidence, Not a Full Grid

PESTEL names six forces acting on the market: **Political, Economic, Social, Technological, Environmental, Legal.** The goal is evidence, not a filled grid. Each force is committed either as **evidence with a source**, or as an **open question to research**. A PESTEL full of generic forces ("technology is changing fast," "regulation is increasing") fits every market and informs none.

Ask the PM first which forces they know should, or should not, be considered. They know things about this market that no search will find.

##### A Segment Is Defined by Shared Needs, Goals, and Behaviors

A segment is a potential group of customers that is **unique and identifiable through a set of shared traits, goals, preferences, and behaviors.** Industry and company size can bound a segment, but they rarely define one. Two hospitals of the same size can buy for completely different reasons.

Every segment needs:

- a **name** and a brief description of the traits, desires, and preferences that make it unique
- **explicit cut logic**: what makes it distinguishable from the other segments, stated so it can be tested
- the **people operating in it**: users, buyers, and influencers. A segment with no real buyer or user in it is a segment for show.

The template holds two segments, and the Play asks for at least two. A **high-potential segment** has strong underserved needs and problems worth solving to validate.

##### TAM, SAM, SOM: The Productside Way

- **TAM (Total Addressable Market):** think broadly. The whole market the product could serve.
- **SAM (Serviceable Addressable Market):** for **each segment**, the part of the TAM the product can actually serve.
- **SOM (Serviceable Obtainable Market):** for each segment, the share of the SAM the team can realistically win, in **annual revenue**. It must consider **competition**, plus pricing and company constraints.

Name the **counting unit** (sites, firms, accounts, people, checkpoints) and keep it consistent through TAM, SAM, and SOM. Check that SOM ≤ SAM ≤ TAM in the same unit. Revenue is units × an annual price per that same unit.

**SOM can wait.** If there is an existing product, estimate SOM. If not, skip it until solutions have been ideated, or show it as a conditional formula with the price marked as an assumption.

##### Every Number Is a Blank to Source

AI is fast at structure and dangerous at facts. Every figure about size, growth, or competitors that no one can trace to a source is a guess dressed as a finding. So:

- **Write sizing as formulas**, with every input labeled by its source (`[S1]`, `[S2]`) or marked `[TO SOURCE]`.
- **Triangulate.** Use three different approaches (top-down, bottom-up, analogous products, subject-matter experts). Don't rely on a single search or one source.
- **Use ranges.** Ranges reduce overconfidence and turn a debate about one number into a discussion of risk.
- **A market share needs a basis.** "5% in two years" is not a basis. Competitive position, reach, win rate, and capacity are.
- **Never cite competitor revenues** that no filing or report states.

##### "Is It Worth It?" Stays With the PM

The skill can recommend which segments look most promising and say why. The judgment that a market or segment is worth pursuing belongs to the PM and their team.

##### How AI Supports This Play

The Playbook calls AI **fast at structure and dangerous at facts**. It can lay out a PESTEL skeleton, suggest ways to segment a market, and frame a TAM/SAM/SOM calculation. What it cannot do is know the market. Use it to organize the sources the PM has and to expose the gaps still to fill. That turns scattered evidence into a shape the team can reason about.

In this Play, the Playbook's own prompts ask AI to research, propose segments, and recommend two. So this skill does propose, with its reasoning visible and every claim cited. It never supplies a number without a source the PM can check.

- **Use it when:** the market is named (or nearly) and there are real sources, or web research is available, and the PM needs help structuring or sharpening the analysis.
- **Avoid it when:** there are no sources and no way to research, or the request is simply "what's the market size?" Build the structure and mark the numbers `[TO SOURCE]` instead.
- **Return:** a PESTEL with the evidence organized and gaps flagged as questions, segments with explicit cut logic the team can test, and TAM/SAM/SOM as formulas with sourced inputs.

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

Use Template (uploaded reference: `02-context.md`, section `ps-market-selection-sizing / Template`) for the scaffold.


##### Required Output Convention

Default to a **one-page market analysis that mirrors the template**:

- **Market Selection:** the market name, and a PESTEL with one short entry per force, each tagged with a source ID or marked as an open question
- **Total Addressable Market:** one or two sized facts, each with a source ID
- **Segments 1 and 2:** name, one- or two-sentence description, and the users, buyers, and influencers operating in it
- **SAM per segment:** the counting logic as a short formula, with units and a range
- **SOM per segment:** the share basis and units × price = annual revenue, as a range, or "deferred until solutions are ideated"
- **Source register** below the artifact: ID, source, date, what it supports
- **Open questions** below the register: the `[TO SOURCE]` blanks and PESTEL questions, ranked by how much they could change the sizing

Use the provenance tags shared across this library wherever content is not the PM's own: `[RESEARCH]` with a source ID for anything found, `[AI-SUGGESTED, VALIDATE THIS]` for forces, segments, or cut logic you proposed. Mark numbers with no source `[TO SOURCE]`, never a guessed value.

Keep entries compact. The template's PESTEL cells, segment descriptions, and sizing boxes are small.

##### If the PM Brings a Draft

When the PM arrives with a market analysis, review it before adding to it:

1. **Altitude.** Is the market named around who the product serves and the benefit, at a level that can be analyzed and sized?
2. **PESTEL.** Flag generic forces and unsourced claims. Ask which are evidence and which are open questions.
3. **Segments.** Is the cut logic explicit and testable? Do the segments differ by needs, goals, and behaviors, or only by industry and size? Does each have real users, buyers, and influencers?
4. **Numbers.** Does every input have a source? Are units consistent, and is SOM ≤ SAM ≤ TAM? Is the market share justified by competition and capacity, or assumed?
5. **Offer fixes last**, as options to accept, adapt, or reject. Return the review as a compact table (element, verdict, why, suggested fix).

##### Step 1: Confirm the Product and Who It Serves

Before anything else, answer:

- What product or product idea is this, existing or new?
- Who is it for, and what benefit does it provide them?
- What decision is this analysis meant to inform?

**Guard against tech-role bias.** Models default to picturing software buyers and developer users. A market is defined by the people with the problem. A pump-station monitoring product's market is water utilities and the operators and directors who run them, not "IoT platforms." The users, buyers, and influencers named in each segment should be the real roles in that market (operators, technicians, directors, council members, regulators), not technologists, unless the product truly serves technologists.

##### Step 2: Gather Evidence Before Drafting

This skill uses **web research and user-supplied artifacts.** Offer both before drafting:

1. **Web research.** Offer to search for the market. Prefer primary sources: government statistics and registries, regulator data, trade-association reports, company filings, and practitioner forums. Cite each source with a link and date. Analyst summaries and vendor marketing are weak sources for sizing.
2. **User-supplied artifacts.** Ask for what the PM already holds: market reports, pricing, competitor information, company constraints, customer lists, or prior strategy work.

If no sources exist yet and web research is unavailable, say so. The Playbook advises against AI sizing without sources. Build the structure, mark every number `[TO SOURCE]`, and give a short research plan. Do not fill the gap with plausible numbers.

##### Step 3: Pressure-Test the Market Definition

Ask the three altitude questions one at a time (see [Name the Market at the Right Altitude](#name-the-market-at-the-right-altitude)). Then propose a market definition and ask the PM to confirm or iterate. Lock it before moving on.

##### Step 4: Build the PESTEL

1. Ask the PM which forces they know should, or should not, be considered.
2. Research each of the six forces.
3. Commit each as evidence with a source ID, or as an open question to research. Label assumptions and uncertainties, and suggest where reliable information could be found.

One short entry per force. If a force has nothing specific to this market, say so rather than filling the cell with a generic trend.

##### Step 5: Segment the Market

1. Propose 4-6 candidate segments defined by needs, goals, and behaviors. For each, state the cut logic and name 2-3 real buyer and user roles who operate in it. Tag them `[AI-SUGGESTED, VALIDATE THIS]` unless they came from the PM or a source.
2. Recommend two high-potential segments (strong underserved needs, problems worth solving to validate) and justify each with evidence.
3. Invite the PM to challenge the cuts and add their own knowledge. The PM chooses the segments that go in the template, at least two.
4. For each chosen segment, list the users, buyers, and influencers. Think broadly.

##### Step 6: Size the Market and Segments

1. **Name the counting unit** for this market and keep it throughout.
2. **TAM.** Size the broad market from the best available sources. Show the arithmetic.
3. **SAM per segment.** Show the counting logic as a formula (for example, number of sites × average units per site), with each input sourced or `[TO SOURCE]`.
4. **Triangulate.** Name three sizing approaches (top-down, bottom-up, analogous products, subject-matter experts) and the research each needs. Note where they agree and disagree.
5. **Express ranges**, not point estimates.
6. **SOM per segment, if there is a product.** State the share basis (competitive alternatives, reach, win rate, capacity, time horizon), then units × annual price = annual revenue, as a range. Mark an assumed price as a pricing assumption, not evidence. If there is no product yet, write "deferred until solutions are ideated."

##### Step 7: Check the Numbers

Before presenting:

- every input has a source ID or is marked `[TO SOURCE]`
- units are consistent across TAM, SAM, and SOM
- SOM ≤ SAM ≤ TAM
- no market share without a stated basis
- no competitor revenue or customer count without a source that states it
- ranges, not single numbers

##### Step 8: Hand the Call to the PM

Present the artifact with the open questions ranked by how much they could change the sizing. Recommend the segment the evidence favors if asked, and say why. Do not declare the market worth pursuing. That call stays with the PM.

##### Step 9: Offer Next Steps

Offer, as options:

1. **Write jobs for the people in the chosen segments** (ps-jobs-to-be-done). The segments and the people named in them are its input.
2. **Build a proto-persona** for the primary user in the most promising segment (ps-proto-persona).
3. **Close the biggest `[TO SOURCE]` gaps** before taking the sizing to leadership.

The user decides what comes next. Revisit this artifact as discovery produces evidence.

### ps-market-selection-sizing / Template

##### When to Use This

Use this template in the **Context** phase, before Jobs-to-Be-Done and Personas, to name the market a product serves, understand the forces acting on it, cut it into segments, and size the opportunity. It is a first pass you will revisit as you learn more.

Downstream: the segments and the people named in them feed ps-jobs-to-be-done, ps-proto-persona, ps-empathy-interviews, and ps-positioning-statement.

##### Template

```markdown
# Market Selection & Sizing

## Context
- Product or product idea (existing / new):
- Who it is for, and the benefit it provides:
- Decision this analysis informs:
- Counting unit (sites, firms, accounts, people, ...):

## 1. Market Selection
- Market:

### PESTEL
| Force | Entry | Source or status |
|---|---|---|
| Political | | [S#] / OPEN QUESTION |
| Economic | | |
| Social | | |
| Technological | | |
| Environmental | | |
| Legal | | |

> Quality check: Is the market named around who the product is for and the benefit, at a level you can analyze and size?
> Quality check: Is every entry specific to this market? A force that fits any market is generic. Replace it, or mark it OPEN QUESTION.
> Capacity check: One short line per force.

## Total Addressable Market (TAM)
- Sized fact 1: [S#]
- Sized fact 2: [S#]
- TAM (range, in the counting unit):

## 2. Segments

### Segment 1:
- Description (traits, goals, preferences, behaviors that make it unique):
- Cut logic (what distinguishes it from Segment 2, stated so it can be tested):
- Users:
- Buyers:
- Influencers:

### Segment 2:
- Description:
- Cut logic:
- Users:
- Buyers:
- Influencers:

> Quality check: Do the segments differ by needs, goals, and behaviors, not just by industry or size?
> Quality check: Does every segment have a real user and buyer in it?
> Provenance check: Tag suggested segments and cut logic `[AI-SUGGESTED, VALIDATE THIS]` until the team or a source confirms them.

## 3. Size the Market & Segments

### Serviceable Addressable Market (SAM)
| Segment | Counting logic (formula) | Inputs and sources | SAM (range) |
|---|---|---|---|
| 1 | | | |
| 2 | | | |

### Serviceable Obtainable Market (SOM), annual revenue
| Segment | Share basis (competition, reach, win rate, capacity, horizon) | Units x annual price | SOM (range) |
|---|---|---|---|
| 1 | | | |
| 2 | | | |

> Quality check: Does every input have a source ID or `[TO SOURCE]`? No guessed values.
> Quality check: Same counting unit throughout? Is SOM <= SAM <= TAM?
> Quality check: Is every market share justified by competition and capacity, not assumed?
> Quality check: Ranges, not single numbers? Triangulated from more than one approach?
> SOM rule: With no product yet, write "deferred until solutions are ideated," or show a conditional formula with the price marked as an assumption.

## Source Register
| ID | Source (title, publisher, link) | Date | What it supports |
|---|---|---|---|
| S1 | | | |

## Open Questions
Ranked by how much the answer could change the sizing.
1.
2.
3.
```

##### Usage Guidance

- Work the three parts in order: market, then segments, then size.
- Keep entries compact. The canonical template's PESTEL cells, segment boxes, and sizing boxes are small.
- Every number needs a source the PM can check. A number without one is `[TO SOURCE]`.
- The "is it worth it" judgment stays with the PM and their team.
- Revisit this artifact as discovery produces evidence.

### ps-market-selection-sizing / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For pump-station monitoring, name utilities and their operators, count stations consistently, and source every population and price input. Leave unknown inputs open.
- **Weak:** "Every utility is our market" leaves segment needs and purchasing conditions undefined.
- **Drift to avoid:** The free five percent: SOM is not an arbitrary percentage of a larger market. Show reachable accounts, capacity, adoption assumptions, and evidence.


#### Common Pitfalls

- **AI Invents the Market Size:** Every number carries a source ID or `[TO SOURCE]`. Never fill a blank with a plausible figure.

- **Competitor Numbers No One Can Know:** Use only competitive facts a filing, a report, or a named source states. Otherwise describe the competitor qualitatively and mark the gap.

- **A Generic PESTEL:** One specific entry per force, tied to this market, with a source, or an honest open question.

- **Segments for Show:** Define segments by shared needs, goals, and behaviors, and state the cut logic so it can be tested. Use size or industry only as a boundary.

- **Segments With No People in Them:** Name the users, buyers, and influencers in every segment. Think broadly.

- **The Market at the Wrong Altitude:** Run the three altitude questions. Center the definition on who the product is for and the benefit it provides.

- **The Free Five Percent:** State the share basis: the alternatives customers use, how many the team can reach, a win-rate assumption, and delivery capacity over a named horizon. If there is no basis yet, show SOM as a conditional formula and say what would anchor it.

- **Mixed Counting Units:** Name one counting unit, convert explicitly when needed, and check SOM ≤ SAM ≤ TAM.

- **One Source, One Number:** Triangulate with three approaches and present ranges.

- **Professional-Looking Logic, Never Tested:** Tag AI-suggested cut logic for validation, rank the open questions, and revisit the analysis as discovery produces evidence.

#### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-market-selection-sizing) for supporting source material and expanded examples.
