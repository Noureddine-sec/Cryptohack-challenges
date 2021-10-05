
input='string'
key=13
ords=[ord(x)^13 for x in input]
output="".join(chr(o) for o in ords)
print(output)