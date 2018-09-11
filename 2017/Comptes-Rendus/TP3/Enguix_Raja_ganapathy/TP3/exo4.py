from module import *
import matplotlib.pyplot as plt

#A.
#Voir la fonction f dans module.py

#B.
u0 = 1.0
T = 2.0
n = 10
p = euler(f, u0, T, n)
print('Test Euler\n')
print(p)

#C.
u0 = 1.0
T = 2.0
n = 10
p = euler(f1, u0, T, n)
print('Test 1\n')
print(p)

u0 = 1.0
T = 2.0
n = 10
p = euler(f2, u0, T, n)
print('Test 2\n')
print(p)

u0 = 1.0
T = 2.0
n = 10
p = euler(f3, u0, T, n)
print('Test 3\n')
print(p)

