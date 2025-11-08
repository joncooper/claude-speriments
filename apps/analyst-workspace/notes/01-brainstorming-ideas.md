# Comprehensive Brainstorming - Analyst Superpowers

This document captures the deep brainstorming session on ways Claude Code can transform equity research.

## The Analyst's Cognitive Workflow

Before building tools, we mapped the actual mental models:

### The Research Lifecycle
1. **Ambient Awareness** → noticing things worth investigating
2. **Hypothesis Formation** → "I think X is true because Y"
3. **Evidence Gathering** → testing the hypothesis
4. **Synthesis** → connecting evidence to thesis
5. **Conviction Building** → how sure am I?
6. **Communication** → explaining to others
7. **Monitoring** → watching for thesis breaks
8. **Evolution** → updating as facts change
9. **Retrospective** → what did I learn?

**Key Insight:** Most tools focus on #3 and #6. The real leverage is in #1, #2, #4, #5, #7, #8, #9.

---

## CLUSTER A: The "Research Memory Palace"

**Core insight:** Analysts forget their own insights. The best research happens when you connect Insight X from 6 months ago with Fact Y you learned today.

### A1: Personal Research Graph
- Every insight, fact, question, observation gets added to a knowledge graph
- Nodes: companies, people, concepts, trends, events, questions
- Edges: relationships you've discovered
- `/graph-add [observation]` - Connects to company + concept nodes
- `/graph-query [question]` - Navigate your mental model
- `/graph-surface-connections [topic]` - Find non-obvious connections
- Store as JSON in git (version controlled thinking)
- Visualize with Graphviz or D3

### A2: Insight Half-Life Tracking
- Tag insights by durability:
  - **Structural** (e.g., "Network effects") - years
  - **Cyclical** (e.g., "Pricing power in current environment") - quarters
  - **Tactical** (e.g., "Q3 will beat") - weeks
- `/aging-insights [ticker]` - "These 5 beliefs are getting stale, revalidate them"
- System reminds you to revisit/revalidate as insights age

### A3: Context Collapse Prevention
- When revisiting a ticker after 3 months, restore full context
- `/context-restore [ticker] [date]` - "Here's what you knew, what you were watching, what you were uncertain about"
- Includes: model assumptions, open questions, concerns, conviction level, recent events
- Like a save-state in a video game for your research

---

## CLUSTER B: The "Thinking Partner" Paradigm

**Core insight:** Best analysts have thinking partners who challenge them. Most analysts are lone wolves. Claude can be that partner.

### B1: Socratic Questioning Engine
Not just answering questions - asking better questions than you ask yourself.

`/socratic [thesis]` - Claude asks progressively harder questions:
- "What evidence would convince you that you're wrong?"
- "Why doesn't your competitor see it this way?"
- "What's the most important thing you don't know?"
- "If this is so obvious, why isn't the stock higher?"
- "What needs to be true for this to work?"
- "What's the second-order effect you're not considering?"

### B2: Intellectual Honesty Enforcer
- `/claim-tracker [statement]` - Track claims you make over time
- System checks: Do they actually deliver? Are you cherry-picking?
- `/confirmation-bias-check [thesis]` - "Here's evidence you're ignoring"
- Shows you your own motivated reasoning

### B3: Explain It to Different Audiences
If you can't explain it simply, you don't understand it.

- `/explain-to-smart-12-year-old [concept]` - No jargon allowed
- `/explain-to-skeptical-pm [thesis]` - Assumes you're wrong until proven right
- `/explain-to-yourself-drunk [idea]` - What's the ONE thing that matters?
- `/explain-to-board-member [situation]` - Strategic level, not tactical

### B4: Argument Inversion
- Take your bull thesis
- `/invert-argument [thesis]` - Claude steelmans the exact opposite
- Forces you to see the other side as rational people seeing different things
- Often reveals: "We're both right, but in different timeframes"

---

## CLUSTER C: The "Pattern Recognition Machine"

**Core insight:** Great analysts are pattern matchers. They've seen 1000 companies and know "this rhymes with that situation."

### C1: Situational Archetypes
Build a library of recurring situations:
- "High growth hitting law of large numbers"
- "Disruption from below" (Clayton Christensen style)
- "Winner-take-most dynamics emerging"
- "Cyclical disguised as secular decline"
- "Management change → strategic pivot → multiple expansion"
- "Roll-up strategy showing acquisition fatigue"

For each archetype:
- Characteristics: How do you recognize it?
- Typical evolution: What happens next?
- Historical examples: When has this happened before?
- Key variables: What determines success/failure?
- Timing: How long does this play out?

`/match-archetype [situation]` - Returns historical examples and typical outcomes

### C2: Leading Indicator Database
Track your own observations: "When I see X, Y usually follows in 6 months"

Examples:
- "Rising DSO → revenue quality issues → miss in 2 quarters"
- "Employee Glassdoor sentiment declining → product quality issues → customer churn"
- "Competitor capex surge → price war in 12 months"

`/leading-indicators [observation]` - Based on your history, what does this predict?

### C3: Cross-Industry Pattern Transfer
- SaaS companies went through land-and-expand in 2010s
- Now vertical software doing same thing
- E-commerce playbook → D2C brands
- Marketplace dynamics → two-sided networks everywhere

`/pattern-transfer [industry-A] [industry-B]` - What patterns from A apply to B?

### C4: The Playbook Detector
Companies run from known playbooks:
- "Amazon playbook": Sacrifice margins for growth → scale → margin expansion
- "Platform playbook": Build network effects → monetize later
- "Razor/blade playbook": Subsidize hardware, monetize consumables

`/detect-playbook [company]` - "They're running the X playbook, here's where they are, here are the risks"

---

## CLUSTER D: The "Quantified Judgment" Framework

**Core insight:** Analysts make hundreds of small judgments. Most are never recorded. What if you tracked them?

### D1: Micro-Predictions Market
Make tiny predictions constantly:
- "I predict Q3 revenue beats by 3%"
- "I predict they announce acquisition in next 6 months"
- "I predict new product launch fails"

`/predict [claim] [probability] [timeframe]` - Log it
`/prediction-results` - Track your calibration over time

Learn:
- Which types of predictions you're good at
- Which you're overconfident on
- Where your edge actually is

### D2: Judgment Decomposition
Break complex judgments into components:

"What's the stock worth?"
- Business quality (8/10) × Growth (6/10) × Management (7/10) × Valuation (5/10) × Timing (4/10)
- Each component has sub-components
- Track each separately

Benefits:
- Can disagree productively ("I agree on quality, disagree on timing")
- Can see which components changed
- Can identify blind spots ("I'm always too generous on management quality")

### D3: Reference Class Forecasting
Instead of guessing or asking management:
- `/reference-class [situation]` - Find 20 similar situations
- Look at actual distribution: 10th percentile, median, 90th percentile
- Use that for your forecast

Works for:
- Product launch success rates
- Turnaround timelines
- M&A synergy realization
- Margin expansion paths

### D4: Confidence Interval Thinking
Point estimates are lies. Everything is a range.

Instead of: "Revenue will be $500M"
Think: "90% confident revenue is $450-550M, 50% confident it's $480-520M"

`/confidence-intervals [forecast]` - Force yourself to give ranges
`/narrow-the-range [uncertainty]` - "What research would shrink this interval?"

---

## CLUSTER E: The "Research Leverage" System

**Core insight:** Not all research is equally valuable. How do you find the highest-ROI research questions?

### E1: Value of Information Calculator
Before doing research, estimate its value:
- Current expected value: $X
- If research confirms: $Y
- If research disconfirms: $Z
- Probability research is conclusive: P%
- Expected value of information: (P × |Y-X|) + ((1-P) × |Z-X|)

`/voi [research-question]` - Should you do this work or not?

### E2: Conviction Per Hour Tracking
Track:
- Activity: Read 10-K, management call, expert call, store visit
- Time spent: 3 hours
- Conviction change: +2 points
- Conviction per hour: 0.67

Learn what's high yield for YOU:
- Maybe you're great at reading between lines in transcripts
- Maybe you waste time on sell-side research

`/research-roi-analysis` - What activities give you best return?

### E3: The 80/20 Question Finder
`/critical-questions [situation]` - Generate ranked list:
1. Questions that, if answered, would change your view
2. Questions you're most uncertain about
3. Questions that are tractable (can actually answer)

The intersection is where to focus.

### E4: Diminishing Returns Detector
`/research-saturation [topic]` - "Have you learned enough?"

Signals:
- Last 3 sources told you same thing
- Conviction hasn't changed in 5 hours of work
- You're reading to procrastinate, not to learn

---

## CLUSTER F: The "Collaborative Intelligence" Layer

**Core insight:** The firm's collective knowledge vastly exceeds any individual's. How do you tap it?

### F1: Question Routing System
`/who-knows-about [topic]` searches:
- Past research reports (who's written on this?)
- Meeting notes (who's met with similar companies?)
- Coverage lists (who covers adjacent spaces?)

Returns: "Ask Sarah (fintech analyst), she covered a similar situation in 2022"

### F2: Collaborative Thesis Building
Multiple analysts covering different parts of value chain collaborate:
- `/shared-thesis-space [theme]` - Create shared workspace
- Each contributes observations from their domain
- System identifies: Confirmations, contradictions, gaps
- "Chip analyst sees slowing orders, cloud analyst sees capex increasing - investigate!"

### F3: Peer Review Protocol
`/peer-review [report] [reviewer-type]`
- Reviewer types: Skeptic, Generalist, Domain Expert, PM, Compliance
- Each brings different lens
- System facilitates structured review
- Not to create consensus, but to stress-test thinking

### F4: Knowledge Market
Create internal market for insights:
- Analyst posts question
- Others bid time to answer
- Asker allocates "points" for helpful answers
- Leaderboard for contributors

---

## CLUSTER G: The "Meta-Learning" Engine

**Core insight:** You should get better at research over time. But how do you track skill development?

### G1: Skills Taxonomy + Progress Tracking
Map the skills tree:
- Financial Analysis (Statement Analysis, Ratio Analysis, Cash Flow, Valuation)
- Industry Analysis (Competitive Dynamics, Regulatory, Technology Trends)
- Company Analysis (Business Model, Management, Strategic Positioning)
- Communication (Written Reports, Presentations, PM Interactions)
- Judgment (Idea Generation, Risk Assessment, Timing/Catalysts)

For each skill:
- Current level (1-10)
- Recent examples
- Gaps to work on
- Learning resources

### G2: Research Process Improvement
After completing project:
`/research-retro [project]` asks:
- What went well?
- What went poorly?
- What would you do differently?
- Time spent vs value created?

Aggregate to spot patterns:
- "I always underestimate time for model building"
- "Expert calls are consistently high-value"

### G3: Mistake Taxonomy
All mistakes are not equal:
- **Fact mistakes**: Misread the data (fixable with care)
- **Logic mistakes**: Reasoning flaw (fixable with thinking)
- **Judgment mistakes**: Weighed factors wrong (calibration issue)
- **Process mistakes**: Skipped a step (checklist issue)
- **Bias mistakes**: Confirmation bias, etc (awareness issue)

`/analyze-mistake [what-happened]` - Categorizes + suggests fix

### G4: Deliberate Practice Generator
`/practice-generator [skill]` creates exercises:
- Skill: "Identifying inflection points"
- Exercise: "Here are 10 historical companies at each quarter. Predict inflection points."

---

## CLUSTER H: The "External World Interface"

**Core insight:** Analysts need to synthesize information from everywhere.

### H1: Multi-Modal Monitoring Grid
**Continuous Monitoring** (daily):
- SEC filings, price/volume, news, social sentiment, Glassdoor, job postings

**Periodic Review** (weekly/monthly):
- Trade publications, patents, competitor moves, supplier earnings, regulatory

**Event-Driven**:
- Earnings, management changes, M&A, analyst days, product launches

`/monitoring-grid [ticker]` - Set up comprehensive monitoring
`/digest [frequency]` - Summarize only what matters

### H2: Signal vs Noise Filtering
Build filters:
- Stock moves >5% → Always review
- Management buys stock → Review
- 10-K filed → Deep read
- 10-Q filed → Changes only
- Press release about award → Ignore

`/signal-rules [ticker]` - Define what matters for THIS company

### H3: Smart Alerting System
Not just "something happened" but "something that matters to YOUR thesis happened"

Your thesis: "Company will expand margins through automation"
Alert: "Indeed job postings show 50% increase in warehouse workers"
Context: This contradicts automation thesis - investigate!

### H4: Alternative Data Integration
MCP servers for:
- Web traffic (SimilarWeb)
- App downloads (Sensor Tower)
- Satellite imagery (parking lots, construction)
- Credit card data
- Job postings
- Glassdoor sentiment
- GitHub activity

---

## CLUSTER I: The "Model as Living Artifact"

**Core insight:** Models aren't just calculators - they're representations of understanding.

### I1: Assumption Governance System
Every model cell gets metadata:
```yaml
Cell: D15 (Revenue Growth)
Value: 15%
Basis: Historical 12%, Management guide 18%, Your view 15%
Confidence: 6/10
Sensitivity: High (1% change = 5% to PT)
Last_updated: 2024-11-07
Dependencies: [TAM growth, market share]
Risks: [Competition, macro slowdown]
```

### I2: Scenario Engine
Multi-dimensional scenarios:
- Macro: Strong / Moderate / Weak
- Execution: Beat / Meet / Miss
- Competition: Rational / Intense

`/scenario-reducer [dimensions]` - Identify the 5-6 scenarios that matter

### I3: Model Diff Tool
`/model-diff [current] [prior]` produces:
- Price target: $50 → $55 (+10%)
- Changes decomposed:
  - Revenue growth: 15% → 17% (+$8 PT impact)
  - Multiple: 20x → 21x (+$3 PT impact)

### I4: Model Forensics
When model is wrong, why?
`/model-autopsy [ticker] [date]` - Decompose the error
- Revenue: You: $500M, Actual: $480M
  - Volume: -5%, Price: +1%
- Volume miss drove revenue miss

---

## CLUSTER J: The "Writing as Thinking" Framework

**Core insight:** Writing isn't just communicating research - it's DOING research.

### J1: Progressive Elaboration
Start with skeleton, flesh out iteratively:
- Version 1: Thesis in one sentence
- Version 2: Thesis + 3 supporting points
- Version 3: Each point gets paragraph
- Version 4: Add evidence
- Version 5: Add counterarguments

`/elaborate [draft]` - Suggests next level of detail

### J2: Argument Structure Validator
`/validate-argument-structure [draft]` checks:
- Is claim clear?
- Are supporting points independent?
- Is evidence actually supporting?
- Does conclusion follow from premises?

### J3: Prose Rhythm Checker
`/prose-rhythm [draft]` analyzes:
- Sentence length variety
- Paragraph structure
- Flow and readability

### J4: Jargon Translator
`/jargon-check [draft]` flags jargon, suggests plain English:
- "Operating leverage" → "costs grow slower than revenue"
- "Mix shift" → "selling more of the profitable products"

---

## CLUSTER K: The "Idea Generation" System

**Core insight:** Best analysts are proactive (generate ideas), not just reactive.

### K1: Screening on Steroids
Screen on insights, not just numbers:
- "Companies where R&D growing faster than revenue" (investing for future)
- "CFO joined from Big Tech in last 6 months" (professionalization)
- "Glassdoor ratings improving after declining" (turnaround)
- "Mentioning 'AI' in 10-K for first time"

`/creative-screen [hypothesis]` - Build insight-based screens

### K2: Contradiction Finder
Markets sometimes hold contradictory beliefs:
- Stock A up because "economy strong"
- Stock B up because "defensive quality"

`/find-contradictions [market-moves]` - Identifies logical inconsistencies

### K3: Second-Order Idea Generator
Fact: "Company X guiding revenue down"
- First-order: Sell X (obvious)
- Second-order:
  - Who takes their share? → Buy competitor Y
  - What do they buy less of? → Sell supplier Z
  - Will they get acquired? → Who would buy them?

`/second-order-ideas [event]` - Generate derivative ideas

### K4: Analogy Engine
`/find-analogies [company]` - What does this remind you of?
`/analogy-completion [partial]` - If AWS is to cloud, then ____ is to AI infrastructure?

### K5: Inversion Idea Generation
Charlie Munger: "Invert, always invert"

Instead of: "How to find winners?"
Ask: "How to avoid losers?" then invert

`/invert [question]` - Reframe in opposite direction

---

## CLUSTER L: The "Communication Optimization" Layer

**Core insight:** Research is useless if not communicated well.

### L1: Know Your Audience Profiler
`/audience-profile [PM-name]` learns preferences:
- Prefers bullets vs paragraphs?
- Wants details vs summary?
- Cares about what metrics?

`/write-for [PM-name] [content]` - Customizes communication

### L2: Answer the Unasked Question
PM asks: "What's your PT on XYZ?"

They're really asking:
- Should I own it? How much? What's the risk? What could go wrong? When will it work?

`/unpack-question [surface-question]` - Reveals underlying questions

### L3: Visualization Suggester
`/suggest-viz [data] [point]` - "You're trying to show X, use Y visualization"

### L4: Headline Optimizer
`/headline-optimize [report]` - Generates options:
- Thesis-driven: Lead with the call
- Catalyst-driven: Lead with the event
- Surprise-driven: Lead with contrarian view

### L5: Complexity Throttle
Match complexity to time available:
- 30 seconds: One sentence thesis
- 2 minutes: Thesis + 3 bullets
- 10 minutes: Full summary
- 1 hour: Deep dive

`/complexity-level [content] [time]` - Adapts detail level

---

## CLUSTER M: The "Continuous Calibration" System

**Core insight:** You can't improve what you don't measure.

### M1: Performance Attribution
When stock moves, why?
`/attribute-performance [ticker] [period]` - Decompose returns

### M2: Conviction-Performance Scatter
Plot: X-axis = Your conviction, Y-axis = Actual returns
`/conviction-calibration-chart` - Visualize over time

### M3: Timing Analysis
Track:
- When you initiated
- When stock inflected
- Time between (lag/lead)

"On turnarounds, I'm typically 6 months early - factor this in"

### M4: Idea Half-Life
How long do your ideas stay relevant?
- Catalyst-driven: Days to weeks
- Business quality: Years
- Turnaround: Quarters

---

## CLUSTER N: The "Risk Management" Framework

**Core insight:** Returns are what you report. Risk is what you live.

### N1: Pre-Mortem Protocol
Before investing, assume it failed. Why?
`/pre-mortem [ticker]` - "We're 2 years in, you lost 50%. What happened?"

For each scenario:
- How likely?
- How could you detect early?
- What would you do?

### N2: Risk Register
```yaml
Company: XYZ
Risks:
  - Type: Execution
    Probability: 30%
    Impact: -20% to stock
    Monitoring: Customer feedback
    Trigger: If preorders <50% of target, exit
```

### N3: Downside Scenario Planning
For every stock:
- Bull case (80th percentile)
- Base case (50th percentile)
- Bear case (20th percentile)
- Disaster case (5th percentile)

`/scenario-ev [ticker]` - Calculate probability-weighted expected value

### N4: Correlation Mapping
`/correlation-analysis [portfolio]` - Are you actually diversified or owning same trade 5 times?

---

## CLUSTER O: The "Speed Layer"

**Core insight:** Some decisions need to be fast.

### O1: Earnings Reaction Function
Stock moves 10% on earnings. You have 30 minutes.

Pre-built template walks through:
1. Headline numbers vs expectations (2 min)
2. Check guidance (2 min)
3. Scan for surprises (3 min)
4. Compare to your model (3 min)
5. Decide: Overreaction, justified, or more to come? (5 min)

`/earnings-rapid-response [ticker]`

### O2: News Event Classifier
`/news-triage [headline]` classifies:
- Ignore: Noise
- Monitor: Potentially relevant
- Analyze: Meaningful, do work
- Act: Material, contact PM immediately

### O3: Quick-Turn Analysis Templates
Common requests:
- M&A announcement → M&A template
- Earnings miss → Earnings triage
- Competitor product launch → Competitive response

`/quick-turn [situation] [ticker]` - Load template

---

## CLUSTER P: The "Long-Term Compounding" Layer

**Core insight:** Great analysts compound knowledge over decades.

### P1: Research Journaling
Daily/weekly: What did I learn?
- About how markets work
- About how I think
- What works in research
- Patterns I'm noticing

`/research-journal [entry]` - After years, search for forgotten insights

### P2: Thesis Evolution Tracker
Track how beliefs change:
- 2020: "E-commerce will grow forever"
- 2023: "Secular growth but slower"

`/belief-timeline [topic]` - See when you're slow to update vs fickle

### P3: Career-Long Pattern Book
Over 20-year career, you'll see many cycles:
- Credit cycles, M&A waves, tech bubbles, regulatory shifts

`/pattern-book [observation]` - Add to long-term library

### P4: Mentor Yourself
Every year: `/letter-to-past-self [years-ago]`
- What I wish I knew then
- What I'd do differently

---

## CLUSTER Q: The "Integration and Workflow" Layer

**Core insight:** All these tools are useless if they don't fit your workflow.

### Q1: Morning Routine Automation
Every morning:
1. `/portfolio-overnight-moves`
2. `/news-digest [sector]`
3. `/calendar-brief [today]`
4. `/priorities [today]`
5. `/set-intentions [today]`

Takes 15 minutes, you're oriented.

### Q2: Context Switching Protocol
When switching companies:
1. `/save-context [current]`
2. `/load-context [new]`
3. Work
4. Repeat

### Q3: Review Rhythms
- Daily: News monitoring
- Weekly: Review each position
- Monthly: Deep dive one position
- Quarterly: Thesis review all
- Annually: Career reflection

`/rhythm-check [frequency]` - Trigger appropriate review

### Q4: State Machine for Research Projects
Track: Idea → Hypothesis → Research → Analysis → Thesis → Communication → Monitoring → Evolution → Closure

`/project-status [ticker]` - Current state, next actions, blockers

---

## CLUSTER R: The "Firm-Wide Infrastructure" Layer

**Core insight:** Individual tools are good. Firm-wide systems are transformative.

### R1: Research Graph (Firm-Wide)
Connect everything:
- Companies → Industries → Themes
- Analysts → Coverage → Expertise
- Research → Questions → Insights

`/firm-graph-query [question]` - "Who knows about vertical software scaling?"

### R2: Collective Intelligence Dashboard
Real-time view:
- Conviction changes
- Emerging themes
- Disagreements
- Blindspots

### R3: Onboarding Acceleration
`/onboard-analyst [name] [sector]`:
1. Firm's research standards
2. Best examples from sector
3. Historical context
4. People to learn from

Compress 6-month learning to 6 weeks.

### R4: Research OS
Everything integrated:
- Data (MCP servers)
- Workflows (slash commands)
- Collaboration (git)
- Learning (pattern libraries)

Becomes competitive advantage in recruiting and retention.

---

## Meta-Principles: System Design

1. **Progressive Disclosure** - Start simple, reveal complexity as analyst gets sophisticated
2. **Taste Development** - Help analysts develop better judgment, not replace it
3. **Compound Learning** - Every piece of research makes next piece better
4. **Social Dynamics** - Some tools private (your edge), some shared (firm culture)
5. **Provenance Everywhere** - Always trace: Where did this come from? Why did I believe this?
6. **Time Arbitrage** - Automate tedious, enhance creative
7. **Failure Analysis** - Most systems optimize for success. Build in retrospectives on misses.

---

## Implementation Philosophy

**Start Small, Compound:**
- Week 1: Basic slash commands
- Month 1: Thesis tracking
- Quarter 1: Calibration/learning
- Year 1: Firm-wide knowledge sharing

**Analyst-Driven, Not IT-Driven:**
- Analysts build their own tools
- IT supports infrastructure
- If IT builds it, it's generic and unloved
- If analysts build it, it's specific and adopted

**Make It Feel Like Thinking, Not Software:**
- Slash commands in normal workflow
- Markdown files you already use
- Git you already know
- Don't build a new app, enhance existing workflow

**Measure Outcomes, Not Activity:**
- Research quality improving?
- Analysts getting better calibrated?
- Firm generating more alpha?

**Build for Emergence:**
- Create primitives, let analysts combine unexpectedly
- Best use case will be one you didn't imagine

**Version Control Your Thinking:**
- Everything in git
- Track evolution, collaborate, learn from history
