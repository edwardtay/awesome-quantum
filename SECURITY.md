# Security policy

This repository is a curated resource list with documentation, templates, a local checker, and an educational cryptographic example. Its linked projects have their own security policies and release processes.

## Reporting an issue

Use the repository's **Security → Report a vulnerability** interface for a sensitive issue affecting this repository. Include the affected file or commit, reproduction steps, impact, and suggested remediation if available. Do not put secrets or an unannounced vulnerability in a public issue or pull request.

Report vulnerabilities in a linked library or protocol implementation directly to that project's maintainers using its security policy. Use ordinary issues for broken links, outdated descriptions, and non-sensitive corrections.

## Automation and examples

GitHub Actions uses read-only repository permissions, pinned action commits, and checkouts that do not persist credentials. Pull requests run local validation and the self-contained example; external URL checks run only on scheduled or manual events.

The example uses the runtime's cryptographic primitives and does not implement a secure transport protocol. Running its assertions does not certify a library, protocol, or deployment. Review API and runtime support using [the example instructions](examples/README.md).

## Maintaining the repository

Keep private keys, credentials, internal inventories, and unpublished assessment evidence out of contributions. Review upstream action updates before changing pinned commits, and investigate failed checks rather than weakening validation to make a status green.
