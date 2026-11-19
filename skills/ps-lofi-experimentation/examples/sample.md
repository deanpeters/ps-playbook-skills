# Lo-fi Experimentation: Examples

These examples use a B2B SaaS onboarding scenario (not HR). The product is a project management tool for small professional services firms (consultancies, agencies, law firms). The proposed solution is a guided onboarding wizard that replaces the current self-serve setup experience.

---

## Strong Example

**Why This Works:** Both assumptions are make-or-break, about customer behavior, and testable within days. The hypothesis names a specific test stimulus and a numeric threshold that can be clearly met or missed. The Decision Rule creates genuine decision points - the pivot tier has real teeth. The Experiment Description is specific enough to hand off to another person to run.

---

### Lo-fi Experimentation

**Product Context**

- Product or service: Runtrack - project management for professional services firms
- Proposed solution direction: Guided onboarding wizard that walks new accounts through workspace setup in a structured sequence rather than an open canvas
- Primary customer: Operations lead at a 10-30 person consultancy, typically the person who evaluates and sets up new software for the team

**1. Key Assumptions**

**Assumption 1:** Operations leads at small consultancies expect to complete initial workspace setup in a single session and will abandon a setup experience that requires them to return later to finish.

**Assumption 2:** When shown a step-by-step guided wizard, operations leads feel confident enough to invite team members without first consulting a support resource or watching a tutorial video.

**2. Hypothesis Statement**

Testing Assumption 1 because it is higher-impact: if ops leads abandon mid-setup, no amount of wizard polish recovers the account. Assumption 2 matters, but abandonment is the upstream risk.

**Hypothesis:**

If we walk 8 operations leads through a Concierge-facilitated simulation of the guided onboarding wizard using a screen-share and a clickable Figma prototype,

then at least 6 of the 8 (75%) will complete all four setup stages in a single session under 20 minutes without requesting to pause or return later.

**3. Design Experiment**

**Method:** Concierge session using a Figma clickable prototype. The PM plays the role of the guided wizard, narrating each step and clicking through the prototype while sharing screen with the participant. No working code required.

**Audience:** 8 operations leads recruited from current trial accounts that have not yet completed setup. Recruited via in-app message to trial users with fewer than 3 team members invited and account age under 7 days.

**Metric(s):** Completion rate - the percentage of participants who complete all four setup stages (workspace name, first project, first task template, first team member invite) within a single 20-minute session without requesting to stop or return later.

**Time Window:** 5 business days (recruit on days 1-2, run sessions on days 3-5).

**Decision Rule:**

- 75% or above (6 of 8 participants complete): continue to development with the wizard as designed
- 50% to 74% (4-5 of 8 complete): adjust - identify where participants stall, redesign those stages, and run a second experiment before development
- Below 50% (3 or fewer of 8 complete): pivot - the single-session assumption is wrong; redesign the onboarding model around save-and-return checkpoints before investing further

**4. Experiment Description**

Each session runs as a 30-minute video call. The first 5 minutes are introduction and context-setting: "You've just signed up for Runtrack for your team. I'm going to walk you through what the setup experience will look like. Please tell me what you're thinking as we go."

The PM then shares a Figma prototype and narrates each screen as if it were the wizard: "This is your workspace name screen - what would you type here?" Participants interact verbally; the PM advances the prototype.

The four stages are timed: workspace naming (target 2 min), first project creation (target 5 min), template selection (target 5 min), team member invite (target 3 min).

Session ends when the participant completes all four stages or asks to stop. Time and completion status are recorded.

**Evidence Notes**

- Upstream artifacts used: ps-solution-hypothesis output (guided wizard If/Then chain), 6 empathy interview notes from operations leads citing "confusing initial setup" as primary churn driver
- Assumption remaining untested: Assumption 2 (confidence to invite without support) - design a second Concierge session focused on the team invite stage once Assumption 1 is resolved
- Recommended next experiment: If Assumption 1 validates, run a 5-person Wizard-of-Oz test of the template selection step with real template options to test Assumption 2
- Open risk not addressed: whether the 20-minute target holds when the operations lead is interrupted mid-session (test in a later, longer-running unmoderated prototype study)

---

## Weak Example

**Why This Fails:** The assumptions read like requirements, not uncertain beliefs. Neither one would change the solution direction if false. The hypothesis has no threshold - "find it more intuitive" is not falsifiable. The Decision Rule does not have a pivot tier; all outcomes lead to continuing. The Experiment Description describes the desired product experience rather than a specific, runnable test.

---

### Lo-fi Experimentation

**Product Context**

- Product or service: Runtrack
- Proposed solution direction: Improved onboarding
- Primary customer: New users

**1. Key Assumptions**

**Assumption 1:** Users need a guided onboarding experience to get started with the product.

**Assumption 2:** The new wizard will make setup faster and easier for teams.

**2. Hypothesis Statement**

Testing Assumption 1.

**Hypothesis:**

If we build the guided onboarding wizard, then users will find it more intuitive than the current setup experience.

**3. Design Experiment**

**Method:** Show users a demo of the new wizard.

**Audience:** Some current users and potential users.

**Metric(s):** User feedback on whether the new wizard is better.

**Time Window:** Next two weeks.

**Decision Rule:**

- If feedback is positive: continue building
- If feedback is mixed: get more feedback
- If feedback is negative: get more feedback and iterate

**4. Experiment Description**

We will show users the planned onboarding wizard and explain how it will work. We will describe the four setup stages and ask them if they think it will be helpful. We will collect their impressions and use the feedback to improve the design before we build the full experience. This will help us understand whether users want a guided onboarding wizard.

---

## Drift-Bug Example: The Solution Description Bug

**Named Failure:** Solution Description Bug

**What it looks like:** The Hypothesis Statement describes what the solution does rather than what observable result will confirm or deny the assumption. The IF clause describes building or deploying the solution, not running a test. The THEN clause describes a feature outcome rather than a measurable signal.

**Example of the bug:**

> **Hypothesis:**
>
> If we build a guided onboarding wizard that walks users through workspace setup in four stages,
>
> then users will have a structured setup experience that reduces confusion and improves time-to-value.

**Why this fails:** "Builds a guided onboarding wizard" in the IF is a project milestone, not a test stimulus. "Reduces confusion and improves time-to-value" in the THEN is a description of what the solution is intended to do - not an observable, countable result. This hypothesis cannot be tested without building the product first, and it cannot be falsified even then.

**Fix:**

Identify the specific stimulus you can stage this week and the specific observable result you expect to see.

> **Corrected Hypothesis:**
>
> If we walk 8 new users through a Concierge simulation of the four-stage onboarding wizard using a Figma prototype,
>
> then at least 6 of the 8 (75%) will complete all four stages in a single session under 20 minutes without requesting help or asking to pause.

The corrected version names a test that can be run without engineering work, names a countable threshold, and can be clearly met or missed.
