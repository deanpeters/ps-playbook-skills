# Skills

A skill gives your AI assistant instructions for working through a Productside Playbook Play with you. Choose one below. Each Play folder contains only `SKILL.md`, with instructions, a working template, compact examples, and quality checks in that file.

For a chat, attach the chosen Play's `SKILL.md`, then describe your product and the help you need. Ask: "Walk me through this one question at a time."

For an agent tool that supports skill folders, use the complete `psk-...` folder and follow that tool's installation instructions.

Every skill supports **Guided** (learn and complete the work step by step, with context-relevant recommendations), **Expert** (bring context and get the result, with guidance on any step when needed), and **Discovery** (synthesize missing context and quickly sketch or simulate a walkthrough). The assistant reuses supplied context and hands decisions back to you. Discovery assumptions stay labeled; this interaction mode is distinct from the Blueprint's Discover phases and does not claim research was conducted.

```mermaid
flowchart TD
    M{"How would you like to work?"}
    M --> G["Guided<br/>Learn and complete each step"]
    M --> E["Expert<br/>Bring context and get the result"]
    M --> D["Discovery<br/>Sketch with synthesized assumptions"]
    E -->|Help on one step| H["Get coaching on that step"]
    H -->|Resume| E
    G --> R["Review the result<br/>and decide what to keep"]
    E --> R
    D --> R

    classDef mode fill:#eef2ff,stroke:#4f46e5,color:#111827
    class G,E,D mode
```

Switch modes when needed; keep the context already supplied. A Discovery result remains provisional until its assumptions are validated.

For copy-and-paste prompts, use the separate [prompt collection](../prompts/README.md). No prompts or source PDFs are duplicated inside the skill folders.

25 skills cover all 24 numbered Plays, plus a Blueprint navigator and Storyboarding. The Outcome Tree covers two numbered Plays. Numbers follow the November 2026 B2B work-in-progress Playbook, which is not yet ratified.

### Navigator (cross-phase)

| Directory | Template | Type |
|---|---|---|
| [psk-blueprint-advisor](psk-blueprint-advisor/SKILL.md) | Blueprint (pages 1-3) | process |

### Context

| Directory | Template | Type |
|---|---|---|
| [psk-outcome-strategy-discussion](psk-outcome-strategy-discussion/SKILL.md) | 01 | process |
| [psk-stakeholder-alignment](psk-stakeholder-alignment/SKILL.md) | 02 | component |
| [psk-outcome-tree](psk-outcome-tree/SKILL.md) | 03 + 23 | component |
| [psk-market-selection-sizing](psk-market-selection-sizing/SKILL.md) | 04 | component |

### Discover + Investigate

| Directory | Template | Type |
|---|---|---|
| [psk-jobs-to-be-done](psk-jobs-to-be-done/SKILL.md) | 05 | component |
| [psk-proto-persona](psk-proto-persona/SKILL.md) | 06 | component |
| [psk-empathy-interviews](psk-empathy-interviews/SKILL.md) | 07 | process |
| [psk-affinity-mapping](psk-affinity-mapping/SKILL.md) | 08 | process |
| [psk-problem-identification](psk-problem-identification/SKILL.md) | 09 | component |
| [psk-framing-the-problem](psk-framing-the-problem/SKILL.md) | 10 | component |

### Discover + Define

| Directory | Template | Type |
|---|---|---|
| [psk-exploring-solution-space](psk-exploring-solution-space/SKILL.md) | 11 | process |
| [psk-solution-hypothesis](psk-solution-hypothesis/SKILL.md) | 12 | component |
| [psk-positioning-statement](psk-positioning-statement/SKILL.md) | 13 | component |
| [psk-lofi-experimentation](psk-lofi-experimentation/SKILL.md) | 14 | component |
| [psk-storyboarding](psk-storyboarding/SKILL.md) | none (instruction page only) | component |
| [psk-risk-assessment](psk-risk-assessment/SKILL.md) | 15 | component |
| [psk-product-outcome-canvas](psk-product-outcome-canvas/SKILL.md) | 16 | component |

### Create

| Directory | Template | Type |
|---|---|---|
| [psk-outcome-roadmap](psk-outcome-roadmap/SKILL.md) | 17 | component |
| [psk-tiny-acts-discovery](psk-tiny-acts-discovery/SKILL.md) | 18 | process |
| [psk-output-prioritization](psk-output-prioritization/SKILL.md) | 19 | component |
| [psk-go-to-market](psk-go-to-market/SKILL.md) | 20 | component |
| [psk-product-readiness](psk-product-readiness/SKILL.md) | 21 | component |

### Deliver

| Directory | Template | Type |
|---|---|---|
| [psk-measuring-outcomes](psk-measuring-outcomes/SKILL.md) | 22 | component |
| [psk-process-retrospective](psk-process-retrospective/SKILL.md) | 24 | process |
