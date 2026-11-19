# Measuring Outcomes Prompts

**Source:** Productside Playbook, B2B work-in-progress deck (`wip-b2b-2026-11`), slides 103-104. Not yet ratified as canonical.

This is a copy-paste prompt for grading the product success metrics you drafted, in any chat-based AI tool. You don't need this skill installed to use it. If the skill *is* installed, it already behaves this way. It sorts your metrics, sends business results and survey scores back for a rethink, and widens the behaviors you could watch. It doesn't pick your metrics.

The Playbook's rule for every AI page: **you do the thinking, and AI pressure-tests it.**

## How AI Supports This Play

A product outcome moves when customers change their behavior. This Play makes sure you are measuring that change, not the things that are easier to count. AI sorts the metrics you drafted, tells you which ones track real customer behavior toward your outcome and which are business results, operational plumbing, or a reflexive satisfaction score, then pushes you to imagine behaviors worth watching.

What AI cannot do is tell you the outcome was met. That verdict comes from real data, read by you, and a metric AI proposes is a candidate to weigh, never an answer to adopt.

A product success metric is a leading indicator: the customer behavior that, when it moves, should pull the business outcome up behind it. Measure the behavior, not just the money that follows.

| Use AI when | Avoid AI when |
|---|---|
| You have product outcomes from the Outcome Tree and want metrics that prove customers are behaving the way the outcome predicts. | Your product outcome is vague, or is really a business outcome. AI will hand you confident metrics aimed at the wrong target. |

**Inputs you provide**

- Your business and product outcomes from the Outcome Tree
- Your draft success and health metrics
- How each metric could realistically be measured

**Outputs to expect**

- Each metric sorted into success, health, or business
- Lagging and lazy metrics sent back for a rethink
- Customer behaviors that signal the outcome is moving

## Common Traps

| Business outcomes disguised as product outcomes | Health metrics posing as success |
|---|---|
| Revenue counted as product success | Uptime logged as progress |
| A lagging number, not leading | An operational guardrail called an outcome |
| Customer behavior never measured | Plumbing mistaken for value |

## How to Use This Prompt

1. **Define your success metrics.** Turn your product outcome into customer behaviors that show it is moving, not business results or survey scores. Run the prompt on your draft.
2. **Define your health metrics.** Name the operational guardrails that keep the product running, and keep them out of your success list.
3. **Tie metrics to measurement.** Give each metric a real way to be measured, confirm your success metrics lead the business outcome, and watch for tradeoffs.

Commit each set to the template ([../template.md](../template.md)) before the next.

| # | Prompt | Goal | You bring | You commit |
|---|---|---|---|---|
| 1 | [01-grade-success-metrics.md](01-grade-success-metrics.md) | Success metrics that capture customer behavior leading the outcome | Product outcome, business outcome, your draft success metrics | Graded success metrics, each a customer behavior with a way to measure it |

**Recommended tool type:** chat-based AI tool.

## Source Notes

- Slide 104 lists three steps (success metrics, health metrics, measurement) but provides one prompt, for success metrics. Steps 2 and 3 are done in the template; the skill covers all three.
- The WIP example's first success metric is a survey score ("Screening awareness survey improvement of 50%"), the kind of metric the prompt pushes back on.
- The baseline example's health metrics were NPS, CSAT, and churn. The WIP example's are operational (uptime, feature usage, detection accuracy).
