---
name: ps-affinity-mapping
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

## Key Concepts

### This Skill Bridges Interviews and Problem Identification

Affinity mapping is the synthesis step. Raw observations from empathy interviews are too granular to act on directly. Affinity mapping groups them into patterns. Those patterns become the input to ps-problem-identification.

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
- **Real notes, and the PM asks you to group them (or chooses best guess):** produce a draft map, labeled **AI draft grouping: for the team to challenge**. Show why each cluster holds together, and end with the groupings you were least sure of. The team still decides.
- **Fragments only:** coach or draft as above, and label every theme provisional.
- **No real notes:** stop. Affinity mapping on invented data teaches nothing and proves nothing. Offer to help prepare interviews (ps-empathy-interviews), or to set up the template for a workshop once notes exist. Never invent observations or quotes to map. Labeling the work "hypotheses" doesn't change this: produce no themes, clusters, or map layout at all. If the PM needs something for a meeting, offer a short plain list of assumptions to test in interviews, clearly labeled, and point to ps-empathy-interviews.

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

Use [template.md](template.md) for the scaffold.

See the source play pages in [assets/ps_affinity_mapping_playbook_pages.pdf](assets/ps_affinity_mapping_playbook_pages.pdf).

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
- outputs from ps-empathy-interviews, ps-jobs-to-be-done, or ps-proto-persona

The more raw material supplied, the stronger the clustering. If only fragments are available, note that the resulting themes are provisional and should be validated before being used in ps-problem-identification.

Do not skip this ask.

### Step 3: Coach the Method (Default)

Unless the PM asks you to group the notes, walk them through the Playbook's method one step at a time. Do not move on until they finish the current step. This mirrors [prompts/01](prompts/01-learn-affinity-mapping.md).

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

1. **Use these key insights in ps-problem-identification** to turn the strongest patterns into candidate problem statements.
2. **Review the insights as a team** to identify which pattern represents the highest-priority problem to pursue.
3. **Re-run affinity mapping with a different grouping lens** to check whether a different clustering reveals patterns the first pass missed.

## Examples

See [examples/sample.md](examples/sample.md).

The example set includes:

- a strong affinity map from a B2B logistics domain with well-labeled themes and product-relevant insights
- a weak version with vague topic labels and insights that restate rather than infer
- a drift-bug example showing the Observation Overlap Bug and how to resolve it

## Common Pitfalls

### Pitfall 1: Naming Themes by Topic, Not Pattern

**Symptom:** Theme labels like "Communication," "Technology," or "People."

**Consequence:** The label holds almost any observation. The clustering reveals nothing about what is actually happening for the customer.

**Fix:** Name what is happening, not what it is about. "Fragmented Communication Tools Slow Handoffs" has diagnostic value. "Communication" does not.

### Pitfall 2: Treating Key Insights as Summaries

**Symptom:** The key insight paragraph restates the theme label in slightly more words. Example: "Theme: Scheduling Delays. Insight: Scheduling delays are a problem for customers."

**Consequence:** The synthesis step adds no value. The PM is no closer to knowing what to do.

**Fix:** Write insights that answer "so what?" and "what does this mean for what we prioritize or build?" If the insight paragraph could have been inferred from the label alone, it is not yet an insight.

### Pitfall 3: Discarding Outlier Observations

**Symptom:** Observations that do not fit neatly into existing clusters are dropped or lumped into an "Other" category.

**Consequence:** The outliers often signal the most overlooked or underserved problems. Discarding them creates a false sense of clean data.

**Fix:** Keep outlier observations visible. If multiple outliers cluster loosely together, name that as an emerging theme. If a single observation stands alone, flag it in the completeness review.

### Pitfall 4: Collapsing Distinct Themes to Hit a Target Count

**Symptom:** Two different patterns are merged into one theme because both involve, for example, "slow processes." The merged label becomes "Slow Processes."

**Consequence:** The distinction between two different root causes disappears. The PM ends up solving for the combined label rather than the separate problems.

**Fix:** Keep themes separate if the underlying observations point to different root causes or different customer roles. Six specific themes are more useful than three bloated ones.

### Pitfall 5: Mapping Team Opinions Instead of Customer Evidence

**Symptom:** The observations read like a backlog grooming session. Entries like "we need better reporting" or "the API is too slow" appear in the clustering.

**Consequence:** The affinity map reflects what the team already believed, not what customers actually said. The insights confirm existing assumptions rather than challenging them.

**Fix:** Return to Step 1. Replace internal opinion entries with direct customer observations. If no customer-side data exists yet, run ps-empathy-interviews before mapping.

### Pitfall 6: Stopping at the Cluster, Skipping the Insight

**Symptom:** The output has labeled clusters with grouped observations but no key insights section. The PM presents the clusters as the deliverable.

**Consequence:** The analytical value of affinity mapping lives in the inference step. Clusters are intermediate work. Without key insights, the PM still has to make the synthesis leap alone, which is where the exercise was supposed to help.

**Fix:** Always complete the key insights section before treating the affinity map as done.

### Pitfall 7: Running Affinity Mapping Alone

**Symptom:** A single PM reviews the interview notes and produces the affinity map without involving other team members.

**Consequence:** The map reflects one person's interpretation. Disagreements that would have surfaced in a group session go unresolved. Team members do not develop shared ownership of the findings.

**Fix:** Run affinity mapping as a cross-functional team exercise. The process of debating where an observation belongs is part of the value. When the group agrees on a theme label, they have done the sensemaking together.

### Pitfall 8: Writing Insights Too Narrowly to Be Actionable

**Symptom:** A key insight is scoped to one customer's specific complaint. Example: "Insight: Lisa at Acme Corp had trouble logging in on her mobile device."

**Consequence:** A single-customer observation is not a pattern. Acting on it produces a fix for one person rather than a solution for a segment.

**Fix:** Key insights should reflect patterns across multiple observations from multiple customers or sources. If only one observation supports a theme, the theme may not yet be valid.

### Pitfall 9: AI's Themes Quietly Become the Team's

**Symptom:** The PM pastes the notes, the skill returns tidy clusters, and the team adopts them unchallenged. Nobody can say why a note sits where it does.

**Consequence:** The grouping looks authoritative and goes unchecked. The team skips the sense-making, which is where affinity mapping creates its value.

**Fix:** Coach by default (Step 3). If the PM asks for a draft grouping, label it as one, show why each cluster holds together, and have the team challenge it before anything moves downstream.

### Pitfall 10: Guided Is Mistaken for Validated

**Symptom:** The team works every step of the method, and finishing the steps starts to feel like proof. The themes get presented as findings even though they rest on two interviews.

**Consequence:** Confidence rises while evidence does not. No one re-checks the finished map. Process rigor replaces data rigor.

**Fix:** State the evidence base on the map (number and type of sources). Mark themes resting on thin evidence as provisional, and name what more research would confirm them.

## References

### Skill Files

- [template.md](template.md) - affinity map scaffold
- [prompts/](prompts/README.md) - copy-paste prompt for chat-based AI tools (1: learn affinity mapping by doing it)
- [examples/sample.md](examples/sample.md) - strong, weak, and drift-bug examples

### Related Skills

- [ps-empathy-interviews](../ps-empathy-interviews/SKILL.md) (primary upstream source of observations)
- [ps-jobs-to-be-done](../ps-jobs-to-be-done/SKILL.md) (upstream: jobs and outcomes as additional input)
- [ps-proto-persona](../ps-proto-persona/SKILL.md) (upstream: persona context for interpreting observations)
- [ps-problem-identification](../ps-problem-identification/SKILL.md) (downstream: key insights feed candidate problem statements)

### Related Project Docs

- [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)
- [framework-glossary.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/framework-glossary.md) (Evidence, Discovery, Assumption)
- [skill-authoring-workflow.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/skill-authoring-workflow.md)

### Source Material

- [Baseline Playbook version](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml). Full source PDF supplied separately.
- [assets/ps_affinity_mapping_playbook_pages.pdf](assets/ps_affinity_mapping_playbook_pages.pdf)
- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 36-40: Template 08 of 24 there, with the AI overview on slide 38 and the prompt on slide 39. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).
- Productside Playbook companion document (supplied separately)
