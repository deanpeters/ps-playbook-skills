# Lo-fi Experimentation Prompts

**Source:** Productside Playbook, B2B work-in-progress deck (`wip-b2b-2026-11`), slides 67-69. Not yet ratified as canonical.

These are copy-paste prompts for finding the riskiest assumption under a solution and designing the leanest test for it, in any chat-based AI tool. You don't need this skill installed to use them. If the skill *is* installed, it already behaves this way. It widens your list of assumptions and pressure-tests your risk ranking, but you choose the riskiest, the decision, and what a pass looks like.

The Playbook's rule for every AI page: **you do the thinking, and AI pressure-tests it.**

## How AI Supports This Play

Lo-fi experimentation is how you buy evidence cheaply, before you spend a quarter building the wrong thing. AI works as a thought partner in two moments. First, after you list what must be true for your solution to pay off, it widens your view toward the assumptions you cannot see on your own and pressure-tests which one is genuinely riskiest. Then it helps you design the smallest, fastest test that could prove you wrong.

The reasoning stays yours. You name the assumptions, you rank the risk, you decide what a pass looks like and what you will do about it. If AI hands you the riskiest assumption, you have skipped the thinking that tells you whether you understand your own idea.

A test exists to settle a decision. AI sharpens the probe. The signal comes from real people, never from the model.

| Use AI when | Avoid AI when |
|---|---|
| You have a prioritized solution and want to find the riskiest assumption under it, then design a cheap, fast experiment that drives a real decision. | Your problem, persona, or solution is still vague. AI will manufacture confident assumptions and a tidy test with nothing real beneath them. |

**Inputs you provide**

- Your solution hypothesis
- The persona and problem it serves
- Your own first pass at what must be true for your solution idea to work

**Outputs to expect**

- Blind-spot assumptions you missed, raised for you to weigh
- A single riskiest assumption, tied to a decision
- The smallest test that produces a real pass-or-fail signal

## Common Traps

| AI names your assumptions | The test grows, or decides nothing |
|---|---|
| You ask AI what must be true | The experiment is bigger than the question needs |
| The riskiest one is AI's pick | A measure for success was never defined |
| Blind spots stay invisible to you | It gathers "nice-to-know," not "need-to-know," evidence |
| The risk ranking is borrowed, not reasoned | |

## How to Use These Prompts

Commit each step to the template ([../template.md](../template.md)) before moving on.

| # | Prompt | Goal | You bring | You commit |
|---|---|---|---|---|
| 1 | [01-find-riskiest-assumption.md](01-find-riskiest-assumption.md) | Surface the single riskiest assumption, tie it to a decision, define win and failure | Solution, persona, problem, and your own list of assumptions | Riskiest assumption, the decision it informs, win-and-failure condition |
| 2 | [02-design-leanest-test.md](02-design-leanest-test.md) | Turn it into an If/then hypothesis and the leanest experiment that produces that signal | Your finish line from prompt 1 | Method, audience, metric, time window, decision rule. Then build only enough to run it. |

**Recommended tool type:** chat-based AI tool. Prompt 2 asks it to search the web for more test methods.

## Source Notes

- Slide 68: the step heading “Run the prompt to converge and define ‘done.’” opens with a straight quote and closes with a curly one.
- Slide 69 lists a "vibe coded prototype" among lightweight methods. The baseline deck's worked example used "Vibe Coding and Synthetic Data" with 100 simulated users as the audience. The WIP example replaces it with a Wizard-of-Oz test on 8-10 real passengers. The skill treats a vibe-coded prototype as a stimulus shown to real people, never as a source of simulated participants.
