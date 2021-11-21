
"""Need to conc=vert the x509 certfiicate from the DER form to the PEM format, 
so we can use the same command as in the previous challenge
the commande for converting : 
 openssl x509 -inform der -in 2048b-rsa-example-cert.der -out 2048-rsa-example-cert.pem 
 the PEM file will be in the same folder. 
 """
from Crypto.PublicKey import RSA

key = RSA.importKey(open('2048-rsa-example-cert.pem').read())



print(key.n)