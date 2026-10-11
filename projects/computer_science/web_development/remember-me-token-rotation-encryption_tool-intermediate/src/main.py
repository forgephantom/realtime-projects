#!/usr/bin/env python3
"""Remember-Me Token Rotation: Encryption Tool: a stream cipher for Remember-Me Token Rotation data.

Remember-me cookies trade convenience for risk, so secure designs use rotating token series: a persistent series id plus a one-time token, where each use issues a fresh token and invalidates the old one. If a stolen token is replayed, the series mismatch reveals theft and the whole series is revoked. This gives long-lived login with theft detection built in.
Data idea: Simulates seeded login sessions including token theft and replay, verifying rotation succeeds and replay triggers full-series revocation.

Encrypts and decrypts bytes with a hand-written XOR stream cipher: the
keystream is SHA-256 in counter mode, so encryption and decryption are the
same XOR operation. Default run does a full encrypt/decrypt round trip and
prints the ciphertext hex plus a verification line.
"""

import argparse
import hashlib
import random

PARAMS = {'series_bytes': 'series identifier entropy', 'token_bytes': 'one-time token entropy', 'lifetime_days': 'remember-me duration'}


def derive_key(seed, key_text):
    """Derive a 32-byte key from --key text, or from the seed by default."""
    material = key_text if key_text else "stream-key-{}".format(seed)
    return hashlib.sha256(material.encode("utf-8")).digest()


def keystream(key, length):
    """SHA-256 counter-mode keystream of exactly `length` bytes."""
    out = b""
    counter = 0
    while len(out) < length:
        out += hashlib.sha256(key + counter.to_bytes(8, "big")).digest()
        counter += 1
    return out[:length]


class StreamCipher:
    """XOR stream cipher over a SHA-256 counter-mode keystream."""

    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        """Encrypt bytes; returns ciphertext bytes."""
        ks = keystream(self.key, len(plaintext))
        return bytes(a ^ b for a, b in zip(plaintext, ks))

    def decrypt(self, ciphertext):
        """Decrypt bytes; XOR is its own inverse."""
        return self.encrypt(ciphertext)


def main():
    parser = argparse.ArgumentParser(
        description="Remember-Me Token Rotation: Encryption Tool: encrypt Remember-Me Token Rotation data.")
    parser.add_argument("--seed", type=int, default=42,
                        help="random seed (default 42)")
    parser.add_argument("--key", default="",
                        help="passphrase (default: derived from --seed)")
    parser.add_argument("--encrypt", metavar="TEXT",
                        help="encrypt this text and print hex")
    parser.add_argument("--decrypt", metavar="HEX",
                        help="decrypt this hex string and print text")
    parser.add_argument("--message", default="Remember-Me Token Rotation payload 12345",
                        help="demo message for the default round trip")
    args = parser.parse_args()
    random.seed(args.seed)

    cipher = StreamCipher(derive_key(args.seed, args.key))

    if args.encrypt is not None:
        blob = cipher.encrypt(args.encrypt.encode("utf-8"))
        print(blob.hex())
        return
    if args.decrypt is not None:
        plain = cipher.decrypt(bytes.fromhex(args.decrypt))
        print(plain.decode("utf-8", errors="replace"))
        return

    plaintext = args.message.encode("utf-8")
    ciphertext = cipher.encrypt(plaintext)
    recovered = cipher.decrypt(ciphertext)
    print("Remember-Me Token Rotation stream-cipher round trip")
    print("plaintext : {}".format(args.message))
    print("ciphertext: {}".format(ciphertext.hex()))
    print("recovered : {}".format(recovered.decode("utf-8")))
    print("MATCH" if recovered == plaintext else "MISMATCH")


if __name__ == "__main__":
    main()
