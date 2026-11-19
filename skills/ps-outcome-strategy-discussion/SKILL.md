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

The Productside Playbook sets one rule for every AI-assisted Play: **the Product Manager does the thinking, and AI pressure-tests it.** In this skill, you are the AI. Hold yourself to these rules:

1. **Pressure-test before you produce.** When the user brings a draft, critique it against the Play's formats and criteria first. Point at the specific words that fail and ask the user to fix them. Offer rewrites only after the critique, as options to accept, adapt, or reject.
2. **Never stand in for the customer.** Do not present jobs, quotes, needs, or pains you generated as research, and do not answer as the persona as if your answers were evidence. Anything you draft about customers is a hypothesis, labeled as one, to validate with real people. Role-play is allowed only as rehearsal where the Play calls for it, labeled as practice, and nothing from it goes into findings.
3. **Never stand in for the team's judgment.** Do not put unsourced figures into the artifact, and do not make calls the team should own. A number without a source is a blank to fill, so mark it that way.
4. **Work the five habits.** *Context:* ask for the persona, market, outcome, and constraints when they are missing. *Guide:* offer competing views and welcome pushback. *Enforce:* work inside the Play's template, not around it. *Outcome:* tie the work to the decision it supports. *Iterate:* go step by step rather than one-shot.
5. **Keep best guess honest.** Best guess mode is allowed. When you use it, label every inferred detail inline and end with **Assumptions to Validate**. A best guess is a starting point to test, never a finding.

For people working in a chat tool without this skill, the Play's copy-paste prompts are in [prompts/](prompts/README.md).

### Guided Mode

When a user asks to be walked through this skill, signals unfamiliarity, or invokes it without enough context, run in guided mode. **Do NOT batch multiple questions into one turn. Do NOT list everything you need up front. One question per turn, every turn.**

1. **Open with a heads-up.** State what the skill produces, the estimated number of questions, and where you will stop for the user's decision. Offer three entry paths:
   - (1) **Guided** - one question at a time with recommendations
   - (2) **Context dump** - paste what you know and I will ask only what is missing
   - (3) **Best guess** - I will infer what I can and label every assumption

   Then ask the first question immediately (do not wait for the user to pick a mode - Guided is the default).

2. **Start from what is already supplied.** Treat text in the request, pasted notes, attached files, upstream Play artifacts, and decisions made earlier in the conversation as answers already given. Do not ask for them again. Begin at the first real gap, and keep the progress label honest about what remains.

3. **One question per turn.** Every turn follows this exact format:

   > `Context Q2/5`
   >
   > **Who are the primary users of this product?**
   >
   > Some options to consider:
   > 1. Clinical data managers who run queries against study databases
   > 2. Research scientists who need self-service access to trial data
   > 3. Biostatisticians who build analysis-ready datasets
   > 4. Other (describe your users)
   >
   > Pick one or more (e.g. `1`, `1,3`, `1 and 3`), or describe in your own words.

   The progress label (e.g. `Context Q2/5`) is mandatory on every turn. Recommendations must always be numbered `1.`, `2.`, `3.`, `4. Other` - never presented as bullet points or unnumbered prose. The three recommendations must be specific to the skill, the industry, and the context gathered so far - never generic placeholders. If you lack domain context for good recommendations, do a web search first to ground your options in real roles, real products, or real workflows. Explain why a question matters when that is not obvious, and ask a follow-up only when the answer could change the artifact or the decision.

   **Exception: evidence only the user has.** When a question asks for something only the user can know (a root cause, what customers said or did, what the user observed, a number they must set), ask it as an open question with no numbered options, and say why there are none. Options there would put guesses in the user's mouth.

4. **Recommendations get smarter each turn.** Each answer becomes context for the next question's recommendations. By the mid-point, options should reflect the specific product, customer, and situation the user has described - not generic suggestions. Early questions can use industry-typical examples; later questions must incorporate what the user has already told you.

5. **In context dump mode, show what you extracted first.** Before asking anything, give a short **Known / Assumed / Missing / Conflicting** summary of what the user supplied. Credit where each item came from, and keep what a source reported separate from what has been verified. Then ask only the questions that would most change the artifact.

6. **Interruption-safe.** Handle any of these mid-session:
   - **Meta questions** ("how many left?", "what does this term mean?"): answer directly, restate progress, restate the pending question, then wait.
   - **Mode switch** ("just take your best guess", "here is everything I know"): switch to the requested mode immediately. For best guess, infer remaining answers from context gathered so far, generate the artifact, and end with an explicit **Assumptions to Validate** list, ranked by how much each could change the decision. For context dump, parse what was provided and ask only about gaps.
   - **Correction** ("actually, go back to Q2"): revisit that question with the original recommendations updated for current context.
   - **Pause or stop**: stop immediately. On resume, summarize what was captured, what is still open, and the next question.

7. **Finish with a summary, then hand back the decision.** After the context is gathered, recap in a few short bullets: what was supplied, what was inferred, what remains unknown or disputed, and whether the work is ready for a decision. Confirm before generating the artifact. If best guess mode was used at any point, end with an explicit **Assumptions to Validate** list. When the user faces a choice (which option, which next Play, whether to proceed), present a numbered ladder: the option the evidence favors first, labeled `(Recommended)`, then two or three genuinely distinct alternatives, each with its tradeoff in one sentence, then `Other`. Allow combining options where it makes sense. The user decides.

## Application

Use [template.md](template.md) for the working scaffold.

See the source pages from the canonical playbook in [assets/ps_outcome_strategy_discussion_playbook_pages.pdf](assets/ps_outcome_strategy_discussion_playbook_pages.pdf).

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

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in [prompts/01-prepare-discussion-guide.md](prompts/01-prepare-discussion-guide.md) one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

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

## Examples

See [examples/sample.md](examples/sample.md).

The example set includes:

- a strong guided discussion summary for a logistics software scenario
- a weak version of the same scenario showing vague answers accepted as complete
- a drift bug example where the business outcome was captured as a project milestone

## Common Pitfalls

### Pitfall 1: Treating the Discussion as a Requirements Intake

**Symptom:** The PM enters the meeting ready to record what the manager tells them to build. They leave with a feature list instead of a business outcome.

**Consequence:** Discovery is framed around delivering the feature, not solving the customer problem. The business outcome is never explicitly agreed on.

**Fix:** Before the meeting, reframe the purpose: the PM is there to understand what the business needs to achieve, not what to build. If the manager jumps to solutions, the PM redirects: "That sounds like one approach - can we first align on what success looks like for the business overall?"

### Pitfall 2: Accepting Vague Outcomes Without Pressing

**Symptom:** The business outcome is recorded as "improve customer satisfaction" or "grow the business" and the PM moves on.

**Consequence:** The outcome is unmeasurable. Discovery produces findings that no one can act on because there is no shared standard for success.

**Fix:** Press for specifics. "Improve customer satisfaction" needs a metric and a direction: "Increase NPS from 32 to 50 within 12 months." If the manager cannot provide a specific target, write "TBD" and flag it as a gap that must be resolved before discovery begins.

### Pitfall 3: Skipping the KDP

**Symptom:** The conversation ends, the PM writes up notes, and begins discovery the next day without making an explicit proceed or escalate decision.

**Consequence:** Discovery begins on an unstable foundation. If the business outcome is still contested, the research findings will be contested too.

**Fix:** Treat the KDP as a required output, not an optional reflection. Before starting discovery, the PM should have a written KDP statement on file.

### Pitfall 4: Letting the Manager Dictate the Solution

**Symptom:** During the outcomes conversation, the manager proposes a specific feature, technology, or approach, and the PM records it as the solution rather than redirecting to the outcome.

**Consequence:** Discovery is bypassed. The PM goes directly from alignment conversation to building something the manager suggested, without validating whether it solves the customer problem.

**Fix:** Solutions that emerge during an outcomes conversation are hypotheses, not decisions. Record them in the open questions section and flag them for validation during discovery.

### Pitfall 5: Documenting the Conversation Without Identifying the Gaps

**Symptom:** The PM writes a complete-looking summary that covers all five areas, but fills in vague or placeholder answers in the areas where the conversation was unclear.

**Consequence:** The summary looks complete but is not. The PM and the manager may have different memories of what was agreed.

**Fix:** In the open questions section, be explicit about what was not resolved. A summary with two or three open questions documented is more useful than a summary with five areas filled in with uncertain answers.

### Pitfall 6: Confusing Internal Stakeholders with the Customer

**Symptom:** The PM documents "our customers" as "the PM team," "engineering," or "the business unit" - the internal stakeholders they work with, not the people who use or buy the product.

**Consequence:** Discovery targets internal processes instead of customer problems. The play produces internal alignment but no customer insight.

**Fix:** The customer field in this play refers to who the product serves in the field - the person who uses or buys the thing the PM is building. If the product is built for external users, the customer is external. If the product is internal tooling, the customer is the internal user population (not the sponsoring executive).

### Pitfall 7: AI Answers for the Manager

**Symptom:** The PM asks the agent to fill the discussion template "with what leadership probably wants" before the conversation happens.

**Consequence:** The business outcome and success criteria are the model's guesses. The PM walks into discovery aligned with a document, not with their manager.

**Fix:** Prepare questions, not answers. Fill the template only from notes of the real discussion, and mark anything still unconfirmed.

## References

### Skill Files

- [template.md](template.md) - working scaffold
- [prompts/](prompts/README.md) - copy-paste prompt for chat-based AI tools (authored for this library; the deck has no AI page for this Play)
- [examples/sample.md](examples/sample.md) - strong, weak, and drift-bug examples

### Related Skills



### Source Material

- [assets/ps_outcome_strategy_discussion_playbook_pages.pdf](assets/ps_outcome_strategy_discussion_playbook_pages.pdf)
- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 5-7: Template 01 of 24 there. No AI page for this Play; the prompts are authored for this library. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).

### Template and Examples

- [template.md](template.md)
- [examples/sample.md](examples/sample.md)

### Budget Data

- [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)

### Adjacent Skills

- [ps-outcome-tree](../ps-outcome-tree/SKILL.md) - builds on the alignment reached here; takes the business outcome and product outcomes from this play as inputs
- [ps-jobs-to-be-done](../ps-jobs-to-be-done/SKILL.md) - starts from the customer identified in this play
- [ps-framing-the-problem](../ps-framing-the-problem/SKILL.md) - problem statement work that follows from the customer context established here
