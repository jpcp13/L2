#Exercice 2


from tp3 import *

#a)

import numpy as np
T = 2.0
n = 10
h = T/n

tt = np.zeros(n+1)
for k in range(n+1) :
	tt[k] = k*h

uu = np.zeros(n+1)
u0 = 1.0
uu[0] = u0
for k in range(1, n+1) :
	u1 = u0 + h * f(tt[k-1], u0)
	uu[k] = u1
	u0 = u1

#b)

import matplotlib.pyplot as plt


plt.plot(tt, uu, 'r.', tt, u(tt)) 
plt.grid()
plt.savefig('graphtp1.png')

