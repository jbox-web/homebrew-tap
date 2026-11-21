# homebrew-tap

Homebrew tap for [jbox-web](https://github.com/jbox-web) tools.

## Install

```sh
brew install jbox-web/tap/<formula>
brew install --cask jbox-web/tap/<cask>
```

## Formulae

| Formula | Description |
|---------|-------------|
| `crystalreleaser` | Release automation for Crystal projects |
| `donico` | Build, test, push and clean Docker images from a single `donico.yml` |

The formulae are generated and pushed by each project's release, with
[crystalreleaser](https://github.com/jbox-web/crystalreleaser): do not edit
them by hand, the next release overwrites them.

## Casks

| Cask | Description |
|------|-------------|
| `wattsup` | Watch UPSes served by NUT servers from the macOS menu bar |

The casks are generated and pushed by their project's release script
(`apple/release.sh` in [wattsup](https://github.com/jbox-web/wattsup)): do not
edit them by hand either.
