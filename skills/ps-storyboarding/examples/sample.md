# Storyboarding Examples

The three examples below use a **manufacturing quality control** scenario. A PM is building a product that helps quality inspectors at a mid-size precision parts manufacturer catch and document defects before components leave the facility.

---

## Example 1 (Strong)

**Context:** Vera Martinez is a quality inspector at a contract manufacturer supplying aerospace components. The PM's product is a mobile inspection logging tool that replaces paper checklists and spreadsheet-based defect tracking. The solution hypothesis is in hand.

---

### Storyboard

**Solution Hypothesis Statement:**

IF we give quality inspectors a mobile-first logging tool that captures defect data at the point of inspection, THEN inspectors can close daily reports in under 30 minutes and defect escape rate drops below 0.5%. IF defect escape rate drops below 0.5%, THEN the facility retains its AS9100 certification and avoids the $2M annual rework cost from returned components.

---

**Three Story Elements Check**

- Character: Vera Martinez, quality inspector, aerospace components, 12 years on the floor
- Conflict: defects escape to the customer because paper logs are transcribed hours after inspection and discrepancies are caught too late to pull parts
- Resolution: mobile logging at the point of inspection closes the transcription gap and enables same-day defect review

---

**Panel 1: "Once upon a time..."**

Vera Martinez has inspected aerospace components for twelve years. She knows the tolerance specs by memory, flags the subtle surface irregularities that junior inspectors miss, and takes pride in the zero-escape months she has put together.

Visual description: Inspector with calipers at a machining floor inspection station, clipboard nearby.

---

**Panel 2: "Every day..."**

After each shift, Vera sits in the break room and transcribes her paper inspection notes into a shared spreadsheet. She works from memory and handwritten shorthand. On busy days, the notes from the morning inspection are four hours old by the time they are entered.

Visual description: Person at a breakroom table, hand-transcribing from a paper checklist into a laptop.

---

**Panel 3: "Until one day..."**

A batch of 80 precision bushings she flagged verbally at the line - but had not yet entered into the log - shipped to the airline customer before she could update the spreadsheet. The customer rejected the full shipment. The facility paid $140,000 in rework and expedite fees. The customer issued a corrective action request that put the AS9100 certification review at risk.

Visual description: Red "Customer Return - Full Batch" label on a shipping pallet; inspector looking at her notes in disbelief.

---

**Panel 4: "Because of that..."**

The operations director asked Vera to pilot a mobile inspection app that logged directly to a shared system at the moment of inspection. The first morning she used it, she flagged a surface deviation on a batch mid-line, saw it appear instantly in the shared queue, and watched the production lead pull the batch for reinspection before it moved to final assembly.

Visual description: Inspector photographing a part with a mobile device; defect flag appears in real time on a shared queue screen behind her.

---

**Panel 5: "Until finally..."**

Three weeks into the pilot, Vera submitted her end-of-shift summary from the floor in eight minutes. She felt a relief she had not expected - not just that the work was faster, but that she was no longer carrying the risk of a transcription error in her head for the rest of the day.

Visual description: Inspector walking to the parking lot at the end of shift, phone in hand, report already filed.

---

**Panel 6: "And every day after that..."**

Vera stops staying late to transcribe. Her defect logs are live as she walks the floor. The monthly quality review now uses her data directly, without a cleanup pass from the quality manager. She has trained two junior inspectors on the system and is the informal go-to for the pilot expansion across two other lines.

Visual description: Vera leading a short training huddle with two junior inspectors, each with a mobile device.

---

### Why This Works

- **Character is grounded.** Vera has a name, a role, a tenure, and a specific thing she is proud of. The reader knows her before the problem starts.
- **Conflict is specific and consequential.** Panel 3 names a dollar figure, a customer consequence, and a certification risk. Vague conflict would produce vague feedback. This panel can be tested: show it to a quality manager and ask "does this happen?"
- **Panel 4 is an experience, not a feature list.** The first thing Vera notices is what the system does for her without being asked - the part flag appearing in the shared queue. She did not configure anything.
- **Panel 5 names the emotion.** Relief. And the relief is specific: not just time saved, but the end of carrying mental risk through the day.
- **Panel 6 shows behavioral change.** Vera stops doing the late transcription. Her data is used differently. She becomes a trainer. All of this is observable and verifiable.
- **The story follows the hypothesis.** The IF/THEN statement matches the conflict in Panel 3 (transcription gap, defect escape) and the resolution in Panels 4-6 (real-time logging, same-day review, certification protection).

---

## Example 2 (Weak)

**Context:** Same scenario. Same product. Weaker execution.

---

### Storyboard

**Solution Hypothesis Statement:**

IF we improve the inspection logging process, THEN quality will be better.

---

**Three Story Elements Check**

- Character: a quality inspector
- Conflict: inefficient process
- Resolution: the new tool helps

---

**Panel 1: "Once upon a time..."**

There was a quality inspector who worked at a manufacturing facility and had been doing inspections for a long time. She was experienced and took her job seriously.

Visual description: A person at a factory.

---

**Panel 2: "Every day..."**

She followed the standard quality inspection process, which involved a lot of paperwork and manual steps. This created some inefficiencies in her workflow.

Visual description: Person doing paperwork.

---

**Panel 3: "Until one day..."**

The team started having some issues with the current quality tracking approach and it became clear that something needed to change. There were some problems with customer returns.

Visual description: A problem.

---

**Panel 4: "Because of that..."**

She started using the new mobile inspection platform, which provides real-time logging, automated defect categorization, photo documentation, bulk status updates, integration with the ERP system, and a role-based dashboard for the quality manager.

Visual description: Mobile app on a phone.

---

**Panel 5: "Until finally..."**

The new system made her work much faster and easier. She was able to complete her reports more quickly and the whole process was improved significantly.

Visual description: Happy inspector.

---

**Panel 6: "And every day after that..."**

Everything was better. The quality process was more efficient and the team was happier with the new way of working.

Visual description: Happy team.

---

### Why This Fails

- **The hypothesis is empty.** "Improve the process" and "quality will be better" are not testable claims. There is nothing to validate.
- **The character has no world.** The inspector is unnamed, her tenure is irrelevant, her pride in her work is absent. There is no one to root for.
- **Panel 2 is generic.** "A lot of paperwork and manual steps" applies to almost any back-office process. It does not ground the story in the specific friction of quality inspection.
- **Panel 3 has no stakes.** "Some issues" and "some problems" give the reader nothing to react to. A real quality manager or inspector will not recognize this as their crisis because there is no crisis.
- **Panel 4 is a feature list.** Seven product capabilities are named without any description of what the inspector experiences. The persona has disappeared from the story.
- **Panel 5 names no emotion.** "Much faster and easier" is speed, not feeling. What did she feel? When did she know it was working?
- **Panel 6 is entirely vague.** "Everything was better" and "team was happier" are not behavioral changes. This panel could be removed without losing any information.

---

## Example 3 (Drift Bug - Tech-Role Inversion)

**Context:** Same manufacturing quality control product. The PM has defaulted to a developer persona for a product that serves quality inspectors - non-technical floor staff who have never written a line of code.

---

### Storyboard

**Solution Hypothesis Statement:**

IF we build a modern API-integrated inspection logging system with a React frontend and real-time data sync, THEN developers can deploy quality tracking features faster.

---

**Three Story Elements Check**

- Character: a software developer building the quality tracking system
- Conflict: legacy codebase and manual deployment pipeline slow down feature releases
- Resolution: new platform with better developer tooling and automated CI/CD

---

**Panel 1: "Once upon a time..."**

There was a software developer at a manufacturing technology company responsible for maintaining the legacy quality management system. He spent most of his time managing technical debt, handling hotfix deployments, and trying to keep the system stable during production runs.

Visual description: Developer at a laptop with multiple terminal windows open.

---

**Panel 2: "Every day..."**

He spent two to three hours per week manually deploying updates to the QMS across fourteen factory sites. Each deployment required coordination with the on-site IT contact and a rollback procedure if something went wrong.

Visual description: Deployment pipeline diagram with multiple failure points highlighted.

---

**Panel 3: "Until one day..."**

A critical defect tracking script failed silently during a high-volume production run and no one noticed until the next morning. He spent the weekend writing a patch and coordinating emergency rollouts.

Visual description: Developer on a video call at midnight, error logs on screen.

---

**Panel 4: "Because of that..."**

He convinced his manager to approve a migration to the new platform. He set up the dev environment in four hours, connected the REST API to the existing ERP, and had the first automated test suite running by end of week.

Visual description: Clean terminal output showing all tests passing.

---

**Panel 5: "Until finally..."**

He deployed the full system to all fourteen sites in one afternoon using the automated pipeline. He closed his laptop at 5pm for the first time in three months.

Visual description: Developer leaving the office on time, laptop closed.

---

**Panel 6: "And every day after that..."**

He monitors the system from a single dashboard, deploys updates across all sites in under an hour, and spends the time he used to burn on maintenance actually building new features.

Visual description: Clean dashboard with green status indicators across all sites.

---

### What Went Wrong

This is a **tech-role inversion**. The product is a mobile inspection logging tool for quality inspectors who work on manufacturing floors. The hero of this storyboard is a software developer managing a deployment pipeline.

The developer's problems (legacy codebase, manual deployments, CI/CD friction) are real problems in their own right - but they are not the problem the product was built to solve. The product was built for Vera, not for the developer who builds the system Vera uses.

This failure has a specific trigger: when no persona is specified and the PM does not provide upstream artifacts, the default assumption tends toward the kind of person who builds software. This is the tech-role bias described in Step 1.

**How to fix it:**

1. Stop at Step 1. Ask: "Who is the product built for?" The answer is the quality inspector - the person on the floor with the calipers, not the developer in the office with the CI/CD pipeline.
2. Re-read the product description. Does it describe a tool for inspectors or a tool for developers? If it describes a tool for inspectors, the developer is an implementation concern, not the hero.
3. Rebuild the Three Story Elements check with the inspector as the character. The developer can appear in the storyboard as a supporting role if relevant, but the persona - the hero - is the person who uses the product in the field.

A storyboard built around the wrong persona cannot be validated. When you show it to quality inspectors, they will not recognize their world. When you show it to developers, they will recognize their world but have no stake in whether the inspection logging tool succeeds.
