import numpy as np
import math
#exo 1
#d
def is_prime(n):
	if (n < 2):
		return False
	
	for p in range(2, (int(np.sqrt(n))+1)):
		if n%p == 0:
			return False

	return True
#e
def Fn(n):
	return 2**(2**n) + 1

#exo 2
#b
def primes(n):
	P = [k for k in range(2, n) if is_prime(k)]
	return P
#d
def pi(n):
	return np.shape(primes(n))[0]

def f(n):
	return n/(math.log(n))
#e

def pgcd(a, b):
	r = a%b
	while r != 0:
		a = b
		b = r
		r = a%b
	return b
#hors tp
def listesABR(a, b):
	r = a%b
	A = []
	B = []
	R = []
	while r != 0:
		A.append(a)
		B.append(b)
		R.append(r)
		a = b
		b = r
		r = a%b
	return A,B,R

#exo 3
#c
def factors(n):
	P = primes(n)
	FF = []
	for p in P:
		while n%p == 0:
			n = n/p
			FF.append(p)
	return FF						
#exo 4
#e
def euclide(a,b):
	d = a
	dp = b
	x = 1
	y = 0
	xp = 0
	yp = 1
	while (dp != 0):
		q = d/dp
		ds = d
		xs = x
		ys = y
		d = dp
		x = xp
		y = yp
		dp = ds - q*dp
		xp = xs - q*xp
		yp = ys - q*yp
	return d,x,y

def difference(A,B):
	C = []
	c =  np.shape(A)[0]
	for i in range(0, c):
		a = A[i]
		if a not in B:
			C.append(a)
	return C



