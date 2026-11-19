# ps-market-selection-sizing Examples

All three examples use the same domain: remote monitoring for water and wastewater pump stations, sold to U.S. utilities.

**Every figure and source below is illustrative.** The numbers show the shape of the reasoning, not real market data. Do not reuse them as facts.

## Example 1: Strong Market Analysis

Scenario: a company with an existing pump-station monitoring product (cellular sensors and alerting) is deciding which utility segments to explore next.

```markdown
# Market Selection & Sizing

## Context
- Product or product idea: Existing. Cellular sensors and alerting for unattended pump and lift stations
- Who it is for, and the benefit it provides: Utilities that run unattended pump stations; earlier warning of failures and overflows
- Decision this analysis informs: Which segment to run discovery in next quarter
- Counting unit: pump stations (priced per station per year)

## 1. Market Selection
- Market: Remote monitoring of unattended pump and lift stations for U.S. water and wastewater utilities

### PESTEL
| Force | Entry | Source or status |
|---|---|---|
| Political | State revolving-fund grants now prioritize resilience upgrades | [S1] |
| Economic | Rate caps squeeze operating budgets; capital spend is easier to fund | [S2] |
| Social | Licensed operators retiring faster than they are replaced | [S3] |
| Technological | Cellular sensors replacing legacy radio telemetry at small sites | [S4] |
| Environmental | Heavier storms overloading lift stations in some regions | OPEN QUESTION: which regions, how often? |
| Legal | Overflow reporting rules raise penalty exposure for missed alarms | [S5] |

## Total Addressable Market (TAM)
- Sized fact 1: 48,000-52,000 utilities operate at least one pump or lift station [S6]
- Sized fact 2: 3-4 stations per utility on average, across all sizes [S7]
- TAM: 145,000-210,000 pump stations

## 2. Segments

### Segment 1: Mid-size systems with stretched on-call crews
- Description: Serve 10,000-100,000 people; stations unattended; a small crew covers nights by rotation; overflow fines are a board-level worry
- Cut logic: Staffing model (rotating on-call crew, no 24/7 control room) and penalty exposure, not population alone [AI-SUGGESTED, VALIDATE THIS]
- Users: Lead operators, on-call technicians
- Buyers: Utility director, public works director
- Influencers: Consulting engineers, state regulators, city council

### Segment 2: Small rural systems with a shared circuit-rider operator
- Description: Serve under 10,000 people; one licensed operator covers several systems part-time; upgrades depend on grants
- Cut logic: One operator across multiple systems, and a grant-funded buying path [FROM YOU]
- Users: Circuit-rider operator
- Buyers: Town manager, water board chair
- Influencers: State rural water association technical assistants, grant administrators

## 3. Size the Market & Segments

### Serviceable Addressable Market (SAM)
| Segment | Counting logic (formula) | Inputs and sources | SAM (range) |
|---|---|---|---|
| 1 | systems x stations per system | 4,000-5,000 systems [S6]; 8-15 stations each [S8] | 32,000-75,000 stations |
| 2 | systems x stations per system | 20,000-25,000 systems [S6]; 1-3 stations each [S8, TO SOURCE for under-3,300] | 20,000-75,000 stations |

Triangulation: top-down from the system inventory [S6], bottom-up from 12 customer station counts [S9], and two consulting engineers' estimates [S10]. Segment 1 agrees within 20%. Segment 2's bottom-up runs low; see Open Questions.

### Serviceable Obtainable Market (SOM), annual revenue
| Segment | Share basis (competition, reach, win rate, capacity, horizon) | Units x annual price | SOM (range) |
|---|---|---|---|
| 1 | Three SCADA-bundled competitors [S11]. Reach 120-200 utilities in 24 months through two regional partners [S12]. Win rate 20-30% (assumption, from last year's pilots [S9]). | 24-60 utilities x 10 stations x $1,200-1,800 per station per year (current list price [S13]) | $0.29M-$1.08M per year at month 24 |
| 2 | No validated product fit for single-operator systems yet | Deferred until solutions are ideated | Deferred |

## Source Register
| ID | Source | Date | What it supports |
|---|---|---|---|
| S1-S13 | (Illustrative placeholders: a federal system inventory, a state grant program, an operator workforce report, regulator rules, company sales and pricing data, customer counts, and engineer interviews) | n/a | As cited above |

## Open Questions
1. Segment 2 stations per system: bottom-up suggests 1-2, not 1-3. This could halve Segment 2's SAM.
2. Win rate: two years of pilots is a thin basis. Confirm with partner pipeline data.
3. Environmental: which regions see storm-driven overloads, and is that a buying trigger?
```

**Why this works**

- **The market is named at the right altitude:** who it serves (utilities with unattended stations) and the benefit (earlier warning), narrow enough to size.
- **The PESTEL is specific.** Every entry is about this market, with a source, and the one the team couldn't source is an honest open question.
- **Segments differ by behavior, not just size.** The cut is staffing model and buying path, and each segment names real users, buyers, and influencers.
- **The sizing is a formula with a source on every input,** in one counting unit (stations), as ranges, triangulated three ways, with SOM ≤ SAM ≤ TAM.
- **The SOM share has a basis:** competitors, partner reach, a win rate traced to pilots, a horizon, and the price is the company's own list price.
- **Segment 2's SOM is deferred,** because there is no product fit to price yet. That is what the Playbook asks for.
- **Provenance is visible.** The team's own cut is `[FROM YOU]`; the model's suggestion is tagged for validation.

## Example 2: Weak Market Analysis

```markdown
# Market Selection & Sizing

## 1. Market Selection
- Market: Smart water

### PESTEL
| Force | Entry |
|---|---|
| Political | Government regulation is increasing |
| Economic | Inflation is affecting budgets |
| Social | Sustainability matters more to people |
| Technological | AI and IoT are transforming the industry |
| Environmental | Climate change |
| Legal | Compliance requirements |

## Total Addressable Market (TAM)
- The global smart water management market is $18.4B, growing at 12.3% CAGR

## 2. Segments
### Segment 1: Large utilities
### Segment 2: Small utilities

## 3. Size the Market & Segments
- SAM: $4.1B (North America)
- SOM: 2% of SAM = $82M
```

**Why this fails**

- **"Smart water" is too broad** to analyze. It isn't centered on who the product serves or the benefit it provides.
- **Every PESTEL entry is generic.** Each would fit any market, and none has a source.
- **The TAM is a guess dressed as a finding:** a precise global figure with no source, in a different unit (dollars, global) from anything the product sells.
- **The segments are size labels** with no description, no cut logic, and no users or buyers in them. The next plays have no one to write about.
- **The SOM is an assumed share** with no competition, reach, or capacity basis, and $82M is not tied to any count of stations or price.

## Example 3: Drift Bug, "The Free Five Percent"

The market, PESTEL, segments, and SAM are as strong as Example 1. Then the SOM:

```markdown
### Serviceable Obtainable Market (SOM), annual revenue
| Segment | Share basis | Units x annual price | SOM (range) |
|---|---|---|---|
| 1 | Capture 5% of SAM in 24 months | 5% x 32,000-75,000 stations x $1,500 | $2.4M-$5.6M per year |
| 2 | Capture 5% of SAM in 24 months | 5% x 20,000-75,000 stations x $1,500 | $1.5M-$5.6M per year |
```

**Why this fails**

- **The share is a wish.** Nothing explains why 5%: no competitors, no reach, no win rate, no delivery capacity. The Playbook says SOM must consider competition.
- **It inflates by up to 5x.** Example 1's grounded basis gives Segment 1 $0.29M-$1.08M. The free five percent gives $2.4M-$5.6M.
- **It prices a segment with no product fit.** Segment 2 gets a confident SOM for a product that has not been shown to work for single-operator systems.
- **It's easy to miss,** because everything above it is rigorous. Rigor upstream lends false credibility to the assumption downstream.

**Fix:** Build the share from the bottom up: utilities the team can reach over the horizon × a win rate with a stated basis, capped by delivery capacity. Defer SOM for any segment without a product to price. If there is no basis yet, show a conditional formula and name what would anchor it.
