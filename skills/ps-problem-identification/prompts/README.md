# Problem Identification Prompts

**Source:** Productside Playbook, B2B work-in-progress deck (`wip-b2b-2026-11`), slides 43-44. Not yet ratified as canonical.

This is a copy-paste prompt for shaping problem statements in any chat-based AI tool. You don't need this skill installed to use it. If the skill *is* installed, it already behaves this way. It asks you for the root cause beneath each pain instead of naming it, catches features posing as problems, and marks every cause still to be validated.

The Playbook's rule for every AI page: **you do the thinking, and AI pressure-tests it.**

## How AI Supports This Play

You have done the research and learning. AI helps you turn it into clear problem statements. Feed it your affinity themes, interview insights, jobs, and personas, and it shapes scattered notes into sharp, well-formed problems.

Its most useful job is separating pains from problems. A pain is what your customer feels; a problem is the root cause beneath it. AI coaches that distinction and formats the result, but the cause has to come from you.

A clean problem statement is not a proven one. The format makes your thinking legible, not correct. The root cause you name stays a hypothesis until your interviews back it, and that diagnosis is yours to own.

| Use AI when | Avoid AI when |
|---|---|
| You have real insights from your affinity map and interviews and want help shaping them into clear problem statements that separate symptoms from causes. | You have not talked to customers yet. AI will format confident root causes and problem statements you cannot defend. |

**Inputs you provide**

- Themes and insights from your affinity map and interviews
- The outcomes and personas these problems serve
- The pains you heard, plus your first read on their causes

**Outputs to expect**

- Pains separated from the root causes beneath them
- Problem statements in one clear, consistent format
- Guessed root causes marked for you to validate

## Common Traps

| A pain confused for a problem | Format mistaken for proof |
|---|---|
| A symptom reworded as the root cause | A polished statement on thin evidence |
| A missing feature named as the problem | Structure mistaken for rigor |
| No cause beneath the statement | Accepted because it looks right |
| The format hides the skipped diagnosis | The root cause is still a guess |

## How to Use This Prompt

1. **Gather your raw material.** Bring your affinity themes, interview insights, jobs and outcomes, personas, and the pains you heard. This is the evidence you will shape.
2. **Run the prompt to separate and format.** Sort the pains from the causes beneath them, then write each problem in the template's format. You name the root cause; AI helps you spot symptoms and sharpen the wording.
3. **Commit your problem statements.** Record each as `[Problem] gets in the way of achieving [Outcome] for [Persona]` in the template ([../template.md](../template.md)), marking any cause you still need to validate.

| # | Prompt | Goal | You bring | You commit |
|---|---|---|---|---|
| 1 | [01-shape-problem-statements.md](01-shape-problem-statements.md) | Turn research into problem statements that separate pains from root causes | Affinity themes, insights, jobs, outcomes, personas, pains, your first read on causes | Problem statements, with unvalidated causes marked |

**Recommended tool type:** chat-based AI tool.

## Source Notes

- The AI overview (slide 43) cites its inputs as "Plays 07, 08" and "Plays 05, 06," using the WIP deck's numbering (Empathy Interviews, Affinity Mapping, Jobs-to-Be-Done, Personas).
- In the baseline deck's example (Internal Teams, slide 26), two of six problem statements name a missing feature as the problem ("Lack of system integration..." and "No automated compliance alerts..."). That is the "missing feature named as problem" trap on this Play's new AI page. The WIP deck's Airport Security example avoids it.
