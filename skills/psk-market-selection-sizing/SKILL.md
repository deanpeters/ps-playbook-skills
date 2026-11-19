---
name: psk-market-selection-sizing
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

### Usage Notes

- **Type:** component. **Phase:** Context. **Evidence:** web research + user artifacts.
- **Every number needs a source.** Sizing is written as formulas whose inputs carry source IDs or `[TO SOURCE]`, in one counting unit, as ranges, with SOM ≤ SAM ≤ TAM.
- **AI may propose, never invent.** Following the Playbook's own prompts, the skill proposes market definitions, PESTEL entries, and segments with its reasoning visible, and cites what it finds. It never fills a sizing blank with a plausible number.
- **SOM can wait:** it is estimated only when there is a product to price. Otherwise it is deferred until solutions are ideated.
- **Downstream:** psk-jobs-to-be-done, psk-proto-persona, psk-empathy-interviews, and psk-positioning-statement use the segments and the people named in them.
- The source deck is not yet ratified, and its pages are not objectified (no named shapes). The budget entry in `technical/data/canonical_template_budgets.yaml` has guidance only, no shape budgets.

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

1. **Write jobs for the people in the chosen segments** (psk-jobs-to-be-done). The segments and the people named in them are its input.
2. **Build a proto-persona** for the primary user in the most promising segment (psk-proto-persona).
3. **Close the biggest `[TO SOURCE]` gaps** before taking the sizing to leadership.

The user decides what comes next. Revisit this artifact as discovery produces evidence.

## Template

### When to Use This

Use this template in the **Context** phase, before Jobs-to-Be-Done and Personas, to name the market a product serves, understand the forces acting on it, cut it into segments, and size the opportunity. It is a first pass you will revisit as you learn more.

Downstream: the segments and the people named in them feed psk-jobs-to-be-done, psk-proto-persona, psk-empathy-interviews, and psk-positioning-statement.

### Template

```markdown
# Market Selection & Sizing

## Context
- Product or product idea (existing / new):
- Who it is for, and the benefit it provides:
- Decision this analysis informs:
- Counting unit (sites, firms, accounts, people, ...):

## 1. Market Selection
- Market:

### PESTEL
| Force | Entry | Source or status |
|---|---|---|
| Political | | [S#] / OPEN QUESTION |
| Economic | | |
| Social | | |
| Technological | | |
| Environmental | | |
| Legal | | |

> Quality check: Is the market named around who the product is for and the benefit, at a level you can analyze and size?
> Quality check: Is every entry specific to this market? A force that fits any market is generic. Replace it, or mark it OPEN QUESTION.
> Capacity check: One short line per force.

## Total Addressable Market (TAM)
- Sized fact 1: [S#]
- Sized fact 2: [S#]
- TAM (range, in the counting unit):

## 2. Segments

### Segment 1:
- Description (traits, goals, preferences, behaviors that make it unique):
- Cut logic (what distinguishes it from Segment 2, stated so it can be tested):
- Users:
- Buyers:
- Influencers:

### Segment 2:
- Description:
- Cut logic:
- Users:
- Buyers:
- Influencers:

> Quality check: Do the segments differ by needs, goals, and behaviors, not just by industry or size?
> Quality check: Does every segment have a real user and buyer in it?
> Provenance check: Tag suggested segments and cut logic `[AI-SUGGESTED, VALIDATE THIS]` until the team or a source confirms them.

## 3. Size the Market & Segments

### Serviceable Addressable Market (SAM)
| Segment | Counting logic (formula) | Inputs and sources | SAM (range) |
|---|---|---|---|
| 1 | | | |
| 2 | | | |

### Serviceable Obtainable Market (SOM), annual revenue
| Segment | Share basis (competition, reach, win rate, capacity, horizon) | Units x annual price | SOM (range) |
|---|---|---|---|
| 1 | | | |
| 2 | | | |

> Quality check: Does every input have a source ID or `[TO SOURCE]`? No guessed values.
> Quality check: Same counting unit throughout? Is SOM <= SAM <= TAM?
> Quality check: Is every market share justified by competition and capacity, not assumed?
> Quality check: Ranges, not single numbers? Triangulated from more than one approach?
> SOM rule: With no product yet, write "deferred until solutions are ideated," or show a conditional formula with the price marked as an assumption.

## Source Register
| ID | Source (title, publisher, link) | Date | What it supports |
|---|---|---|---|
| S1 | | | |

## Open Questions
Ranked by how much the answer could change the sizing.
1.
2.
3.
```

### Usage Guidance

- Work the three parts in order: market, then segments, then size.
- Keep entries compact. The canonical template's PESTEL cells, segment boxes, and sizing boxes are small.
- Every number needs a source the PM can check. A number without one is `[TO SOURCE]`.
- The "is it worth it" judgment stays with the PM and their team.
- Revisit this artifact as discovery produces evidence.

## Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For pump-station monitoring, name utilities and their operators, count stations consistently, and source every population and price input. Leave unknown inputs open.
- **Weak:** "Every utility is our market" leaves segment needs and purchasing conditions undefined.
- **Drift to avoid:** The free five percent: SOM is not an arbitrary percentage of a larger market. Show reachable accounts, capacity, adoption assumptions, and evidence.


## Common Pitfalls

- **AI Invents the Market Size:** Every number carries a source ID or `[TO SOURCE]`. Never fill a blank with a plausible figure.

- **Competitor Numbers No One Can Know:** Use only competitive facts a filing, a report, or a named source states. Otherwise describe the competitor qualitatively and mark the gap.

- **A Generic PESTEL:** One specific entry per force, tied to this market, with a source, or an honest open question.

- **Segments for Show:** Define segments by shared needs, goals, and behaviors, and state the cut logic so it can be tested. Use size or industry only as a boundary.

- **Segments With No People in Them:** Name the users, buyers, and influencers in every segment. Think broadly.

- **The Market at the Wrong Altitude:** Run the three altitude questions. Center the definition on who the product is for and the benefit it provides.

- **The Free Five Percent:** State the share basis: the alternatives customers use, how many the team can reach, a win-rate assumption, and delivery capacity over a named horizon. If there is no basis yet, show SOM as a conditional formula and say what would anchor it.

- **Mixed Counting Units:** Name one counting unit, convert explicitly when needed, and check SOM ≤ SAM ≤ TAM.

- **One Source, One Number:** Triangulate with three approaches and present ranges.

- **Professional-Looking Logic, Never Tested:** Tag AI-suggested cut logic for validation, rank the open questions, and revisit the analysis as discovery produces evidence.

## References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-market-selection-sizing) for supporting source material and expanded examples.
