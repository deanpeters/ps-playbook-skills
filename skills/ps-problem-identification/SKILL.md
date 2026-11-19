---
name: ps-problem-identification
description: >-
  Identify customer jobs, pains, gains, and candidate problem statements in
  Productside format, or review drafted problem statements ("X gets in the way
  of achieving Y"). Use when you need compact, evidence-backed problem
  candidates from customer research, or want drafted statements checked.
intent: >-
  Help a Product Manager synthesize Voice-of-the-Customer evidence into customer
  jobs, pains, gains, supporting quotes, and candidate problem statements that
  fit the Productside Problem Identification play without turning the output
  into cleanup work.
type: component
blueprint_stage: Discover + Investigate
best_for:
  - "Turning customer research into jobs, pains, gains, and candidate problem statements"
  - "Consolidating empathy interview findings into a compact working surface"
  - "Selecting the strongest candidate problem to frame in the next play"
scenarios:
  - "I need to turn our interview findings into candidate problem statements"
  - "Help me consolidate customer jobs, pains, and gains from our discovery research"
---


## Purpose

Create a **Productside-style Problem Identification artifact** from customer research.

This skill helps a Product Manager turn customer understanding into a compact working surface:

- customer jobs
- pains
- gains
- supporting empathy interview quotes
- candidate problem statements

The point is not to produce a long explanation of the problem space. The point is to help the human complete the play.

This artifact is also a **cross-functional alignment tool.** The output makes customer understanding visible, shareable, and debatable across product, design, engineering, and leadership  -  not just useful to the PM who ran the discovery.

### Usage Notes

- This exemplar follows the `ps-` naming contract
- It is intentionally budget-aware and template-capacity-aware
- Most default outputs should stay sticky-note-sized or small-cell-sized
- **Coach by default:** the skill asks the PM for the root cause beneath each pain rather than naming it, and catches features posing as problems
- **Evidence honesty:** quotes come only from supplied research (unfilled slots are marked `[needs a real quote]`), and unvalidated causes are marked `[CAUSE TO VALIDATE]`

## Key Concepts

### This Play Is an Aggregator

Problem Identification is where earlier discovery work gets pulled together:

- jobs from Jobs-to-Be-Done
- pains and outcomes from Personas & Proto-Personas
- quotes and lived experience from Empathy Interviews
- patterns from Affinity Mapping

The skill should therefore synthesize, not restart discovery from scratch. **Jobs brought in from earlier work should be treated as revisable**  -  as you validate with customers, reframe any job that doesn't hold up. Evidence updates the artifact; don't treat earlier assumptions as fixed truth.

### The Customer Circle Is the Visual Structure

The canonical template organizes this play as a concentric circle:

- **Center:** the customer persona
- **Inner ring:** Pains and Gains
- **Outer ring:** Customer Jobs
- **Outside the circle:** Problems (root causes of pains, barriers to gains)
- **Sidebar:** Empathy Interview Quotes

This structure is not decoration  -  it shows how problems relate to jobs and how pains and gains are distinct layers between the customer and the things blocking them. A PM filling this template should be thinking in those concentric layers, not just populating a flat list.

### Problem Statements Use a Specific Productside Format

Candidate problems should use this structure:

`[Problem] gets in the way of achieving [Outcome] for [Persona].`

Do not improvise a different sentence form unless the user explicitly asks for alternatives.

### Jobs, Pains, Gains, and Problems Are Not the Same

- **Customer jobs** = what the customer is trying to get done
- **Pains** = friction, obstacles, or negative experience
- **Gains** = positive outcomes or benefits they want
- **Problems** = root causes or barriers that block gains or create pains

If these blur together, the play gets muddy fast.

### A Pain Is a Symptom; a Problem Is the Cause Beneath It

A pain is what the customer **feels**. A problem is the **root cause** that creates the pain or blocks the outcome. "Passengers arrive unprepared" is a pain. "Confusing or late prep instructions" is a cause. Restating a pain in the problem format ("Unprepared passengers get in the way of...") skips the diagnosis while looking finished.

To get from pain to problem, ask what creates the pain. If the answer is the pain reworded, keep digging.

### A Missing Feature Is Not a Problem

"No real-time dashboard," "lack of integration," and "no automated alerts" name solutions by their absence. When a candidate problem is really a missing feature, ask what problem that feature would solve, and write that instead. Keep the play in the problem space.

### A Clean Statement Is Not a Proven One

The format makes thinking legible, not correct. A root cause stays a hypothesis until interviews back it. Mark every cause that isn't yet backed by evidence `[CAUSE TO VALIDATE]`, so the team knows what to test before framing the problem in the next play.

### The Agent's Role: Coach by Default, Draft on Request

- **Default:** for each pain, ask the PM what root cause creates it. Push back when the answer is the pain reworded or a feature in disguise. Once the PM names a real cause, help write it in the Productside format and sharpen the wording. Do not name the cause for them, in any form: no lists, no examples ("it might be..."), and no causes folded into a question ("Is it that she can't see X, or that Y?"). Ask open questions about what the PM heard, saw, or was told ("What happens today when...? What did they say gets in the way?").
- **On request, or in best guess mode:** propose candidate causes, each marked `[CAUSE TO VALIDATE]`, for the PM to accept, adjust, or reject.
- **Always:** never invent quotes, outcomes, or personas. Quotes come only from supplied research.

### Quotes Are Supporting Evidence, Not Decoration

The quotes help prove the candidate problems are grounded in real customer experience.

They should sound like lived reality, not sanitized summary copy.

### Template Capacity Matters

The canonical Productside template for this play has many **sticky-note-sized or small-cell fields**.

That means the default output must be:

- short
- specific
- paste-ready

Do not generate mini-essays for fields that behave like notes.

See [Template and capacity guidance](#template) for the real canonical budgets.

### How AI Supports This Play

The Playbook casts AI as a **coach that separates pains from problems and formats the result**. The PM has done the research. AI helps shape affinity themes, interview insights, jobs, and personas into sharp, well-formed problem statements. The cause has to come from the PM and their evidence.

- **Use it when:** the PM has real insights from affinity mapping and interviews and wants help separating symptoms from causes.
- **Avoid it when:** the PM has not talked to customers yet. AI will format confident root causes and problem statements no one can defend. Say so, and route to ps-empathy-interviews.
- **Return:** pains separated from the root causes beneath them, problem statements in one consistent format, and every guessed root cause marked `[CAUSE TO VALIDATE]`.

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


### Required Output Convention

Default to a **clean, paste-ready artifact**.

That means:

- fill every expected slot in the template
- jobs, pains, and gains should be short enough for sticky-note or small-cell use
- quotes should be short enough to fit the playbook cells
- problem statements should fit the canonical carrying capacity
- explanation belongs below the artifact, not inside the fields

For the default output, produce exactly:

- 4 customer jobs
- 4 pains
- 4 gains
- up to 6 empathy interview quotes, **real quotes only**
- 6 candidate problem statements

Do not silently reduce those counts because a shorter list feels more elegant. The one exception is quotes: never invent a quote to fill a slot. If the research supplies fewer than six, fill the rest with `[needs a real quote]`.

Append `[CAUSE TO VALIDATE]` to any candidate problem whose root cause is not yet backed by evidence.

If the user wants extended reasoning, add it after a fully completed artifact in a short trailing note.

### Step 1: Start from Customer Evidence

Before drafting, ask the user whether they have materials to share that would ground the artifact in real evidence:

- customer interview notes or transcripts
- support tickets or call logs
- quotes already collected
- jobs, pains, or gains identified in earlier discovery
- persona or proto-persona output
- any other internal research or field observations

This skill synthesizes earlier discovery work - the more the user can supply, the less the output relies on assumption. Do not skip this ask.

If there is no customer evidence at all, say so plainly. The Playbook advises against this play until the PM has talked to customers. Recommend ps-empathy-interviews first. If the PM still wants a first pass (best guess), produce it as a labeled hypothesis: no quotes (every slot `[needs a real quote]`), and every candidate problem marked `[CAUSE TO VALIDATE]`.

### If the PM Brings a Draft

When the PM arrives with pains and a first read on their causes, or with drafted problem statements, work through them rather than redrafting. This mirrors the critique guidance in this Play.

1. **For each pain, ask for the root cause.** If the PM's answer is the pain reworded, say so and ask them to dig.
2. **Watch for solutions in disguise.** If a "problem" is a missing feature, point at it and ask what problem the feature would solve. Don't list candidate causes for the PM to pick from, and don't hint at them as examples or "is it X or Y?" questions; the cause has to come from what they heard. This applies to a cause that looks like a symptom, too: ask why it happens, without guessing the answer.
3. **Format the real causes.** Write each as `[Problem] gets in the way of achieving [Outcome] for [Persona]`, pulling the outcome and persona from what the PM gave you.
4. **Mark the guesses.** Append `[CAUSE TO VALIDATE]` to any cause the PM is still guessing at.

### Step 2: Write the Customer Jobs

Capture what the customer is trying to get done.

For this play, jobs should be **compact**. Most should fit in a sticky-note-sized field.

Avoid:

- broad mission statements
- generic aspirations
- internal team tasks

Prefer:

- short action-oriented job statements
- concrete customer progress

Output exactly 4 jobs unless the user explicitly asks for a different count.

### Step 3: Identify Pains

Pains are the friction, obstacles, risks, delays, confusion, or negative experiences surrounding the job.

Keep them short enough to paste directly into the playbook.

Do not turn them into explanation paragraphs.

Output exactly 4 pains unless the user explicitly asks for a different count.

### Step 4: Identify Gains

Gains are the positive outcomes the customer wants when the job goes well.

Keep gains distinct from pains:

- pains remove friction
- gains create positive progress or benefit

Output exactly 4 gains unless the user explicitly asks for a different count.

### Step 5: Select Supporting Quotes

Choose quotes that make the problem feel real. **Select them from the research the PM supplied. Never write them.** A quote the agent wrote is not evidence, however real it sounds.

Good quotes:

- show frustration, workaround, or unmet need
- were actually said by a customer
- are short enough to fit the template

Output up to 6 quotes. Mark any unfilled slot `[needs a real quote]`.

### Step 6: Write Candidate Problems

Use the Productside sentence structure:

`[Problem] gets in the way of achieving [Outcome] for [Persona].`

Each candidate should be:

- concrete
- customer-centered
- a cause, not a pain reworded or a missing feature
- short enough to fit the canonical field

By default, get the cause from the PM (see [If the PM Brings a Draft](#if-the-pm-brings-a-draft)). Mark any cause not yet backed by evidence `[CAUSE TO VALIDATE]`.

Do not pad the sentence with unnecessary context. The field is small.

Output exactly 6 candidate problems unless the user explicitly asks for a different count.

### Step 7: Keep the Artifact Compact

For this skill, brevity is usability.

If the output is so long that the human Product Manager has to rewrite it before using it, the skill has failed.

Do not let good prose outrank usable template completion.

### Step 8: Add Optional Short Notes

If helpful, add a brief trailing section such as:

- `What to pressure-test next`
- `Weakest candidate problems`
- `Open evidence gaps`

Keep it separate from the paste-ready artifact.

Do not add a notes section at all unless:

- the user asks for it, or
- the artifact is already fully complete

## Template

Use this template to build a **Productside-style Problem Identification artifact** from customer research.

Most fields in this play are small. Keep entries compact and paste-ready.

### Template

```markdown
# Problem Identification

## Product Context
- Product or service:
- Target persona:
- Research source:

## Customer Jobs
- Job 1:
- Job 2:
- Job 3:
- Job 4:

> Quality check: Keep jobs short and concrete. Most should fit in a sticky-note-sized field.
> Completion rule: Fill all 4.

## Pains
- Pain 1:
- Pain 2:
- Pain 3:
- Pain 4:

> Quality check: These are obstacles, risks, frustrations, or negative experiences. Keep them compact.
> Completion rule: Fill all 4.

## Gains
- Gain 1:
- Gain 2:
- Gain 3:
- Gain 4:

> Quality check: Gains are positive outcomes the customer wants, not just the absence of pains.
> Completion rule: Fill all 4.

## Empathy Interview Quotes
- Quote 1:
- Quote 2:
- Quote 3:
- Quote 4:
- Quote 5:
- Quote 6:

> Quality check: Every quote was actually said by a customer and is short enough to fit the template.
> Completion rule: Real quotes only. Mark any unfilled slot `[needs a real quote]`. Never invent one.

## Candidate Problems
- Problem 1: [Problem] gets in the way of achieving [Outcome] for [Persona].
- Problem 2: [Problem] gets in the way of achieving [Outcome] for [Persona].
- Problem 3: [Problem] gets in the way of achieving [Outcome] for [Persona].
- Problem 4: [Problem] gets in the way of achieving [Outcome] for [Persona].
- Problem 5: [Problem] gets in the way of achieving [Outcome] for [Persona].
- Problem 6: [Problem] gets in the way of achieving [Outcome] for [Persona].

> Quality check: Keep each candidate short enough to paste directly into the playbook field. Do not add explanation inside the statement.
> Quality check: Is each [Problem] a root cause, not a pain reworded and not a missing feature?
> Evidence check: Append `[CAUSE TO VALIDATE]` to any candidate whose cause is not yet backed by evidence.
> Completion rule: Fill all 6.

## What To Pressure-Test Next
- Which problem feels strongest?
- Which problem feels weakest?
- What evidence gap still matters?
```

### Usage Guidance

- Do not turn jobs, pains, gains, or problems into paragraphs.
- If the user wants explanation, add it after the artifact.
- Respect the canonical template capacity in [Template and capacity guidance](#template).
- Do not add the `What To Pressure-Test Next` section unless the artifact is already fully complete.

## Examples

Illustrative and fictional, not customer evidence.

- **Strong:** "Late schedule updates get in the way of keeping dock assignments aligned." Connect this candidate to real observations and retain the customer's language.
- **Weak:** A paragraph combining several problems makes it hard to investigate any one of them.
- **Drift to avoid:** Missing feature as problem: "No dashboard" is a solution-shaped complaint. Identify the customer progress it obstructs.


## Common Pitfalls

- **Writing Novellas into Sticky-Note Fields:** Respect the template capacity. Small field means short entry.

- **Pitfall 1b: Underfilling the Template:** Match the template slot count by default.

- **Confusing Pains with Problems:** Use pains as evidence, then write a candidate problem in the Productside format.

- **Writing Generic Jobs:** Write short but concrete customer jobs.

- **Making Gains a Mirror Image of Pains:** Ask what better looks like for the customer, not just what less-bad looks like.

- **Losing the Quotes:** Include short quotes that support the candidate problems.

- **Letting Commentary Replace the Artifact:** Complete the artifact first. Commentary is optional and trailing only.

- **Naming a Missing Feature as the Problem:** Ask what problem the missing feature would solve, and write that. "Late notice of policy changes gets in the way of achieving compliance for Henry" leaves the solution open.

- **Format Mistaken for Proof:** Mark every cause not yet backed by evidence `[CAUSE TO VALIDATE]`. Name the evidence base in Product Context. Treat the marked causes as the next round's interview topics.

- **Inventing Quotes to Fill the Slots:** Quotes come only from supplied research. Leave unfilled slots as `[needs a real quote]`.

## References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-problem-identification) for supporting source material and expanded examples.
