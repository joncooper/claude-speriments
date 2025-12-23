# Ghostty Explainer

An interactive explainer website for developers who want to understand and contribute to [Ghostty](https://github.com/ghostty-org/ghostty), a fast, native, feature-rich terminal emulator written in Zig.

## Features

- **Architecture Tour**: High-level overview of Ghostty's architecture, directory structure, and threading model
- **Key Components**: Deep dive into Surface, Terminal, Parser, Screen, Renderer, and Font systems
- **Design & Tradeoffs**: Understanding the philosophy behind Ghostty's design decisions
- **Libraries**: Comprehensive list of Zig and C libraries used
- **Zig Primer**: Quick introduction to Zig concepts you'll encounter in the codebase
- **Getting Started**: How to set up your development environment and find issues to work on

## Development

This is a simple static site with no build step.

```bash
# Preview locally
cd apps/ghostty-explainer
python3 -m http.server 8000
# Visit http://localhost:8000

# Deploy to GitHub Pages
./deploy-to-pages.sh
```

## Notes

This explainer was built by analyzing the Ghostty repository at version 1.3.0-dev. Key sources:

- Repository structure and source code analysis
- CONTRIBUTING.md, HACKING.md, AGENTS.md
- build.zig.zon for dependency information
- Terminal emulation code in src/terminal/
- Renderer implementations in src/renderer/
- Platform-specific code in macos/ and src/apprt/gtk/

The content reflects the actual codebase as of December 2024.
