# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Homebrew tap for `jbox-web` tools, hosted at `https://github.com/jbox-web/homebrew-tap`.
Lets users install tools with `brew install jbox-web/tap/<formula>`.

## Where the formulae come from

Nothing here is written by hand. Each tool's release runs
[crystalreleaser](https://github.com/jbox-web/crystalreleaser), which generates
`Formula/<name>.rb` from the archives it has just published and pushes it to
`master` in one commit (`Brew formula update for <name> version <tag>`). There
is no update script and no pull request: an edit made here is overwritten by
the next release of that tool.

The push uses a token stored as `HOMEBREW_TAP_TOKEN` in each tool's
repository: a fine-grained personal access token with read and write access to
the contents of this repository.

A formula is fixed by fixing its tool's `.crystalreleaser.yml` (`brews:`), or
crystalreleaser itself, then releasing again.

## Where the casks come from

`Casks/` holds the macOS apps, which crystalreleaser does not build. Each cask is
written by its project's release script, with the same rule: nothing by hand.
`Casks/wattsup.rb` comes from `apple/release.sh` (template `apple/cask.rb.sh`) in
`jbox-web/wattsup`, which pushes it to `master` in one commit
(`Brew cask update for wattsup version <tag>`) with the maintainer's own git
credentials. A cask is fixed in that template, then `apple/release.sh --cask`.

## Formula details

- `on_macos`/`on_linux` × `on_intel`/`on_arm` blocks, one per platform the tool
  publishes a `tar.gz` for.
- No `version` line when Homebrew reads the version from the download URL
  (`brew audit --strict` refuses a redundant one); crystalreleaser writes it
  only for a pre-release whose archive names do not hold the version.

## CI

`.github/workflows/audit.yml` runs `brew audit --strict` on every formula of
`Formula/`, and `brew audit --cask --strict --online` on every cask of `Casks/`
(which downloads each archive and checks its sha256), each named explicitly: `brew audit --tap=jbox-web/tap` audits none
of them and exits 0. `Homebrew/actions/setup-homebrew` attaches the checkout as
the `jbox-web/tap` tap and trusts it, so the workflow has no tap step.

Locally, `brew tap jbox-web/tap "$(pwd)"` clones the checkout (uncommitted
edits are not seen), and `brew trust jbox-web/tap` is required: Homebrew
refuses to load formulae from an untrusted third-party tap, and the audit then
checks nothing.
