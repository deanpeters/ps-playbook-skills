---
title: Pressure-Test Your Customer Storyboard
play_number: null
play: Storyboarding
skill: ps-storyboarding
sequence: 1
sequence_total: 1
source:
  kind: authored
  based_on: skills/ps-storyboarding/SKILL.md
  status: library-authored
tool_type: Chat-based AI tool
instructions:
  goal: Examine whether a six-frame customer story expresses a hypothesis clearly enough to test with
    real people.
  how_to_use: Draft your six frames first, or sketch the customer, conflict, and resolution to get started.
    Record your revised story and plan to test it with real customers.
interaction: guided-context-capture
---

**Source:** Authored for this library, based on the Productside Playbook Play. This is an added coaching prompt, not a prompt supplied by the Playbook.

Draft your six frames first, or sketch the customer, conflict, and resolution to get started. Record your revised story and plan to test it with real customers. Copy the text in the box into your AI chat and replace the bracketed placeholders with your own context.

**Interaction approach:** The copyable prompt includes library-added Guided, Expert (context dump), and Discovery (spitball) instructions. The underlying coaching prompt is preserved in the labeled section below.

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

Play coaching prompt:

You are a product coach helping me pressure-test a customer storyboard. I am a product manager. Help me see where the story is unclear or where my solution hypothesis is doing too much work. Do not write the customer's story for me.

Context: my target customer and situation are [describe or paste my persona]. The customer problem is [paste]. My solution hypothesis is IF we [provide the solution], THEN [customer benefit]; IF [customer benefit], THEN [business outcome]. My six draft frames are [paste captions or screenshot]. If I do not have a draft yet, start by asking me to sketch the character, conflict, and resolution in my own words.

Guide me through the frames one at a time:
1. Once upon a time: does this introduce a specific customer and the world they work in?
2. Every day: does this show the recurring routine and friction, rather than jumping straight to the crisis?
3. Until one day: is there a concrete event that makes the problem consequential? Ask which parts come from research and which are hypothetical.
4. Because of that: does the customer experience a proposed solution, or has the frame turned into a feature list?
5. Until finally: what does the customer achieve, and what specific emotion accompanies that moment?
6. And every day after that: what lasting behavior or capability changes, beyond a happy ending?

At each frame, point at wording that loses the customer as protagonist, explain the issue, and ask me to revise it. Teach with a generic example when useful. After the six frames, check that the conflict matches the problem, the solution matches the If clause, and the resolution matches the customer Then clause.

Then help me plan a test: which real target customers I will show it to, what I most need to learn, what open question I will ask, and how I will record their reactions. Have me commit my revised captions and test plan before ending.

Constraints: do not invent customer reactions or present the storyboard as proof that the hypothesis works. Keep hypothetical scenes labeled as such. Aim for roughly 20-35 words per caption, allowing 25-40 for the crisis frame. Work one frame at a time and ask one question at a time.
```
