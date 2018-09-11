from math import *
from time import *
from methodes import *

I = pi/6 + sqrt(3)/4

def f(x) :
	return sqrt(1-x**2)

n = 10
a = -0.5
b = 0.5

e_1, t_1 = trapeze(f, a, b, n)

print('Avec la methode du trapeze, l integrale a ete calcule en {0} avec une erreur commise de {1}'.format(t_1,e_1))

