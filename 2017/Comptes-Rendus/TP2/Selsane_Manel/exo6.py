from tp2 import *
from math import pi
from time import clock

#a)

import numpy as np
import matplotlib.pyplot as plt

t =np.linspace(0, 2*pi, 40)

x = np.cos(t)
y = np.sin(t)

plt.plot(x,y)
plt.grid('on')
plt.axis('equal')
plt.savefig('cercle1.png')

#b)

import numpy as np
import random

print(np.random.uniform(0,1,10))
print(np.random.uniform(-1,1,10))

#c)
N = 1000
X = np.random.uniform(-1,1,N)
Y = np.random.uniform(-1,1,N)

aa,bb,cc,dd=[] ,[] ,[] ,[]
I = 0
E = 0
for i in range(1000):

	if (X[i]**2 + Y[i]**2)>1:
		
		A = X[i]
		aa.append(A)
		B = Y[i]
		bb.append(B)
		E +=1

	else: 
		
		C = X[i]
		cc.append(C)
		D = Y[i]
		dd.append(D)
		I +=1

plt.plot(aa, bb,'.g',cc,dd,'.r') 
plt.grid('on')
plt.axis('equal')
plt.savefig('cerclepoint.png')

#d)
S = pi*1 

t0 = clock()
A  = abs(I*4/N - S)
t1 = clock()
t2 = t1 - t0
H = abs(A-S)
print('Temp de calcul\n')
print(t2)
print('Nombre de point interieur\n')
print(I)
print('Nombre de point Exterieur\n')
print(E)
print ('Surface \n')
print(A)
print('Erreur comise\n')
print(H)



#e)
#voir tp2.py

#f)
n = "n"
d = "erreur"
t = "temps (sec.)"

print('Monte carlo\n')
print('{0:10}| {1:10}      | {2:10}'.format(n,d,t))

x = "----------------------------------------------"
print( x)

for i in range(1, 6):
	t6 = clock()
	p = monte_carlo(10**i)
	t7 = clock()
	V = abs(p-pi)
	t8 = t7-t6

	print('{0:10}|{1:10}|{2:10}'.format(10**i,V,t8))

#g)
print('\n')
print('Monte carlo 2\n')


x = "----------------------------------------------"
print('{0:10}| {1:10}      | {2:10}'.format(n,d,t))
print( x)

for i in range(1, 6):
	t6 = clock()
	p = monte_carlo2(10**i)
	t7 = clock()
	V = abs(p-((4*pi)/3))
	t8 = t7-t6

	print('{0:10}|{1:10}|{2:10}'.format(10**i,V,t8))
 
		

