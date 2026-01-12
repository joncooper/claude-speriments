# Claude Experiments (claude-speriments)

A collection of applications, agents, and skills exploring Claude Code's capabilities. Each experiment is self-contained with comprehensive documentation.

## Quick Reference

| Name | Type | Description | Status |
|------|------|-------------|--------|
| [Twitter Data Analyzer](./apps/twitter-data-analyzer/) | App | CLI to audit Twitter profiles with AI analysis | Complete |
| [Analyst Workspace](./apps/analyst-workspace/) | App | Claude-powered equity research tools | In Development |
| [AuctionNinja Finder](./apps/auction-ninja-app/) | App | Find nearby auctions ending soon | Complete |
| [Visual Sound Mirror](./apps/visual-sound-mirror/) | App | Gesture-controlled music instrument | Complete |
| [3D Room Planner](./apps/3d-scan-viewer/) | App | Edit iPhone room scans, add virtual furniture | Complete |
| [Audio Transcription CLI](./apps/audio-transcription-cli/) | App | Local transcription with speaker diarization | Complete |
| [DBT Daily Logger](./apps/dbt-daily-logger/) | App | Flutter app for DBT diary tracking | Complete |
| [Sideshow](./apps/gist-app-highlight/) | App | Annotated markdown viewer with Firebase | Complete |
| [Ghostty Explainer](./apps/ghostty-explainer/) | App | Interactive contributor's guide to Ghostty | Complete |
| [Email-to-LLM](./apps/email-llm-poc/) | App | Email conversations with AI via SendGrid | In Development |
| [Investor DD System](./apps/investor-dd-system/) | App | AI-powered due diligence for hedge funds | Planning |
| [Forensic Accounting](./agents/forensic-accounting/) | Agent | Detect earnings manipulation with Beneish M-Score | Complete |
| [Management Integrity](./agents/equity-mgmt-integrity/) | Agent | Track if management keeps commitments | Complete |
| [Verbalized Sampling](./skills/verbalized-sampling/) | Skill | Research-backed prompts for diverse outputs | Complete |
| [Cialdini Persuasion](./skills/cialdini-persuasion/) | Skill | Psychology-based prompts for better adherence | Complete |

---

## Applications

### Twitter Data Analyzer
CLI to download, store, and analyze your Twitter/X data using DuckDB and Google Gemini AI. Features interactive TUI browser and profile audit for identifying problematic content before going public.
**Status:** Complete | [Learn more](./apps/twitter-data-analyzer/)

### Analyst Workspace
Claude Code-powered tools for equity research analysts. Autonomous agents perform deep-dive company research, saving 4-6 hours of manual work per analysis.
**Status:** In Development | [Learn more](./apps/analyst-workspace/)

### AuctionNinja Nearby Finder
Full-stack web app to find auctions on AuctionNinja.com ending soon within a specified radius. React + Express + Puppeteer with beautiful responsive UI.
**Status:** Complete | [Learn more](./apps/auction-ninja-app/)

### Visual Sound Mirror
Interactive music instrument controlled entirely by hand gestures via webcam. Three modes (ribbons, theremin, drum pads) with 6 visualizations and real-time Web Audio synthesis.
**Status:** Complete | [Try it live](https://joncooper.github.io/claude-speriments/visual-sound-mirror/) | [Learn more](./apps/visual-sound-mirror/)

### 3D Room Planner
Interactive room planning tool for iPhone RoomPlanner scans. Load USDZ files, remove furniture, paint walls, add virtual furniture with real dimensions, and export modified scenes.
**Status:** Complete | [Try it live](https://joncooper.github.io/claude-speriments/3d-scan-viewer/) | [Learn more](./apps/3d-scan-viewer/)

### Audio Transcription CLI
Local audio transcription with multiple model support (Whisper, Granite, Canary), speaker diarization, and voice activity detection. Privacy-first with beautiful CLI output.
**Status:** Complete | [Learn more](./apps/audio-transcription-cli/)

### DBT Daily Logger
Production-ready Flutter app for tracking DBT (Dialectical Behavior Therapy) diary entries. Firebase backend with cloud sync, offline support, and Material Design 3 UI.
**Status:** Complete | [Learn more](./apps/dbt-daily-logger/)

### Sideshow
Client-side web app for creating annotated markdown documents with highlights and sidenotes, inspired by Genius.com. TypeScript + Vite + Firebase with shareable short links.
**Status:** Complete | [Learn more](./apps/gist-app-highlight/)

### Ghostty Explainer
Interactive explainer website for developers wanting to contribute to Ghostty terminal emulator. Covers architecture, key components, design tradeoffs, and Zig primer.
**Status:** Complete | [Learn more](./apps/ghostty-explainer/)

### Email-to-LLM Conversation System
Proof-of-concept enabling turn-by-turn conversations with an LLM via email. Firebase + SendGrid + Gemini with proper threading and context preservation.
**Status:** In Development | [Learn more](./apps/email-llm-poc/)

### Investor Due Diligence Management System
AI-powered system to streamline hedge fund LP due diligence. RAG-based answer drafting, consistency checking, smart routing to SMEs, and complete audit trail.
**Status:** Planning | [Learn more](./apps/investor-dd-system/)

---

## Agents

### Forensic Accounting Agent
Professional-grade forensic accounting analysis using Beneish M-Score to detect earnings manipulation. Identifies red flags across revenue quality, earnings quality, working capital, and leverage. Uses SEC EDGAR MCP server.
**Command:** `/forensic-analyze TICKER:AAPL`
**Status:** Complete | [Learn more](./agents/forensic-accounting/)

### Management Integrity Agent
AI-powered analysis of whether management follows through on commitments. Extracts forward-looking statements from SEC filings, verifies outcomes, and scores credibility with letter grades.
**Command:** `/mgmt-integrity TICKER:AAPL`
**Status:** Complete | [Learn more](./agents/equity-mgmt-integrity/)

---

## Skills

### Verbalized Sampling
12 slash commands implementing research-backed prompting for 1.6-2.1x output diversity improvement. Based on [arXiv:2510.01171](https://arxiv.org/abs/2510.01171).
**Commands:** `/vs`, `/brainstorm`, `/creative-diverse`, `/multi-perspective`, `/code-diverse`, and more
**Status:** Complete | [Learn more](./skills/verbalized-sampling/)

### Cialdini Persuasion Techniques
10 slash commands applying Dr. Robert Cialdini's 7 principles of persuasion to improve AI instruction adherence and task completion.
**Commands:** `/cialdini-reciprocity`, `/cialdini-commitment`, `/cialdini-authority`, `/cialdini-all`, and more
**Status:** Complete | [Learn more](./skills/cialdini-persuasion/)

---

## Getting Started

Each experiment has its own installation instructions. Generally:

```bash
# Clone the repository
git clone https://github.com/joncooper/claude-speriments.git
cd claude-speriments

# Navigate to any experiment
cd apps/twitter-data-analyzer
cat README.md
```

**Python projects** use [uv](https://docs.astral.sh/uv/) (10-100x faster than pip).
**JavaScript/TypeScript projects** use [bun](https://bun.sh/) (10-100x faster than npm).

---

## Contributing

This is a personal experimental repository. If you find these techniques useful and want to suggest improvements, feel free to open an issue!

## About Claude Code

[Claude Code](https://claude.com/claude-code) is Anthropic's official CLI for Claude. These experiments extend Claude Code with custom applications, agents, and skills.

## License

Each experiment may have its own license. Generally provided for educational and research purposes.

---

**Last updated:** January 2026
