from tp4 import *
from math import log
import matplotlib.pyplot as plt
import numpy as np

#a)voir fichier odt
#b) voir tp4.py
#c) 

L = primes(1000)
print(L)

titre = ' Entiers premiers inferieurs a 1000'
with open('primes.txt','w') as fichier : 
	fichier.write(titre +'\n')
	fichier.write('\n')
	fichier.write(str(L)+'\n')

#d)

N = 100
nn = range(2, N)

gn = [n/log(n) for n in nn]
pin = [pi(n) for n in nn]

plt.clf()

plt.plot(nn, pin, 'r-', nn, gn, 'b') 
plt.grid('on')
plt.axis('equal')
plt.savefig('graph2.png')

#e)
n = "n"
d = "pi(n)"
t = "n/log n"

print('{0:10}| {1:10} | {2:10}'.format(n,d,t))

t = "----------------------------------------------"
print(t)
for i in range(1, 6):
	p = 10**i	
	V = pi(p)
	g = p/log(p)
	print('{0:10}|{1:10}  |{2:10}'.format(p,V,g))

