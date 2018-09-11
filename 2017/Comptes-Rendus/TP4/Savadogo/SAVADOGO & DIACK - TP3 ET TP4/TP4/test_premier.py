from math import *



def primes(n, p=[2,3,5]):
    
    k = p[-1]+2
    if n < k:
        return [x for x in p if x<=n]
    while k <= n:
        i = 0
        while i < len(p):
            if p[i]*p[i] > k:
                p.append(k)
                break
            if (k % p[i]) == 0:
                break
            i += 1
        k += 2
    return p
 

