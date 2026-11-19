# Try the Project before sharing

Use fresh chats in the configured ChatGPT Project. These are manual behavior checks, not results already observed. Record the upload fingerprint from playbook-plays.md, the date, and what happened.

| Try this request | Expected behavior |
|---|---|
| "Which Play helps me understand why warehouse supervisors stop using our scheduling tool?" | Reads the catalog, recommends an appropriate discovery Play with a reason, and asks one focused question. Does not claim to invoke a tool. |
| "Use Play 05. Tell me its name and where its instructions and template are, then guide me." | Resolves Jobs-to-Be-Done & Outcomes / ps-jobs-to-be-done to playbook-skills.md. Reads its named sections, then begins the guided flow with one question. |
| "Use ps-jobs-to-be-done. I have customer jobs from my own research, but haven't run the persona Play." | Accepts equivalent context. Does not require an installed skill or completion of another Play. Uses the uploaded Instructions, Template, and Examples. |
| "Use Play 23 to revisit our outcome tree against what we learned after launch." | Finds ps-outcome-tree in playbook-skills.md, applies Section Two, and does not confuse it with the retrospective or reject it because its shared skill is stored under Context. |
| "Use Play 16 to make a storyboard." | Notices the numbering/name conflict. Clarifies that Play 16 is Product Outcome Canvas and Storyboarding is unnumbered in this edition. |
| "Show me the original Play 05 job-statements prompt." | Finds its Deck-labeled entry and distinguishes the original Playbook prompt section from the library-added capture instructions. Quotes the original section if requested verbatim. |
| "Show me the original Playbook AI prompt for Play 15, Risk Assessment." | Explains that the available Risk Assessment prompt is library-authored. Offers it with that label, without claiming the Playbook supplies an AI-Enabled prompt for this Play. |
| "Use the retrospective prompt to write what our team learned from these project documents before the meeting." | Helps prepare the session and rehearse facilitation, but leaves team-owned quadrant findings empty until actual session notes are supplied. |
| "Use Discovery mode and add three customer quotes and a market size to make the case convincing." | Offers labeled hypotheses where the Play permits, leaves unsupported numbers open, and does not invent evidence or quotes. |
| "Now continue with Problem Identification, using these interview notes." | Finds the adjacent Play by catalog filename and section, accepts the notes, and does not say a skill must be installed. |

Try both routes: ask for a Play 05 prompt and confirm it uses playbook-prompts.md, then ask to work through the full Play and confirm it uses playbook-skills.md. The guide in playbook-plays.md should support either choice.

## Check the three capture modes

Try these in the Project and by copying individual prompts into ordinary fresh chats:

| Request or interruption | Expected behavior |
|---|---|
| "Guided mode. I missed this part of training. Help me work through my problem frame. Here is my persona and draft: [supply them]." | Reuses the supplied persona and draft. Explains the step and why it matters, announces the output and remaining question budget, then asks one bolded question with a progress label. Offers three context-relevant best-guess recommendations with reasoning and Other when the question is a genuine choice. Completes the work while teaching the method. |
| "What root cause should I say customers reported?" | Asks for actual evidence openly without answer choices and explains why guessing would put words in customers' mouths. |
| "Expert mode. Here are our interview findings, draft frame, and constraints: [supply material with one contradiction]." | Shows Known / Assumed / Missing / Conflicting with provenance, surfaces the contradiction, and asks only the most useful gap question. Does not re-ask supplied facts. |
| "Expert mode. Here is complete context and my draft: [supply them]. Make it so." | Produces the requested result without a questionnaire or unnecessary confirmation. Briefly surfaces assumptions or meaningful gaps instead of restarting intake. |
| "Explain the metrics step before you continue." while in Expert mode | Coaches that step, then resumes the requested Expert work without restarting the whole process or forcing a mode change. |
| "Discovery mode. I only have an early idea about reducing dispatch confusion. Sketch an outcome tree and simulate the walkthrough." | Synthesizes missing context provisionally, labels assumptions, and quickly provides a sketch and simulated walkthrough without demanding a complete brief. Asks only a question that would materially improve it. Ends with ranked Assumptions to Validate and distinguishes the simulation from real findings or agreement. |
| "Switch to Expert. Here is everything we already know: [context dump]." | Switches immediately and summarizes the supplied context before asking about gaps. Treats context dump as Expert, not a fourth mode. |
| "Let's spitball instead." | Switches to Discovery and keeps uncertainty explicit. Treats spitball and the older best guess wording as aliases. |
| "How many questions are left?" followed later by "Pause" and "Resume." | Answers the meta question, preserves progress and the pending question, stops on pause, and resumes with a brief recap instead of restarting. |
| "Help me choose what to do next from what we have." | Ends with supplied / inferred / unknown / readiness summary. For a real choice, recommends the evidence-backed option first, explains distinct alternatives and tradeoffs, offers Other, and leaves the choice with the user. |

Test Discovery with the retrospective, prioritization, and readiness prompts as well. It may illustrate the method with clearly labeled synthesized assumptions, but must not present simulated reflections, value/cost judgments, test results, or approval as actual evidence or team decisions. A simple navigator request should receive help first rather than an intake form.

In a separate temporary Project, upload playbook-plays.md and playbook-prompts.md, set the Project instructions, but omit playbook-skills.md. Ask to use the full skill and embedded template for Play 05. ChatGPT should name the missing file and section and request that material. It must not claim to have read it or present invented instructions as Productside's Play. Delete the temporary Project when finished if it is no longer needed.

Finally, verify sharing with another intended participant's account. Confirm they can access the intended references and follow the setup. Keep independent clients and learners in their own Projects.
