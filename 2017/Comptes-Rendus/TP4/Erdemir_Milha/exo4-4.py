from tp4 import *

#a)

a= factors(4864)
print(a)

b = factors(3458)
print(b)

y = euclide(4864,3458)
print(y)

u = primes(200)
print(u)

#e)

def euclide(a, b):
    r, u, v = a, 1, 0
    rp, up, vp = b, 0, 1
    while rp != 0:
        q = r//rp
        rs, us, vs = r, u, v
        r, u, v = rp, up, vp
        rp, up, vp = (rs - q*rp), (us - q*up), (vs - q*vp)

    return (r, u, v)

    
