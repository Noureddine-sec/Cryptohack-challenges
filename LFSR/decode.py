import codecs



def shift12(r):
  r0=str(int(r[1],2)^int(r[6],2))

  s=str(int(r[11]))

  return s, (r0+r[:11])

def shift12_byte1(r):
    byte1 = ''
    for i in range(8):
        b =  shift12(r)
        r = b[1]
        byte1 = b[0]+byte1

    return byte1,r



def shift19(r):

  r0= str(int(r[4],2) ^ int(r[10],2))

  s=str(int(r[18]))

  return s, (r0+r[:18])

def shift19_byte2(r):
    byte2 = ''
    for i in range(8):
        b =  shift19(r)
        r = b[1]
        byte2 = b[0]+byte2

    return byte2,r

def lfsr(reg1, reg2):
    result = shift12_byte1(reg1)
    key1 = result[0]
    reg1 = result[1]
    result = shift19_byte2(reg2)
    key2 = result[0]
    reg2 = result[1]
    new_key = (int(key1,2) + int(key2,2))%255 
    return new_key, reg1, reg2


def decipher(reg1, reg2, cipher):
    result = shift12_byte1(reg1)
    key1 = result[0]
    reg1 = result[1]
    result = shift19_byte2(reg2)
    key2 = result[0]
    reg2 = result[1]
    key = (int(key1,2) + int(key2,2))%255 

    plain = int(cipher.hex(),16) ^ key

    return reg1, reg2, plain


seed1 = '110010111000'
seed2 = '0100101100000110001'
reg1= seed1
reg2= seed2
f1 = open("flag.enc","rb")
f2 = open("flag.png","wb")

value = f1.read(1)

while value:
    print(value)
    decoded = decipher(reg1,reg2,value)
    reg1 = decoded[0]
    reg2 = decoded[1]
    decoded_byte = decoded[2]
    decoded_byte = int(decoded_byte)
    print(decoded_byte)
    decoded_byte = decoded_byte.to_bytes(1,byteorder='big')

    print(decoded_byte)
    f2.write(decoded_byte)

    value = f1.read(1)

f1.close()
f2.close()


