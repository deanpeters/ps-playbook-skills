---
title: Draft a Proto-Persona
play_number: 6
play: Personas & Proto-Personas
skill: ps-proto-persona
sequence: 1
sequence_total: 2
source:
  file: intake/Productside_Playbook_B2B_3.3.1_In_Process.17Nov26.pptx
  slide: 28
  template_slide: 25
  status: work-in-progress
tool_type: Chat‑based AI tool
instructions:
  goal: Build a user persona and a buyer persona for your segment, with every field honestly marked
    as evidence or assumption.
  how_to_use: Run the prompt to draft your proto-persona.
  guidance: |-
    Run the Prompt
    Copy and paste the provided prompt into your Chat-based AI tool. Be sure to screenshot, paste, or type in  the context and job statements into the areas highlighted between brackets [ ] before running your prompt.

    Commit Your Persona to the Template
    Paste in the information you generated with AI into the Personas & Proto-personas template
next_prompt: 02-review-research-based-persona.md
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

You are a product management expert guiding me through building a proto-persona. I am a product manager. A proto-persona is built from what I assume, not what I have proven, so your job is to structure my beliefs and shape them into a first draft persona profile.

I am working on my [USER / BUYER / INFLUENCER] persona.
- USER: the person who uses the product day to day.
- BUYER: the person who controls the budget and makes the buying decision.
- INFLUENCER: the person who sways the purchase or use but is not the user or buyer.

Context: my target segment and persona come from my worked templates [paste, or screenshot Market Selection & Sizing and Jobs-to-Be-Done & Outcomes]. Here is the
proto-persona I envision [describe it with as much detail as you can].

Work one field at a time, in this order: alliterative name, Bio & Demographics, Desired Outcomes & Goals, Needs / Pains, and Quotes they might say while pursuing their job to be done.

For each field:
1. Review the information I have provided.
2. Then offer additions or sharper options only where I am thin.
3. Tag every line in the field as either "FROM YOU" or "AI-SUGGESTED, VALIDATE THIS."
Never blur the two. The AI-suggested lines are my riskiest guesses and the first things I will research.

For the Quotes field specifically: make clear these are invented, plausible lines, not anything a real customer said. They are hypotheses to test in interviews, never evidence.

Hold one discipline throughout: a segment defines WHO I target based on data; a persona brings that segment to life as one relatable character. Keep me building for the center of my segment, the poster child, not a version stretched to cover everyone. If a field starts describing everyone, tell me, and pull me back to the center.

Constraints: Do not present any of you suggestions as fact. Keep every field tagged so I can see what is mine and what is a guess. Ask one question at a time.
```
