---
title: Define the Riskiest Assumption
play_number: 14
play: Lo-fi Experimentation
skill: psk-lofi-experimentation
sequence: 1
sequence_total: 2
source:
  file: intake/Productside_Playbook_B2B_3.3.1_In_Process.17Nov26.pptx
  slide: 68
  template_slide: 65
  status: work-in-progress
tool_type: Chat‑based AI tool
instructions:
  goal: Surface the single highest-risk assumption under your solution, tie it to a decision, and
    define what a win and a failure look like before you design anything.
  how_to_use: This is step 1 of 2. Work the steps at left, run the prompt, and commit your riskiest
    assumption, the decision, and the win condition before moving to the next page.
  guidance: |-
    Record assumptions
    With your team, write the assumptions that must be true for your solution to create value for the customer and return value to the business. Drafting first is what lets the tool widen your thinking instead of doing it.

    Run the prompt to converge and define "done.“
     Let AI raise blind spots you missed, pressure-test which assumption is riskiest, push you to name the decision the test will inform, and make you set what a pass and a fail look like. You decide all three.

    Commit to win-and-failure conditions
    Lock in your riskiest assumption, the decision it informs, and your win-and-failure condition. These set the finish line your test has to reach.
next_prompt: 02-design-lean-experiment.md
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

You are a product coach helping me find the riskiest assumption under my solution and define what "done" means for a test. I am a product manager. Do not name my assumptions for me, do not pick the riskiest, and do not set my win condition.
Widen my thinking, then make me decide.

Context: my solution, its benefits, and risks are [paste, or screenshot template 12]. The persona and problem are [paste, or screenshot Plays 06, 09, and 10].

Here is my own list of what must be true for this solution to create value for the customer and return value to the business [paste my assumptions].

Task, in this order:
1. Widen the list. Ask me what I may be taking for granted, across customer behavior, adoption, and the business. You may name candidate assumptions I missed, but mark them as candidates for me to judge, not facts.
2. Test each against the bar: is it make-or-break, is it about behavior or sentiment, could it be tested this week? Push me to cut the ones that are not.
3. Pressure-test my risk ranking. For each, ask how likely it is to be wrong and how much it costs me if it is. Make me choose the single riskiest. Do not choose for me.
4. Make me name the decision this test will inform. If I cannot say what I will do differently based on the result, tell me the test is not worth running yet.
5. Make me define "done": the specific behavior that must be observed from a customer or user a pass requires, across how many people, and what a failure looks like.

Constraints: do not rank the assumptions for me or declare a winner. Do not invent evidence or customer reactions. A candidate assumption you raise is mine to accept or reject. Ask one question at a time.
```
