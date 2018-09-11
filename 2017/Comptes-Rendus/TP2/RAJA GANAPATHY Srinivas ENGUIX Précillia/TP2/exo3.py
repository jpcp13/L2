#ENGUIX Precillia
#RAJA GANAPATHY Srinivas

#FONCTIONS
from math import sqrt
from math import pi
from time import clock
from module import *


print('Methode du trapeze')
a = -0.5
b = 0.5
n = 10
s= trapeze(f, a, b, n)
print(s)

I = sqrt(3.0)/4 + (pi/6)

n = "n"
d = "erreur"
t = "temps (sec.)"

with open ("table2.txt", 'w') as tab:
	entete = '{0:10} | {1:13} | {2:10}\n'.format(n,d,t)
	print(entete)
	tab.write(entete)
	print(40*'-'+'\n')
	tab.write(40*'-'+'\n')
	for i in range(6):
		n = 10**(i+1)
		t0 = clock()
		S = trapeze(f, -0.5, 0.5, n)
		t1 = clock()
		r = abs(S-I)
		t2 = t1 - t0
		ligne = '{0:10} | {1:13g} | {2:10g}\n'.format(n, r, t2)
		print(ligne)
		tab.write(ligne)
