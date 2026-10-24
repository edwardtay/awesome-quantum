# Quantum and PQC glossary

[← Awesome Quantum](../README.md)

| Term | Meaning in this list |
|---|---|
| Post-quantum cryptography (PQC) | Classical cryptographic constructions intended to withstand attacks by classical and quantum adversaries. They run on ordinary computers. |
| Quantum computing | Computation using quantum states and operations; distinct from implementing PQC algorithms on a conventional processor. |
| Cryptographically relevant quantum computer (CRQC) | A quantum computer capable of executing attacks that threaten deployed cryptographic systems at a relevant scale. A raw qubit count alone does not establish that capability. |
| Harvest now, decrypt later | Collecting encrypted information today in the hope of decrypting it with future capabilities. |
| Key-encapsulation mechanism (KEM) | A public-key mechanism for establishing shared secret material through encapsulation and decapsulation. A KEM alone is not a complete authenticated encryption protocol. |
| Digital signature | A mechanism for signing and verifying data under a public key. Its purpose differs from confidential key establishment. |
| ML-KEM | The module-lattice KEM specified by FIPS 203, derived from CRYSTALS-Kyber. |
| ML-DSA | The module-lattice signature scheme specified by FIPS 204, derived from CRYSTALS-Dilithium. |
| SLH-DSA | The stateless hash-based signature scheme specified by FIPS 205, derived from SPHINCS+. |
| FN-DSA | The name associated with NIST's standardization work on Falcon-derived signatures. Check current publication status. |
| Hybrid key establishment | A specified construction combining traditional and post-quantum mechanisms. Security depends on the actual construction, protocol, and assumptions. |
| Crypto agility | The ability to change cryptographic mechanisms and their dependencies across a system's lifecycle. It includes more than configuring an algorithm name. |
| Cryptographic bill of materials (CBOM) | A structured inventory of cryptographic assets and their relationships to software and systems. |
| Quantum key distribution (QKD) | Establishing key material using quantum communication and an authenticated classical channel, with specialized hardware and implementation assumptions. |
| Quantum random-number generation (QRNG) | Generating randomness from a quantum physical process; it does not itself migrate encryption or signature schemes. |
| Logical qubit | An encoded unit of quantum information, often protected by error correction using multiple physical qubits. |
| Physical qubit | A hardware unit used to represent or process quantum information; noise and connectivity affect its usefulness. |
| Fault tolerance | Methods for carrying out quantum computation while controlling the propagation and impact of errors. |
| Resource estimate | A conditional analysis of computational resources, including runtime, logical operations, physical qubits, and error correction. It is not a delivery forecast. |
| Known-answer test (KAT) | A test comparing implementation outputs to specified inputs and expected outputs. |
| ACVP | Automated Cryptographic Validation Protocol; a protocol and ecosystem for algorithm testing. Local use of sample vectors is distinct from completing validation. |
| Algorithm standardization | Publication of an algorithm specification following a standards process. It does not establish the security of every implementation. |
| Module validation | Assessment of a particular cryptographic module under a defined validation program and configuration. It is distinct from merely implementing a standardized algorithm. |

## Primary references

- [NIST PQC project](https://csrc.nist.gov/projects/post-quantum-cryptography) and the linked FIPS publications.
- [NIST PQC explainer](https://www.nist.gov/cybersecurity-and-privacy/what-post-quantum-cryptography) for the threat and migration context.
- [SP 800-227](https://csrc.nist.gov/pubs/sp/800/227/final) for KEM terminology and use.
- [NIST crypto agility project](https://csrc.nist.gov/projects/crypto-agility) for lifecycle considerations.
- [CycloneDX CBOM](https://cyclonedx.org/capabilities/cbom/) for inventory representation.
- [ETSI QKD](https://www.etsi.org/technical-groups/qkd/) for quantum communication standards.
- [Azure Quantum resource estimation](https://learn.microsoft.com/en-us/azure/quantum/intro-to-resource-estimation) for logical and physical resource accounting.
- [NIST CMVP](https://csrc.nist.gov/projects/cryptographic-module-validation-program) for module validation.
