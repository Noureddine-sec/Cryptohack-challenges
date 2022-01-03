import hashlib
import sys

def PoW( val_in, zeros):

  hex_dig=''
  working=''
  nonce=0
  while True:
    val=val_in+str(nonce)
    inp=val.encode()
    hash_object = hashlib.sha256(inp)
    hex_dig = hash_object.hexdigest()
    working=working+val+hex_dig+'\n'
    if (hex_dig.startswith(zeros)): break
    nonce=nonce+1
  print ('Nonce is ', nonce)
  print ('Result is ',val)
  print ('Hash is ',hex_dig)


message1='hello'
message2='current transaction: from Noureddine to marc send 1 btc: last block hash=0006bc9ad4253c42e32b546dc17e5ea3fe daecdabef371b09906cea9387e8696'
zeros="000"
PoW (message2, zeros)