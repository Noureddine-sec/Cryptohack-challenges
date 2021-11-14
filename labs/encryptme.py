# This is the program we believe was used to encode the intercepted message.
# some of the retrieved program was damaged (show as &&&&)
# Can you use this to figure out how it was encoded and decode it? 
# Good Luck

import string
import random
from base64 import b64encode, b64decode

secret = 'Why do elephants have big ears?' # We don't know the original message or length

secret_encoding = ['step1', 'step2', 'step3']
secret_encoding_inv = ['step1_inv', 'step2_inv', 'step3_inv']

def step1(s):
	_step1 = string.maketrans("zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA","mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON")
	return string.translate(s, _step1)

def step1_inv(s):
	_step1 = string.maketrans("mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON", "zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA")
	return string.translate(s, _step1)

def step2(s): return b64encode(s)
def step2_inv(s): return b64decode(s)

def step3(plaintext, shift=4):
    loweralpha = string.ascii_lowercase
    shifted_string = loweralpha[shift:] + loweralpha[:shift]
    converted = string.maketrans(loweralpha, shifted_string)
    return plaintext.translate(converted)

def step3_inv(s, shift=4):
    loweralpha = string.ascii_lowercase
    shifted_string = loweralpha[shift:] + loweralpha[:shift]
    converted = string.maketrans(shifted_string, loweralpha)
    return s.translate(converted)

def make_secret(plain, count):
	a = '2{}'.format(b64encode(plain))
	# print('a -> {}'.format(a))
	for count in xrange(count):
		r = random.choice(secret_encoding)
		si = secret_encoding.index(r) + 1
		_a = globals()[r](a)
		a = '{}{}'.format(si, _a)
	return a

def decode(text):
	a = text
	index = int(a[0])
	while 1 <= index<= 3:
		print(index)
		a = globals()[secret_encoding_inv[index-1]](a)
		try: index = int(a[0])
		except: break
	return a
if __name__ == '__main__':
	print(make_secret(secret, count=68))
	# f = open('intercepted.txt','r')
	# print(decode(f.read()))




