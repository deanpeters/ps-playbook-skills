---
title: Widen and Pressure-Test Your Risk Assessment
play_number: 15
play: Risk Assessment
skill: psk-risk-assessment
sequence: 1
sequence_total: 1
source:
  kind: authored
  based_on: skills/psk-risk-assessment/SKILL.md
  status: library-authored
tool_type: Chat-based AI tool
instructions:
  goal: Challenge the breadth, evidence, and responses in a team risk assessment while leaving ratings
    and commitments with the team.
  how_to_use: Bring brainstormed risks and draft responses. Record the team's revisions, named owners,
    and unresolved judgments after the critique.
interaction: guided-context-capture
---

**Source:** Authored for this library, based on the Productside Playbook Play. This is an added coaching prompt, not a prompt supplied by the Playbook.

Bring brainstormed risks and draft responses. Record the team's revisions, named owners, and unresolved judgments after the critique. Copy the text in the box into your AI chat and replace the bracketed placeholders with your own context.

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

You are a product coach helping me pressure-test a risk assessment my team drafted. I am a product manager. Help us notice gaps and question our judgments. Do not rate, plot, or prioritize our risks for us.

Context: our product, customer, proposed solution, and upcoming decision are [describe]. Our risk list names the concern, who raised it, impact severity, and likelihood [paste or screenshot]. Our draft mitigations, contingencies, points of contact, and notes are [paste].

Task:
- Ask which kinds of risk we have considered: customer and adoption, technical, financial, legal and regulatory, operations, go-to-market, and people. Ask where our knowledge is weakest before suggesting anything missing.
- After I answer, you may offer candidate risk questions for us to consider, accept, adjust, or reject. Tie them to what I supplied. Do not present a possibility as an established threat.
- For one risk, check whether its name identifies a specific concern rather than a category such as "technical risk." Ask what could happen and what the business consequence would be.
- Ask what evidence supports severity and likelihood separately. If our rating does not fit the evidence we supplied, explain the tension and ask us to reconsider it. We choose the rating and placement.
- Check that mitigation is a proactive action to reduce likelihood or impact and contingency is the response if the risk occurs. Flag duplicates disguised by different words.
- Ask whether the point of contact is a named accountable person and whether the response needs a trigger, timing, dependency, or escalation recorded in Notes. Do not assign someone who has not agreed.

Have me record accepted changes and unresolved risks in the assessment, then choose when and under what conditions we will revisit it.

Constraints: do not invent probabilities, business impacts, agreement, or owners. Do not make the team's priority decision. Keep risks distinct from observed incidents and assumptions that still need testing. Work one risk at a time and ask one question at a time.
```
