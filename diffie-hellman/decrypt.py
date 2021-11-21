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


# if __name__ == '__main__':
#     shared_secret = '?'
#     iv = '?'
#     ciphertext = '?'

#     print(decrypt_flag(shared_secret, iv, ciphertext))
# Solution script
#from decrypt import decrypt_flag

g=2

b=197395083814907028991785772714920885908249341925650951555219049411298436217190605190824934787336279228785809783531814507661385111220639329358048196339626065676869119737979175531770768861808581110311903548567424039264485661330995221907803300824165469977099494284722831845653985392791480264712091293580274947132480402319812110462641143884577706335859190668240694680261160210609506891842793868297672619625924001403035676872189455767944077542198064499486164431451944
A=0x404a8ebffd1b9d954f5dc4edacc06b9033b613203592664ded9201dc09763cabfccdca8a59de83b4fd11b211285a320b7f97352ea5de9f6f5112a572c41a39409ee4bf9d3b04c790f265a36ea7d543ee6e5b55f5fe0c87097ac382b796d6be38104a5c5b82a5324664280496a95895ddb88dc4b7ec36e037389d5330b4f8a30f0c525f86d6e14f49080863aab60a08bd802895d382842f09a42215d1d45fc82440d5421aa7986e4c68b40fab5eefd455f2337a15f5f21664d85a24fecd4f2b1c
p=0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff
B=pow(g,b,p)

B=hex(B)
print(B)
# p=int(p,16)
# A=int(A,16)

# B=0x83e907190b6484aa982847f873111a28a3f1a0617a0973b24f8ed036d01d01009f050fa636cfe030cdd26f1309465cdea4ebc97d421fa5ebeedda63d948c8b00e81c8e8e63e720ad74bf867139ac2112883928d0441290f9f40e67a44e4447b7f8841f6f573b8b6a85d679bb611d7f026a4c2c904dd4a97a2d0048531f43b78e7c539d9e59149229ed32630506d11f13b42609bb4b8c4644e0f3ede537022ac7de96288c1794746f3f57b25a2668363a4314879c3834a9961ba3800f7de4798d

msg= {"iv": "67a6aa4e9ba6d424e178adaa50a0d809", "encrypted_flag": "2733077364230ca6c7a8f80bb32bf5be161d627d8be897ee167d20d02f0b2a1e"}






shared_secret = pow(A, b, p)
iv = msg['iv']
ciphertext = msg['encrypted_flag']

print(decrypt_flag(shared_secret, iv, ciphertext))
