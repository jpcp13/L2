#Exercice 4

from tp3 import *
import matplotlib.pyplot as plt

#a)

#voir tp3.py

#b)

u0 = 1.0
T = 2.0
n = 10
p = euler(f, u0, T, n)
print('Test Euler\n')
print(p)

#c)


u0 = 1.0
T = 2.0
n = 10
p = euler(f1, u0, T, n)
print('Test premiere ED0\n')
print(p)


u0 = 1.0
T = 2.0
n = 10
p = euler(f2, u0, T, n)
print('Test deuxieme EDO\n')
print(p)


u0 = 1.0
T = 2.0
n = 10
p = euler(f3, u0, T, n)
print('Test troisieme EDO\n')
print(p)
