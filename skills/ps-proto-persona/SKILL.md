---
name: ps-proto-persona
description: >-
  Create a Productside-style proto-persona for a primary user, then optionally a
  buyer persona, or review a finished research-based persona before sharing it.
  Use when you need a working customer profile before deeper validation, or
  want a persona sharpened for stakeholders, polished for a readout, or given
  more quotes.
intent: >-
  Build a Productside-style proto-persona that keeps the customer at the center,
  makes assumptions visible, and gives the team a practical profile to use in
  discovery, prioritization, and framing work until research validates it.
type: component
blueprint_stage: Discover + Investigate
best_for:
  - "Building a working customer profile before deeper research validates it"
  - "Making the target customer feel real to the team during early discovery"
  - "Identifying what still needs customer validation versus what is assumed"
  - "Reviewing a research-based persona for a stakeholder or executive readout"
scenarios:
  - "I need a working customer profile for a new product before we start interviewing"
  - "Help me build a proto-persona for our primary user so the team has a shared reference"
  - "Make this persona from our interviews ready for the exec readout"
---


## Purpose

Create a **Productside-style proto-persona** for the person your product is serving.

This skill is for the **Discover + Investigate** phase, when you need a usable customer profile before you have enough research to call it validated. It helps a Product Manager capture the person behind the segment in a way that is specific enough to guide discovery and prioritization, while staying honest about what is still assumption.

Start with the **primary user persona**. Only after that is coherent should you build the **buyer persona**.

Use this skill when you need to:

- make the target customer feel real to the team
- capture needs, pains, goals, and attitudes in one place
- keep the team from designing for an abstract segment
- identify what still needs customer validation

This is not a validated persona. Until it is grounded in research, it is explicitly a **proto-persona**.

### Usage Notes

- It starts with the **user persona** first, then optionally the buyer and influencer
- It keeps the profile explicitly **proto** until validated by research
- **Provenance tags:** every line of a working draft is tagged `[FROM YOU]`, `[RESEARCH]`, or `[AI-SUGGESTED, VALIDATE THIS]`. Invented quotes are always AI-suggested. The committed copy moves the tags out of the fields and keeps a ranked Riskiest Assumptions list.
- **Two draft paths:** beliefs or notes get drafted field by field with tags; a finished research-based persona gets reviewed against Clarity, Story, Empathy, Relevance, and Focus, and nothing is added that the research did not produce.
- **Five fields, following the B2B work-in-progress template.** The baseline's separate "What is this persona trying to do?" and "Attitudes & Influences" fields are folded in: what the persona is trying to accomplish goes under Needs | Pains, and attitudes and influences under Desired Outcomes | Goals.

## Key Concepts

### Persona vs. Proto-Persona

Productside makes an important distinction:

- **Persona**: a composite profile grounded in real customer research
- **Proto-persona**: a working profile built from limited evidence, team knowledge, and informed assumptions

If you have not validated it with customer research, call it proto.

### User First, Buyer Second

This play starts with the **user persona**.

That means the person who actually uses, experiences, or lives with the product or service. In many B2B contexts, that is not the same person as the buyer, approver, or executive sponsor.

Only after the user persona is coherent should you repeat the exercise for the buyer.

**Who owns which personas:** Product Managers focus primarily on user personas  -  the people who experience the product day-to-day. Marketing and Sales typically own buyer and influencer personas. Knowing this scopes the PM's work: go deep on the user, treat the buyer as the secondary pass.

The Playbook names three persona types:

- **User:** the person who uses the product day to day
- **Buyer:** the person who controls the budget and makes the buying decision
- **Influencer:** the person who sways the purchase or use but is not the user or buyer

### Segment vs. Persona: Build for the Center

A segment defines **who** you target, based on data. A persona brings that segment to life as **one relatable character**. Build for the center of the segment (the poster child), not a version stretched to cover everyone.

If a field starts describing everyone ("values efficiency," "wants better tools"), the persona has drifted off-center. Pull it back to the specific person at the heart of the segment.

### A Persona Is a Communication Tool

A persona's job is to help stakeholders quickly understand and empathize with the people the product serves, so they make better product decisions. Judge a finished persona by five tests:

- **Clarity:** could a busy stakeholder grasp who this person is in under a minute?
- **Story:** do the pieces add up to one believable, coherent person?
- **Empathy:** would stakeholders feel this person's goals and pains?
- **Relevance:** is it clear why this person matters to product decisions?
- **Focus:** is this the specific center of one segment, or a blurry everyone?

The bar is stakeholder empathy, not a perfect document. When a persona is fit for purpose, say so and stop polishing.

### Customer-Side, Not Product-Team-Side

The persona should usually describe the **customer-side person your product serves**, not the Product Manager building the product.

If your product truly serves Product Managers, then that can be correct. Otherwise, turning "the PM" into the default persona is a drift bug, not a shortcut.

### The Working Parts of the Productside Persona

The canonical playbook template centers on these fields:

- name and portrait
- bio and demographics
- quotes
- needs and pains (including what the persona is trying to accomplish and the behavior you observe)
- desired outcomes and goals (including their attitudes and influences)

Those fields are the working surface. They are not decoration.

The name is **alliterative**, pairing a first name with the role (Henry HR Specialist, Serena Security Officer), so the team remembers the person and the role together.

This skill follows the B2B work-in-progress template, which has five fields. The baseline template's separate "What is this persona trying to do?" and "Attitudes & Influences" fields are folded in, as the WIP instructions do: what the persona is trying to accomplish and the behavior you observe go under **Needs | Pains**; attitudes and influences go under **Desired Outcomes | Goals**.

### Proto Means Hypothesis

A proto-persona is **a hypothesis wearing a face**. It should help the team act, but it must not claim certainty it has not earned. It stays provisional until research confirms it. The moment the team treats it as settled, it stops being a proto-persona and becomes a persona profile the team has committed to.

The Playbook's discipline is to **never blur what the PM believes with what was filled in for them**. Every line of a working draft carries one provenance tag:

- `[FROM YOU]` - the PM or their stakeholders supplied it
- `[RESEARCH]` - it came from evidence (interview notes, artifacts, web research), with the source named in the trailing evidence section
- `[AI-SUGGESTED, VALIDATE THIS]` - you filled a gap; this is a guess about the customer and among the first things to test

Quotes you write are always invented. Tag them `[AI-SUGGESTED, VALIDATE THIS]` and treat them as lines to test in interviews, never as evidence. Only words a real customer said get `[RESEARCH]`.

### How AI Supports This Play

The Playbook casts AI as the **drafter of the proto-persona**. Given what the PM and their stakeholders already believe about this user, it turns those beliefs into a structured persona fast, so research starts with a target instead of a blank page. It fills gaps, but it marks every gap it filled, because those are guesses about the customer and the first things to test. What to believe, and what to test, stays the PM's call.

- **Use it when:** the work is early, before research, and the PM can name what the team already assumes about this user.
- **Avoid it when:** the PM already has real customer research (review the research-based persona instead, see [If the PM Brings a Draft](#if-the-pm-brings-a-draft)), or the proto-persona will never be validated. An untested proto-persona is just a committed stereotype. Say so if the PM has no plan to test it.
- **Return:** every line tagged by provenance, the riskiest assumptions marked to test first, and a plan to validate the profile through research.

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

Use [Template](#template) for the full scaffold.


### Required Output Convention

Default to a **clean persona artifact** that a human can use directly.

The artifact comes first. Commentary is secondary.

That means:

- fill every main section of the persona
- keep each section sized to the canonical carrying capacity
- do not add analysis, ranking, or advice before the artifact is complete

The output comes in two stages:

1. **Working draft.** Every line ends with its provenance tag (`[FROM YOU]`, `[RESEARCH]`, `[AI-SUGGESTED, VALIDATE THIS]`). Tags are the only annotation allowed inside the fields. They are short and sit at the end of the line, so the field content still fits the template.
2. **Committed copy.** Once the PM accepts the draft, offer a clean, paste-ready copy with the tags removed, followed by a short **Riskiest Assumptions** list built from the AI-suggested lines, ranked by what to test first. The tags move out of the fields, but they never disappear.

If the PM asks for a clean copy straight away, give it, but still end with the Riskiest Assumptions list.

### If the PM Brings a Draft

There are two kinds of draft. Treat them differently.

**Beliefs, notes, or a rough proto-persona** (before research). Follow the Playbook's drafting order: alliterative name, Bio & Demographics, Desired Outcomes & Goals, Needs | Pains, then Quotes. For each field, review what the PM gave you first, add only where they are thin, and tag every line. Ask one question at a time when a field is too thin to fill honestly. This mirrors the critique guidance in this Play.

**A finished, research-based persona.** Do not redraft it. This mirrors the critique guidance in this Play:

1. Ask who the stakeholder audience is if you don't know.
2. Give one honest read: is it already good enough to share? If yes, say so plainly and stop.
3. If not, work through the five tests (Clarity, Story, Empathy, Relevance, Focus) one at a time. Say what works, name the one change that would most improve it, and offer a concrete suggestion to accept, adjust, or reject.
4. Prioritize three to five changes. Name the weak spots minor enough to leave alone.
5. Sharpen wording, structure, and emphasis only. **Never add attributes, quotes, or data the research did not produce.** That includes counts and frequencies ("7 of 9 interviewees said...", "most fraud leads") unless the PM supplied them. If a count would strengthen the persona, ask the PM for it instead. When asked to add quotes to a research persona, offer only to pull real lines from the interview notes. Don't offer to write illustrative or composite quotes, even labeled.

### Canonical Capacity Rules

The canonical example page has real carrying-capacity limits. Respect them.

Use the budgets in [Template and capacity guidance](#template).

Default expectations:

- `Name & Portrait`: extremely short
- `Quotes`: a few compact quotes or quote fragments
- `Bio & Demographics`: the largest field, but still compact
- `Needs | Pains`: concise summary, not a paragraph pile, including a tight line on what they are trying to accomplish
- `Desired Outcomes | Goals`: compact future-state statements, plus short attitudes and influences

If the output would need summarizing before it can be pasted into the playbook, it is too long.

### Step 1: Confirm Who the Product Serves

Before writing anything, answer:

- what product or service are we talking about?
- who experiences the problem most directly?
- who uses the product in the field?
- is that person different from the buyer?

If you cannot answer those clearly, stop and resolve the customer-side target first.

**Guard against tech-role bias.** LLMs default heavily toward software engineers, architects,
and developers when asked about technology products. Most products - even deeply technical
ones - serve people who are not programmers. An IoT platform PM's customer is a fleet
manager, a logistics director, or a smart city program lead - not a solutions architect.
A clinical data platform PM's customer is a clinical operations lead - not a data engineer.

Before writing the persona, confirm the role by asking: does this person write code, design
systems, or architect solutions as their primary job? If the answer is no, the persona
should not read like a technologist. Pains, tools, language, and daily work should reflect
the actual role, not a developer proxy.

### Step 2: Gather Evidence Before Writing

Once you know the role and industry, offer the user two things before drafting:

1. **Web research** - offer to run a quick search for the target role in the target industry. Good sources include job postings, industry forums, trade press, day-in-the-life profiles, and professional community discussions. The goal is to replace assumptions with real language, real pain points, and real context.

2. **User-supplied artifacts** - ask whether the user has materials they want to share: interview notes, support tickets, call recordings, internal research, job descriptions, competitive intel, or anything else that would ground the persona in evidence.

Either, both, or neither is fine - the user decides. But always offer before drafting.

What to look for in web research:

- how practitioners in this role describe their own work and frustrations
- tools, systems, and workflows they mention
- organizational pressures and incentives specific to the industry
- language and jargon they actually use (not marketing language about them)
- hiring patterns that reveal what the role really does day-to-day

Feed what you find directly into the persona fields. Cite sources lightly in the trailing evidence section, not inline.

### Step 3: Build the Primary User Persona

Start with the **user persona**.

Fill all of these sections:

- `Name & Portrait`
- `Bio & Demographics`
- `Quotes`
- `Needs | Pains` (with what they are trying to accomplish and the behavior you observe)
- `Desired Outcomes | Goals` (with attitudes and influences)

Do not start with the buyer unless the buyer is also the primary user.

Do not silently skip a section because you think the persona is "already clear enough."

### Step 4: Use Real Signals Where You Have Them

Pull from any available evidence:

- interview notes
- call notes
- support themes
- field observations
- existing research
- sales or customer success insights

If you do not have direct evidence for something, avoid fake certainty. Acknowledge that in one short trailing note instead of bloating the artifact itself.

### Step 5: Give the Persona a Real Shape

The persona should feel like a person the team could recognize.

That means:

- specific enough to guide choices
- grounded in behavior, not just demographics
- written in language the customer might actually use

Weak:

- "Works in tech"
- "Needs better tools"
- "Wants productivity"

Stronger:

- "Regional operations planner responsible for keeping warehouse labor, carrier timing, and dock capacity aligned across three sites"
- "Spends two hours every shift reconciling schedule changes across email, spreadsheets, and the warehouse system"

### Step 6: Separate Pains from Goals

Do not flatten everything into one blob.

- `Needs | Pains` = friction, obstacles, frustrations, unmet needs
- `Desired Outcomes | Goals` = what better looks like for this person

This distinction matters because later Productside plays depend on it.

### Step 7: Capture Attitudes and Influences Within Goals

The WIP template asks about attitudes and influences under Desired Outcomes | Goals. They are not filler. Capture them there:

- beliefs that shape adoption
- organizational pressures
- tools or people they trust
- incentives, fears, or habits that affect behavior

### Step 8: Make Provenance and Risk Explicit

Before treating the profile as useful:

- check that every line carries a provenance tag, and that no AI-suggested line is tagged as the PM's or as research
- list the **Riskiest Assumptions**: the AI-suggested lines that would most change the persona if wrong, ranked by what to test first
- name how to validate them (who to interview, what to observe)

If you skip this, the team may treat a hypothesis as truth. Keep the trailing section concise. The tags carry most of the honesty, so the list only needs the top risks.

### Step 9: Repeat for the Buyer Only If Needed

After the user persona is coherent, you may repeat the same structure for the buyer persona.

Keep them separate if:

- one person uses the product
- another person approves the purchase
- another person influences the decision

### Step 10: Do Not Add Extra "Helpful" Commentary by Default

Do not add:

- strongest-section commentary
- ranking of pains or goals
- long caveats
- side analysis

unless the user explicitly asks for it.

The default skill output should be a persona the human can use immediately.

### Step 11: Evolve It

Personas are only helpful if the team uses and updates them.

As research progresses:

- replace assumed quotes with real ones
- refine pains and goals
- split one proto-persona into two if the segment was too broad
- retire fields that turn out to be wrong

## Template

Use this template to build a **Productside-style proto-persona** for the primary user first, then optionally the buyer.

Tag every line of the working draft with where it came from:

- `[FROM YOU]` - the PM or their stakeholders supplied it
- `[RESEARCH]` - it came from evidence; name the source under Proto-Persona Caveats
- `[AI-SUGGESTED, VALIDATE THIS]` - a filled gap; a guess to test first

Tags go at the end of the line and are the only annotation allowed inside the fields. When the PM commits the persona, the clean copy drops the tags from the fields and keeps the Riskiest Assumptions list.

### When to Use This

Use this when you need a working customer profile before full validation, and you want the team to have a shared understanding of who the product is serving.

### Template

```markdown
# Proto-Persona

## Persona Type
- User, Buyer, or Influencer:
- Validation status: Proto-persona / Validated persona
- Confidence level: Low / Medium / High

## Product Context
- Product or service:
- Problem space:
- Why this persona matters:

## Name & Portrait
- Name (alliterative, first name + role, e.g. "Henry HR Specialist"):
- Portrait description:

> Quality check: The persona should feel specific enough to remember and discuss. Avoid placeholders like "User A" unless this is a temporary working draft.

## Bio & Demographics
- Role / title:
- Industry or operating context:
- Organization context:
- Seniority or experience level:
- Relevant demographics:
- Backstory:

> Quality check: Include only demographics and background that actually help the team understand product behavior, needs, or constraints.

## Quotes
- Quote 1:
- Quote 2:
- Quote 3:

> Quality check: Quotes should reveal how this person thinks, speaks, or feels. Avoid generic lines like "I want better tools."
> Provenance check: Invented quotes are always `[AI-SUGGESTED, VALIDATE THIS]`. Only words a real customer said are `[RESEARCH]`.
> Capacity check: Keep quotes compact enough to fit the canonical quotes field.

## Needs | Pains
- Pain or need 1:
- Pain or need 2:
- Pain or need 3:
- What they are trying to accomplish, and the behavior we observe:

> Quality check: These should describe meaningful friction, unmet need, or frustration. Make them specific enough that the team can respond to them.
> Capacity check: Keep this section concise enough to paste into the canonical pain field.

## Desired Outcomes | Goals
- Desired outcome or goal 1:
- Desired outcome or goal 2:
- Desired outcome or goal 3:
- Attitudes and influences (beliefs, people and tools they trust, pressures):

> Quality check: Keep this future-state oriented. These are not tasks or features. They are the improvements this person wants in their work or life.
> Capacity check: Write compact future-state statements, not long rationale.

## Proto-Persona Caveats
- What still feels provisional:
- What should be validated next:
- Highest-priority research gaps:
- Evidence sources (for `[RESEARCH]` lines):

## Riskiest Assumptions
The AI-suggested lines that would most change this persona if wrong, ranked by what to test first.
1.
2.
3.

> Quality check: Does every line above carry a provenance tag? Is any AI-suggested line passed off as the PM's belief or as research?
> Focus check: Does this persona describe the center of one segment, or a blurry everyone?

## Buyer Relationship
- Is this person also the buyer?
- If not, who likely buys or approves?
- What tension might exist between user needs and buyer priorities?

## Research Next Steps
- Who should we interview next?
- What should we validate first?
- Which assumptions are riskiest?
```

### Usage Guidance

- Build the **user persona first**.
- Only then create a separate buyer persona if the buyer is materially different.
- Keep the proto nature explicit until research confirms the profile.
- Do not use confidential client details in examples or shareable artifacts.
- Keep provenance tags short and at the end of each line. Keep validation notes concise unless the user explicitly asks for heavier evidence annotation.
- Complete every main persona section before adding any commentary.

## Examples

Illustrative and fictional, not customer evidence.

- **Strong:** Describe the warehouse operations analyst's responsibilities, goals, pains, and workarounds, marking sourced observations separately from assumptions.
- **Weak:** "Busy professional who values efficiency" cannot guide a specific product decision.
- **Drift to avoid:** Invented authenticity: a believable customer quote or research label generated by AI is not evidence. Omit it or label it as fictional.


## Common Pitfalls

- **Making the Persona Too Generic:** Add behavioral context, concrete pains, and language that reflects how the person actually works.

- **Treating Assumptions as Research:** Tag every line of the working draft with its provenance, and end with a ranked Riskiest Assumptions list. The clean committed copy drops the tags from the fields but keeps that list.

- **Pitfall 2b: Adding Commentary That Displaces the Artifact:** Complete the artifact first. Keep commentary short and trailing.

- **Building the Buyer First:** Build the user first. Add buyer second when relevant.

- **Making the Product Manager the Persona by Default:** Ask explicitly: who experiences the product's value or pain in the field?

- **Defaulting to a Tech Role:** Ask what the customer actually does day-to-day. Most products - even deeply technical ones - serve people whose primary job is not writing code or designing systems. A fleet manager, a logistics director, a clinical operations lead, a utility substation engineer - these are the real customers. If the role does not involve building software as its core function, the persona should not read like a technologist.

- **Confusing Pains with Goals:** Keep friction separate from the future state the persona wants to achieve.

- **Never Updating the Proto-Persona:** Treat the proto-persona as a living document and revise it as discovery produces evidence.

- **Exceeding Template Capacity:** Write to the canonical budget, not to the model's appetite for prose.

- **The Assumptions Are the Model's, Not the Team's:** Review what the PM supplied before adding anything. Add only where they are thin, and tag every addition `[AI-SUGGESTED, VALIDATE THIS]`. If most of the persona is AI-suggested, say so and ask for more of the team's own beliefs before going further.

- **A Name and a Face Imply Proof:** Keep validation status visible ("Proto-persona") on the artifact. Keep invented quotes tagged as invented. Route the Riskiest Assumptions into empathy interviews (ps-empathy-interviews) before the persona is shared as a validated profile.

- **Stretching the Persona to Cover Everyone:** Build for the center of the segment. If the segment really holds two different people, split it into two personas rather than averaging them into one.

## References

Based on materials from Productside, licensed under CC BY-NC-SA 4.0 with Additional Internal Business Use Permissions. November 2026 B2B work-in-progress Playbook; not yet ratified. See the [original Play reference](https://github.com/Productside/Productside-Playbook-Skills/tree/main/reusable-agent-skills/ps-proto-persona) for supporting source material and expanded examples.
