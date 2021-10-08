
def gcd():
    a= input("give your first number:")
    b= input("give your second number:")


    if a>b : 
        result=a
        while (result!=0):
            result= a%b
            a=b
            b=result
        return a


    else:
        result=b
        while (result!=0):
            result= b%a
            b=a
            a=result
        return b

print (gcd())
# Teh resut of print(gcd()) with a= 12, and b=8 is 4
# The esut of print(gcd()) with a= 66528, and b= 52920 is  1512 
#    