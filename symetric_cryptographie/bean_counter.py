import requests
from Crypto.Util.strxor import strxor

url='http://aes.cryptohack.org/bean_counter/encrypt/'
response=requests.get(url)

data=bytes.fromhex(response.json()['encrypted'])

#this was the only clue to figuring out the iv
#the file was a .png image, which has its initial 16 bytes fixed more or less 
header=bytes.fromhex('89504e470d0a1a0a0000000d49484452')

iv=strxor(header,data[:16])

plaintext=b''
for i in range(0,len(data),16):
	block=data[i:i+16]
	plaintext+=strxor(block,iv[0:len(block)])


f=open('flag.png','wb').write(plaintext)