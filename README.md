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
│   ├── README.md
│   ├── PAPER_SUMMARY.md
│   ├── NOTES.md
│   └── commands/               # 12 slash commands
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
