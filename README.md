# homebrew-tap

Homebrew tap for [jbox-web](https://github.com/jbox-web) tools.

## Install

```sh
brew install jbox-web/tap/<formula>
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

None at the moment. Watt's Up had one until 0.1.2; from 0.2.0 it ships as an installer
package that updates itself: see [wattsup](https://github.com/jbox-web/wattsup#install).
