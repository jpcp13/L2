#Fonctions
from math import*
import numpy as np

def f(x):
	return x/log(x)

def fermat(n):
	return 2**2**n +1

def is_prime(p):

	card_div_p = 0
	d = 2

	while d <= floor(sqrt(p)):

		if (p % d == 0):
			card_div_p += 1

		d += 1


	if card_div_p == 0:
		return True


	else:
		return False

def primes(n):

	P = [] 

	for i in range(2,n+1):

		if is_prime(i):
			P.append(i)


	return P

def factors(n):

	P = []
	D = primes(n)
	p = D[0]
	l = int(sqrt(n))
	N = n
	for i in range(1,l+1):
		if (N % p == 0):
			while(N % p == 0):
				N = N/p
				P.append(p)
			
		p = D[i]
		

	return P







def euclide (a,b):

	r1 = a
	u1 = 1
	v1 = 0
	r2 =b
	u2 = 0
	v2 = 1

	while r2 != 0:

		q = r1/r2

		r1 = r2
		u1 = u2
		v1 = v2
		r2 = r1 - q*r2
		u2 = u1 -q*u2
		v2 = v1 - q*v2

	return r1, u1, v1 
		



