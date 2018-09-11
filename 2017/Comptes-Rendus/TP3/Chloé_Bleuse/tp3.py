###Exercice 1###

from scipy import *

def u(x):
	y = -exp(-x)
	return y

def f(t,u): #Q4a
	return -u

def f1(t,u): #Q4c
	return -u + t

def f2(t,u): #Q4c
	return u**2

def f3(t,u): #Q4c
	return u**2 - t

"""
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 2.0, 0.1)
y = u(x)
plt.plot(x, y)
plt.show()

###1)c)###
import matplotlib.pyplot as plt 
import numpy as np

t=np.linspace(0,2,10)
plt.plot(t,u(t),'r-')
plt.grid ('on')
plt.axis ('equal')
plt.savefig('graphU.png')
"""

###Exercice 2###
###a###
import matplotlib.pyplot as plt
import numpy as np
T=2.0
n=10
h=T/n

tt=np.zeros(n+1) 
for k in range (n+1):
	tt[k]=k*h

uu=np.zeros(n+1)
u0=1.0
uu[0]=u0
for k in range(1,n+1):
	u1=u0+h*f(tt[k-1],u0)
	uu[k]=u1
	u0=u1


plt.plot(tt,uu,'r',tt,u(tt))
plt.grid()
plt.savefig('graphtp1.png')
"""
###Exercice3###
import numpy as np
import matplotlib.pyplot as plt
def euler(f, U0, T, n):
	h=T/n
	tt=np.zeros(n+1)
	for k in range (n+1):
		tt[k]=k*h
	uu=np.zeros(n+1)
	uu[0]=u0
	for k in range (1, n+1):
		u1= u0+ h *f(tt[k-1], u0)
		uu[k]=u1
		u0=u1
	return tt, uu
	tt=np.zeros(n)

###5)c 
"""

def euler_2 (f,U0,T,n):

	U=U0
	d=U0.shape[0]
	t=0.0
	h=T/n
	tt=np.zeros(n)
	UU=np.zeros((d,n))
	for i in range (n):
		if d==1:
			UU=U
		else:
			UU[:,i]=U
		tt[i]=t
		U=U +h*f(t,U)
		t+=h

	return tt, UU

###5)b
def f5(t,U) :

	omega=1.0
	u=U[0]
	v=U[1]
	U_out=np.zeros(2)
	U_out[0]=v
	U_out[1]=-omega**2 *u

	return U_out	
"""
#plt.plot(fonction)
###Exercice4

r = euler(f, 2.0, 1.0, 10) #Q4b
print r
"""
###Exercice5
u0 = 1.0
v0 = 0.0
U0 = np.array ([u0, v0])
T = 4*math.pi
n = 1000
tt, UU = euler_2(f5, U0, T, n)
print tt
print UU

import matplotlib.pyplot as plt
plt.plot(tt, UU[0], 'r-')
plt.plot(tt, UU[1], 'b-')
plt.plot(UU[0], UU[1], 'v-')
plt.grid('on')
plt.axis('equal')
plt.savefig('graphf5.png')


