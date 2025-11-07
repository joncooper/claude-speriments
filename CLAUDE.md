# Claude Code Repository Guide

This document provides guidance for working with the `claude-speriments` repository in Claude Code. It explains the repository structure, conventions, and best practices for adding new experiments and applications.

## Repository Purpose

This repository is a collection of experiments exploring Claude Code's capabilities, including:
- Collaborative applications built with Claude
- Novel prompting techniques based on research papers
- Custom slash commands and skills
- Agent configurations and workflows
- Tools and utilities that enhance Claude Code usage

## Repository Structure

```
claude-speriments/
├── README.md                    # Public-facing documentation
├── CLAUDE.md                    # This file - guidance for Claude Code
├── apps/                        # Collaborative applications
│   └── twitter-data-analyzer/   # Full-featured CLI applications
├── skills/                      # Slash commands and skills
│   ├── verbalized-sampling/     # Prompting technique experiments
│   └── cialdini-persuasion/     # Prompting technique experiments
└── [future directories]/        # agents/, hooks/, mcp/, etc.
```

### Directory Organization

#### `apps/` - Collaborative Applications

**Purpose:** Full-featured applications built collaboratively with Claude Code.

**What goes here:**
- Complete CLI tools and utilities
- Web applications
- Desktop applications
- Scripts that solve specific problems
- Production-ready or near-production code

**Structure:**
```
apps/
└── app-name/
    ├── README.md              # Usage guide
    ├── NOTES.md               # Implementation notes
    ├── ICEBOX.md              # Future enhancement backlog
    ├── src/                   # Source code
    ├── tests/                 # Tests (if applicable)
    ├── docs/                  # Additional documentation
    └── pyproject.toml         # Dependencies (Python projects)
```

**Examples:**
- `apps/twitter-data-analyzer/` - CLI tool to audit Twitter profiles

**Best practices:**
- Each app should be self-contained with its own README
- Use modern package managers (uv for Python, etc.)
- Include comprehensive documentation
- Store prompts in external files (prompts/ directory)
- Maintain an ICEBOX.md for future ideas

#### `skills/` - Slash Commands and Skills

**Purpose:** Slash commands and skills for Claude Code, including prompting techniques and research implementations.

**What goes here:**
- Slash command collections
- Prompting technique demonstrations
- Research paper implementations
- Technique showcases
- Custom skills for Claude Code

**Structure:**
```
skills/
└── skill-name/
    ├── README.md              # Usage guide
    ├── NOTES.md               # Implementation notes
    ├── PAPER_SUMMARY.md       # Research summary (if applicable)
    ├── commands/              # Slash commands
    │   ├── command1.md
    │   └── command2.md
    └── examples/              # Example outputs
```

**Examples:**
- `skills/verbalized-sampling/` - Implements research on improving LLM diversity
- `skills/cialdini-persuasion/` - Applies psychological principles to prompts

**Best practices:**
- Document the research or technique being explored
- Provide clear examples and usage instructions
- Include citations for research papers
- Test commands before committing

#### Future Directories

As the repository grows, we'll add:

- **`agents/`** - Agent configurations and workflows
  - Specialized agent setups for specific tasks
  - Agent orchestration patterns

- **`hooks/`** - Session hooks and automation
  - SessionStart hooks for project setup
  - Custom hook implementations

- **`mcp/`** - Model Context Protocol servers
  - Custom MCP implementations
  - Tool servers and integrations

## Working with This Repository

### Adding a New Application

1. Create a new directory under `apps/`
2. Set up the project structure with README, NOTES, and ICEBOX
3. Use modern tooling (uv for Python, etc.)
4. Store prompts in `prompts/` subdirectory
5. Include comprehensive documentation
6. Commit with descriptive messages

### Adding a New Skill

1. Create a new directory under `skills/` with a descriptive name
2. Add README with overview and usage
3. Add NOTES.md with implementation details
4. Create `commands/` directory for slash commands
5. Include examples and test cases
6. Document any research or techniques used

### Conventions

#### Python Projects
- Use **uv** as the primary package manager (10-100x faster than pip)
- Include both `pyproject.toml` (modern) and `requirements.txt` (legacy support)
- Use `.python-version` to specify Python version
- Store configuration in `.env` files (with `.env.example` templates)
- Follow PEP 8 style guidelines

#### Documentation
- Every project/experiment needs a README.md
- Use NOTES.md for implementation details and decisions
- Use ICEBOX.md for future enhancement backlogs
- Store prompts in separate `.md` files for easy iteration
- Include QUICKSTART.md for complex projects

#### Git Practices
- Use descriptive commit messages
- Develop on feature branches (claude/*)
- Reference the session in branch names
- Push regularly to track progress
- Keep working tree clean between features

#### LLM Integration
- Prefer external prompt files over inline prompts
- Add observability/logging for AI-powered features
- Use DIY approaches (DuckDB, SQLite) before external services
- Document API keys and configuration clearly
- Consider local LLM alternatives for privacy

## Common Patterns

### Project Setup
```bash
# For Python projects
cd apps/new-project/
uv init
uv add package-name
uv run script.py
```

### Prompt Management
```
prompts/
├── README.md              # Guide to customizing prompts
├── system_prompt.md       # Main system prompt
├── analysis_prompt.md     # Specific task prompts
└── templates/             # Reusable templates
```

### Observability
- Use local databases (DuckDB, SQLite) for logging
- Track: timestamps, API calls, tokens, latency, errors
- Build simple CLI commands to view logs (`logs`, `stats`)
- Prefer DIY over external services (Langfuse, Phoenix)

### Testing
- Test slash commands manually before committing
- Include example inputs/outputs in documentation
- For apps, consider adding automated tests
- Document known issues and limitations

## Tips for Claude Code Sessions

1. **Start with context:** Read README.md and CLAUDE.md at session start
2. **Check structure:** Use `ls` to understand the current organization
3. **Read before edit:** Always read files before modifying them
4. **Document decisions:** Update NOTES.md with important implementation choices
5. **Track progress:** Use TodoWrite for multi-step tasks
6. **Commit often:** Small, focused commits with clear messages
7. **Update docs:** Keep README and other docs in sync with code
8. **Think about users:** Applications should be well-documented and easy to use

## Repository Evolution

This repository will continue to evolve as we:
- Build more collaborative applications
- Explore new prompting techniques
- Test Claude Code features (skills, agents, MCP)
- Implement research papers and novel ideas
- Create reusable tools and utilities

The structure is designed to be flexible and accommodate new types of experiments while maintaining clear organization.

## Questions and Feedback

If you have questions about where something should go or how to organize a new experiment, consider:
- Is it a complete application? → `apps/`
- Is it a prompting technique or slash commands? → `skills/` directory
- Is it an agent configuration? → Future `agents/` directory
- Is it configuration or tooling? → Consider if it belongs in an existing project

When in doubt, ask the user for guidance on organization.

---

**Last updated:** November 2025
