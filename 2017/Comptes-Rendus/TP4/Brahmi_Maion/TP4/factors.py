from tp4 import *
from math import *
from time import *
			 


def factors(n):
    
    f = []
    if n==1:
        return f
    
    while n>=2:
        x,r = divmod(n,2)
        if r!=0:
            break
        f.append(2)
        n = x
   
    i=3
    rn = sqrt(n)+1
    while i<=n:
        if i>rn:
            f.append(n)
            break
        x,r = divmod(n,i)
        if r==0:
            f.append(i)
            n=x
            rn = sqrt(n)+1
        else:
            i += 2
    return f   
     
