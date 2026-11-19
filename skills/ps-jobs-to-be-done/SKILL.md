---
name: ps-jobs-to-be-done
description: >-
  Identify customer Jobs-to-Be-Done and desired Product Outcomes using
  Productside job statement formats. Two steps - Step 1 enumerates job
  statements and personas (pre-discovery), Step 2 fills in product outcomes
  (often after empathy interviews). Use when you need to articulate what
  customers are trying to accomplish before jumping to solutions.
intent: >-
  Help a Product Manager capture the jobs their customers are trying to get done
  and the outcomes those customers want to achieve, using the Productside
  three-type job framework and the Direction + Metric + Context outcome format,
  so the team stays focused on customer progress instead of jumping to
  solutions. The skill supports two steps: enumerating jobs first, then filling
  in product outcomes after discovery evidence strengthens the PM's
  understanding.
type: component
blueprint_stage: Discover + Investigate
best_for:
  - "Capturing functional, emotional, and social jobs your customer is hiring your product to do"
  - "Defining desired product outcomes in Direction + Metric + Context format"
  - "Grounding discovery in what customers are trying to accomplish, not what you plan to build"
scenarios:
  - "I need to document the jobs our customers are hiring our product to do"
  - "Help me capture the functional, emotional, and social jobs for our target persona"
---


## Purpose

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

### Usage Notes

- **Two steps:** Step One (job statements + personas) can be done pre-discovery. Step Two (product outcomes) is strongest after empathy interviews provide evidence. Both steps can be completed in one session if evidence exists.
- **Review path:** if the PM brings a draft, the skill pressure-tests it first (verdict per job and outcome) before offering rewrites. This matches the Playbook's AI prompts.
- The template produces two artifacts: a Job Statement + Persona table and a Product Outcome & Context table.
- Job statements use three Productside formats: Functional, Emotional, Social.
- Product outcomes use the Direction + Metric + Context format. "Optimize," "enhance," and "improve" are never a direction.
- Upstream (B2B work-in-progress deck): Market Selection & Sizing defines the segment these jobs belong to.
- Downstream: ps-problem-identification uses jobs and outcomes from this skill as input. Product outcomes feed into ps-outcome-tree.

## Key Concepts

### Three Types of Jobs

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

### Product Outcomes Use a Specific Format

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

### What Makes a Good Product Outcome

The Playbook gives three tests:

- **Stable over time.** It doesn't change when technology changes. "Decrease the time to diagnose engine failure" holds whether the diagnosis is manual or AI-driven.
- **Linked to satisfaction.** It reflects what makes the customer satisfied or dissatisfied when trying to reach a goal.
- **Reveals unmet or overserved needs.** It shows where customers struggle, or where they have more capability than they need.

### Jobs, Outcomes, and Pains Are Linked

The playbook states this directly: *"Customers experience Pains when they are unable to achieve the desired Outcomes when executing a Job."*

This is load-bearing for the next play. Pains do not float free  -  they arise when a Job is hard to execute and the desired Outcome is out of reach. Writing precise, measurable Outcomes in this play is what makes Problem Identification tractable: the PM already knows what "success" looks like for each Job, so the Pains become specific gaps between where the customer is and where they want to be.

### Jobs, Outcomes, and Solutions Are Not the Same

- **Job** = what the customer is trying to accomplish
- **Outcome** = the result the customer wants when the job goes well
- **Solution** = what you build to help them (not part of this skill)

If a job statement mentions your product, a feature, or a tool, it is a solution masquerading as a job. Strip it back to the underlying customer progress.

Jobs define the scope of the work. Outcomes define the success criteria within that scope. The most common mistake is writing an outcome and labeling it a job, which mixes up what the customer is trying to accomplish with how they measure success. That undermines opportunity analysis and pulls the team toward feature-driven thinking.

**Jobs are intentionally stable.** Products, tools, and workflows change. Jobs persist. A job anchored to today's implementation ("export the weekly report from the legacy system") will expire with that system. A job anchored to progress ("share weekly checkpoint performance with leadership") will not.

### Product Outcomes vs. Business Outcomes

This play captures **product outcomes** - things the customer wants to achieve. Business outcomes (revenue, retention, market share) belong in the Outcome Tree (Template 03), not here.

The playbook explicitly says: "Remember product outcomes are the things your customer wants to achieve."

### Two Steps, One Artifact

The JTBD artifact has two halves: job statements (Table 1) and product outcomes (Table 2). These can be filled at the same time or at different times.

**Why separate them:** Job statements describe what the customer is trying to do. They can be drafted from the PM's current understanding, existing research, or market knowledge. Product outcomes describe the measurable results customers want. These are harder to get right without evidence.

The common pattern is:

1. **Step One:** Draft job statements and personas based on what the PM knows now. Use this to design empathy interview questions.
2. **Run empathy interviews** (ps-empathy-interviews) to validate and enrich understanding.
3. **Step Two:** Return to the JTBD artifact and fill in product outcomes informed by what customers actually said.

If the PM already has strong discovery evidence, both steps can be completed in one session. The skill supports either workflow.

### Pair with Persona Work

The JTBD template has a Persona column next to every job statement. That column forces you to name *who* has this job - not a generic segment, but a recognizable role.

If you have already built a proto-persona, use that persona name. If not, use a concrete role title that reflects the actual customer (not the PM building the product).

### How AI Supports This Play

The Playbook casts AI as a **sharp second reader** for jobs and outcomes. It checks each entry against the format, flags a job that is really an outcome or a solution, and pushes for the emotional and social jobs the PM skipped.

What AI cannot do is say what customers are trying to accomplish. Jobs come from real people in a real context. Any job or persona this skill drafts is a hypothesis to validate through Voice-of-the-Customer, never a finding.

- **Use it when:** the target segment is named and the PM has drafted jobs and outcomes, or wants a labeled starting draft to take into discovery.
- **Avoid it when:** the segment is vague or unnamed. Resolve the segment first (Step 1). Without it, any jobs produced are generic and validate nothing.
- **When reviewing a draft, return:** a verdict on each job (clean, or contaminated with an outcome or a solution), the missing emotional and social jobs *named* rather than written, and each outcome checked for direction, metric, and context. See [If the PM Brings a Draft](#if-the-pm-brings-a-draft).

### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

### Guided Mode

These three modes support different ways of learning and doing the work. Reuse the chosen mode and supplied context; do not restart intake on every turn.

1. **Offer the right way to work.** Guided coaches the user through the process one step at a time, so they complete the work and learn the method, including steps they missed or forgot. Expert accepts a context dump, draft, or artifacts from an experienced user and gets on with the requested result; guidance is available on any step. Discovery synthesizes missing context provisionally and quickly sketches the outcomes sought, using just enough guidance to simulate a useful walkthrough. Default to Guided when context is missing and no mode was chosen. With sufficient context, proceed directly unless the user chose Guided to learn. For Guided, state the output, approximate remaining question count, and where the user decides. For a simple Blueprint navigator request, help first without a mandatory intake.
2. **Use what is already supplied.** Treat the request, notes, attachments, prior artifacts, and earlier decisions as context already given. Do not ask for it again. In Expert mode, briefly show Known / Assumed / Missing / Conflicting with source credit, distinguishing reported claims from verified evidence. If context is sufficient, produce the requested result without a questionnaire or extra confirmation. Ask only about gaps that would materially change it. If the user asks for help on a step, coach that step and then resume Expert mode without restarting.
3. **Coach, one question at a time.** In Guided mode, explain the current step and why it matters, then use an honest progress label such as Context Q2/5, one bolded question, three context-relevant numbered best-guess recommendations, option 4 Other (specify), and an input hint allowing multiple selections or free text. Explain the reasoning behind recommendations so the user learns; they are possibilities to consider, accept, adjust, or reject, not presumed facts or the user's answer. Adapt them to the Play, domain, and prior answers; use research only where appropriate and available. For facts only the user can supply, ask openly without suggested answers and explain why.
4. **Synthesize just enough in Discovery.** Do not demand a complete brief. Use the available context to synthesize what is missing, label inferred details inline, and quickly provide a provisional sketch or simulated skill walkthrough. Ask one question only when it would materially improve that sketch; otherwise proceed. Where a Play needs real research, a team session, or an unavailable draft, illustrate the method with clearly labeled synthesized assumptions rather than claim the real activity occurred. Keep simulated outcomes separate from actual findings, commitments, and decisions. Context-relevant suggestions in every mode remain open to correction.
5. **Handle interruptions and switches.** Answer a meta question, restate progress and any pending question, then wait. Honor corrections and switch modes immediately. Accept context dump as Expert and spitball or best guess as Discovery, not extra modes. Stop when asked; on resume, recap captured context, open gaps, and the next step. A request for guidance on one step in Expert mode is not a request to restart the whole process in Guided mode.
6. **Finish visibly in every mode.** Summarize what was supplied, what was synthesized or inferred, what remains unknown or disputed, and whether the work is ready for a decision. In Guided mode, confirm the captured context before generating an artifact when the Play calls for one. Expert delivers the requested work using sufficient supplied context; Discovery delivers a fast provisional sketch with just enough walkthrough to make it useful. If anything was inferred, end with Assumptions to Validate ranked by decision impact.
7. **Hand the decision back.** When there is a real choice, show a numbered decision ladder: the option the evidence favors first, labeled (Recommended), then distinct alternatives with a one-sentence tradeoff, then Other. Allow combinations where sensible. If evidence does not favor an option, say so. Do not turn a factual question into invented choices. The user decides.

Guided teaches while completing the work. Expert moves experienced users from context to result and offers coaching on demand. Discovery fills gaps provisionally to sketch and simulate, not to claim customer research, team agreement, test results, or approval. These are interaction modes, distinct from the Blueprint phases; real evidence and decisions remain with people.

## Application

Use [Template](#template) for the full scaffold.


### Required Output Convention

Default to a **clean, paste-ready two-table artifact**.

That means:

- fill both tables (Job Statement + Persona on the left, Product Outcome & Context on the right)
- produce exactly 10 job rows covering all three job types unless the user asks for a different count
- produce at least 10 product outcomes (one or more per job)
- keep job statements short enough for the template table cells (~8-10 words)
- keep product outcomes short enough for the template table cells (~12-14 words)
- explanation belongs below the artifact, not inside the table cells

The artifact comes first. Commentary is secondary.

### If the PM Brings a Draft

When the user arrives with drafted job statements or outcomes, review the draft instead of drafting from scratch. This is the path the Playbook's AI prompts take (the critique guidance in this Play, the critique guidance in this Play).

1. **Confirm the segment.** If it is unnamed or vague, resolve it first (Step 1). Do not review jobs for a segment no one can name.
2. **Review each job.** Give a verdict per row: clean, wrong format, contaminated with an outcome, or contaminated with a solution. Quote the words that cause the problem.
3. **Name the gaps.** Name the missing job types (usually emotional and social) and the personas with no rows. Do not write them unless the user asks.
4. **Review each outcome.** Check direction (never optimize, enhance, or improve), metric (quantitative or qualitative), and context (no solution). Apply the three good-outcome tests.
5. **Offer rewrites last.** Propose fixes as options to accept, adapt, or reject, then fill the template with what the user commits.

Return the review as a compact table (entry, verdict, why, suggested fix) before any rewritten artifact.

### Step 1: Confirm the Product and Target Market Segment

Before writing anything, answer:

- what product or service are we talking about?
- who is the target market segment?
- who are the personas within that segment? (user, buyer, influencer)

If you cannot answer those clearly, stop and resolve the target first.

**Guard against tech-role bias.** The jobs belong to the customer - the person who uses or buys the product in the field. An IoT platform's customer jobs belong to a fleet manager or logistics director, not a solutions architect. A clinical data platform's customer jobs belong to a clinical operations lead, not a data engineer. Before writing job statements, confirm: does this person write code, design systems, or architect solutions as their primary job? If no, the jobs should not read like a technologist's workday.

### Step 2: Gather Evidence Before Writing

Once you know the target segment and role, offer the user two things before drafting:

1. **Web research** - offer to run a quick search for the target role in the target industry. Look for how practitioners describe their own work, frustrations, and goals. Job postings, industry forums, trade press, and professional community discussions are good sources. The goal is to capture real customer language, not marketing language about them.

2. **User-supplied artifacts** - ask whether the user has materials to share: interview notes, support tickets, call logs, existing persona or discovery work, competitive intel, or anything else that would ground the jobs and outcomes in evidence.

Either, both, or neither is fine - the user decides. But always offer before drafting.

### Step 3: Identify the Personas Involved

Before writing job statements, name the personas who will appear in the Persona column.

For most products, there are 2-4 distinct personas involved:

- the primary user (the person who does the job day-to-day)
- the buyer (the person who approves or funds the product)
- influencers or secondary users

Each job row names the persona who has that specific job. Different personas can appear in different rows. Use concrete role titles, not generic labels.

If a proto-persona already exists from the ps-proto-persona skill, reuse that persona name.

**Distribute rows across roles.** Do not repeat the same persona in every row. The point of the Persona column is to show that different people have different jobs. If the product serves a Regional Operations Planner, a Dock Supervisor, and a VP of Distribution, all three should appear in the table - not just the primary user 10 times.

### Step 4: Write Functional Job Statements

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

### Step 5: Write Emotional Job Statements

Emotional jobs capture how the customer wants to feel.

Format: `Feel [Emotion] when [Circumstance]`

These are not filler. Emotional jobs explain:

- why customers resist or adopt new tools
- what "good enough" means to them
- what turns a satisfied user into an advocate

Weak: "Feel happy using the product"
Stronger: "Feel confident when presenting compliance data to auditors"

Produce at least 2 emotional jobs.

### Step 6: Write Social Job Statements

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

### Step One / Step Two Boundary

Steps 1-6 above complete **Step One** of this skill: job statements and personas. At this point, the PM has a choice:

1. **Continue to Step Two now** if they already have enough evidence to write product outcomes confidently (prior research, customer data, domain expertise).
2. **Pause and run empathy interviews first** (ps-empathy-interviews) to validate the jobs and gather evidence about what outcomes customers actually care about. Then return to Step Two.

If the PM chooses to pause, offer to help design empathy interview questions based on the job statements just captured. The jobs from Step One make excellent interview prompts.

---

### Step 7: Identify Product Outcomes for Each Job (Step Two)

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

### Step 8: Separate Outcomes from Solutions

Before finalizing, scan every outcome and ask: is this something the *customer* wants to achieve, or is it something *we* want to build?

Solution indicators to strip out:

- mentions of your product name
- feature descriptions ("a dashboard that...", "an integration with...")
- implementation details ("automated alerts for...", "API-driven...")

Rewrite any solution-contaminated outcomes as customer-centered results.

### Step 9: Keep the Artifact Compact

The canonical template uses table cells. Job statements should be ~8-10 words. Product outcomes should be ~12-14 words. Persona entries should be 2-3 words (a role title).

If the output requires summarizing before it can be pasted into the playbook, it is too long.

Do not let good prose outrank usable template completion.

### Step 10: Add Optional Trailing Notes

If helpful, add a brief trailing section such as:

- `Jobs that need more evidence`
- `Outcomes that feel assumed`
- `Gaps in job type coverage`

Keep it separate from the paste-ready artifact.

Do not add a notes section at all unless:

- the user asks for it, or
- the artifact is already fully complete

### Step 11: Offer Next Steps

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

## Template

### When to Use This

Use this template during **Discover + Investigate** to capture what your target customers are trying to accomplish and what success looks like for them. Pair this with persona work - the playbook says to consider Jobs-to-Be-Done and Persona at the same time.

This template supports **two steps** that can be completed together or at different times:

- **Step One:** Fill the Job Statements & Personas table (Section 1). This can be done pre-discovery.
- **Step Two:** Fill the Product Outcomes table (Section 2). This is often done after empathy interviews provide evidence about what outcomes customers actually care about.

### Template

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

### Usage Guidance

#### Filling the Template

**Step One (can be done pre-discovery):**

1. Start with **Product Context** to anchor who this is for.
2. Fill **Job Statements** starting with functional jobs, then adding emotional and social jobs. Use the Productside sentence formats - do not improvise different structures.

**Step Two (strongest after empathy interviews):**

3. Fill **Product Outcomes** for each job. One job can have multiple outcomes. Use Direction + Metric + Context. If you completed empathy interviews between steps, let customer language inform the outcome statements.
4. The **Evidence Notes** section is optional and trailing. Do not let it displace or delay the main artifact.

#### How Many Rows

The canonical template has 12 rows. Default to 10 filled rows:

- at least 5-6 functional jobs
- at least 2 emotional jobs
- at least 2 social jobs
- at least 10 product outcomes (one or more per job)
- distribute rows across multiple personas, not one repeated role

Add more rows if the evidence supports them. Do not pad with vague jobs to fill the template.

#### What Goes in the Persona Column

Use a concrete role title that reflects the actual customer - the person who has this job in the field. If you built a proto-persona already, reuse that persona name.

Do not use:
- "User" (too vague)
- "Stakeholder" (too abstract)
- The Product Manager's own title (unless the product truly serves PMs)

#### Connecting to Other Skills

- **Upstream:** Proto-persona (the persona names in this template should match)
- **Downstream:** Problem Identification uses the jobs, pains, and outcomes from this artifact
- **Parallel:** The Outcome Tree (Template 03) uses product outcomes from this skill as input

#### Capacity Reference

See [Template and capacity guidance](#template) for the exact word and character budgets per field.

| Field | Word Budget | Guidance |
|-------|-------------|----------|
| Job Statement | ~8-10 | Compact action phrase; use Productside format |
| Persona | ~2-3 | Role title only |
| Product Outcome | ~12-14 | Direction + Metric + Context; one sentence max |

## Examples

Illustrative and fictional, not customer evidence.

- **Strong:** Warehouse planner: Functional, "Coordinate daily labor assignments"; Emotional, "Feel confident when reallocating crews"; Social, "Seen as dependable by site supervisors." Outcome: "Reduce reassignment delays during shift changes."
- **Weak:** "Improve efficiency" has no named metric or clear direction.
- **Drift to avoid:** Jobs as solutions: "Use the scheduling dashboard" describes a product interaction. State what the planner is trying to accomplish.


## Common Pitfalls

- **Writing Only Functional Jobs:** After writing functional jobs, explicitly ask: how does this person want to feel while doing this work? How do they want to be seen by their peers and leadership? Write at least 1-2 emotional and 1-2 social jobs.

- **Confusing Jobs with Solutions:** Strip out any mention of products, features, tools, or implementation. Rewrite as the underlying customer progress: "Track regional performance against quarterly targets."

- **Making Outcomes Vague:** Use the Direction + Metric + Context format, and never use "optimize," "enhance," or "improve" as the direction. "Improve efficiency" becomes "Reduce time spent reconciling data across multiple HR systems." Adding a specific threshold ("by 40% during month-end close") makes it stronger when you have the evidence  -  but even without a number, a named metric beats a vague direction.

- **Defaulting to a Tech Role:** Ask what the customer actually does day-to-day. Most products serve people whose primary job is not writing code. A fleet manager's jobs involve route optimization, driver coordination, and compliance reporting - not API integration or system architecture.

- **Writing Internal Team Tasks as Customer Jobs:** Ask: who experiences the product's value in the field? That person's jobs go in the template. The PM's jobs belong in process docs, not in customer discovery artifacts.

- **Restating Jobs as Outcomes:** Outcomes should describe a measurable result: "Reduce time to complete payroll data entry." "Reduce errors in new employee form submissions." Where the PM has evidence for a specific threshold, adding it strengthens the outcome  -  but a named metric without a number beats a vague direction every time. The outcome is what success looks like *for the customer* when the job goes well.

- **Exceeding Template Capacity:** Job statements: ~8-10 words. Outcomes: ~12-14 words. Persona entries: 2-3 words. Write for the template cell, not for the model's appetite for prose.

- **Underfilling the Template:** Default to 10 job rows covering all three types (Functional, Emotional, Social) with at least 10 outcomes. Distribute rows across multiple personas - do not repeat one role in every row.

- **Presenting AI-Drafted Jobs as Findings:** Label every drafted job and outcome as a hypothesis, and end with Assumptions to Validate. Route the hypotheses into empathy interviews (ps-empathy-interviews) before treating any of them as evidence.

## References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-jobs-to-be-done) for supporting source material and expanded examples.
