# Choosing a PQC library

[← Awesome Quantum](../README.md) · [Protocol guide](protocols.md) · [Pilot report template](../templates/pilot-report.md)

**Documentation reviewed: 2026-10-24.** This is a shortlist for investigation, not a benchmark or a security ranking. Coverage below describes the linked documentation; it does not establish that a particular installed package enables the same algorithms.

Use the [algorithm guide](algorithms.md) to compare parameter sets and object sizes before selecting an implementation.

## Start with the integration boundary

| Your task | Start with | First decision |
|---|---|---|
| Upgrade an existing TLS service | The service's supported TLS library and configuration. | Which supported release exposes the required protocol group through this application? |
| Add PQ key establishment to a Go service | `crypto/tls` for TLS; `crypto/mlkem` for a primitive-level experiment. | Do you need a complete channel or a low-level KEM API? |
| Integrate PQC with a Java or .NET application | The relevant Bouncy Castle implementation and provider documentation. | Does the consuming framework use that provider and understand the required keys and encodings? |
| Explore PQC in JavaScript | Noble post-quantum and the target runtime's APIs. | Are execution environment, randomness, timing behavior, and key serialization suitable? |
| Integrate a portable C primitive | mlkem-native or mldsa-native for the required algorithm. | Who owns the protocol, randomness, secret handling, and platform integration around it? |
| Evaluate Rust implementations | Algorithm-specific RustCrypto crates and libcrux components. | Which exact crate, release, features, and verification scope meet the use case? |
| Compare multiple PQC constructions | liboqs and its documented integrations. | Is this a research experiment or a dependency selection for a supported service? |

## Documentation-backed comparison

The table intentionally names documented capabilities instead of using a single “PQC supported” checkbox. Check release notes and package documentation when making a deployment decision.

| Project and evidence | Documented coverage | Integration boundary | Review before selecting |
|---|---|---|---|
| [OpenSSL 3.5 release](https://openssl-library.org/post/2025-04-08-openssl-35-final-release/) | Native ML-KEM, ML-DSA, and SLH-DSA. | General-purpose cryptographic library and TLS implementation. | Distribution patches, enabled providers, application exposure of APIs and groups, and the exact module validation claim if required. |
| [Go crypto/mlkem](https://pkg.go.dev/crypto/mlkem) | ML-KEM-768 and ML-KEM-1024 APIs. | KEM primitive in the standard library. | Use [crypto/tls](https://pkg.go.dev/crypto/tls) for a TLS channel; inspect the Go version's defaults and negotiated group. |
| [Botan public-key reference](https://botan.randombit.net/handbook/api_ref/pubkey.html) | ML-KEM, ML-DSA, and SLH-DSA within the documented public-key API. | C++ cryptographic library. | Enabled modules, parameter naming, serialization, and support in the consuming protocol. |
| [Noble post-quantum](https://github.com/paulmillr/noble-post-quantum) | ML-KEM, ML-DSA, and SLH-DSA implementations, alongside other constructions. | JavaScript / TypeScript primitives; some wrappers require runtime support. | Package version, runtime capabilities, audit scope, randomness, and the project's security discussion. |
| [Node.js 24 crypto](https://nodejs.org/docs/latest-v24.x/api/crypto.html) | Built-in ML-KEM and ML-DSA APIs used by the [local example](../examples/README.md). | Runtime-provided cryptographic primitives. | Runtime version, build and provider support, API stability, and application protocol integration. |
| [mlkem-native](https://github.com/pq-code-package/mlkem-native) | ML-KEM / FIPS 203 with portable C and architecture-specific backends. | Low-level KEM implementation. | Target backend, build configuration, randomness integration, and which proof properties cover that target. |
| [mldsa-native](https://github.com/pq-code-package/mldsa-native) | ML-DSA / FIPS 204 with portable C and architecture-specific backends. | Low-level signature implementation. | Target backend, signing behavior, secret handling, and the release's assurance statement. |
| [libcrux](https://github.com/celabshq/libcrux) | Separate ML-KEM and ML-DSA crates among a broader set of components. | Rust primitives with component-specific verification. | The README labels the crates pre-release; check the individual crate and proof boundary, including Rust API wrappers. |
| [liboqs](https://github.com/open-quantum-safe/liboqs) | Multiple KEMs and signature schemes behind a C API. | Prototyping and algorithm experimentation. | Algorithm status, selected implementation, library version, and upstream limitations on operational use. |
| [oqs-provider](https://github.com/open-quantum-safe/oqs-provider) | PQC integration through the OpenSSL provider interface. | Experimental integration requiring OpenSSL and liboqs. | Version compatibility and algorithms disabled when native OpenSSL implementations are available. |

## OpenSSL API references

For native OpenSSL 3.5 support, start with the actual primitive documentation:

- [ML-KEM operations](https://docs.openssl.org/3.5/man7/EVP_KEM-ML-KEM/) for encapsulation and decapsulation.
- [ML-DSA signatures](https://docs.openssl.org/3.5/man7/EVP_SIGNATURE-ML-DSA/) for signing options and verification behavior.
- [SLH-DSA signatures](https://docs.openssl.org/3.5/man7/EVP_SIGNATURE-SLH-DSA/) for the hash-based signature API.
- [s_client](https://docs.openssl.org/3.5/man1/openssl-s_client/) for TLS inspection, group selection, certificate verification, and diagnostics.

Provider availability, application configuration, and negotiated protocol behavior are separate observations. Record all three in a pilot.

## Compare evidence, not labels

| Claim | Evidence to request | Remaining question |
|---|---|---|
| Implements a standard | Exact FIPS revision, parameter sets, encodings, and conformance test results. | Does the deployed build match the tested one? |
| Audited | Public report or an assessable scope, release or commit, and remediation status. | Were your enabled features and platform included? |
| Formally verified | Property statements, assumptions, toolchain, code boundary, and target architecture. | Do wrappers, randomness, compiler behavior, and integration sit outside the proof? |
| Constant-time | Defined leakage model and platform-specific analysis or proof. | Does the claim hold on the target execution environment? |
| Validated | Certificate, exact module version, approved configuration, and security policy. | Does your use fall within that validation? |
| Interoperable | Peer versions, identifiers, formats, test conditions, and captured results. | Does it cover your actual clients, termination hops, and failure cases? |

Use the [pilot report](../templates/pilot-report.md) to capture the evidence behind a choice. Revisit the decision when changing algorithms, providers, compiler targets, key formats, or protocol versions.
