"""
Intercepted from Alice: {"p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", "g": "0x02", "A": "0xb1460e1bb9c45ed20f8756f3d9d6d6d00d85099fe1a5bef23fe420344924ff4107b71e16c319c39e32517a25368934d4cfadab418711bc72e1a04c0fc06df1def2407f4ef063db0b81a9da3f4314faf859adcbe2a36d762e6cd6bdc9246274a3b4800c186e422f292387f5879497bcbcc16628e0e185a0a6c492e55525c0e1fdfbd45dc0db8639db6e5b2c75411db1158093710d7323f896616ee5e40bfc355ab5c7ebb2b8ffe23278d749d8f4065eaaa8c4dc677e92bdd33b38d9acf2a1e4f2"}
Intercepted from Bob: {"B": "0x8d79b69390f639501d81bdce911ec9defb0e93d421c02958c8c8dd4e245e61ae861ef9d32aa85dfec628d4046c403199297d6e17f0c9555137b5e8555eb941e8dcfd2fe5e68eecffeb66c6b0de91eb8cf2fd0c0f3f47e0c89779276fa7138e138793020c6b8f834be20a16237900c108f23f872a5f693ca3f93c3fd5a853dfd69518eb4bab9ac2a004d3a11fb21307149e8f2e1d8e1d7c85d604aa0bee335eade60f191f74ee165cd4baa067b96385aa89cbc7722e7426522381fc94ebfa8ef0"}
Intercepted from Alice: {"iv": "66b107e4efa28c04513adc6e5953b292", "encrypted": "89e53f4ecfc8772df144454c4e8aa8b3d85a4233f9f7f7a6b457d081b5792df3"}

Modification of initial g <-- A and sent it to bob so we can get A^b mod p=shared secret

# We should make sure that the new value of 1 is shorted, because the lenth of hole message sould < 1024bits{"p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", "g": "0xb1460e1bb9c45ed20f8756f3d9d6d6d00d85099fe1a5bef23fe420344924ff4107b71e16c319c39e32517a25368934d4cfadab418711bc72e1a04c0fc06df1def2407f4ef063db0b81a9da3f4314faf859adcbe2a36d762e6cd6bdc9246274a3b4800c186e422f292387f5879497bcbcc16628e0e185a0a6c492e55525c0e1fdfbd45dc0db8639db6e5b2c75411db1158093710d7323f896616ee5e40bfc355ab5c7ebb2b8ffe23278d749d8f4065eaaa8c4dc677e92bdd33b38d9acf2a1e4f2", "A": "0xb1460e1bb9c45ed20f8756f3d9d6d6d00d85099fe1a5bef23fe42"}

Bob connects to you, send him some parameters: {"p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", "g": "0xb1460e1bb9c45ed20f8756f3d9d6d6d00d85099fe1a5bef23fe420344924ff4107b71e16c319c39e32517a25368934d4cfadab418711bc72e1a04c0fc06df1def2407f4ef063db0b81a9da3f4314faf859adcbe2a36d762e6cd6bdc9246274a3b4800c186e422f292387f5879497bcbcc16628e0e185a0a6c492e55525c0e1fdfbd45dc0db8639db6e5b2c75411db1158093710d7323f896616ee5e40bfc355ab5c7ebb2b8ffe23278d749d8f4065eaaa8c4dc677e92bdd33b38d9acf2a1e4f2", "A": "0xb1460e1bb9c45ed20f8756f3d9d6d6d00d85099fe1a5bef23fe42"}
Bob says to you: {"B": "0xa2db2c7a0abad0a7acd5b584feba07972b5f8ca5cba4c5bbbcf61245375ed4f9fe530c32a70bf8b3e1e17222210ef5533a116365506c2053d71d0d8d1f8ec40734a00e4ef8659e9198b467fc8bbe076bab6ccba74dd9c1ce30f70830f5ba3f661ed39bf36ed8ddab0bd077b272e08b78e7bbaf2ba4e254f4a167a5e70cef7af86a0889a661407019e922605b34127ecc8afc1b4a9ab153bea14467e173f3d7588475784ffd24da1759e8eb4b18244b9b2221e9b6b4e252e7496038116aaf56db"}
Bob says to you: {"iv": "9f9d5a5c235e6334e060d2bf1550e076", "encrypted": "31e191e85044fa4ac194daff28c4285336b421f7d74510c46ed4027d960694165a6d614772db3bcde732d3c42c48c12f7cf95e3ae27333ccfaf294cfb1891f89e2fa6d65c451b2f3f72f8a771b809991"}

"""
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
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



msg = {"iv": "66b107e4efa28c04513adc6e5953b292", "encrypted": "89e53f4ecfc8772df144454c4e8aa8b3d85a4233f9f7f7a6b457d081b5792df3"}



shared_secret = 0xa2db2c7a0abad0a7acd5b584feba07972b5f8ca5cba4c5bbbcf61245375ed4f9fe530c32a70bf8b3e1e17222210ef5533a116365506c2053d71d0d8d1f8ec40734a00e4ef8659e9198b467fc8bbe076bab6ccba74dd9c1ce30f70830f5ba3f661ed39bf36ed8ddab0bd077b272e08b78e7bbaf2ba4e254f4a167a5e70cef7af86a0889a661407019e922605b34127ecc8afc1b4a9ab153bea14467e173f3d7588475784ffd24da1759e8eb4b18244b9b2221e9b6b4e252e7496038116aaf56db

iv = msg['iv']
ciphertext = msg['encrypted']

print(decrypt_flag(shared_secret, iv, ciphertext))