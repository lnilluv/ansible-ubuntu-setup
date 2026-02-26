# Bootstrap Password Fallback Design

## Goal

Allow first connection with root password when key injection is unavailable, while keeping Tailscale-only SSH as final state.

## Approach

- Add `bootstrap_auth_method` with modes `auto`, `key`, and `password`.
- Keep key-first behavior and enable password fallback through runtime variables only.
- Validate required auth inputs in bootstrap and compatibility playbooks.

## Security

- No hardcoded password in repository files.
- Password passed only via runtime extra vars or vault.
- Lockdown phase still enforces key-based, Tailscale-only SSH policy.
