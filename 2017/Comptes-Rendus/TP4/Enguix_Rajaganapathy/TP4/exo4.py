from module import *

#A.
print("Decomposition en facteurs premiers de 4864")
a = factors(4864)
print(a)
print('\n')

print("Decomposition en facteurs premiers de 3458")
b = factors(3458)
print(b)
print('\n')

print("Coefficient de Bezout pour a = 4864 et b = 3458")
y = euclide(4864,3458)
print(y)
