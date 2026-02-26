# Ubuntu 22.04 Tailscale-Only Implementation Plan

1. Parameterize inventory and remove hardcoded addresses.
2. Split into bootstrap and lockdown playbooks.
3. Replace sensitive variable patterns with runtime or vault values.
4. Add Ubuntu 22.04 baseline, admin user, tailscale, sysctl, and validation roles.
5. Rework SSH and firewall roles for staged hardening.
6. Update README for secure runbook and recovery path.
