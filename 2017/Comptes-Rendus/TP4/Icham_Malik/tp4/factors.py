from tp4 import *


from time import time
from math import sqrt
 
def ifactor(n):
    p = xrange(2,int(sqrt(n))+1)
    pl = []
    k = 0
    while n>1 and k < len(p):
        i = 0
        q = n/p[k]
        while q*p[k] == n:
            i = i + 1
            n = q
            q = n/p[k]
        if i != 0:
            pl.append((p[k],i))
        k = k + 1
    return pl
 
n = 25
start = time()
print 'ifactor(', n, ') =', ifactor(n)

