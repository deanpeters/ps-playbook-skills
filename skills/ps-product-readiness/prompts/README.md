# Product Readiness Testing Prompts

**Source:** authored for this library. Not yet in the Productside Playbook. This Play is Template 21 of 24 in the B2B work-in-progress deck (slides 98-100), which has no AI page for it. The prompt follows the style of the deck's own AI prompts and apply its global rule.

This is a copy-paste prompt for working this Play in any chat-based AI tool. You don't need this skill installed to use it. If the skill *is* installed, it already behaves this way.

The Playbook's rule for every AI page: **you do the thinking, and AI pressure-tests it.**

## How AI Supports This Play

AI works here as a critic of the readiness test plan the PM drafted. It checks that participants are defined by profile, that goals have numeric targets resting on a baseline, that Go/No Go criteria are committed before the test, and that quote capture is planned. The targets and the Go/No Go criteria are the PM's to set.

| Use AI when | Avoid AI when |
|---|---|
| The PM has a draft readiness test plan and wants it pressure-tested before the test starts. | The request is to set the Go/No Go thresholds, or to predict how participants will react. |

**Outputs to expect:** participant profiles sharpened, each goal checked for a measure and a baseline, Go/No Go criteria tested for whether they would really stop a launch, and gaps in quote capture and scope flagged.

## Common Trap

**Thresholds Nobody Chose.** The PM asks for Go/No Go criteria and gets "Go if task success is above 85% and CSAT is above 4.2." The thresholds have no baseline and no owner. When results land at 83%, nobody knows whether to stop the launch.

## How to Use This Prompt

Draft your own work first, then run the prompt, and commit what survives to the template ([../template.md](../template.md)).

| # | Prompt | Goal | You bring | You commit |
|---|---|---|---|---|
| 1 | [01-pressure-test-readiness-plan.md](01-pressure-test-readiness-plan.md) | Pressure-Test Your Readiness Test Plan | Your solution and personas; Your draft readiness test plan: customer profiles, participants, duration, team roles, goals with targets, Go/No Go criteria, and out-of-scope assumptions and risks | A readiness plan with real participant profiles, goals with grounded targets, and Go/No Go criteria committed before the test |

**Recommended tool type:** chat-based AI tool.
