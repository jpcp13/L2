from module import *
from math import log
from time import clock
import matplotlib.pyplot as plt
import numpy as np

#C
"""
L = primes(1000)
print(L)

titre = 'Entiers premiers inferieur a 1000'
with open('primes.txt','w') as fichier:
	fichier.write(titre + '\n')
	fichier.write('\n')
	fichier.write(str(L) + '\n')

#D

N = 1000
nn = range(2, N)

gn = [n/log(n) for n in nn]
pin = [pi(n) for n in nn]

plt.clf()

plt.plot(nn, pin, 'r-', nn, gn, 'b-')
plt.grid('on')
plt.axis('equal')
plt.savefig('graph2.png')
"""
#E

n = "n"
d = "pi(n)"
t = "n/log n"


print('{0:10} | {1:10} | {2:10}'.format(n,d,t))

m = "----------------------------------------------"
print (m)

for i in range (1,7):
	p = 10**i
	V = pi(p)
	g = p / log(p)
	print('{0:10} | {1:10} | {2:10}'.format(10**(i), V, g))


print('\n')

with open('table1.txt','w') as fichier:
	entete = '{0:15}|{1:15}|{2:15}'.format(n,d,t)
	tirets = '-'*50
	fichier.write('\n')
	fichier.write(entete+'\n')
	fichier.write(tirets+'\n')
	for i in range (1,7):
		p = 10**i
	    	V = pi(p)
	    	g = p/log(p)
	        ligne = '{0:15d}|{1:15g}|{2:15g}'.format(10**(i), V, g)
	        fichier.write(ligne+'\n')
		fichier.write('\n')


