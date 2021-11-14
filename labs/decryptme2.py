import string
import random
from base64 import b64encode, b64decode

secret_encoding_inv = ['step1_inv', 'step2_inv', 'step3_inv']

def step1_inv(s):
	_step1 = str.maketrans("mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON", "zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA")
	return str.translate(s, _step1)

def step2_inv(s): return b64decode(s).decode("utf-8")

def step3_inv(s, shift=4):
    loweralpha = string.ascii_lowercase
    shifted_string = loweralpha[shift:] + loweralpha[:shift]
    converted = str.maketrans(shifted_string, loweralpha)
    return s.translate(converted)

def make_plain(text):
  a = text
  index = int(a[0])
  count =0
  while 1 <= index <= 3:
    count +=1
    a2 = a[1:]
    r=secret_encoding_inv[index-1]
    a = globals()[r](a2)
    try:
      index = int(a[0])    
    except:
      break
  print('the file has been enrypted {} times and the value of count is {}. the original message was:'.format(count, count-1))
  return a


f=open('intercepted.txt','r')
print(make_plain(f.read()))




