from methodes import * 
from pylab import * 
import numpy as np

def f(t, u):
	return -u
# a) 

def euler (f, u0, T, n): # Nous avons ecris euler dans ce fichier car l'importation ne fonctionnait pas correctement 
	h = float(T)/n
	print(h)
	tt = np.zeros(n+1)
	uu = np.zeros(n+1)
	tk = 0.0
	uk = u0
	tt[0] = tk
	uu[0] = uk
	for k in range (1, n+1):
		tk = tk + h 
		uk = uk + h*f(tk, uk) 
		tt[k] = tk	
		uu[k] = uk 
	return tt, uu 

u0 = 1.0
T = 2.0
n = 10
tt, uu = euler(f0, u0, T, n) 

clf()
plot(tt, uu, 'b')
grid()
plt.savefig('Question4a')

#show()

# b) 
#Test de la premiere fonction

u0 = 1.0
T = 2.0
n = 10
p = euler(f1, u0 ,T,n)
print('Test EDO1\n')
print(p[0])
print('\n')
print(p[1])
print('\n')

#Test de la deuxieme fonction

u0 = 1.0
T = 2.0
n = 10
p = euler(f2, u0 ,T,n)
print('Test EDO2\n')
print(p[0])
print('\n')
print(p[1])
print('\n')

#Test de la troisieme fonction

u0 = 1.0
T = 2.0
n = 10
p = euler(f3, u0 ,T,n)
print('Test EDO3\n')
print(p[0])
print('\n')
print(p[1])
print('\n')






