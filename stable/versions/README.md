# ARIGATO version archive

Each release gets its own immutable folder: `vMAJOR.MINOR.PATCH/`.

## Release index

| Version | Status | Repository | Notes |
|---|---|---|---|
| v0.6.0 | UNVERIFIED | `devmansworld/devmansworld.github.io` | Initial version folder; do not treat as a passing build until tested |

## Status rules

- `UNVERIFIED`: archived, but not yet tested.
- `PASS`: tested against the stated checks and environment.
- `BROKEN`: confirmed failure; record the exact repository name and failing version.
- `SUPERSEDED`: replaced by a later release, not necessarily broken.

A status applies only to the exact repository and version named. Do not infer failures or successes from similarly named repositories, forks, mirrors, or other versions.

## Release discipline

1. Copy the complete release into its version folder.
2. Record the exact repository as `owner/repository`.
3. Record the source commit, version, date, and checks performed.
4. Never overwrite a previous version folder. Fixes create a new version.
5. A release without test evidence remains `UNVERIFIED`.
