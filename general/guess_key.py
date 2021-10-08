from pwn import xor
input=bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104') 
#We know that the flag start by 'crypto{' => so we will xor this part with the input
guess='crypto{'
guess= guess.encode()
key=xor(input, guess)
print (key)
#the result is b'myXORke+y_Q\x0bHOMe$~seG8bGURN\x04DFWg)a|\x1dTM!an\x7f'
#We find that the key start by 'myXORke'
#let's assume that our expected key is 'myXORkey'
#If we xor this key with the input , the xor() function will repeat (padding) the key many time 
# in order to cover all the input message
flag=xor(input, 'myXORkey'.encode())
print(flag)
