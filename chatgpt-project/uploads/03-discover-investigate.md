# Discover + Investigate: Play references

November 2026 B2B work-in-progress Playbook. Not yet ratified.

Find Plays by stable identifier in 01-playbook-navigator.md. Each Play below contains its instructions, template, and examples. Mentions of skills or agents in the preserved source mean applying the Play from these uploaded references.

## ps-jobs-to-be-done | Jobs-to-Be-Done & Outcomes

Playbook number: 05. Phase: Discover + Investigate.

### ps-jobs-to-be-done / Instructions

#### Purpose

Create a **Productside-style Jobs-to-Be-Done & Outcomes artifact** for your target market segment.

This skill has **two steps** that can happen together or at different times:

**Step One (Discover + Investigate, pre-discovery):** Enumerate job statements and personas. Capture what the customer is trying to get done across functional, emotional, and social dimensions. Name the personas who have each job. This step produces the Job Statements & Personas table.

**Step Two (often after empathy interviews):** Fill in product outcomes for each job using the Direction + Metric + Context format. This step is stronger when informed by discovery evidence - empathy interviews, field observations, or customer data that validates or corrects the PM's assumptions about what customers actually want to achieve.

The two steps can be run in one session if the PM already has strong evidence. More often, Step One is done first to frame the discovery questions, and Step Two is completed after empathy interviews reveal what outcomes customers actually care about.

The playbook says to consider Jobs-to-Be-Done and Persona at the same time. If you have not built a proto-persona yet, consider doing that first or alongside this skill.

Use this skill when you need to:

- orient the team around customer needs instead of solutions (Step One)
- capture functional, emotional, and social jobs in one place (Step One)
- define product outcomes that are measurable and customer-centered (Step Two)
- build the foundation for problem identification, opportunity framing, and prioritization (both steps)

This is not a solution specification. Until you know what the customer is trying to accomplish, you are not ready to define what to build.

##### Usage Notes

- **Two steps:** Step One (job statements + personas) can be done pre-discovery. Step Two (product outcomes) is strongest after empathy interviews provide evidence. Both steps can be completed in one session if evidence exists.
- **Review path:** if the PM brings a draft, the skill pressure-tests it first (verdict per job and outcome) before offering rewrites. This matches the Playbook's AI prompts.
- The template produces two artifacts: a Job Statement + Persona table and a Product Outcome & Context table.
- Job statements use three Productside formats: Functional, Emotional, Social.
- Product outcomes use the Direction + Metric + Context format. "Optimize," "enhance," and "improve" are never a direction.
- Upstream (B2B work-in-progress deck): Market Selection & Sizing defines the segment these jobs belong to.
- Downstream: ps-problem-identification uses jobs and outcomes from this skill as input. Product outcomes feed into ps-outcome-tree.

#### Key Concepts

##### Three Types of Jobs

Productside distinguishes three types of customer jobs. Most teams only think about functional jobs and miss the emotional and social dimensions that drive adoption, satisfaction, and switching behavior.

**Functional:** What the customer is trying to get done in practical terms.
Format: `[Action verb] + [object of the action]`

Examples:
- "Onboard new employees"
- "Reconcile inventory across three warehouses"
- "Track patient medication adherence"

**Emotional:** How the customer wants to feel while doing the job.
Format: `Feel [Emotion] when [Circumstance]`

Examples:
- "Feel confident when presenting compliance data to auditors"
- "Feel satisfied that my work is helping others"
- "Feel in control when managing multiple site schedules"

**Social:** How the customer wants to be perceived by others.
Format: `Seen as [Social Perception] to [whom]`

Examples:
- "Be seen as responsible and trustworthy by employees and leadership"
- "Be seen as the go-to expert on regional logistics"
- "Be seen as ready for the Director role"

A complete JTBD artifact must include all three types. Functional jobs alone produce a flat, utilitarian view of the customer that misses the human motivations behind adoption and loyalty.

##### Product Outcomes Use a Specific Format

Product outcomes express what the customer wants to achieve. They are not internal business metrics and they are not feature requests.

Format: `Direction + Metric + Context/Circumstance`

The metric names what is being measured. **Default to including a quantified target**  -  a percentage, ratio, range, or exact number. When in doubt, put something in. The PM can refine it; a vague direction cannot be refined.

Preference order for the quantified value: **percentage > ratio > range > exact number**. For time-based outcomes, use a range ("by Q3", "by H2", "by EOY") rather than an exact date  -  specific dates stale out quickly.

Examples:
- "Reduce payroll data entry errors by 30% during quarterly onboarding cycles" (percentage)
- "Reduce HR query response time from 2-day to same-day for tier-1 requests" (ratio)
- "Add 3 new regional customers through HR partner channel by Q4" (exact number + range)
- "Increase HR self-service revenue to $1.2M by H2" (dollar figure + range)

Every outcome must have a direction. Direction + named metric ("Reduce time to complete payroll data entry") is the minimum viable form  -  acceptable when the PM has no basis for a threshold yet, but always the starting point to improve from. Add the quantified threshold ("by 30%", "from 2-day to same-day") when any evidence supports it.

Avoid: "improve efficiency," "faster onboarding," "better HR tools"  -  these are not metrics, just sentiment. **"Optimize," "enhance," and "improve" are never a direction.** They don't say which way the metric moves. Use increase/decrease, faster/slower, expand/contract, reduce, or eliminate.

Metrics can be quantitative (time, cost, quantity) or qualitative (confidence, trust, satisfaction). Qualitative metrics are especially useful for emotional and social jobs: "Increase confidence in incident-handling procedures" is a real outcome. When a qualitative metric can be measured, name how (for example, "trust scores on passenger security surveys").

The context is the result or impact the persona is seeking, expressed through their workflow and constraints. It is tied to whether they are satisfied or dissatisfied with reaching a goal. **The context never references a potential solution.**

Each job can have multiple outcomes. The outcomes should be specific enough to measure and customer-centered enough to guide prioritization.

##### What Makes a Good Product Outcome

The Playbook gives three tests:

- **Stable over time.** It doesn't change when technology changes. "Decrease the time to diagnose engine failure" holds whether the diagnosis is manual or AI-driven.
- **Linked to satisfaction.** It reflects what makes the customer satisfied or dissatisfied when trying to reach a goal.
- **Reveals unmet or overserved needs.** It shows where customers struggle, or where they have more capability than they need.

##### Jobs, Outcomes, and Pains Are Linked

The playbook states this directly: *"Customers experience Pains when they are unable to achieve the desired Outcomes when executing a Job."*

This is load-bearing for the next play. Pains do not float free  -  they arise when a Job is hard to execute and the desired Outcome is out of reach. Writing precise, measurable Outcomes in this play is what makes Problem Identification tractable: the PM already knows what "success" looks like for each Job, so the Pains become specific gaps between where the customer is and where they want to be.

##### Jobs, Outcomes, and Solutions Are Not the Same

- **Job** = what the customer is trying to accomplish
- **Outcome** = the result the customer wants when the job goes well
- **Solution** = what you build to help them (not part of this skill)

If a job statement mentions your product, a feature, or a tool, it is a solution masquerading as a job. Strip it back to the underlying customer progress.

Jobs define the scope of the work. Outcomes define the success criteria within that scope. The most common mistake is writing an outcome and labeling it a job, which mixes up what the customer is trying to accomplish with how they measure success. That undermines opportunity analysis and pulls the team toward feature-driven thinking.

**Jobs are intentionally stable.** Products, tools, and workflows change. Jobs persist. A job anchored to today's implementation ("export the weekly report from the legacy system") will expire with that system. A job anchored to progress ("share weekly checkpoint performance with leadership") will not.

##### Product Outcomes vs. Business Outcomes

This play captures **product outcomes** - things the customer wants to achieve. Business outcomes (revenue, retention, market share) belong in the Outcome Tree (Template 03), not here.

The playbook explicitly says: "Remember product outcomes are the things your customer wants to achieve."

##### Two Steps, One Artifact

The JTBD artifact has two halves: job statements (Table 1) and product outcomes (Table 2). These can be filled at the same time or at different times.

**Why separate them:** Job statements describe what the customer is trying to do. They can be drafted from the PM's current understanding, existing research, or market knowledge. Product outcomes describe the measurable results customers want. These are harder to get right without evidence.

The common pattern is:

1. **Step One:** Draft job statements and personas based on what the PM knows now. Use this to design empathy interview questions.
2. **Run empathy interviews** (ps-empathy-interviews) to validate and enrich understanding.
3. **Step Two:** Return to the JTBD artifact and fill in product outcomes informed by what customers actually said.

If the PM already has strong discovery evidence, both steps can be completed in one session. The skill supports either workflow.

##### Pair with Persona Work

The JTBD template has a Persona column next to every job statement. That column forces you to name *who* has this job - not a generic segment, but a recognizable role.

If you have already built a proto-persona, use that persona name. If not, use a concrete role title that reflects the actual customer (not the PM building the product).

##### How AI Supports This Play

The Playbook casts AI as a **sharp second reader** for jobs and outcomes. It checks each entry against the format, flags a job that is really an outcome or a solution, and pushes for the emotional and social jobs the PM skipped.

What AI cannot do is say what customers are trying to accomplish. Jobs come from real people in a real context. Any job or persona this skill drafts is a hypothesis to validate through Voice-of-the-Customer, never a finding.

- **Use it when:** the target segment is named and the PM has drafted jobs and outcomes, or wants a labeled starting draft to take into discovery.
- **Avoid it when:** the segment is vague or unnamed. Resolve the segment first (Step 1). Without it, any jobs produced are generic and validate nothing.
- **When reviewing a draft, return:** a verdict on each job (clean, or contaminated with an outcome or a solution), the missing emotional and social jobs *named* rather than written, and each outcome checked for direction, metric, and context. See [If the PM Brings a Draft](#if-the-pm-brings-a-draft).

##### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

##### Guided Mode

When asked for guidance, when the user is unfamiliar, or when context is missing:

1. Explain the output and estimated question count. Offer Guided, Context dump, or Best guess; default to Guided and ask the first question immediately.
2. Use supplied context instead of asking again. In Context dump mode, summarize Known / Assumed / Missing / Conflicting first.
3. Ask one bolded question per turn with a progress label, three context-specific numbered recommendations, option 4 Other, and an input hint. For facts only the user can know, ask openly without suggested answers and explain why. Ground unfamiliar domain options in research when needed.
4. Adapt recommendations to the answers. Explain why a question matters when helpful.
5. Answer interruptions, honor corrections and mode switches, and stop when asked. Resume with a brief recap and the pending question.
6. Recap supplied facts, assumptions, gaps, and readiness; confirm before generating a guided artifact. When the user faces a decision, recommend an option with reasons and offer distinct alternatives. The user decides.
7. Best guess may proceed immediately: label inferred details inline and end with Assumptions to Validate, ranked by decision impact. With sufficient supplied context, execute directly.

#### Application

Use Template (uploaded reference: `03-discover-investigate.md`, section `ps-jobs-to-be-done / Template`) for the full scaffold.


##### Required Output Convention

Default to a **clean, paste-ready two-table artifact**.

That means:

- fill both tables (Job Statement + Persona on the left, Product Outcome & Context on the right)
- produce exactly 10 job rows covering all three job types unless the user asks for a different count
- produce at least 10 product outcomes (one or more per job)
- keep job statements short enough for the template table cells (~8-10 words)
- keep product outcomes short enough for the template table cells (~12-14 words)
- explanation belongs below the artifact, not inside the table cells

The artifact comes first. Commentary is secondary.

##### If the PM Brings a Draft

When the user arrives with drafted job statements or outcomes, review the draft instead of drafting from scratch. This is the path the Playbook's AI prompts take (the critique guidance in this Play, the critique guidance in this Play).

1. **Confirm the segment.** If it is unnamed or vague, resolve it first (Step 1). Do not review jobs for a segment no one can name.
2. **Review each job.** Give a verdict per row: clean, wrong format, contaminated with an outcome, or contaminated with a solution. Quote the words that cause the problem.
3. **Name the gaps.** Name the missing job types (usually emotional and social) and the personas with no rows. Do not write them unless the user asks.
4. **Review each outcome.** Check direction (never optimize, enhance, or improve), metric (quantitative or qualitative), and context (no solution). Apply the three good-outcome tests.
5. **Offer rewrites last.** Propose fixes as options to accept, adapt, or reject, then fill the template with what the user commits.

Return the review as a compact table (entry, verdict, why, suggested fix) before any rewritten artifact.

##### Step 1: Confirm the Product and Target Market Segment

Before writing anything, answer:

- what product or service are we talking about?
- who is the target market segment?
- who are the personas within that segment? (user, buyer, influencer)

If you cannot answer those clearly, stop and resolve the target first.

**Guard against tech-role bias.** The jobs belong to the customer - the person who uses or buys the product in the field. An IoT platform's customer jobs belong to a fleet manager or logistics director, not a solutions architect. A clinical data platform's customer jobs belong to a clinical operations lead, not a data engineer. Before writing job statements, confirm: does this person write code, design systems, or architect solutions as their primary job? If no, the jobs should not read like a technologist's workday.

##### Step 2: Gather Evidence Before Writing

Once you know the target segment and role, offer the user two things before drafting:

1. **Web research** - offer to run a quick search for the target role in the target industry. Look for how practitioners describe their own work, frustrations, and goals. Job postings, industry forums, trade press, and professional community discussions are good sources. The goal is to capture real customer language, not marketing language about them.

2. **User-supplied artifacts** - ask whether the user has materials to share: interview notes, support tickets, call logs, existing persona or discovery work, competitive intel, or anything else that would ground the jobs and outcomes in evidence.

Either, both, or neither is fine - the user decides. But always offer before drafting.

##### Step 3: Identify the Personas Involved

Before writing job statements, name the personas who will appear in the Persona column.

For most products, there are 2-4 distinct personas involved:

- the primary user (the person who does the job day-to-day)
- the buyer (the person who approves or funds the product)
- influencers or secondary users

Each job row names the persona who has that specific job. Different personas can appear in different rows. Use concrete role titles, not generic labels.

If a proto-persona already exists from the ps-proto-persona skill, reuse that persona name.

**Distribute rows across roles.** Do not repeat the same persona in every row. The point of the Persona column is to show that different people have different jobs. If the product serves a Regional Operations Planner, a Dock Supervisor, and a VP of Distribution, all three should appear in the table - not just the primary user 10 times.

##### Step 4: Write Functional Job Statements

Functional jobs are the practical things the customer is trying to get done.

Format: `[Action verb] + [object of the action]`

Keep them:

- short (8-10 words fits the template cell)
- action-oriented (start with a verb)
- customer-centered (not your product's feature list)
- concrete (not "improve workflow" or "be more efficient")

Weak: "Manage data"
Stronger: "Reconcile shift schedules across three warehouse sites"

Produce at least 5-6 functional jobs.

##### Step 5: Write Emotional Job Statements

Emotional jobs capture how the customer wants to feel.

Format: `Feel [Emotion] when [Circumstance]`

These are not filler. Emotional jobs explain:

- why customers resist or adopt new tools
- what "good enough" means to them
- what turns a satisfied user into an advocate

Weak: "Feel happy using the product"
Stronger: "Feel confident when presenting compliance data to auditors"

Produce at least 2 emotional jobs.

##### Step 6: Write Social Job Statements

Social jobs capture how the customer wants to be perceived.

Format: `Seen as [Social Perception] to [whom]`

Social jobs reveal:

- career motivations that shape product requirements
- organizational pressures that affect adoption
- peer dynamics that drive or block behavior change

Weak: "Be seen as competent"
Stronger: "Be seen as the team's go-to expert on regional logistics by warehouse managers"

Produce at least 2 social jobs.

---

##### Step One / Step Two Boundary

Steps 1-6 above complete **Step One** of this skill: job statements and personas. At this point, the PM has a choice:

1. **Continue to Step Two now** if they already have enough evidence to write product outcomes confidently (prior research, customer data, domain expertise).
2. **Pause and run empathy interviews first** (ps-empathy-interviews) to validate the jobs and gather evidence about what outcomes customers actually care about. Then return to Step Two.

If the PM chooses to pause, offer to help design empathy interview questions based on the job statements just captured. The jobs from Step One make excellent interview prompts.

---

##### Step 7: Identify Product Outcomes for Each Job (Step Two)

For each job, express the product outcomes the customer wants to achieve.

Format: `Direction + Metric + Context/Circumstance`

- **Direction**: Increase, Decrease, Expand, Contract, Reduce, Eliminate  -  always required, never optional
- **Metric**: what is being measured (time, errors, satisfaction, revenue, customer count)  -  default to including a quantified target: percentage, ratio, range, or exact number ($3.5M, 3 new regional customers). Use a time range ("by Q3", "by H2") rather than an exact date. When in doubt, put a number in  -  the PM can refine it.
- **Context**: the specific circumstance that bounds the outcome

Each job can have one or more outcomes. Produce at least 10 outcomes total across all jobs.

If the PM completed empathy interviews between Step One and Step Two, ask what they learned before drafting outcomes. Customer language from interviews should inform the outcome statements directly.

Weak: "Better efficiency"
Stronger: "Reduce time spent reconciling shift schedules across sites" or "Reduce shift reconciliation time by 40% during weekly planning cycles"

Do not write outcomes that are feature requests ("have a dashboard that shows X") or internal business metrics ("increase revenue by 5%"). Product outcomes describe the customer's desired state.

##### Step 8: Separate Outcomes from Solutions

Before finalizing, scan every outcome and ask: is this something the *customer* wants to achieve, or is it something *we* want to build?

Solution indicators to strip out:

- mentions of your product name
- feature descriptions ("a dashboard that...", "an integration with...")
- implementation details ("automated alerts for...", "API-driven...")

Rewrite any solution-contaminated outcomes as customer-centered results.

##### Step 9: Keep the Artifact Compact

The canonical template uses table cells. Job statements should be ~8-10 words. Product outcomes should be ~12-14 words. Persona entries should be 2-3 words (a role title).

If the output requires summarizing before it can be pasted into the playbook, it is too long.

Do not let good prose outrank usable template completion.

##### Step 10: Add Optional Trailing Notes

If helpful, add a brief trailing section such as:

- `Jobs that need more evidence`
- `Outcomes that feel assumed`
- `Gaps in job type coverage`

Keep it separate from the paste-ready artifact.

Do not add a notes section at all unless:

- the user asks for it, or
- the artifact is already fully complete

##### Step 11: Offer Next Steps

After the current step is complete, offer context-appropriate options:

**If Step One is complete but Step Two is not yet done:**

1. **Run empathy interviews** (ps-empathy-interviews) - use the job statements to design interview questions that test whether these are real customer needs. Return to Step Two afterward.
2. **Build or refine a proto-persona** (ps-proto-persona) - if no persona exists yet, or if the JTBD work revealed a persona gap.
3. **Continue to Step Two now** - if the PM already has enough evidence to write product outcomes.

**If both steps are complete:**

1. **Move to Problem Identification** (ps-problem-identification) - synthesize the jobs, pains, and outcomes into candidate problem statements.
2. **Feed product outcomes into the Outcome Tree** (ps-outcome-tree) - the product outcomes from this skill can inform the Outcome Tree's product outcome section.
3. **Build or refine a proto-persona** (ps-proto-persona) - if persona work has not been done yet.

Present these as options, not as mandatory steps. The user decides what comes next.

### ps-jobs-to-be-done / Template

##### When to Use This

Use this template during **Discover + Investigate** to capture what your target customers are trying to accomplish and what success looks like for them. Pair this with persona work - the playbook says to consider Jobs-to-Be-Done and Persona at the same time.

This template supports **two steps** that can be completed together or at different times:

- **Step One:** Fill the Job Statements & Personas table (Section 1). This can be done pre-discovery.
- **Step Two:** Fill the Product Outcomes table (Section 2). This is often done after empathy interviews provide evidence about what outcomes customers actually care about.

##### Template

```markdown
# Jobs-to-Be-Done & Outcomes

## Product Context

- Product or service:
- Target market segment:
- Primary user persona:
- Buyer persona (if different):

## 1. Job Statements & Personas

Write job statements using the Productside formats:
- **Functional:** [Action verb] + [object of the action]
- **Emotional:** Feel [Emotion] when [Circumstance]
- **Social:** Seen as [Social Perception] to [whom]

| # | Type | Job Statement | Persona |
|---|------|---------------|---------|
| 1 | F | | |
| 2 | F | | |
| 3 | F | | |
| 4 | F | | |
| 5 | F | | |
| 6 | F | | |
| 7 | E | | |
| 8 | E | | |
| 9 | S | | |
| 10 | S | | |

> Quality check: Does every job describe customer progress, not a product feature or internal team task?
> Quality check: Are all three job types represented (Functional, Emotional, Social)?
> Quality check: Would the named persona recognize this as something they are actually trying to do?
> Quality check: Are rows distributed across multiple personas, not one repeated role?
> Capacity check: Job statements should be ~8-10 words. Persona entries should be 2-3 words (a role title).

## 2. Product Outcomes

For each job, express the desired product outcomes using:
**Direction + Metric + Context/Circumstance**

| # | Product Outcome & Context | Related Job(s) |
|---|--------------------------|-----------------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |
| 6 | | |
| 7 | | |
| 8 | | |
| 9 | | |
| 10 | | |

> Quality check: Does every outcome start with a direction word (reduce, increase, minimize, improve, eliminate)?
> Quality check: Is every outcome measurable - could you tell if it happened?
> Quality check: Are these things the *customer* wants to achieve, not internal business metrics?
> Quality check: Have you avoided feature requests disguised as outcomes ("have a dashboard that...")?
> Capacity check: Product outcomes should be ~12-14 words per row.

## Evidence Notes (optional)

- What is well-supported by evidence:
- What is still assumption:
- Recommended next validation steps:
```

##### Usage Guidance

###### Filling the Template

**Step One (can be done pre-discovery):**

1. Start with **Product Context** to anchor who this is for.
2. Fill **Job Statements** starting with functional jobs, then adding emotional and social jobs. Use the Productside sentence formats - do not improvise different structures.

**Step Two (strongest after empathy interviews):**

3. Fill **Product Outcomes** for each job. One job can have multiple outcomes. Use Direction + Metric + Context. If you completed empathy interviews between steps, let customer language inform the outcome statements.
4. The **Evidence Notes** section is optional and trailing. Do not let it displace or delay the main artifact.

###### How Many Rows

The canonical template has 12 rows. Default to 10 filled rows:

- at least 5-6 functional jobs
- at least 2 emotional jobs
- at least 2 social jobs
- at least 10 product outcomes (one or more per job)
- distribute rows across multiple personas, not one repeated role

Add more rows if the evidence supports them. Do not pad with vague jobs to fill the template.

###### What Goes in the Persona Column

Use a concrete role title that reflects the actual customer - the person who has this job in the field. If you built a proto-persona already, reuse that persona name.

Do not use:
- "User" (too vague)
- "Stakeholder" (too abstract)
- The Product Manager's own title (unless the product truly serves PMs)

###### Connecting to Other Skills

- **Upstream:** Proto-persona (the persona names in this template should match)
- **Downstream:** Problem Identification uses the jobs, pains, and outcomes from this artifact
- **Parallel:** The Outcome Tree (Template 03) uses product outcomes from this skill as input

###### Capacity Reference

See Template and capacity guidance (uploaded reference: `03-discover-investigate.md`, section `ps-jobs-to-be-done / Template`) for the exact word and character budgets per field.

| Field | Word Budget | Guidance |
|-------|-------------|----------|
| Job Statement | ~8-10 | Compact action phrase; use Productside format |
| Persona | ~2-3 | Role title only |
| Product Outcome | ~12-14 | Direction + Metric + Context; one sentence max |

### ps-jobs-to-be-done / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** Warehouse planner: Functional, "Coordinate daily labor assignments"; Emotional, "Feel confident when reallocating crews"; Social, "Seen as dependable by site supervisors." Outcome: "Reduce reassignment delays during shift changes."
- **Weak:** "Improve efficiency" has no named metric or clear direction.
- **Drift to avoid:** Jobs as solutions: "Use the scheduling dashboard" describes a product interaction. State what the planner is trying to accomplish.


#### Common Pitfalls

- **Writing Only Functional Jobs:** After writing functional jobs, explicitly ask: how does this person want to feel while doing this work? How do they want to be seen by their peers and leadership? Write at least 1-2 emotional and 1-2 social jobs.

- **Confusing Jobs with Solutions:** Strip out any mention of products, features, tools, or implementation. Rewrite as the underlying customer progress: "Track regional performance against quarterly targets."

- **Making Outcomes Vague:** Use the Direction + Metric + Context format, and never use "optimize," "enhance," or "improve" as the direction. "Improve efficiency" becomes "Reduce time spent reconciling data across multiple HR systems." Adding a specific threshold ("by 40% during month-end close") makes it stronger when you have the evidence  -  but even without a number, a named metric beats a vague direction.

- **Defaulting to a Tech Role:** Ask what the customer actually does day-to-day. Most products serve people whose primary job is not writing code. A fleet manager's jobs involve route optimization, driver coordination, and compliance reporting - not API integration or system architecture.

- **Writing Internal Team Tasks as Customer Jobs:** Ask: who experiences the product's value in the field? That person's jobs go in the template. The PM's jobs belong in process docs, not in customer discovery artifacts.

- **Restating Jobs as Outcomes:** Outcomes should describe a measurable result: "Reduce time to complete payroll data entry." "Reduce errors in new employee form submissions." Where the PM has evidence for a specific threshold, adding it strengthens the outcome  -  but a named metric without a number beats a vague direction every time. The outcome is what success looks like *for the customer* when the job goes well.

- **Exceeding Template Capacity:** Job statements: ~8-10 words. Outcomes: ~12-14 words. Persona entries: 2-3 words. Write for the template cell, not for the model's appetite for prose.

- **Underfilling the Template:** Default to 10 job rows covering all three types (Functional, Emotional, Social) with at least 10 outcomes. Distribute rows across multiple personas - do not repeat one role in every row.

- **Presenting AI-Drafted Jobs as Findings:** Label every drafted job and outcome as a hypothesis, and end with Assumptions to Validate. Route the hypotheses into empathy interviews (ps-empathy-interviews) before treating any of them as evidence.

#### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-jobs-to-be-done) for supporting source material and expanded examples.

## ps-proto-persona | Personas & Proto-Personas

Playbook number: 06. Phase: Discover + Investigate.

### ps-proto-persona / Instructions

#### Purpose

Create a **Productside-style proto-persona** for the person your product is serving.

This skill is for the **Discover + Investigate** phase, when you need a usable customer profile before you have enough research to call it validated. It helps a Product Manager capture the person behind the segment in a way that is specific enough to guide discovery and prioritization, while staying honest about what is still assumption.

Start with the **primary user persona**. Only after that is coherent should you build the **buyer persona**.

Use this skill when you need to:

- make the target customer feel real to the team
- capture needs, pains, goals, and attitudes in one place
- keep the team from designing for an abstract segment
- identify what still needs customer validation

This is not a validated persona. Until it is grounded in research, it is explicitly a **proto-persona**.

##### Usage Notes

- It starts with the **user persona** first, then optionally the buyer and influencer
- It keeps the profile explicitly **proto** until validated by research
- **Provenance tags:** every line of a working draft is tagged `[FROM YOU]`, `[RESEARCH]`, or `[AI-SUGGESTED, VALIDATE THIS]`. Invented quotes are always AI-suggested. The committed copy moves the tags out of the fields and keeps a ranked Riskiest Assumptions list.
- **Two draft paths:** beliefs or notes get drafted field by field with tags; a finished research-based persona gets reviewed against Clarity, Story, Empathy, Relevance, and Focus, and nothing is added that the research did not produce.
- **Five fields, following the B2B work-in-progress template.** The baseline's separate "What is this persona trying to do?" and "Attitudes & Influences" fields are folded in: what the persona is trying to accomplish goes under Needs | Pains, and attitudes and influences under Desired Outcomes | Goals.

#### Key Concepts

##### Persona vs. Proto-Persona

Productside makes an important distinction:

- **Persona**: a composite profile grounded in real customer research
- **Proto-persona**: a working profile built from limited evidence, team knowledge, and informed assumptions

If you have not validated it with customer research, call it proto.

##### User First, Buyer Second

This play starts with the **user persona**.

That means the person who actually uses, experiences, or lives with the product or service. In many B2B contexts, that is not the same person as the buyer, approver, or executive sponsor.

Only after the user persona is coherent should you repeat the exercise for the buyer.

**Who owns which personas:** Product Managers focus primarily on user personas  -  the people who experience the product day-to-day. Marketing and Sales typically own buyer and influencer personas. Knowing this scopes the PM's work: go deep on the user, treat the buyer as the secondary pass.

The Playbook names three persona types:

- **User:** the person who uses the product day to day
- **Buyer:** the person who controls the budget and makes the buying decision
- **Influencer:** the person who sways the purchase or use but is not the user or buyer

##### Segment vs. Persona: Build for the Center

A segment defines **who** you target, based on data. A persona brings that segment to life as **one relatable character**. Build for the center of the segment (the poster child), not a version stretched to cover everyone.

If a field starts describing everyone ("values efficiency," "wants better tools"), the persona has drifted off-center. Pull it back to the specific person at the heart of the segment.

##### A Persona Is a Communication Tool

A persona's job is to help stakeholders quickly understand and empathize with the people the product serves, so they make better product decisions. Judge a finished persona by five tests:

- **Clarity:** could a busy stakeholder grasp who this person is in under a minute?
- **Story:** do the pieces add up to one believable, coherent person?
- **Empathy:** would stakeholders feel this person's goals and pains?
- **Relevance:** is it clear why this person matters to product decisions?
- **Focus:** is this the specific center of one segment, or a blurry everyone?

The bar is stakeholder empathy, not a perfect document. When a persona is fit for purpose, say so and stop polishing.

##### Customer-Side, Not Product-Team-Side

The persona should usually describe the **customer-side person your product serves**, not the Product Manager building the product.

If your product truly serves Product Managers, then that can be correct. Otherwise, turning "the PM" into the default persona is a drift bug, not a shortcut.

##### The Working Parts of the Productside Persona

The canonical playbook template centers on these fields:

- name and portrait
- bio and demographics
- quotes
- needs and pains (including what the persona is trying to accomplish and the behavior you observe)
- desired outcomes and goals (including their attitudes and influences)

Those fields are the working surface. They are not decoration.

The name is **alliterative**, pairing a first name with the role (Henry HR Specialist, Serena Security Officer), so the team remembers the person and the role together.

This skill follows the B2B work-in-progress template, which has five fields. The baseline template's separate "What is this persona trying to do?" and "Attitudes & Influences" fields are folded in, as the WIP instructions do: what the persona is trying to accomplish and the behavior you observe go under **Needs | Pains**; attitudes and influences go under **Desired Outcomes | Goals**.

##### Proto Means Hypothesis

A proto-persona is **a hypothesis wearing a face**. It should help the team act, but it must not claim certainty it has not earned. It stays provisional until research confirms it. The moment the team treats it as settled, it stops being a proto-persona and becomes a persona profile the team has committed to.

The Playbook's discipline is to **never blur what the PM believes with what was filled in for them**. Every line of a working draft carries one provenance tag:

- `[FROM YOU]` - the PM or their stakeholders supplied it
- `[RESEARCH]` - it came from evidence (interview notes, artifacts, web research), with the source named in the trailing evidence section
- `[AI-SUGGESTED, VALIDATE THIS]` - you filled a gap; this is a guess about the customer and among the first things to test

Quotes you write are always invented. Tag them `[AI-SUGGESTED, VALIDATE THIS]` and treat them as lines to test in interviews, never as evidence. Only words a real customer said get `[RESEARCH]`.

##### How AI Supports This Play

The Playbook casts AI as the **drafter of the proto-persona**. Given what the PM and their stakeholders already believe about this user, it turns those beliefs into a structured persona fast, so research starts with a target instead of a blank page. It fills gaps, but it marks every gap it filled, because those are guesses about the customer and the first things to test. What to believe, and what to test, stays the PM's call.

- **Use it when:** the work is early, before research, and the PM can name what the team already assumes about this user.
- **Avoid it when:** the PM already has real customer research (review the research-based persona instead, see [If the PM Brings a Draft](#if-the-pm-brings-a-draft)), or the proto-persona will never be validated. An untested proto-persona is just a committed stereotype. Say so if the PM has no plan to test it.
- **Return:** every line tagged by provenance, the riskiest assumptions marked to test first, and a plan to validate the profile through research.

##### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

##### Guided Mode

When asked for guidance, when the user is unfamiliar, or when context is missing:

1. Explain the output and estimated question count. Offer Guided, Context dump, or Best guess; default to Guided and ask the first question immediately.
2. Use supplied context instead of asking again. In Context dump mode, summarize Known / Assumed / Missing / Conflicting first.
3. Ask one bolded question per turn with a progress label, three context-specific numbered recommendations, option 4 Other, and an input hint. For facts only the user can know, ask openly without suggested answers and explain why. Ground unfamiliar domain options in research when needed.
4. Adapt recommendations to the answers. Explain why a question matters when helpful.
5. Answer interruptions, honor corrections and mode switches, and stop when asked. Resume with a brief recap and the pending question.
6. Recap supplied facts, assumptions, gaps, and readiness; confirm before generating a guided artifact. When the user faces a decision, recommend an option with reasons and offer distinct alternatives. The user decides.
7. Best guess may proceed immediately: label inferred details inline and end with Assumptions to Validate, ranked by decision impact. With sufficient supplied context, execute directly.

#### Application

Use Template (uploaded reference: `03-discover-investigate.md`, section `ps-proto-persona / Template`) for the full scaffold.


##### Required Output Convention

Default to a **clean persona artifact** that a human can use directly.

The artifact comes first. Commentary is secondary.

That means:

- fill every main section of the persona
- keep each section sized to the canonical carrying capacity
- do not add analysis, ranking, or advice before the artifact is complete

The output comes in two stages:

1. **Working draft.** Every line ends with its provenance tag (`[FROM YOU]`, `[RESEARCH]`, `[AI-SUGGESTED, VALIDATE THIS]`). Tags are the only annotation allowed inside the fields. They are short and sit at the end of the line, so the field content still fits the template.
2. **Committed copy.** Once the PM accepts the draft, offer a clean, paste-ready copy with the tags removed, followed by a short **Riskiest Assumptions** list built from the AI-suggested lines, ranked by what to test first. The tags move out of the fields, but they never disappear.

If the PM asks for a clean copy straight away, give it, but still end with the Riskiest Assumptions list.

##### If the PM Brings a Draft

There are two kinds of draft. Treat them differently.

**Beliefs, notes, or a rough proto-persona** (before research). Follow the Playbook's drafting order: alliterative name, Bio & Demographics, Desired Outcomes & Goals, Needs | Pains, then Quotes. For each field, review what the PM gave you first, add only where they are thin, and tag every line. Ask one question at a time when a field is too thin to fill honestly. This mirrors the critique guidance in this Play.

**A finished, research-based persona.** Do not redraft it. This mirrors the critique guidance in this Play:

1. Ask who the stakeholder audience is if you don't know.
2. Give one honest read: is it already good enough to share? If yes, say so plainly and stop.
3. If not, work through the five tests (Clarity, Story, Empathy, Relevance, Focus) one at a time. Say what works, name the one change that would most improve it, and offer a concrete suggestion to accept, adjust, or reject.
4. Prioritize three to five changes. Name the weak spots minor enough to leave alone.
5. Sharpen wording, structure, and emphasis only. **Never add attributes, quotes, or data the research did not produce.** That includes counts and frequencies ("7 of 9 interviewees said...", "most fraud leads") unless the PM supplied them. If a count would strengthen the persona, ask the PM for it instead. When asked to add quotes to a research persona, offer only to pull real lines from the interview notes. Don't offer to write illustrative or composite quotes, even labeled.

##### Canonical Capacity Rules

The canonical example page has real carrying-capacity limits. Respect them.

Use the budgets in Template and capacity guidance (uploaded reference: `03-discover-investigate.md`, section `ps-proto-persona / Template`).

Default expectations:

- `Name & Portrait`: extremely short
- `Quotes`: a few compact quotes or quote fragments
- `Bio & Demographics`: the largest field, but still compact
- `Needs | Pains`: concise summary, not a paragraph pile, including a tight line on what they are trying to accomplish
- `Desired Outcomes | Goals`: compact future-state statements, plus short attitudes and influences

If the output would need summarizing before it can be pasted into the playbook, it is too long.

##### Step 1: Confirm Who the Product Serves

Before writing anything, answer:

- what product or service are we talking about?
- who experiences the problem most directly?
- who uses the product in the field?
- is that person different from the buyer?

If you cannot answer those clearly, stop and resolve the customer-side target first.

**Guard against tech-role bias.** LLMs default heavily toward software engineers, architects,
and developers when asked about technology products. Most products - even deeply technical
ones - serve people who are not programmers. An IoT platform PM's customer is a fleet
manager, a logistics director, or a smart city program lead - not a solutions architect.
A clinical data platform PM's customer is a clinical operations lead - not a data engineer.

Before writing the persona, confirm the role by asking: does this person write code, design
systems, or architect solutions as their primary job? If the answer is no, the persona
should not read like a technologist. Pains, tools, language, and daily work should reflect
the actual role, not a developer proxy.

##### Step 2: Gather Evidence Before Writing

Once you know the role and industry, offer the user two things before drafting:

1. **Web research** - offer to run a quick search for the target role in the target industry. Good sources include job postings, industry forums, trade press, day-in-the-life profiles, and professional community discussions. The goal is to replace assumptions with real language, real pain points, and real context.

2. **User-supplied artifacts** - ask whether the user has materials they want to share: interview notes, support tickets, call recordings, internal research, job descriptions, competitive intel, or anything else that would ground the persona in evidence.

Either, both, or neither is fine - the user decides. But always offer before drafting.

What to look for in web research:

- how practitioners in this role describe their own work and frustrations
- tools, systems, and workflows they mention
- organizational pressures and incentives specific to the industry
- language and jargon they actually use (not marketing language about them)
- hiring patterns that reveal what the role really does day-to-day

Feed what you find directly into the persona fields. Cite sources lightly in the trailing evidence section, not inline.

##### Step 3: Build the Primary User Persona

Start with the **user persona**.

Fill all of these sections:

- `Name & Portrait`
- `Bio & Demographics`
- `Quotes`
- `Needs | Pains` (with what they are trying to accomplish and the behavior you observe)
- `Desired Outcomes | Goals` (with attitudes and influences)

Do not start with the buyer unless the buyer is also the primary user.

Do not silently skip a section because you think the persona is "already clear enough."

##### Step 4: Use Real Signals Where You Have Them

Pull from any available evidence:

- interview notes
- call notes
- support themes
- field observations
- existing research
- sales or customer success insights

If you do not have direct evidence for something, avoid fake certainty. Acknowledge that in one short trailing note instead of bloating the artifact itself.

##### Step 5: Give the Persona a Real Shape

The persona should feel like a person the team could recognize.

That means:

- specific enough to guide choices
- grounded in behavior, not just demographics
- written in language the customer might actually use

Weak:

- "Works in tech"
- "Needs better tools"
- "Wants productivity"

Stronger:

- "Regional operations planner responsible for keeping warehouse labor, carrier timing, and dock capacity aligned across three sites"
- "Spends two hours every shift reconciling schedule changes across email, spreadsheets, and the warehouse system"

##### Step 6: Separate Pains from Goals

Do not flatten everything into one blob.

- `Needs | Pains` = friction, obstacles, frustrations, unmet needs
- `Desired Outcomes | Goals` = what better looks like for this person

This distinction matters because later Productside plays depend on it.

##### Step 7: Capture Attitudes and Influences Within Goals

The WIP template asks about attitudes and influences under Desired Outcomes | Goals. They are not filler. Capture them there:

- beliefs that shape adoption
- organizational pressures
- tools or people they trust
- incentives, fears, or habits that affect behavior

##### Step 8: Make Provenance and Risk Explicit

Before treating the profile as useful:

- check that every line carries a provenance tag, and that no AI-suggested line is tagged as the PM's or as research
- list the **Riskiest Assumptions**: the AI-suggested lines that would most change the persona if wrong, ranked by what to test first
- name how to validate them (who to interview, what to observe)

If you skip this, the team may treat a hypothesis as truth. Keep the trailing section concise. The tags carry most of the honesty, so the list only needs the top risks.

##### Step 9: Repeat for the Buyer Only If Needed

After the user persona is coherent, you may repeat the same structure for the buyer persona.

Keep them separate if:

- one person uses the product
- another person approves the purchase
- another person influences the decision

##### Step 10: Do Not Add Extra "Helpful" Commentary by Default

Do not add:

- strongest-section commentary
- ranking of pains or goals
- long caveats
- side analysis

unless the user explicitly asks for it.

The default skill output should be a persona the human can use immediately.

##### Step 11: Evolve It

Personas are only helpful if the team uses and updates them.

As research progresses:

- replace assumed quotes with real ones
- refine pains and goals
- split one proto-persona into two if the segment was too broad
- retire fields that turn out to be wrong

### ps-proto-persona / Template

Use this template to build a **Productside-style proto-persona** for the primary user first, then optionally the buyer.

Tag every line of the working draft with where it came from:

- `[FROM YOU]` - the PM or their stakeholders supplied it
- `[RESEARCH]` - it came from evidence; name the source under Proto-Persona Caveats
- `[AI-SUGGESTED, VALIDATE THIS]` - a filled gap; a guess to test first

Tags go at the end of the line and are the only annotation allowed inside the fields. When the PM commits the persona, the clean copy drops the tags from the fields and keeps the Riskiest Assumptions list.

##### When to Use This

Use this when you need a working customer profile before full validation, and you want the team to have a shared understanding of who the product is serving.

##### Template

```markdown
# Proto-Persona

## Persona Type
- User, Buyer, or Influencer:
- Validation status: Proto-persona / Validated persona
- Confidence level: Low / Medium / High

## Product Context
- Product or service:
- Problem space:
- Why this persona matters:

## Name & Portrait
- Name (alliterative, first name + role, e.g. "Henry HR Specialist"):
- Portrait description:

> Quality check: The persona should feel specific enough to remember and discuss. Avoid placeholders like "User A" unless this is a temporary working draft.

## Bio & Demographics
- Role / title:
- Industry or operating context:
- Organization context:
- Seniority or experience level:
- Relevant demographics:
- Backstory:

> Quality check: Include only demographics and background that actually help the team understand product behavior, needs, or constraints.

## Quotes
- Quote 1:
- Quote 2:
- Quote 3:

> Quality check: Quotes should reveal how this person thinks, speaks, or feels. Avoid generic lines like "I want better tools."
> Provenance check: Invented quotes are always `[AI-SUGGESTED, VALIDATE THIS]`. Only words a real customer said are `[RESEARCH]`.
> Capacity check: Keep quotes compact enough to fit the canonical quotes field.

## Needs | Pains
- Pain or need 1:
- Pain or need 2:
- Pain or need 3:
- What they are trying to accomplish, and the behavior we observe:

> Quality check: These should describe meaningful friction, unmet need, or frustration. Make them specific enough that the team can respond to them.
> Capacity check: Keep this section concise enough to paste into the canonical pain field.

## Desired Outcomes | Goals
- Desired outcome or goal 1:
- Desired outcome or goal 2:
- Desired outcome or goal 3:
- Attitudes and influences (beliefs, people and tools they trust, pressures):

> Quality check: Keep this future-state oriented. These are not tasks or features. They are the improvements this person wants in their work or life.
> Capacity check: Write compact future-state statements, not long rationale.

## Proto-Persona Caveats
- What still feels provisional:
- What should be validated next:
- Highest-priority research gaps:
- Evidence sources (for `[RESEARCH]` lines):

## Riskiest Assumptions
The AI-suggested lines that would most change this persona if wrong, ranked by what to test first.
1.
2.
3.

> Quality check: Does every line above carry a provenance tag? Is any AI-suggested line passed off as the PM's belief or as research?
> Focus check: Does this persona describe the center of one segment, or a blurry everyone?

## Buyer Relationship
- Is this person also the buyer?
- If not, who likely buys or approves?
- What tension might exist between user needs and buyer priorities?

## Research Next Steps
- Who should we interview next?
- What should we validate first?
- Which assumptions are riskiest?
```

##### Usage Guidance

- Build the **user persona first**.
- Only then create a separate buyer persona if the buyer is materially different.
- Keep the proto nature explicit until research confirms the profile.
- Do not use confidential client details in examples or shareable artifacts.
- Keep provenance tags short and at the end of each line. Keep validation notes concise unless the user explicitly asks for heavier evidence annotation.
- Complete every main persona section before adding any commentary.

### ps-proto-persona / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** Describe the warehouse operations analyst's responsibilities, goals, pains, and workarounds, marking sourced observations separately from assumptions.
- **Weak:** "Busy professional who values efficiency" cannot guide a specific product decision.
- **Drift to avoid:** Invented authenticity: a believable customer quote or research label generated by AI is not evidence. Omit it or label it as fictional.


#### Common Pitfalls

- **Making the Persona Too Generic:** Add behavioral context, concrete pains, and language that reflects how the person actually works.

- **Treating Assumptions as Research:** Tag every line of the working draft with its provenance, and end with a ranked Riskiest Assumptions list. The clean committed copy drops the tags from the fields but keeps that list.

- **Pitfall 2b: Adding Commentary That Displaces the Artifact:** Complete the artifact first. Keep commentary short and trailing.

- **Building the Buyer First:** Build the user first. Add buyer second when relevant.

- **Making the Product Manager the Persona by Default:** Ask explicitly: who experiences the product's value or pain in the field?

- **Defaulting to a Tech Role:** Ask what the customer actually does day-to-day. Most products - even deeply technical ones - serve people whose primary job is not writing code or designing systems. A fleet manager, a logistics director, a clinical operations lead, a utility substation engineer - these are the real customers. If the role does not involve building software as its core function, the persona should not read like a technologist.

- **Confusing Pains with Goals:** Keep friction separate from the future state the persona wants to achieve.

- **Never Updating the Proto-Persona:** Treat the proto-persona as a living document and revise it as discovery produces evidence.

- **Exceeding Template Capacity:** Write to the canonical budget, not to the model's appetite for prose.

- **The Assumptions Are the Model's, Not the Team's:** Review what the PM supplied before adding anything. Add only where they are thin, and tag every addition `[AI-SUGGESTED, VALIDATE THIS]`. If most of the persona is AI-suggested, say so and ask for more of the team's own beliefs before going further.

- **A Name and a Face Imply Proof:** Keep validation status visible ("Proto-persona") on the artifact. Keep invented quotes tagged as invented. Route the Riskiest Assumptions into empathy interviews (ps-empathy-interviews) before the persona is shared as a validated profile.

- **Stretching the Persona to Cover Everyone:** Build for the center of the segment. If the segment really holds two different people, split it into two personas rather than averaging them into one.

#### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-proto-persona) for supporting source material and expanded examples.

## ps-empathy-interviews | Empathy Interviews

Playbook number: 07. Phase: Discover + Investigate.

### ps-empathy-interviews / Instructions

#### Purpose

Create a **Productside-style Empathy Interview artifact** for your target customer.

This skill is for the **Discover + Investigate** phase. It closes the evidence loop - moving the team from assumptions about customer needs to validated understanding grounded in real conversation.

This is a **process skill**, not a content-fill skill. It spans three phases:

1. **Prepare** - define learning objectives, choose topic areas, sharpen the PM's interview questions, and optionally rehearse technique against realistic interview moments
2. **Conduct** - provide the PM with a reference card for running the interview (the agent cannot do this step)
3. **Document** - help structure raw interview notes into a findings board the team can act on

The agent helps with phases 1 and 3. Phase 2 happens in the field - the PM conducts the actual interview. The agent cannot substitute for face-to-face (or video) conversation with a real customer. It can play the customer in a rehearsal, but a rehearsal is practice, never research.

Use this skill when you need to:

- validate assumptions from proto-persona or JTBD work with real customers
- understand the customer's actual workflow, frustrations, and motivations
- discover jobs, outcomes, and problems you did not anticipate
- capture the emotional dimension of the customer experience (what they feel, not just what they do)
- build empathy across the product team by documenting first-person customer language

This is not a survey design tool, a usability test script, or a sales call framework. Empathy interviews are discovery conversations - open-ended, story-seeking, and judgment-free.

##### Usage Notes

- This is a **process skill** (`type: process`), not a component skill. It spans preparation, interview conduct, and findings documentation across multiple sessions.
- The agent helps with preparation (Phase 1) and documentation (Phase 3). The PM conducts the actual interview (Phase 2) in the field - the agent cannot substitute for real customer conversation.
- **Preparation follows the Playbook's AI pages:** name the decision, set learning objectives, choose 4-5 topic areas, and review the PM's own questions (leading, closed, solution-fishing, no objective). The agent drafts questions only on request, labeled as a starting draft.
- **Rehearsal (optional):** the agent can play the persona in a technique drill, one tough moment at a time, then review the PM's technique. It is practice, never research. Nothing from a rehearsal goes into findings.
- Evidence gathering: this skill qualifies for **web research + user artifacts**. Web research grounds the PM in the interviewee's domain before the interview. User artifacts (persona work, JTBD output, prior research) inform question preparation.
- The findings board produces structured output that feeds downstream skills: Jobs-to-Be-Done, Desired Outcomes, Problems, and Feels/Appears.
- Upstream: ps-proto-persona (persona grounds the interview target), ps-jobs-to-be-done (provides assumptions to test).
- Downstream: ps-problem-identification (uses problems and jobs from findings), ps-proto-persona (refine with real quotes and observations).

#### Key Concepts

##### The 70/30 Rule

The interviewee is the star. Target 70% listening, 30% talking. If the PM is talking more than the interviewee, they are lecturing, not learning.

##### Open-Ended Questions Over Yes/No

Questions that start with "Can you walk me through..." or "Tell me about the last time..." produce stories. Questions that start with "Do you..." or "Is it..." produce one-word answers that teach nothing.

##### "Tell Me About the Last Time..." Is the Key Probe

The most powerful interview technique is asking about a specific, recent occurrence. "Tell me about the last time you had to reconcile data across systems" produces richer insight than "How do you usually handle data reconciliation?"

##### Look for Say/Feel/Do/Think Inconsistencies

Customers say one thing, feel another, do a third, and think a fourth. The gap between what someone says they do and what they actually do is where the real insight lives. Watch for these disconnects during the interview.

##### Biased Questions Poison the Findings

Leading questions ("Don't you think a dashboard would help?") confirm the PM's hypothesis instead of testing it. The PM must learn to ask neutral questions that let the customer lead.

##### Confirm Understanding by Reflecting Back

After the interviewee shares something significant, repeat back what you heard in your own words: "So if I understand correctly, you're saying..." This does two things: it confirms you captured their meaning accurately, and it often prompts the interviewee to correct, expand, or go deeper  -  surfacing nuance a follow-up probe alone might miss.

##### The Findings Board Maps to Downstream Artifacts

The documentation phase produces four categories that feed directly into other playbook skills:

- **Jobs-to-Be-Done** - what the customer is trying to accomplish (feeds ps-jobs-to-be-done)
- **Desired Outcomes** - what success looks like for the customer (feeds ps-jobs-to-be-done)
- **Problems** - friction, blockers, and pain points observed (feeds ps-problem-identification)
- **Feels/Appears** - emotional and behavioral observations (feeds ps-proto-persona refinement)

##### Team Sport

The playbook says to make it a team sport. Have design and engineering counterparts listen in on interviews. They catch different signals than the PM does, and shared exposure to the customer builds alignment faster than secondhand summaries.

##### Prepared but Not Rigid

Prepare 5-8 questions, but do not follow the list like a script. The best insights come from following the customer's thread, not from checking boxes. If the customer opens an unexpected door, walk through it.

##### The Rescue Probe

If the conversation stalls or the PM gets stuck, the universal fallback is: "Why?" or "Tell me more." These two phrases restart almost any stalled thread.

##### Learning Objectives Serve a Decision

Every interview round should inform a decision the team has to make. Name it before writing a single question ("whether to build for hub airports or small airports first," "whether reconciliation or scheduling is the bigger pain"). Every question the PM keeps should trace to a learning objective, and every learning objective should trace to that decision. A question with no objective behind it is a question to cut.

##### Topic Areas, Not a Script

The Playbook prepares interviews around **4-5 topic areas**, not a fixed list of questions. Topic areas let the PM improvise and dig deeply while the interviewee steers the conversation and tells their stories. Aim them at what the interviews must validate: the persona's jobs and desired outcomes, and the **root-cause problems** that cause pains and block those outcomes.

Questions still matter. The PM writes them, a few per topic area, as starting points. The interview follows the story, not the list.

##### Rehearse Before It Counts

Empathy interviewing is a skill and must be practiced. The Playbook says to role-play with friends and colleagues, and an AI rehearsal partner works too. The drill presents one tough interview moment at a time (a one-word answer, a feature request, a say/do contradiction, silence), and the PM practices the reflex: dig deeper, stay neutral, confirm understanding, resist pitching. Rehearsing out loud, in a chat tool's voice mode, lets the PM hear their own leading phrasing and practice sitting in silence.

A rehearsal is practice, not data. Nothing from it goes into findings.

##### How AI Supports This Play

The Playbook casts AI as **preparation partner and sparring partner**. It focuses the PM on what matters so they can guide the conversation, and it can play tough interview moments so the PM can rehearse before it counts.

What AI cannot do is be the person being interviewed. The whole point of this Play is the real conversation. The moment AI answers as the customer and that answer is treated as input, the team has a script, not research, and the Play is corrupted.

- **Use it when:** real interviews are scheduled and the PM wants to sharpen questions or rehearse technique.
- **Avoid it when:** the PM wants AI to answer as the customer in place of an interview. A simulated interview is practice, not research. If no interviews are scheduled, help schedule them; do not simulate them.
- **Return:** leading or closed questions identified for the PM to rewrite, each kept question tied to a learning objective, and the PM's follow-up reflexes drilled against realistic interview moments. See [If the PM Brings a Draft](#if-the-pm-brings-a-draft) and Step 6.

##### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

##### Guided Mode

When asked for guidance, when the user is unfamiliar, or when context is missing:

1. Explain the output and estimated question count. Offer Guided, Context dump, or Best guess; default to Guided and ask the first question immediately.
2. Use supplied context instead of asking again. In Context dump mode, summarize Known / Assumed / Missing / Conflicting first.
3. Ask one bolded question per turn with a progress label, three context-specific numbered recommendations, option 4 Other, and an input hint. For facts only the user can know, ask openly without suggested answers and explain why. Ground unfamiliar domain options in research when needed.
4. Adapt recommendations to the answers. Explain why a question matters when helpful.
5. Answer interruptions, honor corrections and mode switches, and stop when asked. Resume with a brief recap and the pending question.
6. Recap supplied facts, assumptions, gaps, and readiness; confirm before generating a guided artifact. When the user faces a decision, recommend an option with reasons and offer distinct alternatives. The user decides.
7. Best guess may proceed immediately: label inferred details inline and end with Assumptions to Validate, ranked by decision impact. With sufficient supplied context, execute directly.

#### Application

Use Template (uploaded reference: `03-discover-investigate.md`, section `ps-empathy-interviews / Template`) for the full scaffold.


##### Required Output Convention

This skill produces artifacts in **three phases**. Not all phases happen in a single session:

- **Phase 1 output:** The decision and learning objectives, 4-5 topic areas, the PM's interview questions (reviewed) with follow-up probes, and a conduct reference card. Optionally, a rehearsal and its technique review.
- **Phase 3 output:** A structured findings board with Jobs-to-Be-Done, Desired Outcomes, Problems, and Feels/Appears entries sized for the canonical template.

The PM returns to the agent after conducting the interview (Phase 2) to get help with Phase 3.

##### If the PM Brings a Draft

When the PM arrives with draft questions or topic areas, review them before writing anything new. This mirrors the critique guidance in this Play.

1. **Confirm the persona and the decision.** If no learning objectives exist, get them first (Step 3).
2. **Review each question.** Flag leading questions, closed (yes/no) questions, and questions that fish for the PM's solution. Quote the words at fault.
3. **Tie each kept question to a learning objective.** Name any question with no objective behind it, and any objective with no questions.
4. **Name the gaps.** Name missing topic areas (often current workarounds, impact, and the emotional cost) without writing the questions for them.
5. **Offer rewrites last**, as options to accept, adapt, or reject. The PM writes the final wording.

Return the review as a compact table (question, verdict, why, objective) before any rewritten guide.

##### Step 1: Confirm the Product Context and Target Persona

Before writing anything, answer:

- What product or service are we talking about?
- Who is the target customer (the person who will be interviewed)?
- What is their role and what do they do day-to-day?

If you cannot answer these clearly, stop and resolve the target first.

**Guard against tech-role bias.** The interviewee should be the actual customer - the person who uses or buys the product in the field. An IoT platform PM interviews fleet managers, not solutions architects. A clinical data platform PM interviews clinical operations leads, not data engineers. Before drafting questions, confirm: does this person write code, design systems, or architect solutions as their primary job? If no, the questions should not read like a technical interview.

##### Step 2: Gather Evidence Before Writing

Once you know the target persona and role, offer the user two things before drafting questions:

1. **Web research** - offer to run a quick search for the target role in the target industry. Look for how practitioners describe their own work, frustrations, and daily reality. Job postings, industry forums, trade press, and professional community discussions are good sources. The goal is to understand the domain well enough to ask informed questions - not to replace the interview.

2. **User-supplied artifacts** - ask whether the user has materials to share: existing persona work, JTBD output, problem identification artifacts, support tickets, previous interview notes, or any other discovery work that would ground the questions in evidence.

Either, both, or neither is fine - the user decides. But always offer before drafting.

##### Step 3: Define Learning Objectives

Before writing questions, ask the PM: what decision will these interviews inform? What do you need to learn to make it? What assumptions need testing?

Learning objectives are not interview questions - they are the strategic goals behind the questions. Examples:

- "We assume clinical data managers spend 40% of their time on manual reconciliation - is that true?"
- "We do not know how this role currently solves the problem - what workarounds exist?"
- "We need to understand the emotional cost of the current process, not just the operational cost."

3-5 learning objectives are enough. They guide question selection and help the PM stay focused during the interview.

##### Step 4: Choose Topic Areas, Then Sharpen the Questions

**Topic areas first.** Suggest 4-5 topic areas tied to the learning objectives, aimed at the persona's jobs, desired outcomes, and the root-cause problems behind their pains. Give one or two example open-ended questions per area so the PM sees what good looks like.

**The PM writes the questions.** Ask the PM to draft a few questions per topic area, then review them using [If the PM Brings a Draft](#if-the-pm-brings-a-draft). If the PM asks you to draft the questions (or is in best guess mode), write 5-8 and label them a starting draft for the PM to rewrite in their own voice. Run the same review on your own draft before handing it over.

Whoever writes them, structure the questions to flow naturally:

1. **Opening** - warm-up questions about the person's role and daily work ("Can you walk me through a typical day...")
2. **Core exploration** - questions that dig into the target problem area ("Tell me about the last time...")
3. **Current state** - how they handle the problem today ("What have you tried to make this faster? What has worked best?")
4. **Impact** - what the problem costs them ("How does this affect your work / team / goals...")
5. **Closing** - open-ended wrap-up ("Is there anything else you'd like to share...")

For each question, include 1-2 follow-up probes. Follow-ups should dig deeper:

- "Can you tell me about a specific time that happened?"
- "Why did you choose that approach?"
- "What happened next?"
- "How did that make you feel?"

Do not include yes/no questions. Do not include questions that mention the product or a specific solution. Every kept question names the learning objective it serves.

##### Step 5: Review Conduct Guidance

Before the PM goes into the field, surface the conduct reference card:

- **70/30 rule** - listen 70%, talk 30%
- **Open-ended probes** - "Tell me about the last time...", "Can you walk me through...", "Why?"
- **Story-seeking** - ask about specific recent occurrences, not general habits
- **Bias avoidance** - do not mention the product, do not suggest solutions, do not ask leading questions
- **Inconsistency watch** - note gaps between what they say, feel, do, and think
- **Note-taking** - record exact quotes when possible; note emotions and body language
- **Rescue probe** - if stuck, ask "Why?" or "Tell me more"
- **Closing** - thank them, ask if they are open to further conversations or testing

##### Step 6: Rehearse Technique (Optional)

If the PM wants to practice, run a rehearsal drill. This mirrors the critique guidance in this Play.

1. **Say what this is.** It's practice, not data, and nothing from it goes into findings. Suggest voice mode if the PM's tool has one.
2. **Present one realistic interview moment at a time**, playing the persona: a one-word answer, a jump to a feature request, saying one thing while describing the opposite, going quiet. Respond to the PM's moves as the persona plausibly would, then present the next moment.
3. **When the PM says they are done, give an honest review.** Did they dig deeper, stay neutral and unbiased, confirm understanding, and resist pitching solutions? Say where they slipped and what to do differently next time.
4. **Close by sending them to a real customer.** Remind the PM not to treat anything the simulated persona said as truth.

Never carry rehearsal lines into Step 8 (Document Findings), into quotes, or into any downstream artifact.

##### Step 7: The PM Conducts the Interview

**The agent cannot do this step.** The PM (or a teammate) conducts the actual interview in the field. The agent waits for the PM to return with notes.

When the PM returns, ask for their raw notes, quotes, and observations before structuring findings.

##### Step 8: Document Findings

After the interview, help the PM structure raw notes into the findings board. The board has four quadrants:

**Jobs-to-Be-Done** - what the customer is trying to accomplish, discovered from their stories. Use the Productside job format:
- Functional: [Action verb] + [object of the action]
- Emotional: Feel [Emotion] when [Circumstance]
- Social: Seen as [Social Perception] to [whom]

4-6 entries, ~6-8 words each (sticky-note sized).

**Desired Outcomes** - what success looks like for the customer. Use Direction + Metric + Context format. 3-4 entries, ~8-12 words each.

**Problems** - friction, blockers, and pain points observed during the interview. Write as concrete observations, not abstract categories. 4-6 entries, ~8-12 words each (sticky-note sized).

**Feels/Appears** - emotional and behavioral observations. What the customer appeared to feel, not what they explicitly said. 4 entries, ~6-10 words each (sticky-note sized).

##### Step 9: Capture Raw Quotes

Pull 4-6 direct quotes from the interview notes. These are the customer's actual words - not paraphrased, not cleaned up. Quotes ground the findings in real evidence and are powerful artifacts for building team empathy.

Keep quotes to ~15-20 words each.

##### Step 10: Synthesize Across Interviews

If the PM has conducted multiple interviews, help identify patterns:

- Which jobs and problems appear across multiple interviews?
- Where do interviewees agree? Where do they diverge?
- Are there persona segments emerging from the data?
- What was surprising or unexpected?

Do not force consensus. Divergence is signal, not noise.

##### Step 11: Offer Next Steps

After the findings are documented, offer the user up to three next-step options:

1. **Refine the proto-persona** - update the persona with real quotes, validated pains, and observed attitudes using ps-proto-persona
2. **Move to Problem Identification** - synthesize interview findings into candidate problem statements using ps-problem-identification
3. **Conduct more interviews** - if the sample is small or the findings are inconclusive, prepare questions for another round

Present these as options, not as mandatory steps. The user decides what comes next.

### ps-empathy-interviews / Template

##### When to Use This

Use this template during **Discover + Investigate** to prepare for empathy interviews, guide conduct, and document findings. This is a process skill that spans three phases - preparation, interview conduct (PM does this in the field), and documentation.

##### Template

###### Phase 1: Interview Preparation

```markdown
# Empathy Interview Preparation

## Product Context

- Product or service:
- Target market segment:
- Target interviewee role:
- Interviewee's primary job:

## Decision These Interviews Inform

- Decision:
- Who makes it, and by when:

## Learning Objectives

What do we need to learn to make that decision? What assumptions need testing?

1.
2.
3.
4.
5.

> Quality check: Are these learning objectives specific enough to guide question selection?
> Quality check: Do they focus on the customer's reality, not on validating a feature idea?
> Quality check: Does every learning objective trace to the decision above?

## Topic Areas

4-5 areas to explore. They let the interviewee steer and tell stories while you dig deeper. Aim them at the persona's jobs, desired outcomes, and the root-cause problems behind their pains.

| # | Topic Area | Learning Objective It Serves | Example Open-Ended Question |
|---|------------|------------------------------|-----------------------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

## Interview Questions

Prepare 5-8 open-ended questions in your own words, a few per topic area. Do not follow this list rigidly - explore deeper when the customer opens a thread.

| # | Question | Follow-Up Probes | Objective |
|---|----------|-----------------|-----------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |

> Quality check: Does every question start with "Can you...", "Tell me about...", "What...", "How...", or "Why..."?
> Quality check: Does any question mention the product name, a feature, or a specific solution? If yes, rewrite it.
> Quality check: Could any question be answered with just "yes" or "no"? If yes, convert to open-ended.
> Quality check: Do the questions cover: daily workflow, pain points, current solutions, impact, and emotional experience?
> Quality check: Does every question name the learning objective it serves? Cut any that don't.
> Capacity check: Questions should be ~15-20 words. Follow-up probes should be ~8-12 words.
```

###### Phase 2: Conduct Guidance (Reference Card)

```markdown
# Interview Conduct Reference Card

## Before the Interview
- [ ] Rehearse your technique (optional): one tough moment at a time, out loud if you can. Practice only; nothing from it goes into findings.
- [ ] Review learning objectives
- [ ] Have questions accessible but not as a rigid script
- [ ] Set up note-taking (or have a teammate take notes)
- [ ] Test recording equipment if applicable (with permission)

## During the Interview

**Opening**
- Introduce yourself and explain why you are talking with them
- Set expectations: "There are no right or wrong answers - I want to learn from your experience"
- Ask permission to take notes or record

**Core Rules**
- 70% listening, 30% talking
- Ask about specific recent occurrences ("Tell me about the last time...")
- Dig deeper on surface answers ("Why?", "Can you say more about that?", "What happened next?")
- Do NOT mention the product, pitch features, or suggest solutions
- Do NOT ask yes/no questions - convert to open-ended
- Do NOT ask "Would you use a tool that...?" or "How would you feel about...?"

**Watch For**
- Inconsistencies between what they say, feel, do, and think
- Emotional reactions - frustration, pride, resignation, anxiety
- Workarounds and hacks they have built
- Language they use to describe their work (capture exact words)

**If You Get Stuck**
- Ask "Why?"
- Ask "Tell me more"
- Ask "Can you give me a specific example?"

**Closing**
- "Is there anything else you'd like to share about your experience?"
- Thank them
- Ask if they are open to further conversations or testing

## After the Interview
- [ ] Document findings within 24 hours (use Phase 3)
- [ ] Share raw notes with teammates who listened in
- [ ] Note what surprised you - surprises are the highest-signal findings
```

###### Phase 3: Document Findings

```markdown
# Empathy Interview Findings

## Interview Context

- Interviewee role:
- Date:
- Interview duration:
- Product context:
- Interviewer(s):

## Raw Quotes

Capture 4-6 direct quotes - the customer's actual words, not paraphrased.

| # | Quote |
|---|-------|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |
| 6 | |

> Quality check: Are these the customer's actual words, or a paraphrase? Use their language.
> Capacity check: Quotes should be ~15-20 words each.

## Findings Board

### Jobs-to-Be-Done

What is the customer trying to accomplish? Discovered from their stories.

| # | Job (Functional / Emotional / Social) |
|---|---------------------------------------|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |
| 6 | |

> Quality check: Do these jobs come from what the customer said, not what you assumed before the interview?
> Quality check: Are all three job types represented if the evidence supports them?
> Capacity check: ~6-8 words per entry (sticky-note sized).

### Desired Outcomes

What does success look like for the customer? Use Direction + Metric + Context.

| # | Desired Outcome |
|---|-----------------|
| 1 | |
| 2 | |
| 3 | |
| 4 | |

> Quality check: Does every outcome use the Direction + Metric + Context format?
> Quality check: Are these the customer's desired outcomes, not your product's value propositions?
> Capacity check: ~8-12 words per entry.

### Problems

Friction, blockers, and pain points observed during the interview.

| # | Problem |
|---|---------|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |
| 6 | |

> Quality check: Are these concrete and specific, not abstract categories like "inefficiency"?
> Quality check: Did the customer describe this problem, or are you inferring it?
> Capacity check: ~8-12 words per entry (sticky-note sized).

### Feels / Appears

Emotional and behavioral observations. What the customer appeared to feel, not just what they said.

| # | Observation |
|---|-------------|
| 1 | |
| 2 | |
| 3 | |
| 4 | |

> Quality check: Do these capture emotions and behaviors, not just opinions?
> Quality check: Did you note any say/feel/do/think inconsistencies?
> Capacity check: ~6-10 words per entry (sticky-note sized).

## Key Insights

- What surprised you:
- What confirmed prior assumptions:
- What contradicted prior assumptions:
- What needs more interviews to validate:

## Evidence Notes

- What is well-supported by this interview:
- What is still a single data point:
- Recommended next steps:
```

##### Usage Guidance

###### The Three Phases

This template covers a multi-session process:

1. **Phase 1 (Preparation)** - the agent helps name the decision, define learning objectives, choose topic areas, review the PM's questions, and optionally rehearse technique. This happens before the interview.
2. **Phase 2 (Conduct)** - the PM takes the reference card into the field and conducts the interview. The agent cannot do this step.
3. **Phase 3 (Documentation)** - the PM returns with raw notes. The agent helps structure findings into the board format.

The PM may complete Phase 1, leave for days or weeks, and return for Phase 3. That is normal.

###### How Many Questions

The canonical template has 6 question slots. Default to 5-8 questions:

- 1-2 opening questions about the person's role and daily work
- 2-3 core questions exploring the target problem area
- 1-2 questions about current solutions and impact
- 1 closing question

Add follow-up probes for each question. Do not over-prepare - 8 questions is a ceiling, not a target.

###### Findings Board Sizing

The findings board maps to the canonical template's sticky-note grid:

| Section | Entries | Words per Entry | Guidance |
|---------|---------|-----------------|----------|
| Jobs-to-Be-Done | 4-6 | ~6-8 | Use Productside JTBD formats |
| Desired Outcomes | 3-4 | ~8-12 | Direction + Metric + Context |
| Problems | 4-6 | ~8-12 | Concrete, specific observations |
| Feels/Appears | 4 | ~6-10 | Emotional and behavioral |
| Raw Quotes | 4-6 | ~15-20 | Customer's actual words |

###### Connecting to Other Skills

- **Upstream:** Proto-persona (grounds the interview target and questions); JTBD (provides assumptions to test)
- **Downstream:** Problem Identification uses the problems and jobs from this artifact; proto-persona refinement uses the quotes and emotional observations
- **Parallel:** JTBD can be updated with newly discovered jobs and outcomes from the interview

###### Capacity Reference

See Template and capacity guidance (uploaded reference: `03-discover-investigate.md`, section `ps-empathy-interviews / Template`) for the exact word and character budgets per field.

| Field | Word Budget | Guidance |
|-------|-------------|----------|
| Interview Question | ~15-20 | Open-ended, no product mentions |
| Follow-Up Probe | ~8-12 | Dig deeper: "Why?", "Tell me more" |
| Raw Quote | ~15-20 | Customer's actual words |
| Job-to-Be-Done | ~6-8 | Sticky-note sized; Productside format |
| Desired Outcome | ~8-12 | Direction + Metric + Context |
| Problem | ~8-12 | Sticky-note sized; concrete observation |
| Feels/Appears | ~6-10 | Sticky-note sized; emotional/behavioral |

### ps-empathy-interviews / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** Ask a regional store manager: "Tell me about the last time inventory differed across your stores." Record the real interview separately from preparation.
- **Weak:** "Would a real-time dashboard solve your inventory problem?" leads the witness toward the proposed solution.
- **Drift to avoid:** Rehearsal as research: simulated interview answers must never enter findings as customer evidence.


#### Common Pitfalls

- **Asking Leading Questions:** Strip the question of any solution language or implied answer. "How do you currently monitor [process]?" lets the customer describe their reality. "Don't you think a dashboard would help?" tells them what to say.

- **Asking Yes/No Questions:** Convert to open-ended: "Can you walk me through the last time you had to reconcile data across systems? What happened?"

- **Talking More Than 30%:** Set a physical reminder (a sticky note that says "LISTEN"). After asking a question, wait. Count to five silently before saying anything else. Silence prompts the customer to fill the gap with real insight.

- **Asking About Features Instead of Problems:** Ask about their current reality, not a hypothetical future. "What happens today when X goes wrong?" reveals the problem. "What features would fix it?" reveals the customer's guess about a solution, which is not the same thing.

- **Not Digging Deeper on Surface-Level Answers:** Probe: "Can you tell me more about how you manage it?" or "What does 'fine' look like on a bad day?" The second layer is almost always richer than the first.

- **Skipping Documentation:** Document findings within 24 hours of the interview. Use the findings board structure - it forces categorization and makes the data usable by the rest of the team.

- **Defaulting to a Tech Role:** Before drafting questions, confirm: is this the person who uses or buys the product in the field? If their primary job is not writing code or designing systems, the questions should reflect their actual daily work.

- **Treating This as a Content-Generation Skill:** Phase 3 (Document Findings) requires real interview data as input. If the PM has not talked to a customer, the agent should help with Phase 1 (Prepare Questions) and send the PM into the field. Do not fabricate findings.

- **Treating a Rehearsal as Research:** Label every rehearsal as practice at the start and the end. Refuse to document findings from a simulated interview. If the PM has no real interviews yet, help them recruit and schedule them.

- **Reading the Question List Like a Script:** Prepare around topic areas, not a script. Treat questions as starting points, follow the thread the interviewee opens, and use "Why?" and "Tell me more" to go deeper. Rehearsal (Step 6) builds the reflex.

#### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-empathy-interviews) for supporting source material and expanded examples.

## ps-affinity-mapping | Affinity Mapping

Playbook number: 08. Phase: Discover + Investigate.

### ps-affinity-mapping / Instructions

#### Purpose

Create a **Productside-style Affinity Map** from qualitative customer research.

This skill helps a Product Manager synthesize raw observations from empathy interviews, customer feedback, or other research into a working artifact with:

- labeled theme clusters grouping similar observations
- named patterns that reveal what the data is actually saying
- key insights that translate patterns into product-relevant implications

The point is not to produce a summary of what customers said. The point is to surface what the observations collectively reveal.

##### Usage Notes

- **Coach by default.** With real notes, the skill walks the PM through the Playbook's five-step method (orient, split, immerse, group, name) and the PM does the grouping, labeling, and insights.
- **Draft on request.** If the PM asks the skill to group the notes, it produces a map labeled "AI draft grouping: for the team to challenge."
- **No real notes, no map.** The skill will not map invented observations. It routes to ps-empathy-interviews instead.

#### Key Concepts

##### This Skill Bridges Interviews and Problem Identification

Affinity mapping is the synthesis step. Raw observations from empathy interviews are too granular to act on directly. Affinity mapping groups them into patterns. Those patterns become the input to ps-problem-identification.

Without this step, teams often jump from "we talked to customers" to "here is our feature roadmap" without ever making the intermediate inference.

##### Observations and Insights Are Different Things

- **Observations** are what you heard, saw, or documented during research. They are factual and specific.
- **Themes** are labels for clusters of similar observations. They name the pattern.
- **Key insights** are inferences about what those patterns mean for product decisions.

A key insight is not a summary of a theme. It answers: "Given this pattern, what does that mean for what we should build or prioritize?"

##### The Grouping Is Not Permanent

The playbook tip: "Group your data in multiple ways to reveal new insights. There is no wrong way to do it."

Affinity mapping is iterative. If a different grouping reveals something the first pass missed, that is a feature, not a mistake. The artifact should invite re-examination, not lock conclusions.

##### Minimum Three Applies to Both Themes and Insights

Fewer than three themes usually signals that the grouping is too coarse. Fewer than three key insights usually signals that the synthesis stopped at clustering and never made the inferential leap.

##### The Sense-Making Is the Point

The value of affinity mapping lives in the team's debate over where each note belongs. Whoever does the grouping does the thinking. That is why the Playbook keeps the clustering, the theme labels, and the insights with the PM and their team, and casts AI as a guide through the method.

##### The Agent's Role: Coach by Default, Draft on Request

- **Real notes, default:** coach the PM through the method (Step 3). The PM groups, labels, and writes the insights. You teach, question, and illustrate. The line, from the Playbook: you may point at two notes and ask "are these the same behavior?" You may not say "these two go together under this theme."
- **Real notes, and the PM asks you to group them (or chooses best guess):** produce a draft map, labeled **AI draft grouping: for the team to challenge**. Show why each cluster holds together, and end with the groupings you were least sure of. The team still decides.
- **Fragments only:** coach or draft as above, and label every theme provisional.
- **No real notes:** stop. Affinity mapping on invented data teaches nothing and proves nothing. Offer to help prepare interviews (ps-empathy-interviews), or to set up the template for a workshop once notes exist. Never invent observations or quotes to map. Labeling the work "hypotheses" doesn't change this: produce no themes, clusters, or map layout at all. If the PM needs something for a meeting, offer a short plain list of assumptions to test in interviews, clearly labeled, and point to ps-empathy-interviews.

##### What Binds a Cluster

Test every grouping against the same questions:

- Do these notes share the same **behavior or need**, or just the same **topic**?
- Is this a **real pattern**, or a coincidence of wording?
- What binds them? Usually a **shared pain**, a **shared workaround**, or a **shared goal**.

A theme label captures that shared behavior or need. A label that only names a topic ("Technology," "Communication") has not found the pattern yet.

##### How AI Supports This Play

The Playbook casts AI as a **live guide through the method**. Affinity mapping often starts slow, with a pile of real notes and no clear way in. AI walks the PM through each grouping decision, one note or cluster at a time, and asks the questions that sharpen their reasoning: why does this note belong here, what separates this group from that one, is this a real pattern or a coincidence.

The clustering, the labels, and the insights stay the PM's calls. AI makes the method less intimidating. It does not make the decisions.

- **Use it when:** the PM has real interview or research notes and knows grouping needs to happen but doesn't know how to start.
- **Avoid it when:** there are no real notes yet. Guiding a method on fake data teaches nothing worth learning.
- **Return:** guidance through the method, and a completed set of grouped, labeled themes that the PM can explain and defend.

##### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

##### Guided Mode

When asked for guidance, when the user is unfamiliar, or when context is missing:

1. Explain the output and estimated question count. Offer Guided, Context dump, or Best guess; default to Guided and ask the first question immediately.
2. Use supplied context instead of asking again. In Context dump mode, summarize Known / Assumed / Missing / Conflicting first.
3. Ask one bolded question per turn with a progress label, three context-specific numbered recommendations, option 4 Other, and an input hint. For facts only the user can know, ask openly without suggested answers and explain why. Ground unfamiliar domain options in research when needed.
4. Adapt recommendations to the answers. Explain why a question matters when helpful.
5. Answer interruptions, honor corrections and mode switches, and stop when asked. Resume with a brief recap and the pending question.
6. Recap supplied facts, assumptions, gaps, and readiness; confirm before generating a guided artifact. When the user faces a decision, recommend an option with reasons and offer distinct alternatives. The user decides.
7. Best guess may proceed immediately: label inferred details inline and end with Assumptions to Validate, ranked by decision impact. With sufficient supplied context, execute directly.

#### Application

Use Template (uploaded reference: `03-discover-investigate.md`, section `ps-affinity-mapping / Template`) for the scaffold.


##### Required Output Convention

Default to a **clean, paste-ready artifact**.

That means:

- at least three labeled theme clusters, each with grouped observation bullets
- at least three key insights, each with a one-sentence title and a short paragraph
- observation bullets kept short (8-12 words each)
- key insight paragraphs sized for the template (50-80 words)
- explanation and methodology notes below the artifact, not inside the fields
- the map states who grouped it: **the team** (coached) or **AI draft grouping: for the team to challenge**

##### Step 1: Check the Source Data

Before grouping observations, verify the data is customer-side evidence: observations about customer behavior, experience, friction, and goals.

Flag and do not proceed if the observations are primarily:

- internal team opinions or preferences
- product feature requests written in the PM's voice
- engineering architecture notes
- stakeholder directives

Affinity mapping is only as useful as the evidence it synthesizes. If the input data is not customer-side, the output themes will reflect team assumptions, not customer reality.

##### Step 2: Collect Available Artifacts

Ask whether the user has materials to supply:

- empathy interview notes or transcripts
- customer feedback logs or support tickets
- survey open-text responses
- competitive research observations
- outputs from ps-empathy-interviews, ps-jobs-to-be-done, or ps-proto-persona

The more raw material supplied, the stronger the clustering. If only fragments are available, note that the resulting themes are provisional and should be validated before being used in ps-problem-identification.

Do not skip this ask.

##### Step 3: Coach the Method (Default)

Unless the PM asks you to group the notes, walk them through the Playbook's method one step at a time. Do not move on until they finish the current step. This mirrors the critique guidance in this Play.

1. **Orient.** In a few sentences, explain what affinity mapping is and what a good result looks like.
2. **Break notes into observations.** Coach the PM to put each distinct observation on its own note. Show one example of splitting a note that holds two ideas, then have them check theirs.
3. **Immerse.** Have the PM read all the notes first. Ask what stands out, what surprises them, what repeats. Do not summarize the notes for them.
4. **Group.** Have the PM put together notes that seem to share something. Test each grouping with the questions in [What Binds a Cluster](#what-binds-a-cluster). When they are stuck, offer the kinds of things that bind a cluster (shared pain, shared workaround, shared goal) to consider. Do not say which notes go together.
5. **Name the themes.** For each cluster, ask what the notes truly share and have the PM write the label. If the label only names a topic, show a generic example of a stronger label, then have them try again.
6. **Develop the key insights.** Have the PM write at least three. Test each with Step 6's rules.

Mark every example or suggestion as something to consider, accept, adjust, or reject, never as the answer. Keep the PM encouraged; this is a skill they are building. Then format what they commit into the template.

If the PM asks you to group the notes instead, Steps 4-6 below are how you build the draft. They are also the rules you hold the PM's own grouping to when coaching.

##### Step 4: Group the Observations

Cluster the raw observations into groups where similar findings sit together.

Rules for this step:

- Create at least three clusters. More is fine if the data warrants it.
- Do not force observations into neat categories if they genuinely sit between two clusters. A cross-cutting observation is useful data.
- Each cluster should be internally consistent: observations within a cluster should be meaningfully similar, not just topically adjacent.
- Do not discard outlier observations. Findings that do not cluster easily often signal the most overlooked problems.

##### Step 5: Label the Themes

Give each cluster a theme label that names the pattern happening in that cluster, not just the subject area.

Strong theme label: names what is happening for the customer.
- Example: "Scheduling Delays Caused by Disconnected Systems"
- Not: "Scheduling" or "System Problems"

Weak theme label: names a topic that could hold almost any observation.
- Example: "Process Issues" or "Communication Challenges"

Each theme label should be specific enough that a teammate unfamiliar with the research could roughly predict what observations belong inside it.

Default to 4 themes when the data supports it. The blank template has 4 circles. Do not artificially limit to 4 if the data warrants more.

##### Step 6: Develop the Key Insights

Write at least three key insights. One insight per major theme is the baseline. A particularly rich or important theme may warrant a dedicated insight even if it is not the largest cluster.

Each key insight has two required parts:

**Title (one sentence, 5-8 words):** Names the challenge or pattern in plain language.

**Paragraph (50-80 words):** Explains what this pattern means for product decisions. Should answer: What is happening for the customer? Why does it matter? What should the product team understand or do differently because of this?

Key insights are inferences, not summaries. If the insight paragraph could have been written by reading only the theme label, it has not done the synthesis work.

##### Step 7: Review for Completeness

Before finalizing:

- Did the team do the grouping, or is this an AI draft? If it is a draft, is it labeled as one, and has the team challenged it?

- Do the themes cover the breadth of the data, or is there a major cluster of observations that went unlabeled?
- Does any single observation appear in more than one theme cluster? If so, resolve which cluster owns it, or name it as a cross-cutting theme.
- Do the key insights answer "so what?" or do they just restate the theme label?
- Are there at least three themes and at least three insights?
- Are the observation bullets short enough to be paste-ready?

##### Step 8: Offer Next Steps

After delivering the completed affinity map, offer three paths:

1. **Use these key insights in ps-problem-identification** to turn the strongest patterns into candidate problem statements.
2. **Review the insights as a team** to identify which pattern represents the highest-priority problem to pursue.
3. **Re-run affinity mapping with a different grouping lens** to check whether a different clustering reveals patterns the first pass missed.

### ps-affinity-mapping / Template

##### When to Use This

Use this template during **Discover + Investigate** after you have collected qualitative observations from customer research. You are ready to map when you have raw notes from empathy interviews, customer feedback, survey responses, or other customer-side sources and need to organize them into patterns.

Upstream work that feeds this template: ps-empathy-interviews (primary), ps-jobs-to-be-done, ps-proto-persona.

Downstream: the key insights from this map feed ps-problem-identification.

##### Template

```markdown
# Affinity Map

## Research Context

- Product or service:
- Research conducted:
- Number of observation sources (interviews, surveys, feedback entries, etc.):
- Date mapped:
- Grouped by: The team (coached) / AI draft grouping: for the team to challenge

## Theme Clusters

Group your observations into clusters of similar findings. Label each cluster with a theme
that names the pattern, not just the subject area.

> Quality check: Does each theme label name what is happening for the customer, not just what
> the topic is?
> Quality check: For each cluster, can you say what binds it (a shared pain, workaround, goal,
> or behavior), and is it a real pattern rather than shared wording?
> Quality check: Is each observation a single idea? Split any note that holds two.
> Quality check: Are there at least three distinct clusters?
> Quality check: Do the clusters together cover the breadth of the data, not just the
> loudest findings?
> Capacity check: Theme label should be 6-10 words. Each observation bullet should be 8-12
> words. Aim for 5-8 observations per cluster.

### Theme 1: [Pattern Label]

- [Observation: what a customer said, did, or experienced]
-
-
-
-

### Theme 2: [Pattern Label]

- [Observation]
-
-
-
-

### Theme 3: [Pattern Label]

- [Observation]
-
-
-
-

### Theme 4: [Pattern Label] (add more themes as the data warrants)

- [Observation]
-
-
-
-

## Key Insights

Write at least three key insights. Each insight has a title (one sentence naming the
challenge or pattern) and a paragraph (50-80 words explaining what this pattern means
for product decisions).

Key insights are inferences, not summaries. The paragraph should answer: what is happening
for the customer, why does it matter, and what should the product team understand because
of this pattern?

> Quality check: Does each title name a challenge or pattern in plain language?
> Quality check: Does each paragraph answer "so what?" rather than restating the theme label?
> Quality check: Is each insight grounded in multiple observations, not a single anecdote?
> Capacity check: Title 5-8 words. Paragraph 50-80 words.

### Key Insight 1: [One-Sentence Title]

[Paragraph explaining what this pattern means for product decisions. What is the customer
experiencing? Why does this matter? What should the team understand or do differently
because of this finding?]

### Key Insight 2: [One-Sentence Title]

[Paragraph]

### Key Insight 3: [One-Sentence Title]

[Paragraph]

## Completeness Check

Before treating this map as final, confirm:

- [ ] All major clusters from the raw data are labeled (no significant observations left
      ungrouped)
- [ ] No observation appears in more than one theme cluster without resolution
- [ ] Each key insight answers "so what?" rather than restating its theme label
- [ ] At least three themes and at least three key insights are present
- [ ] Observation bullets are short enough to paste into the template (8-12 words each)

## Notes (optional)

- Observations that did not cluster:
- Themes considered and discarded:
- Suggested re-grouping angles to explore:
- Open questions for follow-up:
```

##### Usage Guidance

###### Filling the Template

1. Start with **Research Context** to anchor what data went into this map.
2. Fill **Theme Clusters** one at a time. Label the theme only after you have seen what observations belong together - resist naming the theme before clustering.
3. Write **Key Insights** after all clusters are labeled. Do not write insights cluster by cluster as you go; seeing all the clusters together often changes what the insights should say.
4. Run the **Completeness Check** before treating the map as done.
5. The **Notes** section is optional. Use it if there are outlier observations or re-grouping ideas worth capturing.

###### If You Have No Observation Data Yet

Affinity mapping requires input data. If no customer-side observations are available:

- Offer to help the user run ps-empathy-interviews first.
- If the user wants a scaffold to use in an upcoming workshop, fill the theme and insight sections with labeled placeholder sections and explain that they should be completed collaboratively with the team after data is collected.
- Do not generate observations from the agent's training data and present them as customer findings.

###### What Goes Where

| Section | Contains | Does NOT Contain |
|---------|----------|------------------|
| Theme Clusters | Direct customer observations grouped by pattern | Opinions, solutions, feature requests, team preferences |
| Theme Labels | A named pattern describing what is happening | A broad topic area that could hold any observation |
| Key Insights | Inferences about what the patterns mean for the product | Restatements of theme labels, feature recommendations |
| Notes | Outliers, open questions, re-grouping ideas | The main deliverable content |

###### Connecting to Other Skills

- **Upstream:** ps-empathy-interviews provides the raw observation notes. ps-jobs-to-be-done and ps-proto-persona provide additional customer context that can inform how observations are grouped.
- **Downstream:** The key insights from this map feed ps-problem-identification. The strongest insight often becomes the focal point for the candidate problem that gets developed in ps-framing-the-problem.

###### Capacity Reference

| Field | Guidance |
|-------|----------|
| Theme label | 6-10 words. Names the pattern, not the topic. |
| Observation bullet | 8-12 words. Direct, factual, customer-side. |
| Key insight title | 5-8 words. Plain language. |
| Key insight paragraph | 50-80 words. Answers "so what?" |

### ps-affinity-mapping / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** Freight-broker observations about chasing shipment updates form a pattern: visibility gaps create reactive operations. Keep each observation in one cluster and explain the implication.
- **Weak:** A cluster called "Visibility" names a topic without showing a pattern.
- **Drift to avoid:** Observation overlap: putting the same note in several clusters inflates the apparent evidence. Assign its primary meaning or split genuinely separate observations.


#### Common Pitfalls

- **Naming Themes by Topic, Not Pattern:** Name what is happening, not what it is about. "Fragmented Communication Tools Slow Handoffs" has diagnostic value. "Communication" does not.

- **Treating Key Insights as Summaries:** Write insights that answer "so what?" and "what does this mean for what we prioritize or build?" If the insight paragraph could have been inferred from the label alone, it is not yet an insight.

- **Discarding Outlier Observations:** Keep outlier observations visible. If multiple outliers cluster loosely together, name that as an emerging theme. If a single observation stands alone, flag it in the completeness review.

- **Collapsing Distinct Themes to Hit a Target Count:** Keep themes separate if the underlying observations point to different root causes or different customer roles. Six specific themes are more useful than three bloated ones.

- **Mapping Team Opinions Instead of Customer Evidence:** Return to Step 1. Replace internal opinion entries with direct customer observations. If no customer-side data exists yet, run ps-empathy-interviews before mapping.

- **Stopping at the Cluster, Skipping the Insight:** Always complete the key insights section before treating the affinity map as done.

- **Running Affinity Mapping Alone:** Run affinity mapping as a cross-functional team exercise. The process of debating where an observation belongs is part of the value. When the group agrees on a theme label, they have done the sensemaking together.

- **Writing Insights Too Narrowly to Be Actionable:** Key insights should reflect patterns across multiple observations from multiple customers or sources. If only one observation supports a theme, the theme may not yet be valid.

- **AI's Themes Quietly Become the Team's:** Coach by default (Step 3). If the PM asks for a draft grouping, label it as one, show why each cluster holds together, and have the team challenge it before anything moves downstream.

- **Guided Is Mistaken for Validated:** State the evidence base on the map (number and type of sources). Mark themes resting on thin evidence as provisional, and name what more research would confirm them.

#### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-affinity-mapping) for supporting source material and expanded examples.

## ps-problem-identification | Problem Identification

Playbook number: 09. Phase: Discover + Investigate.

### ps-problem-identification / Instructions

#### Purpose

Create a **Productside-style Problem Identification artifact** from customer research.

This skill helps a Product Manager turn customer understanding into a compact working surface:

- customer jobs
- pains
- gains
- supporting empathy interview quotes
- candidate problem statements

The point is not to produce a long explanation of the problem space. The point is to help the human complete the play.

This artifact is also a **cross-functional alignment tool.** The output makes customer understanding visible, shareable, and debatable across product, design, engineering, and leadership  -  not just useful to the PM who ran the discovery.

##### Usage Notes

- This exemplar follows the `ps-` naming contract
- It is intentionally budget-aware and template-capacity-aware
- Most default outputs should stay sticky-note-sized or small-cell-sized
- **Coach by default:** the skill asks the PM for the root cause beneath each pain rather than naming it, and catches features posing as problems
- **Evidence honesty:** quotes come only from supplied research (unfilled slots are marked `[needs a real quote]`), and unvalidated causes are marked `[CAUSE TO VALIDATE]`

#### Key Concepts

##### This Play Is an Aggregator

Problem Identification is where earlier discovery work gets pulled together:

- jobs from Jobs-to-Be-Done
- pains and outcomes from Personas & Proto-Personas
- quotes and lived experience from Empathy Interviews
- patterns from Affinity Mapping

The skill should therefore synthesize, not restart discovery from scratch. **Jobs brought in from earlier work should be treated as revisable**  -  as you validate with customers, reframe any job that doesn't hold up. Evidence updates the artifact; don't treat earlier assumptions as fixed truth.

##### The Customer Circle Is the Visual Structure

The canonical template organizes this play as a concentric circle:

- **Center:** the customer persona
- **Inner ring:** Pains and Gains
- **Outer ring:** Customer Jobs
- **Outside the circle:** Problems (root causes of pains, barriers to gains)
- **Sidebar:** Empathy Interview Quotes

This structure is not decoration  -  it shows how problems relate to jobs and how pains and gains are distinct layers between the customer and the things blocking them. A PM filling this template should be thinking in those concentric layers, not just populating a flat list.

##### Problem Statements Use a Specific Productside Format

Candidate problems should use this structure:

`[Problem] gets in the way of achieving [Outcome] for [Persona].`

Do not improvise a different sentence form unless the user explicitly asks for alternatives.

##### Jobs, Pains, Gains, and Problems Are Not the Same

- **Customer jobs** = what the customer is trying to get done
- **Pains** = friction, obstacles, or negative experience
- **Gains** = positive outcomes or benefits they want
- **Problems** = root causes or barriers that block gains or create pains

If these blur together, the play gets muddy fast.

##### A Pain Is a Symptom; a Problem Is the Cause Beneath It

A pain is what the customer **feels**. A problem is the **root cause** that creates the pain or blocks the outcome. "Passengers arrive unprepared" is a pain. "Confusing or late prep instructions" is a cause. Restating a pain in the problem format ("Unprepared passengers get in the way of...") skips the diagnosis while looking finished.

To get from pain to problem, ask what creates the pain. If the answer is the pain reworded, keep digging.

##### A Missing Feature Is Not a Problem

"No real-time dashboard," "lack of integration," and "no automated alerts" name solutions by their absence. When a candidate problem is really a missing feature, ask what problem that feature would solve, and write that instead. Keep the play in the problem space.

##### A Clean Statement Is Not a Proven One

The format makes thinking legible, not correct. A root cause stays a hypothesis until interviews back it. Mark every cause that isn't yet backed by evidence `[CAUSE TO VALIDATE]`, so the team knows what to test before framing the problem in the next play.

##### The Agent's Role: Coach by Default, Draft on Request

- **Default:** for each pain, ask the PM what root cause creates it. Push back when the answer is the pain reworded or a feature in disguise. Once the PM names a real cause, help write it in the Productside format and sharpen the wording. Do not name the cause for them, in any form: no lists, no examples ("it might be..."), and no causes folded into a question ("Is it that she can't see X, or that Y?"). Ask open questions about what the PM heard, saw, or was told ("What happens today when...? What did they say gets in the way?").
- **On request, or in best guess mode:** propose candidate causes, each marked `[CAUSE TO VALIDATE]`, for the PM to accept, adjust, or reject.
- **Always:** never invent quotes, outcomes, or personas. Quotes come only from supplied research.

##### Quotes Are Supporting Evidence, Not Decoration

The quotes help prove the candidate problems are grounded in real customer experience.

They should sound like lived reality, not sanitized summary copy.

##### Template Capacity Matters

The canonical Productside template for this play has many **sticky-note-sized or small-cell fields**.

That means the default output must be:

- short
- specific
- paste-ready

Do not generate mini-essays for fields that behave like notes.

See Template and capacity guidance (uploaded reference: `03-discover-investigate.md`, section `ps-problem-identification / Template`) for the real canonical budgets.

##### How AI Supports This Play

The Playbook casts AI as a **coach that separates pains from problems and formats the result**. The PM has done the research. AI helps shape affinity themes, interview insights, jobs, and personas into sharp, well-formed problem statements. The cause has to come from the PM and their evidence.

- **Use it when:** the PM has real insights from affinity mapping and interviews and wants help separating symptoms from causes.
- **Avoid it when:** the PM has not talked to customers yet. AI will format confident root causes and problem statements no one can defend. Say so, and route to ps-empathy-interviews.
- **Return:** pains separated from the root causes beneath them, problem statements in one consistent format, and every guessed root cause marked `[CAUSE TO VALIDATE]`.

##### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

##### Guided Mode

When asked for guidance, when the user is unfamiliar, or when context is missing:

1. Explain the output and estimated question count. Offer Guided, Context dump, or Best guess; default to Guided and ask the first question immediately.
2. Use supplied context instead of asking again. In Context dump mode, summarize Known / Assumed / Missing / Conflicting first.
3. Ask one bolded question per turn with a progress label, three context-specific numbered recommendations, option 4 Other, and an input hint. For facts only the user can know, ask openly without suggested answers and explain why. Ground unfamiliar domain options in research when needed.
4. Adapt recommendations to the answers. Explain why a question matters when helpful.
5. Answer interruptions, honor corrections and mode switches, and stop when asked. Resume with a brief recap and the pending question.
6. Recap supplied facts, assumptions, gaps, and readiness; confirm before generating a guided artifact. When the user faces a decision, recommend an option with reasons and offer distinct alternatives. The user decides.
7. Best guess may proceed immediately: label inferred details inline and end with Assumptions to Validate, ranked by decision impact. With sufficient supplied context, execute directly.

#### Application

Use Template (uploaded reference: `03-discover-investigate.md`, section `ps-problem-identification / Template`) for the scaffold.


##### Required Output Convention

Default to a **clean, paste-ready artifact**.

That means:

- fill every expected slot in the template
- jobs, pains, and gains should be short enough for sticky-note or small-cell use
- quotes should be short enough to fit the playbook cells
- problem statements should fit the canonical carrying capacity
- explanation belongs below the artifact, not inside the fields

For the default output, produce exactly:

- 4 customer jobs
- 4 pains
- 4 gains
- up to 6 empathy interview quotes, **real quotes only**
- 6 candidate problem statements

Do not silently reduce those counts because a shorter list feels more elegant. The one exception is quotes: never invent a quote to fill a slot. If the research supplies fewer than six, fill the rest with `[needs a real quote]`.

Append `[CAUSE TO VALIDATE]` to any candidate problem whose root cause is not yet backed by evidence.

If the user wants extended reasoning, add it after a fully completed artifact in a short trailing note.

##### Step 1: Start from Customer Evidence

Before drafting, ask the user whether they have materials to share that would ground the artifact in real evidence:

- customer interview notes or transcripts
- support tickets or call logs
- quotes already collected
- jobs, pains, or gains identified in earlier discovery
- persona or proto-persona output
- any other internal research or field observations

This skill synthesizes earlier discovery work - the more the user can supply, the less the output relies on assumption. Do not skip this ask.

If there is no customer evidence at all, say so plainly. The Playbook advises against this play until the PM has talked to customers. Recommend ps-empathy-interviews first. If the PM still wants a first pass (best guess), produce it as a labeled hypothesis: no quotes (every slot `[needs a real quote]`), and every candidate problem marked `[CAUSE TO VALIDATE]`.

##### If the PM Brings a Draft

When the PM arrives with pains and a first read on their causes, or with drafted problem statements, work through them rather than redrafting. This mirrors the critique guidance in this Play.

1. **For each pain, ask for the root cause.** If the PM's answer is the pain reworded, say so and ask them to dig.
2. **Watch for solutions in disguise.** If a "problem" is a missing feature, point at it and ask what problem the feature would solve. Don't list candidate causes for the PM to pick from, and don't hint at them as examples or "is it X or Y?" questions; the cause has to come from what they heard. This applies to a cause that looks like a symptom, too: ask why it happens, without guessing the answer.
3. **Format the real causes.** Write each as `[Problem] gets in the way of achieving [Outcome] for [Persona]`, pulling the outcome and persona from what the PM gave you.
4. **Mark the guesses.** Append `[CAUSE TO VALIDATE]` to any cause the PM is still guessing at.

##### Step 2: Write the Customer Jobs

Capture what the customer is trying to get done.

For this play, jobs should be **compact**. Most should fit in a sticky-note-sized field.

Avoid:

- broad mission statements
- generic aspirations
- internal team tasks

Prefer:

- short action-oriented job statements
- concrete customer progress

Output exactly 4 jobs unless the user explicitly asks for a different count.

##### Step 3: Identify Pains

Pains are the friction, obstacles, risks, delays, confusion, or negative experiences surrounding the job.

Keep them short enough to paste directly into the playbook.

Do not turn them into explanation paragraphs.

Output exactly 4 pains unless the user explicitly asks for a different count.

##### Step 4: Identify Gains

Gains are the positive outcomes the customer wants when the job goes well.

Keep gains distinct from pains:

- pains remove friction
- gains create positive progress or benefit

Output exactly 4 gains unless the user explicitly asks for a different count.

##### Step 5: Select Supporting Quotes

Choose quotes that make the problem feel real. **Select them from the research the PM supplied. Never write them.** A quote the agent wrote is not evidence, however real it sounds.

Good quotes:

- show frustration, workaround, or unmet need
- were actually said by a customer
- are short enough to fit the template

Output up to 6 quotes. Mark any unfilled slot `[needs a real quote]`.

##### Step 6: Write Candidate Problems

Use the Productside sentence structure:

`[Problem] gets in the way of achieving [Outcome] for [Persona].`

Each candidate should be:

- concrete
- customer-centered
- a cause, not a pain reworded or a missing feature
- short enough to fit the canonical field

By default, get the cause from the PM (see [If the PM Brings a Draft](#if-the-pm-brings-a-draft)). Mark any cause not yet backed by evidence `[CAUSE TO VALIDATE]`.

Do not pad the sentence with unnecessary context. The field is small.

Output exactly 6 candidate problems unless the user explicitly asks for a different count.

##### Step 7: Keep the Artifact Compact

For this skill, brevity is usability.

If the output is so long that the human Product Manager has to rewrite it before using it, the skill has failed.

Do not let good prose outrank usable template completion.

##### Step 8: Add Optional Short Notes

If helpful, add a brief trailing section such as:

- `What to pressure-test next`
- `Weakest candidate problems`
- `Open evidence gaps`

Keep it separate from the paste-ready artifact.

Do not add a notes section at all unless:

- the user asks for it, or
- the artifact is already fully complete

### ps-problem-identification / Template

Use this template to build a **Productside-style Problem Identification artifact** from customer research.

Most fields in this play are small. Keep entries compact and paste-ready.

##### Template

```markdown
# Problem Identification

## Product Context
- Product or service:
- Target persona:
- Research source:

## Customer Jobs
- Job 1:
- Job 2:
- Job 3:
- Job 4:

> Quality check: Keep jobs short and concrete. Most should fit in a sticky-note-sized field.
> Completion rule: Fill all 4.

## Pains
- Pain 1:
- Pain 2:
- Pain 3:
- Pain 4:

> Quality check: These are obstacles, risks, frustrations, or negative experiences. Keep them compact.
> Completion rule: Fill all 4.

## Gains
- Gain 1:
- Gain 2:
- Gain 3:
- Gain 4:

> Quality check: Gains are positive outcomes the customer wants, not just the absence of pains.
> Completion rule: Fill all 4.

## Empathy Interview Quotes
- Quote 1:
- Quote 2:
- Quote 3:
- Quote 4:
- Quote 5:
- Quote 6:

> Quality check: Every quote was actually said by a customer and is short enough to fit the template.
> Completion rule: Real quotes only. Mark any unfilled slot `[needs a real quote]`. Never invent one.

## Candidate Problems
- Problem 1: [Problem] gets in the way of achieving [Outcome] for [Persona].
- Problem 2: [Problem] gets in the way of achieving [Outcome] for [Persona].
- Problem 3: [Problem] gets in the way of achieving [Outcome] for [Persona].
- Problem 4: [Problem] gets in the way of achieving [Outcome] for [Persona].
- Problem 5: [Problem] gets in the way of achieving [Outcome] for [Persona].
- Problem 6: [Problem] gets in the way of achieving [Outcome] for [Persona].

> Quality check: Keep each candidate short enough to paste directly into the playbook field. Do not add explanation inside the statement.
> Quality check: Is each [Problem] a root cause, not a pain reworded and not a missing feature?
> Evidence check: Append `[CAUSE TO VALIDATE]` to any candidate whose cause is not yet backed by evidence.
> Completion rule: Fill all 6.

## What To Pressure-Test Next
- Which problem feels strongest?
- Which problem feels weakest?
- What evidence gap still matters?
```

##### Usage Guidance

- Do not turn jobs, pains, gains, or problems into paragraphs.
- If the user wants explanation, add it after the artifact.
- Respect the canonical template capacity in Template and capacity guidance (uploaded reference: `03-discover-investigate.md`, section `ps-problem-identification / Template`).
- Do not add the `What To Pressure-Test Next` section unless the artifact is already fully complete.

### ps-problem-identification / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** "Late schedule updates get in the way of keeping dock assignments aligned." Connect this candidate to real observations and retain the customer's language.
- **Weak:** A paragraph combining several problems makes it hard to investigate any one of them.
- **Drift to avoid:** Missing feature as problem: "No dashboard" is a solution-shaped complaint. Identify the customer progress it obstructs.


#### Common Pitfalls

- **Writing Novellas into Sticky-Note Fields:** Respect the template capacity. Small field means short entry.

- **Pitfall 1b: Underfilling the Template:** Match the template slot count by default.

- **Confusing Pains with Problems:** Use pains as evidence, then write a candidate problem in the Productside format.

- **Writing Generic Jobs:** Write short but concrete customer jobs.

- **Making Gains a Mirror Image of Pains:** Ask what better looks like for the customer, not just what less-bad looks like.

- **Losing the Quotes:** Include short quotes that support the candidate problems.

- **Letting Commentary Replace the Artifact:** Complete the artifact first. Commentary is optional and trailing only.

- **Naming a Missing Feature as the Problem:** Ask what problem the missing feature would solve, and write that. "Late notice of policy changes gets in the way of achieving compliance for Henry" leaves the solution open.

- **Format Mistaken for Proof:** Mark every cause not yet backed by evidence `[CAUSE TO VALIDATE]`. Name the evidence base in Product Context. Treat the marked causes as the next round's interview topics.

- **Inventing Quotes to Fill the Slots:** Quotes come only from supplied research. Leave unfilled slots as `[needs a real quote]`.

#### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-problem-identification) for supporting source material and expanded examples.

## ps-framing-the-problem | Framing the Problem

Playbook number: 10. Phase: Discover + Investigate.

### ps-framing-the-problem / Instructions

#### Purpose

Create a **Productside-style Framing the Problem artifact** that documents a validated problem and produces a clear problem statement.

This skill is for the **Discover + Investigate** phase and marks a **Key Decision Point** in the Productside Blueprint. It sits at the intersection of Investigate and Define - the PM is deciding that the problem is validated enough to move forward into solution definition.

This is a synthesis skill. It pulls together findings from earlier discovery work:

- persona work (ps-proto-persona)
- jobs-to-be-done (ps-jobs-to-be-done)
- empathy interviews
- problem identification (ps-problem-identification)
- affinity mapping

The output is a structured problem frame using the five-stem sequence, context and constraints, and a final problem statement. This artifact is what the PM reviews with their manager and introduces to product governance.

Use this skill when you need to:

- synthesize prior discovery into a single, reviewable problem definition
- craft a problem statement that leadership can evaluate and act on
- document the customer perspective before moving into solution space
- validate that the team is solving a real, evidence-backed problem

This is not a solution specification. If the output mentions features, tools, or implementation approaches, the framing has drifted into solution space.

##### Usage Notes

- The template produces a single artifact with three sections: Problem Framing (five stems), Context and Constraints, and Final Problem Statement.
- The five-stem sequence is fixed order: I am / Trying to / But / Because / Which makes me feel.
- Evidence gathering is **user artifacts only** - no web research offered. This skill synthesizes the PM's own discovery work.
- Upstream: ps-proto-persona, ps-jobs-to-be-done, ps-problem-identification, empathy interviews.
- Downstream: solution hypothesis, positioning, exploring the solution space (Discover + Define phase).

#### Key Concepts

##### Focus on the Why, and the Outcomes Will Follow

The playbook puts it simply: *"Focus on the 'why,' and the outcomes will follow."*

A problem frame that nails the root cause  -  the **Because** stem  -  gives the team more clarity about what to build than any amount of solution sketching. Don't rush to "what we need to build" before the "why this problem exists" is solid.

This is also a human-centered design exercise. It starts with the person experiencing the problem, not the solution space, and leaves room for creativity and imagination once the why is clear.

##### The Five-Stem Sequence Is a Fixed Structure

The Productside problem frame uses five stems in exact order. Do not reorder, skip, or merge them:

1. **I am:** Describe the user persona's experience with the problem in 3-4 key points
2. **Trying to:** List the outcome they care about
3. **But:** Describe what problem barriers stand in the way
4. **Because:** Enter the root cause of why the problem or barrier exists
5. **Which makes me feel:** Describe the emotions from the customer's point of view

Each stem has a specific job. "I am" establishes who and what they face. "Trying to" names the desired outcome. "But" names the concrete barriers. "Because" explains the root cause. "Which makes me feel" captures the emotional impact. Together they build a complete problem frame from the customer's perspective.

##### Context and Constraints Are Separate from the Problem Frame

Section 2 of the template captures the external conditions surrounding the problem - industry dynamics, regulatory requirements, geographic limitations, technology constraints, budget restrictions, or population characteristics.

These are not barriers (barriers go in "But"). Constraints are the environment the problem exists within. A barrier is what blocks the persona. A constraint is a condition the solution must operate within.

##### The Final Problem Statement Synthesizes the Stems

Section 3 takes the five stems and combines them into one cohesive problem statement. The statement should read as a single flowing narrative that a manager or governance body could understand without seeing the stem breakdown.

The statement must be consistent with the stems above it. If the final statement introduces new information not in the stems, or drops key elements, the frame is broken.

##### This Is a Decision Point

The playbook explicitly marks this template as a Key Decision Point. The output goes to leadership and product governance. The PM is saying: "I have identified and validated this problem. I want to move into defining a solution."

This means the problem frame should be polished enough to present, not a rough working draft. It also means the evidence behind it should be real - from customer research, not from assumptions.

##### Customer Perspective, Not Product Team Perspective

Every stem is written from the customer's point of view. "I am" refers to the customer. "Which makes me feel" captures the customer's emotions. If any stem reads like something the product team would say about their own work, the perspective has drifted.

##### Problem Framing, Not Solution Framing

No solution language is allowed in the problem frame. Do not mention:

- product names or features
- tools or technologies that could solve the problem
- implementation approaches
- "we need to build" or "the product should"

The problem frame describes the world as the customer experiences it today. Solutions come later, in a different play.

##### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **critic of the problem frame the PM drafted**. It checks each stem of the I am / Trying to / But / Because / Which makes me feel sequence for customer voice and evidence, catches a solution hiding in the frame, and tests whether the final statement synthesizes the stems. The frame stays the PM's, built from their discovery evidence.

- **Use it when:** the PM has discovery evidence and a draft frame, and wants it pressure-tested before the decision point.
- **Avoid it when:** there is no discovery evidence yet. A well-formed frame on a guessed problem is still a guess. Route to ps-problem-identification or ps-empathy-interviews.
- **Return:** each stem checked for customer voice, specificity, and evidence; solution language flagged; and the final statement tested against the stems.

##### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

##### Guided Mode

When asked for guidance, when the user is unfamiliar, or when context is missing:

1. Explain the output and estimated question count. Offer Guided, Context dump, or Best guess; default to Guided and ask the first question immediately.
2. Use supplied context instead of asking again. In Context dump mode, summarize Known / Assumed / Missing / Conflicting first.
3. Ask one bolded question per turn with a progress label, three context-specific numbered recommendations, option 4 Other, and an input hint. For facts only the user can know, ask openly without suggested answers and explain why. Ground unfamiliar domain options in research when needed.
4. Adapt recommendations to the answers. Explain why a question matters when helpful.
5. Answer interruptions, honor corrections and mode switches, and stop when asked. Resume with a brief recap and the pending question.
6. Recap supplied facts, assumptions, gaps, and readiness; confirm before generating a guided artifact. When the user faces a decision, recommend an option with reasons and offer distinct alternatives. The user decides.
7. Best guess may proceed immediately: label inferred details inline and end with Assumptions to Validate, ranked by decision impact. With sufficient supplied context, execute directly.

#### Application

Use Template (uploaded reference: `03-discover-investigate.md`, section `ps-framing-the-problem / Template`) for the full scaffold.


##### Required Output Convention

Default to a **clean, paste-ready problem frame artifact**.

That means:

- fill all five stems, context and constraints, and the final problem statement
- keep each stem within its word budget (see Capacity Reference below)
- produce a final statement that synthesizes the stems into one cohesive narrative
- explanation belongs below the artifact, not inside the stem fields
- the artifact comes first; commentary is secondary

##### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

##### Step 1: Confirm the Product and Persona

Before writing anything, answer:

- what product or service is the PM building?
- who is the customer persona whose problem is being framed?
- what prior discovery work exists (persona, JTBD, empathy interviews, problem identification)?

If you cannot identify a specific customer persona, stop and resolve the target first.

**Guard against tech-role bias.** The problem belongs to the customer - the person who uses or buys the product in the field. A clinical data platform's customer problem belongs to a clinical operations lead, not a data engineer. An industrial IoT platform's customer problem belongs to a plant manager, not a solutions architect. Before writing the "I am" stem, confirm: does this person actually experience the problem day-to-day?

##### Step 2: Gather Evidence Before Writing

Once you know the product and persona, offer the user materials to share before drafting:

**User-supplied artifacts** - ask whether the user has materials to ground the frame: interview notes, empathy mapping output, problem identification artifacts, JTBD work, support tickets, or earlier skill outputs.

This skill is **user artifacts only** - it synthesizes the PM's own discovery work. Web research is not offered because the problem frame should come from validated customer evidence, not from external sources the PM has not yet verified.

If the user has no artifacts and no prior discovery work, surface the tension: a problem frame without evidence is an assumption frame. Recommend doing persona, JTBD, or empathy interview work first, but proceed if the user wants to draft an assumption-based frame.

##### Step 3: Fill the "I am" Stem

Describe the persona's experience with the problem in 3-4 key points.

This stem establishes:

- who the persona is (role, not name)
- what their situation looks like
- what they are dealing with day-to-day

Write from the persona's perspective. Use concrete, specific language. "An HR specialist overwhelmed by manual processes" is better than "a professional facing challenges."

Word budget: ~30-40 words.

##### Step 4: Fill the "Trying to" Stem

State the outcome the persona cares about - what they are trying to achieve.

This is not a task list. It is the desired end state. "Automate administrative tasks and free up time for strategic initiatives" describes an outcome. "Complete form A-7 by Friday" describes a task.

Word budget: ~15-20 words.

##### Step 5: Fill the "But" Stem

Name the concrete barriers that stand in the way of the desired outcome.

Barriers are specific and observable:

- "Manual and time-consuming HR processes" - concrete
- "Things are difficult" - vague and useless
- "Outdated systems and fragmented tools slow progress" - concrete

Do not put constraints here. Constraints (regulatory, budget, geographic) go in Context and Constraints. Barriers are what blocks the persona from achieving their outcome.

Word budget: ~20-25 words.

##### Step 6: Fill the "Because" Stem

Explain the root cause - why the barrier exists.

This is the "why behind the why." The barrier is what blocks; the root cause is why that barrier persists. If the barrier is "manual and time-consuming processes," the root cause might be "the lack of an integrated platform and real-time data access."

Push past surface-level causes. "Because things have always been done this way" is not a root cause. "Because the organization's systems were implemented independently over a decade and were never integrated" is closer.

Word budget: ~20-25 words.

##### Step 7: Fill the "Which makes me feel" Stem

Capture the emotional impact from the persona's point of view.

This stem is not optional. It grounds the problem frame in the human experience. Product governance decisions are influenced by understanding the severity of the problem, and emotional impact is part of severity.

Use specific emotional language:

- "Frustrated, stressed, and unable to deliver the value my role demands" - specific
- "Bad" - not specific enough
- "Overwhelmed by the gap between what is expected and what is possible" - specific

Word budget: ~15-20 words.

##### Step 8: Write Context and Constraints

Document the external conditions surrounding the problem:

- **Industry context** - regulatory environment, competitive dynamics, market pressures
- **Geographic constraints** - regional requirements, distributed operations
- **Technology constraints** - legacy systems, integration limitations
- **Budget constraints** - limited resources, competing priorities
- **Population constraints** - characteristics of the target users

Constraints frame the environment the solution must operate within. They are not barriers (those went in "But") and they are not the problem itself.

Word budget: ~30-40 words.

##### Step 9: Synthesize the Final Problem Statement

Combine the five stems into one cohesive statement.

The final statement should:

- read as a single flowing narrative
- use the stem structure: "I am [role] [situation]. Trying to [outcome]. But [barriers]. Because [root cause]. Which makes me feel [emotions]."
- be consistent with the stems above - no new information, no dropped elements
- be presentable to leadership without additional context

Word budget: ~40-50 words.

##### Step 10: Keep the Artifact Compact

The canonical template uses defined fields with limited space. Every stem, the context section, and the final statement should fit within the word budgets specified.

If the output requires summarizing before it can be pasted into the playbook, it is too long.

Do not let good prose outrank usable template completion.

##### Step 11: Offer Next Steps

After the artifact is complete, offer the user up to three next-step options:

1. **Move to solution hypothesis** - the problem is framed and validated; begin exploring what to build (Discover + Define phase)
2. **Refine positioning** - use the problem frame to sharpen how the product is positioned against the problem
3. **Review upstream work** - if the problem frame exposed gaps, go back to proto-persona, JTBD, or empathy interviews to strengthen the evidence

Present these as options, not as mandatory steps. The user decides what comes next.

### ps-framing-the-problem / Template

##### When to Use This

Use this template during **Discover + Investigate** when you have enough discovery evidence to frame a validated problem and craft a problem statement. This is a **Key Decision Point** - the output goes to leadership and product governance to justify moving into solution definition.

Upstream work that feeds this template: proto-persona, jobs-to-be-done, empathy interviews, problem identification, affinity mapping.

##### Template

```markdown
# Framing the Problem

## Product Context

- Product or service:
- Target market segment:
- Primary persona (the customer with the problem):

## 1. Problem Framing

**I am:**
Describe the user persona's experience with the problem in 3-4 key points


**Trying to:**
List the outcome they care about


**But:**
Describe what problem barriers stand in the way


**Because:**
Enter the root cause of why the problem or barrier exists


**Which makes me feel:**
Describe the emotions from the customer's point of view


> Quality check: Is every stem written from the customer's perspective, not the product team's?
> Quality check: Does the "But" name concrete, observable barriers - not vague "challenges"?
> Quality check: Is the "Because" a root cause, not a restatement of the barrier?
> Quality check: Is the "Which makes me feel" stem present with specific emotions, not just "frustrated"?
> Quality check: Is there any solution language in the stems (product names, features, tools)? Remove it.
> Capacity check: I am ~30-40 words. Trying to ~15-20 words. But ~20-25 words. Because ~20-25 words. Which makes me feel ~15-20 words.

## 2. Context and Constraints

Describe the industry, regulatory, geographic, technology, budget, or population constraints surrounding the problem.


> Quality check: Are these external conditions, not barriers? Barriers go in "But." Constraints describe the environment the solution must operate within.
> Capacity check: ~30-40 words.

## 3. Final Problem Statement

Synthesize the five stems into one cohesive statement.


> Quality check: Does the statement follow the stem structure (I am / Trying to / But / Because / Which makes me feel)?
> Quality check: Is every element in the statement traceable to a stem above? No new information should appear here.
> Quality check: Could a manager read this statement alone and understand the problem without seeing the stems?
> Capacity check: ~40-50 words.

## Evidence Notes (optional)

- Discovery sources used:
- What is well-supported by evidence:
- What is still assumption:
- Recommended next validation steps:
```

##### Usage Guidance

###### Filling the Template

1. Start with **Product Context** to anchor who this is for and whose problem it is.
2. Fill the **five stems in order** - do not skip or reorder. Each stem builds on the previous one.
3. Fill **Context and Constraints** separately - these are external conditions, not part of the problem frame itself.
4. Write the **Final Problem Statement** last, synthesizing all five stems into one cohesive narrative.
5. The **Evidence Notes** section is optional and trailing. Do not let it displace or delay the main artifact.

###### The Stem Sequence Is Fixed

The five stems must appear in this exact order:

1. I am
2. Trying to
3. But
4. Because
5. Which makes me feel

Do not merge stems, skip stems, or reorder them. Each has a distinct function in building the problem frame.

###### What Goes Where

| Section | Contains | Does NOT Contain |
|---------|----------|------------------|
| I am | Persona role, situation, 3-4 key experience points | Product features, team perspective |
| Trying to | The desired outcome | Task lists, feature requests |
| But | Concrete, observable barriers | Constraints (those go in Context) |
| Because | Root cause of the barrier | Surface-level restatements |
| Which makes me feel | Specific customer emotions | "Bad" or "frustrated" alone |
| Context and Constraints | Industry, regulatory, budget, technology, geographic conditions | Barriers (those go in But) |
| Final Problem Statement | Synthesis of all five stems | New information not in the stems |

###### Connecting to Other Skills

- **Upstream:** Proto-persona provides the "I am." JTBD provides the "Trying to." Problem Identification provides barriers, root causes, and candidate problems. Empathy interviews provide emotional evidence.
- **Downstream:** The validated problem statement justifies moving into Discover + Define - solution hypothesis, positioning, exploring the solution space.

###### Capacity Reference

See Template and capacity guidance (uploaded reference: `03-discover-investigate.md`, section `ps-framing-the-problem / Template`) for the exact word and character budgets per field.

| Field | Word Budget | Guidance |
|-------|-------------|----------|
| I am | ~30-40 | Role + situation + 3-4 key experience points |
| Trying to | ~15-20 | One clear outcome statement |
| But | ~20-25 | Concrete barriers, not vague "challenges" |
| Because | ~20-25 | Root cause, not barrier restatement |
| Which makes me feel | ~15-20 | 2-3 specific emotions with context |
| Context and Constraints | ~30-40 | External conditions bounding the solution space |
| Final Problem Statement | ~40-50 | Cohesive synthesis of all five stems |

### ps-framing-the-problem / Examples

Illustrative and fictional, not customer evidence.

- **Strong:** A superintendent is trying to coordinate trades, but learns of sequencing changes too late because crews rely on disconnected updates, leaving them anxious about rework. Develop all five stems.
- **Weak:** "We need a scheduling dashboard" names a solution rather than a customer problem.
- **Drift to avoid:** Perspective inversion: "Our team needs to ship faster" frames the product team's work, not the superintendent's experience.


#### Common Pitfalls

- **Jumping to Solutions in the Problem Frame:** Strip out any mention of products, features, tools, or technologies. Rewrite barriers as the customer's experienced friction: "But manual processes across disconnected systems create delays and errors."

- **Writing from the Product Team's Perspective:** Every stem must be written from the customer's point of view. The "I am" is the customer. The emotions in "Which makes me feel" are the customer's emotions. If the frame sounds like a project brief, the perspective has drifted.

- **Making the "But" Too Vague:** Name concrete, observable barriers. What specifically blocks the persona? What do they run into? What fails, breaks, or takes too long? "But manual data reconciliation across three disconnected systems creates weekly reporting delays of 2-3 days."

- **Skipping the Emotional Stem:** Write 2-3 specific emotions with context. "Frustrated" alone is not enough. "Frustrated by the gap between what leadership expects and what current tools allow, and anxious about being seen as ineffective" tells a story.

- **Conflating Constraints with Barriers:** Barriers go in "But" - these are things the persona runs into while trying to achieve their outcome. Constraints go in Context and Constraints - these are conditions the solution must operate within. A barrier is "manual processes create delays." A constraint is "the industry requires SOC 2 compliance."

- **Final Statement Does Not Match the Stems:** The final statement is a synthesis of the stems, not a rewrite. Every element in the statement should trace back to a stem. If the statement needs new information, update the stems first.

- **Defaulting to a Tech Role as the Persona:** Before writing "I am," confirm who actually uses or buys the product in the field. Most products serve people whose primary job is not writing code. A clinical data platform's customer is a clinical operations lead, not a data engineer.

- **Exceeding Template Capacity:** Respect the word budgets. "I am" is ~30-40 words. "Trying to" is ~15-20. "But" is ~20-25. "Because" is ~20-25. "Which makes me feel" is ~15-20. Context is ~30-40. Final statement is ~40-50. Write for the template field, not for the model's appetite for prose.

- **A Frame With No Evidence Under It:** Ask what evidence backs each stem. Mark any stem without evidence as a hypothesis, and route back to discovery before the decision point.

#### References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-framing-the-problem) for supporting source material and expanded examples.
