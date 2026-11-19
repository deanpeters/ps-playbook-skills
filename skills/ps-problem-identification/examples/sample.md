# ps-problem-identification Examples

## Example 1: Strong Productside-Style Artifact

This example is intentionally sanitized and fictionalized.

```markdown
# Problem Identification

## Product Context
- Product or service: Multi-site warehouse scheduling and exception-management platform
- Target persona: Alicia Operations Analyst
- Research source: 12 operations interviews plus dispatch-shadowing notes

## Customer Jobs
- Keep schedules aligned across sites
- Resolve daily exceptions quickly
- Share the latest plan with supervisors
- Prevent avoidable dock delays

## Pains
- Schedule changes arrive from too many channels
- Teams work from conflicting versions
- Exception handling depends on manual reconciliation
- Delays surface too late to prevent downstream disruption

## Gains
- One trusted operational plan
- Faster exception resolution
- Early warning on schedule risk
- More time for active coordination

## Empathy Interview Quotes
- "I spend half my shift figuring out which version is real."
- "By the time we see the issue, the dock is already backed up."
- "Every team swears they're using the latest schedule."
- "I don't need another dashboard. I need fewer surprises."
- "Most of the job is chasing changes across disconnected tools."
- "When a carrier shifts late, the whole day unravels."

## Candidate Problems
- Fragmented schedule updates get in the way of achieving one trusted operating plan for Alicia.
- Manual reconciliation gets in the way of achieving fast exception resolution for Alicia.
- Late visibility into schedule risk gets in the way of achieving preventable delay reduction for Alicia.
- Conflicting plan versions get in the way of achieving coordinated supervisor action for Alicia.
- Disconnected operational tools get in the way of achieving reliable daily execution for Alicia.
- Reactive exception handling gets in the way of achieving more time for active coordination for Alicia. [CAUSE TO VALIDATE]
```

**Why this works**

- jobs, pains, and gains are compact enough to paste into the template
- quotes sound like lived operational frustration
- problems use the Productside sentence structure
- all expected slots are filled before any commentary appears
- every quote comes from the 12 interviews named in Product Context
- each problem names a cause, not a pain reworded or a missing feature
- the one cause only two interviewees mentioned is marked `[CAUSE TO VALIDATE]`

## Example 2: Weak Overwritten Artifact

```markdown
# Problem Identification

## Customer Jobs
- Alicia is trying to orchestrate a highly dynamic multi-party logistics environment in a way that balances timing, labor coordination, and dock throughput while also maintaining communication quality across the regional network.

## Pains
- Alicia often experiences a wide range of coordination-related breakdowns that create frustration, uncertainty, duplicated work, emotional fatigue, and downstream execution confusion that affects the quality of the operating day.

## Gains
- Alicia would ideally like a future-state operating environment in which every participant has real-time shared awareness and a frictionless planning process that feels coordinated, predictable, and strategically empowering.
```

**Why this fails**

- too long to paste into the playbook
- abstract language replaces usable entries
- no supporting quotes
- turns the artifact into cleanup work for the human

## Example 3: Weak Problem Statement Pattern

```markdown
- Problem 1: Alicia is frustrated and the current workflow is not ideal.
```

**Why this fails**

- not in the Productside problem format
- too vague to guide framing
- describes dissatisfaction without naming the barrier to the outcome

## Example 4: Drift Bug: Missing Feature Named as Problem

```markdown
- Problem 1: No real-time dashboard gets in the way of achieving one trusted operating plan for Alicia.
- Problem 2: Lack of carrier integration gets in the way of achieving fast exception resolution for Alicia.
```

**Why this fails**

- each "problem" is a solution described by its absence
- the team inherits a predetermined answer before framing the problem
- fix: ask what problem the feature would solve. "Fragmented schedule updates" and "late carrier changes arriving by phone and email" keep the solution space open
