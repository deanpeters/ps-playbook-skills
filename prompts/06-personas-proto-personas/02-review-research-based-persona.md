---
title: Review a Research-Based Persona
play_number: 6
play: Personas & Proto-Personas
skill: ps-proto-persona
sequence: 2
sequence_total: 2
source:
  file: intake/Productside_Playbook_B2B_3.3.1_In_Process.17Nov26.pptx
  slide: 29
  template_slide: 25
  status: work-in-progress
tool_type: Chat‑based AI tool
instructions:
  goal: Evaluate your persona profile to sharpen your evidence-based research and properly communicate
    who your product serves.
  how_to_use: After you have done your research and validated your proto-persona, come back to this
    prompt to have AI evaluate your work and offer suggestions for how to improve it. This prompt
    works best after you have used the Empathy Interview, Affinity Mapping, Problem Identification,
    and Problem Framing  templates
  guidance: |-
    Run the Prompt
    Copy and paste the provided prompt into your Chat-based AI tool. Be sure to screenshot, paste, or type in  the context and job statements into the areas highlighted between brackets [ ] before running your prompt.

    Share your Persona Profile
    You’re ready to share your persona with stakeholders!
previous_prompt: 01-draft-proto-persona.md
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

You are a product management expert reviewing a finished, research-based persona I built. I am a product manager. A persona is a communication tool: its job is to help my stakeholders quickly understand and empathize with the people we serve. Evaluate mine against that bar and help me improve it.

Context: here is my persona profile [upload it, or paste or screenshot it]. It is based on real research. This persona represents a [USER / BUYER / INFLUENCER]. My audience is my stakeholders [name them, for example executives, sales, marketing, engineering, design], who need to make product decisions with this person in mind.

Start by telling me, in one honest read, whether this persona is already good enough to put in front of my stakeholders. If it is, say so plainly and stop me from over-polishing.

If it is not yet there, work through it with me one dimension at a time. For each, tell me what works, name the one change that would most improve it, and offer a concrete suggestion I can accept, adjust, or reject.
- Clarity: could a busy stakeholder grasp who this person is in under a minute?
- Story: do the pieces add up to one believable, coherent person?
- Empathy: would my stakeholders feel this person's goals and pains?
- Relevance: is it clear why this person matters to our product decisions?
- Focus: is this the specific center of one segment, or a blurry everyone?

Prioritize. Give me the three to five changes that matter most for communicating this persona, and tell me which weak spots are minor enough to leave alone. When the persona is fit for purpose tell me it is ready and that further polishing is not
worth my time.

Constraints: your suggestions may sharpen wording, structure, and emphasis, but must not add attributes, quotes, or data my research did not produce. Improving how a real finding is communicated is fair; inventing new substance is not. Aim to drive stakeholder empathy, not a perfect document. Ask one question at a time.
```
