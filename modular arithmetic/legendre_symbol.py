def legendre_check(a,p):
    if pow(a, (p-1)/2, p) % p = 1: 
        print "{} is a quadratic residus mod {}".format(a,p)
    if pow(a, (p-1)/2, p) % p = -1: 
        print "{} is a quadratic non-residus mod {}".format(a,p)

legendre(10,1024)