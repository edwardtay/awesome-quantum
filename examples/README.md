# Hands-on PQC example

[← Awesome Quantum](../README.md) · [Learning paths](../docs/learning-paths.md)

Run [node-pqc.mjs](node-pqc.mjs) with Node.js 24.7 or newer and a build supporting ML-KEM and ML-DSA:

```sh
node examples/node-pqc.mjs
```

Run the command from the repository root. The example uses built-in cryptographic APIs, requires no npm packages or network connection, and generates fresh keys in memory. Older runtimes exit with a requirement message.

| Check | Observation |
|---|---|
| ML-KEM-768 round trip | Both operations produce the same shared secret. |
| Altered ciphertext | Same-length tampering produces a different secret through implicit rejection. |
| ML-DSA-65 round trip | The original message verifies. |
| Changed message | Verification fails. |
| Changed signature | Verification fails. |
| Unrelated verification key | Verification fails. |

The script prints pass messages and runtime versions. It does not print key material. Its assertions check these examples; they are not standard conformance vectors, an audit, or a protocol implementation.

A KEM alone does not authenticate a peer. For a network application, evaluate a defined protocol and its implementation using the [protocol guide](../docs/protocols.md). Do not turn the example into a custom transport protocol.

## API references

- [Node.js 24 crypto documentation](https://nodejs.org/docs/latest-v24.x/api/crypto.html) for key generation, encapsulation, decapsulation, signing, verification, and API stability.
- [FIPS 203](https://csrc.nist.gov/pubs/fips/203/final) for ML-KEM's definition and rejection behavior.
- [FIPS 204](https://csrc.nist.gov/pubs/fips/204/final) for ML-DSA's definition.

## Validation record

Executed on 2026-10-24 with Node.js 24.22.1 and its bundled OpenSSL 3.5.9: all six assertions passed. The runtime archive's SHA-256 matched Node.js's published distribution manifest. The older installed Node.js 20.20.0 exited with the documented requirement message. The temporary validation runtime was kept separate from system Node.js.

The GitHub Actions workflow includes an independent Node.js 24 job to rerun the example. Hosted CI also passed on 2026-10-24 after publication.
