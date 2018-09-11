#ENGUIX Precillia
#RAJA GANAPATHY Srinivas

#FONCTIONS
from math import sqrt
from math import pi
from time import clock
from module import *

#EXERCICE 2

#2A.

#Rendu papier

#2B.

x0 = -0.5
xx = [x0]
for i in range (5):
        x1 = x0 + 0.25
        xx.append(x1)
        x0 = x1
        
print(x0)
print(xx)
print('\n')


cc = [] #creation d'une nouvelle liste vide
for i in range (5):
        c = (xx[i] + xx[i+1])/2
        cc.append(c)
        



print('\n')

#2C.

ss = []
for i in range(4) :
        s = 0.25*f(cc[i+1])
        ss.append(s)
print(ss)   
print('\n')

t0 = clock ()


S = ss[0] + ss[1]  + ss[2] + ss[3]  
print('Somme de la surface') 
print(S) 

t1 = clock ()

I = (sqrt(3)/4) + (pi/6)
print('\n')

A = abs(S-I)
print('Erreur commise : ')
print(A)
print('\n')

#2D.

t2 = t1 - t0
print('Le temps de calcul de l integrale est :')
print(t2)
print('\n')

#2F.
print('Test 1') 
a = -0.5
b = 0.5
n = 100
r = point_milieu(f, a, b, n)
print('Methode du point milieu')
print(r)
print('\n')

#2G.
I = sqrt(3.0)/4 + (pi/6)

n = "n"
d = "erreur"
t = "temps (sec.)"

with open ("table.txt", 'w') as tab:
	entete = '{0:10} | {1:13} | {2:10}\n'.format(n,d,t)
	print(entete)
	tab.write(entete)
	print(40*'-'+'\n')
	tab.write(40*'-'+'\n')
	for i in range(6):
		n = 10**(i+1)
		t0 = clock()
		S = point_milieu(f, -0.5, 0.5, n)
		t1 = clock()
		r = abs(S-I)
		t2 = t1 - t0
		ligne = '{0:10} | {1:13g} | {2:10g}\n'.format(n, r, t2)
		print(ligne)
		tab.write(ligne)


