# PQC pilot report

[Template instructions](README.md) · [Migration field guide](../docs/migration.md)

Copy this document into your project. Replace instructions with recorded evidence and use `not assessed` for work that has not been performed.

## Scope and ownership

| Field | Record |
|---|---|
| Pilot ID and owner | Assign a stable ID and an accountable team. |
| Review date and reviewers | Identify the people assessing the evidence. |
| Inventory references | List asset IDs and exact connections or signing workflows. |
| Objective | State the behavior the experiment is intended to establish. |
| Boundary | Name the clients, termination points, dependencies, and excluded paths. |
| Threat and lifetime | State confidentiality and trust requirements relevant to this pilot. |

## Configuration under test

| Component | Version and build | Provider or features | Relevant configuration | Evidence reference |
|---|---|---|---|---|
| Client | Record. | Record. | Record. | Record. |
| Server or verifier | Record. | Record. | Record. | Record. |
| Proxy or intermediary | Record, or mark outside scope. | Record. | Record. | Record. |
| Key management or signer | Record, or mark outside scope. | Record. | Record. | Record. |

Include algorithm identifiers, parameter sets, key and certificate encodings, protocol revisions, operating system, hardware architecture, and compiler where relevant. For research code, identify the commit or release and any local changes.

## Acceptance criteria

Define thresholds and expected behavior before collecting results.

| Criterion | Required result | Observed result | Evidence | Assessment |
|---|---|---|---|---|
| Representative peer compatibility | Specify supported peer matrix. | Not assessed. | Pending. | Pending. |
| Negotiated key establishment | Specify exact groups or exchange rounds. | Not assessed. | Pending. | Pending. |
| Authentication and verification | Specify algorithms, chain policy, and expected verification. | Not assessed. | Pending. | Pending. |
| Performance | Specify workload and latency, CPU, memory, and traffic budgets. | Not assessed. | Pending. | Pending. |
| Unsupported peers and fallback | Specify expected success or failure policy. | Not assessed. | Pending. | Pending. |
| Rotation, revocation, and recovery | Specify operational cases. | Not assessed. | Pending. | Pending. |

## Test cases

| Case | Expected behavior | Observed behavior | Evidence | Result |
|---|---|---|---|---|
| Normal connection or verification | Define. | Not assessed. | Pending. | Pending. |
| Unsupported algorithm or peer | Define. | Not assessed. | Pending. | Pending. |
| Malformed key, ciphertext, signature, or certificate | Define according to the protocol and API. | Not assessed. | Pending. | Pending. |
| Changed provider or disabled feature | Define. | Not assessed. | Pending. | Pending. |
| Network or packet-size constraint | Define, or explain why inapplicable. | Not assessed. | Pending. | Pending. |
| Key rotation and restart | Define. | Not assessed. | Pending. | Pending. |
| Recovery or rollback | Define. | Not assessed. | Pending. | Pending. |

## Performance method

Record the baseline, workload, concurrency, sample count, warm-up, measurement method, network conditions, and summary statistics. Keep setup, key generation, handshake, signing, verification, and steady-state traffic costs distinguishable where they apply. Include failures and retries in the report.

## Decision and follow-up

| Field | Record |
|---|---|
| Decision | Expand, revise, stop, or leave undecided with a reason. |
| Unresolved findings | Assign an owner and next action to each. |
| Evidence limits | State untested platforms, peers, workflows, and threat assumptions. |
| Rollout boundary | Identify the exact next scope if expansion is approved. |
| Rollback conditions | Define triggers, owner, and expected security behavior. |
| Next review | Set a date and triggers such as dependency or standards changes. |
