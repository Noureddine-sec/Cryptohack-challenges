# run the command on windows: python -m primefac -v 510143758735509025530880200653196460532653147

#  We can also use the web site : 
#  http://factordb.com

def factorize(m):
    import primefac
    import sys

    
    factors = list( primefac.primefac(m) )
    return factors

m= 510143758735509025530880200653196460532653147
print(factorize(m))