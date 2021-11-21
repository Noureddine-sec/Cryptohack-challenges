

data = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')
print(data)
key = data[0] ^ ord('c')

flag=""
for c in data:
    flag += chr(c ^ key)

print(flag)
