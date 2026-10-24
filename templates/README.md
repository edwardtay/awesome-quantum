# PQC migration templates

[← Awesome Quantum](../README.md) · [Migration field guide](../docs/migration.md)

Copy these files into your own project and replace the instructions with evidence from your environment. They are working documents, not declarations of compliance or security.

| Template | Use it to | Completion criterion |
|---|---|---|
| [Cryptographic inventory](crypto-inventory.csv) | Record each cryptographic purpose on each service path. | Every row has an owner, observation date, evidence reference, and next action. |
| [Pilot report](pilot-report.md) | Define and evaluate a bounded interoperability experiment. | Acceptance criteria are assessed against recorded results, including failures. |
| [Supplier questionnaire](supplier-questionnaire.md) | Request implementation and support evidence. | Answers identify exact versions, coverage, limitations, and supporting documentation. |

## Inventory conventions

Use one row per asset, cryptographic purpose, and connection or signing workflow. A service with TLS key establishment, certificate authentication, and firmware signing needs separate records. A TLS path with several termination points needs separate connection records.

- Assign stable IDs so evidence and pilot reports can reference individual rows.
- Use ISO dates, such as `2026-10-24`, for observations and review dates.
- Record exact algorithm identifiers and versions where known; use `unknown` with a discovery action when they are not known.
- Treat `confidentiality_lifetime` and `trust_lifetime` as separate fields.
- Store evidence in an appropriate internal location; reference it by ID or path.
- Keep secrets and private keys out of inventories and public issues. Public contributions should describe resources, not your internal estate.
- The CSV is a human working template, not a CycloneDX document. Use [CycloneDX CBOM](https://cyclonedx.org/capabilities/cbom/) for structured exchange where appropriate.
