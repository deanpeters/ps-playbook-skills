---
name: ps-outcome-strategy-discussion
description: >-
  Facilitate a structured PM-manager alignment conversation to confirm the
  business outcome, context, and success criteria before discovery begins.
intent: >-
  Help a PM prepare for and document a guided discussion with their manager or
  leadership so they enter discovery with a clear, shared business outcome.
type: process
blueprint_stage: Context
best_for:
  - "Aligning with your manager on the business outcome before discovery begins"
  - "Preparing for a strategy conversation with an executive sponsor"
  - "Documenting the agreed business context so the team starts from shared ground"
scenarios:
  - "I have a new initiative and need to align with my VP on the business outcome before starting discovery"
  - "Help me prepare for a strategy conversation with my executive sponsor about what success looks like"
---


## Purpose

Run the opening play of the Productside Playbook.

Before discovery begins, a PM needs one thing: a clear, shared understanding of the business outcome they are being asked to achieve. This play produces that understanding through a structured guided discussion with a manager, executive sponsor, or product leadership. The agent helps the PM prepare for that conversation and document what emerges from it. The conversation itself is PM-owned.

Use this skill when you need to:

- prepare a structured discussion guide before meeting with a manager or sponsor
- document the business outcome, context, and success criteria after the conversation
- surface assumptions the PM is already carrying so they can be validated rather than asserted
- make a Key Decision Point call: proceed to discovery, escalate for clarity, or reschedule

This is not a requirements intake. The PM is not receiving a brief. The PM is facilitating a two-way alignment where both parties build shared understanding. If the manager is dictating solutions during a conversation about outcomes, that is a signal to redirect.

## Key Concepts

### 1. Guided Discussion vs. Requirements Handoff

A requirements handoff is one-directional: someone tells you what to build. A guided discussion is two-directional: both parties contribute to building shared understanding of what the business needs to achieve and why.

The PM facilitates the discussion by asking open-ended questions, pressing when answers are vague, and recording what emerges. The manager or sponsor provides context, constraints, and strategic rationale. The output is not a spec. It is a shared written record of the alignment reached.

If a PM enters this conversation expecting to receive a feature list, they will miss the purpose of the play. The goal is a business outcome, not a scope document.

### 2. Business Outcome First

The central task of this play is establishing the business outcome: what the organization is trying to achieve at a strategic or operational level. This is not a feature. It is not a project milestone. It is a measurable change in the state of the business.

Weak: "Launch the new shipper dashboard by Q3"
Stronger: "Reduce 90-day churn among mid-market shippers by 15%"

The launch is an output. The churn reduction is an outcome. This distinction matters because discovery cannot begin without clarity on the outcome. If the PM starts discovery while the business outcome is still defined as a project scope, they will optimize for the project and miss the customer problem.

### 3. The Key Decision Point (KDP)

At the end of this play, the PM makes an explicit call about whether to proceed.

- Go: alignment is clear, the PM proceeds to discovery
- Partial: some areas are clear, others need follow-up by a specific date
- No-go: alignment is missing or contradictory - escalate or reschedule before continuing

The KDP is not a formality. Skipping it is the failure mode where a PM enters discovery without a stable business outcome and then produces research that no one can act on because the frame is still contested. If the manager cannot agree on the outcome, the PM should not proceed - they should surface the disagreement and request a follow-up.

### 4. Three Roles of the PM in This Play

The PM wears three hats during this play:

- **Facilitator:** asks open-ended questions, creates space for the manager to think aloud, follows up when answers are vague or contradictory
- **Recorder:** captures what the manager says in structured notes during or immediately after the conversation, writes the agreed business outcome in one clear sentence
- **Sense-maker:** reviews the notes afterward to find gaps, contradictions, and unstated assumptions; flags open questions before starting discovery

The agent supports preparation (before) and documentation (after). The PM owns the middle.

### 5. Preparing the Guide vs. Running the Discussion vs. Documenting Results

There are three distinct phases of this play:

- **Preparing the guide (agent-supported):** Draft open-ended questions for each discussion area. Surface assumptions the PM already holds. Flag visible gaps or contradictions before the conversation begins.
- **Running the discussion (PM-owned, agent cannot participate):** The PM facilitates the conversation, takes notes, and makes judgment calls in real time. The agent cannot do this.
- **Documenting outcomes (agent-supported):** After the conversation, the PM shares their notes with the agent, who helps structure the summary, identify gaps, and draft the KDP call.

If the user asks the agent to conduct the discussion itself or generate what "the manager probably said," redirect: the discussion must happen with a real person who has context the agent does not have.

### 6. The Five Discussion Areas

Every guided discussion for this play covers five areas:

1. **Business Outcome** - what the business needs to achieve, written as a measurable change
2. **Why Now** - what changed that makes this the priority, and what happens if it is not addressed
3. **Customer** - who the product serves (role and context), and whether there are secondary stakeholders
4. **Success Criteria** - what measurable change would indicate the outcome was achieved
5. **Constraints and Non-Negotiables** - what is already decided, what is off-limits, and what dependencies exist

These five areas are the structure of both the discussion guide and the documentation template. A conversation that covers all five and produces specific, agreed answers is a successful execution of this play.

### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **preparation coach for the discussion, never a stand-in for the manager**. It helps the PM gather what they already know, turn it into sharp, unbiased questions for each discussion area, and name the decision the discussion must reach. The answers come from the manager, in the room.

- **Use it when:** the PM has gathered the key documents and wants to prepare questions for the discussion, or has notes from the discussion to turn into the template.
- **Avoid it when:** the request is to guess what the manager will say, or to fill the discussion template without the discussion happening.
- **Return:** the PM's own questions for each discussion area, tested for bias and clarity; the business outcome stated as a measurable change; and, after the discussion, the template filled only from the PM's notes.

### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

## Application

Use [Template](#template) for the working scaffold.


### Required Output Convention

Default to a **clean, paste-ready structured summary** with clearly labeled sections.

That means:

- fill all five discussion areas
- write the business outcome as a single, specific, measurable sentence
- keep the customer statement concrete (a job title and context, not an org chart entry)
- list open questions rather than omitting them
- write the KDP call with a checkbox clearly marked

The summary comes first. Commentary is secondary.

### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses Discovery mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

### Step 1: Confirm Scope and Participants

Before preparing the guide, establish:

- Who is the discussion with? (direct manager, exec sponsor, product leadership - name and role if possible)
- What product or initiative is this for?
- What is the time horizon? (quarterly, annual, multi-year)
- Has any prior alignment work been done? (existing OKRs, product brief, strategy deck)

This play does not require a tech-role bias guard. The subject of this conversation is internal strategic alignment, not a customer persona. The customer who the product serves will be identified during the discussion and documented afterward - they are not the subject of this exercise.

Note any prior materials the PM already has, because they will inform which questions can be skipped and which need more depth.

### Step 2: Prepare the Discussion Guide

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

### Step 3: Run the Discussion (PM-Owned)

This step is performed by the PM. The agent does not participate.

The PM should:

- facilitate rather than receive (ask questions, follow up, redirect solution-talk back to outcome-talk)
- take notes during or immediately after the conversation
- watch for vague answers and press for specifics ("improve performance" needs a metric; "grow the business" needs a direction and timeframe)
- note when the manager starts proposing solutions - this is a signal that the outcome is not yet clear
- watch for false alignment: both parties nodding without actually agreeing on specifics

**What good alignment feels like:** both parties can state the business outcome in the same specific terms, the customer is named by role and context (not by org chart), and both parties agree on at least one measurable success criterion.

**What false alignment looks like:** the meeting ends with everyone feeling satisfied, but the PM's notes contain phrases like "something around retention," "the usual metrics," or "they mentioned a few things."

### Step 4: Document the Outcomes

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

### Step 5: Make the KDP Call

After the summary is complete, the PM makes an explicit Key Decision Point decision:

- **Go:** alignment is clear across all five areas. The PM proceeds to discovery.
- **Partial:** most areas are clear, but one or two need follow-up. Document which areas, what is unclear, and a target date for resolution. The PM should not begin full discovery until partial items are resolved.
- **No-go:** the business outcome is still contested, the customer is undefined, or success criteria are absent. The PM escalates the misalignment to the manager or reschedules before continuing.

The agent can help draft the KDP statement, but the call belongs to the PM.

## Template

### When to Use This

Use this template before discovery begins to document the alignment conversation between a PM and their manager or executive sponsor. The conversation must happen first. Fill in the outcome section after the discussion, not before.

Completing this template is the exit condition for this play. Do not begin discovery work until the Key Decision Point is marked.

---

### Template

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

## Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For shipper retention, align with the manager on the business result, customer, decision boundaries, and evidence needed before discovery.
- **Weak:** "Improve retention somehow" leaves the result and authority unclear.
- **Drift to avoid:** Outcome as project: "Launch a shipper portal" is an output. Establish the business change it is expected to produce.


## Common Pitfalls

- **Treating the Discussion as a Requirements Intake:** Before the meeting, reframe the purpose: the PM is there to understand what the business needs to achieve, not what to build. If the manager jumps to solutions, the PM redirects: "That sounds like one approach - can we first align on what success looks like for the business overall?"

- **Accepting Vague Outcomes Without Pressing:** Press for specifics. "Improve customer satisfaction" needs a metric and a direction: "Increase NPS from 32 to 50 within 12 months." If the manager cannot provide a specific target, write "TBD" and flag it as a gap that must be resolved before discovery begins.

- **Skipping the KDP:** Treat the KDP as a required output, not an optional reflection. Before starting discovery, the PM should have a written KDP statement on file.

- **Letting the Manager Dictate the Solution:** Solutions that emerge during an outcomes conversation are hypotheses, not decisions. Record them in the open questions section and flag them for validation during discovery.

- **Documenting the Conversation Without Identifying the Gaps:** In the open questions section, be explicit about what was not resolved. A summary with two or three open questions documented is more useful than a summary with five areas filled in with uncertain answers.

- **Confusing Internal Stakeholders with the Customer:** The customer field in this play refers to who the product serves in the field - the person who uses or buys the thing the PM is building. If the product is built for external users, the customer is external. If the product is internal tooling, the customer is the internal user population (not the sponsoring executive).

- **AI Answers for the Manager:** Prepare questions, not answers. Fill the template only from notes of the real discussion, and mark anything still unconfirmed.

## References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-outcome-strategy-discussion) for supporting source material and expanded examples.
