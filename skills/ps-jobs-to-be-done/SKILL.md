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

The metric names what is being measured. **Default to including a quantified target** — a percentage, ratio, range, or exact number. When in doubt, put something in. The PM can refine it; a vague direction cannot be refined.

Preference order for the quantified value: **percentage > ratio > range > exact number**. For time-based outcomes, use a range ("by Q3", "by H2", "by EOY") rather than an exact date — specific dates stale out quickly.

Examples:
- "Reduce payroll data entry errors by 30% during quarterly onboarding cycles" (percentage)
- "Reduce HR query response time from 2-day to same-day for tier-1 requests" (ratio)
- "Add 3 new regional customers through HR partner channel by Q4" (exact number + range)
- "Increase HR self-service revenue to $1.2M by H2" (dollar figure + range)

Every outcome must have a direction. Direction + named metric ("Reduce time to complete payroll data entry") is the minimum viable form — acceptable when the PM has no basis for a threshold yet, but always the starting point to improve from. Add the quantified threshold ("by 30%", "from 2-day to same-day") when any evidence supports it.

Avoid: "improve efficiency," "faster onboarding," "better HR tools" — these are not metrics, just sentiment. **"Optimize," "enhance," and "improve" are never a direction.** They don't say which way the metric moves. Use increase/decrease, faster/slower, expand/contract, reduce, or eliminate.

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

This is load-bearing for the next play. Pains do not float free — they arise when a Job is hard to execute and the desired Outcome is out of reach. Writing precise, measurable Outcomes in this play is what makes Problem Identification tractable: the PM already knows what "success" looks like for each Job, so the Pains become specific gaps between where the customer is and where they want to be.

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

The Productside Playbook sets one rule for every AI-assisted Play: **the Product Manager does the thinking, and AI pressure-tests it.** In this skill, you are the AI. Hold yourself to these rules:

1. **Pressure-test before you produce.** When the user brings a draft, critique it against the Play's formats and criteria first. Point at the specific words that fail and ask the user to fix them. Offer rewrites only after the critique, as options to accept, adapt, or reject.
2. **Never stand in for the customer.** Do not present jobs, quotes, needs, or pains you generated as research, and do not answer as the persona as if your answers were evidence. Anything you draft about customers is a hypothesis, labeled as one, to validate with real people. Role-play is allowed only as rehearsal where the Play calls for it, labeled as practice, and nothing from it goes into findings.
3. **Never stand in for the team's judgment.** Do not put unsourced figures into the artifact, and do not make calls the team should own. A number without a source is a blank to fill, so mark it that way.
4. **Work the five habits.** *Context:* ask for the persona, market, outcome, and constraints when they are missing. *Guide:* offer competing views and welcome pushback. *Enforce:* work inside the Play's template, not around it. *Outcome:* tie the work to the decision it supports. *Iterate:* go step by step rather than one-shot.
5. **Keep best guess honest.** Best guess mode is allowed. When you use it, label every inferred detail inline and end with **Assumptions to Validate**. A best guess is a starting point to test, never a finding.

For people working in a chat tool without this skill, the Play's copy-paste prompts are in [prompts/](prompts/README.md).

### Guided Mode

When a user asks to be walked through this skill, signals unfamiliarity, or invokes it without enough context, run in guided mode. **Do NOT batch multiple questions into one turn. Do NOT list everything you need up front. One question per turn, every turn.**

1. **Open with a heads-up.** State what the skill produces, the estimated number of questions, and where you will stop for the user's decision. Offer three entry paths:
   - (1) **Guided** - one question at a time with recommendations
   - (2) **Context dump** - paste what you know and I will ask only what is missing
   - (3) **Best guess** - I will infer what I can and label every assumption

   Then ask the first question immediately (do not wait for the user to pick a mode - Guided is the default).

2. **Start from what is already supplied.** Treat text in the request, pasted notes, attached files, upstream Play artifacts, and decisions made earlier in the conversation as answers already given. Do not ask for them again. Begin at the first real gap, and keep the progress label honest about what remains.

3. **One question per turn.** Every turn follows this exact format:

   > `Context Q2/5`
   >
   > **Who are the primary users of this product?**
   >
   > Some options to consider:
   > 1. Clinical data managers who run queries against study databases
   > 2. Research scientists who need self-service access to trial data
   > 3. Biostatisticians who build analysis-ready datasets
   > 4. Other (describe your users)
   >
   > Pick one or more (e.g. `1`, `1,3`, `1 and 3`), or describe in your own words.

   The progress label (e.g. `Context Q2/5`) is mandatory on every turn. Recommendations must always be numbered `1.`, `2.`, `3.`, `4. Other` - never presented as bullet points or unnumbered prose. The three recommendations must be specific to the skill, the industry, and the context gathered so far - never generic placeholders. If you lack domain context for good recommendations, do a web search first to ground your options in real roles, real products, or real workflows. Explain why a question matters when that is not obvious, and ask a follow-up only when the answer could change the artifact or the decision.

   **Exception: evidence only the user has.** When a question asks for something only the user can know (a root cause, what customers said or did, what the user observed, a number they must set), ask it as an open question with no numbered options, and say why there are none. Options there would put guesses in the user's mouth.

4. **Recommendations get smarter each turn.** Each answer becomes context for the next question's recommendations. By the mid-point, options should reflect the specific product, customer, and situation the user has described - not generic suggestions. Early questions can use industry-typical examples; later questions must incorporate what the user has already told you.

5. **In context dump mode, show what you extracted first.** Before asking anything, give a short **Known / Assumed / Missing / Conflicting** summary of what the user supplied. Credit where each item came from, and keep what a source reported separate from what has been verified. Then ask only the questions that would most change the artifact.

6. **Interruption-safe.** Handle any of these mid-session:
   - **Meta questions** ("how many left?", "what does this term mean?"): answer directly, restate progress, restate the pending question, then wait.
   - **Mode switch** ("just take your best guess", "here is everything I know"): switch to the requested mode immediately. For best guess, infer remaining answers from context gathered so far, generate the artifact, and end with an explicit **Assumptions to Validate** list, ranked by how much each could change the decision. For context dump, parse what was provided and ask only about gaps.
   - **Correction** ("actually, go back to Q2"): revisit that question with the original recommendations updated for current context.
   - **Pause or stop**: stop immediately. On resume, summarize what was captured, what is still open, and the next question.

7. **Finish with a summary, then hand back the decision.** After the context is gathered, recap in a few short bullets: what was supplied, what was inferred, what remains unknown or disputed, and whether the work is ready for a decision. Confirm before generating the artifact. If best guess mode was used at any point, end with an explicit **Assumptions to Validate** list. When the user faces a choice (which option, which next Play, whether to proceed), present a numbered ladder: the option the evidence favors first, labeled `(Recommended)`, then two or three genuinely distinct alternatives, each with its tradeoff in one sentence, then `Other`. Allow combining options where it makes sense. The user decides.

## Application

Use [template.md](template.md) for the full scaffold.

See the original three-page playbook source in [assets/ps_jobs_to_be_done_playbook_pages.pdf](assets/ps_jobs_to_be_done_playbook_pages.pdf).

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

When the user arrives with drafted job statements or outcomes, review the draft instead of drafting from scratch. This is the path the Playbook's AI prompts take ([prompts/01](prompts/01-check-job-statements.md), [prompts/02](prompts/02-check-product-outcomes.md)).

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

- **Direction**: Increase, Decrease, Expand, Contract, Reduce, Eliminate — always required, never optional
- **Metric**: what is being measured (time, errors, satisfaction, revenue, customer count) — default to including a quantified target: percentage, ratio, range, or exact number ($3.5M, 3 new regional customers). Use a time range ("by Q3", "by H2") rather than an exact date. When in doubt, put a number in — the PM can refine it.
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

## Examples

See [examples/sample.md](examples/sample.md).

The example set includes:

- a stronger Productside-style JTBD artifact with all three job types
- a weak, generic version
- a drift-bug example showing jobs written as solutions
- commentary on why the weak versions fail

## Common Pitfalls

### Pitfall 1: Writing Only Functional Jobs

**Symptom:** Every job is a task ("process orders," "generate reports," "track shipments") with no emotional or social dimension.

**Consequence:** The team builds a tool that does the job but nobody wants to use because it ignores how people feel about their work and how they want to be perceived.

**Fix:** After writing functional jobs, explicitly ask: how does this person want to feel while doing this work? How do they want to be seen by their peers and leadership? Write at least 1-2 emotional and 1-2 social jobs.

### Pitfall 2: Confusing Jobs with Solutions

**Symptom:** "Use our analytics dashboard to track KPIs" or "Integrate data from multiple systems."

**Consequence:** The team starts from a solution and works backward, skipping the customer need entirely.

**Fix:** Strip out any mention of products, features, tools, or implementation. Rewrite as the underlying customer progress: "Track regional performance against quarterly targets."

### Pitfall 3: Making Outcomes Vague

**Symptom:** "Improve efficiency," "Better visibility," "Streamline processes."

**Consequence:** The outcome cannot be measured, so nobody can tell if the product is working.

**Fix:** Use the Direction + Metric + Context format, and never use "optimize," "enhance," or "improve" as the direction. "Improve efficiency" becomes "Reduce time spent reconciling data across multiple HR systems." Adding a specific threshold ("by 40% during month-end close") makes it stronger when you have the evidence — but even without a number, a named metric beats a vague direction.

### Pitfall 4: Defaulting to a Tech Role

**Symptom:** The user asks about an IoT platform PM's customers and gets job statements for a solutions architect or platform engineer.

**Consequence:** The JTBD artifact reflects LLM training bias, not the real customer population.

**Fix:** Ask what the customer actually does day-to-day. Most products serve people whose primary job is not writing code. A fleet manager's jobs involve route optimization, driver coordination, and compliance reporting - not API integration or system architecture.

### Pitfall 5: Writing Internal Team Tasks as Customer Jobs

**Symptom:** "Prioritize the product backlog," "Align stakeholders on the roadmap," "Define acceptance criteria."

**Consequence:** The JTBD artifact describes the Product Manager's own work, not the customer's.

**Fix:** Ask: who experiences the product's value in the field? That person's jobs go in the template. The PM's jobs belong in process docs, not in customer discovery artifacts.

### Pitfall 6: Restating Jobs as Outcomes

**Symptom:** Job: "Onboard new employees." Outcome: "Onboarding is faster."

**Consequence:** The outcome adds no new information. The team cannot tell what "better" means.

**Fix:** Outcomes should describe a measurable result: "Reduce time to complete payroll data entry." "Reduce errors in new employee form submissions." Where the PM has evidence for a specific threshold, adding it strengthens the outcome — but a named metric without a number beats a vague direction every time. The outcome is what success looks like *for the customer* when the job goes well.

### Pitfall 7: Exceeding Template Capacity

**Symptom:** Job statements become full sentences with context clauses. Outcomes turn into multi-sentence explanations.

**Consequence:** The human cannot paste the output into the playbook without rewriting it.

**Fix:** Job statements: ~8-10 words. Outcomes: ~12-14 words. Persona entries: 2-3 words. Write for the template cell, not for the model's appetite for prose.

### Pitfall 8: Underfilling the Template

**Symptom:** The model produces 3-5 jobs and 3-5 outcomes because it thinks the synthesis is cleaner.

**Consequence:** The human has blank rows to fill, missing job types, and incomplete role coverage.

**Fix:** Default to 10 job rows covering all three types (Functional, Emotional, Social) with at least 10 outcomes. Distribute rows across multiple personas - do not repeat one role in every row.

### Pitfall 9: Presenting AI-Drafted Jobs as Findings

**Symptom:** A best-guess JTBD table, plausible and well formatted, goes into a stakeholder deck or straight into Problem Identification as if customers had said it. Nothing marks which jobs came from research and which came from the model.

**Consequence:** The team validates nothing and builds on a stereotype. The Playbook names this the first AI trap: AI standing in for the customer.

**Fix:** Label every drafted job and outcome as a hypothesis, and end with Assumptions to Validate. Route the hypotheses into empathy interviews (ps-empathy-interviews) before treating any of them as evidence.

## References

### Skill Files

- [template.md](template.md) - working scaffold
- [prompts/](prompts/README.md) - copy-paste prompts for chat-based AI tools (2, in order)
- [examples/sample.md](examples/sample.md) - strong, weak, and drift-bug examples

### Related Project Docs

- [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)
- [framework-glossary.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/framework-glossary.md)
- [skill-authoring-workflow.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/skill-authoring-workflow.md)
- [template_conversion_rules.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/template_conversion_rules.md)
- [template_conversion_usage.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/template_conversion_usage.md)

### Related Skills

- [ps-proto-persona](../ps-proto-persona/SKILL.md) - build a persona before or alongside this skill
- [ps-problem-identification](../ps-problem-identification/SKILL.md) - uses jobs from this skill as input

### Source Material

- [Baseline Playbook version](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml). Full source PDF supplied separately.
- [assets/ps_jobs_to_be_done_playbook_pages.pdf](assets/ps_jobs_to_be_done_playbook_pages.pdf)
- Productside Playbook companion document (supplied separately)
- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 19-24: Template 05 of 24 there, with the AI overview on slide 21 and prompts on slides 22-23. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).
