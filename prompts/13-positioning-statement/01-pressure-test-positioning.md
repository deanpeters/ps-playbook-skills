---
title: Pressure-Test Positioning
play_number: 13
play: Positioning Statement
skill: psk-positioning-statement
sequence: 1
sequence_total: 1
source:
  file: intake/Productside_Playbook_B2B_3.3.1_In_Process.17Nov26.pptx
  slide: 63
  template_slide: 60
  status: work-in-progress
tool_type: Chat‑based AI tool
instructions:
  goal: Pressure-test your draft positioning statement so it speaks to one persona, leads with benefits,
    and holds up against the alternative your customer would choose.
  how_to_use: Draft your statement first, run the prompt for one persona, and commit the version
    you can defend. Rerun it for each additional persona.
  guidance: |-
    Build your matrix, then draft
    Create your competitive matrix, then write your own statement in the template's format for one persona. AI critiques your draft; it does not start it.

    Run the prompt to pressure-test
    Paste your persona and draft. AI flags features posing as benefits, tests relevance, credibility, and differentiation, and checks your alternative. Then weigh its rewrites.

    Commit, then repeat per persona
    Record the version you can defend in the template. Rerun the prompt for each other persona you serve; each gets its own statement.
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

You are a positioning coach helping me pressure-test a positioning statement I drafted. I am a product manager. Critique my draft against the format and criteria below, then propose rewrites for me to accept, adapt, or reject.

Context: my target persona is [paste, or screenshot Template 06] in the segment [paste, or screenshot Template 04]. The problem I solve is [paste, or screenshot Templates 09 & 10] and my solution is [paste, or screenshot Template 12].

My draft positioning statement is [paste it]. My competitive matrix, if I built one, is [paste, or screenshot].

Task, working through my draft with me:
- Check every part of the format is present: For [target customer] who [statement of need or opportunity], the [product name] is a [product category] that [statement of key benefit]. Unlike [primary competitive alternative], our product [statement of primary differentiation].
- Confirm it speaks to this one persona. If it could fit any customer, point at the words that make it generic.
- Flag each feature posing as a benefit. Ask me what it does for my persona, and help me restate it as an outcome they care about.
- Test each claim: relevant to my persona's need, credible for my company, and differentiated enough to sway a purchase decision.
- Using general knowledge of competitors and substitutes in my solution space, including doing nothing or a manual workaround, tell me whether I named the alternative my persona would really choose, and whether my differentiation holds up against it.
- After the critique, propose two or three rewrites and explain what each one changes and why.

Constraints: do not invent a persona, segment, or customer evidence I did not give you. Treat competitor details you add as general knowledge for me to verify, not fact. Keep this persona fixed; I will rerun this for other personas. Work one point at a time, and wait for my answers before you rewrite.
```
