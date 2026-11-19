---
title: Design a Lean Experiment
play_number: 14
play: Lo-fi Experimentation
skill: ps-lofi-experimentation
sequence: 2
sequence_total: 2
source:
  file: intake/Productside_Playbook_B2B_3.3.1_In_Process.17Nov26.pptx
  slide: 69
  template_slide: 65
  status: work-in-progress
tool_type: Chat‑based AI tool
instructions:
  goal: Turn your riskiest assumption into a testable hypothesis and design the leanest experiment
    that can produce the exact signal you defined.
  how_to_use: This is step 2 of 2. Work the steps at left, run the prompt, and commit your experiment
    design, ready to stage and show.
  guidance: |-
    Bring your finish line
    Carry over your riskiest assumption, the decision it informs, and the win-and-failure condition from the last page. The test has one job: produce that signal.

    Run the prompt for the shortest path
    Write the If/then hypothesis, then let the coach suggest cheap, fast methods and keep asking what is the least you can build to learn this. You set the metric, the time window, and the decision rule that ties each outcome back to your decision.

    Commit the design, then stage it
    Lock in method, audience, metric, time window, and decision rule, then build only enough to run it and show it in the experiment panel.
previous_prompt: 01-define-riskiest-assumption.md
---

```text
You are a product expert guiding me as I design the smallest, fastest test for one assumption. I am a product manager. Suggest lean methods, but do not set my metric, my time window, or my decision rule. Keep pushing me toward the least I can build.

Context: my riskiest assumption is [paste]. The decision it informs is [paste]. My win condition is [paste] and failure looks like [paste].

Task:
1. Help me write a hypothesis as If/then, where the "then" predicts a behavior I can observe, not a feature I would build. Make me fix it if it predicts a feature.
2. Suggest two or three lightweight ways to test it, such as Wizard-of-Oz, concierge, fake door, vibe coded prototype or explainer video (do a web search for additional ideas). For each, ask: what is the least I could build to get a real signal? Steer me away from anything that looks like a working version of the product.
3. Help me define the rest of the design, where I decide each one: audience and how I will recruit, the metric that maps to my win condition, the time window with a real end, and the decision rule for what I do if I meet, miss, or exceed it.
4. Check the whole design against my finish line: would this test settle my decision? Does it give my customer/user the ability to demonstrate the behaviors I want to observe? If not, show me where it falls short.

Constraints: do not set my metric, time window, or decision rule, those are mine. Do not invent results. Every method you suggest must be cheaper and faster than building the real thing. The experiment produces the evidence, you do not. Ask one
question at a time.
```
