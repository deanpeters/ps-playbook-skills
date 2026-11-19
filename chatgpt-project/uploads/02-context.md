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

The Productside Playbook sets one rule for every AI-assisted Play: **the Product Manager does the thinking, and AI pressure-tests it.** In this skill, you are the AI. Hold yourself to these rules:

1. **Pressure-test before you produce.** When the user brings a draft, critique it against the Play's formats and criteria first. Point at the specific words that fail and ask the user to fix them. Offer rewrites only after the critique, as options to accept, adapt, or reject.
2. **Never stand in for the customer.** Do not present jobs, quotes, needs, or pains you generated as research, and do not answer as the persona as if your answers were evidence. Anything you draft about customers is a hypothesis, labeled as one, to validate with real people. Role-play is allowed only as rehearsal where the Play calls for it, labeled as practice, and nothing from it goes into findings.
3. **Never stand in for the team's judgment.** Do not put unsourced figures into the artifact, and do not make calls the team should own. A number without a source is a blank to fill, so mark it that way.
4. **Work the five habits.** *Context:* ask for the persona, market, outcome, and constraints when they are missing. *Guide:* offer competing views and welcome pushback. *Enforce:* work inside the Play's template, not around it. *Outcome:* tie the work to the decision it supports. *Iterate:* go step by step rather than one-shot.
5. **Keep best guess honest.** Best guess mode is allowed. When you use it, label every inferred detail inline and end with **Assumptions to Validate**. A best guess is a starting point to test, never a finding.

For people working in a chat tool without this skill, the Play's copy-paste prompts are in prompts/ (uploaded reference: `07-prompts.md`, section `ps-outcome-strategy-discussion / Companion / README.md`).

##### Guided Mode

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

#### Application

Use template.md (uploaded reference: `02-context.md`, section `ps-outcome-strategy-discussion / Template`) for the working scaffold.

See the source pages from the canonical playbook in assets/ps_outcome_strategy_discussion_playbook_pages.pdf (source material, not included in this upload kit).

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

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in prompts/01-prepare-discussion-guide.md (uploaded reference: `07-prompts.md`, section `ps-outcome-strategy-discussion / Companion / 01-prepare-discussion-guide.md`) one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

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

#### Examples

See examples/sample.md (uploaded reference: `02-context.md`, section `ps-outcome-strategy-discussion / Examples`).

The example set includes:

- a strong guided discussion summary for a logistics software scenario
- a weak version of the same scenario showing vague answers accepted as complete
- a drift bug example where the business outcome was captured as a project milestone

#### Common Pitfalls

##### Pitfall 1: Treating the Discussion as a Requirements Intake

**Symptom:** The PM enters the meeting ready to record what the manager tells them to build. They leave with a feature list instead of a business outcome.

**Consequence:** Discovery is framed around delivering the feature, not solving the customer problem. The business outcome is never explicitly agreed on.

**Fix:** Before the meeting, reframe the purpose: the PM is there to understand what the business needs to achieve, not what to build. If the manager jumps to solutions, the PM redirects: "That sounds like one approach - can we first align on what success looks like for the business overall?"

##### Pitfall 2: Accepting Vague Outcomes Without Pressing

**Symptom:** The business outcome is recorded as "improve customer satisfaction" or "grow the business" and the PM moves on.

**Consequence:** The outcome is unmeasurable. Discovery produces findings that no one can act on because there is no shared standard for success.

**Fix:** Press for specifics. "Improve customer satisfaction" needs a metric and a direction: "Increase NPS from 32 to 50 within 12 months." If the manager cannot provide a specific target, write "TBD" and flag it as a gap that must be resolved before discovery begins.

##### Pitfall 3: Skipping the KDP

**Symptom:** The conversation ends, the PM writes up notes, and begins discovery the next day without making an explicit proceed or escalate decision.

**Consequence:** Discovery begins on an unstable foundation. If the business outcome is still contested, the research findings will be contested too.

**Fix:** Treat the KDP as a required output, not an optional reflection. Before starting discovery, the PM should have a written KDP statement on file.

##### Pitfall 4: Letting the Manager Dictate the Solution

**Symptom:** During the outcomes conversation, the manager proposes a specific feature, technology, or approach, and the PM records it as the solution rather than redirecting to the outcome.

**Consequence:** Discovery is bypassed. The PM goes directly from alignment conversation to building something the manager suggested, without validating whether it solves the customer problem.

**Fix:** Solutions that emerge during an outcomes conversation are hypotheses, not decisions. Record them in the open questions section and flag them for validation during discovery.

##### Pitfall 5: Documenting the Conversation Without Identifying the Gaps

**Symptom:** The PM writes a complete-looking summary that covers all five areas, but fills in vague or placeholder answers in the areas where the conversation was unclear.

**Consequence:** The summary looks complete but is not. The PM and the manager may have different memories of what was agreed.

**Fix:** In the open questions section, be explicit about what was not resolved. A summary with two or three open questions documented is more useful than a summary with five areas filled in with uncertain answers.

##### Pitfall 6: Confusing Internal Stakeholders with the Customer

**Symptom:** The PM documents "our customers" as "the PM team," "engineering," or "the business unit" - the internal stakeholders they work with, not the people who use or buy the product.

**Consequence:** Discovery targets internal processes instead of customer problems. The play produces internal alignment but no customer insight.

**Fix:** The customer field in this play refers to who the product serves in the field - the person who uses or buys the thing the PM is building. If the product is built for external users, the customer is external. If the product is internal tooling, the customer is the internal user population (not the sponsoring executive).

##### Pitfall 7: AI Answers for the Manager

**Symptom:** The PM asks the agent to fill the discussion template "with what leadership probably wants" before the conversation happens.

**Consequence:** The business outcome and success criteria are the model's guesses. The PM walks into discovery aligned with a document, not with their manager.

**Fix:** Prepare questions, not answers. Fill the template only from notes of the real discussion, and mark anything still unconfirmed.

#### References

##### Skill Files

- template.md (uploaded reference: `02-context.md`, section `ps-outcome-strategy-discussion / Template`) - working scaffold
- prompts/ (uploaded reference: `07-prompts.md`, section `ps-outcome-strategy-discussion / Companion / README.md`) - copy-paste prompt for chat-based AI tools (authored for this library; the deck has no AI page for this Play)
- examples/sample.md (uploaded reference: `02-context.md`, section `ps-outcome-strategy-discussion / Examples`) - strong, weak, and drift-bug examples

##### Related Skills



##### Source Material

- assets/ps_outcome_strategy_discussion_playbook_pages.pdf (source material, not included in this upload kit)
- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 5-7: Template 01 of 24 there. No AI page for this Play; the prompts are authored for this library. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).

##### Template and Examples

- template.md (uploaded reference: `02-context.md`, section `ps-outcome-strategy-discussion / Template`)
- examples/sample.md (uploaded reference: `02-context.md`, section `ps-outcome-strategy-discussion / Examples`)

##### Budget Data

- [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)

##### Adjacent Skills

- ps-outcome-tree (uploaded reference: `02-context.md`, section `ps-outcome-tree / Instructions`) - builds on the alignment reached here; takes the business outcome and product outcomes from this play as inputs
- ps-jobs-to-be-done (uploaded reference: `03-discover-investigate.md`, section `ps-jobs-to-be-done / Instructions`) - starts from the customer identified in this play
- ps-framing-the-problem (uploaded reference: `03-discover-investigate.md`, section `ps-framing-the-problem / Instructions`) - problem statement work that follows from the customer context established here

### ps-outcome-strategy-discussion / Template

### Outcome & Strategy: Guided Discussion

#### When to Use This

Use this template before discovery begins to document the alignment conversation between a PM and their manager or executive sponsor. The conversation must happen first. Fill in the outcome section after the discussion, not before.

Completing this template is the exit condition for this play. Do not begin discovery work until the Key Decision Point is marked.

---

#### Template

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

### Outcome & Strategy: Guided Discussion - Examples

---

#### Example 1: Strong

**Scenario:** A PM at a logistics software company whose product helps freight carriers manage shipper relationships. The PM's manager has flagged shipper churn as a growing problem and requested a PM-led initiative to address it.

```markdown
# Outcome & Strategy: Guided Discussion

## Scope

- Discussion with: Priya Venkataraman, VP of Product
- Initiative or product: Shipper Retention Initiative
- Date: 14 March 2026
- Time horizon: 12 months (FY26)

---

## Outcome of the Discussion

### Business Outcome (one sentence)

Reduce 90-day shipper churn among mid-market accounts from 22% to under 12% by the end of FY26.

### Why It Matters Now

Mid-market shippers represent 60% of contracted revenue but have shown accelerating churn since Q3 last year, driven in part by two competitors launching improved onboarding experiences. The board has flagged net revenue retention as a primary health metric for FY26 and this segment is pulling it below target.

### Customer

Mid-market shipper operations managers at companies moving 200 to 2,000 shipments per month, responsible for carrier selection, freight cost management, and exception handling. They use our platform daily but currently describe the first 90 days as confusing and unsupported.

### Success Criteria

| Criteria | Metric or Signal | Target |
|---|---|---|
| 90-day churn rate (mid-market) | Percentage of mid-market accounts churning within 90 days of contract start | Under 12% by Q4 FY26 |
| Time to first successful shipment | Days from account activation to first completed shipment | Under 7 days (from current 18) |
| Early-stage support ticket volume | Support tickets per account in first 90 days | Reduce by 40% |

### Constraints

- Engineering capacity: one squad available for this initiative through Q3; a second squad can be added in Q4 if early results warrant it
- Timeline: any changes affecting the shipper onboarding flow must be live before the summer shipping peak (end of May)
- Technology: the current onboarding module is being migrated to the new platform in Q3; solutions must work within the existing module or be designed to port to the new platform
- Out of scope: enterprise accounts and spot-freight shippers are handled by a separate team

### Open Questions and Gaps

- The 12% churn target came from the finance team's NRR model, but no one has validated whether that target is achievable with the resources available. Need to confirm with finance by end of month.
- The root cause of churn is assumed to be onboarding quality, but we have not yet spoken to churned shippers. This assumption drives the entire initiative frame and needs to be tested early in discovery.

---

## Key Decision Point

- [x] Go: alignment is clear across all five areas. Proceed to discovery.

Caveat: the finance target confirmation and root-cause assumption should be first items on the discovery agenda.
```

**Why this works:**

- The business outcome is specific and measurable: a named segment, a named metric (90-day churn), a current baseline (22%), a target (under 12%), and a time horizon (FY26). A third party could assess whether it was achieved.
- The customer is named by role and context. It identifies not just a job title but the operational situation (200 to 2,000 shipments per month, daily users, 90-day struggle) that makes this population meaningful.
- The success criteria table has three rows, each with a named metric and a specific target. None of them say "improve" without quantifying what improvement means.
- The open questions section does not paper over gaps. It explicitly flags two assumptions that could invalidate the entire initiative if unchecked - and the PM takes responsibility for testing them early.
- The KDP is marked Go, but with a documented caveat rather than unqualified sign-off. This is honest alignment.

---

#### Example 2: Weak

**Scenario:** The same company, the same manager, the same conversation - but the PM recorded vague answers, accepted weak language as complete, and left critical fields underdefined.

```markdown
# Outcome & Strategy: Guided Discussion

## Scope

- Discussion with: VP of Product
- Initiative or product: Churn project
- Date: March 2026
- Time horizon: this year

---

## Outcome of the Discussion

### Business Outcome (one sentence)

Improve shipper satisfaction and reduce churn.

### Why It Matters Now

Churn has been a problem and the board wants to see it fixed. We are behind competitors.

### Customer

Shippers who use our platform.

### Success Criteria

| Criteria | Metric or Signal | Target |
|---|---|---|
| Satisfaction | NPS or CSAT | Improve |
| Churn | Churn rate | Reduce |

### Constraints

- Limited engineering time
- Need to move fast

### Open Questions and Gaps

None noted.

---

## Key Decision Point

- [x] Go: proceed to discovery.
```

**Why this fails:**

- **Business Outcome:** "Improve shipper satisfaction and reduce churn" bundles two different outcomes with no measurement and no target. A third party cannot assess whether this was achieved. This is the acceptance of vague language that Pitfall 2 describes.
- **Why Now:** "Churn has been a problem" is background noise, not strategic rationale. It does not establish urgency or explain what changed to make this the current priority.
- **Customer:** "Shippers who use our platform" covers potentially thousands of accounts across multiple segments with different needs. It gives discovery no useful frame. Is this small shippers? Enterprise shippers? The entire customer base?
- **Success Criteria:** Both rows say "improve" or "reduce" without a baseline, a target, or a timeframe. These are not success criteria. They are aspirations. A PM cannot tell whether they succeeded if they have no definition of success.
- **Constraints:** "Limited engineering time" and "need to move fast" are not constraints. They are vague acknowledgments that resources are finite. Every project has finite resources. A real constraint names what is fixed: a specific team, a deadline, a technical boundary.
- **Open Questions:** Marking "None noted" when two major assumptions are unvalidated (root cause of churn, achievability of any target) is active gap suppression. The gaps exist. They are just not documented.
- **KDP:** The Go call is marked without any basis for confidence. This PM is proceeding to discovery while carrying a contested outcome, an undefined customer, and unmeasured success criteria.

---

#### Example 3: Drift Bug - Outcome Captured as a Project

**Scenario:** Same company, same conversation. But in this version, the PM writes down what the manager said at the end of the meeting - a project scope - instead of the business outcome the project is meant to achieve.

```markdown
### Business Outcome (one sentence)

Launch the new shipper onboarding dashboard by Q3.
```

**Why this fails:**

This is the most common failure mode in this play, and it is easy to miss because it sounds specific and concrete. "Launch the new shipper onboarding dashboard by Q3" has a named deliverable and a date. It feels like a well-defined outcome. It is not.

A project milestone describes what the team will ship. A business outcome describes what changes for the business when the project succeeds.

The dashboard launch is an output. Reducing 90-day churn among mid-market shippers is the outcome. These are categorically different, and the distinction matters for everything that follows:

- **Discovery framed around the project:** the PM will research how to build a better dashboard, not whether a dashboard solves the customer's actual problem. If the real problem is something the dashboard cannot address (pricing, support response time, competitor switching costs), the project will be completed on time and still fail.
- **Success defined by delivery:** the team celebrates shipping the dashboard in Q3, but no one tracks whether churn improved. The business outcome that motivated the project is never measured.
- **No KDP leverage:** if the PM reaches a Go decision with "launch dashboard by Q3" as the outcome, there is no meaningful escalation path if discovery reveals the approach is wrong. You cannot escalate "we should reconsider the dashboard" when the entire frame is "deliver the dashboard."

**The fix:** before recording a business outcome, ask: "Is this what we are delivering, or is this what changes for the business when we deliver it successfully?" If the answer is "what we are delivering," press for the outcome behind it. "What should improve for the business as a result of launching the dashboard?" - that answer is the business outcome.

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

This is the distinction that matters most. Engagement modes are not a comms schedule — they determine who has input on which decisions and at what depth.

- **Manage Closely** stakeholders are in the room for trade-off discussions. They have a voice in decisions, not just updates.
- **Keep Satisfied** stakeholders are briefed on outcomes and key decisions, but they are not consulted in the decision process itself. They need altitude-appropriate information, not operational depth.
- **Keep Informed** stakeholders receive regular updates but do not affect decisions. Their value is advocacy and downstream adoption, not direction-setting.
- **Monitor** stakeholders are not in the decision loop at all. Periodic check-ins prevent surprises, but they do not shape the work.

Treating all engagement as a communication cadence question misses this. A PM who sends weekly updates to all stakeholders has not done stakeholder management — they have sent emails. The quadrant assignment determines who the PM brings into decisions, not just who receives communications.

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

Different functions bring different priorities: legal thinks about risk, finance thinks about returns, engineering thinks about technical feasibility. Those differences create friction — but they do not make stakeholders adversaries.

The playbook is explicit: you may have different roles, but you are all working on the same team. A skeptical legal counsel who raises a compliance concern in week two is not an obstacle — they are a teammate whose input prevented a problem at launch. A finance stakeholder who pushes back on scope is not blocking the product — they are enforcing a constraint that is real for the business.

Approach every stakeholder as someone who shares the organization's goals, even if they express those goals differently than you do. The map is a tool for building a communication strategy across that diversity, not a list of people to manage around.

##### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **critic of the stakeholder map the PM drafted**. It looks for stakeholders the PM missed, asks for the evidence behind each power and interest placement, and checks that each engagement strategy fits the quadrant. The placements and strategies stay the PM's, because only the PM knows these people.

- **Use it when:** the PM has listed stakeholders and wants the map pressure-tested for gaps and placement.
- **Avoid it when:** the request is to characterize real colleagues' motives or influence from a name and a title. The model doesn't know them. When given names and titles, first ask what the PM has observed about each person's decisions and influence, and name any roles that may be missing. Offer placements, each tagged `[AI-SUGGESTED, VALIDATE THIS]`, only if the PM then asks for a best guess.
- **Return:** missing stakeholder roles named for the PM to consider, each placement questioned against what the PM has observed, and engagement strategies checked against decision rights.

##### Working With AI

The Productside Playbook sets one rule for every AI-assisted Play: **the Product Manager does the thinking, and AI pressure-tests it.** In this skill, you are the AI. Hold yourself to these rules:

1. **Pressure-test before you produce.** When the user brings a draft, critique it against the Play's formats and criteria first. Point at the specific words that fail and ask the user to fix them. Offer rewrites only after the critique, as options to accept, adapt, or reject.
2. **Never stand in for the customer.** Do not present jobs, quotes, needs, or pains you generated as research, and do not answer as the persona as if your answers were evidence. Anything you draft about customers is a hypothesis, labeled as one, to validate with real people. Role-play is allowed only as rehearsal where the Play calls for it, labeled as practice, and nothing from it goes into findings.
3. **Never stand in for the team's judgment.** Do not put unsourced figures into the artifact, and do not make calls the team should own. A number without a source is a blank to fill, so mark it that way.
4. **Work the five habits.** *Context:* ask for the persona, market, outcome, and constraints when they are missing. *Guide:* offer competing views and welcome pushback. *Enforce:* work inside the Play's template, not around it. *Outcome:* tie the work to the decision it supports. *Iterate:* go step by step rather than one-shot.
5. **Keep best guess honest.** Best guess mode is allowed. When you use it, label every inferred detail inline and end with **Assumptions to Validate**. A best guess is a starting point to test, never a finding.

For people working in a chat tool without this skill, the Play's copy-paste prompts are in prompts/ (uploaded reference: `07-prompts.md`, section `ps-stakeholder-alignment / Companion / README.md`).

##### Guided Mode

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

#### Application

Use template.md (uploaded reference: `02-context.md`, section `ps-stakeholder-alignment / Template`) for the full scaffold.

See the source pages from the canonical playbook in assets/ps_stakeholder_alignment_playbook_pages.pdf (source material, not included in this upload kit).

##### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in prompts/01-pressure-test-stakeholder-map.md (uploaded reference: `07-prompts.md`, section `ps-stakeholder-alignment / Companion / 01-pressure-test-stakeholder-map.md`) one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

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

#### Examples

See examples/sample.md (uploaded reference: `02-context.md`, section `ps-stakeholder-alignment / Examples`).

The example set includes:

- a strong stakeholder map (complete, balanced, with actionable engagement strategies)
- a weak version (supporters only, vague strategies, empty risks)
- a drift bug example (customers listed as stakeholders)

#### Common Pitfalls

##### Pitfall 1: Listing Only Supporters

**Symptom:** The map contains five people, all in "manage closely," all listed as Supportive.

**Consequence:** The first skeptic who surfaces during a key decision is a surprise. The team has no strategy for them.

**Fix:** Before closing the map, ask explicitly: who might push back? Who was not consulted on similar initiatives? Add them.

##### Pitfall 2: Confusing Stakeholders with Customers

**Symptom:** Truck drivers, field technicians, or end users appear in the stakeholder table because they are "affected by" the initiative.

**Consequence:** The PM spends time managing internal engagement with people who actually need product discovery and empathy work.

**Fix:** Customers who use the product in the field belong in the persona play (ps-proto-persona), not here. The stakeholder map covers people who affect the initiative organizationally. Keep these lists separate.

##### Pitfall 3: Equating Influence with Seniority

**Symptom:** A VP is rated High Influence for every initiative because of their title. A junior engineer who owns the deployment process is rated Low Influence.

**Consequence:** The engagement strategy misses the people who actually control the outcome.

**Fix:** Rate influence based on actual power over this specific initiative. Ask: can this person approve, block, accelerate, or veto the work? That is influence. Title alone is not.

##### Pitfall 4: Treating Interest and Influence as Binary

**Symptom:** Every stakeholder is either High or Low. Nobody is Medium.

**Consequence:** Too many stakeholders end up in "manage closely," diluting attention.

**Fix:** Use Medium deliberately. Reserve High for stakeholders with genuine power or deep engagement with this initiative specifically.

##### Pitfall 5: Building the Map Once and Never Revisiting

**Symptom:** The map is filled out during the Context phase and never opened again.

**Consequence:** Relationships that shift during discovery, framing, or launch go untracked. The team is blindsided.

**Fix:** Revisit the map at each major phase boundary. Note what changed and why.

##### Pitfall 6: Assigning Everyone to "Manage Closely"

**Symptom:** All stakeholders are rated High Influence and High Interest.

**Consequence:** The PM tries to manage every stakeholder at the same depth and exhausts themselves. Nobody is getting the right level of attention.

**Fix:** Force distribution. Reserve "manage closely" for the two to four stakeholders who genuinely require it. Everyone else gets a lighter strategy.

##### Pitfall 7: Writing Engagement Strategies as Communication Schedules

**Symptom:** Every strategy reads as a cadence: "monthly update email," "weekly Slack message," "invite to demo." No strategy specifies what the stakeholder has input on.

**Consequence:** The PM manages the cadence but not the relationship. Stakeholders in "manage closely" who are never brought into actual trade-off discussions will feel sidelined and surface objections at the wrong moment.

**Fix:** For every "manage closely" and "keep satisfied" stakeholder, specify at least one type of decision they will be consulted on - not just a communication format. Example: "Involve in go/no-go discussion before framing is complete" is an engagement strategy. "Weekly update email" is not.

##### Pitfall 8: AI Places Stakeholders It Has Never Met

**Symptom:** The PM pastes ten names and titles and asks the agent to place them on the power/interest grid. The grid comes back filled in.

**Consequence:** Placements rest on job titles, not on how these people actually decide. The PM manages the wrong relationships.

**Fix:** The PM places each stakeholder from what they have observed. The skill asks for the evidence behind each placement and names roles the PM may have missed.

#### References

##### Skill Files

- template.md (uploaded reference: `02-context.md`, section `ps-stakeholder-alignment / Template`) - working scaffold
- prompts/ (uploaded reference: `07-prompts.md`, section `ps-stakeholder-alignment / Companion / README.md`) - copy-paste prompt for chat-based AI tools (authored for this library; the deck has no AI page for this Play)
- examples/sample.md (uploaded reference: `02-context.md`, section `ps-stakeholder-alignment / Examples`) - strong, weak, and drift-bug examples

##### Related Skills



##### Source Material

- Source: assets/ps_stakeholder_alignment_playbook_pages.pdf (source material, not included in this upload kit)
- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 8-10: Template 02 of 24 there. No AI page for this Play; the prompts are authored for this library. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).
- Template: template.md (uploaded reference: `02-context.md`, section `ps-stakeholder-alignment / Template`)
- Examples: examples/sample.md (uploaded reference: `02-context.md`, section `ps-stakeholder-alignment / Examples`)
- Budget data: [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)

##### Adjacent Skills

- **ps-outcome-strategy-discussion** - identifies who to have the guided discussion with; the stakeholder map informs that list
- **ps-empathy-interviews** - the stakeholder map helps identify who to recruit for interviews and who to brief before fieldwork begins
- **ps-proto-persona** - the destination for customers who should not be in the stakeholder map

### ps-stakeholder-alignment / Template

### ps-stakeholder-alignment Template

Use this template to build a **Productside-style stakeholder map** before discovery begins.

If some stakeholders are not yet identified, note that in the Risks and Gaps section rather than leaving the table sparse. A complete map with unknowns flagged is more useful than a partial map that looks tidy.

#### When to Use This

Use this during the Context phase, before empathy interviews or discovery work begins. The stakeholder map tells you who to involve, who to brief, and who to watch.

#### Template

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

#### Usage Guidance

- Build this map before empathy interviews begin.
- Rate influence based on actual power over this initiative, not title alone.
- Keep stakeholders and customers separate. Customers who use the product belong in ps-proto-persona.
- Revisit this map at each major phase boundary (after framing, after discovery, before launch).
- A map with no skeptics or blockers should be treated as incomplete, not as good news.

### ps-stakeholder-alignment / Examples

### ps-stakeholder-alignment Examples

All examples use a fictionalized scenario: a PM at a mid-size food distribution company building a **route optimization platform** for their logistics operations team.

---

#### Example 1: Strong Stakeholder Map

This example shows a complete, balanced map with actionable engagement strategies and a meaningful risks section.

```markdown
# Stakeholder Alignment

## Context

- Initiative / product: Route Optimization Platform
- PM: Jordan Rivera
- Date: March 2026

---

## Stakeholder Table

| Name | Role / Team | Interest in This Initiative | Influence | Sentiment |
|---|---|---|---|---|
| Marcus Chen | VP Operations | Owns the cost and service KPIs this platform affects | High | Supportive |
| Linda Osei | Director of Logistics | Day-to-day owner of route planning and dispatcher teams | High | Supportive |
| Priya Mehta | IT Infrastructure Lead | Responsible for systems the platform must integrate with | High | Skeptical |
| David Russo | Finance Director | Controls capital budget and must approve tool spend over $50K | High | Neutral |
| Sandra Kowalski | Legal / Compliance | Reviewing data sharing terms with the carrier API provider | Medium | Unknown |
| Tomas Vega | Regional Warehouse Manager | Manages the sites piloting the first rollout | Medium | Supportive |
| Aisha Nkrumah | Customer Success Lead | Escalates customer complaints when delivery windows are missed | Medium | Neutral |
| Ray Park | Head of Sales | Sells delivery reliability as a competitive differentiator | Low | Supportive |
| Felix Olawale | Carrier Relations Manager | Manages contracts with the carriers whose data feeds the platform | High | Skeptical |

---

## Interest / Influence Matrix

### Manage Closely (High Influence, High Interest)
Marcus Chen, Linda Osei, Priya Mehta, Felix Olawale
- Engagement: Weekly sync with Linda and Priya for operational and technical alignment; biweekly executive brief with Marcus; dedicated working session with Felix to address carrier data concerns before pilot begins

### Keep Satisfied (High Influence, Low Interest)
David Russo
- Engagement: Monthly one-page financial summary covering projected savings, spend to date, and risk to budget; flagged immediately when scope or timeline changes affect approved spend

### Keep Informed (Low Influence, High Interest)
Sandra Kowalski, Tomas Vega, Aisha Nkrumah
- Engagement: Biweekly written update shared via email covering progress, open decisions, and pilot schedule; Sandra gets a separate heads-up on any change to carrier data handling; Tomas and Aisha invited to pilot demos

### Monitor (Low Influence, Low Interest)
Ray Park
- Engagement: Quarterly update on release milestones; notified when the platform reaches GA so Sales can update messaging

---

## Risks and Gaps

### Missing stakeholders
IT Security has not been identified yet. Any platform ingesting real-time carrier GPS and routing data will require a security review. Need to identify the right contact before vendor contracts are signed.

### Potential blockers
Felix Olawale (Carrier Relations) is skeptical because a previous integration project damaged a key carrier relationship. If he is not involved early in the API design decisions, he may raise concerns at the contract stage that delay the pilot by a quarter.

Priya Mehta (IT Infrastructure) has flagged concerns about the platform's dependency on a cloud infrastructure configuration her team does not currently support. If that is not resolved before development begins, the pilot environment may not be ready in time.

### Political dynamics
Marcus Chen and David Russo have a documented history of disagreement over technology investment. Marcus has pushed for faster modernization; David has blocked two prior initiatives on ROI grounds. Any proposal to Marcus should be framed with David's financial framing in mind, not just operational benefit.
```

**Why this works**

- the table includes skeptics (Priya Mehta, Felix Olawale) alongside supporters, which makes the map useful when friction surfaces
- influence ratings reflect actual power over this initiative, not just title (Felix, a manager-level role, is correctly rated High because of carrier relationship control)
- Finance is represented even though this is primarily an operations initiative
- engagement strategies are specific: cadence, format, and content are named for each quadrant
- the risks section names a concrete blocker with a mechanism (Felix's concern about a prior integration) and a specific consequence (a quarter delay to pilot)
- IT Security is flagged as a gap before it becomes a problem

---

#### Example 2: Weak Stakeholder Map

Same initiative, same company - but the map is incomplete and the engagement strategies are too vague to act on.

```markdown
# Stakeholder Alignment

## Context

- Initiative / product: Route Optimization Platform
- PM: Jordan Rivera
- Date: March 2026

---

## Stakeholder Table

| Name | Role / Team | Interest in This Initiative | Influence | Sentiment |
|---|---|---|---|---|
| Marcus Chen | VP Operations | Interested in the project | High | Supportive |
| Linda Osei | Director of Logistics | Key stakeholder | High | Supportive |
| Tomas Vega | Regional Manager | Involved in pilot | High | Supportive |

---

## Interest / Influence Matrix

### Manage Closely (High Influence, High Interest)
Marcus Chen, Linda Osei, Tomas Vega
- Engagement: Keep them updated

### Keep Satisfied (High Influence, Low Interest)
[None identified]

### Keep Informed (Low Influence, High Interest)
[None identified]

### Monitor (Low Influence, Low Interest)
[None identified]

---

## Risks and Gaps

[None identified]
```

**Why this fails**

- only three stakeholders, all listed as Supportive - no skeptics, no blockers, no Finance or Legal
- Tomas Vega is rated High Influence, which inflates the "manage closely" quadrant without justification; his actual influence is Medium
- interest descriptions are placeholders ("interested in the project," "key stakeholder") with no content
- "Keep them updated" is not an engagement strategy - it has no cadence, format, or content
- the risks section is empty, which means the PM will be surprised by Felix Olawale and IT Security when they surface later
- three quadrants are completely empty, which signals the ratings have not been calibrated against the full stakeholder landscape

---

#### Example 3: Drift Bug - Customers Listed as Stakeholders

This is a common misuse. The PM has included the end users of the route optimization platform - the people who will actually use the product in the field - inside the stakeholder table.

```markdown
## Stakeholder Table

| Name | Role / Team | Interest in This Initiative | Influence | Sentiment |
|---|---|---|---|---|
| Marcus Chen | VP Operations | Owns the KPIs this platform affects | High | Supportive |
| Linda Osei | Director of Logistics | Day-to-day owner of route planning | High | Supportive |
| Route dispatchers | Operations / Dispatch | Will use the platform daily | Medium | Unknown |
| Truck drivers | Field / Delivery | Will receive optimized routes from the system | Low | Unknown |
```

**Why this is a drift bug**

Route dispatchers and truck drivers are the customers the product serves in the field. They experience the problem the platform is solving. They need product discovery and empathy work - interviews, observations, prototype feedback.

They are not stakeholders in the organizational sense. They cannot greenlight or block the initiative. They do not need to be briefed on budget decisions or release timelines. Including them in the stakeholder table creates confusion about who needs organizational engagement vs. who needs discovery work.

The correct destination for route dispatchers and truck drivers is the persona play (ps-proto-persona), where their jobs-to-be-done, pains, and goals can be captured properly.

The stakeholder map covers the people inside the organization who affect whether the initiative succeeds. The persona play covers the people in the field who the product serves. Keep these lists separate.

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

**Section Two (Deliver phase — reuses the Outcome Tree design; the baseline deck labels this occurrence "Template 3 of 24"; the B2B work-in-progress deck numbers it Template 23):** Update the tree after discovery. Revise product outcomes that discovery validated or invalidated. Fill in metrics that were TBD. Add baselines and targets now that real data exists. Record actuals against planned targets. Retire outcomes that turned out to be wrong.

The trigger for Section Two is evidence: completed empathy interviews, validated hypotheses, experiment results, or post-launch measurement data. If the PM has not done discovery work since building Section One, Section Two will just reproduce the same guesses with more confidence. That is not useful.

##### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **critic of the outcome tree the PM drafted**, in both sections. In Section One it checks that the business outcome is measurable, that product outcomes describe what customers achieve, and that metrics are in the right place. In Section Two it asks what discovery evidence supports or contradicts each product outcome. The outcomes, targets, and the verdict on each stay the PM's.

- **Use it when:** the PM has drafted Section One, or has discovery evidence to review in Section Two.
- **Avoid it when:** the request is to invent the business outcome, or to fill in baselines, targets, or actuals without data.
- **Return:** each outcome and metric checked for format and placement, the causal chain from product outcomes to business outcome tested, and in Section Two, each product outcome matched to evidence for the PM to keep, revise, or retire.

##### Working With AI

The Productside Playbook sets one rule for every AI-assisted Play: **the Product Manager does the thinking, and AI pressure-tests it.** In this skill, you are the AI. Hold yourself to these rules:

1. **Pressure-test before you produce.** When the user brings a draft, critique it against the Play's formats and criteria first. Point at the specific words that fail and ask the user to fix them. Offer rewrites only after the critique, as options to accept, adapt, or reject.
2. **Never stand in for the customer.** Do not present jobs, quotes, needs, or pains you generated as research, and do not answer as the persona as if your answers were evidence. Anything you draft about customers is a hypothesis, labeled as one, to validate with real people. Role-play is allowed only as rehearsal where the Play calls for it, labeled as practice, and nothing from it goes into findings.
3. **Never stand in for the team's judgment.** Do not put unsourced figures into the artifact, and do not make calls the team should own. A number without a source is a blank to fill, so mark it that way.
4. **Work the five habits.** *Context:* ask for the persona, market, outcome, and constraints when they are missing. *Guide:* offer competing views and welcome pushback. *Enforce:* work inside the Play's template, not around it. *Outcome:* tie the work to the decision it supports. *Iterate:* go step by step rather than one-shot.
5. **Keep best guess honest.** Best guess mode is allowed. When you use it, label every inferred detail inline and end with **Assumptions to Validate**. A best guess is a starting point to test, never a finding.

For people working in a chat tool without this skill, the Play's copy-paste prompts are in prompts/ (uploaded reference: `07-prompts.md`, section `ps-outcome-tree / Companion / README.md`).

##### Guided Mode

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

#### Application

Use template.md (uploaded reference: `02-context.md`, section `ps-outcome-tree / Template`) for the full scaffold.

See the original three-page playbook source in assets/ps_outcome_tree_playbook_pages.pdf (source material, not included in this upload kit).

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

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in prompts/01-check-section-one.md (uploaded reference: `07-prompts.md`, section `ps-outcome-tree / Companion / 01-check-section-one.md`) one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

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

#### Examples

See examples/sample.md (uploaded reference: `02-context.md`, section `ps-outcome-tree / Examples`).

The example set includes:

- a strong Outcome Tree artifact for a sustainable agriculture platform
- a weak, vague version of the same scenario
- a drift-bug example showing product outcomes confused with business outcomes and internal tasks
- commentary on why the weak versions fail

#### Common Pitfalls

##### Pitfall 1: Confusing Product Outcomes with Business Outcomes

**Symptom:** Product outcomes read like organizational goals: "Increase market share by 15%" or "Reduce operational costs by $2M."

**Consequence:** The tree conflates two levels. The product team cannot act on business outcomes directly, and the causal link between product work and business results disappears.

**Fix:** Ask: who experiences this outcome? If the answer is "the business" or "leadership," it is a business outcome. If the answer is "the customer using the product," it is a product outcome. Keep them in their respective boxes.

##### Pitfall 2: Writing Feature Descriptions as Product Outcomes

**Symptom:** "The product provides a self-service portal" or "Automated notifications for pending tasks."

**Consequence:** The tree describes what the product does instead of what the customer achieves. The team optimizes for shipping features rather than delivering outcomes.

**Fix:** Strip out the product. Ask: what is different for the customer when this feature works? "New employees complete required onboarding steps without waiting for HR availability" is a product outcome. "Self-service onboarding portal" is a feature.

##### Pitfall 3: Setting More Than 5 Product Objectives

**Symptom:** The tree lists 7, 8, or 10 product outcomes.

**Consequence:** The team cannot focus. Every sprint touches a different outcome. Progress is diffuse and unmeasurable.

**Fix:** The playbook limit is 2-5 product outcomes per tree. If you have more, either consolidate related outcomes or split into multiple trees for different business outcomes.

##### Pitfall 4: Making Business Outcomes Too Vague

**Symptom:** "Grow the business," "Improve customer satisfaction," "Be more innovative."

**Consequence:** The business outcome cannot be measured, so the entire tree has no anchor. The team cannot tell if the product is contributing to business success.

**Fix:** Add a direction, a metric, and a target. "Improve customer satisfaction" becomes "Increase Net Promoter Score from 32 to 50 within 12 months." If the user cannot specify a target, at least specify a direction and a metric.

##### Pitfall 5: Defaulting to Tech-Role Language in Product Outcomes

**Symptom:** "Data engineers can build pipelines 40% faster" or "Platform architects can deploy microservices with fewer configuration errors."

**Consequence:** The product outcomes reflect LLM training bias toward technical roles, not the actual customer population.

**Fix:** Before writing product outcomes, confirm who the product actually serves. Most products serve people whose primary job is not writing code. An HR platform serves HR managers and employees, not data engineers.

##### Pitfall 6: Treating This as a One-Time Exercise

**Symptom:** The team builds the Outcome Tree once, files it away, and never revisits it.

**Consequence:** The tree becomes stale. Business outcomes shift, product outcomes are achieved or abandoned, and metrics change. The artifact stops reflecting reality.

**Fix:** The playbook says to revisit regularly and bring it to team meetings. Schedule periodic reviews and update the tree as strategy evolves.

##### Pitfall 7: Skipping Product Success Metrics

**Symptom:** Product outcomes are defined but their success metrics are left permanently blank.

**Consequence:** The team cannot tell if an outcome is being achieved. Product outcomes without metrics are aspirational statements, not actionable targets.

**Fix:** Even if exact metrics are not known yet, define the type of measurement. "TBD" is acceptable as a starting point, but flag it as a gap that must be resolved before the next planning cycle.

##### Pitfall 8: Confusing Product Health Metrics with Product Success Metrics

**Symptom:** "99.9% uptime" listed as a product success metric for an outcome like "HR managers spend less time on tactical tasks."

**Consequence:** The team conflates operational health (is the product working?) with outcome achievement (is the product delivering value?). A product can have perfect uptime and still fail to move outcomes.

**Fix:** Keep them in separate sections. Product health metrics (uptime, latency, error rates) go in the health section. Product success metrics (task completion rates, time savings, adoption of key workflows) go next to their respective outcomes.

##### Pitfall 9: AI Writes the Tree

**Symptom:** The PM asks for an outcome tree for their product and gets a complete one: business outcome, five product outcomes, metrics, targets.

**Consequence:** The targets have no baseline, and the outcomes are the model's view of the business. The tree looks like strategy and is a guess.

**Fix:** The PM drafts; the skill checks each outcome and metric. Targets and baselines come from the PM's data or are marked to be set.

#### References

##### Skill Files

- template.md (uploaded reference: `02-context.md`, section `ps-outcome-tree / Template`) - working scaffold
- prompts/ (uploaded reference: `07-prompts.md`, section `ps-outcome-tree / Companion / README.md`) - copy-paste prompts for chat-based AI tools (authored for this library; the deck has no AI page for this Play)
- examples/sample.md (uploaded reference: `02-context.md`, section `ps-outcome-tree / Examples`) - strong, weak, and drift-bug examples

##### Related Project Docs

- [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)
- [framework-glossary.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/framework-glossary.md)
- [skill-authoring-workflow.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/skill-authoring-workflow.md)
- [template_conversion_rules.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/template_conversion_rules.md)
- [template_conversion_usage.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/template_conversion_usage.md)

##### Related Skills

- ps-jobs-to-be-done (uploaded reference: `03-discover-investigate.md`, section `ps-jobs-to-be-done / Instructions`) - product outcomes from JTBD feed into this tree
- ps-framing-the-problem (uploaded reference: `03-discover-investigate.md`, section `ps-framing-the-problem / Instructions`) - problem statement feeds the Problem Statement box
- ps-solution-hypothesis (uploaded reference: `04-discover-define.md`, section `ps-solution-hypothesis / Instructions`) - solution summary feeds the Solution Summary box
- ps-proto-persona (uploaded reference: `03-discover-investigate.md`, section `ps-proto-persona / Instructions`) - persona work informs who the product outcomes serve

##### Source Material

- [Baseline Playbook version](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml). Full source PDF supplied separately.
- assets/ps_outcome_tree_playbook_pages.pdf (source material, not included in this upload kit)
- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 11-13 and 106-108: Template 03 and 23 of 24 there. No AI page for this Play; the prompts are authored for this library. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).
- Productside Playbook companion document (supplied separately)

### ps-outcome-tree / Template

### Outcome Tree - Section One

#### When to Use This

Use this template during the **Context** phase to connect your product work to a measurable business goal. This is foundational: until you can articulate what the business is trying to achieve and how the product supports that, prioritization and roadmap decisions lack an anchor.

Revisit this artifact regularly. Bring it to team meetings. Use it to share success metrics and check assumptions with the team.

#### Template

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

#### Usage Guidance

##### Filling the Template

1. Start with **Product Context** to anchor who this is for.
2. Add the **Problem Statement** if one exists from previous work.
3. Define the **Business Outcome** first. Everything else flows from it.
4. Add **Business Success Metrics** (even if some are TBD).
5. Define **Product Outcomes** (2-5). These describe what the customer achieves.
6. Add **Product Success Metrics** for each product outcome.
7. Add **Product Health Metrics** for the product itself.
8. Add the **Solution Summary** if one exists.
9. Walk through the **Causal Chain Review** to verify connections.

##### How Many Product Outcomes

The playbook sets a hard limit of 2-5. Default to 2-3 for a focused product. Use 4-5 only when the product serves multiple distinct user roles or the business outcome is broad enough to require multiple paths.

If you find yourself writing more than 5, either:

- consolidate related outcomes into a single, broader outcome
- split into multiple trees, each with a different business outcome

##### What Goes in the Product Outcome Statements

Write each product outcome as a statement about the customer's improved state. Use role names (e.g., "HR managers," "field technicians," "compliance officers"), not individual persona names (e.g., "Maya," "Carlos").

Do not use:

- feature descriptions ("The product provides...")
- implementation details ("Automated workflow for...")
- business metrics ("Revenue increases by...")
- internal team goals ("The engineering team ships...")

##### Connecting to Other Skills

- **Upstream:** ps-framing-the-problem provides the Problem Statement; ps-solution-hypothesis provides the Solution Summary
- **Parallel:** ps-jobs-to-be-done produces product outcomes that may feed into this tree
- **Downstream:** Section Two (this skill, Modality 2) updates the tree after discovery and define work

---

#### Section Two: Updating the Outcome Tree After Discovery

Use this scaffold when returning to the Outcome Tree after completing discovery work. This is not a new artifact. It is an update pass on the Section One artifact above.

##### Prerequisites

Before running Section Two, the PM should have completed at least one of:

- empathy interviews (ps-empathy-interviews)
- solution hypothesis validation (ps-solution-hypothesis)
- lo-fi experimentation (ps-lofi-experimentation)
- market or customer research
- post-launch measurement data

##### Update Scaffold

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

##### When to Run Section Two

Section Two adds value when the PM has new evidence that changes the tree. Common triggers:

- Completed empathy interviews revealed different customer priorities than assumed
- Solution hypothesis testing invalidated an assumed product outcome
- Market research shifted the competitive context
- Post-launch data shows actual vs. planned variance
- Business strategy changed, altering the business outcome or its metrics

Section Two does not add value when:

- The PM has not done discovery work since Section One (the tree will not change)
- The only change is cosmetic rewording (edit the Section One artifact directly)

##### Capacity Reference

See [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml) for the exact word and character budgets per field.

| Field | Word Budget | Guidance |
|-------|-------------|----------|
| Business Outcome | ~15-25 | Specific, measurable business goal |
| Business Success Metric | ~10-15 | Measurable indicator with units |
| Product Outcome | ~15-20 | Customer-centered value statement |
| Product Success Metric | ~10-15 | Leading indicator tied to an outcome |
| Product Health Metric | ~5-10 | Operational metric with target |

### ps-outcome-tree / Examples

### Outcome Tree - Section One: Examples

#### Example 1: Strong Productside-Style Outcome Tree

Scenario: A sustainable agriculture technology company building a precision irrigation platform for regional farm operations managers and agronomists.

```markdown
# Outcome Tree - Section One

## Product Context

- Product or service: AquaPrecision - precision irrigation management platform
- Business or organization: AgriTech Solutions (mid-market agricultural technology provider)
- Primary customer/user role: Regional Farm Operations Manager
- Buyer (if different): VP of Agricultural Operations

## Problem Statement (from Framing the Problem play, if available)

> Regional farm operations managers currently rely on manual field inspections and weather forecasts to schedule irrigation, resulting in 25-35% water waste and inconsistent crop yields across managed acreage. They need a way to make irrigation decisions based on real-time soil and weather data so they can reduce water usage while maintaining or improving yield consistency.

## 1. Business Outcome

| Business Outcome |
|------------------|
| Reduce water consumption across managed farm operations by 20% within 18 months while maintaining crop yield targets |

## 2. Business Success Metrics

| # | Business Success Metric | Status |
|---|------------------------|--------|
| 1 | Total water usage per acre across all managed properties (gallons/acre/season) | Defined |
| 2 | Crop yield variance from target across managed properties (percentage) | Defined |
| 3 | Irrigation-related operational cost per acre (dollars/acre/season) | TBD |

## 3. Product Outcomes (2-5)

| # | Product Outcome |
|---|----------------|
| 1 | Regional farm operations managers make irrigation scheduling decisions based on current field conditions rather than manual inspections |
| 2 | Agronomists identify water stress across multiple fields before visible crop damage occurs |
| 3 | Field technicians complete irrigation system adjustments in a single site visit instead of multiple trips |

## 4. Product Success Metrics

| # | Product Success Metric | Related Outcome | Status |
|---|----------------------|-----------------|--------|
| 1 | Percentage of irrigation decisions made using platform data vs. manual inspection | 1 | TBD |
| 2 | Average time from water stress onset to agronomist awareness (hours) | 2 | TBD |
| 3 | Average number of site visits per irrigation adjustment cycle | 3 | Defined |
| 4 | Percentage of managed acres with active sensor coverage | 1, 2 | Defined |

## 5. Product Health Metrics

| # | Product Health Metric | Target |
|---|---------------------|--------|
| 1 | Sensor data ingestion uptime | 99.5% |
| 2 | Average time from sensor reading to dashboard update | < 15 minutes |
| 3 | Weekly active users as percentage of licensed accounts | > 70% |

## Solution Summary (from Solution Hypothesis Statement play, if available)

> Not yet defined

## Causal Chain Review

- Product Outcome 1 (data-driven irrigation decisions) directly reduces water waste by replacing imprecise manual scheduling.
- Product Outcome 2 (early stress detection) prevents yield loss that would otherwise offset water savings.
- Product Outcome 3 (single-visit adjustments) reduces operational cost per acre, supporting the cost metric.
- Gap: No product outcome addresses seasonal planning or long-term water budgeting. This may be needed if the 20% reduction target requires structural changes, not just better daily decisions.
```

##### Why This Works

- **Clear causal chain.** Each product outcome connects logically to the business outcome. Reducing water consumption requires better irrigation decisions (Outcome 1), preventing crop damage that undermines savings (Outcome 2), and reducing operational cost of the changes (Outcome 3).
- **Business outcome is specific and measurable.** "Reduce water consumption by 20% within 18 months while maintaining yield targets" has a direction, a metric, a target, and a timeframe.
- **Product outcomes are customer-centered.** Each describes what a specific role achieves, not what the product does. "Regional farm operations managers make irrigation scheduling decisions based on current field conditions" is about the manager's changed behavior, not a product feature.
- **Role names, not persona names.** "Regional farm operations managers," "agronomists," and "field technicians" are roles. No individual names like "Carlos" or "Priya."
- **Metrics are distinguished by type.** Business success metrics (water per acre, yield variance) are separate from product success metrics (decisions using platform data, time to awareness) and product health metrics (uptime, latency, adoption). No confusion between levels.
- **Honest about gaps.** The causal chain review flags a gap in seasonal planning. TBD metrics are marked as such rather than invented.

---

#### Example 2: Weak Generic Outcome Tree

Same scenario, written poorly.

```markdown
# Outcome Tree - Section One

## Product Context

- Product or service: Smart irrigation system
- Business or organization: AgriTech company
- Primary customer/user role: Farmer
- Buyer (if different): Same

## 1. Business Outcome

| Business Outcome |
|------------------|
| Grow the business and improve sustainability |

## 2. Business Success Metrics

| # | Business Success Metric | Status |
|---|------------------------|--------|
| 1 | Revenue growth | TBD |
| 2 | Customer satisfaction | TBD |

## 3. Product Outcomes (2-5)

| # | Product Outcome |
|---|----------------|
| 1 | Better water management |
| 2 | Improved crop yields |
| 3 | Reduced costs |
| 4 | Increased efficiency |
| 5 | Better data visibility |
| 6 | Faster decision making |
| 7 | Improved sustainability metrics |

## 4. Product Success Metrics

| # | Product Success Metric | Related Outcome | Status |
|---|----------------------|-----------------|--------|
| 1 | User satisfaction | All | TBD |

## 5. Product Health Metrics

| # | Product Health Metric | Target |
|---|---------------------|--------|
| 1 | System uptime | High |
```

##### Why This Fails

- **Business outcome is unmeasurable.** "Grow the business and improve sustainability" has no direction, no metric, and no target. Nobody can tell if it happened.
- **Product outcomes are vague abstractions.** "Better water management" and "increased efficiency" could mean anything. They do not describe a customer's changed state.
- **Too many product outcomes.** Seven outcomes exceeds the 2-5 limit. The team cannot focus.
- **No customer roles.** "Farmer" is too generic. Which farmer? The operations manager, the agronomist, the field technician? Different roles have different outcomes.
- **Metrics are absent or generic.** "User satisfaction" as a single metric for all outcomes provides no signal. "High" is not a target.
- **No causal chain.** There is no visible logic connecting product outcomes to the business outcome. The tree is a wish list, not a strategy artifact.

---

#### Example 3: Drift Bug - Product Outcomes Confused with Business Outcomes and Internal Tasks

```markdown
## 3. Product Outcomes (2-5)

| # | Product Outcome |
|---|----------------|
| 1 | Increase market share in the precision agriculture segment by 15% |
| 2 | Achieve $5M in annual recurring revenue from irrigation management subscriptions |
| 3 | Ship the Q3 release with sensor integration on time |
| 4 | Reduce customer churn rate to below 8% annually |
| 5 | Complete SOC 2 compliance certification before fiscal year end |
```

##### Why This Is Wrong

Every entry confuses the level of the tree it belongs in:

- **"Increase market share by 15%"** is a business outcome, not a product outcome. Market share is a business-level metric. The product team cannot directly control market share. This belongs in the Business Outcome box, not in the Product Outcomes section.
- **"Achieve $5M in ARR"** is a business financial target. It tells you nothing about what the customer achieves. Revenue is a consequence of delivering product outcomes, not a product outcome itself.
- **"Ship the Q3 release on time"** is an internal team task. It describes what the engineering team does, not what the customer gets. Shipping on time may be necessary, but it is not a product outcome.
- **"Reduce customer churn to below 8%"** is a business retention metric. Churn rate is a lagging business indicator. The product outcome would describe what changed for the customer that made them stay.
- **"Complete SOC 2 compliance certification"** is an internal operational task. It may be a prerequisite for selling to certain customers, but it is not something the customer achieves.

**Fix:** For each entry, ask: "Who experiences this? Is it the customer using the product, or is it the business/team?" Then rewrite:

- "Increase market share by 15%" becomes the Business Outcome (or a business metric)
- "$5M ARR" becomes a Business Success Metric
- "Ship Q3 release" gets removed entirely (this is a project milestone, not an outcome at any level)
- "Reduce churn to below 8%" becomes a Business Success Metric
- "SOC 2 certification" gets removed or noted as a prerequisite, not an outcome

The actual product outcomes would describe what farm operations managers, agronomists, or field technicians achieve differently because the product exists.

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

The Productside Playbook sets one rule for every AI-assisted Play: **the Product Manager does the thinking, and AI pressure-tests it.** In this skill, you are the AI. Hold yourself to these rules:

1. **Pressure-test before you produce.** When the user brings a draft, critique it against the Play's formats and criteria first. Point at the specific words that fail and ask the user to fix them. Offer rewrites only after the critique, as options to accept, adapt, or reject.
2. **Never stand in for the customer.** Do not present jobs, quotes, needs, or pains you generated as research, and do not answer as the persona as if your answers were evidence. Anything you draft about customers is a hypothesis, labeled as one, to validate with real people. Role-play is allowed only as rehearsal where the Play calls for it, labeled as practice, and nothing from it goes into findings.
3. **Never stand in for the team's judgment.** Do not put unsourced figures into the artifact, and do not make calls the team should own. A number without a source is a blank to fill, so mark it that way.
4. **Work the five habits.** *Context:* ask for the persona, market, outcome, and constraints when they are missing. *Guide:* offer competing views and welcome pushback. *Enforce:* work inside the Play's template, not around it. *Outcome:* tie the work to the decision it supports. *Iterate:* go step by step rather than one-shot.
5. **Keep best guess honest.** Best guess mode is allowed. When you use it, label every inferred detail inline and end with **Assumptions to Validate**. A best guess is a starting point to test, never a finding.

For people working in a chat tool without this skill, the Play's copy-paste prompts are in prompts/ (uploaded reference: `07-prompts.md`, section `ps-market-selection-sizing / Companion / README.md`).

##### Guided Mode

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

#### Application

Use template.md (uploaded reference: `02-context.md`, section `ps-market-selection-sizing / Template`) for the scaffold.

See the source play pages in assets/ps_market_selection_sizing_playbook_pages.pdf (source material, not included in this upload kit).

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

#### Examples

See examples/sample.md (uploaded reference: `02-context.md`, section `ps-market-selection-sizing / Examples`).

The example set includes:

- a strong market analysis for municipal water-utility pump-station monitoring, with sourced inputs, cut logic, and ranges (figures are illustrative)
- a weak version in the same domain: confident unsourced numbers, demographic segments, and a generic PESTEL
- a drift-bug example, "the free five percent," showing an SOM built on an assumed share

#### Common Pitfalls

##### Pitfall 1: AI Invents the Market Size

**Symptom:** The TAM box says "$4.2B, growing 9% annually," with no source, or with a source no one can find.

**Consequence:** A guess dressed as a finding goes into a leadership deck. The first person who asks "where did this come from?" ends the PM's credibility on the topic.

**Fix:** Every number carries a source ID or `[TO SOURCE]`. Never fill a blank with a plausible figure.

##### Pitfall 2: Competitor Numbers No One Can Know

**Symptom:** "Competitor X has 30% share and $80M in revenue in this segment," for a private company with no disclosures.

**Consequence:** The SOM rests on invented competitive data.

**Fix:** Use only competitive facts a filing, a report, or a named source states. Otherwise describe the competitor qualitatively and mark the gap.

##### Pitfall 3: A Generic PESTEL

**Symptom:** "Political: regulation is increasing. Technological: AI is changing everything. Economic: inflation."

**Consequence:** The analysis fits every market and informs none. The team learns nothing about this market's forces.

**Fix:** One specific entry per force, tied to this market, with a source, or an honest open question.

##### Pitfall 4: Segments for Show

**Symptom:** Segments are "Small, Medium, Enterprise" or "Healthcare, Finance, Retail," with tidy cuts that would fit any market.

**Consequence:** Customers inside a segment don't share needs, so jobs, personas, and positioning built on the segment don't hold.

**Fix:** Define segments by shared needs, goals, and behaviors, and state the cut logic so it can be tested. Use size or industry only as a boundary.

##### Pitfall 5: Segments With No People in Them

**Symptom:** Each segment has a name and a description, but no one in it: no user, buyer, or influencer.

**Consequence:** The next plays (Jobs-to-Be-Done, Personas) have no one to write about. The Playbook names this trap: segments with no real persona.

**Fix:** Name the users, buyers, and influencers in every segment. Think broadly.

##### Pitfall 6: The Market at the Wrong Altitude

**Symptom:** The market is "software" or "healthcare," or it is one customer's workflow.

**Consequence:** Too broad can't be analyzed. Too narrow can't be sized or segmented.

**Fix:** Run the three altitude questions. Center the definition on who the product is for and the benefit it provides.

##### Pitfall 7: The Free Five Percent

**Symptom:** "If we capture just 5% of the SAM..." with no reason why 5%.

**Consequence:** The SOM is a wish. It ignores competition, which the Playbook says SOM must consider.

**Fix:** State the share basis: the alternatives customers use, how many the team can reach, a win-rate assumption, and delivery capacity over a named horizon. If there is no basis yet, show SOM as a conditional formula and say what would anchor it.

##### Pitfall 8: Mixed Counting Units

**Symptom:** TAM counts companies, SAM counts sites, SOM multiplies employees by a per-seat price.

**Consequence:** The math is wrong in a way that looks right. SOM can exceed SAM without anyone noticing.

**Fix:** Name one counting unit, convert explicitly when needed, and check SOM ≤ SAM ≤ TAM.

##### Pitfall 9: One Source, One Number

**Symptom:** A single search result becomes the TAM, presented to the dollar.

**Consequence:** False precision. The conversation becomes a defense of the number instead of a discussion of risk.

**Fix:** Triangulate with three approaches and present ranges.

##### Pitfall 10: Professional-Looking Logic, Never Tested

**Symptom:** A polished analysis with clean formulas and confident segment names that no one has checked against a customer or an expert.

**Consequence:** The structure is mistaken for rigor, and the team commits to a segment on untested logic.

**Fix:** Tag AI-suggested cut logic for validation, rank the open questions, and revisit the analysis as discovery produces evidence.

#### References

##### Skill Files

- template.md (uploaded reference: `02-context.md`, section `ps-market-selection-sizing / Template`) - market analysis scaffold
- prompts/ (uploaded reference: `07-prompts.md`, section `ps-market-selection-sizing / Companion / README.md`) - copy-paste prompts for chat-based AI tools (4, run in order in one chat)
- examples/sample.md (uploaded reference: `02-context.md`, section `ps-market-selection-sizing / Examples`) - strong, weak, and drift-bug examples
- assets/ps_market_selection_sizing_playbook_pages.pdf (source material, not included in this upload kit) - source pages from the B2B work-in-progress deck (slides 14-18)

##### Related Skills

- ps-outcome-tree (uploaded reference: `02-context.md`, section `ps-outcome-tree / Instructions`) - Context-phase neighbor; the business outcome this market should serve
- ps-jobs-to-be-done (uploaded reference: `03-discover-investigate.md`, section `ps-jobs-to-be-done / Instructions`) - downstream; jobs for the people in the chosen segments
- ps-proto-persona (uploaded reference: `03-discover-investigate.md`, section `ps-proto-persona / Instructions`) - downstream; a persona for the center of a chosen segment
- ps-positioning-statement (uploaded reference: `04-discover-define.md`, section `ps-positioning-statement / Instructions`) - downstream; positioning for one persona in one segment

##### Related Project Docs

- [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml)
- [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)
- [skill-authoring-workflow.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/skill-authoring-workflow.md)

##### Source Material

- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 14-18: Template 04 of 24, with the AI overview on slide 16 and prompts on slide 17. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).
- assets/ps_market_selection_sizing_playbook_pages.pdf (source material, not included in this upload kit)

### ps-market-selection-sizing / Template

### Market Selection & Sizing

#### When to Use This

Use this template in the **Context** phase, before Jobs-to-Be-Done and Personas, to name the market a product serves, understand the forces acting on it, cut it into segments, and size the opportunity. It is a first pass you will revisit as you learn more.

Downstream: the segments and the people named in them feed ps-jobs-to-be-done, ps-proto-persona, ps-empathy-interviews, and ps-positioning-statement.

#### Template

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

#### Usage Guidance

- Work the three parts in order: market, then segments, then size.
- Keep entries compact. The canonical template's PESTEL cells, segment boxes, and sizing boxes are small.
- Every number needs a source the PM can check. A number without one is `[TO SOURCE]`.
- The "is it worth it" judgment stays with the PM and their team.
- Revisit this artifact as discovery produces evidence.

### ps-market-selection-sizing / Examples

### ps-market-selection-sizing Examples

All three examples use the same domain: remote monitoring for water and wastewater pump stations, sold to U.S. utilities.

**Every figure and source below is illustrative.** The numbers show the shape of the reasoning, not real market data. Do not reuse them as facts.

#### Example 1: Strong Market Analysis

Scenario: a company with an existing pump-station monitoring product (cellular sensors and alerting) is deciding which utility segments to explore next.

```markdown
# Market Selection & Sizing

## Context
- Product or product idea: Existing. Cellular sensors and alerting for unattended pump and lift stations
- Who it is for, and the benefit it provides: Utilities that run unattended pump stations; earlier warning of failures and overflows
- Decision this analysis informs: Which segment to run discovery in next quarter
- Counting unit: pump stations (priced per station per year)

## 1. Market Selection
- Market: Remote monitoring of unattended pump and lift stations for U.S. water and wastewater utilities

### PESTEL
| Force | Entry | Source or status |
|---|---|---|
| Political | State revolving-fund grants now prioritize resilience upgrades | [S1] |
| Economic | Rate caps squeeze operating budgets; capital spend is easier to fund | [S2] |
| Social | Licensed operators retiring faster than they are replaced | [S3] |
| Technological | Cellular sensors replacing legacy radio telemetry at small sites | [S4] |
| Environmental | Heavier storms overloading lift stations in some regions | OPEN QUESTION: which regions, how often? |
| Legal | Overflow reporting rules raise penalty exposure for missed alarms | [S5] |

## Total Addressable Market (TAM)
- Sized fact 1: 48,000-52,000 utilities operate at least one pump or lift station [S6]
- Sized fact 2: 3-4 stations per utility on average, across all sizes [S7]
- TAM: 145,000-210,000 pump stations

## 2. Segments

### Segment 1: Mid-size systems with stretched on-call crews
- Description: Serve 10,000-100,000 people; stations unattended; a small crew covers nights by rotation; overflow fines are a board-level worry
- Cut logic: Staffing model (rotating on-call crew, no 24/7 control room) and penalty exposure, not population alone [AI-SUGGESTED, VALIDATE THIS]
- Users: Lead operators, on-call technicians
- Buyers: Utility director, public works director
- Influencers: Consulting engineers, state regulators, city council

### Segment 2: Small rural systems with a shared circuit-rider operator
- Description: Serve under 10,000 people; one licensed operator covers several systems part-time; upgrades depend on grants
- Cut logic: One operator across multiple systems, and a grant-funded buying path [FROM YOU]
- Users: Circuit-rider operator
- Buyers: Town manager, water board chair
- Influencers: State rural water association technical assistants, grant administrators

## 3. Size the Market & Segments

### Serviceable Addressable Market (SAM)
| Segment | Counting logic (formula) | Inputs and sources | SAM (range) |
|---|---|---|---|
| 1 | systems x stations per system | 4,000-5,000 systems [S6]; 8-15 stations each [S8] | 32,000-75,000 stations |
| 2 | systems x stations per system | 20,000-25,000 systems [S6]; 1-3 stations each [S8, TO SOURCE for under-3,300] | 20,000-75,000 stations |

Triangulation: top-down from the system inventory [S6], bottom-up from 12 customer station counts [S9], and two consulting engineers' estimates [S10]. Segment 1 agrees within 20%. Segment 2's bottom-up runs low; see Open Questions.

### Serviceable Obtainable Market (SOM), annual revenue
| Segment | Share basis (competition, reach, win rate, capacity, horizon) | Units x annual price | SOM (range) |
|---|---|---|---|
| 1 | Three SCADA-bundled competitors [S11]. Reach 120-200 utilities in 24 months through two regional partners [S12]. Win rate 20-30% (assumption, from last year's pilots [S9]). | 24-60 utilities x 10 stations x $1,200-1,800 per station per year (current list price [S13]) | $0.29M-$1.08M per year at month 24 |
| 2 | No validated product fit for single-operator systems yet | Deferred until solutions are ideated | Deferred |

## Source Register
| ID | Source | Date | What it supports |
|---|---|---|---|
| S1-S13 | (Illustrative placeholders: a federal system inventory, a state grant program, an operator workforce report, regulator rules, company sales and pricing data, customer counts, and engineer interviews) | n/a | As cited above |

## Open Questions
1. Segment 2 stations per system: bottom-up suggests 1-2, not 1-3. This could halve Segment 2's SAM.
2. Win rate: two years of pilots is a thin basis. Confirm with partner pipeline data.
3. Environmental: which regions see storm-driven overloads, and is that a buying trigger?
```

**Why this works**

- **The market is named at the right altitude:** who it serves (utilities with unattended stations) and the benefit (earlier warning), narrow enough to size.
- **The PESTEL is specific.** Every entry is about this market, with a source, and the one the team couldn't source is an honest open question.
- **Segments differ by behavior, not just size.** The cut is staffing model and buying path, and each segment names real users, buyers, and influencers.
- **The sizing is a formula with a source on every input,** in one counting unit (stations), as ranges, triangulated three ways, with SOM ≤ SAM ≤ TAM.
- **The SOM share has a basis:** competitors, partner reach, a win rate traced to pilots, a horizon, and the price is the company's own list price.
- **Segment 2's SOM is deferred,** because there is no product fit to price yet. That is what the Playbook asks for.
- **Provenance is visible.** The team's own cut is `[FROM YOU]`; the model's suggestion is tagged for validation.

#### Example 2: Weak Market Analysis

```markdown
# Market Selection & Sizing

## 1. Market Selection
- Market: Smart water

### PESTEL
| Force | Entry |
|---|---|
| Political | Government regulation is increasing |
| Economic | Inflation is affecting budgets |
| Social | Sustainability matters more to people |
| Technological | AI and IoT are transforming the industry |
| Environmental | Climate change |
| Legal | Compliance requirements |

## Total Addressable Market (TAM)
- The global smart water management market is $18.4B, growing at 12.3% CAGR

## 2. Segments
### Segment 1: Large utilities
### Segment 2: Small utilities

## 3. Size the Market & Segments
- SAM: $4.1B (North America)
- SOM: 2% of SAM = $82M
```

**Why this fails**

- **"Smart water" is too broad** to analyze. It isn't centered on who the product serves or the benefit it provides.
- **Every PESTEL entry is generic.** Each would fit any market, and none has a source.
- **The TAM is a guess dressed as a finding:** a precise global figure with no source, in a different unit (dollars, global) from anything the product sells.
- **The segments are size labels** with no description, no cut logic, and no users or buyers in them. The next plays have no one to write about.
- **The SOM is an assumed share** with no competition, reach, or capacity basis, and $82M is not tied to any count of stations or price.

#### Example 3: Drift Bug, "The Free Five Percent"

The market, PESTEL, segments, and SAM are as strong as Example 1. Then the SOM:

```markdown
### Serviceable Obtainable Market (SOM), annual revenue
| Segment | Share basis | Units x annual price | SOM (range) |
|---|---|---|---|
| 1 | Capture 5% of SAM in 24 months | 5% x 32,000-75,000 stations x $1,500 | $2.4M-$5.6M per year |
| 2 | Capture 5% of SAM in 24 months | 5% x 20,000-75,000 stations x $1,500 | $1.5M-$5.6M per year |
```

**Why this fails**

- **The share is a wish.** Nothing explains why 5%: no competitors, no reach, no win rate, no delivery capacity. The Playbook says SOM must consider competition.
- **It inflates by up to 5x.** Example 1's grounded basis gives Segment 1 $0.29M-$1.08M. The free five percent gives $2.4M-$5.6M.
- **It prices a segment with no product fit.** Segment 2 gets a confident SOM for a product that has not been shown to work for single-operator systems.
- **It's easy to miss,** because everything above it is rigorous. Rigor upstream lends false credibility to the assumption downstream.

**Fix:** Build the share from the bottom up: utilities the team can reach over the horizon × a win rate with a stated basis, capped by delivery capacity. Defer SOM for any segment without a product to price. If there is no basis yet, show a conditional formula and name what would anchor it.
