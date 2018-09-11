
#ENGUIX Precillia
#RAJA GANAPATHY Srinivas

#FONCTIONS
from math import sqrt
from math import pi
from time import clock
from module import *


print('Methode de Simpson')
a = -0.5
b = 0.5
n = 10
x1 = simpson(f, a, b, n)
print(x1)

print('Methode de Simpson')
a = -0.5
b = 0.5
n = 100
x2 = simpson(f, a, b, n)
print(x2)

print('Methode de Simpson')
a = -0.5
b = 0.5
n = 1000
x3 = simpson(f, a, b, n)
print(x3)

print('Methode de Simpson')
a = -0.5
b = 0.5
n = 10000
x4 = simpson(f, a, b, n)
print(x4)

print('Methode de Simpson')
a = -0.5
b = 0.5
n = 100000
x5 = simpson(f, a, b, n)
print(x5)

print('Methode de Simpson')
a = -0.5
b = 0.5
n = 1000000
x6 = simpson(f, a, b, n)
print(x6)

I = sqrt(3.0)/4 + (pi/6)

n = "n"
d = "erreur"
t = "temps (sec.)"

with open ("table3.txt", 'w') as tab:
	entete = '{0:10} | {1:13} | {2:10}\n'.format(n,d,t)
	print(entete)
	tab.write(entete)
	print(40*'-'+'\n')
	tab.write(40*'-'+'\n')
	for i in range(6):
		n = 10**(i+1)
		t0 = clock()
		S = simpson(f, -0.5, 0.5, n)
		t1 = clock()
		r = abs(S-I)
		t2 = t1 - t0
		ligne = '{0:10} | {1:13g} | {2:10g}\n'.format(n, r, t2)
		print(ligne)
		tab.write(ligne)
