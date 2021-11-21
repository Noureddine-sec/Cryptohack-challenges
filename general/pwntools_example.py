from pwn import * # pip install pwntools
import json
from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
import codecs
import random
from binascii import unhexlify

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def list_to_string(s):
    output = ""
    return(output.join(s))

for i in range(101):
    received = json_recv()
    print("hello")
    if "flag" in received:
        print('FLAG:{}'.format(received["flag"]))
        break

    print("-Iteration : {}".format(i))
    print("-Received type: {}".format(received["type"]))
    print("-Received value: {}".format(received["encoded"]))

    value = received["encoded"]
    encoding = received["type"]


    if encoding== "base64":
        decoded = base64.b64decode(value).decode('utf8')
    elif encoding == "hex":
        decoded=(unhexlify(value)).decode('utf8')
    elif encoding=="rot13":
        decoded=codecs.decode(value, 'rot_13')
    elif encoding =="bigint":
        decoded=unhexlify(value.replace("0x","")).decode('utf8')
    elif encoding=="utf-8":
        decoded = list_to_string([chr(b) for b in value])

    print ("- Decoded : {}".format(decoded))
    print ("- Decoded type : {}".format(type(decoded)))



# print("Received type: ")
# print(received["type"])
# print("Received encoded value: ")
# print(received["encoded"])

    to_send = {
        "decoded": decoded
    }
    json_send(to_send)

# json_recv()
