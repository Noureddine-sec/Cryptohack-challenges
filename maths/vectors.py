import numpy as np
v = (2,6,3)
w = (1,0,0) 
u = (7,7,2) 
v=np.array(v)
w=np.array(w)
u=np.array(u)
print(v)
print(w)
print(u)
print(2*v)
# calculate 3*(2*v - w) ∙ 2*u. 
result= np.dot(3*(2*v - w) , 2*u)
print(result)