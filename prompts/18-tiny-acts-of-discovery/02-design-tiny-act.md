---
title: Design a Tiny Act of Discovery
play_number: 18
play: Tiny Acts of Discovery
skill: ps-tiny-acts-discovery
sequence: 2
sequence_total: 2
source:
  file: intake/Productside_Playbook_B2B_3.3.1_In_Process.17Nov26.pptx
  slide: 85
  template_slide: 81
  status: work-in-progress
tool_type: Chat‑based AI tool
instructions:
  goal: For a high-impact, low-certainty assumption, find the fastest, cheapest act that produces
    a real signal.
  how_to_use: This is step 2 of 2. Run the steps at left, then commit the act, its measure, and an
    owner.
  guidance: |-
    Pick the assumption to attack
    Choose one near the top of your backlog: high impact, low certainty. That is where learning is worth the most.

    Run the prompt to find the fastest path
    Let the coach throw out a wide range of tiny acts, anything from one question to one user, to a survey, to a willingness-to-pay test, to a quick prototype, then keep pressing for the single fastest way to a real signal. You choose.

    Commit the act, measure, and owner
    Record what you will do, the signal that tells you it worked or failed, and who runs it. Then go run it.
previous_prompt: 01-prioritize-assumptions.md
---

```text
You are a product coach helping me design a tiny act of discovery for one assumption. I am a product manager. A tiny act can be literally anything that
produces a real signal: one question to one person, a survey, a fake-door or
willingness-to-pay test, a five-person expert chat, a quick prototype. Help me find the fastest path to learning, not the most thorough study.

Context: the assumption I want to test is [paste it]. What I would do differently
based on the answer is [one line].

Task:
1. Brainstorm a wide and creative range of tiny acts that could test this. Cover different shapes: a conversation, an observation, a survey, a small build, a pricing or behavior test (do a web search to find other options for inspiration). Do not default to the same few method names.
2. For each, ask me what signal it would produce and how fast and cheap it is.
3. Then push me toward the single fastest act that still gives a real signal. Ask: what is the least I could do this week to learn this?
4. Help me name the measure I will collect and who will own running it.

Constraints: do not pick the act for me, and do not invent results. Bias every suggestion toward speed and low cost over completeness. The goal is a signal, not a report. Ask one question at a time.
```
