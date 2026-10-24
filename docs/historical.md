# Historical resources and lifecycle changes

[← Awesome Quantum](../README.md)

These resources remain useful for understanding papers, old benchmarks, and existing dependencies. They are separated from the main implementation list because their maintenance status affects new adoption. Status reviewed on 2026-10-24.

| Resource | Lifecycle evidence | How to use it |
|---|---|---|
| [PQClean](https://github.com/PQClean/PQClean) | [Organization archived in August 2026](https://github.com/PQClean). | Read historical portable implementations and test infrastructure; investigate the maintenance chain of packages that vendor this code. |
| [Rust pqcrypto](https://github.com/rustpq/pqcrypto) | [Maintainer retirement notice](https://github.com/rustpq/pqcrypto/issues/97); repository archived in September 2026. | Identify existing PQClean-based Rust dependencies and evaluate maintained alternatives for the required algorithms. |
| [pqm4](https://github.com/mupq/pqm4) | [Maintainers announced plans to archive in or after January 2027](https://github.com/mupq/pqm4/issues/409). | Reproduce Cortex-M4 benchmarks with pinned versions; verify whether implementations match the final standards. |
| [ctgrind](https://github.com/agl/ctgrind) | Original Valgrind patch and demonstration code rather than a maintained PQC testing suite. | Understand dynamic checks for secret-dependent behavior; establish compatibility with a current analysis toolchain separately. |

For new implementation work, evaluate the [main library and implementation sections](../README.md#-cryptographic-libraries), including the PQ Code Package projects and language-specific libraries. There is no universal drop-in replacement: compare API, algorithm coverage, encodings, target architecture, and security requirements.

Historical publications are different from abandoned dependencies. A foundational paper or book may remain valuable without software maintenance; the main list identifies older learning material where its age affects interpretation.
