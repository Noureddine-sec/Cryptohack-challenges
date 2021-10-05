#Base 64 Challenge
import base64
input='72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
output=bytes.fromhex(input)
output=base64.b64encode(output)
print(output)