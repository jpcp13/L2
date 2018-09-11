#EXO1
from math import*
import numpy as np


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


Q = []
Q = primes(200)

