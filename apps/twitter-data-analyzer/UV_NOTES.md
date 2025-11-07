# Using uv with Twitter Data Analyzer

This project uses [uv](https://docs.astral.sh/uv/) as the primary package manager for faster, more reliable Python package management.

## Why uv?

**Performance:**
- 10-100x faster than pip for package installation
- Faster virtual environment creation
- Built in Rust for maximum performance

**Reliability:**
- Better dependency resolution
- More predictable installs
- Clearer error messages

**Compatibility:**
- Drop-in replacement for pip
- Same commands (`uv pip install` = `pip install`)
- Works with existing `requirements.txt` and `pyproject.toml`

## Quick Start with uv

### Install uv

```bash
# macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or with pip
pip install uv
```

### Set Up Project

```bash
# Navigate to project
cd twitter-data-analyzer

# Create virtual environment (much faster than venv!)
uv venv

# Activate it
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install project in development mode
uv pip install -e .
```

### Common Commands

```bash
# Install package
uv pip install package-name

# Install from requirements.txt
uv pip install -r requirements.txt

# Install project in editable mode
uv pip install -e .

# Upgrade a package
uv pip install --upgrade package-name

# List installed packages
uv pip list

# Show package info
uv pip show package-name

# Uninstall package
uv pip uninstall package-name
```

## Performance Comparison

Typical installation times for this project:

| Tool | Time | Speed |
|------|------|-------|
| pip | ~30-45s | 1x |
| uv | ~2-5s | 10-15x faster |

*Times vary based on system and network*

## Using pip Instead

If you prefer pip or can't use uv, everything still works:

```bash
# Traditional approach
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
# Or: pip install -e .
```

## Files Overview

- **pyproject.toml** - Modern package configuration (works with both uv and pip)
- **requirements.txt** - Legacy format (kept for compatibility)
- **setup.py** - Legacy setup file (kept for compatibility)
- **.python-version** - Specifies Python version for uv

## Migration from pip

If you're currently using pip, switching to uv is easy:

```bash
# 1. Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Create new venv with uv
uv venv

# 3. Activate it
source .venv/bin/activate

# 4. Install dependencies
uv pip install -e .

# Done! Everything else stays the same
```

## Benefits for This Project

1. **Faster Setup**: Users can get started in seconds, not minutes
2. **Better UX**: Clear progress indicators and error messages
3. **Modern**: Uses `pyproject.toml` (PEP 621) for configuration
4. **Reliable**: Consistent installs across different machines
5. **Compatible**: Still works with pip for users who prefer it

## Resources

- [uv Documentation](https://docs.astral.sh/uv/)
- [uv GitHub](https://github.com/astral-sh/uv)
- [PEP 621 (pyproject.toml)](https://peps.python.org/pep-0621/)

## Troubleshooting

### "uv: command not found"

Make sure uv is in your PATH. After installation, you may need to:
```bash
source ~/.bashrc  # or ~/.zshrc
# Or restart your terminal
```

### Virtual environment issues

```bash
# Remove old venv and recreate
rm -rf .venv
uv venv
source .venv/bin/activate
uv pip install -e .
```

### Falls back to pip

If you want to use pip instead:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

**Note:** This project fully supports both uv and pip. Use whichever you're comfortable with!
