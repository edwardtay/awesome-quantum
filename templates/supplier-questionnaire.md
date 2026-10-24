# PQC supplier questionnaire

[Template instructions](README.md) · [Library guide](../docs/libraries.md)

Request answers for a named product, release, deployment configuration, and service boundary. Ask the supplier to distinguish released support from experiments and planned features. Record the respondent, response date, documentation version, and follow-up owner.

## Product and coverage

1. Which generally available product versions implement which exact standardized algorithms, parameter sets, and protocol identifiers?
2. Which functions are covered: key establishment, authentication, certificate issuance, code signing, or another workflow?
3. Which library, provider, runtime, operating system, and hardware configurations provide that support?
4. Which features are enabled by default, configurable, experimental, or dependent on another component?
5. Which termination hops and external dependencies fall within the claim?

## Interoperability and behavior

6. Which peer implementations and versions have been tested, and can you share the test matrix and results?
7. Which key encodings, certificate formats, OIDs, protocol revisions, and hybrid constructions are used?
8. How can an operator observe the actual negotiated algorithms and detect fallback?
9. What occurs when a peer lacks support or when an algorithm is disabled?
10. What are the measured effects on latency, bandwidth, memory, CPU, packet sizes, and constrained clients, with what workload?

## Keys and assurance

11. How are keys generated, stored, backed up, rotated, revoked, restored, and destroyed?
12. What HSM, KMS, trust-store, boot-chain, or timestamping dependencies remain?
13. What audits, conformance results, proofs, or validation certificates support your claims? Identify exact versions, scope, assumptions, and outstanding findings.
14. What analysis covers timing leakage, malformed inputs, randomness failures, and secret handling on the supported platforms?

## Lifecycle and operations

15. What is the supported migration path from our current configuration, including replacement hardware if needed?
16. Which signing and verification capabilities remain available for older artifacts and backups?
17. How are standards revisions, changed encodings, security advisories, and algorithm retirement handled?
18. What are the support commitments, end-of-support dates, monitoring interfaces, and rollback options?

## Response tracking

| Question number | Answer | Supporting evidence | Limitation or dependency | Follow-up owner and date |
|---|---|---|---|---|
| Record. | Pending. | Pending. | Pending. | Assign. |
