# Jobs-to-Be-Done & Outcomes

## When to Use This

Use this template during **Discover + Investigate** to capture what your target customers are trying to accomplish and what success looks like for them. Pair this with persona work - the playbook says to consider Jobs-to-Be-Done and Persona at the same time.

This template supports **two steps** that can be completed together or at different times:

- **Step One:** Fill the Job Statements & Personas table (Section 1). This can be done pre-discovery.
- **Step Two:** Fill the Product Outcomes table (Section 2). This is often done after empathy interviews provide evidence about what outcomes customers actually care about.

## Template

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

## Usage Guidance

### Filling the Template

**Step One (can be done pre-discovery):**

1. Start with **Product Context** to anchor who this is for.
2. Fill **Job Statements** starting with functional jobs, then adding emotional and social jobs. Use the Productside sentence formats - do not improvise different structures.

**Step Two (strongest after empathy interviews):**

3. Fill **Product Outcomes** for each job. One job can have multiple outcomes. Use Direction + Metric + Context. If you completed empathy interviews between steps, let customer language inform the outcome statements.
4. The **Evidence Notes** section is optional and trailing. Do not let it displace or delay the main artifact.

### How Many Rows

The canonical template has 12 rows. Default to 10 filled rows:

- at least 5-6 functional jobs
- at least 2 emotional jobs
- at least 2 social jobs
- at least 10 product outcomes (one or more per job)
- distribute rows across multiple personas, not one repeated role

Add more rows if the evidence supports them. Do not pad with vague jobs to fill the template.

### What Goes in the Persona Column

Use a concrete role title that reflects the actual customer - the person who has this job in the field. If you built a proto-persona already, reuse that persona name.

Do not use:
- "User" (too vague)
- "Stakeholder" (too abstract)
- The Product Manager's own title (unless the product truly serves PMs)

### Connecting to Other Skills

- **Upstream:** Proto-persona (the persona names in this template should match)
- **Downstream:** Problem Identification uses the jobs, pains, and outcomes from this artifact
- **Parallel:** The Outcome Tree (Template 03) uses product outcomes from this skill as input

### Capacity Reference

See [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml) for the exact word and character budgets per field.

| Field | Word Budget | Guidance |
|-------|-------------|----------|
| Job Statement | ~8-10 | Compact action phrase; use Productside format |
| Persona | ~2-3 | Role title only |
| Product Outcome | ~12-14 | Direction + Metric + Context; one sentence max |
