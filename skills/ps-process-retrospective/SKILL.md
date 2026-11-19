---
name: ps-process-retrospective
description: >-
  Help a PM prepare for, facilitate documentation of, and close out a team
  retrospective using the Productside nautical four-quadrant model. Use when a
  team needs to reflect on a completed phase, sprint, launch, or project and
  produce concrete action items.
intent: >-
  Help a Product Manager structure and document a team retrospective that
  surfaces honest reflection on what worked, what did not, where the team is
  headed, and what obstacles lie ahead. The agent sets up and documents; the
  team runs the session. Psychological safety is the prerequisite; action items
  with owners and dates are the deliverable.
type: process
blueprint_stage: Deliver
best_for:
  - "Preparing and documenting a structured team reflection session"
  - "Capturing what went well, what failed, and what the team is aiming for next"
  - "Building a continuous improvement habit tied to the Productside lifecycle"
scenarios:
  - "We just finished a product cycle and I need to prepare a team retrospective"
  - "Help me document what went well, what failed, and our action items from the retro session"
---

## Purpose

Create a **Productside-style Process Retrospective artifact** from a structured team reflection session.

This is a process skill. The agent helps the PM prepare the session (roster, context, discussion prompts) and document the results after the team meets. The team itself surfaces what went well, what failed, what they are aiming for, and what they are worried about. The agent cannot substitute for that conversation.

This play reviews the **PM process itself** - how the team conducted discovery, framing, validation, and launch - not just what shipped or what engineering delivered. Wind and Anchors items should surface PM-process observations: "Discovery closed before enough customer interviews ran." "Problem statement was not validated with the team before framing began." "The outcome roadmap was never updated after the storyboard changed." These are the items that make a PM-process retrospective distinct from a generic team debrief.

The playbook is direct on two points. First: "Skipping retrospectives reduces the ability for teams to get better together." Second: "Create a safe space for admitting mistakes and learning from failure. Harnessing a growth mindset on the team is the only way to benefit from retros." Both of these are prerequisites, not afterthoughts. A retro run without psychological safety will not surface anything honest. A retro without action items is just a meeting.

Use this skill when you need to:

- close out a phase, launch, or discovery cycle with structured team reflection
- surface what the team learned and what to carry forward
- generate concrete action items with named owners before the next phase starts
- create an honest record of what worked and what failed in the PM process

This is not a software sprint retrospective. The standard agile format (What Went Well / What Didn't / What to Try Next) is a different structure with a different scope. The Productside model uses four named quadrants with a nautical metaphor, reviews the PM process not just delivery outputs, and requires action items with specific owners and dates. If you are running a sprint ceremony, this is the wrong play.

## Key Concepts

### The Four-Quadrant Nautical Model

The retrospective is organized around a sailboat illustration that divides the canvas into four quadrants:

**Wind in Our Sails** (upper-left) - past-facing, positive. What has helped the team move forward? What has been successful? What has excited or motivated the team? Items here are honest wins and momentum.

**Beacons on the Horizon** (upper-right) - future-facing, positive. What milestones can the team work toward? What goals are within reach? What can the team get excited about? Items here are forward-looking aspirations and near-term anchors.

**Anchors Holding Us Back** (lower-left) - past-facing, problems. What has dragged the team down? What has prevented progress? When did the team fail or flounder? Items here name specific system and process failures - not individuals.

**Barriers We See Ahead** (lower-right) - future-facing, problems. What will the team need to navigate around? Where might the team get stuck? What problems are likely to get worse? Items here are anticipated obstacles that warrant planning now.

### The Two Axes

- **Left vs. right**: left quadrants are retrospective (what happened); right quadrants are prospective (what is coming). They require different conversations and different mindsets.
- **Upper vs. lower**: upper quadrants are positive (what is helping and where we are headed); lower quadrants are problems (what is hindering and what lies ahead). Both halves are required.

### Psychological Safety

Without it, the Anchors quadrant will stay empty or fill with safe abstractions. The team will perform positivity instead of reflection. The PM's job before the session is to create conditions where it is safe to name failures honestly - by name, specifically, without blame attaching to individuals.

The Anchors quadrant is the highest-signal quadrant. If it is empty or vague, the retro has not done its job.

### The Retrospective Builds Team Communication and Trust

The immediate output of a retro is a set of action items. The downstream output is a team that communicates better and trusts each other more.

When team members share their honest experience — what frustrated them, what they got wrong, where the process broke — and the team responds with curiosity instead of defensiveness, trust deepens. Engineers who hear the PM name a process failure, designers who hear that a handoff gap hurt the team, cross-functional partners who see that honest reflection is expected here — the retro is the practice that makes this kind of candor normal.

Teams that skip retros lose this mechanism. The frustrations remain; the shared understanding that comes from naming them together does not develop. "Skipping retrospectives reduces the ability for teams to get better together" — not only because the action items are lost, but because the communication habit that produces them is what builds the team over time.

### Items Are Sticky-Note Sized

Each quadrant contains short, specific items - 5 to 8 words each. Not paragraphs. Not explanations. "Deployment review had no rollback criteria" is a good item. "Our deployment processes were sometimes inadequate for the complexity of releases" is not. Specificity is the point.

### Action Items Are the Artifact That Matters

A retro without action items is venting, not improvement. Action items must have:
- An owner (a named person, not "the team" or "engineering")
- A specific action (not "improve communication")
- A date (by when, specifically)

The format is: [Owner] will [action] by [date].

### Phase Agnosticism

Retrospectives are not only for the end of a project. They can and should run at the end of any phase, sprint, launch, or cycle. The skill works for all of these.

### How AI Supports This Play

This Play has no AI page in the B2B work-in-progress deck. This guidance applies the deck's global rule (the PM does the thinking, AI pressure-tests it) to this Play. Here AI works as a **facilitation coach before the session and recorder after it**. It helps the PM prepare quadrant prompts and protect psychological safety, then turns the team's own items into specific, owned action items. The items come from the team; the agent never writes what the team experienced.

- **Use it when:** the PM is preparing to run a retrospective, or has the team's raw items to organize into action items.
- **Avoid it when:** the request is to write the team's Wind, Anchors, Beacons, or Barriers without a session.
- **Return:** discussion prompts for each quadrant, moves that keep the room safe, and action items with an owner and a date, built only from the team's items.

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

See the source play pages in [assets/ps_process_retrospective_playbook_pages.pdf](assets/ps_process_retrospective_playbook_pages.pdf).

### If the PM Brings a Draft

When the PM arrives with a draft (or, for a session-based Play, with notes from the session), review it before writing anything new. Work through the checks in [prompts/01-prepare-and-close-retro.md](prompts/01-prepare-and-close-retro.md) one at a time, quote the words at fault, and offer rewrites last, as options to accept, adapt, or reject. If the PM asks you to draft instead, or chooses best guess mode, tag what you supply `[AI-SUGGESTED, VALIDATE THIS]` and never invent evidence, data, or what other people said. Numbers stay the PM's even then: leave every target, threshold, baseline, and rating as `[PM TO SET]` with a note on what evidence would anchor it.

### Step 1: Confirm Scope and Timeframe

Before any setup, confirm:

- What product, project, feature, or sprint is this retro reviewing?
- What time period does it cover (start date to end date)?
- Is this a phase-end retro, a sprint retro, a post-launch retro, or something else?
- Has the work being reviewed concluded, or is it still in flight?

This grounds every subsequent step. A retro for a two-week sprint looks different from a retro for a six-month launch.

### Step 2: Set Up the Administrative Section

Fill in the left sidebar:

- **Retrospective for**: the product, project, or feature being reviewed (3-8 words)
- **Date**: the date the session will be or was held
- **Point of Contact roster**: the team roles and their owners. Standard roles include Project Manager, Executive Sponsor, Product Manager, Sales, Marketing, Communications, Operations, Customer Support, Release Engineer, and Legal. Add or remove rows to match the actual team. Each row captures: Role | Name and Title | Other (additional context).

Do not leave the roster blank. Part of the retro's value is that the right people are in the room. An empty roster means no one has decided who those people are.

### Step 3: Prepare Discussion Prompts for Each Quadrant

Offer the team the three guiding questions for each quadrant. These are not a rigid script - they are entry points.

**Wind in Our Sails:**
- What has helped us move forward?
- What has been successful so far?
- What has excited or motivated us?

**Beacons on the Horizon:**
- What milestones can we work toward?
- What goals do we have?
- What can we get excited about?

**Anchors Holding Us Back:**
- What is dragging us down?
- What has kept us from making progress?
- When did we fail or flounder?

**Barriers We See Ahead:**
- What will we need to navigate around?
- Where might we get stuck?
- What problems might get worse?

Share these prompts with the PM so they can prime the discussion or use them as facilitation aids in the session.

### Step 4: Provide Note-Taking Guidance

Before the session, brief the PM on item quality:

- Items should be short, honest, and specific - 5 to 8 words each.
- Name the concrete thing, not the abstract category. "Weekly standup ran over 30 minutes and blocked engineering time" is useful. "Communication was poor" is not.
- Items in the Anchors quadrant should name process and system failures, not individuals. "Deployment checklist was not followed for the Oct 3 release" is right. "Alex did not follow the process" is not.
- Both positive and negative quadrants need real content. A full Wind in Our Sails and an empty Anchors is a sign of a safety problem, not a good project.

### Step 5: Team Runs the Session

This step belongs to the team. The agent pauses here.

The PM facilitates the session, collects items in each quadrant, and captures raw notes. When the session is complete, the PM returns with the raw output and the agent picks up documentation from Step 6.

Offer this handoff explicitly: "Ready to help document the results when the session is done. Share the raw notes from each quadrant when you are back."

### Step 6: Record Wind in Our Sails Items

From the session output, record 3-5 specific items from the Wind in Our Sails quadrant. Keep each item to 5-8 words. If the raw notes are longer, help the PM compress them without losing the specific observation.

### Step 7: Record Anchors Holding Us Back Items

From the session output, record 3-5 specific items from the Anchors quadrant. This is the highest-priority documentation step.

If the team's Anchors items are vague ("things were hard sometimes"), flag this before recording. Offer to help the PM work backward to the specific observation: "What specifically was hard? What did 'hard' look like in practice?"

Ensure no item names an individual. If a raw item does, help the PM reframe it toward the system or process: "The approval process requires a 5-day wait with no parallel path" instead of "Jim takes too long to approve things."

### Step 8: Record Beacons on the Horizon Items

From the session output, record 3-5 items from the Beacons quadrant. If Beacons is empty, prompt the PM: "Did the team surface any goals or milestones they are excited about? Even rough ones count here." A team with no Beacons has no positive forward momentum - that is worth naming.

### Step 9: Record Barriers We See Ahead Items

From the session output, record 3-5 items from the Barriers quadrant. Note the difference from Anchors: Barriers are anticipated future problems, not past ones. They call for planning, not postmortem.

If items bleed between Anchors (past) and Barriers (future), help the PM sort them. The same root cause can generate both: an Anchor is the past occurrence, a Barrier is the recurrence risk.

### Step 10: Formulate Action Items

For each Anchor and each Barrier that has a concrete next step, draft an action item. Format: [Owner] will [specific action] by [date].

- Owner must be a named individual, not "the team" or "PM" as a generic.
- Action must be specific enough to verify completion. "Improve the deployment process" is not an action. "Priya will add a rollback checklist to the deployment runbook by Nov 1" is.
- Date must be real. If the PM does not have a date, prompt for one: "What is a realistic deadline for this given the current sprint?"

Produce 1-3 action items minimum. If the team surfaced 5+ Anchors and Barriers but produced 0 action items, something has gone wrong - name that.

### Step 11: Offer Next Steps

After completing the documented artifact, offer:

1. Share the completed retro with the full team for review - the people in the room should see the documented output before it is filed.
2. Schedule a follow-up check-in at the next logical milestone to review action item progress. A retro with no follow-up is a filing exercise.
3. Note whether any Barriers identified here should feed into a risk assessment (ps-risk-assessment) if they are significant enough to warrant formal mitigation and contingency planning.

## Examples

See [examples/sample.md](examples/sample.md).

The example set includes:

- a strong field service dispatch retro with a complete roster, all four quadrants filled with specific items, and owner-dated action items
- a weak version of the same scenario where Anchors is vague, Beacons is empty, and action items lack owners and dates
- a drift-bug example where the PM asks the agent to fill in the quadrants from the project description, and the agent correctly names the process skill boundary and offers to help structure the session instead

## Common Pitfalls

### Pitfall 1: Running the Retro Without Psychological Safety

**Symptom:** The Anchors quadrant contains 0-1 items, or contains only safe abstractions ("some things could have gone better"). Wind in Our Sails is full.

**Consequence:** The team has performed a celebration instead of a retrospective. Real failures go unnamed, repeat in the next cycle, and accumulate.

**Fix:** Before the session, the PM should explicitly frame it as a safe space for naming mistakes. The Anchors quadrant is the measure of whether the safety worked. If it is empty, the session should be reconvened with a different frame - or the underlying safety issues should be addressed before trying again.

### Pitfall 2: Items Written as Abstractions Instead of Observations

**Symptom:** Items read as categories: "Communication was bad," "Process was unclear," "Team was misaligned."

**Consequence:** Abstract items cannot be acted on. They produce abstract action items ("improve communication") that no one can verify or close.

**Fix:** Push to the specific observation. "Design review was scheduled with 2 hours notice three times in October" is actionable. "Communication was bad" is not. For every abstract item, ask: what specifically happened? When? What was the concrete effect?

### Pitfall 3: Action Items Without Owners or Dates

**Symptom:** Action items read as intentions: "We will improve our release process," "Team will communicate more proactively."

**Consequence:** No one is accountable. No one knows when it should be done. The action items are aspirations, not commitments. They will not be completed.

**Fix:** Every action item requires a named owner and a specific date. The format is: [Owner] will [specific action] by [date]. If either is missing, the item is not yet an action item.

### Pitfall 4: Only the PM Fills In the Template

**Symptom:** The PM writes all four quadrants alone, based on their own memory of the project.

**Consequence:** A solo retro is a journal entry. It misses the perspectives of the people who did the work - engineering, support, sales - and produces a skewed picture that reflects the PM's vantage point, not the team's.

**Fix:** The retro must involve the team. The PM can prepare the template and prompts alone (Steps 1-4 above). The content must come from the session. If a live session is not possible, the PM can collect async input from each team member and synthesize it - but solo input is a fallback, not the default.

### Pitfall 5: Conflating Anchors and Barriers

**Symptom:** Past failures appear in the Barriers quadrant. Future risks appear in the Anchors quadrant. Or the two quadrants contain the same items.

**Consequence:** The team does not distinguish between fixing what already happened and preventing what has not happened yet. The two require different responses - postmortem versus risk planning.

**Fix:** Anchors = what happened in the past that hurt us. Barriers = what we anticipate could hurt us in the future. The same root cause can generate both. Help the team make the cut explicitly: "Was this something that happened, or something you are worried might happen?"

### Pitfall 6: Filing the Output Without Following Up on Action Items

**Symptom:** The retro is documented, shared, and then nothing happens. At the next retro, the same action items appear again.

**Consequence:** The team learns that retros produce documentation, not change. Participation and honesty decline in subsequent sessions.

**Fix:** Schedule a check-in at the next milestone to review action item status. Ask whether each item was completed, deferred, or dropped - and why. A retro that generates the same action items twice in a row is a signal that either the action items were not specific enough, or the follow-up structure is broken.

### Pitfall 7: Skipping the Beacons Quadrant

**Symptom:** Wind in Our Sails is complete (what worked), Anchors is complete (what failed), Barriers is complete (future risks) - but Beacons is left blank or has one generic item ("ship the next release").

**Consequence:** The team ends the session with a clear picture of what went wrong and what problems are coming, but no positive forward pull. Retros that only surface problems without naming aspirations can leave teams demoralized.

**Fix:** Beacons do not have to be ambitious. Near-term milestones, small wins the team is looking forward to, a specific deliverable they are excited about - all count. Push the PM to ask the team: "What is something in the next cycle we can look forward to?"

### Pitfall 8: Making It a Blame Session

**Symptom:** Anchors items name individuals: "Jordan was late on deliverables," "The dev team did not communicate," "Sarah dropped the ball on the handoff."

**Consequence:** The person named becomes defensive. Others protect themselves in future retros. The team learns that Anchors is a place where people get blamed, so they stop contributing to it honestly.

**Fix:** Anchors should name system and process failures, not individuals. "The handoff checklist did not include a sign-off step for the receiving team" names the process gap. "The delivery window was set without engineering input" names the planning failure. Help the PM reframe individual-blame items toward the systemic cause before documenting them.

### Pitfall 9: A Retrospective Without the Team

**Symptom:** The PM asks the agent to "fill in the retro for last sprint" and gets plausible items in all four quadrants.

**Consequence:** The team's real anchors stay unspoken, and the action items fix problems nobody named. The retro's main value, team trust, never happens.

**Fix:** Prepare the session; record only the team's items. Turn them into action items with an owner and a date.

## References

### Skill Files

- [template.md](template.md) - working scaffold
- [prompts/](prompts/README.md) - copy-paste prompt for chat-based AI tools (authored for this library; the deck has no AI page for this Play)
- [examples/sample.md](examples/sample.md) - strong, weak, and drift-bug examples

### Related Skills

- **Downstream:** ps-risk-assessment: significant Barriers identified in the retro may be candidates for formal risk assessment and mitigation planning
- **This skill is phase-agnostic:** it does not require upstream skills and can be run at any point in the product lifecycle

### Project Docs

- [technical/data/canonical_template_budgets.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/canonical_template_budgets.yaml)
- [informative-documents/framework-glossary.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/framework-glossary.md)
- [informative-documents/skill-dependency-map.md](https://github.com/Productside/Productside-Playbook-Skills/blob/main/docs/skill-dependency-map.md)

### Source Material

- [assets/ps_process_retrospective_playbook_pages.pdf](assets/ps_process_retrospective_playbook_pages.pdf)
- B2B work-in-progress deck (`wip-b2b-2026-11`), slides 109-111: Template 24 of 24 there. No AI page for this Play; the prompts are authored for this library. Not yet ratified. See [technical/data/source_versions.yaml](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml).
- [Baseline Playbook version](https://github.com/Productside/Productside-Playbook-Skills/blob/main/technical/data/source_versions.yaml). Full source PDF supplied separately.
- Productside Playbook companion document (supplied separately)
