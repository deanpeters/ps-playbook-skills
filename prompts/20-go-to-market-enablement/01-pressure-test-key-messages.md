---
title: Pressure-Test Key Messages
play_number: 20
play: Go-to-Market Enablement
skill: ps-go-to-market
sequence: 1
sequence_total: 2
source:
  file: intake/Productside_Playbook_B2B_3.3.1_In_Process.17Nov26.pptx
  slide: 95
  template_slide: 92
  status: work-in-progress
tool_type: Chat‑based AI tool
instructions:
  goal: Sharpen benefit-led key messages for your user and buyer personas, each backed by proof points
    they would trust.
  how_to_use: This is step 1 of 2. Draft your messages first, run the prompt, and commit what survives
    before moving to launch goals.
  guidance: |-
    Draft for user and buyer
    Pick at least one user and one buyer persona. Write two or three benefit-led messages for each, with proof points behind every message.

    Run the prompt to pressure-test
    AI flags features posing as benefits, jargon, drift from your positioning, and proof your persona would not trust. Then weigh its rewrites.

    Commit messages and proof
    Record each persona's messages and proof points in the template. Note any proof you still need to gather before launch.
next_prompt: 02-pressure-test-launch-goals.md
---

```text
You are a product marketing coach helping me pressure-test the key messages and proof points I drafted for a launch. I am a product manager. Critique my drafts, then propose rewrites for me to accept, adapt, or reject.

Context: my positioning statement is [paste, or screenshot Template 13]. My personas, at least one user and one buyer, are [paste, or screenshot Template 06]. My solution summary is [paste, or screenshot Template 12].

My draft key messages and proof points, by persona, are [paste, or screenshot].

Task, one persona at a time:
- Confirm I have at least one user and one buyer persona. If not, ask me who uses the product and who decides to buy it.
- Check each message is a benefit this persona cares about. If it is a feature, ask me "so that what?" until I reach the benefit.
- Check each message traces back to my positioning statement, and point at any that drift from it.
- Flag jargon that sales, marketing, or support could misread, or that this persona would never say.
- For each proof point, ask whether this persona would trust it and whether it really backs the message. Point at any message with no proof behind it.
- Show me where my user and buyer messages overlap; a buyer usually cares about different outcomes than a user.
- After the critique, propose rewrites and explain what each one changes and why.

Constraints: do not invent personas, quotes, testimonials, test results, or data as proof. You may suggest types of proof I could gather, labeled as proof I still need. Work one persona at a time, and wait for my answers before you rewrite.
```
