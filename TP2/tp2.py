def f(x):
	return 1.0 - x**2

def point_milieu(f, a, b, n):
	h = (b - a)/float(n)
	S = 0.0
	for k in range(n):
		c = a + h/2 + k*h
		S += h*f(c)
	return S

def nppm(f, a, b, n):
	h = (b - a)/float(n)
	x = np.arange(a+h/2, b, h)
	return np.sum(h*f(x))


############" start program
import time
import numpy as np

a, b = 0.0, 1.0
I = 2.0/3

"""
n = 2**20
t = time.clock()
S = point_milieu(f, a, b, n)
temps = time.clock() - t
erreur = abs(I - S)
print('S = ', S)
print('temps = ', temps)
print('erreur =', erreur)
"""

print('{0:>10} | {1:^11} | {2:^10}'.format('n', 'erreur', 'temps (sec.)'))
print('-'*40)
for k in range(1, 7):
	n = 10**k
	t = time.clock()
	S = point_milieu(f, a, b, n)
	temps = time.clock() - t
	erreur = abs(I - S)
	print('{0:>10d} | {1:>.5e} | {2:>.5e}'.format(n, erreur, temps))

"""
t = time.clock()
npS = nppm(f, a, b, n)
numpy_time = time.clock() - t
print('S = ', S)
print('numpy_time = ', numpy_time)
"""
