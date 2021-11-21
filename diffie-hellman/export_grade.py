
"""
└─$ nc socket.cryptohack.org 13379
Intercepted from Alice: {"supported": ["DH1536", "DH1024", "DH512", "DH256", "DH128", "DH64"]}
Send to Bob: {"supported": ["DH64"]}                                                   
Intercepted from Bob: {"chosen": "DH64"}
Send to Alice: {"chosen": "DH64"}
Intercepted from Alice: {"p": "0xde26ab651b92a129", "g": "0x2", "A": "0xb9a2d39850e14d12"}
Intercepted from Bob: {"B": "0x250abc706476fb8e"}
Intercepted from Alice: {"iv": "53899ade29b766564a4bdd58d54074f4", "encrypted_flag": "4d684e0749805a96fb4e0b54f9b2668930610e71ce2f58e03353e0674f3e020b"}

"""

from sympy.ntheory import discrete_log
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')






msg= {"iv": "53899ade29b766564a4bdd58d54074f4", "encrypted_flag": "4d684e0749805a96fb4e0b54f9b2668930610e71ce2f58e03353e0674f3e020b"}



p=0xde26ab651b92a129
g=0x2
A=0xb9a2d39850e14d12
B=0x250abc706476fb8e
a=discrete_log(p,A,g)
print(a)

shared_secret = pow(B, a, p)
iv = msg['iv']
ciphertext = msg['encrypted_flag']

print(decrypt_flag(shared_secret, iv, ciphertext))





