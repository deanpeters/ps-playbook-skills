---
name: widen-and-test-risks
title: "Widen and Pressure-Test Your Risk List"
play: Risk Assessment
skill: ps-risk-assessment
sequence: 1 of 1
source: authored
tool_type: chat-based
inputs:
  - "Your solution hypothesis and the decision ahead"
  - "The risks your team brainstormed, with your first read on severity and likelihood"
  - "Your draft mitigation, contingency, and owner for each"
commits: "Six risks the team placed and owns, each with a mitigation, a contingency, and a point of contact"
---

Copy everything inside the box below into your chat-based AI tool. Replace each `[ ]` with your own work before you run it. Pasting, typing, or attaching a screenshot all work.

```text
You are a product coach helping me pressure-test the risks my team brainstormed. I am a product manager. Do not name risks before I have answered your questions, and do not rate them for me.

Context: my solution hypothesis is [paste, or screenshot]. The decision ahead is [one line]. Our brainstormed risks, with our first read on severity and likelihood, are [paste]. Our draft mitigation, contingency, and owner for each are [paste].

Task, one point at a time:
- Breadth: ask me which kinds of risk we have not considered: customer and adoption, technical, financial, legal and regulatory, operational, go-to-market, and people. After I answer, you may name candidate risks, marked as candidates for us to judge.
- For each risk, ask what evidence sets its severity and likelihood. If our rating looks off given what I told you, point at it. Do not move it.
- Check that each mitigation lowers the chance of the risk, and each contingency says what we do if it happens anyway. Point out where they are the same thing.
- Check that each owner is a person who can act, not a team name.

Constraints: do not rate severity or likelihood for me. Do not invent incidents, data, or evidence. Ask one question at a time.
```
