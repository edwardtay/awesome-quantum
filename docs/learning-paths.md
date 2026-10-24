# Learning paths with practical outcomes

[← Awesome Quantum](../README.md) · [Glossary](glossary.md)

Choose a route by the outcome you need. Work through the steps in order, or skip material you can already explain. These are self-directed sequences, not estimates of course length or professional qualifications.

## Understand the quantum threat

| Step | Resource | Exercise |
|---|---|---|
| 1 | [NIST PQC explainer](https://www.nist.gov/cybersecurity-and-privacy/what-post-quantum-cryptography) | Explain why the confidentiality lifetime of collected traffic matters before a CRQC exists. |
| 2 | [Quirk](https://algassert.com/quirk) | Create a two-qubit Bell circuit and observe how measurement changes its outputs. |
| 3 | [IBM Quantum Learning](https://quantum.cloud.ibm.com/learning/en/courses) | Study states, measurements, circuits, and entanglement in the foundational courses. |
| 4 | [Shor's paper](https://arxiv.org/abs/quant-ph/9508027) and [Grover's paper](https://arxiv.org/abs/quant-ph/9605043) | Identify the problems each algorithm solves before interpreting their cryptographic implications. |
| 5 | [Resource-estimation introduction](https://learn.microsoft.com/en-us/azure/quantum/intro-to-resource-estimation) | List the hardware and error-correction assumptions missing from a raw qubit-count claim. |

**Outcome:** explain why PQC, quantum hardware, QKD, and resource estimates describe different things, and which evidence matters for a cryptographic threat claim.

## Build an application-level PQC experiment

| Step | Resource | Exercise |
|---|---|---|
| 1 | [KEM guidance](https://csrc.nist.gov/pubs/sp/800/227/final) | Separate key establishment from authentication and encryption of application data. |
| 2 | [Local Node.js example](../examples/README.md) | Run the six checks and explain why changed ciphertext and changed signatures behave differently. |
| 3 | [Library chooser](libraries.md) | Select a candidate by language, integration boundary, documented capabilities, and evidence requirements. |
| 4 | [Protocol guide](protocols.md) | Define one connection or signing workflow to investigate. |
| 5 | [Pilot report](../templates/pilot-report.md) | Record versions, expected behavior, observed algorithms, failure cases, and evidence limits. |

**Outcome:** a bounded compatibility experiment and a report that distinguishes observed behavior from assumptions. Running the primitive example completes step 2, not the full route.

## Plan an organization's migration

| Step | Resource | Exercise |
|---|---|---|
| 1 | [NCCoE migration project](https://www.nccoe.nist.gov/applied-cryptography/migration-to-pqc) | Identify discovery and interoperability work relevant to your environment. |
| 2 | [Migration field guide](migration.md) | Choose a small estate or service path and name its owners and protection lifetimes. |
| 3 | [Inventory template](../templates/crypto-inventory.csv) and [CBOM overview](https://cyclonedx.org/capabilities/cbom/) | Build an inventory from multiple evidence sources; assign actions to unknowns. |
| 4 | [Supplier questionnaire](../templates/supplier-questionnaire.md) | Request exact release, configuration, dependency, and support evidence. |
| 5 | [NCSC migration guidance](https://www.ncsc.gov.uk/guidance/pqc-migration-timelines) | Compare its planning phases with your requirements and jurisdiction, then define a prioritized pilot. |

**Outcome:** an owned inventory, a dependency map, and a pilot plan with acceptance criteria and review dates.

## Study PQC constructions and implementations

| Step | Resource | Exercise |
|---|---|---|
| 1 | [Boneh–Shoup](https://toc.cryptobook.us/) | Review security definitions, randomized algorithms, signatures, and authenticated key exchange. |
| 2 | [Peikert's lattice survey](https://eprint.iacr.org/2015/939) and [Regev's course](https://cims.nyu.edu/~regev/teaching/lattices_fall_2009/) | Work through the assumptions and reductions underlying lattice constructions. |
| 3 | [FIPS 203](https://csrc.nist.gov/pubs/fips/203/final) or [FIPS 204](https://csrc.nist.gov/pubs/fips/204/final), with the [algorithm guide](algorithms.md) | Map a standardized interface to a documented implementation, including parameter sets, encodings, input validation, and randomness. |
| 4 | [NIST ACVP material](https://github.com/usnistgov/ACVP-Server) | Identify the relevant algorithm revision and reproduce selected test vectors. |
| 5 | [Assurance resources](../README.md#-testing-and-implementation-assurance) | Contrast vectors, negative tests, leakage detection, proofs, and module validation. |

**Outcome:** a reproducible implementation investigation with a clearly stated security model and assurance scope.

## Develop quantum programs

| Step | Resource | Exercise |
|---|---|---|
| 1 | [IBM Quantum Learning](https://quantum.cloud.ibm.com/learning/en/courses) | Work through the mathematical and circuit foundations. |
| 2 | [SDK shortlist](../README.md#-quantum-sdks-and-programming) | Pick one SDK and reproduce a small circuit on a local simulator. |
| 3 | [Quantum Algorithm Zoo](https://quantumalgorithmzoo.org/) | Choose a problem and identify the algorithm's access model and assumptions. |
| 4 | [Simulator shortlist](../README.md#-simulators-and-compilers) | Explain how the chosen simulation method limits the circuits you can study. |
| 5 | [Error correction and estimation](../README.md#-error-correction-and-resource-estimation) | Record noise, logical operations, error-correction assumptions, and classical comparison costs. |

**Outcome:** a reproducible quantum computing experiment whose results are scoped to the tested problem, model, and hardware assumptions.
