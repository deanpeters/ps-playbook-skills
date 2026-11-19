---
title: Check Job Statements
play_number: 5
play: Jobs-to-Be-Done & Outcomes
skill: psk-jobs-to-be-done
sequence: 1
sequence_total: 2
source:
  file: intake/Productside_Playbook_B2B_3.3.1_In_Process.17Nov26.pptx
  slide: 22
  template_slide: 19
  status: work-in-progress
tool_type: Chat‑based AI tool
instructions:
  goal: Build a clean set of job statements for the potential customers operating in your segment.
  how_to_use: Capture context from your previous templates, draft your job statements, and run the
    prompt to check your work.
  guidance: |-
    Set the Context
    Review & capture the work you did the Market Selection & Sizing Template

    Write Your Job Statements
    Draft your Functional, Social, Emotional job statements in the Jobs-to-Be-Done & Outcomes Template for potential customers in your selected segments.

    Run the Prompt
    Copy and paste the provided prompt into your Chat-based AI tool. Be sure to screenshot, paste, or type in  the context and job statements into the areas highlighted between brackets [ ] before running your prompt.
next_prompt: 02-check-product-outcomes.md
interaction: guided-context-capture
---

**Interaction approach:** The copyable prompt includes library-added Guided, Expert (context dump), and Discovery (spitball) instructions. The underlying Playbook prompt is preserved in the labeled section below.

```text
Guided context capture (library-added interaction instructions):

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

Original Playbook prompt (unchanged):

You are a product expert helping me with a Jobs-to-Be-Done exercise. I am a product manager. I have already drafted job statements for my target persona, and I want you review my work to ensure I have written the statements in the correct format and not confused Jobs-to-Be-Done with Outcomes.

Context: my target segment and customers are [paste, or screenshot my work from the Market Selection & Sizing Template].

Evaluate the job statements I have written for this persona [paste, or screenshot your completed job statements.]

Then, evaluate them using the following information.

Ensure job statements fit the following templates:

Functional Jobs
[Action verb] + [object of the action]

Emotional Jobs
Feel [Emotion] when [Circumstance]

Social Jobs
Seen as [Social Perception] to [whom]

PMs frequently write outcome statements and mislabel them as Jobs-to-Be-Done, conflating what customers are trying to accomplish (jobs) with how they measure success (outcomes). Jobs define the scope of work; outcomes define the success criteria within that scope. Mixing them undermines a PMs ability to conduct rigorous opportunity analysis and typically results in feature-driven thinking rather than genuine customer-centered innovation.

A job describes what the customer is trying to accomplish in a specific situation. It is not a feature request and it is not a task in your product. It is the progress the customer wants to make in their life or work, including functional, emotional, and social dimensions.

Jobs are intentionally stable. Products, tools, and workflows change. Jobs persist. When product teams anchor on jobs, they avoid building solutions that only make sense for today’s implementation.

It is important to always think beyond functional and include emotional and social jobs so products and messages resonate with the persona.

It is important to NOT include outcomes and solutions in a job-to-be-done statement. If we mix outcomes and solutions into the job statement, we lose clarity and bias our thinking towards a specific product or feature. A clean job statement ensures we stay focused on the customer’s goal, not our assumptions.
```
