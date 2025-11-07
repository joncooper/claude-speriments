# Claude Experiments (claude-speriments)

A collection of experiments exploring advanced prompting techniques, slash commands, and tools for Claude Code.

## About This Repository

This repository contains various experiments and implementations based on research papers, novel prompting techniques, and practical tools to enhance Claude Code usage. Each experiment is self-contained in its own directory with complete documentation.

## Experiments

### 🎲 [Verbalized Sampling](./verbalized-sampling/)

Implementation of the **Verbalized Sampling** technique from the research paper ["Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity"](https://arxiv.org/abs/2510.01171) (arXiv:2510.01171v3).

**What it does:** 12 Claude Code slash commands that dramatically improve output diversity without sacrificing quality.

**Key results:**
- 1.6-2.1x diversity improvement
- 25.7% quality improvement in human evaluations
- Training-free, works via prompting alone

**Commands include:** `/vs`, `/brainstorm`, `/creative-diverse`, `/multi-perspective`, `/dialogue-sim`, `/code-diverse`, and more.

**Status:** ✅ Complete

---

### 🧠 [Cialdini Persuasion Techniques](./cialdini-persuasion/)

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

### 🐦 [Twitter Data Analyzer](./twitter-data-analyzer/)

A **command-line utility** to download, store, and analyze your Twitter/X data using DuckDB and Google Gemini AI.

**What it does:** Download all your tweets, likes, and bookmarks, store them in a local DuckDB database, and analyze them with AI.

**Key features:**
- Fetch all your Twitter data via Twitter API v2
- Store in fast, queryable DuckDB database
- **Interactive terminal UI** for browsing data with keyboard navigation
- AI-powered analysis with Google Gemini
- Run custom SQL queries on your data
- Privacy-first: all data stays local

**Commands include:** `init`, `fetch`, `analyze`, `query`, `ask`, `browse` (interactive TUI)

**Status:** ✅ Complete

---

## Installation

Each experiment has its own installation instructions in its README. Generally:

```bash
# Clone the repository
git clone https://github.com/joncooper/claude-speriments.git
cd claude-speriments

# Navigate to an experiment and follow its README
cd verbalized-sampling
cat README.md
```

## Structure

```
claude-speriments/
├── README.md                    # This file
├── verbalized-sampling/         # Verbalized Sampling experiment
│   ├── README.md                # Usage guide
│   ├── PAPER_SUMMARY.md         # Research paper summary
│   ├── NOTES.md                 # Implementation notes
│   └── commands/                # 12 slash commands
├── cialdini-persuasion/         # Cialdini Persuasion experiment
│   ├── README.md                # Usage guide
│   ├── proposal.md              # Detailed principle explanations
│   ├── test-plan.md             # Testing methodology
│   ├── NOTES.md                 # Implementation notes
│   └── commands/                # 10 slash commands
├── twitter-data-analyzer/       # Twitter Data Analyzer
│   ├── README.md                # Usage guide
│   ├── NOTES.md                 # Implementation notes
│   ├── src/twitter_analyzer/    # Python package
│   ├── requirements.txt         # Dependencies
│   └── setup.py                 # Package setup
└── [future experiments]/
```

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
