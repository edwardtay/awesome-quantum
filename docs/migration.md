# PQC migration field guide

[← Awesome Quantum](../README.md)

Use this guide to structure a migration investigation and its deliverables. Adapt decisions to the relevant protocol, threat model, assurance requirements, and jurisdiction. The main references are the [NCCoE migration project](https://www.nccoe.nist.gov/applied-cryptography/migration-to-pqc), [NCSC migration guidance](https://www.ncsc.gov.uk/guidance/pqc-migration-timelines), and [NIST crypto agility project](https://csrc.nist.gov/projects/crypto-agility).

Start with the reusable [inventory, pilot report, and supplier questionnaire](../templates/README.md). Use the [library chooser](libraries.md) and [protocol guide](protocols.md) when narrowing the scope of an experiment.

## 1. Define what must stay protected

Separate long-lived confidentiality from authentication, software signing, and trust anchors. Record how long information must remain confidential, how long signed artifacts must remain trustworthy, and how long replacing hardware or coordinating suppliers will take. These lifetimes help prioritize work without predicting a date for a cryptographically relevant quantum computer.

| Question | Example evidence to collect |
|---|---|
| What could be collected today and decrypted later? | Data classification, retention periods, externally exposed encrypted traffic, and network paths. |
| What signatures must remain trustworthy for years? | Firmware, update packages, archival documents, signing keys, and verification policy. |
| What will be hard to replace? | Embedded roots of trust, field devices, HSM dependencies, and supplier end-of-support dates. |
| Who must interoperate? | Clients, servers, proxies, inspection devices, certificate authorities, and external partners. |

## 2. Build an inventory with owners

Combine source scanning, dependency manifests, runtime configuration, network observations, certificate inventories, and supplier documentation. Use a format such as [CycloneDX CBOM](https://cyclonedx.org/capabilities/cbom/) where it fits. No single scan sees all deployed cryptography.

| Field | Record |
|---|---|
| Asset and owner | Service, environment, accountable team, and escalation route. |
| Cryptographic purpose | Key establishment, authentication, signing, encryption at rest, or key wrapping. |
| Algorithm and parameters | Exact identifiers, parameter sets, certificate signature algorithms, and key types. |
| Implementation | Library, runtime, package version, provider, build flags, and deployment image. |
| Protocol path | Every termination point, including CDN, load balancer, proxy, origin, and partner. |
| Key custody | Generation, storage, HSM or KMS, backup, rotation, revocation, and recovery. |
| Exposure and lifetime | Data sensitivity, confidentiality period, artifact lifetime, and trust-anchor lifetime. |
| Evidence | Discovery method, observation date, scan coverage, and confidence. |
| Dependency and readiness | Supplier statement, supported upgrade path, blocked consumers, and end-of-support. |
| Migration tracking | Priority, chosen pilot, acceptance criteria, owner, and target milestone. |

## 3. Choose a migration unit

Treat a protocol path or signing workflow as the unit of work. Substituting a cryptographic primitive inside one library does not migrate all clients, certificates, keys, trust stores, or hardware on that path.

| Workflow | Verify separately |
|---|---|
| TLS | Negotiated key-establishment group, certificate authentication, session resumption, every termination hop, and client compatibility. |
| SSH | Key exchange, host-key authentication, user authentication, agent support, and operational tooling. |
| IPsec / IKEv2 | Exchange rounds, peer authentication, initial setup, IKE and Child SA rekeying, fragmentation, and fallback policy. |
| Messaging | Initial agreement, ongoing key evolution, identity authentication, backups, and device linking. |
| PKI and signing | Formats, OIDs, certificate chains, validators, revocation, timestamps, HSM support, and long-lived verification. |
| Firmware and embedded devices | Boot-chain roots, available memory, signature size, update channels, recovery, and field replacement. |
| Archived encrypted data | Key wrapping and custody, backups, retention, and the limits of re-encryption after possible prior collection. |

Follow the protocol's specified hybrid construction where applicable. Concatenating primitives or selecting an experimental algorithm independently is not a substitute for a defined protocol and its security analysis. For concrete sources, see [protocols and interoperability](../README.md#protocols-and-interoperability).

## 4. Run a measurable pilot

Before testing, agree on the client matrix, supported versions, expected algorithms, performance budget, failure policy, and rollback conditions.

- Record exact client, server, library, provider, and algorithm versions.
- Capture negotiated algorithms rather than relying on a feature toggle or an advertised capability.
- Measure handshake latency, traffic size, CPU, memory, and connection success under representative conditions.
- Exercise middleboxes, path MTU constraints, certificate-chain growth, retries, and constrained clients.
- Test malformed inputs, disabled algorithms, version mismatches, and downgrade or fallback behavior.
- Test key rotation, revocation, restore, monitoring, and recovery with the operations team.
- Have an owner review whether acceptance criteria were met before expanding the rollout.

Known-answer tests check particular computations. Interoperability tests check whether implementations communicate. Side-channel analysis checks another class of behavior. Module validation has its own process. Keep these forms of evidence distinct.

## 5. Keep the change maintainable

Record exceptions with owners and review dates. Monitor upstream security advisories, standards changes, and provider support. Exercise cryptographic upgrades and recovery as routine maintenance; crypto agility includes keys, protocols, deployment processes, and dependent systems.

## Supplier review questions

- Which released product versions support which exact standardized algorithms and protocol groups?
- Does support cover key establishment, authentication, signing, or only a subset?
- Which deployment configurations and cryptographic providers are supported?
- What interoperability evidence exists for our client and server matrix?
- What is the scope of any audit, proof, certification, or validation claim?
- How are keys generated, stored, backed up, rotated, revoked, and recovered?
- What are the upgrade, rollback, support, and hardware replacement paths?
- Which dependencies and parts of the service path remain outside that support?
