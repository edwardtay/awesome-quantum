// Educational primitive checks. This does not construct a secure channel.
import assert from 'node:assert/strict';
import * as crypto from 'node:crypto';

if (typeof crypto.encapsulate !== 'function' || typeof crypto.decapsulate !== 'function') {
  console.error('This example requires Node.js 24.7+ with ML-KEM and ML-DSA support.');
  console.error(`Detected ${process.version}. See examples/README.md.`);
  process.exit(1);
}

// The library generates keys and obtains randomness internally.
const kemKeys = crypto.generateKeyPairSync('ml-kem-768');
const { sharedKey, ciphertext } = crypto.encapsulate(kemKeys.publicKey);
const recoveredKey = crypto.decapsulate(kemKeys.privateKey, ciphertext);
assert(crypto.timingSafeEqual(sharedKey, recoveredKey), 'ML-KEM secrets should agree');
console.log('PASS ML-KEM-768: encapsulated and decapsulated secrets agree.');

// A same-length altered ciphertext exercises implicit rejection. Decapsulation
// returns different secret material, rather than authenticating the sender.
const changedCiphertext = Buffer.from(ciphertext);
changedCiphertext[0] ^= 1;
const rejectedKey = crypto.decapsulate(kemKeys.privateKey, changedCiphertext);
assert.equal(rejectedKey.length, sharedKey.length);
assert(!crypto.timingSafeEqual(sharedKey, rejectedKey), 'Altered ciphertext should not recover the original secret');
console.log('PASS ML-KEM-768: altered ciphertext produces a different secret.');

const signingKeys = crypto.generateKeyPairSync('ml-dsa-65');
const message = Buffer.from('awesome-quantum educational example', 'utf8');
const signature = crypto.sign(null, message, signingKeys.privateKey);
assert(crypto.verify(null, message, signingKeys.publicKey, signature));
console.log('PASS ML-DSA-65: original message and signature verify.');

const changedMessage = Buffer.from(message);
changedMessage[0] ^= 1;
assert(!crypto.verify(null, changedMessage, signingKeys.publicKey, signature));
console.log('PASS ML-DSA-65: changed message fails verification.');

const changedSignature = Buffer.from(signature);
changedSignature[0] ^= 1;
assert(!crypto.verify(null, message, signingKeys.publicKey, changedSignature));
console.log('PASS ML-DSA-65: changed signature fails verification.');

const unrelatedKeys = crypto.generateKeyPairSync('ml-dsa-65');
assert(!crypto.verify(null, message, unrelatedKeys.publicKey, signature));
console.log('PASS ML-DSA-65: unrelated public key fails verification.');

console.log(`Runtime: Node.js ${process.version}; OpenSSL ${process.versions.openssl}.`);
console.log('Six primitive checks passed. No keys or shared secrets were printed or written.');
