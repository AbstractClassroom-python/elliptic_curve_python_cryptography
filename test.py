import json
from EllipticCurve import EllipticCurve
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def load_curve_from_json(curve_id, filepath="curves.json"):
    with open(filepath, "r") as f:
        data = json.load(f)
    if curve_id not in data:
        raise ValueError(f"Curve '{curve_id}' not found in {filepath}")
    
    params = data[curve_id]
    return EllipticCurve(
        int(params["a"]),
        int(params["b"]),
        int(params["p"]),
        int(params["Gx"]),
        int(params["Gy"]),
        int(params["n"])
    )

# === Driver code ===
if __name__ == "__main__":
    ecc = load_curve_from_json("NIST_P256")

    # Generate key pairs
    alice_priv, alice_pub = ecc.generate_keypair()
    bob_priv, bob_pub = ecc.generate_keypair()

    print("Alice Private:", alice_priv)
    print("Alice Public: ", alice_pub)
    print("Bob Private:  ", bob_priv)
    print("Bob Public:   ", bob_pub)

    # Derive shared point and AES key
    shared_point = ecc.get_shared_key_point(alice_priv, bob_pub)
    print("Shared Point: ", shared_point)

    aes_key = ecc.get_shared_key(alice_priv, bob_pub)
    print("AES Key:      ", aes_key.hex())

    # Encrypt a message using AES
    plaintext = b"Top secret from Alice to Bob"
    cipher = AES.new(aes_key, AES.MODE_CBC)
    iv = cipher.iv
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    # print("Ciphertext:   ", ciphertext.hex())

    # Decrypt with Bob's AES key
    bob_aes_key = ecc.get_shared_key(bob_priv, alice_pub)
    assert aes_key == bob_aes_key

    decipher = AES.new(bob_aes_key, AES.MODE_CBC, iv)
    decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)
    print("Decrypted:    ", decrypted)

    # ECDSA Sign and Verify
    message = "Signed message"
    signature = ecc.sign(message, alice_priv)
    # print("Signature:    ", signature)

    valid = ecc.verify(message, signature, alice_pub)
    print("Signature valid?", valid)