from tp4 import *

def factors(n):
	Primes = primes(n)
	FF = []
	for p in Primes:
		while n%p == 0:
			n = n/p
			FF.append(p)
	return FF


p = factors(60)
print(p)


    
