---
name: psk-empathy-interviews
description: >-
  Prepare empathy interview questions, get conduct guidance, and document
  structured findings using the Productside empathy interview framework. Use
  when you need to validate assumptions about customer needs through direct
  conversation.
intent: >-
  Help a Product Manager prepare for, conduct, and document empathy interviews
  that uncover customer motivations, goals, and challenges, using the
  Productside interview framework that keeps the interviewee at the center and
  produces structured findings the team can act on.
type: process
blueprint_stage: Discover + Investigate
best_for:
  - "Preparing tailored interview questions grounded in a specific persona and product context"
  - "Structuring raw interview notes into a findings board the team can act on"
  - "Validating assumptions from proto-persona or JTBD work with real customers"
scenarios:
  - "I need to prepare interview questions for a clinical operations lead we are meeting next week"
  - "I just finished three customer interviews and need help structuring the findings"
---


## Purpose

Create a **Productside-style Empathy Interview artifact** for your target customer.

This skill is for the **Discover + Investigate** phase. It closes the evidence loop - moving the team from assumptions about customer needs to validated understanding grounded in real conversation.

This is a **process skill**, not a content-fill skill. It spans three phases:

1. **Prepare** - define learning objectives, choose topic areas, sharpen the PM's interview questions, and optionally rehearse technique against realistic interview moments
2. **Conduct** - provide the PM with a reference card for running the interview (the agent cannot do this step)
3. **Document** - help structure raw interview notes into a findings board the team can act on

The agent helps with phases 1 and 3. Phase 2 happens in the field - the PM conducts the actual interview. The agent cannot substitute for face-to-face (or video) conversation with a real customer. It can play the customer in a rehearsal, but a rehearsal is practice, never research.

Use this skill when you need to:

- validate assumptions from proto-persona or JTBD work with real customers
- understand the customer's actual workflow, frustrations, and motivations
- discover jobs, outcomes, and problems you did not anticipate
- capture the emotional dimension of the customer experience (what they feel, not just what they do)
- build empathy across the product team by documenting first-person customer language

This is not a survey design tool, a usability test script, or a sales call framework. Empathy interviews are discovery conversations - open-ended, story-seeking, and judgment-free.

### Usage Notes

- This is a **process skill** (`type: process`), not a component skill. It spans preparation, interview conduct, and findings documentation across multiple sessions.
- The agent helps with preparation (Phase 1) and documentation (Phase 3). The PM conducts the actual interview (Phase 2) in the field - the agent cannot substitute for real customer conversation.
- **Preparation follows the Playbook's AI pages:** name the decision, set learning objectives, choose 4-5 topic areas, and review the PM's own questions (leading, closed, solution-fishing, no objective). The agent drafts questions only on request, labeled as a starting draft.
- **Rehearsal (optional):** the agent can play the persona in a technique drill, one tough moment at a time, then review the PM's technique. It is practice, never research. Nothing from a rehearsal goes into findings.
- Evidence gathering: this skill qualifies for **web research + user artifacts**. Web research grounds the PM in the interviewee's domain before the interview. User artifacts (persona work, JTBD output, prior research) inform question preparation.
- The findings board produces structured output that feeds downstream skills: Jobs-to-Be-Done, Desired Outcomes, Problems, and Feels/Appears.
- Upstream: psk-proto-persona (persona grounds the interview target), psk-jobs-to-be-done (provides assumptions to test).
- Downstream: psk-problem-identification (uses problems and jobs from findings), psk-proto-persona (refine with real quotes and observations).

## Key Concepts

### The 70/30 Rule

The interviewee is the star. Target 70% listening, 30% talking. If the PM is talking more than the interviewee, they are lecturing, not learning.

### Open-Ended Questions Over Yes/No

Questions that start with "Can you walk me through..." or "Tell me about the last time..." produce stories. Questions that start with "Do you..." or "Is it..." produce one-word answers that teach nothing.

### "Tell Me About the Last Time..." Is the Key Probe

The most powerful interview technique is asking about a specific, recent occurrence. "Tell me about the last time you had to reconcile data across systems" produces richer insight than "How do you usually handle data reconciliation?"

### Look for Say/Feel/Do/Think Inconsistencies

Customers say one thing, feel another, do a third, and think a fourth. The gap between what someone says they do and what they actually do is where the real insight lives. Watch for these disconnects during the interview.

### Biased Questions Poison the Findings

Leading questions ("Don't you think a dashboard would help?") confirm the PM's hypothesis instead of testing it. The PM must learn to ask neutral questions that let the customer lead.

### Confirm Understanding by Reflecting Back

After the interviewee shares something significant, repeat back what you heard in your own words: "So if I understand correctly, you're saying..." This does two things: it confirms you captured their meaning accurately, and it often prompts the interviewee to correct, expand, or go deeper  -  surfacing nuance a follow-up probe alone might miss.

### The Findings Board Maps to Downstream Artifacts

The documentation phase produces four categories that feed directly into other playbook skills:

- **Jobs-to-Be-Done** - what the customer is trying to accomplish (feeds psk-jobs-to-be-done)
- **Desired Outcomes** - what success looks like for the customer (feeds psk-jobs-to-be-done)
- **Problems** - friction, blockers, and pain points observed (feeds psk-problem-identification)
- **Feels/Appears** - emotional and behavioral observations (feeds psk-proto-persona refinement)

### Team Sport

The playbook says to make it a team sport. Have design and engineering counterparts listen in on interviews. They catch different signals than the PM does, and shared exposure to the customer builds alignment faster than secondhand summaries.

### Prepared but Not Rigid

Prepare 5-8 questions, but do not follow the list like a script. The best insights come from following the customer's thread, not from checking boxes. If the customer opens an unexpected door, walk through it.

### The Rescue Probe

If the conversation stalls or the PM gets stuck, the universal fallback is: "Why?" or "Tell me more." These two phrases restart almost any stalled thread.

### Learning Objectives Serve a Decision

Every interview round should inform a decision the team has to make. Name it before writing a single question ("whether to build for hub airports or small airports first," "whether reconciliation or scheduling is the bigger pain"). Every question the PM keeps should trace to a learning objective, and every learning objective should trace to that decision. A question with no objective behind it is a question to cut.

### Topic Areas, Not a Script

The Playbook prepares interviews around **4-5 topic areas**, not a fixed list of questions. Topic areas let the PM improvise and dig deeply while the interviewee steers the conversation and tells their stories. Aim them at what the interviews must validate: the persona's jobs and desired outcomes, and the **root-cause problems** that cause pains and block those outcomes.

Questions still matter. The PM writes them, a few per topic area, as starting points. The interview follows the story, not the list.

### Rehearse Before It Counts

Empathy interviewing is a skill and must be practiced. The Playbook says to role-play with friends and colleagues, and an AI rehearsal partner works too. The drill presents one tough interview moment at a time (a one-word answer, a feature request, a say/do contradiction, silence), and the PM practices the reflex: dig deeper, stay neutral, confirm understanding, resist pitching. Rehearsing out loud, in a chat tool's voice mode, lets the PM hear their own leading phrasing and practice sitting in silence.

A rehearsal is practice, not data. Nothing from it goes into findings.

### How AI Supports This Play

The Playbook casts AI as **preparation partner and sparring partner**. It focuses the PM on what matters so they can guide the conversation, and it can play tough interview moments so the PM can rehearse before it counts.

What AI cannot do is be the person being interviewed. The whole point of this Play is the real conversation. The moment AI answers as the customer and that answer is treated as input, the team has a script, not research, and the Play is corrupted.

- **Use it when:** real interviews are scheduled and the PM wants to sharpen questions or rehearse technique.
- **Avoid it when:** the PM wants AI to answer as the customer in place of an interview. A simulated interview is practice, not research. If no interviews are scheduled, help schedule them; do not simulate them.
- **Return:** leading or closed questions identified for the PM to rewrite, each kept question tied to a learning objective, and the PM's follow-up reflexes drilled against realistic interview moments. See [If the PM Brings a Draft](#if-the-pm-brings-a-draft) and Step 6.

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

This skill produces artifacts in **three phases**. Not all phases happen in a single session:

- **Phase 1 output:** The decision and learning objectives, 4-5 topic areas, the PM's interview questions (reviewed) with follow-up probes, and a conduct reference card. Optionally, a rehearsal and its technique review.
- **Phase 3 output:** A structured findings board with Jobs-to-Be-Done, Desired Outcomes, Problems, and Feels/Appears entries sized for the canonical template.

The PM returns to the agent after conducting the interview (Phase 2) to get help with Phase 3.

### If the PM Brings a Draft

When the PM arrives with draft questions or topic areas, review them before writing anything new. This mirrors the critique guidance in this Play.

1. **Confirm the persona and the decision.** If no learning objectives exist, get them first (Step 3).
2. **Review each question.** Flag leading questions, closed (yes/no) questions, and questions that fish for the PM's solution. Quote the words at fault.
3. **Tie each kept question to a learning objective.** Name any question with no objective behind it, and any objective with no questions.
4. **Name the gaps.** Name missing topic areas (often current workarounds, impact, and the emotional cost) without writing the questions for them.
5. **Offer rewrites last**, as options to accept, adapt, or reject. The PM writes the final wording.

Return the review as a compact table (question, verdict, why, objective) before any rewritten guide.

### Step 1: Confirm the Product Context and Target Persona

Before writing anything, answer:

- What product or service are we talking about?
- Who is the target customer (the person who will be interviewed)?
- What is their role and what do they do day-to-day?

If you cannot answer these clearly, stop and resolve the target first.

**Guard against tech-role bias.** The interviewee should be the actual customer - the person who uses or buys the product in the field. An IoT platform PM interviews fleet managers, not solutions architects. A clinical data platform PM interviews clinical operations leads, not data engineers. Before drafting questions, confirm: does this person write code, design systems, or architect solutions as their primary job? If no, the questions should not read like a technical interview.

### Step 2: Gather Evidence Before Writing

Once you know the target persona and role, offer the user two things before drafting questions:

1. **Web research** - offer to run a quick search for the target role in the target industry. Look for how practitioners describe their own work, frustrations, and daily reality. Job postings, industry forums, trade press, and professional community discussions are good sources. The goal is to understand the domain well enough to ask informed questions - not to replace the interview.

2. **User-supplied artifacts** - ask whether the user has materials to share: existing persona work, JTBD output, problem identification artifacts, support tickets, previous interview notes, or any other discovery work that would ground the questions in evidence.

Either, both, or neither is fine - the user decides. But always offer before drafting.

### Step 3: Define Learning Objectives

Before writing questions, ask the PM: what decision will these interviews inform? What do you need to learn to make it? What assumptions need testing?

Learning objectives are not interview questions - they are the strategic goals behind the questions. Examples:

- "We assume clinical data managers spend 40% of their time on manual reconciliation - is that true?"
- "We do not know how this role currently solves the problem - what workarounds exist?"
- "We need to understand the emotional cost of the current process, not just the operational cost."

3-5 learning objectives are enough. They guide question selection and help the PM stay focused during the interview.

### Step 4: Choose Topic Areas, Then Sharpen the Questions

**Topic areas first.** Suggest 4-5 topic areas tied to the learning objectives, aimed at the persona's jobs, desired outcomes, and the root-cause problems behind their pains. Give one or two example open-ended questions per area so the PM sees what good looks like.

**The PM writes the questions.** Ask the PM to draft a few questions per topic area, then review them using [If the PM Brings a Draft](#if-the-pm-brings-a-draft). If the PM asks you to draft the questions (or is in Discovery mode), write 5-8 and label them a starting draft for the PM to rewrite in their own voice. Run the same review on your own draft before handing it over.

Whoever writes them, structure the questions to flow naturally:

1. **Opening** - warm-up questions about the person's role and daily work ("Can you walk me through a typical day...")
2. **Core exploration** - questions that dig into the target problem area ("Tell me about the last time...")
3. **Current state** - how they handle the problem today ("What have you tried to make this faster? What has worked best?")
4. **Impact** - what the problem costs them ("How does this affect your work / team / goals...")
5. **Closing** - open-ended wrap-up ("Is there anything else you'd like to share...")

For each question, include 1-2 follow-up probes. Follow-ups should dig deeper:

- "Can you tell me about a specific time that happened?"
- "Why did you choose that approach?"
- "What happened next?"
- "How did that make you feel?"

Do not include yes/no questions. Do not include questions that mention the product or a specific solution. Every kept question names the learning objective it serves.

### Step 5: Review Conduct Guidance

Before the PM goes into the field, surface the conduct reference card:

- **70/30 rule** - listen 70%, talk 30%
- **Open-ended probes** - "Tell me about the last time...", "Can you walk me through...", "Why?"
- **Story-seeking** - ask about specific recent occurrences, not general habits
- **Bias avoidance** - do not mention the product, do not suggest solutions, do not ask leading questions
- **Inconsistency watch** - note gaps between what they say, feel, do, and think
- **Note-taking** - record exact quotes when possible; note emotions and body language
- **Rescue probe** - if stuck, ask "Why?" or "Tell me more"
- **Closing** - thank them, ask if they are open to further conversations or testing

### Step 6: Rehearse Technique (Optional)

If the PM wants to practice, run a rehearsal drill. This mirrors the critique guidance in this Play.

1. **Say what this is.** It's practice, not data, and nothing from it goes into findings. Suggest voice mode if the PM's tool has one.
2. **Present one realistic interview moment at a time**, playing the persona: a one-word answer, a jump to a feature request, saying one thing while describing the opposite, going quiet. Respond to the PM's moves as the persona plausibly would, then present the next moment.
3. **When the PM says they are done, give an honest review.** Did they dig deeper, stay neutral and unbiased, confirm understanding, and resist pitching solutions? Say where they slipped and what to do differently next time.
4. **Close by sending them to a real customer.** Remind the PM not to treat anything the simulated persona said as truth.

Never carry rehearsal lines into Step 8 (Document Findings), into quotes, or into any downstream artifact.

### Step 7: The PM Conducts the Interview

**The agent cannot do this step.** The PM (or a teammate) conducts the actual interview in the field. The agent waits for the PM to return with notes.

When the PM returns, ask for their raw notes, quotes, and observations before structuring findings.

### Step 8: Document Findings

After the interview, help the PM structure raw notes into the findings board. The board has four quadrants:

**Jobs-to-Be-Done** - what the customer is trying to accomplish, discovered from their stories. Use the Productside job format:
- Functional: [Action verb] + [object of the action]
- Emotional: Feel [Emotion] when [Circumstance]
- Social: Seen as [Social Perception] to [whom]

4-6 entries, ~6-8 words each (sticky-note sized).

**Desired Outcomes** - what success looks like for the customer. Use Direction + Metric + Context format. 3-4 entries, ~8-12 words each.

**Problems** - friction, blockers, and pain points observed during the interview. Write as concrete observations, not abstract categories. 4-6 entries, ~8-12 words each (sticky-note sized).

**Feels/Appears** - emotional and behavioral observations. What the customer appeared to feel, not what they explicitly said. 4 entries, ~6-10 words each (sticky-note sized).

### Step 9: Capture Raw Quotes

Pull 4-6 direct quotes from the interview notes. These are the customer's actual words - not paraphrased, not cleaned up. Quotes ground the findings in real evidence and are powerful artifacts for building team empathy.

Keep quotes to ~15-20 words each.

### Step 10: Synthesize Across Interviews

If the PM has conducted multiple interviews, help identify patterns:

- Which jobs and problems appear across multiple interviews?
- Where do interviewees agree? Where do they diverge?
- Are there persona segments emerging from the data?
- What was surprising or unexpected?

Do not force consensus. Divergence is signal, not noise.

### Step 11: Offer Next Steps

After the findings are documented, offer the user up to three next-step options:

1. **Refine the proto-persona** - update the persona with real quotes, validated pains, and observed attitudes using psk-proto-persona
2. **Move to Problem Identification** - synthesize interview findings into candidate problem statements using psk-problem-identification
3. **Conduct more interviews** - if the sample is small or the findings are inconclusive, prepare questions for another round

Present these as options, not as mandatory steps. The user decides what comes next.

## Template

### When to Use This

Use this template during **Discover + Investigate** to prepare for empathy interviews, guide conduct, and document findings. This is a process skill that spans three phases - preparation, interview conduct (PM does this in the field), and documentation.

### Template

#### Phase 1: Interview Preparation

```markdown
# Empathy Interview Preparation

## Product Context

- Product or service:
- Target market segment:
- Target interviewee role:
- Interviewee's primary job:

## Decision These Interviews Inform

- Decision:
- Who makes it, and by when:

## Learning Objectives

What do we need to learn to make that decision? What assumptions need testing?

1.
2.
3.
4.
5.

> Quality check: Are these learning objectives specific enough to guide question selection?
> Quality check: Do they focus on the customer's reality, not on validating a feature idea?
> Quality check: Does every learning objective trace to the decision above?

## Topic Areas

4-5 areas to explore. They let the interviewee steer and tell stories while you dig deeper. Aim them at the persona's jobs, desired outcomes, and the root-cause problems behind their pains.

| # | Topic Area | Learning Objective It Serves | Example Open-Ended Question |
|---|------------|------------------------------|-----------------------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

## Interview Questions

Prepare 5-8 open-ended questions in your own words, a few per topic area. Do not follow this list rigidly - explore deeper when the customer opens a thread.

| # | Question | Follow-Up Probes | Objective |
|---|----------|-----------------|-----------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |

> Quality check: Does every question start with "Can you...", "Tell me about...", "What...", "How...", or "Why..."?
> Quality check: Does any question mention the product name, a feature, or a specific solution? If yes, rewrite it.
> Quality check: Could any question be answered with just "yes" or "no"? If yes, convert to open-ended.
> Quality check: Do the questions cover: daily workflow, pain points, current solutions, impact, and emotional experience?
> Quality check: Does every question name the learning objective it serves? Cut any that don't.
> Capacity check: Questions should be ~15-20 words. Follow-up probes should be ~8-12 words.
```

#### Phase 2: Conduct Guidance (Reference Card)

```markdown
# Interview Conduct Reference Card

## Before the Interview
- [ ] Rehearse your technique (optional): one tough moment at a time, out loud if you can. Practice only; nothing from it goes into findings.
- [ ] Review learning objectives
- [ ] Have questions accessible but not as a rigid script
- [ ] Set up note-taking (or have a teammate take notes)
- [ ] Test recording equipment if applicable (with permission)

## During the Interview

**Opening**
- Introduce yourself and explain why you are talking with them
- Set expectations: "There are no right or wrong answers - I want to learn from your experience"
- Ask permission to take notes or record

**Core Rules**
- 70% listening, 30% talking
- Ask about specific recent occurrences ("Tell me about the last time...")
- Dig deeper on surface answers ("Why?", "Can you say more about that?", "What happened next?")
- Do NOT mention the product, pitch features, or suggest solutions
- Do NOT ask yes/no questions - convert to open-ended
- Do NOT ask "Would you use a tool that...?" or "How would you feel about...?"

**Watch For**
- Inconsistencies between what they say, feel, do, and think
- Emotional reactions - frustration, pride, resignation, anxiety
- Workarounds and hacks they have built
- Language they use to describe their work (capture exact words)

**If You Get Stuck**
- Ask "Why?"
- Ask "Tell me more"
- Ask "Can you give me a specific example?"

**Closing**
- "Is there anything else you'd like to share about your experience?"
- Thank them
- Ask if they are open to further conversations or testing

## After the Interview
- [ ] Document findings within 24 hours (use Phase 3)
- [ ] Share raw notes with teammates who listened in
- [ ] Note what surprised you - surprises are the highest-signal findings
```

#### Phase 3: Document Findings

```markdown
# Empathy Interview Findings

## Interview Context

- Interviewee role:
- Date:
- Interview duration:
- Product context:
- Interviewer(s):

## Raw Quotes

Capture 4-6 direct quotes - the customer's actual words, not paraphrased.

| # | Quote |
|---|-------|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |
| 6 | |

> Quality check: Are these the customer's actual words, or a paraphrase? Use their language.
> Capacity check: Quotes should be ~15-20 words each.

## Findings Board

### Jobs-to-Be-Done

What is the customer trying to accomplish? Discovered from their stories.

| # | Job (Functional / Emotional / Social) |
|---|---------------------------------------|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |
| 6 | |

> Quality check: Do these jobs come from what the customer said, not what you assumed before the interview?
> Quality check: Are all three job types represented if the evidence supports them?
> Capacity check: ~6-8 words per entry (sticky-note sized).

### Desired Outcomes

What does success look like for the customer? Use Direction + Metric + Context.

| # | Desired Outcome |
|---|-----------------|
| 1 | |
| 2 | |
| 3 | |
| 4 | |

> Quality check: Does every outcome use the Direction + Metric + Context format?
> Quality check: Are these the customer's desired outcomes, not your product's value propositions?
> Capacity check: ~8-12 words per entry.

### Problems

Friction, blockers, and pain points observed during the interview.

| # | Problem |
|---|---------|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |
| 6 | |

> Quality check: Are these concrete and specific, not abstract categories like "inefficiency"?
> Quality check: Did the customer describe this problem, or are you inferring it?
> Capacity check: ~8-12 words per entry (sticky-note sized).

### Feels / Appears

Emotional and behavioral observations. What the customer appeared to feel, not just what they said.

| # | Observation |
|---|-------------|
| 1 | |
| 2 | |
| 3 | |
| 4 | |

> Quality check: Do these capture emotions and behaviors, not just opinions?
> Quality check: Did you note any say/feel/do/think inconsistencies?
> Capacity check: ~6-10 words per entry (sticky-note sized).

## Key Insights

- What surprised you:
- What confirmed prior assumptions:
- What contradicted prior assumptions:
- What needs more interviews to validate:

## Evidence Notes

- What is well-supported by this interview:
- What is still a single data point:
- Recommended next steps:
```

### Usage Guidance

#### The Three Phases

This template covers a multi-session process:

1. **Phase 1 (Preparation)** - the agent helps name the decision, define learning objectives, choose topic areas, review the PM's questions, and optionally rehearse technique. This happens before the interview.
2. **Phase 2 (Conduct)** - the PM takes the reference card into the field and conducts the interview. The agent cannot do this step.
3. **Phase 3 (Documentation)** - the PM returns with raw notes. The agent helps structure findings into the board format.

The PM may complete Phase 1, leave for days or weeks, and return for Phase 3. That is normal.

#### How Many Questions

The canonical template has 6 question slots. Default to 5-8 questions:

- 1-2 opening questions about the person's role and daily work
- 2-3 core questions exploring the target problem area
- 1-2 questions about current solutions and impact
- 1 closing question

Add follow-up probes for each question. Do not over-prepare - 8 questions is a ceiling, not a target.

#### Findings Board Sizing

The findings board maps to the canonical template's sticky-note grid:

| Section | Entries | Words per Entry | Guidance |
|---------|---------|-----------------|----------|
| Jobs-to-Be-Done | 4-6 | ~6-8 | Use Productside JTBD formats |
| Desired Outcomes | 3-4 | ~8-12 | Direction + Metric + Context |
| Problems | 4-6 | ~8-12 | Concrete, specific observations |
| Feels/Appears | 4 | ~6-10 | Emotional and behavioral |
| Raw Quotes | 4-6 | ~15-20 | Customer's actual words |

#### Connecting to Other Skills

- **Upstream:** Proto-persona (grounds the interview target and questions); JTBD (provides assumptions to test)
- **Downstream:** Problem Identification uses the problems and jobs from this artifact; proto-persona refinement uses the quotes and emotional observations
- **Parallel:** JTBD can be updated with newly discovered jobs and outcomes from the interview

#### Capacity Reference

See [Template and capacity guidance](#template) for the exact word and character budgets per field.

| Field | Word Budget | Guidance |
|-------|-------------|----------|
| Interview Question | ~15-20 | Open-ended, no product mentions |
| Follow-Up Probe | ~8-12 | Dig deeper: "Why?", "Tell me more" |
| Raw Quote | ~15-20 | Customer's actual words |
| Job-to-Be-Done | ~6-8 | Sticky-note sized; Productside format |
| Desired Outcome | ~8-12 | Direction + Metric + Context |
| Problem | ~8-12 | Sticky-note sized; concrete observation |
| Feels/Appears | ~6-10 | Sticky-note sized; emotional/behavioral |

## Examples

Illustrative and fictional, not customer evidence.

- **Strong:** Ask a regional store manager: "Tell me about the last time inventory differed across your stores." Record the real interview separately from preparation.
- **Weak:** "Would a real-time dashboard solve your inventory problem?" leads the witness toward the proposed solution.
- **Drift to avoid:** Rehearsal as research: simulated interview answers must never enter findings as customer evidence.


## Common Pitfalls

- **Asking Leading Questions:** Strip the question of any solution language or implied answer. "How do you currently monitor [process]?" lets the customer describe their reality. "Don't you think a dashboard would help?" tells them what to say.

- **Asking Yes/No Questions:** Convert to open-ended: "Can you walk me through the last time you had to reconcile data across systems? What happened?"

- **Talking More Than 30%:** Set a physical reminder (a sticky note that says "LISTEN"). After asking a question, wait. Count to five silently before saying anything else. Silence prompts the customer to fill the gap with real insight.

- **Asking About Features Instead of Problems:** Ask about their current reality, not a hypothetical future. "What happens today when X goes wrong?" reveals the problem. "What features would fix it?" reveals the customer's guess about a solution, which is not the same thing.

- **Not Digging Deeper on Surface-Level Answers:** Probe: "Can you tell me more about how you manage it?" or "What does 'fine' look like on a bad day?" The second layer is almost always richer than the first.

- **Skipping Documentation:** Document findings within 24 hours of the interview. Use the findings board structure - it forces categorization and makes the data usable by the rest of the team.

- **Defaulting to a Tech Role:** Before drafting questions, confirm: is this the person who uses or buys the product in the field? If their primary job is not writing code or designing systems, the questions should reflect their actual daily work.

- **Treating This as a Content-Generation Skill:** Phase 3 (Document Findings) requires real interview data as input. If the PM has not talked to a customer, the agent should help with Phase 1 (Prepare Questions) and send the PM into the field. Do not fabricate findings.

- **Treating a Rehearsal as Research:** Label every rehearsal as practice at the start and the end. Refuse to document findings from a simulated interview. If the PM has no real interviews yet, help them recruit and schedule them.

- **Reading the Question List Like a Script:** Prepare around topic areas, not a script. Treat questions as starting points, follow the thread the interviewee opens, and use "Why?" and "Tell me more" to go deeper. Rehearsal (Step 6) builds the reflex.

## References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-empathy-interviews) for supporting source material and expanded examples.
