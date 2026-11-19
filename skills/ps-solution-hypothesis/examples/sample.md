# Solution Hypothesis Statement - Examples

## Example 1: Strong Productside-Style Solution Hypothesis

Scenario: An agricultural technology company building a supply chain visibility platform for regional produce distributors managing perishable inventory across multiple grower relationships.

```markdown
# Solution Hypothesis Statement

## Product Context

- Product or service: FreshTrack - perishable supply chain visibility platform
- Target market segment: Regional produce distributors (50-200 grower relationships)
- Primary customer (the person who uses or buys the product): Distribution Operations Manager

## 1. Problem Statement

I am a Distribution Operations Manager coordinating perishable produce shipments from dozens of independent growers using phone calls, spreadsheets, and faxed invoices. Trying to minimize spoilage losses and fill customer orders completely from available inventory. But harvest timing, transit delays, and cold chain gaps cause spoilage and stockouts that I discover only when trucks arrive at the warehouse. Because each grower tracks their own harvest and shipment schedule independently, and there is no shared visibility into what is in transit or at what temperature. Which makes me feel unable to plan reliably and anxious about the margin erosion I cannot prevent.

## 2. Solution Summary

Provide a supply chain visibility platform that connects grower harvest logs, transit tracking, and cold chain monitoring into a single shared view, giving distribution operations managers advance notice of what is arriving, when, and in what condition.

## 3. Solution Benefits

- Early warning of spoilage risk, allowing rerouting before product loss occurs
- Improved order fill rates through better visibility into available inventory
- Reduced manual coordination time spent calling growers and carriers for status updates
- Stronger grower relationships through shared data and fewer disputed shipments

## 4. Risks and Assumptions

- Growers with limited technology adoption may resist installing tracking hardware or using a new system
- Cold chain sensor hardware costs may exceed what small distributors can absorb upfront
- Cellular connectivity gaps in rural growing regions may cause data transmission delays
- Existing ERP systems at distributor warehouses may require custom integration work

## 5. Solution Hypothesis Statement

### Customer-Focused Hypothesis

IF we provide distribution operations managers with a shared supply chain view that connects grower harvest data, transit tracking, and cold chain monitoring in one platform, THEN they will reduce spoilage losses and improve order fill rates by catching problems before trucks arrive at the warehouse.

### Business-Focused Hypothesis

IF distribution operations managers reduce spoilage losses and improve order fill rates through early problem detection, THEN we will achieve our goal of reducing distributor spoilage-related margin loss by 25% within the first growing season and increasing average order fill rates from 82% to 93%.
```

### Why This Works

- **All five sections present and in order.** Problem statement, solution summary, benefits, risks, and two-column hypothesis are all complete.
- **Problem statement is imported, not rewritten.** It reads as a ps-framing-the-problem output, with the five-stem structure visible in the narrative.
- **Solution summary is specific and testable.** "Connects grower harvest logs, transit tracking, and cold chain monitoring into a single shared view" describes a concrete solution. Not "build a better platform."
- **Benefits are outcomes, not features.** "Early warning of spoilage risk, allowing rerouting before product loss occurs" is an outcome. "Dashboard" would be a feature.
- **Risks are specific and testable.** "Growers with limited technology adoption may resist installing tracking hardware" is a risk the team can investigate through grower interviews. "Things might go wrong" is not.
- **Two hypotheses chain correctly.** The THEN of hypothesis 1 ("reduce spoilage losses and improve order fill rates") becomes the IF of hypothesis 2. The chain is unbroken.
- **Customer hypothesis focuses on customer value.** It describes what the customer gains, not what the business earns.
- **Business hypothesis includes measurable outcomes.** "Reducing spoilage-related margin loss by 25%" and "increasing order fill rates from 82% to 93%" are specific, verifiable targets.
- **Role names used throughout.** "Distribution operations managers" appears in both hypotheses, not a persona name like "Carlos."
- **No implementation details.** The solution summary describes what the platform provides, not how it is architected.

---

## Example 2: Weak Generic Solution Hypothesis

Same scenario, written poorly.

```markdown
# Solution Hypothesis Statement

## Product Context

- Product or service: Supply chain platform
- Target market segment: Agriculture
- Primary customer (the person who uses or buys the product): Supply chain professional

## 1. Problem Statement

Supply chain management is challenging in the agriculture industry due to the perishable nature of products and complex logistics networks.

## 2. Solution Summary

Build a better platform that helps with supply chain visibility and efficiency improvements.

## 3. Solution Benefits

- Better visibility
- Improved efficiency
- Cost savings
- Better relationships

## 4. Risks and Assumptions

- Users might not adopt the new system
- There could be technical challenges
- Budget constraints
- Competition from other solutions

## 5. Solution Hypothesis Statement

If we build an integrated supply chain platform with real-time tracking, automated alerts, cold chain monitoring, dashboards, grower portals, and API integrations, then our customers will be happier and more efficient, which will help us grow revenue and expand into new markets.
```

### Why This Fails

- **Problem statement is not imported from upstream.** It is a generic one-sentence observation about the industry, not a validated problem framed from the customer's perspective. There is no five-stem structure, no specific persona, no emotional impact.
- **Solution summary is untestable.** "Build a better platform" describes nothing specific. Better than what? Platform for whom? What does it actually do?
- **Benefits are feature labels, not outcomes.** "Better visibility" and "improved efficiency" are abstract words with no concrete meaning. Visibility into what? Efficiency measured how? These cannot be validated.
- **Risks are generic worries.** "Users might not adopt" and "technical challenges" apply to any product in any industry. They give the team nothing to investigate.
- **Only one hypothesis, not two.** The customer-to-business chain is collapsed into a single run-on sentence. There is no separation between customer value and business outcome.
- **The hypothesis is a feature list.** "Real-time tracking, automated alerts, cold chain monitoring, dashboards, grower portals, and API integrations" is a feature spec, not an If/Then hypothesis. It says what to build, not what outcome to expect.
- **"Happier and more efficient" is not measurable.** There is no specific outcome. How would the team know if this hypothesis was confirmed or refuted?
- **No role specificity.** "Supply chain professional" and "our customers" are too broad. Who, specifically, benefits?

---

## Example 3: Drift Bug - Feature List Disguised as Hypothesis

```markdown
## 5. Solution Hypothesis Statement

### Customer-Focused Hypothesis

IF we build a platform with the following features:
- Real-time GPS tracking for all shipments
- IoT temperature sensors with automated alerts
- Grower self-service portal for harvest reporting
- Warehouse receiving dashboard with ETA predictions
- Mobile app for drivers with delivery confirmation

THEN distribution operations managers will have better tools for managing their supply chain.

### Business-Focused Hypothesis

IF distribution operations managers have better tools, THEN we will be able to charge a premium subscription price, expand into adjacent verticals like dairy and seafood, and build a defensible market position through data network effects.
```

### Why This Is Wrong

The structure looks like two If/Then statements, but both are broken:

- **Hypothesis 1 is a feature list, not a solution description.** The IF lists five specific features rather than describing the value the solution provides. A hypothesis should say what the solution does for the customer, not enumerate every component. "IF we provide a shared supply chain view connecting harvest data, transit, and cold chain monitoring" is a solution description. A bulleted feature roadmap is not.
- **The THEN of hypothesis 1 is vague.** "Better tools for managing their supply chain" is not a specific customer benefit. Better how? What outcome changes? "Reduce spoilage losses and improve order fill rates" is specific. "Better tools" is a tautology.
- **Hypothesis 2 jumps to go-to-market strategy.** Premium pricing, vertical expansion, and data network effects are business strategy items, not outcomes tied to the customer benefit above. The business hypothesis should say: if we achieve X customer benefit, then Y measurable business result follows. Instead, it leaps from "better tools" to a three-part strategy pitch.
- **The chain is broken.** The THEN of hypothesis 1 ("better tools") does not clearly become the IF of hypothesis 2 ("have better tools"). Technically the words match, but because "better tools" is meaningless, the chain carries no information. The connection is syntactic, not logical.

**Fix:** Rewrite hypothesis 1 with a solution description (not a feature list) in the IF and a specific customer outcome in the THEN. Then write hypothesis 2 where the IF restates that customer outcome and the THEN names a measurable business result. Strip the go-to-market strategy into a separate document; it does not belong in the hypothesis.
