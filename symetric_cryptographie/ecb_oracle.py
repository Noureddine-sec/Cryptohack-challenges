#!/usr/bin/python3
import requests
import string
import binascii,json

url='http://aes.cryptohack.org/ecb_oracle/encrypt/'

"""
Function for hex encoding
"""
def hex(p):
    return (binascii.hexlify(p.encode())).decode()

"""
Logic is to take a reference block and compare with a block iterating ascii
Assume flag is      : crypto{wow}
Elignment is        : crypto{w ow}xxxxx (x is padding)
Send 'A'*15 now
the elignment is    : AAAAAAAA AAAAAAAc rypto{wo w}xxxxxx
                      -----------------
                       reference block
Send 'A'*15+'a-z'
now the elignment
is                  : AAAAAAAA AAAAAAAAa crypto{w ow}xxxxx
                      ------------------
                       identifier block
if reference block matches identifier block then we got the first letter. So this way we can obtain total flag ;)
"""
flag=''
input='A'*32 #Let's assume flag length is between 16-32
k=0
while k<33:
    for i in string.ascii_letters+string.digits+'{_}':
        r = requests.get(url+hex(input[:-1]))
        ref_block=json.loads(r.text)["ciphertext"][:64] #Reference block
        r = requests.get(url+hex(input[:-1]+flag+i))
        if json.loads(r.text)["ciphertext"][:64]==ref_block:
            flag+=i
            print("\r"+flag, flush=True, end='') #crypto{p3n6u1n5_h473_3cb}
            break
    k+=1
    input=input[:-1]