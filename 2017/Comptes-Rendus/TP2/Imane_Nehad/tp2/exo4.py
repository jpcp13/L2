from math import *
from time import *
from methodes import *

I = pi/6 + sqrt(3)/4

def f(x) :
	return sqrt(1-x**2)

n = 10
a = -0.5
b = 0.5


D, erreur, temps = simpson(f, a, b, n)

print('Avec la methode de Simpson, l integrale a ete calcule en {0} secondes avec une erreur commise de {1}'.format(temps,erreur))
