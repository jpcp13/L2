
import numpy as np
import matplotlib.pyplot as plt
import time
import math

# exo 2
def f(x):
	return math.sqrt(1-x**2)

x0=-0.5
x1=-0.25
x2=0
x3=0.25
x4=0.5


S1= f((x0+x1)/2)*0.25
S2= f((x2+x1)/2)*0.25
S3= f((x2+x3)/2)*0.25
S4= f((x3+x4)/2)*0.25
Sk= S1+S2+S3+S4
print('Sk=', Sk)

#erreur commise

I=((math.pi)/6)+(math.sqrt(3)/4) #calculer a la main
erreur_commise= abs(Sk-I)
print('erreur_commise=', erreur_commise)
n = 10**4
a = 0

t = time.clock()
for i in range(n):
	a = a + 1.57

print('a =', a)
temps_ecoule = time.clock() - t
print('temps en secondes = {0}'.format(temps_ecoule))

def point_milieu1(f, a, b, n):
	I=(math.pi/6)+(math.sqrt(3)/4)
	S=0
	x1=a
	d=(b-a)/n
	x2=a+d
	
	for i in range(n):
		c=(x1+x2)/2
		s=d*f(c)
		S=S+s
		x1=x1+d
		x2=x2+d
	return S

def point_milieu(f, a, b, n):
	I=(math.pi/6)+(math.sqrt(3)/4)
	S=0
	x1=a
	d=(b-a)/n
	x2=a+d
	start = time.clock()

	for i in range(n):
		c=(x1+x2)/2
		s=d*f(c)
		S=S+s
		x1=x1+d
		x2=x2+d
	
	tps_ecoule = (time.clock() - start)
	#~ print('integrale =', S,'erreur_commise =',abs(S-I),'temps_ecoule =', tps_ecoule.format(x, y, z))
	print('integrale = {0:.5f}, erreur_commise = {1:.2g}, temps_ecoule = {2:.2g}'.format(S, abs(S-I), tps_ecoule))
	return S

for k in range(1,7):
	print(10**k, point_milieu(f,-0.5, 0.5, 10**k))

def p(x,n):
	if n>0:
		return x*p(x,n-1)
	else:
		return 1

def erreur(x):
	return abs(x-0.96)

print('      n     erreur       temps')
print('------------------------------')
for i in range (1,7):
    x = p(10,i)
    t1 = time.clock()
    y = abs(point_milieu1(f,-0.5,0.5,10**i)-I)
    t2 = t1 - time.clock()
    #~ s = repr(x) + '\t' + repr(y) + '\t'+ repr(t2) + '\n'
    print('{0:>7d}  {1:>.3e}  {2:>.3e}'.format(x, y, t2))
    #~ print(s)

