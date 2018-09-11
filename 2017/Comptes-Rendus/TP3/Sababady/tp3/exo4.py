#SABABADY Kamala
#SELVARAJAH Dinusan

from tp3 import *

#b) Test de la fonction Euler 
u0 = 1.0
U0 = np.array([u0])
T = 2.0
n = 10
p = euler(f, U0 ,T,n)
print('Test Euler\n')
print(p[0])
print('\n')
print(p[1])
print('\n')

#c) Test de la premiere fonction
u0 = 1.0
U0 = np.array([u0])
T = 2.0
n = 10
p = euler(f1, U0 ,T,n)
print('Test EDO1\n')
print(p[0])
print('\n')
print(p[1])
print('\n')

#Test de la deuxieme fonction
u0 = 1.0
U0 = np.array([u0])
T = 2.0
n = 10
p = euler(f2, U0 ,T,n)
print('Test EDO2\n')
print(p[0])
print('\n')
print(p[1])
print('\n')

#Test de la troisieme fonction
u0 = 1.0
U0 = np.array([u0])
T = 2.0
n = 10
p = euler(f3, U0 ,T,n)
print('Test EDO3\n')
print(p[0])
print('\n')
print(p[1])
print('\n')

