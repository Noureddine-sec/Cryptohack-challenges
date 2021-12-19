from Crypto.Cipher import AES
import hashlib
import random
import binascii


# /usr/share/dict/words from
# https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words
with open("words.txt") as f:
    words = [w.strip() for w in f.readlines()]
   
# keyword = random.choice(words)

# KEY = hashlib.md5(keyword.encode()).digest()
# FLAG = ?


ciphertext= 'c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66'


    

# @chal.route('/passwords_as_keys/decrypt/<ciphertext>/<password_hash>/')
def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    print(password_hash)
    key = password_hash

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


# @chal.route('/passwords_as_keys/encrypt_flag/')
def encrypt_flag():
    cipher = AES.new(KEY, AES.MODE_ECB)
    encrypted = cipher.encrypt(FLAG.encode())

    return {"ciphertext": encrypted.hex()}



for c in words: 
    # print(c)
    KEY = hashlib.md5(c.encode()).digest()
    output= binascii.unhexlify(decrypt(ciphertext, KEY)['plaintext'])
    # print(output)
    # print('crypto{'.encode())
    if output.startswith('crypto{'.encode()):
        print("the key is :{}".format(c))
        print(output.decode())
        break