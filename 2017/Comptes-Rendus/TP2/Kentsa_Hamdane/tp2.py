#KENTSA MELI Edgar
#HAMDANE Amine
from math import *
import matplotlib.pyplot as plt
from time import *
from fonctiontp2 import *
from numpy import *
#Execice 1
#a/

def f(x):
	y = sqrt(1 - x**2)
	return y

#b/

t = linspace(-0.5, 0.5, 100)
plt.plot(t, f(t), 'r-')
plt.grid('on')
plt.axis('equal')
plt.savefig('Graphique de f')

a = -0.5
b = 0.5
n = 4
s = point_milieu(f, a, b, n)

#f

I = sqrt(3.0)/4 + pi/6

print('Tableau avec la methode du rectangle:')
print('n         | erreur        |  temps (sec.) ')
print('--------------------------------------------')
for i in range(1, 7):
	n = 10**i
	start = clock()
	S = point_milieu(f, a, b, n) 
	stop = clock()
	J = abs(S - I)
	# stop et start encadrent mon point milieu
	tps = stop - start
	print('{0:10g}| {1:10g}    | {2:10g}'.format(n, J, tps))
	i = i + 1


#g
entete1 = 'Tableau avec la methode du rectangle:'
entete2 = 'n         | erreur        |  temps (sec.) '
tirets = '-'*40

with open ('tableau','w') as fichier:
	fichier.write(entete1+'\n')
	fichier.write(entete2+'\n')
	fichier.write('------------------------------------------------------------'+'\n')
	for i in range(1, 7):
		n = 10**i
		start = clock()
		S = point_milieu(f, a, b, n) 
		stop = clock()
		J = abs(S - I)
		tps = stop - start
		ligne = '{0:10g}| {1:10g}    | {2:10g}'.format(n, J, tps)
		fichier.write(ligne+'\n')
		i = i + 1

# exo 3

print('Tableau avec la methode du trapeze:')
print('n         | erreur        |  temps (sec.) ')
print('--------------------------------------------')
for i in range(1, 7):
	n = 10**i
	start = clock()
	S = point_trapeze(f, a, b, n) 
	stop = clock()
	J = abs(S - I)
	tps = stop - start
	print('{0:10g}| {1:15g}| {2:g}'.format(n, J, tps))
	i = i + 1
entete1 = 'Tableau avec la methode du trapeze:'
entete2 = 'n         | erreur        |  temps (sec.) '


with open ('tableau2','w') as fichier:
	fichier.write(entete1+'\n')
	fichier.write(entete2+'\n')
	fichier.write('------------------------------------------------------------'+'\n')
	for i in range(1, 7):
		n = 10**i
		start = clock()
		S = point_trapeze(f, a, b, n) 
		stop = clock()
		J = abs(S - I)
		tps = stop - start
		ligne = '{0:10g}| {1:10g}    | {2:10g}'.format(n, J, tps)
		fichier.write(ligne+'\n')
		i = i + 1
#exo 4

print('Tableau avec la methode simpson:')
print('n         | erreur        |  temps (sec.) ')
print('--------------------------------------------')
for i in range(1, 7):
	n = 10**i
	start = clock()
	S = point_simpson(f, a, b, n) 
	stop = clock()
	J = abs(S - I)
	tps = stop - start
	print('{0:10g}| {1:10g}    | {2:10g}'.format(n, J, tps))
	i = i + 1
entete1 = 'Tableau avec la methode simpson:'
entete2 = 'n         | erreur        |  temps (sec.) '

with open ('tableau3','w') as fichier:
	fichier.write(entete1+'\n')
	fichier.write(entete2+'\n')
	fichier.write('------------------------------------------------------------'+'\n')
	for i in range(1, 7):
		n = 10**i
		start = clock()
		S = point_simpson(f, a, b, n) 
		stop = clock()
		J = abs(S - I)
		tps = stop - start
		ligne = '{0:10g}| {1:10g}    | {2:10g}'.format(n, J, tps)
		fichier.write(ligne+'\n')
		i = i + 1


#exo 6
#a

from numpy import *
t = linspace(-pi, pi, 100)

x = cos(t)
y = sin(t)

plt.plot(x,y)
plt.grid('on')
plt.axis('equal')


#b
for i in range(10):
	xpoint = 2*random.rand()-1
	ypoint = 2*random.rand()-1
	if (xpoint**2+ypoint**2)<1:
		plt.scatter(xpoint,ypoint, color='blue', marker='.')
	else:
		plt.scatter(xpoint,ypoint, color='pink', marker='.')
plt.savefig('Cercle monte_carlo')

#c
for i in range(1000):
	xpoint = 2*random.rand()-1
	ypoint = 2*random.rand()-1
	if (xpoint**2+ypoint**2)<1:
		plt.scatter(xpoint,ypoint, color='red', marker='.')
	else:
		plt.scatter(xpoint,ypoint, color='green', marker='.')
plt.savefig('Cercle monte_carlo')

print('Tableau avec la methode monte_carlo:')
print('n         | erreur        |  temps (sec.) ')
print('--------------------------------------------')
for i in range(1, 8):
	N = 10**i
	start = clock()
	S = monte_carlo(N)
	stop = clock()
	J = abs(S - pi)
	tps = stop - start
	print('{0:10g}| {1:20g}    | {2:10g}'.format(N, J, tps))
	i = i + 1

entete1 = 'Tableau avec la methode monte_carlo:'
entete2 = 'N         | erreur               |  temps (sec.) '
with open ('tableau4','w') as fichier:
	fichier.write(entete1+'\n')
	fichier.write(entete2+'\n')
	fichier.write('----------------------------------------------------------------'+'\n')
	for i in range(1, 7):
		N = 10**i
		start = clock()
		S = monte_carlo(N)
		stop = clock()
		J = abs(S - pi)
		tps = stop - start
		ligne = '{0:10g}{1:20g}| {2:10g}'.format(N, J, tps)
		fichier.write(ligne+'\n')
		i = i + 1

#g

L = 0
M = 0
XA, YA, ZA = [] ,[], []
XB, YB, ZB = [] ,[], []
for i in range(0,N):
	x = random.uniform(-1,1)
	y = random.uniform(-1,1)
	z = random.uniform(-1,1)	
	if(x**2 + y**2 + z**2 <= 1):
		XA.append(x)
		YA.append(y)
		ZA.append(z)
		L = L + 1
	else:
		XB.append(x)
		YB.append(y)
		ZB.append(z)
		M = M + 1

