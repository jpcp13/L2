from math import * 
from string import *
from pylab import *

def is_prime(n):
	if n == 0:
		return False 
	for i in range(2,n-1):
		if n%i == 0 :
			return False
	return True
	
def Fermat(n):
	return (2**(2**n)) + 1

def primes(n):
	liste = [] 
	for i in range(2,n):
		if is_prime(i) == True: 
			liste.append(i)
	return liste

def Pi(n):
	S = 0
	for i in range(2,n):
		if is_prime(i) == True:
			S = S +1 
	return S

def factors(n):
	liste = list()
	i = 2
	j = 2
	N = n 
	while i < n+1:
		if n % i == 0 and is_prime(i) == True:
				liste.append(i)
				n = n/i
				while n % i == 0 and N % i**j == 0:
					liste.append(i)
					j += 1
					n = n/i
		i += 1
		j = 2
	return liste 

def euclide(a,b):
	if a < b:
		a,b = b,a 
	while b > 0: 
		r = a % b
		a = b 
		b = r 
	return a 



















	
