#IDOUFKER Aboubakr
#BENAMARA Taha

import numpy as np
from fonctiontp3 import *
import matplotlib.pyplot as plt
#exo 1
#c
def u(t):
	return np.exp(-t)
def f(t , u):
	return -u


t = np.linspace(0, 2.0, 100)
plt.plot(t, u(t), 'r-')
plt.grid('on')
plt.axis('equal')
plt.savefig('Graphiquedef.png')




#exo 2
#b

t0 = 0
u0 = u(t0)

T = 2.0
n = 10
h = T/n

tt = np.zeros(n)
uu = np.zeros(n)
uu[0] = u0
tt[0] = 0.0
for i in range(1, n):
	u1 = u0 - h*u0
	tt[i] = h*i
	uu[i] = u1
	u0 = u1

plt.clf()
plt.plot(tt, u(tt), '-r', tt, uu, '+k')
plt.savefig('Graphiquedeeuler.png')

#exo 4
#a voir en haut en #1

#b
e = euler(f, u0, T, n)
#c
def f1(u ,t):
	return -u + t
def f2(u ,t):
	return u**2
def f3(u, t):
	return u**2 - t

#exo 5
#b
u0 = 1.0
T = 4*np.pi
v0 = 0.0
U0 = np.array([u0,v0])
U = U0
n = 1000
def F(t, U):
	w = 1.0
	u = U[0]
	v = U[1]
	Up = np.zeros(2)
	Up[0] = v
	Up[1] = -u*w**2
	return Up

#d
tt, UU = euler2(F, U0, T, n)
#e
plt.clf()
plt.plot(tt, UU[0],'r-')
plt.grid('on')
plt.axis('equal')
plt.savefig('position.png')
plt.clf()
plt.plot(tt, UU[1],'b-')
plt.grid('on')
plt.axis('equal')
plt.savefig('vitesse.png')
plt.clf()
plt.plot(UU[0], UU[1], 'v-')
plt.grid('on')
plt.axis('equal')
plt.savefig('cercle.png')

