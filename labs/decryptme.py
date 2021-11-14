import string
import random
from base64 import b64encode, b64decode

secret_encoding_inv = ['step1_inv', 'step2_inv', 'step3_inv']

def step1_inv(s):
	_step1 = string.maketrans("mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON", "zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA")
	return string.translate(s, _step1)

def step2_inv(s): return b64decode(s)

def step3_inv(s, shift=4):
    loweralpha = string.ascii_lowercase
    shifted_string = loweralpha[shift:] + loweralpha[:shift]
    converted = string.maketrans(shifted_string, loweralpha)
    return s.translate(converted)

def make_plain(text):
  a = text
  index = int(a[0])
  while 1 <= index <= 3:
    a2 = a[1:]
    r=secret_encoding_inv[index-1]
    a = globals()[r](a2)
    try:
      index = int(a[0])    
    except:
      break
  return a


f=open('intercepted.txt','r')
print(make_plain(f.read()))




