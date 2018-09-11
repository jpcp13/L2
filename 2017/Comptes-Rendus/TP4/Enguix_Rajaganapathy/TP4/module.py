#RAJA GANAPATHY Srinivas
#ENGUIX Precillia

#FONCTIONS

from math import sqrt

def is_prime(n):
	if n==0 or n==1:
		return False
	if n==2:
		return True
	else:
		i = 2
		k = 1
		while i<= sqrt(n):
			if n % i == 0:
				k = 0
				break
			else:
				i = i+1
	if k == 0:
		return False
	else:
		return True

def primes(n):
	return [i for i in range(2, n+1) if is_prime(i)]

def pi(n):
	L = primes(n)
	k = len(L)
	return k

def factors(n):
	Primes = primes(n)
	FF = []
	for p in Primes:
		while n%p == 0:
			n = n/p
			FF.append(p)
	return FF

def euclide(a,b):
	r, u, v = a, 1, 0
	rp, up, vp = b, 0, 1
	while rp != 0:
		q = r//rp
		rs, us, vs = r, u, v
		r, u, v = rp, up, vp
		rp, up, vp = (rs - q*rp), (us - q*up), (vs - q*vp)
	return (r, u, v)



