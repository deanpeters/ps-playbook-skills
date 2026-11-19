# Market Selection & Sizing Prompts

**Source:** Productside Playbook, B2B work-in-progress deck (`wip-b2b-2026-11`), slides 16-17. Not yet ratified as canonical. Market Selection & Sizing is new in that deck (Template 04); the baseline deck has no equivalent Play.

These are copy-paste prompts for working through a market analysis in any chat-based AI tool that can search the web. You don't need this skill installed to use them. If the skill *is* installed, it already behaves this way. It proposes structure and segments with its reasoning shown, cites what it finds, and never hands you a market size without a source.

The Playbook's rule for every AI page: **you do the thinking, and AI pressure-tests it.**

## How AI Supports This Play

AI is fast at structure and dangerous at facts. It can lay out a PESTEL skeleton, suggest ways to segment your market, and frame a TAM/SAM/SOM calculation. What it cannot do is know your market. Every number it gives you about size, growth, or competitors is a guess dressed as a finding.

Use AI to organize the sources you already have and expose the gaps you still need to fill. It turns scattered evidence into a shape you can reason about.

AI does not replace your judgment about what is real. Treat every figure it produces as a blank to source, not a fact to paste. The moment you cite an AI number as if it were sourced, you trade your credibility for speed.

| Use AI when | Avoid AI when |
|---|---|
| You have named the market and gathered real sources, and need help structuring or sharpening the analysis. | You have no sources yet, or you are about to ask AI for the market size. |

**Inputs you provide**

- The named market and any real sources you have gathered
- Your product and who it serves
- Pricing, competitor, or constraint information you already hold

**Outputs to expect**

- A PESTEL with your evidence organized and gaps flagged as questions
- Segments with explicit cut logic you can test
- TAM/SAM/SOM as formulas with inputs you source

## Common Traps

| AI invents the market | Segments for show, not truth |
|---|---|
| Confident market sizes with no source | Tidy cuts that fit any market |
| Competitor revenues it cannot know | Segments with no real persona (buyer or users) |
| A PESTEL full of generic forces | Professional-looking logic that goes untested |

## How to Use These Prompts

Run them in order, **in the same chat**. Prompts 2-4 continue the conversation prompt 1 starts. Answer honestly, including "I don't know yet," and commit something to your market analysis ([../template.md](../template.md)) before moving to the next.

| # | Prompt | Goal | You commit |
|---|---|---|---|
| 1 | [01-pressure-test-market.md](01-pressure-test-market.md) | Name the right market at the right altitude | The market you named, in your own words |
| 2 | [02-build-pestel.md](02-build-pestel.md) | Work the six forces one at a time. The goal is evidence, not a full grid. | Each force as evidence or an open question to research |
| 3 | [03-segment-market.md](03-segment-market.md) | Cut the market, then defend each cut | At least two segments, with named users, buyers, and influencers in each |
| 4 | [04-first-pass-sizing.md](04-first-pass-sizing.md) | Build the sizing logic without inventing numbers | TAM and SAM with a source behind every input; SOM only if you have a product |

Two tips from the Playbook's example page:

- **Triangulate.** Build accuracy in your market sizes by triangulating your numbers. Don't rely on a single search or one source.
- **Use ranges.** Ranges reduce overconfidence and change the conversation from defending a number to discussing risk.

**Recommended tool type:** chat-based AI tool. Use one with web search, because prompts 1-3 ask it to find and cite sources. Check every source it cites before you commit a number.

## Source Notes

Prompt text is kept verbatim from the deck. These issues are recorded here for the Productside content team:

- Slide 17's "How to use this page" lists three steps, but the page holds four prompts. Prompts 2-4 read as continuations of prompt 1's chat.
- Slide 16 says to avoid AI "when you are about to ask AI for the market size," while prompts 1-3 ask AI to research, segment, and recommend. The skill reconciles these: AI may propose structure and segments, and may find and cite sources, but every number needs a source the PM can check.
- Slide 15's worked example uses "5% market share 24 months after successful trials" with no stated basis. Slide 14 says SOM "should consider competition to determine what share of the SAM you can potentially achieve." The skill requires a stated basis for any share.
- Slide 14: "Service Obtainable Market" should read "Serviceable Obtainable Market"; "enables you define" is missing "to"; "As your work through" should read "As you work through."
- Slide 15 TIP 02: "an umber" should read "a number."
- Slide 18 (the blank template) is titled "AI Product Management."
- Slide 19, the next Play's overview (Jobs-to-Be-Done), repeats this Play's Key Takeaways about PESTEL and TAM/SAM/SOM.
