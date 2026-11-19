# Personas & Proto-Personas Prompts

**Source:** Productside Playbook, B2B work-in-progress deck (`wip-b2b-2026-11`), slides 27-29. Not yet ratified as canonical.

These are copy-paste prompts for working through the Personas & Proto-Personas Play in any chat-based AI tool. You don't need this skill installed to use them. If the skill *is* installed, it already behaves this way. It tags every line of a draft persona by where it came from, and it reviews a finished persona without adding anything your research didn't produce.

The Playbook's rule for every AI page: **you do the thinking, and AI pressure-tests it.**

## How AI Supports This Play

AI drafts your proto-persona. Give it what you and your team already believe about this user, and it turns those beliefs into a structured persona fast, so your research starts with a target instead of a blank page.

It organizes your beliefs and fills the gaps, but it marks every gap it filled. Those are guesses about your customer, and they're the first things you go test. What to believe, and what to test, stays your call.

A proto-persona is a hypothesis wearing a face. It stays provisional until research confirms it. The moment your team treats it as settled, it stops being a proto-persona and becomes a persona profile you have committed to.

| Use AI when | Avoid AI when |
|---|---|
| You are early, before research, and can name what you and your stakeholders already assume about this user, and you want it made explicit and testable. | You already have real customer research (use prompt 2 instead), or you know this proto-persona will never be validated. An untested proto-persona is just a committed stereotype. |

**Inputs you provide**

- Your target segment from Market Selection & Sizing, or any equivalent segment definition
- What you and your stakeholders already assume about this persona
- Desired outcomes for this persona from Jobs-to-Be-Done & Outcomes

**Outputs to expect**

- Each field marked as evidenced or assumed
- The riskiest assumptions marked to test first
- A plan to validate this profile through research

## Common Traps

| The assumptions are AI's, not yours | The proto-persona passes as validated |
|---|---|
| AI invents beliefs you never held | A polished draft feels finished |
| You end up validating the model's guesses | Assumptions get mistaken for facts |
| A generic stereotype, not your segment | A name and a face imply proof |
| Gap-fills you never caught | Never validated, never revisited, and the team builds on a guess |

## How to Use These Prompts

| # | Prompt | When | You bring | You commit |
|---|---|---|---|---|
| 1 | [01-draft-proto-persona.md](01-draft-proto-persona.md) | Early, before research | Segment, JTBD work, and your team's beliefs | A user persona, then a buyer persona, every line tagged FROM YOU or AI-SUGGESTED |
| 2 | [02-review-research-persona.md](02-review-research-persona.md) | After research (Empathy Interviews, Affinity Mapping, Problem Identification, Framing the Problem) | Your research-based persona and its stakeholder audience | A persona ready to share with stakeholders |

1. **Run prompt 1** once per persona. Start with the user, then the buyer. Add an influencer if one matters.
2. **Commit the persona to the template** ([../template.md](../template.md)). Keep the AI-suggested lines visible as your research list.
3. **Do the research.** The AI-suggested lines and invented quotes are what you test first.
4. **Run prompt 2** on the research-based persona, then share it with your stakeholders.

**Recommended tool type:** chat-based AI tool.

## Source Notes

Prompt text is kept verbatim from the deck, so these wording issues remain in the prompt files. They're recorded here for the Productside content team:

- Prompt 1: "Do not present any of you suggestions as fact" should read "your suggestions."
- Slide 29 title: "Part 2 or 2" should read "Part 2 of 2."
- Slide 29's instructions call the fourth Play "Problem Framing." The Play is named "Framing the Problem."
- The WIP blank template (slide 30) drops two fields the baseline template has: "What is this persona trying to do?" and "Attitudes & Influences." The skill follows the WIP and folds them into Needs | Pains and Desired Outcomes | Goals, as the WIP instruction page does.
