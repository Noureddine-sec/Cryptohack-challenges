"""
In this challenge we need to generate the PEM format  from the PUB format
For this the command ssh-keygen will help
ssh-keygen -f bruce_rsa.pub  -e -m pkcs8 > bruce_rsa.pem

the above command create a PEM format (AKA PKCS8) and write the this key in the file bruxe_rsa.pem
Afetr we will just use our script from previuous challenge
"""

from Crypto.PublicKey import RSA


pubKey = RSA.importKey(open('bruce_rsa.pem').read())
# print(pubKey.exportKey())

print(pubKey.n)