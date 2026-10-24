# Awesome Quantum [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated guide to post-quantum cryptography and quantum computing: understand the threat, choose tools, plan migrations, test implementations, and learn to build with qubits.

**PQC first, quantum beyond security.** Start with the decision guides, then explore standards, libraries, protocols, learning resources, and quantum software. Descriptions explain what each resource is useful for; stars and vendor claims are not quality ratings.

[Library chooser](docs/libraries.md) · [Protocol guide](docs/protocols.md) · [Migration field guide](docs/migration.md) · [Migration templates](templates/README.md)

[Learning paths](docs/learning-paths.md) · [Run a PQC example](examples/README.md) · [Glossary](docs/glossary.md) · [Historical resources](docs/historical.md) · [Contribute](CONTRIBUTING.md)

## Contents

- [How to choose](#how-to-choose)
- [Learning paths](#learning-paths)
- [Post-quantum essentials](#post-quantum-essentials)
- [Standards and algorithm status](#standards-and-algorithm-status)
- [Migration and crypto agility](#migration-and-crypto-agility)
- [Discovery and cryptographic inventories](#discovery-and-cryptographic-inventories)
- [Cryptographic libraries](#cryptographic-libraries)
- [PQC implementations and research tools](#pqc-implementations-and-research-tools)
- [Protocols and interoperability](#protocols-and-interoperability)
- [Testing and implementation assurance](#testing-and-implementation-assurance)
- [PQC learning and research](#pqc-learning-and-research)
- [Quantum computing foundations](#quantum-computing-foundations)
- [Quantum SDKs and programming](#quantum-sdks-and-programming)
- [Simulators and compilers](#simulators-and-compilers)
- [Algorithms and applications](#algorithms-and-applications)
- [Error correction and resource estimation](#error-correction-and-resource-estimation)
- [Quantum networks and communication](#quantum-networks-and-communication)
- [Hardware and cloud access](#hardware-and-cloud-access)
- [Communities and research discovery](#communities-and-research-discovery)
- [Related awesome lists](#related-awesome-lists)

## How to choose

| I want to… | Start here | What to look for |
|---|---|---|
| Understand why PQC matters | [Post-quantum essentials](#post-quantum-essentials) | Distinguish future cryptanalysis from present-day data collection. |
| Compare PQC algorithms and sizes | [Algorithm guide](docs/algorithms.md) | Purpose, parameter sets, security categories, and serialized object sizes. |
| Plan an organization's migration | [Migration field guide](docs/migration.md) | Inventory, data lifetime, owners, dependencies, and measurable milestones. |
| Choose a library for an application | [Library chooser](docs/libraries.md) | Documented algorithm coverage, integration boundary, release status, and assurance evidence. |
| Explore algorithm implementations | [PQC implementations](#pqc-implementations-and-research-tools) | Final-standard compatibility, test coverage, and upstream security policy. |
| Evaluate TLS, SSH, VPNs, messaging, or PKI | [Protocol guide](docs/protocols.md) | Key establishment and authentication are separate migration tasks. |
| Find cryptography in an estate | [Discovery and inventories](#discovery-and-cryptographic-inventories) | Combine source, dependency, runtime, network, and supplier evidence. |
| Validate an implementation | [Testing and assurance](#testing-and-implementation-assurance) | Vectors, negative tests, interoperability, and side-channel analysis. |
| Record a migration investigation | [Migration templates](templates/README.md) | Copy an inventory, pilot report, and supplier questionnaire into your own project. |
| Learn quantum computing by doing | [Quantum foundations](#quantum-computing-foundations) | Begin with an interactive circuit tool, then an SDK. |
| Investigate quantum algorithms | [Algorithms and applications](#algorithms-and-applications) | Compare against strong classical baselines and include encoding costs. |
| Assess claims about breaking cryptography | [Resource estimation](#error-correction-and-resource-estimation) | Logical qubits, physical qubits, error correction, runtime, and assumptions. |

## Learning paths

These are suggested sequences, not prerequisites for every resource.

| Reader | Suggested route | Concrete outcome |
|---|---|---|
| Curious beginner | NIST explainer → Quirk → IBM Quantum Learning. | Explain the difference between PQC running on ordinary computers and programs running on quantum hardware. |
| Application developer | PQC essentials → your existing library's documentation → protocol documentation → test vectors. | A compatibility experiment with explicit versions and recorded negotiation results. |
| Security or platform engineer | NCCoE migration project → CycloneDX CBOM → discovery tools → migration field guide. | An owned inventory and a prioritized pilot plan. |
| Cryptography student | Boneh–Shoup → lattice course → FIPS specifications → implementation and assurance tools. | Reproduce a standard's test cases and explain its assumptions. |
| Quantum software developer | IBM Quantum Learning → Qiskit or Cirq → simulation → error correction and resource estimation. | A reproducible circuit experiment with a classical comparison. |

Find the named resources in the sections below. Commercial hardware access and some courses may require accounts or payment; local SDKs and simulators offer a separate starting point.

The [expanded learning paths](docs/learning-paths.md) add concrete exercises and completion outcomes. The [local PQC example](examples/README.md) demonstrates ML-KEM and ML-DSA with six assertions, including altered inputs and an unrelated verification key.

## Post-quantum essentials

| Resource | Why it belongs here |
|---|---|
| [NIST PQC explainer](https://www.nist.gov/cybersecurity-and-privacy/what-post-quantum-cryptography) | Accessible starting point for the quantum threat and the purpose of replacement cryptography. |
| [NIST PQC project](https://csrc.nist.gov/projects/post-quantum-cryptography) | Authoritative entry point for NIST standards, migration work, and continuing algorithm evaluation. |
| [NIST PQC FAQs](https://csrc.nist.gov/projects/post-quantum-cryptography/faqs) | Clarifications that matter when interpreting standards and implementation requirements. |
| [Open Quantum Safe FAQ](https://openquantumsafe.org/faq.html) | Explains the OQS project's scope and limitations before you use its experimental integrations. |

**PQC runs on classical computers.** It concerns cryptographic constructions intended to resist quantum attacks. Quantum key distribution (QKD) uses quantum communication hardware and has different deployment assumptions. A KEM establishes a shared secret; a signature authenticates data. Replacing one does not replace the other. See the [glossary](docs/glossary.md) for these distinctions and their sources.

## Standards and algorithm status

**Status reviewed: 2026-10-24.** The linked standards bodies are authoritative for subsequent changes. Algorithm standardization does not certify a particular implementation, product, or deployment.

| Specification or project | Role | Status at review |
|---|---|---|
| [FIPS 203: ML-KEM](https://csrc.nist.gov/pubs/fips/203/final) | Module-lattice key encapsulation; derived from CRYSTALS-Kyber. | Final standard. Use the publication page for errata and updates. |
| [FIPS 204: ML-DSA](https://csrc.nist.gov/pubs/fips/204/final) | Module-lattice digital signatures; derived from CRYSTALS-Dilithium. | Final standard. |
| [FIPS 205: SLH-DSA](https://csrc.nist.gov/pubs/fips/205/final) | Stateless hash-based digital signatures; derived from SPHINCS+. | Final standard. |
| [Falcon / FN-DSA](https://falcon-sign.info/) | Lattice signatures with compact signatures. | Selected by NIST; standardization is in progress. Follow the [NIST process](https://csrc.nist.gov/projects/post-quantum-cryptography/post-quantum-cryptography-standardization) for FIPS 206 status. |
| [HQC](https://pqc-hqc.org/) | Code-based KEM providing a different mathematical family from ML-KEM. | Selected for standardization in 2025; selection is distinct from a final standard. |
| [NIST additional signatures project](https://csrc.nist.gov/projects/pqc-dig-sig) | Evaluation of further signature constructions. | Ongoing evaluation; candidate status is not approval. |
| [SP 800-208](https://csrc.nist.gov/pubs/sp/800/208/final) | Stateful hash-based signatures, including LMS and XMSS parameter sets. | Final guidance; state management is a central implementation requirement. |
| [SP 800-227](https://csrc.nist.gov/pubs/sp/800/227/final) | Guidance on key-encapsulation mechanisms. | Final guidance on KEM properties and use. |

Pre-standard Kyber and Dilithium names appear throughout papers and code. Check the exact algorithm, encoding, parameter set, and standard revision before assuming compatibility with ML-KEM or ML-DSA.

The [algorithm guide](docs/algorithms.md) compares purpose, parameter sets, public-key sizes, ciphertext sizes, and signature sizes using the final standards' tables.

## Migration and crypto agility

| Resource | Scope and practical use |
|---|---|
| [NCCoE migration to PQC](https://www.nccoe.nist.gov/applied-cryptography/migration-to-pqc) | Discovery, interoperability, and performance workstreams, with links to the latest project publications. |
| [NCSC migration timelines](https://www.ncsc.gov.uk/guidance/pqc-migration-timelines) | UK guidance structuring discovery, priority migrations, and completion milestones. Read its scope before applying dates elsewhere. |
| [CISA quantum readiness](https://www.cisa.gov/resources-tools/resources/quantum-readiness-migration-post-quantum-cryptography) | Joint migration guidance covering inventories, roadmaps, and engagement with suppliers. |
| [NSA post-quantum cybersecurity resources](https://www.nsa.gov/Cybersecurity/Post-Quantum-Cybersecurity-Resources/) | CNSA-related guidance for US National Security Systems; its requirements have a specific audience. |
| [ETSI quantum-safe cryptography](https://www.etsi.org/technical-groups/cyber/) | TC CYBER's quantum-safe work on migration guidance, architecture, and cryptographic mechanisms. |
| [IETF PQUIP](https://datatracker.ietf.org/wg/pquip/about/) | Working group connecting PQC use in Internet protocols with operational guidance. |
| [NIST crypto agility project](https://csrc.nist.gov/projects/crypto-agility) | Strategies for making cryptographic changes manageable across systems and their lifecycles. |

Use the [migration field guide](docs/migration.md) to turn these resources into inventory fields, a pilot plan, and review questions. Guidance from one jurisdiction is not a universal compliance deadline.

## Discovery and cryptographic inventories

| Resource | Evidence it helps collect | Important limit |
|---|---|---|
| [CycloneDX CBOM](https://cyclonedx.org/capabilities/cbom/) | Structured records of algorithms, keys, certificates, and relationships to software components. | An inventory format does not discover assets by itself. |
| [CBOMkit](https://github.com/cbomkit) | Open-source ecosystem for generating and working with cryptographic bills of materials. | Review individual component support and deployment requirements. |
| [Sonar Cryptography](https://github.com/cbomkit/sonar-cryptography) | SonarQube plugin identifying cryptographic assets in supported source languages. | Coverage depends on language, rules, and available build context. |
| [CBOMkit library](https://github.com/cbomkit/cbomkit-lib) | Programmatic indexing and scanning of source projects for CBOM generation. | Source findings require validation against deployed code and configuration. |
| [testssl.sh](https://github.com/testssl/testssl.sh) | TLS configuration and exposed cryptographic behavior on network services. | Check the installed release's algorithm support; a TLS scan is not a complete PQC assessment. |
| [SSLyze](https://github.com/nabla-c0d3/sslyze) | Automated TLS configuration analysis suitable for repeatable service inventories. | Observed TLS capabilities do not reveal internal key storage or signing dependencies. |
| [ssh-audit](https://github.com/jtesta/ssh-audit) | SSH algorithm negotiation and configuration assessment. | A server's advertised algorithms do not prove what every client negotiates. |

## Cryptographic libraries

These are starting points for evaluating an existing stack, not interchangeable recommendations. Language, algorithm availability, protocol support, and assurance vary by release. “Implements FIPS 203” and “FIPS-validated module” are different claims.

Use the [library chooser](docs/libraries.md) for a documentation-backed comparison and questions to narrow the shortlist.

| Library | Stack | Why evaluate it |
|---|---|---|
| [OpenSSL](https://github.com/openssl/openssl) | C; widely integrated TLS and cryptographic APIs. | Native ML-KEM, ML-DSA, and SLH-DSA support arrived in [OpenSSL 3.5](https://openssl-library.org/post/2025-04-08-openssl-35-final-release/); inspect the deployed build and provider configuration. |
| [Go crypto/mlkem](https://pkg.go.dev/crypto/mlkem) | Go standard library. | ML-KEM without a third-party primitive dependency; use protocol packages for complete secure channels. |
| [Bouncy Castle Java](https://github.com/bcgit/bc-java) | Java providers and cryptographic APIs. | Broad PQC coverage for JVM applications; check provider selection and standard versus legacy algorithm names. |
| [Bouncy Castle C#](https://github.com/bcgit/bc-csharp) | C# cryptographic APIs. | PQC primitives for .NET applications with a separate release and API surface from the Java project. |
| [Botan](https://github.com/randombit/botan) | C++ cryptographic library. | PQC implementations within an established general-purpose library and documented build configuration. |
| [wolfSSL / wolfCrypt](https://github.com/wolfSSL/wolfssl) | C; embedded and TLS applications. | PQC integration for constrained environments; inspect build flags, licensing, and supported configurations. |
| [AWS-LC](https://github.com/aws/aws-lc) | C cryptographic library. | Low-level implementations used in AWS's cryptographic ecosystem; distinguish the library from its consumers. |
| [CIRCL](https://github.com/cloudflare/circl) | Go cryptographic library. | Broader experimental and implementation coverage for comparing PQC constructions and integrations. |
| [RustCrypto KEMs](https://github.com/RustCrypto/KEMs) | Rust. | Pure Rust KEM implementations; review each crate's release status and security notes. |
| [RustCrypto signatures](https://github.com/RustCrypto/signatures) | Rust. | Signature implementations, including PQC work; maturity and assurance are specific to each crate. |
| [libcrux](https://github.com/celabshq/libcrux) | Rust with generated and verified cryptographic components. | Pre-release crates with component-specific assurance; inspect maturity and the boundaries of verification. |
| [Noble post-quantum](https://github.com/paulmillr/noble-post-quantum) | JavaScript / TypeScript. | Readable PQC implementations for the JS ecosystem; review runtime, audit, and side-channel considerations. |
| [Node.js crypto](https://nodejs.org/docs/latest-v24.x/api/crypto.html) | Node.js built-in APIs. | ML-KEM APIs from 24.7 and ML-DSA from 24.6; review build support and API stability. A [local example](examples/README.md) exercises both. |

## PQC implementations and research tools

| Project | Best use | Boundary |
|---|---|---|
| [mlkem-native](https://github.com/pq-code-package/mlkem-native) | Portable C ML-KEM with optimized backends and documented assurance work. | Low-level primitive integration still needs correct randomness, memory handling, and protocol use. |
| [mldsa-native](https://github.com/pq-code-package/mldsa-native) | Portable C ML-DSA with optimized backends and verification artifacts. | Review the assurance statement for the exact release and target. |
| [liboqs](https://github.com/open-quantum-safe/liboqs) | Common C API for experimenting with multiple PQC algorithms. | Research and prototyping scope; inclusion of an algorithm is not an endorsement for deployment. |
| [oqs-provider](https://github.com/open-quantum-safe/oqs-provider) | OpenSSL provider for experimenting with PQC and hybrid integrations. | Check the support matrix and overlap with OpenSSL's native implementations. |
| [liboqs-python](https://github.com/open-quantum-safe/liboqs-python) | Python experiments using liboqs primitives. | Wrapper around liboqs with the same underlying research limitations. |
| [OQS demos](https://github.com/open-quantum-safe/oqs-demos) | Application and protocol integration experiments with component-specific support. | Partially supported: select maintained examples; some integrations are explicitly unmaintained. |
| [PQ Code Package](https://github.com/pq-code-package) | Discover implementation projects and their assurance documentation. | Evaluate component repositories individually. |
| [lattice-estimator](https://github.com/malb/lattice-estimator) | Compare estimated attack costs against lattice parameter choices. | Research estimates depend on models and assumptions; they do not prove security. |

For older PQClean-based code and embedded benchmarks, read [Historical resources](docs/historical.md) before choosing dependencies.

## Protocols and interoperability

Follow the linked document's current status. An Internet-Draft can change or expire; an RFC's existence does not imply universal implementation support.

The [protocol guide](docs/protocols.md) maps each workflow to the observations needed for a pilot, including individual TLS termination hops and IPsec rekeying.

| Resource | Layer | What to learn or verify |
|---|---|---|
| [RFC 10024: hybrid key agreement for TLS 1.3](https://www.rfc-editor.org/rfc/rfc10024.html) | TLS key establishment. | Defined combinations of traditional ECDHE and ML-KEM; verify the group actually negotiated by both peers. |
| [ML-KEM key agreement for TLS 1.3](https://datatracker.ietf.org/doc/draft-ietf-tls-mlkem/) | TLS key establishment. | Track the specification and status of standalone ML-KEM groups separately from hybrid groups. |
| [RFC 9881: ML-DSA in X.509](https://www.rfc-editor.org/rfc/rfc9881.html) | PKI and certificates. | Algorithm identifiers and encodings; certificate ecosystem acceptance is a separate interoperability question. |
| [IETF LAMPS documents](https://datatracker.ietf.org/wg/lamps/documents/) | PKI, certificates, and secure messaging. | Track work on algorithm identifiers, certificate formats, and cryptographic message syntax. |
| [OpenSSH PQC guide](https://www.openssh.org/pq.html) | SSH key establishment. | Explains hybrid key exchange and release behavior; host-key and user authentication need separate attention. |
| [RFC 9370: multiple key exchanges in IKEv2](https://www.rfc-editor.org/rfc/rfc9370.html) | IPsec / VPN key establishment. | Defines multiple exchanges during setup and rekeying; algorithm-specific specifications and peer support remain separate. |
| [ML-KEM in IKEv2](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-mlkem/) | IPsec / VPN key establishment. | Internet-Draft at review; track ML-KEM exchange rules and identifiers for compatible peer implementations. |
| [strongSwan algorithm proposals](https://docs.strongswan.org/docs/latest/config/proposals.html) | IPsec implementation. | Documents ML-KEM proposal names and additional exchange rounds; verify release, plugins, and negotiated behavior. |
| [Go crypto/tls](https://pkg.go.dev/crypto/tls) | TLS implementation. | Check supported curve preferences, defaults, and negotiation behavior for the Go release in use. |
| [s2n-tls](https://github.com/aws/s2n-tls) | C TLS implementation. | Evaluate PQC integration through the documented security policies and cryptographic backend. |
| [rustls](https://github.com/rustls/rustls) | Rust TLS implementation. | Inspect cryptographic provider capabilities and configuration when evaluating PQC key exchange. |
| [Signal PQXDH](https://signal.org/docs/specifications/pqxdh/) | Asynchronous messaging key agreement. | Protocol construction and threat model, including the distinction between PQ secrecy and authentication. |
| [Signal Double Ratchet specification](https://signal.org/docs/specifications/doubleratchet/) | Messaging key evolution. | Read the current specification's post-quantum ratchet and composition sections alongside PQXDH. |
| [Cloudflare PQC documentation](https://developers.cloudflare.com/ssl/post-quantum-cryptography/) | Deployment case study. | Practical discussion of transport deployment and where protection applies in a service path. |
| [Open Quantum Safe integrations](https://openquantumsafe.org/applications/) | Protocol experimentation. | Discover integration projects for TLS, SSH, and certificate experiments with their stated limitations. |

## Testing and implementation assurance

| Resource | What it contributes | What it does not establish |
|---|---|---|
| [NIST ACVP server](https://github.com/usnistgov/ACVP-Server) | Algorithm test infrastructure and sample vectors; inspect the generation and revision information. | Passing local vectors alone does not confer algorithm or module validation. |
| [ACVP protocol and specifications](https://github.com/usnistgov/ACVP) | Test protocol definitions and algorithm-specific requirements. | A specification is distinct from an operational validation certificate. |
| [Community Cryptography Test Vectors](https://github.com/C2SP/CCTV) | Community test vectors, including edge cases for cryptographic implementations. | Coverage is algorithm-specific and does not replace protocol testing. |
| [Wycheproof](https://github.com/C2SP/wycheproof) | Cryptographic negative tests for detecting implementation errors; check current PQC coverage. | Tests cannot prove an implementation secure. |
| [dudect](https://github.com/oreparaz/dudect) | Statistical detection of timing differences in implementations. | A passing run does not prove constant-time execution on all inputs or platforms. |
| [Jasmin](https://github.com/jasmin-lang/jasmin) | Language and tooling for high-assurance cryptographic implementation. | Assurance depends on the properties proved and the compiler and execution assumptions. |
| [EasyCrypt](https://github.com/EasyCrypt/easycrypt) | Machine-checked reasoning about cryptographic constructions and programs. | A proof's assumptions and relation to deployed code still require review. |

Also test malformed inputs, randomness failures, downgrade behavior, key and certificate encodings, packet-size effects, and cross-implementation compatibility. Record compiler, architecture, library versions, algorithm identifiers, and benchmark conditions.

## PQC learning and research

| Resource | Level and focus |
|---|---|
| [A Graduate Course in Applied Cryptography](https://toc.cryptobook.us/) | Free book by Dan Boneh and Victor Shoup for the cryptographic foundations behind protocol and primitive choices. |
| [A Decade of Lattice Cryptography](https://eprint.iacr.org/2015/939) | Chris Peikert's survey connecting lattice assumptions, constructions, and security arguments. |
| [Lattice cryptography course](https://cims.nyu.edu/~regev/teaching/lattices_fall_2009/) | Oded Regev's course notes for a mathematical route into lattice cryptography. |
| [Post-Quantum Cryptography book](https://link.springer.com/book/10.1007/978-3-540-88702-7) | Foundational edited volume whose algorithm landscape predates current standards; publisher access may require purchase or a subscription. |
| [PQCrypto conference](https://www.pqcrypto.org/conferences.html) | Conference series focused on cryptography against quantum adversaries. |
| [IACR Cryptology ePrint Archive](https://eprint.iacr.org/) | Early access to cryptographic research; submissions are not automatically peer-reviewed. |
| [Shor's factoring and discrete-logarithm paper](https://arxiv.org/abs/quant-ph/9508027) | Primary source for the algorithmic threat to widely used public-key constructions. |
| [Grover's search paper](https://arxiv.org/abs/quant-ph/9605043) | Primary source for quantum search speedups; useful for understanding why symmetric and public-key impacts differ. |

## Quantum computing foundations

| Resource | Best starting point for |
|---|---|
| [IBM Quantum Learning](https://quantum.cloud.ibm.com/learning/en/courses) | Structured courses on quantum information, algorithms, and error correction with practical SDK connections. |
| [Quirk](https://algassert.com/quirk) | Interactive browser experiments with circuits, measurements, and state visualization. |
| [Quantum Computing for the Very Curious](https://quantum.country/qcvc) | A free conceptual introduction with embedded spaced-repetition questions. |
| [Preskill's lecture notes](https://www.preskill.caltech.edu/ph219/) | A deeper mathematical treatment of quantum computation and information. |
| [The Theory of Quantum Information](https://cs.uwaterloo.ca/~watrous/TQI/) | John Watrous's freely available graduate-level textbook and supporting material. |
| [Introduction to Classical and Quantum Computing](https://www.thomaswong.net/) | Thomas Wong's accessible textbook and teaching resources. |
| [PennyLane demos](https://pennylane.ai/demonstrations/) | Runnable explanations of quantum algorithms, machine learning, and chemistry. |

## Quantum SDKs and programming

| Project | Stack | Useful for |
|---|---|---|
| [Qiskit](https://github.com/Qiskit/qiskit) | Python. | Building, transforming, and transpiling quantum circuits within a broad software ecosystem. |
| [Cirq](https://github.com/quantumlib/Cirq) | Python. | Circuit construction and hardware-aware experiments, especially in Google's quantum ecosystem. |
| [PennyLane](https://github.com/PennyLaneAI/pennylane) | Python. | Differentiable quantum programming with machine learning and chemistry workflows. |
| [Q# and Quantum Development Kit](https://github.com/microsoft/qdk) | Q# and supporting tooling. | Quantum programming, simulation, and resource-estimation workflows. |
| [Amazon Braket SDK](https://github.com/amazon-braket/amazon-braket-sdk-python) | Python. | Local simulation and access to devices through Amazon Braket. |
| [CUDA-Q](https://github.com/NVIDIA/cuda-quantum) | C++ and Python. | Hybrid quantum-classical programs and accelerator-backed simulation. |
| [D-Wave Ocean](https://github.com/dwavesystems/dwave-ocean-sdk) | Python. | Optimization workflows using annealing and hybrid solvers; a different model from gate-based circuits. |

## Simulators and compilers

| Project | Specialty |
|---|---|
| [Qiskit Aer](https://github.com/Qiskit/qiskit-aer) | Circuit simulation with configurable methods and noise models. |
| [QuTiP](https://github.com/qutip/qutip) | Open quantum systems, dynamics, and numerical experiments beyond circuit-only models. |
| [qsim](https://github.com/quantumlib/qsim) | High-performance circuit simulation with integration into Cirq workflows. |
| [QuEST](https://github.com/QuEST-Kit/QuEST) | Quantum simulation across CPU, GPU, and distributed computing environments. |
| [Qulacs](https://github.com/qulacs/qulacs) | Fast quantum circuit simulation with Python and C++ interfaces. |
| [quimb](https://github.com/jcmgray/quimb) | Tensor-network methods and quantum information calculations. |
| [TKET / pytket](https://github.com/Quantinuum/tket) | Circuit compilation, optimization, and backend integration through C++ tooling and Python bindings. |
| [OpenQASM](https://github.com/openqasm/openqasm) | Language specifications and reference material for quantum circuit interchange and control. |
| [QIR Alliance](https://www.qir-alliance.org/) | LLVM-based intermediate representation ecosystem for quantum toolchains. |

## Algorithms and applications

| Resource | Why use it |
|---|---|
| [Quantum Algorithm Zoo](https://quantumalgorithmzoo.org/) | Find algorithms by problem and follow references to their assumptions and speedups. |
| [Quantum algorithms lecture notes](https://quantumalgorithms.org/) | An extended introduction to algorithmic techniques with connections to applications. |
| [OpenFermion](https://github.com/quantumlib/OpenFermion) | Represent and transform fermionic systems for quantum chemistry and materials workflows. |
| [Qiskit Nature](https://github.com/qiskit-community/qiskit-nature) | Natural-science problem representations and quantum algorithm workflows. |
| [Qualtran](https://github.com/quantumlib/Qualtran) | Describe algorithm building blocks and analyze their resource costs. |

For application claims, ask what is counted: state preparation, data loading, repeated measurements, optimization, error correction, and the best relevant classical method. A small demonstration and an end-to-end advantage answer different questions.

## Error correction and resource estimation

| Resource | Question it helps answer |
|---|---|
| [Error Correction Zoo](https://errorcorrectionzoo.org/) | Which code families exist, and how are they related? |
| [Stim](https://github.com/quantumlib/Stim) | How can I efficiently simulate stabilizer circuits and detector error models? |
| [PyMatching](https://github.com/oscarhiggott/PyMatching) | How do matching-based decoders behave on a specified error model? |
| [Sinter](https://github.com/quantumlib/Stim/tree/main/glue/sample) | How can I collect and compare logical-error statistics across repeated decoding experiments? |
| [Azure Quantum resource estimator](https://learn.microsoft.com/en-us/azure/quantum/intro-to-resource-estimation) | What physical resources follow from a program, hardware assumptions, and error-correction choices? |
| [Factoring 2048-bit RSA with noisy qubits](https://arxiv.org/abs/1905.09749) | How are factoring resource estimates constructed? A worked research estimate with explicit assumptions, not a forecast. |

## Quantum networks and communication

PQC, QKD, quantum networking, and quantum random-number generation solve different problems. Keep their threat models and hardware requirements separate when comparing them.

| Resource | Focus |
|---|---|
| [QuTech Quantum Network Explorer](https://www.quantum-network.com/) | Learning and experimentation around quantum networking and its applications. |
| [SquidASM](https://github.com/QuTech-Delft/squidasm) | Simulation of applications running on quantum networks. |
| [SeQUeNCe](https://github.com/sequence-toolbox/SeQUeNCe) | Discrete-event simulation for quantum network architectures and protocols. |
| [NetSquid](https://netsquid.org/) | Quantum network simulation; review access and licensing requirements. |
| [ETSI quantum key distribution](https://www.etsi.org/technical-groups/qkd/) | QKD interfaces, specifications, and standardization context. |

## Hardware and cloud access

Provider entries link to official documentation so readers can evaluate access and supported workflows. Prices, quotas, devices, and availability change; compare them at the source.

| Platform | Explore |
|---|---|
| [IBM Quantum Platform](https://quantum.cloud.ibm.com/) | Gate-based hardware, runtime services, and the Qiskit ecosystem. |
| [Amazon Braket](https://docs.aws.amazon.com/braket/latest/developerguide/what-is-braket.html) | Managed access to quantum devices, simulators, and hybrid jobs. |
| [Azure Quantum](https://learn.microsoft.com/en-us/azure/quantum/) | Provider access, Q# tooling, and resource estimation. |
| [D-Wave Leap](https://docs.dwavequantum.com/en/latest/) | Annealing and hybrid optimization services with Ocean tooling. |
| [Quantinuum documentation](https://docs.quantinuum.com/) | Hardware and software workflows in Quantinuum's ecosystem. |
| [IQM documentation](https://docs.iqm.tech/) | Hardware access and software interfaces for IQM systems. |

## Communities and research discovery

| Resource | Why follow it |
|---|---|
| [Post-Quantum Cryptography Alliance](https://pqca.org/) | Open-source PQC collaboration, including OQS and PQ Code Package. |
| [NIST PQC forum](https://groups.google.com/a/list.nist.gov/g/pqc-forum) | Public technical discussion and announcements around NIST's PQC process. |
| [Quantum Open Source Foundation](https://qosf.org/) | Open-source quantum software initiatives and community programs. |
| [Unitary Foundation](https://unitary.foundation/) | Community support for quantum software and open-source projects. |
| [QWorld](https://qworld.net/) | Community education and workshops in quantum computing. |
| [Quantum Computing Stack Exchange](https://quantumcomputing.stackexchange.com/) | Searchable technical questions about algorithms, tools, and quantum information. |
| [arXiv quantum physics](https://arxiv.org/list/quant-ph/recent) | New quantum research preprints; evaluate claims and publication status independently. |
| [Quantum journal](https://quantum-journal.org/) | Open-access, peer-reviewed research in quantum science. |

## Related awesome lists

These lists informed the coverage review. Each has its own useful scope; descriptions here are written independently.

| List | Complementary coverage |
|---|---|
| [Awesome Post-Quantum](https://github.com/veorq/awesome-post-quantum) | Standards, government guidance, protocols, software, and research surveys. |
| [Awesome PQC](https://github.com/AppliedPQC/awesome-pqc) | Applied implementation, testing, deployment, and migration resources. |
| [Awesome Quantum Computing](https://github.com/desireevl/awesome-quantum-computing) | Learning materials, books, courses, and quantum computing community resources. |
| [Awesome Quantum Software](https://github.com/qosf/awesome-quantum-software) | A broader catalog of open-source quantum software across specialist categories. |

## Contributing

Read the [contribution guidelines](CONTRIBUTING.md) before suggesting a resource. Explain the specific reader need it fills, link to primary documentation, and disclose any affiliation. Corrections and removals are as valuable as additions.

## Footnotes

Standards and lifecycle statements are dated snapshots. Link accessibility checks do not constitute security review, hands-on evaluation, or endorsement. See [maintenance and verification](docs/maintenance.md) and the [HTTP review snapshot](data/link-review.json) for recorded checks and unresolved access limitations.
