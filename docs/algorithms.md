# PQC algorithm tradeoffs and sizes

[← Awesome Quantum](../README.md) · [Library chooser](libraries.md) · [Protocol guide](protocols.md)

**Standards reviewed: 2026-10-24.** These tables describe standardized primitives, not complete protocol messages. Sizes are bytes, excluding certificates, ASN.1 wrappers, transport headers, and hybrid components. Security categories are NIST's comparison categories, not direct measurements of “quantum bits of security.”

## Choose by purpose first

| Family | Purpose | Engineering question |
|---|---|---|
| ML-KEM | Establish shared secret material. | Does the chosen protocol authenticate peers and define how the secret is used? |
| ML-DSA | Sign and verify data. | Do signers, key stores, formats, and relying parties support the required parameter set? |
| SLH-DSA | Stateless hash-based signatures. | Can the workflow accommodate its signature sizes and signing costs? |
| LMS / XMSS | Stateful hash-based signatures. | Can the signing system safely maintain state across backups, replicas, crashes, and recovery? |

Sources: [FIPS 203](https://csrc.nist.gov/pubs/fips/203/final), [FIPS 204](https://csrc.nist.gov/pubs/fips/204/final), [FIPS 205](https://csrc.nist.gov/pubs/fips/205/final), and [SP 800-208](https://csrc.nist.gov/pubs/sp/800/208/final). The [standards table](../README.md#-standards-and-algorithm-status) separately tracks algorithms still in standardization.

## ML-KEM

| Parameter set | Security category | Public encapsulation key | Ciphertext | Shared secret |
|---|---|---|---|---|
| ML-KEM-512 | 1 | 800 | 768 | 32 |
| ML-KEM-768 | 3 | 1184 | 1088 | 32 |
| ML-KEM-1024 | 5 | 1568 | 1568 | 32 |

Source: [FIPS 203, Table 3 and Section 8](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf), printed pages 39–40. The names `512`, `768`, and `1024` are parameter-set identifiers; they are not the public-key sizes or a count of security bits.

A TLS hybrid also carries its traditional component and protocol framing. Use these figures for understanding the primitive, then measure the complete handshake in the intended implementation.

## ML-DSA

| Parameter set | Security category | Public key | Signature |
|---|---|---|---|
| ML-DSA-44 | 2 | 1312 | 2420 |
| ML-DSA-65 | 3 | 1952 | 3309 |
| ML-DSA-87 | 5 | 2592 | 4627 |

Source: [FIPS 204, Section 4 and Table 2](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf), printed pages 15–16. Certificate chains and signed artifacts introduce additional objects and encodings beyond one public key and one signature.

## SLH-DSA

Each row represents both the SHA2 and SHAKE variants with that suffix. They share these sizes but remain distinct algorithm identifiers. The `s` variants favor smaller signatures; the `f` variants favor faster signing.

| Suffix | Security category | Public key | Signature |
|---|---|---|---|
| 128s | 1 | 32 | 7856 |
| 128f | 1 | 32 | 17088 |
| 192s | 3 | 48 | 16224 |
| 192f | 3 | 48 | 35664 |
| 256s | 5 | 64 | 29792 |
| 256f | 5 | 64 | 49856 |

Source: [FIPS 205, Table 2](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf), printed page 43. For example, `SLH-DSA-SHA2-128s` and `SLH-DSA-SHAKE-128s` belong to the first row. A small public key does not imply a small signature or a low-cost signing operation.

## Compare complete workflows

| Constraint | What to measure or inspect |
|---|---|
| Network bandwidth | Full handshakes, certificate chains, retries, and steady-state traffic. |
| Packet size | Fragmentation, path MTU, middleboxes, and constrained peers. |
| CPU and latency | Key generation, encapsulation, decapsulation, signing, and verification separately. |
| Memory | Stack, heap, temporary buffers, and simultaneous operations on the target. |
| Key storage | The implementation's seed, expanded-key, DER, PEM, or provider-managed representation. |
| Long-lived trust | Signing and verification support across the complete artifact lifetime and recovery process. |
| Interoperability | Exact algorithm identifiers, parameter sets, encodings, contexts, and protocol versions. |

Record the results in the [pilot report](../templates/pilot-report.md). Check the publication pages for errata before implementing a standard, and avoid treating object sizes as a substitute for a deployment benchmark.
