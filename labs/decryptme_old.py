

import string
import random
from base64 import b64encode, b64decode

secret = '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'


secret_decoding = ['step1', 'step2', 'step3']

def step1(s):
	_step1 = string.maketrans("zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA","mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON")
	return string.translate(s, _step1)

def step2(s): return b64decode(s)

def step3(plaintext, shift=-4):
    loweralpha = string.ascii_lowercase
    shifted_string = loweralpha[shift:] + loweralpha[:shift]
    converted = string.maketrans(loweralpha, shifted_string)
    return plaintext.translate(converted)


def decrypt_secret(secret_text):
    count = 0
    while True:
        si = 0
        count = count +1
        try:
            si = int(secret_text[0])
            r = secret_decoding[si-1]
        except:
            print ("Counter used for encryption =", count) 
            return secret_text
        secret_text = secret_text[1:]
        _secret_text = globals()[r](secret_text)
        secret_text = _secret_text



print(decrypt_secret(secret))