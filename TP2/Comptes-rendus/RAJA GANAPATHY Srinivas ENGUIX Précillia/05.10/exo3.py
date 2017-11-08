#ENGUIX Precillia
#RAJA GANAPATHY Srinivas

#FONCTIONS
from math import sqrt
from math import pi
from time import clock
from exo1 import f
def trapeze(f, a, b, n):
	h = (b - a) / n
	S = 0
	for i in range(n):
		s=(f(a+(i*h)-h)+f(a+(i*h)))*h/2
		S+=s
	return S

I = sqrt(3.0)/4 + (pi/6)
print('Methode du trapeze')
a = -0.5
b = 0.5
n = 100000
S = trapeze(f, a, b, n)
print(S-I)
