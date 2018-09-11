import math
import numpy as np

# Des modifications ont ete apporte par rapport au programme imprime pour plus de lisibilite

#Definitions de fonction 

# Bessel-Integrale
def bessel(x,cst,z) :
	sinus = cst*(x) - z*math.sin(x)	
	return math.cos(sinus)/math.pi

#Simpson: permet de calculer l'integrale de Bessel
def simpson(f,a,b,n,cst,z):
	S=0
	w=(b-a)/n
	x1=a
	x2 = a+w
        import time as time
	start = time.clock()

	for i in range(n):
		s = w*(f(x1,cst,z) + 4*f((x1+x2)/2,cst,z) + f(x2,cst,z))
		S = S+s
		x1=x2
		x2 = x2+w
        elapsed = (time.clock()-start)
        return S, elapsed


#Bessel-Somme pour n entier naturel
def bessel2(x,n):
	Somme = 0
	j = 10
	for p in range(j):
		denom = math.factorial(p)*math.factorial(n+p)
		coeff = (x/2)**(2*p+n)
		Somme = Somme + (-1)**p/denom * coeff
	return Somme

# Tests des fonctions
print "Calcul de l'integrale de Bessel a l'aide de la methode de Simpson \n"
n = 10
cst = 5
z = 2
for i in range(6):
	print "Test entre 0 et infini pour n =",n
	d, t = simpson(bessel,0,math.pi,n,cst,z)
	print "valeur de l'integrale:" 	       ,d,"\n","Temps:",t,"\n"
	n = n * 10
n = 10
print "Test somme de Bessel pour x=",z,"et n =",n,":",bessel2(z,n)



