# Claude Code Repository Guide

This document provides guidance for working with the `claude-speriments` repository in Claude Code. It explains the repository structure, conventions, and best practices for adding new experiments and applications.

**Audience:** Claude Code sessions working in this repository. Read this file at the start of any session.

## Table of Contents

- [Repository Purpose](#repository-purpose)
- [Repository Structure](#repository-structure)
- [Directory Organization](#directory-organization)
- [README Documentation Strategy](#readme-documentation-strategy)
- [Project Status Conventions](#project-status-conventions)
- [Standard Project Files](#standard-project-files)
- [Working with This Repository](#working-with-this-repository)
- [Conventions by Language](#conventions-by-language)
- [Common Patterns](#common-patterns)
- [Tips for Claude Code Sessions](#tips-for-claude-code-sessions)
- [Questions and Feedback](#questions-and-feedback)

---

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
├── README.md                    # Repository index (quick reference table + brief descriptions)
├── CLAUDE.md                    # This file - guidance for Claude Code
├── apps/                        # Collaborative applications
│   ├── twitter-data-analyzer/   # CLI tool to audit Twitter profiles
│   ├── visual-sound-mirror/     # Gesture-controlled music instrument
│   ├── 3d-scan-viewer/          # 3D room planner for iPhone scans
│   ├── dbt-daily-logger/        # Flutter DBT diary tracker
│   └── ...                      # And more
├── agents/                      # Agent configurations and workflows
│   ├── forensic-accounting/     # Beneish M-Score analysis
│   └── equity-mgmt-integrity/   # Management credibility tracking
├── skills/                      # Slash commands and skills
│   ├── verbalized-sampling/     # Prompting technique experiments
│   └── cialdini-persuasion/     # Prompting technique experiments
├── docs/                        # GitHub Pages deployments
└── [future directories]/        # hooks/, mcp/, etc.
```

## Directory Organization

### `apps/` - Collaborative Applications

**Purpose:** Full-featured applications built collaboratively with Claude Code.

**What goes here:**
- Complete CLI tools and utilities
- Web applications (client-side or full-stack)
- Mobile applications (Flutter, React Native)
- Desktop applications
- Scripts that solve specific problems

**Structure:**
```
apps/app-name/
├── README.md              # Comprehensive usage guide
├── NOTES.md               # Implementation decisions and learnings
├── ICEBOX.md              # Future enhancement backlog
├── src/                   # Source code
├── prompts/               # External prompt files (if AI-powered)
├── tests/                 # Tests (if applicable)
└── [config files]         # pyproject.toml, package.json, pubspec.yaml, etc.
```

**Examples:**
- `apps/twitter-data-analyzer/` - Python CLI with DuckDB and Gemini
- `apps/gist-app-highlight/` - TypeScript + Vite + Firebase web app
- `apps/dbt-daily-logger/` - Flutter mobile app with Firebase

**Best practices:**
- Each app should be self-contained with its own README
- Use modern package managers (uv for Python, bun for JS/TS, flutter for Dart)
- Store prompts in external files (`prompts/` directory) for easy iteration
- Include `.env.example` for any required configuration
- Maintain ICEBOX.md for future ideas that arise during development

### `skills/` - Slash Commands and Skills

**Purpose:** Slash commands and skills for Claude Code, including prompting techniques and research implementations.

**What goes here:**
- Slash command collections
- Prompting technique demonstrations
- Research paper implementations
- Technique showcases

**Structure:**
```
skills/skill-name/
├── README.md              # Usage guide with examples
├── NOTES.md               # Implementation notes
├── PAPER_SUMMARY.md       # Research summary (if based on a paper)
├── commands/              # Slash command files
│   ├── command1.md
│   └── command2.md
└── examples/              # Example outputs
```

**Examples:**
- `skills/verbalized-sampling/` - Research paper implementation (arXiv:2510.01171)
- `skills/cialdini-persuasion/` - Psychology-based prompting techniques

**Best practices:**
- Document the research or technique being explored
- Provide clear examples and usage instructions
- Include citations for research papers
- Test commands manually before committing
- Show before/after comparisons when demonstrating techniques

### `agents/` - Agent Configurations

**Purpose:** Specialized agents for specific analytical or research tasks, typically using MCP servers for data access.

**What goes here:**
- Agents that use MCP servers for external data
- Multi-step analytical workflows
- Slash commands that invoke complex agent behavior
- Domain-specific analysis tools

**Structure:**
```
agents/agent-name/
├── README.md              # Comprehensive usage guide with examples
├── TESTING.md             # Testing instructions and sample tickers/inputs
├── commands/              # Slash commands that invoke the agent
├── lib/                   # Python analysis library (if applicable)
└── data/                  # Generated reports and cached data
```

**Examples:**
- `agents/forensic-accounting/` - SEC EDGAR analysis with Beneish M-Score
- `agents/equity-mgmt-integrity/` - Management credibility tracking from filings

**Best practices:**
- Document MCP server dependencies clearly in README
- Include sample inputs for testing (e.g., known-good ticker symbols)
- Store generated reports in `data/` with clear naming conventions
- Provide TESTING.md with step-by-step verification instructions
- Handle API errors gracefully with informative messages

### Future Directories

As the repository grows, we'll add:

- **`hooks/`** - Session hooks and automation (SessionStart, etc.)
- **`mcp/`** - Custom Model Context Protocol server implementations

---

## README Documentation Strategy

This repository uses a **two-tier documentation approach**:

### Main README (Repository Index)
The root `README.md` serves as a **quick reference index**, not comprehensive documentation:

- **Quick Reference Table** - Scannable table with name, type, one-line description, status
- **Brief Descriptions** - 2-3 sentences per project with status and "Learn more" link
- **No Feature Lists** - Detailed features belong in project READMEs
- **No Directory Trees** - Avoid redundant structure documentation

**Rationale:** The main README helps users quickly find what they're looking for and navigate to project-specific documentation. It's an index, not a manual.

### Project READMEs (Comprehensive Documentation)
Each project's `README.md` contains **all the details**:

- Complete feature lists and capabilities
- Installation and setup instructions
- Usage examples and commands
- Technical architecture and design decisions
- Troubleshooting guides

**Rationale:** Detailed documentation lives where the code lives. This keeps docs in sync and makes projects self-contained.

### When Adding a New Project

1. **Create a comprehensive project README** with all details users need
2. **Add a brief entry to the main README**:
   - One row in the Quick Reference table
   - One short section (2-3 sentences + status + link)
3. **Never duplicate** detailed information between the two

### README Maintenance

- When updating features, update the **project README only**
- The main README description should rarely change after initial creation
- Update the main README's "Last updated" date when adding new projects

---

## Project Status Conventions

Use these status labels consistently across READMEs:

| Status | Meaning |
|--------|---------|
| **Planning** | Idea documented, not yet started. May have design docs or specs. |
| **Initial Spike** | First working version in progress. Core functionality being built. |
| **Iterating** | Working version exists. Actively improving based on usage. |
| **Complete** | Stable, documented, ready for use. May receive maintenance updates. |

Update status in both the Quick Reference table and the project section when it changes.

---

## Standard Project Files

### NOTES.md - Implementation Decisions

Use NOTES.md to document:
- **Why** decisions were made (not just what)
- Trade-offs considered and rejected approaches
- Lessons learned during implementation
- Technical debt acknowledged but deferred
- Links to relevant documentation or research

This creates institutional memory for future sessions.

### ICEBOX.md - Future Ideas

Use ICEBOX.md to capture:
- Feature ideas that arose during development
- Nice-to-haves that aren't critical
- User requests for future consideration
- Refactoring ideas for later
- Integration possibilities

This prevents scope creep while preserving good ideas.

---

## Working with This Repository

### Adding a New Application

1. Create directory under `apps/` with kebab-case name
2. Initialize with appropriate tooling (see [Conventions by Language](#conventions-by-language))
3. Create README.md with comprehensive documentation
4. Create NOTES.md and ICEBOX.md (can start empty)
5. Add brief entry to main README (table row + short section)
6. Commit with descriptive message

### Adding a New Skill

1. Create directory under `skills/` with descriptive name
2. Create README.md with overview, installation, and usage
3. Create `commands/` directory with slash command `.md` files
4. Add NOTES.md documenting the technique or research
5. Include examples showing the technique in action
6. Add brief entry to main README
7. Test commands before committing

### Adding a New Agent

1. Create directory under `agents/` with descriptive name
2. Document MCP server dependencies in README.md
3. Create `commands/` directory with slash command files
4. Add TESTING.md with verification steps and sample inputs
5. Create `lib/` for any Python analysis code
6. Create `data/` directory for generated reports (gitignore large files)
7. Add brief entry to main README
8. Test with known-good inputs before committing

---

## Conventions by Language

### Python Projects

**Package manager:** [uv](https://docs.astral.sh/uv/) (10-100x faster than pip)

```bash
cd apps/new-project/
uv init
uv add package-name
uv run python script.py
```

**Standards:**
- `pyproject.toml` for dependencies and project config
- `.python-version` to pin Python version
- `.env` for configuration (with `.env.example` template)
- Follow PEP 8 style guidelines

### JavaScript/TypeScript Projects

**Package manager:** [bun](https://bun.sh/) (all-in-one: package manager + runtime + bundler)

```bash
cd apps/
bun create vite new-project --template vanilla-ts
cd new-project/
bun install
bun add firebase marked        # Example dependencies
bun add -d @types/marked       # Dev dependencies
bun run dev                    # Development server
bun run build                  # Production build
```

**Standards:**
- TypeScript preferred for type safety
- Vite for web applications
- `package.json` + `bun.lock` for dependencies
- `.env` for configuration (gitignored) with `.env.example`

### Flutter/Dart Projects

**Package manager:** Flutter SDK

```bash
flutter create new_project
cd new_project/
flutter pub add firebase_core
flutter pub add cloud_firestore
flutter run
```

**Standards:**
- `pubspec.yaml` for dependencies
- Follow Flutter style guide
- Use Material Design 3 components
- Separate business logic from UI

### Other Languages

For languages not covered above, follow the ecosystem's standard practices and document any special setup in the project README.

---

## Common Patterns

### Prompt Management

For AI-powered applications, store prompts externally:

```
prompts/
├── README.md              # Guide to customizing prompts
├── system_prompt.md       # Main system prompt
├── analysis_prompt.md     # Task-specific prompts
└── templates/             # Reusable templates
```

This allows prompt iteration without code changes.

### Observability for AI Features

- Use local databases (DuckDB, SQLite) for logging
- Track: timestamps, API calls, tokens used, latency, errors
- Build simple CLI commands to view logs (`logs`, `stats`)
- Prefer DIY over external services initially

### Deploying to GitHub Pages

Web apps can be deployed to GitHub Pages via the `/docs` directory:

1. **Develop** in `apps/app-name/`
2. **Build** to `/docs/app-name/` (use a deploy script or build config)
3. **Update** `/docs/index.html` to list the new experiment

See `apps/visual-sound-mirror/deploy-to-pages.sh` for an example deploy script.

---

## Tips for Claude Code Sessions

1. **Start with context:** Read README.md and CLAUDE.md at session start
2. **Check structure:** Use `ls` to understand current organization
3. **Read before edit:** Always read files before modifying them
4. **Document decisions:** Update NOTES.md with important implementation choices
5. **Track progress:** Use TodoWrite for multi-step tasks
6. **Commit often:** Small, focused commits with clear messages
7. **Update docs:** Keep README current with code changes
8. **Capture ideas:** Add future ideas to ICEBOX.md rather than implementing immediately

---

## Questions and Feedback

If you have questions about where something should go:

| Type | Location |
|------|----------|
| Complete application | `apps/` |
| Slash commands or prompting techniques | `skills/` |
| Agent with MCP integration | `agents/` |
| Session hooks | Future `hooks/` |
| Custom MCP server | Future `mcp/` |

When in doubt, ask the user for guidance on organization.

---

**Last updated:** January 2026
