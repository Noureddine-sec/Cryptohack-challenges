# p = 857504083339712752489993810777

# q = 1029224947942998075080348647219

# and the exponent:

# e = 65537

# What is the private key d? 

p = 857504083339712752489993810777

q = 1029224947942998075080348647219

totient= (p-1)*(q-1)

e = 65537

d = pow( e, -1, totient)
print(d)

# result = 121832886702415731577073962957377780195510499965398469843281