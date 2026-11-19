---
name: find-riskiest-assumption
title: "Find Your Riskiest Assumption and Define Done"
play: Lo-fi Experimentation
skill: ps-lofi-experimentation
sequence: 1 of 2
source: playbook
source_version: wip-b2b-2026-11
source_slides: [68]
tool_type: chat-based
inputs:
  - "Your solution, its benefits, and its risks (Solution Hypothesis Statement, or equivalent)"
  - "The persona and problem it serves"
  - "Your own list of what must be true for the solution to create value for the customer and return value to the business"
commits: "Your riskiest assumption, the decision it informs, and your win-and-failure condition"
next: 02-design-leanest-test.md
---

Before you run this, write down with your team the assumptions that must be true for your solution to work. Drafting first is what lets the tool widen your thinking instead of doing it.

Copy everything inside the box below into your chat-based AI tool. Replace each `[ ]` with your own work before you run it. Pasting, typing, or attaching a screenshot all work.

```text
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
