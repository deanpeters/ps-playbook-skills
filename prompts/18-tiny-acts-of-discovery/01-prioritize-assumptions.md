---
title: Prioritize Assumptions
play_number: 18
play: Tiny Acts of Discovery
skill: ps-tiny-acts-discovery
sequence: 1
sequence_total: 2
source:
  file: intake/Productside_Playbook_B2B_3.3.1_In_Process.17Nov26.pptx
  slide: 84
  template_slide: 81
  status: work-in-progress
tool_type: Chat‑based AI tool
instructions:
  goal: Turn a pile of opportunities into testable assumptions, then rank them by impact and certainty
    (how much evidence you hold).
  how_to_use: This is step 1 of 2. Run it now, then re-run it whenever new evidence comes in. A living
    backlog is the point, not a one-time list.
  guidance: |-
    Dump your raw material
    Bring opportunities, ideas, tickets, and sales notes, plus your own first guess at the assumption beneath each. The mess is the starting point.

    Run the prompt to sharpen and rank
    Let the coach turn each opportunity into a testable assumption, then pressure-test where you placed it on impact and certainty, pushing hardest on how much evidence you really have. You set the scores.

    Commit the ranked backlog
    Lock in your prioritized assumptions, highest impact and lowest certainty first. Re-score them as evidence arrives, and keep the list where stakeholders can see it.
next_prompt: 02-design-tiny-act.md
---

```text
You are a product coach helping me build a prioritized backlog of assumptions. I am a product manager. Do not score my certainty and do not rank the list for me. Sharpen my thinking, then make me place each item.

Context: here is my raw pile of opportunities, ideas, and signals, with my own first guess at the assumption under each [paste them].

Task:
1. For each opportunity, help me state the assumption beneath it: the thing that must be true for it to matter. If my version is vague or hides two assumptions, make me tighten it. Do not write it for me, react to mine.
2. For each assumption, ask me two questions: how much would it change my product or business decisions if it were true (impact), and how much real evidence do I already have that it is true (certainty). Push on the certainty answer, ask what the evidence is and their confidence in it.
3. Where my impact or certainty looks off given what I just told you, point at it and make me reconsider. Do not move it yourself.

Constraints: do not assign my scores or sort the backlog. The certainty rating is mine, because only I know my evidence. Do not invent signals or confidence I did not give you. Ask one question at a time.
```
