# Affinity Mapping

## When to Use This

Use this template during **Discover + Investigate** after you have collected qualitative observations from customer research. You are ready to map when you have raw notes from empathy interviews, customer feedback, survey responses, or other customer-side sources and need to organize them into patterns.

Upstream work that feeds this template: ps-empathy-interviews (primary), ps-jobs-to-be-done, ps-proto-persona.

Downstream: the key insights from this map feed ps-problem-identification.

## Template

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

## Usage Guidance

### Filling the Template

1. Start with **Research Context** to anchor what data went into this map.
2. Fill **Theme Clusters** one at a time. Label the theme only after you have seen what observations belong together - resist naming the theme before clustering.
3. Write **Key Insights** after all clusters are labeled. Do not write insights cluster by cluster as you go; seeing all the clusters together often changes what the insights should say.
4. Run the **Completeness Check** before treating the map as done.
5. The **Notes** section is optional. Use it if there are outlier observations or re-grouping ideas worth capturing.

### If You Have No Observation Data Yet

Affinity mapping requires input data. If no customer-side observations are available:

- Offer to help the user run ps-empathy-interviews first.
- If the user wants a scaffold to use in an upcoming workshop, fill the theme and insight sections with labeled placeholder sections and explain that they should be completed collaboratively with the team after data is collected.
- Do not generate observations from the agent's training data and present them as customer findings.

### What Goes Where

| Section | Contains | Does NOT Contain |
|---------|----------|------------------|
| Theme Clusters | Direct customer observations grouped by pattern | Opinions, solutions, feature requests, team preferences |
| Theme Labels | A named pattern describing what is happening | A broad topic area that could hold any observation |
| Key Insights | Inferences about what the patterns mean for the product | Restatements of theme labels, feature recommendations |
| Notes | Outliers, open questions, re-grouping ideas | The main deliverable content |

### Connecting to Other Skills

- **Upstream:** ps-empathy-interviews provides the raw observation notes. ps-jobs-to-be-done and ps-proto-persona provide additional customer context that can inform how observations are grouped.
- **Downstream:** The key insights from this map feed ps-problem-identification. The strongest insight often becomes the focal point for the candidate problem that gets developed in ps-framing-the-problem.

### Capacity Reference

| Field | Guidance |
|-------|----------|
| Theme label | 6-10 words. Names the pattern, not the topic. |
| Observation bullet | 8-12 words. Direct, factual, customer-side. |
| Key insight title | 5-8 words. Plain language. |
| Key insight paragraph | 50-80 words. Answers "so what?" |
