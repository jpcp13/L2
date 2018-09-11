# 11502702 SABABADY Kamala 
# 11502168 SELVARAJAH Dinusan 
#*********************************************************
import math
import numpy as np
import matplotlib.pyplot as plt
import time
from fonction import *

# On trace le cercle d'unite. 
theta = np.linspace(0, 2*np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)
plt.plot(x, y)
plt.axis("equal")
plt.grid()
plt.savefig('cercle.png')

#On genere quelques valeurs aleatoires suivant la distribution de loi uniforme sur [0,1] et [-1,1].
s = np.random.uniform(0,1,10)
print('Quelques valeurs aleatoire x:')
print(s)
print('\n')
r = np.random.uniform(-1,1,10)
print('Quelques valeurs aleatoire y:')
print(r)
print('\n')

#On genere N points suivant la distribution uniforme sur le carre [-1,1] et on fait l'apparaitre sur le graphique.
N=1000
X = np.random.uniform(-1,1,N)
Y = np.random.uniform(-1,1,N)
ss,vv,dd,tt =[] ,[],[] ,[]
I=0
E=0
for i in range(N):
		
		if (X[i]**2+Y[i]**2)<1: #les points interieurs au disque unite 
			S=X[i]
			ss.append(S)
			V=Y[i]
			vv.append(V)
			I+=1
		else: # les points exterieurs au disque.
			D=X[i]
			dd.append(D)
			T=Y[i]
			tt.append(T)
			E+=1
		
plt.plot(ss, vv,'.r', dd, tt,'.g')
plt.axis("equal")
plt.grid()
plt.savefig('rougevert.png')

S=math.pi
t0=time.clock()
M=((I*4.0)/N)
K=abs(M-S)
t1=time.clock()
t2=t1-t0


print('Le nombre de points a interieurs du disque:')
print 'I=', I
print('Le nombre de points a exterieur du disque:')
print 'E=', E 
print('\n')
print('La surface S:')
print(S)
print('\n')
print('L\'approximation de la surface S')
print(M)
print('\n')
print('erreur commise:')
print(K)
print('\n')
print('le temps du calcul:')
print(t2)
print('\n')

# afficher dans le terminal
print('Test de Monte_Carlo avec N=10^k, k variant 1 a 6:')
print('\n')
n="n"
d="erreur"
u="temps (sec.)"
print('{0:10} | {1:17} | {2:10}'.format(n,d,u))
t="---------------------------------------------"
print(t)
for i in range(1,7):

    t5=time.clock()
    p= monte_carlo(10**(i))
    t6=time.clock()
    k=math.pi
    S=abs(p-k)
    y=t6-t5
    print('{0:10} | {1:17} | {2:10}'.format(10**(i),S,y))
print('\n')

print('Test de Monte_Carlo_2 avec N=10^k, k variant 1 a 6:')
print('\n')
print('{0:10} | {1:17} | {2:10}'.format(n,d,u))
print(t)
for i in range(1,7):
    t5=time.clock()
    p= monte_carlo_2(10**(i))
    t6=time.clock()
    k=(4/3)*math.pi
    S=abs(p-k)
    y=t6-t5
    print('{0:10} | {1:13} | {2:10}'.format(10**(i),S,y))

#enrengistrer dans un fichier 
titre = 'METHODE DE MONTE CARLO'
entete = '{0:15s}|{1:15s}|{2:15s}'. format('n','erreur','temps')
tirets = '-'*42
with open('montecarlo.txt','w') as fichier:
    fichier.write(titre +'\n')
    fichier.write('\n')
    fichier.write(entete+'\n')
    fichier.write(tirets+'\n')
    for i in range (1,7):
	t5=time.clock()
    	p= monte_carlo(10**(i))
   	t6=time.clock()
    	k=math.pi
    	S=abs(p-k)
    	y=t6-t5
        ligne = '{0:15d}|{1:15g}|{2:15g}'. format(10**(i), S, y)
        fichier.write(ligne+'\n')
	fichier.write('\n')
	

#enrengistre dans le meme fichier
titre = 'METHODE DE MONTE CARLO 2'
entete = '{0:15s}|{1:15s}|{2:15s}'. format('n','erreur','temps')
tirets = '-'*42

with open('montecarlo.txt','a') as fichier:
    fichier.write(titre +'\n')
    fichier.write('\n')
    fichier.write(entete+'\n')
    fichier.write(tirets+'\n')
    for i in range (1,7):
	t5=time.clock()
    	p= monte_carlo_2(10**(i))
   	t6=time.clock()
    	k=(4/3)*math.pi
    	S=abs(p-k)
    	y=t6-t5
        ligne = '{0:15d}|{1:15g}|{2:15g}'. format(10**(i), S, y)
        fichier.write(ligne+'\n')
	fichier.write('\n')

