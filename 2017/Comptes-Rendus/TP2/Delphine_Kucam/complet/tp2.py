import numpy as np
import matplotlib.pyplot as plt
import time
import math

def f(x):
	return sqrt(1-x**2)


x = linspace(-0.5, 0.5, 10)
plot(x, f(x))
grid()
show()


#exo2
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

I=((math.pi)/6)+(sqrt(3)/4) #calculer a la main
erreur_commise= abs(Sk-I)

n = 10**6
a = 0

t = time.clock()
for i in range(n):
	a = a + 1.57

print('a =', a)
temps_ecoule = time.clock() - t
print('temps en secondes = {0}'.format(temps_ecoule))


#a<b
#def point_milieu(f,a,b,n):
#	base=(b-a)*n
#	for i in range ():
#		f(a+i(b-a)/n)

