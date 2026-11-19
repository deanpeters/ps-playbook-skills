---
name: ps-stakeholder-alignment
description: >-
  Map stakeholders by role, interest, and influence, then assign engagement
  strategies before discovery begins. Use also when asked to place named people
  on a power/interest grid.
intent: >-
  Help a Product Manager build a complete Productside-style stakeholder map
  using the Interest/Influence matrix and four engagement modes (Manage Closely,
  Keep Satisfied, Keep Informed, Monitor), so they know who has input on which
  decisions, who needs briefing on progress, and who to watch for resistance
  before discovery begins.
type: component
blueprint_stage: Context
best_for:
  - "Mapping every person who affects or is affected by your initiative"
  - "Assigning engagement strategies based on interest and influence"
  - "Preventing late-stage stakeholder surprises by building the map before discovery"
scenarios:
  - "I need to map all the stakeholders for a new product initiative before kickoff"
  - "Help me figure out who to keep informed versus who needs active engagement on this project"
---

## Purpose

Build a **complete stakeholder map** before discovery begins.

This skill is for the **Context** phase, the second play in the Productside Playbook. It helps a Product Manager identify every person who affects or is affected by their initiative, rate each one by interest and influence, and assign engagement strategies that are specific enough to act on.

A stakeholder map is not a one-time artifact. It is a working tool that should be updated as relationships shift, as skeptics become allies, and as new influencers surface during discovery and delivery.

Use this skill when you need to:

- understand who has power over your initiative before you start
- identify skeptics and blockers before they become problems
- assign engagement strategies that match the actual relationship, not a generic default
- give the team a shared picture of the political landscape

This play comes before empathy interviews and discovery work. The map guides who to recruit, who to brief, and who to watch.

This is not a communications plan, a RACI chart, or a customer list. A communications plan describes when and how to send updates. A RACI describes task ownership. A customer list belongs in the persona play. The stakeholder map does something different: it determines who has input into which decisions and at what depth, before discovery shapes those decisions.

## Key Concepts

### Stakeholder vs. Customer

These are distinct categories and must not be conflated.

**Stakeholders** are internal or partner-side people who affect or are affected by the PM's work. They live inside the organization or at the boundary (executives, legal, finance, engineering leads, partner teams). They need to be managed, informed, or satisfied.

**Customers** are the people the product serves in the field. They experience the problem the product is solving. They belong in the persona play (ps-proto-persona), not in the stakeholder map.

Mixing customers into the stakeholder table creates confusion about who needs organizational engagement vs. who needs product discovery. The two groups need fundamentally different treatment.

### Interest vs. Influence

These two dimensions are independent. Either can be high or low regardless of the other.

**Interest** is how much a stakeholder cares about this specific initiative. A legal counsel may not care about most product initiatives but may be intensely interested in one that touches data privacy.

**Influence** is how much power a stakeholder has over the initiative. Influence is not the same as seniority. A junior engineer who controls the deployment pipeline has high influence. A VP who has no say in technical decisions may have lower influence than their title suggests.

Rating both dimensions separately, and honestly, is the whole point of the matrix.

### The Four Engagement Modes

The Interest/Influence matrix places stakeholders in one of four quadrants, each with a different engagement strategy:

**Manage closely (High Influence, High Interest):** These are your key partners. They care, and they have power. Involve them early, keep them informed in detail, and make them feel like co-owners where possible. Weekly touchpoints or embedded collaboration. Surprises here are costly.

**Keep satisfied (High Influence, Low Interest):** These are often executive sponsors who are not day-to-day participants. They have the power to greenlight or block, but they do not want to be in every meeting. Keep them briefed at the right altitude - progress, risks, key decisions - without pulling them into operational detail.

**Keep informed (Low Influence, High Interest):** These stakeholders care deeply but cannot directly affect the outcome. They may be strong advocates or enthusiastic users of adjacent systems. Keep them updated through regular communications; they are often your best ambassadors if things go well.

**Monitor (Low Influence, Low Interest):** Minimal engagement needed. Check in periodically so they are not blindsided by major changes, but do not over-invest attention here.

### Engagement Modes Are About Decision Rights, Not Just Communication

This is the distinction that matters most. Engagement modes are not a comms schedule — they determine who has input on which decisions and at what depth.

- **Manage Closely** stakeholders are in the room for trade-off discussions. They have a voice in decisions, not just updates.
- **Keep Satisfied** stakeholders are briefed on outcomes and key decisions, but they are not consulted in the decision process itself. They need altitude-appropriate information, not operational depth.
- **Keep Informed** stakeholders receive regular updates but do not affect decisions. Their value is advocacy and downstream adoption, not direction-setting.
- **Monitor** stakeholders are not in the decision loop at all. Periodic check-ins prevent surprises, but they do not shape the work.

Treating all engagement as a communication cadence question misses this. A PM who sends weekly updates to all stakeholders has not done stakeholder management — they have sent emails. The quadrant assignment determines who the PM brings into decisions, not just who receives communications.

### The Map is a Working Tool

Relationships shift. A skeptic becomes an ally after a successful pilot. An executive who was "keep satisfied" suddenly becomes deeply involved after a business unit change. A new hire in legal introduces a regulatory concern no one anticipated.

Revisit the map at the start of each major phase: after framing, after discovery, before launch. The version you build before discovery is a starting hypothesis, not a final assessment.

### Completeness Check

The most common failure mode is listing only supporters. A map full of advocates looks optimistic but is nearly useless when a skeptic surfaces during a key decision.

A good stakeholder map includes:

- supporters and champions
- skeptics and cautious observers
- potential blockers
- people who were not consulted on similar initiatives in the past and caused friction as a result

If the map skews entirely positive, something is missing.

### Stakeholders Are Teammates, Not Opponents

Different functions bring different priorities: legal thinks about risk, finance thinks about returns, engineering thinks about technical feasibility. Those differences create friction — but they do not make stakeholders adversaries.

The playbook is explicit: you may have different roles, but you are all working on the same team. A skeptical legal counsel who raises a compliance concern in week two is not an obstacle — they are a teammate whose input prevented a problem at launch. A finance stakeholder who pushes back on scope is not blocking the product — they are enforcing a constraint that is real for the business.

Approach every stakeholder as someone who shares the organization's goals, even if they express those goals differently than you do. The map is a tool for building a communication strategy across that diversity, not a list of people to manage around.

### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **critic of the stakeholder map the PM drafted**. It looks for stakeholders the PM missed, asks for the evidence behind each power and interest placement, and checks that each engagement strategy fits the quadrant. The placements and strategies stay the PM's, because only the PM knows these people.

- **Use it when:** the PM has listed stakeholders and wants the map pressure-tested for gaps and placement.
- **Avoid it when:** the request is to characterize real colleagues' motives or influence from a name and a title. The model doesn't know them. When given names and titles, first ask what the PM has observed about each person's decisions and influence, and name any roles that may be missing. Offer placements, each tagged `[AI-SUGGESTED, VALIDATE THIS]`, only if the PM then asks for a best guess.
- **Return:** missing stakeholder roles named for the PM to consider, each placement questioned against what the PM has observed, and engagement strategies checked against decision rights.

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

See the source pages from the canonical playbook in [assets/ps_stakeholder_alignment_playbook_pages.pdf](assets/ps_stakeholder_alignment_playbook_pages.pdf).

### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in [prompts/01-pressure-test-stakeholder-map.md](prompts/01-pressure-test-stakeholder-map.md) one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

### Step 1: Tech-Role Bias Guard

Before drafting, pause and check who is missing.

In product work, the most visible stakeholders are often engineers, architects, or technical leads - the people the PM works with directly every day. They matter, but they are rarely the only stakeholders and often not the most influential ones.

Before drafting the table, explicitly ask: who else has interest or influence?

Check across these functions:

- Legal and compliance (especially if the initiative touches data, privacy, regulation, or contracts)
- Finance (if the initiative requires budget, headcount, or affects reported metrics)
- Sales and marketing (if the initiative changes the product the sales team sells or the story marketing tells)
- Customer success (if the initiative affects customer onboarding, support, or renewal)
- Operations (if the initiative changes workflows or operational capacity)
- Executive sponsors (who need to greenlight or protect the initiative at senior levels)

Technical roles may still make the list - but they should not be the only roles on it.

### Step 2: Gather Internal Artifacts

Look at what already exists before writing anything new:

- Org charts or team rosters that show reporting lines and team boundaries
- Prior project retrospectives or postmortems that name who caused friction or was left out
- Prior communications or briefing documents that show who was engaged on similar initiatives
- Existing knowledge about who is skeptical, who is a champion, and who was burned by a previous failure

Ask: who was involved in similar initiatives before? Who was left out and caused problems later?

This is internal artifact work. No web research needed. The evidence lives in documents, relationships, and organizational memory.

### Step 3: Build the Stakeholder Table

For each stakeholder, capture:

- **Name** - the person's actual name (4 words maximum)
- **Role / Team** - their title and team (6 words maximum)
- **Interest in This Initiative** - one clear sentence describing why they care (12 words maximum)
- **Influence** - High, Medium, or Low
- **Sentiment** - Supportive, Neutral, Skeptical, or Unknown

Aim for 6 to 10 stakeholders. Fewer than six usually means someone important has been missed. More than fifteen usually means the ratings are inflated or the scope of "stakeholder" has been defined too broadly.

Better to include someone and de-prioritize them in the matrix than to miss them entirely.

### Step 4: Place Stakeholders on the Interest/Influence Matrix

Assign each stakeholder to one of the four quadrants based on their interest and influence ratings.

After placing everyone, check for balance. A map where every stakeholder lands in "manage closely" is a signal that ratings have been inflated. Not every stakeholder is a high-priority engagement. If the ratings feel off, recalibrate.

### Step 5: Assign Engagement Strategies

For each quadrant, write a brief, specific engagement strategy.

Specific is better than generic:

- "Weekly async update via Slack with decision log" is actionable.
- "Keep informed" is not.

Each strategy should answer: how often, what to share, and what to ask for.

### Step 6: Identify Risks and Gaps

Three things to capture before closing the map:

**Missing stakeholders:** Anyone who should be here but is not yet identified. A good check is asking: who has blocked similar work in the past? Who has authority that has not been mentioned yet?

**Potential blockers:** Stakeholders who could slow or stop progress if not engaged early. These may not be formal opponents - they may simply be people who will raise concerns at a late stage if they feel uninvolved.

**Political dynamics:** Relationships between stakeholders that create complexity. For example: two stakeholders who have a history of conflict, or a senior stakeholder whose opinion a key influencer defers to entirely.

## Examples

See [examples/sample.md](examples/sample.md).

The example set includes:

- a strong stakeholder map (complete, balanced, with actionable engagement strategies)
- a weak version (supporters only, vague strategies, empty risks)
- a drift bug example (customers listed as stakeholders)

## Common Pitfalls

### Pitfall 1: Listing Only Supporters

**Symptom:** The map contains five people, all in "manage closely," all listed as Supportive.

**Consequence:** The first skeptic who surfaces during a key decision is a surprise. The team has no strategy for them.

**Fix:** Before closing the map, ask explicitly: who might push back? Who was not consulted on similar initiatives? Add them.

### Pitfall 2: Confusing Stakeholders with Customers

**Symptom:** Truck drivers, field technicians, or end users appear in the stakeholder table because they are "affected by" the initiative.

**Consequence:** The PM spends time managing internal engagement with people who actually need product discovery and empathy work.

**Fix:** Customers who use the product in the field belong in the persona play (ps-proto-persona), not here. The stakeholder map covers people who affect the initiative organizationally. Keep these lists separate.

### Pitfall 3: Equating Influence with Seniority

**Symptom:** A VP is rated High Influence for every initiative because of their title. A junior engineer who owns the deployment process is rated Low Influence.

**Consequence:** The engagement strategy misses the people who actually control the outcome.

**Fix:** Rate influence based on actual power over this specific initiative. Ask: can this person approve, block, accelerate, or veto the work? That is influence. Title alone is not.

### Pitfall 4: Treating Interest and Influence as Binary

**Symptom:** Every stakeholder is either High or Low. Nobody is Medium.

**Consequence:** Too many stakeholders end up in "manage closely," diluting attention.

**Fix:** Use Medium deliberately. Reserve High for stakeholders with genuine power or deep engagement with this initiative specifically.

### Pitfall 5: Building the Map Once and Never Revisiting

**Symptom:** The map is filled out during the Context phase and never opened again.

**Consequence:** Relationships that shift during discovery, framing, or launch go untracked. The team is blindsided.

**Fix:** Revisit the map at each major phase boundary. Note what changed and why.

### Pitfall 6: Assigning Everyone to "Manage Closely"

**Symptom:** All stakeholders are rated High Influence and High Interest.

**Consequence:** The PM tries to manage every stakeholder at the same depth and exhausts themselves. Nobody is getting the right level of attention.

**Fix:** Force distribution. Reserve "manage closely" for the two to four stakeholders who genuinely require it. Everyone else gets a lighter strategy.

### Pitfall 7: Writing Engagement Strategies as Communication Schedules

**Symptom:** Every strategy reads as a cadence: "monthly update email," "weekly Slack message," "invite to demo." No strategy specifies what the stakeholder has input on.

**Consequence:** The PM manages the cadence but not the relationship. Stakeholders in "manage closely" who are never brought into actual trade-off discussions will feel sidelined and surface objections at the wrong moment.

**Fix:** For every "manage closely" and "keep satisfied" stakeholder, specify at least one type of decision they will be consulted on - not just a communication format. Example: "Involve in go/no-go discussion before framing is complete" is an engagement strategy. "Weekly update email" is not.

### Pitfall 8: AI Places Stakeholders It Has Never Met

**Symptom:** The PM pastes ten names and titles and asks the agent to place them on the power/interest grid. The grid comes back filled in.

**Consequence:** Placements rest on job titles, not on how these people actually decide. The PM manages the wrong relationships.

**Fix:** The PM places each stakeholder from what they have observed. The skill asks for the evidence behind each placement and names roles the PM may have missed.

## References

### Skill Files

- [template.md](template.md) - working scaffold
- [prompts/](prompts/README.md) - copy-paste prompt for chat-based AI tools (authored for this library; the deck has no AI page for this Play)
- [examples/sample.md](examples/sample.md) - strong, weak, and drift-bug examples

### Related Skills



### Source Material

- Source: [assets/ps_stakeholder_alignment_playbook_pages.pdf](assets/ps_stakeholder_alignment_playbook_pages.pdf)
- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 8-10: Template 02 of 24 there. No AI page for this Play; the prompts are authored for this library. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).
- Template: [template.md](template.md)
- Examples: [examples/sample.md](examples/sample.md)
- Budget data: [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)

### Adjacent Skills

- **ps-outcome-strategy-discussion** - identifies who to have the guided discussion with; the stakeholder map informs that list
- **ps-empathy-interviews** - the stakeholder map helps identify who to recruit for interviews and who to brief before fieldwork begins
- **ps-proto-persona** - the destination for customers who should not be in the stakeholder map
