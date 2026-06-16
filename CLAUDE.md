# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Homebrew tap for `jbox-web` tools, hosted at `https://github.com/jbox-web/homebrew-tap`.
Lets users install tools with `brew install jbox-web/tap/<formula>`.

Currently contains one formula: `mcp-grimoire-server` — a Crystal MCP server that indexes documentation via Ollama embeddings.

## Key commands

```bash
# Audit formula style locally (requires Homebrew)
brew tap jbox-web/tap "$(pwd)"
brew audit --strict --except-cops=FormulaAudit/Homepage mcp-grimoire-server

# Test the SHA update script with dummy values
python3 scripts/update_formula.py \
  --formula Formula/mcp-grimoire-server.rb \
  --version 0.1.0 \
  --darwin-arm64  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa \
  --darwin-x86-64 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb \
  --linux-arm64   cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc \
  --linux-x86-64  dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
```

## Architecture

| File | Role |
|------|------|
| `Formula/mcp-grimoire-server.rb` | Homebrew formula — downloads pre-built static binary per platform |
| `scripts/update_formula.py` | CLI script called by CI to bump version + SHA256 in the formula |
| `.github/workflows/audit.yml` | CI — runs `brew audit --strict` on every push/PR |

The auto-update flow lives in the **`mcp-grimoire-server` repo** (not here), in `.github/workflows/release-tap.yml`. On each release it: downloads the 4 platform binaries, computes SHA256, then calls `scripts/update_formula.py` and opens a PR here.

## Formula details

The formula supports 4 platform targets via `on_macos`/`on_linux` + `on_arm`/`on_intel` blocks:
- `darwin-arm64`, `darwin-x86_64`, `linux-arm64`, `linux-x86_64`

Binary filenames from releases follow the pattern `mcp-grimoire-server-<platform>`. The `install` block renames the downloaded file to `mcp-grimoire-server`.

## SHA update script

`scripts/update_formula.py` uses regex to replace `version` and `sha256` values in-place. It matches sha256 lines by looking for the URL containing the platform slug immediately above them. If a platform slug is not found, the script exits with code 1.

## CI prerequisite

The audit workflow taps the local checkout with `brew tap jbox-web/tap "$(pwd)"` before auditing, so `brew audit` sees the formula without needing a GitHub push.

## Auto-update prerequisite

A fine-grained PAT with Contents + Pull requests (read+write) on `jbox-web/homebrew-tap` must be stored as secret `TAP_GITHUB_TOKEN` on `jbox-web/mcp-grimoire-server`.
