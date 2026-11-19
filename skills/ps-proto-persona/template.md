# ps-proto-persona Template

Use this template to build a **Productside-style proto-persona** for the primary user first, then optionally the buyer.

Tag every line of the working draft with where it came from:

- `[FROM YOU]` - the PM or their stakeholders supplied it
- `[RESEARCH]` - it came from evidence; name the source under Proto-Persona Caveats
- `[AI-SUGGESTED, VALIDATE THIS]` - a filled gap; a guess to test first

Tags go at the end of the line and are the only annotation allowed inside the fields. When the PM commits the persona, the clean copy drops the tags from the fields and keeps the Riskiest Assumptions list.

## When to Use This

Use this when you need a working customer profile before full validation, and you want the team to have a shared understanding of who the product is serving.

## Template

```markdown
# Proto-Persona

## Persona Type
- User, Buyer, or Influencer:
- Validation status: Proto-persona / Validated persona
- Confidence level: Low / Medium / High

## Product Context
- Product or service:
- Problem space:
- Why this persona matters:

## Name & Portrait
- Name (alliterative, first name + role, e.g. "Henry HR Specialist"):
- Portrait description:

> Quality check: The persona should feel specific enough to remember and discuss. Avoid placeholders like "User A" unless this is a temporary working draft.

## Bio & Demographics
- Role / title:
- Industry or operating context:
- Organization context:
- Seniority or experience level:
- Relevant demographics:
- Backstory:

> Quality check: Include only demographics and background that actually help the team understand product behavior, needs, or constraints.

## Quotes
- Quote 1:
- Quote 2:
- Quote 3:

> Quality check: Quotes should reveal how this person thinks, speaks, or feels. Avoid generic lines like "I want better tools."
> Provenance check: Invented quotes are always `[AI-SUGGESTED, VALIDATE THIS]`. Only words a real customer said are `[RESEARCH]`.
> Capacity check: Keep quotes compact enough to fit the canonical quotes field.

## Needs | Pains
- Pain or need 1:
- Pain or need 2:
- Pain or need 3:
- What they are trying to accomplish, and the behavior we observe:

> Quality check: These should describe meaningful friction, unmet need, or frustration. Make them specific enough that the team can respond to them.
> Capacity check: Keep this section concise enough to paste into the canonical pain field.

## Desired Outcomes | Goals
- Desired outcome or goal 1:
- Desired outcome or goal 2:
- Desired outcome or goal 3:
- Attitudes and influences (beliefs, people and tools they trust, pressures):

> Quality check: Keep this future-state oriented. These are not tasks or features. They are the improvements this person wants in their work or life.
> Capacity check: Write compact future-state statements, not long rationale.

## Proto-Persona Caveats
- What still feels provisional:
- What should be validated next:
- Highest-priority research gaps:
- Evidence sources (for `[RESEARCH]` lines):

## Riskiest Assumptions
The AI-suggested lines that would most change this persona if wrong, ranked by what to test first.
1.
2.
3.

> Quality check: Does every line above carry a provenance tag? Is any AI-suggested line passed off as the PM's belief or as research?
> Focus check: Does this persona describe the center of one segment, or a blurry everyone?

## Buyer Relationship
- Is this person also the buyer?
- If not, who likely buys or approves?
- What tension might exist between user needs and buyer priorities?

## Research Next Steps
- Who should we interview next?
- What should we validate first?
- Which assumptions are riskiest?
```

## Usage Guidance

- Build the **user persona first**.
- Only then create a separate buyer persona if the buyer is materially different.
- Keep the proto nature explicit until research confirms the profile.
- Do not use confidential client details in examples or shareable artifacts.
- Keep provenance tags short and at the end of each line. Keep validation notes concise unless the user explicitly asks for heavier evidence annotation.
- Complete every main persona section before adding any commentary.
