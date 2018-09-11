from math import *
from time import *

I = pi/6 + sqrt(3)/4

def f(x) :
	return sqrt(1-x**2)

def trapeze(f,a,b,n) :
	k  = clock()
	h=(b-a)/float(n)
	t=0.5*(f(a)+f(b))
	for i in range(1,n) :
		t=t+f(a+i*h)
	S = h*t
	e = abs(I-S)
	temps = clock() - k
	return temps, S, e

# le temps de calcul de l'integrale
T = []
G = []
Q = []
AUX = []
n=1000000
aux = 10
while aux <= n:
	q, r, g = trapeze(f,-0.5,0.5,aux)
	T.append(aux)
    	G.append(g)
    	Q.append(q)
	AUX.append(aux)
    	aux = aux*10

print('{0:10s}|{1:10s}|{2:10s}'.format('n','erreur','temps'))
print('--------------------------------')

for x in T:

    temps, S, erreur = trapeze(f,-0.5,0.5,x)
    print('{0:10d}|{1:g}|{2:g}'.format(x, erreur, temps))

