# 11502702 SABABADY Kamala 
# 11502168 SELVARAJAH Dinusan 

#*********************************************************
from fonction import *

import time

def f(x):
	from math import sqrt
	return sqrt(1-x**2)


#Partie2

x0=-0.5
xx=[x0] # Ceci enregistre les points xi de la subdivision dans une liste
#On calcule la longueur 
for i in range(4):
	x1= x0 + 0.25
	xx.append(x1)
	x0=x1

cc = [] # Ceci enregistre les milieux de ces sous intervalles dans une liste
#On calcule la largeur 
for i in range(4):
	c=(xx[i]+xx[i+1])/2
	cc.append(c)

t0=time.clock()
#On calcul la surface:
ss=[]
for i in range(4):

	s = (xx[i+1]-xx[i])*f(cc[i])
	ss.append(s)
#On calcule la somme des surface(on calcule l'integrale)
S=0
for i in range (4):
	S+=ss[i]
# S est l'approximation de I	
t1=time.clock()

print('Les points:')
print(xx)   
print('\n')

print('Les milieux :')
print(cc)
print('\n')

print('La somme de la surface :')
print(S)
print('\n')

print("Le temps de calcul est:")
t=t1-t0
print(t)
print('\n')


print('L\'integrale I:')
import math
from math import sqrt
I= math.pi/6 + sqrt(3)/4
print(I)
print('\n')

r=abs(s-I)
print('L\'erreur commise:')
print(r)
print('\n')



n="n"
d="erreur"
t="temps (sec.)"

print('{0:10} | {1:17} | {2:10}'.format(n,d,t))
t="---------------------------------------------"
print(t)
for i in range(1,7):
    t5=time.clock()
    p= point_milieu(f,-0.5,0.5,10**(i))
    t6=time.clock()
    r=abs(p-I)
    y=t6-t5
    print('{0:10} | {1:15} | {2:15}'.format(10**(i),r,y))


titre = 'METHODE DU POINT MILIEU:'
entete = '{0:15s}|{1:15s}|{2:15s}'. format('n','erreur','temps')
tirets = '-'*42

with open('point_milieu.txt','w') as fichier:
    fichier.write(titre +'\n')
    fichier.write('\n')
    fichier.write(entete+'\n')
    fichier.write(tirets+'\n')
    for i in range (1,7):
        t5=time.clock()
        p = point_milieu(f,-0.5,0.5,10**(i))
        t6=time.clock()
        r=abs(p-I)
        y=t6-t5
        ligne = '{0:15d}|{1:15g}|{2:15g}'. format(10**(i), r, y)
        fichier.write(ligne+'\n')
    fichier.write('\n')
    

