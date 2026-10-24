# Contributing

Help readers make a better decision. A focused correction, a removed stale dependency, or a clearer limitation can improve this list more than another link.

## Scope

The list prioritizes post-quantum cryptography while covering quantum computing, error correction, resource estimation, and quantum communication. It favors primary standards, maintained software, substantive learning resources, and reproducible research. It is a curated guide rather than a directory of every company or project.

## Suggesting a resource

1. Choose the closest existing category and check for duplicates.
2. Link to the canonical project, primary documentation, standards publication, or author-hosted material.
3. Explain what the reader can do with it and what distinguishes it from existing entries.
4. Check documentation, maintenance status, licensing or access conditions, and any security policy. Popularity alone is insufficient.
5. For PQC software, verify the exact algorithms, final-standard compatibility, and release requirements. Label experiments and prototypes accurately.
6. For status claims, include a dated primary source in the pull request. Distinguish candidates, selections, drafts, final standards, released implementations, and validated modules.
7. Disclose affiliation and any commercial access requirements relevant to the description.

## Editing style

- Reuse the existing Markdown tables and concise sentence descriptions.
- Describe a concrete use or distinction; avoid promotional language and unsupported security claims.
- Use one canonical entry per project. Cross-link sections rather than duplicating entries.
- End descriptions with a period. Preserve official project names and capitalization.
- Keep full paragraphs on one line and use relative links for files in this repository.
- Put retired software and useful but stale implementations in `docs/historical.md`, with lifecycle evidence.
- Do not add star counters, rankings based on popularity, affiliate links, sponsored placements, or marketing-only resources.
- Keep standards and lifecycle review dates honest; a working URL alone is not a content review.
- When changing a library or protocol claim, update the corresponding guide in `docs/libraries.md` or `docs/protocols.md` and cite the relevant primary documentation there.
- When changing algorithm-size tables, verify each value and its units against the cited standard, including the parameter set and any encoding overhead.
- Treat `data/link-review.json` as a dated observation, not a permanent guarantee. Never turn access blocks or timeouts into successful results to make the report look clean.

## Checks

Run the local structural checks with Python 3.11 or newer:

```sh
python3 scripts/check.py
```

Optionally check external links and write a machine-readable report:

```sh
python3 scripts/check.py --network --report /tmp/awesome-quantum-links.json
```

Review redirects, access blocks, archived repository notices, and changed document status. A `403` or `429` requires manual investigation; do not remove a useful resource solely because automated requests were blocked. The checker does not verify security, implementation correctness, external page fragments, or factual claims. See [maintenance](docs/maintenance.md).

For changes to the educational example, also run `node examples/node-pqc.mjs` on a supported Node.js runtime. Preserve the negative cases and keep the example self-contained; see [example instructions](examples/README.md).

Submit a focused pull request using the template. Do not include private inventory data, credentials, or confidential vulnerability reports.
