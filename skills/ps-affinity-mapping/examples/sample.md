# Affinity Mapping Examples

## Strong Example

**Domain:** B2B logistics tracking software (freight brokers and carriers)

**Why This Works**

- Theme labels name patterns, not topics. "Real-Time Visibility Gaps Create Reactive Operations" tells you what is happening; "Visibility" does not.
- Observation bullets are short, specific, and grounded in what customers said or did.
- Key insights answer "so what?" and have clear product implications. Each insight paragraph connects the pattern to what the product team should understand, not just what customers complained about.
- Four clusters cover distinct root causes. They do not bleed into each other.
- The insights were written after seeing all four clusters together, so they reflect the full picture of the data.
- The team did the grouping. The map says so, which tells readers the themes were argued over, not accepted from a draft.

---

**Affinity Map**

**Research Context**

- Product or service: FreightView, a shipment tracking and carrier communication platform for freight brokers
- Research conducted: 8 empathy interviews with freight brokers, 3 with carrier dispatch managers, 22 support ticket themes
- Number of observation sources: 33
- Date mapped: June 2026
- Grouped by: The team (coached), with the PM facilitating

**Theme Clusters**

**Theme 1: Real-Time Visibility Gaps Create Reactive Operations**

- Brokers check carrier portals manually every 2-3 hours to find status updates
- Customers call brokers asking for ETAs that brokers do not have
- Brokers described spending 30-40% of their day chasing status from carriers
- Dispatch managers paste updates into email threads rather than updating the system
- Late status updates discovered only when the customer escalates
- One broker said "I find out there is a problem at the same time my customer does"
- Brokers build personal relationships with specific carrier reps to get faster callbacks

**Theme 2: Multi-System Fragmentation Slows Every Handoff**

- Brokers use 3-4 separate tools for quoting, booking, tracking, and invoicing
- Copy-pasting shipment details between systems is described as a daily ritual
- Errors introduced during manual data transfer cause invoice disputes
- Carrier contact info stored in spreadsheets outside the main system
- Brokers maintain personal notebooks with carrier preference notes not captured anywhere shared
- New brokers spend weeks learning which systems hold which information

**Theme 3: Exception Handling Depends on Institutional Knowledge**

- Senior brokers handle exceptions quickly because they know which carriers respond to calls vs. texts
- Junior brokers escalate nearly all exceptions because they lack the informal carrier knowledge
- No standard process for rerouting a delayed shipment; each broker improvises
- Teams described "tribal knowledge" as both essential and fragile
- When a senior broker leaves, their carrier relationship knowledge leaves with them
- Onboarding a new broker takes 3-6 months before they handle exceptions independently

**Theme 4: Billing Disputes Consume Disproportionate Time After Delivery**

- Invoice reconciliation done manually against original quotes after every shipment
- Accessorial charges (detention, fuel surcharges) appear unexpectedly on final invoices
- Disputes require pulling email threads and screenshots as evidence
- Some brokers described keeping a separate spreadsheet just to track disputed charges
- Average dispute resolution takes 5-7 business days
- Customers blame brokers for charges they did not authorize, even when the carrier added them

**Key Insights**

**Key Insight 1: Brokers Are Running a Status Lookup Business Inside a Logistics Business**

The volume of manual status-checking work that brokers described is not a minor friction point. It is structurally crowding out the relationship and problem-solving work that earns their margin. When brokers spend 30-40% of their day chasing ETAs, they cannot spend that time on exceptions, new business, or carrier development. A product that reduces reactive status-checking directly frees capacity for higher-value broker work.

**Key Insight 2: Fragmentation Is Not Just Inconvenient, It Is a Source of Revenue Leakage**

The errors introduced during manual data transfer between systems result in invoice disputes that take days to resolve. This is not a usability complaint; it is a margin problem. The fragmentation creates both direct costs (staff time on reconciliation) and indirect costs (customer trust erosion from unexpected charges). Reducing the number of system-to-system handoffs is likely to show up in measurable financial outcomes, not just satisfaction scores.

**Key Insight 3: Exception Handling Is a Knowledge Management Problem Disguised as a Process Problem**

The variation in how brokers handle exceptions is not caused by a missing workflow. It is caused by the fact that the most valuable knowledge for resolving exceptions lives in senior brokers' heads and informal relationships, not in the system. This creates a compounding problem: performance is dependent on tenure, onboarding is slow, and organizational knowledge walks out the door when people leave. The product has an opportunity to capture and surface the informal knowledge that currently only experts carry.

**Completeness Check**

- [x] All major clusters from the raw data are labeled
- [x] No observation appears in more than one theme cluster
- [x] Each key insight answers "so what?"
- [x] Three themes and three insights minimum present (four themes, three insights)
- [x] Observation bullets are 8-12 words each

---

## Weak Example

**Domain:** B2B logistics tracking software (same domain, different execution)

**Why This Fails**

- Theme labels name topics, not patterns. "Process Issues," "Technology Problems," and "People Challenges" could hold almost any observation from any domain. They reveal nothing about what is actually happening for this customer.
- Several observations are actually team opinions or solution suggestions, not customer-side evidence. "The system needs better reporting" is what the PM thinks, not what a customer said.
- Key insights restate theme labels rather than making inferences. "Process issues are causing problems for our customers" adds zero analytical value beyond the label.
- Only three clusters when the data likely warrants more, and the clusters bleed into each other.

---

**Affinity Map (Weak)**

**Theme Clusters**

**Theme 1: Process Issues**

- Brokers waste time on manual work
- The current process does not scale
- We need to automate more of the workflow
- Status updates take too long
- Invoicing is complicated

**Theme 2: Technology Problems**

- The system needs better reporting
- Too many tools to manage
- The interface is confusing
- Data does not sync properly
- We should build a mobile app

**Theme 3: People Challenges**

- New brokers take a long time to get up to speed
- Senior brokers are a bottleneck
- Communication between teams is poor
- Customers are frustrated

**Key Insights**

**Key Insight 1: Process Issues Are Causing Problems**

Process issues are causing significant problems for our customers. The manual nature of many workflows is slowing things down and creating frustration. Improving processes would help brokers work more efficiently and serve customers better.

**Key Insight 2: Technology Is Not Meeting User Needs**

The current technology is not meeting user needs. Brokers are struggling with too many systems and poor data quality. Better technology would address these problems and improve the overall experience.

**Key Insight 3: People and Training Need Improvement**

People-related challenges, including onboarding and communication, are creating friction. Investing in training and better communication tools would help teams work together more effectively.

---

## Drift-Bug Example: Observation Overlap Bug

**Named failure:** Observation Overlap Bug

**What it looks like**

The affinity map appears complete: four labeled themes, five or more observations per cluster, three key insights. But several observations appear in two or more theme clusters simultaneously, either because the team was uncertain where they belonged or because the observations were written broadly enough to fit multiple patterns.

Example (using the logistics domain):

Theme 1: "Brokers use multiple systems for different tasks" appears here.
Theme 2: "Brokers use multiple systems for different tasks" also appears here (slightly rephrased as "Too many tools slow the workflow").

The same underlying observation about system fragmentation has been counted twice. If both Theme 1 and Theme 2 generate a key insight about fragmentation, the PM will over-weight fragmentation as a priority relative to the other patterns.

**Why it happens**

Overlapping observations are often a sign that the clustering was done too quickly, or that the observation was written at a level of generality that made it fit multiple buckets. Observations like "the process is slow" or "there are too many steps" are common culprits because they describe a symptom that shows up across multiple root causes.

**The consequence**

The artifact looks complete, but the double-counting inflates the apparent importance of the overlapping observations. Key insights built on inflated clusters produce distorted prioritization signals.

**The fix**

During the completeness check, scan every observation across all clusters. For each observation that appears in more than one cluster:

1. Decide which cluster it primarily belongs to and move it there. Remove it from the others.
2. If the observation genuinely reflects two different underlying patterns, rewrite it as two separate, more specific observations and assign each to its correct cluster.
3. If multiple overlapping observations cluster loosely together across themes, ask whether there is a cross-cutting pattern that deserves its own named theme.

The goal is one home per observation. An observation that belongs everywhere belongs nowhere.
