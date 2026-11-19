---
name: psk-affinity-mapping
description: >-
  Synthesize qualitative research observations into labeled theme clusters and
  key insights in Productside format. Use when you have raw interview findings,
  survey data, or customer feedback to organize into patterns.
intent: >-
  Help a Product Manager turn raw qualitative observations into a structured set
  of themes and key insights that can inform problem identification and
  prioritization, without flattening distinct findings into a single
  undifferentiated list.
type: process
blueprint_stage: Discover + Investigate
best_for:
  - "Synthesizing raw qualitative observations into labeled theme clusters"
  - "Turning interview and research notes into named patterns and key insights"
  - "Bridging discovery evidence to downstream problem identification"
scenarios:
  - "I have raw notes from five customer interviews and need to find the patterns"
  - "Help me organize our research observations into theme clusters the team can discuss"
---


## Purpose

Create a **Productside-style Affinity Map** from qualitative customer research.

This skill helps a Product Manager synthesize raw observations from empathy interviews, customer feedback, or other research into a working artifact with:

- labeled theme clusters grouping similar observations
- named patterns that reveal what the data is actually saying
- key insights that translate patterns into product-relevant implications

The point is not to produce a summary of what customers said. The point is to surface what the observations collectively reveal.

### Usage Notes

- **Coach by default.** With real notes, the skill walks the PM through the Playbook's five-step method (orient, split, immerse, group, name) and the PM does the grouping, labeling, and insights.
- **Draft on request.** If the PM asks the skill to group the notes, it produces a map labeled "AI draft grouping: for the team to challenge."
- **No real notes, no map.** The skill will not map invented observations. It routes to psk-empathy-interviews instead.

## Key Concepts

### This Skill Bridges Interviews and Problem Identification

Affinity mapping is the synthesis step. Raw observations from empathy interviews are too granular to act on directly. Affinity mapping groups them into patterns. Those patterns become the input to psk-problem-identification.

Without this step, teams often jump from "we talked to customers" to "here is our feature roadmap" without ever making the intermediate inference.

### Observations and Insights Are Different Things

- **Observations** are what you heard, saw, or documented during research. They are factual and specific.
- **Themes** are labels for clusters of similar observations. They name the pattern.
- **Key insights** are inferences about what those patterns mean for product decisions.

A key insight is not a summary of a theme. It answers: "Given this pattern, what does that mean for what we should build or prioritize?"

### The Grouping Is Not Permanent

The playbook tip: "Group your data in multiple ways to reveal new insights. There is no wrong way to do it."

Affinity mapping is iterative. If a different grouping reveals something the first pass missed, that is a feature, not a mistake. The artifact should invite re-examination, not lock conclusions.

### Minimum Three Applies to Both Themes and Insights

Fewer than three themes usually signals that the grouping is too coarse. Fewer than three key insights usually signals that the synthesis stopped at clustering and never made the inferential leap.

### The Sense-Making Is the Point

The value of affinity mapping lives in the team's debate over where each note belongs. Whoever does the grouping does the thinking. That is why the Playbook keeps the clustering, the theme labels, and the insights with the PM and their team, and casts AI as a guide through the method.

### The Agent's Role: Coach by Default, Draft on Request

- **Real notes, default:** coach the PM through the method (Step 3). The PM groups, labels, and writes the insights. You teach, question, and illustrate. The line, from the Playbook: you may point at two notes and ask "are these the same behavior?" You may not say "these two go together under this theme."
- **Real notes, and the PM asks you to group them (or chooses Discovery):** produce a draft map, labeled **AI draft grouping: for the team to challenge**. Show why each cluster holds together, and end with the groupings you were least sure of. The team still decides.
- **Fragments only:** coach or draft as above, and label every theme provisional.
- **No real notes:** stop. Affinity mapping on invented data teaches nothing and proves nothing. Offer to help prepare interviews (psk-empathy-interviews), or to set up the template for a workshop once notes exist. Never invent observations or quotes to map. Labeling the work "hypotheses" doesn't change this: produce no themes, clusters, or map layout at all. If the PM needs something for a meeting, offer a short plain list of assumptions to test in interviews, clearly labeled, and point to psk-empathy-interviews.

### What Binds a Cluster

Test every grouping against the same questions:

- Do these notes share the same **behavior or need**, or just the same **topic**?
- Is this a **real pattern**, or a coincidence of wording?
- What binds them? Usually a **shared pain**, a **shared workaround**, or a **shared goal**.

A theme label captures that shared behavior or need. A label that only names a topic ("Technology," "Communication") has not found the pattern yet.

### How AI Supports This Play

The Playbook casts AI as a **live guide through the method**. Affinity mapping often starts slow, with a pile of real notes and no clear way in. AI walks the PM through each grouping decision, one note or cluster at a time, and asks the questions that sharpen their reasoning: why does this note belong here, what separates this group from that one, is this a real pattern or a coincidence.

The clustering, the labels, and the insights stay the PM's calls. AI makes the method less intimidating. It does not make the decisions.

- **Use it when:** the PM has real interview or research notes and knows grouping needs to happen but doesn't know how to start.
- **Avoid it when:** there are no real notes yet. Guiding a method on fake data teaches nothing worth learning.
- **Return:** guidance through the method, and a completed set of grouped, labeled themes that the PM can explain and defend.

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

Use [Template](#template) for the scaffold.


### Required Output Convention

Default to a **clean, paste-ready artifact**.

That means:

- at least three labeled theme clusters, each with grouped observation bullets
- at least three key insights, each with a one-sentence title and a short paragraph
- observation bullets kept short (8-12 words each)
- key insight paragraphs sized for the template (50-80 words)
- explanation and methodology notes below the artifact, not inside the fields
- the map states who grouped it: **the team** (coached) or **AI draft grouping: for the team to challenge**

### Step 1: Check the Source Data

Before grouping observations, verify the data is customer-side evidence: observations about customer behavior, experience, friction, and goals.

Flag and do not proceed if the observations are primarily:

- internal team opinions or preferences
- product feature requests written in the PM's voice
- engineering architecture notes
- stakeholder directives

Affinity mapping is only as useful as the evidence it synthesizes. If the input data is not customer-side, the output themes will reflect team assumptions, not customer reality.

### Step 2: Collect Available Artifacts

Ask whether the user has materials to supply:

- empathy interview notes or transcripts
- customer feedback logs or support tickets
- survey open-text responses
- competitive research observations
- outputs from psk-empathy-interviews, psk-jobs-to-be-done, or psk-proto-persona

The more raw material supplied, the stronger the clustering. If only fragments are available, note that the resulting themes are provisional and should be validated before being used in psk-problem-identification.

Do not skip this ask.

### Step 3: Coach the Method (Default)

Unless the PM asks you to group the notes, walk them through the Playbook's method one step at a time. Do not move on until they finish the current step. This mirrors the critique guidance in this Play.

1. **Orient.** In a few sentences, explain what affinity mapping is and what a good result looks like.
2. **Break notes into observations.** Coach the PM to put each distinct observation on its own note. Show one example of splitting a note that holds two ideas, then have them check theirs.
3. **Immerse.** Have the PM read all the notes first. Ask what stands out, what surprises them, what repeats. Do not summarize the notes for them.
4. **Group.** Have the PM put together notes that seem to share something. Test each grouping with the questions in [What Binds a Cluster](#what-binds-a-cluster). When they are stuck, offer the kinds of things that bind a cluster (shared pain, shared workaround, shared goal) to consider. Do not say which notes go together.
5. **Name the themes.** For each cluster, ask what the notes truly share and have the PM write the label. If the label only names a topic, show a generic example of a stronger label, then have them try again.
6. **Develop the key insights.** Have the PM write at least three. Test each with Step 6's rules.

Mark every example or suggestion as something to consider, accept, adjust, or reject, never as the answer. Keep the PM encouraged; this is a skill they are building. Then format what they commit into the template.

If the PM asks you to group the notes instead, Steps 4-6 below are how you build the draft. They are also the rules you hold the PM's own grouping to when coaching.

### Step 4: Group the Observations

Cluster the raw observations into groups where similar findings sit together.

Rules for this step:

- Create at least three clusters. More is fine if the data warrants it.
- Do not force observations into neat categories if they genuinely sit between two clusters. A cross-cutting observation is useful data.
- Each cluster should be internally consistent: observations within a cluster should be meaningfully similar, not just topically adjacent.
- Do not discard outlier observations. Findings that do not cluster easily often signal the most overlooked problems.

### Step 5: Label the Themes

Give each cluster a theme label that names the pattern happening in that cluster, not just the subject area.

Strong theme label: names what is happening for the customer.
- Example: "Scheduling Delays Caused by Disconnected Systems"
- Not: "Scheduling" or "System Problems"

Weak theme label: names a topic that could hold almost any observation.
- Example: "Process Issues" or "Communication Challenges"

Each theme label should be specific enough that a teammate unfamiliar with the research could roughly predict what observations belong inside it.

Default to 4 themes when the data supports it. The blank template has 4 circles. Do not artificially limit to 4 if the data warrants more.

### Step 6: Develop the Key Insights

Write at least three key insights. One insight per major theme is the baseline. A particularly rich or important theme may warrant a dedicated insight even if it is not the largest cluster.

Each key insight has two required parts:

**Title (one sentence, 5-8 words):** Names the challenge or pattern in plain language.

**Paragraph (50-80 words):** Explains what this pattern means for product decisions. Should answer: What is happening for the customer? Why does it matter? What should the product team understand or do differently because of this?

Key insights are inferences, not summaries. If the insight paragraph could have been written by reading only the theme label, it has not done the synthesis work.

### Step 7: Review for Completeness

Before finalizing:

- Did the team do the grouping, or is this an AI draft? If it is a draft, is it labeled as one, and has the team challenged it?

- Do the themes cover the breadth of the data, or is there a major cluster of observations that went unlabeled?
- Does any single observation appear in more than one theme cluster? If so, resolve which cluster owns it, or name it as a cross-cutting theme.
- Do the key insights answer "so what?" or do they just restate the theme label?
- Are there at least three themes and at least three insights?
- Are the observation bullets short enough to be paste-ready?

### Step 8: Offer Next Steps

After delivering the completed affinity map, offer three paths:

1. **Use these key insights in psk-problem-identification** to turn the strongest patterns into candidate problem statements.
2. **Review the insights as a team** to identify which pattern represents the highest-priority problem to pursue.
3. **Re-run affinity mapping with a different grouping lens** to check whether a different clustering reveals patterns the first pass missed.

## Template

### When to Use This

Use this template during **Discover + Investigate** after you have collected qualitative observations from customer research. You are ready to map when you have raw notes from empathy interviews, customer feedback, survey responses, or other customer-side sources and need to organize them into patterns.

Upstream work that feeds this template: psk-empathy-interviews (primary), psk-jobs-to-be-done, psk-proto-persona.

Downstream: the key insights from this map feed psk-problem-identification.

### Template

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

### Usage Guidance

#### Filling the Template

1. Start with **Research Context** to anchor what data went into this map.
2. Fill **Theme Clusters** one at a time. Label the theme only after you have seen what observations belong together - resist naming the theme before clustering.
3. Write **Key Insights** after all clusters are labeled. Do not write insights cluster by cluster as you go; seeing all the clusters together often changes what the insights should say.
4. Run the **Completeness Check** before treating the map as done.
5. The **Notes** section is optional. Use it if there are outlier observations or re-grouping ideas worth capturing.

#### If You Have No Observation Data Yet

Affinity mapping requires input data. If no customer-side observations are available:

- Offer to help the user run psk-empathy-interviews first.
- If the user wants a scaffold to use in an upcoming workshop, fill the theme and insight sections with labeled placeholder sections and explain that they should be completed collaboratively with the team after data is collected.
- Do not generate observations from the agent's training data and present them as customer findings.

#### What Goes Where

| Section | Contains | Does NOT Contain |
|---------|----------|------------------|
| Theme Clusters | Direct customer observations grouped by pattern | Opinions, solutions, feature requests, team preferences |
| Theme Labels | A named pattern describing what is happening | A broad topic area that could hold any observation |
| Key Insights | Inferences about what the patterns mean for the product | Restatements of theme labels, feature recommendations |
| Notes | Outliers, open questions, re-grouping ideas | The main deliverable content |

#### Connecting to Other Skills

- **Upstream:** psk-empathy-interviews provides the raw observation notes. psk-jobs-to-be-done and psk-proto-persona provide additional customer context that can inform how observations are grouped.
- **Downstream:** The key insights from this map feed psk-problem-identification. The strongest insight often becomes the focal point for the candidate problem that gets developed in psk-framing-the-problem.

#### Capacity Reference

| Field | Guidance |
|-------|----------|
| Theme label | 6-10 words. Names the pattern, not the topic. |
| Observation bullet | 8-12 words. Direct, factual, customer-side. |
| Key insight title | 5-8 words. Plain language. |
| Key insight paragraph | 50-80 words. Answers "so what?" |

## Examples

Illustrative and fictional, not customer evidence.

- **Strong:** Freight-broker observations about chasing shipment updates form a pattern: visibility gaps create reactive operations. Keep each observation in one cluster and explain the implication.
- **Weak:** A cluster called "Visibility" names a topic without showing a pattern.
- **Drift to avoid:** Observation overlap: putting the same note in several clusters inflates the apparent evidence. Assign its primary meaning or split genuinely separate observations.


## Common Pitfalls

- **Naming Themes by Topic, Not Pattern:** Name what is happening, not what it is about. "Fragmented Communication Tools Slow Handoffs" has diagnostic value. "Communication" does not.

- **Treating Key Insights as Summaries:** Write insights that answer "so what?" and "what does this mean for what we prioritize or build?" If the insight paragraph could have been inferred from the label alone, it is not yet an insight.

- **Discarding Outlier Observations:** Keep outlier observations visible. If multiple outliers cluster loosely together, name that as an emerging theme. If a single observation stands alone, flag it in the completeness review.

- **Collapsing Distinct Themes to Hit a Target Count:** Keep themes separate if the underlying observations point to different root causes or different customer roles. Six specific themes are more useful than three bloated ones.

- **Mapping Team Opinions Instead of Customer Evidence:** Return to Step 1. Replace internal opinion entries with direct customer observations. If no customer-side data exists yet, run psk-empathy-interviews before mapping.

- **Stopping at the Cluster, Skipping the Insight:** Always complete the key insights section before treating the affinity map as done.

- **Running Affinity Mapping Alone:** Run affinity mapping as a cross-functional team exercise. The process of debating where an observation belongs is part of the value. When the group agrees on a theme label, they have done the sensemaking together.

- **Writing Insights Too Narrowly to Be Actionable:** Key insights should reflect patterns across multiple observations from multiple customers or sources. If only one observation supports a theme, the theme may not yet be valid.

- **AI's Themes Quietly Become the Team's:** Coach by default (Step 3). If the PM asks for a draft grouping, label it as one, show why each cluster holds together, and have the team challenge it before anything moves downstream.

- **Guided Is Mistaken for Validated:** State the evidence base on the map (number and type of sources). Mark themes resting on thin evidence as provisional, and name what more research would confirm them.

## References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-affinity-mapping) for supporting source material and expanded examples.
