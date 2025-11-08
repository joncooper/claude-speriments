# Claude Experiments (claude-speriments)

A collection of experiments exploring advanced prompting techniques, slash commands, and tools for Claude Code.

## About This Repository

This repository contains various experiments and implementations based on research papers, novel prompting techniques, and practical tools to enhance Claude Code usage. Each experiment is self-contained in its own directory with complete documentation.

## Experiments

### 🎲 [Verbalized Sampling](./skills/verbalized-sampling/)

Implementation of the **Verbalized Sampling** technique from the research paper ["Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity"](https://arxiv.org/abs/2510.01171) (arXiv:2510.01171v3).

**What it does:** 12 Claude Code slash commands that dramatically improve output diversity without sacrificing quality.

**Key results:**
- 1.6-2.1x diversity improvement
- 25.7% quality improvement in human evaluations
- Training-free, works via prompting alone

**Commands include:** `/vs`, `/brainstorm`, `/creative-diverse`, `/multi-perspective`, `/dialogue-sim`, `/code-diverse`, and more.

**Status:** ✅ Complete

---

### 🧠 [Cialdini Persuasion Techniques](./skills/cialdini-persuasion/)

Application of **Dr. Robert Cialdini's 7 principles of persuasion** to improve AI agent instruction adherence and task completion.

**What it does:** 10 Claude Code slash commands that apply proven psychological principles to get better results from AI agents.

**Key principles:**
- Reciprocity - agents reciprocate effort with thorough work
- Commitment - early commitments lead to consistent follow-through
- Social Proof - best practices guide agent behavior
- Authority - official sources increase compliance
- Liking - acknowledgment improves cooperation
- Scarcity - urgency focuses attention
- Unity - shared goals create stronger commitment

**Commands include:** `/cialdini-reciprocity`, `/cialdini-commitment`, `/cialdini-authority`, `/cialdini-persuade`, `/cialdini-all`, and more.

**Status:** ✅ Complete

---

### 🐦 [Twitter Data Analyzer](./apps/twitter-data-analyzer/)

A **command-line utility** to download, store, and analyze your Twitter/X data using DuckDB and Google Gemini AI.

**What it does:** Download all your tweets, likes, and bookmarks, store them in a local DuckDB database, and analyze them with AI.

**Key features:**
- Fetch all your Twitter data via Twitter API v2
- Store in fast, queryable DuckDB database
- **Interactive terminal UI** for browsing data with keyboard navigation
- **Profile audit** to identify problematic content before going public
- AI-powered analysis with Google Gemini
- Run custom SQL queries on your data
- Privacy-first: all data stays local

**Commands include:** `init`, `fetch`, `analyze`, `query`, `ask`, `browse` (interactive TUI), `audit` (profile cleaner)

**Status:** ✅ Complete

---

### 📊 [Analyst Workspace](./apps/analyst-workspace/)

**Claude Code-powered tools for equity research analysts** - Give analysts superpowers to do better, deeper, more thorough research.

**What it does:** Autonomous agents and workflows that help equity research analysts systematically research companies, build investment theses, and compound knowledge over time.

**Key features:**
- **`/deep-dive TICKER`** - Autonomous agent performs 30-60 min comprehensive company research
- Saves 4-6 hours of manual research time
- Git-based knowledge management (version control for thinking)
- Systematic analysis frameworks (business model, financials, competition, risks)
- Pattern recognition across companies
- Thesis evolution tracking

**Architecture:**
- Agentic workflows with human checkpoints
- MCP servers for data access (SEC filings, market data)
- Git-first storage (all research version controlled)
- Local-first execution (analyst's machine is source of truth)

**v1.0 Focus:** One workflow that saves 4+ hours of analyst time

**Status:** 🚧 In Development (Planning complete, ready for implementation)

---

## Installation

Each experiment has its own installation instructions in its README. Generally:

```bash
# Clone the repository
git clone https://github.com/joncooper/claude-speriments.git
cd claude-speriments

# Navigate to a skill and follow its README
cd skills/verbalized-sampling
cat README.md
```

## Structure

```
claude-speriments/
├── README.md                    # This file
├── CLAUDE.md                    # Repository guide for Claude Code
├── apps/                        # Collaborative applications built with Claude
│   ├── twitter-data-analyzer/   # Twitter Data Analyzer
│   │   ├── README.md            # Usage guide
│   │   ├── NOTES.md             # Implementation notes
│   │   ├── src/twitter_analyzer/ # Python package
│   │   ├── requirements.txt     # Dependencies
│   │   └── setup.py             # Package setup
│   └── analyst-workspace/       # Analyst Workspace (equity research tools)
│       ├── README.md            # Project overview
│       ├── STRUCTURE.md         # Repository organization
│       ├── .claude/             # Commands, agents, MCP servers
│       ├── coverage/            # Per-company research
│       ├── patterns/            # Cross-company insights
│       └── notes/               # Design documentation
├── skills/                      # Slash commands and skills
│   ├── verbalized-sampling/     # Verbalized Sampling skill
│   │   ├── README.md            # Usage guide
│   │   ├── PAPER_SUMMARY.md     # Research paper summary
│   │   ├── NOTES.md             # Implementation notes
│   │   └── commands/            # 12 slash commands
│   └── cialdini-persuasion/     # Cialdini Persuasion skill
│       ├── README.md            # Usage guide
│       ├── proposal.md          # Detailed principle explanations
│       ├── test-plan.md         # Testing methodology
│       ├── NOTES.md             # Implementation notes
│       └── commands/            # 10 slash commands
└── [future directories]/        # agents/, hooks/, mcp/, etc. as needed
```

## Organization

This repository is organized to support various types of Claude Code experiments:

- **`apps/`** - Collaborative applications built with Claude (e.g., Twitter Data Analyzer, Analyst Workspace)
- **`skills/`** - Slash commands and skills for Claude Code (e.g., Verbalized Sampling, Cialdini Persuasion)
- **Future directories** - As the repository grows, we'll add more specialized directories for different types of Claude Code experiments

See [CLAUDE.md](./CLAUDE.md) for detailed guidance on working with this repository in Claude Code.

## Contributing

This is a personal experimental repository, but if you find these techniques useful and want to suggest improvements or new experiments, feel free to open an issue!

## About Claude Code

[Claude Code](https://claude.com/claude-code) is Anthropic's official CLI for Claude. These experiments extend Claude Code with custom slash commands and tools based on research and novel techniques.

## License

Each experiment may have its own license. Generally, these implementations are provided for educational and research purposes.

## Citation

If you use any of these experiments in research or writing, please cite the original papers and research that inspired them (citations are provided in each experiment's documentation).

---

**Repository maintained by:** [Your details]
**Last updated:** October 2025
