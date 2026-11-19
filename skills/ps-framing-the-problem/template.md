# Framing the Problem

## When to Use This

Use this template during **Discover + Investigate** when you have enough discovery evidence to frame a validated problem and craft a problem statement. This is a **Key Decision Point** - the output goes to leadership and product governance to justify moving into solution definition.

Upstream work that feeds this template: proto-persona, jobs-to-be-done, empathy interviews, problem identification, affinity mapping.

## Template

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

## Usage Guidance

### Filling the Template

1. Start with **Product Context** to anchor who this is for and whose problem it is.
2. Fill the **five stems in order** - do not skip or reorder. Each stem builds on the previous one.
3. Fill **Context and Constraints** separately - these are external conditions, not part of the problem frame itself.
4. Write the **Final Problem Statement** last, synthesizing all five stems into one cohesive narrative.
5. The **Evidence Notes** section is optional and trailing. Do not let it displace or delay the main artifact.

### The Stem Sequence Is Fixed

The five stems must appear in this exact order:

1. I am
2. Trying to
3. But
4. Because
5. Which makes me feel

Do not merge stems, skip stems, or reorder them. Each has a distinct function in building the problem frame.

### What Goes Where

| Section | Contains | Does NOT Contain |
|---------|----------|------------------|
| I am | Persona role, situation, 3-4 key experience points | Product features, team perspective |
| Trying to | The desired outcome | Task lists, feature requests |
| But | Concrete, observable barriers | Constraints (those go in Context) |
| Because | Root cause of the barrier | Surface-level restatements |
| Which makes me feel | Specific customer emotions | "Bad" or "frustrated" alone |
| Context and Constraints | Industry, regulatory, budget, technology, geographic conditions | Barriers (those go in But) |
| Final Problem Statement | Synthesis of all five stems | New information not in the stems |

### Connecting to Other Skills

- **Upstream:** Proto-persona provides the "I am." JTBD provides the "Trying to." Problem Identification provides barriers, root causes, and candidate problems. Empathy interviews provide emotional evidence.
- **Downstream:** The validated problem statement justifies moving into Discover + Define - solution hypothesis, positioning, exploring the solution space.

### Capacity Reference

See [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml) for the exact word and character budgets per field.

| Field | Word Budget | Guidance |
|-------|-------------|----------|
| I am | ~30-40 | Role + situation + 3-4 key experience points |
| Trying to | ~15-20 | One clear outcome statement |
| But | ~20-25 | Concrete barriers, not vague "challenges" |
| Because | ~20-25 | Root cause, not barrier restatement |
| Which makes me feel | ~15-20 | 2-3 specific emotions with context |
| Context and Constraints | ~30-40 | External conditions bounding the solution space |
| Final Problem Statement | ~40-50 | Cohesive synthesis of all five stems |
