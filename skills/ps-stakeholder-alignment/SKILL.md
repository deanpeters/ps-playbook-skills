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

This is the distinction that matters most. Engagement modes are not a comms schedule  -  they determine who has input on which decisions and at what depth.

- **Manage Closely** stakeholders are in the room for trade-off discussions. They have a voice in decisions, not just updates.
- **Keep Satisfied** stakeholders are briefed on outcomes and key decisions, but they are not consulted in the decision process itself. They need altitude-appropriate information, not operational depth.
- **Keep Informed** stakeholders receive regular updates but do not affect decisions. Their value is advocacy and downstream adoption, not direction-setting.
- **Monitor** stakeholders are not in the decision loop at all. Periodic check-ins prevent surprises, but they do not shape the work.

Treating all engagement as a communication cadence question misses this. A PM who sends weekly updates to all stakeholders has not done stakeholder management  -  they have sent emails. The quadrant assignment determines who the PM brings into decisions, not just who receives communications.

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

Different functions bring different priorities: legal thinks about risk, finance thinks about returns, engineering thinks about technical feasibility. Those differences create friction  -  but they do not make stakeholders adversaries.

The playbook is explicit: you may have different roles, but you are all working on the same team. A skeptical legal counsel who raises a compliance concern in week two is not an obstacle  -  they are a teammate whose input prevented a problem at launch. A finance stakeholder who pushes back on scope is not blocking the product  -  they are enforcing a constraint that is real for the business.

Approach every stakeholder as someone who shares the organization's goals, even if they express those goals differently than you do. The map is a tool for building a communication strategy across that diversity, not a list of people to manage around.

### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **critic of the stakeholder map the PM drafted**. It looks for stakeholders the PM missed, asks for the evidence behind each power and interest placement, and checks that each engagement strategy fits the quadrant. The placements and strategies stay the PM's, because only the PM knows these people.

- **Use it when:** the PM has listed stakeholders and wants the map pressure-tested for gaps and placement.
- **Avoid it when:** the request is to characterize real colleagues' motives or influence from a name and a title. The model doesn't know them. When given names and titles, first ask what the PM has observed about each person's decisions and influence, and name any roles that may be missing. Offer placements, each tagged `[AI-SUGGESTED, VALIDATE THIS]`, only if the PM then asks for a best guess.
- **Return:** missing stakeholder roles named for the PM to consider, each placement questioned against what the PM has observed, and engagement strategies checked against decision rights.

### Working With AI

The Product Manager does the thinking, and AI pressure-tests it. Critique a supplied draft against this Play before offering rewrites. Never invent customer quotes, research findings, or unsupported figures. Label inferred customer details as hypotheses, mark unknown numbers as blanks, and keep decisions with the user or team. Rehearsal is practice, not evidence. Follow this Play's specific AI boundaries below and in the Application.

### Guided Mode

When asked for guidance, when the user is unfamiliar, or when context is missing:

1. Explain the output and estimated question count. Offer Guided, Context dump, or Best guess; default to Guided and ask the first question immediately.
2. Use supplied context instead of asking again. In Context dump mode, summarize Known / Assumed / Missing / Conflicting first.
3. Ask one bolded question per turn with a progress label, three context-specific numbered recommendations, option 4 Other, and an input hint. For facts only the user can know, ask openly without suggested answers and explain why. Ground unfamiliar domain options in research when needed.
4. Adapt recommendations to the answers. Explain why a question matters when helpful.
5. Answer interruptions, honor corrections and mode switches, and stop when asked. Resume with a brief recap and the pending question.
6. Recap supplied facts, assumptions, gaps, and readiness; confirm before generating a guided artifact. When the user faces a decision, recommend an option with reasons and offer distinct alternatives. The user decides.
7. Best guess may proceed immediately: label inferred details inline and end with Assumptions to Validate, ranked by decision impact. With sufficient supplied context, execute directly.

## Application

Use [Template](#template) for the full scaffold.


### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in the critique guidance in this Play one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

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

## Template

Use this template to build a **Productside-style stakeholder map** before discovery begins.

If some stakeholders are not yet identified, note that in the Risks and Gaps section rather than leaving the table sparse. A complete map with unknowns flagged is more useful than a partial map that looks tidy.

### When to Use This

Use this during the Context phase, before empathy interviews or discovery work begins. The stakeholder map tells you who to involve, who to brief, and who to watch.

### Template

```markdown
# Stakeholder Alignment

## Context

- Initiative / product: [name]
- PM: [name]
- Date: [date]

---

## Stakeholder Table

| Name | Role / Team | Interest in This Initiative | Influence | Sentiment |
|---|---|---|---|---|
| | | | High / Medium / Low | Supportive / Neutral / Skeptical / Unknown |
| | | | High / Medium / Low | Supportive / Neutral / Skeptical / Unknown |
| | | | High / Medium / Low | Supportive / Neutral / Skeptical / Unknown |
| | | | High / Medium / Low | Supportive / Neutral / Skeptical / Unknown |
| | | | High / Medium / Low | Supportive / Neutral / Skeptical / Unknown |
| | | | High / Medium / Low | Supportive / Neutral / Skeptical / Unknown |
| | | | High / Medium / Low | Supportive / Neutral / Skeptical / Unknown |
| | | | High / Medium / Low | Supportive / Neutral / Skeptical / Unknown |

> Aim for at least 6-10 stakeholders. Include skeptics and potential blockers, not just supporters.

---

## Interest / Influence Matrix

### Manage Closely (High Influence, High Interest)
[List names]
- Engagement: [frequency and format - e.g., "weekly 1:1, shared decision log, involved in key trade-off discussions"]

### Keep Satisfied (High Influence, Low Interest)
[List names]
- Engagement: [frequency and format - e.g., "monthly executive brief, flagged when decisions affect scope or budget"]

### Keep Informed (Low Influence, High Interest)
[List names]
- Engagement: [frequency and format - e.g., "biweekly async update via shared doc or Slack, invited to demos"]

### Monitor (Low Influence, Low Interest)
[List names]
- Engagement: [frequency and format - e.g., "quarterly check-in, notified of major milestones only"]

---

## Risks and Gaps

### Missing stakeholders
[Anyone who should be here but is not yet identified]

### Potential blockers
[Stakeholders who could slow or stop progress if not engaged early]

### Political dynamics
[Relationships between stakeholders that could affect how you engage them]

---

> **Quality checks**
> - Does the stakeholder table include skeptics and blockers, not just supporters?
> - Is "influence" based on actual power over this initiative, not just seniority?
> - Are engagement strategies specific enough to act on (cadence, format, content)?
> - Is the map distinguishing stakeholders from customers? Customers belong in the persona play, not here.
> - Have you checked across legal, finance, sales, marketing, operations, and executive functions - not just engineering?

> **Capacity notes**
> - Interest description: aim for one clear sentence per stakeholder (10-15 words)
> - Engagement strategy: one to two sentences per quadrant
> - Name field: 4 words maximum
> - Role / Team field: 6 words maximum
```

### Usage Guidance

- Build this map before empathy interviews begin.
- Rate influence based on actual power over this initiative, not title alone.
- Keep stakeholders and customers separate. Customers who use the product belong in ps-proto-persona.
- Revisit this map at each major phase boundary (after framing, after discovery, before launch).
- A map with no skeptics or blockers should be treated as incomplete, not as good news.

## Examples

Illustrative and fictional, not customer evidence.

- **Strong:** For a route-optimization initiative, assess internal stakeholders' interest and influence and choose Manage Closely, Keep Satisfied, Keep Informed, or Monitor accordingly.
- **Weak:** Sending every stakeholder the same weekly update ignores differences in decision involvement.
- **Drift to avoid:** Customers as internal stakeholders: keep discovery subjects distinct from the organizational stakeholder map.


## Common Pitfalls

- **Listing Only Supporters:** Before closing the map, ask explicitly: who might push back? Who was not consulted on similar initiatives? Add them.

- **Confusing Stakeholders with Customers:** Customers who use the product in the field belong in the persona play (ps-proto-persona), not here. The stakeholder map covers people who affect the initiative organizationally. Keep these lists separate.

- **Equating Influence with Seniority:** Rate influence based on actual power over this specific initiative. Ask: can this person approve, block, accelerate, or veto the work? That is influence. Title alone is not.

- **Treating Interest and Influence as Binary:** Use Medium deliberately. Reserve High for stakeholders with genuine power or deep engagement with this initiative specifically.

- **Building the Map Once and Never Revisiting:** Revisit the map at each major phase boundary. Note what changed and why.

- **Assigning Everyone to "Manage Closely":** Force distribution. Reserve "manage closely" for the two to four stakeholders who genuinely require it. Everyone else gets a lighter strategy.

- **Writing Engagement Strategies as Communication Schedules:** For every "manage closely" and "keep satisfied" stakeholder, specify at least one type of decision they will be consulted on - not just a communication format. Example: "Involve in go/no-go discussion before framing is complete" is an engagement strategy. "Weekly update email" is not.

- **AI Places Stakeholders It Has Never Met:** The PM places each stakeholder from what they have observed. The skill asks for the evidence behind each placement and names roles the PM may have missed.

## References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-stakeholder-alignment) for supporting source material and expanded examples.
