from math import *
from time import clock
import numpy as np
import matplotlib.pyplot as plt
from fonction import* 

w = 1.0

def u(t):
    return cos(w*t)

def F(t, U):
	w = 1.0
	u = U[0]
	v = U[1]
	Up = np.zeros(2)
	Up[0] = v
	Up[1] = -u*w**2
	return Up

	
#a)
u0 = 1.0
T = 4*np.pi
v0 = 0.0
U0 = np.array([u0,v0])
U = U0
n= 1000

#d)

u0 = 1.0
T = 4*np.pi
v0 = 0.0
U0 = np.array([u0,v0])
U = U0
n= 1000

tt, UU = euler2(F,U0, T, n)

#e)
T = 4*np.pi
u0 = 1.0
v0 = 0.0
U0 = np.array([u0,v0])
U = U0
n= 1000

tt, UU = euler2(F,U0, T, n)

position = UU[0, :]
vitesse = UU[1, :]

plt.clf()
plt.plot(tt, position, '-r')
plt.grid('on')
plt.savefig('position.png')
plt.clf()
plt.plot(tt,vitesse, '-g')
plt.grid('on')
plt.savefig('vitesse.png')
plt.clf()
plt.plot(position,vitesse, '-k')
plt.grid('on')
plt.savefig('vitpos.png')

