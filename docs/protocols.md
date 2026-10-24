# PQC by protocol and workflow

[← Awesome Quantum](../README.md) · [Library guide](libraries.md) · [Migration field guide](migration.md)

**Documentation reviewed: 2026-10-24.** A supported primitive, a protocol specification, and successful negotiation are distinct milestones. This guide identifies what to inspect without assigning a single readiness score to an entire product.

## Where to investigate

| Workflow | Key establishment | Authentication and trust | Evidence to record |
|---|---|---|---|
| TLS / HTTPS | Check the group negotiated on each connection. [RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html) specifies hybrid ECDHE–ML-KEM groups. | Inspect certificate algorithms, chains, and verification separately. [RFC 9881](https://www.rfc-editor.org/rfc/rfc9881.html) specifies ML-DSA certificate conventions. | Client and server builds, selected group, peer certificate chain, and verification result for each termination hop. |
| SSH | Inspect negotiated key exchange; the [OpenSSH guide](https://www.openssh.org/pq.html) describes its hybrid mechanisms. | Host keys and user authentication have their own algorithms, formats, and tooling. | Client and server versions, negotiated KEX, host-key algorithm, authentication method, and agent dependencies. |
| IPsec / IKEv2 | [RFC 9370](https://www.rfc-editor.org/rfc/rfc9370.html) defines multiple exchanges; the [ML-KEM document](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-mlkem/) is an Internet-Draft at review. | Inspect IKE authentication, certificates or shared credentials, and peer policy independently. | Negotiated exchange rounds, algorithms, authentication, rekey behavior, and fragmentation handling. |
| Asynchronous messaging | [PQXDH](https://signal.org/docs/specifications/pqxdh/) covers initial agreement; the [Double Ratchet specification](https://signal.org/docs/specifications/doubleratchet/) describes ongoing key evolution and PQ constructions. | Review the specified identity authentication and device trust model. | Exact protocol revision, initial agreement, ratchet construction, identity verification, and backup behavior. |
| PKI and artifact signing | A signing workflow may have no key-establishment stage. | Inspect signers, certificate chains, timestamps, validators, trust stores, and recovery. Follow [LAMPS work](https://datatracker.ietf.org/wg/lamps/documents/) for relevant formats. | Signature algorithms and encodings throughout the trust path, supported validators, and artifact lifetime. |

## Follow every TLS termination hop

A browser-to-edge connection, an edge-to-origin connection, and an internal service connection can use different stacks and negotiate different algorithms. Termination points have access to plaintext, and their onward connections establish separate cryptographic contexts. [Cloudflare's documentation](https://developers.cloudflare.com/ssl/post-quantum-cryptography/) is one concrete deployment reference.

| Connection | Record separately |
|---|---|
| Client → CDN or edge | Client compatibility, selected key-establishment group, certificate authentication, and policy. |
| Edge → origin | Origin TLS stack, selected group, origin authentication, and configuration ownership. |
| Service → service | Runtime or proxy library, mutual authentication, selected group, and service-mesh policy. |
| Service → external dependency | Supplier support, client defaults, observed negotiation, and fallback behavior. |

Completing one row establishes evidence for that connection. Keep the inventory and pilot results explicit about which rows were observed.

## IPsec pilot considerations

[strongSwan's proposal documentation](https://docs.strongswan.org/docs/latest/config/proposals.html) describes multiple key exchanges and ML-KEM proposal names. Use the documentation for the installed release and verify that both peers implement compatible identifiers and exchange behavior.

Test initial tunnel setup, IKE rekeying, Child SA creation and rekeying, reconnects, and heterogeneous peers. Record how optional exchange rounds and fallback policies affect what is actually negotiated. Include packet-size constraints and middleboxes in the test environment.

## Common interpretation errors

| Observation | What still needs checking |
|---|---|
| An endpoint advertises a hybrid group. | Which group did a representative client actually select? |
| A session uses PQ key establishment. | Which algorithms authenticate the peer and its certificate chain? |
| A certificate uses ML-DSA. | Do relying parties accept the encoding, chain, revocation mechanisms, and policy? |
| A library exposes a PQC API. | Does the consuming application call it, and does its protocol define the required use? |
| A protocol specification is published. | Do compatible implementations exist in the specific products and versions being evaluated? |
| A compatibility test succeeds. | What happens for unsupported peers, malformed input, rotation, and recovery? |

Capture the results in the [pilot report template](../templates/pilot-report.md), and use the [supplier questionnaire](../templates/supplier-questionnaire.md) for behavior you cannot observe directly.
