# Empathy Interviews - Examples

## Example 1: Strong Empathy Interview Artifact

Scenario: A retail technology company building an inventory management platform for regional store managers at a mid-size grocery chain.

### Phase 1: Interview Preparation

```markdown
# Empathy Interview Preparation

## Product Context

- Product or service: StockPulse - inventory management platform for grocery retail
- Target market segment: Mid-size grocery chains (50-200 stores)
- Target interviewee role: Regional Store Manager
- Interviewee's primary job: Oversees inventory, staffing, and merchandising across 8-12 store locations

## Decision These Interviews Inform

- Decision: Whether the first release targets cross-store stockouts or weekly reconciliation
- Who makes it, and by when: Product lead and engineering lead, before Q3 planning

## Learning Objectives

1. We assume regional managers spend 3+ hours per week on manual inventory reconciliation - is that accurate?
2. We do not know how they currently handle stockouts across multiple stores - what workarounds exist?
3. We need to understand the emotional cost of shrinkage reporting to corporate leadership.
4. We need to learn what information they wish they had before their Monday morning review meetings.

## Topic Areas

| # | Topic Area | Learning Objective It Serves | Example Open-Ended Question |
|---|------------|------------------------------|-----------------------------|
| 1 | The weekly inventory rhythm | 1, 4 | "Walk me through last Monday's review." |
| 2 | Stockouts across stores | 2 | "Tell me about the last stockout that surprised you." |
| 3 | Workarounds between stores | 2 | "What have you tried when one store runs low?" |
| 4 | Reporting up to corporate | 3 | "What happens in the room when shrinkage comes up?" |

## Interview Questions

| # | Question | Follow-Up Probes | Objective |
|---|----------|-----------------|-----------|
| 1 | Can you walk me through a typical Monday morning when you're reviewing inventory across your stores? | What do you look at first? What takes the longest? | 1 |
| 2 | What are the most frustrating parts of keeping track of stock levels across multiple locations? | Can you tell me about a recent time that was especially frustrating? | 1 |
| 3 | Tell me about the last time a stockout at one of your stores caught you off guard. | What happened next? How did you find out about it? | 2 |
| 4 | How does your team currently handle moving inventory between stores when one location runs low? | Why did you end up doing it that way? Who else is involved? | 2 |
| 5 | How does shrinkage reporting affect your work and your relationship with corporate? | Can you describe what that review process feels like? | 3 |
| 6 | What information do you wish you had at the start of each week that you currently don't? | How would having that change what you do on Monday? | 4 |
| 7 | Is there anything else you'd like to share about how you manage inventory today? | | All |
```

### Phase 3: Document Findings (after interview)

```markdown
# Empathy Interview Findings

## Interview Context

- Interviewee role: Regional Store Manager (oversees 10 stores, Southeast region)
- Date: 2026-06-18
- Interview duration: 45 minutes
- Product context: StockPulse inventory management platform
- Interviewer(s): PM (lead), UX Designer (notes)

## Raw Quotes

| # | Quote |
|---|-------|
| 1 | "By the time I find out a store is out of something, a customer has already complained to corporate." |
| 2 | "I spend my Monday mornings calling store managers one by one to piece together what happened over the weekend." |
| 3 | "The shrinkage report is the thing I dread most - it feels like I'm always defending numbers I can't fully explain." |
| 4 | "We move product between stores in the back of someone's personal truck. It works, but it's not exactly a system." |
| 5 | "I wish I could see on Sunday night what's going to be a problem on Monday morning." |

## Findings Board

### Jobs-to-Be-Done

| # | Job (Functional / Emotional / Social) |
|---|---------------------------------------|
| 1 | [F] Reconcile inventory across 10 store locations weekly |
| 2 | [F] Redistribute stock between stores before stockouts hit |
| 3 | [F] Prepare shrinkage explanations for corporate review |
| 4 | [E] Feel prepared before Monday morning inventory reviews |
| 5 | [E] Feel in control of stock levels across the region |
| 6 | [S] Be seen as reliable by corporate leadership on loss prevention |

### Desired Outcomes

| # | Desired Outcome |
|---|-----------------|
| 1 | Reduce time spent reconciling inventory data across store locations |
| 2 | Reduce frequency of stockouts discovered by customer complaints |
| 3 | Increase confidence in shrinkage numbers before corporate reviews |
| 4 | Minimize manual coordination for cross-store inventory transfers |

### Problems

| # | Problem |
|---|---------|
| 1 | No visibility into store-level stock until Monday phone calls |
| 2 | Stockouts discovered reactively through customer complaints to corporate |
| 3 | Cross-store transfers are informal and untracked |
| 4 | Shrinkage numbers require manual reconciliation with no audit trail |
| 5 | Weekend inventory changes are invisible until Monday morning |

### Feels / Appears

| # | Observation |
|---|-------------|
| 1 | Appears anxious about Monday morning reviews |
| 2 | Feels exposed when presenting shrinkage data to corporate |
| 3 | Seems resigned to informal transfer workarounds |
| 4 | Feels pride in knowing each store manager personally |

## Key Insights

- What surprised you: The informal truck-based transfer system - nobody tracks cross-store moves, which contaminates shrinkage data.
- What confirmed prior assumptions: Manual reconciliation time is real (estimated 3-4 hours/week, consistent with our assumption).
- What contradicted prior assumptions: We assumed stockouts were the primary pain; shrinkage reporting and the associated corporate pressure is the bigger emotional burden.
- What needs more interviews to validate: Whether the informal transfer problem is unique to this region or systemic across the chain.

## Evidence Notes

- What is well-supported: Jobs 1-3, Problems 1-4 - directly from the interviewee's own stories and language.
- What is still a single data point: Social job (6) is inferred from tone when discussing corporate reviews, not stated directly.
- Recommended next steps: Interview a Store Manager (individual contributor level) to understand the other side of the Monday phone calls. Interview a corporate loss prevention lead to understand their perspective on shrinkage reports.
```

### Why This Works

- **A decision sits behind the whole guide.** The team named what the interviews must decide (stockouts or reconciliation first), so every learning objective has a reason to exist.
- **Learning objectives drove the questions.** Each question names the objective it serves, and the topic areas let the interviewee steer within them. The PM did not ask random "tell me about your day" questions.
- **Questions are open-ended and product-neutral.** No mention of StockPulse, dashboards, or features. Every question explores the customer's current reality.
- **Follow-up probes dig deeper.** "Can you tell me about a recent time?" and "What happened next?" get past surface-level answers.
- **Findings use real customer language.** The raw quotes capture how the customer actually talks about their work ("piece together what happened," "back of someone's personal truck"). This language is gold for the team.
- **The findings board is structured and sized for the template.** Jobs are 6-8 words. Problems are 8-12 words. Outcomes use Direction + Metric + Context. Everything is paste-ready.
- **Surprises are highlighted.** The most valuable finding - that shrinkage reporting is a bigger emotional burden than stockouts - contradicted the team's assumption. That is exactly what empathy interviews are for.
- **Evidence notes are honest.** They distinguish what came from the customer directly from what was inferred.

---

## Example 2: Weak Generic Artifact

Same scenario, written poorly.

### Phase 1: Interview Preparation (Weak)

```markdown
# Empathy Interview Preparation

## Product Context

- Product or service: Inventory management tool
- Target market segment: Grocery
- Target interviewee role: Manager
- Interviewee's primary job: Manages inventory

## Learning Objectives

(none defined)

## Interview Questions

| # | Question | Follow-Up Probes |
|---|----------|-----------------|
| 1 | Tell me about your day. | |
| 2 | What challenges do you face? | |
| 3 | How do you manage inventory? | |
| 4 | Is the current process slow? | |
| 5 | Do you like your current tools? | |
```

### Phase 3: Document Findings (Weak)

```markdown
# Empathy Interview Findings

## Interview Context

- Interviewee role: Manager
- Date: Last week
- Interview duration: 20 minutes

## Raw Quotes

(none captured)

## Findings

The manager said inventory is hard and takes a lot of time. They don't like the current system. They want something better and more automated. They feel stressed about reporting. The process is manual and could be improved with technology.
```

### Why This Fails

- **No learning objectives.** The PM went in without knowing what they needed to learn, so the questions wander aimlessly.
- **Questions are too vague.** "Tell me about your day" and "What challenges do you face?" are so broad they produce shallow answers. The PM learns nothing specific.
- **Two questions are yes/no.** "Is the current process slow?" gets "yes." "Do you like your current tools?" gets "not really." Neither produces actionable insight.
- **No follow-up probes.** Every question is a dead end. When the customer gives a surface answer, there is no path to dig deeper.
- **No raw quotes captured.** The team has no evidence - only the PM's memory, which will fade within days.
- **Findings are unstructured prose.** A wall of text that mixes observations, assumptions, and the PM's own opinions. No way to feed this into downstream skills (JTBD, problem identification).
- **Product context is vague.** "Manager" of what? "Grocery" at what scale? Without specificity, the questions cannot be tailored.
- **20-minute interview.** Barely enough time to get past warm-up. Real empathy interviews need 30-60 minutes.

---

## Example 3: Bias Bug - Leading Questions That Poison the Well

```markdown
## Interview Questions

| # | Question | Follow-Up Probes |
|---|----------|-----------------|
| 1 | How would you feel about a dashboard that shows real-time inventory across all your stores? | Would that save you time? |
| 2 | Don't you think automated alerts for low stock would help you respond faster? | How much time do you think that would save? |
| 3 | Our platform can predict stockouts 48 hours in advance - would that be valuable to you? | Would you pay for that feature? |
| 4 | If you could see shrinkage data in real-time, wouldn't that make your corporate reviews easier? | |
| 5 | Would you prefer a mobile app or a desktop tool for tracking inventory? | |
```

### Why This Is Wrong

Every question tells the customer what the "right" answer is:

- **"How would you feel about a dashboard..."** - This is pitching, not interviewing. The customer is now evaluating your solution idea instead of describing their problem. They will say "that sounds great" because it costs them nothing to be agreeable.
- **"Don't you think automated alerts would help..."** - A leading question with the answer embedded. "Don't you think" almost always produces "yes." The PM learns nothing except that customers are polite.
- **"Our platform can predict stockouts..."** - The PM is demonstrating the product during a discovery interview. The customer is now reacting to a feature pitch instead of sharing their experience. This is the opposite of empathy.
- **"Wouldn't that make your corporate reviews easier?"** - The question assumes the current reviews are hard (which may be true, but the customer should say so unprompted) and frames the solution as the answer.
- **"Would you prefer mobile or desktop?"** - A false binary that skips the real question: how and where do they actually manage inventory today? The answer to "mobile or desktop" tells you nothing about their workflow.

**The damage:** The PM leaves this interview believing they have validated their product concept. They have not. They have confirmed that customers are agreeable when presented with solutions that sound plausible. Every finding from this interview is contaminated by the framing of the questions.

**The fix:** Strip every question of product references, feature descriptions, and implied answers. Ask about the customer's current reality:

| Biased Version | Neutral Version |
|----------------|-----------------|
| "How would you feel about a real-time dashboard?" | "How do you currently check stock levels across your stores?" |
| "Don't you think automated alerts would help?" | "Tell me about the last time a stockout caught you off guard." |
| "Our platform can predict stockouts..." | "What signals tell you a store might run low on something?" |
| "Wouldn't real-time shrinkage data make reviews easier?" | "Can you walk me through your last shrinkage review with corporate?" |
| "Would you prefer mobile or desktop?" | "Where are you when you need to check inventory? What do you use?" |
