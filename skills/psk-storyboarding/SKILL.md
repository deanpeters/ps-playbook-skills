---
name: psk-storyboarding
description: >-
  Build a six-panel narrative storyboard that validates a product solution
  hypothesis by telling a customer-centered story from problem to lasting
  change. Use during the Create phase, after the solution hypothesis is in hand.
intent: >-
  Help a Product Manager validate their solution hypothesis by constructing a
  low-fidelity six-panel story where the target persona moves from their
  everyday problem through a moment of crisis, discovers the solution, and
  arrives at a changed world. The storyboard is not a polished deliverable; it
  is a fast thinking tool that surfaces gaps in the narrative before anything is
  built.
type: component
blueprint_stage: Discover + Define
best_for:
  - "Validating a solution hypothesis through a six-panel narrative"
  - "Showing how a real persona moves from pain to resolution through your product"
  - "Testing whether the solution story holds together before building anything"
scenarios:
  - "I need to validate our solution hypothesis by walking through a persona story"
  - "Help me build a six-panel storyboard showing how our customer goes from pain to resolution"
---


## Purpose

Create a **Productside-style Storyboard** that validates a solution hypothesis through narrative.

This skill helps a Product Manager build a six-panel story centered on their target persona. The story follows a structured arc from the persona's status quo through a high-stakes conflict, into first contact with the solution, and finally to the lasting change that solution enables.

The storyboard belongs in the **Discover + Define phase** of the Productside Playbook. The B2B work-in-progress deck gives it no template number and places its instruction page right after Lo-fi Experimentation; the baseline deck had it as Template 16 of 24 in Create. It is explicitly low-fidelity. The playbook says it plainly: "Don't spend a lot of time building your storyboard; it doesn't need to look pretty!" Speed and clarity of thinking matter here. Aesthetics do not.

The storyboard does two things: it tests whether the PM's story about the customer rings true, and it gives stakeholders and real users something concrete enough to react to.

### Usage Notes

- This is a component skill that produces a paste-ready six-panel narrative artifact.
- The Solution Hypothesis Statement (from psk-solution-hypothesis) anchors the top of every storyboard.
- Low fidelity is a design principle, not a limitation. Speed and clarity of thinking matter; aesthetics do not.
- The tech-role bias guard in Step 1 of Application is the single most important step in this skill.
- Upstream: psk-solution-hypothesis, psk-proto-persona, psk-framing-the-problem.
- Downstream: leadership alignment, executive communication, Go-to-Market narrative.

## Key Concepts

### Three Story Elements

Every storyboard requires three elements working together. If any one is missing, the story breaks down.

**Character** is the persona - the specific customer whose life the PM is trying to improve. The character must match the User Persona from psk-proto-persona. This is not the PM, not the product team, and not a generic user. It is a concrete individual with a job, a world, and things they care about.

**Conflict** is the problem - the specific breakdown that makes the persona's goal unreachable in the current state. The conflict should echo the Problem Statement from psk-framing-the-problem. A storyboard without a real conflict has no stakes and cannot be validated.

**Resolution** is the solution - how the product enters the persona's world and changes what is possible. The resolution must align with the If/Then structure from the Solution Hypothesis in psk-solution-hypothesis.

All three must be present and internally consistent. A strong character paired with a weak conflict produces a story no one can respond to. A strong conflict with a vague resolution does not validate the hypothesis.

### The Six-Panel Arc

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

### The Persona Is the Hero

The persona drives the story. The solution is their sidekick - it enables their success, but it does not achieve their goal for them. A storyboard where the solution is the hero has inverted the structure. The PM should be asking "what does the persona do differently?" not "what does the product do?"

### Low Fidelity Is the Point

Speed matters more than polish in a storyboard. A rough narrative written in twenty minutes and shared with five users produces more insight than a polished visual deck. The six-panel format forces the PM to be specific without burning time on presentation. Images are optional; captions are sufficient.

### What Validate Means Here

Storyboarding is a validation technique, not just a communication tool. Validation means showing the storyboard to real users or stakeholders and watching how they react. Do they recognize their world in Panel 1? Do they nod at Panel 3? Do they believe Panel 5? If the story does not ring true to people who live it, the hypothesis needs adjustment before anything is built.

### The Storyboard Is Also a Product Visualization Tool

Validation with real users is the primary purpose of storyboarding. But the same artifact serves a second function: giving cross-functional stakeholders  -  designers, engineers, executives  -  a concrete, shared picture of the proposed solution before any build investment is made.

A well-constructed six-panel story makes the product's user experience visible in a way that wireframes and feature lists cannot. Stakeholders see the flow: the problem the product addresses, the moment of first contact with the solution, the breakthrough, the lasting change. They understand what the product actually does for the customer  -  its key capabilities and overall user value  -  without reading a requirements document.

Product leaders can use the storyboard to share the product vision with executives, making the problem and proposed solution vivid in a way that slides and written descriptions cannot. Build it once; show it to users for validation, show it to the team for alignment, and show it to leadership for direction-setting.

### Text-First in This Skill

This skill produces text captions, not visual images. Each panel has a caption describing what should be depicted. The PM or a designer can add visuals later. The written captions are sufficient to share, discuss, and validate.

### The Solution Hypothesis Statement Anchors Every Storyboard

Copy the If/Then statement from psk-solution-hypothesis and place it at the top of every storyboard. This anchors the story to a testable claim. If the story does not follow from the hypothesis, the storyboard is disconnected from the validation the PM needs.

### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **critic of the storyboard the PM wrote, and a planner for showing it to real customers**. It checks that the persona is the hero and the product the sidekick, that the story follows the beginning, middle, and end arc from the solution hypothesis, and that the PM has a plan to show it to real target customers and record their reactions. The story and the reactions come from people, not the model.

- **Use it when:** the PM has a solution hypothesis and a draft story, and wants it sharpened and readied for testing with customers.
- **Avoid it when:** the request is to predict how customers will react to the storyboard. That is the test, and only real people can run it.
- **Return:** the story checked against the hypothesis and the three-part arc, the product kept in the sidekick role, and a plan to show the storyboard to real target customers and record what they say.

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

Use [Template](#template) for the scaffold.


### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses Discovery mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

### Step 1: Tech-Role Bias Guard

Before writing a single word of the storyboard, confirm who the product serves.

LLMs default to developer, architect, or product manager roles when no persona is specified. Most products serve non-programmers. A storyboard centered on a developer deploying a tool, when the product actually serves field technicians, operations staff, clinical workers, or line managers, will produce a narrative that fails to resonate with the real audience.

Ask the PM: who is the user persona for this product? Read the answer carefully. If the persona is a PM, engineer, developer, or architect - confirm this is actually the customer the product serves, not a proxy for the person running the exercise.

If the persona is the PM themselves, that is a signal the exercise has drifted. Redirect: who is the person your product is built for? That person is the hero.

### Step 2: Gather Upstream Artifacts

Ask whether the PM has these artifacts to share:

- Solution Hypothesis from psk-solution-hypothesis (the If/Then statement that anchors the storyboard)
- User Persona from psk-proto-persona (the character's name, role, world, pains, and goals)
- Problem Framing from psk-framing-the-problem (the conflict source for Panel 3)

Accept equivalent input from any source. A PM with a product description but no prior plays can still run this skill. Do not block the exercise on missing upstream artifacts.

If artifacts are missing, gather the minimum needed:
- A specific product and what customer it serves
- A concrete description of the problem the customer faces
- A rough If/Then: if we build X, then the customer can do Y

### Step 3: Write the Solution Hypothesis Statement Header

At the top of the storyboard, place the full If/Then statement from psk-solution-hypothesis (or the PM's equivalent).

Format it as a clearly labeled header:

```
Solution Hypothesis Statement:
IF we [description of solution], THEN [customer benefit].
IF [customer benefit], THEN [business outcome].
```

If only one half of the statement is available, use what is there. Do not fabricate the other half.

### Step 4: Write Panel 1 - Introduce the Persona and World

Write the "Once upon a time..." caption.

Introduce the persona by name and role. Describe their world: what do they do day to day, what do they care about, what does success look like from their perspective? Ground the reader in a concrete person in a concrete context.

This panel should make the reader feel they know this person. Avoid generic descriptions ("a busy professional").

### Step 5: Write Panel 2 - The Routine Status Quo

Write the "Every day..." caption.

Show the pattern of friction that precedes the crisis. What does the persona do repeatedly that is inefficient, risky, error-prone, or demoralizing? This is not the disaster yet - it is the condition that makes the disaster inevitable.

The goal of this panel is credibility. The reader (especially users or stakeholders who live this) should recognize the routine as real.

### Step 6: Write Panel 3 - The Escalation Moment

Write the "Until one day..." caption.

Make this specific and high-stakes. A specific event or consequence tips the frustration into a real failure. Something breaks, something is missed, someone is affected. The stakes should feel real enough that the reader understands why doing nothing is not an option.

Vague conflict ("they faced some challenges") produces no feedback. Specific conflict ("she submitted an incorrect dosing report to the regulator and had to recall 30,000 units for re-audit") gives stakeholders something to react to.

### Step 7: Write Panel 4 - First Encounter with the Solution

Write the "Because of that..." caption.

Show the persona encountering the product for the first time. This is an experience, not a feature list. What does it feel like to discover the solution exists? What is the first thing they do or notice?

Avoid writing "they used the product and it solved their problem." Describe the moment of first contact - what they saw, what they tried, what surprised them.

### Step 8: Write Panel 5 - The Aha Moment

Write the "Until finally..." caption.

Name the emotion. This is the moment of breakthrough - the persona realizes the problem is solved or fundamentally changed. What do they feel? Relief, confidence, pride, surprise? Naming the emotion makes the story resonant and makes it easier for real users to confirm or deny when you show them.

### Step 9: Write Panel 6 - The New Normal

Write the "And every day after that..." caption.

Show the lasting behavioral change. The persona's world is different now. What do they do differently? What is possible that was not possible before? What do they no longer worry about?

Avoid ending on "they were happy." Show what they can do, build, prevent, or decide that was out of reach before.

### Step 10: Describe the Visual for Each Panel

For each panel, add a one-line visual description: what image or icon would represent this moment if the storyboard were illustrated?

This is optional but useful when sharing with visual thinkers or preparing the storyboard for a design session. Keep visual descriptions compact (5-15 words).

### Step 11: Offer Next Steps

After completing the storyboard, offer three options:

1. Share with real users: walk three to five users through the storyboard panel by panel and capture where the story rings true and where it breaks down. The conflict moment and the Aha moment are the most important panels to test.
2. Share with leadership: the storyboard is an effective executive alignment tool. It makes the problem and solution concrete without requiring a slide deck.
3. Use in Go-to-Market messaging: the six-panel arc - problem, escalation, discovery, breakthrough, new normal - maps directly to launch narrative and sales enablement content.

## Template

### When to Use This

Use this template during the **Create phase** after you have a Solution Hypothesis in hand. The storyboard validates your hypothesis by telling the customer's story - from their everyday world through the problem crisis into the solution and beyond.

Upstream artifacts that feed this template:
- Solution Hypothesis (psk-solution-hypothesis): the If/Then statement that anchors Panel 1 and must survive to Panel 6
- User Persona (psk-proto-persona): the character - name, role, world, pains, goals
- Problem Framing (psk-framing-the-problem): the source of the conflict in Panel 3

You can run this with only a product description if needed. The hypothesis and persona can be sketched on the fly. Do not block the exercise on missing upstream artifacts.

### Template

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

### Usage Guidance

#### Filling the Template

1. Paste or write the Solution Hypothesis Statement at the top before writing any panel.
2. Fill in the Three Story Elements check - character, conflict, resolution - before Panel 1.
3. Write all six panels in order. Resist the urge to skip to Panel 4.
4. After writing all six panels, do the Hypothesis Alignment Check.
5. Add visual descriptions last, if at all.

#### What Goes Where

| Panel | Contains | Does NOT Contain |
|-------|----------|-----------------|
| Panel 1 | Named persona, concrete world details | Generic "busy professional" descriptions |
| Panel 2 | The recurring friction pattern | The crisis event (that belongs in Panel 3) |
| Panel 3 | A specific, consequential failure event | Vague struggle or "some challenges" |
| Panel 4 | The persona's experience of first contact | A feature list or product spec |
| Panel 5 | A named emotion plus the success moment | The product's achievement (not the persona's) |
| Panel 6 | Specific behavioral change going forward | Vague happiness or "life is better now" |

#### Connecting to Other Skills

- **Upstream:** psk-solution-hypothesis provides the If/Then statement; psk-proto-persona provides the character; psk-framing-the-problem provides the conflict source
- **Downstream:** the storyboard feeds leadership alignment, executive communication, and Go-to-Market narrative

#### Capacity Reference

| Field | Target Length | Guidance |
|-------|-------------|---------|
| Solution Hypothesis Statement | 40-70 words | Full If/Then statement from psk-solution-hypothesis |
| Panel 1-2 captions | 20-35 words each | One to three sentences; specific but not overlong |
| Panel 3 caption | 25-40 words | Slightly more room - the conflict needs enough specificity to be testable |
| Panel 4-6 captions | 20-35 words each | One to three sentences |
| Visual descriptions | 5-15 words each | Optional; describe the image, not the story |

## Examples

Illustrative and fictional, not customer evidence.

- **Strong:** A manufacturing quality inspector encounters a defect, faces its consequences, uses the proposed solution, and reaches a changed outcome across six frames.
- **Weak:** Six screenshots demonstrate an interface without telling a customer story.
- **Drift to avoid:** Tech-role inversion: the inspector is the protagonist; do not replace them with the developer building the tool.


## Common Pitfalls

- **The Solution Is the Hero:** Rewrite every panel from the persona's perspective. What does the persona do, see, feel, or decide? The product should appear as the enabler of those actions, not the subject of the story.

- **Tech-Role Bias - Developer Persona for a Non-Developer Product:** Before writing Panel 1, confirm who the product is built for. Read the product description. Ask: who uses this in the field? Write for that person.

- **Polished and Long Panels:** Each panel caption should be one to three sentences at most. The prompt phrase does the framing work. The caption adds the specific, concrete detail. Keep it rough.

- **Missing the Conflict - Panel 3 Is Vague:** Name a specific event. Something breaks, fails, or causes visible harm. The more concrete the consequence, the more useful the feedback. "She submitted the wrong version of the report and the audit had to restart" is testable. "She had challenges with the process" is not.

- **Story Disconnected from the Hypothesis:** After completing all six panels, read the If/Then statement and then read Panel 3 and Panel 4. Are they about the same problem and the same solution? If not, the story has drifted. Rewrite to align.

- **Panel 6 Is Too Vague:** Name what the persona can now do, build, prevent, or decide that was impossible before. "She can now submit the monthly compliance report in one day instead of four, and she stops dreading the end of each quarter" is specific. "Things improved" is not.

- **Running This Before the Solution Hypothesis Exists:** Before running this skill, produce at least a rough If/Then statement using psk-solution-hypothesis. Even an informal hypothesis ("IF we automate the reconciliation step, THEN the operations manager can close the books without waiting on the data team") is enough to anchor the story.

- **Jumping to Product Features in Panel 4:** Panel 4 describes the persona's first experience, not the product's capabilities. "She logged in for the first time and saw her three overdue tasks organized by the system - she did not have to create the list herself" is an experience. A feature list is not.

- **Predicted Reactions Instead of a Test:** Show the storyboard to real target customers and record their reactions. Treat any predicted reaction as a guess to test.

## References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-storyboarding) for supporting source material and expanded examples.
