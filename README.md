# Claude Experiments (claude-speriments)

A collection of experiments exploring advanced prompting techniques, slash commands, and tools for Claude Code.

## About This Repository

This repository contains various experiments and implementations based on research papers, novel prompting techniques, and practical tools to enhance Claude Code usage. Each experiment is self-contained in its own directory with complete documentation.

## Experiments

### Applications

#### 🐦 [Twitter Data Analyzer](./apps/twitter-data-analyzer/)

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

#### 📊 [Analyst Workspace](./apps/analyst-workspace/)

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

#### 🔨 [AuctionNinja Nearby Finder](./apps/auction-ninja-app/)

A **full-stack web application** to find nearby auctions on AuctionNinja.com that are ending soon.

**What it does:** Search for auctions within a specified radius of your ZIP code that end within a configurable time window, with advanced filtering and sorting.

**Key features:**
- **Location-based filtering** - Find auctions within X miles of any ZIP code
- **Time-based filtering** - Show only auctions ending within specified hours
- **Headless browser scraping** - Uses Puppeteer to fetch real auction data
- **Beautiful, responsive UI** - Modern React interface with Tailwind CSS
- **Advanced search** - Filter by keyword, category, distance, or time
- **Mobile-optimized** - Works seamlessly on phones and tablets
- **Smart caching** - 5-minute cache for better performance

**Tech stack:** React + Vite, Node.js + Express, Puppeteer, Tailwind CSS

**Status:** ✅ Complete

---

#### 🎨 [Visual Sound Mirror](./apps/visual-sound-mirror/)

An **interactive music instrument** controlled entirely by hand gestures. No keyboard, mouse, or touch required - just your hands in front of the webcam.

**What it does:** Uses AI-powered hand tracking (MediaPipe) to turn hand gestures into music across three distinct modes with 6 dynamic visualizations.

**Three Instrument Modes:**
- **🎨 Ribbons Mode**: Flowing finger trails with filter/delay control - touch fingertips for harmonic chords
- **🎵 Theremin Mode**: Play melodies with hand position (X=pitch, Y=filter, spread=vibrato)
- **🥁 Sample Pads Mode**: 25 drum pads auto-calibrated to your hand geometry - tap forward to trigger

**Key features:**
- Completely hands-free: gesture-based mode switching (1/2/5 fingers)
- Real-time Web Audio synthesis (25+ drum sounds, theremin, effects)
- 6 visualization modes (particle fountain, audio blooms, fluid dynamics, orbits, kaleidoscope, temporal echoes)
- Virtual rotary knobs controlled by pinch gestures
- Musical scale quantization (pentatonic, major, minor, blues, etc.)
- Privacy-first: all processing happens locally in browser
- Single-file monolithic architecture (4,506 lines) - no build step required

**Try it:** [Live demo on GitHub Pages](https://joncooper.github.io/claude-speriments/visual-sound-mirror/) or open `index.html` locally

**Status:** ✅ Complete (v6.7.0)

---

#### 💼 [Investor Due Diligence Management System](./apps/investor-dd-system/)

An **AI-powered system** to streamline hedge fund LP due diligence processes, transforming time-consuming DDQ completion into an efficient, consistent, and auditable workflow.

**What it does:** Manages the two core DD workflows - initial onboarding DDQs (100-500 questions) and periodic/recurring DD (annual updates, ad-hoc requests) - using LLMs, RAG, and agentic approaches.

**Key features:**
- **AI-Powered Drafting**: Generate answers using RAG over firm documents with 70%+ auto-draft rate
- **Consistency Engine**: Automatic detection of contradictions across all investor communications
- **Smart Routing**: Questions auto-classified and routed to appropriate subject matter experts
- **Master Answer Library**: Build institutional knowledge that improves over time
- **Complete Audit Trail**: Track who said what, when, to whom for compliance

**Architecture:**
- RAG pipeline with document embeddings and semantic search
- Multi-LLM support (Claude + OpenAI) for reliability
- PostgreSQL with pgvector for structured + vector data
- FastAPI backend, Next.js frontend
- Human-in-the-loop approval workflows

**Target outcomes:**
- Initial DDQ: 2-4 weeks → 3-5 days
- Time per question: 15-30 min → 2-5 min
- Consistency rate: >99%

**Status:** 📋 Planning Phase (comprehensive plan complete)

---

#### 🏠 [3D Room Planner](./apps/3d-scan-viewer/)

An **interactive room planning tool** for iPhone RoomPlanner scans. Remove furniture, paint walls, and try virtual furniture arrangements with real dimensions.

**What it does:** Load USDZ room scans, edit them by removing/painting/adding furniture, and export modified versions for visualization and planning.

**Room Editing Features:**
- **Object Classification** - Automatically identifies walls, floor, and furniture from USDZ metadata
- **Furniture Removal** - Click to select and delete furniture objects
- **Wall Painting** - Change wall colors with a color picker
- **Virtual Furniture** - Add furniture blocks with real dimensions (meters)
- **Transform Controls** - Move, rotate, and scale virtual furniture
- **Export** - Save modified rooms as GLTF files

**Supported Formats:**
- **Primary**: USDZ (iPhone RoomPlanner with metadata)
- **Also supports**: FBX, OBJ, GLB/GLTF, PLY

**Key features:**
- **View & Edit Modes** - Toggle between viewing and editing
- **Object Selection** - Click objects to select, see classification (wall/floor/furniture)
- **Furniture Presets** - Quick-add common furniture (sofa, table, chair, bed)
- **Real Dimensions** - Input actual sizes in meters for accurate planning
- **Keyboard Shortcuts** - T/R/S for translate/rotate/scale, Delete to remove, ESC to deselect
- **Auto-framing** - Rooms automatically centered and scaled
- **Performance-optimized** - Smooth 60fps rendering

**Tech stack:** Three.js, TypeScript, Vite, Bun

**Try it:** [Live demo on GitHub Pages](https://joncooper.github.io/claude-speriments/3d-scan-viewer/)

**Status:** ✅ Complete (v2.0.0)

---

#### 🎙️ [Audio Transcription CLI](./apps/audio-transcription-cli/)

A **powerful command-line tool** for transcribing audio files using local AI models with speaker diarization and voice activity detection.

**What it does:** Transcribe m4a, mp3, wav, and other audio files using state-of-the-art local models with automatic speaker detection and beautiful CLI output.

**Multi-Model Support:**
- **Whisper Large v3 Turbo** (default) - 8x faster, ~6GB VRAM, best for quick transcriptions
- **IBM Granite Speech 3.3 8B** - Highest accuracy, multilingual (EN/FR/DE/ES/PT), ~16GB VRAM
- **NVIDIA Canary-Qwen 2.5B** - Very fast (418 RTFx), English-only, ~10GB VRAM

**Key features:**
- **Speaker Diarization** - Automatically detect and label different speakers using pyannote.audio
- **Voice Activity Detection (VAD)** - Skip silent portions for faster processing
- **Beautiful CLI** - Rich progress bars, formatted output, model comparison table
- **Markdown Output** - Formatted transcripts with timestamps and speaker labels
- **Privacy-First** - All processing happens locally, no data sent to cloud services
- **GPU & CPU Support** - Automatic device detection with memory optimization

**Usage examples:**
```bash
# Quick transcription
uv run python -m src audio.m4a

# With speaker diarization
uv run python -m src interview.m4a --diarize -o transcript.md

# Choose model
uv run python -m src audio.m4a --model granite --language es
```

**Tech stack:** Python 3.11+, typer + rich, faster-whisper, transformers, pyannote.audio, torch

**Status:** ✅ Complete

---

### Agents

#### 🔍 [Forensic Accounting Agent](./agents/forensic-accounting/)

**Professional-grade forensic accounting analysis** - Detect aggressive accounting practices and potential earnings manipulation in publicly-traded companies.

**What it does:** Acts as a senior forensic accountant to analyze companies for accounting red flags, calculate the Beneish M-Score, and generate comprehensive reports suitable for equity research analysts.

**Key features:**
- **Beneish M-Score Analysis** - Detects earnings manipulation with ~76% accuracy using 8 financial ratios
- **Comprehensive Red Flag Detection** - Identifies issues across revenue quality, earnings quality, working capital, assets, and leverage
- **Trend Analysis** - Shows if accounting policies are becoming more or less aggressive over time
- **Professional Reports** - Generates detailed markdown reports with executive summaries, findings, and recommendations
- **MCP Integration** - Uses SEC EDGAR MCP server for robust financial data fetching
- **5 Years of Analysis** - Examines historical patterns across multiple fiscal years

**Red flags detected:**
- Days Sales Outstanding (DSO) trends
- Revenue vs. accounts receivable divergence
- Operating cash flow vs. net income gaps
- Inventory buildup and liquidity deterioration
- Soft asset growth and capitalization issues
- Margin deterioration and leverage increases

**Command:** `/forensic-analyze TICKER:AAPL`

**Status:** ✅ Complete

---

#### 📊 [Management Integrity Agent](./agents/equity-mgmt-integrity/)

**AI-powered management credibility analysis** - Analyze whether public company management follows through on their commitments.

**What it does:** Answers the critical investor question "Does management do what they say they're going to do?" by extracting commitments from SEC filings, verifying outcomes, and scoring management credibility.

**Key features:**
- **AI-Powered Commitment Extraction** - Uses Claude to identify specific, verifiable commitments from MD&A sections (financial targets, capital allocation, strategic initiatives, etc.)
- **AI-Powered Outcome Verification** - Analyzes subsequent filings to determine if promises were kept (fulfilled, partially fulfilled, not fulfilled, abandoned)
- **Quantitative Scoring** - 0-100 credibility scores with letter grades (A+ to F) based on fulfillment rates
- **Red Flag Detection** - Identifies declining specificity, high miss rates, abandoned initiatives, and systematic underperformance
- **Time Trend Analysis** - Shows if credibility is improving, declining, or stable (declining is a major warning sign)
- **Professional Reports** - Comprehensive markdown reports with evidence, category breakdowns, and investment implications

**Analysis includes:**
- ~10-30 commitments extracted per company
- Category-specific performance (financial, capital allocation, strategic, operational, product)
- Evidence quotes from filings
- Variance calculations for quantitative targets
- Investment risk assessment

**Command:** `/mgmt-integrity TICKER:AAPL`

**Status:** ✅ Complete

---

### Skills

#### 🎲 [Verbalized Sampling](./skills/verbalized-sampling/)

Implementation of the **Verbalized Sampling** technique from the research paper ["Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity"](https://arxiv.org/abs/2510.01171) (arXiv:2510.01171v3).

**What it does:** 12 Claude Code slash commands that dramatically improve output diversity without sacrificing quality.

**Key results:**
- 1.6-2.1x diversity improvement
- 25.7% quality improvement in human evaluations
- Training-free, works via prompting alone

**Commands include:** `/vs`, `/brainstorm`, `/creative-diverse`, `/multi-perspective`, `/dialogue-sim`, `/code-diverse`, and more.

**Status:** ✅ Complete

---

#### 🧠 [Cialdini Persuasion Techniques](./skills/cialdini-persuasion/)

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
│   ├── analyst-workspace/       # Analyst Workspace (equity research tools)
│   │   ├── README.md            # Project overview
│   │   ├── STRUCTURE.md         # Repository organization
│   │   ├── .claude/             # Commands, agents, MCP servers
│   │   ├── coverage/            # Per-company research
│   │   ├── patterns/            # Cross-company insights
│   │   └── notes/               # Design documentation
│   ├── auction-ninja-app/       # AuctionNinja Nearby Finder
│   │   ├── README.md            # Usage guide
│   │   ├── NOTES.md             # Implementation notes
│   │   ├── ICEBOX.md            # Future enhancements
│   │   ├── backend/             # Express + Puppeteer API server
│   │   ├── frontend/            # React + Vite + Tailwind UI
│   │   └── package.json         # Root scripts
│   ├── audio-transcription-cli/ # Audio Transcription CLI
│   │   ├── README.md            # Usage guide
│   │   ├── QUICKSTART.md        # 5-minute setup guide
│   │   ├── NOTES.md             # Implementation notes
│   │   ├── ICEBOX.md            # Future enhancements
│   │   ├── src/                 # Python package
│   │   ├── examples/            # Usage examples
│   │   ├── pyproject.toml       # Project metadata & dependencies
│   │   └── requirements.txt     # Legacy pip support
│   ├── investor-dd-system/      # Investor DD Management System (planning phase)
│   │   ├── README.md            # Project overview
│   │   └── PLAN.md              # Comprehensive product and technical plan
│   └── visual-sound-mirror/     # Interactive art piece with camera and audio
│       ├── README.md            # Usage guide
│       ├── NOTES.md             # Implementation notes
│       ├── ICEBOX.md            # Future enhancements
│       ├── index.html           # Main application
│       ├── app.js               # Application logic
│       └── styles.css           # Styling
├── agents/                      # Agent configurations and workflows
│   ├── forensic-accounting/     # Forensic Accounting Agent
│   │   ├── README.md            # Usage guide and installation
│   │   ├── TESTING.md           # Testing instructions
│   │   ├── commands/            # Slash command
│   │   ├── lib/                 # Analysis library (Beneish, red flags, etc.)
│   │   ├── data/                # MCP-gathered SEC data
│   │   └── reports/             # Generated analysis reports
│   └── equity-mgmt-integrity/   # Management Integrity Agent
│       ├── README.md            # Usage guide and installation
│       ├── TESTING.md           # Testing instructions
│       ├── commands/            # Slash command
│       ├── lib/                 # Analysis library (extractors, trackers, scorers)
│       ├── data/                # Analysis data and reports
│       └── example_analysis.py  # Programmatic usage example
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
└── [future directories]/        # hooks/, mcp/, etc. as needed
```

## Organization

This repository is organized to support various types of Claude Code experiments:

- **`apps/`** - Collaborative applications built with Claude (e.g., Twitter Data Analyzer, Analyst Workspace, AuctionNinja Nearby Finder, Audio Transcription CLI, Investor DD System, Visual Sound Mirror)
- **`agents/`** - Agent configurations and workflows (e.g., Forensic Accounting Agent, Management Integrity Agent)
- **`skills/`** - Slash commands and skills for Claude Code (e.g., Verbalized Sampling, Cialdini Persuasion)
- **Future directories** - As the repository grows, we'll add more specialized directories (hooks/, mcp/, etc.)

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

**Last updated:** January 2026
