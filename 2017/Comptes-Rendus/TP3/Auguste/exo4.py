import numpy as np
from tp3 import *
#Exercice4 

#a)
def u(t):
	return np.exp(-t)

def f(t,u):
	return -u


#b)
u0 = 1.0
T = 2.0
n = 10
p = euler(f, u0, T, n)
print('Test Euler\n')
print(p)




#c)
#Test 1
u0 = 1.0
T = 2.0
n = 10
p = euler(f1, u0, T, n)
print('Test premiere ED0\n')
print(p)

#Test 2
u0 = 1.0
T = 2.0
n = 10
p = euler(f2, u0, T, n)
print('Test deuxieme EDO\n')
print(p)

#Test 3
u0 = 1.0
T = 2.0
n = 10
p = euler(f3, u0, T, n)
print('Test troisieme EDO\n')
print(p)



