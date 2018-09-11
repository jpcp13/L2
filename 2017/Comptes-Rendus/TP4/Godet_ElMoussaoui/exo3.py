import math
def factors(n):
    F = []
    if n==1:
        return F
   
    while n>=2:
        q,r = divmod(n,2)
        if r!=0:
            break
        F.append(2)
        n = q
    
    i=3
    racine = math.sqrt(n)+1
    while i<=n:
        if i>racine:
            F.append(n)
            break
        q,r = divmod(n,i)
        if r==0:
            F.append(i)
            n=q
            racine = math.sqrt(n)+1
        else:
            i += 2
    return F


f = factors(4864)
print f
print factors(3458)
