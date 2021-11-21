from Crypto.PublicKey import RSA


pubKey = RSA.importKey(open('privacy_enhanced_mail.pem').read())
# print(pubKey.exportKey())

print(pubKey.d)
