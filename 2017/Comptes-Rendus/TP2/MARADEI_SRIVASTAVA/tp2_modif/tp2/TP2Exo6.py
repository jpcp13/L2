from math import *
from time import *
from string import *
from pylab import *
from random import *
from fonctions import *

def Monte_carlo(N):
	I = 0
	for i in range (N):
		x = uniform(-1,1)
		y = uniform(-1,1)
		if x*x + y*y <= 1:
			I += 1
	Suruthy = float(I)/N
	return Suruthy

X,Y = [],[]
V,W = [],[]
I = 0 # compteur pour les points rouges
E = 0 # compteur pour les points verts

for i in range(1000):
	x = uniform(-1,1)
	y = uniform(-1,1)
	if x*x + y*y <= 1:
		X.append(x)
		Y.append(y)
		I += 1
	else:
		V.append(x)
		W.append(y)
		E += 1 

theta = linspace(0, 2*pi, 40)
x = cos(theta)
y = sin(theta)
plot(x, y)
plot(X, Y, 'ro', linewidth = 2)
plot(V, W, 'go', linewidth = 1)
axis("equal")
grid()
show()
title("Modelisation de la fonction Monte_Carlo")

t1 = clock()
test = Monte_carlo(150)
t2 = clock() - t1
print t2
print test

with open('table6.txt', 'w') as tab:
	Z = '\t\tTableau correspondant a la fonction Monte_Carlo\n\n'
	tableau = Z+'N\t|\tErreur\t\t|\tTemps (sec.)\t\n'+ 68*'_'+'\n'
	print tableau
	tab.write(tableau)
	#print ('____________________________________________________________________\n')
	for i in range (1,7):
		x = p(10,i)
		t1 = clock()
		w = Monte_carlo(x)
		t2 = clock() - t1
		y = abs(w - 3.14/4)
		#espace = '\t' + '|' + '\t'
		s = repr(x) + '\t' + '|' + '\t' + '%.9f' % y + '\t|' + '\t' + '%.9f' % t2 + '\n'
		#ligne = "{0:7d} \t | \t {1:g} \t | \t {2:g}".format(x, y, t2)
		print(s)
		tab.write(s)




























