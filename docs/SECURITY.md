# Security and privacy boundaries

**Classification:** educational synthetic clickstream. All IDs are fictional. No authentic customer records, logins, payment details, or tracking cookies should be added.

## Built-in protections

- Generated files excluded from git; the only public report contains aggregate marts.
- Explicit test prevents the exported report from containing per-user rows.
- SQL transformations have no user-supplied expressions or dynamic executable queries.
- CI fetches public dependencies; no application secrets are embedded.
- Docker Compose listens on `127.0.0.1` by default and Streamlit runs as a non-root user.
- Read-only public dashboard does not accept or persist visitor identifiers.

## Not implemented / production requirements

A production system would require consent and lawful processing for real event data, authentication, fine-grained warehouse roles, secret management, access logs, throttling, encryption, vulnerability scanning, backup/restore, retention policies, data deletion workflows, privacy review, and tested incident response. The public static demo is NOT a real-time analytics backend or production-grade service.

## Vulnerability reports

Please avoid public disclosure of any real personal data. For possible security issues use GitHub's repository Security settings (if privately reporting is enabled) or contact the maintainer through the portfolio's official contact channel.
