#SABABADY Kamala
#SELVARAJAH Dinusan

from tp4 import *
from math import log

import matplotlib.pyplot as plt
import numpy as np 


k = primes(1000)
print(k)

titre = 'Tous les entiers premiers inferieurs a 1000:'
with open('primes.txt','w') as fichier:
    fichier.write(titre +'\n')
    fichier.write('\n')
    fichier.write(str(k)+'\n')
 

N = 1000
n2 = range (2,N)

gn = [n/log(n) for n in n2]
pin = [pi(n) for n in n2]

plt.clf()

plt.plot(n2,pin,'r-',n2,gn,'b')
plt.grid('on')
plt.axis('equal')
plt.savefig('graph.png')


n="n"
d="pi(n)"
h="n/log(n)"

print('{0:10} | {1:10} | {2:10}'.format(n,d,h))
t = "---------------------------------------------"
print(t)

for i in range (1,7):
    n = 10**i
    r = pi(n)
    y = n/log(n)
    print('{0:10} | {1:10} | {2:10}'.format(10**(i),r,y))

print('\n')

titre = '2. Crible d\'Erathotene, distribution des nombres premiers'
entete = '{0:15}|{1:15}|{2:15}'. format("n",d,h)
tirets = '-'*60
with open('pi.txt','w') as fichier:
    fichier.write(titre +'\n')
    fichier.write('\n')
    fichier.write(entete+'\n')
    fichier.write(tirets+'\n')
    for i in range (1,7):
	n = 10**i
    	r = pi(n)
    	y = n/log(n)
        ligne = '{0:15d}|{1:15g}|{2:15g}'. format(10**(i), r, y)
        fichier.write(ligne+'\n')
	fichier.write('\n')


