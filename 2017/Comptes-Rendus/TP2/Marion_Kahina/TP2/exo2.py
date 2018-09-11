from math import *
from time import *

I = pi/6 + sqrt(3)/4

def f(x) :
	return sqrt(1-x**2)

def pm(f,a,b,n) :
	k  = clock()
	Sub = []
	M = []
	Haut = []
	h = (b-a)/n
	So=0.0

	# les subdivisions regulieres

	for i in range(n+1):

		sub= a + h*i
		Sub.append(sub)

	# les milieux

	for i in range(n):

		m = (Sub[i] + Sub[i+1])/2
		M.append(m)

	# les images des milieux

	for i in M:
		haut=f(i)
		Haut.append(haut)

	# l'integrale

	for i in Haut:
		somme = h*i
		So=So+somme

	e = abs(I-So)
	temps = clock() - k
	return temps, So, e


# le temps de calcul de l'integrale
T = []
G = []
Q = []
AUX = []
n=1000000
aux = 10
while aux <= n:
	q, r, g = pm(f,-0.5,0.5,aux)
	T.append(aux)
    	G.append(g)
    	Q.append(q)
	AUX.append(aux)
    	aux = aux*10

print('{0:10s}|{1:10s}|{2:10s}'.format('n','erreur','temps'))
print('--------------------------------')

for x in T:

    temps, S, erreur = pm(f,-0.5,0.5,x)
    print('{0:10d}|{1:g}|{2:g}'.format(x, erreur, temps))
	

