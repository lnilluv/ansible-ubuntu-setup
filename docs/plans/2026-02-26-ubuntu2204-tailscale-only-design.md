# Ubuntu 22.04 Tailscale-Only Hardening Design

## Goals

- Support any Ubuntu 22.04 VPS with runtime-provided IP and key path.
- Use a two-phase hardening model to avoid lockouts.
- End state: SSH access only through Tailscale.

## Architecture

1. Bootstrap phase over public IP with temporary source allowlist.
2. Install Tailscale and join tailnet.
3. Lockdown phase removes public SSH access and keeps only tailscale-based SSH access.

## Security baseline

- Key-only SSH auth, root login disabled.
- UFW deny inbound by default.
- Fail2ban, unattended upgrades, auditd, and kernel sysctl hardening.
