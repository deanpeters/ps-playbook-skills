---
name: ps-empathy-interviews
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

After the interviewee shares something significant, repeat back what you heard in your own words: "So if I understand correctly, you're saying..." This does two things: it confirms you captured their meaning accurately, and it often prompts the interviewee to correct, expand, or go deeper — surfacing nuance a follow-up probe alone might miss.

### The Findings Board Maps to Downstream Artifacts

The documentation phase produces four categories that feed directly into other playbook skills:

- **Jobs-to-Be-Done** - what the customer is trying to accomplish (feeds ps-jobs-to-be-done)
- **Desired Outcomes** - what success looks like for the customer (feeds ps-jobs-to-be-done)
- **Problems** - friction, blockers, and pain points observed (feeds ps-problem-identification)
- **Feels/Appears** - emotional and behavioral observations (feeds ps-proto-persona refinement)

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

See the original three-page playbook source in [assets/ps_empathy_interviews_playbook_pages.pdf](assets/ps_empathy_interviews_playbook_pages.pdf).

### Required Output Convention

This skill produces artifacts in **three phases**. Not all phases happen in a single session:

- **Phase 1 output:** The decision and learning objectives, 4-5 topic areas, the PM's interview questions (reviewed) with follow-up probes, and a conduct reference card. Optionally, a rehearsal and its technique review.
- **Phase 3 output:** A structured findings board with Jobs-to-Be-Done, Desired Outcomes, Problems, and Feels/Appears entries sized for the canonical template.

The PM returns to the agent after conducting the interview (Phase 2) to get help with Phase 3.

### If the PM Brings a Draft

When the PM arrives with draft questions or topic areas, review them before writing anything new. This mirrors [prompts/01](prompts/01-prepare-interview-guide.md).

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

**The PM writes the questions.** Ask the PM to draft a few questions per topic area, then review them using [If the PM Brings a Draft](#if-the-pm-brings-a-draft). If the PM asks you to draft the questions (or is in best guess mode), write 5-8 and label them a starting draft for the PM to rewrite in their own voice. Run the same review on your own draft before handing it over.

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

If the PM wants to practice, run a rehearsal drill. This mirrors [prompts/02](prompts/02-rehearse-technique.md).

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

1. **Refine the proto-persona** - update the persona with real quotes, validated pains, and observed attitudes using ps-proto-persona
2. **Move to Problem Identification** - synthesize interview findings into candidate problem statements using ps-problem-identification
3. **Conduct more interviews** - if the sample is small or the findings are inconclusive, prepare questions for another round

Present these as options, not as mandatory steps. The user decides what comes next.

## Examples

See [examples/sample.md](examples/sample.md).

The example set includes:

- a strong empathy interview artifact with well-prepared questions and structured findings
- a weak, generic version with no learning objectives and unstructured findings
- a bias-bug example showing questions that lead the interviewee toward a predetermined solution
- commentary on why the weak versions fail

## Common Pitfalls

### Pitfall 1: Asking Leading Questions

**Symptom:** "Don't you think it would be better if you had a real-time dashboard?" or "Would you agree that the current system is too slow?"

**Consequence:** The interviewee agrees to be polite or because the question frames the answer. The PM leaves with "validated" assumptions that were never actually tested.

**Fix:** Strip the question of any solution language or implied answer. "How do you currently monitor [process]?" lets the customer describe their reality. "Don't you think a dashboard would help?" tells them what to say.

### Pitfall 2: Asking Yes/No Questions

**Symptom:** "Do you find data reconciliation frustrating?" "Is the current process slow?"

**Consequence:** The PM gets confirmation without understanding. "Yes, it's frustrating" tells you nothing about why, how often, or what it costs.

**Fix:** Convert to open-ended: "Can you walk me through the last time you had to reconcile data across systems? What happened?"

### Pitfall 3: Talking More Than 30%

**Symptom:** The PM explains the product vision, describes the roadmap, or pitches features during the interview.

**Consequence:** The interview becomes a sales call. The customer mirrors the PM's language back instead of sharing their own experience.

**Fix:** Set a physical reminder (a sticky note that says "LISTEN"). After asking a question, wait. Count to five silently before saying anything else. Silence prompts the customer to fill the gap with real insight.

### Pitfall 4: Asking About Features Instead of Problems

**Symptom:** "How would you feel about a tool that automates X?" or "What features would you want in a solution?"

**Consequence:** The customer designs your product for you - poorly, because they are not product managers. You get a feature wish list instead of problem understanding.

**Fix:** Ask about their current reality, not a hypothetical future. "What happens today when X goes wrong?" reveals the problem. "What features would fix it?" reveals the customer's guess about a solution, which is not the same thing.

### Pitfall 5: Not Digging Deeper on Surface-Level Answers

**Symptom:** Customer says "It's fine" or "We manage." PM moves to the next question.

**Consequence:** The real pain is buried under social politeness. "It's fine" often means "I've accepted the pain because I have no alternative."

**Fix:** Probe: "Can you tell me more about how you manage it?" or "What does 'fine' look like on a bad day?" The second layer is almost always richer than the first.

### Pitfall 6: Skipping Documentation

**Symptom:** The PM conducts the interview, has a vivid memory of the conversation, but never structures the findings.

**Consequence:** Within 48 hours, the nuance fades. Within a week, the PM remembers their interpretation, not the customer's words. The team never sees the raw evidence.

**Fix:** Document findings within 24 hours of the interview. Use the findings board structure - it forces categorization and makes the data usable by the rest of the team.

### Pitfall 7: Defaulting to a Tech Role

**Symptom:** The PM is building a supply chain platform but prepares interview questions for a DevOps engineer or data architect.

**Consequence:** The interview explores technical implementation concerns instead of the operational workflow of the actual customer (a supply chain planner, a procurement manager, a logistics coordinator).

**Fix:** Before drafting questions, confirm: is this the person who uses or buys the product in the field? If their primary job is not writing code or designing systems, the questions should reflect their actual daily work.

### Pitfall 8: Treating This as a Content-Generation Skill

**Symptom:** The PM asks the agent to "generate empathy interview findings" without having conducted an interview.

**Consequence:** The findings are fiction. They reflect LLM training data, not the customer's reality. The team makes decisions based on plausible-sounding but unvalidated assumptions.

**Fix:** Phase 3 (Document Findings) requires real interview data as input. If the PM has not talked to a customer, the agent should help with Phase 1 (Prepare Questions) and send the PM into the field. Do not fabricate findings.

### Pitfall 9: Treating a Rehearsal as Research

**Symptom:** The PM runs an AI rehearsal, or asks AI to "interview" a synthetic customer, then pastes the simulated answers into the findings board as quotes or problems.

**Consequence:** The findings are the model's guesses in a customer's voice. The real conversation gets skipped, and the team believes it has validated something it never tested. The Playbook calls this the Play being corrupted.

**Fix:** Label every rehearsal as practice at the start and the end. Refuse to document findings from a simulated interview. If the PM has no real interviews yet, help them recruit and schedule them.

### Pitfall 10: Reading the Question List Like a Script

**Symptom:** The PM works through the prepared questions in order, word for word, and moves on as soon as each one is answered.

**Consequence:** The interviewee never gets to steer, so the stories that matter never come out. The interview confirms the PM's list instead of the customer's reality.

**Fix:** Prepare around topic areas, not a script. Treat questions as starting points, follow the thread the interviewee opens, and use "Why?" and "Tell me more" to go deeper. Rehearsal (Step 6) builds the reflex.

## References

### Skill Files

- [template.md](template.md) - three-phase scaffold: preparation, conduct guidance, findings
- [prompts/](prompts/README.md) - copy-paste prompts for chat-based AI tools (2: prepare an interview guide, rehearse technique)
- [examples/sample.md](examples/sample.md) - strong, weak, and bias-bug examples

### Related Project Docs

- [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)
- [framework-glossary.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/framework-glossary.md)
- [skill-authoring-workflow.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/skill-authoring-workflow.md)
- [template_conversion_rules.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/template_conversion_rules.md)
- [template_conversion_usage.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/template_conversion_usage.md)

### Related Skills

- [ps-proto-persona](../ps-proto-persona/SKILL.md) - upstream; persona work grounds interview question preparation; interview findings refine the persona
- [ps-jobs-to-be-done](../ps-jobs-to-be-done/SKILL.md) - parallel; JTBD output can inform interview questions; interview findings produce new job and outcome discoveries
- [ps-problem-identification](../ps-problem-identification/SKILL.md) - downstream; interview findings feed directly into problem identification

### Source Material

- [Baseline Playbook version](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml). Full source PDF supplied separately.
- [assets/ps_empathy_interviews_playbook_pages.pdf](assets/ps_empathy_interviews_playbook_pages.pdf)
- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 31-35: Template 07 of 24 there, with the AI overview on slide 33 and both prompts on slide 34. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).
