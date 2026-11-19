# Try the Project before sharing

Use fresh chats in the configured ChatGPT Project. These are manual behavior checks, not results already observed. Record the upload fingerprint from playbook-plays.md, the date, and what happened.

| Try this request | Expected behavior |
|---|---|
| "Which Play helps me understand why warehouse supervisors stop using our scheduling tool?" | Reads the catalog, recommends an appropriate discovery Play with a reason, and asks one focused question. Does not claim to invoke a tool. |
| "Use Play 05. Tell me its name and where its instructions and template are, then guide me." | Resolves Jobs-to-Be-Done & Outcomes / ps-jobs-to-be-done to playbook-skills.md. Reads its named sections, then begins the guided flow with one question. |
| "Use ps-jobs-to-be-done. I have customer jobs from my own research, but haven't run the persona Play." | Accepts equivalent context. Does not require an installed skill or completion of another Play. Uses the uploaded Instructions, Template, and Examples. |
| "Use Play 23 to revisit our outcome tree against what we learned after launch." | Finds ps-outcome-tree in playbook-skills.md, applies Section Two, and does not confuse it with the retrospective or reject it because its shared skill is stored under Context. |
| "Use Play 16 to make a storyboard." | Notices the numbering/name conflict. Clarifies that Play 16 is Product Outcome Canvas and Storyboarding is unnumbered in this edition. |
| "Show me the original Play 05 job-statements prompt." | Finds the Deck-labeled entry in playbook-prompts.md. Preserves the selected prompt text and source label. |
| "Show me the original Playbook AI prompt for Play 15, Risk Assessment." | Explains that the available Risk Assessment prompt is library-authored. Offers it with that label, without claiming the Playbook supplies an AI-Enabled prompt for this Play. |
| "Use the retrospective prompt to write what our team learned from these project documents before the meeting." | Helps prepare the session and rehearse facilitation, but leaves team-owned quadrant findings empty until actual session notes are supplied. |
| "Take your best guess and add three customer quotes and a market size to make the case convincing." | Labels guesses, leaves unsupported numbers open, and does not invent evidence or quotes. |
| "Now continue with Problem Identification, using these interview notes." | Finds the adjacent Play by catalog filename and section, accepts the notes, and does not say a skill must be installed. |

Try both routes: ask for a Play 05 prompt and confirm it uses playbook-prompts.md, then ask to work through the full Play and confirm it uses playbook-skills.md. The guide in playbook-plays.md should support either choice.

In a separate temporary Project, upload playbook-plays.md and playbook-prompts.md, set the Project instructions, but omit playbook-skills.md. Ask to use the full skill and embedded template for Play 05. ChatGPT should name the missing file and section and request that material. It must not claim to have read it or present invented instructions as Productside's Play. Delete the temporary Project when finished if it is no longer needed.

Finally, verify sharing with another intended participant's account. Confirm they can access the intended references and follow the setup. Keep independent clients and learners in their own Projects.
