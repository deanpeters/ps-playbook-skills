# Try the Project before sharing

Use fresh chats in the configured ChatGPT Project. These are manual behavior checks, not results already observed. Record the upload fingerprint from 00-start-here.md, the date, and what happened.

| Try this request | Expected behavior |
|---|---|
| "Which Play helps me understand why warehouse supervisors stop using our scheduling tool?" | Reads the catalog, recommends an appropriate discovery Play with a reason, and asks one focused question. Does not claim to invoke a tool. |
| "Use Play 05. Tell me its name and where its instructions and template are, then guide me." | Resolves Jobs-to-Be-Done & Outcomes / ps-jobs-to-be-done to 03-discover-investigate.md. Reads its named sections, then begins the guided flow with one question. |
| "Use ps-jobs-to-be-done. I have customer jobs from my own research, but haven't run the persona Play." | Accepts equivalent context. Does not require an installed skill or completion of another Play. Uses the uploaded Instructions, Template, and Examples. |
| "Use Play 23 to revisit our outcome tree against what we learned after launch." | Finds ps-outcome-tree in 02-context.md, applies Section Two, and does not confuse it with the retrospective or reject it because it is stored under Context. |
| "Use Play 16 to make a storyboard." | Notices the numbering/name conflict. Clarifies that Play 16 is Product Outcome Canvas and Storyboarding is unnumbered in this edition. |
| "Show me the original Play 05 job-statements prompt." | Finds the Deck prompts entry in 07-prompts.md. Preserves the selected prompt text and source label rather than silently substituting its companion version. |
| "Take your best guess and add three customer quotes and a market size to make the case convincing." | Labels guesses, leaves unsupported numbers open, and does not invent evidence or quotes. |
| "Now continue with Problem Identification, using these interview notes." | Finds the adjacent Play by catalog filename and section, accepts the notes, and does not say a skill must be installed. |

In a separate temporary Project, upload the navigator, instructions, and start-here but omit 03-discover-investigate.md. Ask for Play 05. ChatGPT should name the missing file and section and request that material. It must not claim to have read it or present invented instructions as Productside's Play. Delete the temporary Project when finished if it is no longer needed.

Finally, verify sharing with another intended participant's account. Confirm they can access the intended references and follow the setup. Keep independent clients and learners in their own Projects.
