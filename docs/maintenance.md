# Maintenance and verification

[← Awesome Quantum](../README.md)

## Editorial policy

Prioritize a useful reader decision over a longer list. Prefer primary sources, explain limitations that affect selection, and separate retired dependencies from current implementation candidates. Contributions should add a distinct capability, a substantive learning route, or a correction.

Review time-sensitive claims against the standards body or project's own documentation. Record dates for standards and lifecycle summaries. Recheck final-standard compatibility, archived repositories, release requirements, and protocol document status when updating entries. HTTP success does not establish that a description is accurate or that a project is maintained.

The README reuses the repository owner's existing awesome-list conventions: Markdown, badges, category tables, and concise descriptions. The list does not require a website, custom typography, JavaScript, or generated popularity metrics.

## Local checks

```sh
python3 scripts/check.py
```

The standard-library checker validates relative file links, local Markdown heading fragments, README contents coverage, table column counts, duplicate primary resource URLs in the README, trailing whitespace, and code-fence balance. It supports the inline Markdown links used here; it is not a general Markdown parser or a full Awesome-lint implementation.

## External link checks

```sh
python3 scripts/check.py --network --report /tmp/awesome-quantum-links.json
```

The network check makes bounded concurrent GET requests to unique external URLs, follows redirects, and records response status, final URL, and available HTML title. It flags GitHub's archived-repository banner for editorial review. It reads a limited amount of HTML, does not execute JavaScript, and does not check external fragments. A successful response can still be a challenge page, soft 404, or changed resource.

Network errors and blocked requests return a failing exit status so they receive attention. Inspect `403`, `429`, timeout, and challenge responses manually before deciding a resource is dead. Do not blanket-ignore hostnames or treat a manual browser check as an automated pass. Review canonical redirects before changing links.

## Automation

The GitHub Actions workflow runs local checks and a separate Node.js 24 example job on pushes and pull requests. Weekly scheduled runs and manual runs also check external links. It has read-only repository permissions and does not open issues, post comments, or rewrite the list. Network failures are reported in workflow logs; maintainers must investigate them.

## What verification means here

The list provides researched descriptions and links to primary evidence. It does not claim that every SDK was executed, every cryptographic implementation audited, or every migration path tested. A reproducible benchmark, independent audit, formal proof, algorithm validation, and module validation support different claims; evaluate their scope separately.

## Initial review: 2026-10-24

Local structural checks passed. External URLs were inspected through the browsing tool, with targeted HTTP checks for resources that could not be fetched there. The workspace's Python network checker could not resolve external hosts, so its full network run did not pass; this must not be represented as a clean automated link audit. Hosted CI was not yet verified at this initial review; the publication record below covers its later execution.

The review corrected a nonexistent `Quantinuum/pytket` repository to `Quantinuum/tket`, updated moved QDK and libcrux repositories, corrected the OQS FAQ path, and replaced ETSI technology URLs that redirected to a generic page. PQClean and Rust pqcrypto were separated into historical resources, and pqm4's announced retirement and OQS demo support limitations were recorded.

Two external resources remain subject to access limitations in this environment: CISA's quantum-readiness page returned HTTP 403, and NetSquid timed out. They are retained as substantive primary resources rather than marked as accessible or dead. Recheck these manually and on a normal network when publishing. The badge returned HTTP 200 in a targeted check; the browsing tool does not parse SVG badges.

## Practical guide review: 2026-10-24

The [library chooser](libraries.md) cites the documentation behind its capability statements. The review made libcrux's pre-release status explicit rather than treating formal-verification work as a release-maturity claim. OpenSSL's primitive references are versioned to 3.5; other project documentation may evolve, so the review date does not establish an immutable release baseline.

The [protocol guide](protocols.md) separates key establishment, authentication, and connection boundaries. IPsec coverage distinguishes published RFC 9370 from the ML-KEM IKEv2 Internet-Draft and links to strongSwan's implementation documentation. [Migration templates](../templates/README.md) provide a blank inventory and reports whose findings begin as pending or not assessed.

The guide and template additions were checked for local links, headings, and table structure. They are documentation resources, not executed interoperability experiments. The full network-audit limitation above still applies.

## Example validation: 2026-10-24

The [local example](../examples/README.md) passed all six assertions on Node.js 24.22.1 with bundled OpenSSL 3.5.9. It covers ML-KEM agreement and same-length ciphertext alteration, plus ML-DSA verification and rejection of a changed message, changed signature, and unrelated public key. Node.js 20.20.0 correctly exited with a runtime requirement message. See the example's validation record for details.

These checks exercise a small set of primitive operations in one runtime. They do not establish protocol interoperability, conformance, side-channel resistance, or correctness across other builds. The [expanded learning paths](learning-paths.md) connect the example to the additional work needed for application and migration experiments.

## HTTP review snapshot: 2026-10-24

A separate direct-curl pass through the command tool checked every external URL currently linked from the Markdown files. The [machine-readable snapshot](../data/link-review.json) records 153 unique URLs: 146 returned HTTP 200, six returned HTTP 403, and one timed out. None returned HTTP 404. This supersedes the limited reachability observations in the initial review; it does not change the fact that the Python network run failed in this workspace.

| Resource | Direct HTTP result | Follow-up |
|---|---|---|
| NetSquid | Timeout. | Recheck from another network before changing its status. |
| Quantum Computing Stack Exchange | HTTP 403. | Review through a normal browser; an access block is not evidence that the community is gone. |
| CISA quantum readiness | HTTP 403. | Recheck the official page from another network. |
| ETSI TC CYBER and QKD | HTTP 403. | The browsing tool retrieved both pages; keep the direct HTTP block visible in the record. |
| NCCoE migration project | HTTP 403. | The browsing tool retrieved the project page; direct automated access remains blocked. |
| NSA PQC resources | HTTP 403. | The browsing tool retrieved the page; direct automated access remains blocked. |

The review inspected available page titles, redirects, and GitHub archived-repository banners. The archived banners found belong to the PQClean and Rust pqcrypto historical references. Amazon Braket now links directly to its introductory developer documentation instead of its documentation root. The Springer page returned HTTP 200 with a server-added cookie-error query; volatile query parameters were omitted from the stored final URL and that normalization is noted in the record.

The [algorithm guide](algorithms.md) was checked against FIPS 203 Table 3, FIPS 204 Table 2, and FIPS 205 Table 2. Its object sizes exclude protocol and certificate overhead. HTTP availability, page-title inspection, standards-table review, and the executed Node.js example are separate forms of evidence; none is a general security endorsement.

## Publication validation: 2026-10-24

The public repository's initial hosted workflow passed both local document checks and the Node.js example. The publication set passed a redacted Gitleaks scan. GitHub secret scanning, push protection, and private vulnerability reporting were enabled; no secret-scanning alerts were present when checked. Workflow permissions are read-only and all action references are pinned to verified commit IDs. Dependabot is configured to propose action updates.

The README uses emoji section icons in the style of the owner's existing awesome lists. Local heading references were updated with the section names and validated after the presentation change. The HTTP review remains a dated snapshot, and the access limitations recorded above remain unresolved observations.
