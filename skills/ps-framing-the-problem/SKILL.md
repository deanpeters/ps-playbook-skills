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

## Key Concepts

### Focus on the Why, and the Outcomes Will Follow

The playbook puts it simply: *"Focus on the 'why,' and the outcomes will follow."*

A problem frame that nails the root cause — the **Because** stem — gives the team more clarity about what to build than any amount of solution sketching. Don't rush to "what we need to build" before the "why this problem exists" is solid.

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

Use [template.md](template.md) for the full scaffold.

See the original three-page playbook source in [assets/ps_framing_the_problem_playbook_pages.pdf](assets/ps_framing_the_problem_playbook_pages.pdf).

### Required Output Convention

Default to a **clean, paste-ready problem frame artifact**.

That means:

- fill all five stems, context and constraints, and the final problem statement
- keep each stem within its word budget (see Capacity Reference below)
- produce a final statement that synthesizes the stems into one cohesive narrative
- explanation belongs below the artifact, not inside the stem fields
- the artifact comes first; commentary is secondary

### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in [prompts/01-pressure-test-problem-frame.md](prompts/01-pressure-test-problem-frame.md) one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

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

## Examples

See [examples/sample.md](examples/sample.md).

The example set includes:

- a strong Productside-style problem frame with all five stems, context, and a synthesized final statement
- a weak, generic version with vague barriers and missing emotional stem
- a drift-bug example showing the frame written from the product team's perspective
- commentary on why the weak versions fail

## Common Pitfalls

### Pitfall 1: Jumping to Solutions in the Problem Frame

**Symptom:** The "But" or "Because" stem mentions products, features, or tools. "But there is no integrated dashboard" is a solution statement disguised as a barrier.

**Consequence:** The team skips problem validation and starts building the first solution that comes to mind. The problem frame becomes a requirements doc.

**Fix:** Strip out any mention of products, features, tools, or technologies. Rewrite barriers as the customer's experienced friction: "But manual processes across disconnected systems create delays and errors."

### Pitfall 2: Writing from the Product Team's Perspective

**Symptom:** "I am a product team trying to build a better platform." The stems describe the team's challenge, not the customer's.

**Consequence:** The problem frame justifies the team's existence instead of documenting a real customer problem. Leadership cannot tell if this is a customer need or an internal project.

**Fix:** Every stem must be written from the customer's point of view. The "I am" is the customer. The emotions in "Which makes me feel" are the customer's emotions. If the frame sounds like a project brief, the perspective has drifted.

### Pitfall 3: Making the "But" Too Vague

**Symptom:** "But things are hard" or "But there are challenges" or "But the current situation is not ideal."

**Consequence:** The team cannot identify what to solve. Vague barriers produce vague solutions.

**Fix:** Name concrete, observable barriers. What specifically blocks the persona? What do they run into? What fails, breaks, or takes too long? "But manual data reconciliation across three disconnected systems creates weekly reporting delays of 2-3 days."

### Pitfall 4: Skipping the Emotional Stem

**Symptom:** The "Which makes me feel" stem is blank, one word ("frustrated"), or removed entirely.

**Consequence:** The problem frame loses its human dimension. Leadership sees a process problem but not a severity signal. The emotional stem is what distinguishes "inconvenient" from "career-threatening."

**Fix:** Write 2-3 specific emotions with context. "Frustrated" alone is not enough. "Frustrated by the gap between what leadership expects and what current tools allow, and anxious about being seen as ineffective" tells a story.

### Pitfall 5: Conflating Constraints with Barriers

**Symptom:** Regulatory requirements, budget limitations, or geographic restrictions appear in the "But" stem instead of Context and Constraints.

**Consequence:** The barrier analysis is muddied. The team cannot distinguish between what blocks the persona (barriers) and what bounds the solution space (constraints).

**Fix:** Barriers go in "But" - these are things the persona runs into while trying to achieve their outcome. Constraints go in Context and Constraints - these are conditions the solution must operate within. A barrier is "manual processes create delays." A constraint is "the industry requires SOC 2 compliance."

### Pitfall 6: Final Statement Does Not Match the Stems

**Symptom:** The final problem statement introduces new barriers, changes the persona, or drops the emotional impact.

**Consequence:** The frame is internally inconsistent. A reader who sees the stems and the statement will question which version is correct.

**Fix:** The final statement is a synthesis of the stems, not a rewrite. Every element in the statement should trace back to a stem. If the statement needs new information, update the stems first.

### Pitfall 7: Defaulting to a Tech Role as the Persona

**Symptom:** "I am a data engineer overwhelmed by pipeline complexity" when the product actually serves clinical operations leads or field engineers.

**Consequence:** The problem frame reflects LLM training bias toward technical roles, not the real customer population.

**Fix:** Before writing "I am," confirm who actually uses or buys the product in the field. Most products serve people whose primary job is not writing code. A clinical data platform's customer is a clinical operations lead, not a data engineer.

### Pitfall 8: Exceeding Template Capacity

**Symptom:** The "I am" stem becomes a three-paragraph backstory. The final statement is 150 words.

**Consequence:** The human cannot paste the output into the playbook without rewriting it.

**Fix:** Respect the word budgets. "I am" is ~30-40 words. "Trying to" is ~15-20. "But" is ~20-25. "Because" is ~20-25. "Which makes me feel" is ~15-20. Context is ~30-40. Final statement is ~40-50. Write for the template field, not for the model's appetite for prose.

### Pitfall 9: A Frame With No Evidence Under It

**Symptom:** The PM asks for a problem frame for a persona they have not interviewed, and gets five well-formed stems and a crisp statement.

**Consequence:** The frame passes the decision point on its polish. The team commits to a problem no customer confirmed.

**Fix:** Ask what evidence backs each stem. Mark any stem without evidence as a hypothesis, and route back to discovery before the decision point.

## References

### Skill Files

- [template.md](template.md) - working scaffold
- [prompts/](prompts/README.md) - copy-paste prompt for chat-based AI tools (authored for this library; the deck has no AI page for this Play)
- [examples/sample.md](examples/sample.md) - strong, weak, and drift-bug examples

### Related Project Docs

- [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)
- [framework-glossary.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/framework-glossary.md)
- [skill-authoring-workflow.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/skill-authoring-workflow.md)
- [template_conversion_rules.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/template_conversion_rules.md)
- [template_conversion_usage.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/template_conversion_usage.md)

### Related Skills

#### Upstream (input to this skill)

- [ps-proto-persona](../ps-proto-persona/SKILL.md) - persona work that identifies who has the problem
- [ps-jobs-to-be-done](../ps-jobs-to-be-done/SKILL.md) - jobs and outcomes that feed the "Trying to" stem
- [ps-problem-identification](../ps-problem-identification/SKILL.md) - pains, gains, and candidate problem statements that feed the barrier and root cause stems

#### Downstream (uses output from this skill)

- Solution hypothesis - the validated problem frame justifies moving into solution definition
- Positioning - the problem frame sharpens how the product is positioned
- Exploring the solution space - the framed problem guides what solution territory to explore

### Source Material

- [Baseline Playbook version](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml). Full source PDF supplied separately.
- [assets/ps_framing_the_problem_playbook_pages.pdf](assets/ps_framing_the_problem_playbook_pages.pdf)
- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 46-48: Template 10 of 24 there. No AI page for this Play; the prompts are authored for this library. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).
- Productside Playbook companion document (supplied separately)
