####### TP2
# 1-a)
from methods import *
import numpy as np
from math import *

I= pi/6 + sqrt(3)/4

def f(x):
	from math import sqrt
	return sqrt(1-x**2)
	
import matplotlib.pyplot as plt
import time

x, dx = -0.5, 0.1
X, Y, Points = [], [], [] 
while x <= 0.5:
    y = f(x)
    point = (x, y) 
    
    X.append(x) 
    Y.append(y) 
    Points.append(point)
    x += dx

"""
plt.plot(X, Y, 'y')
plt.grid()
#plt.show()
plt.savefig('figure2.png')
"""
#1-b) Voir figure

#2- METHODE DU POINT MILIEU
#2-a) Voir feuille annexe
#2-f) 

def point_milieu(f, a, b, n):
	s=0
	s4= 0.95
	temps = time.clock()
	for i in range(0,n):
		x1 = a + (b-a)*i/float(n)
		x2 = a + (b-a)*(i+1)/float(n)
		s+= f((x1+x2)/2.0)*(x2-x1)

	return s, time.clock()-temps

a = -0.5
b = 0.5

for i in range (1, 7):
	n = 10
	p_f = point_milieu(f, a, b, n**i)
	print('\n')
	print('{0}eme test point milieu = {1} '.format(i,p_f))

a = -0.5
b = 0.5

n1 = 10
n2 = 100
n3 = 1000
n4 = 10000
n5 = 100000
n6 = 1000000

print('\n')

def enregistrer(methode, func, string, a, b, n):
	with open ('tableau {:s}.txt' .format(string), 'w') as fichier :
		print('{0:12s} | {1:9s} | {2:s}'.format(' Erreur', 'Temps(sec)', 'n'))
		fichier.write ('{0:15s}|{1:12s}|{2:s}\n' .format( 'Erreur','Temps(sec)','n'))
		for j in range(1, n+1):
				integrale,Temps = methode(func, a, b, 10**j)
				Erreur = abs(integrale - I)
				print('{0:e} | {1:e} | {2:d}'.format(Erreur, Temps, 10**j))
				fichier.write('{0:.9e} | {1:e} | {2:d}\n'.format(Erreur, Temps, 10**j))
	print('')

enregistrer(point_milieu, f, 'point_milieu', -0.5, 0.5, 6)





"""
#1er test
p_f = point_milieu(f, a, b, n1)
print ('1er test = {0} '.format(p_f))

print('\n')
#2e test
p_f = point_milieu(f, a, b, n2)
print ('2e test = {0} '.format(p_f))

print('\n')
#3e test
p_f = point_milieu(f, a, b, n3)
print ('3e test = {0} '.format(p_f))

print('\n')
#4e test
p_f = point_milieu(f, a, b, n4)
print ('4e test = {0} '.format(p_f))

print('\n')
#5e test
p_f = point_milieu(f, a, b, n5)
print ('5e test = {0} '.format(p_f))

print('\n')
#6e test
p_f = point_milieu(f, a, b, n6)
print ('6e test = {0} '.format(p_f))
"""




#3) METHODE DES TRAPEZES


def trapezes(f, a, b, n) :
	t = time.clock()
    	h = abs(b - a)/n
    	s = 0
    	for i in range(n):
        	s = s + h * (f(a + i*h) + f( a + (i+1)*h))/2
    	return s, time.clock()-t


print('\n')
for i in range (1, 7):
	n = 10
	t= trapezes(f, a, b, n**i)
	print('\n')
	print('{0}eme test trapezes = {1} '.format(i,t))

enregistrer(trapezes, f, 'trapezes', -0.5, 0.5, 6)

print('\n')

#4) METHODE DE SIMPSON
"""
def simpson(f, a, b, n): 
    
    S = 0 
    for i in range(0, n): 
        x1 = a + (b - a) * i / float(n) 
        x2 = a + (b - a) * (i + 1) / float(n) 
        S += (f(x1) + 4 * f((x1 + x2) / 2.0) + f(x2)) * (x2 - x1) / 6.0 
    return S 



for i in range (1, 7):
	n = 10
	simp= simpson(f, a, b, n**i)
	print('\n')
	print('{0}eme test simpson = {1} '.format(i,simp))

enregistrer(simpson, f, 'simpson', -0.5, 0.5, 6)
"""

"""
theta = np.linspace(0, 2*np.pi, 100)
Xcercle = np.cos(theta)
Ycercle = np.sin(theta)
plt.plot(Xcercle, Ycercle)
plt.axis("equal")
#plt.show()
plt.savefig('cercle.png')
"""
#6-b) 

print('\n')
import numpy.random as npr
print('Quelquesvaleurs aleatoires entre 0 et 1:')
print (npr.rand(10))

print('\n')
print('Quelques valeurs aleatoires entre -1 et 1:')
print(npr.uniform(-1, 1, 10))

#6-c)
"""
for i in range(100):
	xpoint = 2*np.random.rand()-1
	ypoint = 2*np.random.rand()-1
	if (xpoint**2+ypoint**2)<1:
		plt.scatter(xpoint, ypoint, color='red', marker='.')
	else:
		plt.scatter(xpoint, ypoint, color='green', marker='.')

plt.xlim(-1.25, 1.25)
plt.ylim(-1.25, 1.25)
plt.savefig('cercle1.png')
"""
"""
def montecarlo(N):
	t=time.clock()
	cmpt=0
	for i in range(N):
		xpoint = 2*np.random.rand()-1
		ypoint = 2*np.random.rand()-1
		if (xpoint**2+ypoint**2)<1:
			cmpt = cmpt + 1
			plt.scatter(xpoint, ypoint, color='red', marker='.')
	S = (cmpt /float(N)*4)
	return S, time.clock()-t

m_c, cmpt = montecarlo(10000)
print('2er test montecarlo = {0} et le temps {1}'.format(m_c, cmpt))
"""




