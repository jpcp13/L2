import numpy as np
from math import *
import matplotlib.pyplot as plt

#1.d
def is_prime(n):
	if n ==1 or n==0:
		return False
	elif n==2:
		return True
	p=2
	while p <= sqrt(n) and n%p != 0 :
		p = p+1
	if n%p==0:
		return False
	else :
		return True

#2.b
def primes(n):
	P = [k for k in range(2, n) if is_prime(k)]	
	return P
	
	
#2.c
P = primes(1000)

with open('tableau1000', 'w') as fichier :
	fichier.write('tableau des premiers inferieurs a 1000\n')
	compteur = 0
	for p in P :
		compteur +=1
		fichier.write('{0}  '.format(p))
		if compteur%10 == 0:
			fichier.write('\n')
#2.d
def pi(n):
	return np.shape(primes(n))[0]

def f(n):
	return n/(log(n))

for n in range (1, 7):
	pi(n)
plt.clf()
for i in range(2, 1000):
	plt.plot(i, pi(i), '+r',i,f(i),'+k')
plt.grid('on')
plt.axis('equal')
plt.savefig('graph2d')

#2.e
n = "n"
d = "pi(n)"
t = "n/log n"

print('{0:10}  \t {1:10} \t {2:10}'.format(n,d,t))

t="----------------------------------------------"
print(t)
for i in range(1, 7):
	p = 10**i
	V = pi(p)
	g = p/log(p)
	print('{0:10} \t {1:10} \t {2:10}'.format(p,V,g))
#exo3
def factors(n): 
	
	P = primes(n)
	F = []
	m = n
	a = int(n/2)
	i = 0

	while i < 17 :
		
		if m%P[i] == 0 :
			F.append(P[i])
			m = m/P[i]
			i = i
		else : 
			m = m
			i = i + 1

	
	return F

F = factors(60)

print(F)

#4.e
def euclide(a,b):
	d = a
	dp = b
	x = 1
	y = 0
	xp = 0
	yp = 1
	while (dp != 0):
		q = d/dp
		ds = d
		xs = x
		ys = y
		d = dp
		x = xp
		y = yp
		dp = ds - q*dp
		xp = xs - q*xp
		yp = ys - q*yp
	return d,x,y






