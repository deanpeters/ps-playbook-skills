# ps-proto-persona Examples

## Example 1: Strong Productside-Style Proto-Persona

This example is intentionally sanitized and fictionalized. It shows the **working draft**, with a provenance tag on every line. The committed copy has the same content with the tags moved out of the fields.

```markdown
# Proto-Persona

## Persona Type
- User, Buyer, or Influencer: User
- Validation status: Proto-persona
- Confidence level: Medium

## Product Context
- Product or service: Multi-site warehouse scheduling and exception-management platform
- Problem space: Coordinating labor, carrier timing, and dock availability across shifting daily demand
- Why this persona matters: This person experiences the operational chaos the product is meant to reduce

## Name & Portrait
- Name: Alicia Operations Analyst
- Portrait description: Early-career operations analyst managing same-day schedule changes across three warehouse sites

## Bio & Demographics
- Role / title: Operations Analyst [FROM YOU]
- Industry or operating context: Regional logistics network [FROM YOU]
- Organization context: Mid-sized distribution company with three warehouses and mixed in-house / third-party carriers [FROM YOU]
- Seniority or experience level: 4 years in operations planning [AI-SUGGESTED, VALIDATE THIS]
- Relevant demographics: Comfortable with spreadsheets and operations systems; not deeply technical [RESEARCH]
- Backstory: Alicia inherited a patchwork planning process and is now the person everyone pings when inbound and outbound schedules break [FROM YOU]

## Quotes
- Quote 1: "I rework half the day by hand." [AI-SUGGESTED, VALIDATE THIS]
- Quote 2: "We have five versions of the schedule." [AI-SUGGESTED, VALIDATE THIS]
- Quote 3: "I need fewer surprises at 2 p.m." [AI-SUGGESTED, VALIDATE THIS]

## Needs | Pains
- Pain or need 1: Manual reconciliation across tools [RESEARCH]
- Pain or need 2: Low confidence in one shared plan [FROM YOU]
- Pain or need 3: Blame for downstream delays [AI-SUGGESTED, VALIDATE THIS]
- Trying to accomplish: keep schedules aligned, resolve daily exceptions, prevent avoidable delays [FROM YOU]

## Desired Outcomes | Goals
- Desired outcome or goal 1: Less time on reconciliation [FROM YOU]
- Desired outcome or goal 2: One trusted operating plan [FROM YOU]
- Desired outcome or goal 3: Fewer preventable delays [AI-SUGGESTED, VALIDATE THIS]
- Attitudes and influences: Trusts warehouse supervisors and peer planners [FROM YOU]; won't adopt anything that slows shift-start [RESEARCH]; values tools that reduce fire-drills over "visibility" [AI-SUGGESTED, VALIDATE THIS]

## Proto-Persona Caveats
- This is still a proto-persona, not a validated persona.
- Likely areas to validate next: desired confidence threshold, precise influence network, and what information Alicia trusts first during live disruption.
- Evidence sources: support ticket themes from two sites (reconciliation, duplicate entry); a public operations analyst job posting (tools and technical level)

## Riskiest Assumptions
1. Blame for downstream delays is a top pain, not just a frustration (test first: it shapes the whole emotional story)
2. The 2 p.m. surprise pattern is real across sites, not just at one
3. She trusts tools that fit existing routines over tools that change them

## Buyer Relationship
- Is this person also the buyer? No
- If not, who likely buys or approves? Operations director or VP of supply chain
- What tension might exist between user needs and buyer priorities? Buyer may focus on cost and throughput while Alicia cares about fewer surprises and clearer coordination

## Research Next Steps
- Who should we interview next? Warehouse supervisors, transportation manager, second-site planner
- What should we validate first? Whether exception resolution speed is more painful than schedule creation itself
- Which assumptions are riskiest? What "good enough coordination" looks like during live operational pressure
```

**Why this works**

- customer-side person is clear
- quotes sound like a real operator, not marketing copy
- pains and desired outcomes are separated
- the main sections are compact enough to paste back into the playbook
- proto status is explicit, and every line shows whether it came from the team, from research, or from the model
- invented quotes are tagged as invented, so nobody repeats them as customer evidence
- the Riskiest Assumptions list turns the AI-suggested lines into a research plan
- buyer is acknowledged without replacing the user
- tags sit at the end of each line, so the committed copy is clean once they are moved out of the fields

## Example 2: Weak Generic Persona

```markdown
# Proto-Persona

## Persona Type
- User or Buyer: User
- Validation status: Proto-persona
- Confidence level: High

## Product Context
- Product or service: Software
- Problem space: Efficiency
- Why this persona matters: Important user

## Name & Portrait
- Name: Olivia
- Portrait description: Professional person

## Bio & Demographics
- Role / title: Manager
- Industry or operating context: Operations
- Organization context: Company
- Seniority or experience level: Experienced
- Relevant demographics: 30-50 years old
- Backstory: Works hard

## Quotes
- Quote 1: "I want better tools."
- Quote 2: "Efficiency is important."
- Quote 3: "We need innovation."

## Needs | Pains
- Pain or need 1: Processes are bad
- Pain or need 2: Things take too long
- Pain or need 3: Needs more visibility

## Desired Outcomes | Goals
- Desired outcome or goal 1: Save time
- Desired outcome or goal 2: Reduce frustration
- Desired outcome or goal 3: Improve efficiency
```

**Why this fails**

- too abstract to guide any real decision
- title, pains, and goals could describe almost anyone
- no visible difference between evidence and assumption
- language sounds like business cliché, not a person
- confidence is overstated without research support

## Example 3: Drift Bug to Avoid

This is a common misuse in playbook work:

```markdown
Persona: Product Manager Priya
Reason: She is the person filling out the playbook.
```

**Why this is usually wrong**

The person filling out the playbook is not automatically the person the product serves.

Unless the product truly serves Product Managers, the persona should stay on the **customer side of the value chain**.
