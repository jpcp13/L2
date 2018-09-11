
from math import *
from time import clock
import numpy as np
import matplotlib.pyplot as plt


'''
x=522
y=15
R=math.fmod(x,y)
Q=x/y
print Q
print R
'''

#Nombre premiers cest un nombre divisible par un et lui meme,et le resultat est un entier.

def is_prime(x):
  
    if x < 2:
        return False
    else:
        for n in xrange(2,x):
            if x % n == 0:
            	return False
        return True


def eratosthene(n):
    #retourne la tableau des nombres premiers <= n (crible d'eratosthene)
    n += 1
    tableau = [0,0] + [i for i in xrange(2, n)]
    for i in xrange(2, n):
        if tableau[i] != 0:
            # c'est un nombre 1er: on garde, mais on neutralise ses multiples
            for j in xrange(i*2, n, i):
                tableau[j] = 0
    return [p for p in tableau if p!=0]        



N = 1000
primes_liste = [n for n in range(N) if is_prime(n)]
cpt = 0
with open("primes.txt", "w") as fichier:
	for p in primes_liste:
		cpt += 1
		if cpt%10 != 0:
			fichier.write("{0} ".format(p))
		else:
			fichier.write("{0}\n".format(p))

def p(x) :
	return len([n for n in range(x) if is_prime(n)])



