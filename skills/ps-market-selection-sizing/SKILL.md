---
name: ps-market-selection-sizing
description: >-
  Name a market, run a PESTEL on it, cut it into at least two segments with the
  users, buyers, and influencers in each, and size TAM, SAM, and SOM with a
  source behind every input. Use before jobs and persona work, when the team
  has not yet named who it serves or whether the opportunity is worth exploring.
intent: >-
  Help a Product Manager define the market their product serves, understand the
  forces acting on it, segment it by shared needs, goals, and behaviors, and
  size it using the Productside Market Selection & Sizing play, so the team
  chooses segments worth exploring on sourced evidence rather than on numbers a
  model invented.
type: component
blueprint_stage: Context
best_for:
  - "Naming the market a product serves at the right altitude, before discovery starts"
  - "Cutting a market into segments defined by needs and behaviors, with real buyers and users in each"
  - "A first-pass TAM, SAM, and SOM built as sourced formulas and ranges, not as guesses"
scenarios:
  - "We want to explore a new product area and need to know which market and segments are worth it"
  - "Help me size the market for our product before we pitch it to leadership"
  - "Our segments are just industries and company sizes; help me find segments that actually differ"
---

## Purpose

Create a **Productside-style Market Selection & Sizing artifact** for the market a product serves.

This skill is for the **Context** phase. Before diving into a product opportunity, either an iteration of an existing product or a new one, the team needs to understand what market the product serves, what is happening in that market, and whether it is an interesting one to pursue. The artifact has three parts:

1. **Market Selection** - name the market and run a PESTEL analysis of the forces acting on it
2. **Segment the Market** - cut it into at least two distinct segments, and name the users, buyers, and influencers in each
3. **Size the Market & Segments** - TAM for the market, SAM for each segment, and SOM in annual revenue when there is a product to price

Use this skill when you need to:

- name the market before writing jobs, personas, or problem statements for it
- move segmentation beyond simple industries or demographics
- decide which segments are worth exploring, with a first-pass size behind each
- give later plays (Jobs-to-Be-Done, Personas, Empathy Interviews, Positioning) a defined segment to work from

This is not a financial forecast or a business case. It is a first pass, fast and simple, that the team revisits as it learns more. And it is never a place for numbers without sources.

**Source status:** this Play exists only in the B2B work-in-progress deck (Template 04 of 24), which is not yet ratified. The baseline deck has no equivalent.

## Key Concepts

### Name the Market at the Right Altitude

A market definition centers on **who the product is for and the benefit it provides them**. "Healthcare" is too broad to analyze. One customer's workflow is too narrow to size. Three questions, asked one at a time, get to the right altitude:

1. What problem are people trying to solve, or what are they trying to make better, in this space?
2. Who has this problem (businesses, consumers, channel partners), and when does it become important enough for them to look for help?
3. What do they do today to solve it, and what other options could they choose?

Propose a definition from the answers and have the PM confirm or iterate it. Lock it before running the PESTEL.

### PESTEL: Evidence, Not a Full Grid

PESTEL names six forces acting on the market: **Political, Economic, Social, Technological, Environmental, Legal.** The goal is evidence, not a filled grid. Each force is committed either as **evidence with a source**, or as an **open question to research**. A PESTEL full of generic forces ("technology is changing fast," "regulation is increasing") fits every market and informs none.

Ask the PM first which forces they know should, or should not, be considered. They know things about this market that no search will find.

### A Segment Is Defined by Shared Needs, Goals, and Behaviors

A segment is a potential group of customers that is **unique and identifiable through a set of shared traits, goals, preferences, and behaviors.** Industry and company size can bound a segment, but they rarely define one. Two hospitals of the same size can buy for completely different reasons.

Every segment needs:

- a **name** and a brief description of the traits, desires, and preferences that make it unique
- **explicit cut logic**: what makes it distinguishable from the other segments, stated so it can be tested
- the **people operating in it**: users, buyers, and influencers. A segment with no real buyer or user in it is a segment for show.

The template holds two segments, and the Play asks for at least two. A **high-potential segment** has strong underserved needs and problems worth solving to validate.

### TAM, SAM, SOM: The Productside Way

- **TAM (Total Addressable Market):** think broadly. The whole market the product could serve.
- **SAM (Serviceable Addressable Market):** for **each segment**, the part of the TAM the product can actually serve.
- **SOM (Serviceable Obtainable Market):** for each segment, the share of the SAM the team can realistically win, in **annual revenue**. It must consider **competition**, plus pricing and company constraints.

Name the **counting unit** (sites, firms, accounts, people, checkpoints) and keep it consistent through TAM, SAM, and SOM. Check that SOM ≤ SAM ≤ TAM in the same unit. Revenue is units × an annual price per that same unit.

**SOM can wait.** If there is an existing product, estimate SOM. If not, skip it until solutions have been ideated, or show it as a conditional formula with the price marked as an assumption.

### Every Number Is a Blank to Source

AI is fast at structure and dangerous at facts. Every figure about size, growth, or competitors that no one can trace to a source is a guess dressed as a finding. So:

- **Write sizing as formulas**, with every input labeled by its source (`[S1]`, `[S2]`) or marked `[TO SOURCE]`.
- **Triangulate.** Use three different approaches (top-down, bottom-up, analogous products, subject-matter experts). Don't rely on a single search or one source.
- **Use ranges.** Ranges reduce overconfidence and turn a debate about one number into a discussion of risk.
- **A market share needs a basis.** "5% in two years" is not a basis. Competitive position, reach, win rate, and capacity are.
- **Never cite competitor revenues** that no filing or report states.

### "Is It Worth It?" Stays With the PM

The skill can recommend which segments look most promising and say why. The judgment that a market or segment is worth pursuing belongs to the PM and their team.

### How AI Supports This Play

The Playbook calls AI **fast at structure and dangerous at facts**. It can lay out a PESTEL skeleton, suggest ways to segment a market, and frame a TAM/SAM/SOM calculation. What it cannot do is know the market. Use it to organize the sources the PM has and to expose the gaps still to fill. That turns scattered evidence into a shape the team can reason about.

In this Play, the Playbook's own prompts ask AI to research, propose segments, and recommend two. So this skill does propose, with its reasoning visible and every claim cited. It never supplies a number without a source the PM can check.

- **Use it when:** the market is named (or nearly) and there are real sources, or web research is available, and the PM needs help structuring or sharpening the analysis.
- **Avoid it when:** there are no sources and no way to research, or the request is simply "what's the market size?" Build the structure and mark the numbers `[TO SOURCE]` instead.
- **Return:** a PESTEL with the evidence organized and gaps flagged as questions, segments with explicit cut logic the team can test, and TAM/SAM/SOM as formulas with sourced inputs.

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

See the source play pages in [assets/ps_market_selection_sizing_playbook_pages.pdf](assets/ps_market_selection_sizing_playbook_pages.pdf).

### Required Output Convention

Default to a **one-page market analysis that mirrors the template**:

- **Market Selection:** the market name, and a PESTEL with one short entry per force, each tagged with a source ID or marked as an open question
- **Total Addressable Market:** one or two sized facts, each with a source ID
- **Segments 1 and 2:** name, one- or two-sentence description, and the users, buyers, and influencers operating in it
- **SAM per segment:** the counting logic as a short formula, with units and a range
- **SOM per segment:** the share basis and units × price = annual revenue, as a range, or "deferred until solutions are ideated"
- **Source register** below the artifact: ID, source, date, what it supports
- **Open questions** below the register: the `[TO SOURCE]` blanks and PESTEL questions, ranked by how much they could change the sizing

Use the provenance tags shared across this library wherever content is not the PM's own: `[RESEARCH]` with a source ID for anything found, `[AI-SUGGESTED, VALIDATE THIS]` for forces, segments, or cut logic you proposed. Mark numbers with no source `[TO SOURCE]`, never a guessed value.

Keep entries compact. The template's PESTEL cells, segment descriptions, and sizing boxes are small.

### If the PM Brings a Draft

When the PM arrives with a market analysis, review it before adding to it:

1. **Altitude.** Is the market named around who the product serves and the benefit, at a level that can be analyzed and sized?
2. **PESTEL.** Flag generic forces and unsourced claims. Ask which are evidence and which are open questions.
3. **Segments.** Is the cut logic explicit and testable? Do the segments differ by needs, goals, and behaviors, or only by industry and size? Does each have real users, buyers, and influencers?
4. **Numbers.** Does every input have a source? Are units consistent, and is SOM ≤ SAM ≤ TAM? Is the market share justified by competition and capacity, or assumed?
5. **Offer fixes last**, as options to accept, adapt, or reject. Return the review as a compact table (element, verdict, why, suggested fix).

### Step 1: Confirm the Product and Who It Serves

Before anything else, answer:

- What product or product idea is this, existing or new?
- Who is it for, and what benefit does it provide them?
- What decision is this analysis meant to inform?

**Guard against tech-role bias.** Models default to picturing software buyers and developer users. A market is defined by the people with the problem. A pump-station monitoring product's market is water utilities and the operators and directors who run them, not "IoT platforms." The users, buyers, and influencers named in each segment should be the real roles in that market (operators, technicians, directors, council members, regulators), not technologists, unless the product truly serves technologists.

### Step 2: Gather Evidence Before Drafting

This skill uses **web research and user-supplied artifacts.** Offer both before drafting:

1. **Web research.** Offer to search for the market. Prefer primary sources: government statistics and registries, regulator data, trade-association reports, company filings, and practitioner forums. Cite each source with a link and date. Analyst summaries and vendor marketing are weak sources for sizing.
2. **User-supplied artifacts.** Ask for what the PM already holds: market reports, pricing, competitor information, company constraints, customer lists, or prior strategy work.

If no sources exist yet and web research is unavailable, say so. The Playbook advises against AI sizing without sources. Build the structure, mark every number `[TO SOURCE]`, and give a short research plan. Do not fill the gap with plausible numbers.

### Step 3: Pressure-Test the Market Definition

Ask the three altitude questions one at a time (see [Name the Market at the Right Altitude](#name-the-market-at-the-right-altitude)). Then propose a market definition and ask the PM to confirm or iterate. Lock it before moving on.

### Step 4: Build the PESTEL

1. Ask the PM which forces they know should, or should not, be considered.
2. Research each of the six forces.
3. Commit each as evidence with a source ID, or as an open question to research. Label assumptions and uncertainties, and suggest where reliable information could be found.

One short entry per force. If a force has nothing specific to this market, say so rather than filling the cell with a generic trend.

### Step 5: Segment the Market

1. Propose 4-6 candidate segments defined by needs, goals, and behaviors. For each, state the cut logic and name 2-3 real buyer and user roles who operate in it. Tag them `[AI-SUGGESTED, VALIDATE THIS]` unless they came from the PM or a source.
2. Recommend two high-potential segments (strong underserved needs, problems worth solving to validate) and justify each with evidence.
3. Invite the PM to challenge the cuts and add their own knowledge. The PM chooses the segments that go in the template, at least two.
4. For each chosen segment, list the users, buyers, and influencers. Think broadly.

### Step 6: Size the Market and Segments

1. **Name the counting unit** for this market and keep it throughout.
2. **TAM.** Size the broad market from the best available sources. Show the arithmetic.
3. **SAM per segment.** Show the counting logic as a formula (for example, number of sites × average units per site), with each input sourced or `[TO SOURCE]`.
4. **Triangulate.** Name three sizing approaches (top-down, bottom-up, analogous products, subject-matter experts) and the research each needs. Note where they agree and disagree.
5. **Express ranges**, not point estimates.
6. **SOM per segment, if there is a product.** State the share basis (competitive alternatives, reach, win rate, capacity, time horizon), then units × annual price = annual revenue, as a range. Mark an assumed price as a pricing assumption, not evidence. If there is no product yet, write "deferred until solutions are ideated."

### Step 7: Check the Numbers

Before presenting:

- every input has a source ID or is marked `[TO SOURCE]`
- units are consistent across TAM, SAM, and SOM
- SOM ≤ SAM ≤ TAM
- no market share without a stated basis
- no competitor revenue or customer count without a source that states it
- ranges, not single numbers

### Step 8: Hand the Call to the PM

Present the artifact with the open questions ranked by how much they could change the sizing. Recommend the segment the evidence favors if asked, and say why. Do not declare the market worth pursuing. That call stays with the PM.

### Step 9: Offer Next Steps

Offer, as options:

1. **Write jobs for the people in the chosen segments** (ps-jobs-to-be-done). The segments and the people named in them are its input.
2. **Build a proto-persona** for the primary user in the most promising segment (ps-proto-persona).
3. **Close the biggest `[TO SOURCE]` gaps** before taking the sizing to leadership.

The user decides what comes next. Revisit this artifact as discovery produces evidence.

## Examples

See [examples/sample.md](examples/sample.md).

The example set includes:

- a strong market analysis for municipal water-utility pump-station monitoring, with sourced inputs, cut logic, and ranges (figures are illustrative)
- a weak version in the same domain: confident unsourced numbers, demographic segments, and a generic PESTEL
- a drift-bug example, "the free five percent," showing an SOM built on an assumed share

## Common Pitfalls

### Pitfall 1: AI Invents the Market Size

**Symptom:** The TAM box says "$4.2B, growing 9% annually," with no source, or with a source no one can find.

**Consequence:** A guess dressed as a finding goes into a leadership deck. The first person who asks "where did this come from?" ends the PM's credibility on the topic.

**Fix:** Every number carries a source ID or `[TO SOURCE]`. Never fill a blank with a plausible figure.

### Pitfall 2: Competitor Numbers No One Can Know

**Symptom:** "Competitor X has 30% share and $80M in revenue in this segment," for a private company with no disclosures.

**Consequence:** The SOM rests on invented competitive data.

**Fix:** Use only competitive facts a filing, a report, or a named source states. Otherwise describe the competitor qualitatively and mark the gap.

### Pitfall 3: A Generic PESTEL

**Symptom:** "Political: regulation is increasing. Technological: AI is changing everything. Economic: inflation."

**Consequence:** The analysis fits every market and informs none. The team learns nothing about this market's forces.

**Fix:** One specific entry per force, tied to this market, with a source, or an honest open question.

### Pitfall 4: Segments for Show

**Symptom:** Segments are "Small, Medium, Enterprise" or "Healthcare, Finance, Retail," with tidy cuts that would fit any market.

**Consequence:** Customers inside a segment don't share needs, so jobs, personas, and positioning built on the segment don't hold.

**Fix:** Define segments by shared needs, goals, and behaviors, and state the cut logic so it can be tested. Use size or industry only as a boundary.

### Pitfall 5: Segments With No People in Them

**Symptom:** Each segment has a name and a description, but no one in it: no user, buyer, or influencer.

**Consequence:** The next plays (Jobs-to-Be-Done, Personas) have no one to write about. The Playbook names this trap: segments with no real persona.

**Fix:** Name the users, buyers, and influencers in every segment. Think broadly.

### Pitfall 6: The Market at the Wrong Altitude

**Symptom:** The market is "software" or "healthcare," or it is one customer's workflow.

**Consequence:** Too broad can't be analyzed. Too narrow can't be sized or segmented.

**Fix:** Run the three altitude questions. Center the definition on who the product is for and the benefit it provides.

### Pitfall 7: The Free Five Percent

**Symptom:** "If we capture just 5% of the SAM..." with no reason why 5%.

**Consequence:** The SOM is a wish. It ignores competition, which the Playbook says SOM must consider.

**Fix:** State the share basis: the alternatives customers use, how many the team can reach, a win-rate assumption, and delivery capacity over a named horizon. If there is no basis yet, show SOM as a conditional formula and say what would anchor it.

### Pitfall 8: Mixed Counting Units

**Symptom:** TAM counts companies, SAM counts sites, SOM multiplies employees by a per-seat price.

**Consequence:** The math is wrong in a way that looks right. SOM can exceed SAM without anyone noticing.

**Fix:** Name one counting unit, convert explicitly when needed, and check SOM ≤ SAM ≤ TAM.

### Pitfall 9: One Source, One Number

**Symptom:** A single search result becomes the TAM, presented to the dollar.

**Consequence:** False precision. The conversation becomes a defense of the number instead of a discussion of risk.

**Fix:** Triangulate with three approaches and present ranges.

### Pitfall 10: Professional-Looking Logic, Never Tested

**Symptom:** A polished analysis with clean formulas and confident segment names that no one has checked against a customer or an expert.

**Consequence:** The structure is mistaken for rigor, and the team commits to a segment on untested logic.

**Fix:** Tag AI-suggested cut logic for validation, rank the open questions, and revisit the analysis as discovery produces evidence.

## References

### Skill Files

- [template.md](template.md) - market analysis scaffold
- [prompts/](prompts/README.md) - copy-paste prompts for chat-based AI tools (4, run in order in one chat)
- [examples/sample.md](examples/sample.md) - strong, weak, and drift-bug examples
- [assets/ps_market_selection_sizing_playbook_pages.pdf](assets/ps_market_selection_sizing_playbook_pages.pdf) - source pages from the B2B work-in-progress deck (slides 14-18)

### Related Skills

- [ps-outcome-tree](../ps-outcome-tree/SKILL.md) - Context-phase neighbor; the business outcome this market should serve
- [ps-jobs-to-be-done](../ps-jobs-to-be-done/SKILL.md) - downstream; jobs for the people in the chosen segments
- [ps-proto-persona](../ps-proto-persona/SKILL.md) - downstream; a persona for the center of a chosen segment
- [ps-positioning-statement](../ps-positioning-statement/SKILL.md) - downstream; positioning for one persona in one segment

### Related Project Docs

- [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml)
- [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)
- [skill-authoring-workflow.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/skill-authoring-workflow.md)

### Source Material

- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 14-18: Template 04 of 24, with the AI overview on slide 16 and prompts on slide 17. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).
- [assets/ps_market_selection_sizing_playbook_pages.pdf](assets/ps_market_selection_sizing_playbook_pages.pdf)
