---
name: ps-framing-the-problem
description: >-
  Frame a validated customer problem using the Productside stem sequence (I am /
  Trying to / But / Because / Which makes me feel) and craft a clear problem
  statement. Use when you have enough discovery evidence to define what problem
  is worth solving.
intent: >-
  Help a Product Manager synthesize discovery findings into a structured problem
  frame and a clear problem statement that can be shared with leadership and
  used to justify moving into solution definition, using the Productside
  five-stem sequence that keeps the customer's perspective at the center.
type: component
blueprint_stage: Discover + Investigate
best_for:
  - "Writing a validated problem statement using the Productside stem sequence"
  - "Documenting the key decision to move from investigation into definition"
  - "Synthesizing discovery findings into a concise, testable problem frame"
scenarios:
  - "We have validated a customer problem and I need to write a formal problem statement"
  - "Help me frame the problem we discovered so I can present it at our define review"
---


## Purpose

Create a **Productside-style Framing the Problem artifact** that documents a validated problem and produces a clear problem statement.

This skill is for the **Discover + Investigate** phase and marks a **Key Decision Point** in the Productside Blueprint. It sits at the intersection of Investigate and Define - the PM is deciding that the problem is validated enough to move forward into solution definition.

This is a synthesis skill. It pulls together findings from earlier discovery work:

- persona work (ps-proto-persona)
- jobs-to-be-done (ps-jobs-to-be-done)
- empathy interviews
- problem identification (ps-problem-identification)
- affinity mapping

The output is a structured problem frame using the five-stem sequence, context and constraints, and a final problem statement. This artifact is what the PM reviews with their manager and introduces to product governance.

Use this skill when you need to:

- synthesize prior discovery into a single, reviewable problem definition
- craft a problem statement that leadership can evaluate and act on
- document the customer perspective before moving into solution space
- validate that the team is solving a real, evidence-backed problem

This is not a solution specification. If the output mentions features, tools, or implementation approaches, the framing has drifted into solution space.

### Usage Notes

- The template produces a single artifact with three sections: Problem Framing (five stems), Context and Constraints, and Final Problem Statement.
- The five-stem sequence is fixed order: I am / Trying to / But / Because / Which makes me feel.
- Evidence gathering is **user artifacts only** - no web research offered. This skill synthesizes the PM's own discovery work.
- Upstream: ps-proto-persona, ps-jobs-to-be-done, ps-problem-identification, empathy interviews.
- Downstream: solution hypothesis, positioning, exploring the solution space (Discover + Define phase).

## Key Concepts

### Focus on the Why, and the Outcomes Will Follow

The playbook puts it simply: *"Focus on the 'why,' and the outcomes will follow."*

A problem frame that nails the root cause  -  the **Because** stem  -  gives the team more clarity about what to build than any amount of solution sketching. Don't rush to "what we need to build" before the "why this problem exists" is solid.

This is also a human-centered design exercise. It starts with the person experiencing the problem, not the solution space, and leaves room for creativity and imagination once the why is clear.

### The Five-Stem Sequence Is a Fixed Structure

The Productside problem frame uses five stems in exact order. Do not reorder, skip, or merge them:

1. **I am:** Describe the user persona's experience with the problem in 3-4 key points
2. **Trying to:** List the outcome they care about
3. **But:** Describe what problem barriers stand in the way
4. **Because:** Enter the root cause of why the problem or barrier exists
5. **Which makes me feel:** Describe the emotions from the customer's point of view

Each stem has a specific job. "I am" establishes who and what they face. "Trying to" names the desired outcome. "But" names the concrete barriers. "Because" explains the root cause. "Which makes me feel" captures the emotional impact. Together they build a complete problem frame from the customer's perspective.

### Context and Constraints Are Separate from the Problem Frame

Section 2 of the template captures the external conditions surrounding the problem - industry dynamics, regulatory requirements, geographic limitations, technology constraints, budget restrictions, or population characteristics.

These are not barriers (barriers go in "But"). Constraints are the environment the problem exists within. A barrier is what blocks the persona. A constraint is a condition the solution must operate within.

### The Final Problem Statement Synthesizes the Stems

Section 3 takes the five stems and combines them into one cohesive problem statement. The statement should read as a single flowing narrative that a manager or governance body could understand without seeing the stem breakdown.

The statement must be consistent with the stems above it. If the final statement introduces new information not in the stems, or drops key elements, the frame is broken.

### This Is a Decision Point

The playbook explicitly marks this template as a Key Decision Point. The output goes to leadership and product governance. The PM is saying: "I have identified and validated this problem. I want to move into defining a solution."

This means the problem frame should be polished enough to present, not a rough working draft. It also means the evidence behind it should be real - from customer research, not from assumptions.

### Customer Perspective, Not Product Team Perspective

Every stem is written from the customer's point of view. "I am" refers to the customer. "Which makes me feel" captures the customer's emotions. If any stem reads like something the product team would say about their own work, the perspective has drifted.

### Problem Framing, Not Solution Framing

No solution language is allowed in the problem frame. Do not mention:

- product names or features
- tools or technologies that could solve the problem
- implementation approaches
- "we need to build" or "the product should"

The problem frame describes the world as the customer experiences it today. Solutions come later, in a different play.

### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **critic of the problem frame the PM drafted**. It checks each stem of the I am / Trying to / But / Because / Which makes me feel sequence for customer voice and evidence, catches a solution hiding in the frame, and tests whether the final statement synthesizes the stems. The frame stays the PM's, built from their discovery evidence.

- **Use it when:** the PM has discovery evidence and a draft frame, and wants it pressure-tested before the decision point.
- **Avoid it when:** there is no discovery evidence yet. A well-formed frame on a guessed problem is still a guess. Route to ps-problem-identification or ps-empathy-interviews.
- **Return:** each stem checked for customer voice, specificity, and evidence; solution language flagged; and the final statement tested against the stems.

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

Use [Template](#template) for the full scaffold.


### Required Output Convention

Default to a **clean, paste-ready problem frame artifact**.

That means:

- fill all five stems, context and constraints, and the final problem statement
- keep each stem within its word budget (see Capacity Reference below)
- produce a final statement that synthesizes the stems into one cohesive narrative
- explanation belongs below the artifact, not inside the stem fields
- the artifact comes first; commentary is secondary

### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses Discovery mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

### Step 1: Confirm the Product and Persona

Before writing anything, answer:

- what product or service is the PM building?
- who is the customer persona whose problem is being framed?
- what prior discovery work exists (persona, JTBD, empathy interviews, problem identification)?

If you cannot identify a specific customer persona, stop and resolve the target first.

**Guard against tech-role bias.** The problem belongs to the customer - the person who uses or buys the product in the field. A clinical data platform's customer problem belongs to a clinical operations lead, not a data engineer. An industrial IoT platform's customer problem belongs to a plant manager, not a solutions architect. Before writing the "I am" stem, confirm: does this person actually experience the problem day-to-day?

### Step 2: Gather Evidence Before Writing

Once you know the product and persona, offer the user materials to share before drafting:

**User-supplied artifacts** - ask whether the user has materials to ground the frame: interview notes, empathy mapping output, problem identification artifacts, JTBD work, support tickets, or earlier skill outputs.

This skill is **user artifacts only** - it synthesizes the PM's own discovery work. Web research is not offered because the problem frame should come from validated customer evidence, not from external sources the PM has not yet verified.

If the user has no artifacts and no prior discovery work, surface the tension: a problem frame without evidence is an assumption frame. Recommend doing persona, JTBD, or empathy interview work first, but proceed if the user wants to draft an assumption-based frame.

### Step 3: Fill the "I am" Stem

Describe the persona's experience with the problem in 3-4 key points.

This stem establishes:

- who the persona is (role, not name)
- what their situation looks like
- what they are dealing with day-to-day

Write from the persona's perspective. Use concrete, specific language. "An HR specialist overwhelmed by manual processes" is better than "a professional facing challenges."

Word budget: ~30-40 words.

### Step 4: Fill the "Trying to" Stem

State the outcome the persona cares about - what they are trying to achieve.

This is not a task list. It is the desired end state. "Automate administrative tasks and free up time for strategic initiatives" describes an outcome. "Complete form A-7 by Friday" describes a task.

Word budget: ~15-20 words.

### Step 5: Fill the "But" Stem

Name the concrete barriers that stand in the way of the desired outcome.

Barriers are specific and observable:

- "Manual and time-consuming HR processes" - concrete
- "Things are difficult" - vague and useless
- "Outdated systems and fragmented tools slow progress" - concrete

Do not put constraints here. Constraints (regulatory, budget, geographic) go in Context and Constraints. Barriers are what blocks the persona from achieving their outcome.

Word budget: ~20-25 words.

### Step 6: Fill the "Because" Stem

Explain the root cause - why the barrier exists.

This is the "why behind the why." The barrier is what blocks; the root cause is why that barrier persists. If the barrier is "manual and time-consuming processes," the root cause might be "the lack of an integrated platform and real-time data access."

Push past surface-level causes. "Because things have always been done this way" is not a root cause. "Because the organization's systems were implemented independently over a decade and were never integrated" is closer.

Word budget: ~20-25 words.

### Step 7: Fill the "Which makes me feel" Stem

Capture the emotional impact from the persona's point of view.

This stem is not optional. It grounds the problem frame in the human experience. Product governance decisions are influenced by understanding the severity of the problem, and emotional impact is part of severity.

Use specific emotional language:

- "Frustrated, stressed, and unable to deliver the value my role demands" - specific
- "Bad" - not specific enough
- "Overwhelmed by the gap between what is expected and what is possible" - specific

Word budget: ~15-20 words.

### Step 8: Write Context and Constraints

Document the external conditions surrounding the problem:

- **Industry context** - regulatory environment, competitive dynamics, market pressures
- **Geographic constraints** - regional requirements, distributed operations
- **Technology constraints** - legacy systems, integration limitations
- **Budget constraints** - limited resources, competing priorities
- **Population constraints** - characteristics of the target users

Constraints frame the environment the solution must operate within. They are not barriers (those went in "But") and they are not the problem itself.

Word budget: ~30-40 words.

### Step 9: Synthesize the Final Problem Statement

Combine the five stems into one cohesive statement.

The final statement should:

- read as a single flowing narrative
- use the stem structure: "I am [role] [situation]. Trying to [outcome]. But [barriers]. Because [root cause]. Which makes me feel [emotions]."
- be consistent with the stems above - no new information, no dropped elements
- be presentable to leadership without additional context

Word budget: ~40-50 words.

### Step 10: Keep the Artifact Compact

The canonical template uses defined fields with limited space. Every stem, the context section, and the final statement should fit within the word budgets specified.

If the output requires summarizing before it can be pasted into the playbook, it is too long.

Do not let good prose outrank usable template completion.

### Step 11: Offer Next Steps

After the artifact is complete, offer the user up to three next-step options:

1. **Move to solution hypothesis** - the problem is framed and validated; begin exploring what to build (Discover + Define phase)
2. **Refine positioning** - use the problem frame to sharpen how the product is positioned against the problem
3. **Review upstream work** - if the problem frame exposed gaps, go back to proto-persona, JTBD, or empathy interviews to strengthen the evidence

Present these as options, not as mandatory steps. The user decides what comes next.

## Template

### When to Use This

Use this template during **Discover + Investigate** when you have enough discovery evidence to frame a validated problem and craft a problem statement. This is a **Key Decision Point** - the output goes to leadership and product governance to justify moving into solution definition.

Upstream work that feeds this template: proto-persona, jobs-to-be-done, empathy interviews, problem identification, affinity mapping.

### Template

```markdown
# Framing the Problem

## Product Context

- Product or service:
- Target market segment:
- Primary persona (the customer with the problem):

## 1. Problem Framing

**I am:**
Describe the user persona's experience with the problem in 3-4 key points


**Trying to:**
List the outcome they care about


**But:**
Describe what problem barriers stand in the way


**Because:**
Enter the root cause of why the problem or barrier exists


**Which makes me feel:**
Describe the emotions from the customer's point of view


> Quality check: Is every stem written from the customer's perspective, not the product team's?
> Quality check: Does the "But" name concrete, observable barriers - not vague "challenges"?
> Quality check: Is the "Because" a root cause, not a restatement of the barrier?
> Quality check: Is the "Which makes me feel" stem present with specific emotions, not just "frustrated"?
> Quality check: Is there any solution language in the stems (product names, features, tools)? Remove it.
> Capacity check: I am ~30-40 words. Trying to ~15-20 words. But ~20-25 words. Because ~20-25 words. Which makes me feel ~15-20 words.

## 2. Context and Constraints

Describe the industry, regulatory, geographic, technology, budget, or population constraints surrounding the problem.


> Quality check: Are these external conditions, not barriers? Barriers go in "But." Constraints describe the environment the solution must operate within.
> Capacity check: ~30-40 words.

## 3. Final Problem Statement

Synthesize the five stems into one cohesive statement.


> Quality check: Does the statement follow the stem structure (I am / Trying to / But / Because / Which makes me feel)?
> Quality check: Is every element in the statement traceable to a stem above? No new information should appear here.
> Quality check: Could a manager read this statement alone and understand the problem without seeing the stems?
> Capacity check: ~40-50 words.

## Evidence Notes (optional)

- Discovery sources used:
- What is well-supported by evidence:
- What is still assumption:
- Recommended next validation steps:
```

### Usage Guidance

#### Filling the Template

1. Start with **Product Context** to anchor who this is for and whose problem it is.
2. Fill the **five stems in order** - do not skip or reorder. Each stem builds on the previous one.
3. Fill **Context and Constraints** separately - these are external conditions, not part of the problem frame itself.
4. Write the **Final Problem Statement** last, synthesizing all five stems into one cohesive narrative.
5. The **Evidence Notes** section is optional and trailing. Do not let it displace or delay the main artifact.

#### The Stem Sequence Is Fixed

The five stems must appear in this exact order:

1. I am
2. Trying to
3. But
4. Because
5. Which makes me feel

Do not merge stems, skip stems, or reorder them. Each has a distinct function in building the problem frame.

#### What Goes Where

| Section | Contains | Does NOT Contain |
|---------|----------|------------------|
| I am | Persona role, situation, 3-4 key experience points | Product features, team perspective |
| Trying to | The desired outcome | Task lists, feature requests |
| But | Concrete, observable barriers | Constraints (those go in Context) |
| Because | Root cause of the barrier | Surface-level restatements |
| Which makes me feel | Specific customer emotions | "Bad" or "frustrated" alone |
| Context and Constraints | Industry, regulatory, budget, technology, geographic conditions | Barriers (those go in But) |
| Final Problem Statement | Synthesis of all five stems | New information not in the stems |

#### Connecting to Other Skills

- **Upstream:** Proto-persona provides the "I am." JTBD provides the "Trying to." Problem Identification provides barriers, root causes, and candidate problems. Empathy interviews provide emotional evidence.
- **Downstream:** The validated problem statement justifies moving into Discover + Define - solution hypothesis, positioning, exploring the solution space.

#### Capacity Reference

See [Template and capacity guidance](#template) for the exact word and character budgets per field.

| Field | Word Budget | Guidance |
|-------|-------------|----------|
| I am | ~30-40 | Role + situation + 3-4 key experience points |
| Trying to | ~15-20 | One clear outcome statement |
| But | ~20-25 | Concrete barriers, not vague "challenges" |
| Because | ~20-25 | Root cause, not barrier restatement |
| Which makes me feel | ~15-20 | 2-3 specific emotions with context |
| Context and Constraints | ~30-40 | External conditions bounding the solution space |
| Final Problem Statement | ~40-50 | Cohesive synthesis of all five stems |

## Examples

Illustrative and fictional, not customer evidence.

- **Strong:** A superintendent is trying to coordinate trades, but learns of sequencing changes too late because crews rely on disconnected updates, leaving them anxious about rework. Develop all five stems.
- **Weak:** "We need a scheduling dashboard" names a solution rather than a customer problem.
- **Drift to avoid:** Perspective inversion: "Our team needs to ship faster" frames the product team's work, not the superintendent's experience.


## Common Pitfalls

- **Jumping to Solutions in the Problem Frame:** Strip out any mention of products, features, tools, or technologies. Rewrite barriers as the customer's experienced friction: "But manual processes across disconnected systems create delays and errors."

- **Writing from the Product Team's Perspective:** Every stem must be written from the customer's point of view. The "I am" is the customer. The emotions in "Which makes me feel" are the customer's emotions. If the frame sounds like a project brief, the perspective has drifted.

- **Making the "But" Too Vague:** Name concrete, observable barriers. What specifically blocks the persona? What do they run into? What fails, breaks, or takes too long? "But manual data reconciliation across three disconnected systems creates weekly reporting delays of 2-3 days."

- **Skipping the Emotional Stem:** Write 2-3 specific emotions with context. "Frustrated" alone is not enough. "Frustrated by the gap between what leadership expects and what current tools allow, and anxious about being seen as ineffective" tells a story.

- **Conflating Constraints with Barriers:** Barriers go in "But" - these are things the persona runs into while trying to achieve their outcome. Constraints go in Context and Constraints - these are conditions the solution must operate within. A barrier is "manual processes create delays." A constraint is "the industry requires SOC 2 compliance."

- **Final Statement Does Not Match the Stems:** The final statement is a synthesis of the stems, not a rewrite. Every element in the statement should trace back to a stem. If the statement needs new information, update the stems first.

- **Defaulting to a Tech Role as the Persona:** Before writing "I am," confirm who actually uses or buys the product in the field. Most products serve people whose primary job is not writing code. A clinical data platform's customer is a clinical operations lead, not a data engineer.

- **Exceeding Template Capacity:** Respect the word budgets. "I am" is ~30-40 words. "Trying to" is ~15-20. "But" is ~20-25. "Because" is ~20-25. "Which makes me feel" is ~15-20. Context is ~30-40. Final statement is ~40-50. Write for the template field, not for the model's appetite for prose.

- **A Frame With No Evidence Under It:** Ask what evidence backs each stem. Mark any stem without evidence as a hypothesis, and route back to discovery before the decision point.

## References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-framing-the-problem) for supporting source material and expanded examples.
