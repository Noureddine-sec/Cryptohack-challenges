p = 29
ints = [14, 6, 11] 
result= []
for i in ints: 
    for j in range(p):
        x= pow(j,2,p)
        if x == i: 
            result.append(j)

print(result)
print(min(result))

